#!/usr/bin/env python3
"""Re-grade EXACT_MATCH records that are actually synonym matches (#317).

The schema defines the two grades unambiguously:

    EXACT_MATCH:    Direct exact match to ontology term
    SYNONYM_MATCH:  Matches known synonym in ontology

A record whose label matches a ChEBI *synonym* rather than the term's primary
label is `SYNONYM_MATCH` by that definition. 297 records say `EXACT_MATCH`
anyway — 16% of every EXACT_MATCH in the corpus disagreeing with the enum it uses.

Scope, deliberately narrow:

* Only records where a **ChEBI synonym actually matches** are touched. The 59
  records whose label matches *nothing* in ChEBI are a different problem needing
  per-record judgement (locant truncation, scope loss, an outright wrong term)
  and are left alone.
* `ontology_id` is never changed. The term is right; only the claim about *how*
  it was matched is wrong.
* The SSSOM predicate does not move: `reconcile_sssom.PREDICATE` maps both
  EXACT_MATCH and SYNONYM_MATCH to `skos:exactMatch`, so no published mapping
  changes. This corrects the record's internal honesty, not the published
  predicate — if the downstream over-claim is the concern, that map is the thing
  to change, and it is a separate decision.

Matching is case- and punctuation-insensitive, so a mere capitalisation
difference is not treated as a synonym match.

    python scripts/regrade_synonym_matches.py            # dry-run
    python scripts/regrade_synonym_matches.py --apply
"""
from __future__ import annotations

import argparse
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
import yaml  # noqa: E402

from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

COLLECTION = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
CHEBI_DB = Path.home() / ".data" / "oaklib" / "chebi.db"
STAMP = "2026-08-10T00:00:00+00:00"
CURATOR = "regrade_synonym_matches"
ISSUE = "#317"


def norm(s: object) -> str:
    return re.sub(r"[^a-z0-9]", "", str(s or "").lower())


def chebi_synonyms(cur: sqlite3.Cursor, curie: str) -> dict[str, str]:
    """normalised synonym -> the verbatim ChEBI string, for the audit trail."""
    cur.execute(
        "SELECT value FROM statements WHERE subject=? AND predicate LIKE '%ynonym%'",
        (curie,),
    )
    return {norm(v[0]): v[0] for v in cur.fetchall() if v[0]}


DERIVED_SOURCES = ("chebi", "ols")

# A concentration- or solution-qualified label denotes a *preparation*, not the
# solute, so its mapping is wrong at the identity level (#324's neighbourhood),
# not merely mis-graded. Re-grading one would stamp "the term is correct" into
# its curation_history, which is a false statement — and would quietly remove it
# from anyone scanning EXACT_MATCH for problems. Those need re-grounding.
CONCENTRATION_LABEL = re.compile(
    r"^\s*\d+(\.\d+)?\s*(%|M\b|mM\b|g/l\b)|(?<![a-z])solution(?![a-z])|\bstock\b", re.I)


def evidence_is_independent(rec: dict, matched: str) -> bool:
    """True when the matching string is not itself a copy of ChEBI's own data.

    134 of the candidates match only through a synonym whose `source` is
    `chebi_synonym_review` — i.e. a string previously copied *out of* ChEBI and
    into the record. Matching it back against ChEBI is circular: it confirms the
    string is a ChEBI synonym (which we already knew) and says nothing about how
    this ingredient came to be matched to this term. MAPPING_SEMANTICS §3 makes
    the same point about auto-derived chemistry.

    A match on the record's own `preferred_term`, or on a synonym carried in
    from kg_microbe / microbedecoder / a curator, is independent evidence.
    """
    if norm(rec.get("preferred_term")) == norm(matched):
        return True
    for s in rec.get("synonyms") or []:
        if norm(s.get("synonym_text")) == norm(matched):
            src = str(s.get("source") or "").lower()
            return not any(d in src for d in DERIVED_SOURCES)
    return False


def plan(coll: dict, cur: sqlite3.Cursor) -> tuple[list[dict], dict[str, int]]:
    """Return the records to re-grade, plus a tally of why others were skipped."""
    todo: list[dict] = []
    tally = {"not_exact_match": 0, "not_chebi": 0, "label_matches": 0,
             "no_chebi_synonym_match": 0, "circular_evidence_only": 0,
             "deeper_defect_skipped": 0, "regrade": 0}
    # Terms with no structure at all are role/grouping/family classes (#322):
    # a label on one of those is a scope problem, again not a grading one.
    cur.execute("""SELECT DISTINCT subject FROM statements
                   WHERE predicate LIKE '%inchikey%' OR predicate LIKE '%smiles%'
                      OR predicate LIKE '%formula%'""")
    has_structure = {r[0] for r in cur.fetchall()}
    for rec in coll.get("ingredients", []):
        om = rec.get("ontology_mapping") or {}
        if om.get("mapping_quality") != "EXACT_MATCH":
            tally["not_exact_match"] += 1
            continue
        curie = str(om.get("ontology_id") or "")
        if not curie.startswith("CHEBI:"):
            tally["not_chebi"] += 1
            continue
        onto_label = om.get("ontology_label")
        local = {norm(rec.get("preferred_term"))}
        local |= {norm(s.get("synonym_text")) for s in (rec.get("synonyms") or [])}
        if norm(onto_label) in local:
            tally["label_matches"] += 1     # genuinely exact; leave it
            continue
        syns = chebi_synonyms(cur, curie)
        hit = next((syns[k] for k in local if k in syns), None)
        if hit is None:
            tally["no_chebi_synonym_match"] += 1   # the 59; needs judgement
            continue
        if not evidence_is_independent(rec, hit):
            tally["circular_evidence_only"] += 1   # also needs judgement
            continue
        if CONCENTRATION_LABEL.search(str(rec.get("preferred_term") or "")) \
                or curie not in has_structure:
            tally["deeper_defect_skipped"] += 1
            continue
        tally["regrade"] += 1
        todo.append({"rec": rec, "curie": curie, "onto_label": onto_label,
                     "matched_synonym": hit})
    return todo, tally


def apply_one(item: dict) -> str:
    rec, om = item["rec"], item["rec"]["ontology_mapping"]
    om["mapping_quality"] = "SYNONYM_MATCH"
    rec.setdefault("curation_history", []).append({
        "timestamp": STAMP,
        "curator": CURATOR,
        "action": "REGRADED_EXACT_TO_SYNONYM",
        "changes": (
            f"mapping_quality EXACT_MATCH -> SYNONYM_MATCH ({ISSUE}). The record's label "
            f"does not equal the term's primary label {item['onto_label']!r}; it matches "
            f"the ChEBI synonym {item['matched_synonym']!r} on {item['curie']}. The schema "
            f"defines EXACT_MATCH as a direct match to the term and SYNONYM_MATCH as a "
            f"match to a known synonym, so the recorded grade overstated. ontology_id is "
            f"unchanged — the term is correct. The SSSOM predicate is unaffected "
            f"(both grades emit skos:exactMatch)."
        ),
        "llm_assisted": False,
    })
    return (f"{str(rec.get('preferred_term'))[:34]:<34} {item['curie']:<16} "
            f"via synonym {item['matched_synonym'][:34]!r}")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="Write changes (default: dry-run).")
    ap.add_argument("--limit", type=int, help="Show only N examples in the dry-run output.")
    args = ap.parse_args(argv)

    if not CHEBI_DB.exists():
        raise SystemExit(f"chebi.db not found at {CHEBI_DB} — needed to verify synonyms.")

    coll = yaml.safe_load(COLLECTION.read_text(encoding="utf-8", errors="replace")) or {}
    db = sqlite3.connect(f"file:{CHEBI_DB}?mode=ro", uri=True)
    try:
        todo, tally = plan(coll, db.cursor())
    finally:
        db.close()

    lines = [apply_one(i) for i in todo]
    if args.apply and todo:
        save_yaml(coll, COLLECTION)

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'} — "
          f"{len(todo)} record(s) re-graded\n")
    for ln in lines[: args.limit or 15]:
        print(f"  {ln}")
    if len(lines) > (args.limit or 15):
        print(f"  ... {len(lines) - (args.limit or 15)} more")
    print("\nskip tally:")
    for k, v in tally.items():
        print(f"  {k:<24} {v}")
    print("\nNot touched: records whose label matches nothing in ChEBI — those need "
          "per-record judgement, not a re-grade.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
