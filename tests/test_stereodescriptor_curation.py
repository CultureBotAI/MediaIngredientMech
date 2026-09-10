"""Regression coverage for lowercase D stereodescriptor repairs (#460)."""

from __future__ import annotations

import csv
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).parent.parent
CURATED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"

LOWERCASE_D_ARTIFACTS = {
    "3-beta-d-glucan": "3-beta-D-glucan",
    "4-methylumbelliferone Beta-d-glucuronide": (
        "4-methylumbelliferone Beta-D-glucuronide"
    ),
    "6-deoxy-d-galactose": "6-deoxy-D-galactose",
    "Beta-d-glucose": "Beta-D-glucose",
}


@pytest.fixture(scope="module")
def mapped_records() -> list[dict]:
    return yaml.safe_load(CURATED.read_text(encoding="utf-8"))["ingredients"]


@pytest.fixture(scope="module")
def sssom_rows() -> list[dict]:
    lines = [
        line
        for line in SSSOM.read_text(encoding="utf-8").splitlines()
        if not line.startswith("#")
    ]
    return list(csv.DictReader(lines, delimiter="\t"))


def test_lowercase_d_stereodescriptor_artifacts_are_not_live_labels(
    mapped_records: list[dict],
) -> None:
    live = [record for record in mapped_records if record.get("mapping_status") == "MAPPED"]

    preferred_terms = {record["preferred_term"] for record in live}
    assert not (set(LOWERCASE_D_ARTIFACTS) & preferred_terms)
    assert set(LOWERCASE_D_ARTIFACTS.values()).issubset(preferred_terms)

    synonyms = {
        synonym.get("synonym_text")
        for record in live
        for synonym in record.get("synonyms") or []
    }
    assert not (set(LOWERCASE_D_ARTIFACTS) & synonyms)


def test_sssom_uses_corrected_d_stereodescriptor_labels(sssom_rows: list[dict]) -> None:
    by_label = {
        row["subject_label"]: row
        for row in sssom_rows
        if row["subject_label"] in set(LOWERCASE_D_ARTIFACTS) | set(LOWERCASE_D_ARTIFACTS.values())
    }

    assert set(LOWERCASE_D_ARTIFACTS).isdisjoint(by_label)
    assert set(LOWERCASE_D_ARTIFACTS.values()).issubset(by_label)


def test_n_acetyl_d_glucosamine_is_not_mapped_to_peptidoglycan_residue(
    mapped_records: list[dict],
    sssom_rows: list[dict],
) -> None:
    records = [
        record
        for record in mapped_records
        if record.get("preferred_term") == "N-Acetyl-D-glucosamine"
    ]
    assert len(records) == 1
    record = records[0]

    assert record["identifier"] == "CHEBI:506227"
    assert record["kg_microbe_node_id"] == "CHEBI:506227"
    assert record["ontology_mapping"]["ontology_id"] == "CHEBI:506227"
    assert record["ontology_mapping"]["ontology_label"] == "N-acetyl-D-glucosamine"
    assert record["ontology_mapping"]["mapping_quality"] == "EXACT_MATCH"
    assert record["chemical_properties"]["cas_rn"] == "7512-17-6"
    assert record["chemical_properties"]["molecular_formula"] == "C8H15NO6"
    assert "Peptideglycan(N-acetyl-D-glucosamine)" not in {
        synonym.get("synonym_text") for synonym in record.get("synonyms") or []
    }

    sssom_rows = [
        row for row in sssom_rows if row["subject_id"] == "MIM:N-acetyl-d-glucosamine"
    ]
    assert len(sssom_rows) == 1
    assert sssom_rows[0]["object_id"] == "CHEBI:506227"
    assert sssom_rows[0]["other"].endswith("CAS:7512-17-6")
