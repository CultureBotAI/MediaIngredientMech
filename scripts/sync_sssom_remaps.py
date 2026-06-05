#!/usr/bin/env python3
"""Surgically sync mappings/ingredient_mappings.sssom.tsv to the curated remaps.

The SSSOM set has no generator (only a validator), so it drifted from the curated
data after the identifier remaps in PRs #36/#37/#40. This updates ONLY the rows
for the affected subjects, leaving every other row and the file format byte-for-
byte intact (a full from-scratch regeneration would risk a large, subtly-wrong
diff against the bespoke pipeline-provenance columns).

For each listed subject (matched by subject_label = preferred_term):
  * record removed from the curated data  -> drop its SSSOM row(s)
  * record now REJECTED (merged)          -> drop its SSSOM row(s)
  * otherwise -> update the ontology row (object_source startswith "obo:") to the
    current ontology_id / ontology_label / source / predicate, set
    mapping_justification=ManualMappingCuration and mapping_date to RUN_DATE.

Usage:
    python scripts/sync_sssom_remaps.py --date 2026-06-04 [--dry-run]
"""

import argparse
import sys
from pathlib import Path

import yaml

SSSOM = Path("mappings/ingredient_mappings.sssom.tsv")
CURATED = Path("data/curated/mapped_ingredients.yaml")

# Subjects whose ontology mapping changed (or which were removed) since the SSSOM
# was last written. Matched by subject_label (== preferred_term).
SYNC_SUBJECTS = [
    "CHEBI:1",                 # record removed (PR #36)
    "Bacto Soytone",           # now REJECTED, merged -> FOODON:03315720 (PR #36)
    "(R)-3-hydroxybutyrate",   # CHEBI:37054 -> CHEBI:10983 (PR #37)
    "(S)-3-hydroxybutyrate",   # CHEBI:37054 -> CHEBI:11047 (PR #37)
    "L-Carnitine",             # CHEBI:17126 -> CHEBI:16347 (PR #37)
    "Tryptone",                # FOODON:03315719 -> MICRO:0000182 (PR #40)
    "Trypticase",              # FOODON:03315719 -> MICRO:0000175 (PR #40)
]

OBJECT_SOURCE = {
    "CHEBI": "obo:chebi.owl", "FOODON": "obo:foodon.owl", "ENVO": "obo:envo.owl",
    "UBERON": "obo:uberon.owl", "NCIT": "obo:ncit.owl", "MICRO": "obo:micro.owl",
    "BTO": "obo:bto.owl", "MESH": "registry:mesh", "CAS": "registry:cas",
    "kgmicrobe.compound": "kgm:compound", "kgmicrobe.ingredient": "kgm:ingredient",
}
PREDICATE = {
    "EXACT_MATCH": "skos:exactMatch", "CLOSE_MATCH": "skos:closeMatch",
    "SYNONYM_MATCH": "skos:exactMatch", "NARROW_MATCH": "skos:narrowMatch",
    "BROAD_MATCH": "skos:broadMatch",
}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", required=True, help="Run date, e.g. 2026-06-04")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    curated = yaml.safe_load(CURATED.read_text())
    by_term = {r.get("preferred_term"): r for r in curated["ingredients"]}

    lines = SSSOM.read_text().splitlines(keepends=True)
    header = [ln for ln in lines if ln.startswith("#")]
    body = [ln for ln in lines if not ln.startswith("#")]
    col_line, data_lines = body[0], body[1:]
    cols = col_line.rstrip("\n").split("\t")
    idx = {c: i for i, c in enumerate(cols)}

    sync = set(SYNC_SUBJECTS)
    out, removed, updated = [], [], []
    for ln in data_lines:
        f = ln.rstrip("\n").split("\t")
        label = f[idx["subject_label"]]
        if label not in sync:
            out.append(ln)
            continue
        rec = by_term.get(label)
        # Removed or REJECTED record, or a non-ontology (registry) row: drop the
        # ontology row; (these subjects have a single obo: row).
        if rec is None or rec.get("mapping_status") == "REJECTED":
            removed.append((label, f[idx["object_id"]]))
            continue
        if not f[idx["object_source"]].startswith("obo:"):
            out.append(ln)  # keep any registry/identity row untouched
            continue
        om = rec.get("ontology_mapping") or {}
        f[idx["object_id"]] = om["ontology_id"]
        f[idx["object_label"]] = om.get("ontology_label") or ""
        f[idx["object_source"]] = OBJECT_SOURCE.get(om.get("ontology_source"), f[idx["object_source"]])
        f[idx["predicate_id"]] = PREDICATE.get(om.get("mapping_quality"), f[idx["predicate_id"]])
        f[idx["mapping_justification"]] = "semapv:ManualMappingCuration"
        f[idx["mapping_date"]] = args.date
        if "comment" in idx:
            f[idx["comment"]] = f"Synced to curated remap ({args.date})."
        updated.append((label, f[idx["object_id"]]))
        out.append("\t".join(f) + "\n")

    # Refresh the mapping-set version/date in the header.
    new_header = []
    for ln in header:
        if ln.startswith("# mapping_set_version:"):
            ln = f'# mapping_set_version: "{args.date}"\n'
        elif ln.startswith("# mapping_date:"):
            ln = f'# mapping_date: "{args.date}"\n'
        new_header.append(ln)

    print(f"updated rows: {len(updated)}")
    for lbl, oid in updated:
        print(f"   {lbl!r} -> {oid}")
    print(f"removed rows: {len(removed)}")
    for lbl, oid in removed:
        print(f"   {lbl!r} (was {oid})")

    if not args.dry_run:
        SSSOM.write_text("".join(new_header) + col_line + "".join(out))
        print(f"\nWrote {SSSOM}")
    else:
        print("\n[dry-run] not written")


if __name__ == "__main__":
    main()
