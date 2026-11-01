"""The bounded #901 correction must preserve form identity and provisional roles."""

import copy
import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("melezitose_parent", ROOT / "scripts/correct_melezitose_parent.py")
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)


@pytest.fixture
def record():
    return {
        "identifier": "cas:10030-67-8", "preferred_term": "D-(+)-melezitose monohydrate",
        "mapping_status": "MAPPED",
        "ontology_mapping": {
            "ontology_id": "CHEBI:6731", "ontology_label": "melezitose",
            "ontology_source": "CHEBI", "mapping_quality": "CLOSE_MATCH",
            "evidence": [{"evidence_type": "DATABASE_MATCH", "source": "historical #342"}],
        },
        "chemical_properties": {"cas_rn": "10030-67-8", "molecular_formula": "C18H34O17", "pubchem_cid": 16217716},
        "synonyms": [], "occurrence_statistics": {"total_occurrences": 0, "media_count": 0},
        "nutritional_roles": [{"role": "CARBON_SOURCE", "confidence": 0.8,
                               "evidence": [{"reference_type": "COMPUTATIONAL_PREDICTION", "reference_text": "Provisional"}]}],
        "curation_history": [],
    }


def test_correction_preserves_identity_chemistry_roles_and_history(record):
    original = copy.deepcopy(record)
    result = mod.corrected_record(record, timestamp="2026-11-01T00:00:00+00:00")
    assert record == original
    for key in record.keys() - {"ontology_mapping", "curation_history"}:
        assert result[key] == original[key]
    assert result["ontology_mapping"]["mapping_quality"] == "NARROW_MATCH"
    assert result["ontology_mapping"]["evidence"][:-1] == original["ontology_mapping"]["evidence"]
    event = result["curation_history"][-1]
    assert event["curator"] == "correct_melezitose_parent.py"
    assert event["llm_model"] == "gpt-6"
    assert event["llm_assisted"] is True
    assert event["previous_status"] == event["new_status"] == "MAPPED"
    assert mod.corrected_record(result) is None


@pytest.mark.parametrize("section,key,value", [
    (None, "identifier", "cas:207511-10-2"),
    (None, "preferred_term", "D-(+)-melezitose hydrate"),
    ("ontology_mapping", "ontology_id", "CHEBI:183824"),
    ("chemical_properties", "molecular_formula", "C18H32O16"),
    ("chemical_properties", "pubchem_cid", 92817),
    ("ontology_mapping", "mapping_quality", "EXACT_MATCH"),
    ("ontology_mapping", "mapping_quality", "NARROW_MATCH"),
])
def test_rejects_different_form_parent_or_unreviewed_state(record, section, key, value):
    target = record if section is None else record[section]
    target[key] = value
    with pytest.raises(ValueError):
        mod.corrected_record(record)


def test_native_schema_gate_rejects_unexpected_field(record):
    record["invented_review_approval"] = True
    with pytest.raises(ValueError, match="closed-schema"):
        mod.corrected_record(record)
