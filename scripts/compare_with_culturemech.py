#!/usr/bin/env python3
"""Compare MediaIngredientMech data with CultureMech source for review.

This script compares ingredient data between MediaIngredientMech and CultureMech
to identify differences that may warrant a scoped curation update. It never
imports or mutates curated MIM records.
"""

import os
from datetime import datetime
from pathlib import Path

import yaml

# Default paths assume the standard sibling-checkout layout. Override the
# CultureMech location with the CULTUREMECH_DIR env var when running
# elsewhere.
_REPO_ROOT = Path(__file__).resolve().parents[1]
CULTUREMECH_DIR = Path(
    os.environ.get(
        "CULTUREMECH_DIR",
        str((_REPO_ROOT.parent / "CultureMech").resolve()),
    )
)
CULTUREMECH_MAPPED = CULTUREMECH_DIR / "output" / "mapped_ingredients.yaml"
CULTUREMECH_UNMAPPED = CULTUREMECH_DIR / "output" / "unmapped_ingredients.yaml"

# MediaIngredientMech paths (relative to repo root)
MEDIAINGREDIENT_MAPPED = _REPO_ROOT / "data" / "curated" / "mapped_ingredients.yaml"
MEDIAINGREDIENT_UNMAPPED = _REPO_ROOT / "data" / "curated" / "unmapped_ingredients.yaml"


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
    print("Loading MediaIngredientMech data from: data/curated/")

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

    return index


def _mim_ontology_id(ingredient):
    """Return the asserted MIM ontology target from the current record shape."""
    mapping = ingredient.get("ontology_mapping")
    if isinstance(mapping, dict):
        target = mapping.get("ontology_id")
        if target:
            return target
    return ingredient.get("identifier") or ingredient.get("ontology_id")


def _build_mim_status_indexes(mi_mapped, mi_unmapped):
    """Index MIM records by asserted status, never by collection filename."""
    indexes = {"MAPPED": {}, "UNMAPPED": {}}
    rejected = []
    other = []
    for collection, data in (
        ("mapped_ingredients.yaml", mi_mapped),
        ("unmapped_ingredients.yaml", mi_unmapped),
    ):
        for ingredient in data.get("ingredients", []):
            term = ingredient.get("preferred_term")
            if not term:
                continue
            status = ingredient.get("mapping_status")
            if status in indexes:
                indexes[status][term] = ingredient
                continue
            diagnostic = {
                "term": term,
                "mapping_status": status or "MISSING",
                "identifier": ingredient.get("identifier"),
                "collection": collection,
            }
            if status == "REJECTED":
                rejected.append(diagnostic)
            else:
                other.append(diagnostic)
    rejected.sort(key=lambda record: (record["term"], record["collection"]))
    other.sort(key=lambda record: (record["term"], record["collection"]))
    return indexes["MAPPED"], indexes["UNMAPPED"], rejected, other


def _status(mapped_index, unmapped_index, term):
    """Return an explicit status without resolving cross-status collisions."""
    is_mapped = term in mapped_index
    is_unmapped = term in unmapped_index
    if is_mapped and is_unmapped:
        return "MAPPED_AND_UNMAPPED"
    if is_mapped:
        return "MAPPED"
    if is_unmapped:
        return "UNMAPPED"
    return "NOT_PRESENT"


def _status_collision(term, mapped_record, unmapped_record, source):
    """Describe a label present in both collections of one source."""
    if source == "culturemech":
        mapped_target = mapped_record.get("ontology_id")
        mapped_count = mapped_record.get("occurrence_count", 0)
        unmapped_count = unmapped_record.get("occurrence_count", 0)
    else:
        mapped_target = _mim_ontology_id(mapped_record)
        mapped_count = mapped_record.get("occurrence_statistics", {}).get("total_occurrences", 0)
        unmapped_count = unmapped_record.get("occurrence_statistics", {}).get(
            "total_occurrences", 0
        )
    return {
        "term": term,
        "source": source,
        "statuses": ["MAPPED", "UNMAPPED"],
        "mapped_ontology": mapped_target,
        "mapped_occurrence_count": mapped_count,
        "unmapped_occurrence_count": unmapped_count,
    }


def compare_ingredients(cm_mapped, cm_unmapped, mi_mapped, mi_unmapped):
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
    (
        mi_mapped_idx,
        mi_unmapped_idx,
        mi_rejected,
        mi_non_active_or_missing,
    ) = _build_mim_status_indexes(mi_mapped, mi_unmapped)

    # Combine for comparison
    cm_all_terms = set(cm_mapped_idx.keys()) | set(cm_unmapped_idx.keys())
    mi_all_terms = set(mi_mapped_idx.keys()) | set(mi_unmapped_idx.keys())
    mi_rejected_terms = {record["term"] for record in mi_rejected}
    mi_non_active_or_missing_terms = {record["term"] for record in mi_non_active_or_missing}
    mi_known_terms = mi_all_terms | mi_rejected_terms | mi_non_active_or_missing_terms
    rejected_only_cm_terms = sorted((cm_all_terms & mi_rejected_terms) - mi_all_terms)
    non_active_or_missing_cm_terms = sorted(
        (cm_all_terms & mi_non_active_or_missing_terms) - mi_all_terms - mi_rejected_terms
    )

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
            "rejected_count": len(mi_rejected),
            "non_active_or_missing_count": len(mi_non_active_or_missing),
        },
        "present_only_in_current_culturemech_aggregate": sorted(cm_all_terms - mi_known_terms),
        "absent_from_current_culturemech_aggregate": sorted(mi_all_terms - cm_all_terms),
        "culturemech_labels_with_rejected_mim_tombstones": rejected_only_cm_terms,
        "culturemech_labels_with_non_active_or_missing_mim_records": (
            non_active_or_missing_cm_terms
        ),
        "mediaingredientmech_rejected_tombstones": mi_rejected,
        "mediaingredientmech_non_active_or_missing_records": mi_non_active_or_missing,
        "culturemech_status_collisions": [],
        "mediaingredientmech_status_collisions": [],
        "occurrence_changes": [],
        "target_conflicts": [],
        "mim_coverage_gains": [],
        "culturemech_only_grounding": [],
        "both_unmapped": [],
    }

    for term in sorted(cm_all_terms):
        if term in cm_mapped_idx and term in cm_unmapped_idx:
            results["culturemech_status_collisions"].append(
                _status_collision(
                    term,
                    cm_mapped_idx[term],
                    cm_unmapped_idx[term],
                    "culturemech",
                )
            )

    for term in sorted(mi_all_terms):
        if term in mi_mapped_idx and term in mi_unmapped_idx:
            results["mediaingredientmech_status_collisions"].append(
                _status_collision(
                    term,
                    mi_mapped_idx[term],
                    mi_unmapped_idx[term],
                    "mediaingredientmech",
                )
            )

    # Compare common ingredients without silently choosing one side of a
    # mapped/unmapped collision. Those terms are reported above for source repair.
    common_terms = cm_all_terms & mi_all_terms

    for term in sorted(common_terms):
        cm_status = _status(cm_mapped_idx, cm_unmapped_idx, term)
        mi_status = _status(mi_mapped_idx, mi_unmapped_idx, term)
        if "_AND_" in cm_status or "_AND_" in mi_status:
            continue

        cm_ing = cm_mapped_idx[term] if cm_status == "MAPPED" else cm_unmapped_idx[term]
        mi_ing = mi_mapped_idx[term] if mi_status == "MAPPED" else mi_unmapped_idx[term]

        # Compare occurrence counts
        cm_count = cm_ing.get("occurrence_count", 0)
        mi_count = mi_ing.get("occurrence_statistics", {}).get("total_occurrences", 0)

        if cm_count != mi_count:
            results["occurrence_changes"].append(
                {
                    "term": term,
                    "culturemech_count": cm_count,
                    "mediaingredient_count": mi_count,
                    "delta": cm_count - mi_count,
                    "culturemech_status": cm_status,
                    "mediaingredientmech_status": mi_status,
                }
            )

        if cm_status == "MAPPED" and mi_status == "MAPPED":
            cm_ontology = cm_ing.get("ontology_id")
            mi_ontology = _mim_ontology_id(mi_ing)
            if cm_ontology != mi_ontology:
                results["target_conflicts"].append(
                    {
                        "term": term,
                        "culturemech_status": cm_status,
                        "mediaingredientmech_status": mi_status,
                        "culturemech_ontology": cm_ontology,
                        "mediaingredientmech_ontology": mi_ontology,
                    }
                )
        elif cm_status == "UNMAPPED" and mi_status == "MAPPED":
            results["mim_coverage_gains"].append(
                {
                    "term": term,
                    "culturemech_status": cm_status,
                    "mediaingredientmech_status": mi_status,
                    "culturemech_ontology": None,
                    "mediaingredientmech_ontology": _mim_ontology_id(mi_ing),
                }
            )
        elif cm_status == "MAPPED" and mi_status == "UNMAPPED":
            results["culturemech_only_grounding"].append(
                {
                    "term": term,
                    "culturemech_status": cm_status,
                    "mediaingredientmech_status": mi_status,
                    "culturemech_ontology": cm_ing.get("ontology_id"),
                    "mediaingredientmech_ontology": None,
                }
            )
        else:
            results["both_unmapped"].append(
                {
                    "term": term,
                    "culturemech_status": cm_status,
                    "mediaingredientmech_status": mi_status,
                    "culturemech_ontology": None,
                    "mediaingredientmech_ontology": None,
                }
            )

    # Sort occurrence changes by delta (descending)
    results["occurrence_changes"].sort(key=lambda x: abs(x["delta"]), reverse=True)

    return results


def print_comparison_report(results):
    """Print a status-aware comparison report without lifecycle overclaims."""
    print("\n" + "=" * 80)
    print("CULTUREMECH vs MEDIAINGREDIENTMECH COMPARISON")
    print("=" * 80)

    cm_date = results["culturemech"]["generation_date"]
    mi_date = results["mediaingredientmech"]["generation_date"]
    print("\nGENERATION DATES:")
    print(f"  CultureMech:         {cm_date}")
    print(f"  MediaIngredientMech: {mi_date}")
    try:
        cm_dt = datetime.fromisoformat(cm_date.replace("Z", "+00:00"))
        mi_dt = datetime.fromisoformat(mi_date.replace("Z", "+00:00"))
        age_diff = cm_dt - mi_dt
        print(f"  Age difference:      {age_diff.total_seconds() / 3600:.1f} hours")
    except (AttributeError, TypeError, ValueError):
        pass

    cm = results["culturemech"]
    mi = results["mediaingredientmech"]
    print("\nINGREDIENT COUNTS:")
    print(f"  {'':30s} {'CultureMech':>15s} {'MediaIngMech':>15s} {'Delta':>10s}")
    print(f"  {'-' * 70}")
    for label, key in (
        ("Active mapped ingredients", "mapped_count"),
        ("Active unmapped ingredients", "unmapped_count"),
        ("Unique active labels", "total_count"),
    ):
        print(f"  {label:30s} {cm[key]:>15,} {mi[key]:>15,} {cm[key] - mi[key]:>10,}")
    print(f"  {'MIM REJECTED tombstones':30s} {'n/a':>15s} {mi['rejected_count']:>15,}")
    if mi["non_active_or_missing_count"]:
        print(
            f"  {'MIM other non-active/missing':30s} "
            f"{'n/a':>15s} {mi['non_active_or_missing_count']:>15,}"
        )

    print("\nMEDIA COLLECTION:")
    print(f"  CultureMech media count: {cm['media_count']:,}")
    print(f"  Total ingredient instances: {cm['total_instances']:,}")

    present_only = results["present_only_in_current_culturemech_aggregate"]
    absent = results["absent_from_current_culturemech_aggregate"]
    if present_only:
        print(f"\n⚠️  PRESENT ONLY IN CURRENT CULTUREMECH AGGREGATE ({len(present_only)}):")
        for index, term in enumerate(present_only[:20], 1):
            print(f"  {index:2d}. {term}")
        if len(present_only) > 20:
            print(f"  ... and {len(present_only) - 20} more")
    else:
        print("\n✅ No labels unique to the current CultureMech aggregate")

    if absent:
        print(
            "\nℹ️  ABSENT FROM CURRENT CULTUREMECH AGGREGATE "
            f"({len(absent)}; not evidence of removal):"
        )
        for index, term in enumerate(absent[:20], 1):
            print(f"  {index:2d}. {term}")
        if len(absent) > 20:
            print(f"  ... and {len(absent) - 20} more")
    else:
        print("\n✅ Every MIM label occurs in the current CultureMech aggregate")

    rejected_tombstones = results["mediaingredientmech_rejected_tombstones"]
    rejected_cm_matches = results["culturemech_labels_with_rejected_mim_tombstones"]
    print(
        f"\nℹ️  MIM REJECTED TOMBSTONES ({len(rejected_tombstones)}; excluded from "
        "active comparisons)"
    )
    if rejected_cm_matches:
        print(
            "  CultureMech labels matching only a rejected MIM tombstone "
            f"({len(rejected_cm_matches)}):"
        )
        for term in rejected_cm_matches[:20]:
            print(f"    - {term}")
        if len(rejected_cm_matches) > 20:
            print(f"    ... and {len(rejected_cm_matches) - 20} more")

    non_active_or_missing_records = results["mediaingredientmech_non_active_or_missing_records"]
    non_active_cm_matches = results["culturemech_labels_with_non_active_or_missing_mim_records"]
    if non_active_or_missing_records:
        print(
            "\nℹ️  MIM RECORDS WITH OTHER NON-ACTIVE OR MISSING STATUS "
            f"({len(non_active_or_missing_records)}; excluded):"
        )
        for record in non_active_or_missing_records[:20]:
            print(f"  {record['term']}: {record['mapping_status']}")
        if non_active_cm_matches:
            print(
                "  CultureMech labels matching only one of these excluded records "
                f"({len(non_active_cm_matches)}):"
            )
            for term in non_active_cm_matches[:20]:
                print(f"    - {term}")

    cm_collisions = results["culturemech_status_collisions"]
    if cm_collisions:
        print(f"\n⚠️  CULTUREMECH MAPPED/UNMAPPED COLLISIONS ({len(cm_collisions)}):")
        for collision in cm_collisions[:20]:
            print(
                f"  {collision['term']}: mapped={collision['mapped_ontology']}, "
                f"mapped occurrences={collision['mapped_occurrence_count']}, "
                f"unmapped occurrences={collision['unmapped_occurrence_count']}"
            )
        if len(cm_collisions) > 20:
            print(f"  ... and {len(cm_collisions) - 20} more")

    mi_collisions = results["mediaingredientmech_status_collisions"]
    if mi_collisions:
        print(f"\n⚠️  MEDIAINGREDIENTMECH MAPPED/UNMAPPED COLLISIONS ({len(mi_collisions)}):")
        for collision in mi_collisions[:20]:
            print(
                f"  {collision['term']}: mapped={collision['mapped_ontology']}, "
                f"mapped occurrences={collision['mapped_occurrence_count']}, "
                f"unmapped occurrences={collision['unmapped_occurrence_count']}"
            )
        if len(mi_collisions) > 20:
            print(f"  ... and {len(mi_collisions) - 20} more")

    occ_changes = results["occurrence_changes"]
    if occ_changes:
        print(f"\n⚠️  OCCURRENCE COUNT CHANGES ({len(occ_changes)} labels):")
        for change in occ_changes[:15]:
            statuses = f"{change['culturemech_status']}↔{change['mediaingredientmech_status']}"
            print(
                f"  {change['term']} ({statuses}): "
                f"{change['culturemech_count']:,} vs "
                f"{change['mediaingredient_count']:,} "
                f"({change['delta']:+,})"
            )
        if len(occ_changes) > 15:
            print(f"  ... and {len(occ_changes) - 15} more")
    else:
        print("\n✅ No occurrence count changes")

    target_conflicts = results["target_conflicts"]
    if target_conflicts:
        print(f"\n⚠️  MAPPED↔MAPPED TARGET CONFLICTS ({len(target_conflicts)}):")
        for change in target_conflicts[:10]:
            print(f"  {change['term']}:")
            print(f"    CultureMech:         {change['culturemech_ontology']}")
            print(f"    MediaIngredientMech: {change['mediaingredientmech_ontology']}")
        if len(target_conflicts) > 10:
            print(f"  ... and {len(target_conflicts) - 10} more")
    else:
        print("\n✅ No mapped↔mapped ontology target conflicts")

    mim_gains = results["mim_coverage_gains"]
    if mim_gains:
        print(f"\nℹ️  MIM GROUNDING COVERAGE GAINS ({len(mim_gains)}):")
        for change in mim_gains[:10]:
            print(f"  {change['term']} -> {change['mediaingredientmech_ontology']}")
        if len(mim_gains) > 10:
            print(f"  ... and {len(mim_gains) - 10} more")

    cm_only_grounding = results["culturemech_only_grounding"]
    if cm_only_grounding:
        print(f"\n⚠️  CULTUREMECH-ONLY GROUNDING ({len(cm_only_grounding)}):")
        for change in cm_only_grounding[:10]:
            print(f"  {change['term']} -> {change['culturemech_ontology']}")
        if len(cm_only_grounding) > 10:
            print(f"  ... and {len(cm_only_grounding) - 10} more")

    both_unmapped = results["both_unmapped"]
    if both_unmapped:
        print(f"\nℹ️  UNMAPPED IN BOTH SOURCES ({len(both_unmapped)})")

    print("\n" + "=" * 80)
    print("RECOMMENDATION")
    print("=" * 80)
    needs_review = (
        bool(present_only)
        or bool(occ_changes)
        or bool(target_conflicts)
        or bool(mim_gains)
        or bool(cm_only_grounding)
        or bool(cm_collisions)
        or bool(mi_collisions)
        or bool(rejected_cm_matches)
        or bool(non_active_or_missing_records)
    )

    if needs_review:
        print("\n⚠️  SOURCE REVIEW RECOMMENDED")
        print("\nReasons:")
        if present_only:
            print(f"  • {len(present_only)} labels occur only in the current CultureMech aggregate")
        if occ_changes:
            label_word = "label" if len(occ_changes) == 1 else "labels"
            verb = "has" if len(occ_changes) == 1 else "have"
            print(f"  • {len(occ_changes)} {label_word} {verb} occurrence count changes")
        if target_conflicts:
            print(f"  • {len(target_conflicts)} mapped labels have target conflicts")
        if mim_gains:
            print(f"  • {len(mim_gains)} labels are grounded only in MIM")
        if cm_only_grounding:
            print(f"  • {len(cm_only_grounding)} labels are grounded only in CultureMech")
        if cm_collisions:
            print(
                f"  • {len(cm_collisions)} CultureMech labels occur in both mapped "
                "and unmapped aggregates"
            )
        if mi_collisions:
            print(
                f"  • {len(mi_collisions)} MIM labels occur in both mapped and unmapped collections"
            )
        if rejected_cm_matches:
            print(
                f"  • {len(rejected_cm_matches)} CultureMech labels match only a "
                "rejected MIM tombstone"
            )
        if non_active_or_missing_records:
            print(
                f"  • {len(non_active_or_missing_records)} MIM records have another "
                "non-active or missing mapping_status"
            )

        print("\nRecommended action:")
        print("  1. Review the detailed status-aware comparison report")
        print("  2. Treat target conflicts, coverage gaps, and collisions separately")
        print("  3. Apply accepted changes through focused curation tooling")
        print("  4. Preserve source evidence and append curation history")
        print("  5. Run 'just sync-curated' and 'just qc'")
        print("\nDo not bulk-import these aggregates. The legacy importer is retired")
        print("because it overwrote MIM-owned curation with lossy, invalid records (#453).")
    else:
        print("\n✅ NO ACTIONABLE SOURCE DIFFERENCES DETECTED")
        if absent:
            print(
                "\nMIM-only labels were observed, but aggregate absence alone is not "
                "evidence of upstream removal."
            )
        else:
            print("\nThe compared CultureMech aggregate and MIM records agree")

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
