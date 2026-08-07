#!/usr/bin/env python3
"""Record the nearest ontology parent on records that stay UNMAPPED.

The Edison sweep found high-confidence parents for records it also, correctly,
refused to ground: `Calf brains` is brain tissue, `Larchwood xylan` is xylan from
a named wood. The reports forbid asserting identity — for Calf brains, in as many
words: "do **not** assert `skos:exactMatch` or `skos:closeMatch` to
`UBERON:0000955`". Both of those predicates license node substitution, which is
false here; a source-qualified preparation is not interchangeable with the
substance it is prepared from.

But "no identity" is not "no information", and this repo already has the shape
for that. Six UNMAPPED records carry an `ontology_mapping` with
`mapping_quality: NARROW_MATCH` and **no SSSOM row** — `Inorganic salts-starch
agar` holds CHEBI:24839 with the curation note "retained CHEBI inorganic salt
parent mapping only as contextual curation". `reconcile_sssom.py` reports no GAP
for them, because an UNMAPPED record is not expected to publish a row.

So the parent is recorded where a curator will see it, and nothing is published
to kg-microbe. This is the conservative half of #294, applied only where the
record is a source- or grade-qualified preparation of exactly the parent named.

Deliberately excluded after checking the labels against the local builds:

    Sigmacell alpha Type 50 -> CHEBI:62967 is "amorphous cellulose", and a
        Type 50 particulate grade is not established to be the amorphous form
    MnCl4 x 6 H2O -> CHEBI:86368 is manganese(II) chloride TETRAhydrate against
        a label naming six waters, and the report calls the label malformed and
        "not sufficiently" determined

Run once, then delete.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
import yaml
from mediaingredientmech.utils.yaml_handler import save_yaml

UNMAPPED = ROOT / "data" / "curated" / "unmapped_ingredients.yaml"
STAMP = "2026-08-07T00:00:00+00:00"

# preferred_term -> (parent CURIE, parent label as the local build spells it,
#                   source enum, why this record is narrower than that parent)
PARENTS = {
    "Calf brains": (
        "UBERON:0000955", "brain", "UBERON",
        "brain tissue from a calf; the report calls UBERON:0000955 a "
        "\"high-confidence anatomical-source annotation\" while explicitly "
        "refusing exactMatch and closeMatch, which is exactly this shape"),
    "Cow manure": (
        "ENVO:00003031", "animal manure", "ENVO",
        "manure from one named animal; ENVO:00003031 is the unqualified class"),
    "Chitin from shrimp shells": (
        "CHEBI:17029", "chitin", "CHEBI",
        "the report calls it \"a source-qualified polymer preparation, not a "
        "uniquely defined small molecule\"; chitin is that source-free polymer"),
    "Larchwood xylan": (
        "CHEBI:37166", "xylan", "CHEBI",
        "xylan from a named wood; the report refuses even the generic xylan CAS "
        "because it \"would not resolve larchwood specificity\", which is the "
        "argument for narrower-than, not for silence"),
    "dextran, Mw ~1,270": (
        "CHEBI:52071", "dextran", "CHEBI",
        "dextran qualified by a molecular weight the parent class does not carry"),
}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    doc = yaml.safe_load(UNMAPPED.read_text())
    n = 0
    for rec in doc["ingredients"]:
        term = (rec.get("preferred_term") or "").strip()
        if term not in PARENTS:
            continue
        curie, label, source, why = PARENTS[term]

        if (rec.get("ontology_mapping") or {}).get("ontology_id"):
            print(f"  SKIP {term}: already holds "
                  f"{rec['ontology_mapping']['ontology_id']}")
            continue
        if rec.get("mapping_status") not in ("UNMAPPED", "NEEDS_EXPERT"):
            print(f"  SKIP {term}: status is {rec.get('mapping_status')}")
            continue

        rec["ontology_mapping"] = {
            "ontology_id": curie,
            "ontology_label": label,
            "ontology_source": source,
            "mapping_quality": "NARROW_MATCH",
            "evidence": [{
                "evidence_type": "LITERATURE",
                "source": "Edison LITERATURE (PaperQA3) identity research",
                "notes": f"Parent class, not identity: {why}.",
            }],
        }
        rec.setdefault("curation_history", []).append({
            "timestamp": STAMP,
            "curator": "edison_contextual_parent",
            "action": "ADDED_PARENT_CONTEXT",
            "changes": (
                f"Recorded {curie} ({label}) as the nearest ontology parent with "
                f"mapping_quality=NARROW_MATCH: {why}. Status stays UNMAPPED and "
                "NO SSSOM row is published — this follows the existing contextual "
                "pattern on Inorganic salts-starch agar (CHEBI:24839, \"retained "
                "... only as contextual curation\") and five sibling records. "
                "exactMatch/closeMatch are withheld deliberately: they license "
                "node substitution, and a source- or grade-qualified preparation "
                "is not interchangeable with the substance it is prepared from. "
                "Whether this pattern should instead publish a skos:narrowMatch "
                "row is the open question in #294."),
            "llm_assisted": True,
        })
        n += 1
        print(f"  {term[:34]:36} -> {curie} ({label})")

    if args.apply and n:
        save_yaml(doc, UNMAPPED, validate=True, target_class="IngredientCollection")
        print(f"\nrecorded a parent on {n} record(s)")
    else:
        print(f"\n{n} record(s) would get a parent (dry-run)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
