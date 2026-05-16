#!/usr/bin/env python3
"""Intelligently merge CultureMech updates into MediaIngredientMech while preserving role curation.

This script performs a smart merge of the latest CultureMech data into MediaIngredientMech:
- Preserves all media_roles and curation_history (CRITICAL)
- Updates occurrence counts to match CultureMech
- Adds new ingredients from CultureMech
- Archives removed ingredients that have role curation
- Reconciles ontology mapping changes with audit trail
- Merges synonyms (union of both sources)

Usage:
    python scripts/merge_culturemech_updates.py [--dry-run] [--verbose]
"""

import argparse
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


# Default paths
CULTUREMECH_DIR = Path(
    "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech/output"
)
MI_DATA_DIR = Path(
    "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/MediaIngredientMech/data/curated"
)
ANALYSIS_DIR = Path(
    "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/MediaIngredientMech/data/analysis"
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
    # Remove whitespace, lowercase, remove special chars
    import re
    normalized = term.lower().strip()
    # Normalize hydrate separators (• vs x vs · vs .)
    normalized = re.sub(r"[•·×x]\s*", "x", normalized)
    # Remove extra whitespace
    normalized = re.sub(r"\s+", " ", normalized)
    return normalized


def make_curation_event(action: str, changes: str, curator: str = "merge_culturemech_updates") -> dict:
    """Create a curation history event."""
    return {
        "timestamp": TIMESTAMP,
        "curator": curator,
        "action": action,
        "changes": changes,
        "llm_assisted": False,
    }


def merge_synonyms(mi_record: dict, cm_ingredient: dict) -> list[dict]:
    """Merge synonyms from both sources (union)."""
    # Get existing MediaIngredientMech synonyms
    existing = mi_record.get("synonyms", [])
    existing_texts = {s["synonym_text"] for s in existing}

    # Add CultureMech synonyms that don't exist
    cm_synonyms = cm_ingredient.get("synonyms", [])
    merged = list(existing)  # Copy existing

    for cm_syn_text in cm_synonyms:
        cm_syn_text = str(cm_syn_text).strip()
        if cm_syn_text and cm_syn_text not in existing_texts:
            merged.append({
                "synonym_text": cm_syn_text,
                "synonym_type": "RAW_TEXT",
                "source": "CultureMech",
            })
            existing_texts.add(cm_syn_text)

    return merged


def has_role_curation(record: dict) -> bool:
    """Check if an ingredient has role curation work."""
    return bool(record.get("media_roles"))


def merge_ingredient(mi_record: dict, cm_ingredient: dict, verbose: bool = False) -> tuple[dict, dict]:
    """Merge CultureMech data into MediaIngredientMech record.

    Returns:
        (merged_record, changes_dict)
    """
    changes = {}
    merged = dict(mi_record)  # Copy MI record

    # PRESERVE these critical fields from MediaIngredientMech
    preserved_fields = ["media_roles", "curation_history", "id", "identifier"]

    # Update occurrence counts
    cm_count = cm_ingredient.get("occurrence_count", 0)
    cm_media_count = len(cm_ingredient.get("media_occurrences", []))
    mi_count = mi_record.get("occurrence_statistics", {}).get("total_occurrences", 0)
    mi_media_count = mi_record.get("occurrence_statistics", {}).get("media_count", 0)

    if cm_count != mi_count or cm_media_count != mi_media_count:
        changes["occurrence_update"] = {
            "old": {"total": mi_count, "media": mi_media_count},
            "new": {"total": cm_count, "media": cm_media_count},
        }
        merged["occurrence_statistics"] = {
            "total_occurrences": cm_count,
            "media_count": cm_media_count,
        }

    # Check for ontology ID changes
    cm_ontology = cm_ingredient.get("ontology_id")
    mi_ontology = (mi_record.get("identifier") or mi_record.get("ontology_id"))

    if cm_ontology and mi_ontology and cm_ontology != mi_ontology:
        changes["ontology_update"] = {
            "old": mi_ontology,
            "new": cm_ontology,
        }
        merged["ontology_id"] = cm_ontology

        # Update ontology_mapping
        if "ontology_mapping" in merged:
            merged["ontology_mapping"]["ontology_id"] = cm_ontology
            merged["ontology_mapping"]["ontology_label"] = cm_ingredient.get(
                "ontology_label", cm_ingredient["preferred_term"]
            )

        # Add curation event
        event = make_curation_event(
            action="ONTOLOGY_UPDATE",
            changes=f"Ontology changed from {mi_ontology} to {cm_ontology} (CultureMech update)"
        )
        merged.setdefault("curation_history", []).append(event)

    # Merge synonyms
    merged_synonyms = merge_synonyms(mi_record, cm_ingredient)
    if len(merged_synonyms) != len(mi_record.get("synonyms", [])):
        changes["synonyms_added"] = len(merged_synonyms) - len(mi_record.get("synonyms", []))
        merged["synonyms"] = merged_synonyms

    # Add merge event if any changes
    if changes:
        event = make_curation_event(
            action="MERGED_UPDATE",
            changes=f"Merged CultureMech update: {', '.join(changes.keys())}"
        )
        merged.setdefault("curation_history", []).append(event)

    if verbose and changes:
        print(f"  Updated {mi_record['preferred_term']}: {list(changes.keys())}")

    return merged, changes


def build_ingredient_index(ingredients: list[dict], key_field: str = "preferred_term") -> dict:
    """Build a dictionary index of ingredients by a key field."""
    index = {}
    normalized_index = {}

    for ing in ingredients:
        term = ing.get(key_field, "")
        if term:
            index[term] = ing
            normalized_index[normalize_term(term)] = ing

    return index, normalized_index


def import_new_ingredient(cm_ingredient: dict) -> dict:
    """Import a new ingredient from CultureMech."""
    ontology_id = cm_ingredient["ontology_id"]
    ontology_source = cm_ingredient.get("ontology_source", "CHEBI")

    # Extract synonyms
    raw_synonyms = cm_ingredient.get("synonyms", [])
    synonyms = []
    seen = set()
    for text in raw_synonyms:
        text = str(text).strip()
        if text and text not in seen:
            synonyms.append({
                "synonym_text": text,
                "synonym_type": "RAW_TEXT",
                "source": "CultureMech",
            })
            seen.add(text)

    # Map quality
    quality_map = {
        "DIRECT_MATCH": "EXACT_MATCH",
        "SYNONYM_MATCH": "SYNONYM_MATCH",
        "CLOSE_MATCH": "CLOSE_MATCH",
        "MANUAL_CURATION": "MANUAL_CURATION",
    }
    quality = quality_map.get(cm_ingredient.get("mapping_quality", "DIRECT_MATCH"), "PROVISIONAL")

    event = make_curation_event(
        action="IMPORTED",
        changes="Imported from CultureMech update 2026-03-15"
    )
    event["new_status"] = "MAPPED"

    record = {
        "ontology_id": ontology_id,
        "preferred_term": cm_ingredient["preferred_term"],
        "ontology_mapping": {
            "ontology_id": ontology_id,
            "ontology_label": cm_ingredient.get("ontology_label", cm_ingredient["preferred_term"]),
            "ontology_source": ontology_source,
            "mapping_quality": quality,
            "evidence": [
                {
                    "evidence_type": "DATABASE_MATCH",
                    "source": "CultureMech",
                    "notes": f"Imported from CultureMech update, quality={cm_ingredient.get('mapping_quality', 'DIRECT_MATCH')}",
                }
            ],
        },
        "synonyms": synonyms,
        "mapping_status": "MAPPED",
        "occurrence_statistics": {
            "total_occurrences": cm_ingredient.get("occurrence_count", 0),
            "media_count": len(cm_ingredient.get("media_occurrences", [])),
        },
        "curation_history": [event],
    }

    return record


def archive_ingredient(mi_record: dict, reason: str) -> dict:
    """Archive an ingredient removed from CultureMech."""
    archived = dict(mi_record)
    archived["mapping_status"] = "ARCHIVED"
    archived["archive_reason"] = reason

    event = make_curation_event(
        action="ARCHIVED",
        changes=reason
    )
    archived.setdefault("curation_history", []).append(event)

    return archived


def perform_merge(dry_run: bool = False, verbose: bool = False) -> dict:
    """Perform the merge operation.

    Returns:
        Statistics dictionary
    """
    print("Loading data...")

    # Load CultureMech data
    cm_mapped_path = CULTUREMECH_DIR / "mapped_ingredients.yaml"
    cm_data = load_yaml(cm_mapped_path)
    cm_ingredients = cm_data.get("mapped_ingredients", [])

    print(f"Loaded {len(cm_ingredients)} ingredients from CultureMech (generated {cm_data.get('generation_date', 'unknown')})")

    # Load MediaIngredientMech data
    mi_mapped_path = MI_DATA_DIR / "mapped_ingredients.yaml"
    mi_data = load_yaml(mi_mapped_path)
    mi_ingredients = mi_data.get("ingredients", [])

    print(f"Loaded {len(mi_ingredients)} ingredients from MediaIngredientMech (generated {mi_data.get('generation_date', 'unknown')})")

    # Count roles before merge
    roles_before = sum(1 for ing in mi_ingredients if has_role_curation(ing))
    print(f"Ingredients with roles: {roles_before} (MUST BE PRESERVED)")

    # Build indices
    print("\nBuilding indices...")
    cm_index, cm_norm_index = build_ingredient_index(cm_ingredients, "preferred_term")
    mi_index, mi_norm_index = build_ingredient_index(mi_ingredients, "preferred_term")

    # Track merge operations
    stats = {
        "common": 0,
        "new": 0,
        "removed": 0,
        "archived": 0,
        "updated": 0,
        "roles_preserved": 0,
        "ontology_changes": 0,
    }

    merged_ingredients = []
    archived_ingredients = []
    new_ingredients = []

    # Process common ingredients (exist in both)
    print("\nProcessing common ingredients...")
    for term, mi_record in mi_index.items():
        cm_ingredient = cm_index.get(term) or cm_norm_index.get(normalize_term(term))

        if cm_ingredient:
            stats["common"] += 1

            # Merge data
            merged, changes = merge_ingredient(mi_record, cm_ingredient, verbose)
            merged_ingredients.append(merged)

            if changes:
                stats["updated"] += 1
            if "ontology_update" in changes:
                stats["ontology_changes"] += 1
            if has_role_curation(merged):
                stats["roles_preserved"] += 1
        else:
            # Ingredient removed from CultureMech
            stats["removed"] += 1

            if has_role_curation(mi_record):
                # Archive it (preserve roles)
                stats["archived"] += 1
                archived = archive_ingredient(
                    mi_record,
                    "Removed from CultureMech 2026-03-15 (likely complex media decomposition or data cleanup)"
                )
                archived_ingredients.append(archived)

                if verbose:
                    print(f"  Archived {mi_record['preferred_term']} (has {len(mi_record.get('media_roles', []))} roles)")
            else:
                # No roles, just drop it
                if verbose:
                    print(f"  Dropped {mi_record['preferred_term']} (no roles)")

    # Process new ingredients (only in CultureMech)
    print("\nProcessing new ingredients...")
    for term, cm_ingredient in cm_index.items():
        mi_record = mi_index.get(term) or mi_norm_index.get(normalize_term(term))

        if not mi_record:
            stats["new"] += 1

            # Filter out placeholder ingredients (numeric, empty_X)
            if term.isdigit() or term.startswith("empty_"):
                if verbose:
                    print(f"  Skipping placeholder: {term}")
                continue

            new = import_new_ingredient(cm_ingredient)
            new_ingredients.append(new)

            if verbose:
                print(f"  Imported {term}")

    # Combine all ingredients
    all_ingredients = merged_ingredients + archived_ingredients + new_ingredients

    # Sort by preferred_term
    all_ingredients.sort(key=lambda x: x.get("preferred_term", "").lower())

    # Count roles after merge
    roles_after = sum(1 for ing in all_ingredients if has_role_curation(ing))

    # Build output collection
    output_data = {
        "generation_date": TIMESTAMP,
        "total_count": len(all_ingredients),
        "mapped_count": len(merged_ingredients) + len(new_ingredients),
        "unmapped_count": 0,
        "archived_count": len(archived_ingredients),
        "ingredients": all_ingredients,
    }

    # Print statistics
    print("\n" + "="*60)
    print("MERGE SUMMARY")
    print("="*60)
    print(f"Common ingredients:              {stats['common']}")
    print(f"  - Updated:                     {stats['updated']}")
    print(f"  - Ontology changes:            {stats['ontology_changes']}")
    print(f"New ingredients imported:        {stats['new']}")
    print(f"  - Real ingredients:            {len(new_ingredients)}")
    print(f"  - Placeholders skipped:        {stats['new'] - len(new_ingredients)}")
    print(f"Removed from CultureMech:        {stats['removed']}")
    print(f"  - Archived (has roles):        {stats['archived']}")
    print(f"  - Dropped (no roles):          {stats['removed'] - stats['archived']}")
    print()
    print(f"ROLES PRESERVATION CHECK:")
    print(f"  Before merge:                  {roles_before}")
    print(f"  After merge:                   {roles_after}")
    print(f"  Delta:                         {roles_after - roles_before}")
    print()
    print(f"Total ingredients after merge:   {len(all_ingredients)}")
    print(f"  - Active (mapped):             {len(merged_ingredients) + len(new_ingredients)}")
    print(f"  - Archived:                    {len(archived_ingredients)}")
    print("="*60)

    # Validation checks
    if roles_after < roles_before:
        print("\n⚠️  ERROR: ROLES LOST IN MERGE!")
        print(f"   Expected: {roles_before}, Got: {roles_after}")
        print("   Aborting merge.")
        sys.exit(1)

    # Save outputs
    if not dry_run:
        print("\nSaving merged data...")
        save_yaml(output_data, mi_mapped_path)
        print(f"Saved {len(all_ingredients)} ingredients to {mi_mapped_path}")

        # Save merge plan
        plan = {
            "merge_date": TIMESTAMP,
            "statistics": stats,
            "roles_before": roles_before,
            "roles_after": roles_after,
            "new_ingredients": [ing["preferred_term"] for ing in new_ingredients],
            "archived_ingredients": [ing["preferred_term"] for ing in archived_ingredients],
        }
        plan_path = ANALYSIS_DIR / "merge_plan.yaml"
        save_yaml(plan, plan_path)
        print(f"Saved merge plan to {plan_path}")
    else:
        print("\n[DRY RUN] No files written.")

        # Save dry-run plan
        plan = {
            "merge_date": TIMESTAMP,
            "dry_run": True,
            "statistics": stats,
            "roles_before": roles_before,
            "roles_after": roles_after,
            "new_ingredients": [ing["preferred_term"] for ing in new_ingredients],
            "archived_ingredients": [ing["preferred_term"] for ing in archived_ingredients],
        }
        plan_path = ANALYSIS_DIR / "merge_plan_dryrun.yaml"
        save_yaml(plan, plan_path)
        print(f"Saved dry-run plan to {plan_path}")

    return stats


def main():
    parser = argparse.ArgumentParser(
        description="Merge CultureMech updates into MediaIngredientMech while preserving role curation"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview merge without writing files"
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Verbose output"
    )
    args = parser.parse_args()

    print("CultureMech Data Merge Tool")
    print("="*60)

    if args.dry_run:
        print("MODE: DRY RUN (no files will be modified)")
    else:
        print("MODE: LIVE MERGE (files will be modified)")
        print("\nBackups should be created at:")
        print("  data/curated/mapped_ingredients.yaml.pre-merge-YYYYMMDD")

    print("\n")

    stats = perform_merge(dry_run=args.dry_run, verbose=args.verbose)

    print("\n✅ Merge complete!")

    if not args.dry_run:
        print("\nNext steps:")
        print("  1. Validate: PYTHONPATH=src python scripts/validate_roles.py")
        print("  2. Stats: PYTHONPATH=src python scripts/generate_role_statistics.py")
        print("  3. Re-analyze: PYTHONPATH=src python scripts/analyze_culturemech_roles.py")


if __name__ == "__main__":
    main()
