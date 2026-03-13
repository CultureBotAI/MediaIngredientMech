#!/usr/bin/env python3
"""Enhanced batch curation script with chemical name normalization.

Features:
- Auto-normalize chemical names before searching
- Search with multiple variants (original, normalized, expanded)
- Quick accept/reject/skip workflow
- Priority-based ordering (simple chemicals first)
- Resume capability with progress tracking
- Export curation decisions to CSV
"""

from __future__ import annotations

import csv
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

import click
import yaml
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
from rich.prompt import Confirm, Prompt
from rich.table import Table

# Add src to path
_project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_project_root / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator
from mediaingredientmech.utils.chemical_normalizer import (
    categorize_unmapped_name,
    normalize_chemical_name,
)
from mediaingredientmech.utils.ontology_client import OntologyClient

console = Console()

QUALITY_OPTIONS = {
    "1": "EXACT_MATCH",
    "2": "SYNONYM_MATCH",
    "3": "CLOSE_MATCH",
    "4": "MANUAL_CURATION",
}


class BatchCurationSession:
    """Manages a batch curation session with progress tracking."""

    def __init__(
        self,
        curator: IngredientCurator,
        ontology_client: OntologyClient,
        category_filter: Optional[str] = None,
        min_confidence: float = 0.0,
        resume_file: Optional[Path] = None,
    ):
        self.curator = curator
        self.ontology_client = ontology_client
        self.category_filter = category_filter
        self.min_confidence = min_confidence
        self.resume_file = resume_file

        self.curated_count = 0
        self.skipped_count = 0
        self.decisions: list[dict] = []
        self.processed_ids: set[str] = set()

        if resume_file and resume_file.exists():
            self._load_progress()

    def _load_progress(self) -> None:
        """Load progress from resume file."""
        with open(self.resume_file) as f:
            data = yaml.safe_load(f)
            self.processed_ids = set(data.get('processed_ids', []))
            self.decisions = data.get('decisions', [])
            console.print(f"[dim]Resuming session: {len(self.processed_ids)} already processed[/dim]")

    def save_progress(self) -> None:
        """Save current progress to resume file."""
        if self.resume_file:
            data = {
                'processed_ids': list(self.processed_ids),
                'decisions': self.decisions,
                'last_updated': datetime.now().isoformat(),
            }
            self.resume_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.resume_file, 'w') as f:
                yaml.dump(data, f, sort_keys=False)

    def export_decisions(self, output_path: Path) -> None:
        """Export curation decisions to CSV."""
        if not self.decisions:
            return

        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', newline='') as f:
            writer = csv.DictWriter(
                f,
                fieldnames=[
                    'identifier',
                    'original_name',
                    'normalized_name',
                    'search_query',
                    'decision',
                    'ontology_id',
                    'ontology_label',
                    'quality',
                    'normalization_rules',
                    'timestamp',
                ]
            )
            writer.writeheader()
            writer.writerows(self.decisions)

        console.print(f"[green]Decisions exported to: {output_path}[/green]")

    def get_candidates_for_ingredient(
        self,
        record: dict,
    ) -> tuple[list, dict]:
        """Search ontologies with normalization for an ingredient.

        Returns:
            Tuple of (candidates, normalization_result)
        """
        name = record.get('preferred_term', '')
        norm_result = normalize_chemical_name(name)

        all_candidates = []
        seen_ids = set()

        # Try each search variant
        for variant in norm_result.variants[:5]:  # Top 5 variants
            try:
                candidates = self.ontology_client.search(variant, max_results=5)
                for c in candidates:
                    if c.ontology_id not in seen_ids:
                        all_candidates.append(c)
                        seen_ids.add(c.ontology_id)
            except Exception as e:
                console.print(f"[dim red]Search error for '{variant}': {e}[/dim red]")

        # Sort by score
        all_candidates.sort(key=lambda c: c.score, reverse=True)

        return all_candidates, norm_result.__dict__

    def process_ingredient(
        self,
        record: dict,
        auto_accept: bool = False,
    ) -> str:
        """Process a single ingredient.

        Returns:
            Action taken: 'mapped', 'skipped', 'expert', 'ambiguous', 'quit'
        """
        identifier = record.get('identifier', '')
        name = record.get('preferred_term', '')
        category = categorize_unmapped_name(name)

        # Display ingredient
        stats = record.get('occurrence_statistics', {})
        console.print(
            Panel(
                f"[bold]Name:[/bold] {name}\n"
                f"[bold]Category:[/bold] {category}\n"
                f"[bold]Occurrences:[/bold] {stats.get('total_occurrences', 0)} "
                f"across {stats.get('media_count', 0)} media",
                title=f"[cyan]{identifier}[/cyan]",
                border_style="cyan",
            )
        )

        # Get candidates with normalization
        candidates, norm_result = self.get_candidates_for_ingredient(record)

        # Show normalization
        if norm_result['applied_rules']:
            console.print(
                f"[dim]Normalized: {norm_result['normalized']} "
                f"(rules: {', '.join(norm_result['applied_rules'])})[/dim]"
            )

        # Display candidates
        if not candidates:
            console.print("[yellow]No ontology candidates found.[/yellow]")
        else:
            self._display_candidates(candidates)

        # Auto-accept high-confidence exact matches
        if auto_accept and candidates and candidates[0].score >= self.min_confidence:
            top = candidates[0]
            if self._confirm_auto_accept(name, norm_result['normalized'], top):
                self._accept_mapping(record, top, norm_result, auto=True)
                return 'mapped'

        # Interactive decision
        action = self._prompt_action()

        if action == 'a':
            if candidates:
                self._handle_accept(record, candidates, norm_result)
                return 'mapped'
            else:
                console.print("[red]No candidates to accept.[/red]")
                return 'skipped'

        elif action == 's':
            self._record_decision(identifier, name, norm_result, 'skipped')
            return 'skipped'

        elif action == 'e':
            self.curator.change_status(record, 'NEEDS_EXPERT')
            self._record_decision(identifier, name, norm_result, 'needs_expert')
            console.print("[yellow]Marked as NEEDS_EXPERT[/yellow]")
            return 'expert'

        elif action == 'x':
            self.curator.change_status(record, 'AMBIGUOUS')
            self._record_decision(identifier, name, norm_result, 'ambiguous')
            console.print("[yellow]Marked as AMBIGUOUS[/yellow]")
            return 'ambiguous'

        elif action == 'r':
            query = Prompt.ask("Search query")
            try:
                candidates = self.ontology_client.search(query, max_results=10)
                self._display_candidates(candidates)
            except Exception as e:
                console.print(f"[red]Search error: {e}[/red]")
            return self.process_ingredient(record, auto_accept=False)

        elif action == 'q':
            return 'quit'

        return 'skipped'

    def _display_candidates(self, candidates: list) -> None:
        """Display ontology candidates in a table."""
        table = Table(title="Ontology Candidates", show_lines=True)
        table.add_column("#", style="bold", width=4)
        table.add_column("ID", style="green")
        table.add_column("Label", style="white")
        table.add_column("Source", style="blue")
        table.add_column("Score", style="yellow", justify="right")

        for i, c in enumerate(candidates[:10]):
            table.add_row(
                str(i + 1),
                c.ontology_id,
                c.label,
                c.source,
                f"{c.score:.2f}",
            )

        console.print(table)

    def _prompt_action(self) -> str:
        """Prompt for user action."""
        console.print("\n[bold]Actions:[/bold]")
        console.print("  [green]a[/green] - Accept mapping")
        console.print("  [yellow]s[/yellow] - Skip")
        console.print("  [red]e[/red] - Mark NEEDS_EXPERT")
        console.print("  [red]x[/red] - Mark AMBIGUOUS")
        console.print("  [blue]r[/blue] - Re-search")
        console.print("  [dim]q[/dim] - Quit")

        return Prompt.ask(
            "Action",
            choices=['a', 's', 'e', 'x', 'r', 'q'],
            default='s',
        )

    def _confirm_auto_accept(
        self,
        original: str,
        normalized: str,
        candidate,
    ) -> bool:
        """Confirm auto-accepting a high-confidence match."""
        console.print(
            f"\n[bold green]High-confidence match found:[/bold green]\n"
            f"  {original} → {normalized}\n"
            f"  → {candidate.ontology_id} ({candidate.label})\n"
            f"  Score: {candidate.score:.2f}"
        )
        return Confirm.ask("Auto-accept this mapping?", default=True)

    def _handle_accept(
        self,
        record: dict,
        candidates: list,
        norm_result: dict,
    ) -> None:
        """Handle accepting a mapping."""
        choice = Prompt.ask("Select candidate #", default="1")
        try:
            idx = int(choice) - 1
            if idx < 0 or idx >= len(candidates):
                console.print("[red]Invalid candidate number.[/red]")
                return
        except ValueError:
            console.print("[red]Invalid input.[/red]")
            return

        candidate = candidates[idx]
        quality = QUALITY_OPTIONS.get(
            Prompt.ask(
                "Quality (1=EXACT, 2=SYNONYM, 3=CLOSE, 4=MANUAL)",
                choices=list(QUALITY_OPTIONS.keys()),
                default="4",
            )
        )

        self._accept_mapping(record, candidate, norm_result, quality=quality)

    def _accept_mapping(
        self,
        record: dict,
        candidate,
        norm_result: dict,
        quality: str = 'MANUAL_CURATION',
        auto: bool = False,
    ) -> None:
        """Accept an ontology mapping."""
        original_name = norm_result.get('original', '')
        normalized_name = norm_result.get('normalized', '')
        applied_rules = norm_result.get('applied_rules', [])

        # Accept the mapping
        self.curator.accept_mapping(
            record,
            candidate,
            quality=quality,
            llm_assisted=False,
            notes=f"Batch curated with normalization: {', '.join(applied_rules)}" if applied_rules else "Batch curated",
        )

        # Add original form as synonym if normalization was applied
        if applied_rules and original_name != normalized_name:
            self._add_original_as_synonym(record, original_name, applied_rules)

        self._record_decision(
            record.get('identifier', ''),
            original_name,
            norm_result,
            'mapped',
            ontology_id=candidate.ontology_id,
            ontology_label=candidate.label,
            quality=quality,
        )

        console.print(
            f"[bold green]Mapped to {candidate.ontology_id} ({candidate.label})[/bold green]"
        )
        if applied_rules and original_name != normalized_name:
            console.print(
                f"[dim]Added '{original_name}' as synonym (normalization: {', '.join(applied_rules)})[/dim]"
            )
        self.curated_count += 1

    def _add_original_as_synonym(
        self,
        record: dict,
        original_name: str,
        applied_rules: list[str],
    ) -> None:
        """Add the original (pre-normalization) name as a synonym."""
        # Initialize synonyms list if needed
        if 'synonyms' not in record or record['synonyms'] is None:
            record['synonyms'] = []

        # Check if this synonym already exists
        existing_texts = {
            s.get('synonym_text', '').strip().lower() if isinstance(s, dict) else str(s).strip().lower()
            for s in record['synonyms']
        }

        if original_name.strip().lower() not in existing_texts:
            # Determine synonym type based on what was normalized
            if 'stripped_hydrate' in applied_rules:
                synonym_type = 'HYDRATE_FORM'
            elif 'stripped_catalog' in applied_rules:
                synonym_type = 'CATALOG_VARIANT'
            elif 'fixed_incomplete_formula' in applied_rules:
                synonym_type = 'INCOMPLETE_FORMULA'
            else:
                synonym_type = 'ALTERNATE_FORM'

            new_synonym = {
                'synonym_text': original_name.strip(),
                'synonym_type': synonym_type,
                'source': 'batch_curation_normalization',
                'notes': f"Original form before normalization: {', '.join(applied_rules)}",
            }
            record['synonyms'].append(new_synonym)

    def _record_decision(
        self,
        identifier: str,
        name: str,
        norm_result: dict,
        decision: str,
        ontology_id: str = '',
        ontology_label: str = '',
        quality: str = '',
    ) -> None:
        """Record a curation decision."""
        self.decisions.append({
            'identifier': identifier,
            'original_name': name,
            'normalized_name': norm_result.get('normalized', ''),
            'search_query': ', '.join(norm_result.get('variants', [])[:3]),
            'decision': decision,
            'ontology_id': ontology_id,
            'ontology_label': ontology_label,
            'quality': quality,
            'normalization_rules': ', '.join(norm_result.get('applied_rules', [])),
            'timestamp': datetime.now().isoformat(),
        })
        self.processed_ids.add(identifier)


@click.command()
@click.option(
    '--data-path',
    type=click.Path(path_type=Path),
    default=Path('data/curated/unmapped_ingredients.yaml'),
    help='Path to unmapped ingredients YAML',
)
@click.option(
    '--category',
    help='Filter by category (SIMPLE_CHEMICAL, COMPLEX_MIXTURE, etc.)',
)
@click.option(
    '--min-confidence',
    type=float,
    default=0.9,
    help='Minimum score for auto-accept (0.0-1.0)',
)
@click.option(
    '--auto-normalize',
    is_flag=True,
    help='Enable auto-normalization and high-confidence auto-accept',
)
@click.option(
    '--resume',
    type=click.Path(path_type=Path),
    help='Resume from progress file',
)
@click.option(
    '--export-csv',
    type=click.Path(path_type=Path),
    default=Path('notes/curation_decisions.csv'),
    help='Export decisions to CSV',
)
@click.option(
    '--curator',
    default='batch_curator',
    help='Curator name for audit trail',
)
@click.option(
    '--sources',
    default='CHEBI,FOODON',
    help='Comma-separated ontology sources',
)
def main(
    data_path: Path,
    category: Optional[str],
    min_confidence: float,
    auto_normalize: bool,
    resume: Optional[Path],
    export_csv: Path,
    curator: str,
    sources: str,
) -> None:
    """Enhanced batch curation with chemical name normalization."""
    console.print(
        Panel(
            "[bold]Batch Curation Tool[/bold]\n"
            "Systematically curate unmapped ingredients with auto-normalization",
            border_style="blue",
        )
    )

    # Initialize
    source_list = [s.strip() for s in sources.split(',')]
    ontology_client = OntologyClient(sources=source_list)
    curator_obj = IngredientCurator(
        data_path=data_path,
        curator_name=curator,
        ontology_client=ontology_client,
    )

    # Load data
    records = curator_obj.load()
    unmapped = curator_obj.get_unmapped()

    if not unmapped:
        console.print("[green]No unmapped ingredients found![/green]")
        return

    # Filter by category if specified
    if category:
        unmapped = [
            r for r in unmapped
            if categorize_unmapped_name(r.get('preferred_term', '')) == category
        ]
        console.print(f"Filtered to {len(unmapped)} {category} ingredients")

    # Sort by occurrence (prioritize frequent ingredients)
    unmapped.sort(
        key=lambda r: r.get('occurrence_statistics', {}).get('total_occurrences', 0),
        reverse=True,
    )

    # Create session
    session = BatchCurationSession(
        curator=curator_obj,
        ontology_client=ontology_client,
        category_filter=category,
        min_confidence=min_confidence,
        resume_file=resume,
    )

    # Process ingredients
    console.print(f"\nProcessing {len(unmapped)} unmapped ingredients\n")

    try:
        for i, record in enumerate(unmapped):
            identifier = record.get('identifier', '')

            # Skip if already processed
            if identifier in session.processed_ids:
                continue

            console.print(f"\n[bold cyan]--- Ingredient {i + 1}/{len(unmapped)} ---[/bold cyan]\n")

            action = session.process_ingredient(record, auto_accept=auto_normalize)

            # Save progress after each ingredient
            if curator_obj.is_dirty:
                curator_obj.save()
                session.save_progress()

            if action == 'quit':
                break

    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted by user[/yellow]")

    # Final report
    console.print(
        f"\n[bold]Session complete:[/bold]\n"
        f"  Curated: {session.curated_count}\n"
        f"  Skipped: {session.skipped_count}\n"
        f"  Total processed: {len(session.processed_ids)}"
    )

    # Export decisions
    if session.decisions:
        session.export_decisions(export_csv)

    # Save final progress
    session.save_progress()


if __name__ == '__main__':
    main()
