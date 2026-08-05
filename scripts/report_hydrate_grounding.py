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
UNMAPPED = ROOT / "data" / "curated" / "unmapped_ingredients.yaml"
REPORT = ROOT / "reports" / "hydrate_grounding.tsv"
CHEBI_DB = Path(os.path.expanduser("~/.data/oaklib/chebi.db"))

def _load_hydrate_notation():
    """Load the shared regex WITHOUT importing the package.

    `mediaingredientmech.curation.__init__` imports ingredient_curator, which
    imports linkml_runtime — so a plain package import would turn this
    stdlib+PyYAML script into one that needs the full dependency set, and this
    repo has four CI jobs that deliberately run scripts with only pyyaml (and
    click/rich). hydrate_guard itself imports nothing but `re` and `typing`.
    """
    import importlib.util
    path = ROOT / "src" / "mediaingredientmech" / "curation" / "hydrate_guard.py"
    spec = importlib.util.spec_from_file_location("_hydrate_guard", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.HYDRATE_NOTATION


HYDRATE = _load_hydrate_notation()


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
    ap.add_argument("--limit", type=int, default=25,
                    help="cap the violations list")
    ap.add_argument("--queue-limit", type=int, default=25,
                    help="cap the pending-queue list, independently of --limit")
    args = ap.parse_args()

    form = formulas()
    anchored = anchored_subjects()

    def _term_is_hydrate(ontology_id: str, ontology_label: str) -> bool:
        """Water as its own formula component, or the term's own label saying so.

        A bare "H2O" substring is wrong both ways: it matches `H2O4P`
        (dihydrogenphosphate, no water at all) and misses ChEBI hydrate terms
        written without explicit water (`Glycocholic acid hydrate`, C26H43NO6).
        """
        return bool(
            re.search(r"(?:^|\.)\(?[\dn]*H2O\)?n?(?:\.|$)", form.get(ontology_id, ""))
            or re.search(r"hydrate\b", str(ontology_label or ""), re.IGNORECASE))

    rows = []
    for rec in yaml.safe_load(MAPPED.read_text())["ingredients"]:
        term = str(rec.get("preferred_term") or "")
        if not HYDRATE.search(term):
            continue
        ident = str(rec.get("identifier") or "")
        om = rec.get("ontology_mapping") or {}
        target = str(om.get("ontology_id") or "")
        f = form.get(target, "")
        term_is_hydrate = _term_is_hydrate(target, om.get("ontology_label"))
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
        print("no mapped record carries hydrate notation")

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
    # The guard added in #246 refuses these rather than mis-filing them, so they
    # stay UNMAPPED. Without a worklist the hydrate residual grows invisibly
    # instead of visibly, which is only an improvement if someone can see it (#247).
    # A merge folds the hydrate in as a synonym rather than giving it its own
    # identifier, so the collapse survives where neither the mapped bucket (which
    # scans preferred_term) nor any gate can see it: one identifier, one record,
    # and since #229 the label even resolves — to the anhydrous parent. Issue #251.
    syn_rows = []
    for rec in yaml.safe_load(MAPPED.read_text())["ingredients"]:
        term = str(rec.get("preferred_term") or "")
        if HYDRATE.search(term):
            continue                      # already counted in the mapped bucket
        om = rec.get("ontology_mapping") or {}
        target = str(om.get("ontology_id") or "")
        if _term_is_hydrate(target, om.get("ontology_label")):
            continue
        hyd = [str(sy.get("synonym_text") or "") for sy in (rec.get("synonyms") or [])
               if HYDRATE.search(str(sy.get("synonym_text") or ""))]
        if hyd:
            syn_rows.append((str(rec.get("identifier") or ""), term, target, hyd))
    print(f"\n{len(syn_rows)} mapped record(s) carry a hydrate SYNONYM on a non-hydrate "
          "term.")
    if syn_rows:
        print("The hydrate was folded in as a synonym instead of taking its own identifier, "
              "so\nthe #218 collapse survives post-merge and no gate sees it — one "
              "identifier, one\nrecord, and since #229 the label resolves to the anhydrous "
              "parent.")
        for ident, term, target, hyd in syn_rows[:args.queue_limit]:
            print(f"  {ident:16} {term[:24]:24} <- {', '.join(hyd[:2])}")
        if len(syn_rows) > args.queue_limit:
            print(f"  ... and {len(syn_rows) - args.queue_limit} more")

    if not UNMAPPED.exists():
        print(f"\nERROR: {UNMAPPED.relative_to(ROOT)} is missing; cannot report the "
              "pending queue")
        return 2
    doc = yaml.safe_load(UNMAPPED.read_text()) or {}
    if not isinstance(doc.get("ingredients"), list):
        print(f"\nERROR: {UNMAPPED.relative_to(ROOT)} has no 'ingredients' list")
        return 2
    # 'MES Hydrat' is the German spelling and its own history action is
    # REVIEWED_HYDRATE_AMBIGUITY -- the one record whose audit trail says "this is
    # the hydrate problem" was the one the \bhydrate\b anchor dropped.
    pending = [r for r in doc["ingredients"]
               if r.get("mapping_status") == "UNMAPPED"
               and (HYDRATE.search(str(r.get("preferred_term") or ""))
                    or re.search(r"(?<![a-z])hydrat\b", str(r.get("preferred_term") or ""),
                                 re.IGNORECASE))]
    occ = lambda r: (r.get("occurrence_statistics") or {}).get("total_occurrences") or 0
    pending.sort(key=occ, reverse=True)   # a 4-medium record is not a 0-medium one
    print(f"\n{len(pending)} UNMAPPED record(s) whose label carries hydrate notation.")
    if pending:
        print("This is the queue the #246 guard refuses into; it also holds records that "
              "predate\nthe guard. Each needs MAPPING_SEMANTICS.md Section 3: a "
              "hydrate-specific ontology term\nif one exists, else its own cas:<hydrate CAS> "
              "with a narrowMatch to the parent plus\nthe Rule B1 registry row.")
        for r in pending[:args.queue_limit]:
            print(f"  {str(r.get('identifier')):16} occ={occ(r):<4} "
                  f"{str(r.get('preferred_term'))[:48]}")
        if len(pending) > args.queue_limit:
            print(f"  ... and {len(pending) - args.queue_limit} more")

    print(f"\nreport: {REPORT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
