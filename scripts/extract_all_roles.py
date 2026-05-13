#!/usr/bin/env python3
"""Extract roles for ALL ingredients with CultureMech role annotations.

This script extends extract_top100_roles.py to process all 570 ingredients
with role annotations, not just the top 100 by occurrence count.

Steps:
1. Re-analyze all ingredients to find role annotations
2. Extract and apply roles for all ingredients without existing roles
3. Report statistics on role coverage improvement

Input: data/curated/mapped_ingredients.yaml
Output: Updated data/curated/mapped_ingredients.yaml
"""

import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import yaml

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator


# Role mapping from CultureMech role text to IngredientRoleEnum
CULTUREMECH_ROLE_MAPPING = {
    "Mineral source": "MINERAL",
    "Buffer": "BUFFER",
    "Nitrogen source": "NITROGEN_SOURCE",
    "Carbon source": "CARBON_SOURCE",
    "Vitamin source": "VITAMIN_SOURCE",
    "Vitamin": "VITAMIN_SOURCE",
    "Protein source": "PROTEIN_SOURCE",
    "Trace element": "TRACE_ELEMENT",
    "Trace metal": "TRACE_ELEMENT",
    "Solvating media": "SALT",
    "Salt": "SALT",
    "Solidifying agent": "SOLIDIFYING_AGENT",
    "Solidifying component": "SOLIDIFYING_AGENT",
    "Energy source": "ENERGY_SOURCE",
    "Electron acceptor": "ELECTRON_ACCEPTOR",
    "Electron donor": "ELECTRON_DONOR",
    "Cofactor": "COFACTOR_PROVIDER",
    "Cofactor provider": "COFACTOR_PROVIDER",
    "Amino acid source": "AMINO_ACID_SOURCE",
    "pH dependent redox indicator": "REDOX_INDICATOR",
    "Redox indicator": "REDOX_INDICATOR",
    "Reducing agent": "REDOX_INDICATOR",
    "pH indicator": "PH_INDICATOR",
    "Antimicrobial agent": "SELECTIVE_AGENT",
    "Selective agent": "SELECTIVE_AGENT",
    "Surfactant": "SURFACTANT",
    "Detergent": "SURFACTANT",
    # Additional mappings for unmapped roles
    "Growth factor": "VITAMIN_SOURCE",  # Growth factors often vitamin-like
    "Nutrient source": "CARBON_SOURCE",  # General nutrient provision
}

# Pattern to match role text in synonyms
ROLE_PATTERN = re.compile(r"Role:\s*([^;]+);?\s*Properties:\s*(.+)")


def parse_role_annotation(text: str) -> Optional[tuple[str, str]]:
    """Parse role annotation from synonym text.

    Args:
        text: Synonym text (e.g., "Role: Mineral source; Properties: ...")

    Returns:
        (role_text, role_enum) tuple, or None if not a role annotation
    """
    match = ROLE_PATTERN.search(text)
    if not match:
        return None

    role_text = match.group(1).strip()

    # Handle multi-role annotations (e.g., "Mineral source, Buffer")
    # Take the first role for now
    if "," in role_text:
        role_text = role_text.split(",")[0].strip()

    # Map to enum
    role_enum = CULTUREMECH_ROLE_MAPPING.get(role_text)

    if not role_enum:
        return None

    return role_text, role_enum


def calculate_confidence(roles: list[tuple[str, str]], properties: list[str]) -> float:
    """Calculate confidence score based on role consistency and properties.

    Args:
        roles: List of (role_text, role_enum) tuples
        properties: List of property strings

    Returns:
        Confidence score (0.0-1.0)
    """
    if not roles:
        return 0.0

    # Check consistency (all roles map to same enum)
    unique_enums = set(r[1] for r in roles)
    if len(unique_enums) == 1:
        base_confidence = 1.0
    else:
        base_confidence = 0.8  # Multiple different roles

    # Check for "Defined component" property (high quality)
    has_defined = any("Defined component" in p for p in properties)
    if has_defined:
        base_confidence = min(1.0, base_confidence + 0.1)

    return base_confidence


def extract_roles_from_synonyms(record: dict) -> Optional[tuple[str, float, list[str]]]:
    """Extract primary role from ingredient synonyms.

    Args:
        record: Ingredient record

    Returns:
        (primary_role_enum, confidence, properties) tuple, or None if no roles found
    """
    synonyms = record.get("synonyms", [])

    roles = []
    properties = []

    for syn in synonyms:
        text = syn.get("synonym_text", "")

        # Parse role annotation
        role_data = parse_role_annotation(text)
        if role_data:
            roles.append(role_data)

            # Extract properties
            match = ROLE_PATTERN.search(text)
            if match:
                props = match.group(2).strip()
                properties.extend([p.strip() for p in props.split(",")])

    if not roles:
        return None

    # Determine primary role (most common)
    role_counts = defaultdict(int)
    for _, role_enum in roles:
        role_counts[role_enum] += 1

    primary_role = max(role_counts.items(), key=lambda x: x[1])[0]
    confidence = calculate_confidence(roles, properties)

    return primary_role, confidence, properties


def ingredient_has_role(record: dict, role_enum: str) -> bool:
    """Check if ingredient already has a specific role.

    Args:
        record: Ingredient record
        role_enum: Role enum value (e.g., "MINERAL")

    Returns:
        True if role already assigned
    """
    for role_assignment in record.get("media_roles", []):
        if role_assignment.get("role") == role_enum:
            return True
    return False


def add_role_to_ingredient(
    curator: IngredientCurator,
    record: dict,
    role_enum: str,
    confidence: float,
    ontology_id: str,
) -> bool:
    """Add a role to an ingredient record.

    Args:
        curator: Ingredient curator instance
        record: Ingredient record
        role_enum: Role enum value
        confidence: Confidence score
        ontology_id: Ontology ID for citation

    Returns:
        True if role was added, False if already exists
    """
    # Check if role already exists
    if ingredient_has_role(record, role_enum):
        return False

    # Create role assignment
    role_assignment = {
        "role": role_enum,
        "confidence": round(confidence, 3),
        "evidence": [
            {
                "evidence_type": "DATABASE_ENTRY",
                "source": "CultureMech",
                "database_id": ontology_id,
            }
        ],
    }

    # Add to media_roles
    if "media_roles" not in record:
        record["media_roles"] = []

    record["media_roles"].append(role_assignment)

    # Add curation event
    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "curator": "extract_all_roles",
        "action": "ROLE_ASSIGNED",
        "changes": f"Assigned role {role_enum} from CultureMech annotations (confidence: {confidence:.2f})",
        "llm_assisted": False,
    }

    if "curation_history" not in record:
        record["curation_history"] = []

    record["curation_history"].append(event)

    return True


def main():
    print("=" * 80)
    print("Extract Roles for ALL Ingredients")
    print("=" * 80)
    print()

    # Load mapped ingredients
    data_path = Path("data/curated/mapped_ingredients.yaml")
    curator = IngredientCurator(data_path=data_path, curator_name="extract_all_roles")

    print(f"Loading ingredient records from: {data_path}")
    curator.load()
    records = curator.records
    print(f"Loaded {len(records)} records")

    # Statistics
    stats = {
        "total_processed": 0,
        "with_role_annotations": 0,
        "already_have_roles": 0,
        "roles_added": 0,
        "ingredients_updated": 0,
    }

    print(f"\nAnalyzing all {len(records)} ingredients for role annotations...")

    # Process all ingredients
    for i, record in enumerate(records, 1):
        if i % 100 == 0:
            print(f"  Processed {i}/{len(records)} ingredients...")

        stats["total_processed"] += 1

        # Extract roles from synonyms
        role_data = extract_roles_from_synonyms(record)

        if not role_data:
            continue

        stats["with_role_annotations"] += 1
        primary_role, confidence, properties = role_data

        # Check if already has this role
        if ingredient_has_role(record, primary_role):
            stats["already_have_roles"] += 1
            continue

        # Add role
        ontology_id = record.get("ontology_id", "")
        success = add_role_to_ingredient(
            curator, record, primary_role, confidence, ontology_id
        )

        if success:
            stats["roles_added"] += 1
            stats["ingredients_updated"] += 1

    # Save updated records
    print("\nSaving updated records...")
    curator.save()
    print(f"✅ Saved to {data_path}")

    # Report statistics
    print("\n" + "=" * 80)
    print("EXTRACTION SUMMARY")
    print("=" * 80)
    print(f"Total ingredients processed: {stats['total_processed']}")
    print(f"Ingredients with role annotations: {stats['with_role_annotations']}")
    print(f"  - Already had roles: {stats['already_have_roles']}")
    print(f"  - Roles added: {stats['roles_added']}")
    print(f"Ingredients updated: {stats['ingredients_updated']}")
    print()

    # Calculate coverage
    total_with_roles = stats["already_have_roles"] + stats["ingredients_updated"]
    coverage_pct = (total_with_roles / stats["total_processed"]) * 100

    print(f"Final role coverage: {total_with_roles}/{stats['total_processed']} ({coverage_pct:.1f}%)")
    print()
    print("✅ All roles extraction complete!")


if __name__ == "__main__":
    main()
