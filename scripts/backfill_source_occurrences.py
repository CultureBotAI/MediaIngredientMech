#!/usr/bin/env python3
"""Carry the microbedecoder prevalence signal onto its imported records (#196).

The import wrote `total_occurrences: 0 / media_count: 0` for every
microbedecoder-derived record. That is *correct* for those two fields — they count
CultureMech media recipes, and these labels come from BacDive traits / Bergey
substrates, not recipes — but it discarded the source's own occurrence counts
entirely (`esculin` 3569, `indole` 6005, `D-glucose` 3377). That abundance signal
is what ranked the candidates worth onboarding in the first place, so anything
downstream weighting ingredients by prevalence saw several hundred zero-weight
records.

This writes those counts to `occurrence_statistics.source_occurrences`, which is
source-scoped and so cannot inflate the media counts (#196 option 2). Idempotent:
re-running replaces the microbedecoder entry rather than appending a second one.

    python scripts/backfill_source_occurrences.py            # dry-run
    python scripts/backfill_source_occurrences.py --apply
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
import yaml
from mediaingredientmech.utils.yaml_handler import save_yaml

CURATED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
UNMAPPED = ROOT / "data" / "curated" / "unmapped_ingredients.yaml"
SOURCE = ROOT / "data" / "custom" / "microbedecoder" / "unmapped_labels.tsv"
SOURCE_NAME = "microbedecoder"


def _source_index() -> dict[str, dict]:
    """label (casefolded) -> source row. The label is the only join key the import kept."""
    index: dict[str, dict] = {}
    for row in csv.DictReader(SOURCE.read_text().splitlines(), delimiter="\t"):
        label = (row.get("label") or "").strip().lower()
        if not label:
            continue
        # Keep the highest count when a label repeats across categories: the counts
        # are per (label, category) and we are recording prevalence of the label.
        prev = index.get(label)
        if prev is None or int(row.get("occurrences") or 0) > int(prev.get("occurrences") or 0):
            index[label] = row
    return index


def _is_microbedecoder(rec: dict) -> bool:
    """Records whose provenance names the source, however it was recorded."""
    blob = yaml.safe_dump(
        {k: rec.get(k) for k in ("ontology_mapping", "curation_history", "synonyms")},
        default_flow_style=False,
    ).lower()
    return SOURCE_NAME in blob


def backfill(collection: Path, index: dict, apply: bool) -> tuple[int, int]:
    data = yaml.safe_load(collection.read_text())
    changed = skipped = 0
    for rec in data.get("ingredients") or []:
        if not _is_microbedecoder(rec):
            continue
        label = (rec.get("preferred_term") or "").strip().lower()
        row = index.get(label)
        if row is None:
            skipped += 1
            continue
        count = int(row.get("occurrences") or 0)
        if count <= 0:
            skipped += 1
            continue
        stats = rec.setdefault("occurrence_statistics", {})
        stats.setdefault("total_occurrences", 0)
        stats.setdefault("media_count", 0)
        entries = [e for e in (stats.get("source_occurrences") or [])
                   if e.get("source") != SOURCE_NAME]
        entries.append({
            "source": SOURCE_NAME,
            "count": count,
            "source_columns": (row.get("source_columns") or "").strip(),
        })
        stats["source_occurrences"] = entries
        changed += 1
    if apply and changed:
        save_yaml(data, collection, validate=True, target_class="IngredientCollection")
    return changed, skipped


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="write (default: dry-run)")
    args = ap.parse_args()

    index = _source_index()
    print(f"source labels: {len(index)}")
    total_changed = 0
    for path in (CURATED, UNMAPPED):
        if not path.exists():
            continue
        changed, skipped = backfill(path, index, args.apply)
        total_changed += changed
        print(f"  {path.name}: {changed} record(s) carry a source count, {skipped} without one")

    if not args.apply:
        print("\n(dry-run — pass --apply to write)")
    else:
        print(f"\nApplied to {total_changed} record(s). Now run: just export-individual, "
              "just export-lists, just export-browser")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
