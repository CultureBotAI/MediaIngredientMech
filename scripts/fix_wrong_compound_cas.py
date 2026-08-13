#!/usr/bin/env python3
"""Correct or withdraw CAS numbers that denote a different compound (#320).

Distinct from the hydrate scrambling of #334: here the recorded `cas_rn` does not
name a different *form* of the right substance, it names a different substance.
`Sulfur (powder)` carried `7783-06-4`, which is **hydrogen sulfide** — a gas.

The record's ChEBI term is correct in every case; only the CAS moves.

*Corrected* (3) — ChEBI's own `hasDbXref` on the record's own term supplies a
replacement, so the new value comes from the term the record is already mapped
to rather than from a fresh lookup:

    Xylitol         CHEBI:17151 xylitol      488-81-3   (ribitol)          -> 87-99-0
    glycolaldehyde  CHEBI:17071 glycolaldehyde 23147-58-2 (the dimer)      -> 141-46-8
    Sulphur         CHEBI:17909 polysulfur   12597-03-4 (trisulfur)        -> 7704-34-9

*Withdrawn* (2) — the record's term carries no CAS xref, so no verified
replacement exists and the field is cleared rather than guessed:

    Sulfur (powder) CHEBI:33403 elemental sulfur, CAS was hydrogen sulfide
    D               CHEBI:29958 L-aspartic acid residue, CAS was limonene

`Sulfur (powder)` is worth a note: elemental sulfur's CAS `7704-34-9` *is* in
ChEBI, but on the sibling term `CHEBI:17909 polysulfur`, not on `CHEBI:33403`.
Copying it across terms would be a guess dressed as a citation, so it is left
out; the record simply loses a value that was affirmatively wrong.

`D` is a broken record, not merely a bad CAS — a single-character label mapped to
an amino-acid *residue* with a limonene CAS. Withdrawing the CAS removes the one
demonstrably false field; the label and mapping need an upstream source and are
tracked separately.

    python scripts/fix_wrong_compound_cas.py            # dry-run
    python scripts/fix_wrong_compound_cas.py --apply
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
CURATOR = "fix_wrong_compound_cas"
ISSUE = "#320"

# label -> (current cas, new cas, term, what the recorded value denotes)
CORRECT = {
    "Xylitol": ("488-81-3", "87-99-0", "CHEBI:17151", "ribitol, a different pentitol"),
    "glycolaldehyde": ("23147-58-2", "141-46-8", "CHEBI:17071",
                       "the glycolaldehyde dimer, not the monomer"),
    "Sulphur": ("12597-03-4", "7704-34-9", "CHEBI:17909",
                "trisulfur specifically, not polysulfur"),
}
# label -> (current cas, what it denotes, why nothing replaces it)
WITHDRAW = {
    "Sulfur (powder)": (
        "7783-06-4", "hydrogen sulfide, a gas",
        "CHEBI:33403 'elemental sulfur' carries no CAS xref in ChEBI. Elemental "
        "sulfur's 7704-34-9 does appear, but on the sibling term CHEBI:17909 "
        "'polysulfur' — copying it across terms would be a guess dressed as a "
        "citation"),
    "D": (
        "138-86-3", "limonene",
        "CHEBI:29958 'L-aspartic acid residue' carries no CAS xref, and this record "
        "is broken beyond its CAS: a single-character label mapped to an amino-acid "
        "residue. The label and mapping need an upstream source"),
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
                skipped.append(f"{label}: cas is {current!r}, expected {expect!r}")
                continue
            cp["cas_rn"] = new
            rec["chemical_properties"] = cp
            rec.setdefault("curation_history", []).append({
                "timestamp": STAMP, "curator": CURATOR, "action": "CORRECTED_WRONG_COMPOUND_CAS",
                "changes": (
                    f"cas_rn {expect!r} -> {new!r} ({ISSUE}). The recorded value denotes "
                    f"{denotes} — a different compound, not a different form of this one. "
                    f"Replaced with ChEBI's hasDbXref on {term}, the term this record is "
                    f"already mapped to, so the new value comes from the existing mapping "
                    f"rather than a fresh lookup."),
                "llm_assisted": False,
            })
            fixed.append(f"{label:<16} {expect:<12} -> {new:<11} ({denotes})")

        elif label in WITHDRAW:
            expect, denotes, why = WITHDRAW[label]
            if current != expect:
                skipped.append(f"{label}: cas is {current!r}, expected {expect!r}")
                continue
            cp.pop("cas_rn", None)
            rec["chemical_properties"] = cp
            rec.setdefault("curation_history", []).append({
                "timestamp": STAMP, "curator": CURATOR, "action": "WITHDREW_WRONG_CAS",
                "changes": (
                    f"cas_rn {expect!r} removed ({ISSUE}). It denotes {denotes}, a different "
                    f"substance from the one this record names. No verified replacement: "
                    f"{why}. Cleared rather than guessed."),
                "llm_assisted": False,
            })
            cleared.append(f"{label:<16} {expect:<12} removed ({denotes})")

    if args.apply and (fixed or cleared):
        save_yaml(coll, COLLECTION)

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'} — "
          f"{len(fixed)} corrected, {len(cleared)} withdrawn\n")
    for f in fixed:
        print(f"  FIX      {f}")
    for c in cleared:
        print(f"  WITHDRAW {c}")
    for s in skipped:
        print(f"  SKIPPED  {s}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
