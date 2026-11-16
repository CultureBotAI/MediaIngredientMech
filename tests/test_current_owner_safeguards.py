"""Current source-scoped safeguards paired with #1447 historical regressions.

Expected identities below come from the reviewed source distinctions documented
in the fixture README, not by copying the live record. This does not approve
fixed chemistry, source/quantity/role claims or a current publication product.
"""

from __future__ import annotations

import copy
import json

import pytest
import yaml

from tests import historical_owner_context as historical
from tests.stable_id_helpers import current_record

OWNERS = {
    "cysteine": "MIM:0001416",
    "chromium": "MIM:0000760",
    "ferric": "MIM:0001058",
    "magnesium": "MIM:0001680",
    "atcc": "MIM:0000236",
    "wolfe": "MIM:0002643",
    "acriflavine": "MIM:0000264",
    "trihydrate": "MIM:0002928",
    "bsa": "MIM:0000522",
}


@pytest.fixture(scope="module")
def before():
    inputs = historical.context_bytes()
    records = yaml.safe_load(inputs[historical.MAPPED])["ingredients"]
    result = {r["preferred_term"]: r for r in records}
    tri = yaml.safe_load(inputs["data/ingredients/unmapped/Trisodium_Citrate_X_3_H2o.yaml"])
    result[tri["preferred_term"]] = tri
    return result


def assert_history(current, old):
    assert current["curation_history"][: len(old["curation_history"])] == old["curation_history"]


def assert_parent(record, identity, parent):
    assert record["identifier"] == identity
    assert record["ontology_mapping"]["ontology_id"] == parent
    assert record["ontology_mapping"]["mapping_quality"] == "NARROW_MATCH"
    assert record.get("kg_microbe_node_id") != parent


def assert_rejected(record, token):
    matches = [s for s in record.get("synonyms", []) if s["synonym_text"] == token]
    assert matches and all(s["synonym_type"] == "REJECTED_LABEL" for s in matches)


def assert_cysteine(record):
    assert_parent(record, "kgmicrobe.ingredient:l-cysteine_x_hcl_x_h2o_solution", "CHEBI:91248")
    assert record["ingredient_type"] == "STOCK_SOLUTION"
    assert_rejected(record, "QSY9 succinimidyl ester(1+)")
    # The receiving-medium10mL does not supply stock concentration or chemistry.
    assert not record.get("chemical_properties")


def assert_variable(record, kind):
    cas, parent = {
        "chromium": ("15244-38-9", "CHEBI:53471"),
        "ferric": ("15244-10-7", "CHEBI:53438"),
    }[kind]
    assert_parent(record, "cas:" + cas, parent)
    properties = record["chemical_properties"]
    assert properties["cas_rn"] == cas
    assert not any(properties.get(key) for key in ("molecular_weight", "smiles", "inchi"))
    if kind == "chromium":
        assert properties["molecular_formula"] == "Cr2(SO4)3.xH2O"
    else:
        assert not properties.get("molecular_formula")
        assert record["ontology_mapping"]["ontology_id"] != "CHEBI:131387"
        assert properties["cas_rn"] != "43059-01-4"
        assert_rejected(record, "Fe(SO4)3 x n H2O")


def assert_magnesium(record):
    assert_parent(record, "cas:17830-18-1", "CHEBI:32599")
    props = record["chemical_properties"]
    assert props["cas_rn"] == "17830-18-1"
    assert props["molecular_formula"] == "Mg.O4S.6H2O"
    assert not any(props.get(k) for k in ("molecular_weight", "smiles", "inchi", "melting_point"))


def assert_wolfe(record, name, amount):
    hits = [c for c in record["components"] if c["component_name"] == name]
    assert len(hits) == 1
    assert hits[0]["component_id"] == "CHEBI:16494"
    assert hits[0]["reference_scope"] == "MIM_CATALOG"
    assert hits[0]["concentration_value"] == amount
    assert hits[0]["concentration_unit"] == "MG_PER_L"
    if name == "Lipoic acid":
        assert "CultureBotHT Mixes.csv" in hits[0]["source"]
        assert "no R/S or racemate claim" in hits[0]["source"]
        pantothenate = [
            c for c in record["components"] if "pantothen" in c["component_name"].lower()
        ]
        assert len(pantothenate) == 1
        assert pantothenate[0]["reference_scope"] == "UNMAPPED"
        assert "component_id" not in pantothenate[0]


def assert_acriflavine(record, old):
    assert record["identifier"] == record["ontology_mapping"]["ontology_id"] == "NCIT:C76253"
    assert record["ontology_mapping"]["mapping_quality"] == "MANUAL_CURATION"
    assert any(
        "#1386" in e.get("changes", "") and "MANUAL_CURATION" in e["changes"]
        for e in record["curation_history"]
    )
    assert record["chemical_properties"]["cas_rn"] == "65589-70-0"
    # Byte-preservation of existing properties is not their scientific approval.
    assert record["chemical_properties"] == old["chemical_properties"]
    assert "8048-52-0" in record["notes"]


def assert_trihydrate(record):
    assert record["mim_id"] == "MIM:0002928"
    assert_parent(record, "kgmicrobe.compound:trisodium_citrate_trihydrate", "CHEBI:53258")
    assert "UNMAPPED_0852" in record["legacy_identifiers"]
    assert "UNMAPPED_0820" not in record["legacy_identifiers"]
    assert record["chemical_properties"]["molecular_formula"] == "C6H5Na3O7.3H2O"
    assert not record["chemical_properties"].get("cas_rn")
    assert any(
        "#1021" in e.get("changes", "")
        and "UNMAPPED_0820" in e["changes"]
        and "UNMAPPED_0852" in e["changes"]
        for e in record["curation_history"]
    )


def assert_bsa(record, old):
    assert record["identifier"] == "NCIT:C85253"
    for original in old["supplied_form"]:
        matches = [
            f
            for f in record["supplied_form"]
            if f.get("catalog_number") == original["catalog_number"]
        ]
        assert matches == [original]
    # Unknown manufacturer/catalog is an explicit source limitation, not a default.
    unspecified = [
        f for f in record["supplied_form"] if "manufacturer/catalog" in f.get("notes", "").lower()
    ]
    assert unspecified
    assert all(not f.get("catalog_number") and not f.get("supplier") for f in unspecified)


@pytest.mark.parametrize("key", list(OWNERS))
def test_current_owner_preserves_permanent_identity_and_complete_original_history(key, before):
    record = current_record(OWNERS[key])
    assert record["mim_id"] == OWNERS[key]
    assert record["mapping_status"] == "MAPPED"
    assert_history(record, before[record["preferred_term"]])


@pytest.mark.parametrize(
    "key",
    [
        "cysteine",
        "chromium",
        "ferric",
        "magnesium",
        "atcc",
        "wolfe",
        "acriflavine",
        "trihydrate",
        "bsa",
    ],
)
def test_current_scientific_safeguard(key, before):
    r = current_record(OWNERS[key])
    if key == "cysteine":
        assert_cysteine(r)
    elif key in {"chromium", "ferric"}:
        assert_variable(r, key)
    elif key == "magnesium":
        assert_magnesium(r)
    elif key == "atcc":
        assert_wolfe(r, "Thioctic acid", "5.0")
    elif key == "wolfe":
        assert_wolfe(r, "Lipoic acid", "5")
    elif key == "acriflavine":
        assert_acriflavine(r, before[r["preferred_term"]])
    elif key == "trihydrate":
        assert_trihydrate(r)
    elif key == "bsa":
        assert_bsa(r, before[r["preferred_term"]])


@pytest.mark.parametrize("mutation", ["removed", "altered"])
def test_current_history_guard_refuses_loss(mutation, before):
    r = copy.deepcopy(current_record(OWNERS["trihydrate"]))
    old = before[r["preferred_term"]]
    if mutation == "removed":
        r["curation_history"].pop(0)
    else:
        r["curation_history"][0]["changes"] = "altered"
    with pytest.raises(AssertionError):
        assert_history(r, old)


@pytest.mark.parametrize("mutation", ["parent_exact", "wrong_parent", "resolving_dye"])
def test_solution_guard_refuses_collapse_or_bad_alias(mutation):
    r = copy.deepcopy(current_record(OWNERS["cysteine"]))
    if mutation == "parent_exact":
        r["identifier"] = "CHEBI:91248"
    elif mutation == "wrong_parent":
        r["ontology_mapping"]["ontology_id"] = "CHEBI:35235"
    else:
        next(s for s in r["synonyms"] if s["synonym_text"] == "QSY9 succinimidyl ester(1+)")[
            "synonym_type"
        ] = "EXACT_SYNONYM"
    with pytest.raises(AssertionError):
        assert_cysteine(r)


@pytest.mark.parametrize(
    "kind,mutation",
    [
        (k, m)
        for k in ["chromium", "ferric"]
        for m in ["fixed_mass", "structure", "wrong_cas", "parent_exact"]
    ],
)
def test_variable_hydrate_guard_refuses_unsupported_chemistry(kind, mutation):
    r = copy.deepcopy(current_record(OWNERS[kind]))
    if mutation == "fixed_mass":
        r["chemical_properties"]["molecular_weight"] = 399.88
    elif mutation == "structure":
        r["chemical_properties"]["smiles"] = "O"
    elif mutation == "wrong_cas":
        r["chemical_properties"]["cas_rn"] = "43059-01-4"
    else:
        r["ontology_mapping"]["mapping_quality"] = "EXACT_MATCH"
    with pytest.raises(AssertionError):
        assert_variable(r, kind)


@pytest.mark.parametrize("formula", ["Mg.O4S", "Mg.O4S.H2O", "Mg.O4S.7H2O"])
def test_magnesium_guard_refuses_other_water_counts(formula):
    r = copy.deepcopy(current_record(OWNERS["magnesium"]))
    r["chemical_properties"]["molecular_formula"] = formula
    with pytest.raises(AssertionError):
        assert_magnesium(r)


@pytest.mark.parametrize("mutation", ["R_specific", "rescaled", "pantothenate_release"])
def test_wolfe_guard_keeps_generic_component_and_stereochemical_hold(mutation):
    r = copy.deepcopy(current_record(OWNERS["wolfe"]))
    c = next(c for c in r["components"] if c["component_name"] == "Lipoic acid")
    if mutation == "R_specific":
        c["component_id"] = "CHEBI:30314"
    elif mutation == "rescaled":
        c["concentration_value"] = "500"
    else:
        next(c for c in r["components"] if "pantothen" in c["component_name"].lower())[
            "component_id"
        ] = "CHEBI:46905"
    with pytest.raises(AssertionError):
        assert_wolfe(r, "Lipoic acid", "5")


@pytest.mark.parametrize("mutation", ["method", "cas"])
def test_acriflavine_guard_keeps_method_and_registry_scope(mutation, before):
    r = copy.deepcopy(current_record(OWNERS["acriflavine"]))
    if mutation == "method":
        r["ontology_mapping"]["mapping_quality"] = "EXACT_MATCH"
    else:
        r["chemical_properties"]["cas_rn"] = "8048-52-0"
    with pytest.raises(AssertionError):
        assert_acriflavine(r, before[r["preferred_term"]])


@pytest.mark.parametrize("mutation", ["retired", "water", "cas"])
def test_trihydrate_guard_refuses_retired_alias_or_invented_identity(mutation):
    r = copy.deepcopy(current_record(OWNERS["trihydrate"]))
    if mutation == "retired":
        r["legacy_identifiers"].append("UNMAPPED_0820")
    elif mutation == "water":
        r["chemical_properties"]["molecular_formula"] = "C6H5Na3O7.2H2O"
    else:
        r["chemical_properties"]["cas_rn"] = "6132-04-3"
    with pytest.raises(AssertionError):
        assert_trihydrate(r)


@pytest.mark.parametrize("mutation", ["lost_product", "merged_products", "guessed_catalog"])
def test_bsa_guard_refuses_product_loss_or_invented_procurement(mutation, before):
    r = copy.deepcopy(current_record(OWNERS["bsa"]))
    if mutation == "lost_product":
        r["supplied_form"] = [f for f in r["supplied_form"] if f.get("catalog_number") != "A7030"]
    elif mutation == "merged_products":
        next(f for f in r["supplied_form"] if f.get("catalog_number") == "A7409")[
            "catalog_number"
        ] = "A9647"
    else:
        next(f for f in r["supplied_form"] if "manufacturer/catalog" in f.get("notes", "").lower())[
            "catalog_number"
        ] = "invented"
    with pytest.raises(AssertionError):
        assert_bsa(r, before[r["preferred_term"]])


def test_acriflavine_retained_fda_status_is_scoped_to_the_named_record():
    fda = json.loads((historical.ROOT / historical.EVIDENCE / "fda-gsrs.json").read_text())[
        "1T3A50395T"
    ]
    assert fda["substanceClass"] == "mixture"
    codes = {c["code"]: c["type"] for c in fda["codes"] if c["codeSystem"] == "CAS"}
    assert codes == {"8048-52-0": "SUPERSEDED", "65589-70-0": "PRIMARY"}
