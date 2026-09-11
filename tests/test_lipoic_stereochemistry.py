"""Regression coverage for the lipoic/thioctic stereochemistry merge (#454)."""

from __future__ import annotations

import csv
import io
import json
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parents[1]

OLD_IDENTIFIERS = {"CHEBI:30314", "CHEBI:43796"}

GENERIC_SOURCE_LABELS = {
    "Thioctic acid",
    "α-lipoic acid",
    "α--Lipoic acid",
    "D,L-6,8-Thioctic Acid",
}

STEREOSPECIFIC_LABELS = {
    "(+)-alpha-Lipoic acid",
    "(R)-(+)-Lipoate",
    "(R)-(+)-lipoic acid",
    "(R)-1,2-Dithiolane-3-pentanoic acid",
    "(R)-1,2-dithiolane-3-valeric acid",
    "(R)-6,8-thioctic acid",
    "(S)-(-)-lipoic acid",
    "(S)-1,2-dithiolane-3-pentanoic acid",
    "(S)-alpha-lipoic acid",
    "5-[(3R)-1,2-dithiolan-3-yl]pentanoic acid",
    "5-[(3S)-1,2-dithiolan-3-yl]pentanoic acid",
    "L-1,2-dithiolane 3-valeric acid",
    "L-6,8-thioctic acid",
    "L-6-thioctic acid",
    "R-(+)-Lipoic acid",
    "R-LA",
    "RLA",
    "S-LA",
    "SLA",
    "Thioctic acid d-form",
    "thioctic acid l-form",
}


@pytest.fixture(scope="module")
def mapped_records() -> dict[str, dict]:
    data = yaml.safe_load(
        (REPO / "data" / "curated" / "mapped_ingredients.yaml").read_text(encoding="utf-8")
    )
    return {record["preferred_term"]: record for record in data["ingredients"]}


@pytest.fixture(scope="module")
def sssom_rows() -> list[dict[str, str]]:
    text = (REPO / "mappings" / "ingredient_mappings.sssom.tsv").read_text(encoding="utf-8")
    body = "\n".join(line for line in text.splitlines() if not line.startswith("#"))
    return list(csv.DictReader(io.StringIO(body), delimiter="\t"))


@pytest.fixture(scope="module")
def label_index_rows() -> list[dict[str, str]]:
    with (REPO / "docs" / "data" / "label_index.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        return list(csv.DictReader(handle))


@pytest.fixture(scope="module")
def browser_records() -> dict[str, dict]:
    data = json.loads((REPO / "docs" / "data" / "ingredients.json").read_text())
    return {record["preferred_term"]: record for record in data["ingredients"]}


@pytest.fixture(scope="module")
def membership_rows() -> list[dict[str, str]]:
    with (REPO / "mappings" / "culturemech_recipe_membership.tsv").open(
        encoding="utf-8", newline=""
    ) as handle:
        rows = [line for line in handle if not line.startswith("#")]
    return list(csv.DictReader(rows, delimiter="\t"))


def test_lipoic_family_collapses_to_generic_lipoic_acid(mapped_records: dict[str, dict]) -> None:
    record = mapped_records["(DL)-alpha-Lipoic acid"]

    assert record["identifier"] == "CHEBI:16494"
    assert record.get("kg_microbe_node_id") == "CHEBI:16494"
    assert record["mapping_status"] == "MAPPED"
    assert record["occurrence_statistics"] == {
        "total_occurrences": 1748,
        "media_count": 1747,
    }

    mapping = record["ontology_mapping"]
    assert mapping["ontology_id"] == "CHEBI:16494"
    assert mapping["ontology_label"] == "lipoic acid"
    assert mapping["mapping_quality"] == "EXACT_MATCH"


def test_unsupported_lipoic_enantiomer_records_are_tombstoned(
    mapped_records: dict[str, dict],
) -> None:
    for term in ("Thioctic acid", "α-lipoic acid"):
        record = mapped_records[term]

        assert record["identifier"] == "CHEBI:16494"
        assert record["mapping_status"] == "REJECTED"
        assert record["representative"] == "CHEBI:16494"
        assert record["occurrence_statistics"] == {
            "total_occurrences": 0,
            "media_count": 0,
        }
        assert record["ontology_mapping"]["ontology_id"] == "CHEBI:16494"
        assert record["chemical_properties"] == {}


def test_lipoic_tombstones_reject_stereospecific_synonyms(
    mapped_records: dict[str, dict],
) -> None:
    for term in ("Thioctic acid", "α-lipoic acid"):
        synonyms = {
            synonym["synonym_text"]: synonym["synonym_type"]
            for synonym in mapped_records[term].get("synonyms", [])
        }
        rejected_labels = STEREOSPECIFIC_LABELS & set(synonyms)

        assert rejected_labels
        for label in rejected_labels:
            assert synonyms[label] == "REJECTED_LABEL"


def test_surviving_lipoic_record_carries_only_generic_source_labels(
    mapped_records: dict[str, dict],
) -> None:
    synonyms = {
        synonym["synonym_text"]: synonym["synonym_type"]
        for synonym in mapped_records["(DL)-alpha-Lipoic acid"].get("synonyms", [])
    }

    for label in GENERIC_SOURCE_LABELS:
        assert synonyms[label] == "RAW_TEXT"

    for label in STEREOSPECIFIC_LABELS:
        assert label not in synonyms


def test_only_surviving_lipoic_subject_publishes_to_sssom(
    sssom_rows: list[dict[str, str]],
) -> None:
    by_label = {row["subject_label"]: row for row in sssom_rows}

    row = by_label["(DL)-alpha-Lipoic acid"]
    assert row["object_id"] == "CHEBI:16494"
    assert row["object_label"] == "lipoic acid"
    assert row["predicate_id"] == "skos:exactMatch"
    assert "Thioctic acid" in row["other"].split("|")
    assert "α-lipoic acid" in row["other"].split("|")
    assert "D,L-6,8-Thioctic Acid" in row["other"].split("|")

    assert "Thioctic acid" not in by_label
    assert "α-lipoic acid" not in by_label
    assert not OLD_IDENTIFIERS & {row["object_id"] for row in sssom_rows}


def test_lipoic_label_index_resolves_only_to_generic_lipoic_acid(
    label_index_rows: list[dict[str, str]],
) -> None:
    rows = [
        row
        for row in label_index_rows
        if row["mapping_status"] == "MAPPED"
        and row["label"] in GENERIC_SOURCE_LABELS | STEREOSPECIFIC_LABELS
    ]
    by_label = {row["label"]: row for row in rows}

    for label in GENERIC_SOURCE_LABELS:
        assert by_label[label]["identifier"] == "CHEBI:16494"
        assert by_label[label]["ontology_id"] == "CHEBI:16494"

    for label in STEREOSPECIFIC_LABELS:
        assert label not in by_label


def test_lipoic_stereospecific_labels_are_not_searchable(
    label_index_rows: list[dict[str, str]],
) -> None:
    indexed_labels = {row["label"] for row in label_index_rows}

    assert not STEREOSPECIFIC_LABELS & indexed_labels


def test_lipoic_browser_tombstones_do_not_publish_stereospecific_labels(
    browser_records: dict[str, dict],
) -> None:
    for term in ("Thioctic acid", "α-lipoic acid"):
        record = browser_records[term]

        assert not STEREOSPECIFIC_LABELS & set(record["synonyms"])

        searchable = f" {record['searchable'].casefold()} "
        for label in STEREOSPECIFIC_LABELS:
            assert f" {label.casefold()} " not in searchable


def test_lipoic_memberships_are_collapsed_to_generic_lipoic_acid(
    membership_rows: list[dict[str, str]],
) -> None:
    lipoic_rows = [
        row for row in membership_rows if row["mim_identifier"] == "CHEBI:16494"
    ]
    counts: dict[str, int] = {}
    for row in membership_rows:
        counts[row["mim_identifier"]] = counts.get(row["mim_identifier"], 0) + int(
            row["occurrences"]
        )

    assert len(lipoic_rows) == 1747
    assert counts["CHEBI:16494"] == 1748
    assert not OLD_IDENTIFIERS & set(counts)


def test_wolfe_vitamin_components_use_generic_lipoic_acid(
    mapped_records: dict[str, dict],
) -> None:
    for term in ("ATCC Wolfe's vitamin mix", "Wolfe's vitamin mix"):
        components = mapped_records[term]["components"]
        thioctic = [
            component
            for component in components
            if component["component_name"] == "Thioctic acid"
        ]

        assert thioctic == [
            {
                "component_name": "Thioctic acid",
                "component_id": "CHEBI:16494",
                "reference_scope": "MIM_CATALOG",
                "concentration_value": "5.0",
                "concentration_unit": "MG_PER_L",
            }
        ]
