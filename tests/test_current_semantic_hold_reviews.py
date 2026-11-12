"""#1394 current full-row holds need captured native independent release evidence."""

import copy
from types import SimpleNamespace

import pytest
import yaml

from mediaingredientmech.curate import stable_sssom_publication as publication
from mediaingredientmech.validation.current_semantic_release import POLICY, Inputs, _hold_reviews
from tests.test_stable_id_adoption import ROOT, Fixture, api, commit, initialize, write

OWNER = "data/ingredients/mapped/Exact.yaml"
PAYLOADS = "hold-payloads.json"


def native_pair(tmp_path, attack=None, dispositions=("SUPPORTED", "SUPPORTED")):
    """Use real native inspect/save and Git, without a producer/runtime stub."""
    root = tmp_path / "consumer"
    initialize(root)
    for name in (
        "MAPPING_SEMANTICS.md",
        "schema/record_review.yaml",
        "scripts/record_review.py",
        POLICY,
    ):
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes((ROOT / name).read_bytes())
    owner = {"mim_id": "MIM:0000001", "identifier": "CHEBI:1", "preferred_term": "Synthetic"}
    path = root / OWNER
    path.parent.mkdir(parents=True)
    path.write_text(yaml.safe_dump(owner))
    source = root / publication.CANONICAL
    source.parent.mkdir()
    source.write_text(
        "subject_id\tpredicate_id\tobject_id\nMIM:0000001\tskos:exactMatch\tCHEBI:1\n"
    )
    (root / "primary.txt").write_text("Synthetic captured identity and original hold evidence.\n")
    write(root / "context.json", {"scientific_approval": False})
    payload = {
        "hold_id": "synthetic-hold",
        "owner": OWNER,
        "owner_sha256": api.sha(path.read_bytes()),
        "original_negative": {"reason": "Synthetic supplied-form uncertainty"},
        "current_row": {
            "subject_id": "MIM:0000001",
            "predicate_id": "skos:exactMatch",
            "object_id": "CHEBI:1",
        },
        "changed_cells": {},
    }
    write(root / PAYLOADS, {"schema_version": 1, "holds": [payload]})
    commit(root)
    native = publication._CAPTURE.script("scripts/record_review.py")
    author = SimpleNamespace(
        root=root, native=native, request={"eligibility_intake": {"path": "context.json"}}
    )
    target = {
        "target_id": "held-row",
        "kind": "snapshot_row",
        "label": "Synthetic held row",
        "path": PAYLOADS,
        "selector": payload["hold_id"],
        "owner_paths": [{"repository": api.REPOSITORY, "path": OWNER, "role": "Current owner"}],
        "semantic_digest": {
            "algorithm": "sha256-canonical-json-v1",
            "sha256": api.digest(payload),
            "description": "Complete synthetic hold lineage and current full row",
        },
    }
    refs = []
    for index, role in enumerate(("primary", "skeptic")):
        report = Fixture.report(
            author,
            role,
            [copy.deepcopy(target)],
            [PAYLOADS, publication.CANONICAL, OWNER, POLICY, "primary.txt"],
        )
        report["review_id"] = "20260102T000000Z-current-hold-" + role
        report["assessments"] = [
            {
                "assessment_id": "held",
                "area": "identity",
                "topic": "Current release hold",
                "outcome": "supported",
                "summary": "Synthetic exact full-row and hold assessment only.",
                "target_ids": [target["target_id"]],
                "evidence_ids": ["primary"],
                "dimensions": [
                    {
                        "name": key,
                        "value": value,
                        "definition": "Exact current scope",
                        "evidence_ids": ["primary"],
                    }
                    for key, value in {
                        "semantic_scope": "current_mapping_release_and_historical_hold",
                        "disposition": dispositions[index],
                    }.items()
                ],
            }
        ]
        if attack and index == 0:
            if attack == "uncaptured_evidence":
                report["evidence"][0]["snapshot_sha256"] = "0" * 64
            elif attack == "record_only_evidence":
                report["evidence"][0]["kind"] = "record_content"
            elif attack == "context_only_evidence":
                report["evidence"][0]["support"] = "context_only"
            elif attack == "installation_scope":
                report["assessments"][0]["dimensions"][0]["value"] = (
                    "canonical_installation_not_release_approval"
                )
            elif attack == "missing_owner":
                report["source"]["inputs"] = [
                    item for item in report["source"]["inputs"] if item["path"] != OWNER
                ]
            elif attack == "changed_payload":
                report["targets"][0]["semantic_digest"]["sha256"] = "0" * 64
            else:
                raise AssertionError(attack)
        saved = native.save_review(root, report, schema_path=root / "schema/record_review.yaml")
        refs.append(
            {
                "path": str(saved.relative_to(root)),
                "sha256": api.sha(saved.read_bytes()),
                "markdown_sha256": api.sha(saved.with_name("review.md").read_bytes()),
                "target_id": target["target_id"],
                "assessment_id": "held",
            }
        )
    request = {"hold_reviews": {payload["hold_id"]: refs}, "review_inputs": {}}
    return Inputs(root), request, [payload], PAYLOADS


def test_current_independent_native_pair_can_review_complete_hold(tmp_path):
    assert _hold_reviews(*native_pair(tmp_path)) == {"synthetic-hold": "SUPPORTED"}


def test_disagreement_preserves_hold(tmp_path):
    assert _hold_reviews(*native_pair(tmp_path, dispositions=("SUPPORTED", "WITHHOLD"))) == {
        "synthetic-hold": "WITHHOLD"
    }


@pytest.mark.parametrize(
    "attack,reason",
    [
        ("installation_scope", "installation review is not hold release approval"),
        ("missing_owner", "hold review omits current input"),
        ("changed_payload", "hold review does not bind complete lineage"),
        ("uncaptured_evidence", "captured evidence"),
        ("record_only_evidence", "captured primary evidence"),
        ("context_only_evidence", "captured primary evidence"),
    ],
)
def test_native_valid_pair_cannot_replace_current_hold_proof(tmp_path, attack, reason):
    with pytest.raises(ValueError, match=reason):
        _hold_reviews(*native_pair(tmp_path, attack))
