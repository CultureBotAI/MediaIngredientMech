"""Write-time LinkML tests for typed component partonomy (#369)."""

import sys
from copy import deepcopy
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.validation.write_validated import validate_ingredient

BASE = {
    "identifier": "MICRO:0000455",
    "preferred_term": "Test trace element solution",
    "mapping_status": "MAPPED",
    "ingredient_type": "STOCK_SOLUTION",
    "ontology_mapping": {
        "ontology_id": "MICRO:0000455",
        "ontology_label": "x",
        "ontology_source": "MICRO",
        "mapping_quality": "CLOSE_MATCH",
    },
}

ASSERTION = {
    "method": "RECIPE_TRANSCRIPTION",
    "completeness": "COMPLETE",
    "evidence": [
        {
            "evidence_type": "RECIPE_SOURCE",
            "source": "example:recipe-1",
            "source_record": "stock solution A",
        }
    ],
}


def _record_with_components() -> dict:
    rec = deepcopy(BASE)
    rec["components"] = [
        {
            "component_name": "FeCl3 x 6 H2O",
            "component_id": "CHEBI:86254",
            "reference_scope": "MIM_CATALOG",
            "concentration_value": "1.5",
            "concentration_unit": "G_PER_L",
        },
        {
            "component_name": "unpublished cofactor fraction",
            "reference_scope": "UNMAPPED",
        },
    ]
    rec["component_assertion"] = deepcopy(ASSERTION)
    return rec


def _errors(record: dict) -> list:
    return validate_ingredient(record, target_class="IngredientRecord")


def test_record_without_components_valid():
    assert _errors(deepcopy(BASE)) == []


def test_typed_components_valid():
    assert _errors(_record_with_components()) == []


def test_component_name_required():
    rec = _record_with_components()
    rec["components"][0].pop("component_name")
    assert _errors(rec)


def test_component_assertion_required_when_components_present():
    rec = _record_with_components()
    rec.pop("component_assertion")
    assert _errors(rec)


def test_component_assertion_forbidden_without_components():
    rec = deepcopy(BASE)
    rec["component_assertion"] = deepcopy(ASSERTION)
    assert _errors(rec)


def test_component_parent_must_be_composite():
    rec = _record_with_components()
    rec["ingredient_type"] = "SINGLE_INGREDIENT"
    assert _errors(rec)


def test_local_or_external_scope_requires_component_id():
    for scope in ("MIM_CATALOG", "EXTERNAL_TERM"):
        rec = _record_with_components()
        rec["components"][0].pop("component_id")
        rec["components"][0]["reference_scope"] = scope
        assert _errors(rec)


def test_unmapped_scope_forbids_component_id():
    rec = _record_with_components()
    rec["components"][0]["reference_scope"] = "UNMAPPED"
    assert _errors(rec)


def test_concentration_value_and_unit_are_reciprocal():
    for missing in ("concentration_value", "concentration_unit"):
        rec = _record_with_components()
        rec["components"][0].pop(missing)
        assert _errors(rec)


def test_unknown_component_field_rejected():
    rec = _record_with_components()
    rec["components"][0]["concentratoin"] = "1"
    assert _errors(rec)
