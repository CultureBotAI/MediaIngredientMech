#!/usr/bin/env python3
"""Import ingredient data from CultureMech into MediaIngredientMech format.

Transforms CultureMech mapped/unmapped ingredient YAML files into
IngredientRecord collections conforming to the mediaingredientmech schema.

Usage:
    python scripts/import_from_culturemech.py [--source-dir PATH] [--output-dir PATH]
"""

import argparse
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


# Default paths
DEFAULT_SOURCE_DIR = Path(
    "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech/output"
)
DEFAULT_OUTPUT_DIR = Path(
    "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/MediaIngredientMech/data/curated"
)

TIMESTAMP = datetime.now(timezone.utc).isoformat()


def load_source(path: Path) -> dict:
    """Load a CultureMech YAML file."""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def make_curation_event() -> dict:
    """Create an initial IMPORTED curation event."""
    return {
        "timestamp": TIMESTAMP,
        "curator": "import_from_culturemech",
        "action": "IMPORTED",
        "changes": "Initial import from CultureMech pipeline",
        "new_status": None,  # set per-record
        "llm_assisted": False,
    }


def extract_synonyms(ingredient: dict) -> list[dict]:
    """Extract synonyms from a mapped ingredient's synonyms list.

    CultureMech synonyms are role/property descriptions from the raw data.
    We treat them as RAW_TEXT synonyms.
    """
    raw_synonyms = ingredient.get("synonyms", [])
    if not raw_synonyms:
        return []

    seen = set()
    result = []
    for text in raw_synonyms:
        text = str(text).strip()
        if not text or text in seen:
            continue
        seen.add(text)
        result.append(
            {
                "synonym_text": text,
                "synonym_type": "RAW_TEXT",
                "source": "CultureMech",
            }
        )
    return result


def extract_unmapped_synonyms(ingredient: dict) -> list[dict]:
    """Extract synonyms from unmapped ingredient raw_ingredient_text list."""
    raw_texts = ingredient.get("raw_ingredient_text", [])
    if not raw_texts:
        return []

    seen = set()
    result = []
    for text in raw_texts:
        text = str(text).strip()

        # Clean up "Original amount: " prefix from CultureMech notes
        if text.startswith("Original amount: "):
            text = text.replace("Original amount: ", "", 1).strip()

        if not text or text in seen:
            continue
        seen.add(text)
        result.append(
            {
                "synonym_text": text,
                "synonym_type": "RAW_TEXT",
                "source": "CultureMech",
            }
        )
    return result


def map_quality(culturemech_quality: str) -> str:
    """Map CultureMech mapping_quality to schema MappingQualityEnum."""
    mapping = {
        "DIRECT_MATCH": "EXACT_MATCH",
        "SYNONYM_MATCH": "SYNONYM_MATCH",
        "CLOSE_MATCH": "CLOSE_MATCH",
        "MANUAL_CURATION": "MANUAL_CURATION",
    }
    return mapping.get(culturemech_quality, "PROVISIONAL")


def convert_mapped_ingredient(ingredient: dict) -> dict:
    """Convert a single CultureMech mapped ingredient to IngredientRecord."""
    ontology_id = ingredient["ontology_id"]
    ontology_source = ingredient.get("ontology_source", "CHEBI")

    event = make_curation_event()
    event["new_status"] = "MAPPED"

    record: dict[str, Any] = {
        "identifier": ontology_id,
        "preferred_term": ingredient["preferred_term"],
        "ontology_mapping": {
            "ontology_id": ontology_id,
            "ontology_label": ingredient.get("ontology_label", ingredient["preferred_term"]),
            "ontology_source": ontology_source,
            "mapping_quality": map_quality(ingredient.get("mapping_quality", "DIRECT_MATCH")),
            "evidence": [
                {
                    "evidence_type": "DATABASE_MATCH",
                    "source": "CultureMech",
                    "notes": f"Imported from CultureMech pipeline, quality={ingredient.get('mapping_quality', 'DIRECT_MATCH')}",
                }
            ],
        },
        "synonyms": extract_synonyms(ingredient),
        "mapping_status": "MAPPED",
        "occurrence_statistics": {
            "total_occurrences": ingredient.get("occurrence_count", 0),
            "media_count": len(ingredient.get("media_occurrences", [])),
        },
        "curation_history": [event],
    }

    return record


def convert_unmapped_ingredient(ingredient: dict, index: int) -> dict:
    """Convert a single CultureMech unmapped ingredient to IngredientRecord."""
    placeholder = ingredient.get("placeholder_id", "")
    identifier = f"UNMAPPED_{index:04d}"

    # Use parsed_chemical_name as preferred_term if available, else placeholder_id
    preferred_term = ingredient.get("parsed_chemical_name", placeholder) or placeholder or f"Unmapped ingredient {index}"

    event = make_curation_event()
    event["new_status"] = "UNMAPPED"

    record: dict[str, Any] = {
        "identifier": identifier,
        "preferred_term": preferred_term,
        "synonyms": extract_unmapped_synonyms(ingredient),
        "mapping_status": "UNMAPPED",
        "occurrence_statistics": {
            "total_occurrences": ingredient.get("occurrence_count", 0),
            "media_count": len(ingredient.get("media_occurrences", [])),
        },
        "curation_history": [event],
        "notes": f"CultureMech placeholder_id: {placeholder}",
    }

    return record


def build_collection(ingredients: list[dict], mapped_count: int, unmapped_count: int) -> dict:
    """Wrap ingredient records in an IngredientCollection."""
    return {
        "generation_date": TIMESTAMP,
        "total_count": len(ingredients),
        "mapped_count": mapped_count,
        "unmapped_count": unmapped_count,
        "ingredients": ingredients,
    }


def import_mapped(source_dir: Path, output_dir: Path) -> int:
    """Import mapped ingredients and write output file."""
    source_path = source_dir / "mapped_ingredients.yaml"
    data = load_source(source_path)
    source_ingredients = data.get("mapped_ingredients", [])

    records = [convert_mapped_ingredient(ing) for ing in source_ingredients]

    collection = build_collection(records, mapped_count=len(records), unmapped_count=0)

    output_path = output_dir / "mapped_ingredients.yaml"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        yaml.dump(collection, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

    print(f"Wrote {len(records)} mapped ingredients to {output_path}")
    return len(records)


def import_unmapped(source_dir: Path, output_dir: Path) -> int:
    """Import unmapped ingredients and write output file."""
    source_path = source_dir / "unmapped_ingredients.yaml"
    data = load_source(source_path)
    source_ingredients = data.get("unmapped_ingredients", [])

    records = [
        convert_unmapped_ingredient(ing, i + 1) for i, ing in enumerate(source_ingredients)
    ]

    collection = build_collection(records, mapped_count=0, unmapped_count=len(records))

    output_path = output_dir / "unmapped_ingredients.yaml"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        yaml.dump(collection, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

    print(f"Wrote {len(records)} unmapped ingredients to {output_path}")
    return len(records)


def main():
    parser = argparse.ArgumentParser(
        description="Import CultureMech ingredients into MediaIngredientMech format"
    )
    parser.add_argument(
        "--source-dir",
        type=Path,
        default=DEFAULT_SOURCE_DIR,
        help="Directory containing CultureMech output YAML files",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Output directory for curated YAML files",
    )
    args = parser.parse_args()

    mapped_count = import_mapped(args.source_dir, args.output_dir)
    unmapped_count = import_unmapped(args.source_dir, args.output_dir)

    print(f"\nImport complete: {mapped_count} mapped, {unmapped_count} unmapped ingredients")


if __name__ == "__main__":
    main()
