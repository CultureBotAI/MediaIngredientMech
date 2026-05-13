#!/usr/bin/env python3
"""Reconcile MediaIngredientMech unmapped ingredients with CultureMech.

Cross-references CultureMech's unmapped ingredients with MediaIngredientMech's
mapped ingredients to identify:
1. Ingredients that are mapped in MI but unmapped in CM (encoding differences)
2. Truly unmapped ingredients that need curation
3. Ingredients that moved from unmapped to mapped in CM

Usage:
    python scripts/reconcile_unmapped.py [--update] [--verbose]
"""

import argparse
import re
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
    # Remove whitespace, lowercase
    normalized = term.lower().strip()

    # Normalize hydrate separators (• vs x vs · vs *)
    normalized = re.sub(r"[•·×*]\s*", "x", normalized)

    # Normalize various bullet points and dots
    normalized = re.sub(r"[∙⋅]", ".", normalized)

    # Remove extra whitespace
    normalized = re.sub(r"\s+", " ", normalized)

    # Remove leading/trailing special chars
    normalized = normalized.strip(".,;: ")

    return normalized


def build_ingredient_index(ingredients: list[dict], term_field: str = "preferred_term") -> dict:
    """Build normalized index of ingredients."""
    index = {}
    normalized_index = {}

    for ing in ingredients:
        term = ing.get(term_field, "")
        if not term:
            continue

        # Store by exact term
        index[term] = ing

        # Store by normalized term
        norm_term = normalize_term(term)
        if norm_term:
            normalized_index[norm_term] = ing

    return index, normalized_index


def categorize_unmapped(cm_unmapped: list[dict], mi_mapped_index: dict, mi_norm_index: dict) -> dict:
    """Categorize CultureMech unmapped ingredients."""
    categories = {
        "already_mapped": [],  # Mapped in MI (encoding difference)
        "placeholders": [],    # "See source", "Full composition", etc.
        "incomplete_formulas": [],  # Malformed formulas (NaNO, K2HPO)
        "complex_media": [],   # Named media/solutions
        "truly_unmapped": [],  # Need curation
    }

    placeholder_patterns = [
        "see source",
        "full composition",
        "original amount",
        "adjust if required",
    ]

    incomplete_formula_patterns = [
        r"^[A-Z][a-z]?[A-Z][a-z]?$",  # Two elements no numbers (NaCl would be ok, but NaNO is incomplete)
        r"^[A-Z][a-z]?[0-9]*[A-Z][a-z]?$",  # Incomplete formula ending early
    ]

    complex_media_patterns = [
        "medium",
        "solution",
        "extract",
        "soil",
        "seawater",
        "trace",
        "vitamin",
        "metal",
        "buffer stock",
    ]

    for cm_ing in cm_unmapped:
        parsed_name = cm_ing.get("parsed_chemical_name", "")
        placeholder_id = cm_ing.get("placeholder_id", "")

        if not parsed_name:
            continue

        # Check if already mapped in MI
        exact_match = mi_mapped_index.get(parsed_name)
        norm_match = mi_norm_index.get(normalize_term(parsed_name))

        if exact_match or norm_match:
            categories["already_mapped"].append({
                "cm_name": parsed_name,
                "mi_match": (exact_match or norm_match).get("preferred_term"),
                "mi_ontology": (exact_match or norm_match).get("ontology_id"),
                "occurrence_count": cm_ing.get("occurrence_count", 0),
                "reason": "Mapped in MI (likely encoding difference)",
            })
            continue

        # Check if placeholder
        if any(pattern in parsed_name.lower() for pattern in placeholder_patterns):
            categories["placeholders"].append({
                "cm_name": parsed_name,
                "placeholder_id": placeholder_id,
                "occurrence_count": cm_ing.get("occurrence_count", 0),
                "reason": "Placeholder text",
            })
            continue

        # Check if incomplete formula
        if any(re.match(pattern, parsed_name) for pattern in incomplete_formula_patterns):
            categories["incomplete_formulas"].append({
                "cm_name": parsed_name,
                "occurrence_count": cm_ing.get("occurrence_count", 0),
                "reason": "Incomplete chemical formula",
            })
            continue

        # Check if complex media
        if any(pattern in parsed_name.lower() for pattern in complex_media_patterns):
            categories["complex_media"].append({
                "cm_name": parsed_name,
                "occurrence_count": cm_ing.get("occurrence_count", 0),
                "reason": "Complex media or named solution",
            })
            continue

        # Truly unmapped
        categories["truly_unmapped"].append({
            "cm_name": parsed_name,
            "placeholder_id": placeholder_id,
            "occurrence_count": cm_ing.get("occurrence_count", 0),
            "reason": "Needs curation",
        })

    return categories


def compare_with_mi_unmapped(cm_truly_unmapped: list[dict], mi_unmapped: list[dict]) -> dict:
    """Compare truly unmapped from CM with MI unmapped."""
    mi_index, mi_norm_index = build_ingredient_index(mi_unmapped, "preferred_term")

    results = {
        "in_both": [],
        "only_in_cm": [],
        "only_in_mi": [],
    }

    # Build set of CM names
    cm_names = {ing["cm_name"] for ing in cm_truly_unmapped}
    cm_norm_names = {normalize_term(ing["cm_name"]) for ing in cm_truly_unmapped}

    # Check which CM unmapped are in MI unmapped
    for cm_ing in cm_truly_unmapped:
        cm_name = cm_ing["cm_name"]
        norm_name = normalize_term(cm_name)

        if cm_name in mi_index or norm_name in mi_norm_index:
            results["in_both"].append(cm_ing)
        else:
            results["only_in_cm"].append(cm_ing)

    # Check which MI unmapped are not in CM unmapped
    for mi_ing in mi_unmapped:
        mi_name = mi_ing.get("preferred_term", "")
        norm_name = normalize_term(mi_name)

        if mi_name not in cm_names and norm_name not in cm_norm_names:
            # Skip UNMAPPED_XXXX placeholders
            if not mi_name.startswith("UNMAPPED_"):
                results["only_in_mi"].append({
                    "mi_name": mi_name,
                    "mi_id": mi_ing.get("id", ""),
                    "occurrence_count": mi_ing.get("occurrence_statistics", {}).get("total_occurrences", 0),
                })

    return results


def perform_reconciliation(verbose: bool = False) -> dict:
    """Perform the reconciliation."""
    print("="*80)
    print("UNMAPPED INGREDIENT RECONCILIATION")
    print("="*80)
    print()

    # Load CultureMech unmapped
    print("Loading CultureMech unmapped ingredients...")
    cm_unmapped_path = CULTUREMECH_DIR / "unmapped_ingredients.yaml"
    cm_data = load_yaml(cm_unmapped_path)
    cm_unmapped = cm_data.get("unmapped_ingredients", [])
    print(f"  Loaded {len(cm_unmapped)} unmapped ingredients from CultureMech")

    # Load MediaIngredientMech mapped
    print("\nLoading MediaIngredientMech mapped ingredients...")
    mi_mapped_path = MI_DATA_DIR / "mapped_ingredients.yaml"
    mi_mapped_data = load_yaml(mi_mapped_path)
    mi_mapped = mi_mapped_data.get("ingredients", [])
    print(f"  Loaded {len(mi_mapped)} mapped ingredients from MI")

    # Load MediaIngredientMech unmapped
    print("\nLoading MediaIngredientMech unmapped ingredients...")
    mi_unmapped_path = MI_DATA_DIR / "unmapped_ingredients.yaml"
    mi_unmapped_data = load_yaml(mi_unmapped_path)
    mi_unmapped = mi_unmapped_data.get("ingredients", [])
    print(f"  Loaded {len(mi_unmapped)} unmapped ingredients from MI")

    # Build MI mapped index
    print("\nBuilding indices...")
    mi_mapped_index, mi_mapped_norm_index = build_ingredient_index(mi_mapped, "preferred_term")

    # Categorize CultureMech unmapped
    print("\nCategorizing CultureMech unmapped ingredients...")
    categories = categorize_unmapped(cm_unmapped, mi_mapped_index, mi_mapped_norm_index)

    print(f"\nCategorization results:")
    print(f"  Already mapped in MI:     {len(categories['already_mapped'])}")
    print(f"  Placeholders:             {len(categories['placeholders'])}")
    print(f"  Incomplete formulas:      {len(categories['incomplete_formulas'])}")
    print(f"  Complex media:            {len(categories['complex_media'])}")
    print(f"  Truly unmapped:           {len(categories['truly_unmapped'])}")
    print(f"  Total:                    {len(cm_unmapped)}")

    # Compare truly unmapped between CM and MI
    print("\nComparing truly unmapped ingredients...")
    comparison = compare_with_mi_unmapped(categories["truly_unmapped"], mi_unmapped)

    print(f"\nComparison results:")
    print(f"  In both CM and MI:        {len(comparison['in_both'])}")
    print(f"  Only in CultureMech:      {len(comparison['only_in_cm'])}")
    print(f"  Only in MI:               {len(comparison['only_in_mi'])}")

    # Detailed output
    if verbose:
        print("\n" + "="*80)
        print("DETAILED RESULTS")
        print("="*80)

        if categories["already_mapped"]:
            print(f"\n➤ Already mapped in MI ({len(categories['already_mapped'])}):")
            for ing in sorted(categories["already_mapped"], key=lambda x: -x["occurrence_count"])[:10]:
                print(f"  • {ing['cm_name']}")
                print(f"    → Mapped as: {ing['mi_match']} ({ing['mi_ontology']})")
                print(f"    Occurrences: {ing['occurrence_count']}")

        if categories["truly_unmapped"]:
            print(f"\n➤ Truly unmapped ({len(categories['truly_unmapped'])}):")
            for ing in sorted(categories["truly_unmapped"], key=lambda x: -x["occurrence_count"])[:10]:
                print(f"  • {ing['cm_name']} ({ing['occurrence_count']} occurrences)")

        if comparison["only_in_cm"]:
            print(f"\n➤ Only in CultureMech unmapped ({len(comparison['only_in_cm'])}):")
            for ing in sorted(comparison["only_in_cm"], key=lambda x: -x["occurrence_count"])[:5]:
                print(f"  • {ing['cm_name']} ({ing['occurrence_count']} occurrences)")

        if comparison["only_in_mi"]:
            print(f"\n➤ Only in MI unmapped ({len(comparison['only_in_mi'])}):")
            for ing in sorted(comparison["only_in_mi"], key=lambda x: -x["occurrence_count"])[:10]:
                print(f"  • {ing['mi_name']} ({ing['occurrence_count']} occurrences)")

    # Save reconciliation report
    report = {
        "reconciliation_date": TIMESTAMP,
        "culturemech_unmapped_count": len(cm_unmapped),
        "mediaingredientmech_mapped_count": len(mi_mapped),
        "mediaingredientmech_unmapped_count": len(mi_unmapped),
        "categorization": {
            "already_mapped": {
                "count": len(categories["already_mapped"]),
                "ingredients": sorted(categories["already_mapped"], key=lambda x: -x["occurrence_count"]),
            },
            "placeholders": {
                "count": len(categories["placeholders"]),
                "ingredients": categories["placeholders"],
            },
            "incomplete_formulas": {
                "count": len(categories["incomplete_formulas"]),
                "ingredients": categories["incomplete_formulas"],
            },
            "complex_media": {
                "count": len(categories["complex_media"]),
                "ingredients": categories["complex_media"],
            },
            "truly_unmapped": {
                "count": len(categories["truly_unmapped"]),
                "ingredients": sorted(categories["truly_unmapped"], key=lambda x: -x["occurrence_count"]),
            },
        },
        "comparison": {
            "in_both_cm_and_mi": {
                "count": len(comparison["in_both"]),
                "ingredients": comparison["in_both"],
            },
            "only_in_culturemech": {
                "count": len(comparison["only_in_cm"]),
                "ingredients": comparison["only_in_cm"],
            },
            "only_in_mediaingredientmech": {
                "count": len(comparison["only_in_mi"]),
                "ingredients": comparison["only_in_mi"],
            },
        },
        "recommendations": {
            "already_mapped_action": "These are already mapped in MI - likely encoding differences (• vs x). No action needed.",
            "placeholders_action": "These are intentionally unmapped placeholders. Keep as reference but don't curate.",
            "incomplete_formulas_action": "These are malformed formulas. Should be fixed in source data.",
            "complex_media_action": "These are complex media/solutions. Likely decomposed in CultureMech cleanup.",
            "truly_unmapped_action": f"These {len(categories['truly_unmapped'])} ingredients need curation.",
            "only_in_mi_action": f"These {len(comparison['only_in_mi'])} ingredients may have been mapped in CultureMech update. Review for migration to mapped.",
        },
    }

    report_path = ANALYSIS_DIR / "unmapped_reconciliation_report.yaml"
    save_yaml(report, report_path)
    print(f"\n✅ Reconciliation report saved to: {report_path}")

    return report


def main():
    parser = argparse.ArgumentParser(
        description="Reconcile unmapped ingredients between CultureMech and MediaIngredientMech"
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Verbose output with detailed lists"
    )
    args = parser.parse_args()

    report = perform_reconciliation(verbose=args.verbose)

    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"\nCultureMech has {report['categorization']['truly_unmapped']['count']} truly unmapped ingredients")
    print(f"MediaIngredientMech has {report['mediaingredientmech_unmapped_count']} unmapped ingredients")
    print(f"\nOverlap: {report['comparison']['in_both_cm_and_mi']['count']} ingredients")
    print(f"New in CM: {report['comparison']['only_in_culturemech']['count']} ingredients")
    print(f"Only in MI: {report['comparison']['only_in_mediaingredientmech']['count']} ingredients")
    print()
    print("✅ Reconciliation complete!")
    print(f"\nSee detailed report: data/analysis/unmapped_reconciliation_report.yaml")


if __name__ == "__main__":
    main()
