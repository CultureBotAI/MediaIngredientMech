"""Strict OLS source envelopes are independent of legacy mixed-source retrieval."""

from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
from dataclasses import FrozenInstanceError
from pathlib import Path
from urllib.parse import quote

import pytest

from mediaingredientmech.utils import chemical_properties_client as mod


@pytest.fixture
def payload():
    """Synthetic complete source identity; not a newly fetched scientific source."""
    return {
        "obo_id": "CHEBI:15377",
        "iri": "http://purl.obolibrary.org/obo/CHEBI_15377",
        "ontology_name": "chebi",
        "is_defining_ontology": True,
        "is_obsolete": False,
        "label": "water",
        "synonyms": ["oxidane", "water", "oxidane"],
        "annotation": {
            "id": ["CHEBI:15377"],
            "generalized_empirical_formula": ["H2O"],
            "smiles_string": ["O"],
            "inchi_string": ["InChI=1S/H2O/h1H2"],
            "mass": ["18.015"],
        },
    }


class Response:
    def __init__(self, raw, status=200):
        self.content = raw
        self.status_code = status

    def json(self):
        raise AssertionError("Must parse the exact content bytes that are hashed")

    def raise_for_status(self):
        if self.status_code >= 400:
            raise mod.requests.HTTPError(str(self.status_code))


def install(monkeypatch, payload=None, *, raw=None, status=200):
    if raw is None:
        raw = json.dumps(payload, indent=2).encode()
    calls = []

    def get(url, **kwargs):
        calls.append((url, kwargs))
        return Response(raw, status)

    def forbidden(*args, **kwargs):
        raise AssertionError("Strict OLS retrieval touched legacy cache or PubChem")

    monkeypatch.setattr(mod.requests, "get", get)
    monkeypatch.setattr(mod.ChemicalPropertiesClient, "_rate_limit", lambda self: None)
    for name in ("_get_from_cache", "_save_to_cache", "_get_pubchem_properties"):
        monkeypatch.setattr(mod.ChemicalPropertiesClient, name, forbidden)
    return mod.ChemicalPropertiesClient(cache_enabled=True), calls, raw


def test_exact_envelope_hash_schema_and_no_legacy_sources(monkeypatch, tmp_path, payload):
    cache = tmp_path / "legacy-cache"
    cache.mkdir()
    (cache / "CHEBI_15377.json").write_text('{"molecular_formula":"WRONG"}')
    monkeypatch.setattr(mod, "CACHE_DIR", cache)
    client, calls, raw = install(monkeypatch, payload)
    result = client.get_ols_properties("CHEBI:15377")
    assert result is not None
    assert result.ontology_id == result.returned_ontology_id == "CHEBI:15377"
    assert result.label == "water" and result.synonyms == ("oxidane", "water")
    assert result.response_sha256 == hashlib.sha256(raw).hexdigest()
    expected_url = mod.CHEBI_OLS_API + "/" + quote(quote(payload["iri"], safe=""), safe="")
    assert calls == [(expected_url, {"timeout": 10, "allow_redirects": False})]
    assert result.source_url == expected_url
    properties = result.to_dict()
    assert set(properties) == {
        "molecular_formula",
        "smiles",
        "inchi",
        "molecular_weight",
        "data_source",
        "retrieval_date",
    }
    assert properties["molecular_formula"] == "H2O"
    assert properties["molecular_weight"] == 18.015
    assert properties["retrieval_date"] == result.retrieved_at
    assert "CHEBI:15377" in properties["data_source"]
    assert expected_url in properties["data_source"]
    assert "PubChem" not in properties["data_source"]
    properties["molecular_formula"] = "CHANGED"
    assert result.to_dict()["molecular_formula"] == "H2O"
    with pytest.raises(FrozenInstanceError):
        result.label = "changed"
    assert (cache / "CHEBI_15377.json").read_text() == '{"molecular_formula":"WRONG"}'
    assert list(cache.iterdir()) == [cache / "CHEBI_15377.json"]


@pytest.mark.parametrize(
    "identifier", ["", "FOODON:15377", "chebi:15377", "CHEBI:015377", "CHEBI:0", "CHEBI:15377/x"]
)
def test_invalid_requested_identity_has_no_request(monkeypatch, payload, identifier):
    client, calls, _ = install(monkeypatch, payload)
    assert client.get_ols_properties(identifier) is None
    assert not calls


@pytest.mark.parametrize("identifier", ["CHEBI:1２", "CHEBI:1٢"])
def test_1099_unicode_digits_refuse_before_http_even_if_response_echoes_them(
    monkeypatch, payload, identifier
):
    payload["obo_id"] = identifier
    payload["iri"] = "http://purl.obolibrary.org/obo/" + identifier.replace(":", "_")
    payload["annotation"]["id"] = [identifier]
    client, calls, _ = install(monkeypatch, payload)
    assert client.get_ols_properties(identifier) is None
    assert calls == []


@pytest.mark.parametrize(
    "key,value",
    [
        ("obo_id", "CHEBI:999"),
        ("iri", "http://purl.obolibrary.org/obo/CHEBI_999"),
        ("ontology_name", "foodon"),
        ("ontology_name", "CHEBI"),
        ("ontology_prefix", "FOODON"),
        ("short_form", "CHEBI_999"),
        ("term_replaced_by", "http://purl.obolibrary.org/obo/CHEBI_999"),
        ("is_defining_ontology", False),
        ("is_defining_ontology", 1),
        ("is_obsolete", True),
        ("is_obsolete", 0),
        ("label", ""),
        ("label", []),
        ("synonyms", "water"),
        ("synonyms", [None]),
    ],
)
def test_conflicting_or_malformed_term_identity_refuses(monkeypatch, payload, key, value):
    payload[key] = value
    client, _, _ = install(monkeypatch, payload)
    assert client.get_ols_properties("CHEBI:15377") is None


@pytest.mark.parametrize(
    "key",
    [
        "obo_id",
        "iri",
        "ontology_name",
        "is_defining_ontology",
        "is_obsolete",
        "label",
        "annotation",
    ],
)
def test_missing_required_term_identity_refuses(monkeypatch, payload, key):
    del payload[key]
    client, _, _ = install(monkeypatch, payload)
    assert client.get_ols_properties("CHEBI:15377") is None


@pytest.mark.parametrize(
    "annotation",
    [
        [],
        {"id": []},
        {"id": ["CHEBI:999"]},
        {"id": ["CHEBI:15377", "CHEBI:999"]},
        {"formula": []},
        {"formula": "H2O"},
        {"formula": [""]},
        {"formula": [None]},
        {"formula": ["H2O", "H2O2"]},
        {"formula": ["H2O"], "generalized_empirical_formula": ["H2O2"]},
        {"smiles": ["O"], "smiles_string": ["OO"]},
        {"inchi": ["InChI=1S/H2O/h1H2"], "inchi_string": ["DIFFERENT"]},
        {"mass": ["NaN"]},
        {"mass": ["inf"]},
        {"mass": ["-1"]},
        {"mass": ["0"]},
        {"mass": [True]},
        {"mass": ["18.015", "18.016"]},
        {"mass": ["not a number"]},
    ],
)
def test_malformed_or_conflicting_annotations_refuse(monkeypatch, payload, annotation):
    if isinstance(annotation, dict):
        payload["annotation"].update(annotation)
    else:
        payload["annotation"] = annotation
    client, _, _ = install(monkeypatch, payload)
    assert client.get_ols_properties("CHEBI:15377") is None


def test_matching_legacy_current_and_repeated_values_are_accepted(monkeypatch, payload):
    payload["annotation"].update(
        {"formula": ["H2O", "H2O"], "SMILES": ["O"], "mass": ["18.015", 18.015]}
    )
    client, _, _ = install(monkeypatch, payload)
    assert client.get_ols_properties("CHEBI:15377").to_dict()["molecular_formula"] == "H2O"


def test_annotation_id_optional_but_not_invented(monkeypatch, payload):
    del payload["annotation"]["id"]
    client, _, _ = install(monkeypatch, payload)
    assert client.get_ols_properties("CHEBI:15377") is not None


def test_no_properties_refuses(monkeypatch, payload):
    payload["annotation"] = {"id": ["CHEBI:15377"]}
    client, _, _ = install(monkeypatch, payload)
    assert client.get_ols_properties("CHEBI:15377") is None


@pytest.mark.parametrize(
    "raw", [b"not json", b"[]", b"null", b'{"obo_id":"CHEBI:999","obo_id":"CHEBI:15377"}']
)
def test_invalid_or_duplicate_json_refuses(monkeypatch, raw):
    client, _, _ = install(monkeypatch, raw=raw)
    assert client.get_ols_properties("CHEBI:15377") is None


def test_redirect_does_not_choose_another_term(monkeypatch, payload):
    client, calls, _ = install(monkeypatch, payload, status=301)
    assert client.get_ols_properties("CHEBI:15377") is None
    assert len(calls) == 1


@pytest.mark.parametrize("status", [404, 500])
def test_http_failure_propagates_without_choosing_another_term(monkeypatch, payload, status):
    client, calls, _ = install(monkeypatch, payload, status=status)
    with pytest.raises(mod.requests.HTTPError, match=str(status)):
        client.get_ols_properties("CHEBI:15377")
    assert len(calls) == 1


def test_network_failure_propagates_as_provider_failure(monkeypatch, payload):
    client, _, _ = install(monkeypatch, payload)

    def failed(*args, **kwargs):
        raise mod.requests.ConnectionError("fixture refusal")

    monkeypatch.setattr(mod.requests, "get", failed)
    with pytest.raises(mod.requests.ConnectionError, match="fixture refusal"):
        client.get_ols_properties("CHEBI:15377")


def test_import_does_not_create_legacy_cache(tmp_path):
    source = Path(mod.__file__).resolve()
    code = f"""
import pathlib, sys
sys.dont_write_bytecode = True
sys.path.insert(0, {str(source.parents[2])!r})
def refused(*args, **kwargs):
    raise AssertionError('Import attempted to create a directory')
pathlib.Path.mkdir = refused
from mediaingredientmech.utils.chemical_properties_client import ChemicalPropertiesClient
ChemicalPropertiesClient(cache_enabled=False)
"""
    result = subprocess.run(
        [sys.executable, "-B", "-c", code], cwd=tmp_path, capture_output=True, text=True
    )
    assert result.returncode == 0, result.stderr


def test_legacy_client_contract_remains_separate(monkeypatch, payload):
    """An explicitly raw retrieval can still merge PubChem; strict retrieval cannot."""
    client = mod.ChemicalPropertiesClient(cache_enabled=False)
    source = mod.ChemicalProperties(molecular_formula="H2O", data_source="ChEBI")
    monkeypatch.setattr(client, "_get_chebi_properties", lambda *args: copy.deepcopy(source))
    monkeypatch.setattr(
        client, "_get_pubchem_properties", lambda *args: mod.ChemicalProperties(smiles="O")
    )
    props = client.get_properties("CHEBI:15377", "water", "CHEBI")
    assert props.smiles == "O" and props.data_source == "ChEBI+PubChem"


def test_archived_dihydrate_term_derived_from_exact_list_response(monkeypatch):
    path = Path(__file__).parent / "fixtures/chemical_properties/ols-91258-list.json"
    original = path.read_bytes()
    assert (
        hashlib.sha256(original).hexdigest()
        == "e14e1a91519d14765d91d25ca145a56376d176814c62df304f78116dd4ad9278"
    )
    terms = json.loads(original)["_embedded"]["terms"]
    assert len(terms) == 1
    # Explicit derived endpoint fixture, not an archived exact-endpoint response.
    raw = json.dumps(terms[0], sort_keys=True).encode()
    client, _, _ = install(monkeypatch, raw=raw)
    envelope = client.get_ols_properties("CHEBI:91258")
    assert envelope is not None
    assert envelope.label == "disodium hydrogenphosphate dihydrate"
    assert envelope.response_sha256 == hashlib.sha256(raw).hexdigest()
    properties = envelope.to_dict()
    assert properties["molecular_formula"] == "2H2O.HO4P.2Na"
    assert properties["smiles"] == "O.O.O=P([O-])([O-])O.[Na+].[Na+]"
    assert properties["inchi"].startswith("InChI=1S/2Na.H3O4P.2H2O/")
    assert "inchi_key_string" not in properties and "monoisotopic_mass" not in properties
