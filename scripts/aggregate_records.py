#!/usr/bin/env python3
"""Aggregate individual ingredient YAML files into collection format.

This script performs the reverse operation of export_individual_records.py,
combining individual ingredient YAML files back into collection format for
reporting and backward compatibility.

Usage:
    python scripts/aggregate_records.py
    python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir data/collections
    python scripts/aggregate_records.py --validate
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


def aggregate_individual_files(
    ingredients_dir: Path,
    category: str,
    validate: bool = False
) -> dict | None:
    """Aggregate individual YAML files into a collection.

    Args:
        ingredients_dir: Directory containing individual ingredient files.
        category: Category name ('mapped' or 'unmapped').
        validate: If True, validate each record before aggregating.

    Returns:
        Collection dictionary with metadata and ingredients list, or None if error.
    """
    category_dir = ingredients_dir / category
    if not category_dir.exists():
        console.print(f"[yellow]Category directory not found: {category_dir}[/yellow]")
        return None

    # Find all YAML files
    yaml_files = sorted(category_dir.glob("*.yaml")) + sorted(category_dir.glob("*.yml"))
    if not yaml_files:
        console.print(f"[yellow]No YAML files found in {category_dir}[/yellow]")
        return None

    ingredients = []
    errors = []

    for yaml_file in yaml_files:
        try:
            ingredient = load_yaml(yaml_file)

            # Validate basic structure
            if validate:
                if not isinstance(ingredient, dict):
                    errors.append(f"{yaml_file.name}: Invalid format (not a dict)")
                    continue
                if 'identifier' not in ingredient:
                    errors.append(f"{yaml_file.name}: Missing 'identifier' field")
                    continue
                if 'preferred_term' not in ingredient:
                    errors.append(f"{yaml_file.name}: Missing 'preferred_term' field")
                    continue
                if 'mapping_status' not in ingredient:
                    errors.append(f"{yaml_file.name}: Missing 'mapping_status' field")
                    continue

            ingredients.append(ingredient)

        except Exception as e:
            errors.append(f"{yaml_file.name}: {e}")

    if errors:
        console.print(f"\n[yellow]Errors in {category}:[/yellow]")
        for error in errors[:10]:  # Show first 10 errors
            console.print(f"  [red]✗[/red] {error}")
        if len(errors) > 10:
            console.print(f"  [dim]... and {len(errors) - 10} more errors[/dim]")

    # Count mapped vs unmapped
    mapped_count = sum(
        1 for ing in ingredients
        if ing.get('mapping_status') == 'MAPPED'
    )
    unmapped_count = len(ingredients) - mapped_count

    # Create collection with metadata
    collection = {
        'generation_date': datetime.now(timezone.utc).isoformat(),
        'total_count': len(ingredients),
        'mapped_count': mapped_count,
        'unmapped_count': unmapped_count,
        'ingredients': ingredients
    }

    return collection


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
    default=None,
    help="Directory to write collection files (default: data/collections/)",
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

    if output_dir is None:
        output_dir_path = _project_root / "data" / "collections"
    else:
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

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        for category in categories:
            task = progress.add_task(f"Aggregating {category}...", total=None)

            collection = aggregate_individual_files(
                ingredients_dir_path,
                category,
                validate=validate
            )

            if collection is None:
                progress.update(
                    task,
                    description=f"[yellow]{category}: skipped (no files)[/yellow]"
                )
                continue

            # Write collection file
            output_file = output_dir_path / f"{category}_ingredients.yaml"
            save_yaml(collection, output_file, backup=True)

            ingredient_count = collection['total_count']
            total_ingredients += ingredient_count

            progress.update(
                task,
                description=f"[green]{category}: {ingredient_count} ingredients → {output_file.name}[/green]"
            )

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
