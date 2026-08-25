"""Regression tests for current MIM addressing after retirement of `id`."""

from __future__ import annotations

import ast
from pathlib import Path
from types import SimpleNamespace

import pytest
import yaml

from mediaingredientmech.validation.ingredient_reviewer import (
    RULE_P1_3,
    IngredientReviewer,
)
from scripts.enrich_existing_roles import load_crossref_lookup
from scripts.extract_top100_roles import build_record_lookup, extract_roles_for_top100
from scripts.generate_role_statistics import analyze_ingredients

ROOT = Path(__file__).resolve().parent.parent


def _record(identifier: str, preferred_term: str) -> dict:
    return {
        "identifier": identifier,
        "preferred_term": preferred_term,
        "mapping_status": "MAPPED",
        "ontology_mapping": {"ontology_id": identifier},
    }


def test_role_target_lookup_preserves_shared_identifier_siblings():
    first = _record("CHEBI:1", "first form")
    second = _record("CHEBI:1", "second form")
    lookup = build_record_lookup([first, second])

    assert lookup[("CHEBI:1", "first form")] is first
    assert lookup[("CHEBI:1", "second form")] is second


def test_role_target_lookup_rejects_duplicate_composite_address():
    with pytest.raises(ValueError, match="Duplicate role-target address"):
        build_record_lookup([_record("CHEBI:1", "same"), _record("CHEBI:1", "same")])


def test_top100_extraction_resolves_composite_address_in_dry_run():
    first = _record("CHEBI:1", "first form")
    second = _record("CHEBI:1", "second form")
    curator = SimpleNamespace(records=[first, second])
    crossref = {
        "ingredients": [
            {
                "identifier": "CHEBI:1",
                "preferred_term": "first form",
                "occurrence_count": 3,
                "confidence": 0.9,
                "all_roles": ["BUFFER"],
                "raw_annotations": [],
            }
        ]
    }

    assert extract_roles_for_top100(curator, crossref, dry_run=True) == (1, 1, 0)


def test_crossref_lookup_preserves_shared_identifier_siblings(tmp_path):
    path = tmp_path / "crossref.yaml"
    path.write_text(
        yaml.safe_dump(
            {
                "ingredients": [
                    {"identifier": "CHEBI:1", "preferred_term": "first form"},
                    {"identifier": "CHEBI:1", "preferred_term": "second form"},
                ]
            }
        ),
        encoding="utf-8",
    )

    lookup = load_crossref_lookup(path)
    assert set(lookup) == {
        ("CHEBI:1", "first form"),
        ("CHEBI:1", "second form"),
    }


def test_p1_3_allows_distinct_identity_and_grounding_but_rejects_placeholder(
    monkeypatch,
):
    reviewer = IngredientReviewer(enable_kg_microbe_checks=False)
    monkeypatch.setattr(reviewer, "check_term_exists", lambda _curie: True)

    matching = _record("CHEBI:1", "matching")
    matching_issues = reviewer._validate_p1(matching, "CHEBI:1", "matching")
    assert not any(issue.rule_id == RULE_P1_3 for issue in matching_issues)

    separately_grounded = _record("kgmicrobe.compound:sugars", "Sugars")
    grounding_issues = reviewer._validate_p1(
        separately_grounded, "CHEBI:16646", "Sugars"
    )
    assert not any(issue.rule_id == RULE_P1_3 for issue in grounding_issues)

    unresolved = _record("UNMAPPED_0001", "unresolved")
    unresolved_issues = reviewer._validate_p1(
        unresolved, "CHEBI:16646", "unresolved"
    )
    assert [issue.rule_id for issue in unresolved_issues].count(RULE_P1_3) == 1


def test_role_statistics_keep_semantic_identity_separate_from_grounding():
    record = _record("kgmicrobe.compound:sugars", "Sugars")
    record["ontology_mapping"] = {"ontology_id": "CHEBI:16646"}
    record["nutritional_roles"] = [
        {"role": "CARBON_SOURCE", "confidence": 0.9, "evidence": []}
    ]

    stats = analyze_ingredients(SimpleNamespace(records=[record]))

    assert stats["top_ingredients"][0]["identifier"] == "kgmicrobe.compound:sugars"
    assert stats["top_ingredients"][0]["ontology_id"] == "CHEBI:16646"


def test_maintained_mim_tools_do_not_read_retired_record_id():
    for relative_path in (
        "scripts/analyze_culturemech_roles.py",
        "scripts/enrich_existing_roles.py",
        "scripts/extract_top100_roles.py",
        "scripts/generate_role_statistics.py",
        "scripts/identify_complex_media.py",
    ):
        tree = ast.parse((ROOT / relative_path).read_text(encoding="utf-8"))
        retired_reads = []
        for node in ast.walk(tree):
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "get"
                and node.args
                and isinstance(node.args[0], ast.Constant)
                and node.args[0].value == "id"
            ):
                retired_reads.append(node.lineno)
            if (
                isinstance(node, ast.Subscript)
                and isinstance(node.slice, ast.Constant)
                and node.slice.value == "id"
            ):
                retired_reads.append(node.lineno)
        assert not retired_reads, f"{relative_path} reads retired id at {retired_reads}"


def test_complex_media_detector_is_read_only():
    text = (ROOT / "scripts" / "identify_complex_media.py").read_text(encoding="utf-8")
    assert "reclassify_record" not in text
    assert "auto-reclassify" not in text
