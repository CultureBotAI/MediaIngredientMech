#!/usr/bin/env python3
"""Enrich MediaIngredientMech with role annotations from CultureMech concentration_info.

This script extracts role annotations from CultureMech's concentration_info[].notes
field and adds them as synonyms to the corresponding MediaIngredientMech ingredients.

This addresses the ~1,006 missing role annotations that were not imported during
the original CultureMech import (which only extracted from the synonyms field).

Usage:
    python scripts/enrich_with_concentration_notes.py [--dry-run]
"""

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


# Paths
CULTUREMECH_DIR = Path(
    "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech/output"
)
MI_DATA_DIR = Path(
    "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/MediaIngredientMech/data/curated"
)

TIMESTAMP = datetime.now(timezone.utc).isoformat()


def load_yaml(path: Path) -> dict:
    """Load a YAML file."""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def save_yaml(data: dict, path: Path):
    """Save data to YAML file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)


def normalize_term(term: str) -> str:
    """Normalize an ingredient term for matching."""
    normalized = term.lower().strip()
    # Normalize hydrate separators
    normalized = re.sub(r"[•·×*]\s*", "x", normalized)
    normalized = re.sub(r"\s+", " ", normalized)
    return normalized


def extract_concentration_notes(cm_ingredient: dict) -> list[str]:
    """Extract role annotations from concentration_info notes.

    Args:
        cm_ingredient: CultureMech ingredient dictionary

    Returns:
        List of unique role annotation strings
    """
    conc_info = cm_ingredient.get("concentration_info", [])
    if not conc_info:
        return []

    seen = set()
    notes = []

    for entry in conc_info:
        note = entry.get("notes", "").strip()

        # Skip empty notes or merge annotations
        if not note or note.startswith("[Merged"):
            continue

        # Only extract notes that contain role annotations
        if "Role:" not in note:
            continue

        # Avoid duplicates
        if note in seen:
            continue

        seen.add(note)
        notes.append(note)

    return notes


def enrich_ingredient(mi_record: dict, cm_ingredient: dict) -> int:
    """Add concentration_info role annotations to MI ingredient.

    Args:
        mi_record: MediaIngredientMech ingredient record
        cm_ingredient: CultureMech ingredient dictionary

    Returns:
        Number of new synonyms added
    """
    # Extract concentration notes from CultureMech
    conc_notes = extract_concentration_notes(cm_ingredient)

    if not conc_notes:
        return 0

    # Get existing synonym texts
    existing_synonyms = mi_record.get("synonyms", [])
    existing_texts = {s.get("synonym_text", "") for s in existing_synonyms}

    # Add new synonyms that don't already exist
    new_count = 0
    for note in conc_notes:
        if note not in existing_texts:
            mi_record.setdefault("synonyms", []).append(
                {
                    "synonym_text": note,
                    "synonym_type": "RAW_TEXT",
                    "source": "CultureMech",
                }
            )
            existing_texts.add(note)
            new_count += 1

    # Add curation event if synonyms were added
    if new_count > 0:
        event = {
            "timestamp": TIMESTAMP,
            "curator": "enrich_with_concentration_notes",
            "action": "SYNONYMS_ENRICHED",
            "changes": f"Added {new_count} role annotations from CultureMech concentration_info",
            "llm_assisted": False,
        }
        mi_record.setdefault("curation_history", []).append(event)

    return new_count


def perform_enrichment(dry_run: bool = False) -> dict:
    """Perform the enrichment.

    Returns:
        Statistics dictionary
    """
    print("="*80)
    print("ENRICH WITH CONCENTRATION_INFO ROLE ANNOTATIONS")
    print("="*80)
    print()

    # Load CultureMech mapped ingredients
    print("Loading CultureMech data...")
    cm_path = CULTUREMECH_DIR / "mapped_ingredients.yaml"
    cm_data = load_yaml(cm_path)
    cm_ingredients = cm_data.get("mapped_ingredients", [])
    print(f"  Loaded {len(cm_ingredients)} ingredients from CultureMech")

    # Load MediaIngredientMech mapped ingredients
    print("\nLoading MediaIngredientMech data...")
    mi_path = MI_DATA_DIR / "mapped_ingredients.yaml"
    mi_data = load_yaml(mi_path)
    mi_ingredients = mi_data.get("ingredients", [])
    print(f"  Loaded {len(mi_ingredients)} ingredients from MI")

    # Build CM index
    print("\nBuilding CultureMech index...")
    cm_index = {}
    cm_norm_index = {}
    for cm_ing in cm_ingredients:
        term = cm_ing.get("preferred_term", "")
        if term:
            cm_index[term] = cm_ing
            cm_norm_index[normalize_term(term)] = cm_ing

    # Count role annotations before
    role_count_before = sum(
        1 for ing in mi_ingredients
        for syn in ing.get("synonyms", [])
        if "Role:" in syn.get("synonym_text", "")
    )

    # Statistics
    stats = {
        "ingredients_processed": 0,
        "ingredients_enriched": 0,
        "synonyms_added": 0,
        "ingredients_with_conc_notes": 0,
    }

    print("\nEnriching ingredients with concentration_info notes...")

    # Process MI ingredients
    for mi_ing in mi_ingredients:
        term = mi_ing.get("preferred_term", "")
        if not term:
            continue

        stats["ingredients_processed"] += 1

        # Find matching CM ingredient
        cm_ing = cm_index.get(term) or cm_norm_index.get(normalize_term(term))

        if not cm_ing:
            continue

        # Check if CM ingredient has concentration notes
        if not cm_ing.get("concentration_info"):
            continue

        stats["ingredients_with_conc_notes"] += 1

        # Enrich with concentration notes
        new_count = enrich_ingredient(mi_ing, cm_ing)

        if new_count > 0:
            stats["ingredients_enriched"] += 1
            stats["synonyms_added"] += new_count

        if stats["ingredients_processed"] % 100 == 0:
            print(f"  Processed {stats['ingredients_processed']}/{len(mi_ingredients)} ingredients...")

    # Count role annotations after
    role_count_after = sum(
        1 for ing in mi_ingredients
        for syn in ing.get("synonyms", [])
        if "Role:" in syn.get("synonym_text", "")
    )

    # Save if not dry-run
    if not dry_run:
        print("\nSaving enriched data...")
        save_yaml(mi_data, mi_path)
        print(f"✅ Saved to {mi_path}")
    else:
        print("\n[DRY RUN] No files written.")

    # Report statistics
    print("\n" + "="*80)
    print("ENRICHMENT SUMMARY")
    print("="*80)
    print(f"Ingredients processed: {stats['ingredients_processed']}")
    print(f"Ingredients with concentration_info: {stats['ingredients_with_conc_notes']}")
    print(f"Ingredients enriched: {stats['ingredients_enriched']}")
    print(f"Synonyms added: {stats['synonyms_added']}")
    print()
    print(f"Role annotations before: {role_count_before}")
    print(f"Role annotations after:  {role_count_after}")
    print(f"Increase: +{role_count_after - role_count_before} ({((role_count_after - role_count_before) / role_count_before * 100):.1f}%)")
    print()

    if not dry_run:
        print("✅ Enrichment complete!")
        print("\nNext steps:")
        print("  1. Re-run role extraction: PYTHONPATH=src python scripts/extract_all_roles.py")
        print("  2. Generate statistics: PYTHONPATH=src python scripts/generate_role_statistics.py")
    else:
        print("[DRY RUN] Run without --dry-run to apply changes.")

    return stats


def main():
    parser = argparse.ArgumentParser(
        description="Enrich MI with role annotations from CultureMech concentration_info"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without saving"
    )
    args = parser.parse_args()

    stats = perform_enrichment(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
