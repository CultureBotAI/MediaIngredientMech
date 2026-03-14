#!/usr/bin/env python3
"""Export lists of mapped and unmapped ingredients from curated YAML files.

Generates JSON, CSV, and Markdown lists for both mapped and unmapped ingredients.
Uses the curated collection files as source.
"""

from __future__ import annotations

import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import click
import yaml
from rich.console import Console
from rich.table import Table

console = Console()


def load_ingredients(yaml_path: Path) -> list[dict]:
    """Load ingredients from YAML file."""
    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    # Handle collection format
    if isinstance(data, dict) and "ingredients" in data:
        return data["ingredients"]
    elif isinstance(data, list):
        return data
    return []


def export_to_json(ingredients: list[dict], output_path: Path):
    """Export ingredients to JSON format."""
    records = []
    for ing in ingredients:
        record = {
            "id": ing.get("id", ""),
            "ontology_id": ing.get("ontology_id", ""),
            "preferred_term": ing.get("preferred_term", ""),
            "mapping_status": ing.get("mapping_status", ""),
        }

        # Add ontology mapping details if mapped
        if ing.get("ontology_mapping"):
            om = ing["ontology_mapping"]
            record.update({
                "ontology_label": om.get("ontology_label", ""),
                "ontology_source": om.get("ontology_source", ""),
                "mapping_quality": om.get("mapping_quality", ""),
            })

        # Add statistics
        if ing.get("occurrence_statistics"):
            stats = ing["occurrence_statistics"]
            record.update({
                "total_occurrences": stats.get("total_occurrences", 0),
                "media_count": stats.get("media_count", 0),
            })

        records.append(record)

    with open(output_path, "w") as f:
        json.dump(records, f, indent=2)

    return len(records)


def export_to_csv(ingredients: list[dict], output_path: Path):
    """Export ingredients to CSV format."""
    fieldnames = [
        "id",
        "ontology_id",
        "preferred_term",
        "mapping_status",
        "ontology_label",
        "ontology_source",
        "mapping_quality",
        "total_occurrences",
        "media_count",
    ]

    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for ing in ingredients:
            row = {
                "id": ing.get("id", ""),
                "ontology_id": ing.get("ontology_id", ""),
                "preferred_term": ing.get("preferred_term", ""),
                "mapping_status": ing.get("mapping_status", ""),
            }

            # Add ontology mapping details
            if ing.get("ontology_mapping"):
                om = ing["ontology_mapping"]
                row.update({
                    "ontology_label": om.get("ontology_label", ""),
                    "ontology_source": om.get("ontology_source", ""),
                    "mapping_quality": om.get("mapping_quality", ""),
                })

            # Add statistics
            if ing.get("occurrence_statistics"):
                stats = ing["occurrence_statistics"]
                row.update({
                    "total_occurrences": stats.get("total_occurrences", 0),
                    "media_count": stats.get("media_count", 0),
                })

            writer.writerow(row)

    return len(ingredients)


def export_to_markdown(ingredients: list[dict], output_path: Path, title: str):
    """Export ingredients to Markdown table format."""
    lines = [
        f"# {title}",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        f"Total: {len(ingredients)} ingredients",
        "",
        "| ID | Ontology ID | Preferred Term | Status | Source | Quality | Occurrences |",
        "|---|---|---|---|---|---|---|",
    ]

    for ing in ingredients:
        id_val = ing.get("id", "")
        ont_id = ing.get("ontology_id", "")
        term = ing.get("preferred_term", "")
        status = ing.get("mapping_status", "")

        source = ""
        quality = ""
        if ing.get("ontology_mapping"):
            om = ing["ontology_mapping"]
            source = om.get("ontology_source", "")
            quality = om.get("mapping_quality", "")

        occurrences = ""
        if ing.get("occurrence_statistics"):
            occurrences = str(ing["occurrence_statistics"].get("total_occurrences", 0))

        lines.append(f"| {id_val} | {ont_id} | {term} | {status} | {source} | {quality} | {occurrences} |")

    with open(output_path, "w") as f:
        f.write("\n".join(lines))

    return len(ingredients)


@click.command()
@click.option(
    "--mapped-input",
    type=click.Path(exists=True, path_type=Path),
    default=Path("data/curated/mapped_ingredients.yaml"),
    help="Input YAML file with mapped ingredients",
)
@click.option(
    "--unmapped-input",
    type=click.Path(exists=True, path_type=Path),
    default=Path("data/curated/unmapped_ingredients.yaml"),
    help="Input YAML file with unmapped ingredients",
)
@click.option(
    "--output-dir",
    type=click.Path(path_type=Path),
    default=Path("docs/data"),
    help="Output directory for exported files",
)
@click.option(
    "--format",
    type=click.Choice(["json", "csv", "markdown", "all"]),
    default="all",
    help="Output format",
)
def main(
    mapped_input: Path,
    unmapped_input: Path,
    output_dir: Path,
    format: str,
):
    """Export lists of mapped and unmapped ingredients."""
    console.print("\n[bold]Ingredient List Exporter[/bold]")

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load ingredients
    console.print(f"\nLoading mapped ingredients from {mapped_input}...")
    mapped = load_ingredients(mapped_input)
    console.print(f"  Found {len(mapped)} mapped ingredients")

    console.print(f"\nLoading unmapped ingredients from {unmapped_input}...")
    unmapped = load_ingredients(unmapped_input)
    console.print(f"  Found {len(unmapped)} unmapped ingredients")

    all_ingredients = mapped + unmapped
    console.print(f"\n[bold]Total: {len(all_ingredients)} ingredients[/bold]")

    # Export in requested formats
    formats_to_export = ["json", "csv", "markdown"] if format == "all" else [format]

    for fmt in formats_to_export:
        console.print(f"\n[cyan]Exporting {fmt.upper()} files...[/cyan]")

        if fmt == "json":
            # Mapped JSON
            mapped_json = output_dir / "mapped_ingredients.json"
            count = export_to_json(mapped, mapped_json)
            console.print(f"  ✓ {mapped_json} ({count} records)")

            # Unmapped JSON
            unmapped_json = output_dir / "unmapped_ingredients.json"
            count = export_to_json(unmapped, unmapped_json)
            console.print(f"  ✓ {unmapped_json} ({count} records)")

            # All JSON
            all_json = output_dir / "all_ingredients.json"
            count = export_to_json(all_ingredients, all_json)
            console.print(f"  ✓ {all_json} ({count} records)")

        elif fmt == "csv":
            # Mapped CSV
            mapped_csv = output_dir / "mapped_ingredients.csv"
            count = export_to_csv(mapped, mapped_csv)
            console.print(f"  ✓ {mapped_csv} ({count} records)")

            # Unmapped CSV
            unmapped_csv = output_dir / "unmapped_ingredients.csv"
            count = export_to_csv(unmapped, unmapped_csv)
            console.print(f"  ✓ {unmapped_csv} ({count} records)")

            # All CSV
            all_csv = output_dir / "all_ingredients.csv"
            count = export_to_csv(all_ingredients, all_csv)
            console.print(f"  ✓ {all_csv} ({count} records)")

        elif fmt == "markdown":
            # Mapped MD
            mapped_md = output_dir / "mapped_ingredients.md"
            count = export_to_markdown(mapped, mapped_md, "Mapped Ingredients")
            console.print(f"  ✓ {mapped_md} ({count} records)")

            # Unmapped MD
            unmapped_md = output_dir / "unmapped_ingredients.md"
            count = export_to_markdown(unmapped, unmapped_md, "Unmapped Ingredients")
            console.print(f"  ✓ {unmapped_md} ({count} records)")

            # All MD
            all_md = output_dir / "all_ingredients.md"
            count = export_to_markdown(all_ingredients, all_md, "All Ingredients")
            console.print(f"  ✓ {all_md} ({count} records)")

    # Summary
    console.print("\n[bold green]✅ Export complete![/bold green]")
    console.print(f"\nFiles saved to: {output_dir}")

    # Show sample
    console.print("\n[bold]Sample Records:[/bold]")
    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("ID", style="yellow")
    table.add_column("Ontology ID", style="green")
    table.add_column("Preferred Term", style="white")
    table.add_column("Status", style="magenta")

    for ing in all_ingredients[:5]:
        table.add_row(
            ing.get("id", "")[:25],
            ing.get("ontology_id", "")[:25],
            ing.get("preferred_term", "")[:40],
            ing.get("mapping_status", ""),
        )

    console.print(table)
    console.print(f"\n... and {len(all_ingredients) - 5} more")


if __name__ == "__main__":
    main()
