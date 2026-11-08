"""#1174 closed projection/native receipt and publication boundary regressions.

The owner writer and external producer have separate native integration tests.
These fixtures isolate those two inputs while exercising actual canonical
projection, policy reconstruction, native maker/replay, and filesystem writes.
"""

import copy
import csv
import io
import importlib.util
import json
import os
from pathlib import Path

import pytest

from mediaingredientmech import campaign_publication as c
from mediaingredientmech.validation import mapping_change_receipts as native

ROOT = Path(__file__).resolve().parents[1]


def put(root, name, value):
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(value if isinstance(value, bytes) else c.encoded(value))
    return path


def row(name, target=None, **extra):
    return {
        "subject_id": "MIM:" + name,
        "subject_label": name,
        "predicate_id": "skos:exactMatch",
        "object_id": target or "CHEBI:1",
        "object_label": name,
        "object_source": "CHEBI",
        "mapping_justification": "semapv:ManualMappingCuration",
        "source": "historic",
        "mapping_date": "2026-10-01",
        "confidence": "0.9",
        "comment": "retained",
        "other": "",
        "validation_method": "old stamp",
    } | extra


def sssom(rows):
    out = io.StringIO()
    out.write(
        "# mapping_set_id: https://example.org/fixture\n# predicate_semantics: skos\n"
        "# mapping_date: 2026-10-01\n# mapping_set_version: 2026-10-01\n"
    )
    writer = csv.DictWriter(out, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue().encode()


def history(root, before):
    rows = c.table(before)[2]
    put(root, native.BASELINE, {"schema_version": 1, "source_sha256": c.sha(before), "rows": rows})
    for path in (native.TRAIT_REFRESH, native.PARENT_REFRESH):
        put(
            root,
            path,
            {
                "schema_version": 1,
                "before_sha256": c.sha(before),
                "after_sha256": c.sha(before),
                "row_count": len(rows),
                "changed_rows": 0,
                "changes": [],
            },
        )
    (root / native.RECEIPTS_DIR).mkdir(parents=True, exist_ok=True)


def inventory(root):
    return {
        p.relative_to(root).as_posix(): c.sha(p.read_bytes())
        for bucket in ("mapped", "unmapped")
        for p in sorted((root / "data/ingredients" / bucket).glob("*.yaml"))
    }


@pytest.fixture
def case(tmp_path, monkeypatch):
    root = tmp_path / "repository"
    root.mkdir()
    before = sssom([row("A"), row("Unrelated", "CHEBI:9")])
    candidate = sssom(
        [
            row(
                "A",
                other="reviewed alias",
                source="native",
                comment="",
                confidence="0.8",
                mapping_date="2026-11-08",
            ),
            row("B", "CHEBI:2", mapping_date="2026-11-08"),
            row("P", "CHEBI:3", mapping_date="2026-11-08"),
            row("Unrelated", "CHEBI:999", source="unrelated native drift"),
        ]
    )
    sidecar = b"subject_id\ttoken_key\ttoken\towner_subject_ids\tdisposition\tinput_surfaces\tsource_refs\tevidence_refs\n"
    baseline = b"subject_id\ttoken_key\n"
    owner_paths = [
        "data/ingredients/mapped/A.yaml",
        "data/ingredients/mapped/B.yaml",
        "data/ingredients/unmapped/C.yaml",
        "data/ingredients/mapped/P.yaml",
    ]
    for p in owner_paths:
        put(root, p, ("identifier: CHEBI:1\npreferred_term: " + Path(p).stem + "\n").encode())
    after_inventory = inventory(root)
    before_inventory = {
        owner_paths[0]: c.sha(b"old A"),
        owner_paths[2]: c.sha(b"old C"),
        "data/ingredients/unmapped/P_old.yaml": c.sha(b"old P"),
    }
    records = []
    for i, path in enumerate(owner_paths):
        old_path = "data/ingredients/unmapped/P_old.yaml" if i == 3 else path
        kind = "create" if i == 1 else "promote" if i == 3 else "edit"
        records.append(
            {
                "operation_id": str(i),
                "kind": kind,
                "source_record": path,
                "source_path": None if i == 1 else old_path,
                "destination_path": path,
                "shape": (
                    "new_record" if i == 1 else "promotion" if i == 3 else "campaign_owner_edit"
                ),
                "before_yaml_sha256": before_inventory.get(old_path),
                "after_yaml_sha256": after_inventory[path],
                "change": "Fixture reviewed change",
                "verification": "Fixture evidence; no approval",
            }
        )
        if i == 3:
            records[-1]["before_source_record"] = old_path
    policy = dict.fromkeys(c.POLICY_REQUIRED, "historical")
    policy.update(
        schema_version=1,
        policy_version="owned-name-policy-v1",
        approval="NONE: original historical policy",
        artifacts={c.SOURCE: c.sha(before), c.SIDECAR: c.sha(sidecar), c.BASELINE: c.sha(baseline)},
        source_owner_sha256=dict(before_inventory),
        decisions=[{"historic": "unchanged"}],
        policy_evidence=["old evidence"],
        source_alias_addition_updates=[{"old": "history"}],
    )
    for path, value in [
        (c.SOURCE, before),
        (c.POLICY, policy),
        (c.SIDECAR, sidecar),
        (c.BASELINE, baseline),
        (c.MAKER, (ROOT / c.MAKER).read_bytes()),
        (
            "src/mediaingredientmech/campaign_publication.py",
            (ROOT / "src/mediaingredientmech/campaign_publication.py").read_bytes(),
        ),
    ]:
        put(root, path, value)
    history(root, before)

    def reference(name, value):
        p = put(root, "reports/fixture/" + name, value)
        return {"path": p.relative_to(root).as_posix(), "sha256": c.sha(p.read_bytes())}

    plan = {
        "schema_version": 1,
        "kind": "unmatched_campaign_publication_v1",
        "issue": c.ISSUE,
        "approval": "NONE",
        "batch": "issue1174-fixture",
        "scope": "Bounded multi-owner fixture",
        "owner_plan": reference("owner-plan.json", {"accepted": "fixture"}),
        "owner_receipt": reference("owner-receipt.json", {"status": "complete"}),
        "before": {
            "canonical": reference("before.tsv", before),
            "policy": reference("policy-before.json", policy),
            "sidecar": reference("sidecar-before.tsv", sidecar),
            "baseline": reference("baseline-before.tsv", baseline),
        },
        "generation": {
            "candidate": reference("candidate.tsv", candidate),
            "sidecar": reference("diagnostic-sidecar.tsv", sidecar),
            "manifest": reference("generation.json", {"fixture": "isolated producer boundary"}),
            "producer_root": str(root / "producer"),
            "kg_root": str(root / "kg"),
        },
        "receipt_prefix": {},
        "native_context": {p: c.sha((root / p).read_bytes()) for p in native.HISTORICAL_CONTEXT},
        "rows": [
            {
                "owner": owner_paths[0],
                "before_position": 1,
                "native_position": 1,
                "preserve_fields": ["source", "comment", "confidence", "validation_method"],
            },
            {
                "owner": owner_paths[1],
                "before_position": None,
                "native_position": 2,
                "preserve_fields": [],
            },
            {
                "owner": owner_paths[3],
                "before_position": None,
                "native_position": 3,
                "preserve_fields": [],
            },
        ],
    }
    path = put(root, "reports/fixture/publication-plan.json", plan)
    out = root / "reports/publication"
    out.mkdir()
    owner_proof = {
        "plan_sha256": plan["owner_plan"]["sha256"],
        "receipt_sha256": plan["owner_receipt"]["sha256"],
        "before_inventory": before_inventory,
        "after_inventory": after_inventory,
        "records": records,
        "checkpoint": {"input_sha256": {**plan["native_context"], c.SOURCE: c.sha(before)}},
        "protected_snapshot": {
            "input_sha256": {
                c.POLICY: c.sha(c.encoded(policy)),
                c.SIDECAR: c.sha(sidecar),
                c.BASELINE: c.sha(baseline),
            }
        },
    }

    def verify_owner(actual_root, actual_plan):
        assert actual_root == root
        c.require(inventory(root) == after_inventory, "fixture owner membership/bytes changed")
        for key in ("owner_plan", "owner_receipt"):
            c.require(
                c.sha((root / actual_plan[key]["path"]).read_bytes()) == actual_plan[key]["sha256"],
                "fixture owner evidence changed",
            )
        return copy.deepcopy(owner_proof)

    def generation(capture, actual_plan, old, inv):
        assert old == before and inv == after_inventory
        g = actual_plan["generation"]
        a, b, m = (capture.ref(g[key]) for key in ("candidate", "sidecar", "manifest"))
        return a, b, json.loads(m)

    monkeypatch.setattr(c, "_owner_proof", verify_owner)
    monkeypatch.setattr(c, "_generation", generation)
    return {
        "root": root,
        "path": path,
        "plan": plan,
        "out": out,
        "records": records,
        "before": before,
        "owner_proof": owner_proof,
    }


def save(case):
    case["path"].write_bytes(c.encoded(case["plan"]))


def test_actual_native_multi_owner_new_promotion_and_source_only_publication(case):
    r = c.publish(case["root"], case["path"], case["out"], apply=True)
    assert r["status"] == "complete" and r["owner_count"] == 4
    assert c.validate(case["root"], case["path"])["status"] == "verified"
    receipt = json.loads((case["root"] / r["receipt_path"]).read_bytes())
    assert receipt["approval"].startswith("NONE")
    assert (
        len(receipt["records"]) == 4 and receipt["added_rows"] == 2 and receipt["changed_rows"] == 1
    )
    promoted = receipt["records"][-1]
    assert promoted["shape"] == "promotion" and promoted["before_yaml_sha256"]
    assert promoted["before_source_record"] == "data/ingredients/unmapped/P_old.yaml"
    assert receipt["records"][1]["before_yaml_sha256"] is None
    assert receipt["records"][2]["source_record"].endswith("/C.yaml")
    after = (case["root"] / c.SOURCE).read_bytes()
    assert c.table(after)[3][1] == c.table(case["before"])[3][1]
    policy = json.loads((case["root"] / c.POLICY).read_bytes())
    old = json.loads((case["root"] / case["plan"]["before"]["policy"]["path"]).read_bytes())
    for key in old.keys() - {"artifacts"}:
        assert policy[key] == old[key]
    assert policy[c.UPDATE][0]["approval"].startswith("NONE")
    assert native.verify_mapping_chain(case["root"])["state"] == c.table(after)[2]


def test_dry_run_has_no_outputs(case):
    result = c.publish(case["root"], case["path"], case["out"])
    assert result["status"] == "dry_run" and not list(case["out"].iterdir())
    assert (case["root"] / c.SOURCE).read_bytes() == case["before"]


@pytest.mark.parametrize(
    "mutation",
    [
        "unknown",
        "approval",
        "row-missing",
        "row-extra",
        "row-owner",
        "row-native",
        "row-preserve",
        "row-position-bool",
        "old-policy",
        "prefix",
        "source-extra",
        "new-suppression",
    ],
)
def test_closed_plan_and_current_input_refusals(case, mutation):
    plan, root = case["plan"], case["root"]
    if mutation == "unknown":
        plan["allow_anything"] = True
    elif mutation == "approval":
        plan["approval"] = "SUPPORTED"
    elif mutation == "row-missing":
        plan["rows"].pop()
    elif mutation == "row-extra":
        plan["rows"].append(copy.deepcopy(plan["rows"][0]))
    elif mutation == "row-owner":
        plan["rows"][0]["owner"] = "data/ingredients/mapped/Other.yaml"
    elif mutation == "row-native":
        plan["rows"][0]["native_position"] = 4
    elif mutation == "row-preserve":
        plan["rows"][0]["preserve_fields"].append("object_id")
    elif mutation == "row-position-bool":
        plan["rows"][0]["before_position"] = True
    elif mutation == "old-policy":
        p = root / c.POLICY
        d = json.loads(p.read_bytes())
        d["decisions"] = []
        p.write_bytes(c.encoded(d))
    elif mutation == "prefix":
        plan["receipt_prefix"][native.RECEIPTS_DIR + "/unknown.json"] = "0" * 64
    elif mutation == "source-extra":
        put(root, "data/ingredients/mapped/.Hidden.yaml", b"extra")
    elif mutation == "new-suppression":
        ref = plan["generation"]["sidecar"]
        p = root / ref["path"]
        p.write_bytes(
            p.read_bytes() + b'MIM:A\towned\tOwned\t["MIM:Other"]\tSUPPRESS\t[]\t[]\t[]\n'
        )
        ref["sha256"] = c.sha(p.read_bytes())
    save(case)
    with pytest.raises((ValueError, FileNotFoundError)):
        c.publish(root, case["path"], case["out"], apply=True)
    assert (root / c.SOURCE).read_bytes() == case["before"]


@pytest.mark.parametrize(
    "attack", ["existing-output", "symlink-output", "hardlink-input", "aliased-role"]
)
def test_preexisting_or_aliased_paths_refused(case, attack):
    root, plan = case["root"], case["plan"]
    log = case["out"] / "publication.json"
    if attack == "existing-output":
        log.write_bytes(b"unrelated")
    elif attack == "symlink-output":
        log.symlink_to(root / c.SOURCE)
    elif attack == "hardlink-input":
        os.link(root / plan["generation"]["candidate"]["path"], case["out"] / "linked")
    else:
        plan["before"]["canonical"] = {"path": c.SOURCE, "sha256": c.sha(case["before"])}
        save(case)
    with pytest.raises(ValueError):
        c.publish(root, case["path"], case["out"], apply=True)
    assert (root / c.SOURCE).read_bytes() == case["before"]


@pytest.mark.parametrize("phase", ["before", "after"])
@pytest.mark.parametrize(
    "role", ["candidate", "manifest", "owner_plan", "owner_receipt", "owner", "receipt_inventory"]
)
def test_late_drift_never_leaves_success_receipts(case, monkeypatch, phase, role):
    real = c.publish_validated
    called = False

    def drift():
        root, plan = case["root"], case["plan"]
        if role in {"candidate", "manifest"}:
            p = root / plan["generation"][role]["path"]
        elif role in {"owner_plan", "owner_receipt"}:
            p = root / plan[role]["path"]
        elif role == "owner":
            p = root / case["records"][0]["source_record"]
        else:
            p = root / native.RECEIPTS_DIR / "late.json"
        p.write_bytes(b"late drift")

    def wrapper(target, render, recheck):
        nonlocal called
        if called:
            return real(target, render, recheck)
        called = True
        if phase == "before":
            drift()
        result = real(target, render, recheck)
        if phase == "after":
            drift()
        return result

    monkeypatch.setattr(c, "publish_validated", wrapper)
    with pytest.raises((ValueError, FileNotFoundError)):
        c.publish(case["root"], case["path"], case["out"], apply=True)
    assert (case["out"] / "publication.json").read_bytes() == b""
    assert (case["root"] / native.RECEIPTS_DIR / "issue1174-fixture.json").read_bytes() == b""
    assert (case["out"] / "canonical-before.tsv").read_bytes() == case["before"]


def test_changed_policy_history_cannot_be_validated_even_after_hash_restamping(case):
    c.publish(case["root"], case["path"], case["out"], apply=True)
    path = case["root"] / c.POLICY
    policy = json.loads(path.read_bytes())
    policy["source_alias_addition_updates"][0]["old"] = "forged"
    path.write_bytes(c.encoded(policy))
    with pytest.raises(ValueError, match="projection/policy"):
        c.validate(case["root"], case["path"])


def test_native_receipt_approval_transfer_refused(case):
    result = c.publish(case["root"], case["path"], case["out"], apply=True)
    path = case["root"] / result["receipt_path"]
    receipt = json.loads(path.read_bytes())
    receipt["approval"] = "SUPPORTED"
    path.write_bytes(c.encoded(receipt))
    with pytest.raises(ValueError, match="approval-free"):
        c.validate(case["root"], case["path"])


def test_final_completion_boundary_drift_invalidates_both_success_receipts(case, monkeypatch):
    real = c.finish_receipt

    def late(handle, path, payload, recheck):
        def changed():
            (case["root"] / c.SIDECAR).write_bytes(b"changed sidecar")
            recheck()

        return real(handle, path, payload, changed)

    monkeypatch.setattr(c, "finish_receipt", late)
    with pytest.raises(ValueError):
        c.publish(case["root"], case["path"], case["out"], apply=True)
    assert (case["out"] / "publication.json").read_bytes() == b""
    assert (case["root"] / native.RECEIPTS_DIR / "issue1174-fixture.json").read_bytes() == b""


def test_promotion_with_native_old_path_history_refused(case):
    proof = native.verify_mapping_chain(case["root"])
    proof["owner_chains"]["data/ingredients/unmapped/P_old.yaml"] = [{"sequence": 1}]
    capture = c.Capture(case["root"])
    with pytest.raises(ValueError, match="promotion old path"):
        c._receipt(
            proof, c._maker(capture), case["plan"], case["records"], case["before"], case["before"]
        )


def test_bad_native_chain_refused(case):
    before = json.loads((case["root"] / native.BASELINE).read_bytes())
    before["rows"][0]["object_id"] = "CHEBI:9999"
    put(case["root"], native.BASELINE, before)
    case["plan"]["native_context"][native.BASELINE] = c.sha(
        (case["root"] / native.BASELINE).read_bytes()
    )
    save(case)
    with pytest.raises(ValueError, match="replay"):
        c.publish(case["root"], case["path"], case["out"], apply=True)


def test_selected_historical_owner_pin_requires_exact_native_bridge(case):
    root, plan = case["root"], case["plan"]
    owner = case["records"][0]
    older = c.sha(b"older historical reviewed owner")
    receipt = {
        "schema_version": 1,
        "batch": "old-link",
        "sequence": 1,
        "issue": "https://example.org/history",
        "scope": "Old exact source correction",
        "approval": "NONE: historical withdrawal",
        "before_sha256": c.sha(case["before"]),
        "after_sha256": c.sha(case["before"]),
        "before_row_count": 2,
        "after_row_count": 2,
        "position_map": [1, 2],
        "changes": [],
        "changed_rows": 0,
        "added_rows": 0,
        "removed_rows": 0,
        "records": [
            {
                "source_record": owner["source_record"],
                "shape": "old_correction",
                "before_yaml_sha256": older,
                "after_yaml_sha256": owner["before_yaml_sha256"],
            }
        ],
    }
    p = put(root, native.RECEIPTS_DIR + "/old-link.json", receipt)
    plan["receipt_prefix"][p.relative_to(root).as_posix()] = c.sha(p.read_bytes())
    case["owner_proof"]["checkpoint"]["input_sha256"][p.relative_to(root).as_posix()] = c.sha(
        p.read_bytes()
    )
    policy = json.loads((root / c.POLICY).read_bytes())
    policy["source_owner_sha256"][owner["source_record"]] = older
    put(root, c.POLICY, policy)
    ref = plan["before"]["policy"]
    put(root, ref["path"], policy)
    ref["sha256"] = c.sha((root / ref["path"]).read_bytes())
    case["owner_proof"]["protected_snapshot"]["input_sha256"][c.POLICY] = ref["sha256"]
    save(case)
    result = c.publish(root, case["path"], case["out"], apply=True)
    assert json.loads((root / result["receipt_path"]).read_bytes())["sequence"] == 2
    assert (
        json.loads((root / c.POLICY).read_bytes())["source_owner_sha256"][owner["source_record"]]
        == older
    )
    assert (root / native.RECEIPTS_DIR / "old-link.json").read_bytes() == c.encoded(receipt)


def test_missing_historical_owner_bridge_refused(case):
    root, plan = case["root"], case["plan"]
    policy = json.loads((root / c.POLICY).read_bytes())
    policy["source_owner_sha256"][case["records"][0]["source_record"]] = c.sha(b"unproved")
    put(root, c.POLICY, policy)
    ref = plan["before"]["policy"]
    put(root, ref["path"], policy)
    ref["sha256"] = c.sha((root / ref["path"]).read_bytes())
    case["owner_proof"]["protected_snapshot"]["input_sha256"][c.POLICY] = ref["sha256"]
    save(case)
    with pytest.raises(ValueError, match="lacks native bridge"):
        c.publish(root, case["path"], case["out"], apply=True)


def test_source_swap_same_bytes_still_refused(case, monkeypatch):
    original = c.publish_validated

    def swap(target, render, recheck):
        path = case["root"] / case["plan"]["generation"]["candidate"]["path"]
        content = path.read_bytes()
        path.rename(path.with_suffix(".old"))
        path.write_bytes(content)
        return original(target, render, recheck)

    monkeypatch.setattr(c, "publish_validated", swap)
    with pytest.raises(ValueError, match="identity changed"):
        c.publish(case["root"], case["path"], case["out"], apply=True)
    assert (case["root"] / c.SOURCE).read_bytes() == case["before"]


def test_late_output_parent_swap_never_writes_replacement_directory(case, monkeypatch):
    original = os.open
    outside = case["root"] / "unrelated"
    outside.mkdir()
    sentinel = outside / "sentinel"
    sentinel.write_bytes(b"unrelated preserved")
    moved = case["out"].with_name("original-held-directory")
    attacked = False

    def swap(path, flags, *args, **kwargs):
        nonlocal attacked
        fd = original(path, flags, *args, **kwargs)
        if not attacked and Path(path) == case["out"] and flags & os.O_DIRECTORY:
            attacked = True
            case["out"].rename(moved)
            case["out"].symlink_to(outside, target_is_directory=True)
        return fd

    monkeypatch.setattr(os, "open", swap)
    with pytest.raises(ValueError, match="alias"):
        c.publish(case["root"], case["path"], case["out"], apply=True)
    assert attacked and list(outside.iterdir()) == [sentinel]
    assert sentinel.read_bytes() == b"unrelated preserved"
    assert not list(moved.iterdir())
    assert (case["root"] / c.SOURCE).read_bytes() == case["before"]


def test_removal_is_traced_and_unrelated_physical_line_preserved(case):
    rows = c.table(case["before"])[2]
    candidate = sssom([rows[1]])
    record = [case["records"][0]]
    plan = [
        {
            "owner": record[0]["source_record"],
            "before_position": 1,
            "native_position": None,
            "preserve_fields": [],
        }
    ]
    after, trace = c.row_projection(case["before"], candidate, record, plan)
    assert c.table(after)[2] == [rows[1]]
    assert c.table(after)[3] == [c.table(case["before"])[3][1]]
    assert {x["basis"] for x in trace[0]["changed_cells"]} == {"native_slot_absent"}


def test_untraced_candidate_cell_cannot_be_written_from_plan(case):
    plan = copy.deepcopy(case["plan"]["rows"])
    plan[0]["after"] = {"object_id": "CHEBI:999"}
    with pytest.raises(ValueError, match="row plan fields"):
        c.row_projection(
            case["before"],
            (case["root"] / case["plan"]["generation"]["candidate"]["path"]).read_bytes(),
            case["records"],
            plan,
        )


@pytest.mark.parametrize("source_name", ["canonical", "policy"])
def test_hardlink_created_at_last_replace_is_refused_without_touching_old_inode(
    case, monkeypatch, source_name
):
    original = os.replace
    path = case["root"] / (c.SOURCE if source_name == "canonical" else c.POLICY)
    before = path.read_bytes()
    linked = case["root"] / "unrelated-old-inode"
    attacked = False

    def replace(src, dst, *args, **kwargs):
        nonlocal attacked
        if not attacked and dst == path.name:
            attacked = True
            os.link(path, linked)
        return original(src, dst, *args, **kwargs)

    monkeypatch.setattr(os, "replace", replace)
    with pytest.raises(ValueError, match="hardlink appeared"):
        c.publish(case["root"], case["path"], case["out"], apply=True)
    assert attacked and linked.read_bytes() == before
    assert (case["out"] / "publication.json").read_bytes() == b""
    assert (case["root"] / native.RECEIPTS_DIR / "issue1174-fixture.json").read_bytes() == b""


def test_hidden_receipt_addition_after_completion_replay_is_rejected(case, monkeypatch):
    real = c.validate

    def late(root, plan):
        result = real(root, plan)
        put(root, native.RECEIPTS_DIR + "/.late.json", b"{}")
        return result

    monkeypatch.setattr(c, "validate", late)
    with pytest.raises(ValueError, match="membership changed"):
        c.publish(case["root"], case["path"], case["out"], apply=True)
    assert (case["out"] / "publication.json").read_bytes() == b""


def test_sidecar_reattribution_is_refused_even_with_unchanged_canonical(case):
    p = case["root"] / c.SIDECAR
    p.write_bytes(p.read_bytes() + b"MIM:A\ttoken\tToken\t[]\tSUPPRESS\tprior_only\t[]\t[]\n")
    with pytest.raises(ValueError, match="sidecar/baseline changed"):
        c.publish(case["root"], case["path"], case["out"], apply=True)


@pytest.mark.parametrize("name", ["../outside", "/absolute", "a//b", "a/./b", "a\\b"])
def test_noncanonical_plan_reference_refused(case, name):
    case["plan"]["owner_plan"]["path"] = name
    save(case)
    with pytest.raises(ValueError):
        c.publish(case["root"], case["path"], case["out"], apply=True)


def test_actual_owner_writer_checkpoint_survives_native_mapping_publication(tmp_path, monkeypatch):
    """Real source apply/retirement plus real publisher/maker/chain; no owner stub."""
    spec = importlib.util.spec_from_file_location(
        "campaign_owner_fixture", ROOT / "tests/test_campaign_owner_apply.py"
    )
    fixture = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fixture)
    owner = fixture.owner
    source_plan = fixture.setup(tmp_path)
    before = sssom([row("Existing")])
    put(tmp_path, c.SOURCE, before)
    history(tmp_path, before)
    put(tmp_path, c.MAKER, (ROOT / c.MAKER).read_bytes())
    put(tmp_path, "src/mediaingredientmech/campaign_publication.py", Path(c.__file__).read_bytes())
    sidecar = b"subject_id\ttoken_key\ttoken\towner_subject_ids\tdisposition\tinput_surfaces\tsource_refs\tevidence_refs\n"
    baseline = b"subject_id\ttoken_key\n"
    policy = dict.fromkeys(c.POLICY_REQUIRED, "historical")
    policy.update(
        schema_version=1,
        policy_version="owned-name-policy-v1",
        approval="NONE: fixture",
        artifacts={c.SOURCE: c.sha(before), c.SIDECAR: c.sha(sidecar), c.BASELINE: c.sha(baseline)},
        source_owner_sha256=owner.hashes(owner.inventory(tmp_path)),
        decisions=[],
        policy_evidence=[],
    )
    put(tmp_path, c.POLICY, policy)
    put(tmp_path, c.SIDECAR, sidecar)
    put(tmp_path, c.BASELINE, baseline)
    protected = {
        p: c.sha((tmp_path / p).read_bytes()) for p in (c.SOURCE, c.POLICY, c.SIDECAR, c.BASELINE)
    }
    put(tmp_path, "protected.json", {"schema_version": 1, "files": protected})
    source_plan["protected_inputs"] = fixture.ref(tmp_path, "protected.json")
    fixture.run_git(
        tmp_path,
        "add",
        c.SOURCE,
        c.POLICY,
        c.SIDECAR,
        c.BASELINE,
        c.MAKER,
        *native.HISTORICAL_CONTEXT,
        "src/mediaingredientmech/campaign_publication.py",
        "protected.json",
    )
    fixture.run_git(
        tmp_path,
        "-c",
        "user.email=fixture@example.invalid",
        "-c",
        "user.name=Fixture",
        "commit",
        "-qm",
        "Add publication fixture context",
    )
    source_plan["baseline_commit"] = fixture.run_git(tmp_path, "rev-parse", "HEAD")
    fixture.save_contract(tmp_path, source_plan)
    owner.apply(
        owner.prepare(tmp_path, tmp_path / "plan.json", tmp_path / "acceptance.json"),
        tmp_path / "source-receipt",
        enabled=True,
    )
    completed = owner.verify_completed(
        tmp_path, tmp_path / "plan.json", tmp_path / "source-receipt/application.json"
    )
    candidate = sssom(
        [
            row("Existing", mapping_date="2026-11-07"),
            row("New", "CHEBI:2", mapping_date="2026-11-07"),
            row("Stock_curated", "kgmicrobe.ingredient:fixture_stock", mapping_date="2026-11-07"),
        ]
    )

    def ref(name, value):
        p = put(tmp_path, "reports/fixture/" + name, value)
        return {"path": str(p.relative_to(tmp_path)), "sha256": c.sha(p.read_bytes())}

    plan = {
        "schema_version": 1,
        "kind": "unmatched_campaign_publication_v1",
        "issue": c.ISSUE,
        "approval": "NONE",
        "batch": "issue1174-real-owner-interface",
        "scope": "Private native interface fixture",
        "owner_plan": fixture.ref(tmp_path, "plan.json"),
        "owner_receipt": fixture.ref(tmp_path, "source-receipt/application.json"),
        "before": {
            "canonical": ref("before.tsv", before),
            "policy": ref("before-policy.json", policy),
            "sidecar": ref("before-sidecar.tsv", sidecar),
            "baseline": ref("before-baseline.tsv", baseline),
        },
        "generation": {
            "candidate": ref("candidate.tsv", candidate),
            "sidecar": ref("diagnostic-sidecar.tsv", sidecar),
            "manifest": ref("generation.json", {"fixture": "isolated producer input"}),
            "producer_root": str(tmp_path / "producer"),
            "kg_root": str(tmp_path / "kg"),
        },
        "receipt_prefix": {},
        "native_context": {
            p: c.sha((tmp_path / p).read_bytes()) for p in native.HISTORICAL_CONTEXT
        },
        "rows": [
            {
                "owner": r["source_record"],
                "before_position": 1 if i == 0 else None,
                "native_position": i + 1,
                "preserve_fields": [],
            }
            for i, r in enumerate(completed["records"])
        ],
    }
    path = put(tmp_path, "reports/fixture/publication-plan.json", plan)
    out = tmp_path / "reports/publication"
    out.mkdir()

    def generation(capture, actual, old, inv):
        assert old == before and inv == completed["after_inventory"]
        data = [capture.ref(actual["generation"][k]) for k in ("candidate", "sidecar", "manifest")]
        return data[0], data[1], json.loads(data[2])

    monkeypatch.setattr(c, "_generation", generation)
    result = c.publish(tmp_path, path, out, apply=True)
    assert result["status"] == "complete"
    assert c.validate(tmp_path, path)["status"] == "verified"
    assert (
        owner.verify_completed(
            tmp_path, tmp_path / "plan.json", tmp_path / "source-receipt/application.json"
        )
        == completed
    )
    assert (
        native.verify_mapping_chain(tmp_path)["receipts"][-1]["records"][-1]["shape"] == "promotion"
    )
