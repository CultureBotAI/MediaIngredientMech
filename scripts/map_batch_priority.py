#!/usr/bin/env python3
"""Map high-priority unmapped ingredients from curation list."""

from datetime import datetime, timezone
from pathlib import Path
import yaml

# Paths
DATA_DIR = Path(__file__).parent.parent / "data" / "curated"
UNMAPPED_PATH = DATA_DIR / "unmapped_ingredients.yaml"
MAPPED_PATH = DATA_DIR / "mapped_ingredients.yaml"

TIMESTAMP = datetime.now(timezone.utc).isoformat()

# Mappings to apply - Batch 2
MAPPINGS = [
    {
        "preferred_term": "Glycylglycine",
        "ontology_id": "CHEBI:73998",
        "ontology_label": "glycylglycine",
        "ontology_source": "CHEBI",
        "quality": "EXACT_MATCH",
        "match_level": "EXACT",
        "reasoning": "Glycylglycine (CAS: 556-50-3) is a dipeptide. CHEBI:73998 is the exact match for this compound.",
    },
    {
        "preferred_term": "Na2HPO4•7H2O",
        "ontology_id": "CHEBI:34702",
        "ontology_label": "disodium hydrogen phosphate heptahydrate",
        "ontology_source": "CHEBI",
        "quality": "EXACT_MATCH",
        "match_level": "EXACT",
        "reasoning": "Na2HPO4•7H2O is the chemical formula for disodium hydrogen phosphate heptahydrate. CHEBI:34702 is the exact match.",
    },
    {
        "preferred_term": "Pea",
        "ontology_id": "FOODON:00002753",
        "ontology_label": "pea seed",
        "ontology_source": "FOODON",
        "quality": "CLOSE_MATCH",
        "match_level": "EXACT",
        "reasoning": "Pea used in media typically refers to pea seeds or pea grains. CLOSE_MATCH because the ingredient may be whole seeds, flour, or other pea-derived preparation.",
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
                "curator": "map_batch_priority",
                "confidence_score": 0.95,
                "notes": mapping["reasoning"],
                "timestamp": TIMESTAMP,
            }
        ],
    }

    # Add curation event
    record.setdefault("curation_history", []).append({
        "timestamp": TIMESTAMP,
        "curator": "map_batch_priority",
        "action": "MAPPED",
        "changes": f"Mapped to {mapping['ontology_id']} ({mapping['ontology_label']})",
        "llm_assisted": False,
    })

    return record


def main():
    """Map batch of priority ingredients."""
    print("=" * 80)
    print("MAP BATCH PRIORITY INGREDIENTS")
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
            print(f"  ⚠️ Not found in unmapped ingredients (may already be mapped)")

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
    print("BATCH MAPPING COMPLETE")
    print("=" * 80)
    print(f"Mapped: {mapped_count} ingredients")
    print(f"Total mapped: {len(mapped_ingredients)}")
    print(f"Total unmapped: {len(unmapped_ingredients)}")
    print()


if __name__ == "__main__":
    main()
