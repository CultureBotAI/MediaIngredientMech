"""Source-scoped occurrence counts survive a merge (#196).

`occurrence_statistics.total_occurrences` / `media_count` count CultureMech media
recipes, so they are legitimately 0 for an ingredient sourced from BacDive traits
or Bergey substrates. `source_occurrences` keeps that source's own prevalence
signal without inflating the media counts.

The merge path is where it can vanish silently: `merge_mapped_records` sums the
two totals and then replaces the SOURCE record's whole stats block with zeros as
a tombstone. Anything not moved before that point is destroyed, not just
double-counted.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "merge_mapped_records",
    Path(__file__).resolve().parent.parent / "scripts" / "merge_mapped_records.py",
)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)

transfer = mod.transfer_occurrences


def test_totals_are_summed():
    src = {"occurrence_statistics": {"total_occurrences": 25, "media_count": 3}}
    dst = {"occurrence_statistics": {"total_occurrences": 11, "media_count": 2}}
    assert transfer(src, dst) == (25, 3)
    assert dst["occurrence_statistics"]["total_occurrences"] == 36
    assert dst["occurrence_statistics"]["media_count"] == 5


def test_source_counts_move_when_the_destination_has_none():
    """The signal must not be left behind on a record about to be zeroed."""
    src = {"occurrence_statistics": {
        "total_occurrences": 0, "media_count": 0,
        "source_occurrences": [
            {"source": "microbedecoder", "count": 3569,
             "source_columns": "BacDive_Metabolite_utilization"}]}}
    dst = {"occurrence_statistics": {"total_occurrences": 4, "media_count": 1}}
    transfer(src, dst)
    got = dst["occurrence_statistics"]["source_occurrences"]
    assert got == [{"source": "microbedecoder", "count": 3569,
                    "source_columns": "BacDive_Metabolite_utilization"}]
    # and the media totals are untouched by a non-media signal
    assert dst["occurrence_statistics"]["total_occurrences"] == 4


def test_same_source_on_both_sides_is_summed_not_duplicated():
    src = {"occurrence_statistics": {
        "source_occurrences": [{"source": "microbedecoder", "count": 100}]}}
    dst = {"occurrence_statistics": {
        "source_occurrences": [{"source": "microbedecoder", "count": 25}]}}
    transfer(src, dst)
    got = dst["occurrence_statistics"]["source_occurrences"]
    assert len(got) == 1, "one entry per source, not one per merge"
    assert got[0]["count"] == 125


def test_distinct_sources_are_kept_separate_and_ordered():
    src = {"occurrence_statistics": {
        "source_occurrences": [{"source": "microbedecoder", "count": 7}]}}
    dst = {"occurrence_statistics": {
        "source_occurrences": [{"source": "bergey", "count": 2}]}}
    transfer(src, dst)
    got = dst["occurrence_statistics"]["source_occurrences"]
    assert [e["source"] for e in got] == ["bergey", "microbedecoder"]


def test_absent_source_counts_do_not_invent_an_empty_key():
    """Records with no source signal must not grow an empty list."""
    src = {"occurrence_statistics": {"total_occurrences": 1, "media_count": 1}}
    dst = {"occurrence_statistics": {"total_occurrences": 0, "media_count": 0}}
    transfer(src, dst)
    assert "source_occurrences" not in dst["occurrence_statistics"]


def test_the_source_record_is_not_mutated_by_the_transfer():
    """Mutating src here would corrupt the tombstone the caller writes next."""
    src = {"occurrence_statistics": {
        "source_occurrences": [{"source": "microbedecoder", "count": 10}]}}
    dst = {"occurrence_statistics": {
        "source_occurrences": [{"source": "microbedecoder", "count": 5}]}}
    transfer(src, dst)
    assert src["occurrence_statistics"]["source_occurrences"][0]["count"] == 10
