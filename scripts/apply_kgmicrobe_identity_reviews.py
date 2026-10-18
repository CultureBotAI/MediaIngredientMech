#!/usr/bin/env python3
"""Apply twelve source-reviewed ingredient identity dispositions (#762, #753).

Dry-run by default. Complete before-images and exact source hashes bound the
batch; fresh row reviews remain necessary after its approval-free receipt.
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

EVIDENCE = "reports/sssom_completion_20260921/mapping_review/identity-review-20260924"
CURATOR = "kgmicrobe_identity_review_20260924"
LOCAL = "kgmicrobe.ingredient:lysozyme"
DECISIONS = {
    "Acriflavine": (
        "NCIT:C76253",
        "65589-70-0",
        "FDA GSRS 1T3A50395T establishes the mixture and NCIT identity. Use its PRIMARY CAS 65589-70-0. The original 8048-52-0 is SUPERSEDED in that FDA record; retain source-qualified history, not an active CAS synonym or exact mapping. No global CAS withdrawal is asserted.",
    ),
    "Anabasine_Hydrochloride": (
        "NCIT:C216370",
        "53912-89-3",
        "Source CAS, NCIT, FDA W4917XZ12G and PubChem 3041330 agree on the stereospecific monohydrochloride. Preserve the existing stereochemical InChI and align its SMILES; no free base or other salt is substituted.",
    ),
    "Bovine_Serum_Albumin": (
        "NCIT:C85253",
        "9048-46-8",
        "Review the generic bovine albumin ingredient at NCIT:C85253. FDA qualifies CAS 9048-46-8 as GENERIC (FAMILY). Retain source Sigma A7030 and other recipe-specific fraction V/products as supplied forms, not exact synonyms. Preserve all seven original recipe memberships and their preparation qualifiers.",
    ),
    "Cotarnine_Chloride": (
        "NCIT:C79997",
        "10018-19-6",
        "Source CAS, NCIT and FDA 03F6B8N3QN agree on the 1:1 cotarninium chloride salt. Preserve that salt, not free cotarnine or its isolated cation.",
    ),
    "Locust_Bean_Gum": (
        "FOODON:03413132",
        "9000-40-2",
        "Source Sigma G0753, JECFA INS 410 and FoodOn identify the same generic seed-derived locust/carob gum. Retain the supplier and original autoclaved qualifier in supplied_form notes; it is not an exact synonym or evidence for clarified gum.",
    ),
    "Lysozyme": (
        LOCAL,
        None,
        "Preserve unresolved source material locally. The original CultureBotHT row provides no supplier/catalog or preparation evidence. Reject invalid CAS 2650-88-3 from active identifiers, properties and annotations. Neither 12650-88-3 nor exact FOODON:03413135 identity is assigned without original material evidence.",
    ),
    "Pretomanid": (
        "NCIT:C166606",
        "187235-37-6",
        "Original name/CAS, NCIT, FDA 2XOI31YC4N and PubChem 456199 establish the S identity. Existing InChI agrees exactly; align the previously unstereospecific SMILES.",
    ),
    "Sodium_Adipate": (
        "FOODON:03413240",
        "7486-38-6",
        "Original CAS, FoodOn INS 356 and JECFA identify disodium adipate. PubChem 24073 agrees with MIM formula and InChI containing two sodium ions. No monosodium form or hydrate is inferred.",
    ),
    "Sunflower_Oil": (
        "NCIT:C1241",
        "8001-21-6",
        "Original generic name/CAS agrees with NCIT and FDA 3W1JG795YI for sunflower seed oil. The source has no processing/grade qualifier; no hydrogenated, refined or high-oleic preparation is inferred.",
    ),
    "Sutezolid": (
        "NCIT:C152482",
        "168828-58-8",
        "Original CAS, NCIT, FDA 3A71182L8P and PubChem 465951 establish the S identity. Existing InChI agrees exactly; align the previously unstereospecific SMILES.",
    ),
    "Tara_Gum": (
        "FOODON:03413299",
        "39300-88-4",
        "Original Biosynth YT58656 product/CAS, JECFA INS 417 and FoodOn agree on tara seed-endosperm gum. Retain product provenance; no viscosity grade is inferred.",
    ),
    "Zymosan": (
        "NCIT:C183132",
        "9010-72-4",
        "Original name/CAS, NCIT and MeSH D015054 agree on the named yeast-wall zymosan preparation. This does not equate arbitrary purified beta-glucan or a single molecule with zymosan.",
    ),
}
SUPPLIED = {
    "Bovine_Serum_Albumin": [
        {
            "name": "Bovine Serum Albumin",
            "cas_rn": "9048-46-8",
            "supplier": "Sigma-Aldrich",
            "catalog_number": "A7030",
            "form": "lyophilized powder; heat shock fraction; protease free; fatty acid free; essentially globulin free",
            "notes": "Original CultureBotHT product; supplier page confirms CAS and preparation. Source-specific product, not a restriction on all seven recipes. See "
            + EVIDENCE
            + "/README.md.",
        },
        {
            "name": "Bovine serum albumin fraction V",
            "supplier": "Sigma-Aldrich",
            "catalog_number": "A9647",
            "notes": "Explicit product in CultureMech:015191 preparation note; preserved from the original recipe, not assigned to other recipes. See "
            + EVIDENCE
            + "/bsa-recipe-occurrences.json.",
        },
        {
            "name": "BSA solution",
            "supplier": "Sigma-Aldrich",
            "catalog_number": "A7409",
            "form": "solution",
            "notes": "Alternative product explicitly named in CultureMech:015191; no concentration or independent product CAS inferred. See "
            + EVIDENCE
            + "/bsa-recipe-occurrences.json.",
        },
    ],
    "Locust_Bean_Gum": [
        {
            "name": "Locust bean gum",
            "cas_rn": "9000-40-2",
            "supplier": "Sigma-Aldrich",
            "catalog_number": "G0753",
            "form": "Ceratonia siliqua seed-derived powder",
            "notes": "Original CultureBotHT synonym field says 'Locust bean gum; autoclaved'. Autoclaved remains a preparation qualifier, not an exact synonym. Source does not specify clarified gum. See "
            + EVIDENCE
            + "/README.md.",
        }
    ],
    "Tara_Gum": [
        {
            "name": "Tara gum",
            "cas_rn": "39300-88-4",
            "supplier": "Biosynth",
            "catalog_number": "YT58656",
            "notes": "Original CultureBotHT catalog reference confirmed by supplier. No particular viscosity grade is assigned. See "
            + EVIDENCE
            + "/README.md.",
        }
    ],
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_tsv(path):
    lines = path.read_text().splitlines(keepends=True)
    reader = csv.DictReader((s for s in lines if not s.startswith("#")), delimiter="\t")
    return [s for s in lines if s.startswith("#")], reader.fieldnames, list(reader)


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
    parser.add_argument("--log", required=True, type=Path)
    args = parser.parse_args()
    before = json.loads((ROOT / EVIDENCE / "source-records.json").read_text())["before_records"]
    structures = {
        p["CID"]: p
        for p in json.loads((ROOT / EVIDENCE / "pubchem-structures.json").read_text())["properties"]
    }
    records, log, moved_ids = {}, [], {}
    for slug, (target, cas, note) in DECISIONS.items():
        path = ROOT / before[slug]["path"]
        if sha(path) != before[slug]["sha256"]:
            raise ValueError(f"{slug}: source changed or batch already applied")
        record = yaml.safe_load(path.read_text())
        old = record["identifier"]
        mapping = record["ontology_mapping"]
        if mapping["mapping_quality"] != "NARROW_MATCH":
            raise ValueError(f"{slug}: unexpected source grade")
        for item in mapping.get("evidence", []):
            item["notes"] = (
                "Historical source assertion; grounding superseded by #762/#753 review: "
                + item.get("notes", "")
            )
        mapping.update(
            ontology_id=target,
            ontology_label=(
                record["preferred_term"] if target == LOCAL else mapping["ontology_label"]
            ),
            ontology_source=target.split(":")[0],
            mapping_quality="EXACT_MATCH",
        )
        mapping["evidence"].append(
            {"evidence_type": "CURATOR_JUDGMENT", "source": EVIDENCE + "/README.md", "notes": note}
        )
        record["identifier"] = target
        props = record["chemical_properties"]
        if cas:
            props["cas_rn"] = cas
        else:
            props.pop("cas_rn", None)
        props["data_source"] = (
            EVIDENCE + "/README.md; original source claim preserved in source-records.json"
        )
        props["retrieval_date"] = "2026-09-24T00:00:00Z"
        if props.get("pubchem_cid") in structures:
            authority = structures[props["pubchem_cid"]]
            if (
                props["inchi"] != authority["InChI"]
                or props["molecular_formula"] != authority["MolecularFormula"]
            ):
                raise ValueError(f"{slug}: structure differs from reviewed identity")
            props["smiles"] = authority["SMILES"]
        if slug in SUPPLIED:
            if record.get("supplied_form"):
                raise ValueError(f"{slug}: unexpected supplied forms")
            record["supplied_form"] = SUPPLIED[slug]
        record["notes"] = (record.get("notes", "") + "\n" + note).strip()
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
        moved_ids[old] = target
        log.append(
            {
                "source_record": str(path.relative_to(ROOT)),
                "shape": "reviewed_ingredient_identity",
                "before_yaml_sha256": sha(path),
                "change": f"{old} -> {target}; reviewed scope, CAS and supplied forms",
                "verification": note,
            }
        )

    source = ROOT / "mappings/ingredient_mappings.sssom.tsv"
    comments, fields, original = read_tsv(source)
    for key in ("mapping_date", "mapping_set_version"):
        comments = [
            f'# {key}: "2026-09-24"\n' if line.startswith(f"# {key}:") else line
            for line in comments
        ]
    rows, seen = [], Counter()
    for row in original:
        slug = row["subject_id"].removeprefix("MIM:")
        if slug not in DECISIONS:
            rows.append(row)
            continue
        target, _, note = DECISIONS[slug]
        if row["object_id"] != target:
            continue
        row.update(
            predicate_id="skos:exactMatch",
            object_label=records[slug]["ontology_mapping"]["ontology_label"],
            object_source=(
                "kgm:ingredient"
                if target == LOCAL
                else "obo:" + target.split(":")[0].lower() + ".owl"
            ),
            mapping_justification="semapv:ManualMappingCuration",
            source=row["source"] + "|MIM:curator=" + CURATOR,
            mapping_date="2026-09-24",
            confidence="0.99",
            comment=note,
            other="",
            validation_method="manual:" + CURATOR + "|IDENTITY_REVIEW|2026-09-24",
        )
        rows.append(row)
        seen[slug] += 1
    if seen != Counter(dict.fromkeys(DECISIONS, 1)):
        raise ValueError(f"Unexpected selected mapping rows: {seen}")
    membership = ROOT / "mappings/culturemech_recipe_membership.tsv"
    mc, mf, members = read_tsv(membership)
    moved = []
    for row in members:
        if row["mim_identifier"] in moved_ids:
            moved.append(dict(row))
            row["mim_identifier"] = moved_ids[row["mim_identifier"]]
    expected = {
        r["recipe_id"]
        for r in json.loads((ROOT / EVIDENCE / "bsa-recipe-occurrences.json").read_text())[
            "occurrences"
        ]
    }
    if (
        len(moved) != 7
        or {r["recipe_id"] for r in moved} != expected
        or {r["mim_identifier"] for r in moved} != {"cas:9048-46-8"}
    ):
        raise ValueError("Recipe membership baseline changed")
    members.sort(key=lambda r: (r["mim_identifier"], r["recipe_id"]))
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
            json.dumps({"records": log, "membership_before": moved}, indent=2) + "\n"
        )
    print(
        json.dumps(
            {
                "applied": args.apply,
                "records": list(records),
                "source_rows": len(rows),
                "removed_rows": len(original) - len(rows),
                "membership_moved": len(moved),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
