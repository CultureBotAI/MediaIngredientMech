#!/usr/bin/env python3
"""Map the final 2 ingredients from OTHER category."""

import sys
from datetime import datetime, timezone
from pathlib import Path
import yaml

from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.utils.yaml_handler import save_yaml
from mediaingredientmech.validation.write_validated import ValidationFailedError

# Paths
DATA_DIR = Path(__file__).parent.parent / "data" / "curated"
UNMAPPED_PATH = DATA_DIR / "unmapped_ingredients.yaml"
MAPPED_PATH = DATA_DIR / "mapped_ingredients.yaml"

TIMESTAMP = datetime.now(timezone.utc).isoformat()

# Final 2 mappings
FINAL_MAPPINGS = [
    {
        "preferred_term": "Trizma Base pH",
        "ontology_id": "CHEBI:9754",
        "ontology_label": "Trizma base",
        "ontology_source": "CHEBI",
        "quality": "CLOSE_MATCH",
        "match_level": "NORMALIZED",
        "confidence": 0.90,
        "reasoning": "Trizma Base pH is Tris buffer adjusted to specific pH. CLOSE_MATCH (not EXACT) because 'pH' suffix indicates pH-adjusted preparation, not pure Trizma base. Maps to CHEBI:9754 (Trizma base = Tris).",
    },
    {
        "preferred_term": "FE EDTA",
        "ontology_id": "CHEBI:28937",
        "ontology_label": "Fe-EDTA",
        "ontology_source": "CHEBI",
        "quality": "CLOSE_MATCH",
        "match_level": "NORMALIZED",
        "confidence": 0.90,
        "reasoning": "FE EDTA is iron-EDTA chelate complex. CLOSE_MATCH because uppercase 'FE' notation and lack of oxidation state specification. CHEBI:28937 covers iron-EDTA chelate complexes.",
    },
]


def load_yaml(path):
    """Load YAML file."""
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def map_ingredient(record, mapping):
    """Apply mapping to ingredient record."""
    # Update core fields
    record["identifier"] = mapping["ontology_id"]
    record.pop("ontology_id", None)  # drop any stale legacy root key
    record["mapping_status"] = "MAPPED"

    # Add ontology mapping
    record["ontology_mapping"] = {
        "ontology_id": mapping["ontology_id"],
        "ontology_label": mapping["ontology_label"],
        "ontology_source": mapping["ontology_source"],
        "mapping_quality": mapping["quality"],
        "match_level": mapping["match_level"],
        "evidence": [
            {
                "evidence_type": "MANUAL_CURATION",
                "curator": "map_final_two",
                "confidence_score": mapping["confidence"],
                "notes": mapping["reasoning"],
                "timestamp": TIMESTAMP,
            }
        ],
    }

    # Add curation event
    record_curation_event(
        record,
        curator="map_final_two",
        action="MAPPED",
        changes=f"Mapped to {mapping['ontology_id']} ({mapping['ontology_label']})",
    )

    return record


def main():
    """Map final 2 ingredients."""
    print("=" * 80)
    print("MAP FINAL 2 INGREDIENTS")
    print("=" * 80)
    print()

    # Load files
    print("Loading data files...")
    unmapped_data = load_yaml(UNMAPPED_PATH)
    mapped_data = load_yaml(MAPPED_PATH)

    unmapped_ingredients = unmapped_data["ingredients"]
    mapped_ingredients = mapped_data["ingredients"]

    print(f"  Unmapped: {len(unmapped_ingredients)} ingredients")
    print(f"  Mapped: {len(mapped_ingredients)} ingredients")
    print()

    # Process mappings
    mapped_count = 0

    for mapping in FINAL_MAPPINGS:
        term = mapping["preferred_term"]
        print(f"Mapping: {term}")
        print(f"  → {mapping['ontology_id']}: {mapping['ontology_label']}")
        print(f"  Quality: {mapping['quality']}, Match: {mapping['match_level']}")
        print(f"  Confidence: {mapping['confidence']}")

        # Find ingredient in unmapped
        found = False
        for i, record in enumerate(unmapped_ingredients):
            if record["preferred_term"] == term:
                # Apply mapping
                mapped_record = map_ingredient(record, mapping)

                # Move to mapped
                mapped_ingredients.append(mapped_record)
                del unmapped_ingredients[i]

                mapped_count += 1
                found = True
                print(f"  ✓ Mapped and moved to mapped_ingredients.yaml")
                break

        if not found:
            print(f"  ⚠️ Not found in unmapped ingredients")

        print()

    # Update counts
    unmapped_data["total_count"] = len(unmapped_ingredients)
    unmapped_data["unmapped_count"] = len(unmapped_ingredients)
    mapped_data["total_count"] = len(mapped_ingredients)

    # Save files
    print("Saving updated files...")
    try:
        save_yaml(unmapped_data, UNMAPPED_PATH, validate=True, target_class="IngredientCollection")
        save_yaml(mapped_data, MAPPED_PATH, validate=True, target_class="IngredientCollection")
    except ValidationFailedError as exc:
        print(f"  ✗ validation failed: refusing to write", file=sys.stderr)
        print(exc.summary(), file=sys.stderr)
        raise
    print(f"  ✓ Saved {UNMAPPED_PATH}")
    print(f"  ✓ Saved {MAPPED_PATH}")
    print()

    # Summary
    print("=" * 80)
    print("FINAL MAPPING COMPLETE")
    print("=" * 80)
    print(f"Mapped: {mapped_count} ingredients")
    print(f"Total mapped: {len(mapped_ingredients)}")
    print(f"Total unmapped: {len(unmapped_ingredients)}")
    print()

    if len(unmapped_ingredients) == 68:
        print("🎉 SUCCESS! Only intentionally unmappable ingredients remain!")
        print()
        print("Remaining unmapped breakdown:")
        print("  - Complex media: 61 (intentionally unmappable)")
        print("  - Placeholders: 7 (reference markers)")
        print("  - Total: 68 (100% have definitive status)")
        print()
        print("✅ ALL MAPPABLE INGREDIENTS HAVE BEEN MAPPED!")
    else:
        print(f"⚠️ {len(unmapped_ingredients)} unmapped remain")

    print()


if __name__ == "__main__":
    main()
