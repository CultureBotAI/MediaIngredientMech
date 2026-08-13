#!/usr/bin/env python3
"""Merge four CAS-conflict records that shadow a correctly-mapped sibling (#320).

#320 flags records whose `cas_rn` ChEBI registers against a *different* term than
the record's CURIE. Splitting those 84 by ChEBI ancestry shows 48 are not defects
at all — the CAS is simply finer-grained than a deliberately generic term
(`Arginine` -> `CHEBI:29016 arginine`, CAS `74-79-3` -> `L-arginine`), which §3
step 4 makes correct.

Of the genuine conflicts, these four resolve the same way, and it is the root
cause already identified in #315 and #334: **the CAS conflict is a symptom of a
duplicate record, not of a bad mapping.** In each case ChEBI has the right term,
the record's own CAS points straight at it, and *another MIM record already holds
it under the correct name*:

    m-Inositol               CHEBI:10642 scyllo-inositol -> CHEBI:17268, held by `myo-Inositol`
    NiSO4 x 6 H2O            CHEBI:53001 nickel sulfate  -> CHEBI:53437, held by `Nickel (II) sulfate hexahydrate`
    Sodium succinate dibasic CHEBI:15741 succinic acid   -> CHEBI:63675, held by `Sodium succinate`
    maltose                  CHEBI:18167 alpha-maltose   -> CHEBI:17306, held by `Maltose`

`m-Inositol` is the sharpest: "m-Inositol" is myo-inositol, and it was grounded to
*scyllo*-inositol — a different stereoisomer — by a `CAS_RN_LOOKUP` that its own
CAS `87-89-8` contradicts. `maltose` differs from `Maltose` only in case.

Because the target identifier is held, each is a merge, not a re-grounding. The
winners already carry the correct term, formula and grade, so nothing is
recomputed: occurrences transfer, the raw label is kept as a RAW_TEXT synonym,
and the loser is tombstoned with its SSSOM rows dropped.

**Deliberately not merged**, though both are ancestor-cases in the same triage:

* `Dextrose` -> `CHEBI:4167 D-glucopyranose`. Its CAS resolves to three terms
  (`glucose`, `D-glucose`, `aldehydo-D-glucose`), each already held by a
  different MIM record (`Glucose`, `D-Glucose`, `glucose`). That is a four-way
  tangle and picking one winner piecemeal would prejudge it; it needs coordinated
  treatment with the rest of the glucose family.
* `N-Acetyl-L-glutamine` -> `CHEBI:21553 N-acetyl-L-glutamine`. Here the record's
  own term matches its label *exactly* and the CAS's term
  (`N(2)-acetylglutamine`) is the stereo-unspecified ancestor, so §3 step 4 makes
  the current mapping correct and the CAS the looser field. Merging would lose
  the L- stereochemistry.

    python scripts/merge_cas_conflict_duplicates.py            # dry-run
    python scripts/merge_cas_conflict_duplicates.py --apply
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
CURATOR = "merge_cas_conflict_duplicates"
ISSUE = "#320"

# loser label -> (old CURIE, old label, winner id, winner label, why)
MERGE = {
    "m-Inositol": (
        "CHEBI:10642", "scyllo-inositol", "CHEBI:17268", "myo-Inositol",
        "'m-Inositol' is myo-inositol. The record was grounded to scyllo-inositol, a "
        "different stereoisomer, by a CAS_RN_LOOKUP that its own CAS 87-89-8 "
        "contradicts — ChEBI registers that CAS against CHEBI:17268 myo-inositol"),
    "NiSO4 x 6 H2O": (
        "CHEBI:53001", "nickel sulfate", "CHEBI:53437",
        "Nickel (II) sulfate hexahydrate",
        "the record's CAS 10101-97-0 is registered by ChEBI against CHEBI:53437 "
        "'nickel sulfate hexahydrate', the specific term §3 step 1 requires; the "
        "record sat on the generic sulfate and carried its anhydrous formula"),
    "Sodium succinate dibasic": (
        "CHEBI:15741", "succinic acid", "CHEBI:63675", "Sodium succinate",
        "the record is the disodium salt but was mapped to the free acid. Its CAS "
        "150-90-3 is registered against CHEBI:63675 'sodium succinate (anhydrous)', "
        "whose formula C4H4O4.2Na is the dibasic salt the label names"),
    "maltose": (
        "CHEBI:18167", "alpha-maltose", "CHEBI:17306", "Maltose",
        "differs from the winning record only in the case of its first letter, and "
        "was grounded to the alpha anomer while the winner holds the anomer-agnostic "
        "term its CAS 69-79-4 points at"),
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

    for label, (old_id, old_label, win_id, win_label, why) in MERGE.items():
        lose = find(recs, label=label)
        win = find(recs, ident=win_id, label=win_label, status="MAPPED")
        if lose is None or lose.get("mapping_status") == "REJECTED":
            out.append(f"{label}: not present or already tombstoned — skipped")
            continue
        if lose.get("identifier") != old_id:
            out.append(f"{label}: identifier is {lose.get('identifier')}, expected "
                       f"{old_id} — moved since this was verified; skipped")
            continue
        if win is None:
            out.append(f"{label}: winner {win_id} {win_label!r} not found — skipped")
            continue

        locc = lose.get("occurrence_statistics") or {}
        wocc = win.setdefault("occurrence_statistics", {})
        before = (wocc.get("total_occurrences") or 0, wocc.get("media_count") or 0)
        wocc["total_occurrences"] = before[0] + (locc.get("total_occurrences") or 0)
        wocc["media_count"] = before[1] + (locc.get("media_count") or 0)

        syns = win.setdefault("synonyms", [])
        if label.lower() not in {str(s.get("synonym_text", "")).lower() for s in syns}:
            syns.append({"synonym_text": label, "synonym_type": "RAW_TEXT",
                         "source": f"MERGED_FROM_{old_id}"})
        win.setdefault("curation_history", []).append({
            "timestamp": STAMP, "curator": CURATOR, "action": "MERGED_FROM",
            "changes": (
                f"Absorbed {label!r} ({ISSUE}), which sat on {old_id} ({old_label!r}). "
                f"Merged because {why}. The CAS-vs-CURIE conflict #320 flagged on that "
                f"record was a symptom of the duplicate, not of a bad mapping. "
                f"Occurrences {before[0]}/{before[1]} + {locc.get('total_occurrences', 0)}/"
                f"{locc.get('media_count', 0)} -> {wocc['total_occurrences']}/"
                f"{wocc['media_count']}. Raw label kept as a RAW_TEXT synonym."),
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
            "changes": (f"Merged into {win_id} {win_label!r}; occurrences transferred. "
                        f"Was on {old_id} ({old_label!r}); {why}. Tombstoned REJECTED, "
                        f"SSSOM rows dropped ({ISSUE})."),
            "llm_assisted": False,
        })
        drop.add(label)
        out.append(f"MERGE  {label:<26} {old_id} {old_label[:22]:<24} -> {win_id} "
                   f"{win_label} (occ -> {wocc['total_occurrences']})")

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
    print("\n  Not merged: Dextrose (four-way glucose tangle, needs coordinated "
          "treatment), N-Acetyl-L-glutamine (own term matches the label exactly; "
          "the CAS's term is the stereo-unspecified ancestor)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
