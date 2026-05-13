#!/usr/bin/env python3
"""
Cross-check ingredient synonyms with ontology synonyms.

Usage:
    python scripts/validate_synonyms.py
    python scripts/validate_synonyms.py --add-missing
    python scripts/validate_synonyms.py --report-only
    python scripts/validate_synonyms.py --ingredient "glucose"
"""

import argparse
import sys
from pathlib import Path
from datetime import datetime

from rich.console import Console
from rich.table import Table
from rich import box

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator
from mediaingredientmech.utils.ontology_client import OntologyClient

console = Console()


def compare_synonyms(ingredient: dict, ontology_client: OntologyClient) -> dict:
    """
    Compare ingredient synonyms with ontology synonyms.

    Returns dict with:
      - ontology_synonyms: Set of synonyms from ontology
      - record_synonyms: Set of synonyms in record
      - missing: Synonyms in ontology but not in record
      - extra: Synonyms in record but not in ontology
    """
    ontology_id = ingredient.get("ontology_mapping", {}).get("ontology_id")
    if not ontology_id:
        return {}

    # Get ontology synonyms
    term_info = ontology_client.get_term_info(ontology_id)
    if not term_info:
        return {}

    ontology_syns = set(term_info.get("synonyms", []))

    # Get record synonyms
    record_syns = set()
    for syn in ingredient.get("synonyms", []):
        if isinstance(syn, dict):
            record_syns.add(syn.get("text", ""))
        else:
            record_syns.add(syn)

    # Compare
    missing = ontology_syns - record_syns
    extra = record_syns - ontology_syns
    shared = ontology_syns & record_syns

    return {
        "ontology_synonyms": ontology_syns,
        "record_synonyms": record_syns,
        "missing": missing,
        "extra": extra,
        "shared": shared,
    }


def display_synonym_comparison(ingredient: dict, comparison: dict):
    """Display synonym comparison in a table."""
    console.print(f"\n[bold]Ingredient: {ingredient.get('preferred_term')}[/bold]")
    console.print(f"Ontology ID: {ingredient.get('ontology_mapping', {}).get('ontology_id')}")
    console.print()

    # Create table
    table = Table(title="Synonym Comparison", box=box.ROUNDED)
    table.add_column("Source", style="cyan")
    table.add_column("Synonyms", style="white")
    table.add_column("Count", style="magenta")

    table.add_row(
        "Ontology",
        "\n".join(sorted(comparison["ontology_synonyms"]))[:200] + "...",
        str(len(comparison["ontology_synonyms"])),
    )

    table.add_row(
        "Record",
        "\n".join(sorted(comparison["record_synonyms"]))[:200] + "...",
        str(len(comparison["record_synonyms"])),
    )

    table.add_row(
        "Shared",
        "\n".join(sorted(comparison["shared"]))[:200] + "...",
        str(len(comparison["shared"])),
    )

    console.print(table)

    # Show missing
    if comparison["missing"]:
        console.print(f"\n[yellow]Missing from record ({len(comparison['missing'])}):[/yellow]")
        for syn in sorted(comparison["missing"])[:10]:
            console.print(f"  + {syn}")
        if len(comparison["missing"]) > 10:
            console.print(f"  ...and {len(comparison['missing']) - 10} more")

    # Show extra
    if comparison["extra"]:
        console.print(f"\n[blue]In record but not ontology ({len(comparison['extra'])}):[/blue]")
        for syn in sorted(comparison["extra"])[:10]:
            console.print(f"  - {syn}")
        if len(comparison["extra"]) > 10:
            console.print(f"  ...and {len(comparison['extra']) - 10} more")


def add_missing_synonyms(
    curator: IngredientCurator, ingredient: dict, missing_synonyms: set, interactive: bool = True
) -> bool:
    """
    Add missing synonyms to ingredient record.

    Returns:
        True if synonyms were added
    """
    if not missing_synonyms:
        return False

    if interactive:
        console.print(f"\n[yellow]Add {len(missing_synonyms)} missing synonyms?[/yellow]")
        for syn in sorted(missing_synonyms)[:5]:
            console.print(f"  + {syn}")
        if len(missing_synonyms) > 5:
            console.print(f"  ...and {len(missing_synonyms) - 5} more")

        response = console.input("\nAdd missing synonyms? [y/N]: ")
        if response.lower() != "y":
            return False

    # Add synonyms (schema keys: synonym_text / synonym_type)
    if "synonyms" not in ingredient:
        ingredient["synonyms"] = []

    added = 0
    for syn in missing_synonyms:
        if not syn:
            continue
        ingredient["synonyms"].append({
            "synonym_text": syn,
            "synonym_type": "EXACT_SYNONYM",
            "source": "validate_synonyms.py",
        })
        added += 1

    # Add curation history event using the canonical event shape
    # (timestamp / curator / action / changes); `event`/`details` is not
    # part of the CurationEvent schema.
    if "curation_history" not in ingredient:
        ingredient["curation_history"] = []

    ingredient["curation_history"].append({
        "timestamp": datetime.now().isoformat(),
        "curator": "validate_synonyms.py",
        "action": "ADDED_SYNONYMS",
        "changes": (
            f"Added {added} ontology-derived synonym(s); source=ontology_validation"
        ),
        "llm_assisted": False,
    })

    # Curator has no `update_ingredient`; the in-memory record we just mutated
    # already lives in `curator.records`, so `save()` is enough to persist.
    curator.save()
    console.print(f"[green]✓ Added {added} synonyms[/green]")

    return True


def main():
    parser = argparse.ArgumentParser(description="Validate ingredient synonyms")
    parser.add_argument(
        "--add-missing",
        action="store_true",
        help="Add missing synonyms from ontology",
    )
    parser.add_argument(
        "--report-only",
        action="store_true",
        help="Generate report without modifications",
    )
    parser.add_argument(
        "--ingredient",
        help="Validate specific ingredient by preferred term",
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Prompt before adding each synonym set",
    )
    parser.add_argument(
        "--min-missing",
        type=int,
        default=3,
        help="Minimum missing synonyms to report (default: 3)",
    )

    args = parser.parse_args()

    # Initialize
    curator = IngredientCurator()
    oak_client = OntologyClient()

    # Get ingredients
    if args.ingredient:
        ingredient = curator.get_by_preferred_term(args.ingredient)
        if not ingredient:
            console.print(f"[red]✗ Ingredient '{args.ingredient}' not found[/red]")
            return 1
        ingredients = [ingredient]
    else:
        ingredients = curator.get_by_status("MAPPED")

    console.print(f"[cyan]Validating synonyms for {len(ingredients)} ingredients...[/cyan]\n")

    # Validate synonyms
    total_missing = 0
    ingredients_with_missing = []

    for ingredient in ingredients:
        comparison = compare_synonyms(ingredient, oak_client)

        if not comparison:
            continue

        # Check if significant missing synonyms
        if len(comparison["missing"]) >= args.min_missing:
            ingredients_with_missing.append((ingredient, comparison))
            total_missing += len(comparison["missing"])

    # Report
    console.print(f"\n[bold]Synonym Validation Summary:[/bold]")
    console.print(f"  Total ingredients: {len(ingredients)}")
    console.print(f"  Ingredients with missing synonyms: {len(ingredients_with_missing)}")
    console.print(f"  Total missing synonyms: {total_missing}")

    if args.report_only:
        # Show detailed report
        for ingredient, comparison in ingredients_with_missing[:10]:
            display_synonym_comparison(ingredient, comparison)

        if len(ingredients_with_missing) > 10:
            console.print(f"\n[dim]...and {len(ingredients_with_missing) - 10} more ingredients[/dim]")

        return 0

    # Add missing synonyms if requested
    if args.add_missing and ingredients_with_missing:
        added_count = 0

        for ingredient, comparison in ingredients_with_missing:
            if args.interactive:
                display_synonym_comparison(ingredient, comparison)

            if add_missing_synonyms(
                curator, ingredient, comparison["missing"], interactive=args.interactive
            ):
                added_count += 1

        # Save
        if added_count > 0:
            curator.save()
            console.print(f"\n[green]✓ Updated {added_count} ingredients with missing synonyms[/green]")
        else:
            console.print("\n[yellow]No synonyms added[/yellow]")

    return 0


if __name__ == "__main__":
    sys.exit(main())
