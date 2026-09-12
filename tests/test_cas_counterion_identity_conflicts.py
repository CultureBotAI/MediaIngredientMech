"""Regression coverage for the CAS-selected salt/counterion repairs (#455)."""

from __future__ import annotations

import csv
import io
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parents[1]

CAS_REGROUNDINGS = {
    "Glycyrrhizic Acid, Ammonium Salt": (
        "cas:53956-04-0",
        "CHEBI:15939",
        "C42H65NO16",
        62074,
    ),
    "Dimethylsulfoniopropionate hydrochloride": (
        "cas:4337-33-1",
        "CHEBI:16457",
        "C5H11ClO2S",
        5316899,
    ),
    "N-lauroylsarcosine sodium salt": (
        "cas:137-16-6",
        "CHEBI:183705",
        "C15H28NNaO3",
        23668817,
    ),
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


def _other_tokens(row: dict[str, str]) -> set[str]:
    return {token.strip().casefold() for token in row["other"].split("|") if token.strip()}


def test_salt_forms_have_distinct_cas_identities(mapped_records: dict[str, dict]):
    for label, (identifier, parent, formula, pubchem_cid) in CAS_REGROUNDINGS.items():
        record = mapped_records[label]

        assert record["identifier"] == identifier
        assert record["ontology_mapping"]["ontology_id"] == parent
        assert record["ontology_mapping"]["mapping_quality"] == "NARROW_MATCH"
        assert record["chemical_properties"]["molecular_formula"] == formula
        assert record["chemical_properties"]["pubchem_cid"] == pubchem_cid


def test_salt_forms_publish_parent_cas_and_kgm_identity_rows(
    sssom_rows: list[dict[str, str]],
):
    by_label: dict[str, dict[str, dict[str, str]]] = {}
    for row in sssom_rows:
        by_label.setdefault(row["subject_label"], {})[row["object_id"]] = row

    for label, (identifier, parent, _, _) in CAS_REGROUNDINGS.items():
        parent_row = by_label[label][parent]
        assert parent_row["predicate_id"] == "skos:narrowMatch"
        assert not any(token.startswith("cas:") for token in _other_tokens(parent_row))

        cas_row = by_label[label][identifier]
        assert cas_row["predicate_id"] == "skos:exactMatch"
        assert cas_row["object_source"] == "registry:cas"
        assert identifier in _other_tokens(cas_row)

        subject_slug = parent_row["subject_id"].removeprefix("MIM:")
        kgm_row = by_label[label][f"kgmicrobe.compound:{subject_slug.lower()}"]
        assert kgm_row["predicate_id"] == "skos:exactMatch"
        assert kgm_row["object_source"] == "kgm:compound"
        assert identifier in _other_tokens(kgm_row)


@pytest.mark.parametrize(
    ("label", "old_curie"),
    [
        ("Glycyrrhizic Acid, Ammonium Salt", "CHEBI:15939"),
        ("Dimethylsulfoniopropionate hydrochloride", "CHEBI:16457"),
        ("N-lauroylsarcosine sodium salt", "CHEBI:183704"),
        ("Colistin sulfate salt", "CHEBI:37943"),
    ],
)
def test_bad_exact_chEBI_rows_are_gone(
    sssom_rows: list[dict[str, str]],
    label: str,
    old_curie: str,
):
    assert not [
        row
        for row in sssom_rows
        if row["subject_label"] == label
        and row["object_id"] == old_curie
        and row["predicate_id"] == "skos:exactMatch"
    ]


def test_colistin_sulfate_salt_was_merged(mapped_records: dict[str, dict]):
    loser = mapped_records["Colistin sulfate salt"]
    winner = mapped_records["Colistin Sulfate"]

    assert loser["identifier"] == "NCIT:C386"
    assert loser["mapping_status"] == "REJECTED"
    assert loser["chemical_properties"] == {}

    assert winner["chemical_properties"]["cas_rn"] == "1264-72-8"
    assert "SELECTIVE_AGENT" in {row["role"] for row in winner.get("physicochemical_roles", [])}
    assert any(
        synonym["synonym_text"] == "Colistin sulfate salt" for synonym in winner.get("synonyms", [])
    )


def test_colistin_sulfate_publishes_cas(sssom_rows: list[dict[str, str]]):
    rows = [
        row
        for row in sssom_rows
        if row["subject_label"] == "Colistin Sulfate" and row["object_id"] == "NCIT:C386"
    ]

    assert len(rows) == 1
    assert "cas:1264-72-8" in _other_tokens(rows[0])


def test_potassium_tellurate_was_relabelled(mapped_records: dict[str, dict]):
    record = mapped_records["potassium tellurite"]

    assert "potassium tellurate" not in mapped_records
    assert record["identifier"] == "CHEBI:75248"
    assert record["ontology_mapping"]["ontology_id"] == "CHEBI:75248"
    assert record["chemical_properties"]["cas_rn"] == "7790-58-1"


def test_potassium_tellurite_subject_matches_renamed_file(
    sssom_rows: list[dict[str, str]],
):
    rows = [row for row in sssom_rows if row["subject_label"] == "potassium tellurite"]

    assert len(rows) == 1
    assert rows[0]["subject_id"] == "MIM:Potassium_Tellurite"
    assert rows[0]["predicate_id"] == "skos:exactMatch"
    assert rows[0]["object_id"] == "CHEBI:75248"
    assert "cas:7790-58-1" in _other_tokens(rows[0])


def test_stale_chEBI_synonyms_no_longer_resolve(
    label_index_rows: list[dict[str, str]],
):
    bad = {
        "30-hydroxy-11,30-dioxoolean-12-en-3beta-yl "
        "(2-O-beta-D-glucopyranosyluronic acid)-alpha-D-glucopyranosiduronic acid",
        "3-(dimethylsulfonio)propanoate",
        "[dodecanoyl(methyl)amino] acetate",
        "sodium;2-[dodecanoyl(methyl)amino]acetate",
    }

    assert not [
        row
        for row in label_index_rows
        if row["preferred_term"].casefold()
        in {
            "glycyrrhizic acid, ammonium salt",
            "dimethylsulfoniopropionate hydrochloride",
            "n-lauroylsarcosine sodium salt",
        }
        and row["label"].casefold() in {label.casefold() for label in bad}
    ]
