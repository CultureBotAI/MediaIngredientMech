"""Tests for MediaIngredientMech schema loading, enums, required fields, and patterns."""

import re
import tempfile
from pathlib import Path

import pytest
import yaml

SCHEMA_PATH = Path(__file__).parent.parent / "src" / "mediaingredientmech" / "schema" / "mediaingredientmech.yaml"
FIXTURES_DIR = Path(__file__).parent / "fixtures"


def load_schema():
    """Load and return the schema YAML."""
    with open(SCHEMA_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


class TestSchemaLoading:
    """Test that the schema YAML loads and has expected top-level structure."""

    def setup_method(self):
        self.schema = load_schema()

    def test_schema_loads_successfully(self):
        assert self.schema is not None
        assert isinstance(self.schema, dict)

    def test_schema_has_id(self):
        assert "id" in self.schema
        assert "mediaingredientmech" in self.schema["id"]

    def test_schema_has_name(self):
        assert self.schema["name"] == "mediaingredientmech-schema"

    def test_schema_has_classes(self):
        assert "classes" in self.schema
        assert isinstance(self.schema["classes"], dict)

    def test_schema_has_enums(self):
        assert "enums" in self.schema
        assert isinstance(self.schema["enums"], dict)

    def test_schema_imports_linkml_types(self):
        assert "imports" in self.schema
        assert "linkml:types" in self.schema["imports"]

    def test_schema_has_prefixes(self):
        prefixes = self.schema.get("prefixes", {})
        assert "CHEBI" in prefixes
        assert "FOODON" in prefixes
        assert "linkml" in prefixes


class TestSchemaClasses:
    """Test that expected classes are defined with correct attributes."""

    def setup_method(self):
        self.schema = load_schema()
        self.classes = self.schema["classes"]

    def test_ingredient_collection_exists(self):
        assert "IngredientCollection" in self.classes

    def test_ingredient_collection_is_tree_root(self):
        assert self.classes["IngredientCollection"].get("tree_root") is True

    def test_ingredient_collection_has_ingredients_attr(self):
        attrs = self.classes["IngredientCollection"]["attributes"]
        assert "ingredients" in attrs
        ing = attrs["ingredients"]
        assert ing["range"] == "IngredientRecord"
        assert ing["multivalued"] is True

    def test_ingredient_collection_has_count_attrs(self):
        attrs = self.classes["IngredientCollection"]["attributes"]
        assert "total_count" in attrs
        assert "mapped_count" in attrs
        assert "unmapped_count" in attrs

    def test_ingredient_record_exists(self):
        assert "IngredientRecord" in self.classes

    def test_ingredient_record_required_fields(self):
        attrs = self.classes["IngredientRecord"]["attributes"]
        assert attrs["ontology_id"].get("required") is True
        assert attrs["preferred_term"].get("required") is True
        assert attrs["mapping_status"].get("required") is True

    def test_ingredient_record_identifier_is_key(self):
        attrs = self.classes["IngredientRecord"]["attributes"]
        assert attrs["ontology_id"].get("ontology_id") is True

    def test_ingredient_record_has_synonyms(self):
        attrs = self.classes["IngredientRecord"]["attributes"]
        syn = attrs["synonyms"]
        assert syn["range"] == "IngredientSynonym"
        assert syn["multivalued"] is True

    def test_ingredient_record_has_curation_history(self):
        attrs = self.classes["IngredientRecord"]["attributes"]
        hist = attrs["curation_history"]
        assert hist["range"] == "CurationEvent"
        assert hist["multivalued"] is True

    def test_ontology_mapping_exists(self):
        assert "OntologyMapping" in self.classes

    def test_ontology_mapping_required_fields(self):
        attrs = self.classes["OntologyMapping"]["attributes"]
        for field in ["ontology_id", "ontology_label", "ontology_source", "mapping_quality"]:
            assert attrs[field].get("required") is True, f"{field} should be required"

    def test_ontology_id_has_pattern(self):
        attrs = self.classes["OntologyMapping"]["attributes"]
        pattern = attrs["ontology_id"].get("pattern")
        assert pattern is not None, "ontology_id should have a pattern constraint"
        assert "^" in pattern and "$" in pattern

    def test_mapping_evidence_exists(self):
        assert "MappingEvidence" in self.classes

    def test_mapping_evidence_required_fields(self):
        attrs = self.classes["MappingEvidence"]["attributes"]
        assert attrs["evidence_type"].get("required") is True

    def test_ingredient_synonym_exists(self):
        assert "IngredientSynonym" in self.classes

    def test_ingredient_synonym_required_fields(self):
        attrs = self.classes["IngredientSynonym"]["attributes"]
        assert attrs["synonym_text"].get("required") is True

    def test_occurrence_stats_exists(self):
        assert "OccurrenceStats" in self.classes

    def test_occurrence_stats_required_fields(self):
        attrs = self.classes["OccurrenceStats"]["attributes"]
        assert attrs["total_occurrences"].get("required") is True
        assert attrs["media_count"].get("required") is True

    def test_curation_event_exists(self):
        assert "CurationEvent" in self.classes

    def test_curation_event_required_fields(self):
        attrs = self.classes["CurationEvent"]["attributes"]
        for field in ["timestamp", "curator", "action"]:
            assert attrs[field].get("required") is True, f"{field} should be required"

    def test_curation_event_has_llm_fields(self):
        attrs = self.classes["CurationEvent"]["attributes"]
        assert "llm_assisted" in attrs
        assert attrs["llm_assisted"]["range"] == "boolean"
        assert "llm_model" in attrs

    def test_all_expected_classes_present(self):
        expected = [
            "IngredientCollection",
            "IngredientRecord",
            "OntologyMapping",
            "MappingEvidence",
            "IngredientSynonym",
            "OccurrenceStats",
            "CurationEvent",
        ]
        for cls_name in expected:
            assert cls_name in self.classes, f"Class {cls_name} missing from schema"


class TestSchemaEnums:
    """Test that all enums have expected values."""

    def setup_method(self):
        self.schema = load_schema()
        self.enums = self.schema["enums"]

    def test_mapping_status_enum_exists(self):
        assert "MappingStatusEnum" in self.enums

    def test_mapping_status_values(self):
        values = set(self.enums["MappingStatusEnum"]["permissible_values"].keys())
        expected = {"MAPPED", "UNMAPPED", "PENDING_REVIEW", "IN_PROGRESS", "NEEDS_EXPERT", "AMBIGUOUS", "REJECTED"}
        assert values == expected

    def test_mapping_quality_enum_exists(self):
        assert "MappingQualityEnum" in self.enums

    def test_mapping_quality_values(self):
        values = set(self.enums["MappingQualityEnum"]["permissible_values"].keys())
        expected = {"EXACT_MATCH", "SYNONYM_MATCH", "CLOSE_MATCH", "MANUAL_CURATION", "LLM_ASSISTED", "PROVISIONAL"}
        assert values == expected

    def test_ontology_source_enum_exists(self):
        assert "OntologySourceEnum" in self.enums

    def test_ontology_source_values(self):
        values = set(self.enums["OntologySourceEnum"]["permissible_values"].keys())
        expected = {"CHEBI", "FOODON", "NCIT", "MESH", "UBERON", "ENVO"}
        assert values == expected

    def test_curation_action_enum_exists(self):
        assert "CurationActionEnum" in self.enums

    def test_curation_action_values(self):
        values = set(self.enums["CurationActionEnum"]["permissible_values"].keys())
        expected = {
            "CREATED", "IMPORTED", "MAPPED", "SYNONYM_ADDED",
            "VALIDATED", "CORRECTED", "MERGED", "STATUS_CHANGED", "ANNOTATED",
        }
        assert values == expected

    def test_synonym_type_enum_exists(self):
        assert "SynonymTypeEnum" in self.enums

    def test_synonym_type_values(self):
        values = set(self.enums["SynonymTypeEnum"]["permissible_values"].keys())
        expected = {"EXACT_SYNONYM", "RELATED_SYNONYM", "RAW_TEXT", "ABBREVIATION", "COMMON_NAME", "SYSTEMATIC_NAME"}
        assert values == expected

    def test_evidence_type_enum_exists(self):
        assert "EvidenceTypeEnum" in self.enums

    def test_evidence_type_values(self):
        values = set(self.enums["EvidenceTypeEnum"]["permissible_values"].keys())
        expected = {"DATABASE_MATCH", "CURATOR_JUDGMENT", "LLM_SUGGESTION", "LITERATURE", "TEXT_SIMILARITY", "CROSS_REFERENCE"}
        assert values == expected

    def test_all_enum_values_have_descriptions(self):
        for enum_name, enum_def in self.enums.items():
            for val_name, val_def in enum_def["permissible_values"].items():
                assert val_def.get("description"), (
                    f"Enum {enum_name}.{val_name} missing description"
                )


class TestOntologyIdPattern:
    """Test the ontology ID pattern constraint from the schema."""

    def setup_method(self):
        schema = load_schema()
        attrs = schema["classes"]["OntologyMapping"]["attributes"]
        self.pattern = re.compile(attrs["ontology_id"]["pattern"])

    @pytest.mark.parametrize("valid_id", [
        "CHEBI:26710",
        "CHEBI:15377",
        "FOODON:3311109",
        "NCIT:12345",
        "MESH:67890",
        "UBERON:0001234",
        "ENVO:00002001",
    ])
    def test_valid_ontology_ids(self, valid_id):
        assert self.pattern.match(valid_id), f"{valid_id} should match pattern"

    @pytest.mark.parametrize("invalid_id", [
        "chebi:26710",
        "CHEBI-26710",
        "CHEBI26710",
        "CHEBI:",
        ":26710",
        "CHEBI:abc",
        "",
        "http://purl.obolibrary.org/obo/CHEBI_26710",
    ])
    def test_invalid_ontology_ids(self, invalid_id):
        assert not self.pattern.match(invalid_id), f"{invalid_id} should NOT match pattern"


class TestFixtureDataValidation:
    """Validate that fixture YAML files conform to schema structure."""

    def setup_method(self):
        self.schema = load_schema()
        self.enum_values = {}
        for enum_name, enum_def in self.schema["enums"].items():
            self.enum_values[enum_name] = set(enum_def["permissible_values"].keys())

        self.ontology_id_pattern = re.compile(
            self.schema["classes"]["OntologyMapping"]["attributes"]["ontology_id"]["pattern"]
        )

    def _load_fixture(self, filename):
        with open(FIXTURES_DIR / filename, encoding="utf-8") as f:
            return yaml.safe_load(f)

    def test_mapped_fixture_loads(self):
        data = self._load_fixture("sample_mapped.yaml")
        assert "ingredients" in data
        assert len(data["ingredients"]) == 10

    def test_unmapped_fixture_loads(self):
        data = self._load_fixture("sample_unmapped.yaml")
        assert "ingredients" in data
        assert len(data["ingredients"]) == 10

    def test_invalid_fixture_loads(self):
        data = self._load_fixture("invalid_records.yaml")
        assert data is not None
        assert isinstance(data, dict)

    def test_mapped_records_have_required_fields(self):
        data = self._load_fixture("sample_mapped.yaml")
        for rec in data["ingredients"]:
            assert "ontology_id" in rec, f"Record missing identifier: {rec}"
            assert "preferred_term" in rec, f"Record missing preferred_term: {rec}"
            assert "mapping_status" in rec, f"Record missing mapping_status: {rec}"

    def test_mapped_records_have_valid_status(self):
        data = self._load_fixture("sample_mapped.yaml")
        for rec in data["ingredients"]:
            assert rec["mapping_status"] in self.enum_values["MappingStatusEnum"], (
                f"Invalid status {rec['mapping_status']} in {rec['identifier']}"
            )

    def test_mapped_records_have_ontology_mappings(self):
        data = self._load_fixture("sample_mapped.yaml")
        for rec in data["ingredients"]:
            assert rec["mapping_status"] == "MAPPED"
            assert "ontology_mapping" in rec, f"Mapped record {rec['identifier']} missing ontology_mapping"

    def test_mapped_ontology_ids_match_pattern(self):
        data = self._load_fixture("sample_mapped.yaml")
        for rec in data["ingredients"]:
            ont = rec["ontology_mapping"]
            assert self.ontology_id_pattern.match(ont["ontology_id"]), (
                f"Invalid ontology_id format: {ont['ontology_id']}"
            )

    def test_mapped_ontology_sources_valid(self):
        data = self._load_fixture("sample_mapped.yaml")
        for rec in data["ingredients"]:
            ont = rec["ontology_mapping"]
            assert ont["ontology_source"] in self.enum_values["OntologySourceEnum"], (
                f"Invalid source: {ont['ontology_source']}"
            )

    def test_mapped_quality_values_valid(self):
        data = self._load_fixture("sample_mapped.yaml")
        for rec in data["ingredients"]:
            ont = rec["ontology_mapping"]
            assert ont["mapping_quality"] in self.enum_values["MappingQualityEnum"], (
                f"Invalid quality: {ont['mapping_quality']}"
            )

    def test_unmapped_records_have_varied_statuses(self):
        data = self._load_fixture("sample_unmapped.yaml")
        statuses = {rec["mapping_status"] for rec in data["ingredients"]}
        assert len(statuses) >= 3, "Unmapped fixture should cover multiple status values"

    def test_all_synonym_types_valid(self):
        for fixture_file in ["sample_mapped.yaml", "sample_unmapped.yaml"]:
            data = self._load_fixture(fixture_file)
            for rec in data["ingredients"]:
                for syn in rec.get("synonyms", []):
                    if "synonym_type" in syn:
                        assert syn["synonym_type"] in self.enum_values["SynonymTypeEnum"], (
                            f"Invalid synonym type: {syn['synonym_type']} in {rec['identifier']}"
                        )

    def test_all_evidence_types_valid(self):
        for fixture_file in ["sample_mapped.yaml", "sample_unmapped.yaml"]:
            data = self._load_fixture(fixture_file)
            for rec in data["ingredients"]:
                ont = rec.get("ontology_mapping", {})
                for ev in ont.get("evidence", []):
                    assert ev["evidence_type"] in self.enum_values["EvidenceTypeEnum"], (
                        f"Invalid evidence type: {ev['evidence_type']} in {rec['identifier']}"
                    )

    def test_all_curation_actions_valid(self):
        for fixture_file in ["sample_mapped.yaml", "sample_unmapped.yaml"]:
            data = self._load_fixture(fixture_file)
            for rec in data["ingredients"]:
                for event in rec.get("curation_history", []):
                    assert event["action"] in self.enum_values["CurationActionEnum"], (
                        f"Invalid action: {event['action']} in {rec['identifier']}"
                    )
