#!/usr/bin/env python3
"""Correct or withdraw CAS numbers that name the wrong hydrate (#320, #334).

Seven records carry a `cas_rn` denoting a hydration state their own label
contradicts — `NiCl2 x 2 H2O` and `NiCl2 x 5 H2O` both carry the *hexahydrate's*
`7791-20-0`, `CaCl2 x 6 H2O` carries anhydrous `10043-52-4`. This is the #334
scrambling: one CAS applied across a whole salt family regardless of hydration.

Two remedies, and which applies turns on whether the record's ChEBI term matches
the hydration state the label states:

*Correct* (3) — the term is the specific hydrate the label names, so **ChEBI's own
`hasDbXref` on that term** is the right CAS. That xref is independent of the
recorded value being replaced, which is the provenance standard §3 sets:

    CaCl2 x 6 H2O  CHEBI:91243 calcium chloride hexahydrate  10043-52-4 -> 7774-34-7
    Na2S x 9 H2O   CHEBI:76209 sodium sulfide nonahydrate    1313-82-2  -> 1313-84-4
    Na2SeO3        CHEBI:48843 disodium selenite             26970-82-1 -> 10102-18-8

*Withdraw* (4) — the term is the **anhydrous or generic parent**, so its xref is
the anhydrous CAS and is just as wrong for a hydrate as the recorded value.
Substituting one wrong number for another would look like a fix while publishing
a second false identifier, so the field is cleared instead. Nothing true is lost:
the recorded value demonstrably denotes a different substance.

    NiCl2 x 2 H2O    7791-20-0  is the hexahydrate; term is anhydrous NiCl2
    NiCl2 x 5 H2O    7791-20-0  is the hexahydrate; term is anhydrous NiCl2
    NiSO4 x 7 H2O    10101-97-0 is the hexahydrate; term is generic nickel sulfate
    Na2MoO4 x 7 H2O  10102-40-6 is the dihydrate;   term has no CAS xref at all

**Three lookalikes are deliberately left alone**: `alpha-Lactose`,
`Sodium Citrate` and `Meropenem` carry a CAS for the monohydrate, dihydrate and
trihydrate respectively, but none of their labels states a hydration state — so
the CAS is more specific than the label rather than contradicting it. That is the
same modelling gap as #342 (ChEBI does not subsume a hydrate under its anhydrous
form), and it reads as a conflict only because of it.

    python scripts/fix_scrambled_hydrate_cas.py            # dry-run
    python scripts/fix_scrambled_hydrate_cas.py --apply
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
CURATOR = "fix_scrambled_hydrate_cas"
ISSUE = "#320/#334"

# label -> (expected current cas, new cas, term, what the recorded value denotes)
CORRECT = {
    "CaCl2 x 6 H2O": ("10043-52-4", "7774-34-7", "CHEBI:91243",
                      "anhydrous calcium dichloride"),
    "Na2S x 9 H2O": ("1313-82-2", "1313-84-4", "CHEBI:76209",
                     "anhydrous sodium sulfide"),
    "Na2SeO3": ("26970-82-1", "10102-18-8", "CHEBI:48843",
                "disodium selenite pentahydrate, while the label is the bare formula"),
}
# label -> (expected current cas, what it denotes, why no replacement exists)
WITHDRAW = {
    "NiCl2 x 2 H2O": ("7791-20-0", "nickel chloride hexahydrate",
                      "the record's term CHEBI:34887 is anhydrous nickel dichloride, so "
                      "its xref 7718-54-9 is the anhydrous CAS — wrong for a dihydrate"),
    "NiCl2 x 5 H2O": ("7791-20-0", "nickel chloride hexahydrate",
                      "the record's term CHEBI:34887 is anhydrous nickel dichloride, so "
                      "its xref 7718-54-9 is the anhydrous CAS — wrong for a pentahydrate"),
    "NiSO4 x 7 H2O": ("10101-97-0", "nickel sulfate hexahydrate",
                      "the record's term CHEBI:53001 is generic nickel sulfate, so its "
                      "xref 7786-81-4 is the anhydrous CAS — wrong for a heptahydrate"),
    "Na2MoO4 x 7 H2O": ("10102-40-6", "sodium molybdate dihydrate",
                        "the record's term CHEBI:86473 (heptahydrate) carries no CAS "
                        "xref in ChEBI, so no verified replacement exists"),
}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    coll = yaml.safe_load(COLLECTION.read_text(encoding="utf-8", errors="replace")) or {}
    fixed: list[str] = []
    cleared: list[str] = []
    skipped: list[str] = []

    for rec in coll.get("ingredients", []):
        if rec.get("mapping_status") == "REJECTED":
            continue
        label = str(rec.get("preferred_term") or "")
        cp = rec.get("chemical_properties") or {}
        current = str(cp.get("cas_rn") or "").strip()

        if label in CORRECT:
            expect, new, term, denotes = CORRECT[label]
            if current != expect:
                skipped.append(f"{label}: cas is {current!r}, expected {expect!r} — "
                               f"moved since this was verified")
                continue
            cp["cas_rn"] = new
            rec["chemical_properties"] = cp
            rec.setdefault("curation_history", []).append({
                "timestamp": STAMP, "curator": CURATOR, "action": "CORRECTED_SCRAMBLED_CAS",
                "changes": (
                    f"cas_rn {expect!r} -> {new!r} ({ISSUE}). The recorded value denotes "
                    f"{denotes}, contradicting the hydration state this record's own label "
                    f"states. Replaced with ChEBI's hasDbXref on {term}, the specific term "
                    f"this record is mapped to — provenance independent of the value being "
                    f"replaced, per MAPPING_SEMANTICS §3."),
                "llm_assisted": False,
            })
            fixed.append(f"{label:<18} {expect:<12} -> {new:<12} ({term})")

        elif label in WITHDRAW:
            expect, denotes, why = WITHDRAW[label]
            if current != expect:
                skipped.append(f"{label}: cas is {current!r}, expected {expect!r} — "
                               f"moved since this was verified")
                continue
            cp.pop("cas_rn", None)
            rec["chemical_properties"] = cp
            rec.setdefault("curation_history", []).append({
                "timestamp": STAMP, "curator": CURATOR, "action": "WITHDREW_WRONG_CAS",
                "changes": (
                    f"cas_rn {expect!r} removed ({ISSUE}). It denotes {denotes}, which "
                    f"contradicts the hydration state this record's label states — the "
                    f"#334 scrambling, where one CAS is applied across a salt family "
                    f"regardless of hydration. No verified replacement is available: "
                    f"{why}. Cleared rather than substituted, because swapping in a second "
                    f"wrong number would read as a correction while still publishing a "
                    f"false identifier."),
                "llm_assisted": False,
            })
            cleared.append(f"{label:<18} {expect:<12} removed ({denotes})")

    if args.apply and (fixed or cleared):
        save_yaml(coll, COLLECTION)

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'} — "
          f"{len(fixed)} corrected, {len(cleared)} withdrawn\n")
    print(f"  Corrected from ChEBI's xref on the record's own specific term ({len(fixed)}):")
    for f in fixed:
        print(f"     {f}")
    print(f"\n  Withdrawn — no verified replacement exists ({len(cleared)}):")
    for c in cleared:
        print(f"     {c}")
    for s in skipped:
        print(f"\n  SKIPPED {s}")
    print("\n  Left alone: alpha-Lactose, Sodium Citrate, Meropenem — their labels state "
          "no hydration state, so a hydrate CAS is more specific than the label rather "
          "than contradicting it (the #342 modelling gap).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
