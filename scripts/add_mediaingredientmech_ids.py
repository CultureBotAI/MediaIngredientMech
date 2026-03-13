#!/usr/bin/env python3
"""Add MediaIngredientMech IDs to all ingredient records.

Assigns stable, unique identifiers in the format MediaIngredientMech:000001
to each ingredient record. These IDs are independent of mapping status and
provide persistent references for KG-Hub integration.

Usage:
    python scripts/add_mediaingredientmech_ids.py --dry-run
    python scripts/add_mediaingredientmech_ids.py
"""

import argparse
import logging
import sys
from pathlib import Path
from typing import Any

import yaml
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

console = Console()


def generate_mediaingredientmech_id(index: int, prefix: str = "MediaIngredientMech") -> str:
    """Generate MediaIngredientMech ID with zero-padded index.

    Args:
        index: Sequential index (1-based).
        prefix: ID prefix (default: MediaIngredientMech).

    Returns:
        Formatted ID like "MediaIngredientMech:000001"
    """
    return f"{prefix}:{index:06d}"


def add_ids_to_records(
    records: list[dict[str, Any]],
    start_index: int = 1,
    id_field: str = "id",
    force_overwrite: bool = False
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Add MediaIngredientMech IDs to records.

    Args:
        records: List of ingredient records.
        start_index: Starting index for ID generation (default: 1).
        id_field: Field name for the ID (default: "id").
        force_overwrite: Overwrite existing IDs (default: False).

    Returns:
        Tuple of (updated_records, stats_dict).
    """
    stats = {
        "total_records": len(records),
        "ids_added": 0,
        "ids_skipped": 0,
        "ids_overwritten": 0,
    }

    current_index = start_index

    for record in records:
        # Check if ID already exists
        if id_field in record and record[id_field]:
            if force_overwrite:
                old_id = record[id_field]
                new_id = generate_mediaingredientmech_id(current_index)
                record[id_field] = new_id
                stats["ids_overwritten"] += 1
                logger.debug(f"Overwritten: {old_id} → {new_id}")
            else:
                stats["ids_skipped"] += 1
                logger.debug(f"Skipped (already has ID): {record[id_field]}")
                current_index += 1
                continue
        else:
            # Add new ID
            new_id = generate_mediaingredientmech_id(current_index)
            record[id_field] = new_id
            stats["ids_added"] += 1
            logger.debug(f"Added ID: {new_id} to {record.get('preferred_term', 'UNKNOWN')}")

        current_index += 1

    return records, stats


def display_stats(stats: dict[str, Any], dry_run: bool = True) -> None:
    """Display statistics in a formatted panel."""
    mode_str = "DRY RUN" if dry_run else "EXECUTED"

    console.print(
        Panel(
            f"[bold]MediaIngredientMech ID Assignment ({mode_str})[/bold]\n"
            f"Total records: {stats['total_records']}\n"
            f"IDs added: {stats['ids_added']}\n"
            f"IDs skipped (already exist): {stats['ids_skipped']}\n"
            f"IDs overwritten: {stats['ids_overwritten']}",
            title="Results",
            border_style="green" if stats['ids_added'] > 0 else "yellow",
        )
    )


def display_sample_records(records: list[dict[str, Any]], limit: int = 10) -> None:
    """Display sample records with their new IDs."""
    table = Table(title=f"Sample Records (showing {min(limit, len(records))})", show_header=True, header_style="bold cyan")
    table.add_column("MediaIngredientMech ID", style="cyan")
    table.add_column("Preferred Term", style="green")
    table.add_column("Mapping Status", style="yellow")
    table.add_column("Ontology ID", style="magenta")

    for record in records[:limit]:
        mid_id = record.get("id", "N/A")
        preferred_term = record.get("preferred_term", "UNKNOWN")
        mapping_status = record.get("mapping_status", "UNKNOWN")
        ontology_id = record.get("ontology_mapping", {}).get("ontology_id",
                                 record.get("identifier", "N/A"))

        # Truncate long names
        if len(preferred_term) > 40:
            preferred_term = preferred_term[:37] + "..."

        table.add_row(mid_id, preferred_term, mapping_status, ontology_id)

    console.print(table)


def load_yaml_file(file_path: Path) -> dict[str, Any]:
    """Load YAML file."""
    with open(file_path) as f:
        return yaml.safe_load(f) or {}


def save_yaml_file(file_path: Path, data: dict[str, Any]) -> None:
    """Save YAML file with proper formatting."""
    with open(file_path, "w") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Add MediaIngredientMech IDs to ingredient records"
    )
    parser.add_argument(
        "--data-path",
        type=Path,
        default=Path("data/curated/unmapped_ingredients.yaml"),
        help="Path to ingredient data file",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without saving",
    )
    parser.add_argument(
        "--start-index",
        type=int,
        default=1,
        help="Starting index for ID generation (default: 1)",
    )
    parser.add_argument(
        "--id-field",
        type=str,
        default="id",
        help="Field name for MediaIngredientMech ID (default: 'id')",
    )
    parser.add_argument(
        "--force-overwrite",
        action="store_true",
        help="Overwrite existing IDs (use with caution)",
    )
    parser.add_argument(
        "--show-samples",
        type=int,
        default=10,
        help="Number of sample records to display (default: 10)",
    )

    args = parser.parse_args()

    # Load data
    console.print(f"[bold]Loading ingredients from {args.data_path}[/bold]")

    if not args.data_path.exists():
        console.print(f"[red]Error: File not found: {args.data_path}[/red]")
        sys.exit(1)

    data = load_yaml_file(args.data_path)
    records = data.get("ingredients", [])

    if not records:
        console.print("[yellow]No ingredient records found[/yellow]")
        sys.exit(0)

    console.print(f"Loaded {len(records)} ingredient records\n")

    # Add IDs
    updated_records, stats = add_ids_to_records(
        records,
        start_index=args.start_index,
        id_field=args.id_field,
        force_overwrite=args.force_overwrite,
    )

    # Display results
    display_stats(stats, dry_run=args.dry_run)

    if args.show_samples > 0:
        console.print()
        display_sample_records(updated_records, limit=args.show_samples)

    # Save if not dry run
    if not args.dry_run:
        console.print(f"\n[bold green]Saving changes to {args.data_path}[/bold green]")
        data["ingredients"] = updated_records
        save_yaml_file(args.data_path, data)
        console.print("[green]✓ Saved successfully[/green]")
    else:
        console.print("\n[yellow]DRY RUN: No changes saved[/yellow]")
        console.print(f"[dim]Run without --dry-run to apply changes[/dim]")


if __name__ == "__main__":
    main()
