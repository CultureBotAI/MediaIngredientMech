"""The existing classifier must not repeat the historical #268 type cascade."""

import importlib.util
from copy import deepcopy
from pathlib import Path

import pytest
import yaml


def classifier():
    path = Path(__file__).resolve().parents[1] / "scripts/classify_ingredient_type.py"
    spec = importlib.util.spec_from_file_location("classification_scope_fixture", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize("scope", ["UNDEFINED_MIXTURE", "STOCK_SOLUTION"])
def test_explicit_types_and_history_unchanged_even_with_single_formula(
    tmp_path, monkeypatch, scope
):
    mod = classifier()
    record = {
        "identifier": "CHEBI:78020",
        "preferred_term": "Casamino acids",
        "ingredient_type": scope,
        "mapping_status": "MAPPED",
        "chemical_properties": {"molecular_formula": "C27H53O2"},
        "curation_history": [{"action": "OLD"}],
    }
    before = deepcopy(record)
    collection = {"ingredients": [record]}
    path = tmp_path / "collection.yaml"
    path.write_text(yaml.safe_dump(collection))
    db = tmp_path / "chebi.db"
    db.touch()
    monkeypatch.setattr(mod, "COLLECTION", path)
    monkeypatch.setattr(mod, "CHEBI_DB", db)
    monkeypatch.setattr(mod, "structural_chebi_terms", lambda _: {"CHEBI:78020"})
    monkeypatch.setattr(
        mod, "save_yaml", lambda *a, **k: pytest.fail("already typed record written")
    )
    assert mod.main(["--apply"]) == 0
    assert yaml.safe_load(path.read_text())["ingredients"] == [before]


def test_unset_mixture_name_outranks_namespace_and_derived_formula():
    mod = classifier()
    record = {
        "identifier": "CHEBI:78020",
        "preferred_term": "Casamino acids",
        "chemical_properties": {"molecular_formula": "C27H53O2"},
    }
    before = deepcopy(record)
    assert mod.classify(record, {"CHEBI:78020"})[0] == "UNDEFINED_MIXTURE" and record == before


def test_formula_alone_is_not_structural_ontology_evidence():
    mod = classifier()
    record = {
        "identifier": "CHEBI:1",
        "preferred_term": "some compound",
        "chemical_properties": {"molecular_formula": "H2O"},
    }
    assert mod.classify(record, set())[0] is None
