"""Turning the kg-microbe cross-reference off, and proving it stays off (#589).

Loading the dictionary costs ~5s and ~350MB. `review_ingredient.py` reviews a
single record per invocation and paid that whole cost for two rules, so both
review CLIs grew a `--no-kg-microbe` flag.

A flag that merely parses is worth nothing, so these assert the behaviour
underneath it: the dictionary is never constructed, never read, and the two
rules return no findings.
"""

from __future__ import annotations

import ast
from pathlib import Path

import pytest

from mediaingredientmech.validation.ingredient_reviewer import IngredientReviewer

ROOT = Path(__file__).resolve().parents[1]


def test_disabled_never_touches_the_dictionary(monkeypatch):
    """The point of the flag: not a faster load, no load."""

    def explode(*args, **kwargs):  # pragma: no cover - must never run
        raise AssertionError("KgMicrobeDict was constructed despite the checks being off")

    monkeypatch.setattr(
        "mediaingredientmech.validation.ingredient_reviewer.KgMicrobeDict", explode
    )
    reviewer = IngredientReviewer(enable_kg_microbe_checks=False)
    assert reviewer._get_kg_microbe_dict() is None


def test_the_two_rules_return_nothing_when_disabled():
    reviewer = IngredientReviewer(enable_kg_microbe_checks=False)
    record = {"preferred_term": "Glucose", "synonyms": [{"synonym_text": "Dextrose"}]}

    issues, suggestions = reviewer._check_kg_microbe_disagreement(
        record, "CHEBI:17234", "CHEBI:17234"
    )
    assert (issues, suggestions) == ([], [])

    issues, suggestions = reviewer._check_kg_microbe_synonym_enrichment(
        record, "CHEBI:17234", "CHEBI:17234"
    )
    assert (issues, suggestions) == ([], [])


def test_enabled_is_still_the_default():
    """The flag opts out; it must not quietly become the new normal."""
    assert IngredientReviewer().enable_kg_microbe_checks is True


@pytest.mark.parametrize("script", ["review_ingredient.py", "batch_review.py"])
def test_both_review_clis_expose_the_flag(script):
    """Parsed from the source, so the assertion does not depend on importing a CLI."""
    tree = ast.parse((ROOT / "scripts" / script).read_text(encoding="utf-8"))
    flags = {
        arg.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "add_argument"
        for arg in node.args
        if isinstance(arg, ast.Constant) and isinstance(arg.value, str)
    }
    assert "--no-kg-microbe" in flags


@pytest.mark.parametrize("script", ["review_ingredient.py", "batch_review.py"])
def test_the_flag_is_wired_to_the_reviewer(script):
    """A flag that parses but is never read is the failure this guards."""
    source = (ROOT / "scripts" / script).read_text(encoding="utf-8")
    assert "enable_kg_microbe_checks=not args.no_kg_microbe" in source
