"""Report records whose label is a hydrate but whose term is not (#238).

MAPPING_SEMANTICS.md Section 3 makes a hydration state a distinct substance: it
takes a hydrate-specific ontology term if one exists, else its own `cas:` id with
a narrowMatch to the anhydrous parent. Grounding a hydrate directly onto the
anhydrous term is the identity collapse that produced the 32 families of #218.

The id-label gate cannot see this. Its `plausible` waiver compares
`ontology_id` against `ontology_label` -- the *term's own* label -- and hydrate
names live in `preferred_term`. Adding that pair to the gate surfaces 50
unrelated IMPLAUSIBLE_LABEL findings and still no hydrates, so this reports the
population directly instead: report-then-enforce, without breaking a gate first.

Compares each record's hydrate-notated preferred_term against its term's formula
from the local chebi.db. Exits 0 -- it is a measurement, not a gate.
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import sqlite3
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
REPORT = ROOT / "reports" / "hydrate_grounding.tsv"
CHEBI_DB = Path(os.path.expanduser("~/.data/oaklib/chebi.db"))

HYDRATE = re.compile(
    r"[x·•]\s*(?:\d+|n)?\s*H2\s*O|\d\s*H2\s*O"
    r"|(?<![a-z])(?:hemi|sesqui|mono|di|tri|tetra|penta|hexa|hepta|octa|nona|deca|dodeca)*"
    r"hydrate\b", re.IGNORECASE)


def formulas() -> dict[str, str]:
    if not CHEBI_DB.exists():
        # exit 2, not 0: "cannot measure" must not be indistinguishable from
        # "measured, nothing found" to anyone reading exit codes.
        print(f"ERROR: no chebi.db at {CHEBI_DB}; cannot compare formulas")
        raise SystemExit(2)
    con = sqlite3.connect(CHEBI_DB)
    q = ("select subject, value from statements "
         "where predicate like '%formula%' and subject like 'CHEBI:%'")
    return {s: v for s, v in con.execute(q)}


def anchored_subjects() -> set[str]:
    """subject_labels that carry BOTH a parent narrow/broadMatch and the Rule B1
    kgmicrobe registry row — Section 3 step 2 requires both, not just a cas: id."""
    sssom = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
    parents: set[str] = set()
    registry: set[str] = set()
    # the file opens with a commented YAML curie_map preamble; DictReader would
    # otherwise take the first comment line as the header and match nothing
    lines = sssom.read_text().splitlines(keepends=True)
    start = next(i for i, ln in enumerate(lines) if ln.startswith("subject_id"))
    with __import__("io").StringIO("".join(lines[start:])) as fh:
        r = csv.DictReader(fh, delimiter="\t")
        for row in r:
            lab, pred, obj = row.get("subject_label"), row.get("predicate_id",""), row.get("object_id","")
            if not lab:
                continue
            if pred in ("skos:narrowMatch", "skos:broadMatch"):
                parents.add(lab)
            elif pred == "skos:exactMatch" and obj.startswith("kgmicrobe."):
                registry.add(lab)
    return parents & registry


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--limit", type=int, default=25)
    args = ap.parse_args()

    form = formulas()
    anchored = anchored_subjects()
    rows = []
    for rec in yaml.safe_load(MAPPED.read_text())["ingredients"]:
        term = str(rec.get("preferred_term") or "")
        if not HYDRATE.search(term):
            continue
        ident = str(rec.get("identifier") or "")
        om = rec.get("ontology_mapping") or {}
        target = str(om.get("ontology_id") or "")
        f = form.get(target, "")
        # A bare "H2O" substring is wrong both ways: it matches `H2O4P`
        # (dihydrogenphosphate, no water at all) and misses ChEBI hydrate terms
        # written without explicit water (`Glycocholic acid hydrate` C26H43NO6).
        # Require water as its own dot-separated component, or the term's own
        # label to say hydrate.
        term_is_hydrate = bool(
            re.search(r"(?:^|\.)\(?[\dn]*H2O\)?[\dn]*(?:\.|$)", f)
            or re.search(r"hydrate\b", str(om.get("ontology_label") or ""), re.IGNORECASE))
        if ident.startswith("cas:"):
            status = ("OK_OWN_CAS_ID" if term in anchored
                      else "CAS_MISSING_ANCHOR_ROWS")
        elif term_is_hydrate:
            status = "OK_HYDRATE_TERM"
        elif target.startswith("CHEBI:") and f:
            status = "HYDRATE_ON_ANHYDROUS_TERM"
        else:
            status = "UNKNOWN_NO_FORMULA"
        rows.append({"identifier": ident, "preferred_term": term,
                     "ontology_id": target, "ontology_label": om.get("ontology_label") or "",
                     "term_formula": f, "status": status})

    FIELDS = ["identifier", "preferred_term", "ontology_id", "ontology_label",
              "term_formula", "status"]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    with REPORT.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS, delimiter="\t")
        w.writeheader(); w.writerows(rows)
    if not rows:
        print("no record carries hydrate notation")
        print(f"\nreport: {REPORT.relative_to(ROOT)}")
        return 0

    import collections
    c = collections.Counter(r["status"] for r in rows)
    print(f"{len(rows)} record(s) whose preferred_term carries hydrate notation\n")
    for k in ("HYDRATE_ON_ANHYDROUS_TERM", "CAS_MISSING_ANCHOR_ROWS",
              "OK_HYDRATE_TERM", "OK_OWN_CAS_ID", "UNKNOWN_NO_FORMULA"):
        if c.get(k):
            print(f"  {k:28} {c[k]}")
    bad = [r for r in rows if r["status"] == "HYDRATE_ON_ANHYDROUS_TERM"]
    if bad:
        print(f"\nGrounded onto a term whose formula has no water (Section 3 violations):")
        for r in bad[:args.limit]:
            print(f"  {r['preferred_term'][:34]:34} -> {r['ontology_id']:14} "
                  f"{r['ontology_label'][:26]:26} [{r['term_formula']}]")
        if len(bad) > args.limit:
            print(f"  ... and {len(bad) - args.limit} more")
    print(f"\nreport: {REPORT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
