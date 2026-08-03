#!/usr/bin/env python3
"""Aggregate individual ingredient YAML files into collection format.

This script performs the reverse operation of export_individual_records.py,
combining individual ingredient YAML files back into collection format for
reporting and backward compatibility.

--output-dir is REQUIRED. It used to default to data/collections/, which nothing
in the repo reads, so a bare invocation looked successful while changing nothing
that mattered (#169).

Usage:
    # Write the per-record tree back into the LIVE collection (`just sync-curated`).
    python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir data/curated

    # Verify a round trip without touching the tree (`just qc-roundtrip`).
    python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir "$(mktemp -d)"
"""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

import click
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

# Ensure the src package is importable when running the script directly
_project_root = Path(__file__).resolve().parents[1]
_src = _project_root / "src"
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from mediaingredientmech.utils.yaml_handler import load_yaml, save_yaml

console = Console()


def _exporter_authored_fields() -> tuple[str, ...]:
    """Fields authored only on per-record files, which the collection never carries.

    Imported from the exporter rather than re-declared: if the two lists drift,
    aggregating would inject a field the collection format does not have, and the
    next export would either wipe it or fight over it.
    """
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "_mim_export_individual_records", Path(__file__).with_name("export_individual_records.py")
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return tuple(mod.PER_RECORD_AUTHORED_FIELDS)


PER_RECORD_ONLY_FIELDS: tuple[str, ...] = _exporter_authored_fields()


def aggregate_individual_files(
    ingredients_dir: Path,
    category: str,
    validate: bool = False,
    exclude_fields: tuple[str, ...] = PER_RECORD_ONLY_FIELDS,
) -> tuple[dict | None, list[str]]:
    """Aggregate individual YAML files into a collection.

    Args:
        ingredients_dir: Directory containing individual ingredient files.
        category: Category name ('mapped' or 'unmapped').
        validate: If True, validate each record before aggregating.
        exclude_fields: Per-record-authored fields to drop, so the output is in
            the collection's shape. Defaults to the exporter's
            PER_RECORD_AUTHORED_FIELDS -- without this, aggregating back into
            data/curated/ injects `discussions` into a document that by design
            does not carry it.

    Returns:
        ``(collection, errors)``. ``collection`` is None only when the category
        directory is absent or empty. ``errors`` lists per-file failures; a record
        that fails to load is SKIPPED, so a non-empty list means the collection is
        missing records and the caller MUST NOT treat it as complete.
    """
    category_dir = ingredients_dir / category
    if not category_dir.exists():
        console.print(f"[yellow]Category directory not found: {category_dir}[/yellow]")
        return None, []

    # Find all YAML files
    yaml_files = sorted(category_dir.glob("*.yaml")) + sorted(category_dir.glob("*.yml"))
    if not yaml_files:
        console.print(f"[yellow]No YAML files found in {category_dir}[/yellow]")
        return None, []

    ingredients = []
    errors = []

    for yaml_file in yaml_files:
        try:
            ingredient = load_yaml(yaml_file)

            # Structural checks that run ALWAYS, not just under --validate,
            # because they are the ones that cause silent record loss. load_yaml
            # returns {} for an empty or comment-only document, which would
            # otherwise be appended as a `- {}` record: the file's real content is
            # gone, the collection still "has" a record, and nothing errors.
            if not isinstance(ingredient, dict):
                errors.append(f"{yaml_file.name}: Invalid format (not a mapping)")
                continue
            if not ingredient:
                errors.append(f"{yaml_file.name}: Empty document (truncated or comment-only?)")
                continue
            if 'mapping_status' not in ingredient:
                # Required by the schema, and the aggregator counts on it; without
                # it the header's status counts silently under-report.
                errors.append(f"{yaml_file.name}: Missing 'mapping_status' field")
                continue

            # Validate basic structure
            if validate:
                if 'identifier' not in ingredient:
                    errors.append(f"{yaml_file.name}: Missing 'identifier' field")
                    continue
                if 'preferred_term' not in ingredient:
                    errors.append(f"{yaml_file.name}: Missing 'preferred_term' field")
                    continue
                # `mapping_status` is checked unconditionally above.

            for field_name in exclude_fields:
                ingredient.pop(field_name, None)

            ingredients.append(ingredient)

        except Exception as e:
            errors.append(f"{yaml_file.name}: {e}")

    if errors:
        # Loud, and fatal in main(): each of these is a record MISSING from the
        # collection. Silently dropping one and exiting 0 meant `sync-curated`
        # could delete a record from data/curated/, after which the next export
        # deletes its per-record file too and the round-trip gate — comparing two
        # sources that now agree it does not exist — passes.
        console.print(f"\n[red]Errors in {category} — {len(errors)} record(s) NOT aggregated:[/red]")
        for error in errors[:10]:  # Show first 10 errors
            console.print(f"  [red]✗[/red] {error}")
        if len(errors) > 10:
            console.print(f"  [dim]... and {len(errors) - 10} more errors[/dim]")

    # Count by status explicitly. `unmapped_count` used to be `total - mapped`,
    # which silently relabelled every other status as UNMAPPED — REJECTED records
    # were reported as unmapped in the header consumers read.
    mapped_count = sum(1 for ing in ingredients if ing.get('mapping_status') == 'MAPPED')
    unmapped_count = sum(1 for ing in ingredients if ing.get('mapping_status') == 'UNMAPPED')
    other_count = len(ingredients) - mapped_count - unmapped_count
    if other_count:
        # The counts legitimately do not sum: IngredientCollection is closed and
        # has no slot for other statuses, so say so here rather than folding them
        # into unmapped_count and asserting something false in the file.
        other_statuses = sorted(
            {
                str(ing.get('mapping_status'))
                for ing in ingredients
                if ing.get('mapping_status') not in ('MAPPED', 'UNMAPPED')
            }
        )
        console.print(
            f"[yellow]note:[/yellow] {category}: {other_count} record(s) are neither "
            f"MAPPED nor UNMAPPED ({', '.join(other_statuses)}), so "
            f"mapped_count + unmapped_count < total_count. This is accurate, not a "
            f"miscount — the schema has no slot for these."
        )

    # Create collection with metadata
    collection = {
        'generation_date': datetime.now(timezone.utc).isoformat(),
        'total_count': len(ingredients),
        'mapped_count': mapped_count,
        'unmapped_count': unmapped_count,
        'ingredients': ingredients
    }

    return collection, errors


@click.command()
@click.option(
    "--ingredients-dir",
    type=click.Path(exists=False),
    default=None,
    help="Directory containing individual ingredient files (default: data/ingredients/)",
)
@click.option(
    "--output-dir",
    type=click.Path(exists=False),
    required=True,
    help=(
        "Directory to write collection files. REQUIRED — there is deliberately no "
        "default. It used to default to data/collections/, which nothing in the repo "
        "reads, so a bare invocation looked like it worked while changing nothing that "
        "mattered (#169); that is how 55 curation events sat unreconciled (#148). "
        "Use data/curated/ to write back into the live collection (`just sync-curated`), "
        "or a temp dir to verify a round trip without touching the tree."
    ),
)
@click.option(
    "--validate",
    is_flag=True,
    help="Validate each record before aggregating",
)
def main(ingredients_dir: str | None, output_dir: str | None, validate: bool):
    """Aggregate individual ingredient YAML files into collections."""
    # Set default paths
    if ingredients_dir is None:
        ingredients_dir_path = _project_root / "data" / "ingredients"
    else:
        ingredients_dir_path = Path(ingredients_dir)

    output_dir_path = Path(output_dir)

    if not ingredients_dir_path.exists():
        console.print(f"[red]Ingredients directory not found: {ingredients_dir_path}[/red]")
        console.print("[yellow]Run export_individual_records.py first to create individual files.[/yellow]")
        sys.exit(1)

    # Header
    console.print("\n[bold]Aggregate Individual Ingredients to Collections[/bold]")
    console.print(f"Input:  {ingredients_dir_path}")
    console.print(f"Output: {output_dir_path}")
    if validate:
        console.print("[yellow]Validation: enabled[/yellow]")
    console.print()

    # Create output directory
    output_dir_path.mkdir(parents=True, exist_ok=True)

    # Process both categories
    categories = ['mapped', 'unmapped']
    total_ingredients = 0
    total_errors = 0
    pending: list[tuple[str, dict]] = []

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        for category in categories:
            task = progress.add_task(f"Aggregating {category}...", total=None)

            collection, errors = aggregate_individual_files(
                ingredients_dir_path,
                category,
                validate=validate
            )
            total_errors += len(errors)

            if collection is None:
                progress.update(
                    task,
                    description=f"[yellow]{category}: skipped (no files)[/yellow]"
                )
                continue

            # Buffer, do not write yet. `sync-curated` points --output-dir at
            # data/curated/, so writing a category before knowing whether a later
            # one failed would overwrite the live collection with a short one and
            # then exit 1 — destroying the record in the working tree and leaving
            # the caller to notice and `git checkout`. Nothing is written unless
            # every record aggregated.
            pending.append((category, collection))
            total_ingredients += collection['total_count']

            progress.update(
                task,
                description=f"[green]{category}: {collection['total_count']} ingredients[/green]"
            )

    if total_errors:
        # Fail BEFORE writing anything.
        console.print(
            f"\n[bold red]✗ {total_errors} record(s) could not be aggregated.[/bold red]"
        )
        console.print(
            "[red]No collections were written — the existing files are untouched.[/red]"
        )
        console.print("[red]Fix the offending file(s) and re-run.[/red]")
        sys.exit(1)

    for category, collection in pending:
        output_file = output_dir_path / f"{category}_ingredients.yaml"
        save_yaml(collection, output_file, backup=True)

    # Summary
    console.print("\n[bold]Summary:[/bold]")
    console.print(f"  Total ingredients aggregated: {total_ingredients}")
    console.print(f"  Collections written to: {output_dir_path}")

    for category in categories:
        output_file = output_dir_path / f"{category}_ingredients.yaml"
        if output_file.exists():
            console.print(f"    [green]✓[/green] {output_file.name}")

    if validate:
        console.print("\n[green]Validation passed for all files[/green]")

    sys.exit(0)


if __name__ == "__main__":
    main()
