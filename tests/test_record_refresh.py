"""Section receipts preserve audit history, never approvals across changed bytes.

Built on a real record's bytes so both the audit peel and exact-byte review
boundary are exercised against the maintained per-record serialization.
"""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path

import pytest
import yaml

from mediaingredientmech.record_refresh import (
    RECEIPT_KIND,
    REFRESH_DIR,
    RecordRefreshes,
    dump_record,
    peel,
    sha256,
)

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "data/ingredients/mapped/D-glucose.yaml"
GRAPH = [{
    "graph_id": "d_glucose_uptake",
    "graph_kind": "UPTAKE",
    "scope_status": "MECHANISTIC",
    "nodes": [{"node_id": "glc", "label": "D-glucopyranose", "node_type": "CHEMICAL",
               "grounding": "CHEBI:4167"}],
    "edges": [],
}]


def _event(action="CAUSAL_GRAPH_ADDED", curator="cross_mech_graph_curation", changes=None, **extra):
    event = {"timestamp": "2026-10-05T00:00:00+00:00", "curator": curator, "action": action,
             "changes": changes or "added causal_graphs (UPTAKE) linking sibling-Mech records"}
    event.update(extra)
    return event


def _refresh(record: dict, section: str, value, event: dict) -> tuple[bytes, dict]:
    before = dump_record(record)
    after_record = copy.deepcopy(record)
    after_record[section] = value
    after_record.setdefault("curation_history", []).append(event)
    after = dump_record(after_record)
    entry = {"source_record": SOURCE, "section": section, "before_yaml_sha256": sha256(before),
             "after_yaml_sha256": sha256(after), "before_value": record.get(section), "event": event}
    return after, entry


@pytest.fixture
def record() -> dict:
    return yaml.safe_load((ROOT / SOURCE).read_bytes())


def test_the_real_record_round_trips_through_the_writer_format(record):
    assert dump_record(record) == (ROOT / SOURCE).read_bytes()


def test_an_added_graph_peels_back_to_the_reviewed_bytes(record):
    after, entry = _refresh(record, "causal_graphs", GRAPH, _event())
    assert peel(after, entry) == (ROOT / SOURCE).read_bytes()


def test_a_counts_refresh_peels_back(record):
    stats = dict(record["occurrence_statistics"])
    new = dict(stats, media_count=stats["media_count"] + 3, total_occurrences=stats["total_occurrences"] + 3)
    event = _event("CORRECTED", "refresh_occurrence_statistics",
                   f"occurrence_statistics {stats['media_count']}/{stats['total_occurrences']} -> "
                   f"{new['media_count']}/{new['total_occurrences']} (media_count/total_occurrences)")
    after, entry = _refresh(record, "occurrence_statistics", new, event)
    assert peel(after, entry) == (ROOT / SOURCE).read_bytes()


def test_an_edit_outside_the_section_is_refused(record):
    after, entry = _refresh(record, "causal_graphs", GRAPH, _event())
    tampered = yaml.safe_load(after)
    tampered["preferred_term"] = "D-Glucose (edited)"
    tampered_bytes = dump_record(tampered)
    entry["after_yaml_sha256"] = sha256(tampered_bytes)
    with pytest.raises(ValueError, match="changed more than causal_graphs"):
        peel(tampered_bytes, entry)


@pytest.mark.parametrize("section", ["ontology_mapping", "synonyms", "nutritional_roles", "identifier"])
def test_reviewed_sections_are_not_refreshable(record, section):
    after, entry = _refresh(record, section, record.get(section), _event())
    entry["section"] = section
    with pytest.raises(ValueError, match="not refreshable"):
        peel(after, entry)


def test_the_event_must_be_the_last_one_and_of_the_section_kind(record):
    after, entry = _refresh(record, "causal_graphs", GRAPH, _event())
    entry["event"] = dict(entry["event"], action="CORRECTED")
    with pytest.raises(ValueError, match="last event|not a causal_graphs refresh"):
        peel(after, entry)
    after, entry = _refresh(record, "causal_graphs", GRAPH, _event(action="CORRECTED"))
    with pytest.raises(ValueError, match="not a causal_graphs refresh"):
        peel(after, entry)


def test_a_counts_refresh_must_not_be_llm_assisted_or_touch_other_stats(record):
    stats = dict(record["occurrence_statistics"])
    event = _event("CORRECTED", "refresh_occurrence_statistics",
                   f"occurrence_statistics {stats['media_count']}/{stats['total_occurrences']} -> "
                   f"{stats['media_count']}/{stats['total_occurrences']}", llm_assisted=True)
    after, entry = _refresh(record, "occurrence_statistics", dict(stats, source_occurrences=[]), event)
    with pytest.raises(ValueError):
        peel(after, entry)


def _write_receipts(root: Path, *receipts: dict) -> None:
    directory = root / REFRESH_DIR
    directory.mkdir(parents=True, exist_ok=True)
    for receipt in receipts:
        (directory / f"{receipt['batch']}.json").write_text(json.dumps(receipt))


def _receipt(sequence: int, *entries: dict) -> dict:
    return {"schema_version": 1, "kind": RECEIPT_KIND, "batch": f"batch-{sequence}", "sequence": sequence,
            "approval": "NONE: test", "records": list(entries)}


def test_successive_verified_refreshes_still_require_fresh_approval(tmp_path, record):
    original = (ROOT / SOURCE).read_bytes()
    after1, entry1 = _refresh(record, "causal_graphs", GRAPH, _event())
    second = yaml.safe_load(after1)
    graph2 = copy.deepcopy(GRAPH) + [dict(GRAPH[0], graph_id="d_glucose_catabolism")]
    after2, entry2 = _refresh(second, "causal_graphs", graph2, _event("CAUSAL_GRAPH_UPDATED"))
    target = tmp_path / SOURCE
    target.parent.mkdir(parents=True)
    target.write_bytes(after2)
    _write_receipts(tmp_path, _receipt(1, entry1), _receipt(2, entry2))
    refreshes = RecordRefreshes(tmp_path)
    assert refreshes.equivalents(SOURCE) == {sha256(after2)}
    assert not refreshes.matches(SOURCE, sha256(original))
    assert not refreshes.matches(SOURCE, sha256(after1))
    assert refreshes.matches(SOURCE, sha256(after2))
    assert refreshes.record_at(SOURCE, sha256(original)) is None
    assert refreshes.record_at(SOURCE, sha256(after2)) == yaml.safe_load(after2)
    assert refreshes.receipts_used(SOURCE, sha256(original)) == []

    # Reusing the same inspector cannot retain approval after another edit.
    edited = yaml.safe_load(after2)
    edited["notes"] = "edited without a receipt"
    target.write_bytes(dump_record(edited))
    assert refreshes.equivalents(SOURCE) == {sha256(dump_record(edited))}
    assert not refreshes.matches(SOURCE, sha256(after2))


def test_receipts_must_be_numbered_and_approval_free(tmp_path, record):
    _after, entry = _refresh(record, "causal_graphs", GRAPH, _event())
    _write_receipts(tmp_path, _receipt(2, entry))
    with pytest.raises(ValueError, match="numbered"):
        RecordRefreshes(tmp_path)
    receipt = _receipt(1, entry)
    receipt["approval"] = "APPROVED"
    (tmp_path / REFRESH_DIR / "batch-2.json").unlink()
    _write_receipts(tmp_path, receipt)
    with pytest.raises(ValueError, match="approval"):
        RecordRefreshes(tmp_path)


@pytest.mark.parametrize("disposition", ["SUPPORTED", "WITHHOLD"])
def test_a_mapping_followup_requires_the_exact_current_owner(disposition):
    spec = importlib.util.spec_from_file_location(
        "assemble_review_refresh", ROOT / "reports/sssom_completion_20260921/assemble_review.py")
    assembler = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(assembler)
    row = {"subject_id": "MIM:A", "predicate_id": "skos:exactMatch", "object_id": "CHEBI:1", "other": ""}
    entry = {"mapping": row, "row_sha256": assembler.row_sha256(row), "owner_record": "A.yaml",
             "owner_record_sha256": "reviewed-digest", "disposition": disposition,
             "token_reviews": {}, "resolved_negative_reviews": [],
             "evidence_inputs": {"README.md": assembler.digest(ROOT / "README.md")},
             "identity_review": "x", "reason": "x"}
    with pytest.raises(ValueError, match="stale row or owner"):
        assembler.apply_followup(entry, row, "A.yaml", "current-digest", [], ROOT)
    entry["owner_record_sha256"] = "current-digest"
    assert assembler.apply_followup(entry, row, "A.yaml", "current-digest", [], ROOT)[0] == disposition


# --- review round (#818-#828) ------------------------------------------------


def _counts_refresh(record, *, media_delta=3, total_delta=3, event_extra=None, stats_extra=None, curator="refresh_occurrence_statistics", text=None):
    stats = dict(record["occurrence_statistics"])
    new = dict(stats, media_count=stats["media_count"] + media_delta,
               total_occurrences=stats["total_occurrences"] + total_delta, **(stats_extra or {}))
    changes = text or (f"occurrence_statistics {stats['media_count']}/{stats['total_occurrences']} -> "
                       f"{new['media_count']}/{new['total_occurrences']} (media_count/total_occurrences)")
    event = _event("CORRECTED", curator, changes, **(event_extra or {}))
    return _refresh(record, "occurrence_statistics", new, event)


@pytest.mark.parametrize("case", ["curator", "llm", "other_stats", "event_text"])
def test_each_counts_rule_is_enforced_on_its_own(record, case):
    """One rule broken per case, so deleting any single check fails a test (#820)."""
    if case == "curator":
        after, entry = _counts_refresh(record, curator="someone_else")
    elif case == "llm":
        after, entry = _counts_refresh(record, event_extra={"llm_assisted": True})
    elif case == "other_stats":
        after, entry = _counts_refresh(record, stats_extra={"source_occurrences": []})
    else:
        after, entry = _counts_refresh(record, text="occurrence_statistics refreshed")
    with pytest.raises(ValueError):
        peel(after, entry)


def test_a_valid_counts_refresh_still_passes(record):
    after, entry = _counts_refresh(record)
    assert peel(after, entry) == (ROOT / SOURCE).read_bytes()


def _install(tmp_path, content: bytes, *receipts):
    target = tmp_path / SOURCE
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(content)
    _write_receipts(tmp_path, *receipts)


def test_a_retired_section_loads_but_carries_nothing(tmp_path, record, monkeypatch):
    import mediaingredientmech.record_refresh as rr
    after, entry = _refresh(record, "causal_graphs", GRAPH, _event())
    _install(tmp_path, after, _receipt(1, entry))
    assert not rr.RecordRefreshes(tmp_path).matches(SOURCE, entry["before_yaml_sha256"])
    monkeypatch.setitem(rr.RETIRED_SECTIONS, "causal_graphs", "graph edges are reviewed")
    monkeypatch.delitem(rr.REFRESHABLE_SECTIONS, "causal_graphs")
    refreshes = rr.RecordRefreshes(tmp_path)  # historical receipt still loads (#822)
    assert not refreshes.matches(SOURCE, entry["before_yaml_sha256"])
    assert refreshes.equivalents(SOURCE) == {sha256(after)}


def test_a_missing_record_has_no_equivalents(tmp_path, record):
    _after, entry = _refresh(record, "causal_graphs", GRAPH, _event())
    _write_receipts(tmp_path, _receipt(1, entry))
    refreshes = RecordRefreshes(tmp_path)  # the record file is absent (#823)
    assert refreshes.equivalents(SOURCE) == set()
    assert not refreshes.matches(SOURCE, entry["before_yaml_sha256"])


def test_reverting_a_later_refresh_does_not_restore_an_earlier_approval(tmp_path, record):
    """Historical receipts survive a revert, but only the current exact bytes qualify."""
    after1, entry1 = _refresh(record, "causal_graphs", GRAPH, _event())
    graph2 = copy.deepcopy(GRAPH) + [dict(GRAPH[0], graph_id="d_glucose_catabolism")]
    _after2, entry2 = _refresh(yaml.safe_load(after1), "causal_graphs", graph2, _event("CAUSAL_GRAPH_UPDATED"))
    _install(tmp_path, after1, _receipt(1, entry1), _receipt(2, entry2))  # file reverted to after1
    refreshes = RecordRefreshes(tmp_path)
    assert not refreshes.matches(SOURCE, entry1["before_yaml_sha256"])
    assert refreshes.matches(SOURCE, sha256(after1))
    assert refreshes.receipts_used(SOURCE, entry1["before_yaml_sha256"]) == []
    assert refreshes.receipts_used(SOURCE, sha256(after1)) == []


def _producer():
    spec = importlib.util.spec_from_file_location("make_receipt_under_test", ROOT / "scripts/make_record_refresh_receipt.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_producer_reads_nul_separated_non_ascii_paths():
    raw = "data/ingredients/mapped/Α-lipoic_Acid.yaml\0data/ingredients/mapped/D-glucose.yaml\0".encode()
    assert _producer()._paths(raw) == ["data/ingredients/mapped/Α-lipoic_Acid.yaml", "data/ingredients/mapped/D-glucose.yaml"]


@pytest.mark.parametrize("value", [{1: "x"}, {"retrieved_on": __import__("datetime").date(2026, 10, 1)}])
def test_producer_refuses_values_json_would_change(value):
    with pytest.raises(SystemExit):
        _producer()._json_faithful(value)


def test_producer_keeps_json_faithful_values():
    assert _producer()._json_faithful(GRAPH) == GRAPH


@pytest.mark.parametrize("forged", [False, True])
def test_audit_receipts_cannot_advance_the_reviewed_baseline(tmp_path, record, forged):
    after, entry = _refresh(record, "causal_graphs", GRAPH, _event())
    if forged:
        entry["before_yaml_sha256"] = "0" * 64
    _install(tmp_path, after, _receipt(1, entry))
    refreshes = RecordRefreshes(tmp_path)
    known = entry["before_yaml_sha256"]
    assert refreshes.advance(SOURCE, known, sha256(after)) == known
    assert not refreshes.matches(SOURCE, known)


@pytest.mark.parametrize("change", ["whitespace", "comment", "counts", "graphs", "history"])
def test_every_record_byte_change_requires_fresh_approval(tmp_path, record, change):
    before = dump_record(record)
    _install(tmp_path, before)
    refreshes = RecordRefreshes(tmp_path)
    assert refreshes.matches(SOURCE, sha256(before))
    if change == "whitespace":
        after = before + b"\n"
    elif change == "comment":
        after = b"# Audit comment\n" + before
    elif change == "counts":
        after, _ = _counts_refresh(record)
    elif change == "graphs":
        after, _ = _refresh(record, "causal_graphs", GRAPH, _event())
    else:
        record["curation_history"].append(_event())
        after = dump_record(record)
    (tmp_path / SOURCE).write_bytes(after)
    assert not refreshes.matches(SOURCE, sha256(before))
    assert refreshes.matches(SOURCE, sha256(after))
    assert refreshes.record_at(SOURCE, sha256(before)) is None
