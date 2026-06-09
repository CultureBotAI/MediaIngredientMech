"""Tests for the StockComponent schema slot (recipe-level decomposition).

`IngredientRecord.components` lets a STOCK_SOLUTION / DEFINED_MEDIUM record carry
its recipe as a list of StockComponent entries. These pin the slot's closed-schema
behavior so it can't silently regress once recipes start being populated.
"""

import sys
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


def test_record_without_components_valid():
    # components is optional — existing records (none have it) stay valid.
    assert validate_ingredient(dict(BASE), target_class="IngredientRecord") == []


def test_record_with_components_valid():
    rec = dict(BASE)
    rec["components"] = [
        {
            "component_name": "FeCl3 x 6 H2O",
            "component_id": "CHEBI:30808",
            "concentration_value": "1.5",
            "concentration_unit": "G_PER_L",
            "source": "CultureMech:M278",
        },
        {"component_name": "H3BO3", "concentration_value": "0.01", "concentration_unit": "G_PER_L"},
    ]
    assert validate_ingredient(rec, target_class="IngredientRecord") == []


def test_component_name_required():
    rec = dict(BASE)
    rec["components"] = [{"concentration_value": "1", "concentration_unit": "G_PER_L"}]
    assert len(validate_ingredient(rec, target_class="IngredientRecord")) >= 1


def test_unknown_component_field_rejected():
    # closed schema: a typo'd component field must be caught.
    rec = dict(BASE)
    rec["components"] = [{"component_name": "X", "concentratoin": "1"}]
    assert len(validate_ingredient(rec, target_class="IngredientRecord")) >= 1
