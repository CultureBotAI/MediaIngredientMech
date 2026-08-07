#!/usr/bin/env python3
"""Add CAS-RNs Edison recovered, where the CAS denotes the WHOLE record.

The literature reports frequently surface a CAS Registry Number for records that
carry none. Of the 20 such cases in this sweep, roughly half are usable and half
are traps of one specific kind: the report names the CAS of a **component** of a
multi-part label.

    PY-fructose          -> 57-48-7    fructose -- but PY-fructose is a MEDIUM
    Formate+methanol     -> 67-56-1    methanol -- one of two components
    2-butanol+CO2        -> 78-92-2    2-butanol -- likewise
    Esculin Ferric Citrate -> 531-75-9 esculin -- one half of the reagent
    Vitamin B            -> 98-92-0    niacinamide -- one vitamin of a family
    Amphotericin         -> 1397-89-3  amphotericin B -- the narrower variant

Adding those would assert that a mixture IS its component, which is the same
over-claim #242 and #263 exist to undo. Only the entries below, where the CAS
denotes the substance the record actually names, are applied.

This is ENRICHMENT, not grounding: it writes `chemical_properties.cas_rn` and
changes no mapping. Records stay UNMAPPED / NEEDS_EXPERT.

Run once, then delete.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
import yaml
from mediaingredientmech.utils.yaml_handler import save_yaml

UNMAPPED = ROOT / "data" / "curated" / "unmapped_ingredients.yaml"
STAMP = "2026-08-07T00:00:00+00:00"
CAS_RE = re.compile(r"^\d{2,7}-\d{2}-\d$")

# preferred_term -> (CAS, what the CAS denotes, the report's own affirming words)
APPLY = {
    "MES Hydrat": (
        "145224-94-8", "2-(N-morpholino)ethanesulfonic acid monohydrate",
        "the report's own recommendation is to \"Add the source-backed preferred "
        "name, exact monohydrate synonyms, CAS RN 145224-94-8, and hydrate-state "
        "annotation\", citing a peer-reviewed materials section that names the "
        "monohydrate and associates it with that number"),
    "KH2PO3": (
        "13977-65-6", "potassium phosphite monobasic",
        "the report calls the label \"sufficiently resolved chemically as the "
        "defined single salt potassium phosphite monobasic, KH2PO3, CAS RN "
        "13977-65-6\" on a culture-medium method that names supplier and CAS, and "
        "says the number \"can be stored as chemical registry grounding but should "
        "not be presented as an ontology CURIE\" — which is exactly this write"),
    "TitaniumIII chloride": (
        "7705-07-9", "titanium trichloride",
        "the report says \"a specialist inorganic-chemistry reference assigns "
        "titanium trichloride CAS RN 7705-07-9\" and describes four solid "
        "polymorphs rather than a mixture or named formulation, so the number "
        "denotes the compound this record names"),
    "CrKSO42 x 12 H2O": (
        "7788-99-0", "potassium chromium(III) sulfate dodecahydrate",
        "the report equates chrome alum with KCr(SO4)2*12H2O from peer-reviewed "
        "literature and gives CAS RN 7788-99-0 from a chemical reference, listing "
        "it under an unqualified \"CAS Registry Number:\" heading"),
}

# Scraped by the same pass and NOT applied, because each report forbids it in
# terms leaving no room to interpret. Kept here because the omissions are the
# load-bearing part: a regex that harvests every CAS in a report also harvests
# the ones sitting in rejected-candidate rows.
REFUSED = {
    "HBO3": "10043-35-3 (boric acid) — \"Do not map from HBO3 yet ... plausibility "
            "is not identity evidence\"; the CAS sits in a candidate row the report "
            "rejects, since boric acid is H3BO3 and metaboric acid is HBO2",
    "α-D-Glucose monohydrate": "5996-10-1 — \"Do not assert CAS:5996-10-1 as "
            "verified until checked against CAS or an authoritative pharmacopeial "
            "or supplier record\"",
    "Larchwood xylan": "9014-63-5 — \"Do not add CAS 9014-63-5 ... merely because "
            "it is associated elsewhere with generic/commercial xylan; it was not "
            "source-validated here and would not resolve larchwood specificity\"",
    "Sigmacell alpha Type 50": "9004-34-6 — \"Do not assign CAS 9004-34-6 without "
            "supplier documentation for S5504\"",
    "dextran, Mw ~1,270": "9004-54-0 — generic dextran; the record is qualified by "
            "a molecular weight the number does not carry",
    "Na2 beta-glycerol PO4 x 5 H2O": "13408-09-8 — the report hedges: literature "
            "links the number to β-glycerophosphate but \"does not explicitly "
            "confirm that this CAS is the exact disodium pentahydrate form rather "
            "than a less-specific parent/supplier entry\". This record is also one "
            "of a four-way duplicate cluster (see the tracking issue), which is "
            "the larger problem and should be settled before either is enriched",
    "Na2Glycerophosphate•5H2O": "13408-09-8 — same hedge, same duplicate cluster",
}

# Multi-part labels whose report names a CAS for exactly ONE component. Asserting
# it would claim the mixture IS its part, which is the over-claim #242 and #263
# exist to undo.
COMPONENT_ONLY = {
    "PY-fructose": "57-48-7 is fructose; the record is a medium",
    "Formate+methanol": "67-56-1 is methanol, one of two named components",
    "2-butanol+CO2": "78-92-2 is 2-butanol, one of two",
    "Cyclopentanol+CO2": "96-41-3 is cyclopentanol, one of two",
    "Glucose + Acetate": "50-99-7 is glucose, one of two",
    "PYG-0.02% Tween 80": "9005-65-6 is Tween 80, one component of a medium",
    "Esculin Ferric Citrate": "531-75-9 is esculin, one half of the reagent",
    "Vitamin B": "98-92-0 is niacinamide, one vitamin of a family label",
    "Amphotericin": "1397-89-3 is amphotericin B, the narrower variant of a "
                    "family name that also covers amphotericin A",
}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    doc = yaml.safe_load(UNMAPPED.read_text())
    n = 0
    for rec in doc["ingredients"]:
        term = (rec.get("preferred_term") or "").strip()
        if term not in APPLY:
            continue
        cas, denotes, because = APPLY[term]
        assert CAS_RE.match(cas), f"{cas} fails the #287 CAS pattern"
        cp = rec.setdefault("chemical_properties", {})
        if (cp.get("cas_rn") or "").strip():
            print(f"  SKIP {term}: already has {cp['cas_rn']}")
            continue
        cp["cas_rn"] = cas
        cp["data_source"] = "Edison LITERATURE deep research"
        rec.setdefault("curation_history", []).append({
            "timestamp": STAMP,
            "curator": "edison_cas_enrichment",
            "action": "ADDED_CAS_RN",
            "changes": (
                f"Added cas_rn {cas} ({denotes}) from Edison literature research: "
                f"{because}. Enrichment only — the mapping status is unchanged, "
                "because a CAS identifies a substance without supplying an ontology "
                "term. Applied only because the report AFFIRMS the number for this "
                "record's own substance: the same scan pulled CAS numbers out of "
                "five other reports that forbid them outright (HBO3, "
                "α-D-Glucose monohydrate, Larchwood xylan, Sigmacell alpha Type 50, "
                "dextran Mw ~1,270), because a CAS printed in a rejected-candidate "
                "row looks identical to one in a conclusion."),
            "llm_assisted": True,
        })
        n += 1
        print(f"  {term[:38]:40} += CAS {cas}  ({denotes})")

    print(f"\nrefused ({len(REFUSED)}), each on its own report's instruction:")
    for term, why in REFUSED.items():
        print(f"  {term[:38]:40} {why[:96]}")
    print(f"\ncomponent-of-mixture, not applied ({len(COMPONENT_ONLY)}):")
    for term, why in COMPONENT_ONLY.items():
        print(f"  {term[:38]:40} {why[:96]}")

    if args.apply and n:
        save_yaml(doc, UNMAPPED, validate=True, target_class="IngredientCollection")
        print(f"\nenriched {n} record(s)")
    else:
        print(f"\n{n} record(s) would be enriched (dry-run)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
