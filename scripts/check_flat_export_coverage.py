"""Every raw label MIM knows must be resolvable from a published flat artifact (#229).

MIM's job is turning a raw ingredient string from a medium recipe into an
ontology term. Consumers do that by joining against the published flat
artifacts -- `docs/data/all_ingredients.csv` or the SSSOM TSV.

Merging a duplicate deletes its record and keeps the raw label only as a
synonym on the target, and merges add no SSSOM row (SSSOM subjects are
preferred_terms of MAPPED records, never synonyms). So before #229 a merged
label was published nowhere: `D-lactate` resolved to UNMAPPED_0654 before
PR #227 and to nothing after it. Per-record coverage went up while the surface
consumers actually use went down, and every existing gate stayed green --
reconcile was GAP/ORPHAN/STALE 0, roundtrip clean, duplicate-ids clean.

This asserts the property those gates cannot see: for every record in the
curated collections, its preferred_term AND all of its synonyms appear in
`docs/data/all_ingredients.csv`. Exits 2 on any gap.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
COLLECTIONS = (ROOT / "data" / "curated" / "mapped_ingredients.yaml",
               ROOT / "data" / "curated" / "unmapped_ingredients.yaml")
FLAT = ROOT / "docs" / "data" / "all_ingredients.csv"
SEP = "|"


def curated_labels() -> dict[str, list[str]]:
    """label -> the record identifier(s) that answer to it."""
    out: dict[str, list[str]] = {}
    for path in COLLECTIONS:
        doc = yaml.safe_load(path.read_text()) or {}
        for rec in doc.get("ingredients") or []:
            ident = str(rec.get("identifier", "?"))
            labels = [rec.get("preferred_term")]
            labels += [(s or {}).get("synonym_text") for s in (rec.get("synonyms") or [])]
            for lab in labels:
                if lab:
                    out.setdefault(lab, []).append(ident)
    return out


def published_labels() -> set[str]:
    if not FLAT.exists():
        print(f"ERROR: {FLAT.relative_to(ROOT)} does not exist — run `just export-lists`.")
        raise SystemExit(2)
    found: set[str] = set()
    with FLAT.open(newline="") as fh:
        reader = csv.DictReader(fh)
        if "synonyms" not in (reader.fieldnames or []):
            print(f"ERROR: {FLAT.relative_to(ROOT)} has no `synonyms` column, so every "
                  "merged raw label is unpublished. Regenerate with `just export-lists`.")
            raise SystemExit(2)
        for row in reader:
            if row.get("preferred_term"):
                found.add(row["preferred_term"])
            for s in (row.get("synonyms") or "").split(SEP):
                if s:
                    found.add(s)
    return found


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--limit", type=int, default=20, help="how many gaps to print")
    args = ap.parse_args()

    curated = curated_labels()
    published = published_labels()
    missing = sorted(lab for lab in curated if lab not in published)

    print(f"{len(curated)} distinct raw label(s) across the curated collections")
    print(f"{len(published)} resolvable from {FLAT.relative_to(ROOT)}")

    if not missing:
        print("\nOK: every curated label is published.")
        return 0

    print(f"\nERROR: {len(missing)} label(s) are known to MIM but resolve to nothing "
          f"in {FLAT.relative_to(ROOT)}")
    for lab in missing[:args.limit]:
        print(f"  {lab!r}  (record {', '.join(curated[lab])})")
    if len(missing) > args.limit:
        print(f"  ... and {len(missing) - args.limit} more")
    print("\nUsually this means docs/data/ is stale — run `just export-lists`. If it "
          "persists, an export path is dropping labels.")
    return 2


if __name__ == "__main__":
    sys.exit(main())
