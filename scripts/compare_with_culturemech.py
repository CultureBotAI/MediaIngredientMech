#!/usr/bin/env python3
"""Compare MediaIngredientMech data with CultureMech source to detect updates.

This script compares ingredient data between MediaIngredientMech and CultureMech
to determine if an update/re-import is needed.
"""

import sys
from pathlib import Path
from collections import defaultdict
from datetime import datetime

import yaml

# CultureMech paths
CULTUREMECH_DIR = Path("/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech")
CULTUREMECH_MAPPED = CULTUREMECH_DIR / "output" / "mapped_ingredients.yaml"
CULTUREMECH_UNMAPPED = CULTUREMECH_DIR / "output" / "unmapped_ingredients.yaml"

# MediaIngredientMech paths
MEDIAINGREDIENT_MAPPED = Path("data/curated/mapped_ingredients.yaml")
MEDIAINGREDIENT_UNMAPPED = Path("data/curated/unmapped_ingredients.yaml")


def load_culturemech_data():
    """Load CultureMech ingredient data.

    Returns:
        Tuple of (mapped_data, unmapped_data)
    """
    print(f"Loading CultureMech data from: {CULTUREMECH_DIR}")

    with open(CULTUREMECH_MAPPED) as f:
        mapped_data = yaml.safe_load(f)

    with open(CULTUREMECH_UNMAPPED) as f:
        unmapped_data = yaml.safe_load(f)

    return mapped_data, unmapped_data


def load_mediaingredient_data():
    """Load MediaIngredientMech ingredient data.

    Returns:
        Tuple of (mapped_data, unmapped_data)
    """
    print(f"Loading MediaIngredientMech data from: data/curated/")

    with open(MEDIAINGREDIENT_MAPPED) as f:
        mapped_data = yaml.safe_load(f)

    with open(MEDIAINGREDIENT_UNMAPPED) as f:
        unmapped_data = yaml.safe_load(f)

    return mapped_data, unmapped_data


def build_ingredient_index(data, data_type="culturemech_mapped"):
    """Build index of ingredients by preferred term.

    Args:
        data: Ingredient data dictionary
        data_type: Type of data (for field names)

    Returns:
        Dictionary mapping preferred_term → ingredient_data
    """
    index = {}

    if data_type == "culturemech_mapped":
        for ingredient in data.get("mapped_ingredients", []):
            preferred_term = ingredient.get("preferred_term")
            if preferred_term:
                index[preferred_term] = ingredient

    elif data_type == "culturemech_unmapped":
        for ingredient in data.get("unmapped_ingredients", []):
            # Unmapped use parsed_chemical_name or placeholder_id as key
            # Prefer parsed_chemical_name over placeholder_id to avoid numeric IDs
            key = ingredient.get("parsed_chemical_name") or ingredient.get("placeholder_id")
            if key and not key.isdigit() and key not in ["empty_0", "empty_8"]:
                # Skip pure numeric IDs and empty placeholders - these are data quality issues
                index[key] = ingredient

    elif data_type == "mediaingredient":
        for ingredient in data.get("ingredients", []):
            preferred_term = ingredient.get("preferred_term")
            if preferred_term:
                index[preferred_term] = ingredient

    return index


def compare_ingredients(
    cm_mapped, cm_unmapped, mi_mapped, mi_unmapped
):
    """Compare ingredients between CultureMech and MediaIngredientMech.

    Args:
        cm_mapped: CultureMech mapped data
        cm_unmapped: CultureMech unmapped data
        mi_mapped: MediaIngredientMech mapped data
        mi_unmapped: MediaIngredientMech unmapped data

    Returns:
        Dictionary with comparison results
    """
    # Build indices
    cm_mapped_idx = build_ingredient_index(cm_mapped, "culturemech_mapped")
    cm_unmapped_idx = build_ingredient_index(cm_unmapped, "culturemech_unmapped")
    mi_mapped_idx = build_ingredient_index(mi_mapped, "mediaingredient")
    mi_unmapped_idx = build_ingredient_index(mi_unmapped, "mediaingredient")

    # Combine for comparison
    cm_all_terms = set(cm_mapped_idx.keys()) | set(cm_unmapped_idx.keys())
    mi_all_terms = set(mi_mapped_idx.keys()) | set(mi_unmapped_idx.keys())

    results = {
        "culturemech": {
            "generation_date": cm_mapped.get("generation_date"),
            "mapped_count": len(cm_mapped_idx),
            "unmapped_count": len(cm_unmapped_idx),
            "total_count": len(cm_all_terms),
            "total_instances": cm_mapped.get("total_instances", 0),
            "media_count": cm_mapped.get("media_count", 0),
        },
        "mediaingredientmech": {
            "generation_date": mi_mapped.get("generation_date"),
            "mapped_count": len(mi_mapped_idx),
            "unmapped_count": len(mi_unmapped_idx),
            "total_count": len(mi_all_terms),
        },
        "new_in_culturemech": sorted(cm_all_terms - mi_all_terms),
        "removed_from_culturemech": sorted(mi_all_terms - cm_all_terms),
        "occurrence_changes": [],
        "mapping_changes": [],
    }

    # Check for occurrence count changes in common ingredients
    common_terms = cm_all_terms & mi_all_terms

    for term in common_terms:
        # Get from both sources
        cm_ing = cm_mapped_idx.get(term) or cm_unmapped_idx.get(term)
        mi_ing = mi_mapped_idx.get(term) or mi_unmapped_idx.get(term)

        if not cm_ing or not mi_ing:
            continue

        # Compare occurrence counts
        cm_count = cm_ing.get("occurrence_count", 0)
        mi_count = mi_ing.get("occurrence_statistics", {}).get("total_occurrences", 0)

        if cm_count != mi_count:
            results["occurrence_changes"].append({
                "term": term,
                "culturemech_count": cm_count,
                "mediaingredient_count": mi_count,
                "delta": cm_count - mi_count,
            })

        # Compare ontology mappings
        cm_ontology = cm_ing.get("ontology_id")
        mi_ontology = mi_ing.get("ontology_id")

        if cm_ontology != mi_ontology:
            results["mapping_changes"].append({
                "term": term,
                "culturemech_ontology": cm_ontology,
                "mediaingredient_ontology": mi_ontology,
            })

    # Sort occurrence changes by delta (descending)
    results["occurrence_changes"].sort(key=lambda x: abs(x["delta"]), reverse=True)

    return results


def print_comparison_report(results):
    """Print formatted comparison report.

    Args:
        results: Comparison results dictionary
    """
    print("\n" + "=" * 80)
    print("CULTUREMECH vs MEDIAINGREDIENTMECH COMPARISON")
    print("=" * 80)

    # Generation dates
    cm_date = results["culturemech"]["generation_date"]
    mi_date = results["mediaingredientmech"]["generation_date"]

    print(f"\nGENERATION DATES:")
    print(f"  CultureMech:        {cm_date}")
    print(f"  MediaIngredientMech: {mi_date}")

    # Parse dates to calculate age difference
    try:
        cm_dt = datetime.fromisoformat(cm_date.replace('Z', '+00:00'))
        mi_dt = datetime.fromisoformat(mi_date.replace('Z', '+00:00'))
        age_diff = cm_dt - mi_dt
        print(f"  Age difference:     {age_diff.total_seconds() / 3600:.1f} hours")
    except:
        pass

    # Counts
    print(f"\nINGREDIENT COUNTS:")
    print(f"  {'':30s} {'CultureMech':>15s} {'MediaIngMech':>15s} {'Delta':>10s}")
    print(f"  {'-'*70}")

    cm = results["culturemech"]
    mi = results["mediaingredientmech"]

    print(f"  {'Mapped ingredients':30s} {cm['mapped_count']:>15,} {mi['mapped_count']:>15,} {cm['mapped_count']-mi['mapped_count']:>10,}")
    print(f"  {'Unmapped ingredients':30s} {cm['unmapped_count']:>15,} {mi['unmapped_count']:>15,} {cm['unmapped_count']-mi['unmapped_count']:>10,}")
    print(f"  {'Total ingredients':30s} {cm['total_count']:>15,} {mi['total_count']:>15,} {cm['total_count']-mi['total_count']:>10,}")

    print(f"\nMEDIA COLLECTION:")
    print(f"  CultureMech media count: {cm['media_count']:,}")
    print(f"  Total ingredient instances: {cm['total_instances']:,}")

    # New ingredients
    new_count = len(results["new_in_culturemech"])
    if new_count > 0:
        print(f"\n⚠️  NEW INGREDIENTS IN CULTUREMECH ({new_count}):")
        for i, term in enumerate(results["new_in_culturemech"][:20], 1):
            print(f"  {i:2d}. {term}")
        if new_count > 20:
            print(f"  ... and {new_count - 20} more")
    else:
        print(f"\n✅ No new ingredients in CultureMech")

    # Removed ingredients
    removed_count = len(results["removed_from_culturemech"])
    if removed_count > 0:
        print(f"\n⚠️  INGREDIENTS REMOVED FROM CULTUREMECH ({removed_count}):")
        for i, term in enumerate(results["removed_from_culturemech"][:20], 1):
            print(f"  {i:2d}. {term}")
        if removed_count > 20:
            print(f"  ... and {removed_count - 20} more")
    else:
        print(f"\n✅ No ingredients removed from CultureMech")

    # Occurrence changes
    occ_changes = results["occurrence_changes"]
    if occ_changes:
        print(f"\n⚠️  OCCURRENCE COUNT CHANGES ({len(occ_changes)} ingredients):")
        print(f"  {'Ingredient':40s} {'CM Count':>12s} {'MI Count':>12s} {'Delta':>10s}")
        print(f"  {'-'*74}")
        for change in occ_changes[:15]:
            print(f"  {change['term']:40s} {change['culturemech_count']:>12,} {change['mediaingredient_count']:>12,} {change['delta']:>+10,}")
        if len(occ_changes) > 15:
            print(f"  ... and {len(occ_changes) - 15} more with changes")
    else:
        print(f"\n✅ No occurrence count changes")

    # Mapping changes
    map_changes = results["mapping_changes"]
    if map_changes:
        print(f"\n⚠️  ONTOLOGY MAPPING CHANGES ({len(map_changes)} ingredients):")
        for change in map_changes[:10]:
            print(f"  {change['term']}:")
            print(f"    CultureMech:        {change['culturemech_ontology']}")
            print(f"    MediaIngredientMech: {change['mediaingredient_ontology']}")
        if len(map_changes) > 10:
            print(f"  ... and {len(map_changes) - 10} more")
    else:
        print(f"\n✅ No ontology mapping changes")

    # Recommendation
    print("\n" + "=" * 80)
    print("RECOMMENDATION")
    print("=" * 80)

    needs_update = (
        new_count > 0 or
        removed_count > 0 or
        len(occ_changes) > 10 or
        len(map_changes) > 0
    )

    if needs_update:
        print("\n⚠️  UPDATE RECOMMENDED")
        print("\nReasons:")
        if new_count > 0:
            print(f"  • {new_count} new ingredients in CultureMech")
        if removed_count > 0:
            print(f"  • {removed_count} ingredients removed from CultureMech")
        if len(occ_changes) > 10:
            print(f"  • {len(occ_changes)} ingredients have occurrence count changes")
        if len(map_changes) > 0:
            print(f"  • {len(map_changes)} ingredients have ontology mapping changes")

        print("\nRecommended action:")
        print("  1. Review changes above")
        print("  2. Backup current data:")
        print("     cp data/curated/mapped_ingredients.yaml data/curated/mapped_ingredients.yaml.backup")
        print("  3. Re-run import:")
        print("     PYTHONPATH=src python scripts/import_from_culturemech.py")
        print("  4. Re-run role extraction for new ingredients:")
        print("     PYTHONPATH=src python scripts/analyze_culturemech_roles.py")
        print("  5. Validate results:")
        print("     PYTHONPATH=src python scripts/validate_roles.py")
    else:
        print("\n✅ NO UPDATE NEEDED")
        print("\nMediaIngredientMech is up-to-date with CultureMech")

    print("\n" + "=" * 80)


def main():
    """Main comparison workflow."""
    print("=" * 80)
    print("CultureMech Update Check")
    print("=" * 80)

    # Load data
    cm_mapped, cm_unmapped = load_culturemech_data()
    mi_mapped, mi_unmapped = load_mediaingredient_data()

    # Compare
    results = compare_ingredients(cm_mapped, cm_unmapped, mi_mapped, mi_unmapped)

    # Print report
    print_comparison_report(results)

    # Save detailed results
    output_path = Path("data/analysis/culturemech_comparison.yaml")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w") as f:
        yaml.safe_dump(results, f, default_flow_style=False, sort_keys=False)

    print(f"\nDetailed results saved to: {output_path}")


if __name__ == "__main__":
    main()
