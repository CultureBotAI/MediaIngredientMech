#!/usr/bin/env python3
"""
Batch enrich all CHEBI-mapped ingredients from OLS.

Usage:
    python scripts/enrich_from_ols.py
    python scripts/enrich_from_ols.py --batch-size 50 --delay 0.5
    python scripts/enrich_from_ols.py --resume
    python scripts/enrich_from_ols.py --dry-run --limit 10
"""

import argparse
import json
import sys
import time
from pathlib import Path
from datetime import datetime, timezone

import yaml
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn, TimeRemainingColumn

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator
from mediaingredientmech.validation.ingredient_reviewer import IngredientReviewer

console = Console()

CHECKPOINT_FILE = Path("reports/enrichment_checkpoint.json")
FAILURES_FILE = Path("reports/enrichment_failures.json")


MAPPED_FILE = Path("data/curated/mapped_ingredients.yaml")


def load_mapped_ingredients():
    """Load the full mapped_ingredients collection (including metadata)."""
    with open(MAPPED_FILE) as f:
        data = yaml.safe_load(f) or {}
    return data


def save_mapped_ingredients(collection):
    """Save mapped ingredients back to YAML, preserving the collection
    metadata (`generation_date`, `total_count`, `mapped_count`,
    `unmapped_count`) instead of writing only `{"ingredients": ...}`.
    """
    with open(MAPPED_FILE, "w") as f:
        yaml.dump(
            collection, f, default_flow_style=False, sort_keys=False, allow_unicode=True
        )


def load_checkpoint() -> dict:
    """Load checkpoint if it exists."""
    if CHECKPOINT_FILE.exists():
        with open(CHECKPOINT_FILE) as f:
            return json.load(f)
    return {"completed": [], "last_index": 0}


def save_checkpoint(checkpoint: dict):
    """Save checkpoint."""
    CHECKPOINT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CHECKPOINT_FILE, "w") as f:
        json.dump(checkpoint, f, indent=2)


def save_failures(failures: list):
    """Save failed enrichments to file."""
    FAILURES_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(FAILURES_FILE, "w") as f:
        json.dump(failures, f, indent=2)


def main():
    parser = argparse.ArgumentParser(description="Enrich CHEBI ingredients from OLS")
    parser.add_argument(
        "--batch-size",
        type=int,
        default=50,
        help="Checkpoint progress every N ingredients (default: 50)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.5,
        help="Delay between API calls in seconds (default: 0.5)",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Resume from last checkpoint",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview without saving changes",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Process only first N ingredients (for testing)",
    )

    args = parser.parse_args()

    # Initialize
    reviewer = IngredientReviewer()

    # Load full collection (with metadata) and operate on its ingredients
    # list in place so saves preserve generation_date / total_count / etc.
    console.print("[cyan]Loading CHEBI-mapped ingredients...[/cyan]")
    collection = load_mapped_ingredients()
    all_ingredients = collection.get("ingredients", []) or []

    # Filter for CHEBI terms
    chebi_ingredients = [
        ing
        for ing in all_ingredients
        if (ing.get("ontology_mapping") or {}).get("ontology_id", "").startswith("CHEBI:")
    ]

    console.print(f"Found {len(chebi_ingredients)} CHEBI-mapped ingredients")

    # Load checkpoint if resuming
    checkpoint = load_checkpoint() if args.resume else {"completed": [], "last_index": 0}
    start_index = checkpoint["last_index"]

    if args.resume and start_index > 0:
        console.print(f"[yellow]Resuming from ingredient {start_index}[/yellow]")

    # Limit if specified
    if args.limit:
        chebi_ingredients = chebi_ingredients[start_index : start_index + args.limit]
    else:
        chebi_ingredients = chebi_ingredients[start_index:]

    console.print(f"Processing {len(chebi_ingredients)} ingredients...\n")

    # Enrich ingredients
    enriched_count = 0
    skipped_count = 0
    failed_count = 0
    failures = []

    with Progress(
        SpinnerColumn(),
        *Progress.get_default_columns(),
        TimeElapsedColumn(),
        TimeRemainingColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("Enriching...", total=len(chebi_ingredients))

        for i, ingredient in enumerate(chebi_ingredients):
            ontology_id = ingredient.get("ontology_mapping", {}).get("ontology_id")
            preferred_term = ingredient.get("preferred_term", "unknown")

            # Skip if already has chemical properties
            if ingredient.get("chemical_properties") and not args.dry_run:
                skipped_count += 1
                progress.update(task, advance=1)
                continue

            # Try to enrich from OLS
            try:
                properties = reviewer.enrich_from_ols(ontology_id)

                if properties:
                    if not args.dry_run:
                        # Add chemical properties
                        ingredient["chemical_properties"] = properties

                        # Add curation history event
                        if "curation_history" not in ingredient:
                            ingredient["curation_history"] = []

                        ingredient["curation_history"].append({
                            "timestamp": datetime.now(timezone.utc).isoformat(),
                            "curator": "enrich_from_ols.py",
                            "action": "AUTO_BACKFILL_CHEBI_CHEMISTRY",
                            "changes": (
                                "Enriched chemical_properties from EBI OLS v4: "
                                + ", ".join(sorted(properties.keys()))
                            ),
                            "llm_assisted": False,
                        })

                        enriched_count += 1

                        # Checkpoint progress
                        if (i + 1) % args.batch_size == 0:
                            checkpoint["completed"].append(ontology_id)
                            checkpoint["last_index"] = start_index + i + 1
                            save_checkpoint(checkpoint)
                            save_mapped_ingredients(collection)

                    else:
                        console.print(
                            f"[dim]Would enrich {preferred_term}: {list(properties.keys())}[/dim]"
                        )
                        enriched_count += 1

                else:
                    # No properties available
                    skipped_count += 1
                    failures.append({
                        "ontology_id": ontology_id,
                        "preferred_term": preferred_term,
                        "reason": "No chemical properties available in OLS",
                    })

            except Exception as e:
                # Enrichment failed
                failed_count += 1
                failures.append({
                    "ontology_id": ontology_id,
                    "preferred_term": preferred_term,
                    "error": str(e),
                })

            # Rate limiting
            time.sleep(args.delay)

            progress.update(task, advance=1)

    # Final save (collection retains generation_date/total_count/etc.)
    if not args.dry_run and enriched_count > 0:
        save_mapped_ingredients(collection)

    # Clean up checkpoint
    if CHECKPOINT_FILE.exists() and not args.dry_run:
        CHECKPOINT_FILE.unlink()

    # Save failures
    if failures:
        save_failures(failures)

    # Summary
    console.print(f"\n[bold]Enrichment Summary:[/bold]")
    console.print(f"  Total processed: {len(chebi_ingredients)}")
    console.print(f"  [green]Enriched: {enriched_count} ({enriched_count / max(len(chebi_ingredients), 1) * 100:.1f}%)[/green]")
    console.print(f"  [yellow]Skipped: {skipped_count}[/yellow]")
    console.print(f"  [red]Failed: {failed_count}[/red]")

    if failures:
        console.print(f"\n[yellow]Failed ingredients saved to: {FAILURES_FILE}[/yellow]")

    if args.dry_run:
        console.print("\n[yellow]Dry-run mode - no changes saved[/yellow]")

    return 0 if failed_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
