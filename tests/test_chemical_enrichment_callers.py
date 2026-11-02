"""Exercise all four automatic write entry points with the real shared guard."""

import importlib.util
import sys
from copy import deepcopy
from pathlib import Path

import pytest
import yaml
from click.testing import CliRunner

from mediaingredientmech.curation.ingredient_curator import IngredientCurator
from mediaingredientmech.utils.chemical_properties_client import ChemicalPropertiesClient
from mediaingredientmech.validation import ingredient_reviewer as reviewer_module
from mediaingredientmech.validation.write_validated import validate_ingredient
from tests.test_chemical_properties_guard import envelope, record

ROOT = Path(__file__).resolve().parents[1]


def script(name):
    spec = importlib.util.spec_from_file_location(
        "test_caller_" + name, ROOT / "scripts" / f"{name}.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def suggestion():
    return reviewer_module.ReviewResult(
        status="WARNING",
        issues=[
            reviewer_module.ValidationIssue(
                "P3", "P3.1", "missing_chemical_properties", "missing", {}, "water"
            )
        ],
        suggestions=[
            reviewer_module.CorrectionSuggestion(
                "enrich_properties", "chemical_properties", {}, "<fetch>", True, 1.0, "OLS"
            )
        ],
    )


def invoke(name, rec, monkeypatch, tmp_path, dry=False):
    if name == "curator":
        curator = IngredientCurator.__new__(IngredientCurator)
        curator._dirty = False
        curator.curator_name = "test curator"
        result = curator.enrich_chemical_properties(rec)
        return result, {"dirty": curator.is_dirty}
    if name == "reviewer":
        reviewer = reviewer_module.IngredientReviewer.__new__(reviewer_module.IngredientReviewer)
        reviewer.review_ingredient = lambda r: suggestion()
        monkeypatch.setattr(
            reviewer, "enrich_from_ols", lambda *a: pytest.fail("raw retrieval called")
        )
        return reviewer.auto_correct(rec, correction_types=["chemical_properties"]), {}
    module = script(name)
    collection = {"generation_date": "retained", "total_count": 1, "ingredients": [rec]}
    saved = []
    monkeypatch.setattr(module, "save_yaml", lambda data, *args, **kw: saved.append(deepcopy(data)))
    if name == "enrich_from_ols":
        monkeypatch.setattr(module, "load_mapped_ingredients", lambda: collection)
        monkeypatch.setattr(module, "CHECKPOINT_FILE", tmp_path / "checkpoint.json")
        monkeypatch.setattr(module, "FAILURES_FILE", tmp_path / "failures.json")
        monkeypatch.setattr(module.time, "sleep", lambda _: None)
        monkeypatch.setattr(
            sys, "argv", ["enrich_from_ols", "--delay", "0"] + (["--dry-run"] if dry else [])
        )
        assert module.main() == 0
    else:
        source = tmp_path / "source.yaml"
        source.write_text("fixture")
        monkeypatch.setattr(module, "load_ingredients", lambda _: collection)
        result = CliRunner().invoke(
            module.main, ["--input", str(source)] + (["--dry-run"] if dry else [])
        )
        assert result.exit_code == 0, result.output
    if saved:
        assert saved[0]["generation_date"] == "retained" and saved[0]["total_count"] == 1
    return rec, {"saved": saved, "files": sorted(p.name for p in tmp_path.iterdir())}


@pytest.fixture
def fetch(monkeypatch):
    calls = []
    monkeypatch.setattr(
        ChemicalPropertiesClient,
        "get_ols_properties",
        lambda self, oid: calls.append(oid) or envelope(),
    )
    monkeypatch.setattr(
        ChemicalPropertiesClient, "get_properties", lambda *a, **k: pytest.fail("legacy API")
    )
    return calls


@pytest.mark.parametrize(
    "caller", ["curator", "reviewer", "enrich_from_ols", "enrich_chemical_properties"]
)
def test_each_caller_adds_one_guarded_block_and_truthful_event(
    caller, monkeypatch, tmp_path, fetch
):
    original = record()
    before = deepcopy(original)
    result, meta = invoke(caller, original, monkeypatch, tmp_path)
    assert fetch == ["CHEBI:15377"] and result["chemical_properties"]["molecular_formula"] == "H2O"
    assert result["curation_history"][:-1] == before["curation_history"]
    assert len(result["curation_history"]) == len(before["curation_history"]) + 1
    event = result["curation_history"][-1]
    assert "CHEBI:15377" in event["changes"] and "response SHA256" in event["changes"]
    assert "retrieved 2026-11-02" in event["changes"]
    assert result["ontology_mapping"] == before["ontology_mapping"]
    if caller == "reviewer":
        assert original == before
    if caller == "curator":
        assert meta["dirty"] is True
    if caller.startswith("enrich_"):
        assert len(meta["saved"]) == 1


@pytest.mark.parametrize(
    "caller", ["curator", "reviewer", "enrich_from_ols", "enrich_chemical_properties"]
)
@pytest.mark.parametrize(
    "change",
    [
        {"chemical_properties": {"cas_rn": "7732-18-5"}},
        {"ingredient_type": "UNDEFINED_MIXTURE"},
        {"preferred_term": "water dihydrate"},
    ],
)
def test_every_caller_refuses_without_fetch_or_history_change(
    caller, change, monkeypatch, tmp_path, fetch
):
    rec = record(**change)
    before = deepcopy(rec)
    result, meta = invoke(caller, rec, monkeypatch, tmp_path)
    assert result == rec == before and fetch == []
    assert not meta.get("dirty") and not meta.get("saved")


@pytest.mark.parametrize("caller", ["enrich_from_ols", "enrich_chemical_properties"])
@pytest.mark.parametrize("block", [None, {"cas_rn": "7732-18-5"}])
def test_dry_runs_use_identical_protection_and_never_save(
    caller, block, monkeypatch, tmp_path, fetch
):
    rec = record(chemical_properties=block)
    before = deepcopy(rec)
    result, meta = invoke(caller, rec, monkeypatch, tmp_path, dry=True)
    assert result == before and not meta["saved"]
    assert fetch == (["CHEBI:15377"] if block is None else [])
    assert not (tmp_path / "checkpoint.json").exists() and not (tmp_path / "failures.json").exists()


@pytest.mark.parametrize("selector", [["chemical_properties"], ["enrich_properties"], None])
def test_1097_public_selector_and_legacy_action_both_reach_guard(selector, fetch, monkeypatch):
    reviewer = reviewer_module.IngredientReviewer.__new__(reviewer_module.IngredientReviewer)
    reviewer.review_ingredient = lambda r: suggestion()
    result = reviewer.auto_correct(record(), correction_types=selector)
    assert fetch == ["CHEBI:15377"] and result["chemical_properties"]["smiles"] == "O"


def test_reviewer_rechecks_mutation_after_suggestion(fetch):
    reviewer = reviewer_module.IngredientReviewer.__new__(reviewer_module.IngredientReviewer)

    def review(rec):
        result = suggestion()
        rec["ingredient_type"] = "STOCK_SOLUTION"
        return result

    reviewer.review_ingredient = review
    result = reviewer.auto_correct(record(), correction_types=["chemical_properties"])
    assert fetch == [] and "chemical_properties" not in result
    assert result["curation_history"] == [{"action": "OLD"}]


@pytest.mark.parametrize(
    "changes,automatic",
    [
        ({}, True),
        ({"chemical_properties": {"cas_rn": "7732-18-5"}}, False),
        ({"ingredient_type": None}, False),
        ({"preferred_term": "water hydrate"}, False),
    ],
)
def test_suggestion_generation_is_pure_and_records_review_only_reason(changes, automatic, fetch):
    reviewer = reviewer_module.IngredientReviewer.__new__(reviewer_module.IngredientReviewer)
    reviewer.get_term_info = lambda _: None
    issues, suggestions = reviewer._validate_p3(record(**changes), "CHEBI:15377", "water")
    suggestion = [s for s in suggestions if s.action == "enrich_properties"][0]
    assert suggestion.auto_correctable is automatic and fetch == []
    if not automatic:
        assert "Enrich from EBI" not in suggestion.rationale


@pytest.fixture
def blocked_then_eligible_collection(tmp_path):
    """Schema-valid local records, not live catalogue or scientific evidence."""
    collection = {
        "generation_date": "2026-11-02T00:00:00+00:00",
        "total_count": 2,
        "mapped_count": 2,
        "unmapped_count": 0,
        "ingredients": [
            record(curation_history=[], ingredient_type="STOCK_SOLUTION"),
            record(curation_history=[]),
        ],
    }
    assert not validate_ingredient(collection, target_class="IngredientCollection")
    source = tmp_path / "collection.yaml"
    source.write_text(yaml.safe_dump(collection, sort_keys=False))
    return collection, source


@pytest.mark.parametrize("dry", [False, True])
def test_1100_limit_counts_eligible_candidates_with_real_validated_save(
    blocked_then_eligible_collection, fetch, dry
):
    collection, source = blocked_then_eligible_collection
    before = source.read_bytes()
    module = script("enrich_chemical_properties")
    assert len(module.filter_chebi_without_properties(collection)) == 1
    result = CliRunner().invoke(
        module.main,
        ["--input", str(source), "--limit", "1"] + (["--dry-run"] if dry else []),
    )
    assert result.exit_code == 0, result.output
    assert fetch == ["CHEBI:15377"]
    assert "Enriched: 1" in result.output
    after = yaml.safe_load(source.read_text())
    assert after["ingredients"][0] == collection["ingredients"][0]
    assert {k: v for k, v in after.items() if k != "ingredients"} == {
        k: v for k, v in collection.items() if k != "ingredients"
    }
    if dry:
        assert source.read_bytes() == before
        assert sorted(p.name for p in source.parent.iterdir()) == [source.name]
    else:
        changed = after["ingredients"][1]
        assert changed["chemical_properties"] == envelope().to_dict()
        assert len(changed["curation_history"]) == 1
        assert changed["curation_history"][0]["action"] == "AUTO_BACKFILL_CHEBI_CHEMISTRY"
        assert "response SHA256" in changed["curation_history"][0]["changes"]
        assert {
            k: v for k, v in changed.items() if k not in ("chemical_properties", "curation_history")
        } == {k: v for k, v in collection["ingredients"][1].items() if k != "curation_history"}
        assert not validate_ingredient(after, target_class="IngredientCollection")


@pytest.mark.parametrize("dry", [False, True])
def test_1100_candidate_filter_does_not_replace_apply_time_guard(
    blocked_then_eligible_collection, monkeypatch, fetch, dry
):
    _, source = blocked_then_eligible_collection
    before = source.read_bytes()
    module = script("enrich_chemical_properties")
    original_filter = module.filter_chebi_without_properties
    selected = []

    def select_then_change_scope(data):
        candidates = original_filter(data)
        assert len(candidates) == 1
        selected.extend(candidates)
        candidates[0]["ingredient_type"] = "STOCK_SOLUTION"
        return candidates

    monkeypatch.setattr(module, "filter_chebi_without_properties", select_then_change_scope)
    result = CliRunner().invoke(
        module.main,
        ["--input", str(source), "--limit", "1"] + (["--dry-run"] if dry else []),
    )
    assert result.exit_code == 0, result.output
    assert len(selected) == 1
    assert fetch == []
    assert "Enriched: 0; Skipped: 1" in result.output
    assert source.read_bytes() == before
    assert sorted(p.name for p in source.parent.iterdir()) == [source.name]
