#!/usr/bin/env python3
"""Extract role information from RAW_TEXT synonyms and populate the role facets.

This script parses synonym text like:
  "Role: Mineral source; Properties: Defined component, Inorganic compound"

And converts them to structured role assignments on the nutritional /
physicochemical / cellular-metabolic facet that owns each role.
"""

import re
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator
from mediaingredientmech.utils.role_facets import add_role
from mediaingredientmech.utils.role_iteration import FACET_ROLE_SLOTS, iter_role_assignments

# Mapping from CultureMech role text to facet role values.
# "Salt" and "Solvating media" are deliberately absent: upstream they tag water,
# acids and solvents indiscriminately, so they carry no usable role.
ROLE_MAPPING = {
    # No facet has a generic mineral role; "Mineral source" is a catch-all whose
    # element is not recoverable from the text, so it lands in the residual bucket.
    "Mineral source": "MINERAL_SOURCE",
    "Buffer": "BUFFER",
    "Nitrogen source": "NITROGEN_SOURCE",
    "Carbon source": "CARBON_SOURCE",
    "Vitamin source": "VITAMIN_SOURCE",
    "Protein source": "PROTEIN_SOURCE",
    "Trace element": "TRACE_ELEMENT",
    "Solidifying agent": "SOLIDIFYING_AGENT",
    "Energy source": "ENERGY_SOURCE",
    "Electron acceptor": "ELECTRON_ACCEPTOR",
    "Electron donor": "ELECTRON_DONOR",
    "Cofactor": "COFACTOR_PROVIDER",
    "Amino acid source": "AMINO_ACID_SOURCE",
    # Additional unambiguous CultureMech role texts with valid facet role targets.
    # (Heterogeneous texts like "Growth factor" / "Nutrient source" are intentionally
    # omitted because they map to no single role.)
    "Vitamin": "VITAMIN_SOURCE",
    "pH indicator": "PH_INDICATOR",
    "pH dependent redox indicator": "REDOX_INDICATOR",
    "Redox indicator": "REDOX_INDICATOR",
    "Solidifying component": "SOLIDIFYING_AGENT",
    "Surfactant": "SURFACTANT",
    "Antimicrobial agent": "SELECTIVE_AGENT",
    "Selective agent": "SELECTIVE_AGENT",
    "Reducing agent": "REDUCING_AGENT",
    "Chelating agent": "CHELATOR",
    "Chelator": "CHELATOR",
}

# Pattern to match role text in synonyms
ROLE_PATTERN = re.compile(r"Role:\s*([^;]+);?\s*Properties:\s*(.+)")


def extract_role_from_synonym(synonym_text: str) -> tuple[list[str], list[str]]:
    """Extract role(s) and properties from a synonym text.

    Handles compound role texts (comma-separated), e.g.
    "Role: Buffer, Mineral source; Properties: ..." maps to both BUFFER and
    MINERAL_SOURCE.

    Args:
        synonym_text: Text like "Role: Mineral source; Properties: Defined component, ..."

    Returns:
        Tuple of (role_enum_values, properties_list). role_enum_values is empty
        if there is no match or no component maps to a known enum value.
    """
    match = ROLE_PATTERN.match(synonym_text)
    if not match:
        return [], []

    role_text = match.group(1).strip()
    properties_text = match.group(2).strip()

    # A single "Role:" field may list several comma-separated roles; map each.
    role_enums = []
    for part in role_text.split(","):
        role_enum = ROLE_MAPPING.get(part.strip())
        if role_enum and role_enum not in role_enums:
            role_enums.append(role_enum)

    # Parse properties
    properties = [p.strip() for p in properties_text.split(",")]

    return role_enums, properties


def should_skip_ingredient(record: dict) -> bool:
    """Check if ingredient should be skipped.

    Only unmapped ingredients are skipped. Records that already have
    facet roles are still processed: extraction is additive and idempotent
    (existing roles are deduped against in extract_roles_for_ingredient), so
    re-running picks up newly-mappable roles without duplicating prior ones.
    """
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

    # Seed with roles already on the record so re-runs stay idempotent and
    # never add a duplicate of an existing assignment.
    roles_added = {
        ra.get("role")
        for _slot, ra in iter_role_assignments(record, slots=FACET_ROLE_SLOTS)
        if ra.get("role")
    }
    preexisting = len(roles_added)

    # Process all RAW_TEXT synonyms
    for synonym in record.get("synonyms", []):
        if synonym.get("synonym_type") != "RAW_TEXT":
            continue

        synonym_text = synonym.get("synonym_text", "")
        role_enums, properties = extract_role_from_synonym(synonym_text)

        for role_enum in role_enums:
            if role_enum in roles_added:
                continue

            # Determine confidence based on properties
            confidence = 1.0 if "Defined component" in properties else 0.9

            # Add the role with DATABASE_ENTRY citation (from CultureMech)
            add_role(
                curator,
                record,
                role_enum,
                confidence=confidence,
                reference_text="Imported from CultureMech pipeline",
                reference_type="DATABASE_ENTRY",
                curator_note=f"Original role text: {role_enum.replace('_', ' ').title()}",
            )

            roles_added.add(role_enum)

    return len(roles_added) - preexisting


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
            for _slot, role_assignment in iter_role_assignments(
                record, slots=FACET_ROLE_SLOTS
            ):
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
