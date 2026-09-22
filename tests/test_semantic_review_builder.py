"""Regression checks for #716 source binding and #717 mapping review scope."""

import copy
import hashlib
import importlib.util
import json
from pathlib import Path

import pytest

PATH = Path(__file__).parents[1] / "reports/semantic_review_20260921/resolution/build_review.py"
SPEC = importlib.util.spec_from_file_location("semantic_review_builder", PATH)
builder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(builder)


@pytest.fixture
def role_review():
    assertion = {"role": "ELECTRON_DONOR", "metabolic_context": "named isolate only",
                 "evidence": [{"reference_type": "PEER_REVIEWED_PUBLICATION", "doi": "10.1234/fixture"}]}
    record = {"identifier": "CHEBI:fixture", "cellular_metabolic_roles": [assertion]}
    item = {"source_path": "ingredient.yaml", "source_position": "1", "after_sha256": "reviewed-hash",
            "after_record": copy.deepcopy(record), "after_assertion": copy.deepcopy(assertion)}
    return item, record, assertion


def test_role_approval_binds_chemical_identity_and_position(role_review):
    item, record, assertion = role_review
    assert builder.role_supported(item, "ingredient.yaml", record, "reviewed-hash", "1", assertion)
    assert not builder.role_supported(item, "other.yaml", record, "reviewed-hash", "1", assertion)
    assert not builder.role_supported(item, "ingredient.yaml", record, "reviewed-hash", "2", assertion)
    assert not builder.role_supported(item, "ingredient.yaml", record, "changed-hash", "1", assertion)
    record["identifier"] = "CHEBI:different_chemical"
    assert not builder.role_supported(item, "ingredient.yaml", record, "reviewed-hash", "1", assertion)


@pytest.mark.parametrize("change", ["identity", "duplicate_role", "file_hash"])
def test_stale_role_plan_cannot_close_old_finding(role_review, change):
    item, record, assertion = role_review
    hashes = {"ingredient.yaml": "reviewed-hash"}
    if change == "identity":
        record["identifier"] = "CHEBI:another_chemical"
    elif change == "duplicate_role":
        record["cellular_metabolic_roles"].append(copy.deepcopy(assertion))
    else:
        hashes["ingredient.yaml"] = "new-bytes"
    with pytest.raises(ValueError, match="Role plan no longer describes"):
        builder.validate_explicit_plans({"ingredient.yaml": record}, hashes, [item], {}, [], [])


@pytest.mark.parametrize("change", ["source", "hash", "position"])
def test_identical_payload_does_not_transfer_review_to_another_source(change):
    old = {"source_record": "reviewed.yaml", "assertion_type": "nutritional_roles", "assertion_sha256": "shared-payload",
           "verdict": "pass", "record_sha256": "original-hash", "edge_id": "reviewed-edge",
           "review_report": "review.md", "historical_review_sha256": "reasoning-hash"}
    claim = {"evidence": [{"reference_type": "PEER_REVIEWED_PUBLICATION"}]}
    role_review = {"source_record": "reviewed.yaml", "source_record_sha256": "original-hash",
                   "assertion_type": "nutritional_roles", "assertion_sha256": "shared-payload",
                   "edge_id": "reviewed-edge", "source_position": "1", "disposition": "ELIGIBLE_PRIMARY_STUDY",
                   "historical_review_path": "review.md", "historical_review_sha256": "reasoning-hash",
                   "review_reason": "Exact scoped claim inspected in primary study"}
    args = dict(old_rows=[old], hashes={"reviewed.yaml": "original-hash"}, owner="reviewed.yaml",
                kind="nutritional_roles", payload_sha="shared-payload", edge={"id": "reviewed-edge", "source_position": "1"}, assertion=claim,
                role_reviews=[role_review])
    assert builder.inherited_approval(**args)
    if change == "source":
        args["owner"] = "unreviewed.yaml"
        args["hashes"]["unreviewed.yaml"] = "original-hash"
    elif change == "hash":
        args["hashes"]["reviewed.yaml"] = "changed-hash"
    else:
        args["edge"]["id"] = "same-claim-at-new-position"
    assert not builder.inherited_approval(**args)


@pytest.mark.parametrize("kind,assertion", [
    ("nutritional_roles", {"evidence": []}),
    ("nutritional_roles", {"evidence": [{"reference_type": "COMPUTATIONAL_PREDICTION"}]}),
    ("cellular_metabolic_roles", {"evidence": [{"reference_type": "PEER_REVIEWED_PUBLICATION"}]}),
    ("component", {"component_assertion": {"method": "ABBREVIATION_EXPANSION"}}),
    ("component", {"component_assertion": {"method": "CURATED_INTERPRETATION"}}),
    ("recipe_reference", {"relationship": "CANDIDATE_UNVERIFIED"}),
])
def test_old_positive_verdict_cannot_override_explicit_evidence_gap(kind, assertion):
    old = {"source_record": "a.yaml", "assertion_type": kind, "assertion_sha256": "claim",
           "verdict": "pass", "record_sha256": "file", "edge_id": "edge"}
    assert not builder.inherited_approval([old], {"a.yaml": "file"}, "a.yaml", kind, "claim", {"id": "edge"}, assertion)


@pytest.fixture
def identity():
    return {"identifier": "cas:13902-54-0", "preferred_term": "Artepaulin",
            "ontology_mapping": {"ontology_id": "cas:13902-54-0", "ontology_label": "Artepaulin", "mapping_quality": "FALLBACK_REGISTRY"}}


@pytest.mark.parametrize("field,value", [
    ("object_id", "CHEBI:78018"),
    ("predicate_id", "skos:broadMatch"),
    ("object_label", "dodecylphosphocholine"),
    ("subject_label", "another ingredient"),
])
def test_reviewed_subject_does_not_approve_a_different_mapping(identity, field, value):
    mapping = {"subject_label": "Artepaulin", "object_id": "cas:13902-54-0",
               "predicate_id": "skos:exactMatch", "object_label": "Artepaulin"}
    assert builder.identity_mapping_supported(identity, mapping)
    mapping[field] = value
    assert not builder.identity_mapping_supported(identity, mapping)


def test_reviewed_close_relation_cannot_be_promoted_to_exact(identity):
    identity["ontology_mapping"].update(ontology_id="CHEBI:fixture", ontology_label="related parent", mapping_quality="CLOSE_MATCH")
    mapping = {"subject_label": "Artepaulin", "object_id": "CHEBI:fixture",
               "predicate_id": "skos:closeMatch", "object_label": "related parent"}
    assert builder.identity_mapping_supported(identity, mapping)
    mapping["predicate_id"] = "skos:exactMatch"
    assert not builder.identity_mapping_supported(identity, mapping)


def test_inherited_reasoning_is_archived_and_works_in_clean_checkout(tmp_path):
    report = tmp_path / "ignored-review.md"
    report.write_text("Original bounded scientific reasoning.\n")
    report_sha = hashlib.sha256(report.read_bytes()).hexdigest()
    old = {"source_record": "a.yaml", "verdict": "pass", "record_sha256": "record-hash", "review_report": report.name}
    original = {"a.yaml": {"record_sha256": "record-hash", "review_report": report.name, "report_sha256": report_sha}}
    archive = tmp_path / "historical.json"
    assert builder.archive_historical_reviews(tmp_path, [old], original, {"a.yaml": "record-hash"}, archive) == [old]
    archived = json.loads(archive.read_text())["reports"][report.name]
    assert archived["sha256"] == report_sha and archived["text"] == report.read_text()
    report.unlink()
    assert builder.archive_historical_reviews(tmp_path, [old], original, {"a.yaml": "record-hash"}, archive) == [old]


@pytest.mark.parametrize("change", ["missing", "changed", "wrong_path", "wrong_record", "changed_archive"])
def test_unbound_historical_reasoning_does_not_grant_approval(tmp_path, change):
    report = tmp_path / "review.md"
    data = b"Reviewed reasoning.\n"
    report.write_bytes(data)
    expected = hashlib.sha256(data).hexdigest()
    old = {"source_record": "a.yaml", "verdict": "pass", "record_sha256": "record", "review_report": report.name}
    original = {"a.yaml": {"record_sha256": "record", "review_report": report.name, "report_sha256": expected}}
    archive = tmp_path / "archive.json"
    if change == "missing":
        report.unlink()
    elif change == "changed":
        report.write_text("A more permissive changed review")
    elif change == "wrong_path":
        old["review_report"] = "unreviewed.md"
    elif change == "wrong_record":
        original["a.yaml"]["record_sha256"] = "a different ingredient"
    else:
        report.unlink()
        archive.write_text(json.dumps({"reports": {report.name: {"sha256": expected, "text": "Tampered approval"}}}))
    assert builder.archive_historical_reviews(tmp_path, [old], original, {"a.yaml": "record"}, archive) == []


@pytest.mark.parametrize("mutation", ["missing_role_review", "unverified_promotion", "record", "position", "report", "reason"])
def test_record_pass_cannot_approve_unreviewed_biological_promotion(mutation):
    old = {"source_record": "Bacl2.yaml", "assertion_type": "nutritional_roles", "assertion_sha256": "claim",
           "verdict": "pass", "record_sha256": "record", "edge_id": "edge",
           "review_report": "Bacl2.md", "historical_review_sha256": "report"}
    claim = {"role": "TRACE_ELEMENT", "evidence": [{"reference_type": "DATABASE_ENTRY", "curator_note": "Original role text: Mineral"}]}
    review = {"source_record": "Bacl2.yaml", "source_record_sha256": "record", "assertion_type": "nutritional_roles",
              "assertion_sha256": "claim", "edge_id": "edge", "source_position": "1",
              "historical_review_path": "Bacl2.md", "historical_review_sha256": "report",
              "review_reason": "Synthetic explicit source-scope review", "disposition": "ELIGIBLE_PRIMARY_STUDY"}
    reviews = [review]
    if mutation == "missing_role_review":
        reviews = []
    elif mutation == "unverified_promotion":
        review["disposition"] = "OPEN_NEEDS_CLAIM_EVIDENCE"
    elif mutation == "record":
        review["source_record_sha256"] = "different-chemical"
    elif mutation == "position":
        review["source_position"] = "2"
    elif mutation == "report":
        review["historical_review_sha256"] = "changed-reasoning"
    else:
        review["review_reason"] = " "
    assert not builder.inherited_approval([old], {"Bacl2.yaml": "record"}, "Bacl2.yaml", "nutritional_roles",
                                          "claim", {"id": "edge", "source_position": "1"}, claim, reviews)


def test_scientific_role_audit_keeps_all24_unverified_promotions_open():
    ledger = json.loads((PATH.parent / "roles/inherited-role-review.json").read_text())
    entries = ledger["entries"]
    assert len(entries) == 138
    opened = [entry for entry in entries if entry["disposition"] == "OPEN_NEEDS_CLAIM_EVIDENCE"]
    assert len(opened) == 24
    assert {entry["role"] for entry in opened} == {
        "TRACE_ELEMENT", "IRON_SOURCE", "PHOSPHATE_SOURCE", "SULFUR_SOURCE", "VITAMIN_SOURCE"}
    for stem in ("Bacl2", "Sncl2_X_2_H2o", "Dl-alpha-lipoic_Acid"):
        assert any(entry["source_record"].endswith(f"/{stem}.yaml") for entry in opened)

@pytest.fixture
def release_hold():
    document = json.loads((PATH.parent / "release-holds.json").read_text())
    # Keep exercising the original active hold after its source correction.
    document = {"schema_version": 1, "required_hold_ids": document["required_hold_ids"],
                "holds": document.get("historical_holds", document["holds"])}
    hold = document["holds"][0]
    fields = (
        "assertion_id",
        "source_record",
        "source_record_sha256",
        "assertion_type",
        "source_position",
        "assertion_sha256",
    )
    decision = {
        **{key: hold[key] for key in fields},
        "resolution_status": "APPROVED",
        "review_reason": "Existing positive review",
        "review_evidence": "old-review.json",
    }
    edge = {key: hold[key] for key in ("source_record", "assertion_type", "source_position")}
    edge.update(id=hold["edge_id"], assertion_json=json.dumps(hold["assertion"]))
    unaffected = copy.deepcopy(decision)
    unaffected.update(assertion_id="MIM.review:unaffected", source_position="999")
    unaffected_edge = copy.deepcopy(edge)
    unaffected_edge.update(id="MIM.assertion:unaffected", source_position="999")
    return {
        "document": document,
        "assertions": [decision, unaffected],
        "edges": [edge, unaffected_edge],
        "owners": {hold["assertion"]["subject_id"]: hold["owner_record"]},
        "record_hashes": {hold["owner_record"]: hold["owner_record_sha256"]},
        "evidence_path": "release-holds.json",
    }


def test_negative_release_review_overrides_positive_without_editing_raw_claim(release_hold):
    raw_edges = copy.deepcopy(release_hold["edges"])
    unaffected = copy.deepcopy(release_hold["assertions"][1])
    builder.apply_release_holds(**release_hold)
    held = release_hold["assertions"][0]
    assert held["resolution_status"] == "OPEN"
    assert held["review_evidence"] == "release-holds.json"
    assert held["review_reason"] == builder.FROZEN_RELEASE_HOLD_REASON
    assert release_hold["assertions"][1] == unaffected
    assert release_hold["edges"] == raw_edges
    assert "degradation: aromatic compound" in json.loads(raw_edges[0]["assertion_json"])["other"]


def test_hold_cannot_be_retargeted_to_a_different_claim_from_same_owner(release_hold):
    hold = release_hold["document"]["holds"][0]
    other = release_hold["assertions"][1]
    for field in (
        "assertion_id",
        "source_record",
        "source_record_sha256",
        "assertion_type",
        "source_position",
        "assertion_sha256",
    ):
        hold[field] = other[field]
    hold["edge_id"] = release_hold["edges"][1]["id"]
    before = copy.deepcopy(release_hold["assertions"])
    with pytest.raises(
        ValueError, match="Maintained release-hold policy was altered or retargeted"
    ):
        builder.apply_release_holds(**release_hold)
    assert release_hold["assertions"] == before


@pytest.mark.parametrize(
    "mutation",
    [
        "required",
        "missing",
        "duplicate",
        "assertion_id",
        "payload_hash",
        "source_hash",
        "position",
        "owner",
        "owner_hash",
        "payload",
        "reason",
        "reason_scope",
        "issue",
    ],
)
def test_invalid_frozen_release_hold_stops_before_any_decision_changes(release_hold, mutation):
    document = release_hold["document"]
    hold = document["holds"][0]
    if mutation == "required":
        document["required_hold_ids"] = []
    elif mutation == "missing":
        document["holds"] = []
    elif mutation == "duplicate":
        document["holds"].append(copy.deepcopy(hold))
    elif mutation == "assertion_id":
        hold["assertion_id"] = "MIM.review:missing"
    elif mutation == "payload_hash":
        hold["assertion_sha256"] = "stale-payload"
    elif mutation == "source_hash":
        hold["source_record_sha256"] = "stale-sssom"
    elif mutation == "position":
        hold["source_position"] = "2"
    elif mutation == "owner":
        hold["owner_record"] = "another-ingredient.yaml"
    elif mutation == "owner_hash":
        hold["owner_record_sha256"] = "stale-ingredient"
    elif mutation == "payload":
        hold["assertion"]["other"] = "cleaned without a new review"
    elif mutation == "reason":
        hold["review_reason"] = " "
    elif mutation == "reason_scope":
        hold["review_reason"] = "Different unreviewed exclusion"
    else:
        hold["issues"] = []
    before = copy.deepcopy(release_hold["assertions"])
    with pytest.raises(ValueError):
        builder.apply_release_holds(**release_hold)
    assert release_hold["assertions"] == before
