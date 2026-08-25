"""Regression tests for CultureMech mapping-quality translation (#317)."""

from __future__ import annotations

import importlib.util
from pathlib import Path

from mediaingredientmech.import_quality import map_culturemech_quality

_SPEC = importlib.util.spec_from_file_location(
    "import_from_culturemech",
    Path(__file__).parent.parent / "scripts" / "import_from_culturemech.py",
)
assert _SPEC is not None and _SPEC.loader is not None
mod = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(mod)

_MERGE_SPEC = importlib.util.spec_from_file_location(
    "merge_culturemech_updates",
    Path(__file__).parent.parent / "scripts" / "merge_culturemech_updates.py",
)
assert _MERGE_SPEC is not None and _MERGE_SPEC.loader is not None
merge_mod = importlib.util.module_from_spec(_MERGE_SPEC)
_MERGE_SPEC.loader.exec_module(merge_mod)


def _source(**overrides) -> dict:
    ingredient = {
        "preferred_term": "sodium chloride",
        "ontology_id": "CHEBI:26710",
        "ontology_label": "sodium chloride",
        "ontology_source": "CHEBI",
        "mapping_quality": "DIRECT_MATCH",
    }
    ingredient.update(overrides)
    return ingredient


def test_direct_match_is_never_silently_strengthened_to_exact():
    assert map_culturemech_quality("DIRECT_MATCH") == "PROVISIONAL"


def test_missing_surfaces_or_quality_never_default_to_exact():
    assert map_culturemech_quality(None) == "PROVISIONAL"
    assert map_culturemech_quality("UNKNOWN") == "PROVISIONAL"


def test_explicit_source_grades_are_preserved():
    assert map_culturemech_quality("EXACT_MATCH") == "EXACT_MATCH"
    assert map_culturemech_quality("SYNONYM_MATCH") == "SYNONYM_MATCH"
    assert map_culturemech_quality("CAS_RN_LOOKUP") == "CAS_RN_LOOKUP"
    assert map_culturemech_quality("CLOSE_MATCH") == "CLOSE_MATCH"
    assert map_culturemech_quality("MANUAL_CURATION") == "MANUAL_CURATION"


def test_converter_records_why_ambiguous_direct_match_is_provisional():
    record = mod.convert_mapped_ingredient(
        _source(
            preferred_term="HEPES",
            ontology_id="CHEBI:42334",
            ontology_label="2-[4-(2-hydroxyethyl)piperazin-1-yl]ethanesulfonic acid",
        )
    )

    mapping = record["ontology_mapping"]
    assert mapping["mapping_quality"] == "PROVISIONAL"
    note = mapping["evidence"][0]["notes"]
    assert "DIRECT_MATCH is an aggregate default" in note
    assert "not preserved primary-label/synonym provenance (#317)" in note


def test_converter_preserves_only_an_explicit_exact_grade():
    record = mod.convert_mapped_ingredient(_source(mapping_quality="EXACT_MATCH"))

    mapping = record["ontology_mapping"]
    assert mapping["mapping_quality"] == "EXACT_MATCH"
    assert "source quality=EXACT_MATCH; MIM quality=EXACT_MATCH" in mapping["evidence"][0]["notes"]


def test_historical_merge_import_also_keeps_direct_match_provisional():
    record = merge_mod.import_new_ingredient(_source())
    mapping = record["ontology_mapping"]
    assert mapping["mapping_quality"] == "PROVISIONAL"
    assert "DIRECT_MATCH is an aggregate default" in mapping["evidence"][0]["notes"]


def test_target_change_resets_old_exact_grade_without_mutating_source_record():
    current = {
        "identifier": "CHEBI:1",
        "preferred_term": "source label",
        "ontology_mapping": {
            "ontology_id": "CHEBI:1",
            "ontology_label": "old target",
            "ontology_source": "CHEBI",
            "mapping_quality": "EXACT_MATCH",
            "evidence": [],
        },
        "mapping_status": "MAPPED",
        "occurrence_statistics": {"total_occurrences": 1, "media_count": 1},
    }
    update = _source(
        preferred_term="source label",
        ontology_id="CHEBI:2",
        ontology_label="new target",
        occurrence_count=1,
        media_occurrences=[{"medium_name": "one"}],
    )

    merged, changes = merge_mod.merge_ingredient(current, update)

    assert changes["ontology_update"] == {"old": "CHEBI:1", "new": "CHEBI:2"}
    assert merged["ontology_mapping"]["mapping_quality"] == "PROVISIONAL"
    assert (
        "DIRECT_MATCH is an aggregate default"
        in (merged["ontology_mapping"]["evidence"][-1]["notes"])
    )
    assert current["ontology_mapping"]["mapping_quality"] == "EXACT_MATCH"
    assert current["ontology_mapping"]["evidence"] == []
