#!/usr/bin/env python3
"""Reground `Aromatic hydrocarbon` to CHEBI:33658 `arene` (SSSOM delivery).

This is the corpus's **only** `skos:broadMatch` row, and it is the one row
kg-microbe reads backwards.

## Why it inverts downstream

`MAPPING_SEMANTICS` §`skos:broadMatch` defines it as *"MIM:X is broader than Y;
Y is a kind-of MIM:X"*. kg-microbe's consolidator treats **both** asymmetric
predicates identically —

    # Asymmetric matches (skos:narrowMatch / broadMatch): the MIM
    # subject is a NARROWER concept than the ontology object

— so it emits `Aromatic hydrocarbon` as a **child** of `polycyclic arene`, which
is the opposite of what MIM asserts and is chemically false: polycyclic arenes
are a subset of aromatic hydrocarbons, not the other way round.

## The record contradicts itself

Its own history holds both readings:

    REGRADED_CLASS_OVERSTATEMENT  EXACT_MATCH -> BROAD_MATCH (#322);
                                  "the record is BROADER than the term"
    MINTED_REGISTRY_IDENTIFIER    CHEBI:33848 -> kgmicrobe.compound:...
                                  "The record is narrower than CHEBI:33848"

The regrade was right and the mint applied §3 step 3's boilerplate rationale
without re-reading it. A mint exists to give a record that is *narrower* than
every available term its own identity; this record is broader, so the mint was
never the right instrument.

## The fix is step 1, not a predicate flip

`MAPPING_SEMANTICS` §3 step 1 says use the specific ontology term when one
exists, and one does — it was simply never looked for:

    CHEBI:33658  'arene'            "Any monocyclic or polycyclic aromatic hydrocarbon."
    CHEBI:33848  'polycyclic arene' "A polycyclic aromatic hydrocarbon."

CHEBI:33658's definition *is* the record's name. Grounding there makes the
mapping symmetric and true, which removes the broadMatch row rather than
arguing about its direction, and drops the mint the record never needed.
CHEBI:33658 is held by no other record.

**This is not a #322 class-term overstatement.** That defect is a *specific
substance* asserted equal to a *class*. Here both sides are the same class: the
MIM record is the ingredient category "aromatic hydrocarbon" and `arene` is that
category. Graded SYNONYM_MATCH, since `arene` is ChEBI's preferred label and
`aromatic hydrocarbon` its synonym.

The record has 0 occurrences, so nothing downstream depends on the old shape.

    python scripts/reground_aromatic_hydrocarbon.py            # dry-run
    python scripts/reground_aromatic_hydrocarbon.py --apply
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
import yaml  # noqa: E402

from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
DATE = "2026-08-18"
STAMP = f"{DATE}T00:00:00+00:00"
CURATOR = "reground_aromatic_hydrocarbon"

LABEL = "Aromatic hydrocarbon"
OLD_ID = "kgmicrobe.compound:aromatic_hydrocarbon"
OLD_TERM = "CHEBI:33848"
NEW_TERM = "CHEBI:33658"
NEW_LABEL = "arene"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    mapped = yaml.safe_load(MAPPED.read_text(encoding="utf-8")) or {}
    records = mapped.get("ingredients") or []
    rec = next((r for r in records if str(r.get("preferred_term")) == LABEL), None)
    if rec is None:
        print(f"SKIP: no record {LABEL!r}")
        return 0
    if str(rec.get("identifier")) != OLD_ID:
        print(f"SKIP: {LABEL!r} is on {rec.get('identifier')}, expected {OLD_ID}")
        return 0
    holder = next((r for r in records
                   if str(r.get("identifier")) == NEW_TERM and r is not rec), None)
    if holder is not None:
        print(f"SKIP: {NEW_TERM} already held by {holder.get('preferred_term')!r}")
        return 0

    note = (
        f"Regrounded {OLD_TERM} ({OLD_ID}) -> {NEW_TERM} {NEW_LABEL!r}. "
        f"CHEBI:33658 is defined as 'Any monocyclic or polycyclic aromatic "
        f"hydrocarbon', which is exactly what this record names; CHEBI:33848 "
        f"'polycyclic arene' is a proper subset of it. The old shape asserted "
        f"skos:broadMatch — the corpus's only one — and kg-microbe's "
        f"consolidator reads narrowMatch and broadMatch identically as 'the MIM "
        f"subject is NARROWER than the object', so it published this record as a "
        f"CHILD of polycyclic arene: backwards, and chemically false. The "
        f"record's own history carried both readings, the regrade calling it "
        f"broader and the mint that followed calling it narrower. Grounding at "
        f"the term that actually denotes it makes the mapping symmetric and true, "
        f"which removes the disagreement rather than arguing about direction, and "
        f"retires a registry mint the record never needed — a mint gives identity "
        f"to a record NARROWER than every available term. Not a #322 class "
        f"overstatement: both sides are the same class.")

    om = rec.setdefault("ontology_mapping", {})
    rec["identifier"] = NEW_TERM
    om.update({"ontology_id": NEW_TERM, "ontology_label": NEW_LABEL,
               "ontology_source": "CHEBI", "mapping_quality": "SYNONYM_MATCH"})
    om.setdefault("evidence", []).append({
        "evidence_type": "MANUAL_CURATION",
        "source": "MIM curation (SSSOM delivery review)", "notes": note})
    rec.setdefault("curation_history", []).append({
        "timestamp": STAMP, "curator": CURATOR,
        "action": "REGROUNDED_TO_DENOTING_TERM",
        "changes": note, "llm_assisted": False})

    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    kept, dropped, subject = [], 0, None
    for line in lines:
        cells = line.rstrip("\n").split("\t")
        # Drop BOTH old rows: the broadMatch to polycyclic arene and the
        # registry exactMatch that only existed to satisfy Rule B1 for it.
        if len(cells) >= 4 and cells[1] == LABEL and cells[3] in (OLD_TERM, OLD_ID):
            subject = subject or cells[0]      # keep the EXISTING MIM: subject
            dropped += 1
            continue
        kept.append(line)

    # reconcile_sssom refuses to invent provenance for a new row ("GAP(s) need
    # new rows with full provenance — not auto-added"), which is correct: a
    # generated row would claim a curation that never happened. So the
    # replacement is written here, reusing the subject the dropped rows already
    # carried rather than re-deriving it from the label — re-derivation is the
    # mistake #293/#307 record, and it silently matches nothing.
    hdr = next(i for i, l in enumerate(kept) if l.startswith("subject_id"))
    ncols = len(kept[hdr].rstrip("\n").split("\t"))
    row = [subject or f"MIM:{LABEL.replace(' ', '_')}", LABEL, "skos:exactMatch",
           NEW_TERM, NEW_LABEL, "obo:chebi.owl", "semapv:ManualMappingCuration",
           f"MIM:curation (SSSOM delivery review)|MIM:curator={CURATOR}",
           DATE, "0.95", "", "", f"manual:{CURATOR}|{DATE}"]
    kept.insert(hdr + 1, "\t".join((row + [""] * ncols)[:ncols]) + "\n")

    if args.apply:
        save_yaml(mapped, MAPPED)
        SSSOM.write_text("".join(kept), encoding="utf-8")

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'}\n")
    print(f"  {LABEL!r}")
    print(f"     identifier  {OLD_ID} -> {NEW_TERM}")
    print(f"     term        {OLD_TERM} 'polycyclic arene' -> {NEW_TERM} {NEW_LABEL!r}")
    print(f"     quality     BROAD_MATCH -> SYNONYM_MATCH  (predicate -> skos:exactMatch)")
    print(f"     dropped {dropped} SSSOM row(s); reconcile_sssom re-emits the new one")
    print(f"\n  This was the corpus's only skos:broadMatch row.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
