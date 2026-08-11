#!/usr/bin/env python3
"""Correct `3',6-Dihydroxyflavone`, which carries a different compound's identity (#324).

The record's label names one compound and every other field describes another:

    label            3',6-Dihydroxyflavone      = PubChem CID 688662, C15H10O4
    identifier       cas:71592-46-6         ->    PubChem CID 676293, C17H14O4
    chemical_props   C17H14O4, SMILES with two methoxy groups, CID 676293
    ontology parent  CHEBI:107657 "6-methoxy-2-(3-methoxyphenyl)-1-benzopyran-4-one"

Verified against PubChem: CID 676293 is titled **6,3'-Dimethoxyflavone** and
CID 688662 is **6,3'-Dihydroxyflavone**, whose synonym list contains the literal
string `3',6-DIHYDROXYFLAVONE`. They differ by two methyls, +28.05 Da.

**The CAS is the root defect, not the mapping.** `CREATED_FROM_CAS_FALLBACK`
took 71592-46-6 from `CultureBotHT compounds_to_cas.csv`, then
`AUTO_BACKFILL_PUBCHEM_CHEMISTRY` resolved that CAS and imported the dimethoxy
compound's formula, SMILES, InChI and CID, and `BACKFILL_PARENT_CHEBI` followed
the same CID to a dimethoxy parent. Every downstream field is self-consistent
*with each other* and wrong for the label — which is why no internal check
caught it.

Resolution follows MAPPING_SEMANTICS §3 in order:

  step 1  no exact term — 13 dihydroxyflavone terms exist in ChEBI, none is the
          6,3'- isomer, and a lookup by the compound's InChIKey
          (YHLLABKHTFWHSZ) returns nothing.
  step 2  unavailable — PubChem lists **no CAS** for CID 688662, and the CAS it
          had belongs to a different substance, so there is none to anchor to.
  step 3  applies — mint `kgmicrobe.compound:<slug>`, `narrowMatch` to the
          nearest real parent, plus the Rule B1 registry row.

The wrong chemistry is removed rather than replaced. Correct values for CID
688662 are known (C15H10O4, InChIKey YHLLABKHTFWHSZ-UHFFFAOYSA-N) but populating
them is a separate enrichment decision; leaving the block empty is honest, and
`ingredient_type` no longer has "chemical structure populated" as its basis.

    python scripts/fix_dihydroxyflavone_wrong_compound.py            # dry-run
    python scripts/fix_dihydroxyflavone_wrong_compound.py --apply
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
CURATOR = "fix_dihydroxyflavone_wrong_compound"

OLD_ID = "cas:71592-46-6"
NEW_ID = "kgmicrobe.compound:36-dihydroxyflavone"
LABEL = "3',6-Dihydroxyflavone"
SUBJECT = "MIM:36-Dihydroxyflavone"
PARENT_ID, PARENT_LABEL = "CHEBI:24698", "hydroxyflavone"
JUSTIFICATION = "semapv:ManualMappingCuration"
SOURCE = "MIM:curation (#324)"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    coll = yaml.safe_load(COLLECTION.read_text(encoding="utf-8", errors="replace")) or {}
    rec = next((r for r in coll.get("ingredients", []) if r.get("identifier") == OLD_ID), None)
    if rec is None:
        print(f"No record on {OLD_ID}; nothing to do.")
        return 0

    dropped = dict(rec.get("chemical_properties") or {})
    rec["identifier"] = NEW_ID
    rec["chemical_properties"] = {}
    om = rec.setdefault("ontology_mapping", {})
    om["ontology_id"] = PARENT_ID
    om["ontology_label"] = PARENT_LABEL
    om["ontology_source"] = "CHEBI"
    om["mapping_quality"] = "NARROW_MATCH"
    # The two pre-existing evidence notes both assert the wrong compound's
    # provenance ("matched_via='pubchem CID 676293'"), so they are superseded
    # rather than left to be read as corroboration.
    for ev in om.get("evidence") or []:
        note = str(ev.get("notes", ""))
        if not note.startswith("SUPERSEDED"):
            ev["notes"] = (f"SUPERSEDED (#324): this evidence describes CID 676293, "
                           f"6,3'-dimethoxyflavone, which is NOT this ingredient. "
                           f"Original note follows. {note}")
    om.setdefault("evidence", []).append({
        "evidence_type": "DATABASE_MATCH",
        "source": "MIM curation (#324)",
        "notes": (
            "Re-grounded per MAPPING_SEMANTICS §3 step 3. The label names PubChem CID "
            "688662 6,3'-dihydroxyflavone (C15H10O4, InChIKey YHLLABKHTFWHSZ-UHFFFAOYSA-N), "
            "whose synonyms include the literal string \"3',6-DIHYDROXYFLAVONE\". ChEBI has "
            "no term for it — 13 dihydroxyflavone terms exist, none the 6,3'- isomer, and an "
            "InChIKey lookup returns nothing — and PubChem lists no CAS for it, so steps 1 "
            "and 2 are both unavailable. Previous identifier cas:71592-46-6 belongs to CID "
            "676293 6,3'-dimethoxyflavone (C17H14O4), two methyls heavier."),
    })
    rec.setdefault("curation_history", []).append({
        "timestamp": STAMP, "curator": CURATOR, "action": "CORRECTED_WRONG_COMPOUND",
        "changes": (
            f"identifier {OLD_ID} -> {NEW_ID}; ontology_mapping CHEBI:107657 "
            f"(a dimethoxy compound) -> {PARENT_ID} {PARENT_LABEL} NARROW_MATCH; "
            f"chemical_properties cleared (they described CID 676293, not this "
            f"ingredient: {dropped.get('molecular_formula')}, CID "
            f"{dropped.get('pubchem_cid')}, sourced {dropped.get('data_source')}). "
            f"Root cause is the CAS in compounds_to_cas.csv, which belongs to "
            f"6,3'-dimethoxyflavone; the chemistry and parent backfills then followed it "
            f"and agreed with each other, so no internal check could see the conflict (#324)."),
        "llm_assisted": False,
    })

    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    kept = [ln for ln in lines if not ln.startswith(SUBJECT + "\t")]
    removed = len(lines) - len(kept)
    date = STAMP[:10]
    # The file is 13 columns wide (…confidence, comment, other, validation_method).
    # A short row parses into a dict missing those keys and crashes the
    # reconciler with KeyError, so every emitted row is padded to full width.
    ncols = len(next(ln for ln in lines if ln.startswith("subject_id")).rstrip("\n").split("\t"))

    def row(predicate: str, obj_id: str, obj_label: str, obj_source: str) -> str:
        cells = [SUBJECT, LABEL, predicate, obj_id, obj_label, obj_source,
                 JUSTIFICATION, SOURCE, date]
        cells += [""] * (ncols - len(cells))
        return "\t".join(cells) + "\n"

    new_rows = [
        row("skos:narrowMatch", PARENT_ID, PARENT_LABEL, "obo:chebi.owl"),
        row("skos:exactMatch", NEW_ID, LABEL, "kgm:compound"),
    ]
    # Insert in the file's sort order by subject id, as the reconciler expects.
    # Start *after* the `subject_id` header, not at it: the header's first cell
    # sorts above any `MIM:` subject, so anchoring on it puts the new rows above
    # the header and every subsequent row parses without a subject_label.
    header_idx = next(i for i, ln in enumerate(kept) if ln.startswith("subject_id\t"))
    idx = len(kept)
    for i in range(header_idx + 1, len(kept)):
        if kept[i].split("\t", 1)[0] > SUBJECT:
            idx = i
            break
    kept[idx:idx] = new_rows

    if args.apply:
        save_yaml(coll, COLLECTION)
        SSSOM.write_text("".join(kept), encoding="utf-8")

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'}\n")
    print(f"  identifier          {OLD_ID} -> {NEW_ID}")
    print(f"  ontology_mapping    CHEBI:107657 (dimethoxy!) -> {PARENT_ID} {PARENT_LABEL} [NARROW_MATCH]")
    print(f"  chemical_properties cleared: {dropped.get('molecular_formula')} / CID {dropped.get('pubchem_cid')}")
    print(f"  sssom               {removed} stale row(s) replaced by 2 (parent + Rule B1 registry)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
