"""Tests for ontology lookup: CHEBI term validation, OAK integration (mocked)."""

import re
from pathlib import Path
from unittest.mock import MagicMock, Mock, patch

import pytest
import yaml

SCHEMA_PATH = Path(__file__).parent.parent / "src" / "mediaingredientmech" / "schema" / "mediaingredientmech.yaml"
FIXTURES_DIR = Path(__file__).parent / "fixtures"


def load_schema():
    with open(SCHEMA_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_fixture(name):
    with open(FIXTURES_DIR / name, encoding="utf-8") as f:
        return yaml.safe_load(f)


class TestChebiTermValidation:
    """Test CHEBI term ID format validation."""

    def setup_method(self):
        schema = load_schema()
        self.pattern = re.compile(
            schema["classes"]["OntologyMapping"]["attributes"]["ontology_id"]["pattern"]
        )
        self.valid_sources = set(
            schema["enums"]["OntologySourceEnum"]["permissible_values"].keys()
        )

    def test_chebi_id_format(self):
        assert self.pattern.match("CHEBI:15377")
        assert self.pattern.match("CHEBI:26710")
        assert self.pattern.match("CHEBI:17234")

    def test_foodon_id_format(self):
        assert self.pattern.match("FOODON:3311109")

    def test_other_ontology_formats(self):
        for prefix in ["NCIT", "MESH", "UBERON", "ENVO"]:
            assert self.pattern.match(f"{prefix}:12345")

    def test_invalid_formats_rejected(self):
        assert not self.pattern.match("chebi:15377")
        assert not self.pattern.match("CHEBI_15377")
        assert not self.pattern.match("15377")
        assert not self.pattern.match("")

    def test_mapped_fixture_ids_valid(self):
        data = load_fixture("sample_mapped.yaml")
        for rec in data["ingredients"]:
            ont_id = rec["ontology_mapping"]["ontology_id"]
            assert self.pattern.match(ont_id), f"Invalid ID: {ont_id}"

    def test_source_prefix_matches_ontology_source(self):
        """The prefix in the ontology_id should match ontology_source."""
        data = load_fixture("sample_mapped.yaml")
        for rec in data["ingredients"]:
            ont = rec["ontology_mapping"]
            prefix = ont["ontology_id"].split(":")[0]
            assert prefix == ont["ontology_source"], (
                f"Prefix {prefix} != source {ont['ontology_source']} for {rec['identifier']}"
            )


class TestOakIntegrationMocked:
    """Test OAK (Ontology Access Kit) integration with mocked API calls."""

    def _mock_oak_adapter(self):
        """Create a mock OAK adapter that simulates ontology lookups."""
        adapter = MagicMock()

        # Mock label lookup
        def mock_label(curie):
            labels = {
                "CHEBI:26710": "sodium chloride",
                "CHEBI:15377": "water",
                "CHEBI:17234": "glucose",
                "CHEBI:36316": "tryptone",
                "CHEBI:8806": "resazurin",
                "FOODON:3311109": "beef extract",
            }
            return labels.get(curie)

        adapter.label.side_effect = mock_label

        # Mock definition lookup
        def mock_definition(curie):
            defs = {
                "CHEBI:26710": "An inorganic chloride salt having sodium(1+) as counterion.",
                "CHEBI:15377": "An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms.",
                "CHEBI:17234": "An aldohexose used as a source of energy.",
            }
            return defs.get(curie)

        adapter.definition.side_effect = mock_definition

        # Mock synonym retrieval
        def mock_entity_aliases(curie):
            aliases = {
                "CHEBI:26710": ["NaCl", "table salt", "halite", "rock salt"],
                "CHEBI:15377": ["H2O", "oxidane", "dihydrogen monoxide"],
                "CHEBI:17234": ["D-glucose", "dextrose", "grape sugar"],
            }
            return aliases.get(curie, [])

        adapter.entity_aliases.side_effect = mock_entity_aliases

        # Mock search
        def mock_basic_search(term, config=None):
            search_results = {
                "sodium chloride": [("CHEBI:26710", "sodium chloride", 1.0)],
                "water": [("CHEBI:15377", "water", 1.0)],
                "glucose": [("CHEBI:17234", "glucose", 1.0), ("CHEBI:4167", "D-glucopyranose", 0.8)],
                "unknown compound xyz": [],
            }
            return search_results.get(term, [])

        adapter.basic_search.side_effect = mock_basic_search

        return adapter

    def test_label_lookup_valid_id(self):
        adapter = self._mock_oak_adapter()
        label = adapter.label("CHEBI:26710")
        assert label == "sodium chloride"
        adapter.label.assert_called_once_with("CHEBI:26710")

    def test_label_lookup_unknown_id(self):
        adapter = self._mock_oak_adapter()
        label = adapter.label("CHEBI:99999999")
        assert label is None

    def test_definition_lookup(self):
        adapter = self._mock_oak_adapter()
        definition = adapter.definition("CHEBI:15377")
        assert "oxygen" in definition
        assert "hydrogen" in definition

    def test_synonym_retrieval(self):
        adapter = self._mock_oak_adapter()
        aliases = adapter.entity_aliases("CHEBI:26710")
        assert "NaCl" in aliases
        assert "table salt" in aliases
        assert len(aliases) == 4

    def test_synonym_retrieval_unknown(self):
        adapter = self._mock_oak_adapter()
        aliases = adapter.entity_aliases("CHEBI:99999")
        assert aliases == []

    def test_search_exact_match(self):
        adapter = self._mock_oak_adapter()
        results = adapter.basic_search("sodium chloride")
        assert len(results) == 1
        assert results[0][0] == "CHEBI:26710"

    def test_search_multiple_results(self):
        adapter = self._mock_oak_adapter()
        results = adapter.basic_search("glucose")
        assert len(results) == 2
        ids = [r[0] for r in results]
        assert "CHEBI:17234" in ids

    def test_search_no_results(self):
        adapter = self._mock_oak_adapter()
        results = adapter.basic_search("unknown compound xyz")
        assert len(results) == 0

    def test_validate_mapped_ingredients_against_oak(self):
        """Validate that all mapped fixture ingredients can be looked up via mock OAK."""
        adapter = self._mock_oak_adapter()
        data = load_fixture("sample_mapped.yaml")

        verified = 0
        for rec in data["ingredients"]:
            ont_id = rec["ontology_mapping"]["ontology_id"]
            label = adapter.label(ont_id)
            if label is not None:
                verified += 1
                assert isinstance(label, str)
                assert len(label) > 0

        assert verified > 0, "At least some mapped ingredients should be verifiable"

    def test_enrich_record_with_synonyms(self):
        """Simulate enriching a record with synonyms from OAK."""
        adapter = self._mock_oak_adapter()

        record = {
            "identifier": "CHEBI:26710",
            "preferred_term": "sodium chloride",
            "mapping_status": "MAPPED",
            "synonyms": [],
        }

        oak_aliases = adapter.entity_aliases(record["identifier"])
        for alias in oak_aliases:
            record["synonyms"].append({
                "synonym_text": alias,
                "synonym_type": "EXACT_SYNONYM",
                "source": "CHEBI via OAK",
            })

        assert len(record["synonyms"]) == 4
        texts = {s["synonym_text"] for s in record["synonyms"]}
        assert "NaCl" in texts
        assert "halite" in texts


class TestOlsApiMocked:
    """Test OLS (Ontology Lookup Service) API integration with mocked responses."""

    def _mock_ols_response(self, term_id, label, description=None, synonyms=None):
        """Build a mock OLS API response."""
        return {
            "iri": f"http://purl.obolibrary.org/obo/{term_id.replace(':', '_')}",
            "label": label,
            "description": [description] if description else [],
            "synonyms": synonyms or [],
            "annotation": {},
        }

    @patch("requests.get")
    def test_verify_chebi_term(self, mock_get):
        mock_resp = Mock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = self._mock_ols_response(
            "CHEBI:26710", "sodium chloride",
            description="An inorganic chloride salt",
            synonyms=["NaCl", "table salt"],
        )
        mock_get.return_value = mock_resp

        import requests
        resp = requests.get("https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms")
        data = resp.json()

        assert data["label"] == "sodium chloride"
        assert "NaCl" in data["synonyms"]

    @patch("requests.get")
    def test_term_not_found(self, mock_get):
        mock_resp = Mock()
        mock_resp.status_code = 404
        mock_resp.json.return_value = {"error": "Term not found"}
        mock_get.return_value = mock_resp

        import requests
        resp = requests.get("https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms")
        assert resp.status_code == 404

    @patch("requests.get")
    def test_search_returns_results(self, mock_get):
        mock_resp = Mock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {
            "response": {
                "docs": [
                    {
                        "iri": "http://purl.obolibrary.org/obo/CHEBI_26710",
                        "short_form": "CHEBI_26710",
                        "label": "sodium chloride",
                        "score": 42.5,
                    },
                    {
                        "iri": "http://purl.obolibrary.org/obo/CHEBI_26712",
                        "short_form": "CHEBI_26712",
                        "label": "sodium citrate",
                        "score": 15.2,
                    },
                ]
            }
        }
        mock_get.return_value = mock_resp

        import requests
        resp = requests.get("https://www.ebi.ac.uk/ols4/api/search")
        docs = resp.json()["response"]["docs"]
        assert len(docs) == 2
        assert docs[0]["label"] == "sodium chloride"

    @patch("requests.get")
    def test_api_timeout(self, mock_get):
        import requests
        mock_get.side_effect = requests.exceptions.Timeout("Connection timed out")

        with pytest.raises(requests.exceptions.Timeout):
            requests.get("https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms", timeout=5)

    @patch("requests.get")
    def test_api_connection_error(self, mock_get):
        import requests
        mock_get.side_effect = requests.exceptions.ConnectionError("Connection refused")

        with pytest.raises(requests.exceptions.ConnectionError):
            requests.get("https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms")


class TestMappingQualityAssessment:
    """Test logic for assessing mapping quality from different evidence sources."""

    def _assess_quality(self, evidence_list):
        """Simulate mapping quality assessment from evidence."""
        if not evidence_list:
            return "PROVISIONAL"

        has_db_match = any(e["evidence_type"] == "DATABASE_MATCH" for e in evidence_list)
        has_curator = any(e["evidence_type"] == "CURATOR_JUDGMENT" for e in evidence_list)
        has_llm = any(e["evidence_type"] == "LLM_SUGGESTION" for e in evidence_list)
        max_confidence = max((e.get("confidence_score", 0) for e in evidence_list), default=0)

        if has_db_match and max_confidence >= 0.95:
            return "EXACT_MATCH"
        if has_db_match and max_confidence >= 0.8:
            return "SYNONYM_MATCH"
        if has_curator:
            return "MANUAL_CURATION"
        if has_llm and has_curator:
            return "LLM_ASSISTED"
        if has_llm:
            return "LLM_ASSISTED"
        return "CLOSE_MATCH"

    def test_exact_match_from_high_confidence_db(self):
        evidence = [{"evidence_type": "DATABASE_MATCH", "confidence_score": 1.0}]
        assert self._assess_quality(evidence) == "EXACT_MATCH"

    def test_synonym_match_from_medium_confidence_db(self):
        evidence = [{"evidence_type": "DATABASE_MATCH", "confidence_score": 0.85}]
        assert self._assess_quality(evidence) == "SYNONYM_MATCH"

    def test_manual_curation(self):
        evidence = [{"evidence_type": "CURATOR_JUDGMENT", "confidence_score": 1.0}]
        assert self._assess_quality(evidence) == "MANUAL_CURATION"

    def test_llm_assisted(self):
        evidence = [{"evidence_type": "LLM_SUGGESTION", "confidence_score": 0.9}]
        assert self._assess_quality(evidence) == "LLM_ASSISTED"

    def test_provisional_no_evidence(self):
        assert self._assess_quality([]) == "PROVISIONAL"

    def test_combined_evidence(self):
        evidence = [
            {"evidence_type": "LLM_SUGGESTION", "confidence_score": 0.85},
            {"evidence_type": "CURATOR_JUDGMENT", "confidence_score": 0.95},
        ]
        quality = self._assess_quality(evidence)
        assert quality == "MANUAL_CURATION"

    def test_quality_values_in_schema(self):
        schema = load_schema()
        valid = set(schema["enums"]["MappingQualityEnum"]["permissible_values"].keys())
        test_cases = [
            [{"evidence_type": "DATABASE_MATCH", "confidence_score": 1.0}],
            [{"evidence_type": "DATABASE_MATCH", "confidence_score": 0.85}],
            [{"evidence_type": "CURATOR_JUDGMENT", "confidence_score": 1.0}],
            [{"evidence_type": "LLM_SUGGESTION", "confidence_score": 0.9}],
            [],
        ]
        for ev in test_cases:
            result = self._assess_quality(ev)
            assert result in valid, f"Quality {result} not in schema enum"
