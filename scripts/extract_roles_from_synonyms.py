#!/usr/bin/env python3
"""Extract role information from RAW_TEXT synonyms and populate media_roles field.

This script parses synonym text like:
  "Role: Mineral source; Properties: Defined component, Inorganic compound"

And converts them to structured RoleAssignment objects with appropriate enum values.
"""

import re
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator

# Mapping from CultureMech role text to IngredientRoleEnum values
ROLE_MAPPING = {
    "Mineral source": "MINERAL",
    "Buffer": "BUFFER",
    "Nitrogen source": "NITROGEN_SOURCE",
    "Carbon source": "CARBON_SOURCE",
    "Vitamin source": "VITAMIN_SOURCE",
    "Protein source": "PROTEIN_SOURCE",
    "Trace element": "TRACE_ELEMENT",
    "Solvating media": "SALT",  # Contextual mapping - water and salts
    "Salt": "SALT",
    "Solidifying agent": "SOLIDIFYING_AGENT",
    "Energy source": "ENERGY_SOURCE",
    "Electron acceptor": "ELECTRON_ACCEPTOR",
    "Electron donor": "ELECTRON_DONOR",
    "Cofactor": "COFACTOR_PROVIDER",
    "Amino acid source": "AMINO_ACID_SOURCE",
}

# Pattern to match role text in synonyms
ROLE_PATTERN = re.compile(r"Role:\s*([^;]+);?\s*Properties:\s*(.+)")


def extract_role_from_synonym(synonym_text: str) -> tuple[str | None, list[str]]:
    """Extract role and properties from a synonym text.

    Args:
        synonym_text: Text like "Role: Mineral source; Properties: Defined component, ..."

    Returns:
        Tuple of (role_enum_value, properties_list) or (None, []) if no match
    """
    match = ROLE_PATTERN.match(synonym_text)
    if not match:
        return None, []

    role_text = match.group(1).strip()
    properties_text = match.group(2).strip()

    # Map to enum value
    role_enum = ROLE_MAPPING.get(role_text)

    # Parse properties
    properties = [p.strip() for p in properties_text.split(",")]

    return role_enum, properties


def should_skip_ingredient(record: dict) -> bool:
    """Check if ingredient already has media_roles or should be skipped."""
    # Skip if already has roles
    if record.get("media_roles"):
        return True

    # Skip unmapped ingredients (we'll handle them separately)
    if record.get("mapping_status") != "MAPPED":
        return True

    return False


def extract_roles_for_ingredient(curator: IngredientCurator, record: dict) -> int:
    """Extract roles from synonyms and add to record.

    Args:
        curator: IngredientCurator instance
        record: Ingredient record to update

    Returns:
        Number of roles added
    """
    if should_skip_ingredient(record):
        return 0

    roles_added = set()  # Track unique roles to avoid duplicates

    # Process all RAW_TEXT synonyms
    for synonym in record.get("synonyms", []):
        if synonym.get("synonym_type") != "RAW_TEXT":
            continue

        synonym_text = synonym.get("synonym_text", "")
        role_enum, properties = extract_role_from_synonym(synonym_text)

        if role_enum and role_enum not in roles_added:
            # Determine confidence based on properties
            confidence = 1.0 if "Defined component" in properties else 0.9

            # Add the role with DATABASE_ENTRY citation (from CultureMech)
            curator.add_media_role(
                record,
                role=role_enum,
                confidence=confidence,
                reference_text="Imported from CultureMech pipeline",
                reference_type="DATABASE_ENTRY",
                curator_note=f"Original role text: {role_enum.replace('_', ' ').title()}",
            )

            roles_added.add(role_enum)

    return len(roles_added)


def main():
    """Main extraction workflow."""
    print("=" * 80)
    print("PHASE 1: Extract Roles from RAW_TEXT Synonyms")
    print("=" * 80)

    # Load mapped ingredients
    curator = IngredientCurator(
        data_path=Path("data/curated/mapped_ingredients.yaml"),
        curator_name="extract_roles_from_synonyms",
    )

    print("\nLoading ingredient records...")
    curator.load()
    total_records = len(curator.records)
    print(f"Loaded {total_records} records")

    # Extract roles
    print("\nExtracting roles from synonyms...")
    total_roles_added = 0
    ingredients_updated = 0
    role_counts = {}

    for i, record in enumerate(curator.records, 1):
        if i % 100 == 0:
            print(f"  Processed {i}/{total_records} ingredients...")

        roles_added = extract_roles_for_ingredient(curator, record)
        if roles_added > 0:
            ingredients_updated += 1
            total_roles_added += roles_added

            # Count role types
            for role_assignment in record.get("media_roles", []):
                role = role_assignment.get("role")
                role_counts[role] = role_counts.get(role, 0) + 1

    # Save results
    print("\nSaving updated records...")
    curator.save()

    # Summary statistics
    print("\n" + "=" * 80)
    print("EXTRACTION SUMMARY")
    print("=" * 80)
    print(f"Total ingredients: {total_records}")
    print(f"Ingredients updated: {ingredients_updated} ({ingredients_updated/total_records*100:.1f}%)")
    print(f"Total roles added: {total_roles_added}")
    print(f"Average roles per ingredient: {total_roles_added/ingredients_updated:.2f}")

    print("\nRole distribution:")
    for role, count in sorted(role_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {role:25s}: {count:4d}")

    print("\n✅ Phase 1 complete! Roles extracted from synonyms.")


if __name__ == "__main__":
    main()
