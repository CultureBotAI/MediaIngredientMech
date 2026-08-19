#!/usr/bin/env python3
"""Merge the `aldehydo-` duplicate pairs onto the class term (#398).

Two substances each have two records, split across a ChEBI class term and its
open-chain `aldehydo-` form:

    N-acetylmuramic acid   CHEBI:47965  N-acetylmuramic acid           occ  1
    n-Acetyl-muramic acid  CHEBI:47966  aldehydo-N-acetylmuramic acid  occ 10

    D-lyxose               CHEBI:62318  D-lyxose                       occ  0
    D-(-)-lyxose           CHEBI:16789  aldehydo-D-lyxose              occ  0

The muramic pair carry the SAME CAS and formula on both records, so they are one
substance recorded twice.

## Why the class term wins, when the CAS says otherwise

ChEBI hangs the **commercial** CAS on the open-chain form in both cases:

    CHEBI:47965  N-acetylmuramic acid           cas 1856-93-5
    CHEBI:47966  aldehydo-N-acetylmuramic acid  cas 10597-89-4   <- what you buy
    CHEBI:62318  D-lyxose                       (no cas)
    CHEBI:16789  aldehydo-D-lyxose              cas 1114-34-7    <- what you buy

So by CAS alone the `aldehydo-` groundings are defensible, and an earlier reading
of the orderability rule pointed at them. That was the wrong conclusion, for a
reason the rule now states: **the identifier optimises for how the node reads in
the knowledge graph.** No catalogue sells "aldehydo-N-acetylmuramic acid"; the
`aldehydo-` prefix is a tautomer designation, and in solution the open-chain form
is a minor component of an equilibrium. Naming a growth-medium ingredient after
it — and, since MIM is the naming authority, renaming the ChEBI node to match —
describes the substance worse than the class term does.

Nothing about orderability is lost, because it no longer has to ride on the
identity: the purchasable CAS goes in `supplied_form`, and
`publish_cas_as_synonym.py` republishes it as a synonym on the node.

## The merge

Standard tombstone: the loser takes the winner's identifier, is REJECTED, its
occurrences transfer, and its raw label is kept as a RAW_TEXT synonym so the
string still resolves. SSSOM rows for the loser are dropped.

    python scripts/merge_aldehydo_duplicates.py            # dry-run
    python scripts/merge_aldehydo_duplicates.py --apply
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
CURATOR = "merge_aldehydo_duplicates"

# winner label -> (winner term, loser label, loser term, supplied CAS, supplied name)
PAIRS = [
    ("N-acetylmuramic acid", "CHEBI:47965",
     "n-Acetyl-muramic acid", "CHEBI:47966",
     "10597-89-4", "N-Acetylmuramic acid"),
    ("D-lyxose", "CHEBI:62318",
     "D-(-)-lyxose", "CHEBI:16789",
     "1114-34-7", "D-(-)-Lyxose"),
]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    coll = yaml.safe_load(MAPPED.read_text(encoding="utf-8")) or {}
    recs = coll.get("ingredients") or []
    by_label = {}
    for r in recs:
        by_label.setdefault(str(r.get("preferred_term")), r)

    done, skipped, drop_labels = [], [], set()

    for win_lab, win_term, lose_lab, lose_term, cas, prod in PAIRS:
        win, lose = by_label.get(win_lab), by_label.get(lose_lab)
        if win is None or lose is None:
            skipped.append(f"{lose_lab}: record or winner missing")
            continue
        if str(win.get("identifier")) != win_term or str(lose.get("identifier")) != lose_term:
            skipped.append(f"{lose_lab}: identifiers moved "
                           f"({win.get('identifier')} / {lose.get('identifier')})")
            continue

        why = (
            f"Absorbed {lose_lab!r} ({lose_term} {'aldehydo- form'}) into {win_term} "
            f"(#398). Both records name the same substance — the muramic pair carry "
            f"an identical CAS and formula — split across a ChEBI class term and its "
            f"open-chain aldehydo- form. The class term wins because the identifier "
            f"optimises for how the node READS in the knowledge graph: no catalogue "
            f"sells an 'aldehydo-' tautomer, and MIM is kg-microbe's naming authority, "
            f"so grounding here would rename the ChEBI node after a minor solution-"
            f"equilibrium component. ChEBI does hang the commercial CAS ({cas}) on the "
            f"aldehydo- term, which is why the earlier reading of the orderability rule "
            f"pointed the other way; that CAS is now carried in supplied_form and "
            f"republished as a synonym, so nothing purchasable is lost from the identity.")

        locc = lose.get("occurrence_statistics") or {}
        wocc = win.setdefault("occurrence_statistics", {})
        before = (wocc.get("total_occurrences") or 0, wocc.get("media_count") or 0)
        wocc["total_occurrences"] = before[0] + (locc.get("total_occurrences") or 0)
        wocc["media_count"] = before[1] + (locc.get("media_count") or 0)

        # The loser's LABEL *and* its own synonyms. Keeping only the label was a
        # review finding: the tombstone's SSSOM row is dropped by this merge, so
        # anything left on it stops reaching KGX even though label_index still
        # resolves it (label_index publishes REJECTED rows). The losers here
        # carry real chemical names — `D-Lyx`, `D-lyxo-pentose`, the systematic
        # forms — not notation noise.
        syns = win.setdefault("synonyms", [])
        have = {str(s.get("synonym_text", "")).lower() for s in syns}
        for text, kind in ([(lose_lab, "RAW_TEXT")]
                           + [(str(s.get("synonym_text") or ""),
                               s.get("synonym_type") or "RAW_TEXT")
                              for s in (lose.get("synonyms") or [])]):
            if text and text.lower() not in have and text.lower() != win_lab.lower():
                syns.append({"synonym_text": text, "synonym_type": kind,
                             "source": f"MERGED_FROM {lose_lab} (#398)"})
                have.add(text.lower())

        # The purchasable form, kept OUT of the identity (#402's supplied_form).
        win.setdefault("supplied_form", []).append({
            "name": prod, "cas_rn": cas,
            "notes": (f"The CAS ChEBI attaches to {lose_term}, the open-chain form. It is "
                      f"what a lab orders; the record is grounded at the class term so the "
                      f"graph node reads sensibly, and publish_cas_as_synonym.py "
                      f"republishes this CAS as a synonym on that node."),
        })

        win.setdefault("curation_history", []).append({
            "timestamp": STAMP, "curator": CURATOR, "action": "MERGED_FROM",
            "changes": (f"{why} Occurrences {before[0]}/{before[1]} + "
                        f"{locc.get('total_occurrences', 0)}/{locc.get('media_count', 0)} "
                        f"-> {wocc['total_occurrences']}/{wocc['media_count']}."),
            "llm_assisted": False})

        lose["identifier"] = win_term
        lose["mapping_status"] = "REJECTED"
        lo = lose.setdefault("occurrence_statistics", {})
        lo["total_occurrences"] = 0
        lo["media_count"] = 0
        lose.setdefault("curation_history", []).append({
            "timestamp": STAMP, "curator": CURATOR, "action": "MERGED_INTO",
            "changes": (f"Merged into {win_term} {win_lab!r}; occurrences transferred. "
                        f"{why} Tombstoned REJECTED so a lookup on this label still "
                        f"resolves, SSSOM rows dropped."),
            "llm_assisted": False})
        drop_labels.add(lose_lab)
        done.append(f"{lose_lab[:26]:<28} -> {win_lab[:24]:<26} {win_term} "
                    f"(occ -> {wocc['total_occurrences']}, supplied CAS {cas})")

    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    kept, dropped = [], 0
    for line in lines:
        cells = line.rstrip("\n").split("\t")
        if len(cells) >= 2 and cells[1] in drop_labels:
            dropped += 1
            continue
        kept.append(line)

    if args.apply and done:
        coll["mapped_count"] = sum(1 for r in recs if r.get("mapping_status") == "MAPPED")
        save_yaml(coll, MAPPED)
        SSSOM.write_text("".join(kept), encoding="utf-8")

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'} — "
          f"{len(done)} merge(s), {dropped} SSSOM row(s) dropped\n")
    for d in done:
        print(f"  {d}")
    for s in skipped:
        print(f"  SKIPPED {s}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
