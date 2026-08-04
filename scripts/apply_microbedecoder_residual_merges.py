"""Apply the residual dispositions closed PR #201 recorded but never landed (#212).

Two kinds of change, neither of which `promote_resolved_unmapped.py` can make:

  merges   a raw microbedecoder label that duplicates an ALREADY-mapped record.
           The label becomes a RAW_TEXT synonym on the existing record and the
           UNMAPPED record goes away. No SSSOM row -- the target already has one.

  flags    multi-component blends / named media, and CSV-split parse fragments,
           which no single ontology term can ground. They stay in the unmapped
           collection but move to NEEDS_EXPERT so they stop being counted as
           unworked grounding candidates.

The 56-row blend list is read from PR #201's manifest. The merge and noise sets
are NOT in any manifest -- #201 recorded them only in its commit message -- so
they are literal tables here and each row carries its own reason. Five rows that
#201 filed as blends are in fact single ingredients this repo already maps; they
are re-routed to MERGES below rather than retired as blends.

Dry-run by default; pass --apply to write.
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

# raw label -> the already-mapped record it duplicates. `target_term` disambiguates
# when a CURIE is carried by more than one record (MICRO:0000178 is held by both
# "Bacto peptone" and "Peptone"); None means the CURIE is unique. Resolution is
# strict -- an ambiguous or missing target is an error, never a last-wins guess.
MERGES = [
    # from #201's microbedecoder_residual_locant_fixed.tsv (targets already mapped)
    ("2-dichloropropane", "CHEBI:142468", None,
     "dropped-locant duplicate of 1,2-dichloropropane"),
    ("2-trichloroethane", "CHEBI:36018", None,
     "dropped-locant duplicate of 1,1,2-trichloroethane"),
    # concentration-prefixed duplicates
    ("1% Sodium Chloride", "CHEBI:26710", None,
     "concentration-prefixed duplicate of sodium chloride"),
    ("1 % Sodium Lactate", "CHEBI:75228", None,
     "concentration-prefixed duplicate of sodium lactate"),
    # #201 filed these five as blends, but each is a single ingredient already
    # mapped here -- flagging them NEEDS_EXPERT would retire groundable records
    # behind a rationale asserting they are multi-component. See PR review.
    ("(+)-D-glycogen", "CHEBI:28087", "Glycogen",
     "optical-rotation-prefixed duplicate of glycogen; a single macromolecule, not a blend"),
    ("(+)-L-lyxitol", "CHEBI:18403", "Arabitol",
     "L-lyxitol is a ChEBI synonym of L-arabinitol (CHEBI:18403); a single polyol, not a blend"),
    ("Peptones", "MICRO:0000178", "Peptone",
     "plural of the already-mapped peptone record"),
    ("Peptone (0.01 %", "MICRO:0000178", "Peptone",
     "concentration-truncated duplicate of peptone"),
    ("Yeast Extract (0.01 %", "FOODON:03315426", "Yeast extract",
     "concentration-truncated duplicate of yeast extract"),
]

# Blend-manifest rows handled as merges above rather than flagged.
BLEND_ROWS_REROUTED = {t for t, _, _, _ in MERGES}

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
    """#201's blend manifest, minus the rows re-routed to MERGES."""
    path = MANIFESTS / "microbedecoder_residual_blends.tsv"
    with path.open() as fh:
        return {
            r["preferred_term"]: "multi-component blend or named medium; no single "
            "ontology term grounds it -- needs decomposition into constituents"
            for r in csv.DictReader(fh, delimiter="\t")
            if r["preferred_term"] not in BLEND_ROWS_REROUTED
        }


def resolve_target(mapped: dict, curie: str, term: str | None) -> dict:
    """The one mapped record for `curie`. Ambiguity is an error, not a guess."""
    hits = [r for r in mapped["ingredients"] if r["identifier"] == curie]
    if term is not None:
        hits = [r for r in hits if r["preferred_term"] == term]
    if len(hits) != 1:
        raise LookupError(
            f"{curie}"
            + (f" (preferred_term={term!r})" if term else "")
            + f" resolves to {len(hits)} mapped records, expected exactly 1"
        )
    return hits[0]


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

    by_term = {r["preferred_term"]: r for r in unmapped["ingredients"]}

    merged, flagged, skipped = [], [], []

    for term, curie, target_term, why in MERGES:
        src = by_term.get(term)
        if src is None:
            skipped.append(f"merge {term!r} -> {curie}: source record absent")
            continue
        if src.get("mapping_status") != "UNMAPPED":
            skipped.append(f"merge {term!r}: status is {src.get('mapping_status')}, not UNMAPPED")
            continue
        tgt = resolve_target(mapped, curie, target_term)
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
    # aggregate_records.py stamps this on every rebuild; writing the collection
    # directly bypasses it, which would leave the header older than the curation
    # events it now contains.
    unmapped["generation_date"] = stamp
    mapped["generation_date"] = stamp

    print(f"merged into existing mapped records: {len(merged)}")
    for ident, term, curie in merged:
        print(f"   {ident:15} {term!r} -> {curie}")
    print(f"\nflagged NEEDS_EXPERT: {len(flagged)}")
    for ident, term in flagged[:8]:
        print(f"   {ident:15} {term!r}")
    if len(flagged) > 8:
        print(f"   ... and {len(flagged) - 8} more")
    # 'Sodium(+)' is in #201's blend manifest but #202 has since mapped it. That
    # single skip is expected; anything else means the data moved under us and
    # applying a partial batch would be worse than refusing.
    EXPECTED_SKIPS = 1
    if skipped:
        print(f"\nskipped: {len(skipped)}")
        for s in skipped:
            print(f"   {s}")
    print(f"\nunmapped collection: total_count={unmapped['total_count']} "
          f"unmapped_count={unmapped['unmapped_count']}")
    print(f"mapped collection:   total_count={mapped['total_count']} "
          f"mapped_count={mapped['mapped_count']}")

    if len(skipped) > EXPECTED_SKIPS:
        print(f"\nERROR: {len(skipped)} skips, expected at most {EXPECTED_SKIPS}. "
              "Refusing to write a partial batch; re-check the manifests against the data.")
        return 1

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
