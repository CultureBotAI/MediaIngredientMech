"""Regression coverage for the sulfur atom/polysulfur split (#368)."""

from __future__ import annotations

import csv
import io
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parents[1]

OLD_IDENTIFIERS = {
    "CHEBI:26833",
    "CHEBI:17909",
    "kgmicrobe.compound:sulfur_powder",
}

REJECTED = {
    "16S",
    "polysulfur",
    "sulfur atom",
    "sulfur, homopolymer",
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


def test_sulfur_uses_elemental_sulfur_not_atom_or_polysulfur(mapped_records):
    record = mapped_records["Sulfur"]

    assert record["identifier"] == "CHEBI:33403"
    assert record.get("kg_microbe_node_id") == "CHEBI:33403"
    assert record["mapping_status"] == "MAPPED"
    assert record["occurrence_statistics"] == {
        "total_occurrences": 477,
        "media_count": 477,
    }
    assert record.get("chemical_properties") == {}

    mapping = record["ontology_mapping"]
    assert mapping["ontology_id"] == "CHEBI:33403"
    assert mapping["ontology_label"] == "elemental sulfur"
    assert mapping["mapping_quality"] == "EXACT_MATCH"


def test_duplicate_sulfur_records_are_tombstoned(mapped_records):
    for term in ("Sulphur", "Sulfur (powder)"):
        record = mapped_records[term]

        assert record["identifier"] == "CHEBI:33403"
        assert record["mapping_status"] == "REJECTED"
        assert record["representative"] == "CHEBI:33403"
        assert record["occurrence_statistics"] == {
            "total_occurrences": 0,
            "media_count": 0,
        }
        assert record["ontology_mapping"]["ontology_id"] == "CHEBI:33403"


def test_sulfur_carries_source_labels_and_rejects_wrong_term_labels(
    mapped_records,
):
    synonyms = {
        synonym["synonym_text"]: synonym["synonym_type"]
        for synonym in mapped_records["Sulfur"].get("synonyms", [])
    }

    for text in (
        "Sulphur",
        "Sulfur (powder)",
        "Sulfur powder",
        "Elemental sulphur",
        "Sulfur, precipitated",
        "Sulfur, powder",
        "Sulfur, powdered",
    ):
        assert text in synonyms
        assert synonyms[text] != "REJECTED_LABEL"

    for text in REJECTED:
        assert synonyms[text] == "REJECTED_LABEL"


def test_only_surviving_sulfur_subject_publishes_to_sssom(sssom_rows):
    by_label = {row["subject_label"]: row for row in sssom_rows}

    row = by_label["Sulfur"]
    assert row["object_id"] == "CHEBI:33403"
    assert row["object_label"] == "elemental sulfur"
    assert row["predicate_id"] == "skos:exactMatch"
    assert row["comment"] == (
        "Corrected from sulfur atom to weighable elemental sulfur "
        "and merged spelling/form duplicates (#368)."
    )

    assert "Sulphur" not in by_label
    assert "Sulfur (powder)" not in by_label
    assert not OLD_IDENTIFIERS & {row["object_id"] for row in sssom_rows}


def test_rejected_sulfur_labels_do_not_publish(label_index_rows, sssom_rows):
    labels = {row["label"].casefold() for row in label_index_rows}
    sssom_other = {
        token.strip().casefold()
        for row in sssom_rows
        for token in row["other"].split("|")
        if token.strip()
    }

    assert all(label.casefold() not in labels for label in REJECTED)
    assert all(label.casefold() not in sssom_other for label in REJECTED)


def test_sulfur_label_index_resolves_only_to_elemental_sulfur(label_index_rows):
    sulfur_labels = {
        "sulfur",
        "sulphur",
        "sulfur (powder)",
        "sulfur powder",
        "sulfur, powder",
        "sulfur, powdered",
    }
    rows = [row for row in label_index_rows if row["label"].casefold() in sulfur_labels]

    assert {row["identifier"] for row in rows} == {"CHEBI:33403"}
    assert {row["ontology_id"] for row in rows} == {"CHEBI:33403"}


def test_sulfur_memberships_are_collapsed_to_elemental_sulfur(membership_rows):
    counts: dict[str, int] = {}
    for row in membership_rows:
        counts[row["mim_identifier"]] = counts.get(row["mim_identifier"], 0) + int(
            row["occurrences"]
        )

    assert counts["CHEBI:33403"] == 477
    assert not OLD_IDENTIFIERS & set(counts)


def test_yeast_extract_sulfur_component_uses_elemental_sulfur(mapped_records):
    components = mapped_records["Yeast Extract + Sulfur"]["components"]
    sulfur = [component for component in components if component["component_name"] == "sulfur"]

    assert sulfur == [
        {
            "component_name": "sulfur",
            "component_id": "CHEBI:33403",
            "reference_scope": "MIM_CATALOG",
            "source": "microbedecoder research decomposition (#213/#308)",
        }
    ]
