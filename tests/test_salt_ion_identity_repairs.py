"""Regression coverage for salt records that used bare ion identities (#315)."""

from __future__ import annotations

import csv
import io
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parents[1]

REPAIRED = {
    "1-ethyl-3-methylimidazolium lysine": (
        "kgmicrobe.compound:1-ethyl-3-methylimidazolium_lysine",
        "CHEBI:63895",
    ),
    "Na-crotonate": ("kgmicrobe.compound:na-crotonate", "CHEBI:41131"),
    "Na2 alpha-ketoglutarate": (
        "kgmicrobe.compound:na2_alpha-ketoglutarate",
        "CHEBI:30915",
    ),
    "Tetramethyl ammonium": (
        "kgmicrobe.compound:tetramethyl_ammonium",
        "CHEBI:35273",
    ),
}

REJECTED_SYNONYMS = {
    "1-ethyl-3-methylimidazolium acetate": {
        "1-ethyl-3-methyl-1H-imidazol-3-ium",
        "1-ethyl-3-methylimidazolium lysine",
    },
    "1-ethyl-3-methylimidazolium lysine": {
        "1-ethyl-3-methyl-1H-imidazol-3-ium",
    },
    "Na-crotonate": {
        "(2E)-2-butenoate",
        "(2E)-but-2-enoate",
        "(E)-2-butenoate",
        "(E)-crotonate",
        "3-methylacrylate",
        "alpha-butenoate",
        "alpha-crotonate",
        "beta-methacrylate",
        "beta-methylacrylate",
        "crotonate",
        "trans-2-butenoate",
        "trans-crotonate",
    },
    "Na2 alpha-ketoglutarate": {
        "2-Oxoglutarate",
        "2-oxopentanedioate",
        "alpha-ketoglutarate",
        "α-Ketoglutarate",
    },
    "Tetramethyl ammonium": {
        "N,N,N-trimethylmethanaminium",
        "TETRAMETHYLAMMONIUM ION",
        "tetramethylammonium",
        "tetramethylazanium",
    },
    "Tetramethyl ammonium chloride": {
        "N,N,N-trimethylmethanaminium",
    },
}

EXPECTED_OTHER = {
    "1-ethyl-3-methylimidazolium lysine": "",
    "Na-crotonate": "Sodium crotonate",
    "Na2 alpha-ketoglutarate": "Na2 α-ketoglutarate",
    "Tetramethyl ammonium": "",
}


@pytest.fixture(scope="module")
def mapped_records() -> dict[str, dict]:
    data = yaml.safe_load(
        (REPO / "data" / "curated" / "mapped_ingredients.yaml").read_text(
            encoding="utf-8"
        )
    )
    return {record["preferred_term"]: record for record in data["ingredients"]}


@pytest.fixture(scope="module")
def sssom_rows() -> list[dict[str, str]]:
    text = (REPO / "mappings" / "ingredient_mappings.sssom.tsv").read_text(
        encoding="utf-8"
    )
    body = "\n".join(line for line in text.splitlines() if not line.startswith("#"))
    return list(csv.DictReader(io.StringIO(body), delimiter="\t"))


@pytest.fixture(scope="module")
def label_index_rows() -> list[dict[str, str]]:
    with (REPO / "docs" / "data" / "label_index.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        return list(csv.DictReader(handle))


def test_salt_named_records_keep_distinct_local_identities(
    mapped_records: dict[str, dict],
):
    for preferred_term, (identifier, parent) in REPAIRED.items():
        record = mapped_records[preferred_term]
        assert record["identifier"] == identifier
        if "kg_microbe_node_id" in record:
            assert record["kg_microbe_node_id"] == identifier

        ontology_mapping = record["ontology_mapping"]
        assert ontology_mapping["ontology_id"] == parent
        assert ontology_mapping["mapping_quality"] == "NARROW_MATCH"


def test_salt_named_subjects_have_parent_and_registry_sssom_rows(
    sssom_rows: list[dict[str, str]],
):
    by_label: dict[str, dict[str, dict[str, str]]] = {}
    for row in sssom_rows:
        by_label.setdefault(row["subject_label"], {})[row["object_id"]] = row

    for preferred_term, (identifier, parent) in REPAIRED.items():
        parent_row = by_label[preferred_term][parent]
        assert parent_row["predicate_id"] == "skos:narrowMatch"
        assert parent_row["other"] == EXPECTED_OTHER[preferred_term]

        registry_row = by_label[preferred_term][identifier]
        assert registry_row["predicate_id"] == "skos:exactMatch"
        assert registry_row["object_label"] == preferred_term
        assert registry_row["object_source"] == "kgm:compound"
        assert registry_row["other"] == EXPECTED_OTHER[preferred_term]


def test_wrong_ion_synonyms_are_retained_as_rejected_labels(
    mapped_records: dict[str, dict],
):
    for preferred_term, expected in REJECTED_SYNONYMS.items():
        rejected = {
            synonym["synonym_text"]
            for synonym in mapped_records[preferred_term].get("synonyms", [])
            if synonym.get("synonym_type") == "REJECTED_LABEL"
        }
        assert rejected >= expected


def test_rejected_ion_synonyms_are_not_published_through_other(
    sssom_rows: list[dict[str, str]],
):
    rejected = {
        preferred_term: {label.casefold() for label in labels}
        for preferred_term, labels in REJECTED_SYNONYMS.items()
    }

    for row in sssom_rows:
        row_rejected = rejected.get(row["subject_label"])
        if not row_rejected:
            continue
        published = {
            token.strip().casefold()
            for token in row["other"].split("|")
            if token.strip()
        }
        assert published.isdisjoint(row_rejected)


def test_rejected_ion_synonyms_are_not_published_through_label_index(
    label_index_rows: list[dict[str, str]],
):
    assert not [
        row
        for row in label_index_rows
        if row["label"].casefold() == "tetramethylammonium"
    ]


def test_sodium_crotonate_merge_preserved_deleted_source_provenance(
    mapped_records: dict[str, dict],
):
    changes = "\n".join(
        str(event.get("changes") or "")
        for event in mapped_records["Na-crotonate"].get("curation_history", [])
    )

    assert "source_id=mediadive.ingredient:2053" in changes
    assert "Edison literature identity review" in changes
    assert "sodium-crotonate preparation with no ontology CURIE proposed" in changes
