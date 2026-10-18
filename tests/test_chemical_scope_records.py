"""Corpus regressions for the reviewed KG-Microbe scope corrections."""

import csv
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_scoped_identities_and_cas_do_not_collapse():
    expected = {
        "Polymyxin_B": ("NCIT:C61894", "1404-26-8"),
        "Rifamycin": ("CHEBI:26580", None),
        "Rifamycin_Sv": ("CHEBI:29673", "6998-60-3"),
        "Xanthine": ("CHEBI:17712", "69-89-6"),
        "Sorbitan_Monooleate": ("kgmicrobe.ingredient:sorbitan_monooleate", None),
    }
    for slug, (target, cas) in expected.items():
        record = yaml.safe_load((ROOT / f"data/ingredients/mapped/{slug}.yaml").read_text())
        assert record["identifier"] == record["ontology_mapping"]["ontology_id"] == target
        assert (record.get("chemical_properties") or {}).get("cas_rn") == cas
    evidence = (
        ROOT / "reports/sssom_completion_20260921/mapping_review/rifamycin-source-occurrences.json"
    )
    assert len(json.loads(evidence.read_text())["occurrences"]) == 3


def test_sorbitan_occurrences_remain_local_without_molecular_equivalence():
    local = "kgmicrobe.ingredient:sorbitan_monooleate"
    with (ROOT / "mappings/culturemech_recipe_membership.tsv").open() as handle:
        members = [
            row
            for row in csv.DictReader(
                (line for line in handle if not line.startswith("#")), delimiter="\t"
            )
            if row["mim_identifier"] == local
        ]
    assert {(row["recipe_id"], row["occurrences"]) for row in members} == {
        ("CultureMech:008837", "1"),
        ("CultureMech:008839", "1"),
    }
    with (ROOT / "mappings/ingredient_mappings.sssom.tsv").open() as handle:
        mappings = [
            row
            for row in csv.DictReader(
                (line for line in handle if not line.startswith("#")), delimiter="\t"
            )
            if row["subject_id"] == "MIM:Sorbitan_Monooleate"
        ]
    assert len(mappings) == 1
    assert mappings[0]["object_id"] == local
    assert mappings[0]["other"] == ""
