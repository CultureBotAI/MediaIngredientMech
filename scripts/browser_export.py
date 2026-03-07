#!/usr/bin/env python3
"""Browser data exporter for MediaIngredientMech.

Transforms ingredient YAML files into JSON for web browser interface.
Generates searchable, filterable ingredient catalog with statistics.
"""

from __future__ import annotations

import json
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

from mediaingredientmech.utils.yaml_handler import load_yaml

console = Console()


def extract_ingredient_for_browser(ingredient: dict, source_file: str) -> dict:
    """Extract ingredient data into browser-friendly format.

    Args:
        ingredient: IngredientRecord data.
        source_file: Source filename.

    Returns:
        Browser-friendly ingredient record.
    """
    # Core fields
    identifier = ingredient.get('identifier', 'UNKNOWN')
    preferred_term = ingredient.get('preferred_term', 'Unknown')
    mapping_status = ingredient.get('mapping_status', 'UNKNOWN')

    # Ontology mapping
    ontology_mapping = ingredient.get('ontology_mapping', {})
    ontology_id = ontology_mapping.get('ontology_id', '')
    ontology_label = ontology_mapping.get('ontology_label', '')
    ontology_source = ontology_mapping.get('ontology_source', '')
    mapping_quality = ontology_mapping.get('mapping_quality', '')

    # Synonyms
    synonyms = []
    for syn in ingredient.get('synonyms', []):
        synonym_text = syn.get('synonym_text', '')
        if synonym_text and synonym_text not in synonyms:
            synonyms.append(synonym_text)

    # Statistics
    stats = ingredient.get('occurrence_statistics', {})
    total_occurrences = stats.get('total_occurrences', 0)
    media_count = stats.get('media_count', 0)

    # Curation info
    curation_history = ingredient.get('curation_history', [])
    last_curated = ''
    curator = ''
    if curation_history:
        last_event = curation_history[-1]
        last_curated = last_event.get('timestamp', '')
        curator = last_event.get('curator', '')

    # Create browser record
    return {
        'id': identifier,
        'preferred_term': preferred_term,
        'mapping_status': mapping_status,
        'ontology_id': ontology_id,
        'ontology_label': ontology_label,
        'ontology_source': ontology_source,
        'mapping_quality': mapping_quality,
        'synonyms': synonyms,
        'synonym_count': len(synonyms),
        'total_occurrences': total_occurrences,
        'media_count': media_count,
        'last_curated': last_curated,
        'curator': curator,
        'source_file': source_file,
        # Searchable text (for quick filtering)
        'searchable': f"{preferred_term} {ontology_label} {' '.join(synonyms)} {identifier}".lower()
    }


def export_ingredients_to_json(
    ingredients_dir: Path,
    output_file: Path
) -> dict:
    """Export all ingredient files to browser JSON.

    Args:
        ingredients_dir: Directory with individual ingredient files.
        output_file: Output JSON file path.

    Returns:
        Export statistics.
    """
    stats = {'total': 0, 'mapped': 0, 'unmapped': 0}

    all_ingredients = []

    # Process mapped ingredients
    mapped_dir = ingredients_dir / 'mapped'
    if mapped_dir.exists():
        for yaml_file in sorted(mapped_dir.glob('*.yaml')):
            try:
                ingredient = load_yaml(yaml_file)
                browser_record = extract_ingredient_for_browser(
                    ingredient,
                    f"mapped/{yaml_file.name}"
                )
                all_ingredients.append(browser_record)
                stats['total'] += 1
                stats['mapped'] += 1
            except Exception as e:
                console.print(f"[red]Error processing {yaml_file.name}: {e}[/red]")

    # Process unmapped ingredients
    unmapped_dir = ingredients_dir / 'unmapped'
    if unmapped_dir.exists():
        for yaml_file in sorted(unmapped_dir.glob('*.yaml')):
            try:
                ingredient = load_yaml(yaml_file)
                browser_record = extract_ingredient_for_browser(
                    ingredient,
                    f"unmapped/{yaml_file.name}"
                )
                all_ingredients.append(browser_record)
                stats['total'] += 1
                stats['unmapped'] += 1
            except Exception as e:
                console.print(f"[red]Error processing {yaml_file.name}: {e}[/red]")

    # Create export data
    export_data = {
        'metadata': {
            'generated': datetime.now(timezone.utc).isoformat(),
            'total_ingredients': stats['total'],
            'mapped_count': stats['mapped'],
            'unmapped_count': stats['unmapped'],
            'version': '1.0.0'
        },
        'ingredients': all_ingredients
    }

    # Write JSON
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(export_data, f, indent=2, ensure_ascii=False)

    return stats


@click.command()
@click.option(
    "--ingredients-dir",
    type=click.Path(exists=False),
    default=None,
    help="Directory with individual ingredient files (default: data/ingredients/)",
)
@click.option(
    "--output",
    type=click.Path(),
    default=None,
    help="Output JSON file (default: docs/data/ingredients.json)",
)
def main(ingredients_dir: str | None, output: str | None):
    """Export ingredients to browser-friendly JSON format."""
    # Set default paths
    if ingredients_dir is None:
        ingredients_dir_path = _project_root / "data" / "ingredients"
    else:
        ingredients_dir_path = Path(ingredients_dir)

    if output is None:
        output_path = _project_root / "docs" / "data" / "ingredients.json"
    else:
        output_path = Path(output)

    if not ingredients_dir_path.exists():
        console.print(f"[red]Ingredients directory not found: {ingredients_dir_path}[/red]")
        console.print("[yellow]Run 'just export-individual' first.[/yellow]")
        sys.exit(1)

    console.print("\n[bold]Browser Export: Ingredients → JSON[/bold]")
    console.print(f"Source: {ingredients_dir_path}")
    console.print(f"Output: {output_path}\n")

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Exporting...", total=None)

        stats = export_ingredients_to_json(ingredients_dir_path, output_path)

        progress.update(
            task,
            description=f"[green]Exported {stats['total']} ingredients[/green]"
        )

    console.print("\n[bold]Summary:[/bold]")
    console.print(f"  Total ingredients: {stats['total']}")
    console.print(f"  Mapped: {stats['mapped']}")
    console.print(f"  Unmapped: {stats['unmapped']}")
    console.print(f"\n[green]✓ Browser data written to: {output_path}[/green]")

    sys.exit(0)


if __name__ == "__main__":
    main()
