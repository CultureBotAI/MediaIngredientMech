#!/usr/bin/env python3
"""Batch enrichment of chemical properties for CHEBI-mapped ingredients.

Loads ingredient records from YAML, filters for CHEBI mappings without existing
chemical_properties, fetches formula/SMILES/InChI from ChEBI OLS and PubChem APIs,
and updates the records with chemical properties.
"""

from __future__ import annotations

import sys
from pathlib import Path

import click
import yaml
from rich.console import Console
from rich.progress import Progress
from rich.table import Table

# Add src to path so we can import the package
_project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_project_root / "src"))

from mediaingredientmech.utils.chemical_properties_client import (
    ChemicalPropertiesClient,
)

console = Console()


def load_ingredients(yaml_path: Path) -> dict:
    """Load ingredients from YAML file."""
    with open(yaml_path) as f:
        return yaml.safe_load(f)


def save_ingredients(yaml_path: Path, data: dict):
    """Save ingredients to YAML file."""
    with open(yaml_path, "w") as f:
        yaml.dump(
            data,
            f,
            default_flow_style=False,
            sort_keys=False,
            allow_unicode=True,
            width=120,
        )


def filter_chebi_without_properties(data: dict) -> list[dict]:
    """Filter for CHEBI-mapped ingredients without chemical_properties.

    Args:
        data: Loaded YAML data (IngredientCollection or list).

    Returns:
        List of ingredient records that need enrichment.
    """
    # Handle both IngredientCollection (with 'ingredients' key) and raw list
    if isinstance(data, dict) and "ingredients" in data:
        records = data["ingredients"]
    elif isinstance(data, list):
        records = data
    else:
        records = []

    candidates = []
    for record in records:
        # Check if already has chemical_properties
        if record.get("chemical_properties"):
            continue

        # Check if mapped to CHEBI
        ontology_mapping = record.get("ontology_mapping")
        if not ontology_mapping:
            continue

        if ontology_mapping.get("ontology_source") == "CHEBI":
            candidates.append(record)

    return candidates


@click.command()
@click.option(
    "--input",
    "-i",
    "input_path",
    type=click.Path(exists=True, path_type=Path),
    default=Path("data/curated/mapped_ingredients.yaml"),
    help="Input YAML file with ingredient records",
)
@click.option(
    "--output",
    "-o",
    "output_path",
    type=click.Path(path_type=Path),
    default=None,
    help="Output YAML file (defaults to overwrite input)",
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Show what would be enriched without making changes",
)
@click.option(
    "--limit",
    type=int,
    default=None,
    help="Limit number of ingredients to process (for testing)",
)
def main(
    input_path: Path,
    output_path: Optional[Path],
    dry_run: bool,
    limit: Optional[int],
):
    """Enrich CHEBI-mapped ingredients with chemical properties."""
    console.print(f"\n[bold]Chemical Properties Enrichment[/bold]")
    console.print(f"Input: {input_path}")

    # Load data
    data = load_ingredients(input_path)

    # Filter candidates
    candidates = filter_chebi_without_properties(data)

    if not candidates:
        console.print("\n[yellow]No CHEBI ingredients need enrichment.[/yellow]")
        return

    console.print(f"\nFound {len(candidates)} CHEBI-mapped ingredients without properties")

    # Apply limit if specified
    if limit:
        candidates = candidates[:limit]
        console.print(f"Limited to first {limit} ingredients")

    if dry_run:
        console.print("\n[bold yellow]DRY RUN - No changes will be saved[/bold yellow]")

        # Show preview table
        table = Table(title="Ingredients to Enrich")
        table.add_column("Identifier", style="cyan")
        table.add_column("Preferred Term", style="green")
        table.add_column("CHEBI ID", style="yellow")

        for record in candidates[:10]:  # Show first 10
            ontology_mapping = record.get("ontology_mapping", {})
            table.add_row(
                record.get("ontology_id", "N/A"),
                record.get("preferred_term", "N/A"),
                ontology_mapping.get("ontology_id", "N/A"),
            )

        console.print(table)

        if len(candidates) > 10:
            console.print(f"\n... and {len(candidates) - 10} more")

        return

    # Initialize client
    client = ChemicalPropertiesClient(cache_enabled=True)

    # Process with progress bar
    enriched_count = 0
    failed_count = 0
    skipped_count = 0

    results = []

    with Progress() as progress:
        task = progress.add_task(
            "[cyan]Enriching chemical properties...",
            total=len(candidates),
        )

        for record in candidates:
            ontology_mapping = record.get("ontology_mapping", {})
            ontology_id = ontology_mapping.get("ontology_id")
            label = ontology_mapping.get("ontology_label", "")
            source = ontology_mapping.get("ontology_source")

            if not ontology_id or source != "CHEBI":
                skipped_count += 1
                progress.update(task, advance=1)
                continue

            # Get properties
            props = client.get_properties(ontology_id, label, source)

            if props:
                # Add to record
                record["chemical_properties"] = props.to_dict()
                enriched_count += 1
                results.append(
                    {
                        "id": ontology_id,
                        "term": label,
                        "formula": props.molecular_formula or "N/A",
                        "smiles": props.smiles or "N/A",
                        "source": props.data_source or "N/A",
                    }
                )
            else:
                failed_count += 1
                results.append(
                    {
                        "id": ontology_id,
                        "term": label,
                        "formula": "FAILED",
                        "smiles": "FAILED",
                        "source": "N/A",
                    }
                )

            progress.update(task, advance=1)

    # Show results table
    console.print("\n[bold]Enrichment Results[/bold]")

    table = Table(title=f"Processed {len(candidates)} ingredients")
    table.add_column("CHEBI ID", style="cyan")
    table.add_column("Term", style="green")
    table.add_column("Formula", style="yellow")
    table.add_column("SMILES", style="blue", overflow="fold")
    table.add_column("Source", style="magenta")

    for result in results[:20]:  # Show first 20
        table.add_row(
            result["id"],
            result["term"][:40],  # Truncate long names
            result["formula"],
            result["smiles"][:50] if result["smiles"] != "N/A" else "N/A",
            result["source"],
        )

    console.print(table)

    if len(results) > 20:
        console.print(f"\n... and {len(results) - 20} more")

    # Summary
    console.print("\n[bold]Summary[/bold]")
    console.print(f"  Enriched: [green]{enriched_count}[/green]")
    console.print(f"  Failed: [red]{failed_count}[/red]")
    console.print(f"  Skipped: [yellow]{skipped_count}[/yellow]")

    if enriched_count > 0:
        # Save output
        output_path = output_path or input_path
        save_ingredients(output_path, data)
        console.print(f"\n[bold green]Saved to {output_path}[/bold green]")
    else:
        console.print("\n[yellow]No enrichment performed - nothing to save[/yellow]")


if __name__ == "__main__":
    main()
