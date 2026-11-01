"""The execution comparison must include the selected companion (#1064)."""

import importlib.util
import json
import subprocess
import sys
from copy import deepcopy
from pathlib import Path

import pytest

SOURCE = (
    Path(__file__).resolve().parents[1]
    / "reports/strict_approval_receipts_764_20261101/compare_dispositions.py"
)
SPEC = importlib.util.spec_from_file_location("strict_receipt_execution_comparison", SOURCE)
comparison = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(comparison)
PRIOR = "reports/companion/prior.json"
CURRENT = "reports/companion/current.json"
OWNER = "data/ingredients/mapped/Example.yaml"
CLAIMS = "reports/companion/claims.json"
EVIDENCE = "reports/companion/evidence.json"


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n")


@pytest.fixture
def sample(tmp_path):
    root, baseline = tmp_path / "current", tmp_path / "baseline"
    owner = root / OWNER
    owner.parent.mkdir(parents=True)
    owner.write_text("identifier: local:example\n")
    write_json(root / CLAIMS, {"claims": [{"claim_id": "a"}, {"claim_id": "b"}]})
    write_json(root / EVIDENCE, {"source": "fixture evidence"})
    write_json(
        root / comparison.MAPPING,
        {
            "inputs": {},
            "decisions": [{"source_position": 1, "disposition": "WITHHOLD", "reason": "held"}],
        },
    )
    semantic = root / comparison.SEMANTIC
    write_json(
        semantic / "current-review.json",
        {
            "release_verdict": "FAIL",
            "blocking_finding_ids": ["f"],
            "blocking_assertion_ids": ["a"],
            "evidence_gaps": {},
            "record_inputs": {OWNER: comparison.digest(owner)},
        },
    )
    (semantic / "assertion-dispositions.tsv").write_text(
        "assertion_id\tresolution_status\tpayload\na\tOPEN\tretained\n"
    )
    (semantic / "finding-dispositions.tsv").write_text("finding_id\tresolution_status\n f\tOPEN\n")
    companion = {
        "schema_version": 1,
        "base_review": comparison.MAPPING,
        "base_review_sha256": comparison.digest(root / comparison.MAPPING),
        "claims_file": CLAIMS,
        "claims_sha256": comparison.digest(root / CLAIMS),
        "record_inputs": {OWNER: comparison.digest(owner)},
        "inputs": {EVIDENCE: comparison.digest(root / EVIDENCE)},
        "decisions": [
            {
                "claim_id": "a",
                "disposition": "SUPPORTED",
                "owner_record": OWNER,
                "row_sha256": "1" * 64,
                "review_reason": "supported",
            },
            {
                "claim_id": "b",
                "disposition": "WITHHOLD",
                "owner_record": OWNER,
                "row_sha256": "2" * 64,
                "review_reason": "held",
            },
        ],
    }
    write_json(root / PRIOR, companion)
    write_json(root / CURRENT, companion)
    names = [
        comparison.MAPPING,
        comparison.SEMANTIC + "/current-review.json",
        comparison.SEMANTIC + "/assertion-dispositions.tsv",
        comparison.SEMANTIC + "/finding-dispositions.tsv",
        PRIOR,
    ]
    for name in names:
        target = baseline / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes((root / name).read_bytes())
    write_json(
        baseline / "receipt.json",
        {
            "base": "fixture-base",
            "comparison_outputs": {name: comparison.digest(root / name) for name in names},
            "preserve_bytes": {OWNER: comparison.digest(owner)},
        },
    )
    return root, baseline, comparison.digest(baseline / "receipt.json")


def assess(sample):
    return comparison.assess(*sample, PRIOR, CURRENT)


def edit_companion(sample, change):
    path = sample[0] / CURRENT
    value = comparison.read(path)
    change(value)
    write_json(path, value)


def test_unchanged_and_dependency_only_successor(sample):
    assert assess(sample)["status"] == "EXACT_DISPOSITION_AND_SOURCE_PRESERVATION"
    root = sample[0]
    mapping = comparison.read(root / comparison.MAPPING)
    mapping["inputs"]["new-utility.py"] = "a" * 64
    write_json(root / comparison.MAPPING, mapping)
    edit_companion(
        sample,
        lambda value: value.update(base_review_sha256=comparison.digest(root / comparison.MAPPING)),
    )
    result = assess(sample)
    assert result["status"] == "EXACT_DISPOSITION_AND_SOURCE_PRESERVATION"
    assert result["comparisons"]["companion"]["after_count"] == 2
    assert result["current_companion"]["path"] == CURRENT
    assert result["scientific_approval_added"] is False


def test_withheld_companion_promotion_is_detected(sample):
    edit_companion(
        sample,
        lambda value: value["decisions"][1].update(
            disposition="SUPPORTED", review_reason="new approval"
        ),
    )
    result = assess(sample)
    assert result["status"] == "REQUIRES_REVIEW"
    assert result["scientific_approval_added"] is True
    assert set(result["comparisons"]["companion"]["changed"]) == {"b"}


@pytest.mark.parametrize(
    "field,value",
    [("review_reason", "changed"), ("row_sha256", "3" * 64), ("owner_record", "different.yaml")],
)
def test_full_positive_decision_is_compared(sample, field, value):
    edit_companion(sample, lambda review: review["decisions"][0].update({field: value}))
    result = assess(sample)
    assert result["status"] == "REQUIRES_REVIEW"
    assert result["scientific_approval_added"] is True


@pytest.mark.parametrize("action", ["remove", "add", "duplicate"])
def test_companion_membership(sample, action):
    def mutate(value):
        if action == "remove":
            value["decisions"].pop()
        else:
            row = deepcopy(value["decisions"][0])
            if action == "add":
                row["claim_id"] = "extra"
            value["decisions"].append(row)

    edit_companion(sample, mutate)
    if action == "duplicate":
        with pytest.raises(ValueError, match="Duplicate disposition"):
            assess(sample)
    else:
        assert assess(sample)["status"] == "REQUIRES_REVIEW"


@pytest.mark.parametrize(
    "name,field", [(OWNER, "record_inputs"), (EVIDENCE, "inputs"), (CLAIMS, "claims_sha256")]
)
def test_changed_companion_source_or_contract(sample, name, field):
    path = sample[0] / name
    path.write_bytes(path.read_bytes() + b"\n")
    with pytest.raises(ValueError, match="input hash mismatch"):
        assess(sample)

    def update_hash(value):
        if field == "claims_sha256":
            value[field] = comparison.digest(path)
        else:
            value[field][name] = comparison.digest(path)

    edit_companion(sample, update_hash)
    result = assess(sample)
    assert result["status"] == "REQUIRES_REVIEW"
    assert field in result["companion_contract_changes"]


def test_old_review_cannot_stand_in_for_current_dependency(sample):
    root = sample[0]
    value = comparison.read(root / comparison.MAPPING)
    value["inputs"] = {"utility": "b" * 64}
    write_json(root / comparison.MAPPING, value)
    with pytest.raises(ValueError, match="current mapping review"):
        comparison.assess(*sample, PRIOR, PRIOR)


def test_baseline_hash_and_archived_outputs_are_bound(sample):
    root, baseline, expected = sample
    with pytest.raises(ValueError, match="Baseline receipt hash"):
        comparison.assess(root, baseline, "0" * 64, PRIOR, CURRENT)
    (baseline / PRIOR).write_text("{}\n")
    with pytest.raises(ValueError, match="Archived comparison output changed"):
        assess(sample)


def test_baseline_cannot_omit_a_comparison_hash(sample):
    root, baseline, _ = sample
    receipt = comparison.read(baseline / "receipt.json")
    del receipt["comparison_outputs"][comparison.MAPPING]
    write_json(baseline / "receipt.json", receipt)
    with pytest.raises(ValueError, match="exactly the five"):
        comparison.assess(
            root, baseline, comparison.digest(baseline / "receipt.json"), PRIOR, CURRENT
        )


def test_new_null_contract_key_is_not_silently_ignored(sample):
    edit_companion(sample, lambda value: value.update(new_contract=None))
    assert assess(sample)["status"] == "REQUIRES_REVIEW"


def test_input_change_during_comparison_refuses(sample, monkeypatch):
    verify = comparison.Snapshot.verify

    def changed(snapshot):
        owner = sample[0] / OWNER
        owner.write_bytes(owner.read_bytes() + b"# concurrent change\n")
        verify(snapshot)

    monkeypatch.setattr(comparison.Snapshot, "verify", changed)
    with pytest.raises(ValueError, match="Input changed during comparison"):
        assess(sample)


def cli(sample, output):
    root, baseline, expected = sample
    return [
        sys.executable,
        str(SOURCE),
        "--root",
        str(root),
        "--baseline",
        str(baseline),
        "--baseline-receipt-sha256",
        expected,
        "--prior-companion",
        PRIOR,
        "--companion-review",
        CURRENT,
        "--output",
        str(output),
    ]


def test_cli_requires_selected_companion_and_never_overwrites_receipt(sample, tmp_path):
    output = tmp_path / "comparison.json"
    command = cli(sample, output)
    start = command.index("--companion-review")
    missing = subprocess.run(command[:start] + command[start + 2 :], capture_output=True, text=True)
    assert missing.returncode == 2 and not output.exists()
    assert subprocess.run(command, capture_output=True).returncode == 0
    original = output.read_bytes()
    assert subprocess.run(command, capture_output=True).returncode == 2
    assert output.read_bytes() == original


def test_cli_companion_promotion_returns_failure_with_diagnostic(sample, tmp_path):
    edit_companion(sample, lambda value: value["decisions"][1].update(disposition="SUPPORTED"))
    output = tmp_path / "comparison.json"
    assert subprocess.run(cli(sample, output), capture_output=True).returncode == 1
    assert comparison.read(output)["scientific_approval_added"] is True
