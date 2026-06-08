#!/usr/bin/env python3
"""Audit (and optionally fix) occurrence_statistics consistency in the curated set.

Checks every record for:
  MISSING         — occurrence_statistics absent or total_occurrences is null
  REJECTED_NONZERO — a REJECTED (merged) record still reporting occurrences
                     (counts should have been transferred to its representative)
  NEGATIVE        — negative total_occurrences / media_count
  MEDIA_GT_OCC    — media_count greater than total_occurrences (impossible)

--check (default) prints issues and exits 1 if any (CI gate).
--fix backfills MISSING records with total_occurrences=0 / media_count=0 (these
are ontology-derived records that were never tracked in media counting) and records
a curation event. It does NOT touch the other categories — those need judgement.

Usage:
    python scripts/audit_occurrence_stats.py
    python scripts/audit_occurrence_stats.py --fix
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.curation.ingredient_curator import IngredientCurator

DATA = Path("data/curated/mapped_ingredients.yaml")


def find_issues(records: list[dict]) -> dict[str, list]:
    issues = {"missing": [], "rejected_nonzero": [], "negative": [], "media_gt_occ": []}
    for r in records:
        ident = r.get("identifier")
        st = r.get("occurrence_statistics")
        # Treat absent, non-mapping, or partially-populated stats as MISSING; the
        # later numeric checks then only run when both counts are present.
        if not isinstance(st, dict):
            issues["missing"].append(ident)
            continue
        occ = st.get("total_occurrences")
        mc = st.get("media_count")
        if occ is None or mc is None:
            issues["missing"].append(ident)
            continue
        if r.get("mapping_status") == "REJECTED" and occ > 0:
            issues["rejected_nonzero"].append((ident, occ))
        if occ < 0 or mc < 0:
            issues["negative"].append((ident, occ, mc))
        if mc > occ:
            issues["media_gt_occ"].append((ident, occ, mc))
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fix", action="store_true", help="Backfill MISSING with 0/0")
    args = parser.parse_args()

    curator = IngredientCurator(data_path=DATA, curator_name="audit_occurrence_stats")
    curator.load()
    issues = find_issues(curator.records)

    print("occurrence_statistics audit:")
    for k in ("missing", "rejected_nonzero", "negative", "media_gt_occ"):
        print(f"  {k}: {len(issues[k])}", issues[k][:8] if issues[k] else "")

    if not args.fix:
        total = sum(len(v) for v in issues.values())
        if total == 0:
            print("\nOK: occurrence_statistics are consistent.")
            return 0
        print(f"\n{total} issue(s). Backfill MISSING with --fix; resolve others by hand.")
        return 1

    by_ident = {r.get("identifier"): r for r in curator.records}
    n = 0
    for ident in issues["missing"]:
        rec = by_ident[ident]
        st = rec.get("occurrence_statistics")
        st = st if isinstance(st, dict) else {}
        # Preserve any value that is present; only fill the missing count(s).
        rec["occurrence_statistics"] = {
            "total_occurrences": st.get("total_occurrences") or 0,
            "media_count": st.get("media_count") or 0,
        }
        record_curation_event(
            rec,
            curator="audit_occurrence_stats",
            action="CORRECTED",
            changes="Backfilled missing occurrence_statistics (0/0): ontology-derived "
            "record with no tracked media occurrences.",
        )
        n += 1
    curator.save()
    print(f"\nBackfilled {n} record(s). (Other categories, if any, left for manual review.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
