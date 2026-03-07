#!/usr/bin/env python3
"""Verify round-trip integrity between collection and individual file formats.

This script compares the original collection files with aggregated collections
(after export → individual files → aggregate) to ensure data integrity.

Usage:
    python scripts/verify_roundtrip.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table

# Ensure the src package is importable when running the script directly
_project_root = Path(__file__).resolve().parents[1]
_src = _project_root / "src"
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from mediaingredientmech.utils.yaml_handler import load_yaml

console = Console()


def compare_ingredient_records(orig: dict, agg: dict, ignore_fields: set[str] = None) -> list[str]:
    """Compare two ingredient records and return differences.

    Args:
        orig: Original ingredient record.
        agg: Aggregated ingredient record.
        ignore_fields: Fields to ignore in comparison.

    Returns:
        List of difference messages (empty if identical).
    """
    if ignore_fields is None:
        ignore_fields = set()

    diffs = []

    # Check all keys in original
    for key in orig:
        if key in ignore_fields:
            continue
        if key not in agg:
            diffs.append(f"Missing key: {key}")
        elif orig[key] != agg[key]:
            diffs.append(f"Value differs for {key}: {orig[key]} != {agg[key]}")

    # Check for extra keys in aggregated
    for key in agg:
        if key in ignore_fields:
            continue
        if key not in orig:
            diffs.append(f"Extra key: {key}")

    return diffs


def verify_round_trip(original_dir: Path, aggregated_dir: Path) -> dict:
    """Verify round-trip integrity between original and aggregated collections.

    Args:
        original_dir: Directory with original collection files.
        aggregated_dir: Directory with aggregated collection files.

    Returns:
        Dictionary with verification results.
    """
    results = {
        'files_compared': 0,
        'identical': 0,
        'metadata_only_diff': 0,
        'data_diffs': 0,
        'errors': []
    }

    categories = ['mapped_ingredients.yaml', 'unmapped_ingredients.yaml']

    for category_file in categories:
        orig_file = original_dir / category_file
        agg_file = aggregated_dir / category_file

        if not orig_file.exists():
            results['errors'].append(f"Original file not found: {orig_file}")
            continue

        if not agg_file.exists():
            results['errors'].append(f"Aggregated file not found: {agg_file}")
            continue

        results['files_compared'] += 1

        # Load files
        orig_data = load_yaml(orig_file)
        agg_data = load_yaml(agg_file)

        # Check metadata (expected to differ)
        metadata_diff = orig_data.get('generation_date') != agg_data.get('generation_date')

        # Check counts match
        if orig_data.get('total_count') != agg_data.get('total_count'):
            results['errors'].append(
                f"{category_file}: total_count mismatch "
                f"({orig_data.get('total_count')} vs {agg_data.get('total_count')})"
            )

        # Compare ingredient records
        orig_ingredients = orig_data.get('ingredients', [])
        agg_ingredients = agg_data.get('ingredients', [])

        if len(orig_ingredients) != len(agg_ingredients):
            results['errors'].append(
                f"{category_file}: ingredient count mismatch "
                f"({len(orig_ingredients)} vs {len(agg_ingredients)})"
            )
            continue

        # Sort by identifier AND preferred_term to handle duplicate identifiers
        orig_sorted = sorted(
            orig_ingredients,
            key=lambda x: (x.get('identifier', ''), x.get('preferred_term', ''))
        )
        agg_sorted = sorted(
            agg_ingredients,
            key=lambda x: (x.get('identifier', ''), x.get('preferred_term', ''))
        )

        data_identical = True
        for i, (orig_ing, agg_ing) in enumerate(zip(orig_sorted, agg_sorted)):
            diffs = compare_ingredient_records(orig_ing, agg_ing)
            if diffs:
                data_identical = False
                results['errors'].append(
                    f"{category_file}, ingredient {i} ({orig_ing.get('identifier')}): "
                    f"{', '.join(diffs[:3])}"  # Show first 3 diffs
                )
                break  # Only report first mismatch per file

        if data_identical and metadata_diff:
            results['metadata_only_diff'] += 1
        elif data_identical:
            results['identical'] += 1
        else:
            results['data_diffs'] += 1

    return results


@click.command()
@click.option(
    "--original-dir",
    type=click.Path(exists=False),
    default=None,
    help="Directory with original collection files (default: data/curated/)",
)
@click.option(
    "--aggregated-dir",
    type=click.Path(exists=False),
    default=None,
    help="Directory with aggregated collection files (default: data/collections/)",
)
def main(original_dir: str | None, aggregated_dir: str | None):
    """Verify round-trip integrity between original and aggregated collections."""
    # Set default paths
    if original_dir is None:
        original_dir_path = _project_root / "data" / "curated"
    else:
        original_dir_path = Path(original_dir)

    if aggregated_dir is None:
        aggregated_dir_path = _project_root / "data" / "collections"
    else:
        aggregated_dir_path = Path(aggregated_dir)

    console.print("\n[bold]Round-Trip Integrity Verification[/bold]")
    console.print(f"Original:   {original_dir_path}")
    console.print(f"Aggregated: {aggregated_dir_path}\n")

    results = verify_round_trip(original_dir_path, aggregated_dir_path)

    # Summary table
    table = Table(title="Verification Results")
    table.add_column("Metric", style="cyan")
    table.add_column("Count", justify="right")

    table.add_row("Files compared", str(results['files_compared']))
    table.add_row("Identical (including metadata)", str(results['identical']))
    table.add_row("Metadata-only differences", str(results['metadata_only_diff']))
    table.add_row("Data differences", str(results['data_diffs']))
    table.add_row("Errors", str(len(results['errors'])))

    console.print(table)

    # Show errors if any
    if results['errors']:
        console.print("\n[bold red]Errors/Differences:[/bold red]")
        for error in results['errors'][:10]:  # Show first 10
            console.print(f"  [red]✗[/red] {error}")
        if len(results['errors']) > 10:
            console.print(f"  [dim]... and {len(results['errors']) - 10} more errors[/dim]")

    # Verdict
    console.print()
    if results['data_diffs'] == 0 and len(results['errors']) == 0:
        console.print("[bold green]✓ Round-trip integrity verified![/bold green]")
        console.print("[dim]Note: generation_date metadata is expected to differ[/dim]")
        sys.exit(0)
    else:
        console.print("[bold red]✗ Round-trip integrity check failed[/bold red]")
        sys.exit(1)


if __name__ == "__main__":
    main()
