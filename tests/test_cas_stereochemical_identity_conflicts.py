"""Regression coverage for CAS-selected stereochemical repairs (#456)."""

from __future__ import annotations

import csv
import io
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parents[1]

CAS_REGROUNDINGS = {
    "DL-2-Aminobutyric acid": (
        "cas:2835-81-6",
        "CHEBI:35621",
        "C4H9NO2",
        "2835-81-6",
    ),
    "DL-3-Aminoisobutyric acid": (
        "cas:144-90-1",
        "CHEBI:27389",
        "C4H9NO2",
        "144-90-1",
    ),
    "DL-Glyceraldehyde 3-phosphate": (
        "cas:591-59-3",
        "CHEBI:17138",
        "C3H7O6P",
        "591-59-3",
    ),
    "DL-glyceraldehyde": (
        "cas:56-82-6",
        "CHEBI:5445",
        "C3H6O3",
        "56-82-6",
    ),
    "N-(3-oxohexanoyl)-DL-homoserine lactone": (
        "cas:76924-95-3",
        "CHEBI:29640",
        "C10H15NO4",
        "76924-95-3",
    ),
    "rac-3-Hydroxypentanoic Acid": (
        "cas:10237-77-1",
        "CHEBI:139272",
        "C5H10O3",
        "10237-77-1",
    ),
}

KGM_REGROUNDINGS = {
    "methyl-cis-p-coumarate": (
        "kgmicrobe.compound:methyl-cis-p-coumarate",
        "CHEBI:86904",
        "C10H10O3",
        "3943-97-3",
    ),
}

FALLBACK_REGROUNDINGS = {
    "Alpha-Toxicarol (Dl)": (
        "kgmicrobe.compound:alpha-toxicarol_dl",
        "C23H22O7",
        "82-09-7",
    ),
}

EXACT_REGROUNDINGS = {
    "Perillic Acid (-)": ("CHEBI:109544", "C10H14O2", None),
    "Trans,Trans-Farnesol": ("CHEBI:16619", "C15H26O", "106-28-5"),
}

OLD_EXACT_ROWS = {
    "Alpha-Toxicarol (Dl)": "CHEBI:9643",
    "DL-2-Aminobutyric acid": "CHEBI:35621",
    "DL-3-Aminoisobutyric acid": "CHEBI:27389",
    "DL-Glyceraldehyde 3-phosphate": "CHEBI:17138",
    "DL-glyceraldehyde": "CHEBI:5445",
    "methyl-cis-p-coumarate": "CHEBI:86904",
    "N-(3-oxohexanoyl)-DL-homoserine lactone": "CHEBI:29640",
    "Perillic Acid (-)": "CHEBI:36999",
    "rac-3-Hydroxypentanoic Acid": "CHEBI:139272",
    "Trans,Trans-Farnesol": "CHEBI:28600",
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


def test_dl_and_racemic_forms_have_cas_identities(mapped_records: dict[str, dict]):
    for label, (identifier, parent, formula, cas_rn) in CAS_REGROUNDINGS.items():
        record = mapped_records[label]

        assert record["identifier"] == identifier
        assert record["ontology_mapping"]["ontology_id"] == parent
        assert record["ontology_mapping"]["mapping_quality"] == "NARROW_MATCH"
        assert record["chemical_properties"]["molecular_formula"] == formula
        assert record["chemical_properties"]["cas_rn"] == cas_rn


def test_uncatalogued_isomers_have_kgm_identities_without_bad_cas(
    mapped_records: dict[str, dict],
):
    for label, (identifier, parent, formula, old_cas) in KGM_REGROUNDINGS.items():
        record = mapped_records[label]

        assert record["identifier"] == identifier
        assert record["ontology_mapping"]["ontology_id"] == parent
        assert record["ontology_mapping"]["mapping_quality"] == "NARROW_MATCH"
        assert record["chemical_properties"]["molecular_formula"] == formula
        assert record["chemical_properties"].get("cas_rn") != old_cas
        assert record["chemical_properties"].get("cas_rn") is None
        assert record["chemical_properties"].get("inchi") is None
        assert record["chemical_properties"].get("smiles") is None


def test_dl_form_without_parent_has_local_fallback_identity(
    mapped_records: dict[str, dict],
):
    for label, (identifier, formula, old_cas) in FALLBACK_REGROUNDINGS.items():
        record = mapped_records[label]

        assert record["identifier"] == identifier
        assert record["ontology_mapping"]["ontology_id"] == identifier
        assert record["ontology_mapping"]["ontology_source"] == "kgmicrobe.compound"
        assert record["ontology_mapping"]["mapping_quality"] == "FALLBACK_REGISTRY"
        assert record["chemical_properties"]["molecular_formula"] == formula
        assert record["chemical_properties"].get("cas_rn") != old_cas
        assert record["chemical_properties"].get("inchi") is None
        assert record["chemical_properties"].get("smiles") is None


def test_exact_stereochemical_terms_have_exact_chebi_ids(mapped_records: dict[str, dict]):
    for label, (identifier, formula, cas_rn) in EXACT_REGROUNDINGS.items():
        record = mapped_records[label]

        assert record["identifier"] == identifier
        assert record["ontology_mapping"]["ontology_id"] == identifier
        assert record["ontology_mapping"]["mapping_quality"] == "EXACT_MATCH"
        assert record["chemical_properties"]["molecular_formula"] == formula
        assert record["chemical_properties"].get("cas_rn") == cas_rn


def test_narrow_stereochemical_forms_publish_registry_rows(
    sssom_rows: list[dict[str, str]],
):
    by_label: dict[str, dict[str, dict[str, str]]] = {}
    for row in sssom_rows:
        by_label.setdefault(row["subject_label"], {})[row["object_id"]] = row

    for label, (identifier, parent, _, cas_rn) in CAS_REGROUNDINGS.items():
        parent_row = by_label[label][parent]
        assert parent_row["predicate_id"] == "skos:narrowMatch"
        assert not any(token.startswith("cas:") for token in _other_tokens(parent_row))

        cas_row = by_label[label][identifier]
        assert cas_row["predicate_id"] == "skos:exactMatch"
        assert cas_row["object_source"] == "registry:cas"
        assert f"cas:{cas_rn}" in _other_tokens(cas_row)

        subject_slug = parent_row["subject_id"].removeprefix("MIM:")
        kgm_row = by_label[label][f"kgmicrobe.compound:{subject_slug.lower()}"]
        assert kgm_row["predicate_id"] == "skos:exactMatch"
        assert kgm_row["object_source"] == "kgm:compound"
        assert f"cas:{cas_rn}" in _other_tokens(kgm_row)

    for label, (identifier, parent, _, _) in KGM_REGROUNDINGS.items():
        parent_row = by_label[label][parent]
        assert parent_row["predicate_id"] == "skos:narrowMatch"
        assert not any(token.startswith("cas:") for token in _other_tokens(parent_row))

        kgm_row = by_label[label][identifier]
        assert kgm_row["predicate_id"] == "skos:exactMatch"
        assert kgm_row["object_source"] == "kgm:compound"
        assert not any(token.startswith("cas:") for token in _other_tokens(kgm_row))


def test_unparented_dl_form_publishes_only_local_fallback_row(
    sssom_rows: list[dict[str, str]],
):
    for label, (identifier, _, _) in FALLBACK_REGROUNDINGS.items():
        rows = [row for row in sssom_rows if row["subject_label"] == label]

        assert len(rows) == 1
        assert rows[0]["predicate_id"] == "skos:exactMatch"
        assert rows[0]["object_id"] == identifier
        assert rows[0]["object_source"] == "kgm:compound"
        assert not _other_tokens(rows[0])


@pytest.mark.parametrize(("label", "old_curie"), sorted(OLD_EXACT_ROWS.items()))
def test_bad_exact_chebi_rows_are_gone(
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


def test_exact_chEBI_rows_publish_updated_targets(sssom_rows: list[dict[str, str]]):
    by_label = {row["subject_label"]: row for row in sssom_rows}

    perillic = by_label["Perillic Acid (-)"]
    assert perillic["object_id"] == "CHEBI:109544"
    assert perillic["predicate_id"] == "skos:exactMatch"
    assert "cas:7694-45-3" not in _other_tokens(perillic)

    farnesol = by_label["Trans,Trans-Farnesol"]
    assert farnesol["object_id"] == "CHEBI:16619"
    assert farnesol["predicate_id"] == "skos:exactMatch"
    assert "cas:106-28-5" in _other_tokens(farnesol)
    assert "cas:4602-84-0" not in _other_tokens(farnesol)


def test_stale_chEBI_synonyms_no_longer_resolve(
    label_index_rows: list[dict[str, str]],
):
    bad_labels = {
        "2-aminobutanoic acid",
        "3-amino-2-methylpropanoic acid",
        "2-hydroxy-3-oxopropyl dihydrogen phosphate",
        "2,3-dihydroxypropanal",
        "methyl 3-(4-hydroxyphenyl)prop-2-enoate",
        "3-oxo-N-(2-oxotetrahydrofuran-3-yl)hexanamide",
        "4-(prop-1-en-2-yl)cyclohex-1-ene-1-carboxylic acid",
        "3,7,11-trimethyldodeca-2,6,10-trien-1-ol",
    }

    assert not [
        row
        for row in label_index_rows
        if row["preferred_term"] in OLD_EXACT_ROWS and row["label"] in bad_labels
    ]
