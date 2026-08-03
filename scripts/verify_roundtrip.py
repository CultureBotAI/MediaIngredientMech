#!/usr/bin/env python3
"""Verify round-trip integrity between collection and individual file formats.

This script compares the original collection files with aggregated collections
(after export → individual files → aggregate) to ensure data integrity.

--aggregated-dir is REQUIRED. It used to default to data/collections/, a
COMMITTED artifact last regenerated 2026-03-06, so this check kept passing for
months while 55 curation events sat unreconciled (#148). Comparing against any
committed copy is the trap — aggregate into a temp dir first.

Usage:
    just qc-roundtrip          # does the aggregate-into-a-temp-dir dance for you

    python scripts/aggregate_records.py --ingredients-dir data/ingredients \
        --output-dir "$tmp"
    python scripts/verify_roundtrip.py --original-dir data/curated \
        --aggregated-dir "$tmp"
"""

from __future__ import annotations

import sys
from collections import Counter
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

# Fields authored directly on the per-record files and deliberately absent from
# the curated collection (culturebotai-claw's kgscan writes `discussions`; the
# exporter re-attaches them).
#
# IMPORTED, not re-declared. Drift between the two lists is silent in the unsafe
# direction: a field added here but not to the exporter's list would be wiped on
# every export while this gate stayed green — precisely the data loss the gate
# exists to catch.
def _load_exporter_authored_fields() -> tuple[str, ...]:
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "_mim_export_individual_records", Path(__file__).with_name("export_individual_records.py")
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return tuple(mod.PER_RECORD_AUTHORED_FIELDS)


PER_RECORD_ONLY_FIELDS: tuple[str, ...] = _load_exporter_authored_fields()


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


def verify_round_trip(
    original_dir: Path,
    aggregated_dir: Path,
    ignore_fields: set[str] | None = None,
) -> dict:
    """Verify round-trip integrity between original and aggregated collections.

    Args:
        original_dir: Directory with original collection files.
        aggregated_dir: Directory with aggregated collection files.
        ignore_fields: Record fields excluded from the comparison. Defaults to
            the per-record-authored fields that the collection deliberately does
            not carry (see PER_RECORD_AUTHORED_FIELDS in
            scripts/export_individual_records.py) — comparing them would report
            a permanent, expected difference and make the gate useless.

    Returns:
        Dictionary with verification results.
    """
    if ignore_fields is None:
        ignore_fields = set(PER_RECORD_ONLY_FIELDS)
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
        def _pair_key(record: dict) -> tuple[str, str]:
            return (record.get('identifier', ''), record.get('preferred_term', ''))

        orig_sorted = sorted(orig_ingredients, key=_pair_key)
        agg_sorted = sorted(agg_ingredients, key=_pair_key)

        # The two sides arrive in genuinely different orders — data/curated/ is in
        # historical order, a fresh aggregation is in filename order — so records
        # are paired by sorting both and zipping. That is only sound while the
        # sort key is UNIQUE. If two records ever share both identifier and
        # preferred_term, Python's stable sort falls back to each side's input
        # order, which differs, so the zip would pair record A with record B:
        # either a phantom diff or, worse, a real diff masked by two records that
        # happen to match. Masking is precisely what this gate exists to prevent,
        # so refuse to compare rather than report a result we cannot trust.
        # (Today: 0 duplicate pairs, though 61 identifiers are duplicated.)
        duplicate_keys = sorted(
            {k for k, n in Counter(map(_pair_key, orig_sorted)).items() if n > 1}
            | {k for k, n in Counter(map(_pair_key, agg_sorted)).items() if n > 1}
        )
        if duplicate_keys:
            results['errors'].append(
                f"{category_file}: {len(duplicate_keys)} duplicate (identifier, preferred_term) "
                f"key(s) — records cannot be paired reliably, comparison skipped: "
                + ", ".join(f"{i}/{t!r}" for i, t in duplicate_keys[:3])
            )
            results['data_diffs'] += 1
            continue

        data_identical = True
        for i, (orig_ing, agg_ing) in enumerate(zip(orig_sorted, agg_sorted)):
            diffs = compare_ingredient_records(orig_ing, agg_ing, ignore_fields)
            if diffs:
                data_identical = False
                results['errors'].append(
                    f"{category_file}, ingredient {i} ({orig_ing.get('identifier')}): "
                    f"{', '.join(diffs[:3])}"  # Show first 3 diffs
                )
                # Report several per file, not just the first: as a gate, a
                # one-at-a-time drip turns a single fix into many CI rounds.
                if len(results['errors']) >= 25:
                    break

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
    required=True,
    help=(
        "Directory with freshly aggregated collection files. REQUIRED — there is "
        "deliberately no default. It used to default to data/collections/, a COMMITTED "
        "artifact last regenerated 2026-03-06, so this check kept passing for months "
        "while 55 curation events sat unreconciled (#148). Comparing against any "
        "committed copy is the trap; aggregate into a temp dir first "
        "(`just qc-roundtrip` does)."
    ),
)
@click.option(
    "--ignore-fields",
    default=",".join(PER_RECORD_ONLY_FIELDS),
    help=(
        "Comma-separated record fields to exclude from comparison "
        f"(default: {','.join(PER_RECORD_ONLY_FIELDS)}). Pass an empty string to compare everything."
    ),
)
def main(original_dir: str | None, aggregated_dir: str | None, ignore_fields: str):
    """Verify round-trip integrity between original and aggregated collections."""
    # Set default paths
    if original_dir is None:
        original_dir_path = _project_root / "data" / "curated"
    else:
        original_dir_path = Path(original_dir)

    aggregated_dir_path = Path(aggregated_dir)

    console.print("\n[bold]Round-Trip Integrity Verification[/bold]")
    console.print(f"Original:   {original_dir_path}")
    console.print(f"Aggregated: {aggregated_dir_path}\n")

    ignored = {f.strip() for f in ignore_fields.split(",") if f.strip()}
    if ignored:
        console.print(f"[dim]Ignoring per-record-only field(s): {', '.join(sorted(ignored))}[/dim]")

    results = verify_round_trip(original_dir_path, aggregated_dir_path, ignored)

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
