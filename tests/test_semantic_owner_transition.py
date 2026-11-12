"""#1387/#1392: native owner transitions, pinned reviews, unchanged-source attacks."""

from __future__ import annotations

import copy
from pathlib import Path

import pytest
import yaml

from mediaingredientmech.curate import curation_successor as successor
from mediaingredientmech.curate import stable_id_adoption as adoption
from mediaingredientmech.validation.semantic_owner_transition import LEDGERS, verify_owner_steps
from tests.test_curation_successor_publication import corrected
from tests.test_stable_id_adoption import ROOT


def pin(path, root):
    return {"path": str(path.relative_to(root)), "sha256": adoption.sha(path.read_bytes())}


@pytest.fixture(scope="module")
def native_transition(tmp_path_factory):
    """Produce once through real native writers; all adversarial cases use copies."""
    tmp = tmp_path_factory.mktemp("native-owner-transition")
    with pytest.MonkeyPatch.context() as patch:
        fixture, _ = corrected(tmp, patch)
    steps, captured = [], {}

    def store(root, ref, raw=None):
        raw = (Path(root) / ref["path"]).read_bytes() if raw is None else raw
        assert adoption.sha(raw) == ref["sha256"]
        key = (str(root), ref["path"], ref["sha256"])
        assert key not in captured or captured[key] == raw
        captured[key] = raw
        return raw

    for kind, root, stage, receipt in [
        (
            "adoption",
            fixture.predecessor,
            fixture.original.stage,
            fixture.original.receipt / "application.json",
        ),
        (
            "curation",
            fixture.target,
            fixture.target / ".temp/correction-stage",
            fixture.target / ".temp/source-correction-application/application.json",
        ),
    ]:
        manifest_ref = pin(stage / "manifest.json", root)
        manifest = adoption.document(store(root, manifest_ref))
        receipt_ref = pin(receipt, root)
        application = adoption.document(store(root, receipt_ref))
        request_ref = manifest["request"]
        request = adoption.document(store(root, request_ref))
        step = {
            "kind": kind,
            "root": str(root),
            "receipt": receipt_ref,
            "manifest": manifest_ref,
            "request": request_ref,
            "afterimages": {},
        }
        for name, ref in application["beforeimages"].items():
            if ref is not None:
                raw = store(root, ref)
                store(root, {"path": name, "sha256": adoption.sha(raw)}, raw)
        for name, sha in manifest["outputs"].items():
            ref = {"path": str((stage / "candidate" / name).relative_to(root)), "sha256": sha}
            raw = store(root, ref)
            store(root, {"path": name, "sha256": sha}, raw)
            step["afterimages"][name] = ref
        for name, sha in manifest["inputs"].items():
            key = (str(root), name, sha)
            if key not in captured:
                store(root, {"path": name, "sha256": sha})
        for ref in application["retired_sources"].values():
            store(root, ref)
        store(root, application["acceptance"])
        if kind == "adoption":
            for name, sha in manifest["legacy_inputs"].items():
                store(request["legacy"]["root"], {"path": name, "sha256": sha})
        else:
            for specification in request["predecessor"]["historical_reviews"]:
                history_root = specification["identity"]["root"]
                store(history_root, specification["review"])
                store(
                    history_root,
                    {
                        "path": str(Path(specification["review"]["path"]).with_name("review.md")),
                        "sha256": specification["markdown_sha256"],
                    },
                )
        steps.append(step)
    first = adoption.document(
        captured[(steps[0]["root"], steps[0]["receipt"]["path"], steps[0]["receipt"]["sha256"])]
    )
    baseline = {
        name: captured[(steps[0]["root"], ref["path"], ref["sha256"])]
        for name, ref in first["beforeimages"].items()
    }
    current_owners = {
        str(p.relative_to(fixture.target)): p.read_bytes()
        for p in fixture.target.glob("data/ingredients/*/*.yaml")
    }
    return {
        "steps": steps,
        "captured": captured,
        "baseline_owners": {
            n: raw for n, raw in baseline.items() if n.startswith("data/ingredients/")
        },
        "baseline_ledgers": {n: baseline[n] for n in LEDGERS},
        "current_owners": current_owners,
        "current_ledgers": {n: (fixture.target / n).read_bytes() for n in LEDGERS},
        # Genuine same-repository Git ancestry for the original native reports.
        "schema_root": fixture.target,
    }


@pytest.fixture
def transition(native_transition):
    return copy.deepcopy(native_transition)


def run(case, reader=None):
    captured = case["captured"]

    def read(root, ref):
        return captured[(root, ref["path"], ref["sha256"])]

    return verify_owner_steps(
        case["steps"],
        reader or read,
        case["baseline_owners"],
        case["baseline_ledgers"],
        case["current_owners"],
        case["current_ledgers"],
        case["schema_root"],
    )


def document(case, step, name):
    ref = step[name]
    return adoption.document(case["captured"][(step["root"], ref["path"], ref["sha256"])])


def replace(case, root, ref, raw):
    result = {"path": ref["path"], "sha256": adoption.sha(raw)}
    case["captured"][(root, result["path"], result["sha256"])] = raw
    return result


def rebind(case, step, *, request=None, manifest=None, receipt=None):
    """Rehash all immediate containers so negatives test semantics, not stale pins."""
    manifest = document(case, step, "manifest") if manifest is None else manifest
    receipt = document(case, step, "receipt") if receipt is None else receipt
    if request is not None:
        step["request"] = replace(case, step["root"], step["request"], adoption.encoded(request))
        manifest["request"] = step["request"]
        manifest["inputs"][step["request"]["path"]] = step["request"]["sha256"]
    step["manifest"] = replace(case, step["root"], step["manifest"], adoption.encoded(manifest))
    receipt["manifest"] = step["manifest"]
    step["receipt"] = replace(case, step["root"], step["receipt"], adoption.encoded(receipt))


def rebind_correction(case, request, manifest=None):
    """Keep outer native marker/event links coherent while attacking original science."""
    step = case["steps"][-1]
    rebind(case, step, request=request, manifest=manifest)
    manifest, receipt = (document(case, step, name) for name in ("manifest", "receipt"))
    name = successor.MARKER
    reference = step["afterimages"][name]
    marker = adoption.document(
        case["captured"][(step["root"], reference["path"], reference["sha256"])]
    )
    marker["request"] = step["request"]
    raw = adoption.encoded(marker)
    step["afterimages"][name] = replace(case, step["root"], reference, raw)
    manifest["outputs"][name] = receipt["outputs"][name] = adoption.sha(raw)
    for event in receipt["completed_operations"]:
        if event.get("path") == name:
            event["sha256"] = adoption.sha(raw)
    rebind(case, step, manifest=manifest, receipt=receipt)


@pytest.mark.parametrize("role", ["primary", "skeptic"])
def test_1392_corrective_pair_cannot_be_removed_behind_coherent_marker(transition, role):
    step = transition["steps"][-1]
    request = document(transition, step, "request")
    assert request["operations"][0][role]
    request["operations"][0][role] = None
    rebind_correction(transition, request)
    with pytest.raises(ValueError, match="unassessed correction cannot prepare"):
        run(transition)


@pytest.mark.parametrize("part", ["context", "payloads"])
def test_1392_corrective_inspection_cannot_be_replaced_by_a_rehash(transition, part):
    step = transition["steps"][-1]
    request, manifest = (document(transition, step, name) for name in ("request", "manifest"))
    reference = request[part]
    value = adoption.document(
        transition["captured"][(step["root"], reference["path"], reference["sha256"])]
    )
    if part == "context":
        value["historical_obligations"] = []
    else:
        value[0]["before"]["preferred_term"] = "Unreviewed historical identity"
    request[part] = replace(transition, step["root"], reference, adoption.encoded(value))
    manifest["inputs"][reference["path"]] = request[part]["sha256"]
    rebind_correction(transition, request, manifest)
    with pytest.raises(ValueError, match="actual inspected context/payloads required"):
        run(transition)


@pytest.mark.parametrize(
    "attack,reason",
    [
        ("holds", "explicit exact corrective scope/identity/holds"),
        ("findings", "unresolved corrective finding"),
        ("scope", "explicit exact corrective scope/identity/holds"),
        ("target", "scientific target differs"),
        ("input", "scientific review omits current proposal"),
        ("git", "invalid native review provenance"),
        ("evidence", "captured primary corrective evidence"),
        ("independence", "separate independent skeptical correction review"),
    ],
)
def test_1392_native_corrective_pair_retains_exact_science_and_holds(transition, attack, reason):
    step = transition["steps"][-1]
    request, manifest = (document(transition, step, name) for name in ("request", "manifest"))
    operation = request["operations"][0]
    reference = operation["primary"]
    report = adoption.load_yaml(
        transition["captured"][(step["root"], reference["path"], reference["sha256"])]
    )
    dimensions = {item["name"]: item for item in report["assessments"][0]["dimensions"]}
    if attack == "holds":
        dimensions["residual_holds_json"]["value"] = '[{"issue_key":"unreviewed-hold"}]'
    elif attack == "findings":
        dimensions["residual_findings_json"]["value"] = '[{"issue_key":"unreviewed-finding"}]'
    elif attack == "scope":
        dimensions["curation_action"]["value"] = "approve_release"
    elif attack == "target":
        report["targets"][0]["semantic_digest"]["sha256"] = "0" * 64
    elif attack == "input":
        report["source"]["inputs"] = [
            entry
            for entry in report["source"]["inputs"]
            if entry["path"] != operation["before"]["path"]
        ]
    elif attack == "git":
        report["source"]["git_revision"] = "0" * 40
    elif attack == "evidence":
        report["evidence"][0]["snapshot_sha256"] = "0" * 64
    else:
        skeptical = operation["skeptic"]
        other = adoption.load_yaml(
            transition["captured"][(step["root"], skeptical["path"], skeptical["sha256"])]
        )
        report["reviewer"]["identity"] = other["reviewer"]["identity"]
    parser = successor._CAPTURE.script("scripts/record_review.py")
    raw = yaml.safe_dump(report, sort_keys=False).encode()
    markdown = parser.render_markdown(
        report, transition["schema_root"] / "schema/record_review.yaml"
    ).encode()
    md_path = str(Path(reference["path"]).with_name("review.md"))
    reference["sha256"] = adoption.sha(raw)
    reference["markdown_sha256"] = adoption.sha(markdown)
    for name, content in ((reference["path"], raw), (md_path, markdown)):
        digest = adoption.sha(content)
        transition["captured"][(step["root"], name, digest)] = content
        request["review_inputs"][name] = manifest["inputs"][name] = digest
    rebind_correction(transition, request, manifest)
    with pytest.raises(ValueError, match=reason):
        run(transition)


def test_1392_coherent_corrective_hold_change_cannot_inherit_original_pair(transition):
    """#1392: equal hold lists and a rehashed payload still need current review."""
    step = transition["steps"][-1]
    request, manifest = (document(transition, step, name) for name in ("request", "manifest"))
    operation = request["operations"][0]
    original_pair = copy.deepcopy({role: operation[role] for role in ("primary", "skeptic")})
    original_owners = dict(transition["current_owners"])
    holds = [{"issue_key": "synthetic-retained-hold", "reason": "Unreviewed source restriction"}]
    assert operation["inherited_holds"] == operation["residual_holds"] == []
    operation["inherited_holds"] = copy.deepcopy(holds)
    operation["residual_holds"] = copy.deepcopy(holds)
    reference = request["payloads"]
    payloads = adoption.document(
        transition["captured"][(step["root"], reference["path"], reference["sha256"])]
    )
    payload = next(item for item in payloads if item["mim_id"] == operation["mim_id"])
    payload["inherited_holds"] = copy.deepcopy(holds)
    payload["residual_holds"] = copy.deepcopy(holds)
    request["payloads"] = replace(transition, step["root"], reference, adoption.encoded(payloads))
    manifest["inputs"][reference["path"]] = request["payloads"]["sha256"]
    rebind_correction(transition, request, manifest)
    assert {role: operation[role] for role in ("primary", "skeptic")} == original_pair
    assert transition["current_owners"] == original_owners
    with pytest.raises(ValueError, match="original corrective review input closure differs"):
        run(transition)


def test_real_native_adoption_and_curation_semantic_continuity(transition):
    result = run(transition)
    assert result["owners"] == transition["current_owners"]
    assert result["ledgers"] == transition["current_ledgers"]
    assert len(result["operations"]) == 1
    assert (
        result["operations"][0]["delta"]["ontology_mapping"]["after"]["mapping_quality"]
        == "MANUAL_CURATION"
    )
    assert result["scientific_approval_added"] is False
    assert result["scope"] == "semantic_reconstruction_only"
    assert len(result["retained_contexts"]) == 2
    assert any(
        d["disposition"] == "WITHHOLD_IDENTITY" for d in result["retained_contexts"][0]["decisions"]
    )
    assert result["predecessor_owners"] != result["owners"]


@pytest.mark.parametrize("attack", ["owner_missing", "owner_changed", "ledger_changed"])
def test_current_endpoint_must_equal_reconstructed_bytes(transition, attack):
    if attack == "owner_missing":
        transition["current_owners"].pop(next(iter(transition["current_owners"])))
    elif attack == "owner_changed":
        name = next(iter(transition["current_owners"]))
        transition["current_owners"][name] += b"\n"
    else:
        transition["current_ledgers"][LEDGERS[0]] += b"\n"
    with pytest.raises(ValueError, match="current owner/ledger endpoint differs"):
        run(transition)


def test_missing_staged_owner_is_not_hidden_by_present_current_file(transition):
    step = transition["steps"][-1]
    name = next(n for n in step["afterimages"] if n.startswith("data/ingredients/"))
    assert name in transition["current_owners"]
    del step["afterimages"][name]
    with pytest.raises(ValueError, match="incomplete staged output set"):
        run(transition)


def test_equivalent_bytes_at_an_unrelated_path_are_not_native_afterimages(transition):
    step = transition["steps"][-1]
    name = next(iter(step["afterimages"]))
    step["afterimages"][name] = {**step["afterimages"][name], "path": "invented/candidate.yaml"}
    with pytest.raises(ValueError, match="afterimage is not the native staged output"):
        run(transition)


@pytest.mark.parametrize("attack", ["delta", "hold", "event_order"])
def test_rehashed_curation_cannot_forge_delta_or_retire_holds(transition, attack):
    step = transition["steps"][-1]
    request = document(transition, step, "request")
    if attack == "delta":
        request["operations"][0]["delta"] = {}
        rebind(transition, step, request=request)
        expected = "declared complete field delta differs"
    elif attack == "hold":
        request["operations"][0]["inherited_holds"] = [{"issue_key": "synthetic-retained-hold"}]
        rebind(transition, step, request=request)
        expected = "hold retirement is outside successor"
    else:
        receipt = document(transition, step, "receipt")
        receipt["completed_operations"].reverse()
        rebind(transition, step, receipt=receipt)
        expected = "native completed operation order differs"
    with pytest.raises(ValueError, match=expected):
        run(transition)


def test_rehashed_adoption_assignment_cannot_retarget_a_permanent_id(transition):
    step = transition["steps"][0]
    manifest = document(transition, step, "manifest")
    name = next(iter(manifest["assignments"]))
    manifest["assignments"][name] = "MIM:9999999"
    rebind(transition, step, manifest=manifest)
    with pytest.raises(ValueError, match="explicit mint assignments differ"):
        run(transition)


def test_rehashed_adoption_cannot_drop_a_retired_move_archive(transition):
    step = transition["steps"][0]
    receipt = document(transition, step, "receipt")
    assert receipt["retired_sources"]
    receipt["retired_sources"].clear()
    rebind(transition, step, receipt=receipt)
    with pytest.raises(ValueError, match="declared owner moves/retirements differ"):
        run(transition)


def test_rehashed_adoption_cannot_remove_a_source_case(transition):
    step = transition["steps"][0]
    manifest = document(transition, step, "manifest")
    manifest["source_cases"].pop()
    rebind(transition, step, manifest=manifest)
    with pytest.raises(ValueError, match="adoption decisions/source cases differ"):
        run(transition)


@pytest.mark.parametrize(
    "attack,expected",
    [
        ("history", "curation history must preserve exact prefix"),
        ("identity", "permanent identity changed"),
    ],
)
def test_declared_rehashed_source_delta_cannot_rewrite_history_or_identity(
    transition, attack, expected
):
    step = transition["steps"][-1]
    request = document(transition, step, "request")
    manifest = document(transition, step, "manifest")
    receipt = document(transition, step, "receipt")
    op = request["operations"][0]
    before = adoption.load_yaml(
        transition["captured"][(step["root"], op["before"]["path"], op["before"]["sha256"])]
    )
    after = adoption.load_yaml(
        transition["captured"][(step["root"], op["proposal"]["path"], op["proposal"]["sha256"])]
    )
    if attack == "history":
        after["curation_history"][0]["changes"] = "Rewritten original event"
    else:
        after["mim_id"] = "MIM:9999999"
    raw = yaml.safe_dump(after, sort_keys=False).encode()
    op["proposal"] = replace(transition, step["root"], op["proposal"], raw)
    op["delta"] = successor._delta(before, after)
    manifest["inputs"][op["proposal"]["path"]] = op["proposal"]["sha256"]
    name = op["after_path"]
    staged = adoption.serialized(after, ROOT / adoption.SCHEMA)
    step["afterimages"][name] = replace(transition, step["root"], step["afterimages"][name], staged)
    manifest["outputs"][name] = manifest["after_inventory"][name] = adoption.sha(staged)
    receipt["outputs"][name] = adoption.sha(staged)
    for event in receipt["completed_operations"]:
        if event.get("path") == name:
            event["sha256"] = adoption.sha(staged)
    transition["current_owners"][name] = staged
    rebind(transition, step, request=request, manifest=manifest, receipt=receipt)
    with pytest.raises(ValueError, match=expected):
        run(transition)


@pytest.mark.parametrize("name", LEDGERS)
def test_rehashed_adoption_cannot_rewrite_registry_or_lifecycle(transition, name):
    step = transition["steps"][0]
    manifest = document(transition, step, "manifest")
    receipt = document(transition, step, "receipt")
    ref = step["afterimages"][name]
    raw = transition["captured"][(step["root"], ref["path"], ref["sha256"])]
    changed = (
        raw.replace(b"Exact", b"Rewritten original mint")
        if name == LEDGERS[0]
        else raw + b"MIM:0000001\tdeprecated\t\t2026-01-02\tUnreviewed retirement\n"
    )
    assert changed != raw
    step["afterimages"][name] = replace(transition, step["root"], ref, changed)
    manifest["outputs"][name] = receipt["expected_outputs"][name] = adoption.sha(changed)
    rebind(transition, step, manifest=manifest, receipt=receipt)
    with pytest.raises(ValueError, match="registry prefix/lifecycle changed"):
        run(transition)


def test_manifest_reordering_does_not_authorize_another_native_event_order(transition):
    step = transition["steps"][0]
    manifest = document(transition, step, "manifest")
    receipt = document(transition, step, "receipt")
    manifest["outputs"] = dict(reversed(list(manifest["outputs"].items())))
    owners = [
        event
        for event in receipt["completed_operations"]
        if event["kind"] == "write" and event["path"].startswith("data/ingredients/")
    ]
    assert len(owners) > 1
    others = [event for event in receipt["completed_operations"] if event not in owners]
    receipt["completed_operations"] = list(reversed(owners)) + others
    rebind(transition, step, manifest=manifest, receipt=receipt)
    with pytest.raises(ValueError, match="native completed operation order differs"):
        run(transition)


def test_late_captured_evidence_drift_fails(transition):
    first = transition["steps"][0]
    key = (first["root"], first["receipt"]["path"], first["receipt"]["sha256"])
    calls = 0

    def read(root, ref):
        nonlocal calls
        selected = (root, ref["path"], ref["sha256"])
        raw = transition["captured"][selected]
        if selected == key:
            calls += 1
            if calls > 1:
                return raw + b"\n"
        return raw

    with pytest.raises(ValueError, match="late captured evidence drift"):
        run(transition, reader=read)


@pytest.mark.parametrize("attack", ["withhold_to_bind", "erase_other_hold"])
def test_1392_original_native_pair_must_agree_with_retained_hold_decisions(transition, attack):
    step = transition["steps"][0]
    request = document(transition, step, "request")
    manifest = document(transition, step, "manifest")
    unchanged_owners = copy.deepcopy(transition["current_owners"])
    if attack == "withhold_to_bind":
        decision = next(d for d in request["decisions"] if d["disposition"] == "WITHHOLD_IDENTITY")
        assert decision["identity_holds"]
        decision.update(
            disposition="BIND_EXISTING_CONCEPT_ONLY",
            existing_mim_id="MIM:0000001",
            identity_holds=[],
        )
        expected = "explicit current concept decision required"
    else:
        decision = next(d for d in request["decisions"] if d["other_holds"])
        decision["other_holds"] = []
        expected = "explicit residual hold classification"
    # The genuine old report pairs and their pins are deliberately unchanged.
    manifest["decisions"] = copy.deepcopy(request["decisions"])
    rebind(transition, step, request=request, manifest=manifest)
    assert transition["current_owners"] == unchanged_owners
    with pytest.raises(ValueError, match=expected):
        run(transition)


def captured_document(case, root, ref):
    return adoption.document(case["captured"][(root, ref["path"], ref["sha256"])])


@pytest.mark.parametrize("rebind_plan", [False, True])
def test_1392_unselected_source_owner_cannot_change_behind_original_operations(
    transition, rebind_plan
):
    step = transition["steps"][0]
    root = step["root"]
    request = document(transition, step, "request")
    manifest = document(transition, step, "manifest")
    legacy = request["legacy"]
    legacy_root = legacy["root"]
    application = captured_document(transition, legacy_root, legacy["application"])
    plan = captured_document(transition, legacy_root, legacy["plan"])
    old_operations = copy.deepcopy(plan["records"])
    selected = {op["source_record"] for op in plan["records"]}
    name = next(n for n in application["after_inventory"] if n not in selected)
    ref = {"path": name, "sha256": application["after_inventory"][name]}
    record = adoption.load_yaml(transition["captured"][(legacy_root, name, ref["sha256"])])
    record["preferred_term"] = "Unselected scientific label change"
    new = replace(transition, legacy_root, ref, yaml.safe_dump(record, sort_keys=False).encode())
    application["after_inventory"][name] = new["sha256"]
    manifest["legacy_inputs"][name] = new["sha256"]
    if rebind_plan:
        inventory = captured_document(transition, legacy_root, plan["after_inventory"])
        inventory["owners"][name] = new["sha256"]
        plan["after_inventory"] = replace(
            transition, legacy_root, plan["after_inventory"], adoption.encoded(inventory)
        )
        manifest["legacy_inputs"][plan["after_inventory"]["path"]] = plan["after_inventory"][
            "sha256"
        ]
        legacy["plan"] = replace(transition, legacy_root, legacy["plan"], adoption.encoded(plan))
        manifest["legacy_inputs"][legacy["plan"]["path"]] = legacy["plan"]["sha256"]
        application["plan"] = legacy["plan"]
        acceptance = captured_document(transition, legacy_root, application["acceptance"])
        acceptance["plan_sha256"] = legacy["plan"]["sha256"]
        application["acceptance"] = replace(
            transition, legacy_root, application["acceptance"], adoption.encoded(acceptance)
        )
        manifest["legacy_inputs"][application["acceptance"]["path"]] = application["acceptance"][
            "sha256"
        ]
    legacy["application"] = replace(
        transition, legacy_root, legacy["application"], adoption.encoded(application)
    )
    manifest["legacy_inputs"][legacy["application"]["path"]] = legacy["application"]["sha256"]
    context = captured_document(transition, root, request["context"])
    context.update(
        legacy_inventory=application["after_inventory"],
        legacy_application=legacy["application"],
        legacy_plan=plan,
    )
    request["context"] = replace(transition, root, request["context"], adoption.encoded(context))
    manifest["inputs"][request["context"]["path"]] = request["context"]["sha256"]
    rebind(transition, step, request=request, manifest=manifest)
    assert plan["records"] == old_operations
    expected = (
        "unselected legacy owner changed"
        if rebind_plan
        else "legacy plan/application inventories differ"
    )
    with pytest.raises(ValueError, match=expected):
        run(transition)


def test_1392_rehashed_original_review_requires_real_git_commit_authority(transition):
    step = transition["steps"][0]
    request = document(transition, step, "request")
    manifest = document(transition, step, "manifest")
    reference = request["decisions"][0]["primary"]
    path = reference["path"]
    report = adoption.load_yaml(
        transition["captured"][(step["root"], path, request["review_inputs"][path])]
    )
    report["source"]["git_revision"] = "0" * 40
    script = adoption._CAPTURE.script("scripts/record_review.py")
    markdown = script.render_markdown(
        report, transition["schema_root"] / "schema/record_review.yaml"
    ).encode()
    for name, raw in [
        (path, yaml.safe_dump(report, sort_keys=False).encode()),
        (str(Path(path).with_name("review.md")), markdown),
    ]:
        ref = replace(
            transition, step["root"], {"path": name, "sha256": request["review_inputs"][name]}, raw
        )
        manifest["inputs"][name] = request["review_inputs"][name] = ref["sha256"]
    rebind(transition, step, request=request, manifest=manifest)
    with pytest.raises(ValueError, match="invalid native provenance"):
        run(transition)
