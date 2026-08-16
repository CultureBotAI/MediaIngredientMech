#!/usr/bin/env python3
"""Put hydrate records on the specific ChEBI hydrate term (#374, #334, #321).

Seven records name a hydrate while sitting on an anhydrous or generic ChEBI term,
and ChEBI **has** the specific hydrate — so `MAPPING_SEMANTICS` §3 **step 1**
applies and nothing needs minting. Found by cross-checking against
CultureBotAI/CultureMech#272, which regrounds the same labels and is right where
MIM is wrong.

Four of the seven turn out not to be regroundings at all. Each has a **correct
twin already on the right term**, and the two differ only in notation the merge
pass does not recognise — the #334 shadowing pattern:

    FeSO4 x 7 H2O   CHEBI:75836 heptahydrate  occ 2295  <- FeSO4 x 7H2O    (anhydrous, occ 1)
    MgSO4 x 7 H2O   CHEBI:31795 heptahydrate  occ 3618  <- MgSO4·7H2O      (generic,   occ 431)
    MnSO4 x H2O     CHEBI:86364 monohydrate   occ  946  <- MnSO4 x 1 H2O   (generic,   occ 6)
    Na2SeO3 x 5 H2O CHEBI:131361 pentahydrate occ 1413  <- Na2SeO3·5H2O    (anhydrous, occ 45)

`·` versus ` x `, `7H2O` versus `7 H2O`, `1 H2O` versus `H2O`. So they are merges,
and the shadowed twin's occurrences transfer rather than being regrounded in
place. `MgSO47H2O` is the same shape on the *correct* term already, so it merges
too — a duplicate identifier rather than a wrong one.

The other three have no twin and are straight promotions.

**#342 is not in tension with this.** That decision made hydrate→anhydrous a
`closeMatch` for hydrates ChEBI cannot name. These can be named, so they move to
the specific term at EXACT_MATCH and leave the closeMatch question behind.

**Left alone, and filed rather than guessed:** `MgSO4·H2O` sits on CHEBI:31795
*heptahydrate* while its label says one water — a term/label mismatch in the
opposite direction, not a shadowing case. `MgSO4 x 6 H2O`, `MnSO4 x 7 H2O`,
`FeSO4 x 5 H2O` and `FeSO4 x 6 H2O` sit on generic terms and ChEBI has no term
for those hydration states.

    python scripts/fix_hydrate_terms_and_twins.py            # dry-run
    python scripts/fix_hydrate_terms_and_twins.py --apply
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
UNMAPPED = ROOT / "data" / "curated" / "unmapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
STAMP = "2026-08-15T00:00:00+00:00"
CURATOR = "fix_hydrate_terms_and_twins"
ISSUE = "#374/#334"

# loser -> (winner label, shared term, what differs)
MERGE = {
    "FeSO4 x 7H2O": ("FeSO4 x 7 H2O", "CHEBI:75836",
                     "a missing space before H2O"),
    "MgSO4·7H2O": ("MgSO4 x 7 H2O", "CHEBI:31795",
                   "`·` where the twin uses ` x `"),
    "MgSO47H2O": ("MgSO4 x 7 H2O", "CHEBI:31795",
                  "no separator at all; already on the correct term, so this is a "
                  "duplicate identifier rather than a wrong one"),
    "MnSO4 x 1 H2O": ("MnSO4 x H2O", "CHEBI:86364",
                      "an explicit `1` where the twin omits it"),
    "Na2SeO3·5H2O": ("Na2SeO3 x 5 H2O", "CHEBI:131361",
                     "`·` where the twin uses ` x `"),
}
# label -> (old term, new term, new label)
PROMOTE = {
    "Chromium(III) Chloride Hexahydrate": (
        "CHEBI:53351", "CHEBI:53442", "chromium(3+) trichloride hexahydrate"),
    "CoSO4 x 7 H2O": ("CHEBI:53470", "CHEBI:91244", "cobalt(2+) sulfate heptahydrate"),
    "NiSO4 x 7 H2O": ("CHEBI:53001", "CHEBI:53504", "nickel sulfate heptahydrate"),
}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    colls = {p: (yaml.safe_load(p.read_text(encoding="utf-8", errors="replace")) or {})
             for p in (MAPPED, UNMAPPED)}
    index: dict[str, dict] = {}
    for coll in colls.values():
        for rec in coll.get("ingredients", []) or []:
            if rec.get("mapping_status") != "REJECTED":
                index.setdefault(str(rec.get("preferred_term") or ""), rec)

    out, drop, sssom_edits, skipped = [], set(), {}, []

    for loser_label, (winner_label, term, differs) in MERGE.items():
        lose, win = index.get(loser_label), index.get(winner_label)
        if lose is None or win is None:
            skipped.append(f"{loser_label}: record or twin {winner_label!r} not found")
            continue
        if str((win.get("ontology_mapping") or {}).get("ontology_id")) != term:
            skipped.append(f"{loser_label}: twin is not on {term}")
            continue
        locc = lose.get("occurrence_statistics") or {}
        wocc = win.setdefault("occurrence_statistics", {})
        before = (wocc.get("total_occurrences") or 0, wocc.get("media_count") or 0)
        wocc["total_occurrences"] = before[0] + (locc.get("total_occurrences") or 0)
        wocc["media_count"] = before[1] + (locc.get("media_count") or 0)
        why = (
            f"{loser_label!r} and {winner_label!r} are the same substance written two "
            f"ways — {differs} — so the pair escaped dedup, and the loser was then "
            f"grounded to the nearest term lexical matching could reach: "
            f"{(lose.get('ontology_mapping') or {}).get('ontology_id')} "
            f"({(lose.get('ontology_mapping') or {}).get('ontology_label')!r}), which "
            f"does not carry the water its own label states. The #334 shadowing "
            f"pattern. Found by cross-checking CultureBotAI/CultureMech#272, which "
            f"grounds these labels correctly.")
        syns = win.setdefault("synonyms", [])
        if loser_label.lower() not in {str(s.get("synonym_text", "")).lower() for s in syns}:
            syns.append({"synonym_text": loser_label, "synonym_type": "RAW_TEXT",
                         "source": f"MERGED_FROM ({ISSUE})"})
        win.setdefault("curation_history", []).append({
            "timestamp": STAMP, "curator": CURATOR, "action": "MERGED_FROM",
            "changes": (f"Absorbed {loser_label!r} ({ISSUE}). {why} Occurrences "
                        f"{before[0]}/{before[1]} + {locc.get('total_occurrences', 0)}/"
                        f"{locc.get('media_count', 0)} -> {wocc['total_occurrences']}/"
                        f"{wocc['media_count']}."),
            "llm_assisted": False})
        lose["identifier"] = term
        lose["mapping_status"] = "REJECTED"
        lo = lose.setdefault("occurrence_statistics", {})
        lo["total_occurrences"] = 0
        lo["media_count"] = 0
        lo.pop("source_occurrences", None)
        lose.setdefault("curation_history", []).append({
            "timestamp": STAMP, "curator": CURATOR, "action": "MERGED_INTO",
            "changes": (f"Merged into {term} {winner_label!r}; occurrences transferred. "
                        f"{why} Tombstoned REJECTED, SSSOM rows dropped."),
            "llm_assisted": False})
        drop.add(loser_label)
        out.append(f"MERGE    {loser_label[:24]:<26} -> {winner_label[:22]:<24} {term} "
                   f"(occ -> {wocc['total_occurrences']})")

    for label, (old, new, new_label) in PROMOTE.items():
        rec = index.get(label)
        if rec is None:
            skipped.append(f"{label}: not found")
            continue
        om = rec.get("ontology_mapping") or {}
        if str(om.get("ontology_id")) != old:
            skipped.append(f"{label}: on {om.get('ontology_id')}, expected {old}")
            continue
        old_label = om.get("ontology_label")
        rec["identifier"] = new
        om.update({"ontology_id": new, "ontology_label": new_label,
                   "ontology_source": "CHEBI", "mapping_quality": "EXACT_MATCH"})
        note = (
            f"Promoted from {old} ({old_label!r}) to the specific hydrate term {new} "
            f"({new_label!r}) — MAPPING_SEMANTICS §3 step 1: the label names a hydrate, "
            f"ChEBI has the term, so nothing needs minting and no closeMatch question "
            f"arises. The previous term carried no water while the label states it. "
            f"Found by cross-checking CultureBotAI/CultureMech#272 ({ISSUE}).")
        om.setdefault("evidence", []).append({
            "evidence_type": "DATABASE_MATCH",
            "source": f"MIM curation ({ISSUE})", "notes": note})
        rec.setdefault("curation_history", []).append({
            "timestamp": STAMP, "curator": CURATOR, "action": "PROMOTED_TO_SPECIFIC_HYDRATE",
            "changes": f"identifier/ontology_id {old} -> {new}; {note}",
            "llm_assisted": False})
        sssom_edits[label] = (new, new_label)
        out.append(f"PROMOTE  {label[:24]:<26} -> {new} {new_label[:30]}")

    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    kept, rows = [], 0
    for line in lines:
        cells = line.rstrip("\n").split("\t")
        if len(cells) >= 5 and cells[1] in drop:
            rows += 1
            continue
        if len(cells) >= 5 and cells[1] in sssom_edits and cells[3].startswith("CHEBI:"):
            cells[3], cells[4] = sssom_edits[cells[1]]
            line = "\t".join(cells) + "\n"
            rows += 1
        kept.append(line)

    if args.apply and out:
        for path, coll in colls.items():
            recs = coll.get("ingredients") or []
            coll["mapped_count"] = sum(1 for r in recs if r.get("mapping_status") == "MAPPED")
            save_yaml(coll, path)
        SSSOM.write_text("".join(kept), encoding="utf-8")

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'} — "
          f"{len(out)} action(s), {rows} SSSOM row(s)\n")
    for o in out:
        print(f"  {o}")
    for s in skipped:
        print(f"  SKIPPED {s}")
    print("\n  Left alone: MgSO4·H2O (monohydrate label on the HEPTAhydrate term — a "
          "mismatch\n  in the other direction), and MgSO4 x 6 H2O / MnSO4 x 7 H2O / "
          "FeSO4 x 5,6 H2O\n  (ChEBI has no term for those hydration states).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
