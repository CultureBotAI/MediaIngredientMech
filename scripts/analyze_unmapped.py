#!/usr/bin/env python3
"""Analyze and categorize unmapped media ingredients.

This script:
1. Loads all unmapped ingredients
2. Categorizes them by type (simple chemical, mixture, environmental, etc.)
3. Applies normalization to identify likely mappable items
4. Generates a prioritized curation list
5. Outputs analysis report
"""

from __future__ import annotations

import sys
from collections import Counter, defaultdict
from pathlib import Path

import click
import yaml
from rich.console import Console
from rich.table import Table

# Add src to path
_project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_project_root / "src"))

from mediaingredientmech.utils.chemical_normalizer import (
    categorize_unmapped_name,
    normalize_chemical_name,
)

console = Console()


def load_unmapped_ingredients(data_path: Path) -> list[dict]:
    """Load unmapped ingredients from YAML file."""
    if not data_path.exists():
        console.print(f"[red]Error: {data_path} not found[/red]")
        return []

    with open(data_path) as f:
        data = yaml.safe_load(f)

    return [
        ing for ing in data.get('ingredients', [])
        if ing.get('mapping_status') == 'UNMAPPED'
    ]


def analyze_unmapped(ingredients: list[dict]) -> dict:
    """Analyze unmapped ingredients and categorize them.

    Returns:
        Analysis results with categories, priorities, and statistics
    """
    categories = defaultdict(list)
    normalization_stats = Counter()
    mappability_scores = {}

    for ing in ingredients:
        name = ing.get('preferred_term', '')
        identifier = ing.get('identifier', '')
        stats = ing.get('occurrence_statistics', {})
        occurrences = stats.get('total_occurrences', 0)

        # Categorize
        category = categorize_unmapped_name(name)
        categories[category].append(ing)

        # Normalize
        norm_result = normalize_chemical_name(name)
        normalization_stats.update(norm_result.applied_rules)

        # Compute mappability score (0-100)
        # Higher score = more likely to be mappable
        score = 0

        if category == 'SIMPLE_CHEMICAL':
            score += 60
        elif category == 'ENVIRONMENTAL':
            score += 30
        elif category == 'INCOMPLETE':
            score += 20
        elif category == 'COMPLEX_MIXTURE':
            score += 10
        elif category == 'PLACEHOLDER':
            score += 0
        else:
            score += 15

        # Boost if normalization found something
        if norm_result.applied_rules:
            score += 20

        # Boost if we have search variants
        if len(norm_result.variants) > 1:
            score += 10

        # Small boost for frequency (popular ingredients more likely to be real)
        if occurrences > 100:
            score += 5
        elif occurrences > 50:
            score += 3

        mappability_scores[identifier] = min(score, 100)

    return {
        'categories': dict(categories),
        'normalization_stats': dict(normalization_stats),
        'mappability_scores': mappability_scores,
        'total_count': len(ingredients),
    }


def display_analysis_report(analysis: dict) -> None:
    """Display analysis report in terminal."""
    console.print("\n[bold cyan]Unmapped Ingredients Analysis Report[/bold cyan]\n")

    # Category breakdown
    table = Table(title="Category Breakdown", show_lines=True)
    table.add_column("Category", style="bold")
    table.add_column("Count", justify="right")
    table.add_column("Percentage", justify="right")
    table.add_column("Examples", max_width=50)

    total = analysis['total_count']
    for category, ingredients in sorted(
        analysis['categories'].items(),
        key=lambda x: len(x[1]),
        reverse=True
    ):
        count = len(ingredients)
        pct = (count / total * 100) if total > 0 else 0
        examples = [ing.get('preferred_term', '')[:30] for ing in ingredients[:3]]
        examples_str = ', '.join(examples)

        table.add_row(
            category,
            str(count),
            f"{pct:.1f}%",
            examples_str,
        )

    console.print(table)

    # Normalization effectiveness
    if analysis['normalization_stats']:
        console.print("\n[bold cyan]Normalization Rules Applied[/bold cyan]")
        norm_table = Table()
        norm_table.add_column("Rule", style="bold")
        norm_table.add_column("Count", justify="right")

        for rule, count in sorted(
            analysis['normalization_stats'].items(),
            key=lambda x: x[1],
            reverse=True
        ):
            norm_table.add_row(rule, str(count))

        console.print(norm_table)

    # Mappability summary
    scores = list(analysis['mappability_scores'].values())
    if scores:
        console.print("\n[bold cyan]Mappability Estimate[/bold cyan]")
        high_mappability = sum(1 for s in scores if s >= 70)
        medium_mappability = sum(1 for s in scores if 40 <= s < 70)
        low_mappability = sum(1 for s in scores if s < 40)

        map_table = Table()
        map_table.add_column("Likelihood", style="bold")
        map_table.add_column("Count", justify="right")
        map_table.add_column("Percentage", justify="right")

        map_table.add_row(
            "High (≥70)",
            str(high_mappability),
            f"{high_mappability / total * 100:.1f}%",
        )
        map_table.add_row(
            "Medium (40-69)",
            str(medium_mappability),
            f"{medium_mappability / total * 100:.1f}%",
        )
        map_table.add_row(
            "Low (<40)",
            str(low_mappability),
            f"{low_mappability / total * 100:.1f}%",
        )

        console.print(map_table)


def generate_prioritized_list(
    ingredients: list[dict],
    analysis: dict,
    output_path: Path,
) -> None:
    """Generate prioritized curation list sorted by mappability score."""
    scores = analysis['mappability_scores']
    categories = {}
    for cat, ings in analysis['categories'].items():
        for ing in ings:
            categories[ing['identifier']] = cat

    # Sort by mappability score (high to low)
    sorted_ingredients = sorted(
        ingredients,
        key=lambda x: scores.get(x['identifier'], 0),
        reverse=True,
    )

    # Generate markdown report
    lines = [
        "# Unmapped Ingredients - Prioritized Curation List",
        "",
        f"Generated: {Path(__file__).stem}",
        f"Total unmapped: {len(ingredients)}",
        "",
        "## Curation Priority Order",
        "",
        "Ingredients are sorted by estimated mappability (high to low).",
        "",
        "| # | Identifier | Name | Category | Score | Occurrences | Variants |",
        "|---|------------|------|----------|-------|-------------|----------|",
    ]

    for i, ing in enumerate(sorted_ingredients, 1):
        identifier = ing.get('identifier', '')
        name = ing.get('preferred_term', '')
        category = categories.get(identifier, 'UNKNOWN')
        score = scores.get(identifier, 0)
        stats = ing.get('occurrence_statistics', {})
        occurrences = stats.get('total_occurrences', 0)

        # Get normalization variants
        norm_result = normalize_chemical_name(name)
        variant_count = len(norm_result.variants)

        lines.append(
            f"| {i} | `{identifier}` | {name} | {category} | {score} | {occurrences} | {variant_count} |"
        )

    lines.append("")
    lines.append("## Category Descriptions")
    lines.append("")
    lines.append("- **SIMPLE_CHEMICAL**: Likely mappable chemical with notation issues")
    lines.append("- **ENVIRONMENTAL**: Environmental sample (soil, seawater, etc.)")
    lines.append("- **COMPLEX_MIXTURE**: Vitamin/metal solution, media mixture")
    lines.append("- **INCOMPLETE**: Generic or unclear term needing context")
    lines.append("- **PLACEHOLDER**: Reference to external source (not mappable)")
    lines.append("- **UNKNOWN**: Cannot categorize automatically")
    lines.append("")

    # Write to file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text('\n'.join(lines))
    console.print(f"\n[green]Prioritized list saved to: {output_path}[/green]")


def generate_category_files(
    ingredients: list[dict],
    analysis: dict,
    output_dir: Path,
) -> None:
    """Generate separate YAML files for each category."""
    output_dir.mkdir(parents=True, exist_ok=True)

    for category, cat_ingredients in analysis['categories'].items():
        # Sort by occurrences within category
        sorted_ings = sorted(
            cat_ingredients,
            key=lambda x: x.get('occurrence_statistics', {}).get('total_occurrences', 0),
            reverse=True,
        )

        output_file = output_dir / f"{category.lower()}.yaml"
        data = {
            'category': category,
            'count': len(sorted_ings),
            'ingredients': sorted_ings,
        }

        with open(output_file, 'w') as f:
            yaml.dump(data, f, sort_keys=False, allow_unicode=True)

        console.print(f"  - {category}: {len(sorted_ings)} items → {output_file.name}")


@click.command()
@click.option(
    '--data-path',
    type=click.Path(path_type=Path),
    default=Path('data/curated/unmapped_ingredients.yaml'),
    help='Path to unmapped ingredients YAML file',
)
@click.option(
    '--output',
    type=click.Path(path_type=Path),
    default=Path('notes/unmapped_analysis.md'),
    help='Output path for prioritized curation list',
)
@click.option(
    '--category-dir',
    type=click.Path(path_type=Path),
    default=Path('data/ingredients/unmapped'),
    help='Directory to save category-specific YAML files',
)
@click.option(
    '--verbose',
    is_flag=True,
    help='Show detailed normalization for each ingredient',
)
def main(
    data_path: Path,
    output: Path,
    category_dir: Path,
    verbose: bool,
) -> None:
    """Analyze unmapped ingredients and generate curation priorities."""
    console.print("[bold]Analyzing unmapped ingredients...[/bold]\n")

    # Load data
    ingredients = load_unmapped_ingredients(data_path)
    if not ingredients:
        console.print("[yellow]No unmapped ingredients found.[/yellow]")
        return

    console.print(f"Loaded {len(ingredients)} unmapped ingredients\n")

    # Analyze
    analysis = analyze_unmapped(ingredients)

    # Display report
    display_analysis_report(analysis)

    # Generate outputs
    console.print("\n[bold]Generating output files...[/bold]\n")
    generate_prioritized_list(ingredients, analysis, output)
    generate_category_files(ingredients, analysis, category_dir)

    # Verbose output
    if verbose:
        console.print("\n[bold cyan]Detailed Normalization Results[/bold cyan]\n")
        for ing in ingredients[:10]:  # Show first 10
            name = ing.get('preferred_term', '')
            norm_result = normalize_chemical_name(name)
            console.print(f"[bold]{name}[/bold]")
            console.print(f"  Category: {categorize_unmapped_name(name)}")
            console.print(f"  Normalized: {norm_result.normalized}")
            console.print(f"  Variants: {', '.join(norm_result.variants)}")
            console.print(f"  Rules: {', '.join(norm_result.applied_rules) or 'none'}")
            console.print()

    console.print("\n[bold green]Analysis complete![/bold green]")
    console.print(f"Next step: Review {output} and begin curation")


if __name__ == '__main__':
    main()
