"""#1390: original findings need complete dispositions on actual current owner bytes.

All owners, findings and evidence below are synthetic test inputs. These tests
exercise native adjudication; they grant no scientific approval to real records.
"""

from __future__ import annotations

import copy
import csv
import hashlib
import io
import json
from types import SimpleNamespace

import pytest
import yaml

from mediaingredientmech.validation.current_semantic_release import Inputs, current_findings

OWNER = "data/ingredients/mapped/Synthetic.yaml"
MOVED = "data/ingredients/mapped/RenamedSynthetic.yaml"
BASELINE = "historical/findings.tsv"
MANIFEST = "historical/manifest.json"
OLD_DECISIONS = "historical/dispositions.tsv"
CURRENT = "current/dispositions.tsv"
EVIDENCE = "current/evidence.json"
LINEAGE = "current/lineage.json"


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def encoded(value):
    return (json.dumps(value, sort_keys=True, indent=2) + "\n").encode()


def table(entries, columns):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(
        stream, fieldnames=columns, delimiter="\t", quoting=csv.QUOTE_NONE, lineterminator="\n"
    )
    writer.writeheader()
    writer.writerows(entries)
    return stream.getvalue().encode()


@pytest.fixture
def finding_case(tmp_path):
    historical_record = {
        "mim_id": "MIM:0000001",
        "identifier": "kgmicrobe.ingredient:synthetic_test_material",
        "mapping_status": "MAPPED",
        "preferred_name": "Synthetic historical label",
    }
    current_record = {**historical_record, "preferred_name": "Synthetic current label"}
    old_bytes = yaml.safe_dump(historical_record).encode()
    current_bytes = yaml.safe_dump(current_record).encode()
    path = tmp_path / OWNER
    path.parent.mkdir(parents=True)
    path.write_bytes(current_bytes)
    (tmp_path / "current").mkdir()
    (tmp_path / EVIDENCE).write_bytes(
        encoded({"scope": "Synthetic current review and move evidence; test fixture only"})
    )
    findings = [
        {
            "finding_id": "SEM:synthetic-source",
            "source_record": OWNER,
            "record_scope": "active",
            "kind": "component_source_scope",
            "severity": "major",
            "reason": "Synthetic original source-scope obligation.",
        },
        {
            "finding_id": "SEM:synthetic-role",
            "source_record": OWNER,
            "record_scope": "active",
            "kind": "role_evidence",
            "severity": "major",
            "reason": "Synthetic original role-evidence obligation.",
        },
    ]
    decisions = [
        {
            **finding,
            "current_record": OWNER,
            "current_record_sha256": digest(current_bytes),
            "resolution_status": "OPEN",
            "resolution_reason": "",
            "resolution_evidence": "",
        }
        for finding in findings
    ]
    # The old report resolved these on different owner bytes. A portable current
    # review must still use the full original baseline and new dispositions.
    previous = [
        {
            **decision,
            "current_record_sha256": digest(old_bytes),
            "resolution_status": "RESOLVED",
            "resolution_reason": "Synthetic historical decision, not current support.",
            "resolution_evidence": "historical/evidence.json",
        }
        for decision in decisions
    ]
    baseline = table(findings, list(findings[0]))
    history = {
        "original": {
            "baseline_findings": BASELINE,
            "baseline_manifest": MANIFEST,
            "finding_dispositions": OLD_DECISIONS,
        },
        "before": {
            BASELINE: baseline,
            MANIFEST: encoded(
                {
                    "members": {"findings.tsv": {"sha256": digest(baseline)}},
                    "inputs": {OWNER: digest(old_bytes)},
                }
            ),
            OLD_DECISIONS: table(previous, list(previous[0])),
            OWNER: old_bytes,
        },
    }
    return SimpleNamespace(
        root=tmp_path,
        history=history,
        records={OWNER: current_record},
        hashes={OWNER: digest(current_bytes)},
        decisions=decisions,
        columns=list(decisions[0]),
        request={"finding_dispositions": CURRENT, "record_lineage": None, "review_inputs": {}},
    )


def adjudicate(case):
    (case.root / CURRENT).write_bytes(table(case.decisions, case.columns))
    inputs = Inputs(case.root)
    for name, expected in case.hashes.items():
        inputs.read(name, expected)
    result = current_findings(inputs, case.history, case.records, case.hashes, case.request)
    inputs.recheck()
    return result, inputs


def pin_evidence(case):
    case.request["review_inputs"][EVIDENCE] = digest((case.root / EVIDENCE).read_bytes())


def test_current_open_dispositions_do_not_inherit_historical_resolution(finding_case):
    case = finding_case
    before = copy.deepcopy(case.history)
    (decisions, blocking), inputs = adjudicate(case)
    assert decisions == case.decisions
    assert blocking == ["SEM:synthetic-role", "SEM:synthetic-source"]
    assert all(row["current_record_sha256"] == case.hashes[OWNER] for row in decisions)
    assert case.hashes[OWNER] != digest(case.history["before"][OWNER])
    assert inputs.hashes()[CURRENT] == digest((case.root / CURRENT).read_bytes())
    assert case.history == before


def test_stale_historical_owner_hash_cannot_certify_current_disposition(finding_case):
    case = finding_case
    case.decisions[0]["current_record_sha256"] = digest(case.history["before"][OWNER])
    with pytest.raises(ValueError, match="Stale finding disposition"):
        adjudicate(case)


@pytest.mark.parametrize("attack", ["omit_one", "omit_all", "duplicate"])
def test_complete_original_finding_inventory_is_required(finding_case, attack):
    case = finding_case
    if attack == "omit_one":
        case.decisions.pop()
    elif attack == "omit_all":
        case.decisions.clear()
    else:
        case.decisions.append(copy.deepcopy(case.decisions[0]))
    with pytest.raises(
        ValueError, match="Incomplete finding coverage|Duplicate finding disposition"
    ):
        adjudicate(case)


@pytest.mark.parametrize("field,value", [("severity", "minor"), ("reason", "Changed old finding")])
def test_current_disposition_cannot_rewrite_historical_finding(finding_case, field, value):
    finding_case.decisions[0][field] = value
    with pytest.raises(ValueError, match="Historical finding changed"):
        adjudicate(finding_case)


@pytest.mark.parametrize("attack", ["changed_baseline", "omitted_member", "wrong_member_pin"])
def test_historical_baseline_requires_its_original_manifest_pin(finding_case, attack):
    case = finding_case
    if attack == "changed_baseline":
        case.history["before"][BASELINE] = case.history["before"][BASELINE].replace(
            b"Synthetic original source-scope obligation.", b"Altered historical assertion."
        )
    else:
        manifest = json.loads(case.history["before"][MANIFEST])
        if attack == "omitted_member":
            manifest["members"].clear()
        else:
            manifest["members"]["findings.tsv"]["sha256"] = "0" * 64
        case.history["before"][MANIFEST] = encoded(manifest)
    with pytest.raises(ValueError, match="historical baseline finding manifest differs"):
        adjudicate(case)


def resolve_first(case):
    case.decisions[0].update(
        resolution_status="RESOLVED",
        resolution_reason="Explicit synthetic current assessment of this exact owner.",
        resolution_evidence=EVIDENCE,
    )


def test_present_but_unpinned_evidence_cannot_resolve_changed_owner(finding_case):
    case = finding_case
    resolve_first(case)
    assert (case.root / EVIDENCE).is_file()
    with pytest.raises(ValueError, match="Resolution lacks hashed evidence"):
        adjudicate(case)


def test_current_resolution_with_exact_pinned_evidence_is_not_blanket_clearance(finding_case):
    case = finding_case
    resolve_first(case)
    pin_evidence(case)
    (decisions, blocking), inputs = adjudicate(case)
    assert decisions[0]["resolution_status"] == "RESOLVED"
    assert decisions[1]["resolution_status"] == "OPEN"
    assert blocking == ["SEM:synthetic-role"]
    assert inputs.hashes()[EVIDENCE] == case.request["review_inputs"][EVIDENCE]


def test_replaced_evidence_cannot_satisfy_the_declared_review_pin(finding_case):
    case = finding_case
    resolve_first(case)
    pin_evidence(case)
    (case.root / EVIDENCE).write_bytes(b"different evidence\n")
    with pytest.raises(ValueError, match="stale input: current/evidence.json"):
        adjudicate(case)


def move_owner(case):
    (case.root / OWNER).rename(case.root / MOVED)
    case.records[MOVED] = case.records.pop(OWNER)
    case.hashes[MOVED] = case.hashes.pop(OWNER)
    for decision in case.decisions:
        decision["current_record"] = MOVED
    case.request["record_lineage"] = LINEAGE
    pin_evidence(case)
    return {
        "source_record": OWNER,
        "source_sha256": digest(case.history["before"][OWNER]),
        "current_record": MOVED,
        "current_sha256": case.hashes[MOVED],
        "kind": "MOVE",
        "evidence": EVIDENCE,
    }


def test_current_renamed_owner_preserves_both_historical_obligations(finding_case):
    case = finding_case
    lineage = move_owner(case)
    (case.root / LINEAGE).write_bytes(encoded({"moves": [lineage]}))
    (decisions, blocking), inputs = adjudicate(case)
    assert {row["current_record"] for row in decisions} == {MOVED}
    assert case.records[MOVED]["mim_id"] == "MIM:0000001"
    assert blocking == ["SEM:synthetic-role", "SEM:synthetic-source"]
    assert inputs.hashes()[LINEAGE] == digest((case.root / LINEAGE).read_bytes())


@pytest.mark.parametrize(
    "attack,expected",
    [
        ("source_hash", "Lineage source is not bound to the historical baseline"),
        ("current_hash", "Stale lineage target"),
        ("missing_evidence", "Lineage lacks hashed evidence"),
        ("omitted_move", "Finding record continuity is unproven"),
    ],
)
def test_stable_id_does_not_replace_verified_record_move_lineage(finding_case, attack, expected):
    case = finding_case
    lineage = move_owner(case)
    moves = [lineage]
    if attack == "source_hash":
        lineage["source_sha256"] = "0" * 64
    elif attack == "current_hash":
        lineage["current_sha256"] = digest(case.history["before"][OWNER])
    elif attack == "missing_evidence":
        case.request["review_inputs"].clear()
    else:
        moves.clear()
    (case.root / LINEAGE).write_bytes(encoded({"moves": moves}))
    with pytest.raises(ValueError, match=expected):
        adjudicate(case)
