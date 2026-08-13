#!/usr/bin/env python3
"""Add the water of hydration to formulas that describe the anhydrous salt (#321).

These records name a hydrate (`CoCl2 x 2 H2O`) but carry the *anhydrous* parent's
molecular formula (`2Cl.Co`), so the recorded formula describes a different
substance than the label does — and a mass 36 g/mol light for a dihydrate, more
for the higher hydrates. This is the formula half of #321; the identity half (a
hydrate sharing its anhydrous parent's `identifier`) is fixed separately by
`mint_hydrate_registry_terms`.

**The correction is arithmetic the label itself supplies, not a judgement call.**
Two cohorts, both verified against ChEBI rather than computed blind:

*Stated stoichiometry* (22) — the label states `x N H2O`, and the recorded formula
is byte-identical to the ChEBI parent's `chemrof:generalized_empirical_formula`.
That identity is the proof the formula was inherited from the parent rather than
measured for this record. The water is appended in ChEBI's own dot-separated
notation (`2Cl.Co` + `.2H2O` -> `2Cl.Co.2H2O`, matching how ChEBI writes
`CHEBI:53503 cobalt chloride hexahydrate` as `2Cl.Co.6H2O`). ChEBI omits the
coefficient at n=1, so `Betaine x H2O` gets `.H2O`.

*Specific hydrate term* (2) — `Na2HPO4 x 2 H2O` and `x 12 H2O` were promoted onto
`CHEBI:91258`/`CHEBI:91259` by `fix_hydrate_collapse`, and those terms' own
formulas already carry the water (`2H2O.HO4P.2Na`). Here nothing is constructed:
the formula is taken verbatim from the mapped term, which is strictly better
evidence than appending.

**13 records are deliberately left alone**: their labels say "hydrate" without a
number (`Stachyose hydrate`, `Adenine hydrochloride hydrate`, …), so the
stoichiometry is not recoverable from the record, and ChEBI has no specific
hydrate term to read it off. Guessing a coefficient would put a fabricated mass
into a published field. They need a per-record source and are tracked, not
guessed.

    python scripts/add_water_of_hydration.py            # dry-run
    python scripts/add_water_of_hydration.py --apply
"""
from __future__ import annotations

import argparse
import importlib.util
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
import yaml  # noqa: E402

from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

# Reuse the audited detector rather than re-deriving water detection. The
# previous local version scanned molecular_formula + smiles + inchi for the
# string "H2O", and `InChI=1S/Cu.H2O4S/...` contains `.H2O` as part of the
# SULFATE fragment H2O4S. Every sulfate hydrate therefore looked like it already
# had its water and was skipped — 16 records, all of them sulfates or selenites.
_spec = importlib.util.spec_from_file_location(
    "check_hydrate_water", ROOT / "scripts" / "check_hydrate_water.py")
_chw = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_chw)
parse_formula = _chw.parse_formula
classify = _chw.classify

COLLECTION = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
CHEBI_DB = Path.home() / ".data" / "oaklib" / "chebi.db"
STAMP = "2026-08-13T00:00:00+00:00"
CURATOR = "add_water_of_hydration"
ISSUE = "#321"

FORMULA_PRED = "chemrof:generalized_empirical_formula"
# `x 2 H2O`, `·2H2O`, `x H2O` (n=1 implied), and the word forms `monohydrate`,
# `hexahydrate`, ... which the numeric pattern alone does not reach.
HYDRATION_N = re.compile(r"(?:x|·)\s*(\d*)\s*H2O", re.IGNORECASE)
MULTIPLIER = {"mono": 1, "di": 2, "tri": 3, "tetra": 4, "penta": 5, "hexa": 6,
              "hepta": 7, "octa": 8, "nona": 9, "deca": 10, "dodeca": 12}
HYDRATION_WORD = re.compile(
    r"\b(mono|di|tri|tetra|penta|hexa|hepta|octa|nona|deca|dodeca)hydrate\b", re.IGNORECASE)
# "borohydrate" is not a hydrate; it ends in -hydrate purely by spelling.
NOT_A_HYDRATE = re.compile(r"borohydrate", re.IGNORECASE)


def hydration_number(label: str) -> int | None:
    """Waters of hydration the label states, by either notation, or None."""
    m = HYDRATION_N.search(label)
    if m:
        return int(m.group(1) or 1)
    m = HYDRATION_WORD.search(label)
    return MULTIPLIER[m.group(1).lower()] if m else None
# Any notation that already accounts for water, in formula/smiles/inchi.
HAS_WATER = re.compile(r"\.\s*\d*H2O|\d+H2O|H2O\b", re.IGNORECASE)
# No leading \b before `hydrate`: "monohydrate"/"tetrahydrate" have no word
# boundary there, and an earlier version of this pattern silently skipped every
# record spelled that way.
HYDRATE_LABEL = re.compile(r"(\bx\s*\d*\s*h2o\b|·\s*\d*\s*h2o|hydrate\b)", re.IGNORECASE)


def chebi_formula(conn: sqlite3.Connection, curie: str) -> str | None:
    row = conn.execute(
        "SELECT value FROM statements WHERE subject=? AND predicate=?",
        (curie, FORMULA_PRED),
    ).fetchone()
    return row[0] if row else None


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--chebi-db", type=Path, default=CHEBI_DB)
    args = ap.parse_args(argv)

    if not args.chebi_db.exists():
        print(f"ERROR: ChEBI SQLite not found at {args.chebi_db}. Every correction here "
              f"is verified against it, so there is nothing safe to do without it.",
              file=sys.stderr)
        return 1
    conn = sqlite3.connect(f"file:{args.chebi_db}?mode=ro", uri=True)

    coll = yaml.safe_load(COLLECTION.read_text(encoding="utf-8", errors="replace")) or {}
    appended: list[str] = []
    adopted: list[str] = []
    unstated: list[str] = []

    for rec in coll.get("ingredients", []):
        if rec.get("mapping_status") == "REJECTED":
            continue
        label = str(rec.get("preferred_term") or "")
        if not HYDRATE_LABEL.search(label) or NOT_A_HYDRATE.search(label):
            continue
        cp = rec.get("chemical_properties") or {}
        current = str(cp.get("molecular_formula") or "").strip()
        if not current:
            continue

        om = rec.get("ontology_mapping") or {}
        onto_id = str(om.get("ontology_id") or "")
        term_formula = chebi_formula(conn, onto_id) if onto_id.startswith("CHEBI:") else None
        # Element totals, not string matching: a formula can carry its water in
        # combined notation (C7H15N3O5) and an InChI can contain "H2O" that is
        # not water at all.
        verdict, _why = classify(label, current, term_formula,
                                 str(om.get("ontology_label") or ""))
        if verdict == "ok":
            continue

        # Cohort 2 first: the mapped term is itself the hydrate, so read the
        # formula off it rather than constructing one.
        if term_formula and HAS_WATER.search(term_formula):
            new = term_formula
            why = (f"adopted verbatim from the mapped term {onto_id} "
                   f"({om.get('ontology_label')!r}), which is the specific hydrate and "
                   f"already carries the water")
            bucket = adopted
        else:
            n = hydration_number(label)
            if n is None:
                unstated.append(f"{label[:42]:<42} {current:<18} ({onto_id})")
                continue
            # Element totals, not string equality: `C4H6CdO4` and `2C2H3O2.Cd`
            # are the same compound written two ways, and a string compare
            # rejected the pair.
            if not term_formula or parse_formula(current) != parse_formula(term_formula):
                unstated.append(f"{label[:42]:<42} {current:<18} ({onto_id}) "
                                f"— element totals differ from the parent's "
                                f"{term_formula!r}")
                continue
            # ChEBI writes the n=1 case as `.H2O`, not `.1H2O`.
            new = f"{current}.{n if n > 1 else ''}H2O"
            why = (f"the label states {n} water(s) of hydration, and the recorded formula "
                   f"was byte-identical to the anhydrous parent {onto_id}'s ChEBI formula "
                   f"({term_formula!r}) — the mark of a value inherited from the parent "
                   f"rather than measured for this record. Water appended in ChEBI's own "
                   f"dot-separated notation")
            bucket = appended

        if new == current:
            continue
        cp["molecular_formula"] = new
        rec["chemical_properties"] = cp
        om.setdefault("evidence", []).append({
            "evidence_type": "DATABASE_MATCH",
            "source": f"MIM curation ({ISSUE})",
            "notes": (f"molecular_formula {current!r} -> {new!r}. The recorded value "
                      f"described the anhydrous salt while the label names a hydrate, "
                      f"understating the mass by 18 g/mol per water. Corrected because "
                      f"{why}."),
        })
        rec.setdefault("curation_history", []).append({
            "timestamp": STAMP, "curator": CURATOR, "action": "ADDED_WATER_OF_HYDRATION",
            "changes": (f"molecular_formula {current!r} -> {new!r} ({ISSUE}); {why}."),
            "llm_assisted": False,
        })
        bucket.append(f"{label[:34]:<34} {current:<18} -> {new}")

    if args.apply and (appended or adopted):
        save_yaml(coll, COLLECTION)

    total = len(appended) + len(adopted)
    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'} — "
          f"{total} formula(s) corrected\n")
    print(f"  Water appended from the label's stated stoichiometry ({len(appended)}):")
    for a in appended:
        print(f"     {a}")
    print(f"\n  Adopted verbatim from a specific ChEBI hydrate term ({len(adopted)}):")
    for a in adopted:
        print(f"     {a}")
    print(f"\n  Left alone — stoichiometry not stated and no specific ChEBI term "
          f"({len(unstated)}):")
    for u in unstated:
        print(f"     {u}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
