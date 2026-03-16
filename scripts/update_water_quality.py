#!/usr/bin/env python3
"""Update mapping quality for dH2O variants to CLOSE_MATCH."""

from datetime import datetime, timezone
from pathlib import Path
import yaml

# Paths
DATA_DIR = Path(__file__).parent.parent / "data" / "curated"
MAPPED_PATH = DATA_DIR / "mapped_ingredients.yaml"

TIMESTAMP = datetime.now(timezone.utc).isoformat()


def load_yaml(path):
    """Load YAML file."""
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def save_yaml(data, path):
    """Save YAML file."""
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)


def update_water_quality():
    """Update dH2O and sterile dH2O mapping quality to CLOSE_MATCH."""
    print("=" * 80)
    print("UPDATE WATER MAPPING QUALITY")
    print("=" * 80)
    print()

    # Load mapped ingredients
    print("Loading mapped_ingredients.yaml...")
    data = load_yaml(MAPPED_PATH)
    ingredients = data["ingredients"]
    print(f"  Loaded {len(ingredients)} ingredients")
    print()

    # Find and update dH2O variants
    updated_count = 0
    water_terms = ["dH2O", "sterile dH2O"]

    for term in water_terms:
        print(f"Updating: {term}")

        for record in ingredients:
            if record["preferred_term"] == term:
                # Update mapping quality
                old_quality = record["ontology_mapping"]["mapping_quality"]
                record["ontology_mapping"]["mapping_quality"] = "CLOSE_MATCH"

                # Update evidence notes
                for evidence in record["ontology_mapping"]["evidence"]:
                    evidence["notes"] = (
                        f"{term} is an abbreviation for distilled water. "
                        "CLOSE_MATCH (not EXACT_MATCH) because distilled water is purified H2O "
                        "with minerals removed, not generic water. Purity level matters for "
                        "microbiological media - some organisms are sensitive to trace minerals. "
                        "Similar to natural sea-salt → NaCl (contains trace minerals)."
                    )
                    evidence["confidence_score"] = 0.85  # Slightly lower due to purity distinction

                # Add curation event
                record.setdefault("curation_history", []).append({
                    "timestamp": TIMESTAMP,
                    "curator": "update_water_quality",
                    "action": "QUALITY_UPDATE",
                    "changes": f"Updated mapping quality from {old_quality} to CLOSE_MATCH to reflect purity distinction",
                    "llm_assisted": False,
                })

                print(f"  ✓ Updated quality: {old_quality} → CLOSE_MATCH")
                updated_count += 1
                break

        print()

    # Save
    print("Saving updated file...")
    save_yaml(data, MAPPED_PATH)
    print(f"  ✓ Saved {MAPPED_PATH}")
    print()

    # Summary
    print("=" * 80)
    print("UPDATE COMPLETE")
    print("=" * 80)
    print(f"Updated {updated_count} ingredients")
    print()


if __name__ == "__main__":
    update_water_quality()
