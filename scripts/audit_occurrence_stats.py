#!/usr/bin/env python3
"""Audit (and optionally fix) occurrence_statistics consistency in the curated set.

Checks every record for:
  MISSING         — occurrence_statistics absent or total_occurrences is null
  REJECTED_NONZERO — a REJECTED (merged) record still reporting occurrences
                     (counts should have been transferred to its representative)
  NEGATIVE        — negative total_occurrences / media_count
  MEDIA_GT_OCC    — media_count greater than total_occurrences (impossible)

--check (default) prints issues and exits 1 if any (CI gate).
Explicit validated UNKNOWN coverage is accepted for truly absent statistics.
--fix refuses missing records: absence is not evidence of zero. Counts-only
writes still require qualified source evidence and the native guarded workflow.

Usage:
    python scripts/audit_occurrence_stats.py
    python scripts/audit_occurrence_stats.py --fix
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.occurrence_coverage import Coverage, default_coverage, occurrence_view
from mediaingredientmech.curation.ingredient_curator import IngredientCurator

DATA = Path("data/curated/mapped_ingredients.yaml")


def record_address(record: dict) -> tuple[str, str]:
    """Composite address used where a semantic identifier may be shared."""
    return (
        str(record.get("identifier") or ""),
        str(record.get("preferred_term") or ""),
    )


def find_issues(records: list[dict], coverage: Coverage | None = None) -> dict[str, list]:
    issues = {"missing": [], "rejected_nonzero": [], "negative": [], "media_gt_occ": [], "invalid_type": [], "coverage": []}
    for r in records:
        address = record_address(r)
        if "occurrence_statistics" not in r and coverage is not None:
            try:
                if occurrence_view(r, coverage=coverage)["occurrence_statistics_state"] == "UNKNOWN":
                    continue
            except ValueError as exc:
                issues["coverage"].append((address, str(exc)))
                continue
        st = r.get("occurrence_statistics")
        # Treat absent, non-mapping, or partially-populated stats as MISSING; the
        # later numeric checks then only run when both counts are present.
        if not isinstance(st, dict):
            issues["missing"].append(address)
            continue
        occ = st.get("total_occurrences")
        mc = st.get("media_count")
        if occ is None or mc is None:
            issues["missing"].append(address)
            continue
        if type(occ) is not int or type(mc) is not int:
            issues["invalid_type"].append(address)
            continue
        if coverage is not None:
            try:
                if coverage.for_record(r) is not None:
                    issues["coverage"].append((address, "UNKNOWN cannot override stored counts"))
            except ValueError as exc:
                issues["coverage"].append((address, str(exc)))
        if r.get("mapping_status") == "REJECTED" and (occ > 0 or mc > 0):
            issues["rejected_nonzero"].append((address, occ))
        if occ < 0 or mc < 0:
            issues["negative"].append((address, occ, mc))
        if mc > occ:
            issues["media_gt_occ"].append((address, occ, mc))
    return issues


def backfill_missing(records: list[dict], missing: list[tuple[str, str]]) -> int:
    """Refuse inferred zeros; use the qualified guarded counts-only workflow."""
    if missing:
        raise ValueError("Cannot infer zero from missing statistics; use reviewed coverage or evidence-qualified counts")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fix", action="store_true", help="Legacy option; refuses unproven zero filling")
    args = parser.parse_args()

    curator = IngredientCurator(data_path=DATA, curator_name="audit_occurrence_stats")
    curator.load()
    issues = find_issues(curator.records, default_coverage(Path.cwd()))

    print("occurrence_statistics audit:")
    for k in issues:
        print(f"  {k}: {len(issues[k])}", issues[k][:8] if issues[k] else "")

    if not args.fix:
        total = sum(len(v) for v in issues.values())
        if total == 0:
            print("\nOK: occurrence_statistics are consistent.")
            return 0
        print(f"\n{total} issue(s). Resolve missing counts with reviewed coverage/evidence; do not infer zero.")
        return 1

    backfill_missing(curator.records, issues["missing"])
    # No automatic record writes are allowed by this audit (#1431).
    print("No records changed; numeric and coverage findings still require resolution.")
    return 1 if any(issues.values()) else 0



if __name__ == "__main__":
    sys.exit(main())
