#!/usr/bin/env python3
"""Merge abbreviated-counterion duplicates into their correct salt records (#315).

Three records name a salt with an abbreviated counterion prefix, were grounded to
the bare **anion** instead, and duplicate a live record that already holds the
correct salt term:

    Ca-pantothenate  CHEBI:29032 (R)-pantothenate   -> CHEBI:31345 Calcium pantothenate
    Na-glutamate     CHEBI:29988 L-glutamate(2-)    -> CHEBI:64243 Sodium L-glutamate
    Na-tartrate      CHEBI:30924 L-tartrate(2-)     -> CHEBI:63017 Sodium tartrate

Root cause is shared with the duplicate-detection gap: `Ca-` does not lexically
resemble `Calcium …`, so the merge pass missed it, and lexical matching then
grounded the survivor to the nearest thing it could find — the anion.

Follows the existing precedent exactly (`Calcium D-Pantothenate`, merged by
`merge-same-substance-batch`): the loser keeps the **winner's** identifier, is
tombstoned `REJECTED` with a `MERGED_INTO` event, and its SSSOM rows are dropped.

**Synonyms are transferred selectively, and that is the point.** Each loser
carries `EXACT_SYNONYM`s sourced `kg_microbe` / `chebi_synonym_review` that were
enriched from the *anion* term it was wrongly mapped to — `L-tartrate`,
`(2R,3R)-tartrate`, `L-glutamic acid dianion`,
`3-[(2R)-2,4-dihydroxy-3,3-dimethylbutanamido]propanoate`. Copying those onto a
*salt* record would assert that sodium tartrate is also called "L-tartrate",
which is false, and would propagate the very error being fixed. Only the raw
label — the string a medium actually used, and what makes the merge lossless for
anyone resolving raw text — is carried over.

    python scripts/merge_salt_label_duplicates.py            # dry-run
    python scripts/merge_salt_label_duplicates.py --apply
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
CURATOR = "merge_salt_label_duplicates"
ISSUE = "#315"

# loser preferred_term -> (loser id, winner id, winner preferred_term)
MERGES = [
    ("Ca-pantothenate", "CHEBI:29032", "CHEBI:31345", "Calcium pantothenate"),
    ("Na-glutamate", "CHEBI:29988", "CHEBI:64243", "Sodium L-glutamate"),
    ("Na-tartrate", "CHEBI:30924", "CHEBI:63017", "Sodium tartrate"),
]
# Synonym sources that were enriched from the loser's (wrong) anion term.
DERIVED = ("kg_microbe", "chebi", "ols")


def zero_occurrences(lose: dict) -> None:
    """A tombstone must carry zero occurrences once they are transferred.

    Leaving them on both records double-counts the ingredient — the winner now
    includes them and the loser still claims them. `tests/test_occurrence_stats`
    enforces this as `rejected_nonzero`, and the existing `Calcium
    D-Pantothenate` tombstone is 0/0 for the same reason.
    """
    occ = lose.setdefault("occurrence_statistics", {})
    occ["total_occurrences"] = 0
    occ["media_count"] = 0
    occ.pop("source_occurrences", None)


def find(recs, ident, label=None, status=None):
    for r in recs:
        if r.get("identifier") != ident:
            continue
        if label is not None and r.get("preferred_term") != label:
            continue
        if status is not None and r.get("mapping_status") != status:
            continue
        return r
    return None


def merge_occurrences(win: dict, lose: dict) -> str:
    w = win.setdefault("occurrence_statistics", {})
    lo = lose.get("occurrence_statistics") or {}
    before = (w.get("total_occurrences", 0), w.get("media_count", 0))
    w["total_occurrences"] = (w.get("total_occurrences") or 0) + (lo.get("total_occurrences") or 0)
    # media_count is summed, which slightly over-counts if a single medium listed
    # BOTH spellings. Unmeasurable from here and the same assumption the previous
    # merge batch made; flagged rather than silently exact.
    w["media_count"] = (w.get("media_count") or 0) + (lo.get("media_count") or 0)
    by = {(s.get("source"), s.get("source_columns")): dict(s)
          for s in (w.get("source_occurrences") or [])}
    for s in lo.get("source_occurrences") or []:
        k = (s.get("source"), s.get("source_columns"))
        if k in by:
            by[k]["count"] = (by[k].get("count") or 0) + (s.get("count") or 0)
        else:
            by[k] = dict(s)
    if by:
        w["source_occurrences"] = list(by.values())
    return (f"occurrences {before[0]}/{before[1]} + {lo.get('total_occurrences', 0)}/"
            f"{lo.get('media_count', 0)} -> {w['total_occurrences']}/{w['media_count']}")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    coll = yaml.safe_load(COLLECTION.read_text(encoding="utf-8", errors="replace")) or {}
    recs = coll.get("ingredients", [])
    out: list[str] = []
    drop_subjects: list[str] = []

    for lose_label, lose_id, win_id, win_label in MERGES:
        lose = find(recs, lose_id, label=lose_label)
        win = find(recs, win_id, label=win_label, status="MAPPED")
        if lose is None:
            # Already merged. Zeroing the tombstone was added after the first
            # run, so repair any tombstone still carrying transferred counts.
            done = find(recs, win_id, label=lose_label, status="REJECTED")
            if done and (done.get("occurrence_statistics") or {}).get("total_occurrences"):
                n = done["occurrence_statistics"]["total_occurrences"]
                zero_occurrences(done)
                out.append(f"{lose_label}: already merged; zeroed tombstone occurrences ({n} -> 0)")
            else:
                out.append(f"{lose_label}: no record on {lose_id} — already merged")
            continue
        if win is None:
            out.append(f"{lose_label}: winner {win_id} {win_label!r} not found — SKIPPED")
            continue

        occ = merge_occurrences(win, lose)

        syns = win.setdefault("synonyms", [])
        have = {str(s.get("synonym_text", "")).strip().lower() for s in syns}
        added = []
        if lose_label.lower() not in have:
            syns.append({"synonym_text": lose_label, "synonym_type": "RAW_TEXT",
                         "source": f"MERGED_FROM_{lose_id}"})
            added.append(lose_label)
        dropped = [str(s.get("synonym_text"))
                   for s in (lose.get("synonyms") or [])
                   if any(d in str(s.get("source") or "").lower() for d in DERIVED)]

        win.setdefault("curation_history", []).append({
            "timestamp": STAMP, "curator": CURATOR, "action": "MERGED_FROM",
            "changes": (
                f"Absorbed {lose_id} {lose_label!r} ({ISSUE}). Same substance under an "
                f"abbreviated-counterion name; the loser was grounded to the bare anion. "
                f"{occ}. Raw label kept as a RAW_TEXT synonym. "
                f"{len(dropped)} anion-derived synonym(s) deliberately NOT transferred "
                f"(enriched from the loser's wrong term; they name the anion, not this salt): "
                f"{', '.join(dropped[:4])}{'…' if len(dropped) > 4 else ''}"),
            "llm_assisted": False,
        })

        lose["identifier"] = win_id
        lose["mapping_status"] = "REJECTED"
        zero_occurrences(lose)
        lose.setdefault("curation_history", []).append({
            "timestamp": STAMP, "curator": CURATOR, "action": "MERGED_INTO",
            "changes": (f"Merged into {win_id} {win_label!r}; occurrences transferred. "
                        f"Tombstoned REJECTED, SSSOM rows dropped. Same substance under two "
                        f"names — the abbreviated `{lose_label.split('-')[0]}-` prefix is why "
                        f"the earlier merge pass missed it ({ISSUE})."),
            "llm_assisted": False,
        })
        drop_subjects.append(f"MIM:{lose_label.replace(' ', '_')}")
        out.append(f"{lose_label} ({lose_id}) -> {win_id} {win_label}\n"
                   f"        {occ}\n"
                   f"        synonyms added: {added or 'none'}\n"
                   f"        anion synonyms NOT transferred: {len(dropped)}")

    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    kept = [ln for ln in lines if ln.split("\t", 1)[0] not in set(drop_subjects)]
    removed = len(lines) - len(kept)

    if args.apply:
        save_yaml(coll, COLLECTION)
        SSSOM.write_text("".join(kept), encoding="utf-8")

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'}\n")
    for o in out:
        print(f"  {o}")
    print(f"\n  SSSOM rows dropped: {removed} ({', '.join(drop_subjects)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
