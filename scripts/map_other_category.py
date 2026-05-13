#!/usr/bin/env python3
"""Map the 5 mappable ingredients from OTHER category."""

from datetime import datetime, timezone
from pathlib import Path
import yaml

# Paths
DATA_DIR = Path(__file__).parent.parent / "data" / "curated"
UNMAPPED_PATH = DATA_DIR / "unmapped_ingredients.yaml"
MAPPED_PATH = DATA_DIR / "mapped_ingredients.yaml"

TIMESTAMP = datetime.now(timezone.utc).isoformat()

# Mappings for the 5 clearly mappable ingredients
MAPPINGS = [
    {
        "preferred_term": "Tricine",
        "ontology_id": "CHEBI:16325",
        "ontology_label": "tricine",
        "ontology_source": "CHEBI",
        "quality": "EXACT_MATCH",
        "match_level": "EXACT",
        "reasoning": "Tricine (N-[2-hydroxy-1,1-bis(hydroxymethyl)ethyl]glycine) is a buffering agent. CHEBI:16325 is the exact match for this compound.",
    },
    {
        "preferred_term": "Sodium Metasilicate",
        "ontology_id": "CHEBI:86314",
        "ontology_label": "sodium metasilicate",
        "ontology_source": "CHEBI",
        "quality": "EXACT_MATCH",
        "match_level": "EXACT",
        "reasoning": "Sodium metasilicate (Na2SiO3) is a chemical compound. CHEBI:86314 is the exact match.",
    },
    {
        "preferred_term": "TES buffer",
        "ontology_id": "CHEBI:9330",
        "ontology_label": "TES",
        "ontology_source": "CHEBI",
        "quality": "EXACT_MATCH",
        "match_level": "NORMALIZED",
        "reasoning": "TES buffer is N-[tris(hydroxymethyl)methyl]-2-aminoethanesulfonic acid, a common biological buffer. CHEBI:9330 is the exact match. NORMALIZED match level because 'buffer' suffix was removed.",
    },
    {
        "preferred_term": "Barley grains",
        "ontology_id": "FOODON:00002737",
        "ontology_label": "barley grain",
        "ontology_source": "FOODON",
        "quality": "EXACT_MATCH",
        "match_level": "EXACT",
        "reasoning": "Barley grains are cereal grains used as a substrate in some microbial media. FOODON:00002737 is the exact match for barley grain.",
    },
    {
        "preferred_term": "Barley grains autoclaved",
        "ontology_id": "FOODON:00002737",
        "ontology_label": "barley grain",
        "ontology_source": "FOODON",
        "quality": "CLOSE_MATCH",
        "match_level": "NORMALIZED",
        "reasoning": "Autoclaved barley grains are sterilized barley grains. CLOSE_MATCH (not EXACT) because autoclaving is a preparation step that modifies the grain. Maps to the same FOODON term as base ingredient.",
    },
]


def load_yaml(path):
    """Load YAML file."""
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def save_yaml(data, path):
    """Save YAML file."""
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)


def map_ingredient(record, mapping):
    """Apply mapping to ingredient record."""
    # Update core fields
    record["ontology_id"] = mapping["ontology_id"]
    record["identifier"] = mapping["ontology_id"]
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
                "curator": "map_other_category",
                "confidence_score": 0.95,
                "notes": mapping["reasoning"],
                "timestamp": TIMESTAMP,
            }
        ],
    }

    # Add curation event
    record.setdefault("curation_history", []).append({
        "timestamp": TIMESTAMP,
        "curator": "map_other_category",
        "action": "MAPPED",
        "changes": f"Mapped to {mapping['ontology_id']} ({mapping['ontology_label']})",
        "llm_assisted": False,
    })

    return record


def main():
    """Map OTHER category mappable ingredients."""
    print("=" * 80)
    print("MAP OTHER CATEGORY - MAPPABLE INGREDIENTS")
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

    for mapping in MAPPINGS:
        term = mapping["preferred_term"]
        print(f"Mapping: {term}")
        print(f"  → {mapping['ontology_id']}: {mapping['ontology_label']}")
        print(f"  Quality: {mapping['quality']}, Match: {mapping['match_level']}")

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
    save_yaml(unmapped_data, UNMAPPED_PATH)
    save_yaml(mapped_data, MAPPED_PATH)
    print(f"  ✓ Saved {UNMAPPED_PATH}")
    print(f"  ✓ Saved {MAPPED_PATH}")
    print()

    # Summary
    print("=" * 80)
    print("MAPPING COMPLETE")
    print("=" * 80)
    print(f"Mapped: {mapped_count} ingredients")
    print(f"Total mapped: {len(mapped_ingredients)}")
    print(f"Total unmapped: {len(unmapped_ingredients)}")
    print()
    print("Remaining in OTHER category:")
    print("  - Trizma Base pH (expert review needed)")
    print("  - FE EDTA (expert review needed)")
    print()


if __name__ == "__main__":
    main()
