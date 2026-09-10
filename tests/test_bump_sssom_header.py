"""`just bump-sssom-header` — the one command that satisfies Rule G (#602).

Rule G makes a stale header a blocking failure, which is the point (#301), but
every MIM-side row writer appends without touching the header, so without a
bump the only way out of a red gate is hand-editing the field that went stale
in the first place.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

_spec = importlib.util.spec_from_file_location(
    "bump_sssom_header",
    Path(__file__).parent.parent / "scripts" / "bump_sssom_header.py",
)
bump = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(bump)

HEADER = [
    '# mapping_set_id: "https://example.org/x"\n',
    '# mapping_set_version: "2026-08-06"\n',
    '# mapping_date: "2026-08-06"\n',
]
COLUMNS = "subject_id\tobject_id\tmapping_date\n"


def _lines(*dates: str) -> list[str]:
    return HEADER + [COLUMNS] + [f"MIM:X\tCHEBI:1\t{d}\n" for d in dates]


def test_the_newest_row_date_wins_regardless_of_order():
    assert bump.newest_row_date(_lines("2026-05-01", "2026-09-09", "2026-07-04")) == "2026-09-09"


def test_unparseable_dates_are_ignored():
    assert bump.newest_row_date(_lines("2026-05-01", "", "not-a-date")) == "2026-05-01"


def test_no_parseable_date_returns_none():
    assert bump.newest_row_date(_lines("", "nope")) is None


def test_a_set_with_no_rows_returns_none():
    assert bump.newest_row_date(HEADER + [COLUMNS]) is None


def test_both_header_fields_move_together():
    lines, changed = bump.rewrite(_lines("2026-09-09"), "2026-09-09")
    assert changed == {"mapping_set_version": "2026-08-06", "mapping_date": "2026-08-06"}
    assert '# mapping_set_version: "2026-09-09"\n' in lines
    assert '# mapping_date: "2026-09-09"\n' in lines


def test_an_already_current_header_reports_no_change():
    _, changed = bump.rewrite(_lines("2026-08-06"), "2026-08-06")
    assert changed == {}


def test_other_header_fields_are_untouched():
    lines, _ = bump.rewrite(_lines("2026-09-09"), "2026-09-09")
    assert '# mapping_set_id: "https://example.org/x"\n' in lines


def test_rows_are_untouched(tmp_path):
    lines, _ = bump.rewrite(_lines("2026-09-09"), "2026-09-09")
    assert lines[-1] == "MIM:X\tCHEBI:1\t2026-09-09\n"


def test_a_dry_run_writes_nothing(tmp_path):
    path = tmp_path / "s.tsv"
    path.write_text("".join(_lines("2026-09-09")), encoding="utf-8")
    before = path.read_text(encoding="utf-8")
    assert bump.main(["--sssom", str(path)]) == 0
    assert path.read_text(encoding="utf-8") == before


def test_apply_writes_the_newest_date(tmp_path):
    path = tmp_path / "s.tsv"
    path.write_text("".join(_lines("2026-05-01", "2026-09-09")), encoding="utf-8")
    assert bump.main(["--sssom", str(path), "--apply"]) == 0
    text = path.read_text(encoding="utf-8")
    assert '# mapping_set_version: "2026-09-09"' in text
    assert '# mapping_date: "2026-09-09"' in text


def test_a_set_with_no_dates_refuses_rather_than_stamping_nothing(tmp_path):
    path = tmp_path / "s.tsv"
    path.write_text("".join(_lines("")), encoding="utf-8")
    assert bump.main(["--sssom", str(path), "--apply"]) == 1


def test_the_result_satisfies_rule_g():
    """Ties this script to the rule it exists to satisfy, not just to itself."""
    validator_spec = importlib.util.spec_from_file_location(
        "validate_sssom_invariants",
        Path(__file__).parent.parent / "scripts" / "validate_sssom_invariants.py",
    )
    validator = importlib.util.module_from_spec(validator_spec)
    validator_spec.loader.exec_module(validator)

    lines = _lines("2026-05-01", "2026-09-09")
    rows = [{"mapping_date": "2026-05-01"}, {"mapping_date": "2026-09-09"}]
    stale_header = [ln.rstrip("\n") for ln in lines if ln.startswith("#")]
    assert list(validator.evaluate_rule_g(stale_header, rows))  # red before

    bumped, _ = bump.rewrite(lines, bump.newest_row_date(lines))
    fresh_header = [ln.rstrip("\n") for ln in bumped if ln.startswith("#")]
    assert list(validator.evaluate_rule_g(fresh_header, rows)) == []  # green after
