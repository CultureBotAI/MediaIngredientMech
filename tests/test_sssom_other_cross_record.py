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


@pytest.mark.parametrize("status", ["MAPPED", "AMBIGUOUS"])
def test_active_record_keeps_ownership_even_when_ambiguous(tmp_path, monkeypatch, status):
    path = tmp_path / "active.yaml"
    path.write_text(f"preferred_term: Old label\nmapping_status: {status}\n")
    monkeypatch.setattr(val, "_subject_to_path", lambda: {"MIM:Active": path})
    monkeypatch.setattr(val, "_other_baseline", frozenset)
    try:
        val._preferred_term_owners.cache_clear()
        assert val._preferred_term_owners()["old label"] == frozenset({"MIM:Active"})
        assert list(val.evaluate_rule_k(_rows(other="Old label")))
    finally:
        val._preferred_term_owners.cache_clear()


def _tombstone_corpus(tmp_path, monkeypatch, target_identifier="CHEBI:30089", representative=None):
    live = tmp_path / "Acetate.yaml"
    live.write_text(
        "identifier: CHEBI:30089\npreferred_term: Acetate\nmapping_status: MAPPED\n", encoding="utf-8"
    )
    other = tmp_path / "Sodium_Acetate.yaml"
    other.write_text(
        "identifier: CHEBI:32954\npreferred_term: Sodium acetate\nmapping_status: MAPPED\n",
        encoding="utf-8",
    )
    tomb = tmp_path / "Acetate_Carbon_Source.yaml"
    tombstone_text = (
        f"identifier: {target_identifier}\npreferred_term: Acetate (carbon source)\n"
        "mapping_status: REJECTED\n"
    )
    if representative is not None:
        tombstone_text += f"representative: {representative}\n"
    tomb.write_text(tombstone_text, encoding="utf-8")
    monkeypatch.setattr(
        val, "_subject_to_path",
        lambda: {"MIM:Acetate": live, "MIM:Sodium_Acetate": other, "MIM:Acetate_Carbon_Source": tomb},
    )
    monkeypatch.setattr(val, "_other_baseline", frozenset)
    val._preferred_term_owners.cache_clear()


def test_a_merge_tombstones_name_belongs_to_its_target(tmp_path, monkeypatch):
    """A REJECTED record under mapped/ is a merge tombstone (#669): the merge
    moved the name to the live record sharing its identifier, so that record
    carrying it is the rightful holder -- Rule K had baselined 51 such pairs."""
    _tombstone_corpus(tmp_path, monkeypatch)
    try:
        assert val._preferred_term_owners()["acetate (carbon source)"] == frozenset({"MIM:Acetate"})
        target_row = [{"subject_id": "MIM:Acetate", "other": "Acetate (carbon source)"}]
        assert list(val.evaluate_rule_k(target_row)) == []
    finally:
        val._preferred_term_owners.cache_clear()


def test_a_tombstones_name_is_still_refused_to_everyone_else(tmp_path, monkeypatch):
    """The first version of the #669 fix DROPPED the tombstone's name instead of
    crediting it, which left it with no owner: any record could then publish it
    unflagged. An adversarial review caught it -- ``MIM:Feso4`` carrying a
    heptahydrate tombstone's name passed where ``main`` had flagged it."""
    _tombstone_corpus(tmp_path, monkeypatch)
    try:
        thief = [{"subject_id": "MIM:Sodium_Acetate", "other": "Acetate (carbon source)"}]
        findings = list(val.evaluate_rule_k(thief))
        assert findings and "MIM:Acetate" in findings[0][2]
    finally:
        val._preferred_term_owners.cache_clear()


def test_a_rejected_record_with_no_live_target_keeps_its_own_name(tmp_path, monkeypatch):
    """ "REJECTED means merged" is an observed fact, not an enforced invariant --
    ``retire_assay_labels`` writes REJECTED records that were never merged. With
    no live record sharing the identifier, the name must not become ownerless."""
    _tombstone_corpus(tmp_path, monkeypatch, target_identifier="CHEBI:99999999")
    try:
        assert val._preferred_term_owners()["acetate (carbon source)"] == frozenset(
            {"MIM:Acetate_Carbon_Source"}
        )
        assert list(val.evaluate_rule_k([{"subject_id": "MIM:Acetate", "other": "Acetate (carbon source)"}]))
    finally:
        val._preferred_term_owners.cache_clear()


def test_explicit_representative_owns_name_instead_of_old_identifier(tmp_path, monkeypatch):
    """A corrected merge target wins over the loser's retained wrong identifier."""
    _tombstone_corpus(
        tmp_path, monkeypatch, target_identifier="CHEBI:32954", representative="CHEBI:30089"
    )
    try:
        assert val._preferred_term_owners()["acetate (carbon source)"] == frozenset({"MIM:Acetate"})
        assert not list(val.evaluate_rule_k(_rows("MIM:Acetate", "Acetate (carbon source)")))
        assert list(val.evaluate_rule_k(_rows("MIM:Sodium_Acetate", "Acetate (carbon source)")))
    finally:
        val._preferred_term_owners.cache_clear()


@pytest.mark.parametrize("representative", ["CHEBI:99999999", ""])
def test_missing_explicit_target_never_credits_former_identifier_owner(
    tmp_path, monkeypatch, representative
):
    _tombstone_corpus(
        tmp_path, monkeypatch, target_identifier="CHEBI:30089", representative=representative
    )
    try:
        assert val._preferred_term_owners()["acetate (carbon source)"] == frozenset(
            {"MIM:Acetate_Carbon_Source"}
        )
        assert list(val.evaluate_rule_k(_rows("MIM:Acetate", "Acetate (carbon source)")))
    finally:
        val._preferred_term_owners.cache_clear()


def test_the_baseline_has_no_unused_entries():
    """A stale entry silently licenses the pair's reintroduction."""
    text = (_REPO / "mappings" / "ingredient_mappings.sssom.tsv").read_text(encoding="utf-8")
    rows = list(csv.DictReader([ln for ln in text.splitlines() if not ln.startswith("#")], delimiter="\t"))
    val._preferred_term_owners.cache_clear()
    owners = val._preferred_term_owners()
    live = set()
    for row in rows:
        subject = (row.get("subject_id") or "").strip()
        for token in (row.get("other") or "").split("|"):
            token = token.strip()
            holder = owners.get(token.casefold()) if token else None
            if holder and subject not in holder:
                live.add((subject, token.casefold()))
    unused = sorted(val._other_baseline() - live)
    assert not unused, f"baseline entries matching no live violation: {unused[:5]}"
