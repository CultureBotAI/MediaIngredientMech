#!/usr/bin/env python3
"""Rejoin microbedecoder labels the comma-stripping ingest tore in half (#308/#313).

#308 records that the microbedecoder ingest strips commas from every chemical
label. A name containing a comma therefore arrives as two or more records, each
a fragment of the original, and each then grounded — or not — on its own.

The fragments pair up, and the pairing is what identifies the original:

    Butane-1        + 4-diol                      -> butane-1,4-diol
    Ethylenediamine-N + N'-disuccinic Acid (EDDS) -> ethylenediamine-N,N'-disuccinic acid

`2-tetrachloroethane` is the same defect with the head fragments lost: splitting
`1,1,2,2-tetrachloroethane` on commas yields `1`, `1`, `2` and `2-tetrachloroethane`,
and only the last survives as a record because bare digits are not labels.

This is the same mechanism that produced the `D` record resolved in #346, where
`D,L-lactic acid, sodium salt` split into `D` plus a parenthesised remainder, and
the orphaned `D` then attracted a limonene CAS and an aspartate mapping.

**Repairs are only applied where a fragment pair reconstructs a real compound
that ChEBI can confirm.** Two do; one needs a registry mint because ChEBI has no
term for EDDS at all (searched locally and live at OLS4).

`Sulfonamide` is not a comma split — it is included because its label matches
`CHEBI:35358 sulfonamide` exactly and it has been sitting at PENDING_REVIEW.

Deliberately NOT repaired: `0129 (2` and `4-Diamino-6` are two thirds of
`O/129 (2,4-diamino-6,7-diisopropylpteridine)`, the vibriostatic agent, but the
third fragment (`7-diisopropylpteridine)`) is not in the corpus, so the label
cannot be reconstructed from what survives. `3-methylacetate` and
`DL-2-gamma-aminobutyrate` are likewise fragments whose partners are absent, and
guessing the missing text would invent a compound.

    python scripts/repair_comma_split_labels.py            # dry-run
    python scripts/repair_comma_split_labels.py --apply
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
STAMP = "2026-08-14T00:00:00+00:00"
CURATOR = "repair_comma_split_labels"
ISSUE = "#308/#313"

# survivor label -> (fragment absorbed or None, repaired label, identifier,
#                    ontology label, grade, why)
REPAIRS = {
    "Butane-1": (
        "4-diol", "Butane-1,4-diol", "CHEBI:41189", "butane-1,4-diol",
        "EXACT_MATCH",
        "`Butane-1` and `4-diol` are the two halves of `butane-1,4-diol` split at "
        "its only comma. Neither fragment names a compound; rejoined they name one "
        "ChEBI holds as CHEBI:41189 (C4H10O2)"),
    "Ethylenediamine-N": (
        "N'-disuccinic Acid (EDDS)", "Ethylenediamine-N,N'-disuccinic acid (EDDS)",
        "kgmicrobe.compound:ethylenediamine_n_n_disuccinic_acid", None,
        "FALLBACK_REGISTRY",
        "`Ethylenediamine-N` and `N'-disuccinic Acid (EDDS)` are the two halves of "
        "`ethylenediamine-N,N'-disuccinic acid` split at its only comma — the "
        "surviving `(EDDS)` on the second fragment confirms the reading. ChEBI has "
        "no term for EDDS (searched the local build and live at OLS4), so "
        "MAPPING_SEMANTICS §3 step 3 applies and the rejoined record takes a "
        "registry mint"),
    "2-tetrachloroethane": (
        None, "1,1,2,2-Tetrachloroethane", "CHEBI:36026", "1,1,2,2-tetrachloroethane",
        "EXACT_MATCH",
        "`2-tetrachloroethane` is the tail of `1,1,2,2-tetrachloroethane`: splitting "
        "that name on commas yields `1`, `1`, `2` and `2-tetrachloroethane`, and only "
        "the last survives as a record because bare digits are not labels. The "
        "reconstruction is unambiguous — no other compound ends in "
        "`2-tetrachloroethane`"),
    "Sulfonamide": (
        None, "Sulfonamide", "CHEBI:35358", "sulfonamide", "EXACT_MATCH",
        "not a comma split; the label matches CHEBI:35358 `sulfonamide` exactly and "
        "the record had been left at PENDING_REVIEW"),
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
            index.setdefault(str(rec.get("preferred_term") or ""), rec)

    out, skipped = [], []
    for survivor, (frag, label, curie, onto_label, grade, why) in REPAIRS.items():
        rec = index.get(survivor)
        if rec is None or rec.get("mapping_status") not in ("NEEDS_EXPERT", "PENDING_REVIEW"):
            skipped.append(f"{survivor}: absent or already resolved")
            continue
        loser = index.get(frag) if frag else None
        if frag and loser is None:
            skipped.append(f"{survivor}: partner fragment {frag!r} not found")
            continue

        old_id = rec.get("identifier")
        note = (f"Repaired a comma-split label ({ISSUE}): {why}. The ingest strips "
                f"commas from every chemical label, so a name containing one arrives "
                f"as separate fragment records — the same mechanism that produced the "
                f"`D` record resolved in #346.")

        rec["preferred_term"] = label
        rec["identifier"] = curie
        rec["mapping_status"] = "MAPPED"
        syns = rec.setdefault("synonyms", [])
        for raw in filter(None, (survivor, frag)):
            if raw.lower() not in {str(s.get("synonym_text", "")).lower() for s in syns}:
                syns.append({"synonym_text": raw, "synonym_type": "RAW_TEXT",
                             "source": f"comma-split fragment ({ISSUE})"})
        om = rec.setdefault("ontology_mapping", {})
        om.update({"ontology_id": curie, "ontology_label": onto_label or label,
                   "ontology_source": curie.split(":")[0] if ":" in curie else "CHEBI",
                   "mapping_quality": grade})
        om.setdefault("evidence", []).append({
            "evidence_type": "MANUAL_CURATION",
            "source": f"MIM curation ({ISSUE})", "notes": note})
        rec.setdefault("curation_history", []).append({
            "timestamp": STAMP, "curator": CURATOR, "action": "REPAIRED_COMMA_SPLIT_LABEL",
            "previous_status": "NEEDS_EXPERT", "new_status": "MAPPED",
            "changes": (f"preferred_term {survivor!r} -> {label!r}; {old_id} -> {curie}. "
                        + (f"Absorbed the partner fragment {frag!r}. " if frag else "")
                        + note),
            "llm_assisted": False})

        if loser is not None:
            loser["identifier"] = curie
            loser["mapping_status"] = "REJECTED"
            occ = loser.setdefault("occurrence_statistics", {})
            occ["total_occurrences"] = 0
            occ["media_count"] = 0
            loser.setdefault("curation_history", []).append({
                "timestamp": STAMP, "curator": CURATOR, "action": "MERGED_INTO",
                "changes": (f"Merged into {curie} {label!r}: this record is the other "
                            f"half of a comma-split label, not an ingredient. {note}"),
                "llm_assisted": False})

        out.append(f"{survivor[:26]:<28} + {str(frag or '-')[:26]:<28} -> {label[:34]:<36} {curie}")

    if args.apply and out:
        for path, coll in colls.items():
            save_yaml(coll, path)

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'} — "
          f"{len(out)} repaired\n")
    for o in out:
        print(f"  {o}")
    for s in skipped:
        print(f"  SKIPPED {s}")
    print("\n  Not repaired — the partner fragment is absent, so the original label "
          "cannot be\n  reconstructed and guessing it would invent a compound: "
          "`0129 (2` + `4-Diamino-6`\n  (two thirds of the vibriostatic agent "
          "O/129), `3-methylacetate`, `DL-2-gamma-aminobutyrate`.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
