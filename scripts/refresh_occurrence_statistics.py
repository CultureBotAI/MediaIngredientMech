#!/usr/bin/env python3
"""Refresh occurrence_statistics from CultureMech's lossless occurrence table (#449).

The stored counts came from the bulk importer retired in #453, which derived
`media_count` from an occurrence list CultureMech had already truncated to 50
examples. The truncation is still visible in the corpus: 39 records sit at
exactly 50 against a local density of ~2, and `ZnCl2` claims 1579 occurrences
across "50" media.

CultureMech#337 replaced that aggregator. Its `ingredient_occurrences.tsv` is a
row per (recipe, component) carrying the stable `CultureMech:` recipe id, with
no cap, so both counts can be derived honestly:

    media_count       = distinct recipe_id
    total_occurrences = row count

Matching is by `identifier` == `resolved_identifier` -- a stable id on both
sides. Names are never used: CultureMech recipe names are not unique (2291 are
shared, 4784 recipes have none), and MIM has its own label-drift history.

Records with no match are LEFT ALONE rather than zeroed. Absence from a scan can
mean the ingredient is genuinely gone or that resolution changed upstream, and
those are different facts; the report lists the ones holding a non-zero count so
a curator can look.

This writes the COLLECTION (`data/curated/`), like `audit_occurrence_stats`
does, so it must be followed by `just sync-individual` to project onto the
per-record tree. `just sync-curated` is the opposite direction and silently
reverts this write -- it aggregates the stale per-record files back over the
collection. That happened once while writing this; the corpus-level test is
what caught it.

Usage:
    python scripts/refresh_occurrence_statistics.py --occurrences PATH
    python scripts/refresh_occurrence_statistics.py --occurrences PATH --apply
    just sync-individual
"""

from __future__ import annotations

import argparse
import csv
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.curation.ingredient_curator import IngredientCurator

DATA = Path("data/curated/mapped_ingredients.yaml")
REPORT = Path("reports/occurrence_statistics_refresh.tsv")

# `ingredient_json` carries a whole serialized component, so rows blow past the
# default 128 KiB field cap.
csv.field_size_limit(1 << 30)


def source_provenance(path: Path, rows: int, recipes: int) -> str:
    """Where these numbers came from, in one line (#486).

    The values this replaces were untraceable -- nothing recorded that a
    media_count of 50 came from a truncated list, and establishing it took a
    distribution analysis. Writing fresh numbers with the same gap would repeat
    that. CultureMech is actively changing (#337 landed hours before this run,
    and identity resolution changed just before it), so the vintage is what
    makes a count interpretable later.
    """
    sha = "unknown"
    try:
        result = subprocess.run(
            ["git", "-C", str(path.resolve().parent), "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            sha = result.stdout.strip() or "unknown"
    except (OSError, subprocess.SubprocessError):
        pass
    return (f"source={path.name} culturemech_rev={sha} "
            f"rows={rows} distinct_recipes={recipes}")


def read_occurrences(path: Path) -> tuple[dict[str, tuple[int, int]], int, int]:
    """(identifier -> (distinct recipes, rows), total rows, total distinct recipes).

    The two totals are corpus-wide, not sums of the per-identifier figures --
    summing those double-counts every recipe that lists more than one mapped
    ingredient, which is nearly all of them. They exist so a partial or
    truncated input is visible in the provenance line (#486).
    """
    recipes: dict[str, set[str]] = defaultdict(set)
    rows: dict[str, int] = defaultdict(int)
    all_recipes: set[str] = set()
    total_rows = 0
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        for field in ("resolved_identifier", "recipe_id"):
            if field not in (reader.fieldnames or []):
                raise SystemExit(
                    f"error: {path} has no {field!r} column; this needs the "
                    "CultureMech#337 occurrence table, not the pre-#337 aggregate."
                )
        for row in reader:
            identifier = (row.get("resolved_identifier") or "").strip()
            if not identifier:
                continue
            recipes[identifier].add(row["recipe_id"])
            rows[identifier] += 1
            all_recipes.add(row["recipe_id"])
            total_rows += 1
    return ({k: (len(v), rows[k]) for k, v in recipes.items()},
            total_rows, len(all_recipes))


def shared_identifiers(records: list[dict]) -> set[str]:
    """Identifiers carried by more than one MIM record (#225 / #334).

    These counts are per-identifier, so every record sharing one receives the
    same value -- `MgSO4 x 7 H2O` and `MgSO4·H2O` both take the heptahydrate's
    5619. That is the honest per-identifier reading, but it means media_count
    MUST NOT be summed across records, and it means a hydrate cohort still
    awaiting split inherits its family's total. Flagged in the report rather
    than silently applied.
    """
    seen: dict[str, int] = defaultdict(int)
    for record in records:
        seen[str(record.get("identifier") or "")] += 1
    return {k for k, n in seen.items() if n > 1 and k}


def plan(records: list[dict], fresh: dict[str, tuple[int, int]]) -> tuple[list, list]:
    """(changes, unmatched-but-non-zero) without mutating anything."""
    changes, stranded, rejected = [], [], []
    for record in records:
        identifier = str(record.get("identifier") or "")
        if record.get("mapping_status") == "REJECTED":
            # A REJECTED record was merged into a representative and its counts
            # deliberately transferred there; `audit_occurrence_stats` calls a
            # REJECTED record with occurrences an inconsistency. Refreshing one
            # resurrects a count curation had zeroed -- a small version of the
            # "bulk import overwrites MIM-owned curation" failure that retired
            # the importer in #453. Skipped, and reported.
            rejected.append(record)
            continue
        stats = record.get("occurrence_statistics")
        stats = stats if isinstance(stats, dict) else {}
        old = (stats.get("media_count") or 0, stats.get("total_occurrences") or 0)
        if identifier not in fresh:
            if old[0] or old[1]:
                stranded.append((record, old))
            continue
        new = fresh[identifier]
        if new != old:
            changes.append((record, old, new))
    return changes, stranded, rejected


def apply(changes: list, provenance: str) -> None:
    for record, old, new in changes:
        stats = record.get("occurrence_statistics")
        record["occurrence_statistics"] = {
            **(stats if isinstance(stats, dict) else {}),
            "media_count": new[0],
            "total_occurrences": new[1],
        }
        record_curation_event(
            record,
            curator="refresh_occurrence_statistics",
            action="CORRECTED",
            changes=(
                f"occurrence_statistics {old[0]}/{old[1]} -> {new[0]}/{new[1]} "
                "(media_count/total_occurrences), derived from distinct "
                "CultureMech recipe ids in the #337 occurrence table. The prior "
                "values came from the importer retired in #453, whose media_count "
                f"counted a list truncated to 50 examples (#449). [{provenance}]"
            ),
        )


def _kind(record: dict, old: tuple, new: tuple, shared: set[str]) -> str:
    """A downward move is not self-explaining the way an upward one is: it says
    the record was credited with media it no longer matches, which is benign
    re-resolution or a partial scan, and those are different facts (#487)."""
    parts = ["REFRESHED"]
    if new[0] < old[0]:
        parts.append("DECREASED")
    if record.get("identifier") in shared:
        parts.append("SHARED_IDENTIFIER")
    return "_".join(parts)


def write_report(changes: list, stranded: list, shared: set[str],
                 provenance: str) -> None:
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    with REPORT.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh, delimiter="\t", lineterminator="\n")
        writer.writerow([f"# {provenance}"])
        writer.writerow(["kind", "identifier", "preferred_term", "old_media_count",
                         "old_total_occurrences", "new_media_count",
                         "new_total_occurrences"])
        for record, old, new in changes:
            writer.writerow([
                _kind(record, old, new, shared),
                record.get("identifier", ""),
                record.get("preferred_term", ""), old[0], old[1], new[0], new[1]])
        for record, old in stranded:
            writer.writerow(["UNMATCHED_NONZERO", record.get("identifier", ""),
                             record.get("preferred_term", ""), old[0], old[1], "", ""])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--occurrences", type=Path, required=True,
                        help="CultureMech output/ingredient_occurrences.tsv (#337)")
    parser.add_argument("--apply", action="store_true",
                        help="write the refreshed counts (default: report only)")
    args = parser.parse_args()

    fresh, total_rows, total_recipes = read_occurrences(args.occurrences)
    provenance = source_provenance(args.occurrences, total_rows, total_recipes)
    print(provenance)
    curator = IngredientCurator(data_path=DATA, curator_name="refresh_occurrence_statistics")
    curator.load()
    changes, stranded, rejected = plan(curator.records, fresh)
    shared = shared_identifiers(curator.records)

    truncated = sum(1 for _, old, _ in changes if old[0] == 50)
    on_shared = sum(1 for r, _, _ in changes if r.get("identifier") in shared)
    print(f"{len(fresh)} identifiers in the occurrence table")
    print(f"{len(changes)} record(s) would change; {truncated} of them are pinned at "
          "exactly 50 (the truncation signature)")
    print(f"{len(stranded)} unmatched record(s) hold a non-zero count and are LEFT ALONE")
    print(f"{len(rejected)} REJECTED (merged) record(s) skipped -- their counts belong "
          "to the representative they were merged into")
    print(f"{on_shared} change(s) land on an identifier shared by several MIM records "
          "(#225/#334) -- they all take the same value, so media_count must not be summed")
    for record, old, new in sorted(changes, key=lambda c: -c[2][0])[:10]:
        print(f"  {str(record.get('preferred_term'))[:34]:34} "
              f"{old[0]:>6} -> {new[0]:<6} media")

    write_report(changes, stranded, shared, provenance)
    print(f"\nreport: {REPORT}")

    if not args.apply:
        print("dry run; re-run with --apply to write")
        return 0
    apply(changes, provenance)
    curator.save()
    print(f"wrote {len(changes)} record(s) to {DATA}")
    print("run `just sync-individual` to propagate into data/ingredients/ "
          "-- NOT `sync-curated`, which aggregates the other way and would\n"
          "   overwrite this write with the stale per-record files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
