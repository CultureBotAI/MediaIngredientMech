#!/usr/bin/env python3
"""Validate merge field integrity in ingredient data."""

import sys
from pathlib import Path

# Make the package importable when running this script directly without
# installing the wheel or exporting PYTHONPATH.
_SRC = Path(__file__).resolve().parents[1] / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from mediaingredientmech.curation.ingredient_curator import IngredientCurator


def main():
    """Validate merge integrity and display results."""
    console = Console()

    console.print("\n[bold]Validating Merge Integrity[/bold]\n")

    # Load data
    curator = IngredientCurator()
    try:
        curator.load()
    except FileNotFoundError:
        console.print("[red]✗ Data file not found[/red]")
        return 1

    total_records = len(curator.records)
    console.print(f"Loaded {total_records} ingredient records")

    # Count merge-related records
    merged_records = [r for r in curator.records if r.get("representative")]
    representative_records = [r for r in curator.records if r.get("merged")]

    console.print(f"  • {len(merged_records)} merged (REJECTED) records")
    console.print(f"  • {len(representative_records)} representative records with merged list")
    console.print()

    # Validate
    is_valid, errors = curator.validate_merge_integrity()

    if is_valid:
        console.print(Panel("[green]✓ Merge integrity PASSED[/green]", style="green"))

        # Display summary statistics
        if merged_records or representative_records:
            table = Table(title="Merge Statistics")
            table.add_column("Metric", style="cyan")
            table.add_column("Value", style="magenta")

            table.add_row("Total records", str(total_records))
            table.add_row("Representative records", str(total_records - len(merged_records)))
            table.add_row("Merged records", str(len(merged_records)))
            table.add_row("Merge clusters", str(len(representative_records)))

            if representative_records:
                avg_cluster_size = len(merged_records) / len(representative_records)
                table.add_row("Avg cluster size", f"{avg_cluster_size:.1f}")

                max_cluster_size = max(len(r.get("merged", [])) for r in representative_records)
                table.add_row("Max cluster size", str(max_cluster_size))

            console.print()
            console.print(table)

        return 0
    else:
        console.print(
            Panel(
                f"[red]✗ {len(errors)} validation error(s) found[/red]",
                style="red",
            )
        )
        console.print("\n[bold red]Validation Errors:[/bold red]\n")
        for i, error in enumerate(errors, 1):
            console.print(f"  {i}. {error}")

        return 1


if __name__ == "__main__":
    sys.exit(main())
