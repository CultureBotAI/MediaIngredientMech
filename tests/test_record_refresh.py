"""Section refreshes carry content-bound reviews across unreviewed sections only.

Built on a real record's bytes so the peel is exercised against the exact
serialization the per-record writers produce.
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


def test_equivalence_chains_through_successive_refreshes_and_stops_at_other_edits(tmp_path, record):
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
    assert refreshes.equivalents(SOURCE) == {sha256(after2), sha256(after1), sha256(original)}
    assert refreshes.matches(SOURCE, sha256(original))
    assert refreshes.record_at(SOURCE, sha256(original)) == record

    # An unrecorded edit on top breaks every equivalence but the current bytes.
    edited = yaml.safe_load(after2)
    edited["notes"] = "edited without a receipt"
    target.write_bytes(dump_record(edited))
    assert RecordRefreshes(tmp_path).equivalents(SOURCE) == {sha256(dump_record(edited))}


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


def test_a_mapping_followup_binds_to_any_verified_equivalent():
    spec = importlib.util.spec_from_file_location(
        "assemble_review_refresh", ROOT / "reports/sssom_completion_20260921/assemble_review.py")
    assembler = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(assembler)
    row = {"subject_id": "MIM:A", "predicate_id": "skos:exactMatch", "object_id": "CHEBI:1", "other": ""}
    entry = {"mapping": row, "row_sha256": assembler.row_sha256(row), "owner_record": "A.yaml",
             "owner_record_sha256": "reviewed-digest", "disposition": "WITHHOLD",
             "evidence_inputs": {"README.md": assembler.digest(ROOT / "README.md")},
             "identity_review": "x", "reason": "x"}
    with pytest.raises(ValueError, match="stale row or owner"):
        assembler.apply_followup(entry, row, "A.yaml", "current-digest", [], ROOT)
    assert assembler.apply_followup(entry, row, "A.yaml", "current-digest", [], ROOT,
                                    reviewed_hashes={"current-digest", "reviewed-digest"})[0] == "WITHHOLD"
