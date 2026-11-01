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


@pytest.mark.parametrize("change", ["formatting", "missing_hash", "payload"])
def test_identity_plan_requires_archived_exact_bytes(identity, change):
    reviewed = copy.deepcopy(identity)
    item = {"after_record": reviewed, "after_sha256": "archived-output-hash"}
    records, hashes = {"identity.yaml": identity}, {"identity.yaml": "archived-output-hash"}
    builder.validate_explicit_plans(records, hashes, [], {"identity.yaml": item}, [], [])
    if change == "formatting":
        # Parsed YAML remains identical, but the reviewed bytes no longer match.
        hashes["identity.yaml"] = "same-yaml-new-bytes"
    elif change == "missing_hash":
        item.pop("after_sha256")
    else:
        identity["preferred_term"] = "Changed identity"
    with pytest.raises(ValueError, match="Identity plan no longer describes"):
        builder.validate_explicit_plans(records, hashes, [], {"identity.yaml": item}, [], [])


def test_missing_record_and_missing_review_hash_never_match():
    assert not builder._reviewed("missing.yaml", None, None)
    assert not builder._reviewed("missing.yaml", None, "old-hash")
    assert not builder._reviewed("current.yaml", "new-hash", None)


def _byte_chain(owner, *hashes):
    return {"owner_chains": {owner: [
        {"sequence": index, "receipt_path": f"receipts/{index}.json",
         "receipt_sha256": hashlib.sha256(f"receipt{index}".encode()).hexdigest(),
         "before_sha256": before, "after_sha256": after}
        for index, (before, after) in enumerate(zip(hashes, hashes[1:], strict=False), 1)
    ]}}


@pytest.mark.parametrize("kind", ["identity", "role", "component", "component_disposition"])
def test_explicit_plan_withdrawal_requires_its_own_archived_bytes(kind):
    owner = "data/ingredients/mapped/GYPS.yaml"
    old_sha, middle_sha, current_sha = [hashlib.sha256(x).hexdigest() for x in (b"old", b"middle", b"current")]
    claim = {"role": "ELECTRON_DONOR", "metabolic_context": "reviewed isolate"}
    record = {"identifier": "CHEBI:fixture", "cellular_metabolic_roles": [claim]}
    item = {"source_path": owner, "source_record": owner, "after_sha256": old_sha,
            "after_record": record, "after": record, "source_position": "1",
            "after_assertion": claim, "current_record": owner,
            "current_record_sha256": old_sha, "finding_id": "fixture"}
    inputs = {"roles": [], "identity_support": {}, "component_plans": [], "component_dispositions": []}
    inputs[{"identity": "identity_support", "role": "roles", "component": "component_plans",
            "component_disposition": "component_dispositions"}[kind]] = {owner: item} if kind == "identity" else [item]
    chain = _byte_chain(owner, old_sha, middle_sha, current_sha)
    proofs = builder.validate_explicit_plans({owner: record}, {owner: current_sha}, **inputs, chain=chain)
    assert len(proofs) == 1 and proofs[0]["plan_kind"] == kind
    assert proofs[0]["reviewed_sha256"] == old_sha and len(proofs[0]["receipts"]) == 2
    assert builder.plan_superseded(proofs, kind, owner, old_sha)
    assert not builder.plan_superseded(proofs, kind, owner, middle_sha)
    assert not builder.identity_plan_supported(item, record, current_sha)
    assert not builder.role_supported(item, owner, record, current_sha, "1", claim)
    # Equal parsed records are insufficient; only the independently recorded pin
    # may start this chain. A hash that never appeared cannot withdraw the plan.
    broken = _byte_chain(owner, middle_sha, current_sha)
    with pytest.raises(ValueError):
        builder.validate_explicit_plans({owner: record}, {owner: current_sha}, **inputs, chain=broken)


def test_two_plan_kinds_for_one_owner_keep_distinct_reviewed_pins():
    owner = "data/ingredients/mapped/GYPS.yaml"
    first, second, current = [hashlib.sha256(x).hexdigest() for x in (b"first", b"second", b"current")]
    record = {"identifier": "CHEBI:fixture"}
    identity = {"after_record": record, "after_sha256": first}
    component = {"source_record": owner, "after": record, "after_sha256": second}
    proofs = builder.validate_explicit_plans({owner: record}, {owner: current}, [], {owner: identity},
                                            [component], [], chain=_byte_chain(owner, first, second, current))
    assert [(p["plan_kind"], p["reviewed_sha256"], len(p["receipts"])) for p in proofs] == [
        ("identity", first, 2), ("component", second, 1)]


@pytest.mark.parametrize("kind", ["identity", "role", "component"])
def test_equal_hash_inconsistent_payload_cannot_be_withdrawn(kind):
    owner = "data/ingredients/mapped/GYPS.yaml"
    digest = hashlib.sha256(b"same bytes").hexdigest()
    before, current = {"identifier": "CHEBI:old"}, {"identifier": "CHEBI:new"}
    item = {"source_path": owner, "source_record": owner, "after_sha256": digest,
            "after_record": before, "after": before, "source_position": "1",
            "after_assertion": {"role": "ELECTRON_DONOR"}}
    roles, identities, components = [], {}, []
    if kind == "identity":
        identities[owner] = item
    elif kind == "role":
        roles = [item]
    else:
        components = [item]
    with pytest.raises(ValueError, match="no longer describes"):
        builder.validate_explicit_plans({owner: current}, {owner: digest}, roles, identities, components, [],
                                       chain=_byte_chain(owner, digest, digest))


@pytest.fixture
def main_review(tmp_path, monkeypatch):
    """Run the real builder, native receipt replay and graph exporter on one owner.

    The unrelated fixed Aromatic hold is exercised by the full-gate hold tests;
    this fixture omits only that fixed corpus policy, not any approval path.
    """
    import csv
    import sys

    import yaml

    from mediaingredientmech.export.kgx import export_graph
    from mediaingredientmech.export.reviewed_sssom import _tsv, row_sha256
    from mediaingredientmech.validation import mapping_change_receipts as receipts
    from mediaingredientmech.validation import semantic_release as gate

    root = tmp_path
    base = root / "reports/semantic_review_20260921"
    here = base / "resolution"
    owner = "data/ingredients/mapped/GYPS.yaml"
    role = {"role": "ELECTRON_DONOR", "metabolic_context": "synthetic isolate only",
            "evidence": [{"reference_type": "PEER_REVIEWED_PUBLICATION", "doi": "10.1234/fixture"}]}
    record = {"identifier": "CHEBI:15377", "preferred_term": "GYPS", "mapping_status": "MAPPED",
              "ontology_mapping": {"ontology_id": "CHEBI:15377", "ontology_label": "water", "ontology_source": "CHEBI", "mapping_quality": "EXACT_MATCH"},
              "ingredient_type": "UNDEFINED_MIXTURE", "cellular_metabolic_roles": [role],
              "nutritional_roles": [{"role": "CARBON_SOURCE", "evidence": role["evidence"]}],
              "components": [{"component_name": "synthetic part", "reference_scope": "UNMAPPED"}],
              "component_assertion": {"method": "RECIPE_TRANSCRIPTION", "completeness": "PARTIAL", "evidence": [{"evidence_type": "RECIPE_SOURCE", "source": "https://example.test/fixture-recipe"}]},
              "environmental_context": [{"environment_term": "ENVO:00002149", "environment_label": "sea water", "relevance": "NATURAL_SOURCE"}]}
    record_template = record
    mapping = {"subject_id": "MIM:GYPS", "subject_label": "GYPS", "predicate_id": "skos:exactMatch",
               "object_id": "CHEBI:15377", "object_label": "water", "other": ""}

    def write(path, value):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value))

    def table(path, values):
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(values[0]), delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows(values)

    def run(*, stale, recovered=False, explicit_role=True, mapping_supported=False, overlap=None, finding_plan=None, broken_pin=None, role_overlap=False, reverse_roles=False, role_disposition_tamper=None, duplicate_identity_archive=None, reverse_identity_duplicates=False, conflicting_identity_duplicate=True):
        record = copy.deepcopy(record_template)
        if role_overlap:
            record["cellular_metabolic_roles"].append(dict(role, role="ELECTRON_ACCEPTOR", metabolic_context="second synthetic claim"))
        old_bytes = yaml.safe_dump(record).encode()
        old_sha = hashlib.sha256(old_bytes).hexdigest()
        (root / owner).parent.mkdir(parents=True, exist_ok=True)
        (root / owner).write_bytes(old_bytes + (b"# Later metadata curation; no new scientific review.\n" if stale else b""))
        current_sha = gate.sha(root / owner)
        (root / "data/ingredients/unmapped").mkdir(exist_ok=True)
        (root / "data/curated").mkdir(exist_ok=True)
        unknown = {"identifier": "UNMAPPED_0001", "preferred_term": "Unknown", "mapping_status": "UNMAPPED"}
        (root / "data/ingredients/unmapped/Unknown.yaml").write_text(yaml.safe_dump(unknown))
        for group, records in (("mapped", [record]), ("unmapped", [unknown])):
            (root / f"data/curated/{group}_ingredients.yaml").write_text(yaml.safe_dump({"ingredients": records}))
        source = root / receipts.SSSOM_SOURCE
        source.parent.mkdir(exist_ok=True)
        source.write_bytes(b"# mapping_set_id: https://example.test/builder\n# predicate_semantics: skos\n# curie_map:\n#   MIM: https://example.test/mim/\n#   CHEBI: http://purl.obolibrary.org/obo/CHEBI_\n#   ENVO: http://purl.obolibrary.org/obo/ENVO_\n" + _tsv(list(mapping), [mapping]))
        source_sha = gate.sha(source)
        for path, value in {
            receipts.BASELINE: {"schema_version": 1, "rows": [mapping], "source_sha256": source_sha},
            receipts.TRAIT_REFRESH: {"schema_version": 1, "before_sha256": source_sha, "after_sha256": source_sha, "row_count": 1, "changed_rows": 0, "changes": []},
            receipts.PARENT_REFRESH: {"schema_version": 1, "before_sha256": source_sha, "after_sha256": source_sha, "row_count": 1, "changed_rows": 0, "changes": []},
            receipts.RECEIPTS_DIR + "/fixture.json": {"schema_version": 1, "batch": "fixture", "sequence": 1, "approval": "NONE", "before_sha256": source_sha, "after_sha256": source_sha, "before_row_count": 1, "after_row_count": 1, "position_map": [1], "changed_rows": 0, "added_rows": 0, "removed_rows": 0, "changes": [], "records": [{"source_record": owner, "before_yaml_sha256": old_sha, "after_yaml_sha256": current_sha}]},
        }.items():
            write(root / path, value)
        bundle = root / "bundle"
        export_graph(root, bundle)
        edges = gate.rows(bundle / "mim_edges.tsv", kgx=True)
        edge_by_kind = {}
        for edge in edges:
            edge_by_kind.setdefault(edge["assertion_type"], edge)
        (root / "historical.md").write_text("Synthetic exact owner/claim scientific disposition.\n")
        history_sha = gate.sha(root / "historical.md")
        write(base / "manifest.json", {"inputs": {owner: old_sha}})
        table(base / "records.tsv", [{"source_record": owner, "record_sha256": old_sha, "review_report": "historical.md", "report_sha256": history_sha}])
        plan = {"source_path": owner, "destination_path": owner, "after_record": record, "after_sha256": old_sha}
        initial_plan = [] if recovered else [plan]
        recovered_plan = [plan] if recovered else []
        initial_sha = old_sha
        if overlap:
            initial_plan = [plan]
            initial_sha = current_sha if overlap == "initial_current" else old_sha
            recovered_plan = [dict(plan, after_sha256=current_sha if overlap == "recovered_current" else old_sha)]
        if broken_pin == "initial":
            initial_sha = hashlib.sha256(b"unbound initial pin").hexdigest()
        elif broken_pin == "recovered":
            recovered_plan[0] = dict(recovered_plan[0], after_sha256=hashlib.sha256(b"unbound recovered pin").hexdigest())
        if duplicate_identity_archive:
            repeated = copy.deepcopy(plan)
            if conflicting_identity_duplicate:
                repeated["after_record"]["preferred_term"] = "Conflicting historical identity label"
                repeated["after_sha256"] = "0" * 64
            duplicates = [repeated, plan]
            if reverse_identity_duplicates:
                duplicates.reverse()
            if duplicate_identity_archive == "initial":
                initial_plan = duplicates
            else:
                recovered_plan = duplicates
        write(base / "corrections/identity-plan.json", {"records": initial_plan})
        write(base / "corrections/current-review.json", {"record_inputs": {owner: initial_sha}})
        write(here / "identities/identity-plan.json", {"records": recovered_plan})
        role_plans = [{"source_path": owner, "before_sha256": old_sha, "before_assertion": role, "after_record": record, "after_sha256": old_sha, "source_position": "1", "after_assertion": role}] if explicit_role else []
        if role_overlap:
            second = record["cellular_metabolic_roles"][1]
            role_plans.append({"source_path": owner, "before_sha256": old_sha, "before_assertion": second, "after_record": record, "after_sha256": current_sha, "source_position": "2", "after_assertion": second})
        if reverse_roles:
            role_plans.reverse()
        write(here / "roles/cellular-role-plan.json", {"records": role_plans})
        write(here / "components/applied-changes.json", [{"source_record": owner, "after": record, "after_sha256": old_sha}])
        table(here / "components/dispositions.tsv", [{"finding_id": "SEM:component", "current_record": owner, "current_record_sha256": old_sha, "disposition": "SOURCE_SUPPORTED", "reason": "Exact synthetic preparation reviewed"}])
        role_edges = [edge for edge in edges if edge["assertion_type"] == "cellular_metabolic_roles"]
        role_dispositions = [{"before_edge_id": edge["id"], "source_record": owner, "record_before_sha256": old_sha,
                              "assertion_before_sha256": hashlib.sha256(edge["assertion_json"].encode()).hexdigest(),
                              "facet": "cellular_metabolic_roles", "source_position": str(int(edge["source_position"]) - 1),
                              "disposition": "SUPPORTED_IN_STATED_CONTEXT", "reason": "Exact synthetic role reviewed"}
                             for edge in role_edges]
        if role_disposition_tamper:
            field, value = role_disposition_tamper
            role_dispositions[0][field] = value
        table(here / "roles/role-dispositions.tsv", role_dispositions)
        table(base / "corrections/blocker_dispositions.tsv", [{"finding_id": "SEM:identity", "disposition": "IDENTITY_CORRECTED" if (finding_plan or ("recovered" if recovered else "initial")) == "initial" else "REQUIRES_RECOVERY", "reason": "Exact synthetic identity reviewed"}])
        table(base / "findings.tsv", [{"finding_id": "SEM:" + name, "source_record": owner, "record_scope": "active", "kind": kind, "severity": "major", "reason": "Historical synthetic finding", "affected_unit": edge_by_kind["cellular_metabolic_roles"]["id"] if name == "role" else name} for name, kind in (("identity", "recipe_identity"), ("component", "component_source_scope"), ("role", "role_evidence"))])
        if role_overlap:
            findings = gate.rows(base / "findings.tsv")
            findings.append(dict(findings[-1], finding_id="SEM:role2", affected_unit=role_edges[1]["id"]))
            table(base / "findings.tsv", findings)
        inherited = []
        role_reviews = []
        for kind in ("nutritional_roles", "environment"):
            edge = edge_by_kind[kind]
            payload_sha = hashlib.sha256(edge["assertion_json"].encode()).hexdigest()
            inherited.append({"source_record": owner, "record_sha256": old_sha, "assertion_type": kind, "assertion_sha256": payload_sha, "edge_id": edge["id"], "verdict": "pass", "review_report": "historical.md"})
            if kind.endswith("_roles"):
                role_reviews.append({"source_record": owner, "source_record_sha256": old_sha, "assertion_type": kind, "assertion_sha256": payload_sha, "edge_id": edge["id"], "source_position": "1", "historical_review_path": "historical.md", "historical_review_sha256": history_sha, "review_reason": "Synthetic role-specific primary study review", "disposition": "ELIGIBLE_PRIMARY_STUDY"})
        table(base / "kgx_assertions.tsv", inherited)
        write(here / "roles/inherited-role-review.json", {"entries": role_reviews})
        write(here / "release-holds.json", {"resolutions": []})
        disposition = "SUPPORTED" if mapping_supported else "WITHHOLD"
        decision = {"source_position": 1, "row_sha256": row_sha256(mapping), "owner_record": owner, "disposition": disposition, "review_reason": "Independent current mapping-only fixture review", "review_evidence": "mapping-evidence.json", "evidence_key": "fixture"}
        write(root / "mapping-evidence.json", {"entries": {"fixture": {**{key: decision[key] for key in ("row_sha256", "disposition", "review_reason")}, "owner_record_sha256": current_sha}}})
        write(root / "reports/sssom_completion_20260921/review.json", {"schema_version": 1, "source_sssom": receipts.SSSOM_SOURCE, "source_sha256": source_sha, "record_inputs": {owner: current_sha}, "inputs": {"mapping-evidence.json": gate.sha(root / "mapping-evidence.json")}, "decisions": [decision]})
        for relative_path in ("src/mediaingredientmech/validation/semantic_release.py", "src/mediaingredientmech/validation/mapping_change_receipts.py", "src/mediaingredientmech/record_refresh.py", str(PATH.relative_to(PATH.parents[3]))):
            target = root / relative_path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((PATH.parents[3] / relative_path).read_bytes())
        monkeypatch.setattr(builder, "ROOT", root)
        monkeypatch.setattr(builder, "BASE", base)
        monkeypatch.setattr(builder, "HERE", here)
        monkeypatch.setattr(builder, "__file__", str(here / "build_review.py"))
        monkeypatch.setattr(builder, "apply_release_holds", lambda *args, **kwargs: None)
        monkeypatch.setattr(sys, "argv", [str(here / "build_review.py"), "--bundle", str(bundle)])
        builder.main()
        return json.loads((here / "current-review.json").read_text()), gate.rows(here / "finding-dispositions.tsv"), gate.rows(here / "assertion-dispositions.tsv")

    return run


@pytest.mark.parametrize("recovered", [False, True])
@pytest.mark.parametrize("stale", [False, True])
def test_main_withdraws_exact_plans_without_reapproving_roles_or_components(main_review, recovered, stale):
    report, findings, assertions = main_review(stale=stale, recovered=recovered, mapping_supported=True)
    assert {row["resolution_status"] for row in findings} == ({"OPEN"} if stale else {"RESOLVED"})
    by_kind = {row["assertion_type"]: row for row in assertions}
    assert by_kind["mapping"]["resolution_status"] == "APPROVED"
    for kind in ("component", "cellular_metabolic_roles", "nutritional_roles", "environment"):
        assert by_kind[kind]["resolution_status"] == ("OPEN" if stale else "APPROVED")
    assert {proof["plan_kind"] for proof in report["superseded_plans"]} == ({"identity", "role", "component", "component_disposition"} if stale else set())


def test_main_current_mapping_withhold_overrides_archived_positive_identity(main_review):
    _, _, assertions = main_review(stale=False, mapping_supported=False)
    assert next(row for row in assertions if row["assertion_type"] == "mapping")["resolution_status"] == "OPEN"


@pytest.mark.parametrize("current_pin", ["initial", "recovered"])
@pytest.mark.parametrize("finding_plan", ["initial", "recovered"])
def test_main_overlapping_identity_plans_keep_each_archived_pin(main_review, current_pin, finding_plan):
    report, findings, assertions = main_review(
        stale=True, mapping_supported=True, overlap=current_pin + "_current", finding_plan=finding_plan,
    )
    identity = next(row for row in findings if row["finding_id"] == "SEM:identity")
    assert identity["resolution_status"] == ("RESOLVED" if finding_plan == current_pin else "OPEN")
    evidence = {"initial": "reports/semantic_review_20260921/corrections/identity-plan.json",
                "recovered": "reports/semantic_review_20260921/resolution/identities/identity-plan.json"}
    assert identity["resolution_evidence"] == (evidence[finding_plan] if finding_plan == current_pin else "")
    superseded = [pin for pin in report["superseded_plans"] if pin["plan_kind"] == "identity"]
    assert len(superseded) == 1
    assert superseded[0]["plan_evidence"] == evidence["recovered" if current_pin == "initial" else "initial"]
    assert superseded[0]["reviewed_sha256"] != superseded[0]["current_sha256"]
    assert next(row for row in assertions if row["assertion_type"] == "mapping")["resolution_status"] == "APPROVED"
    assert {row["resolution_status"] for row in assertions if row["assertion_type"] != "mapping"} == {"OPEN"}


@pytest.mark.parametrize("broken_pin", ["initial", "recovered"])
def test_main_current_identity_pin_cannot_hide_an_unbound_other_plan(main_review, broken_pin):
    current_pin = "recovered" if broken_pin == "initial" else "initial"
    with pytest.raises(ValueError, match="Identity plan no longer describes"):
        main_review(stale=True, mapping_supported=True, overlap=current_pin + "_current", broken_pin=broken_pin)


@pytest.mark.parametrize("reverse_roles", [False, True])
def test_main_distinct_role_pins_bind_their_own_claim_and_finding(main_review, reverse_roles):
    report, findings, assertions = main_review(stale=True, mapping_supported=True, role_overlap=True, reverse_roles=reverse_roles)
    statuses = {row["finding_id"]: row["resolution_status"] for row in findings}
    assert statuses["SEM:role"] == "OPEN"
    assert statuses["SEM:role2"] == "RESOLVED"
    roles = {row["source_position"]: row["resolution_status"] for row in assertions if row["assertion_type"] == "cellular_metabolic_roles"}
    assert roles == {"1": "OPEN", "2": "APPROVED"}
    pins = [pin for pin in report["superseded_plans"] if pin["plan_kind"] == "role"]
    assert len(pins) == 1 and pins[0]["source_position"] == "1"
    assert len(pins[0]["assertion_sha256"]) == 64


@pytest.mark.parametrize("field,value", [
    ("source_record", "data/ingredients/mapped/Other.yaml"),
    ("source_position", "2"),
    ("record_before_sha256", "0" * 64),
    ("assertion_before_sha256", "0" * 64),
    ("facet", "nutritional_roles"),
])
def test_main_role_disposition_cannot_borrow_another_plan(main_review, field, value):
    with pytest.raises(ValueError, match="exactly one archived role plan"):
        main_review(stale=True, role_overlap=True, role_disposition_tamper=(field, value))


@pytest.mark.parametrize("archive", ["initial", "recovered"])
@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("conflicting", [False, True])
def test_main_rejects_duplicate_identity_owner_before_projection(main_review, archive, reverse, conflicting):
    with pytest.raises(ValueError, match=f"Duplicate destination owner in {archive} identity archive"):
        main_review(stale=False, mapping_supported=True, duplicate_identity_archive=archive,
                    reverse_identity_duplicates=reverse, conflicting_identity_duplicate=conflicting)
