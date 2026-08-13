#!/usr/bin/env python3
"""Classify `ingredient_type` for records that have none (#323).

`ingredient_type` is unset on 556 live records, 511 of them from the 2026-08-04
microbedecoder import. It is load-bearing rather than cosmetic: it is the only
field that distinguishes the three reasons `chemical_properties` can be empty —
*a mixture has no formula*, *a structure-free class has none*, *this one is
simply not filled in yet*. An enrichment pass that reads "empty" as "fill it"
corrupts the first two while fixing the third, which is the root confusion
behind #316.

**The original classifier no longer exists.** 3,512 history events cite a curator
named `auto_classify_ingredient_type`, but no such script is in the repo, so
this is a reimplementation rather than a re-run. Its rules were recovered from
the reasons those events recorded.

Two deliberate departures from the recovered behaviour:

* **Word-boundary matching.** The original matched complex patterns as bare
  substrings, so `malt` matched `Cyclomaltoheptaose`, `Maltose`, `Maltitol` and
  10 more genuine single compounds. Those were saved only by rule order.
* **Consistent precedence.** The original is self-inconsistent: `Bacto Soytone`
  (CHEBI-primary, name matches `Soy`) became SINGLE_INGREDIENT via "CHEBI
  primary", while `Fish-Sperm DNA` — the same shape — became UNDEFINED_MIXTURE
  via the name. Here the name wins, because what a substance *is* outranks which
  namespace happened to have a term for it.

Only unset records are touched; nothing already classified is revisited.

Where the evidence is weak the record is **left unset and reported**, rather than
guessed. A wrong value is worse than an absent one for the purpose above:

* a CHEBI term with no structural definition is a class, not a compound (#322);
* `kgmicrobe.compound:` is the registry fallback for anything lacking an
  ontology term, mixtures included — `Synthetic Sea Salts (sss)` sits there;
* MeSH and NCIT carry both substances and materials.

    python scripts/classify_ingredient_type.py            # dry-run
    python scripts/classify_ingredient_type.py --apply
"""
from __future__ import annotations

import argparse
import collections
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
import yaml  # noqa: E402

from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

COLLECTION = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
CHEBI_DB = Path.home() / ".data" / "oaklib" / "chebi.db"
STAMP = "2026-08-13T00:00:00+00:00"
CURATOR = "classify_ingredient_type"
ISSUE = "#323"

# Recovered from the historical events, plus serum/plasma/blood/bile/liver/brain
# and 'sea salt' — the gaps that left `Bovine_Calf_Serum` unset while its
# same-batch sibling `Brain_Heart_Infusion` was classified.
COMPLEX = ["beef", "casamino", "casein", "fish", "malt", "meat", "milk", "peptone",
           "sea water", "seawater", "sea salt", "sludge", "soil", "soy", "soybean",
           "tomato", "tryptone", "yeast", "broth", "extract", "hydrolysate",
           "infusion", "manure", "serum", "plasma", "digest", "blood", "bile",
           "liver", "brain", "agar"]
SOLUTION = ["stock solution", "salt solution", "salts solution", "vitamin solution",
            "mineral solution", "trace element", "trace metal", "buffer", "solution"]

# Namespaces that were tried as an UNDEFINED_MIXTURE signal and **rejected**
# (#330). Inferring "this is an undefined mixture" from which ontology happened
# to have a term is a different question from what the substance is, and it was
# wrong on roughly a quarter of the records it decided: `Carboxymethyl cellulose
# (sodium salt)` is a defined polymer that happens to be FOODON-primary,
# `Bovine albumin` a purified protein that happens to be MICRO-primary. Marking
# those UNDEFINED_MIXTURE tells every future enrichment pass not to fill a record
# that could be filled — a silent permanent exclusion, which is the failure this
# field exists to prevent, pointed the other way.
#
# They are left unset instead, and reported. Kept as a named set so the rejection
# is visible rather than an absence.
REJECTED_MIXTURE_NS = {"foodon", "micro", "envo", "bto", "ncbitaxon", "uberon",
                       "kgmicrobe.ingredient"}
DEFINED_CHEMICAL_NS = {"cas"}


def word_match(patterns: list[str], text: str) -> str | None:
    """Match on word boundaries, not substrings — `malt` must not hit `Maltose`."""
    low = str(text or "").lower()
    for p in patterns:
        if re.search(r"(?<![a-z])" + re.escape(p) + r"(?![a-z])", low):
            return p
    return None


def structural_chebi_terms(db_path: Path) -> set[str]:
    """CHEBI terms carrying any structural annotation.

    A term with none is a role/grouping/family class (#322), so a record on one
    is not evidence of a single compound.
    """
    db = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    try:
        cur = db.cursor()
        cur.execute("""SELECT DISTINCT subject FROM statements
                       WHERE predicate LIKE '%inchikey%' OR predicate LIKE '%smiles%'
                          OR predicate LIKE '%formula%'""")
        return {r[0] for r in cur.fetchall()}
    finally:
        db.close()


def classify(rec: dict, structural: set[str]) -> tuple[str | None, str]:
    """Return (ingredient_type, reason). A None type means 'leave it unset'."""
    name = str(rec.get("preferred_term") or "")
    ident = str(rec.get("identifier") or "")
    prefix = ident.split(":")[0].lower()

    if (p := word_match(SOLUTION, name)):
        return "STOCK_SOLUTION", f"name matches solution pattern {p!r}"
    if (p := word_match(COMPLEX, name)):
        return "UNDEFINED_MIXTURE", f"name matches complex pattern {p!r}"
    if prefix in REJECTED_MIXTURE_NS:
        return None, (f"{prefix} primary — a biological namespace is not evidence of a "
                      f"mixture (#330); needs a curator")
    if prefix == "chebi":
        if ident in structural:
            return "SINGLE_INGREDIENT", "CHEBI primary with a structural definition"
        return None, "CHEBI primary but the term is a structureless class (#322)"
    if prefix in DEFINED_CHEMICAL_NS:
        return "SINGLE_INGREDIENT", f"{prefix}: primary (defined chemical)"
    return None, f"{prefix} primary — ambiguous namespace, needs a curator"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--list-unresolved", action="store_true",
                    help="Print every record left unset, not just the tally.")
    args = ap.parse_args(argv)

    if not CHEBI_DB.exists():
        raise SystemExit(f"chebi.db not found at {CHEBI_DB} — needed for the #322 gate.")
    structural = structural_chebi_terms(CHEBI_DB)

    coll = yaml.safe_load(COLLECTION.read_text(encoding="utf-8", errors="replace")) or {}
    assigned: collections.Counter = collections.Counter()
    reasons: collections.Counter = collections.Counter()
    unresolved: list[tuple[str, str]] = []

    for rec in coll.get("ingredients", []):
        if rec.get("mapping_status") == "REJECTED" or rec.get("ingredient_type"):
            continue
        itype, why = classify(rec, structural)
        if itype is None:
            unresolved.append((str(rec.get("preferred_term") or ""), why))
            reasons[why] += 1
            continue
        rec["ingredient_type"] = itype
        assigned[itype] += 1
        rec.setdefault("curation_history", []).append({
            "timestamp": STAMP, "curator": CURATOR, "action": "AUTO_CLASSIFY_INGREDIENT_TYPE",
            "changes": f"set ingredient_type={itype} ({why}) ({ISSUE})",
            "llm_assisted": False,
        })

    if args.apply and assigned:
        save_yaml(coll, COLLECTION)

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'}\n")
    for t, n in assigned.most_common():
        print(f"  {t:<20} {n}")
    print(f"\n  left unset on purpose: {len(unresolved)}")
    for why, n in reasons.most_common():
        print(f"     {n:>4}  {why}")
    if args.list_unresolved:
        print()
        for name, why in unresolved:
            print(f"     {name[:52]:<52} {why}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
