"""Publish the three recovered identities and withdraw the false CMC mixture row."""

import csv
import hashlib
import io
import json
from pathlib import Path

import yaml

from mediaingredientmech.utils.object_source import object_source_for
from mediaingredientmech.synonym_policy import is_resolving_synonym

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent


def main():
    path = ROOT / "mappings/ingredient_mappings.sssom.tsv"
    before = path.read_bytes()
    if hashlib.sha256(before).hexdigest() != "acc15e15aba5d42971a41d3d55369b47c0d5937e3db874d476eeda76058cc861":
        raise ValueError("SSSOM no longer matches the reviewed pre-resolution snapshot")
    lines = before.decode().splitlines(keepends=True)
    reader = csv.DictReader((line for line in lines if not line.startswith("#")), delimiter="\t")
    old = list(reader)
    columns = reader.fieldnames
    removed = [row for row in old if row["subject_id"] == "MIM:CMC_PY_Horse_Serum"]
    if len(removed) != 1:
        raise ValueError("Expected exactly one withdrawn CMC mixture identity")
    rows = [row for row in old if row not in removed]
    plan = json.loads((HERE / "identities/identity-plan.json").read_text())["records"]
    added = []
    for item in plan:
        record_path = ROOT / item["destination_path"]
        record = yaml.safe_load(record_path.read_text())
        if record != item["after_record"]:
            raise ValueError(f"Unreviewed identity change: {record_path}")
        subject = "MIM:" + record_path.stem
        if any(row["subject_id"] == subject for row in rows):
            raise ValueError(f"Identity already published: {subject}")
        ontology = record["ontology_mapping"]
        if record["identifier"] != ontology["ontology_id"]:
            raise ValueError("This batch contains primary identities only")
        synonyms = sorted({s["synonym_text"] for s in record.get("synonyms", []) if is_resolving_synonym(s)})
        cas = next(
            (f["cas_rn"] for f in record.get("supplied_form", []) if f.get("cas_rn")),
            (record.get("chemical_properties") or {}).get("cas_rn"),
        )
        if not cas and record["identifier"].startswith("cas:"):
            cas = record["identifier"].split(":", 1)[1]
        if cas:
            synonyms.append("CAS:" + cas)
        row = dict.fromkeys(columns, "")
        row.update(
            subject_id=subject,
            subject_label=record["preferred_term"],
            predicate_id="skos:exactMatch",
            object_id=record["identifier"],
            object_label=ontology["ontology_label"],
            object_source=object_source_for(record["identifier"]),
            mapping_justification="semapv:ManualMappingCuration",
            source="MIM:curator=mim_semantic_review_710",
            mapping_date="2026-09-21",
            confidence="0.99",
            comment="Original source identity recovered and checked; reports/semantic_review_20260921/resolution/identities/README.md",
            other="|".join(dict.fromkeys(synonyms)),
            validation_method="manual:original_source_identity_review|IDENTITY_REVIEWED|2026-09-21",
        )
        added.append(row)
    stream = io.StringIO()
    stream.writelines(line for line in lines if line.startswith("#"))
    writer = csv.DictWriter(stream, fieldnames=columns, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows + added)
    path.write_text(stream.getvalue())
    (HERE / "sssom-changes.json").write_text(json.dumps({
        "before_sha256": hashlib.sha256(before).hexdigest(),
        "after_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "withdrawn_rows": removed,
        "added_rows": added,
    }, indent=2) + "\n")


if __name__ == "__main__":
    main()
