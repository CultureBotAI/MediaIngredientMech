#!/usr/bin/env python3
"""Add MediaIngredientMech:XXXXXX IDs to all mapped ingredients.

Currently only unmapped ingredients have the 'id' field with sequential IDs.
This script adds sequential IDs to all mapped ingredients, continuing from
the highest ID in unmapped_ingredients.yaml.
"""

from __future__ import annotations

import sys
from pathlib import Path

import click
import yaml

# Add src to path
_project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_project_root / "src"))

from mediaingredientmech.utils.id_utils import (
    find_highest_id_single_file,
    generate_xmech_id,
)


def load_yaml(path: Path) -> dict:
    """Load YAML file."""
    with open(path) as f:
        return yaml.safe_load(f)


def save_yaml(path: Path, data: dict):
    """Save YAML file with proper formatting."""
    with open(path, "w") as f:
        yaml.dump(
            data,
            f,
            default_flow_style=False,
            sort_keys=False,
            allow_unicode=True,
            width=120,
        )


@click.command()
@click.option(
    "--unmapped-path",
    type=click.Path(exists=True, path_type=Path),
    default=Path("data/curated/unmapped_ingredients.yaml"),
    help="Path to unmapped ingredients (to find highest ID)",
)
@click.option(
    "--mapped-path",
    type=click.Path(exists=True, path_type=Path),
    default=Path("data/curated/mapped_ingredients.yaml"),
    help="Path to mapped ingredients (to add IDs)",
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Show what would be done without making changes",
)
def main(
    unmapped_path: Path,
    mapped_path: Path,
    dry_run: bool,
):
    """Add MediaIngredientMech:XXXXXX IDs to mapped ingredients."""
    print(f"\n{'='*60}")
    print("Add MediaIngredientMech IDs to Mapped Ingredients")
    print(f"{'='*60}\n")

    # Find highest ID in unmapped
    print(f"Finding highest ID in {unmapped_path}...")
    highest_id = find_highest_id_single_file(
        unmapped_path,
        prefix="MediaIngredientMech",
        collection_key="ingredients"
    )
    if highest_id == 0:
        print("ERROR: No IDs found in unmapped ingredients!")
        sys.exit(1)

    print(f"Highest ID in unmapped: MediaIngredientMech:{highest_id:06d}")

    # Load unmapped to verify
    unmapped_data = load_yaml(unmapped_path)

    # Load mapped ingredients
    print(f"\nLoading {mapped_path}...")
    mapped_data = load_yaml(mapped_path)

    # Get ingredients list
    if isinstance(mapped_data, dict) and "ingredients" in mapped_data:
        ingredients = mapped_data["ingredients"]
    elif isinstance(mapped_data, list):
        ingredients = mapped_data
    else:
        print("ERROR: Unexpected data structure in mapped ingredients")
        sys.exit(1)

    # Count ingredients without IDs
    without_ids = [rec for rec in ingredients if "id" not in rec]
    with_ids = [rec for rec in ingredients if "id" in rec]

    print(f"\nIngredients without IDs: {len(without_ids)}")
    print(f"Ingredients with IDs: {len(with_ids)}")

    if len(without_ids) == 0:
        print("\n✅ All ingredients already have IDs!")
        return

    # Calculate ID range needed
    next_id = highest_id + 1
    last_id = next_id + len(without_ids) - 1

    print(f"\nWill assign IDs: MediaIngredientMech:{next_id:06d} to MediaIngredientMech:{last_id:06d}")

    if dry_run:
        print("\n" + "="*60)
        print("DRY RUN - No changes will be made")
        print("="*60)

        # Show first 10 examples
        print("\nFirst 10 assignments:")
        for i, record in enumerate(without_ids[:10]):
            new_id = generate_xmech_id("MediaIngredientMech", next_id + i)
            identifier = record.get("ontology_id", "N/A")
            preferred_term = record.get("preferred_term", "N/A")
            print(f"  {new_id} → {identifier} ({preferred_term[:50]})")

        if len(without_ids) > 10:
            print(f"\n  ... and {len(without_ids) - 10} more")

        return

    # Assign IDs
    print("\nAssigning IDs...")
    current_id = next_id
    assigned_count = 0

    for record in ingredients:
        if "id" not in record:
            new_id = generate_xmech_id("MediaIngredientMech", current_id)
            # Add 'id' as the FIRST field (insert at beginning of dict)
            new_record = {"id": new_id}
            new_record.update(record)
            # Replace record in list (update in place)
            idx = ingredients.index(record)
            ingredients[idx] = new_record
            current_id += 1
            assigned_count += 1

    print(f"✅ Assigned {assigned_count} new IDs")

    # Update metadata if it exists
    if isinstance(mapped_data, dict):
        mapped_data["ingredients"] = ingredients
        # Update generation timestamp if it exists
        from datetime import datetime, timezone
        if "generation_date" in mapped_data:
            mapped_data["generation_date"] = datetime.now(timezone.utc).isoformat()

    # Save
    print(f"\nSaving to {mapped_path}...")
    save_yaml(mapped_path, mapped_data)

    print("\n✅ Done!")
    print(f"\nTotal ingredients now with IDs: {len(ingredients)}")
    print(f"ID range: MediaIngredientMech:000001 to MediaIngredientMech:{current_id-1:06d}")


if __name__ == "__main__":
    main()
