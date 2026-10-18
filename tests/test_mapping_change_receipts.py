"""Mapping-change receipts supersede pins; they never grant approval (#740, #745, #748).

The resolution review pins records by hash (role, component plans), by parsed
content (identity plans) and by SSSOM row position (the frozen release hold).
A verified later correction, recorded as a chained receipt, must let the build
proceed with the pin *superseded* -- and every approval that rested on the pin
must lapse. An undocumented change, a chain with a gap, a receipt that claims
approval or a lineage whose recomputed ids differ from the frozen ones must
still fail exactly as before.
"""

from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from mediaingredientmech.validation import mapping_change_receipts as mcr

OWNER = "data/ingredients/mapped/Thing.yaml"


def _receipt(sequence, before, after, before_rows, after_rows, position_map, records=()):
    return {
        "schema_version": 1,
        "batch": f"batch{sequence}",
        "sequence": sequence,
        "approval": "NONE: withheld",
        "before_sha256": before,
        "after_sha256": after,
        "before_row_count": before_rows,
        "after_row_count": after_rows,
        "position_map": position_map,
        "records": list(records),
        "changes": [],
    }


def _write(tmp_path: Path, receipts):
    folder = tmp_path / "receipts"
    folder.mkdir()
    for receipt in receipts:
        (folder / f"{receipt['batch']}.json").write_text(json.dumps(receipt))
    return folder


def test_receipts_load_in_sequence_and_chain(tmp_path):
    first = _receipt(1, "s0", "s1", 3, 2, [None, 1, 2])
    second = _receipt(2, "s1", "s2", 2, 2, [1, 2])
    _write(tmp_path, [second, first])
    loaded = mcr.load_receipts(tmp_path, "receipts")
    assert [r["sequence"] for r in loaded] == [1, 2]
    assert mcr.receipt_paths(tmp_path, "receipts") == ["receipts/batch1.json", "receipts/batch2.json"]
    assert mcr.load_receipts(tmp_path, "missing") == []


@pytest.mark.parametrize(
    "mutation, message",
    [
        ("gap", "numbered 1..n"),
        ("digest", "does not chain from"),
        ("rows", "does not chain row counts"),
        ("approval", "approval-free"),
        ("map", "position map is incomplete"),
    ],
)
def test_broken_chains_are_refused(tmp_path, mutation, message):
    first = _receipt(1, "s0", "s1", 3, 2, [None, 1, 2])
    second = _receipt(2, "s1", "s2", 2, 2, [1, 2])
    if mutation == "gap":
        second["sequence"] = 3
    elif mutation == "digest":
        second["before_sha256"] = "elsewhere"
    elif mutation == "rows":
        second["before_row_count"] = 3
        second["position_map"] = [1, 2, None]
    elif mutation == "approval":
        second["approval"] = "APPROVED by nobody"
    elif mutation == "map":
        second["position_map"] = [1]
    _write(tmp_path, [first, second])
    with pytest.raises(ValueError, match=message):
        mcr.load_receipts(tmp_path, "receipts")


def _chains():
    receipts = [
        _receipt(1, "s0", "s1", 1, 1, [1], [{"source_record": OWNER, "before_yaml_sha256": "h0",
                                            "after_yaml_sha256": "h1", "before_record_sha256": "c0"}]),
        _receipt(2, "s1", "s2", 1, 1, [1], [{"source_record": OWNER, "before_yaml_sha256": "h1",
                                            "after_yaml_sha256": "h2"}]),
    ]
    return mcr.record_chains(receipts)


def test_hash_pins_are_superseded_only_by_a_gapless_chain():
    chains = _chains()
    assert mcr.supersedes(chains, OWNER, "h0", "h2")
    assert mcr.supersedes(chains, OWNER, "h1", "h2")
    assert not mcr.supersedes(chains, OWNER, "h2", "h2"), "same bytes is never a supersession"
    assert not mcr.supersedes(chains, OWNER, "h0", "h1"), "chain runs past the current bytes"
    assert not mcr.supersedes(chains, OWNER, "hx", "h2"), "pin is not where the chain starts"
    assert not mcr.supersedes(chains, OWNER, "h0", "h3"), "undocumented change after the chain"
    assert not mcr.supersedes(chains, "other.yaml", "h0", "h2")
    broken = _chains()
    broken[OWNER][1]["before"] = "not-h1"
    assert not mcr.supersedes(broken, OWNER, "h0", "h2"), "a gap between links keeps the pin"


def test_content_pins_need_the_recorded_canonical_digest():
    record = {"identifier": "CHEBI:1", "synonyms": [{"synonym_text": "x"}]}
    chains = _chains()
    chains[OWNER][0]["before_record"] = mcr.record_digest(record)
    assert mcr.supersedes_content(chains, OWNER, record, "h2")
    assert mcr.supersedes_content(chains, OWNER, dict(reversed(list(record.items()))), "h2")
    assert not mcr.supersedes_content(chains, OWNER, dict(record, identifier="CHEBI:2"), "h2")
    assert not mcr.supersedes_content(chains, OWNER, record, "h1")
    chains[OWNER][0]["before_record"] = None
    assert not mcr.supersedes_content(chains, OWNER, record, "h2"), "no recorded content digest, pin stands"


def test_position_maps_compose_and_invert():
    receipts = [
        _receipt(1, "s0", "s1", 4, 3, [1, None, 2, 3]),
        _receipt(2, "s1", "s2", 3, 3, [2, 1, 3]),
    ]
    forward = mcr.forward_map(receipts)
    assert forward == [2, None, 1, 3]
    assert mcr.baseline_position(forward, 1) == 3
    assert mcr.baseline_position(forward, 3) == 4
    assert mcr.baseline_position(forward, 4) is None
    assert mcr.forward_map([]) == []


def _lineage_fixture():
    sha = "payload-sha"
    edge = {"source_record": OWNER, "assertion_type": "mapping", "source_position": "2",
            "subject": "MIM:Thing", "object": "CHEBI:1", "assertion_json": "{}"}
    edge["id"] = mcr._edge_id_at(edge, 2)
    assertion = {"source_record": OWNER, "assertion_type": "mapping", "source_position": "2",
                 "assertion_sha256": sha, "assertion_id": mcr._assertion_id(2, sha)}
    resolution = {"assertion_id": mcr._assertion_id(3, sha), "assertion_sha256": sha,
                  "edge_id": mcr._edge_id_at(edge, 3)}
    receipts = [_receipt(1, "s0", "s1", 3, 2, [None, 1, 2])]
    return receipts, [assertion], [edge], resolution


def test_hold_lineage_recomputes_the_frozen_ids_at_the_baseline_position():
    receipts, assertions, edges, resolution = _lineage_fixture()
    lineage = mcr.hold_lineage(receipts, assertions, edges, [resolution])
    assert lineage == {
        resolution["assertion_id"]: {
            "assertion_id": assertions[0]["assertion_id"],
            "edge_id": edges[0]["id"],
            "baseline_position": 3,
            "current_position": 2,
        }
    }
    assert mcr.hold_lineage([], assertions, edges, [resolution]) == {}


def test_hold_lineage_supports_resolution_repinned_at_later_receipt_boundary():
    """A resolution repinned after an intermediate receipt traces through the remaining suffix."""
    receipts, assertions, edges, resolution = _lineage_fixture()
    # Suppose the resolution was repinned at position 3 (after receipt 1, before receipt 2):
    repinned = dict(
        resolution,
        assertion_id=mcr._assertion_id(3, "payload-sha"),
        edge_id=mcr._edge_id_at(edges[0], 3),
    )
    earlier = {
        "schema_version": 1,
        "sequence": 0,
        "batch": "b0",
        "approval": "NONE: structural",
        "before_sha256": "s-1",
        "after_sha256": "s0",
        "before_row_count": 4,
        "after_row_count": 3,
        "position_map": [None, 1, 2, 3],
    }
    lineage = mcr.hold_lineage([earlier, *receipts], assertions, edges, [repinned])
    assert lineage == {
        repinned["assertion_id"]: {
            "assertion_id": assertions[0]["assertion_id"],
            "edge_id": edges[0]["id"],
            "baseline_position": 3,
            "current_position": 2,
        }
    }



@pytest.mark.parametrize("mutation", ["payload", "position", "edge", "still_present"])
def test_hold_lineage_refuses_anything_but_an_exact_reproduction(mutation):
    receipts, assertions, edges, resolution = _lineage_fixture()
    if mutation == "payload":
        resolution["assertion_sha256"] = "other-payload"
    elif mutation == "position":
        receipts[0]["position_map"] = [None, None, 2]
        receipts[0]["after_row_count"] = 2
        assertions[0]["source_position"] = "2"
        resolution["assertion_id"] = mcr._assertion_id(1, "payload-sha")
    elif mutation == "edge":
        resolution["edge_id"] = "MIM.assertion:tampered"
    elif mutation == "still_present":
        assertions[0]["assertion_id"] = resolution["assertion_id"]
    lineage = mcr.hold_lineage(receipts, assertions, edges, [resolution])
    assert lineage == {}


def test_receipt_writer_shares_the_canonical_content_digest():
    import importlib.util

    root = Path(__file__).parents[1]
    spec = importlib.util.spec_from_file_location(
        "make_receipt_content", root / "reports/sssom_completion_20260921/mapping_changes/make_receipt.py"
    )
    make_receipt = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(make_receipt)
    assert make_receipt.record_digest is mcr.record_digest
    before = copy.deepcopy({"identifier": "CHEBI:1", "label": "thing"})
    assert mcr.record_digest(before) == mcr.record_digest(json.loads(json.dumps(before)))


def test_recomputed_ids_match_the_gate_and_the_exporter():
    """The lineage is only sound if it reproduces the real id formulas byte for byte."""
    from mediaingredientmech.export.kgx import Graph
    from mediaingredientmech.validation import semantic_release as gate

    record = {"identifier": "CHEBI:1", "preferred_term": "thing", "mapping_status": "MAPPED"}
    mappings = [
        {"subject_id": "MIM:Other", "predicate_id": "skos:exactMatch", "object_id": "CHEBI:9"},
        {"subject_id": "MIM:Thing", "predicate_id": "skos:exactMatch", "object_id": "CHEBI:1"},
    ]
    hashes = {OWNER: "bytes"}
    assertions = [row for row in gate.current_assertions({OWNER: record}, mappings, hashes, "sssom-sha")
                  if row["assertion_type"] == "mapping"]
    thing = next(row for row in assertions if row["source_position"] == "2")
    assert mcr._assertion_id(2, thing["assertion_sha256"]) == thing["assertion_id"]
    graph = Graph()
    graph.node("MIM:Thing", "thing", "biolink:ChemicalEntity", "ingredient")
    graph.reference("CHEBI:1", "one")
    # Exactly the exporter's mapping call: no optional fields.
    graph.edge("MIM:Thing", "biolink:exact_match", "CHEBI:1", "skos:exactMatch", "mapping",
               "mappings/ingredient_mappings.sssom.tsv", 2, mappings[1])
    edge = graph.edges[0]
    assert mcr._edge_id_at(edge, 2) == edge["id"]
    assert mcr._edge_id_at(edge, 1) != edge["id"]
    # The KGX TSV carries every optional column as "" (#765); the recomputation
    # must reproduce the id from that shape too.
    from mediaingredientmech.export.kgx import EDGE_COLUMNS

    tsv_shaped = {column: edge.get(column, "") for column in EDGE_COLUMNS}
    assert set(tsv_shaped) > set(edge)
    assert mcr._edge_id_at(tsv_shaped, 2) == edge["id"]


def test_issue_903_replayed_from_commits_are_anchored_and_match_sha256():
    """Every receipt's replayed_from commit must be reachable from HEAD or a review-source/* tag (#903)."""
    import csv
    import hashlib
    import subprocess

    root = Path(__file__).parents[1]
    receipts = mcr.load_receipts(root)
    replayed = [r for r in receipts if "replayed_from" in r]
    assert replayed, "expected receipts with replayed_from provenance"

    for receipt in replayed:
        info = receipt["replayed_from"]
        commit = info["commit"]
        rel_path = info["path"]
        expected_sha = info["sha256"]

        in_head = (
            subprocess.run(
                ["git", "-C", str(root), "merge-base", "--is-ancestor", commit, "HEAD"],
                capture_output=True,
                check=False,
            ).returncode
            == 0
        )
        tags_out = subprocess.run(
            ["git", "-C", str(root), "tag", "--list", "review-source/*", "--contains", commit],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
        assert in_head or bool(tags_out), (
            f"Receipt {receipt['batch']} cites unanchored commit {commit}; "
            "tag it under refs/tags/review-source/*"
        )

        blob = subprocess.run(
            ["git", "-C", str(root), "cat-file", "-p", f"{commit}:{rel_path}"],
            capture_output=True,
            check=True,
        ).stdout
        actual_sha = hashlib.sha256(blob).hexdigest()
        assert actual_sha == expected_sha, (
            f"Receipt {receipt['batch']} replayed_from sha256 mismatch for {commit}:{rel_path}"
        )


def test_issue_902_receipt_corrected_rows_qualify_pre_receipt_reasons():
    """Receipt-corrected rows must lead with the receipt and qualify carried pre-receipt reasons (#902)."""
    import csv

    root = Path(__file__).parents[1]
    receipts = mcr.load_receipts(root)
    chains = mcr.record_chains(receipts)
    assert all("batch" in link and link["batch"] for links in chains.values() for link in links)

    review = json.loads((root / "reports/sssom_completion_20260921/review.json").read_text(encoding="utf-8"))
    evidence = json.loads(
        (root / "reports/sssom_completion_20260921/mapping-evidence.json").read_text(encoding="utf-8")
    )["entries"]

    receipt_decisions = []
    for decision in review["decisions"]:
        entry = evidence[decision["evidence_key"]]
        basis = entry["basis"]
        if "mapping_followup" in basis:
            continue
        if basis.get("mapping_change") or decision.get("owner_record") in chains:
            receipt_decisions.append((decision, basis))

    assert receipt_decisions, "expected receipt-corrected rows in review.json"

    for decision, basis in receipt_decisions:
        batch = basis.get("mapping_change")
        assert batch, f"Row {decision['source_position']} ({decision['owner_record']}) is missing mapping_change"
        reason = decision["review_reason"]
        if basis.get("baseline_position") is None:
            assert reason.startswith(f"Row added by mapping-change receipt {batch} "), (
                f"Added row {decision['source_position']} review_reason does not lead with receipt: {reason!r}"
            )
            continue
        prefix = f"Mapping corrected by receipt {batch}:"
        assert reason.startswith(prefix), (
            f"Row {decision['source_position']} ({decision['owner_record']}) review_reason does not lead with {prefix!r}: {reason!r}"
        )
        tail = reason[len(prefix) :].strip()
        if any(k in basis for k in ("scoped_review", "negative_reviews")):
            assert "Pre-receipt " in tail and "(recorded against the pre-receipt payload):" in tail, (
                f"Row {decision['source_position']} carried reason is not qualified as pre-receipt: {reason!r}"
            )

    findings_path = root / "reports/semantic_review_20260921/resolution/finding-dispositions.tsv"
    with findings_path.open(encoding="utf-8", newline="") as handle:
        finding_rows = list(csv.DictReader(handle, delimiter="\t"))

    superseded_findings = [
        row
        for row in finding_rows
        if row["source_record"] in chains and row["resolution_status"] in {"OPEN", "EXCLUDED_REJECTED"}
    ]
    assert superseded_findings, "expected receipt-superseded findings in finding-dispositions.tsv"
    for row in superseded_findings:
        reason = row["resolution_reason"]
        assert reason.startswith("Mapping corrected by receipt "), (
            f"Finding {row['finding_id']} ({row['source_record']}) resolution_reason does not lead with receipt: {reason!r}"
        )
        if row["resolution_status"] == "OPEN":
            assert "Pre-receipt " in reason, (
                f"Finding {row['finding_id']} ({row['source_record']}) resolution_reason does not qualify pre-receipt text: {reason!r}"
            )

