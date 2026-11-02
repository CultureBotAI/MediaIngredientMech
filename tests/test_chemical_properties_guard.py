"""Record/form boundaries; all providers are deterministic local doubles."""

import hashlib
import json
from copy import deepcopy
from dataclasses import replace
from pathlib import Path
from types import SimpleNamespace

import pytest
import yaml

from mediaingredientmech.curation.chemical_properties_guard import (
    chemistry_preflight,
    prepare_chemical_properties,
)
from mediaingredientmech.utils.chemical_properties_client import OlsChemicalProperties


def record(label="water", oid="CHEBI:15377", **changes):
    rec = {
        "identifier": oid,
        "preferred_term": label,
        "mapping_status": "MAPPED",
        "ingredient_type": "SINGLE_INGREDIENT",
        "ontology_mapping": {
            "ontology_id": oid,
            "ontology_source": "CHEBI",
            "ontology_label": label,
            "mapping_quality": "CAS_RN_LOOKUP",
        },
        "curation_history": [{"action": "OLD"}],
    }
    rec.update(changes)
    return rec


def envelope(label="water", oid="CHEBI:15377", **values):
    url = (
        "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_"
        + oid.split(":")[1]
    )
    date = "2026-11-02T00:00:00+00:00"
    props = {
        "molecular_formula": "H2O",
        "smiles": "O",
        "inchi": "InChI=1S/H2O/h1H2",
        "molecular_weight": 18.015,
        "data_source": f"ChEBI {oid}; {url}",
        "retrieval_date": date,
    }
    props.update(values)
    return OlsChemicalProperties(oid, oid, label, (), url, date, "0" * 64, tuple(props.items()))


class Client:
    def __init__(self, result=None):
        self.result = result or envelope()
        self.calls = []

    def get_ols_properties(self, oid):
        self.calls.append(oid)
        return self.result

    def get_properties(self, *args):
        raise AssertionError("legacy retrieval forbidden")


@pytest.mark.parametrize("grade", ["EXACT_MATCH", "SYNONYM_MATCH", "CAS_RN_LOOKUP"])
def test_grade_independent_identity_and_pure_proposal(grade):
    rec = record()
    rec["ontology_mapping"]["mapping_quality"] = grade
    before = deepcopy(rec)
    client = Client()
    assert chemistry_preflight(rec) is None
    props, reason = prepare_chemical_properties(rec, client)
    assert props["molecular_formula"] == "H2O" and "response SHA256" in reason
    assert client.calls == ["CHEBI:15377"] and rec == before
    props["smiles"] = "changed"
    assert client.result.to_dict()["smiles"] == "O"


@pytest.mark.parametrize(
    "block", [{"cas_rn": "7732-18-5"}, {"data_source": "curator"}, {"molecular_formula": "H2O"}]
)
@pytest.mark.parametrize("grade", ["EXACT_MATCH", "SYNONYM_MATCH", "CAS_RN_LOOKUP"])
def test_every_populated_block_preserved_before_provider(block, grade):
    rec = record(chemical_properties=block)
    rec["ontology_mapping"]["mapping_quality"] = grade
    before = deepcopy(rec)
    client = Client()
    assert chemistry_preflight(rec) is None
    assert prepare_chemical_properties(rec, client) == (None, "EXISTING_CHEMISTRY")
    assert client.calls == [] and rec == before


@pytest.mark.parametrize(
    "updates,reason",
    [
        ({"mapping_status": "REJECTED"}, "INACTIVE_RECORD"),
        ({"representative": "CHEBI:1"}, "RETIRED_RECORD"),
        ({"ingredient_type": None}, "UNRESOLVED_INGREDIENT_SCOPE"),
        ({"ingredient_type": "STOCK_SOLUTION"}, "UNRESOLVED_INGREDIENT_SCOPE"),
        ({"ingredient_type": "UNDEFINED_MIXTURE"}, "UNRESOLVED_INGREDIENT_SCOPE"),
        ({"components": [{"ingredient": "CHEBI:1"}]}, "PREPARATION_SCOPE"),
        ({"component_assertion": {"evidence": "x"}}, "PREPARATION_SCOPE"),
        ({"identifier": "cas:7732-18-5"}, "OWN_IDENTITY_MISMATCH"),
        ({"identifier": "kgmicrobe.ingredient:water"}, "OWN_IDENTITY_MISMATCH"),
        ({"identifier": "CHEBI:999"}, "OWN_IDENTITY_MISMATCH"),
        ({"preferred_term": "0.2 M water"}, "PREPARATION_SCOPE"),
        ({"preferred_term": "20 mg/ml water"}, "PREPARATION_SCOPE"),
        ({"preferred_term": "water stock"}, "PREPARATION_SCOPE"),
        ({"preferred_term": "water extract"}, "MIXTURE_SCOPE"),
        ({"supplied_form": [{"form": "50% solution"}]}, "PREPARATION_SCOPE"),
        ({"supplied_form": [{"form": "sodium salt"}]}, "UNSUPPORTED_SUPPLIED_FORM"),
    ],
)
def test_preflight_refuses_without_fetch(updates, reason):
    rec = record(**updates)
    old = deepcopy(rec)
    client = Client()
    assert prepare_chemical_properties(rec, client) == (None, reason)
    assert not client.calls and rec == old


@pytest.mark.parametrize(
    "left,right",
    [
        ("copper sulfate pentahydrate", "copper sulfate"),
        ("copper sulfate anhydrous", "copper sulfate pentahydrate"),
        ("copper sulfate hydrate", "copper sulfate hydrate"),
        ("copper sulfate hemihydrate", "copper sulfate hemihydrate"),
        ("copper sulfate dihydrate trihydrate", "copper sulfate dihydrate"),
        ("copper sulfate x n H2O", "copper sulfate"),
        ("copper sulfate x 76 H2O", "copper sulfate"),
        ("L-alanine", "D-alanine"),
        ("cis-butene", "butene"),
        ("sodium chloride", "potassium chloride"),
        ("copper(II) chloride", "copper(I) chloride"),
    ],
)
def test_form_or_unresolved_identity_qualifiers_fail_closed(left, right):
    rec = record(left)
    rec["ontology_mapping"]["ontology_label"] = right
    client = Client()
    assert prepare_chemical_properties(rec, client)[0] is None
    assert not client.calls


def test_normal_word_boundaries_do_not_match_molar_unit():
    assert chemistry_preflight(record("ammonium chloride", "CHEBI:1")) is None


def test_legacy_only_client_never_falls_back():
    legacy = SimpleNamespace(get_properties=lambda *a: pytest.fail("legacy called"))
    assert prepare_chemical_properties(record(), legacy) == (None, "UNSUPPORTED_CLIENT")


@pytest.mark.parametrize(
    "key,value",
    [
        ("ontology_id", "CHEBI:1"),
        ("returned_ontology_id", "CHEBI:1"),
        ("label", "hydrogen peroxide"),
        ("source_url", "https://example.invalid/"),
        ("retrieved_at", "not-a-date"),
        ("response_sha256", "wrong"),
    ],
)
def test_returned_envelope_identity_and_provenance_rechecked(key, value):
    client = Client(replace(envelope(), **{key: value}))
    assert prepare_chemical_properties(record(), client)[0] is None


@pytest.mark.parametrize(
    "properties",
    [
        {"molecular_formula": None},
        {"smiles": None},
        {"inchi": None},
        {"molecular_formula": "(C6H10O5)n"},
        {"molecular_formula": "R2O"},
        {"molecular_formula": "H2O2"},
        {"inchi": "garbage"},
        {"smiles": "*"},
        {"inchikey": "unsupported"},
        {"molecular_weight": float("nan")},
    ],
)
def test_missing_malformed_generic_or_inconsistent_structure(properties):
    assert prepare_chemical_properties(record(), Client(envelope(**properties)))[0] is None


def dihydrate():
    raw = (Path(__file__).parent / "fixtures/chemical_properties/ols-91258-list.json").read_bytes()
    assert (
        hashlib.sha256(raw).hexdigest()
        == "e14e1a91519d14765d91d25ca145a56376d176814c62df304f78116dd4ad9278"
    )
    terms = json.loads(raw)["_embedded"]["terms"]
    assert len(terms) == 1
    term = terms[0]
    a = term["annotation"]
    return record(term["label"], term["obo_id"]), envelope(
        term["label"],
        term["obo_id"],
        molecular_formula=a["generalized_empirical_formula"][0],
        inchi=a["inchi_string"][0],
        smiles=a["smiles_string"][0],
        molecular_weight=float(a["mass"][0]),
    )


def test_archived_dihydrate_all_three_components_agree():
    rec, result = dihydrate()
    before = deepcopy(rec)
    props, _ = prepare_chemical_properties(rec, Client(result))
    assert props and props["molecular_formula"] == "2H2O.HO4P.2Na" and rec == before


@pytest.mark.parametrize(
    "key,value",
    [
        ("molecular_formula", "HO4P.2Na"),
        ("inchi", "InChI=1S/2Na.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;;/p-2"),
        ("smiles", "O=P([O-])([O-])O.[Na+].[Na+]"),
        ("molecular_formula", "3H2O.HO4P.2Na"),
    ],
)
def test_hydrate_source_water_evidence_each_required(key, value):
    rec, result = dihydrate()
    props = result.to_dict()
    props[key] = value
    result = replace(result, property_values=tuple(props.items()))
    assert prepare_chemical_properties(rec, Client(result))[0] is None


@pytest.mark.parametrize(
    "formula,inchi,smiles",
    [
        (
            "H2O4P.Na",
            "InChI=1S/Na.H3O4P/c;1-5(2,3)4/h;(H3,1,2,3,4)/q+1;/p-1",
            "O=P([O-])(O)O.[Na+]",
        ),
        ("H2O2", "InChI=1S/H2O2/c1-2/h1-2H", "OO"),
    ],
)
def test_nonwater_atoms_are_not_hydrate_components(formula, inchi, smiles):
    label = "sodium dihydrogenphosphate" if ".Na" in formula else "hydrogen peroxide"
    props, _ = prepare_chemical_properties(
        record(label),
        Client(envelope(label, molecular_formula=formula, inchi=inchi, smiles=smiles)),
    )
    assert props


def test_actual_fifteen_precorrection_owners_preserved_without_calls():
    packet = json.loads(
        (
            Path(__file__).parent / "fixtures/chemical_properties/precorrection-owners.json"
        ).read_bytes()
    )
    assert len(packet["records"]) == 15
    for item in packet["records"]:
        raw = item["raw_yaml"].encode()
        assert hashlib.sha256(raw).hexdigest() == item["sha256"]
        rec = yaml.safe_load(raw)
        before = deepcopy(rec)
        client = Client()
        assert prepare_chemical_properties(rec, client)[0] is None
        assert not client.calls and rec == before


@pytest.mark.parametrize(
    "label,formula,inchi,smiles",
    [
        ("sodium chloride", "ClK", "InChI=1S/ClH.K/h1H;/q;+1/p-1", "[Cl-].[K+]"),
        (
            "disodium hydrogenphosphate",
            "HO4P.Na",
            "InChI=1S/Na.HO4P/c;1-5(2,3)4",
            "O=P([O-])([O-])O.[Na+]",
        ),
    ],
)
def test_source_counterion_contradiction_refused(label, formula, inchi, smiles):
    props = envelope(label, molecular_formula=formula, inchi=inchi, smiles=smiles)
    assert prepare_chemical_properties(record(label), Client(props))[0] is None


@pytest.mark.parametrize("smiles", ["NOT_SMILES", "C1O", "(O", "O)", "[Unknown]", "[Na+]."])
def test_unparseable_structure_is_not_usable_evidence(smiles):
    assert prepare_chemical_properties(record(), Client(envelope(smiles=smiles)))[0] is None


def test_physical_powder_does_not_imply_anhydrous():
    rec, result = dihydrate()
    rec["supplied_form"] = [{"form": "powder"}]
    assert prepare_chemical_properties(rec, Client(result))[0]


def test_source_fetch_failure_is_distinct_from_scope_refusal():
    def fail(_):
        raise RuntimeError("provider unavailable")

    assert prepare_chemical_properties(record(), SimpleNamespace(get_ols_properties=fail)) == (
        None,
        "PROVIDER_FAILURE",
    )


def test_provider_cannot_rebind_owner_during_fetch():
    rec = record()

    def fetch(_):
        rec["identifier"] = "CHEBI:999"
        return envelope()

    assert prepare_chemical_properties(rec, SimpleNamespace(get_ols_properties=fetch)) == (
        None,
        "INPUT_CHANGED_DURING_FETCH",
    )
