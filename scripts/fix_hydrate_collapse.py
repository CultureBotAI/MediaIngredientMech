#!/usr/bin/env python3
"""Break up the worst hydrate collapses (#321, #334).

Four ChEBI terms absorb 13 hydrate records — `CHEBI:34683` alone carries five
distinct `Na2HPO4` hydrates, so a recipe calling for the dodecahydrate and one
calling for the dihydrate become the same node, at 358 vs 178 g/mol.
`MAPPING_SEMANTICS` §3 is explicit that this is a defect and that step 1 applies
wherever a specific term exists.

ChEBI has a specific term for exactly 4 of the 13, and they need **two different
remedies** — which is the point of doing them together:

*Promotion* (target identifier free):
    Na2HPO4 x 2 H2O   -> CHEBI:91258 disodium hydrogenphosphate dihydrate
    Na2HPO4 x 12 H2O  -> CHEBI:91259 disodium hydrogenphosphate dodecahydrate

*Merge* (target identifier already held by a correctly-mapped sibling):
    CoCl2 x 6 H2O     -> CHEBI:53503, held by `Cobalt chloride hexahydrate` (occ 123)
    NiCl2 x 6 H2O     -> CHEBI:53542, held by `Nickel (II) chloride hexahydrate` (occ 122)

The merges are the `Ca-pantothenate` shape from #315: a notation the merge pass
does not recognise as the same substance (`CoCl2 x 6 H2O` vs `Cobalt chloride
hexahydrate`), which then got grounded to the nearest thing lexical matching
could find — the anhydrous parent. A promotion would have failed outright, since
the target identifier is taken.

**CAS is corrected from ChEBI's own xref on the promotions**, because the recorded
values are scrambled across each family (#334): every cobalt record carries the
anhydrous CAS; `NiCl2 x 2 H2O` and `x 5 H2O` both carry the *hexahydrate's*.
ChEBI's xref on the specific term is independent of the mapping being replaced.

The other 9 collapsed records have no ChEBI term and no trustworthy CAS, so they
need a verified CAS (§3 step 2) or a minted term (step 3), per record. Not
attempted blind.

    python scripts/fix_hydrate_collapse.py            # dry-run
    python scripts/fix_hydrate_collapse.py --apply
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
CURATOR = "fix_hydrate_collapse"
ISSUE = "#321/#334"

# label -> (old parent, new term, new label, ChEBI's own CAS xref)
PROMOTE = {
    "Na2HPO4 x 2 H2O": ("CHEBI:34683", "CHEBI:91258",
                        "disodium hydrogenphosphate dihydrate", "10028-24-7"),
    "Na2HPO4 x 12 H2O": ("CHEBI:34683", "CHEBI:91259",
                         "disodium hydrogenphosphate dodecahydrate", "10039-32-4"),
}
# loser label -> (old parent, winner identifier, winner label)
MERGE = {
    "CoCl2 x 6 H2O": ("CHEBI:35696", "CHEBI:53503", "Cobalt chloride hexahydrate"),
    "NiCl2 x 6 H2O": ("CHEBI:34887", "CHEBI:53542", "Nickel (II) chloride hexahydrate"),
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
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    coll = yaml.safe_load(COLLECTION.read_text(encoding="utf-8", errors="replace")) or {}
    recs = coll.get("ingredients", [])
    out: list[str] = []
    sssom_reground: dict[str, tuple[str, str]] = {}
    sssom_drop: set[str] = set()

    for label, (old, new_id, new_label, cas) in PROMOTE.items():
        rec = find(recs, label=label)
        if rec is None or rec.get("identifier") != old:
            out.append(f"{label}: not on {old} — skipped")
            continue
        if find(recs, ident=new_id) is not None:
            out.append(f"{label}: {new_id} already taken — this is a merge, not a promotion; skipped")
            continue
        cp = rec.setdefault("chemical_properties", {})
        old_cas = cp.get("cas_rn")
        rec["identifier"] = new_id
        om = rec.setdefault("ontology_mapping", {})
        om.update({"ontology_id": new_id, "ontology_label": new_label,
                   "ontology_source": "CHEBI", "mapping_quality": "EXACT_MATCH"})
        cp["cas_rn"] = cas
        om.setdefault("evidence", []).append({
            "evidence_type": "DATABASE_MATCH", "source": f"MIM curation ({ISSUE})",
            "notes": (f"Promoted off the anhydrous term {old}, which was absorbing five "
                      f"distinct Na2HPO4 hydrates, to the specific term {new_id} "
                      f"({new_label!r}) — MAPPING_SEMANTICS §3 step 1. cas_rn "
                      f"{old_cas!r} -> {cas!r}, taken from ChEBI's own xref on the "
                      f"specific term; the previous value was shared across the family "
                      f"and did not denote this hydrate (#334)."),
        })
        rec.setdefault("curation_history", []).append({
            "timestamp": STAMP, "curator": CURATOR, "action": "PROMOTED_TO_SPECIFIC_HYDRATE",
            "changes": (f"identifier/ontology_id {old} -> {new_id} {new_label!r}; "
                        f"mapping_quality -> EXACT_MATCH; cas_rn {old_cas!r} -> {cas!r} "
                        f"({ISSUE})."),
            "llm_assisted": False,
        })
        sssom_reground[label] = (new_id, new_label)
        out.append(f"PROMOTE  {label:<20} {old} -> {new_id} {new_label}  cas {old_cas} -> {cas}")

    for label, (old, win_id, win_label) in MERGE.items():
        lose = find(recs, label=label)
        win = find(recs, ident=win_id, label=win_label, status="MAPPED")
        if lose is None or lose.get("identifier") != old:
            out.append(f"{label}: not on {old} — skipped")
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
                         "source": f"MERGED_FROM_{old}"})
        win.setdefault("curation_history", []).append({
            "timestamp": STAMP, "curator": CURATOR, "action": "MERGED_FROM",
            "changes": (f"Absorbed {label!r}, which sat on the anhydrous term {old} "
                        f"({ISSUE}). Same substance in formula notation — a form the "
                        f"merge pass does not recognise, so it escaped dedup and was then "
                        f"grounded to the nearest lexical match. Occurrences "
                        f"{before[0]}/{before[1]} + {locc.get('total_occurrences', 0)}/"
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
                        f"Tombstoned REJECTED, SSSOM rows dropped ({ISSUE})."),
            "llm_assisted": False,
        })
        sssom_drop.add(label)
        out.append(f"MERGE    {label:<20} {old} -> {win_id} {win_label} "
                   f"(occ -> {wocc['total_occurrences']})")

    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    kept, rows = [], 0
    for line in lines:
        cells = line.rstrip("\n").split("\t")
        if len(cells) >= 5 and cells[1] in sssom_drop:
            rows += 1
            continue
        if len(cells) >= 5 and cells[1] in sssom_reground and cells[3].startswith("CHEBI:"):
            cells[3], cells[4] = sssom_reground[cells[1]]
            line = "\t".join(cells) + "\n"
            rows += 1
        kept.append(line)

    if args.apply and out:
        save_yaml(coll, COLLECTION)
        SSSOM.write_text("".join(kept), encoding="utf-8")

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'} — "
          f"{len(out)} action(s), {rows} SSSOM row(s)\n")
    for o in out:
        print(f"  {o}")
    print("\n  Untouched — no ChEBI term and no trustworthy CAS (#334): "
          "Na2HPO4 x 3/6/7 H2O, CoCl2 x 2/4 H2O, NiCl2 x 2/5 H2O, FeCl2 x 6/7 H2O")
    return 0


if __name__ == "__main__":
    sys.exit(main())
