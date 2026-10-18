"""Mapping-change receipts are chain links, never approvals (#742, #743).

A receipt records a verified batch of mapping corrections (re-anchored parents,
regrades, re-groundings, merges, mints) as an explicit, auditable link after
the synonym-only refreshes. Two things must hold for the reviewed release to
stay honest: ``make_receipt.align`` must describe exactly what moved, and the
assembler's ``walk_mapping_changes`` must refuse any receipt that does not
chain -- by digest, by sequence, by approval, or by the row it claims to
change -- including a row corrected twice, whose second ``before`` is the
first ``after`` and not the baseline.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).parent.parent
sys.path.insert(0, str(_REPO / "src"))


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


receipt_mod = _load(
    "make_receipt", _REPO / "reports/sssom_completion_20260921/mapping_changes/make_receipt.py"
)
assemble = _load("assemble_review", _REPO / "reports/sssom_completion_20260921/assemble_review.py")


def _row(subject, obj, predicate="skos:exactMatch", **extra):
    row = {"subject_id": subject, "predicate_id": predicate, "object_id": obj, "other": ""}
    row.update(extra)
    return row


BASE = [
    _row("MIM:A", "CHEBI:1"),
    _row("MIM:B", "CHEBI:2", "skos:broadMatch"),
    _row("MIM:B", "cas:1-1-1"),
    _row("MIM:C", "CHEBI:3"),
]


# --- make_receipt.align -----------------------------------------------------


def test_align_reports_changed_added_removed_and_position_map():
    after = [
        _row("MIM:A", "CHEBI:1"),
        _row("MIM:B", "CHEBI:20", "skos:broadMatch"),  # parent re-anchored in place
        _row("MIM:B", "cas:1-1-1"),
        # MIM:C removed (merged away)
        _row("MIM:D", "kgmicrobe.compound:d"),  # minted
    ]
    changes, position_map = receipt_mod.align(BASE, after)
    kinds = {(c["kind"], c["before_position"], c["after_position"]) for c in changes}
    assert kinds == {("changed", 2, 2), ("removed", 4, None), ("added", None, 4)}
    assert position_map == [1, 2, 3, None]
    changed = next(c for c in changes if c["kind"] == "changed")
    assert changed["before"]["object_id"] == "CHEBI:2" and changed["after"]["object_id"] == "CHEBI:20"


def test_align_refuses_two_rows_in_one_slot():
    doubled = BASE + [_row("MIM:A", "CHEBI:99", "skos:closeMatch")]
    with pytest.raises(ValueError, match="share a slot"):
        receipt_mod.align(doubled, doubled)


def test_slot_distinguishes_registry_rows_from_the_ontology_row():
    assert receipt_mod.slot(_row("MIM:X", "cas:1-1-1")) == ("MIM:X", "cas")
    assert receipt_mod.slot(_row("MIM:X", "kgmicrobe.ingredient:x")) == ("MIM:X", "kgmicrobe.ingredient")
    assert receipt_mod.slot(_row("MIM:X", "CHEBI:1")) == ("MIM:X", "ontology")
    assert receipt_mod.slot(_row("MIM:X", "mesh:D1")) == ("MIM:X", "ontology")


# --- assemble_review.walk_mapping_changes -----------------------------------


def _receipt(batch, sequence, before, after, changes, position_map, before_rows, after_rows, **overrides):
    receipt = {
        "schema_version": 1,
        "batch": batch,
        "sequence": sequence,
        "approval": "NONE: withheld pending mapping-specific review",
        "before_sha256": before,
        "after_sha256": after,
        "before_row_count": before_rows,
        "after_row_count": after_rows,
        "records": [],
        "changes": changes,
        "position_map": position_map,
    }
    receipt.update(overrides)
    return receipt


def _first_batch():
    """Re-anchor MIM:B's parent in place."""
    return _receipt(
        "b1", 1, "s0", "s1",
        [{"kind": "changed", "before_position": 2, "after_position": 2,
          "before": BASE[1], "after": _row("MIM:B", "CHEBI:20", "skos:broadMatch")}],
        [1, 2, 3, 4], 4, 4,
    )


def _second_batch():
    """Re-anchor MIM:B again, merge MIM:C away, mint MIM:D at the end."""
    return _receipt(
        "b2", 2, "s1", "s2",
        [{"kind": "changed", "before_position": 2, "after_position": 2,
          "before": _row("MIM:B", "CHEBI:20", "skos:broadMatch"),
          "after": _row("MIM:B", "CHEBI:200", "skos:broadMatch")},
         {"kind": "removed", "before_position": 4, "after_position": None, "before": BASE[3], "after": None},
         {"kind": "added", "before_position": None, "after_position": 4, "before": None,
          "after": _row("MIM:D", "kgmicrobe.compound:d")}],
        [1, 2, 3, None], 4, 4,
    )


def _walk(receipts, reviewed="s2", refreshed=None):
    return assemble.walk_mapping_changes(
        receipts, start_sha256="s0", reviewed_sha256=reviewed, baseline_rows=BASE,
        refreshed_rows=refreshed or {},
    )


def test_two_receipts_chain_through_the_first_correction():
    forward, last, state = _walk([_second_batch(), _first_batch()])  # any order in
    assert forward == [1, 2, 3, None]
    assert set(last) == {2, 4}
    assert last[2]["receipt"] == "b2" and last[2]["after"]["object_id"] == "CHEBI:200"
    assert last[4]["kind"] == "added" and last[4]["receipt"] == "b2"
    assert [r["subject_id"] for r in state] == ["MIM:A", "MIM:B", "MIM:B", "MIM:D"]
    assert state[1]["object_id"] == "CHEBI:200"


def test_second_receipt_must_chain_from_the_first_after_not_the_baseline():
    second = _second_batch()
    second["changes"][0]["before"] = BASE[1]  # claims the baseline row as its "before"
    with pytest.raises(ValueError, match="does not chain from the reviewed row"):
        _walk([_first_batch(), second])


def test_receipt_before_must_match_the_synonym_refreshed_row():
    refreshed = {2: dict(BASE[1], other="alias")}
    first = _first_batch()  # its "before" is the baseline row, not the refreshed one
    with pytest.raises(ValueError, match="does not chain from the reviewed row"):
        _walk([first], reviewed="s1", refreshed=refreshed)
    first["changes"][0]["before"] = refreshed[2]
    forward, last, state = _walk([first], reviewed="s1", refreshed=refreshed)
    assert last[2]["after"]["object_id"] == "CHEBI:20"


@pytest.mark.parametrize(
    "mutate, message",
    [
        (lambda r: r.update(sequence=2), "numbered 1..n"),
        (lambda r: r.update(approval="SUPPORTED: verified"), "approval-free"),
        (lambda r: r.update(before_sha256="stale"), "does not chain from the previous link"),
        (lambda r: r.update(after_sha256="other"), "does not produce the reviewed source"),
        (lambda r: r.update(position_map=[1, 2, 3]), "position map is incomplete"),
        (lambda r: r.update(position_map=[1, 2, 2, 4]), "not injective"),
        (lambda r: r["changes"].append({"kind": "added", "before_position": None, "after_position": 1,
                                        "before": None, "after": _row("MIM:Z", "CHEBI:9")}),
         "occupied position"),
        (lambda r: r["changes"].__setitem__(0, dict(r["changes"][0], kind="renamed")), "unknown change kind"),
    ],
)
def test_broken_single_receipt_is_refused(mutate, message):
    receipt = _first_batch()
    mutate(receipt)
    with pytest.raises(ValueError, match=message):
        _walk([receipt], reviewed="s1")


def test_removed_row_must_leave_the_position_map():
    second = _second_batch()
    second["position_map"] = [1, 2, 3, 4]  # keeps the row it claims to remove
    second["after_row_count"] = 5
    second["changes"][2]["after_position"] = 5
    with pytest.raises(ValueError, match="removes a row its position map keeps"):
        _walk([_first_batch(), second])


def test_no_receipts_is_the_identity_walk():
    forward, last, state = _walk([], reviewed="s0")
    assert forward == [1, 2, 3, 4] and last == {} and state == BASE
