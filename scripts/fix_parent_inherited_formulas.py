#!/usr/bin/env python3
"""Correct molecular formulas that describe the parent term, not the record (#326).

These records carry a `narrowMatch` to a parent *and* a `molecular_formula`
identical to that parent's. The narrowMatch is correct — the label names a salt
or hydrate, which genuinely is narrower — so the defect is the formula: it
describes the parent rather than the labelled substance.

**Only formulas independently proven wrong are touched.** Each record's own
`cas_rn` came from `CultureBotHT compounds_to_cas.csv` at creation, so it is
independent of the ChEBI mapping under test — which is exactly the provenance
standard `MAPPING_SEMANTICS` §3 sets for evidence. Resolving that CAS in PubChem
gives a formula derived from neither the mapping nor the backfill.

For each, the CAS resolves to a PubChem title matching the record's own label,
and the formula disagrees with what is recorded:

    2-Deoxy-D-ribonic acid lithium salt  7284-15-3     C5H10O5  -> C5H9LiO5
    Betaine hydrochloride                590-46-5      C5H11NO2 -> C5H12ClNO2
    Gly-Gln monohydrate                  172669-64-6   C7H13N3O4-> C7H15N3O5
    Nitrilotriacetic acid disodium salt  15467-20-6    C6H9NO6  -> C6H7NNa2O6
    Sodium hypophosphite monohydrate     10039-56-2    Na.O2P   -> H2NaO3P

Deliberately NOT touched — the other seven of the twelve in #326 group (b):

* four where PubChem **agrees** with the recorded formula (`Carnitine (Dl)
  Hydrochloride`, `D-xylose 5-phosphate lithium salt`, `sn-Glycerol 3-phosphate
  lithium salt`, `Stachyose hydrate`). Matching the parent's formula is
  suspicious but not proof; PubChem's own entry for that CAS carries the same
  value, so there is nothing to correct against.
* three where the CAS gets **no PubChem hit** (`D-Galacturonic Acid monohydrate`,
  `Polygalacturonic acid sodium salt`, `Vancomycin Hydrochloride Hydrate`) and
  the claim cannot be adjudicated either way.

That is the correction to #326 as filed: it described all twelve as "factually
wrong", and only five are demonstrably so.

    python scripts/fix_parent_inherited_formulas.py            # dry-run
    python scripts/fix_parent_inherited_formulas.py --apply
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
import yaml  # noqa: E402

from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

COLLECTION = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
STAMP = "2026-08-13T00:00:00+00:00"
CURATOR = "fix_parent_inherited_formulas"
ISSUE = "#326"

# preferred_term -> (expected cas, wrong formula, correct formula, PubChem title)
FIXES = {
    "2-Deoxy-D-ribonic acid lithium salt": (
        "7284-15-3", "C5H10O5", "C5H9LiO5", "2-Deoxy-D-ribonic acid lithium salt"),
    "Betaine hydrochloride": (
        "590-46-5", "C5H11NO2", "C5H12ClNO2", "Betaine chloride"),
    "Gly-Gln monohydrate": (
        "172669-64-6", "C7H13N3O4", "C7H15N3O5", "Glycyl-glutamine monohydrate"),
    "Nitrilotriacetic acid disodium salt": (
        "15467-20-6", "C6H9NO6", "C6H7NNa2O6", "Disodium nitrilotriacetate"),
    "Sodium hypophosphite monohydrate": (
        "10039-56-2", "Na.O2P", "H2NaO3P", "Sodium hypophosphite monohydrate"),
}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    coll = yaml.safe_load(COLLECTION.read_text(encoding="utf-8", errors="replace")) or {}
    out, skipped = [], []
    for rec in coll.get("ingredients", []):
        spec = FIXES.get(str(rec.get("preferred_term") or ""))
        if spec is None or rec.get("mapping_status") == "REJECTED":
            continue
        cas, wrong, right, title = spec
        cp = rec.setdefault("chemical_properties", {})
        # Guard on both the CAS and the current value: if either has moved since
        # this was verified, the correction is no longer the one that was checked.
        if str(cp.get("cas_rn") or "").strip() != cas:
            skipped.append(f"{rec['preferred_term']}: cas is {cp.get('cas_rn')}, expected {cas}")
            continue
        if str(cp.get("molecular_formula") or "").strip() != wrong:
            skipped.append(f"{rec['preferred_term']}: formula is "
                           f"{cp.get('molecular_formula')}, expected {wrong}")
            continue
        cp["molecular_formula"] = right
        rec.setdefault("curation_history", []).append({
            "timestamp": STAMP, "curator": CURATOR, "action": "CORRECTED_INHERITED_FORMULA",
            "changes": (
                f"molecular_formula {wrong!r} -> {right!r} ({ISSUE}). The recorded value was "
                f"identical to the narrowMatch parent's, so it described the parent rather "
                f"than this salt/hydrate. Corrected from the record's own CAS {cas}, which "
                f"resolves in PubChem to {title!r} — provenance independent of the ChEBI "
                f"mapping under test, per MAPPING_SEMANTICS §3. The narrowMatch itself is "
                f"correct and is unchanged."),
            "llm_assisted": False,
        })
        out.append(f"{rec['preferred_term'][:36]:<36} {wrong:<12} -> {right:<12} (CAS {cas})")

    if args.apply and out:
        save_yaml(coll, COLLECTION)

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'} — {len(out)} corrected\n")
    for o in out:
        print(f"  {o}")
    for s in skipped:
        print(f"  SKIPPED {s}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
