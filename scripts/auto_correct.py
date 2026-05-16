#!/usr/bin/env python3
"""
Auto-fix safe P3/P4 issues without human review.

Usage:
    python scripts/auto_correct.py --dry-run
    python scripts/auto_correct.py --apply
    python scripts/auto_correct.py --apply --types chemical_properties
    python scripts/auto_correct.py --apply --source CHEBI --limit 10
"""

import argparse
import sys
from pathlib import Path
from datetime import datetime, timezone

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator
from mediaingredientmech.validation.ingredient_reviewer import IngredientReviewer

console = Console()


def main():
    parser = argparse.ArgumentParser(description="Auto-correct safe issues")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply corrections (default is dry-run)",
    )
    parser.add_argument(
        "--types",
        help="Correction types (comma-separated): chemical_properties,synonyms,curie_format",
    )
    parser.add_argument(
        "--source",
        help="Filter by ontology source: CHEBI,FOODON,ENVO",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Process only first N ingredients (for testing)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.5,
        help="Delay between OLS API calls in seconds (default: 0.5)",
    )

    args = parser.parse_args()

    # Initialize
    curator = IngredientCurator()
    reviewer = IngredientReviewer()

    # Load ingredients
    console.print("[cyan]Loading mapped ingredients...[/cyan]")
    ingredients = curator.get_by_status("MAPPED")

    # Filter by source if specified
    if args.source:
        sources = args.source.split(",")
        ingredients = [
            ing
            for ing in ingredients
            if ing.get("ontology_mapping", {}).get("ontology_id", "").split(":")[0]
            in sources
        ]
        console.print(f"Filtered to {len(ingredients)} ingredients from {args.source}")

    # Limit if specified
    if args.limit:
        ingredients = ingredients[: args.limit]
        console.print(f"Limited to {args.limit} ingredients")

    # Parse correction types
    correction_types = None
    if args.types:
        correction_types = args.types.split(",")

    # Run corrections
    console.print(
        f"\n[cyan]{'Applying' if args.apply else 'Previewing'} corrections for {len(ingredients)} ingredients...[/cyan]\n"
    )

    corrected_count = 0
    changes_by_type = {}

    with Progress(
        SpinnerColumn(),
        *Progress.get_default_columns(),
        TimeElapsedColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("Processing...", total=len(ingredients))

        for ingredient in ingredients:
            # Get corrections
            corrected = reviewer.auto_correct(ingredient, correction_types=correction_types)

            # Check if anything changed
            changed = False
            change_types = []

            # Check chemical properties
            if corrected.get("chemical_properties") != ingredient.get("chemical_properties"):
                changed = True
                change_types.append("chemical_properties")
                changes_by_type["chemical_properties"] = changes_by_type.get("chemical_properties", 0) + 1

            # Check synonyms
            if len(corrected.get("synonyms", [])) > len(ingredient.get("synonyms", [])):
                changed = True
                change_types.append("synonyms")
                changes_by_type["synonyms"] = changes_by_type.get("synonyms", 0) + 1

            # Check CURIE format
            if corrected.get("ontology_mapping", {}).get("ontology_id") != ingredient.get("ontology_mapping", {}).get("ontology_id"):
                changed = True
                change_types.append("curie_format")
                changes_by_type["curie_format"] = changes_by_type.get("curie_format", 0) + 1

            if changed:
                corrected_count += 1

                if args.apply:
                    # Add curation history event in the canonical shape
                    # (CurationEvent: timestamp / curator / action / changes).
                    if "curation_history" not in corrected:
                        corrected["curation_history"] = []

                    corrected["curation_history"].append({
                        "timestamp": datetime.now(timezone.utc).isoformat(),
                        "curator": "auto_correct.py",
                        "action": "AUTO_CORRECTION_APPLIED",
                        "changes": (
                            "Applied auto-corrections: "
                            + ", ".join(sorted(change_types))
                        ),
                        "llm_assisted": False,
                    })

                    # IngredientCurator has no `update_ingredient`; replace
                    # in-place inside `curator.records` and rely on save().
                    for idx, existing in enumerate(curator.records):
                        if existing is ingredient:
                            curator.records[idx] = corrected
                            break

            progress.update(task, advance=1)

    # Save if applying
    if args.apply:
        curator.save()
        console.print(f"\n[green]✓ Applied corrections to {corrected_count} ingredients[/green]")
    else:
        console.print(f"\n[yellow]Dry-run: Would correct {corrected_count} ingredients[/yellow]")

    # Display summary
    console.print("\n[bold]Corrections Summary:[/bold]")
    for change_type, count in sorted(changes_by_type.items()):
        console.print(f"  {change_type}: {count} ingredients")

    if not args.apply:
        console.print("\n[yellow]Run with --apply to save changes[/yellow]")

    return 0


if __name__ == "__main__":
    sys.exit(main())
