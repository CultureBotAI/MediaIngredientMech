"""Tests for chemical_properties inheritance guards (#268, #871), classify_ingredient_type (#268), and locant check (#313)."""

from __future__ import annotations

import importlib.util
from pathlib import Path

from mediaingredientmech.curation.ingredient_curator import (
    can_inherit_chebi_chemical_properties,
)
from mediaingredientmech.validation.ingredient_reviewer import IngredientReviewer

REPO = Path(__file__).resolve().parents[1]


def _load_script(name: str):
    path = REPO / "scripts" / name
    spec = importlib.util.spec_from_file_location(name.removesuffix(".py"), path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_can_inherit_chebi_chemical_properties_exact_single_ingredient():
    rec = {
        "identifier": "CHEBI:17234",
        "preferred_term": "Glucose",
        "ingredient_type": "SINGLE_INGREDIENT",
        "mapping_status": "MAPPED",
        "ontology_mapping": {
            "ontology_id": "CHEBI:17234",
            "ontology_source": "CHEBI",
            "mapping_quality": "EXACT_MATCH",
        },
    }
    assert can_inherit_chebi_chemical_properties(rec) is True


def test_cannot_inherit_chebi_chemical_properties_for_stock_solution_or_hydrate():
    # #268: Stock solution mapped to solute CHEBI
    stock_rec = {
        "identifier": "CHEBI:9532",
        "preferred_term": "0.2% Thiamine pyrophosphate",
        "ingredient_type": "STOCK_SOLUTION",
        "mapping_status": "MAPPED",
        "ontology_mapping": {
            "ontology_id": "CHEBI:9532",
            "ontology_source": "CHEBI",
            "mapping_quality": "CLOSE_MATCH",
        },
    }
    assert can_inherit_chebi_chemical_properties(stock_rec) is False

    # #871: Hydrate record with cas:* primary identifier and anhydrous CHEBI parent
    hydrate_rec = {
        "identifier": "cas:5786-71-0",
        "preferred_term": "CoCl2 x 2 H2O",
        "ingredient_type": "SINGLE_INGREDIENT",
        "mapping_status": "MAPPED",
        "ontology_mapping": {
            "ontology_id": "CHEBI:35696",
            "ontology_source": "CHEBI",
            "mapping_quality": "NARROW_MATCH",
        },
    }
    assert can_inherit_chebi_chemical_properties(hydrate_rec) is False

    # IngredientReviewer P3.1 should not flag missing SMILES/InChI on hydrate/stock
    reviewer = IngredientReviewer()
    issues, suggestions = reviewer._validate_p3(hydrate_rec, "CHEBI:35696", "cas:5786-71-0")
    assert [i for i in issues if i.rule_id == "P3.1"] == []
    assert [s for s in suggestions if s.action == "enrich_properties"] == []


def test_classify_ingredient_type_leading_percent_and_molar_stock():
    mod = _load_script("classify_ingredient_type.py")
    kind1, _ = mod.classify(
        {"preferred_term": "0.2% Thiamine pyrophosphate", "identifier": "CHEBI:9532"},
        structural={"CHEBI:9532"},
    )
    assert kind1 == "STOCK_SOLUTION"

    kind2, _ = mod.classify(
        {
            "preferred_term": "Disodium phosphate heptahydrate (0.02 M stock)",
            "identifier": "CHEBI:34683",
        },
        structural={"CHEBI:34683"},
    )
    assert kind2 == "STOCK_SOLUTION"
