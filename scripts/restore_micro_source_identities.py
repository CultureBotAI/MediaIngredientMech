#!/usr/bin/env python3
"""Restore the three source-reviewed MICRO identities in #759 (dry-run default).

Writes validated ingredient records, exact SSSOM rows and recipe membership IDs.
The apply log supplies owner hashes for the mapping-change review receipt.
Run sync-curated and generated-export refreshes after applying this batch.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.micro_source import load_source
from mediaingredientmech.validation.write_validated import ValidationFailedError, validate_ingredient, write_validated_ingredient

CURATOR = "restore_micro_source_identities"
DATE = "2026-09-23"
SOURCE = "src/mediaingredientmech/ontology_sources/micro/manifest.json"
TARGETS = {
    "Proteose_Peptone_No_2": ("kgmicrobe.ingredient:proteose_peptone_no_2", "MICRO:0002393", 7),
    "Rabbit_Serum": ("kgmicrobe.ingredient:rabbit_serum", "MICRO:0002392", 21),
    "V-8_Juice": ("kgmicrobe.ingredient:v-8_juice", "MICRO:0002250", 3),
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_tsv(path: Path):
    lines = path.read_text().splitlines(keepends=True)
    comments = [line for line in lines if line.startswith("#")]
    reader = csv.DictReader((line for line in lines if not line.startswith("#")), delimiter="\t")
    return comments, reader.fieldnames, list(reader)


def tsv_text(comments, fields, rows):
    out = io.StringIO()
    out.writelines(comments)
    writer = csv.DictWriter(out, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--log", type=Path, default=ROOT / "reports/micro-restoration-apply.json")
    args = parser.parse_args()
    terms = load_source()
    records, log = {}, []
    for slug, (old, new, count) in TARGETS.items():
        path = ROOT / f"data/ingredients/mapped/{slug}.yaml"
        record = yaml.safe_load(path.read_text())
        if record["identifier"] != old or record["ontology_mapping"]["mapping_quality"] != "NARROW_MATCH":
            raise ValueError(f"{slug}: source changed or restoration already applied")
        if record["occurrence_statistics"] != {"total_occurrences": count, "media_count": count}:
            raise ValueError(f"{slug}: occurrence counts changed")
        if any((record.get(field) or {}).get("cas_rn") for field in ("chemical_properties", "supplied_form")):
            raise ValueError(f"{slug}: new CAS annotation requires a fresh source review")
        term = terms[new]
        note = (
            f"Restore {new} '{term.label}' from the pinned KG-Microbe MICRO KGX (#759). "
            f"Both node snapshots contain this exact class label; current KGX parent(s): {', '.join(term.parents)}. "
            f"Original IRI: {term.iri}. This supersedes #137's canonical-IRI-only rejection; "
            "it does not claim OLS defining-ontology status. No verified CAS RN is supplied for this material."
        )
        mapping = record["ontology_mapping"]
        for evidence in mapping.get("evidence", []):
            evidence["notes"] = "SUPERSEDED by source-backed review #759: " + evidence.get("notes", "")
        mapping.update(ontology_id=new, ontology_label=term.label, ontology_source="MICRO", mapping_quality="EXACT_MATCH")
        mapping.setdefault("evidence", []).append({"evidence_type": "CURATOR_JUDGMENT", "source": SOURCE, "notes": note})
        record["identifier"] = new
        record_curation_event(record, curator=CURATOR, action="CORRECTED", changes=note,
                              previous_status="MAPPED", new_status="MAPPED", llm_assisted=True,
                              llm_model="gpt-6")
        errors = validate_ingredient(record)
        if errors:
            raise ValidationFailedError(path, errors)
        records[slug] = record
        log.append({"source_record": str(path.relative_to(ROOT)), "shape": "ontology_identity_restoration",
                    "before_yaml_sha256": sha(path), "change": f"{old} -> {new}; NARROW_MATCH -> EXACT_MATCH",
                    "verification": note})

    sssom = ROOT / "mappings/ingredient_mappings.sssom.tsv"
    comments, fields, rows = read_tsv(sssom)
    kept, seen, removed = [], Counter(), Counter()
    for row in rows:
        slug = row["subject_id"].removeprefix("MIM:")
        if slug in TARGETS:
            old, new, _ = TARGETS[slug]
            if row["object_id"] == old:
                removed[slug] += 1
                continue
            term = terms[new]
            row.update(predicate_id="skos:exactMatch", object_id=new, object_label=term.label,
                       object_source="obo:micro.owl", mapping_justification="semapv:ManualMappingCuration",
                       source=f"MIM:KG-Microbe MICRO KGX|MIM:curator={CURATOR}", mapping_date=DATE, confidence="0.99",
                       comment=f"Exact source-reviewed MICRO identity (#759); original IRI {term.iri}. Supersedes the local identity and parent-only mapping from #137.",
                       validation_method=f"manual:{CURATOR}|KGX_SOURCE|{DATE}")
            seen[slug] += 1
        kept.append(row)
    if seen != Counter({slug: 1 for slug in TARGETS}) or removed != seen:
        raise ValueError("Expected one ontology and one local identity row per subject")

    membership = ROOT / "mappings/culturemech_recipe_membership.tsv"
    mc, mf, memberships = read_tsv(membership)
    moves = {old: new for old, new, _ in TARGETS.values()}
    moved = Counter()
    for row in memberships:
        old = row["mim_identifier"]
        if old in moves:
            row["mim_identifier"] = moves[old]
            moved[old] += 1
    if moved != Counter({old: count for old, _, count in TARGETS.values()}):
        raise ValueError(f"Unexpected membership counts: {moved}")
    memberships.sort(key=lambda row: (row["mim_identifier"], row["recipe_id"]))
    keys = [(row["mim_identifier"], row["recipe_id"]) for row in memberships]
    if len(keys) != len(set(keys)):
        raise ValueError("Restoration would duplicate recipe memberships")

    if args.apply:
        args.log.parent.mkdir(parents=True, exist_ok=True)
        args.log.with_suffix(".before.sssom.tsv").write_bytes(sssom.read_bytes())
        for entry, (slug, record) in zip(log, records.items(), strict=True):
            path = ROOT / entry["source_record"]
            write_validated_ingredient(record, path)
            entry["after_yaml_sha256"] = sha(path)
        sssom.write_text(tsv_text(comments, fields, kept))
        membership.write_text(tsv_text(mc, mf, memberships))
        args.log.write_text(json.dumps({"records": log, "membership_moves": moved}, indent=2) + "\n")
    print(json.dumps({"applied": args.apply, "records": list(records), "membership_moves": moved,
                      "sssom_changed": sum(seen.values()), "sssom_removed": sum(removed.values())}, indent=2))


if __name__ == "__main__":
    main()
