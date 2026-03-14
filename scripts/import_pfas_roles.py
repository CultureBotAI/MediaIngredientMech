#!/usr/bin/env python3
"""Import role assignments from PFAS database (Phase 2).

This script imports role assignments from a PFAS database TSV file that maps
CHEBI IDs to functional roles. This is a placeholder - adjust based on actual
PFAS data format when available.

Expected TSV format:
    CHEBI_ID    ROLE    CONFIDENCE    SOURCE_DOI    NOTES
    CHEBI:12345 NITROGEN_SOURCE    0.95    10.1234/example    ...
"""

import csv
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator

# Path to PFAS data file (adjust as needed)
PFAS_DATA_FILE = Path("data/external/pfas_role_assignments.tsv")


def parse_pfas_row(row: dict) -> dict | None:
    """Parse a row from PFAS TSV file.

    Args:
        row: Dictionary from csv.DictReader

    Returns:
        Parsed role assignment dict or None if invalid
    """
    chebi_id = row.get("CHEBI_ID", "").strip()
    role = row.get("ROLE", "").strip()
    confidence = row.get("CONFIDENCE", "0.9").strip()
    doi = row.get("SOURCE_DOI", "").strip()
    notes = row.get("NOTES", "").strip()

    if not chebi_id or not role:
        return None

    try:
        confidence = float(confidence)
    except ValueError:
        confidence = 0.9

    return {
        "chebi_id": chebi_id,
        "role": role,
        "confidence": confidence,
        "doi": doi if doi else None,
        "notes": notes,
    }


def find_ingredient_by_chebi(curator: IngredientCurator, chebi_id: str) -> dict | None:
    """Find an ingredient record by CHEBI ID.

    Args:
        curator: IngredientCurator instance
        chebi_id: CHEBI ID to search for (e.g., "CHEBI:12345")

    Returns:
        Ingredient record dict or None if not found
    """
    for record in curator.records:
        mapping = record.get("ontology_mapping")
        if mapping and mapping.get("ontology_id") == chebi_id:
            return record
    return None


def main():
    """Main import workflow."""
    print("=" * 80)
    print("PHASE 2: Import Roles from PFAS Database")
    print("=" * 80)

    # Check if PFAS data file exists
    if not PFAS_DATA_FILE.exists():
        print(f"\n⚠️  PFAS data file not found: {PFAS_DATA_FILE}")
        print("\nThis is expected if PFAS data is not available.")
        print("To use this script:")
        print(f"  1. Place PFAS role assignment data at: {PFAS_DATA_FILE}")
        print("  2. Ensure TSV format with columns: CHEBI_ID, ROLE, CONFIDENCE, SOURCE_DOI, NOTES")
        print("  3. Re-run this script")
        print("\nSkipping Phase 2.")
        return

    # Load mapped ingredients
    curator = IngredientCurator(
        data_path=Path("data/curated/mapped_ingredients.yaml"),
        curator_name="import_pfas_roles",
    )

    print(f"\nLoading ingredient records...")
    curator.load()
    print(f"Loaded {len(curator.records)} records")

    # Parse PFAS data
    print(f"\nParsing PFAS data from {PFAS_DATA_FILE}...")
    roles_added = 0
    ingredients_updated = 0
    skipped = 0
    errors = []

    with open(PFAS_DATA_FILE) as f:
        reader = csv.DictReader(f, delimiter="\t")

        for i, row in enumerate(reader, 1):
            parsed = parse_pfas_row(row)
            if not parsed:
                skipped += 1
                continue

            # Find ingredient
            record = find_ingredient_by_chebi(curator, parsed["chebi_id"])
            if not record:
                skipped += 1
                continue

            # Check if role already exists
            existing_roles = {r.get("role") for r in record.get("media_roles", [])}
            if parsed["role"] in existing_roles:
                skipped += 1
                continue

            # Add role
            try:
                curator.add_media_role(
                    record,
                    role=parsed["role"],
                    confidence=parsed["confidence"],
                    doi=parsed["doi"],
                    reference_type="DATABASE_ENTRY",
                    reference_text="Imported from PFAS database",
                    notes=parsed["notes"],
                )
                roles_added += 1
                if len(record.get("media_roles", [])) == 1:
                    ingredients_updated += 1

            except ValueError as e:
                errors.append(f"Row {i}: {str(e)}")

    # Save results
    if curator.is_dirty:
        print("\nSaving updated records...")
        curator.save()

    # Summary
    print("\n" + "=" * 80)
    print("IMPORT SUMMARY")
    print("=" * 80)
    print(f"PFAS rows processed: {i}")
    print(f"Roles added: {roles_added}")
    print(f"Ingredients updated: {ingredients_updated}")
    print(f"Skipped: {skipped}")

    if errors:
        print(f"\nErrors: {len(errors)}")
        for error in errors[:10]:
            print(f"  • {error}")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more")

    print("\n✅ Phase 2 complete!")


if __name__ == "__main__":
    main()
