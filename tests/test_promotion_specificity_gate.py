"""The specificity half of the microbedecoder promotion gate (#203).

The round-trip half — id resolves, canonical label equals the record's stored
label — is tautological: that stored label came from the same OLS lookup that
produced the grounding, so it re-derives the identity that created the mapping
and passed 386/386 of the population it was written for. It would approve any
wrong grounding whose id resolves.

`MIM:Sulfonamide -> CHEBI:35358` is where that mattered: the structural
functional-group class (2976 direct subclasses) was approved when the intended
target was `CHEBI:87228 "sulfonamide antibiotic"` (24). Since `skos:exactMatch`
licenses node substitution, publishing it would let kg-microbe collapse every
sulfonamide-resistance edge onto the functional-group node.

These pin the decision logic against a synthetic index (real subclass counts,
from the live ChEBI build) so they run without an OAK download.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

_spec = importlib.util.spec_from_file_location(
    "promote_microbedecoder_reviewed",
    Path(__file__).resolve().parent.parent / "scripts"
    / "promote_microbedecoder_reviewed.py",
)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)

ALARM = mod.DEFAULT_SUBCLASS_ALARM

# Direct-subclass counts measured against the local ChEBI build.
COUNTS = {
    "CHEBI:35358": 2976,   # sulfonamide -- the functional-group class (the bad one)
    "CHEBI:87228": 24,     # sulfonamide antibiotic -- the intended target
    "CHEBI:3098": 415,     # bile acid
    "CHEBI:25000": 164,    # lactone
    "CHEBI:33709": 57,     # amino acid
    "CHEBI:59062": 11,     # polymyxin -- narrow, but has 16 more specific labels
    "CHEBI:338412": 0,     # (-)-anisomycin -- a leaf substance
    "CHEBI:474053": 0,     # cefazolin
}
LABELS = {
    "sulfonamide", "sulfonamide antibiotic", "sulfonamide fungicide",
    "bile acid", "bile acid anion", "lactone", "amino acid", "amino acid amide",
    "polymyxin", "polymyxin b", "(-)-anisomycin", "cefazolin",
}
INDEX = {"CHEBI": (COUNTS, LABELS)}


def alarm(curie: str, label: str, threshold: int = ALARM):
    return mod._specificity_alarm(INDEX, curie, label, threshold)


def test_the_known_bad_grounding_is_held():
    """CHEBI:35358 is the one wrong grounding the old gate let through (#203)."""
    reason = alarm("CHEBI:35358", "sulfonamide")
    assert reason is not None, "the functional-group class must not auto-promote"
    assert "2976" in reason
    # The reason names the evidence, so the manifest records WHY, not just that.
    assert "sulfonamide antibiotic" in reason


def test_the_intended_target_is_not_held():
    """The gate must not also reject the term the curator actually wants.

    A check that flags both is no more useful than one that flags neither.
    """
    assert alarm("CHEBI:87228", "sulfonamide antibiotic") is None


@pytest.mark.parametrize("curie,label", [
    ("CHEBI:3098", "bile acid"),
    ("CHEBI:25000", "lactone"),
    ("CHEBI:33709", "amino acid"),
])
def test_broad_class_level_terms_are_held(curie, label):
    assert alarm(curie, label) is not None


@pytest.mark.parametrize("curie,label", [
    ("CHEBI:338412", "(-)-anisomycin"),
    ("CHEBI:474053", "cefazolin"),
])
def test_leaf_substances_promote_freely(curie, label):
    """These are the #207 antibiotics/substances; holding them would be a false alarm."""
    assert alarm(curie, label) is None


def test_prefix_ambiguity_alone_does_not_hold_a_narrow_term():
    """`polymyxin` has 16 strictly-more-specific labels but only 11 subclasses.

    The prefix signal on its own fires on 163 of 403 rows — too noisy to gate on —
    so it only counts above PREFIX_SUBCLASS_FLOOR. Raising the floor above 11
    releases polymyxin; the default (10) holds it.
    """
    assert alarm("CHEBI:59062", "polymyxin") is not None
    assert mod._specificity_alarm(
        {"CHEBI": (COUNTS, LABELS)}, "CHEBI:59062", "polymyxin", ALARM
    ) is not None
    # With the prefix rule effectively disabled it is narrow enough to pass.
    saved = mod.PREFIX_SUBCLASS_FLOOR
    try:
        mod.PREFIX_SUBCLASS_FLOOR = 10_000
        assert alarm("CHEBI:59062", "polymyxin") is None
    finally:
        mod.PREFIX_SUBCLASS_FLOOR = saved


@pytest.mark.parametrize("curie,label", [
    ("CHEBI:35358", "sulfonamide"),               # the broadest term in the corpus
    ("CHEBI:87228", "sulfonamide antibiotic"),
    ("CHEBI:59062", "polymyxin"),                 # trips the prefix rule at the default
])
def test_threshold_zero_really_disables_the_check(curie, label):
    """`--subclass-alarm 0` is the documented escape hatch, so it must DISABLE.

    Without an explicit guard, `n > 0` flags every term carrying even one subclass —
    the exact opposite of the help text. A curator reaching for the escape hatch
    would have held nearly the whole batch.
    """
    assert alarm(curie, label, 0) is None


def test_an_unindexed_ontology_cannot_judge_and_says_so():
    """No index (adapter without a SQL engine) must be a no-op, never a false alarm."""
    assert mod._specificity_alarm({"NCIT": ({}, set())}, "NCIT:C123", "whatever", ALARM) is None
    assert mod._specificity_alarm({}, "FOODON:1", "whatever", ALARM) is None
