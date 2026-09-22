"""A source correction must not erase or retarget the original negative review."""

import copy
import csv
import hashlib
import importlib.util
import json
from pathlib import Path

import pytest
import yaml

from mediaingredientmech.validation import semantic_release as gate

ROOT = Path(__file__).parents[1]
BUILDER_PATH = ROOT / "reports/semantic_review_20260921/resolution/build_review.py"
HOLD_ID = "MIM.hold:724-aromatic-trait-synonym"
TRAIT = "degradation: aromatic compound"


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


builder = load_module("hold_resolution_builder", BUILDER_PATH)


@pytest.fixture
def corrected_hold():
    """Use tracked correction bytes; ignored graph outputs are not test inputs."""
    document = json.loads((BUILDER_PATH.parent / "release-holds.json").read_text())
    resolution = next(r for r in document["resolutions"] if r["hold_id"] == HOLD_ID)
    owner = resolution["owner_record"]
    record = yaml.safe_load((ROOT / owner).read_text())
    source = ROOT / "mappings/ingredient_mappings.sssom.tsv"
    with source.open() as stream:
        mappings = list(
            csv.DictReader((s for s in stream if not s.startswith("#")), delimiter="\t")
        )
    hashes = {owner: gate.sha(ROOT / owner)}
    current = gate.current_assertions({owner: record}, mappings, hashes, gate.sha(source))
    identity = next(r for r in current if r["assertion_id"] == resolution["assertion_id"])
    claim = mappings[int(identity["source_position"]) - 1]
    decision = dict(
        identity,
        resolution_status="OPEN",
        review_reason="Still needs scoped approval",
        review_evidence="",
    )
    edge = {k: identity[k] for k in ("source_record", "assertion_type", "source_position")}
    edge.update(id=resolution["edge_id"], assertion_json=json.dumps(claim))
    return {
        "document": document,
        "assertions": [decision],
        "edges": [edge],
        "owners": {claim["subject_id"]: owner},
        "record_hashes": hashes,
        "evidence_path": "release-holds.json",
    }


def check(args):
    return gate.validate_release_holds(**args)


def test_exact_correction_resolves_hold_without_granting_scientific_approval(corrected_hold):
    before = copy.deepcopy(corrected_hold["assertions"])
    assert check(corrected_hold) == {}
    builder.apply_release_holds(**corrected_hold)
    assert corrected_hold["assertions"] == before
    assert before[0]["resolution_status"] == "OPEN"


def test_reviewed_correction_preserves_rejected_raw_trait_and_original_negative_payload(
    corrected_hold,
):
    historical = corrected_hold["document"]["historical_holds"][0]
    owner = historical["owner_record"]
    record = yaml.safe_load((ROOT / owner).read_text())
    assert any(
        s["synonym_text"] == TRAIT and s["synonym_type"] == "REJECTED_LABEL"
        for s in record["synonyms"]
    )
    assert TRAIT in historical["assertion"]["other"].split("|")
    assert TRAIT not in json.loads(corrected_hold["edges"][0]["assertion_json"])["other"].split("|")
    payload = json.dumps(historical["assertion"], sort_keys=True, separators=(",", ":"))
    assert hashlib.sha256(payload.encode()).hexdigest() == historical["assertion_sha256"]


@pytest.mark.parametrize(
    "mutation", ["resolution", "all_inventories", "history", "history_reason", "duplicate"]
)
def test_resolution_cannot_remove_the_review_obligation(corrected_hold, mutation):
    document = corrected_hold["document"]
    if mutation == "resolution":
        document["resolutions"] = []
    elif mutation == "all_inventories":
        document.update(required_hold_ids=[], holds=[], resolutions=[], historical_holds=[])
    elif mutation == "history":
        document["historical_holds"] = []
    elif mutation == "history_reason":
        document["historical_holds"][0]["review_reason"] = "The old claim was fine."
    else:
        document["resolutions"].append(copy.deepcopy(document["resolutions"][0]))
    before = copy.deepcopy(corrected_hold["assertions"])
    with pytest.raises(ValueError):
        builder.apply_release_holds(**corrected_hold)
    assert corrected_hold["assertions"] == before


@pytest.mark.parametrize("mutation", ["unknown_hold", "unknown_policy", "correction_evidence"])
def test_unreviewed_resolution_policy_is_rejected(corrected_hold, mutation):
    document = corrected_hold["document"]
    resolution = document["resolutions"][0]
    if mutation == "unknown_hold":
        extra = dict(resolution, hold_id="test:unreviewed-resolution")
        document["required_hold_ids"].append(extra["hold_id"])
        document["resolutions"].append(extra)
    elif mutation == "unknown_policy":
        resolution["resolution"] = "CURATOR_WAIVER"
    else:
        resolution["evidence_sha256"] = hashlib.sha256(b"Different unreviewed evidence").hexdigest()
    with pytest.raises(ValueError):
        check(corrected_hold)


@pytest.mark.parametrize("mutation", ["owner", "owner_bytes", "edge", "assertion_hash"])
def test_resolution_is_bound_to_current_owner_and_graph_claim(corrected_hold, mutation):
    if mutation == "owner":
        subject = next(iter(corrected_hold["owners"]))
        corrected_hold["owners"][subject] = "data/ingredients/mapped/Another.yaml"
    elif mutation == "owner_bytes":
        owner = next(iter(corrected_hold["record_hashes"]))
        corrected_hold["record_hashes"][owner] = hashlib.sha256(
            b"Trait restored to EXACT_SYNONYM"
        ).hexdigest()
    elif mutation == "edge":
        corrected_hold["edges"][0]["id"] = "MIM.assertion:different-edge"
    else:
        corrected_hold["assertions"][0]["assertion_sha256"] = hashlib.sha256(
            b"changed claim"
        ).hexdigest()
    with pytest.raises(ValueError):
        check(corrected_hold)


@pytest.mark.parametrize("retarget_resolution", [False, True])
def test_restored_trait_cannot_be_released_by_rehashing_claim_or_resolution(
    corrected_hold, retarget_resolution
):
    edge = corrected_hold["edges"][0]
    claim = json.loads(edge["assertion_json"])
    claim["other"] += "|" + TRAIT
    payload = json.dumps(claim, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha256(payload.encode()).hexdigest()
    identity = corrected_hold["assertions"][0]
    identity_input = [
        identity["source_record"],
        identity["assertion_type"],
        identity["source_position"],
        digest,
    ]
    identity.update(
        assertion_sha256=digest,
        assertion_id="MIM.review:"
        + hashlib.sha256(json.dumps(identity_input, separators=(",", ":")).encode()).hexdigest(),
    )
    edge["assertion_json"] = payload
    edge["id"] = (
        "MIM.assertion:" + hashlib.sha256(json.dumps(edge, sort_keys=True).encode()).hexdigest()
    )
    if retarget_resolution:
        corrected_hold["document"]["resolutions"][0].update(
            assertion_id=identity["assertion_id"], assertion_sha256=digest, edge_id=edge["id"]
        )
    with pytest.raises(ValueError):
        builder.apply_release_holds(**corrected_hold)


@pytest.mark.parametrize(
    "mutation", ["remove_payload", "rewrite_payload", "coherently_rehash_history"]
)
def test_original_negative_payload_is_immutable_after_resolution(corrected_hold, mutation):
    historical = corrected_hold["document"]["historical_holds"][0]
    if mutation == "remove_payload":
        historical.pop("assertion")
    else:
        historical["assertion"]["other"] = "An edited harmless claim"
        if mutation == "coherently_rehash_history":
            payload = json.dumps(historical["assertion"], sort_keys=True, separators=(",", ":"))
            historical["assertion_sha256"] = hashlib.sha256(payload.encode()).hexdigest()
    with pytest.raises(ValueError):
        check(corrected_hold)


def test_original_negative_hold_still_overrides_prior_approval(corrected_hold):
    historical = corrected_hold["document"]["historical_holds"][0]
    document = {"schema_version": 1, "required_hold_ids": [HOLD_ID], "holds": [historical]}
    identity = {
        key: historical[key]
        for key in (
            "assertion_id",
            "source_record",
            "source_record_sha256",
            "assertion_type",
            "source_position",
            "assertion_sha256",
        )
    }
    decision = dict(
        identity,
        resolution_status="APPROVED",
        review_reason="Old positive review",
        review_evidence="old.md",
    )
    edge = {key: identity[key] for key in ("source_record", "assertion_type", "source_position")}
    edge.update(id=historical["edge_id"], assertion_json=json.dumps(historical["assertion"]))
    builder.apply_release_holds(
        document,
        [decision],
        [edge],
        {historical["assertion"]["subject_id"]: historical["owner_record"]},
        {historical["owner_record"]: historical["owner_record_sha256"]},
        "release-holds.json",
    )
    assert decision["resolution_status"] == "OPEN"
    assert decision["review_reason"] == historical["review_reason"]


@pytest.fixture
def resolved_full_review(tmp_path, monkeypatch):
    """Exercise the full gate independently of real-corpus release artifacts."""
    fixture_module = load_module(
        "resolved_full_fixture", Path(__file__).with_name("test_semantic_release.py")
    )
    root, report_path = fixture_module.reviewed_bundle.__wrapped__(tmp_path)
    report = json.loads(report_path.read_text())
    identity = gate.rows(root / "assertions.tsv")[0]
    edge = gate.rows(root / "bundle/mim_edges.tsv", kgx=True)[0]
    owner = "data/ingredients/mapped/Water.yaml"
    hold_id = "test:resolved-negative"
    old_claim = json.loads(edge["assertion_json"])
    old_claim["other"] = "degradation: water"
    old_hash = hashlib.sha256(
        json.dumps(old_claim, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    policy = {
        "hold_id": hold_id,
        "owner_record": owner,
        "assertion_sha256": old_hash,
        "review_reason": "A trait is not a chemical synonym",
        "disposition": "WITHHOLD",
    }
    expected = {
        "assertion_id": identity["assertion_id"],
        "assertion_sha256": identity["assertion_sha256"],
        "owner_record": owner,
        "owner_record_sha256": report["record_inputs"][owner],
        "edge_id": edge["id"],
        "resolution": "SOURCE_CORRECTED",
        "evidence": "evidence.md",
        "evidence_sha256": gate.sha(root / "evidence.md"),
    }
    monkeypatch.setitem(gate.FROZEN_RELEASE_HOLDS, hold_id, policy)
    monkeypatch.setitem(gate.FROZEN_RELEASE_HOLD_RESOLUTIONS, hold_id, expected)
    document = {
        "schema_version": 1,
        "required_hold_ids": [hold_id],
        "holds": [],
        "historical_holds": [dict(policy, assertion=old_claim)],
        "resolutions": [dict(expected, hold_id=hold_id)],
    }
    (root / "holds.json").write_text(json.dumps(document))
    report["inputs"]["holds.json"] = gate.sha(root / "holds.json")
    report_path.write_text(json.dumps(report))
    return root, report_path


def test_full_gate_accepts_exact_reviewed_resolution(resolved_full_review):
    root, report = resolved_full_review
    assert gate.validate(root, report)["semantic_release"] == "PASS"


def test_full_gate_requires_correction_evidence_in_hashed_inputs(resolved_full_review):
    root, path = resolved_full_review
    # Keep approval evidence separately valid so the resolution check is exercised.
    report = json.loads(path.read_text())
    (root / "approval.md").write_text("Independent synthetic mapping approval\n")
    decisions = gate.rows(root / "assertions.tsv")
    for decision in decisions:
        decision["review_evidence"] = "approval.md"
    with (root / "assertions.tsv").open("w") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(decisions[0]), delimiter="\t")
        writer.writeheader()
        writer.writerows(decisions)
    report["inputs"].update(
        {
            "assertions.tsv": gate.sha(root / "assertions.tsv"),
            "approval.md": gate.sha(root / "approval.md"),
        }
    )
    report["inputs"].pop("evidence.md")
    path.write_text(json.dumps(report))
    with pytest.raises(ValueError, match="bound correction evidence"):
        gate.validate(root, path)


def test_full_gate_rejects_rehashed_rewrite_of_original_negative_payload(resolved_full_review):
    root, path = resolved_full_review
    document = json.loads((root / "holds.json").read_text())
    document["historical_holds"][0]["assertion"]["other"] = "No problematic historical trait"
    (root / "holds.json").write_text(json.dumps(document))
    report = json.loads(path.read_text())
    report["inputs"]["holds.json"] = gate.sha(root / "holds.json")
    path.write_text(json.dumps(report))
    with pytest.raises(ValueError):
        gate.validate(root, path)
