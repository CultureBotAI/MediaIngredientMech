"""Tests for curation workflow: import transformation, state transitions, synonym management, history."""

import copy
import re
import tempfile
from datetime import datetime
from pathlib import Path

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


def get_enum_values(schema, enum_name):
    return set(schema["enums"][enum_name]["permissible_values"].keys())


class TestImportTransformation:
    """Test transforming CultureMech ingredient data into MediaIngredientMech format."""

    def setup_method(self):
        self.schema = load_schema()
        self.temp_dir = tempfile.mkdtemp()

    def _create_culturemech_ingredient(self, **overrides):
        """Create a CultureMech-style ingredient dict."""
        base = {
            "preferred_term": "sodium chloride",
            "term": {"id": "CHEBI:26710", "label": "sodium chloride"},
        }
        base.update(overrides)
        return base

    def _transform_to_ingredient_record(self, cm_ingredient):
        """Simulate import transformation from CultureMech to MediaIngredientMech format."""
        term = cm_ingredient.get("term", {})
        term_id = term.get("id", "")
        has_mapping = bool(term_id)

        record = {
            "ontology_id": term_id if has_mapping else f"UNMAPPED_{id(cm_ingredient) % 10000:04d}",
            "preferred_term": cm_ingredient["preferred_term"],
            "mapping_status": "MAPPED" if has_mapping else "UNMAPPED",
        }

        if has_mapping:
            # Determine ontology source from prefix
            prefix = term_id.split(":")[0] if ":" in term_id else ""
            record["ontology_mapping"] = {
                "ontology_id": term_id,
                "ontology_label": term.get("label", ""),
                "ontology_source": prefix if prefix in get_enum_values(self.schema, "OntologySourceEnum") else "CHEBI",
                "mapping_quality": "EXACT_MATCH",
                "evidence": [
                    {
                        "evidence_type": "DATABASE_MATCH",
                        "source": "CultureMech import",
                        "confidence_score": 1.0,
                    }
                ],
            }

        record["curation_history"] = [
            {
                "timestamp": datetime.now().isoformat(),
                "curator": "auto-import",
                "action": "IMPORTED",
                "changes": "Imported from CultureMech",
                "new_status": record["mapping_status"],
            }
        ]

        return record

    def test_mapped_ingredient_transforms(self):
        cm = self._create_culturemech_ingredient()
        record = self._transform_to_ingredient_record(cm)
        assert record["ontology_id"] == "CHEBI:26710"
        assert record["mapping_status"] == "MAPPED"
        assert record["ontology_mapping"]["ontology_id"] == "CHEBI:26710"

    def test_unmapped_ingredient_transforms(self):
        cm = self._create_culturemech_ingredient(term={})
        record = self._transform_to_ingredient_record(cm)
        assert record["ontology_id"].startswith("UNMAPPED_")
        assert record["mapping_status"] == "UNMAPPED"
        assert "ontology_mapping" not in record

    def test_import_creates_curation_history(self):
        cm = self._create_culturemech_ingredient()
        record = self._transform_to_ingredient_record(cm)
        assert len(record["curation_history"]) == 1
        event = record["curation_history"][0]
        assert event["curator"] == "auto-import"
        assert event["action"] == "IMPORTED"

    def test_import_preserves_preferred_term(self):
        cm = self._create_culturemech_ingredient(preferred_term="D-glucose")
        record = self._transform_to_ingredient_record(cm)
        assert record["preferred_term"] == "D-glucose"

    def test_foodon_source_detected(self):
        cm = self._create_culturemech_ingredient(
            term={"id": "FOODON:3311109", "label": "beef extract"}
        )
        record = self._transform_to_ingredient_record(cm)
        assert record["ontology_mapping"]["ontology_source"] == "FOODON"

    def test_transform_output_validates_against_schema(self):
        """Check that transformed record has all required fields from schema."""
        cm = self._create_culturemech_ingredient()
        record = self._transform_to_ingredient_record(cm)

        required_attrs = self.schema["classes"]["IngredientRecord"]["attributes"]
        for attr_name, attr_def in required_attrs.items():
            if attr_def.get("required"):
                assert attr_name in record, f"Missing required field: {attr_name}"

    def test_batch_transform(self):
        """Transform a batch of ingredients."""
        ingredients = [
            self._create_culturemech_ingredient(preferred_term="NaCl"),
            self._create_culturemech_ingredient(preferred_term="glucose", term={"id": "CHEBI:17234", "label": "glucose"}),
            self._create_culturemech_ingredient(preferred_term="mystery extract", term={}),
        ]
        records = [self._transform_to_ingredient_record(cm) for cm in ingredients]
        assert len(records) == 3
        mapped = [r for r in records if r["mapping_status"] == "MAPPED"]
        unmapped = [r for r in records if r["mapping_status"] == "UNMAPPED"]
        assert len(mapped) == 2
        assert len(unmapped) == 1


class TestCurationStateTransitions:
    """Test valid and invalid state transitions for mapping status."""

    VALID_TRANSITIONS = {
        "UNMAPPED": {"PENDING_REVIEW", "IN_PROGRESS", "NEEDS_EXPERT", "MAPPED", "REJECTED"},
        "PENDING_REVIEW": {"MAPPED", "REJECTED", "IN_PROGRESS", "NEEDS_EXPERT", "AMBIGUOUS"},
        "IN_PROGRESS": {"MAPPED", "PENDING_REVIEW", "NEEDS_EXPERT", "AMBIGUOUS", "REJECTED"},
        "NEEDS_EXPERT": {"IN_PROGRESS", "MAPPED", "PENDING_REVIEW", "REJECTED"},
        "AMBIGUOUS": {"IN_PROGRESS", "MAPPED", "NEEDS_EXPERT", "REJECTED"},
        "MAPPED": {"PENDING_REVIEW", "REJECTED"},
        "REJECTED": {"UNMAPPED", "IN_PROGRESS"},
    }

    def _apply_transition(self, record, new_status, curator="test-curator"):
        """Simulate a status transition on a record."""
        old_status = record["mapping_status"]
        record = copy.deepcopy(record)
        record["mapping_status"] = new_status
        if "curation_history" not in record:
            record["curation_history"] = []
        record["curation_history"].append({
            "timestamp": datetime.now().isoformat(),
            "curator": curator,
            "action": "STATUS_CHANGED",
            "previous_status": old_status,
            "new_status": new_status,
            "changes": f"Status changed from {old_status} to {new_status}",
        })
        return record

    def _make_record(self, status="UNMAPPED"):
        return {
            "ontology_id": "TEST:001",
            "preferred_term": "test ingredient",
            "mapping_status": status,
        }

    def test_unmapped_to_pending_review(self):
        record = self._apply_transition(self._make_record("UNMAPPED"), "PENDING_REVIEW")
        assert record["mapping_status"] == "PENDING_REVIEW"
        assert record["curation_history"][-1]["previous_status"] == "UNMAPPED"

    def test_unmapped_to_mapped(self):
        record = self._apply_transition(self._make_record("UNMAPPED"), "MAPPED")
        assert record["mapping_status"] == "MAPPED"

    def test_pending_review_to_mapped(self):
        record = self._apply_transition(self._make_record("PENDING_REVIEW"), "MAPPED")
        assert record["mapping_status"] == "MAPPED"

    def test_pending_review_to_rejected(self):
        record = self._apply_transition(self._make_record("PENDING_REVIEW"), "REJECTED")
        assert record["mapping_status"] == "REJECTED"

    def test_in_progress_to_mapped(self):
        record = self._apply_transition(self._make_record("IN_PROGRESS"), "MAPPED")
        assert record["mapping_status"] == "MAPPED"

    def test_mapped_to_pending_review(self):
        record = self._apply_transition(self._make_record("MAPPED"), "PENDING_REVIEW")
        assert record["mapping_status"] == "PENDING_REVIEW"

    def test_rejected_to_unmapped(self):
        record = self._apply_transition(self._make_record("REJECTED"), "UNMAPPED")
        assert record["mapping_status"] == "UNMAPPED"

    @pytest.mark.parametrize("from_status,to_status", [
        ("UNMAPPED", "PENDING_REVIEW"),
        ("PENDING_REVIEW", "MAPPED"),
        ("IN_PROGRESS", "NEEDS_EXPERT"),
        ("NEEDS_EXPERT", "MAPPED"),
        ("AMBIGUOUS", "IN_PROGRESS"),
        ("MAPPED", "REJECTED"),
        ("REJECTED", "UNMAPPED"),
    ])
    def test_valid_transitions(self, from_status, to_status):
        assert to_status in self.VALID_TRANSITIONS[from_status], (
            f"Transition {from_status} -> {to_status} should be valid"
        )

    def test_transition_records_history(self):
        record = self._make_record("UNMAPPED")
        record = self._apply_transition(record, "IN_PROGRESS", curator="curator-a")
        record = self._apply_transition(record, "MAPPED", curator="curator-b")
        assert len(record["curation_history"]) == 2
        assert record["curation_history"][0]["curator"] == "curator-a"
        assert record["curation_history"][1]["curator"] == "curator-b"
        assert record["curation_history"][1]["previous_status"] == "IN_PROGRESS"
        assert record["curation_history"][1]["new_status"] == "MAPPED"

    def test_all_statuses_have_transitions(self):
        """Every status should have at least one valid transition."""
        statuses = get_enum_values(load_schema(), "MappingStatusEnum")
        for status in statuses:
            assert status in self.VALID_TRANSITIONS, f"No transitions defined for {status}"
            assert len(self.VALID_TRANSITIONS[status]) > 0


class TestSynonymManagement:
    """Test adding, removing, and managing synonyms on ingredient records."""

    def _make_record_with_synonyms(self):
        return {
            "ontology_id": "CHEBI:26710",
            "preferred_term": "sodium chloride",
            "mapping_status": "MAPPED",
            "synonyms": [
                {"synonym_text": "NaCl", "synonym_type": "ABBREVIATION", "source": "common usage", "occurrence_count": 150},
                {"synonym_text": "table salt", "synonym_type": "COMMON_NAME", "source": "common usage", "occurrence_count": 10},
            ],
        }

    def test_add_synonym(self):
        record = self._make_record_with_synonyms()
        new_syn = {"synonym_text": "halite", "synonym_type": "RELATED_SYNONYM", "source": "mineral name"}
        record["synonyms"].append(new_syn)
        assert len(record["synonyms"]) == 3
        texts = [s["synonym_text"] for s in record["synonyms"]]
        assert "halite" in texts

    def test_remove_synonym(self):
        record = self._make_record_with_synonyms()
        record["synonyms"] = [s for s in record["synonyms"] if s["synonym_text"] != "table salt"]
        assert len(record["synonyms"]) == 1
        assert record["synonyms"][0]["synonym_text"] == "NaCl"

    def test_no_duplicate_synonyms(self):
        record = self._make_record_with_synonyms()
        existing_texts = {s["synonym_text"] for s in record["synonyms"]}
        new_syn = {"synonym_text": "NaCl", "synonym_type": "ABBREVIATION"}
        if new_syn["synonym_text"] not in existing_texts:
            record["synonyms"].append(new_syn)
        assert len(record["synonyms"]) == 2  # Should not add duplicate

    def test_synonym_types_valid(self):
        schema = load_schema()
        valid_types = get_enum_values(schema, "SynonymTypeEnum")
        record = self._make_record_with_synonyms()
        for syn in record["synonyms"]:
            assert syn["synonym_type"] in valid_types

    def test_synonym_occurrence_count_tracking(self):
        record = self._make_record_with_synonyms()
        nacl_syn = next(s for s in record["synonyms"] if s["synonym_text"] == "NaCl")
        assert nacl_syn["occurrence_count"] == 150
        nacl_syn["occurrence_count"] += 5
        assert nacl_syn["occurrence_count"] == 155

    def test_raw_text_synonym(self):
        """Raw text from original data should be tagged as RAW_TEXT."""
        record = self._make_record_with_synonyms()
        raw = {"synonym_text": "sodium chloride (NaCl) reagent grade", "synonym_type": "RAW_TEXT", "source": "recipe"}
        record["synonyms"].append(raw)
        raw_syns = [s for s in record["synonyms"] if s["synonym_type"] == "RAW_TEXT"]
        assert len(raw_syns) == 1

    def test_empty_synonyms_list(self):
        record = {
            "ontology_id": "CHEBI:17996",
            "preferred_term": "chloride",
            "mapping_status": "MAPPED",
            "synonyms": [],
        }
        assert len(record["synonyms"]) == 0


class TestHistoryTracking:
    """Test curation history audit trail."""

    def _make_record(self):
        return {
            "ontology_id": "CHEBI:26710",
            "preferred_term": "sodium chloride",
            "mapping_status": "UNMAPPED",
            "curation_history": [
                {
                    "timestamp": "2024-01-15T10:30:00",
                    "curator": "auto-import",
                    "action": "IMPORTED",
                    "changes": "Imported from CultureMech",
                    "new_status": "UNMAPPED",
                }
            ],
        }

    def _add_event(self, record, action, curator="test-curator", **kwargs):
        event = {
            "timestamp": datetime.now().isoformat(),
            "curator": curator,
            "action": action,
        }
        event.update(kwargs)
        record["curation_history"].append(event)
        return record

    def test_initial_history_on_import(self):
        record = self._make_record()
        assert len(record["curation_history"]) == 1
        assert record["curation_history"][0]["action"] == "IMPORTED"

    def test_append_curation_event(self):
        record = self._make_record()
        record = self._add_event(record, "MAPPED", changes="Mapped to CHEBI:26710")
        assert len(record["curation_history"]) == 2
        assert record["curation_history"][-1]["action"] == "MAPPED"

    def test_history_preserves_order(self):
        record = self._make_record()
        record = self._add_event(record, "STATUS_CHANGED", curator="a")
        record = self._add_event(record, "MAPPED", curator="b")
        record = self._add_event(record, "VALIDATED", curator="c")
        curators = [e["curator"] for e in record["curation_history"]]
        assert curators == ["auto-import", "a", "b", "c"]

    def test_llm_assisted_tracking(self):
        record = self._make_record()
        record = self._add_event(
            record, "MAPPED",
            curator="llm-assistant",
            llm_assisted=True,
            llm_model="gpt-4",
            changes="LLM suggested mapping",
        )
        event = record["curation_history"][-1]
        assert event["llm_assisted"] is True
        assert event["llm_model"] == "gpt-4"

    def test_status_change_tracking(self):
        record = self._make_record()
        record = self._add_event(
            record, "STATUS_CHANGED",
            previous_status="UNMAPPED",
            new_status="IN_PROGRESS",
        )
        event = record["curation_history"][-1]
        assert event["previous_status"] == "UNMAPPED"
        assert event["new_status"] == "IN_PROGRESS"

    def test_all_curation_actions_valid(self):
        schema = load_schema()
        valid_actions = get_enum_values(schema, "CurationActionEnum")
        record = self._make_record()
        for action in valid_actions:
            self._add_event(record, action)
        actions_used = {e["action"] for e in record["curation_history"]}
        assert valid_actions.issubset(actions_used)

    def test_history_from_fixture(self):
        """Verify curation history in the unmapped fixture has proper structure."""
        data = load_fixture("sample_unmapped.yaml")
        # Find record with rich history (casamino acids)
        casamino = next(r for r in data["ingredients"] if r["ontology_id"] == "UNMAPPED_005")
        assert len(casamino["curation_history"]) == 2
        assert casamino["curation_history"][0]["action"] == "IMPORTED"
        assert casamino["curation_history"][1]["action"] == "MAPPED"
        assert casamino["curation_history"][1].get("llm_assisted") is True

    def test_mapped_fixture_beef_extract_history(self):
        """Beef extract in mapped fixture should show full workflow."""
        data = load_fixture("sample_mapped.yaml")
        beef = next(r for r in data["ingredients"] if r["ontology_id"] == "FOODON:3311109")
        assert len(beef["curation_history"]) == 3
        actions = [e["action"] for e in beef["curation_history"]]
        assert actions == ["IMPORTED", "MAPPED", "VALIDATED"]


class TestCollectionAggregation:
    """Test IngredientCollection-level operations."""

    def test_count_mapped_unmapped(self):
        mapped_data = load_fixture("sample_mapped.yaml")
        unmapped_data = load_fixture("sample_unmapped.yaml")
        all_ingredients = mapped_data["ingredients"] + unmapped_data["ingredients"]

        mapped_count = sum(1 for r in all_ingredients if r["mapping_status"] == "MAPPED")
        unmapped_count = sum(1 for r in all_ingredients if r["mapping_status"] != "MAPPED")

        collection = {
            "generation_date": datetime.now().isoformat(),
            "total_count": len(all_ingredients),
            "mapped_count": mapped_count,
            "unmapped_count": unmapped_count,
            "ingredients": all_ingredients,
        }

        assert collection["total_count"] == 20
        assert collection["mapped_count"] == 10
        assert collection["unmapped_count"] == 10
        assert collection["mapped_count"] + collection["unmapped_count"] == collection["total_count"]

    def test_collection_serialization(self):
        """Test that a collection can be serialized and deserialized."""
        data = load_fixture("sample_mapped.yaml")
        collection = {
            "generation_date": "2024-03-01T00:00:00",
            "total_count": len(data["ingredients"]),
            "mapped_count": len(data["ingredients"]),
            "unmapped_count": 0,
            "ingredients": data["ingredients"],
        }
        serialized = yaml.dump(collection, default_flow_style=False)
        deserialized = yaml.safe_load(serialized)
        assert deserialized["total_count"] == collection["total_count"]
        assert len(deserialized["ingredients"]) == len(collection["ingredients"])

    def test_unique_identifiers(self):
        """All identifiers in fixtures should be unique."""
        mapped_data = load_fixture("sample_mapped.yaml")
        unmapped_data = load_fixture("sample_unmapped.yaml")
        all_ids = [r["ontology_id"] for r in mapped_data["ingredients"]] + \
                  [r["ontology_id"] for r in unmapped_data["ingredients"]]
        assert len(all_ids) == len(set(all_ids)), "Duplicate identifiers found"
