#!/usr/bin/env python3
"""Apply the five records in the four reviewed KG-Microbe scope decisions.

Dry-run by default. The log and before-image feed the approval-free mapping
change receipt; a separate complete-row review is required for publication.
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

from mediaingredientmech.curate.curation_event import record_curation_event  # noqa: E402
from mediaingredientmech.validation.write_validated import (  # noqa: E402
    validate_ingredient,
    write_validated_ingredient,
)

CURATOR = "kgmicrobe_scope_review"
DATE = "2026-09-23"
EVIDENCE = "reports/sssom_completion_20260921/mapping_review/chemical-scope-review.md"
LOCAL = "kgmicrobe.ingredient:sorbitan_monooleate"
DECISIONS = {
    "Polymyxin_B": (
        "NCIT:C61894",
        "NCIT:C61894",
        "Polymyxin B",
        "1404-26-8",
        "Keep the NCI-defined B1/B2 mixture. CAS 1404-26-8 annotates this mixture; "
        "CHEBI:8309 and CAS 4135-11-9 denote B1. Neither B1 nor sulfate is equivalent to this record.",
    ),
    "Rifamycin": (
        "NCIT:C29406",
        "CHEBI:26580",
        "rifamycins",
        None,
        "Re-ground the three unqualified MicrobeDecoder observations at unspecified rifamycin-family scope. "
        "BacDive 16969 and 13220 report production; 166282 reports resistance. None specifies SV or a CAS. "
        "Family indexing does not imply production of, or resistance to, every member. "
        "The separate Rifamycin_Sv record remains CHEBI:29673; no single CAS is assigned to this family.",
    ),
    "Rifamycin_Sv": (
        "CHEBI:29673",
        "CHEBI:29673",
        "rifamycin SV",
        "6998-60-3",
        "Preserve explicit rifamycin SV and its 28 source observations as CHEBI:29673. "
        "ChEBI independently supports CAS 6998-60-3 on SV; do not propagate it to the rifamycin family.",
    ),
    "Xanthine": (
        "CHEBI:17712",
        "CHEBI:17712",
        "9H-xanthine",
        "69-89-6",
        "Retain the existing CAS-grounded ingredient representation CHEBI:17712 and CAS 69-89-6. "
        "Generic trait observations named xanthine use CHEBI:15318. Preserve the native child-to-parent "
        "relation, not global exact equivalence. Standard InChI agreement does not establish a tautomer-pure reagent. "
        "Existing recipe references are retained; unqualified source observations do not acquire 9H specificity.",
    ),
    "Sorbitan_Monooleate": (
        "NCIT:C75654",
        LOCAL,
        "Sorbitan Monooleate",
        None,
        "Use a local unresolved material identity for the two CultureMech ATCC 416 recipe occurrences. "
        "Withdraw the label-only exact NCIT:C75654 grounding; exact molecular mapping to it or CHEBI:183688 "
        "is withheld pending material/product evidence. ATCC supplies only the generic name (1 g/L); "
        "JECFA describes a commercial mixture. Do not infer Tween 80/CHEBI:53426 from the conflicting FoodOn "
        "alias. Neither CAS 1338-43-8 nor CAS 9005-65-6 is assigned without product confirmation.",
    ),
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_tsv(path):
    lines = path.read_text().splitlines(keepends=True)
    reader = csv.DictReader((line for line in lines if not line.startswith("#")), delimiter="\t")
    return [line for line in lines if line.startswith("#")], reader.fieldnames, list(reader)


def tsv(comments, fields, rows):
    out = io.StringIO()
    out.writelines(comments)
    writer = csv.DictWriter(out, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--log", type=Path, required=True)
    args = parser.parse_args()
    records, log = {}, []
    for slug, (old, new, label, cas, note) in DECISIONS.items():
        path = ROOT / f"data/ingredients/mapped/{slug}.yaml"
        record = yaml.safe_load(path.read_text())
        if record["identifier"] != old or any(
            h.get("curator") == CURATOR for h in record["curation_history"]
        ):
            raise ValueError(f"{slug}: source changed or batch already applied")
        mapping = record["ontology_mapping"]
        if old != new:
            for evidence in mapping.get("evidence", []):
                evidence["notes"] = "SUPERSEDED by chemical-scope review: " + evidence.get(
                    "notes", ""
                )
        mapping.update(ontology_id=new, ontology_label=label, ontology_source=new.split(":")[0])
        if slug != "Xanthine":
            mapping["mapping_quality"] = "EXACT_MATCH"
        mapping.setdefault("evidence", []).append(
            {"evidence_type": "CURATOR_JUDGMENT", "source": EVIDENCE, "notes": note}
        )
        record["identifier"] = new
        record["notes"] = (record.get("notes", "") + "\n" + note).strip()
        if cas and slug != "Xanthine":
            props = record.setdefault("chemical_properties", {})
            if props.get("cas_rn") not in (None, cas):
                raise ValueError(f"{slug}: unexpected CAS")
            props["cas_rn"] = cas
            props["data_source"] = (
                props.get("data_source", "") + "; CAS verified in " + EVIDENCE
            ).lstrip("; ")
        elif not cas and (record.get("chemical_properties") or {}).get("cas_rn"):
            raise ValueError(f"{slug}: unexpected CAS requires new review")
        record_curation_event(
            record,
            curator=CURATOR,
            action="CORRECTED",
            changes=note,
            previous_status="MAPPED",
            new_status="MAPPED",
            llm_assisted=True,
            llm_model="gpt-6",
        )
        if errors := validate_ingredient(record):
            raise ValueError(f"{slug}: {errors}")
        records[slug] = record
        log.append(
            {
                "source_record": str(path.relative_to(ROOT)),
                "shape": "reviewed_chemical_scope",
                "before_yaml_sha256": sha(path),
                "change": f"{old} -> {new}; scope/CAS review",
                "verification": note,
            }
        )

    source = ROOT / "mappings/ingredient_mappings.sssom.tsv"
    comments, fields, rows = read_tsv(source)
    seen = Counter()
    for row in rows:
        slug = row["subject_id"].removeprefix("MIM:")
        if slug not in DECISIONS:
            continue
        old, new, label, cas, note = DECISIONS[slug]
        if row["object_id"] != old:
            raise ValueError(f"{slug}: unexpected mapping row")
        row.update(
            object_id=new,
            object_label=label,
            object_source=(
                "kgm:ingredient" if new == LOCAL else f"obo:{new.split(':')[0].lower()}.owl"
            ),
            mapping_justification="semapv:ManualMappingCuration",
            source=row["source"] + "|MIM:curator=" + CURATOR,
            mapping_date=DATE,
            comment=note,
            validation_method=f"manual:{CURATOR}|SCOPE_REVIEW|{DATE}",
        )
        if cas and slug != "Xanthine":
            row["other"] = "|".join(filter(None, [row["other"], "CAS:" + cas]))
        seen[slug] += 1
    if seen != Counter(dict.fromkeys(DECISIONS, 1)):
        raise ValueError(f"Unexpected row counts: {seen}")
    membership = ROOT / "mappings/culturemech_recipe_membership.tsv"
    mc, mf, members = read_tsv(membership)
    moved = []
    for row in members:
        if row["mim_identifier"] == "NCIT:C75654":
            moved.append(dict(row))
            row["mim_identifier"] = LOCAL
    evidence = json.loads(
        (
            ROOT
            / "reports/sssom_completion_20260921/mapping_review/sorbitan-recipe-occurrences.json"
        ).read_text()
    )
    expected = {item["recipe_id"] for item in evidence["occurrences"]}
    if expected != {"CultureMech:008837", "CultureMech:008839"}:
        raise ValueError("Sorbitan recipe evidence changed")
    if moved or any(row["mim_identifier"] == LOCAL for row in members):
        raise ValueError(
            "Membership baseline changed; review migration instead of filling the known gap"
        )
    added = [
        {"mim_identifier": LOCAL, "recipe_id": recipe, "occurrences": "1"}
        for recipe in sorted(expected)
    ]
    members.extend(added)
    members.sort(key=lambda row: (row["mim_identifier"], row["recipe_id"]))
    if args.apply:
        args.log.parent.mkdir(parents=True, exist_ok=True)
        args.log.with_suffix(".before.sssom.tsv").write_bytes(source.read_bytes())
        for entry, record in zip(log, records.values(), strict=True):
            path = ROOT / entry["source_record"]
            write_validated_ingredient(record, path)
            entry["after_yaml_sha256"] = sha(path)
        source.write_text(tsv(comments, fields, rows))
        membership.write_text(tsv(mc, mf, members))
        args.log.write_text(
            json.dumps({"records": log, "membership_added": added}, indent=2) + "\n"
        )
    print(
        json.dumps(
            {"applied": args.apply, "records": list(records), "membership_added": len(added)},
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
