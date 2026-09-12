"""Regression coverage for element source labels grounded to atom terms (#631)."""

from __future__ import annotations

import csv
import io
from pathlib import Path

import pytest
import yaml

from mediaingredientmech.utils.culturemech_occurrences import (
    mim_identifier_for_occurrence,
)

REPO = Path(__file__).resolve().parents[1]

ATOM_IDENTIFIERS = {
    "CHEBI:22984",
    "CHEBI:25107",
    "CHEBI:18248",
    "CHEBI:28694",
    "CHEBI:28685",
}

DROP_SUBJECTS = {
    "MIM:Calcium",
    "MIM:Magnesium",
    "MIM:Iron_Powder",
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
    with (REPO / "docs" / "data" / "label_index.csv").open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


@pytest.fixture(scope="module")
def membership_rows() -> list[dict[str, str]]:
    with (REPO / "mappings" / "culturemech_recipe_membership.tsv").open(
        encoding="utf-8", newline=""
    ) as handle:
        rows = [line for line in handle if not line.startswith("#")]
    return list(csv.DictReader(rows, delimiter="\t"))


def test_source_element_labels_no_longer_map_to_atom_terms(
    mapped_records: dict[str, dict],
) -> None:
    expected = {
        "Calcium(2+)": ("CHEBI:29108", "calcium(2+)", 2),
        "Magnesium(2+)": ("CHEBI:18420", "magnesium(2+)", 3),
        "Iron": ("CHEBI:82664", "iron(0)", 7),
        "Copper": ("kgmicrobe.compound:copper", "Copper", 2),
        "Molybdenum": ("kgmicrobe.compound:molybdenum", "Molybdenum", 2),
    }

    for preferred_term, (identifier, ontology_label, occurrences) in expected.items():
        record = mapped_records[preferred_term]

        assert record["mapping_status"] == "MAPPED"
        assert record["identifier"] == identifier
        assert record["ontology_mapping"]["ontology_id"] == identifier
        assert record["ontology_mapping"]["ontology_label"] == ontology_label
        assert record["occurrence_statistics"]["total_occurrences"] == occurrences
        assert record["occurrence_statistics"]["media_count"] == occurrences


def test_atom_source_records_are_tombstoned(mapped_records: dict[str, dict]) -> None:
    for preferred_term, representative in {
        "Calcium": "CHEBI:29108",
        "Magnesium": "CHEBI:18420",
        "Iron powder": "CHEBI:82664",
    }.items():
        record = mapped_records[preferred_term]

        assert record["identifier"] == representative
        assert record["mapping_status"] == "REJECTED"
        assert record["representative"] == representative
        assert record["occurrence_statistics"] == {
            "total_occurrences": 0,
            "media_count": 0,
        }


def test_atom_only_iron_synonyms_are_rejected(mapped_records: dict[str, dict]) -> None:
    synonyms = {
        synonym["synonym_text"]: synonym["synonym_type"]
        for synonym in mapped_records["Iron"].get("synonyms", [])
    }

    for text in ("26Fe", "Eisen", "fer", "ferrum", "hierro", "iron atom"):
        assert synonyms[text] == "REJECTED_LABEL"

    for text in ("Iron powder", "Fe(0)", "Fen", "Iron metal", "iron dust"):
        assert synonyms[text] == "RAW_TEXT"


def test_final_sssom_no_longer_publishes_atom_targets(
    sssom_rows: list[dict[str, str]],
) -> None:
    by_subject = {row["subject_id"]: row for row in sssom_rows}

    assert by_subject["MIM:Calcium~282~29"]["object_id"] == "CHEBI:29108"
    assert by_subject["MIM:Calcium~282~29"]["other"] == "Calcium"
    assert by_subject["MIM:Magnesium~282~29"]["object_id"] == "CHEBI:18420"
    assert by_subject["MIM:Magnesium~282~29"]["other"] == "Magnesium"
    assert by_subject["MIM:Iron"]["object_id"] == "CHEBI:82664"
    assert by_subject["MIM:Copper"]["object_id"] == "kgmicrobe.compound:copper"
    assert by_subject["MIM:Copper"]["object_source"] == "kgm:compound"
    assert by_subject["MIM:Molybdenum"]["object_id"] == ("kgmicrobe.compound:molybdenum")
    assert by_subject["MIM:Molybdenum"]["object_source"] == "kgm:compound"

    assert not DROP_SUBJECTS & set(by_subject)
    assert not ATOM_IDENTIFIERS & {row["object_id"] for row in sssom_rows}


def test_label_exports_skip_atom_only_surfaces(
    label_index_rows: list[dict[str, str]],
) -> None:
    by_label: dict[str, set[tuple[str, str]]] = {}
    for row in label_index_rows:
        by_label.setdefault(row["label"].casefold(), set()).add(
            (row["identifier"], row["ontology_id"])
        )

    assert by_label["calcium"] == {("CHEBI:29108", "CHEBI:29108")}
    assert by_label["magnesium"] == {("CHEBI:18420", "CHEBI:18420")}
    assert by_label["iron"] == {("CHEBI:82664", "CHEBI:82664")}
    assert by_label["iron powder"] == {("CHEBI:82664", "CHEBI:82664")}

    for label in ("26Fe", "iron atom"):
        assert label.casefold() not in by_label


def test_culturemech_memberships_move_to_non_atom_identities(
    membership_rows: list[dict[str, str]],
) -> None:
    by_identifier: dict[str, set[str]] = {}
    for row in membership_rows:
        by_identifier.setdefault(row["mim_identifier"], set()).add(row["recipe_id"])

    assert ATOM_IDENTIFIERS.isdisjoint(by_identifier)
    assert {
        "CultureMech:003018",
        "CultureMech:013532",
    } <= by_identifier["CHEBI:82664"]


@pytest.mark.parametrize(
    ("preferred_term", "expected"),
    [
        ("Calcium", "CHEBI:29108"),
        ("Copper", "kgmicrobe.compound:copper"),
        ("Iron", "CHEBI:82664"),
        ("Magnesium", "CHEBI:18420"),
        ("Molybdenum", "kgmicrobe.compound:molybdenum"),
    ],
)
def test_culturemech_source_labels_route_to_repaired_identities(
    preferred_term: str,
    expected: str,
) -> None:
    assert (
        mim_identifier_for_occurrence(
            {"preferred_term": preferred_term, "resolved_identifier": "CHEBI:atom"}
        )
        == expected
    )
