#!/usr/bin/env python3
"""Interactive CLI for curating unmapped media ingredients.

Uses the rich library for terminal UI with progress bars, tables, and colored output.
Loads unmapped ingredients from data/curated/unmapped_ingredients.yaml, presents
ontology search candidates, and records curation decisions with full audit trails.
"""

from __future__ import annotations

import sys
from pathlib import Path

import click
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, Prompt
from rich.table import Table

# Add src to path so we can import the package
_project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_project_root / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator
from mediaingredientmech.curation.synonym_manager import SynonymManager
from mediaingredientmech.utils.ontology_client import OntologyClient

console = Console()

QUALITY_OPTIONS = {
    "1": "EXACT_MATCH",
    "2": "SYNONYM_MATCH",
    "3": "CLOSE_MATCH",
    "4": "MANUAL_CURATION",
    "5": "LLM_ASSISTED",
    "6": "PROVISIONAL",
}


def display_ingredient(record: dict, index: int, total: int) -> None:
    """Display an ingredient record with stats."""
    stats = record.get("occurrence_statistics") or {}
    total_occ = stats.get("total_occurrences", 0)
    media_count = stats.get("media_count", 0)
    samples = stats.get("sample_media", []) or []

    synonyms = record.get("synonyms") or []
    syn_texts = [
        s.get("synonym_text", "") if isinstance(s, dict) else str(s)
        for s in synonyms
    ]

    panel_text = (
        f"[bold]Preferred term:[/bold] {record.get('preferred_term', 'N/A')}\n"
        f"[bold]Status:[/bold] {record.get('mapping_status', 'UNMAPPED')}\n"
        f"[bold]Occurrences:[/bold] {total_occ} across {media_count} media\n"
    )
    if syn_texts:
        panel_text += f"[bold]Synonyms:[/bold] {', '.join(syn_texts[:5])}\n"
    if samples:
        panel_text += f"[bold]Sample media:[/bold] {', '.join(samples[:3])}\n"
    if record.get("notes"):
        panel_text += f"[bold]Notes:[/bold] {record['notes']}\n"

    console.print(
        Panel(
            panel_text.strip(),
            title=f"[bold cyan]Ingredient {index + 1}/{total}[/bold cyan]",
            border_style="cyan",
        )
    )


def display_candidates(candidates: list) -> None:
    """Display ontology search candidates in a table."""
    if not candidates:
        console.print("[yellow]No ontology candidates found.[/yellow]")
        return

    table = Table(title="Ontology Candidates", show_lines=True)
    table.add_column("#", style="bold", width=4)
    table.add_column("ID", style="green")
    table.add_column("Label", style="white")
    table.add_column("Source", style="blue")
    table.add_column("Score", style="yellow", justify="right")
    table.add_column("Definition", style="dim", max_width=40)

    for i, c in enumerate(candidates[:15]):
        defn = (c.definition or "")[:40]
        if c.definition and len(c.definition) > 40:
            defn += "..."
        table.add_row(
            str(i + 1),
            c.ontology_id,
            c.label,
            c.source,
            f"{c.score:.2f}",
            defn,
        )

    console.print(table)


def display_quality_options() -> None:
    """Show mapping quality choices."""
    table = Table(title="Mapping Quality", show_header=False)
    table.add_column("Key", style="bold")
    table.add_column("Quality")
    for key, val in QUALITY_OPTIONS.items():
        table.add_row(key, val)
    console.print(table)


def display_progress_report(report: dict) -> None:
    """Display a curation progress summary."""
    console.print()
    table = Table(title="Curation Progress Report", show_lines=True)
    table.add_column("Metric", style="bold")
    table.add_column("Value", justify="right")

    table.add_row("Total records", str(report["total_records"]))
    table.add_row("Mapped", f"{report['status_breakdown'].get('MAPPED', 0)}")
    table.add_row("Mapped %", f"{report['mapped_percentage']:.1f}%")
    table.add_row("Remaining unmapped", str(report["remaining_unmapped"]))
    table.add_row("Needs expert", str(report["needs_expert"]))
    table.add_row("Ambiguous", str(report["ambiguous"]))
    table.add_row("Pending review", str(report["pending_review"]))

    # Status breakdown
    for status, count in report["status_breakdown"].items():
        if status not in ("MAPPED", "UNMAPPED", "NEEDS_EXPERT", "AMBIGUOUS", "PENDING_REVIEW"):
            table.add_row(status, str(count))

    console.print(table)


def prompt_action() -> str:
    """Prompt the user for an action on the current ingredient."""
    console.print()
    console.print("[bold]Actions:[/bold]")
    console.print("  [green]a[/green] - Accept a mapping")
    console.print("  [yellow]s[/yellow] - Skip (move to next)")
    console.print("  [red]e[/red] - Mark as NEEDS_EXPERT")
    console.print("  [red]x[/red] - Mark as AMBIGUOUS")
    console.print("  [blue]y[/blue] - Add synonym")
    console.print("  [blue]n[/blue] - Add note")
    console.print("  [magenta]r[/magenta] - Re-search with different query")
    console.print("  [dim]p[/dim] - Show progress report")
    console.print("  [dim]q[/dim] - Save and quit")
    console.print()

    choice = Prompt.ask(
        "Choose action",
        choices=["a", "s", "e", "x", "y", "n", "r", "p", "q"],
        default="s",
    )
    return choice


def handle_accept(curator: IngredientCurator, record: dict, candidates: list) -> None:
    """Handle accepting an ontology mapping."""
    if not candidates:
        console.print("[red]No candidates to accept. Search first.[/red]")
        return

    choice = Prompt.ask(
        "Select candidate number",
        default="1",
    )
    try:
        idx = int(choice) - 1
        if idx < 0 or idx >= len(candidates):
            console.print("[red]Invalid candidate number.[/red]")
            return
    except ValueError:
        console.print("[red]Invalid input.[/red]")
        return

    candidate = candidates[idx]
    console.print(f"Selected: [green]{candidate.ontology_id}[/green] - {candidate.label}")

    # Quality rating
    display_quality_options()
    q_choice = Prompt.ask("Quality rating", choices=list(QUALITY_OPTIONS.keys()), default="4")
    quality = QUALITY_OPTIONS[q_choice]

    llm_assisted = Confirm.ask("Was LLM assistance used?", default=False)
    llm_model = None
    if llm_assisted:
        llm_model = Prompt.ask("LLM model identifier", default="unknown")

    notes = Prompt.ask("Notes (optional, press Enter to skip)", default="")

    curator.accept_mapping(
        record,
        candidate,
        quality=quality,
        llm_assisted=llm_assisted,
        llm_model=llm_model,
        notes=notes or None,
    )
    console.print(f"[bold green]Mapped to {candidate.ontology_id} ({candidate.label})[/bold green]")


def handle_add_synonym(
    record: dict, syn_manager: SynonymManager, records: list[dict]
) -> None:
    """Handle adding a synonym to the current record."""
    text = Prompt.ask("Synonym text")
    if not text.strip():
        return

    rec_idx = records.index(record)
    syn_manager.add_synonym(rec_idx, text.strip(), source="curator")
    console.print(f"[green]Added synonym: {text.strip()}[/green]")


@click.command()
@click.option(
    "--data-path",
    type=click.Path(),
    default="data/curated/unmapped_ingredients.yaml",
    help="Path to unmapped ingredients YAML file.",
)
@click.option(
    "--curator",
    default="anonymous",
    help="Curator name for audit trail.",
)
@click.option(
    "--sources",
    default="CHEBI,FOODON",
    help="Comma-separated ontology sources to search.",
)
def main(data_path: str, curator: str, sources: str) -> None:
    """Interactive curation of unmapped media ingredients."""
    console.print(
        Panel(
            "[bold]MediaIngredientMech - Interactive Curation Tool[/bold]\n"
            "Curate unmapped media ingredients with ontology mappings.",
            border_style="blue",
        )
    )

    source_list = [s.strip() for s in sources.split(",")]
    ontology_client = OntologyClient(sources=source_list)
    curator_obj = IngredientCurator(
        data_path=Path(data_path),
        curator_name=curator,
        ontology_client=ontology_client,
    )

    # Load data
    records = curator_obj.load()
    if not records:
        console.print("[yellow]No ingredient records found. Nothing to curate.[/yellow]")
        return

    syn_manager = SynonymManager(records)

    # Get unmapped records sorted by occurrence
    unmapped = curator_obj.get_unmapped()
    total_unmapped = len(unmapped)

    if total_unmapped == 0:
        console.print("[green]All ingredients are already mapped![/green]")
        display_progress_report(curator_obj.get_progress_report())
        return

    console.print(f"Found [bold]{total_unmapped}[/bold] unmapped ingredients to curate.")
    console.print()

    curated_count = 0

    for i, record in enumerate(unmapped):
        display_ingredient(record, i, total_unmapped)

        # Auto-search ontologies
        query = record.get("preferred_term", "")
        candidates = []
        if query:
            console.print(f"Searching ontologies for: [bold]{query}[/bold]...")
            try:
                candidates = curator_obj.search_ontologies(query, sources=source_list)
            except Exception as e:
                console.print(f"[red]Search error: {e}[/red]")
            display_candidates(candidates)

        while True:
            action = prompt_action()

            if action == "a":
                handle_accept(curator_obj, record, candidates)
                curated_count += 1
                break

            elif action == "s":
                console.print("[dim]Skipped.[/dim]")
                break

            elif action == "e":
                curator_obj.change_status(record, "NEEDS_EXPERT", notes="Marked during curation session")
                console.print("[yellow]Marked as NEEDS_EXPERT.[/yellow]")
                curated_count += 1
                break

            elif action == "x":
                curator_obj.change_status(record, "AMBIGUOUS", notes="Marked during curation session")
                console.print("[yellow]Marked as AMBIGUOUS.[/yellow]")
                curated_count += 1
                break

            elif action == "y":
                handle_add_synonym(record, syn_manager, records)
                # Stay on same ingredient

            elif action == "n":
                note = Prompt.ask("Note text")
                if note.strip():
                    curator_obj.add_note(record, note.strip())
                    console.print("[green]Note added.[/green]")
                # Stay on same ingredient

            elif action == "r":
                new_query = Prompt.ask("Search query", default=query)
                console.print(f"Searching for: [bold]{new_query}[/bold]...")
                try:
                    candidates = curator_obj.search_ontologies(new_query, sources=source_list)
                except Exception as e:
                    console.print(f"[red]Search error: {e}[/red]")
                display_candidates(candidates)
                # Stay on same ingredient

            elif action == "p":
                display_progress_report(curator_obj.get_progress_report())
                # Stay on same ingredient

            elif action == "q":
                break

        # Save after each ingredient
        if curator_obj.is_dirty:
            curator_obj.save()
            console.print("[dim]Progress saved.[/dim]")

        if action == "q":
            break

    # Final report
    console.print()
    console.print(f"[bold]Session complete. Curated {curated_count} ingredients.[/bold]")
    display_progress_report(curator_obj.get_progress_report())

    # Check for duplicates
    dupes = syn_manager.find_duplicates()
    if dupes:
        console.print(f"\n[yellow]Warning: {len(dupes)} potential duplicate groups detected.[/yellow]")
        for group in dupes[:5]:
            names = [records[i].get("preferred_term", "?") for i in group]
            console.print(f"  - {', '.join(names)}")


if __name__ == "__main__":
    main()
