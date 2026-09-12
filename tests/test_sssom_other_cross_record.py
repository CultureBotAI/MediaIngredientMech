"""Rule K — `other` must not publish a name another record owns (#669, #622).

kg-microbe merges `other` into the ontology entity's synonym set, so a token
there is a name the subject answers to. When it is another record's
`preferred_term`, two records claim one name and the distinction stops existing
downstream -- a monohydrate ends up answering to the anhydrous compound's name,
which is the conflation MAPPING_SEMANTICS Section 3 exists to prevent, arriving
through the synonym channel rather than through `identifier`.

Most of `other` is kg-microbe's synonyms for the *ontology term*, so a hydrate
family sharing one CHEBI parent gets the parent's synonyms merged into every
member. That is the generator's behaviour, so the 115 known pairs are baselined
and the rule blocks new ones.
"""

from __future__ import annotations

import csv
import importlib.util
import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).parent.parent
sys.path.insert(0, str(_REPO / "src"))
_spec = importlib.util.spec_from_file_location(
    "validate_sssom_invariants", _REPO / "scripts" / "validate_sssom_invariants.py"
)
val = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(val)


def _rows(subject_id="MIM:Glucose", other=""):
    return [{"subject_id": subject_id, "subject_label": "Glucose", "other": other}]


def test_a_row_with_no_other_passes():
    assert list(val.evaluate_rule_k(_rows())) == []


def test_a_token_owned_by_nobody_passes():
    assert list(val.evaluate_rule_k(_rows(other="not-a-record-name-xyz"))) == []


def test_a_token_owned_by_another_record_is_rejected(monkeypatch):
    monkeypatch.setattr(val, "_preferred_term_owners",
                        lambda: {"vibriostat": frozenset({"MIM:Vibriostat"})})
    monkeypatch.setattr(val, "_other_baseline", frozenset)
    findings = list(val.evaluate_rule_k(_rows(other="Vibriostat")))
    assert len(findings) == 1
    assert "MIM:Vibriostat" in findings[0][2]


def test_a_record_owning_its_own_name_is_not_a_violation(monkeypatch):
    """A subject may carry its own preferred_term without claiming another's."""
    monkeypatch.setattr(val, "_preferred_term_owners",
                        lambda: {"glucose": frozenset({"MIM:Glucose"})})
    monkeypatch.setattr(val, "_other_baseline", frozenset)
    assert list(val.evaluate_rule_k(_rows(other="Glucose"))) == []


def test_matching_is_case_insensitive(monkeypatch):
    monkeypatch.setattr(val, "_preferred_term_owners",
                        lambda: {"vibriostat": frozenset({"MIM:Vibriostat"})})
    monkeypatch.setattr(val, "_other_baseline", frozenset)
    assert list(val.evaluate_rule_k(_rows(other="VIBRIOSTAT")))


def test_a_baselined_pair_is_allowed(monkeypatch):
    monkeypatch.setattr(val, "_preferred_term_owners",
                        lambda: {"vibriostat": frozenset({"MIM:Vibriostat"})})
    monkeypatch.setattr(val, "_other_baseline",
                        lambda: frozenset({("MIM:Glucose", "vibriostat")}))
    assert list(val.evaluate_rule_k(_rows(other="Vibriostat"))) == []


def test_the_baseline_does_not_excuse_a_different_subject(monkeypatch):
    """A baselined pair must not licence the same token on another row."""
    monkeypatch.setattr(val, "_preferred_term_owners",
                        lambda: {"vibriostat": frozenset({"MIM:Vibriostat"})})
    monkeypatch.setattr(val, "_other_baseline",
                        lambda: frozenset({("MIM:Glucose", "vibriostat")}))
    assert list(val.evaluate_rule_k(_rows(subject_id="MIM:Fructose", other="Vibriostat")))


def test_the_baseline_file_is_well_formed():
    path = _REPO / "mappings" / "other_cross_record_baseline.tsv"
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    assert rows, "baseline must not be empty while violations are known"
    assert {"subject_id", "token", "owned_by", "disposition"} <= set(rows[0])
    assert all(r["subject_id"].startswith("MIM:") for r in rows)
    assert all(r["disposition"] for r in rows), "every entry needs a disposition"


def test_the_published_set_passes_rule_k():
    """With the baseline applied, the published set is clean."""
    text = (_REPO / "mappings" / "ingredient_mappings.sssom.tsv").read_text(encoding="utf-8")
    body = [ln for ln in text.splitlines() if not ln.startswith("#")]
    rows = list(csv.DictReader(body, delimiter="\t"))
    assert list(val.evaluate_rule_k(rows)) == []
