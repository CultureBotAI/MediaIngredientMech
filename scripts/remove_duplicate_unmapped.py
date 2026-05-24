#!/usr/bin/env python3
"""Remove encoding duplicates from unmapped ingredients."""

import sys
from pathlib import Path
import yaml

from mediaingredientmech.utils.yaml_handler import save_yaml
from mediaingredientmech.validation.write_validated import ValidationFailedError

# Paths
DATA_DIR = Path(__file__).parent.parent / "data" / "curated"
UNMAPPED_PATH = DATA_DIR / "unmapped_ingredients.yaml"

# Ingredients to remove (encoding duplicates of already mapped ingredients)
DUPLICATES_TO_REMOVE = [
    "Na2Glycerophosphate.5H2O",  # Duplicate of Na2glycerophosphate•5H2O
    "Sterile dH2O",  # Duplicate of sterile dH2O (case difference)
    "Na2Glycerophosphate•5H2O",  # Duplicate of Na2glycerophosphate•5H2O (case difference)
]


def load_yaml(path):
    """Load YAML file."""
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    """Remove duplicate unmapped ingredients."""
    print("=" * 80)
    print("REMOVE DUPLICATE UNMAPPED INGREDIENTS")
    print("=" * 80)
    print()

    # Load unmapped
    print("Loading unmapped_ingredients.yaml...")
    data = load_yaml(UNMAPPED_PATH)
    ingredients = data["ingredients"]
    print(f"  Loaded {len(ingredients)} unmapped ingredients")
    print()

    # Remove duplicates
    print("Removing encoding duplicates...")
    removed_count = 0

    for dup_term in DUPLICATES_TO_REMOVE:
        print(f"  Removing: {dup_term}")

        for i, record in enumerate(ingredients):
            if record["preferred_term"] == dup_term:
                del ingredients[i]
                removed_count += 1
                print(f"    ✓ Removed (was {record['ontology_id']})")
                break

    print()

    # Update counts
    data["total_count"] = len(ingredients)
    data["unmapped_count"] = len(ingredients)

    # Save
    print("Saving updated file...")
    try:
        save_yaml(data, UNMAPPED_PATH, validate=True, target_class="IngredientCollection")
    except ValidationFailedError as exc:
        print(exc.summary(), file=sys.stderr)
        raise
    print(f"  ✓ Saved {UNMAPPED_PATH}")
    print()

    # Summary
    print("=" * 80)
    print("CLEANUP COMPLETE")
    print("=" * 80)
    print(f"Removed: {removed_count} duplicate ingredients")
    print(f"Total unmapped: {len(ingredients)}")
    print()
    print("Note: These were encoding variants of already mapped ingredients:")
    print("  - Na2glycerophosphate•5H2O (CHEBI:131871)")
    print("  - sterile dH2O (CHEBI:15377)")
    print()


if __name__ == "__main__":
    main()
