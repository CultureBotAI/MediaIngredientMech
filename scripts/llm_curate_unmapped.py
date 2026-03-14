#!/usr/bin/env python3
"""LLM-assisted batch curation of unmapped ingredients.

Uses Claude API to suggest ontology mappings with reasoning,
validates suggestions against actual ontologies, and presents
them for curator review and acceptance.

Requires: ANTHROPIC_API_KEY environment variable
"""

from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

import click
import yaml
from rich.console import Console
from rich.panel import Panel
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
from mediaingredientmech.utils.llm_curator import (
    LLMCurator,
    LLMSuggestion,
    validate_llm_suggestion,
)
from mediaingredientmech.utils.ontology_client import (
    OntologyCandidate,
    OntologyClient,
)

console = Console()

QUALITY_OPTIONS = {
    "1": "EXACT_MATCH",
    "2": "SYNONYM_MATCH",
    "3": "CLOSE_MATCH",
    "4": "LLM_ASSISTED",
}


def display_llm_suggestion(
    ingredient_name: str,
    suggestion: LLMSuggestion,
    validation_ok: bool,
    validation_error: str | None,
) -> None:
    """Display LLM suggestion with formatting."""
    console.print()
    console.print("[bold cyan]LLM Suggestion[/bold cyan]")

    # Validation status
    if validation_ok:
        status = "[green]✓ Validated[/green]"
    else:
        status = f"[red]✗ Validation failed: {validation_error}[/red]"

    # Build suggestion table
    table = Table(show_header=False, box=None)
    table.add_column("Field", style="bold")
    table.add_column("Value")

    table.add_row("Ontology ID", f"[green]{suggestion.ontology_id}[/green]")
    table.add_row("Label", suggestion.ontology_label)
    table.add_row("Source", suggestion.ontology_source)
    table.add_row(
        "Confidence",
        f"[yellow]{suggestion.confidence:.2f}[/yellow]",
    )
    table.add_row("Status", status)
    table.add_row("Reasoning", suggestion.reasoning)

    if suggestion.alternative_queries:
        table.add_row(
            "Alt. queries",
            ", ".join(suggestion.alternative_queries[:3]),
        )

    console.print(table)
    console.print()


def process_ingredient_with_llm(
    record: dict,
    llm_curator: LLMCurator,
    ingredient_curator: IngredientCurator,
    ontology_client: OntologyClient,
    auto_accept_threshold: float = 0.9,
    dry_run: bool = False,
) -> str:
    """Process one ingredient with LLM assistance.

    Returns:
        Action taken: 'mapped', 'skipped', 'failed', 'quit'
    """
    identifier = record.get("ontology_id", "")
    name = record.get("preferred_term", "")
    stats = record.get("occurrence_statistics", {})

    # Display ingredient
    console.print()
    console.print(
        Panel(
            f"[bold]Name:[/bold] {name}\n"
            f"[bold]ID:[/bold] {identifier}\n"
            f"[bold]Occurrences:[/bold] {stats.get('total_occurrences', 0)} "
            f"across {stats.get('media_count', 0)} media",
            title="[cyan]Unmapped Ingredient[/cyan]",
            border_style="cyan",
        )
    )

    # Normalize and categorize
    norm_result = normalize_chemical_name(name)
    category = categorize_unmapped_name(name)

    if norm_result.applied_rules:
        console.print(
            f"[dim]Normalized: {norm_result.normalized} "
            f"({', '.join(norm_result.applied_rules)})[/dim]"
        )

    console.print(f"[dim]Category: {category}[/dim]")

    # Build context for LLM
    synonyms = []
    for syn in record.get("synonyms", []) or []:
        if isinstance(syn, dict):
            synonyms.append(syn.get("synonym_text", ""))
        else:
            synonyms.append(str(syn))

    context = {
        "synonyms": synonyms[:5],
        "category": category,
        "occurrences": stats.get("total_occurrences", 0),
        "normalized": norm_result.normalized,
        "normalization_rules": norm_result.applied_rules,
    }

    # Get LLM suggestion
    console.print("[dim]Consulting LLM for mapping suggestion...[/dim]")

    try:
        suggestion = llm_curator.suggest_mapping(name, context)
    except Exception as e:
        console.print(f"[red]LLM error: {e}[/red]")
        return "failed"

    # Validate suggestion
    validation_ok, validation_error = validate_llm_suggestion(
        suggestion,
        ontology_client,
    )

    # Display suggestion
    display_llm_suggestion(name, suggestion, validation_ok, validation_error)

    if not validation_ok:
        console.print(
            "[yellow]Warning: LLM suggestion could not be validated. "
            "Manual search recommended.[/yellow]"
        )

        # Offer manual search option
        if Confirm.ask("Search ontologies manually?", default=True):
            return handle_manual_search(
                record,
                ingredient_curator,
                ontology_client,
                norm_result,
            )
        else:
            return "skipped"

    # Auto-accept high-confidence validated suggestions
    if suggestion.confidence >= auto_accept_threshold and validation_ok:
        console.print(
            f"\n[bold green]High-confidence suggestion "
            f"({suggestion.confidence:.2f} ≥ {auto_accept_threshold})[/bold green]"
        )

        if dry_run:
            console.print("[dim]Dry run: would auto-accept this mapping[/dim]")
            return "mapped"

        if Confirm.ask("Auto-accept this mapping?", default=True):
            accept_llm_mapping(
                record,
                suggestion,
                ingredient_curator,
                llm_curator.model,
                norm_result,
            )
            return "mapped"

    # Present options
    console.print("\n[bold]Actions:[/bold]")
    console.print("  [green]a[/green] - Accept LLM suggestion")
    console.print("  [yellow]s[/yellow] - Skip to next")
    console.print("  [blue]m[/blue] - Manual search")
    console.print("  [dim]q[/dim] - Quit")

    action = Prompt.ask("Action", choices=["a", "s", "m", "q"], default="s")

    if action == "a":
        if dry_run:
            console.print("[dim]Dry run: would accept mapping[/dim]")
            return "mapped"

        quality = QUALITY_OPTIONS.get(
            Prompt.ask(
                "Quality (1=EXACT, 2=SYNONYM, 3=CLOSE, 4=LLM_ASSISTED)",
                choices=list(QUALITY_OPTIONS.keys()),
                default="4",
            )
        )
        accept_llm_mapping(
            record,
            suggestion,
            ingredient_curator,
            llm_curator.model,
            norm_result,
            quality=quality,
        )
        return "mapped"

    elif action == "m":
        return handle_manual_search(
            record,
            ingredient_curator,
            ontology_client,
            norm_result,
        )

    elif action == "q":
        return "quit"

    return "skipped"


def accept_llm_mapping(
    record: dict,
    suggestion: LLMSuggestion,
    curator: IngredientCurator,
    llm_model: str,
    norm_result: dict,
    quality: str = "LLM_ASSISTED",
) -> None:
    """Accept an LLM-suggested mapping."""
    # Convert LLMSuggestion to OntologyCandidate
    candidate = OntologyCandidate(
        ontology_id=suggestion.ontology_id,
        label=suggestion.ontology_label,
        source=suggestion.ontology_source,
        score=suggestion.confidence,
        synonyms=[],
        definition=None,
    )

    # Accept mapping with LLM tracking
    curator.accept_mapping(
        record,
        candidate,
        quality=quality,
        llm_assisted=True,
        llm_model=llm_model,
        notes=f"LLM reasoning: {suggestion.reasoning}",
    )

    # Add original form as synonym if normalized
    original_name = norm_result.get("original", "")
    normalized_name = norm_result.get("normalized", "")
    applied_rules = norm_result.get("applied_rules", [])

    if applied_rules and original_name != normalized_name:
        if "synonyms" not in record or record["synonyms"] is None:
            record["synonyms"] = []

        # Determine synonym type
        if "stripped_hydrate" in applied_rules:
            synonym_type = "HYDRATE_FORM"
        elif "stripped_catalog" in applied_rules:
            synonym_type = "CATALOG_VARIANT"
        elif "fixed_incomplete_formula" in applied_rules:
            synonym_type = "INCOMPLETE_FORMULA"
        else:
            synonym_type = "ALTERNATE_FORM"

        record["synonyms"].append(
            {
                "synonym_text": original_name.strip(),
                "synonym_type": synonym_type,
                "source": "llm_curation_normalization",
                "notes": f"Original form before normalization: {', '.join(applied_rules)}",
            }
        )

    console.print(
        f"\n[bold green]✓ Mapped to {suggestion.ontology_id} "
        f"({suggestion.ontology_label})[/bold green]"
    )

    if applied_rules and original_name != normalized_name:
        console.print(
            f"[dim]Added '{original_name}' as synonym[/dim]"
        )


def handle_manual_search(
    record: dict,
    curator: IngredientCurator,
    ontology_client: OntologyClient,
    norm_result: dict,
) -> str:
    """Handle manual ontology search."""
    query = Prompt.ask(
        "Search query",
        default=norm_result.get("normalized", record.get("preferred_term", "")),
    )

    console.print(f"[dim]Searching for: {query}...[/dim]")

    try:
        candidates = ontology_client.search(query, max_results=10)
    except Exception as e:
        console.print(f"[red]Search error: {e}[/red]")
        return "failed"

    if not candidates:
        console.print("[yellow]No results found.[/yellow]")
        return "skipped"

    # Display candidates
    table = Table(title="Manual Search Results")
    table.add_column("#", style="bold", width=4)
    table.add_column("ID", style="green")
    table.add_column("Label")
    table.add_column("Source", style="blue")
    table.add_column("Score", justify="right")

    for i, c in enumerate(candidates, 1):
        table.add_row(
            str(i),
            c.ontology_id,
            c.label,
            c.source,
            f"{c.score:.2f}",
        )

    console.print(table)

    choice = Prompt.ask(
        "Select candidate # (or Enter to skip)",
        default="",
    )

    if not choice:
        return "skipped"

    try:
        idx = int(choice) - 1
        if idx < 0 or idx >= len(candidates):
            console.print("[red]Invalid choice[/red]")
            return "skipped"

        candidate = candidates[idx]
        curator.accept_mapping(
            record,
            candidate,
            quality="MANUAL_CURATION",
            llm_assisted=False,
        )

        console.print(
            f"[green]Mapped to {candidate.ontology_id} ({candidate.label})[/green]"
        )
        return "mapped"

    except ValueError:
        console.print("[red]Invalid input[/red]")
        return "skipped"


@click.command()
@click.option(
    "--data-path",
    type=click.Path(path_type=Path),
    default=Path("data/curated/unmapped_ingredients.yaml"),
    help="Path to unmapped ingredients YAML",
)
@click.option(
    "--category",
    help="Filter by category (SIMPLE_CHEMICAL, COMPLEX_MIXTURE, etc.)",
)
@click.option(
    "--auto-accept-threshold",
    type=float,
    default=0.9,
    help="Auto-accept threshold for LLM confidence (0.0-1.0)",
)
@click.option(
    "--model",
    default="claude-sonnet-4-20250514",
    help="Claude model to use",
)
@click.option(
    "--curator",
    default="llm_curator",
    help="Curator name for audit trail",
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Dry run mode (no changes saved)",
)
@click.option(
    "--limit",
    type=int,
    help="Limit number of ingredients to process",
)
def main(
    data_path: Path,
    category: str | None,
    auto_accept_threshold: float,
    model: str,
    curator: str,
    dry_run: bool,
    limit: int | None,
) -> None:
    """LLM-assisted curation of unmapped ingredients."""
    console.print(
        Panel(
            "[bold]LLM-Assisted Curation Tool[/bold]\n"
            "Uses Claude API to suggest ontology mappings with reasoning",
            border_style="blue",
        )
    )

    # Check API key
    import os

    if not os.environ.get("ANTHROPIC_API_KEY"):
        console.print(
            "[red]Error: ANTHROPIC_API_KEY environment variable not set[/red]\n"
            "Set it with: export ANTHROPIC_API_KEY=your-api-key"
        )
        sys.exit(1)

    # Initialize
    try:
        llm_curator = LLMCurator(model=model)
        ontology_client = OntologyClient(sources=["CHEBI", "FOODON", "ENVO"])
        ingredient_curator = IngredientCurator(
            data_path=data_path,
            curator_name=curator,
            ontology_client=ontology_client,
        )
    except Exception as e:
        console.print(f"[red]Initialization error: {e}[/red]")
        sys.exit(1)

    # Load data
    records = ingredient_curator.load()
    unmapped = ingredient_curator.get_unmapped()

    if not unmapped:
        console.print("[green]No unmapped ingredients found![/green]")
        return

    # Filter by category
    if category:
        unmapped = [
            r
            for r in unmapped
            if categorize_unmapped_name(r.get("preferred_term", "")) == category
        ]
        console.print(f"Filtered to {len(unmapped)} {category} ingredients\n")

    # Sort by occurrence
    unmapped.sort(
        key=lambda r: r.get("occurrence_statistics", {}).get(
            "total_occurrences", 0
        ),
        reverse=True,
    )

    # Limit
    if limit:
        unmapped = unmapped[:limit]

    console.print(f"Processing {len(unmapped)} ingredients\n")

    if dry_run:
        console.print("[yellow]DRY RUN MODE - No changes will be saved[/yellow]\n")

    # Process ingredients
    mapped_count = 0
    skipped_count = 0
    failed_count = 0

    for i, record in enumerate(unmapped, 1):
        console.print(f"\n[bold cyan]--- Ingredient {i}/{len(unmapped)} ---[/bold cyan]")

        action = process_ingredient_with_llm(
            record,
            llm_curator,
            ingredient_curator,
            ontology_client,
            auto_accept_threshold=auto_accept_threshold,
            dry_run=dry_run,
        )

        if action == "mapped":
            mapped_count += 1
            if not dry_run and ingredient_curator.is_dirty:
                ingredient_curator.save()
        elif action == "skipped":
            skipped_count += 1
        elif action == "failed":
            failed_count += 1
        elif action == "quit":
            break

    # Summary
    console.print(
        f"\n[bold]Session complete:[/bold]\n"
        f"  Mapped: {mapped_count}\n"
        f"  Skipped: {skipped_count}\n"
        f"  Failed: {failed_count}\n"
        f"  Total: {len(unmapped)}"
    )


if __name__ == "__main__":
    main()
