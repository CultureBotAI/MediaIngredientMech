#!/usr/bin/env python3
"""
Apply correction plan from JSON file.

Usage:
    python scripts/apply_corrections.py corrections_plan.json --validate
    python scripts/apply_corrections.py corrections_plan.json --dry-run
    python scripts/apply_corrections.py corrections_plan.json --priority P3,P4
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

from rich.console import Console

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator

console = Console()


def validate_correction(correction: dict, ingredient: dict) -> tuple[bool, str]:
    """
    Validate a correction before applying.

    Returns: (is_valid, error_message)
    """
    # Check ingredient exists
    if not ingredient:
        return False, "Ingredient not found"

    # Check auto-correctable flag
    if not correction.get("auto_correctable", False):
        return False, "Not marked as auto-correctable"

    # Check confidence threshold
    if correction.get("confidence", 0) < 0.5:
        return False, f"Confidence too low: {correction.get('confidence')}"

    # Validate action
    valid_actions = ["enrich_properties", "add_synonym", "normalize_curie", "update_field"]
    if correction.get("action") not in valid_actions:
        return False, f"Invalid action: {correction.get('action')}"

    return True, ""


def apply_correction(correction: dict, ingredient: dict) -> dict:
    """Apply a single correction to an ingredient."""
    corrected = ingredient.copy()

    action = correction["action"]

    if action == "enrich_properties":
        # Add chemical properties
        changes = correction.get("changes", {})
        if "chemical_properties" in changes:
            corrected["chemical_properties"] = changes["chemical_properties"]

    elif action == "add_synonym":
        # Add synonym
        new_synonym = correction.get("changes", {}).get("synonym")
        if new_synonym:
            if "synonyms" not in corrected:
                corrected["synonyms"] = []

            # Check if synonym already exists
            existing_texts = set()
            for syn in corrected["synonyms"]:
                if isinstance(syn, dict):
                    existing_texts.add(syn.get("synonym_text") or syn.get("text", ""))
                else:
                    existing_texts.add(syn)

            if new_synonym not in existing_texts:
                corrected["synonyms"].append({
                    "synonym_text": new_synonym,
                    "synonym_type": "EXACT_SYNONYM",
                    "source": "auto_correction",
                })

    elif action == "normalize_curie":
        # Update CURIE format
        suggested_value = correction.get("suggested_value")
        if suggested_value:
            corrected["ontology_mapping"]["ontology_id"] = suggested_value

    elif action == "update_field":
        # Generic field update
        field_path = correction.get("field_path", "")
        suggested_value = correction.get("suggested_value")

        # Simple field path parsing (e.g., "ontology_mapping.quality")
        parts = field_path.split(".")
        if len(parts) == 1:
            corrected[parts[0]] = suggested_value
        elif len(parts) == 2:
            if parts[0] not in corrected:
                corrected[parts[0]] = {}
            corrected[parts[0]][parts[1]] = suggested_value

    # Add curation history event
    if "curation_history" not in corrected:
        corrected["curation_history"] = []

    corrected["curation_history"].append({
        "timestamp": datetime.now().isoformat(),
        "event": "correction_applied",
        "details": {
            "action": action,
            "source": "apply_corrections.py",
            "confidence": correction.get("confidence"),
        },
    })

    return corrected


def main():
    parser = argparse.ArgumentParser(description="Apply correction plan from JSON")
    parser.add_argument(
        "correction_file",
        type=Path,
        help="JSON file with correction plan",
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Validate corrections before applying",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview without applying changes",
    )
    parser.add_argument(
        "--priority",
        help="Filter by priority (comma-separated): P1,P2,P3,P4",
    )

    args = parser.parse_args()

    # Load correction plan
    if not args.correction_file.exists():
        console.print(f"[red]✗ Correction file not found: {args.correction_file}[/red]")
        return 1

    with open(args.correction_file) as f:
        correction_plan = json.load(f)

    corrections = correction_plan.get("corrections", [])
    console.print(f"[cyan]Loaded {len(corrections)} corrections from {args.correction_file}[/cyan]\n")

    # Filter by priority if specified
    if args.priority:
        priorities = args.priority.split(",")
        # Note: Priority is typically in the associated issue, not the correction
        # For simplicity, we'll apply this filter if we enhance the correction format
        console.print(f"[yellow]Priority filter not yet implemented in correction format[/yellow]")

    # Initialize curator
    curator = IngredientCurator()

    # Apply corrections
    applied_count = 0
    skipped_count = 0
    errors = []

    for correction in corrections:
        ingredient_id = correction.get("ingredient_id")
        preferred_term = correction.get("preferred_term")

        # Find ingredient
        ingredient = None
        if preferred_term:
            ingredient = curator.get_by_preferred_term(preferred_term)
        elif ingredient_id:
            # Find by ID
            all_ingredients = curator.get_by_status("MAPPED")
            for ing in all_ingredients:
                if ing.get("id") == ingredient_id:
                    ingredient = ing
                    break

        if not ingredient:
            errors.append({
                "correction": correction,
                "error": "Ingredient not found",
            })
            skipped_count += 1
            continue

        # Validate if requested
        if args.validate:
            is_valid, error_msg = validate_correction(correction, ingredient)
            if not is_valid:
                errors.append({
                    "correction": correction,
                    "error": error_msg,
                })
                skipped_count += 1
                continue

        # Apply correction
        if not args.dry_run:
            corrected = apply_correction(correction, ingredient)
            # `ingredient` is already an element of `curator.records`;
            # apply_correction mutates a copy, so write the result back in
            # place. IngredientCurator has no `update_ingredient` — `save()`
            # later persists everything.
            for idx, existing in enumerate(curator.records):
                if existing is ingredient:
                    curator.records[idx] = corrected
                    break
            applied_count += 1
        else:
            console.print(f"Would apply: {correction['action']} to {preferred_term}")
            applied_count += 1

    # Save changes
    if not args.dry_run and applied_count > 0:
        curator.save()
        console.print(f"\n[green]✓ Applied {applied_count} corrections[/green]")
    elif args.dry_run:
        console.print(f"\n[yellow]Dry-run: Would apply {applied_count} corrections[/yellow]")

    # Report errors
    if errors:
        console.print(f"\n[red]✗ Skipped {skipped_count} corrections due to errors:[/red]")
        for error in errors[:10]:  # Show first 10
            console.print(f"  - {error['error']}: {error['correction'].get('preferred_term', 'unknown')}")

        if len(errors) > 10:
            console.print(f"  ...and {len(errors) - 10} more")

    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
