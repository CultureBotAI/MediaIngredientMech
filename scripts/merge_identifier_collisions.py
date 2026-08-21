#!/usr/bin/env python3
"""Merge the unambiguous identifier collisions from #414.

30 ontology CURIEs are held by two or more LIVE records, which MIM's own rule
forbids: for a mapped record the `identifier` IS the ontology CURIE, so two live
records on one CURIE assert that two ingredients are the same thing.

This script clears **six** of them — only the pairs where the two labels denote
the same substance under any reading, differing in spacing, abbreviation or
brand. The other 24 need per-case judgement and are deliberately left alone.

## Why a chemistry test is not enough to pick these

The obvious rule — "merge when CAS and molecular formula agree" — classifies 22
of the 30 as mergeable, and it is wrong about most of them:

    cas:9036-88-8    'b-Mannan borohydrate reduced carob seed'
                     'Mannan from Saccharomyces cerevisiae'      <- different organisms
    cas:84082-64-4   'Mucin from porcine stomach,Type II'
                     'Mucin from porcine stomach type III'       <- different products
    cas:39280-21-2   Rhamnogalacturonan from SOY / from POTATO   <- different sources
    FOODON:03315719  'Casein peptone' / 'Casamino acids'         <- peptone vs acid hydrolysate
    CHEBI:30769      'Citric acid' / 'Citric Acid*H2O'           <- anhydrous vs monohydrate

Those agree on chemistry because the same CAS was copied onto both records, or
because the hydrate's properties were filled in from the anhydrous form. The
chemistry test reproduces the very error it is being asked to detect. So the
selection here is by hand, and each row carries its reason.

The inverse test is sound and worth stating: where the formulas DIFFER the
records are certainly not mergeable, which is what protects the eight
hydrate/anhydrous families (`CuSO4` / `x 2 H2O` / `x 4 H2O`, `FeSO4` / `x 5 H2O`
/ `x 6 H2O`, ...). Those need re-grounding, not merging — an anhydrous salt and
its hydrate have different formula weights and are ordered separately.

## What a merge does here

The pair already shares an identifier, so unlike the usual tombstone merge
nothing is re-pointed. The loser is marked REJECTED with its occurrences
transferred, its label and its own synonyms fold into the winner, and its SSSOM
rows are dropped. The winner is whichever label has more occurrences — the
string media actually use.

    python scripts/merge_identifier_collisions.py            # dry-run
    python scripts/merge_identifier_collisions.py --apply
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))
import yaml  # noqa: E402

from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

MAPPED = REPO_ROOT / "data" / "curated" / "mapped_ingredients.yaml"
SSSOM = REPO_ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
DATE = "2026-08-20"
STAMP = f"{DATE}T00:00:00+00:00"
CURATOR = "merge_identifier_collisions"

# (identifier, winner, loser, why this pair is one substance)
#
# NOT here: MICRO:0000175 'Trypticase' / 'Trypticase peptone'. It reads like the
# same product, but mappings/duplicate_identifier_baseline.tsv dispositions it
# NEEDS_OWN_ID_MEMBER_UNDECIDED — a curator has already recorded that one member
# is more specific and should take its own id, and that WHICH member surrenders
# MICRO:0000175 is undecided. Merging would overwrite that decision with a
# guess. Every entry below is UNREVIEWED or HYDRATE_FAMILY_UNREVIEWED, i.e. no
# decision exists to contradict.
MERGES = [
    ("CHEBI:86158", "CaCl2 x 2 H2O", "CaCl22H2O",
     "the same string with the spacing removed — identical CAS 10035-04-8 and "
     "formula Ca.2Cl.2H2O, and no reading of 'CaCl22H2O' yields anything but "
     "calcium chloride dihydrate"),
    ("CHEBI:32954", "Na-acetate", "Sodium acetate",
     "abbreviation versus full name for one salt; identical CAS 127-09-3 and "
     "formula C2H3O2.Na"),
    ("CHEBI:32150", "Na2S2O3 x 5 H2O", "Sodium Thiosulfate Pentahydrate",
     "formula notation versus spelled-out name of the same pentahydrate; "
     "identical CAS 10102-17-7, and both state the hydration explicitly so "
     "neither can be the anhydrous form"),
    ("CHEBI:91248", "L-Cysteine HCl x H2O", "L-Cysteine hydrochloride monohydrate",
     "abbreviation versus full name; identical CAS 7048-04-6 and formula "
     "C3H7NO2S.H2O.HCl, both explicitly the monohydrate"),
    ("CHEBI:3312", "CaCl2", "Calcium Chloride",
     "formula versus name for the same anhydrous salt; identical CAS 10043-52-4 "
     "and formula Ca.2Cl. Neither label mentions hydration, so this is not the "
     "hydrate/anhydrous trap that rules out the CuSO4 and FeSO4 families"),
]

# Same substance, but the two records sit on DIFFERENT identifiers, so the loser
# is re-pointed at the winner's CURIE in the usual tombstone way. Kept separate
# from MERGES above because that list asserts nothing about grounding — these
# also correct one.
CROSS_MERGES = [
    ("MgCl2 x 6 H2O", "CHEBI:86345", "MgCl2x 6 H2O", "CHEBI:6636",
     "the identical label with one space missing, yet grounded to different "
     "terms: the 2,285-occurrence spelling sits on magnesium dichloride "
     "HEXAHYDRATE and the 7-occurrence spelling on the ANHYDROUS salt. The "
     "label says '6 H2O' either way, so the anhydrous grounding is simply "
     "wrong. Merging both fixes that grounding and clears CHEBI:6636's "
     "collision, leaving only 'MgCl2' on the anhydrous term where it belongs"),
]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    doc = yaml.safe_load(MAPPED.read_text(encoding="utf-8")) or {}
    recs = doc.get("ingredients", [])
    by_term = {str(r.get("preferred_term")): r for r in recs}

    done, skipped = [], []
    for ident, win_lab, lose_lab, why in MERGES:
        win, lose = by_term.get(win_lab), by_term.get(lose_lab)
        if win is None or lose is None:
            skipped.append((lose_lab, "record not found"))
            continue
        if lose.get("mapping_status") == "REJECTED":
            skipped.append((lose_lab, "already merged"))
            continue
        if str(win.get("identifier")) != ident or str(lose.get("identifier")) != ident:
            skipped.append((lose_lab, f"identifier moved off {ident}"))
            continue

        locc = lose.get("occurrence_statistics") or {}
        wocc = win.setdefault("occurrence_statistics", {})
        before = (wocc.get("total_occurrences") or 0, wocc.get("media_count") or 0)
        wocc["total_occurrences"] = before[0] + (locc.get("total_occurrences") or 0)
        wocc["media_count"] = before[1] + (locc.get("media_count") or 0)

        # The loser's label AND its own synonyms: this merge drops the loser's
        # SSSOM rows, so anything left behind stops reaching KGX even though
        # label_index still resolves it (label_index publishes REJECTED rows).
        syns = win.setdefault("synonyms", [])
        have = {str(s.get("synonym_text", "")).lower() for s in syns}
        for text, kind in ([(lose_lab, "RAW_TEXT")]
                           + [(str(s.get("synonym_text") or ""),
                               s.get("synonym_type") or "RAW_TEXT")
                              for s in (lose.get("synonyms") or [])]):
            if text and text.lower() not in have and text.lower() != win_lab.lower():
                syns.append({"synonym_text": text, "synonym_type": kind,
                             "source": f"MERGED_FROM {lose_lab} (#414)"})
                have.add(text.lower())

        note = (
            f"Absorbed {lose_lab!r} (#414). Both records held {ident} while both were "
            f"live, which MIM's own rule forbids — for a mapped record the identifier "
            f"IS the ontology CURIE, so two live records on it assert that two "
            f"ingredients are one thing. They are one thing: {why}. {win_lab!r} wins "
            f"as the label media actually use ({before[0]} occurrences against "
            f"{locc.get('total_occurrences', 0)}); the other survives as a RAW_TEXT "
            f"synonym, so label_index still answers for it.")
        win.setdefault("curation_history", []).append({
            "timestamp": STAMP, "curator": CURATOR, "action": "MERGED_FROM",
            "changes": note, "llm_assisted": False})

        lose["mapping_status"] = "REJECTED"
        lo = lose.setdefault("occurrence_statistics", {})
        lo["total_occurrences"] = 0
        lo["media_count"] = 0
        lose.setdefault("curation_history", []).append({
            "timestamp": STAMP, "curator": CURATOR, "action": "MERGED_INTO",
            "changes": (f"Merged into {win_lab!r} on {ident} (#414). {why}. "
                        f"Occurrences transferred; kept as a RAW_TEXT synonym there."),
            "llm_assisted": False})
        done.append((ident, win_lab, lose_lab, wocc["total_occurrences"]))

    for win_lab, win_id, lose_lab, lose_id, why in CROSS_MERGES:
        win, lose = by_term.get(win_lab), by_term.get(lose_lab)
        if win is None or lose is None or lose.get("mapping_status") == "REJECTED":
            skipped.append((lose_lab, "not found or already merged"))
            continue
        if str(win.get("identifier")) != win_id or str(lose.get("identifier")) != lose_id:
            skipped.append((lose_lab, "identifiers moved"))
            continue
        locc = lose.get("occurrence_statistics") or {}
        wocc = win.setdefault("occurrence_statistics", {})
        before = (wocc.get("total_occurrences") or 0, wocc.get("media_count") or 0)
        wocc["total_occurrences"] = before[0] + (locc.get("total_occurrences") or 0)
        wocc["media_count"] = before[1] + (locc.get("media_count") or 0)
        syns = win.setdefault("synonyms", [])
        have = {str(s.get("synonym_text", "")).lower() for s in syns}
        for text, kind in ([(lose_lab, "RAW_TEXT")]
                           + [(str(s.get("synonym_text") or ""),
                               s.get("synonym_type") or "RAW_TEXT")
                              for s in (lose.get("synonyms") or [])]):
            if text and text.lower() not in have and text.lower() != win_lab.lower():
                syns.append({"synonym_text": text, "synonym_type": kind,
                             "source": f"MERGED_FROM {lose_lab} (#414)"})
                have.add(text.lower())
        win.setdefault("curation_history", []).append({
            "timestamp": STAMP, "curator": CURATOR, "action": "MERGED_FROM",
            "changes": (f"Absorbed {lose_lab!r} from {lose_id} (#414). {why}."),
            "llm_assisted": False})
        # Tombstone takes the WINNER's identifier, per the merge convention.
        lose["identifier"] = win_id
        lose["mapping_status"] = "REJECTED"
        lo = lose.setdefault("occurrence_statistics", {})
        lo["total_occurrences"] = 0
        lo["media_count"] = 0
        lose.setdefault("curation_history", []).append({
            "timestamp": STAMP, "curator": CURATOR, "action": "MERGED_INTO",
            "changes": (f"Merged into {win_lab!r} on {win_id}, re-pointed from "
                        f"{lose_id} (#414). {why}."),
            "llm_assisted": False})
        done.append((f"{lose_id}->{win_id}", win_lab, lose_lab, wocc["total_occurrences"]))

    # MIM stores every record twice: the curated aggregate and a per-record file
    # under data/ingredients/mapped/. Earlier merge scripts wrote only the
    # aggregate and left the per-record copy to a later export — which is how
    # `generate_ingredient_umap.py`, which reads the PER-RECORD files, went on
    # drawing merged-away labels. Writing both here keeps the stores consistent
    # without invoking the export pairing that #148 found silently reverted 55
    # curation events.
    touched = {lab for _, w, l, _ in done for lab in (w, l)}
    per_record: dict[str, Path] = {}
    for candidate in (REPO_ROOT / "data" / "ingredients" / "mapped").glob("*.yaml"):
        try:
            doc_i = yaml.safe_load(candidate.read_text(encoding="utf-8"))
        except Exception:
            continue
        if isinstance(doc_i, dict):
            term = str(doc_i.get("preferred_term") or "")
            if term in touched:
                per_record[term] = candidate
    synced = []
    for term, path in sorted(per_record.items()):
        if args.apply:
            save_yaml(by_term[term], path)
        synced.append(term)

    losers = {lose for _, _, lose, _ in done}
    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    kept, dropped = [], 0
    for line in lines:
        cells = line.rstrip("\n").split("\t")
        if len(cells) >= 2 and cells[1] in losers:
            dropped += 1
            continue
        kept.append(line)

    if args.apply and done:
        recs_live = [r for r in recs]
        doc["total_count"] = len(recs_live)
        doc["mapped_count"] = sum(1 for r in recs_live
                                  if r.get("mapping_status") == "MAPPED")
        save_yaml(doc, MAPPED)
        SSSOM.write_text("".join(kept), encoding="utf-8")

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'}\n")
    for ident, win_lab, lose_lab, occ in done:
        print(f"  {ident:<16} {lose_lab!r} -> {win_lab!r}  (occ now {occ})")
    if skipped:
        print(f"\n  skipped: {skipped}")
    print(f"\n  per-record files synced: {len(synced)} {synced}")
    print(f"  SSSOM rows dropped for merged-away labels: {dropped}")
    print(f"  collisions cleared: {len(done)} of 30 (#414); the rest need "
          f"per-case judgement")
    return 0


if __name__ == "__main__":
    sys.exit(main())
