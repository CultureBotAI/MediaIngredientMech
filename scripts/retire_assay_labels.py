#!/usr/bin/env python3
"""Retire 7 labels that name an assay or a splice, and mint the 8th (#213/#308).

The last of the microbedecoder residual. Deep research over the API 20 NE reading
table, the ASM gelatinase protocol, Biolog panel listings and MicrO settled all
eight, and the decisive check was local rather than bibliographic:

**Every substrate CURIE one might use as the primary identity is already held by a
live record.** Assigning it to another same-substance label would mint an
unreviewed duplicate family rather than add coverage — the defect
fixed in #370 for `Butane-1,4-diol`, which this script exists partly to avoid
repeating:

    CHEBI:4853   esculin           held by `Esculin Monohydrate`
    CHEBI:5291   gelatin           held by `Gelatine`
    CHEBI:355715 PNPG              held by `4-nitrophenyl beta-D-galactopyranoside`
    CHEBI:78019  TTC               held by `2,3,5-Triphenyltetrazolium chloride`
    CHEBI:73801  Gly-Glu           held by `Gly-Glu`
    CHEBI:73706  bromosuccinate    held by `Bromosuccinate`
    CHEBI:35621  DL-2-aminobutyrate held by `DL-2-Aminobutyric acid`
    CHEBI:16865  GABA              held by `gamma-Aminobutyric acid`

## Retired (7)

Four name an ASSAY or its OUTCOME, not a weighable substance. The API 20 NE table
puts esculin, gelatin and PNPG in the *active ingredients* column and hydrolysis
in the *reactions/enzymes* column, and MicrO models each as an assay class. The
assay CURIE is recorded as a cross-reference in the notes — it is not used as the
mapping, because the record is being retired as an ingredient, not reclassified
as an assay.

Two are splices of two real panel substrates each, from the comma-stripping
ingest of #308. One is an unrecoverable fragment.

**No synonyms are folded onto the substrate records.** `Esculin Hydrolysate` is
not a synonym of esculin — it names the reaction. Adding it would make
`label_index.csv` resolve the assay name to the substrate, asserting an identity
that does not hold.

## Minted (1)

`Mineral solution see Medium No. 976` is a MediaDive cross-reference, but the
corpus already treats that shape as a stock solution rather than retiring it:
`Trace element solution see Medium No. 187` and `Vitamin solution see Medium
No. 403` are both live `kgmicrobe.ingredient:` mints. This follows them.

    python scripts/retire_assay_labels.py            # dry-run
    python scripts/retire_assay_labels.py --apply
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
import yaml  # noqa: E402

from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
UNMAPPED = ROOT / "data" / "curated" / "unmapped_ingredients.yaml"
STAMP = "2026-08-15T00:00:00+00:00"
CURATOR = "retire_assay_labels"
ISSUE = "#213/#308"

RETIRE = {
    "Esculin Hydrolysate": (
        "names the esculin-hydrolysis TEST, not a substance. The API 20 NE reading "
        "table lists esculin and ferric citrate as the cupule's active ingredients "
        "and hydrolysis as the reaction; MicrO models it as MICRO:0000722 'esculin "
        "ferric citrate assay'. The reagents are already records: `Esculin "
        "Monohydrate` (CHEBI:4853) and `Esculin Ferric Citrate`; the released "
        "aglycone esculetin is CHEBI:490095"),
    "Gelatin Hydrolyzed": (
        "names the gelatinase TEST result, not a substance. MicrO models it as "
        "MICRO:0000649 'gelatinase assay'. Hydrolysed gelatin does exist as a "
        "commercial product, but neither ChEBI nor FOODON has a term distinguishing "
        "it from gelatin, and a phenotype table reports the reaction. The substrate "
        "is already a record: `Gelatine` (CHEBI:5291)"),
    "4-nitrophenyl Beta-D-galactopyranoside Hydrolysate": (
        "names the beta-galactosidase TEST outcome — 4-nitrophenol released, yellow "
        "— not a substance. MicrO models it as MICRO:0000724 'beta-galactosidase "
        "assay with PNPG'. The substrate is already a record: `4-nitrophenyl "
        "beta-D-galactopyranoside` (CHEBI:355715), and the product 4-nitrophenol is "
        "CHEBI:16836"),
    "Tetrazolium": (
        "a bare family name reporting a reduction readout. ChEBI has no generic "
        "tetrazolium class — only specific salts — and MicrO models the readout as "
        "MICRO:0000270 'tetrazolium reduction assay'. The salt actually used in "
        "bacterial media, TTC, is already a record: `2,3,5-Triphenyltetrazolium "
        "chloride` (CHEBI:78019). Grounding the bare family name to one of its "
        "members is the error #368 records for sulfur"),
    "Glycyl-L-bromosuccinic Glutamic Acid": (
        "a splice of TWO Biolog panel substrates run together by the #308 ingest: "
        "`glycyl-L-glutamic acid` and `bromosuccinic acid`. Both are already "
        "records — `Gly-Glu` (CHEBI:73801) and `Bromosuccinate` (CHEBI:73706) — so "
        "there is nothing left to ground once the splice is recognised"),
    "DL-2-gamma-aminobutyrate": (
        "a splice of two panel substrates by the same ingest: DL-2-aminobutyrate and "
        "gamma-aminobutyrate. Both are already records — `DL-2-Aminobutyric acid` "
        "(CHEBI:35621) and `gamma-Aminobutyric acid` (CHEBI:16865). No single "
        "compound has this name"),
    "3-methylacetate": (
        "not a chemical name and not reconstructable. It is a fragment from the same "
        "importer that produced `Formate+3-methyl Mercaptopropionate`, so the likely "
        "original is `3-methyl mercaptopropionate` — but its partner text is absent "
        "from the corpus, and guessing it would invent a compound"),
}

MINT = {
    "Mineral solution see Medium No. 976": (
        "kgmicrobe.ingredient:mineral_solution_see_medium_no_976",
        "a MediaDive cross-reference to the mineral/trace-elements solution of DSMZ "
        "Medium 976. The corpus already treats this shape as a stock solution rather "
        "than retiring it — `Trace element solution see Medium No. 187` and `Vitamin "
        "solution see Medium No. 403` are both live kgmicrobe.ingredient mints under "
        "the #288 convention — so this follows its siblings. The composition is not "
        "transcribed here: it lives in the referenced medium, and #288's rule is to "
        "mint the named preparation rather than inline someone else's recipe"),
}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    colls = {p: (yaml.safe_load(p.read_text(encoding="utf-8", errors="replace")) or {})
             for p in (MAPPED, UNMAPPED)}
    index = {}
    for coll in colls.values():
        for rec in coll.get("ingredients", []) or []:
            index.setdefault(str(rec.get("preferred_term") or ""), rec)

    retired, minted, skipped = [], [], []

    for label, why in RETIRE.items():
        rec = index.get(label)
        if rec is None or rec.get("mapping_status") not in ("NEEDS_EXPERT", "PENDING_REVIEW"):
            skipped.append(f"{label}: absent or already resolved")
            continue
        note = (f"Retired as an ingredient record ({ISSUE}): {why}. Not mapped, because "
                f"every substrate identity it could use is already held by a live "
                f"record, so a mapping here would mint an unreviewed duplicate family "
                f"rather than add coverage. No "
                f"synonym is folded onto those records either: this label names a "
                f"reaction or a splice, not the substance, and asserting the synonymy "
                f"would make label_index resolve it to something it does not denote.")
        rec["mapping_status"] = "REJECTED"
        occ = rec.setdefault("occurrence_statistics", {})
        occ["total_occurrences"] = 0
        occ["media_count"] = 0
        rec["notes"] = ((str(rec.get("notes") or "") + " ").strip() + " " + note).strip()
        rec.setdefault("curation_history", []).append({
            "timestamp": STAMP, "curator": CURATOR, "action": "RETIRED_NOT_AN_INGREDIENT",
            "previous_status": "NEEDS_EXPERT", "new_status": "REJECTED",
            "changes": note, "llm_assisted": False})
        retired.append(f"{label[:50]:<52} REJECTED")

    for label, (mint, why) in MINT.items():
        rec = index.get(label)
        if rec is None or rec.get("mapping_status") not in ("NEEDS_EXPERT", "PENDING_REVIEW"):
            skipped.append(f"{label}: absent or already resolved")
            continue
        old = rec.get("identifier")
        rec["identifier"] = mint
        rec["mapping_status"] = "MAPPED"
        rec["ingredient_type"] = "STOCK_SOLUTION"
        note = f"Minted under the #288 STOCK_SOLUTION convention: {why}."
        om = rec.setdefault("ontology_mapping", {})
        om.update({"ontology_id": mint, "ontology_label": label,
                   "ontology_source": "kgmicrobe.ingredient",
                   "mapping_quality": "FALLBACK_REGISTRY"})
        om.setdefault("evidence", []).append({
            "evidence_type": "MANUAL_CURATION",
            "source": f"MIM curation ({ISSUE})", "notes": note})
        rec.setdefault("curation_history", []).append({
            "timestamp": STAMP, "curator": CURATOR, "action": "PROMOTED_TO_MAPPED",
            "previous_status": "NEEDS_EXPERT", "new_status": "MAPPED",
            "changes": f"{old} -> {mint} (FALLBACK_REGISTRY). {note}",
            "llm_assisted": False})
        minted.append(f"{label[:50]:<52} {mint}")

    if args.apply and (retired or minted):
        # A record promoted to MAPPED must MOVE to mapped_ingredients.yaml.
        # reconcile_sssom reads only that file, so a promotion left in place is
        # curated but unpublished — the defect #370 fixed for 62 records. Any
        # promotion path that skips this step recreates it, and this script is
        # such a path.
        um = colls[UNMAPPED]["ingredients"]
        movers = [r for r in um if r.get("mapping_status") == "MAPPED"]
        if movers:
            colls[UNMAPPED]["ingredients"] = [r for r in um if r not in movers]
            colls[MAPPED]["ingredients"] = movers + colls[MAPPED]["ingredients"]
            print(f"  moved {len(movers)} promoted record(s) into mapped_ingredients.yaml (#370)")
        for path, coll in colls.items():
            recs = coll.get("ingredients") or []
            coll["total_count"] = len(recs)
            coll["mapped_count"] = sum(1 for r in recs if r.get("mapping_status") == "MAPPED")
            coll["unmapped_count"] = sum(1 for r in recs if r.get("mapping_status") == "UNMAPPED")
            save_yaml(coll, path)

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'} — "
          f"{len(retired)} retired, {len(minted)} minted\n")
    for r in retired:
        print(f"  {r}")
    print()
    for m in minted:
        print(f"  {m}")
    for s in skipped:
        print(f"  SKIPPED {s}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
