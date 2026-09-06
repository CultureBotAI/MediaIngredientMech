"""Rule F: a published row without a real `mapping_date` is a reject (#550).

The builder emits an empty cell when a record has no parseable
`curation_history` timestamp -- deliberately, since the mtime fallback it
replaced stamped records with whenever the machine cloned (#542). But nothing
else rejected the blank: the shared contract does not mention the column and
the `sssom` package's JSON-schema validation accepts it, verified by blanking a
real row. The builder's warning is one line in a log of hundreds, so a dateless
row would have shipped through every gate the repo has.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def _load():
    spec = importlib.util.spec_from_file_location(
        "validate_sssom_invariants", REPO / "scripts" / "validate_sssom_invariants.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


validator = _load()


def _row(mapping_date: str, subject: str = "MIM:Thing") -> dict[str, str]:
    return {
        "subject_id": subject,
        "predicate_id": "skos:exactMatch",
        "object_id": "CHEBI:1",
        "mapping_date": mapping_date,
    }


def test_dated_rows_pass():
    """The normal case must not produce a reject."""
    rows = [_row("2026-09-06"), _row("2025-01-01", "MIM:Other")]
    assert list(validator.evaluate_rule_f(rows)) == []


def test_empty_date_is_rejected_and_names_the_subject():
    """The exact case the builder now produces on a history-less record."""
    rejects = list(validator.evaluate_rule_f([_row("")]))
    assert len(rejects) == 1
    row_num, row, reason = rejects[0]
    assert row_num == 1
    assert row["subject_id"] == "MIM:Thing"
    assert "empty" in reason
    assert "MIM:Thing" in reason
    assert "#550" in reason


def test_malformed_date_is_rejected():
    """A value that is present but not YYYY-MM-DD is no better than empty."""
    for bad in ("2026-9-6", "yesterday", "2026-09-06T10:00:00", "20260906"):
        rejects = list(validator.evaluate_rule_f([_row(bad)]))
        assert len(rejects) == 1, bad
        assert repr(bad) in rejects[0][2], bad


def test_whitespace_only_counts_as_empty():
    """A cell of spaces must not sneak past as 'present'."""
    rejects = list(validator.evaluate_rule_f([_row("   ")]))
    assert len(rejects) == 1
    assert "empty" in rejects[0][2]


def test_only_offending_rows_are_reported():
    """One bad row among good ones yields exactly one reject, at its position."""
    rows = [_row("2026-01-01", "MIM:A"), _row("", "MIM:B"), _row("2026-01-02", "MIM:C")]
    rejects = list(validator.evaluate_rule_f(rows))
    assert [(n, r["subject_id"]) for n, r, _ in rejects] == [(2, "MIM:B")]
