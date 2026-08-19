#!/usr/bin/env python3
"""Publish each record's CAS-RN into the SSSOM `other` column, so it reaches KGX.

Decided 2026-08-18: the knowledge-graph node should optimise for **how it
reads**, while the CAS-RN — the thing you actually order by — travels as a
**synonym** so it stays findable. This writes the second half.

## The propagation path, verified rather than assumed

kg-microbe's consolidator, for symmetric rows only:

    synonyms = [s for s in (subject_label, object_label) if s]
    if other:
        synonyms.extend(s.strip() for s in other.split("|") if s.strip())

(`scripts/consolidate_chemical_mappings.py`, the `predicate in symmetric`
branch.) So a pipe-separated entry in `other` becomes a synonym on the ontology
entity, and from there a KGX synonym. 1,366 rows already use the column this way
for chemical aliases; this adds the CAS to it.

Asymmetric rows are deliberately untouched: kg-microbe does not merge their
labels into the parent entity — that was the fix for the bug where
`find_chebi_by_name("Vermont Soil")` returned `ENVO:00001998 (soil)` — so a CAS
added there would be dropped, and adding it anyway would imply the parent is
purchasable under the child's CAS.

## Why `CAS:` prefixed

`9004-32-4` alone is a bare number that a synonym search cannot distinguish from
a catalogue code or a concentration. `CAS:9004-32-4` is self-describing and
matches how the curie_map already writes the prefix.

## What this does NOT do

It does not decide identity. A record's `chemical_properties.cas_rn` describes
the substance the record denotes; where the *purchasable* form differs, that
belongs in the `supplied_form` slot, and this script publishes
`supplied_form[].cas_rn` in preference when present — that is the number a lab
would order by.

    python scripts/publish_cas_as_synonym.py            # dry-run
    python scripts/publish_cas_as_synonym.py --apply
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
import yaml  # noqa: E402

MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
SYMMETRIC = {"skos:exactMatch", "skos:closeMatch"}


def cas_for(rec: dict) -> str | None:
    """The CAS a lab would order by, preferring the supplied form."""
    for sf in rec.get("supplied_form") or []:
        if (sf or {}).get("cas_rn"):
            return str(sf["cas_rn"]).strip()
    return (str((rec.get("chemical_properties") or {}).get("cas_rn") or "").strip()
            or None)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    recs = {str(r.get("preferred_term")): r
            for r in (yaml.safe_load(MAPPED.read_text(encoding="utf-8")) or {}
                      ).get("ingredients", [])}

    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    hdr_i = next(i for i, l in enumerate(lines) if l.startswith("subject_id"))
    cols = lines[hdr_i].rstrip("\n").split("\t")
    other_i = cols.index("other")
    pred_i, subj_i = cols.index("predicate_id"), cols.index("subject_label")

    added, already, skipped_asym, no_cas = 0, 0, 0, 0
    out = []
    for i, line in enumerate(lines):
        if i <= hdr_i or line.startswith("#"):
            out.append(line)
            continue
        cells = line.rstrip("\n").split("\t")
        if len(cells) <= other_i:
            out.append(line)
            continue
        if cells[pred_i] not in SYMMETRIC:
            skipped_asym += 1
            out.append(line)
            continue
        rec = recs.get(cells[subj_i])
        cas = cas_for(rec) if rec else None
        if not cas:
            no_cas += 1
            out.append(line)
            continue
        token = f"CAS:{cas}"
        parts = [p for p in cells[other_i].split("|") if p.strip()]
        if any(p.strip().lower() == token.lower() for p in parts):
            already += 1
            out.append(line)
            continue
        parts.append(token)
        cells[other_i] = "|".join(parts)
        added += 1
        out.append("\t".join(cells) + "\n")

    if args.apply and added:
        SSSOM.write_text("".join(out), encoding="utf-8")

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'}\n")
    print(f"  CAS added to `other` on {added} symmetric row(s)")
    print(f"  already present   : {already}")
    print(f"  no CAS on record  : {no_cas}")
    print(f"  asymmetric, skipped by design: {skipped_asym}")
    print("\n  These become synonyms on the ontology entity in kg-microbe, and "
          "from there KGX.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
