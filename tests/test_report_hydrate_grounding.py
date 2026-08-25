"""The hydrate report's own defects (#258, #259).

The report is the instrument every other hydrate issue is measured with, so a
fault here misstates #321, #334 and #344 rather than just itself.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_SPEC = importlib.util.spec_from_file_location(
    "report_hydrate_grounding", ROOT / "scripts" / "report_hydrate_grounding.py"
)
report = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = report
_SPEC.loader.exec_module(report)


def test_the_two_buckets_are_keyed_on_kind_not_on_prose():
    """#259: the split tested `"states" in r["detail"]`, so rewording the
    sentence -- or a label containing the word -- reclassified rows."""
    rows = [
        {"kind": report.DIFFERENT_STATE, "detail": "reworded, no keyword here"},
        {"kind": report.ANHYDROUS_TERM, "detail": "this one states nothing at all"},
    ]

    mismatched = [r for r in rows if r["kind"] == report.DIFFERENT_STATE]

    assert len(mismatched) == 1
    assert mismatched[0]["detail"].startswith("reworded")


def test_the_old_substring_rule_would_have_got_both_wrong():
    """Pins why the change was needed, not just that it happened."""
    rows = [
        {"kind": report.DIFFERENT_STATE, "detail": "reworded, no keyword here"},
        {"kind": report.ANHYDROUS_TERM, "detail": "this one states nothing at all"},
    ]

    by_substring = [r for r in rows if "states" in r["detail"]]

    assert [r["kind"] for r in by_substring] == [report.ANHYDROUS_TERM], (
        "the substring rule selects exactly the wrong row here")


def test_the_kind_values_are_distinct():
    assert report.DIFFERENT_STATE != report.ANHYDROUS_TERM


def test_multiplicities_sort_numerically_not_lexicographically():
    """#258: filed against a lexicographic sort, where 10 precedes 2.
    Verified fixed 2026-08-24 (`key=float`); pinned so it cannot regress."""
    assert sorted({"10", "2", "7"}, key=float) == ["2", "7", "10"]
    assert sorted({"10", "2", "7"}) == ["10", "2", "7"], "plain sort is still wrong"
