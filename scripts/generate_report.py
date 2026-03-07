#!/usr/bin/env python3
"""CLI to generate and display MediaIngredientMech curation reports."""

import sys
from pathlib import Path

import click

# Add project root to path for direct script execution
_project_root = Path(__file__).resolve().parents[1] / "src"
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

from mediaingredientmech.export.report_generator import (
    generate_report,
    report_to_json,
    report_to_markdown,
)


def render_terminal(report: dict) -> None:
    """Render report to terminal using rich."""
    from rich.console import Console
    from rich.table import Table

    console = Console()
    stats = report["statistics"]

    console.rule("[bold blue]MediaIngredientMech Curation Report[/bold blue]")
    console.print(f"Generated: {report['generated_at']}\n")

    if not report["data_files"]["mapped_exists"] and not report["data_files"]["unmapped_exists"]:
        console.print(
            "[yellow]No curated data files found. "
            "Run the import pipeline first to generate data/curated/ files.[/yellow]"
        )
        return

    # Overview table
    overview = Table(title="Overview", show_header=True, header_style="bold cyan")
    overview.add_column("Metric", style="bold")
    overview.add_column("Value", justify="right")
    overview.add_row("Total ingredients", str(stats["total_ingredients"]))
    overview.add_row("Mapped", f"[green]{stats['total_mapped']}[/green]")
    overview.add_row("Unmapped", f"[red]{stats['total_unmapped']}[/red]")
    overview.add_row("Mapping %", f"{stats['mapping_percentage']:.1f}%")
    overview.add_row("Mapped instances", str(stats["mapped_total_instances"]))
    console.print(overview)
    console.print()

    # Ontology distribution
    if stats["ontology_distribution"]:
        ont_table = Table(title="Ontology Distribution", show_header=True, header_style="bold cyan")
        ont_table.add_column("Ontology", style="bold")
        ont_table.add_column("Count", justify="right")
        for ont, count in stats["ontology_distribution"].items():
            ont_table.add_row(ont, str(count))
        console.print(ont_table)
        console.print()

    # Quality distribution
    if stats["quality_distribution"]:
        qual_table = Table(title="Mapping Quality", show_header=True, header_style="bold cyan")
        qual_table.add_column("Quality", style="bold")
        qual_table.add_column("Count", justify="right")
        for qual, count in stats["quality_distribution"].items():
            qual_table.add_row(qual, str(count))
        console.print(qual_table)
        console.print()

    # Unmapped status
    if stats["unmapped_status_distribution"]:
        status_table = Table(title="Unmapped Status", show_header=True, header_style="bold cyan")
        status_table.add_column("Status", style="bold")
        status_table.add_column("Count", justify="right")
        for status, count in stats["unmapped_status_distribution"].items():
            status_table.add_row(status, str(count))
        console.print(status_table)
        console.print()

    # Curator progress
    if report["curator_progress"]:
        cur_table = Table(title="Curator Progress", show_header=True, header_style="bold cyan")
        cur_table.add_column("Curator", style="bold")
        cur_table.add_column("Actions", justify="right")
        for curator, count in report["curator_progress"].items():
            cur_table.add_row(curator, str(count))
        console.print(cur_table)
        console.print()

    # Recent curation activity
    if report["curation_history"]:
        hist_table = Table(title="Recent Curation Activity", show_header=True, header_style="bold cyan")
        hist_table.add_column("Timestamp")
        hist_table.add_column("Curator")
        hist_table.add_column("Action")
        hist_table.add_column("Ingredient")
        for event in report["curation_history"]:
            hist_table.add_row(
                str(event.get("timestamp", "N/A")),
                event.get("curator", "N/A"),
                event.get("action", "N/A"),
                event.get("ingredient", "N/A"),
            )
        console.print(hist_table)
        console.print()

    console.rule("[bold blue]End of Report[/bold blue]")


@click.command()
@click.option(
    "--data-dir",
    type=click.Path(exists=True, path_type=Path),
    default=None,
    help="Path to curated data directory (default: data/curated/)",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(["terminal", "markdown", "json"]),
    default="terminal",
    help="Output format (default: terminal)",
)
@click.option(
    "--output",
    "-o",
    type=click.Path(path_type=Path),
    default=None,
    help="Write output to file instead of stdout",
)
def main(data_dir: Path | None, output_format: str, output: Path | None) -> None:
    """Generate a curation report for MediaIngredientMech."""
    report = generate_report(data_dir)

    if output_format == "terminal":
        render_terminal(report)
        return

    if output_format == "markdown":
        content = report_to_markdown(report)
    else:
        content = report_to_json(report)

    if output:
        output.write_text(content)
        click.echo(f"Report written to {output}")
    else:
        click.echo(content)


if __name__ == "__main__":
    main()
