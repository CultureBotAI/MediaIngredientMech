"""2026-11-07 synthetic controls; no real campaign scientific decisions."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from pathlib import Path

import pytest

MODULE = Path(__file__).with_name("audit_worker_outcomes_v1.py")
SPEC = importlib.util.spec_from_file_location("private_outcome_auditor", MODULE)
NATIVE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(NATIVE)


def write(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")


@pytest.fixture
def bundle(tmp_path):
    artifacts = tmp_path / "artifacts"
    sources = tmp_path / "sources"
    artifacts.mkdir()
    sources.mkdir()
    capture = sources / "synthetic-source.txt"
    capture.write_text("SYNTHETIC testing source; no scientific assertion\n")
    cases = [
        {
            "case_id": "CM_NAME:synthetic-a",
            "source": "culturemech",
            "source_case_id": "A",
            "source_label": "A",
            "raw_source_label": "A",
            "occurrences": [
                {"occurrence_id": "CM_OCC:synthetic-1"},
                {"occurrence_id": "CM_OCC:synthetic-2"},
            ],
        },
        {
            "case_id": "KG_CASE:synthetic-blank",
            "source": "mediadive",
            "source_case_id": "test:blank",
            "source_label": "",
            "raw_source_label": "",
            "original_kg_entry": {"source_record": {"compound": ""}},
        },
    ]
    shard = {"schema_version": 1, "worker_slot": 1, "cases": cases}
    shard_path = sources / "shard.json"
    write(shard_path, shard)
    outcomes = []
    for case in cases:
        outcomes.append(
            {
                "case_id": case["case_id"],
                "case_input_sha256": NATIVE.case_digest(case),
                "source": {
                    field: case[field]
                    for field in ["source", "source_case_id", "source_label", "raw_source_label"]
                },
                "occurrence_ids": [item["occurrence_id"] for item in case.get("occurrences", [])],
                "disposition": "unresolved",
                "reasoning": "Synthetic fixture only: source lacks supplied identity.",
                "applicability": "Synthetic reference corresponds to the exact test source case.",
                "evidence_ids": ["synthetic-source"],
                "proposal_ids": [],
                "no_change_reason": "Synthetic input does not establish an owner.",
                "missing_requirement": "Obtain an exact source identifier for this synthetic test case.",
                "owner_records": [],
                "issue_refs": [],
                "independent_review": {"status": "pending", "evidence_ids": []},
            }
        )
    decisions = {
        "schema_version": 1,
        "phase": "shard",
        "worker_slot": 1,
        "shard_sha256": NATIVE.digest(shard_path),
        "decisions": outcomes,
    }
    evidence = {
        "schema_version": 1,
        "evidence": [
            {
                "evidence_id": "synthetic-source",
                "kind": "source_snapshot",
                "url": None,
                "capture": {
                    "root": "source",
                    "path": capture.name,
                    "sha256": NATIVE.digest(capture),
                },
                "locator": "complete synthetic file",
                "supports_or_contradicts": "Synthetic source provenance only.",
            }
        ],
    }
    proposals = {"schema_version": 1, "proposals": []}
    paths = {name: artifacts / (name + ".json") for name in ["decisions", "evidence", "proposals"]}
    state = {
        "artifacts": artifacts,
        "sources": sources,
        "shard_path": shard_path,
        "shard": shard,
        "decisions": decisions,
        "evidence": evidence,
        "proposals": proposals,
        "paths": paths,
    }

    def run(**kwargs):
        for name, path in paths.items():
            write(path, state[name])
        return NATIVE.audit(
            shard_path,
            paths["decisions"],
            paths["evidence"],
            paths["proposals"],
            artifacts,
            sources,
            **kwargs,
        )

    state["run"] = run
    return state


def test_whole_shard_accounting_is_not_scientific_approval(bundle):
    result = bundle["run"]()
    assert result["accounted_case_count"] == 2
    assert result["structural_accounting"] == "PASS"
    assert result["scientific_adequacy_or_approval_established"] is False
    assert result["independent_review_status_counts"] == {"pending": 2}


def test_only_explicit_canary_allows_exact_singleton(bundle):
    row = bundle["decisions"]["decisions"][1]
    bundle["decisions"].update(phase="canary", decisions=[row])
    result = bundle["run"](canary_case=row["case_id"])
    assert result["accounted_case_count"] == 1
    assert result["assigned_shard_case_count"] == 2
    assert result["out_of_scope_shard_case_ids"] == ["CM_NAME:synthetic-a"]
    with pytest.raises(NATIVE.InvalidOutcome, match="explicit audit scope"):
        bundle["run"]()


def test_missing_case_fails(bundle):
    bundle["decisions"]["decisions"].pop()
    with pytest.raises(NATIVE.InvalidOutcome, match="missing or out-of-scope"):
        bundle["run"]()


def test_duplicate_case_fails(bundle):
    bundle["decisions"]["decisions"].append(copy.deepcopy(bundle["decisions"]["decisions"][0]))
    with pytest.raises(NATIVE.InvalidOutcome, match="duplicate decision"):
        bundle["run"]()


def test_unassigned_case_fails(bundle):
    bundle["decisions"]["decisions"][1]["case_id"] = "KG_CASE:unassigned"
    with pytest.raises(NATIVE.InvalidOutcome, match="missing or out-of-scope"):
        bundle["run"]()


def test_dangling_evidence_fails(bundle):
    bundle["decisions"]["decisions"][0]["evidence_ids"] = ["not-captured"]
    with pytest.raises(NATIVE.InvalidOutcome, match="dangling evidence"):
        bundle["run"]()


def test_evidence_cannot_claim_out_of_scope_case(bundle):
    bundle["evidence"]["evidence"][0]["case_ids"] = ["KG_CASE:other-worker"]
    with pytest.raises(NATIVE.InvalidOutcome, match="evidence claims an unassigned case"):
        bundle["run"]()


def test_modified_capture_fails(bundle):
    (bundle["sources"] / "synthetic-source.txt").write_text("changed")
    with pytest.raises(NATIVE.InvalidOutcome, match="capture hash differs"):
        bundle["run"]()


def test_omitted_occurrence_fails(bundle):
    bundle["decisions"]["decisions"][0]["occurrence_ids"].pop()
    with pytest.raises(NATIVE.InvalidOutcome, match="occurrence reference"):
        bundle["run"]()


def test_raw_blank_label_cannot_be_filled_implicitly(bundle):
    bundle["decisions"]["decisions"][1]["source"]["raw_source_label"] = "guessed ingredient"
    with pytest.raises(NATIVE.InvalidOutcome, match="source identity/name"):
        bundle["run"]()


def test_wrong_case_content_digest_fails(bundle):
    bundle["decisions"]["decisions"][0]["case_input_sha256"] = "0" * 64
    with pytest.raises(NATIVE.InvalidOutcome, match="input case hash"):
        bundle["run"]()


@pytest.mark.parametrize(
    "field", ["missing_requirement", "no_change_reason", "reasoning", "applicability"]
)
def test_required_reasoning_and_explicit_no_change(bundle, field):
    bundle["decisions"]["decisions"][0][field] = ""
    with pytest.raises(NATIVE.InvalidOutcome, match="nonempty string"):
        bundle["run"]()


def test_unassigned_proposal_fails(bundle):
    bundle["proposals"]["proposals"] = [{"proposal_id": "p", "case_ids": ["not-assigned"]}]
    with pytest.raises(NATIVE.InvalidOutcome, match="unassigned case"):
        bundle["run"]()


def test_claimed_independent_review_needs_review_evidence(bundle):
    bundle["decisions"]["decisions"][0]["independent_review"] = {
        "status": "complete",
        "evidence_ids": ["synthetic-source"],
    }
    with pytest.raises(NATIVE.InvalidOutcome, match="wrong evidence kind"):
        bundle["run"]()


def test_path_traversal_capture_fails(bundle):
    bundle["evidence"]["evidence"][0]["capture"]["path"] = "../other.txt"
    with pytest.raises(NATIVE.InvalidOutcome, match="safe relative"):
        bundle["run"]()


def test_symlink_capture_fails(bundle):
    capture = bundle["sources"] / "alias.txt"
    capture.symlink_to(bundle["sources"] / "synthetic-source.txt")
    bundle["evidence"]["evidence"][0]["capture"]["path"] = capture.name
    with pytest.raises(NATIVE.InvalidOutcome, match="symlink"):
        bundle["run"]()


def test_existing_owner_proposal_requires_exact_before_bytes(bundle):
    mim = bundle["artifacts"] / "synthetic-mim"
    owner = mim / "data/ingredients/unmapped/Synthetic.yaml"
    owner.parent.mkdir(parents=True)
    owner.write_text("identifier: UNMAPPED_TEST\n")
    after = bundle["artifacts"] / "proposal.yaml"
    after.write_text("identifier: UNMAPPED_TEST\nnotes: proposed only\n")
    decision = bundle["decisions"]["decisions"][0]
    decision["owner_records"] = [
        {"path": owner.relative_to(mim).as_posix(), "sha256": NATIVE.digest(owner)}
    ]
    decision["proposal_ids"] = ["proposal-1"]
    decision["no_change_reason"] = None
    proposal = {
        "proposal_id": "proposal-1",
        "case_ids": [decision["case_id"]],
        "description": "Synthetic notes proposal only.",
        "kind": "edit_existing_owner",
        "owner_path": owner.relative_to(mim).as_posix(),
        "before_sha256": NATIVE.digest(owner),
        "after_capture": {"root": "artifact", "path": after.name, "sha256": NATIVE.digest(after)},
        "evidence_ids": ["synthetic-source"],
    }
    bundle["proposals"]["proposals"] = [proposal]
    assert bundle["run"](mim_root=mim)["proposal_count"] == 1
    proposal["before_sha256"] = "0" * 64
    with pytest.raises(NATIVE.InvalidOutcome, match="verified owner bytes"):
        bundle["run"](mim_root=mim)


def test_json_duplicate_keys_rejected(tmp_path):
    path = tmp_path / "duplicate.json"
    path.write_text('{"case_id":"a","case_id":"b"}')
    with pytest.raises(NATIVE.InvalidOutcome, match="duplicate JSON key"):
        NATIVE.read_json(path)


def test_case_hash_recipe_is_canonical():
    payload = {"b": "α", "a": 1}
    expected = hashlib.sha256('{"a":1,"b":"α"}'.encode()).hexdigest()
    assert NATIVE.case_digest(payload) == expected
