"""Apply the residual dispositions closed PR #201 recorded but never landed (#212).

Two kinds of change, neither of which `promote_resolved_unmapped.py` can make:

  merges   a raw microbedecoder label that duplicates an ALREADY-mapped record.
           The label becomes a RAW_TEXT synonym on the existing record and the
           UNMAPPED record goes away. No SSSOM row -- the target already has one.

  flags    multi-component blends / named media, and CSV-split parse fragments,
           which no single ontology term can ground. They stay in the unmapped
           collection but move to NEEDS_EXPERT so they stop being counted as
           unworked grounding candidates.

Reads the decision manifests from PR #201 so the applied set is exactly the
reviewed set. Dry-run by default; pass --apply to write.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
UNMAPPED = ROOT / "data" / "curated" / "unmapped_ingredients.yaml"
MANIFESTS = ROOT / "mappings"

# raw label -> already-mapped record it duplicates. From #201's
# microbedecoder_residual_locant_fixed.tsv (the two whose targets already
# exist) plus the two percentage-prefixed duplicates.
MERGES = [
    ("2-dichloropropane", "CHEBI:142468", "dropped-locant duplicate of 1,2-dichloropropane"),
    ("2-trichloroethane", "CHEBI:36018", "dropped-locant duplicate of 1,1,2-trichloroethane"),
    ("1% Sodium Chloride", "CHEBI:26710", "concentration-prefixed duplicate of sodium chloride"),
    ("1 % Sodium Lactate", "CHEBI:75228", "concentration-prefixed duplicate of sodium lactate"),
]

# CSV-split fragments and the one genuinely ambiguous isomer.
NOISE = {
    "2-tetrachloroethane": "raw fragment is reachable from both 1,1,1,2- (CHEBI:34024) and "
    "1,1,2,2-tetrachloroethane (CHEBI:36026); no unique reconstruction",
    "0129 (2": "CSV comma-split fragment of vibriostatic agent O/129 "
    "(2,4-diamino-6,7-di-iso-propylpteridine phosphate)",
    "4-Diamino-6": "CSV comma-split fragment of the same O/129 label",
    "4-diol": "CSV comma-split fragment; parent compound not recoverable from the fragment",
}


def blend_terms() -> dict[str, str]:
    path = MANIFESTS / "microbedecoder_residual_blends.tsv"
    with path.open() as fh:
        return {
            r["preferred_term"]: "multi-component blend or named medium; no single "
            "ontology term grounds it -- needs decomposition into constituents"
            for r in csv.DictReader(fh, delimiter="\t")
        }


def event(action: str, changes: str, *, stamp: str, previous: str | None = None,
          new: str | None = None) -> dict:
    ev = {"timestamp": stamp, "curator": "microbedecoder-residual-dispositions",
          "action": action, "changes": changes}
    if previous:
        ev["previous_status"] = previous
    if new:
        ev["new_status"] = new
    ev["llm_assisted"] = True
    return ev


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true", help="write; default is dry-run")
    args = ap.parse_args()

    stamp = dt.datetime.now(dt.timezone.utc).isoformat()
    mapped = yaml.safe_load(MAPPED.read_text())
    unmapped = yaml.safe_load(UNMAPPED.read_text())

    by_curie = {r["identifier"]: r for r in mapped["ingredients"]}
    by_term = {r["preferred_term"]: r for r in unmapped["ingredients"]}

    merged, flagged, skipped = [], [], []

    for term, curie, why in MERGES:
        src, tgt = by_term.get(term), by_curie.get(curie)
        if src is None or tgt is None:
            skipped.append(f"merge {term!r} -> {curie}: "
                           f"{'source record absent' if src is None else 'target record absent'}")
            continue
        if src.get("mapping_status") != "UNMAPPED":
            skipped.append(f"merge {term!r}: status is {src.get('mapping_status')}, not UNMAPPED")
            continue
        existing = {s.get("synonym_text") for s in tgt.setdefault("synonyms", [])}
        if term not in existing:
            tgt["synonyms"].append(
                {"synonym_text": term, "synonym_type": "RAW_TEXT", "source": "microbedecoder"}
            )
        tgt.setdefault("curation_history", []).append(
            event("MERGED_FROM_UNMAPPED_DUPLICATE",
                  f"Absorbed {src['identifier']} {term!r} as a RAW_TEXT synonym -- {why}. "
                  f"No new SSSOM row; {curie} is already mapped.", stamp=stamp)
        )
        unmapped["ingredients"].remove(src)
        merged.append((src["identifier"], term, curie))

    reasons = {**blend_terms(), **NOISE}
    for term, why in reasons.items():
        rec = by_term.get(term)
        if rec is None:
            skipped.append(f"flag {term!r}: record absent")
            continue
        if rec.get("mapping_status") != "UNMAPPED":
            skipped.append(f"flag {term!r}: status is {rec.get('mapping_status')}, not UNMAPPED")
            continue
        rec["mapping_status"] = "NEEDS_EXPERT"
        rec.setdefault("curation_history", []).append(
            event("FLAGGED_NEEDS_EXPERT", f"Not a single-compound grounding target: {why}.",
                  stamp=stamp, previous="UNMAPPED", new="NEEDS_EXPERT")
        )
        flagged.append((rec["identifier"], term))

    # total_count = records held; unmapped_count = records whose status is UNMAPPED.
    unmapped["total_count"] = len(unmapped["ingredients"])
    unmapped["unmapped_count"] = sum(
        1 for r in unmapped["ingredients"] if r.get("mapping_status") == "UNMAPPED"
    )
    mapped["total_count"] = len(mapped["ingredients"])
    mapped["mapped_count"] = sum(
        1 for r in mapped["ingredients"] if r.get("mapping_status") == "MAPPED"
    )

    print(f"merged into existing mapped records: {len(merged)}")
    for ident, term, curie in merged:
        print(f"   {ident:15} {term!r} -> {curie}")
    print(f"\nflagged NEEDS_EXPERT: {len(flagged)}")
    for ident, term in flagged[:8]:
        print(f"   {ident:15} {term!r}")
    if len(flagged) > 8:
        print(f"   ... and {len(flagged) - 8} more")
    if skipped:
        print(f"\nskipped: {len(skipped)}")
        for s in skipped:
            print(f"   {s}")
    print(f"\nunmapped collection: total_count={unmapped['total_count']} "
          f"unmapped_count={unmapped['unmapped_count']}")
    print(f"mapped collection:   total_count={mapped['total_count']} "
          f"mapped_count={mapped['mapped_count']}")

    if not args.apply:
        print("\nDRY RUN -- nothing written. Pass --apply to write.")
        return 0

    save_yaml(mapped, MAPPED, validate=True, target_class="IngredientCollection")
    save_yaml(unmapped, UNMAPPED, validate=True, target_class="IngredientCollection")
    print("\nwrote data/curated/{mapped,unmapped}_ingredients.yaml")
    print("next: just export-individual && just build-docs && just qc")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
