"""Apply the reviewed, hash-guarded identity plan; local files only.

Run from the MIM root. Refuses changed inputs and repeat application.
"""

from pathlib import Path
import csv
import hashlib
import io
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
from mediaingredientmech.validation.write_validated import (
    validate_ingredient,
    write_validated_ingredient,
)
from mediaingredientmech.synonym_policy import is_resolving_synonym
from mediaingredientmech.sssom_grading import PREDICATE, CONFIDENCE, justification_for
from mediaingredientmech.utils.object_source import object_source_for

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent


def main():
    plan = json.loads((HERE / "identity-plan.json").read_text())
    sssom = ROOT / "mappings/ingredient_mappings.sssom.tsv"
    original = sssom.read_bytes()
    assert hashlib.sha256(original).hexdigest() == plan["sssom_before_sha256"], "SSSOM changed"
    for item in plan["records"]:
        src, dst = ROOT / item["source_path"], ROOT / item["destination_path"]
        if item["before_sha256"] is None:
            assert not src.exists(), f"New record already exists: {src}"
        else:
            assert (
                hashlib.sha256(src.read_bytes()).hexdigest() == item["before_sha256"]
            ), f"Changed source: {src}"
        if src != dst:
            assert not dst.exists(), f"Destination already exists: {dst}"
        errors = validate_ingredient(item["after_record"])
        assert not errors, (src, [e.message for e in errors])
    lines = original.decode().splitlines(keepends=True)
    start = next(i for i, line in enumerate(lines) if line.startswith("subject_id\t"))
    reader = csv.DictReader(lines[start:], delimiter="\t")
    rows = list(reader)
    columns = reader.fieldnames
    labels = {i["before_record"]["preferred_term"] for i in plan["records"] if i["before_record"]}
    old_rows = [r for r in rows if r["subject_label"] in labels]
    new_rows = [r for r in rows if r["subject_label"] not in labels]
    for item in plan["records"]:
        rec = item["after_record"]
        if rec["mapping_status"] != "MAPPED":
            continue
        old = item["before_record"]
        previous = [r for r in old_rows if old and r["subject_label"] == old["preferred_term"]]
        subject = (
            previous[0]["subject_id"] if previous else "MIM:" + Path(item["destination_path"]).stem
        )
        assert all(r["subject_id"] == subject for r in previous)
        rejected = {
            s["synonym_text"].casefold()
            for s in rec.get("synonyms", [])
            if not is_resolving_synonym(s)
        }
        # Retain previous external synonyms only when the semantic identity is unchanged.
        synonyms = [s["synonym_text"] for s in rec.get("synonyms", []) if is_resolving_synonym(s)]
        if old and old["identifier"] == rec["identifier"]:
            synonyms += [
                s
                for r in previous
                for s in r["other"].split("|")
                if s and s.casefold() not in rejected
            ]
        synonyms = sorted(set(synonyms), key=str.casefold)
        primary = rec["identifier"]
        ont = rec["ontology_mapping"]
        targets = [
            (
                primary,
                ont["ontology_label"] if primary == ont["ontology_id"] else rec["preferred_term"],
                "EXACT_MATCH",
            )
        ]
        if primary != ont["ontology_id"]:
            targets.append((ont["ontology_id"], ont["ontology_label"], ont["mapping_quality"]))
        for identifier, label, quality in targets:
            row = dict.fromkeys(columns, "")
            row.update(
                subject_id=subject,
                subject_label=rec["preferred_term"],
                predicate_id=PREDICATE[quality],
                object_id=identifier,
                object_label=label,
                object_source=object_source_for(identifier),
                mapping_justification=(
                    "semapv:ManualMappingCuration"
                    if quality == "EXACT_MATCH"
                    else justification_for(quality)
                ),
                source="MIM:curator=mim_semantic_review_20260921",
                mapping_date="2026-09-21",
                confidence=str(CONFIDENCE[quality]),
                comment=item["reason"] + " Evidence: " + " ; ".join(item["evidence"]),
                other="|".join(synonyms) if identifier == primary else "",
                validation_method="manual:semantic_identity_review|IDENTITY_REVIEWED|2026-09-21",
            )
            # Preserve MIM's procurement-number channel (#403). This token is
            # not an additional exact identity mapping to the registry number.
            cas_rn = next(
                (form["cas_rn"] for form in rec.get("supplied_form", []) if form.get("cas_rn")),
                (rec.get("chemical_properties") or {}).get("cas_rn"),
            )
            if cas_rn and row["predicate_id"] in {"skos:exactMatch", "skos:closeMatch"}:
                token = "CAS:" + cas_rn
                if token.casefold() not in {s.casefold() for s in row["other"].split("|")}:
                    row["other"] = "|".join(filter(None, [row["other"], token]))
            new_rows.append(row)
    buffer = io.StringIO()
    for line in lines[:start]:
        if line.startswith("# mapping_set_version:") or line.startswith("# mapping_date:"):
            line = line.split(":", 1)[0] + ': "2026-09-21"\n'
        buffer.write(line)
    writer = csv.DictWriter(buffer, fieldnames=columns, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    by_subject = {}
    for row in new_rows:
        by_subject.setdefault(row["subject_id"], []).append(row)
    for subject in dict.fromkeys(
        [r["subject_id"] for r in rows] + [r["subject_id"] for r in new_rows]
    ):
        writer.writerows(by_subject.get(subject, []))
    # All inputs and planned records validated before publishing any changes.
    (HERE / "withdrawn_sssom_rows.json").write_text(json.dumps(old_rows, indent=2) + "\n")
    for item in plan["records"]:
        src, dst = ROOT / item["source_path"], ROOT / item["destination_path"]
        write_validated_ingredient(item["after_record"], dst)
        if src != dst:
            src.unlink()
    sssom.write_text(buffer.getvalue())
    print(
        f'Applied {len(plan["records"])} record changes; SSSOM {len(rows)} -> {len(new_rows)} rows'
    )


if __name__ == "__main__":
    main()
