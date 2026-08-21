"""Regression tests for CHEBI duplicate merge controls and provenance."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import SimpleNamespace
from typing import Any, cast

import pytest
import yaml

from mediaingredientmech.curation.chebi_deduplicator import CHEBIDeduplicator
from mediaingredientmech.curation.ingredient_curator import IngredientCurator


def _record(name: str, quality: str = "EXACT_MATCH") -> dict[str, Any]:
    return {
        "identifier": "CHEBI:1234",
        "preferred_term": name,
        "mapping_status": "MAPPED",
        "ingredient_type": "SINGLE_INGREDIENT",
        "ontology_mapping": {
            "ontology_id": "CHEBI:1234",
            "ontology_label": "test compound",
            "ontology_source": "CHEBI",
            "mapping_quality": quality,
        },
        "synonyms": [],
        "occurrence_statistics": {
            "total_occurrences": 1,
            "media_count": 1,
            "sample_media": [],
        },
    }


def _deduplicator() -> CHEBIDeduplicator:
    curator = SimpleNamespace(
        records=[_record("target"), _record("source")],
        curator_name="test-curator",
    )
    return CHEBIDeduplicator(cast("IngredientCurator", curator))


@pytest.mark.parametrize(
    ("dry_run", "auto_merge", "reported_merged", "mutated"),
    [
        (True, False, False, False),
        (True, True, True, False),
        (False, False, False, False),
        (False, True, True, True),
    ],
)
def test_merge_control_truth_table(
    dry_run: bool,
    auto_merge: bool,
    reported_merged: bool,
    mutated: bool,
) -> None:
    deduplicator = _deduplicator()

    result = deduplicator.merge_duplicates(dry_run=dry_run, auto_merge=auto_merge)

    assert bool(result["merged"]) is reported_merged
    assert bool(result["flagged"]) is (not reported_merged)
    assert result["total_removed"] == (1 if reported_merged else 0)
    source = deduplicator.curator.records[1]
    assert (source["mapping_status"] == "REJECTED") is mutated
    assert bool(deduplicator.curator.records[0]["synonyms"]) is mutated
    assert ("curation_history" in source) is mutated


def test_apply_mode_merge_records_provenance_without_type_error() -> None:
    deduplicator = _deduplicator()

    result = deduplicator.merge_duplicates(dry_run=False, auto_merge=True)

    assert result["merged"] == [(0, [1], "CHEBI:1234")]
    target, source = deduplicator.curator.records
    assert target["curation_history"][-1]["action"] == "MERGED_FROM_DUPLICATES"
    assert target["curation_history"][-1]["curator"] == "test-curator"
    assert "Same CHEBI ID (CHEBI:1234)" in target["curation_history"][-1]["changes"]
    assert source["curation_history"][-1] == {
        "timestamp": source["curation_history"][-1]["timestamp"],
        "curator": "test-curator",
        "action": "MERGED",
        "changes": (
            "Merged into 'target'. Same CHEBI ID (CHEBI:1234) - "
            "Same CHEBI ID + same quality (EXACT_MATCH)"
        ),
        "previous_status": "MAPPED",
        "new_status": "REJECTED",
    }


def test_ineligible_group_is_flagged_even_when_auto_merge_is_enabled(monkeypatch) -> None:
    deduplicator = _deduplicator()
    monkeypatch.setattr(
        deduplicator,
        "should_auto_merge",
        lambda target_idx, source_idx: (False, "safety check failed"),
    )

    result = deduplicator.merge_duplicates(dry_run=False, auto_merge=True)

    assert result["merged"] == []
    assert result["flagged"] == [("CHEBI:1234", [0, 1], "safety check failed")]
    assert deduplicator.curator.records[1]["mapping_status"] == "MAPPED"


def test_applied_merge_survives_validated_save(tmp_path) -> None:
    data_path = tmp_path / "ingredients.yaml"
    data_path.write_text(yaml.safe_dump({"ingredients": [_record("target"), _record("source")]}))
    curator = IngredientCurator(data_path=data_path, curator_name="test-curator")
    curator.load()

    CHEBIDeduplicator(curator).merge_duplicates(dry_run=False, auto_merge=True)
    curator.save()

    saved = yaml.safe_load(data_path.read_text())["ingredients"]
    assert saved[1]["mapping_status"] == "REJECTED"
    assert saved[1]["curation_history"][-1]["action"] == "MERGED"


def _load_script_module():
    root = Path(__file__).parent.parent
    script = root / "scripts" / "deduplicate_ingredients.py"
    spec = importlib.util.spec_from_file_location("deduplicate_ingredients", script)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_script_default_apply_mode_does_not_enable_auto_merge(monkeypatch, tmp_path) -> None:
    """The CLI must preserve its default safe, review-only apply behavior."""
    module = _load_script_module()
    calls: list[tuple[bool, bool]] = []

    class FakeCurator:
        def __init__(self, data_path):
            self.records = [_record("only")]

        def load(self):
            return self.records

        def save(self):
            pass

    class FakeDeduplicator:
        def __init__(self, curator):
            pass

        def merge_duplicates(self, dry_run, auto_merge):
            calls.append((dry_run, auto_merge))
            return {
                "merged": [],
                "flagged": [],
                "total_removed": 0,
                "dry_run": dry_run,
            }

        def validate_no_chebi_duplicates(self):
            return True, []

    monkeypatch.setattr(module, "IngredientCurator", FakeCurator)
    monkeypatch.setattr(module, "CHEBIDeduplicator", FakeDeduplicator)
    monkeypatch.setattr(module, "display_chebi_results", lambda *args: None)
    monkeypatch.setattr(
        sys,
        "argv",
        ["deduplicate_ingredients.py", "--chebi-only", "--data-path", str(tmp_path / "x.yaml")],
    )

    module.main()

    assert calls == [(False, False)]
