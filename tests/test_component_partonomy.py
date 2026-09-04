"""Corpus-level semantic tests for component partonomy (#369)."""

from copy import deepcopy
from pathlib import Path

import pytest

from mediaingredientmech.validation.component_partonomy import (
    load_curated_records,
    validate_component_partonomy,
)

ROOT = Path(__file__).resolve().parent.parent


def _target(status: str = "MAPPED") -> dict:
    return {
        "identifier": "CHEBI:123",
        "preferred_term": "alpha salt",
        "mapping_status": status,
        "synonyms": [{"synonym_text": "salt alpha"}],
        "ontology_mapping": {"ontology_label": "alpha compound"},
    }


def _parent() -> dict:
    return {
        "identifier": "kgmicrobe.ingredient:test_mix",
        "preferred_term": "test mix",
        "mapping_status": "MAPPED",
        "ingredient_type": "NAMED_MEDIUM",
        "components": [
            {
                "component_name": "alpha salt",
                "component_id": "CHEBI:123",
                "reference_scope": "MIM_CATALOG",
                "source": "test",
            },
            {
                "component_name": "outside substance",
                "component_id": "CHEBI:999",
                "reference_scope": "EXTERNAL_TERM",
                "source": "test",
            },
            {
                "component_name": "unnamed fraction",
                "reference_scope": "UNMAPPED",
                "source": "test",
            },
        ],
        "component_assertion": {
            "method": "LABEL_ENUMERATION",
            "completeness": "COMPLETE",
            "evidence": [{"evidence_type": "SOURCE_LABEL", "source": "test"}],
        },
    }


def _codes(records: list[dict]) -> set[str]:
    return {finding.code for finding in validate_component_partonomy(records)}


def test_local_external_and_unmapped_references_are_distinct_valid_cases():
    assert validate_component_partonomy([_target(), _parent()]) == []


def test_assertion_and_composite_parent_invariants():
    parent = _parent()
    parent.pop("component_assertion")
    parent["ingredient_type"] = "SINGLE_INGREDIENT"
    assert {"MISSING_ASSERTION", "INVALID_PARENT_TYPE"} <= _codes([_target(), parent])

    orphan = _parent()
    orphan.pop("components")
    assert "ORPHAN_ASSERTION" in _codes([_target(), orphan])


def test_reference_scope_resolution_and_curie_shape():
    parent = _parent()
    parent["components"][0]["component_id"] = "CHEBI 123"
    assert {"MALFORMED_CURIE", "UNRESOLVED_MIM_REFERENCE"} <= _codes([_target(), parent])

    rejected_only = _target("REJECTED")
    assert "UNRESOLVED_MIM_REFERENCE" in _codes([rejected_only, _parent()])

    stale_external = _parent()
    stale_external["components"][1].update(
        {"component_name": "alpha salt", "component_id": "CHEBI:123"}
    )
    assert "STALE_EXTERNAL_SCOPE" in _codes([_target(), stale_external])


def test_local_reference_name_must_match_a_target_surface():
    parent = _parent()
    parent["components"][0]["component_name"] = "wrong material"
    assert "REFERENCE_LABEL_MISMATCH" in _codes([_target(), parent])

    for valid_surface in ("salt alpha", "alpha compound"):
        parent = _parent()
        parent["components"][0]["component_name"] = valid_surface
        assert "REFERENCE_LABEL_MISMATCH" not in _codes([_target(), parent])


def test_self_and_duplicate_parts_are_rejected_by_id_and_name():
    parent = _parent()
    parent["identifier"] = "CHEBI:123"
    parent["preferred_term"] = "alpha salt"
    assert {"SELF_REFERENCE", "SELF_REFERENCE_NAME"} <= _codes([_target(), parent])

    duplicate = _parent()
    duplicate["components"].append(deepcopy(duplicate["components"][0]))
    assert {"DUPLICATE_COMPONENT_ID", "DUPLICATE_COMPONENT_NAME"} <= _codes([_target(), duplicate])


def test_concentration_value_and_unit_must_be_paired():
    for lone_key, value in (("concentration_value", "1.5"), ("concentration_unit", "G_PER_L")):
        parent = _parent()
        parent["components"][0][lone_key] = value
        assert "INCOMPLETE_CONCENTRATION" in _codes([_target(), parent])


def test_assertion_evidence_source_is_nonblank():
    parent = _parent()
    parent["component_assertion"]["evidence"][0]["source"] = ""
    assert "BLANK_EVIDENCE_SOURCE" in _codes([_target(), parent])


def test_real_curated_corpus_has_no_partonomy_violations():
    records = load_curated_records(ROOT / "data" / "curated")
    assert validate_component_partonomy(records) == []
    parents = [record for record in records if record.get("components")]
    assert len(parents) == 60
    assert sum(len(record["components"]) for record in parents) == 209


def test_curated_loader_reports_missing_and_invalid_yaml(tmp_path):
    with pytest.raises(OSError):
        load_curated_records(tmp_path)

    (tmp_path / "mapped_ingredients.yaml").write_text("ingredients: [\n", encoding="utf-8")
    (tmp_path / "unmapped_ingredients.yaml").write_text("ingredients: []\n", encoding="utf-8")
    with pytest.raises(ValueError, match="invalid YAML"):
        load_curated_records(tmp_path)
