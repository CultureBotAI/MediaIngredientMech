"""Rules G, H and I — the invariants a review found already true (#301, #504, #529).

Each of these measured zero on the published set when it was checked. That is
exactly when a property is cheapest to pin and easiest to lose: nothing was
watching any of them, so a regression would have shipped silently and the next
sweep would have rediscovered it from scratch.

Every test here drives the rule from a violating fixture, so a rule that stops
detecting fails rather than quietly passing.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

_spec = importlib.util.spec_from_file_location(
    "validate_sssom_invariants",
    Path(__file__).parent.parent / "scripts" / "validate_sssom_invariants.py",
)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


def _row(**kw):
    row = {
        "subject_id": "MIM:Glucose",
        "subject_label": "Glucose",
        "predicate_id": "skos:exactMatch",
        "object_id": "CHEBI:17234",
        "object_label": "glucose",
        "object_source": "obo:chebi.owl",
        "mapping_date": "2026-09-06",
        "other": "",
    }
    row.update(kw)
    return row


class TestRuleG:
    """The header must move when the mappings move (#301)."""

    HEADER = ['# mapping_set_version: "2026-09-06"', '# mapping_date: "2026-09-06"']

    def test_a_header_matching_the_newest_row_passes(self):
        rows = [_row(mapping_date="2026-05-01"), _row(mapping_date="2026-09-06")]
        assert list(mod.evaluate_rule_g(self.HEADER, rows)) == []

    def test_a_stale_header_is_rejected(self):
        """The #301 shape: rows moved on, the hand-edited header did not."""
        rows = [_row(mapping_date="2026-09-08")]
        rejects = list(mod.evaluate_rule_g(self.HEADER, rows))
        assert len(rejects) == 2  # both mapping_set_version and mapping_date
        assert all("2026-09-08" in reason for _, _, reason in rejects)

    def test_a_header_ahead_of_the_data_is_also_rejected(self):
        """Bumping the version by hand without changing a row is the same lie."""
        rows = [_row(mapping_date="2026-08-01")]
        assert len(list(mod.evaluate_rule_g(self.HEADER, rows))) == 2

    def test_only_the_two_header_fields_are_read(self):
        header = ['# mapping_set_id: "https://example.org/x"', '# license: "CC0"']
        assert list(mod.evaluate_rule_g(header, [_row()])) == []

    def test_a_set_with_no_parseable_date_is_left_to_rule_f(self):
        """Rule F owns the empty-date defect; G must not double-report it."""
        assert list(mod.evaluate_rule_g(self.HEADER, [_row(mapping_date="")])) == []


class TestRuleH:
    """One published label belongs to one record (#504)."""

    def test_registry_rows_for_one_record_are_not_a_collision(self):
        """The documented pattern: one subject, several identity rows."""
        rows = [
            _row(object_id="CHEBI:17234"),
            _row(object_id="cas:50-99-7", object_source="registry:cas"),
            _row(object_id="kgmicrobe.compound:glucose", object_source="kgm:compound"),
        ]
        assert list(mod.evaluate_rule_h(rows)) == []

    def test_two_records_sharing_a_label_are_rejected(self):
        rows = [_row(subject_id="MIM:Glucose"), _row(subject_id="MIM:Glucose_2")]
        rejects = list(mod.evaluate_rule_h(rows))
        assert len(rejects) == 1
        assert "MIM:Glucose_2" in rejects[0][2]

    def test_the_comparison_is_case_insensitive(self):
        rows = [_row(subject_id="MIM:A", subject_label="Glucose"),
                _row(subject_id="MIM:B", subject_label="glucose")]
        assert len(list(mod.evaluate_rule_h(rows))) == 1

    def test_blank_labels_are_not_collapsed_together(self):
        """Two unlabelled rows are a different defect, not a name collision."""
        rows = [_row(subject_id="MIM:A", subject_label=""),
                _row(subject_id="MIM:B", subject_label="")]
        assert list(mod.evaluate_rule_h(rows)) == []


class TestRuleI:
    """`other` is merged into a synonym set, so a repeat is waste (#529)."""

    def test_distinct_tokens_pass(self):
        assert list(mod.evaluate_rule_i([_row(other="D-lactate|D-2-hydroxypropanoate")])) == []

    def test_a_repeated_token_is_rejected(self):
        rejects = list(mod.evaluate_rule_i([_row(other="D-lactate|D-lactate")]))
        assert len(rejects) == 1
        assert "D-lactate" in rejects[0][2]

    def test_the_repeat_check_is_case_insensitive(self):
        """The consumer indexes case-insensitively, so these are one token."""
        assert len(list(mod.evaluate_rule_i([_row(other="D-Lactate|d-lactate")]))) == 1

    def test_an_empty_column_passes(self):
        assert list(mod.evaluate_rule_i([_row(other="")])) == []

    def test_surrounding_whitespace_does_not_hide_a_repeat(self):
        assert len(list(mod.evaluate_rule_i([_row(other="D-lactate| D-lactate ")]))) == 1


class TestRuleJ:
    """`other` is merged into synonyms, so curation notes cannot be tokens."""

    def test_real_synonyms_pass(self):
        assert list(mod.evaluate_rule_j([_row(other="D-lactate|D-2-hydroxypropanoate")])) == []

    def test_an_original_amount_note_is_rejected(self):
        rejects = list(mod.evaluate_rule_j([
            _row(other="D-lactate|Original amount: (NH4)2HPO4(Fisher A686)"),
        ]))
        assert len(rejects) == 1
        assert "Original amount: (NH4)2HPO4(Fisher A686)" in rejects[0][2]

    def test_an_empty_column_passes(self):
        assert list(mod.evaluate_rule_j([_row(other="")])) == []


def test_the_published_set_satisfies_all_pinned_rules():
    """The point of pinning them: they hold today, and must keep holding."""
    path = Path(__file__).parent.parent / "mappings" / "ingredient_mappings.sssom.tsv"
    prelude, _, rows = mod._read_sssom(path)
    assert list(mod.evaluate_rule_g(prelude, rows)) == []
    assert list(mod.evaluate_rule_h(rows)) == []
    assert list(mod.evaluate_rule_i(rows)) == []
    assert list(mod.evaluate_rule_j(rows)) == []


@pytest.mark.parametrize("rule", ["Rule G", "Rule H", "Rule I", "Rule J"])
def test_each_rule_is_wired_into_the_run(rule):
    """A rule nobody calls is not a gate."""
    source = (Path(__file__).parent.parent / "scripts" / "validate_sssom_invariants.py").read_text()
    assert f'_collect("{rule}"' in source
    assert rule.replace("Rule ", "") in source.split("rule_summary = ")[1].split("\n")[0]
