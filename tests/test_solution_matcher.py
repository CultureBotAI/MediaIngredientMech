"""Focused tests for solution, buffer, and stock duplicate matching."""

from __future__ import annotations

import pytest

from mediaingredientmech.curation.solution_matcher import SolutionMatcher, normalize_text


@pytest.fixture
def matcher() -> SolutionMatcher:
    return SolutionMatcher()


def test_normalize_text_collapses_whitespace_and_edge_punctuation() -> None:
    assert normalize_text("  PHOSPHATE\t Buffer...  ") == "phosphate buffer"


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("trace elements", "TRACE_METAL"),
        ("Trace Metal", "TRACE_METAL"),
        ("macro nutrients", "MACRO"),
        ("micronutrients solution", "MICRO"),
        ("vitamin mixture", "VITAMIN"),
        ("mineral mix", "MINERAL"),
        ("phosphate solution", "SOLUTION"),
        ("phosphate buffer", "BUFFER"),
        ("phosphate stock", "STOCK"),
        ("sodium chloride", "CHEMICAL"),
    ],
)
def test_detect_type(matcher: SolutionMatcher, name: str, expected: str) -> None:
    assert matcher.detect_type(name) == expected


def test_extract_base_name_strips_suffix_or_returns_normalized_name(
    matcher: SolutionMatcher,
) -> None:
    assert matcher.extract_base_name("  Phosphate Stock ") == "phosphate"
    assert matcher.extract_base_name("  Sodium   Chloride. ") == "sodium chloride"


def test_normalize_concentration_standardizes_supported_units(
    matcher: SolutionMatcher,
) -> None:
    assert matcher.normalize_concentration("10 µM, 2 µg/L, 3 mg/L, 4 g/L, 5%") == (
        "10 um, 2 ug_l, 3 mg_l, 4 g_l, 5pct"
    )


@pytest.mark.parametrize(
    ("name1", "name2", "expected"),
    [
        ("Phosphate Buffer", "phosphate buffer.", 1.0),
        ("phosphate solution", "phosphate stock", 0.9),
        ("vitamin solution", "vitamin", 0.8),
        (
            "alpha beta gamma delta epsilon solution",
            "alpha beta gamma delta epsilon zeta solution",
            0.7,
        ),
        ("glucose phosphate buffer", "glucose tris buffer", 0.3),
        ("", "phosphate solution", 0.0),
    ],
)
def test_match_confidence_branches(
    matcher: SolutionMatcher, name1: str, name2: str, expected: float
) -> None:
    assert matcher.match_confidence(name1, name2) == pytest.approx(expected)


def test_find_solution_duplicates_filters_and_preserves_record_indices(
    matcher: SolutionMatcher,
) -> None:
    records = [
        {"preferred_term": "phosphate solution", "mapping_status": "MAPPED"},
        {"preferred_term": "phosphate buffer", "mapping_status": "UNMAPPED"},
        {"preferred_term": "glucose", "mapping_status": "MAPPED"},
        {"preferred_term": "phosphate stock", "mapping_status": "REJECTED"},
        {"preferred_term": "phosphate stock"},
        {},
    ]

    assert matcher.find_solution_duplicates(records) == [
        (0, 1, 0.9),
        (0, 4, 0.9),
        (1, 4, 0.9),
    ]
    assert matcher.find_solution_duplicates(records, threshold=0.95) == []


@pytest.mark.parametrize(
    ("name1", "name2", "confidence", "should_merge", "reason_fragment"),
    [
        ("phosphate buffer", "phosphate buffer", 1.0, True, "Exact base name"),
        ("phosphate buffer", "phosphate buffer", 0.95, True, "Same base chemical"),
        ("phosphate buffer", "phosphate solution", 0.9, False, "different types"),
        ("phosphate buffer", "tris buffer", 0.75, False, "manual review"),
        ("phosphate buffer", "glucose solution", 0.4, False, "Low confidence"),
    ],
)
def test_get_merge_recommendation_branches(
    matcher: SolutionMatcher,
    name1: str,
    name2: str,
    confidence: float,
    should_merge: bool,
    reason_fragment: str,
) -> None:
    recommendation, reason = matcher.get_merge_recommendation(
        {"preferred_term": name1},
        {"preferred_term": name2},
        confidence,
    )

    assert recommendation is should_merge
    assert reason_fragment in reason
