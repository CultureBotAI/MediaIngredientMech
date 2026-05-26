#!/usr/bin/env python3
"""Prepare unmapped ingredients for curation.

This script:
1. Imports unmapped ingredients from CultureMech
2. Removes ingredients that are already mapped in MediaIngredientMech
3. Categorizes unmapped ingredients (placeholders, complex media, truly unmapped)
4. Prioritizes by occurrence count for curation
5. Generates a clean unmapped_ingredients.yaml ready for curation

Usage:
    python scripts/prepare_unmapped_for_curation.py
"""

import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.utils.yaml_handler import save_yaml
from mediaingredientmech.validation.write_validated import ValidationFailedError


# Default paths are relative to the repo root (this script lives in
# `<repo>/scripts/`). Override the sibling CultureMech location with the
# CULTUREMECH_DIR env var when running outside the standard sibling-checkout
# layout.
_REPO_ROOT = Path(__file__).resolve().parents[1]
CULTUREMECH_DIR = Path(
    os.environ.get(
        "CULTUREMECH_DIR",
        str((_REPO_ROOT.parent / "CultureMech" / "output").resolve()),
    )
)
MI_DATA_DIR = _REPO_ROOT / "data" / "curated"

TIMESTAMP = datetime.now(timezone.utc).isoformat()


def load_yaml(path: Path) -> dict:
    """Load a YAML file."""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def normalize_term(term: str) -> str:
    """Normalize an ingredient term for matching."""
    normalized = term.lower().strip()
    normalized = re.sub(r"[•·×*]\s*", "x", normalized)
    normalized = re.sub(r"\s+", " ", normalized)
    return normalized


def categorize_unmapped(parsed_name: str) -> str:
    """Categorize an unmapped ingredient.

    Returns:
        Category: PLACEHOLDER, COMPLEX_MEDIA, INCOMPLETE_FORMULA, or CURATION_NEEDED
    """
    name_lower = parsed_name.lower()

    # Placeholders
    placeholder_patterns = [
        "see source",
        "full composition",
        "original amount",
        "adjust if required",
    ]
    if any(p in name_lower for p in placeholder_patterns):
        return "PLACEHOLDER"

    # Complex media/solutions
    complex_patterns = [
        "medium",
        "solution",
        "extract",
        "soil",
        "seawater",
        "trace",
        "vitamin",
        "metal",
        "buffer stock",
        "peptone",
        "tryptone",
        "yeast extract",
    ]
    if any(p in name_lower for p in complex_patterns):
        return "COMPLEX_MEDIA"

    # Incomplete formulas (short chemical formulas ending early)
    if re.match(r"^[A-Z][a-z]?[A-Z][a-z]?$", parsed_name):  # e.g., NaNO, K2HPO
        return "INCOMPLETE_FORMULA"

    # Truly unmapped - needs curation
    return "CURATION_NEEDED"


def convert_unmapped_ingredient(cm_unmapped: dict, index: int, category: str) -> dict:
    """Convert CultureMech unmapped to MediaIngredientMech format.

    Args:
        cm_unmapped: CultureMech unmapped ingredient
        index: Ingredient index for ID generation
        category: Category (PLACEHOLDER, COMPLEX_MEDIA, etc.)

    Returns:
        MediaIngredientMech IngredientRecord
    """
    parsed_name = cm_unmapped.get("parsed_chemical_name", "")
    placeholder_id = cm_unmapped.get("placeholder_id", "")

    preferred_term = parsed_name or placeholder_id or f"Unmapped {index}"
    ontology_id = f"UNMAPPED_{index:04d}"

    # Extract synonyms from raw_ingredient_text
    raw_texts = cm_unmapped.get("raw_ingredient_text", [])
    synonyms = []
    seen = set()

    for text in raw_texts:
        text = str(text).strip()
        if text.startswith("Original amount: "):
            text = text.replace("Original amount: ", "", 1).strip()
        if text and text not in seen:
            synonyms.append({
                "synonym_text": text,
                "synonym_type": "RAW_TEXT",
                "source": "CultureMech",
            })
            seen.add(text)

    # Build record
    record = {
        "identifier": ontology_id,
        "preferred_term": preferred_term,
        "synonyms": synonyms,
        "mapping_status": "UNMAPPED",
        "occurrence_statistics": {
            "total_occurrences": cm_unmapped.get("occurrence_count", 0),
            "media_count": len(cm_unmapped.get("media_occurrences", [])),
        },
    }

    record_curation_event(
        record,
        curator="prepare_unmapped_for_curation",
        action="IMPORTED",
        changes=f"Imported from CultureMech as {category}",
        new_status="UNMAPPED",
        timestamp=TIMESTAMP,
    )

    # Add category note
    if category == "PLACEHOLDER":
        record["notes"] = "Placeholder for 'see source' references - not a real ingredient"
    elif category == "COMPLEX_MEDIA":
        record["notes"] = "Complex media or named solution - intentionally unmapped"
    elif category == "INCOMPLETE_FORMULA":
        record["notes"] = "Incomplete chemical formula - needs correction in source data"

    return record


def prepare_unmapped():
    """Prepare unmapped ingredients for curation."""
    print("="*80)
    print("PREPARE UNMAPPED INGREDIENTS FOR CURATION")
    print("="*80)
    print()

    # Load CultureMech unmapped
    print("Loading CultureMech unmapped ingredients...")
    cm_path = CULTUREMECH_DIR / "unmapped_ingredients.yaml"
    cm_data = load_yaml(cm_path)
    cm_unmapped = cm_data.get("unmapped_ingredients", [])
    print(f"  Loaded {len(cm_unmapped)} unmapped from CultureMech")

    # Load MediaIngredientMech mapped (to filter out)
    print("\nLoading MediaIngredientMech mapped ingredients...")
    mi_mapped_path = MI_DATA_DIR / "mapped_ingredients.yaml"
    mi_mapped_data = load_yaml(mi_mapped_path)
    mi_mapped = mi_mapped_data.get("ingredients", [])
    print(f"  Loaded {len(mi_mapped)} mapped from MI")

    # Build MI mapped index (for filtering)
    mi_index = {}
    mi_norm_index = {}
    for ing in mi_mapped:
        term = ing.get("preferred_term", "")
        if term:
            mi_index[term] = ing
            mi_norm_index[normalize_term(term)] = ing

    # Process CultureMech unmapped
    print("\nProcessing unmapped ingredients...")

    stats = {
        "total": len(cm_unmapped),
        "already_mapped": 0,
        "placeholder": 0,
        "complex_media": 0,
        "incomplete_formula": 0,
        "curation_needed": 0,
    }

    unmapped_records = []
    index = 1

    for cm_ing in cm_unmapped:
        parsed_name = cm_ing.get("parsed_chemical_name", "")

        if not parsed_name:
            continue

        # Check if already mapped in MI
        if parsed_name in mi_index or normalize_term(parsed_name) in mi_norm_index:
            stats["already_mapped"] += 1
            continue

        # Categorize
        category = categorize_unmapped(parsed_name)

        if category == "PLACEHOLDER":
            stats["placeholder"] += 1
        elif category == "COMPLEX_MEDIA":
            stats["complex_media"] += 1
        elif category == "INCOMPLETE_FORMULA":
            stats["incomplete_formula"] += 1
        else:
            stats["curation_needed"] += 1

        # Convert to record
        record = convert_unmapped_ingredient(cm_ing, index, category)
        unmapped_records.append(record)
        index += 1

    # Sort by occurrence count (highest first for curation priority)
    unmapped_records.sort(
        key=lambda x: x["occurrence_statistics"]["total_occurrences"],
        reverse=True
    )

    # Build collection
    collection = {
        "generation_date": TIMESTAMP,
        "total_count": len(unmapped_records),
        "mapped_count": 0,
        "unmapped_count": len(unmapped_records),
        "ingredients": unmapped_records,
    }

    # Save
    output_path = MI_DATA_DIR / "unmapped_ingredients.yaml"
    try:
        save_yaml(collection, output_path, validate=True, target_class="IngredientCollection")
    except ValidationFailedError as exc:
        print(exc.summary(), file=sys.stderr)
        raise

    # Report
    print("\n" + "="*80)
    print("PREPARATION SUMMARY")
    print("="*80)
    print(f"Total in CultureMech: {stats['total']}")
    print(f"Already mapped in MI: {stats['already_mapped']} (filtered out)")
    print()
    print(f"Unmapped ingredients prepared: {len(unmapped_records)}")
    print(f"  - Placeholders: {stats['placeholder']}")
    print(f"  - Complex media: {stats['complex_media']}")
    print(f"  - Incomplete formulas: {stats['incomplete_formula']}")
    print(f"  - Need curation: {stats['curation_needed']}")
    print()
    print(f"✅ Saved to: {output_path}")
    print()
    print("Priority for curation (by occurrence count):")
    for i, rec in enumerate(unmapped_records[:10], 1):
        term = rec["preferred_term"]
        count = rec["occurrence_statistics"]["total_occurrences"]
        cat = "CURATE" if categorize_unmapped(term) == "CURATION_NEEDED" else "SKIP"
        print(f"  {i}. {term} ({count} occ) - {cat}")

    print("\n" + "="*80)
    print(f"✅ Ready for curation: {stats['curation_needed']} ingredients")
    print("="*80)


if __name__ == "__main__":
    prepare_unmapped()
