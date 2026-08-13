#!/usr/bin/env python3
"""Merge four hydrates that were minted a registry CURIE but are duplicates (#321).

`mint_hydrate_registry_terms` applied `MAPPING_SEMANTICS` §3 **step 3** — mint a
`kgmicrobe.compound:` identifier — on the stated grounds that ChEBI has no term
for the hydrate. For these four that premise was false: it was never checked.
ChEBI *does* have the specific term, **and another MIM record already holds it**:

    Na2-EDTA x 2 H2O          -> CHEBI:64758, held by `Na2EDTA·2H2O`
    Na2MoO4·2H2O              -> CHEBI:75213, held by `Na2MoO4 x 2 H2O`
    Sodium acetate·3H2O       -> CHEBI:32138, held by `Sodium acetate trihydrate`
    Trisodium citrate x 2 H2O -> CHEBI:32142, held by `Na3-citrate x 2 H2O`

So step 1 applied, not step 3, and these are **merges** rather than promotions —
the target identifier is taken. Minting would have been the worst outcome
available: it gives a duplicate its own permanent identity, cementing the split
that the shared identifier at least made visible to
`audit_duplicate_identifiers`.

This is the `Ca-pantothenate` shape from #315 once more. Every pair differs only
in notation the merge pass does not recognise as the same substance — `·` versus
` x `, `Na2-EDTA` versus `Na2EDTA`, `Trisodium citrate` versus `Na3-citrate` —
so the duplicate escaped dedup and was then grounded to the nearest thing lexical
matching could reach: the anhydrous parent.

The winner already carries the specific hydrate term, the correct formula
(`2H2O.MoO4.2Na`) and an EXACT_MATCH/SYNONYM_MATCH grade, so nothing is
recomputed here — occurrences transfer, the raw label is kept as a synonym, and
the loser is tombstoned with its SSSOM rows (including the minted registry row)
dropped.

Found by the adversarial review of #341, before merge.

    python scripts/merge_minted_hydrate_duplicates.py            # dry-run
    python scripts/merge_minted_hydrate_duplicates.py --apply
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
STAMP = "2026-08-13T00:00:00+00:00"
CURATOR = "merge_minted_hydrate_duplicates"
ISSUE = "#321"

# loser label -> (winner identifier, winner label, how the term was found)
MERGE = {
    "Na2-EDTA x 2 H2O": (
        "CHEBI:64758", "Na2EDTA·2H2O",
        "ChEBI label search for the dihydrate of the minted-off parent"),
    "Na2MoO4·2H2O": (
        "CHEBI:75213", "Na2MoO4 x 2 H2O",
        "the record's own CAS 10102-40-6 is registered by ChEBI against "
        "CHEBI:75213 'sodium molybdate dihydrate'"),
    "Sodium acetate·3H2O": (
        "CHEBI:32138", "Sodium acetate trihydrate",
        "ChEBI label search for the trihydrate of the minted-off parent"),
    "Trisodium citrate x 2 H2O": (
        "CHEBI:32142", "Na3-citrate x 2 H2O",
        "the record's own CAS 6132-04-3 is registered by ChEBI against "
        "CHEBI:32142 'sodium citrate dihydrate'"),
}


def find(recs, label=None, ident=None, status=None):
    for r in recs:
        if label is not None and r.get("preferred_term") != label:
            continue
        if ident is not None and r.get("identifier") != ident:
            continue
        if status is not None and r.get("mapping_status") != status:
            continue
        return r
    return None


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    coll = yaml.safe_load(COLLECTION.read_text(encoding="utf-8", errors="replace")) or {}
    recs = coll.get("ingredients", [])
    out: list[str] = []
    drop: set[str] = set()

    for label, (win_id, win_label, how) in MERGE.items():
        lose = find(recs, label=label)
        win = find(recs, ident=win_id, label=win_label, status="MAPPED")
        if lose is None or lose.get("mapping_status") == "REJECTED":
            out.append(f"{label}: not present or already tombstoned — skipped")
            continue
        if win is None:
            out.append(f"{label}: winner {win_id} {win_label!r} not found — skipped")
            continue

        minted = lose.get("identifier")
        locc = lose.get("occurrence_statistics") or {}
        wocc = win.setdefault("occurrence_statistics", {})
        before = (wocc.get("total_occurrences") or 0, wocc.get("media_count") or 0)
        wocc["total_occurrences"] = before[0] + (locc.get("total_occurrences") or 0)
        wocc["media_count"] = before[1] + (locc.get("media_count") or 0)

        syns = win.setdefault("synonyms", [])
        if label.lower() not in {str(s.get("synonym_text", "")).lower() for s in syns}:
            syns.append({"synonym_text": label, "synonym_type": "RAW_TEXT",
                         "source": f"MERGED_FROM_{minted}"})
        win.setdefault("curation_history", []).append({
            "timestamp": STAMP, "curator": CURATOR, "action": "MERGED_FROM",
            "changes": (
                f"Absorbed {label!r} ({ISSUE}), which differs from this record only in "
                f"notation the merge pass does not recognise as the same substance, so it "
                f"escaped dedup and was grounded to the anhydrous parent. It had just been "
                f"minted {minted!r} on the false premise that ChEBI has no term for this "
                f"hydrate — {how}. Occurrences {before[0]}/{before[1]} + "
                f"{locc.get('total_occurrences', 0)}/{locc.get('media_count', 0)} -> "
                f"{wocc['total_occurrences']}/{wocc['media_count']}. Raw label kept as a "
                f"RAW_TEXT synonym."),
            "llm_assisted": False,
        })

        lose["identifier"] = win_id
        lose["mapping_status"] = "REJECTED"
        lo = lose.setdefault("occurrence_statistics", {})
        lo["total_occurrences"] = 0
        lo["media_count"] = 0
        lo.pop("source_occurrences", None)
        lose.setdefault("curation_history", []).append({
            "timestamp": STAMP, "curator": CURATOR, "action": "MERGED_INTO",
            "changes": (
                f"Merged into {win_id} {win_label!r}; occurrences transferred. The "
                f"{minted!r} minted for this record is withdrawn: §3 step 3 requires that "
                f"no specific term exists, and one does ({how}), so step 1 applied and the "
                f"target identifier was already held. Tombstoned REJECTED, SSSOM rows "
                f"dropped ({ISSUE})."),
            "llm_assisted": False,
        })
        drop.add(label)
        out.append(f"MERGE  {label:<28} {minted[:34]:<36} -> {win_id} {win_label} "
                   f"(occ -> {wocc['total_occurrences']})")

    # Drops BOTH rows for the loser: the CHEBI narrowMatch and the minted registry row.
    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    kept, rows = [], 0
    for line in lines:
        cells = line.rstrip("\n").split("\t")
        if len(cells) >= 5 and cells[1] in drop:
            rows += 1
            continue
        kept.append(line)

    if args.apply and out:
        save_yaml(coll, COLLECTION)
        SSSOM.write_text("".join(kept), encoding="utf-8")

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'} — "
          f"{len(drop)} merge(s), {rows} SSSOM row(s) dropped\n")
    for o in out:
        print(f"  {o}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
