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
import io
import sys
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
import yaml  # noqa: E402

MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
SYMMETRIC = {"skos:exactMatch", "skos:closeMatch"}


@dataclass(frozen=True)
class PublishStats:
    added: int = 0
    already: int = 0
    skipped_asym: int = 0
    no_cas: int = 0


def cas_for(rec: dict) -> str | None:
    """The CAS a lab would order by, preferring the supplied form."""
    for sf in rec.get("supplied_form") or []:
        if (sf or {}).get("cas_rn"):
            return str(sf["cas_rn"]).strip()
    return str((rec.get("chemical_properties") or {}).get("cas_rn") or "").strip() or None


def publish_cas_rows(text: str, recs: Mapping[str, dict]) -> tuple[str, PublishStats]:
    lines = text.splitlines(keepends=True)
    hdr_i = next(i for i, line in enumerate(lines) if line.startswith("subject_id"))
    reader = csv.DictReader(lines[hdr_i:], delimiter="\t")

    added, already, skipped_asym, no_cas = 0, 0, 0, 0
    body = io.StringIO()
    writer = csv.DictWriter(
        body,
        fieldnames=reader.fieldnames,
        delimiter="\t",
        lineterminator="\n",
    )
    writer.writeheader()

    for row in reader:
        if row["predicate_id"] not in SYMMETRIC:
            skipped_asym += 1
            writer.writerow(row)
            continue
        rec = recs.get(row["subject_label"])
        cas = cas_for(rec) if rec else None
        if not cas:
            no_cas += 1
            writer.writerow(row)
            continue
        token = f"CAS:{cas}"
        parts = [p for p in row["other"].split("|") if p.strip()]
        if any(p.strip().casefold() == token.casefold() for p in parts):
            already += 1
            writer.writerow(row)
            continue
        parts.append(token)
        row["other"] = "|".join(parts)
        added += 1
        writer.writerow(row)

    return "".join(lines[:hdr_i]) + body.getvalue(), PublishStats(
        added=added,
        already=already,
        skipped_asym=skipped_asym,
        no_cas=no_cas,
    )


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    recs = {
        str(r.get("preferred_term")): r
        for r in (yaml.safe_load(MAPPED.read_text(encoding="utf-8")) or {}).get("ingredients", [])
    }

    out, stats = publish_cas_rows(SSSOM.read_text(encoding="utf-8"), recs)
    if args.apply and stats.added:
        SSSOM.write_text(out, encoding="utf-8")

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'}\n")
    print(f"  CAS added to `other` on {stats.added} symmetric row(s)")
    print(f"  already present   : {stats.already}")
    print(f"  no CAS on record  : {stats.no_cas}")
    print(f"  asymmetric, skipped by design: {stats.skipped_asym}")
    kgx_message = (
        "\n  These become synonyms on the ontology entity in kg-microbe, " "and from there KGX."
    )
    print(kgx_message)
    return 0


if __name__ == "__main__":
    sys.exit(main())
