"""Malformed hydrate source labels keep local identities (#344)."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).parent.parent
CURATED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
MEMBERSHIP = ROOT / "mappings" / "culturemech_recipe_membership.tsv"
LABEL_INDEX = ROOT / "docs" / "data" / "label_index.csv"

MALFORMED = {
    "CaCl2 x 7 H2O": ("kgmicrobe.compound:cacl2_x_7_h2o", "CHEBI:3312"),
    "CaSO4 x 7 H2O": ("kgmicrobe.compound:caso4_x_7_h2o", "CHEBI:31346"),
    "CuCl2 x 6 H2O": ("kgmicrobe.compound:cucl2_x_6_h2o", "CHEBI:49553"),
    "FeCl2 x 6 H2O": ("kgmicrobe.compound:fecl2_x_6_h2o", "CHEBI:30812"),
    "FeCl2 x 7 H2O": ("kgmicrobe.compound:fecl2_x_7_h2o", "CHEBI:30812"),
    "FeCl3 x 4 H2O": ("kgmicrobe.compound:fecl3_x_4_h2o", "CHEBI:30808"),
    "K2SO4 x 7 H2O": ("kgmicrobe.compound:k2so4_x_7_h2o", "CHEBI:32036"),
    "MgCl2 x 7 H2O": ("kgmicrobe.compound:mgcl2_x_7_h2o", "CHEBI:6636"),
    "Na2HPO4 x 3 H2O": ("kgmicrobe.compound:na2hpo4_x_3_h2o", "CHEBI:34683"),
    "Na2HPO4 x 6 H2O": ("kgmicrobe.compound:na2hpo4_x_6_h2o", "CHEBI:34683"),
    "NiCl2 x 5 H2O": ("kgmicrobe.compound:nicl2_x_5_h2o", "CHEBI:34887"),
}

SULFATE_MEMBERSHIPS = {
    "kgmicrobe.compound:caso4_x_7_h2o": {
        "CultureMech:002288",
        "CultureMech:010491",
        "CultureMech:014112",
        "CultureMech:014113",
    },
    "kgmicrobe.compound:k2so4_x_7_h2o": {
        "CultureMech:003225",
        "CultureMech:010337",
        "CultureMech:010338",
        "CultureMech:013797",
    },
}

MALFORMED_OTHER_TOKENS = {
    "CaCl2 x 7 H2O": {
        "CaCl2 . 7H2O",
        "CaCl2⋅7H2O",
    },
    "CaSO4 x 7 H2O": {
        "CaSO4・7H2O",
    },
    "CuCl2 x 6 H2O": {
        "CuCl2 × 6H2O",
    },
    "FeCl2 x 6 H2O": {
        "FeCl2·6H2O",
        "FeCl2⋅6H2O",
    },
    "FeCl2 x 7 H2O": set(),
    "FeCl3 x 4 H2O": {
        "FeCl3·4H2O",
    },
    "K2SO4 x 7 H2O": {
        "K2SO4·7H2O",
        "K2SO4・7H2O",
    },
    "MgCl2 x 7 H2O": {
        "MgCl2 x 7H2O",
        "MgCl2x7H2O",
        "MgCl2  x 7 H2O",
    },
    "Na2HPO4 x 3 H2O": set(),
    "Na2HPO4 x 6 H2O": {
        "Na2HPO4·6H2O",
    },
    "NiCl2 x 5 H2O": {
        "NiCl2・5H2O",
    },
}


@pytest.fixture(scope="module")
def records() -> list[dict]:
    return yaml.safe_load(CURATED.read_text(encoding="utf-8"))["ingredients"]


@pytest.fixture(scope="module")
def sssom_rows() -> list[dict[str, str]]:
    with SSSOM.open(newline="", encoding="utf-8") as fh:
        rows = [line for line in fh if not line.startswith("#")]
    return list(csv.DictReader(rows, delimiter="\t"))


@pytest.fixture(scope="module")
def membership_rows() -> list[dict[str, str]]:
    with MEMBERSHIP.open(newline="", encoding="utf-8") as fh:
        rows = [line for line in fh if not line.startswith("#")]
    return list(csv.DictReader(rows, delimiter="\t"))


@pytest.fixture(scope="module")
def label_index_rows() -> list[dict[str, str]]:
    with LABEL_INDEX.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def _by_term(records: list[dict], term: str) -> dict:
    hits = [record for record in records if record.get("preferred_term") == term]
    assert len(hits) == 1
    return hits[0]


@pytest.mark.parametrize("term", sorted(MALFORMED))
def test_malformed_hydrate_labels_are_local_identities(records, term):
    identifier, parent = MALFORMED[term]
    record = _by_term(records, term)

    assert record["identifier"] == identifier
    assert record["ontology_mapping"]["ontology_id"] == parent
    assert record["ontology_mapping"]["mapping_quality"] == "CLOSE_MATCH"
    assert record.get("chemical_properties") == {}
    assert record.get("kg_microbe_node_id") != parent


@pytest.mark.parametrize("term", sorted(MALFORMED))
def test_malformed_hydrate_sssom_keeps_parent_and_registry_rows(sssom_rows, term):
    identifier, parent = MALFORMED[term]
    rows = {row["object_id"]: row for row in sssom_rows if row["subject_label"] == term}

    assert set(rows) == {parent, identifier}
    assert rows[parent]["predicate_id"] == "skos:closeMatch"
    assert rows[parent]["confidence"] == "0.9"
    assert rows[identifier]["predicate_id"] == "skos:exactMatch"
    assert rows[identifier]["object_label"] == term
    assert rows[identifier]["object_source"] == "kgm:compound"
    assert "CAS:" not in rows[parent]["other"]
    assert "CAS:" not in rows[identifier]["other"]


def test_sulfate_heptahydrate_memberships_are_split_from_anhydrous_parents(
    membership_rows,
):
    by_identifier = {}
    for identifier in SULFATE_MEMBERSHIPS:
        by_identifier[identifier] = {
            row["recipe_id"] for row in membership_rows if row["mim_identifier"] == identifier
        }

    assert by_identifier == SULFATE_MEMBERSHIPS
    for parent, recipes in {
        "CHEBI:31346": SULFATE_MEMBERSHIPS["kgmicrobe.compound:caso4_x_7_h2o"],
        "CHEBI:32036": SULFATE_MEMBERSHIPS["kgmicrobe.compound:k2so4_x_7_h2o"],
    }.items():
        parent_recipes = {
            row["recipe_id"] for row in membership_rows if row["mim_identifier"] == parent
        }
        assert parent_recipes.isdisjoint(recipes)


def test_malformed_hydrate_aliases_do_not_leak_to_other_identities(
    sssom_rows,
):
    owner_by_token = {
        token.casefold(): owner
        for owner, tokens in MALFORMED_OTHER_TOKENS.items()
        for token in {owner} | tokens
    }
    leaked = []
    for row in sssom_rows:
        for token in (row["other"] or "").split("|"):
            token = token.strip()
            owner = owner_by_token.get(token.casefold())
            if owner is not None and row["subject_label"] != owner:
                leaked.append((row["subject_label"], token, owner))

    assert leaked == []


def test_malformed_hydrate_label_index_prefers_owning_local_identity(
    label_index_rows,
):
    by_label = defaultdict(list)
    for row in label_index_rows:
        by_label[row["label"]].append(row)

    for owner, tokens in MALFORMED_OTHER_TOKENS.items():
        expected_identifier = MALFORMED[owner][0]
        for token in {owner} | tokens:
            rows = by_label[token]
            assert rows, token

            assert rows[0]["identifier"] == expected_identifier
            assert rows[0]["mapping_status"] == "MAPPED"
            assert rows[0]["preferred_term"] == owner

            mapped_rows = [row for row in rows if row["mapping_status"] == "MAPPED"]
            assert mapped_rows
            assert {(row["identifier"], row["preferred_term"]) for row in mapped_rows} == {
                (expected_identifier, owner)
            }
