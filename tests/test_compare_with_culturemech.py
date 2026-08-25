"""Tests for the status-aware CultureMech comparison path used after #453."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import yaml

_REPO_ROOT = Path(__file__).parent.parent
_SPEC = importlib.util.spec_from_file_location(
    "compare_with_culturemech",
    _REPO_ROOT / "scripts" / "compare_with_culturemech.py",
)
assert _SPEC is not None and _SPEC.loader is not None
mod = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(mod)


def _cm_mapped(*records: tuple[str, str, int]) -> dict:
    return {
        "mapped_ingredients": [
            {
                "preferred_term": term,
                "ontology_id": target,
                "occurrence_count": count,
            }
            for term, target, count in records
        ]
    }


def _cm_unmapped(*records: tuple[str, int]) -> dict:
    return {
        "unmapped_ingredients": [
            {"parsed_chemical_name": term, "occurrence_count": count} for term, count in records
        ]
    }


def _mim_mapped(*records: tuple[str, str, int]) -> dict:
    return {
        "ingredients": [
            {
                "identifier": target,
                "preferred_term": term,
                "mapping_status": "MAPPED",
                "ontology_mapping": {"ontology_id": target},
                "occurrence_statistics": {"total_occurrences": count},
            }
            for term, target, count in records
        ]
    }


def _mim_unmapped(*records: tuple[str, int]) -> dict:
    return {
        "ingredients": [
            {
                "identifier": f"UNMAPPED_{index:04d}",
                "preferred_term": term,
                "mapping_status": "UNMAPPED",
                "occurrence_statistics": {"total_occurrences": count},
            }
            for index, (term, count) in enumerate(records, 1)
        ]
    }


def _mim_rejected(*records: tuple[str, str]) -> dict:
    return {
        "ingredients": [
            {
                "identifier": target,
                "preferred_term": term,
                "mapping_status": "REJECTED",
                "occurrence_statistics": {"total_occurrences": 999},
            }
            for term, target in records
        ]
    }


def _mim_other(*records: tuple[str, str, str]) -> dict:
    return {
        "ingredients": [
            {
                "identifier": identifier,
                "preferred_term": term,
                "mapping_status": status,
            }
            for term, identifier, status in records
        ]
    }


def test_equal_mapped_targets_are_not_reported_as_conflicts():
    result = mod.compare_ingredients(
        _cm_mapped(("sodium chloride", "CHEBI:26710", 1)),
        {},
        _mim_mapped(("sodium chloride", "CHEBI:26710", 1)),
        {},
    )

    assert result["target_conflicts"] == []
    assert result["mim_coverage_gains"] == []
    assert result["culturemech_only_grounding"] == []
    assert result["both_unmapped"] == []
    assert result["occurrence_changes"] == []


def test_mapped_to_mapped_target_difference_is_a_target_conflict():
    result = mod.compare_ingredients(
        _cm_mapped(("sodium chloride", "CHEBI:26710", 1)),
        {},
        _mim_mapped(("sodium chloride", "CHEBI:1", 1)),
        {},
    )

    assert result["target_conflicts"] == [
        {
            "term": "sodium chloride",
            "culturemech_status": "MAPPED",
            "mediaingredientmech_status": "MAPPED",
            "culturemech_ontology": "CHEBI:26710",
            "mediaingredientmech_ontology": "CHEBI:1",
        }
    ]


def test_status_differences_are_classified_as_coverage_not_target_conflicts():
    result = mod.compare_ingredients(
        _cm_mapped(("cm grounded", "CHEBI:2", 1)),
        _cm_unmapped(("mim grounded", 1), ("neither grounded", 1)),
        _mim_mapped(("mim grounded", "CHEBI:1", 1)),
        _mim_unmapped(("cm grounded", 1), ("neither grounded", 1)),
    )

    assert result["target_conflicts"] == []
    assert result["mim_coverage_gains"] == [
        {
            "term": "mim grounded",
            "culturemech_status": "UNMAPPED",
            "mediaingredientmech_status": "MAPPED",
            "culturemech_ontology": None,
            "mediaingredientmech_ontology": "CHEBI:1",
        }
    ]
    assert result["culturemech_only_grounding"] == [
        {
            "term": "cm grounded",
            "culturemech_status": "MAPPED",
            "mediaingredientmech_status": "UNMAPPED",
            "culturemech_ontology": "CHEBI:2",
            "mediaingredientmech_ontology": None,
        }
    ]
    assert result["both_unmapped"] == [
        {
            "term": "neither grounded",
            "culturemech_status": "UNMAPPED",
            "mediaingredientmech_status": "UNMAPPED",
            "culturemech_ontology": None,
            "mediaingredientmech_ontology": None,
        }
    ]


def test_occurrence_changes_retain_statuses_and_always_require_review(capsys):
    result = mod.compare_ingredients(
        {},
        _cm_unmapped(("mim grounded", 3)),
        _mim_mapped(("mim grounded", "CHEBI:1", 1)),
        {},
    )

    assert result["occurrence_changes"] == [
        {
            "term": "mim grounded",
            "culturemech_count": 3,
            "mediaingredient_count": 1,
            "delta": 2,
            "culturemech_status": "UNMAPPED",
            "mediaingredientmech_status": "MAPPED",
        }
    ]

    mod.print_comparison_report(result)
    report = capsys.readouterr().out
    assert "SOURCE REVIEW RECOMMENDED" in report
    assert "1 label has occurrence count changes" in report
    assert "NO ACTIONABLE SOURCE DIFFERENCES DETECTED" not in report


def test_culturemech_cross_status_collision_is_reported_and_not_silently_chosen():
    result = mod.compare_ingredients(
        _cm_mapped(("NaCl", "CHEBI:26710", 8)),
        _cm_unmapped(("NaCl", 2)),
        _mim_mapped(("NaCl", "CHEBI:26710", 8)),
        {},
    )

    assert result["culturemech_status_collisions"] == [
        {
            "term": "NaCl",
            "source": "culturemech",
            "statuses": ["MAPPED", "UNMAPPED"],
            "mapped_ontology": "CHEBI:26710",
            "mapped_occurrence_count": 8,
            "unmapped_occurrence_count": 2,
        }
    ]
    assert result["target_conflicts"] == []
    assert result["mim_coverage_gains"] == []
    assert result["culturemech_only_grounding"] == []
    assert result["both_unmapped"] == []
    assert result["occurrence_changes"] == []


def test_rejected_tombstones_are_reported_but_excluded_from_active_comparison(capsys):
    result = mod.compare_ingredients(
        _cm_mapped(("retired mapped label", "CHEBI:1", 9)),
        _cm_unmapped(("retired unmapped label", 4)),
        _mim_rejected(("retired mapped label", "CHEBI:2")),
        _mim_rejected(("retired unmapped label", "UNMAPPED_0001")),
    )

    assert result["mediaingredientmech"] == {
        "generation_date": None,
        "mapped_count": 0,
        "unmapped_count": 0,
        "total_count": 0,
        "rejected_count": 2,
        "non_active_or_missing_count": 0,
    }
    assert result["mediaingredientmech_rejected_tombstones"] == [
        {
            "term": "retired mapped label",
            "mapping_status": "REJECTED",
            "identifier": "CHEBI:2",
            "collection": "mapped_ingredients.yaml",
        },
        {
            "term": "retired unmapped label",
            "mapping_status": "REJECTED",
            "identifier": "UNMAPPED_0001",
            "collection": "unmapped_ingredients.yaml",
        },
    ]
    assert result["culturemech_labels_with_rejected_mim_tombstones"] == [
        "retired mapped label",
        "retired unmapped label",
    ]
    assert result["present_only_in_current_culturemech_aggregate"] == []
    assert result["absent_from_current_culturemech_aggregate"] == []
    assert result["target_conflicts"] == []
    assert result["mim_coverage_gains"] == []
    assert result["culturemech_only_grounding"] == []
    assert result["both_unmapped"] == []
    assert result["occurrence_changes"] == []

    mod.print_comparison_report(result)
    report = capsys.readouterr().out
    assert "MIM REJECTED TOMBSTONES (2; excluded from active comparisons)" in report
    assert "CultureMech labels matching only a rejected MIM tombstone (2)" in report


def test_other_mim_status_is_known_but_excluded_and_reported(capsys):
    result = mod.compare_ingredients(
        _cm_mapped(("pending label", "CHEBI:1", 3)),
        {},
        _mim_other(("pending label", "CHEBI:2", "PENDING_REVIEW")),
        {},
    )

    assert result["mediaingredientmech"]["non_active_or_missing_count"] == 1
    assert result["mediaingredientmech"]["total_count"] == 0
    assert result["mediaingredientmech_non_active_or_missing_records"] == [
        {
            "term": "pending label",
            "mapping_status": "PENDING_REVIEW",
            "identifier": "CHEBI:2",
            "collection": "mapped_ingredients.yaml",
        }
    ]
    assert result["culturemech_labels_with_non_active_or_missing_mim_records"] == ["pending label"]
    assert result["present_only_in_current_culturemech_aggregate"] == []
    assert result["target_conflicts"] == []
    assert result["occurrence_changes"] == []

    mod.print_comparison_report(result)
    report = capsys.readouterr().out
    assert "MIM RECORDS WITH OTHER NON-ACTIVE OR MISSING STATUS (1; excluded)" in report
    assert "CultureMech labels matching only one of these excluded records (1)" in report


def test_aggregate_absence_is_not_serialized_or_reported_as_removal(capsys):
    result = mod.compare_ingredients(
        _cm_mapped(("CultureMech only", "CHEBI:1", 1)),
        {},
        _mim_mapped(("MIM only", "CHEBI:2", 1)),
        {},
    )

    assert result["present_only_in_current_culturemech_aggregate"] == ["CultureMech only"]
    assert result["absent_from_current_culturemech_aggregate"] == ["MIM only"]
    assert "new_in_culturemech" not in result
    assert "removed_from_culturemech" not in result
    assert "mapping_changes" not in result

    serialized = yaml.safe_dump(result)
    assert "absent_from_current_culturemech_aggregate:" in serialized
    assert "removed_from_culturemech:" not in serialized

    mod.print_comparison_report(result)
    report = capsys.readouterr().out
    assert "ABSENT FROM CURRENT CULTUREMECH AGGREGATE" in report
    assert "not evidence of removal" in report
    assert "REMOVED FROM CULTUREMECH" not in report
