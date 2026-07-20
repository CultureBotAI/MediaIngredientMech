#!/usr/bin/env python3
"""Verify every MICRO id used by MIM against EBI OLS4.

MicrO mints ~1,472 of its 3,450 classes under a malformed IRI
(`…/obo/MicrO.owl/MICRO_nnnnnnn`). Those CURIEs do not round-trip and must not be
emitted. The defect is invisible offline, so this checks each id against OLS4 and
prints the set to paste into `mediaingredientmech.curie.MICRO_VERIFIED`.

Usage:  python scripts/verify_micro_ids.py [--curies MICRO:0000182 ...]
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def micro_ids_in_sssom() -> set[str]:
    p = REPO / "mappings" / "ingredient_mappings.sssom.tsv"
    if not p.exists():
        return set()
    with p.open() as f:
        rows = csv.DictReader((l for l in f if not l.startswith("#")), delimiter="\t")
        return {(r.get("object_id") or "").strip() for r in rows
                if (r.get("object_id") or "").startswith("MICRO:")}


def check(curie: str) -> tuple[bool, str, str]:
    url = ("https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?obo_id="
           + urllib.parse.quote(curie))
    try:
        d = json.load(urllib.request.urlopen(url, timeout=30))
    except Exception as exc:
        return False, f"ERR:{type(exc).__name__}", ""
    terms = d.get("_embedded", {}).get("terms", [])
    if not terms:
        return False, "NOT_FOUND", ""
    t = terms[0]
    iri, label = t.get("iri", ""), t.get("label", "")
    if "MicrO.owl/" in iri:
        return False, "MALFORMED_IRI", label
    if not t.get("is_defining_ontology"):
        return False, "NOT_DEFINING", label
    return True, "OK", label


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--curies", nargs="*", help="explicit ids (default: those in the SSSOM)")
    args = ap.parse_args()

    ids = sorted(set(args.curies) if args.curies else micro_ids_in_sssom())
    if not ids:
        print("no MICRO ids to check", file=sys.stderr)
        return 0

    good, bad = [], []
    for c in ids:
        ok, why, label = check(c)
        (good if ok else bad).append((c, why, label))
        time.sleep(0.05)

    print(f"checked {len(ids)}: {len(good)} good, {len(bad)} problematic\n")
    if bad:
        print("PROBLEMATIC — do not emit these CURIEs:", file=sys.stderr)
        for c, why, label in bad:
            print(f"  {c}  {why}  {label!r}", file=sys.stderr)
        print("", file=sys.stderr)
    print("MICRO_VERIFIED = {")
    for c, _, label in good:
        print(f'    "{c}",  # {label}')
    print("}")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
