"""Tests for chemical properties client."""

from __future__ import annotations

from datetime import datetime
from unittest.mock import MagicMock, Mock, patch

import pytest

from mediaingredientmech.utils.chemical_properties_client import (
    ChemicalProperties,
    ChemicalPropertiesClient,
)


@pytest.fixture
def client():
    """Create a client with caching disabled for tests."""
    return ChemicalPropertiesClient(cache_enabled=False)


def test_skip_non_chebi_terms(client):
    """Verify that non-CHEBI terms return None."""
    # FOODON term should be skipped
    result = client.get_properties(
        ontology_id="FOODON:00001234",
        label="some food",
        source="FOODON",
    )
    assert result is None

    # ENVO term should be skipped
    result = client.get_properties(
        ontology_id="ENVO:00001234",
        label="some environment",
        source="ENVO",
    )
    assert result is None


@patch("mediaingredientmech.utils.chemical_properties_client.requests.get")
def test_get_properties_from_ols(mock_get, client):
    """Test fetching properties from ChEBI OLS API."""
    # Mock OLS response with formula and mass
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "annotation": {
            "formula": ["H2O"],
            "mass": ["18.015"],
        }
    }
    mock_get.return_value = mock_response

    result = client.get_properties(
        ontology_id="CHEBI:15377",
        label="water",
        source="CHEBI",
    )

    assert result is not None
    assert result.molecular_formula == "H2O"
    assert result.molecular_weight == 18.015
    assert result.data_source == "ChEBI"
    assert result.retrieval_date is not None


@patch("mediaingredientmech.utils.chemical_properties_client.requests.get")
def test_get_properties_from_pubchem(mock_get, client):
    """Test fetching SMILES from PubChem API."""
    # First call: OLS returns basic properties
    ols_response = Mock()
    ols_response.status_code = 200
    ols_response.json.return_value = {
        "annotation": {
            "formula": ["H2O"],
            "mass": ["18.015"],
        }
    }

    # Second call: PubChem CID search
    pubchem_cid_response = Mock()
    pubchem_cid_response.status_code = 200
    pubchem_cid_response.json.return_value = {
        "IdentifierList": {"CID": [962]}
    }

    # Third call: PubChem properties
    pubchem_props_response = Mock()
    pubchem_props_response.status_code = 200
    pubchem_props_response.json.return_value = {
        "PropertyTable": {
            "Properties": [
                {
                    "CanonicalSMILES": "O",
                    "InChI": "InChI=1S/H2O/h1H2",
                    "MolecularWeight": 18.015,
                }
            ]
        }
    }

    # Return different responses for each call
    mock_get.side_effect = [ols_response, pubchem_cid_response, pubchem_props_response]

    result = client.get_properties(
        ontology_id="CHEBI:15377",
        label="water",
        source="CHEBI",
    )

    assert result is not None
    assert result.molecular_formula == "H2O"
    assert result.smiles == "O"
    assert result.inchi == "InChI=1S/H2O/h1H2"
    assert result.molecular_weight == 18.015
    assert result.data_source == "ChEBI+PubChem"


@patch("mediaingredientmech.utils.chemical_properties_client.requests.get")
def test_pubchem_not_found(mock_get, client):
    """Test handling PubChem 404 (not found)."""
    # First call: OLS returns basic properties
    ols_response = Mock()
    ols_response.status_code = 200
    ols_response.json.return_value = {
        "annotation": {
            "formula": ["C10H15N"],
        }
    }

    # Second call: PubChem returns 404
    pubchem_response = Mock()
    pubchem_response.status_code = 404
    pubchem_response.raise_for_status.side_effect = Exception("404 Not Found")

    mock_get.side_effect = [ols_response, pubchem_response]

    result = client.get_properties(
        ontology_id="CHEBI:99999",
        label="obscure compound",
        source="CHEBI",
    )

    # Should still have ChEBI data even without PubChem
    assert result is not None
    assert result.molecular_formula == "C10H15N"
    assert result.smiles is None
    assert result.data_source == "ChEBI"


def test_cache_hit_avoids_api_call():
    """Verify that caching works and avoids API calls."""
    # Create client with caching enabled
    client = ChemicalPropertiesClient(cache_enabled=True)

    # Mock properties
    from datetime import timezone
    mock_props = ChemicalProperties(
        molecular_formula="H2O",
        smiles="O",
        molecular_weight=18.015,
        data_source="ChEBI+PubChem",
        retrieval_date=datetime.now(timezone.utc).isoformat(),
    )

    # Manually save to cache
    ontology_id = "CHEBI:15377"
    client._save_to_cache(ontology_id, mock_props)

    # Mock requests to ensure no API calls are made
    with patch("mediaingredientmech.utils.chemical_properties_client.requests.get") as mock_get:
        result = client.get_properties(
            ontology_id=ontology_id,
            label="water",
            source="CHEBI",
        )

        # Should get cached result without API calls
        assert result is not None
        assert result.molecular_formula == "H2O"
        assert result.smiles == "O"
        assert mock_get.call_count == 0  # No API calls


@patch("mediaingredientmech.utils.chemical_properties_client.requests.get")
def test_ols_error_handling(mock_get, client):
    """Test handling of OLS API errors."""
    import requests

    # Mock a request exception
    mock_get.side_effect = requests.RequestException("Connection error")

    result = client.get_properties(
        ontology_id="CHEBI:15377",
        label="water",
        source="CHEBI",
    )

    # Should return None on error
    assert result is None


def test_chemical_properties_to_dict():
    """Test ChemicalProperties serialization to dict."""
    props = ChemicalProperties(
        molecular_formula="H2O",
        smiles="O",
        inchi="InChI=1S/H2O/h1H2",
        molecular_weight=18.015,
        data_source="ChEBI+PubChem",
        retrieval_date="2024-01-01T00:00:00Z",
    )

    result = props.to_dict()

    assert result == {
        "molecular_formula": "H2O",
        "smiles": "O",
        "inchi": "InChI=1S/H2O/h1H2",
        "molecular_weight": 18.015,
        "data_source": "ChEBI+PubChem",
        "retrieval_date": "2024-01-01T00:00:00Z",
    }


def test_chemical_properties_to_dict_partial():
    """Test ChemicalProperties serialization with missing fields."""
    props = ChemicalProperties(
        molecular_formula="H2O",
        # No SMILES, InChI, or other fields
    )

    result = props.to_dict()

    # Should only include non-None fields
    assert result == {
        "molecular_formula": "H2O",
    }
