#!/usr/bin/env python3
"""Re-ground `Aspartate` from the charge-agnostic parent to aspartate(2-) (#319).

    CHEBI:132943  aspartate          <- current, charge-agnostic parent
      |- CHEBI:29995  aspartate(2-)  <- target
      `- CHEBI:35391  aspartate(1-)

Why this is defensible, and why it is a judgement rather than a mechanical fix:

* **Dominant convention.** 30 bare `-ate` labels in this corpus are grounded to a
  charged `X(n-)` term (fumarate, citrate, isocitrate, adipate, terephthalate,
  itaconate, …). Only 7 sit on a charge-agnostic parent that has a charged
  child, and `Aspartate` is one of them — so this moves an outlier into line.
* **Closest precedent.** `Glutamate` — same amino-acid family, same bare-label
  form, same microbedecoder import — is on `CHEBI:29987 glutamate(2-)`.
* **It adds no new claim.** Both terms are stereo-agnostic (neither is L- nor
  D-specific), so only protonation specificity changes; and `aspartate` is
  itself a ChEBI synonym of CHEBI:29995, so the lexical evidence that justified
  the original mapping survives intact.

**The counter-argument, recorded because it is real.** `MAPPING_SEMANTICS` §3
step 4 says an under-specified label with an unspecified-sense parent and *no
record-level evidence* should stay on the parent — and this record has no
synonyms and no chemical_properties. `Malate` is the exact same hierarchy shape
(`CHEBI:25115` with one child, `malate(2-)`) and stays. §3 never addresses
protonation, which is precisely the gap #319 asks to be closed.

So this fixes the highest-traffic case (431 occurrences against 0–13 for the
rest) on the strength of the sibling precedent, and leaves the other six for the
policy decision rather than presuming it:

    Malate, Succinate, Azelaate, Glutarate, Oxalate, Quinate

    python scripts/reground_aspartate.py            # dry-run
    python scripts/reground_aspartate.py --apply
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
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
STAMP = "2026-08-10T00:00:00+00:00"
CURATOR = "reground_aspartate"

FROM_ID, TO_ID = "CHEBI:132943", "CHEBI:29995"
TO_LABEL = "aspartate(2-)"
SUBJECT = "MIM:Aspartate"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    coll = yaml.safe_load(COLLECTION.read_text(encoding="utf-8", errors="replace")) or {}
    recs = coll.get("ingredients", [])
    if any(r.get("identifier") == TO_ID for r in recs):
        raise SystemExit(f"{TO_ID} is already a primary identifier — this would be a merge.")
    rec = next((r for r in recs if r.get("identifier") == FROM_ID), None)
    if rec is None:
        print(f"No record on {FROM_ID}; nothing to do (already re-grounded?).")
        return 0

    om = rec.setdefault("ontology_mapping", {})
    old_label = om.get("ontology_label")
    rec["identifier"] = TO_ID
    om["ontology_id"] = TO_ID
    om["ontology_label"] = TO_LABEL
    om["ontology_source"] = "CHEBI"
    om["mapping_quality"] = "SYNONYM_MATCH"   # 'aspartate' is a synonym of the target
    om.setdefault("evidence", []).append({
        "evidence_type": "DATABASE_MATCH",
        "source": "MIM curation (#319)",
        "notes": (
            f"Re-grounded {FROM_ID} -> {TO_ID}. {FROM_ID} is the charge-agnostic parent "
            f"whose children are aspartate(2-) and aspartate(1-), so a bare label sitting "
            f"on it declines to state a protonation state. The sibling record Glutamate — "
            f"same amino-acid family, same bare-label form, same import — is on "
            f"CHEBI:29987 glutamate(2-), and 30 other bare -ate labels in this corpus are "
            f"likewise on charged terms. Both terms are stereo-agnostic, so no "
            f"stereochemical claim is added; 'aspartate' is a ChEBI synonym of {TO_ID}, so "
            f"the lexical evidence survives. Counter-argument on record: MAPPING_SEMANTICS "
            f"§3 step 4 would keep an evidence-free under-specified label on the parent, "
            f"and Malate (same hierarchy shape) does exactly that — §3 does not address "
            f"protonation, which #319 tracks."
        ),
    })
    rec.setdefault("curation_history", []).append({
        "timestamp": STAMP, "curator": CURATOR, "action": "REGROUNDED_CHARGE_STATE",
        "changes": (f"identifier/ontology_id {FROM_ID} -> {TO_ID}; ontology_label "
                    f"{old_label!r} -> {TO_LABEL!r}; mapping_quality -> SYNONYM_MATCH (#319)."),
        "llm_assisted": False,
    })

    # subject_label is unchanged ('Aspartate'); only the object moves.
    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    sssom_change = None
    for i, line in enumerate(lines):
        if line.startswith(SUBJECT + "\t"):
            cells = line.rstrip("\n").split("\t")
            before = "\t".join(cells[:5])
            cells[3], cells[4] = TO_ID, TO_LABEL
            lines[i] = "\t".join(cells) + "\n"
            sssom_change = f"{before}  ->  " + "\t".join(cells[:5])
            break

    if args.apply:
        save_yaml(coll, COLLECTION)
        if sssom_change:
            SSSOM.write_text("".join(lines), encoding="utf-8")

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'}\n")
    print(f"  record : Aspartate  {FROM_ID} -> {TO_ID} ({TO_LABEL})")
    print(f"  sssom  : {sssom_change or 'NO MATCHING ROW — check the subject id'}")
    print("\n  Left for the #319 policy decision (same shape, not touched):")
    print("    Malate, Succinate, Azelaate, Glutarate, Oxalate, Quinate")
    return 0


if __name__ == "__main__":
    sys.exit(main())
