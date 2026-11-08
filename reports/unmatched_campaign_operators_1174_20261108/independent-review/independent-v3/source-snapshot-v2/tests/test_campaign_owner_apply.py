"""#1174: real source transitions, exclusive publication and retained evidence.

All fixtures are private repositories. Their acceptance is mechanical fixture
data, never a scientific approval for the maintained corpus.
"""

from __future__ import annotations

import copy
import json
import os
import shutil
import subprocess
from pathlib import Path

import pytest

from mediaingredientmech.curate import campaign_owner_apply as owner
from mediaingredientmech.validation import mapping_change_receipts as native
from mediaingredientmech.validation.write_validated import write_validated_ingredient

ROOT = Path(__file__).resolve().parents[1]
EDIT = "data/ingredients/mapped/Existing.yaml"
OLD = "data/ingredients/unmapped/Stock_old.yaml"
NEW = "data/ingredients/mapped/New.yaml"
MOVED = "data/ingredients/mapped/Stock_curated.yaml"
UNTOUCHED = "data/ingredients/mapped/Untouched.yaml"
CANONICAL = "mappings/ingredient_mappings.sssom.tsv"
SSSOM = (
    b"# mapping_set_id: https://example.org/fixture\n# predicate_semantics: skos\n"
    b"subject_id\tsubject_label\tpredicate_id\tobject_id\tobject_label\tother\n"
    b"MIM:Existing\tExisting\tskos:exactMatch\tCHEBI:1\tExisting\t\n"
)


def put(root, name, value):
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(value if isinstance(value, bytes) else owner.encoded(value))
    return path


def ref(root, name):
    return {"path": name, "sha256": owner.digest((root / name).read_bytes())}


def run_git(root, *args):
    return owner.git(root, *args).decode().strip()


def event(action="CREATED", status="MAPPED"):
    return {
        "timestamp": "2026-11-07T00:00:00Z",
        "curator": "fixture",
        "action": action,
        "changes": "Explicit fixture change",
        "new_status": status,
        "llm_assisted": False,
    }


def ingredient(identifier, term, status="MAPPED"):
    return {
        "identifier": identifier,
        "preferred_term": term,
        "mapping_status": status,
        "curation_history": [event(status=status)],
    }


def render(root, name, payload):
    path = root / name
    write_validated_ingredient(payload, path, target_class="IngredientRecord")
    return path


def save_contract(root, plan):
    path = put(root, "plan.json", plan)
    accepted = {
        "schema_version": 1,
        "scope": "source_application_only",
        "plan_sha256": owner.digest(path.read_bytes()),
        "baseline_commit": plan["baseline_commit"],
        "intake_heads": plan["intake_heads"],
        "binding_sha256": {b["binding_id"]: b["sha256"] for b in plan["bindings"]},
        "accepted_operations": {
            r["operation_id"]: r["after_capture"]["sha256"] for r in plan["records"]
        },
        "review_bindings": ["review"],
    }
    put(root, "acceptance.json", accepted)


def repin(root, plan):
    """Fixture authoring only: derive expected after inventory from selected ops."""
    before = json.loads((root / plan["before_inventory"]["path"]).read_bytes())["owners"]
    after = dict(before)
    for entry in plan["records"]:
        entry["after_capture"] = ref(root, entry["after_capture"]["path"])
        if entry["kind"] == "promote":
            del after[entry["before_source_record"]]
        after[entry["source_record"]] = entry["after_capture"]["sha256"]
    put(root, "after.json", {"schema_version": 1, "owners": after})
    plan["after_inventory"] = ref(root, "after.json")
    save_contract(root, plan)


def setup(root, *, chain_on_old=False, chain_owner=None, chain_sha=None, bridge_to_current=False):
    for path in owner.PRODUCERS:
        put(root, path, (ROOT / path).read_bytes())
    old_edit = ingredient("CHEBI:1", "Existing")
    old_stock = ingredient("UNMAPPED_0001", "Stock old", "UNMAPPED")
    render(root, EDIT, old_edit)
    render(root, OLD, old_stock)
    render(root, UNTOUCHED, ingredient("CHEBI:99", "Untouched"))
    put(root, CANONICAL, SSSOM)
    if chain_on_old or chain_owner:
        from mediaingredientmech.export.reviewed_sssom import read_sssom

        rows = read_sssom(root / CANONICAL)[2]
        s = owner.digest(SSSOM)
        put(root, native.BASELINE, {"schema_version": 1, "source_sha256": s, "rows": rows})
        for name in (native.TRAIT_REFRESH, native.PARENT_REFRESH):
            put(
                root,
                name,
                {
                    "schema_version": 1,
                    "before_sha256": s,
                    "after_sha256": s,
                    "row_count": 1,
                    "changed_rows": 0,
                    "changes": [],
                },
            )
        linked_owner = OLD if chain_on_old else chain_owner
        linked_sha = chain_sha or ref(root, linked_owner)["sha256"]
        put(
            root,
            native.RECEIPTS_DIR + "/link-1.json",
            {
                "schema_version": 1,
                "batch": "fixture",
                "sequence": 1,
                "approval": "NONE: fixture",
                "before_sha256": s,
                "after_sha256": s,
                "before_row_count": 1,
                "after_row_count": 1,
                "position_map": [1],
                "changes": [],
                "changed_rows": 0,
                "added_rows": 0,
                "removed_rows": 0,
                "records": [
                    {
                        "source_record": linked_owner,
                        "shape": "existing",
                        "before_yaml_sha256": linked_sha,
                        "after_yaml_sha256": linked_sha,
                    }
                ],
            },
        )
        assert native.verify_mapping_chain(root)["owner_chains"][linked_owner]
        if bridge_to_current:
            link = json.loads((root / (native.RECEIPTS_DIR + "/link-1.json")).read_bytes())
            link.update(sequence=2, batch="explicit-reviewed-source-bridge")
            link["records"][0]["after_yaml_sha256"] = ref(root, linked_owner)["sha256"]
            put(root, native.RECEIPTS_DIR + "/link-2.json", link)
            assert len(native.verify_mapping_chain(root)["owner_chains"][linked_owner]) == 2
    before = owner.hashes(owner.inventory(root))
    put(root, "before.json", {"schema_version": 1, "owners": before})
    put(
        root,
        "protected.json",
        {"schema_version": 1, "files": native.verify_mapping_chain(root)["input_hashes"]},
    )
    edited = copy.deepcopy(old_edit)
    edited["notes"] = "Source-backed fixture note; no mapping approval."
    edited["curation_history"].append(event("ANNOTATED"))
    stock = copy.deepcopy(old_stock)
    stock.update(
        identifier="kgmicrobe.ingredient:fixture_stock",
        preferred_term="Source-qualified fixture stock",
        mapping_status="MAPPED",
    )
    stock["curation_history"].append(event("MAPPED"))
    payloads = [edited, ingredient("CHEBI:2", "New"), stock]
    cases = [
        {"case_id": "case-" + str(i), "source_id": str(i), "label": label}
        for i, label in enumerate(("Existing source", "New source", "Stock source"))
    ]
    put(root, "intake/cases.json", cases)
    proposals = []
    for i, (kind, source, dest, payload) in enumerate(
        zip(
            ("edit", "create", "promote"),
            (EDIT, None, OLD),
            (EDIT, NEW, MOVED),
            payloads,
            strict=True,
        )
    ):
        name = f"intake/payload-{i}.yaml"
        render(root, name, payload)
        proposals.append(
            {
                "proposal_id": f"p{i}",
                "case_ids": [f"case-{i}"],
                "kind": "new_owner" if kind == "create" else "edit_existing_owner",
                "owner_path": source or dest,
                "before_sha256": before.get(source),
                "after_capture": {"root": "artifact", **ref(root, name)},
            }
        )
    put(root, "intake/proposals.json", {"proposals": proposals})
    for role in ("shard", "decision", "evidence", "review", "reconciliation"):
        put(root, f"intake/{role}.json", {"fixture": role, "approval": "NONE"})
    run_git(root, "init", "-q")
    run_git(root, "add", ".")
    run_git(
        root,
        "-c",
        "user.email=fixture@example.invalid",
        "-c",
        "user.name=Fixture",
        "commit",
        "-qm",
        "Fixture baseline",
    )
    head = run_git(root, "rev-parse", "HEAD")
    bindings = []

    def bind(name, role, path, published=False):
        bindings.append(
            dict(
                binding_id=name,
                role=role,
                **ref(root, path),
                published_head=head if published else None,
                published_path=path if published else None,
            )
        )

    bind("cases", "case_ledger", "intake/cases.json")
    bind("proposals", "proposal", "intake/proposals.json", True)
    for role in ("shard", "decision", "evidence", "review", "reconciliation"):
        bind(role, role, f"intake/{role}.json")
    for i, path in enumerate(owner.PRODUCERS):
        bind(f"producer-{i}", "producer", path)
    for i in range(3):
        bind(f"payload-{i}", "evidence", f"intake/payload-{i}.yaml", True)
    operations = []
    for i, (kind, source, dest) in enumerate(
        zip(("edit", "create", "promote"), (EDIT, None, OLD), (EDIT, NEW, MOVED), strict=True)
    ):
        case_hash = owner.digest(
            json.dumps(
                cases[i], sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False
            ).encode()
        )
        operations.append(
            {
                "operation_id": f"o{i}",
                "kind": kind,
                "before_source_record": source,
                "source_record": dest,
                "before_yaml_sha256": before.get(source),
                "after_capture": ref(root, f"intake/payload-{i}.yaml"),
                "origins": [
                    {
                        "worker_slot": "worker-01",
                        "head_sha": head,
                        "proposal_id": f"p{i}",
                        "proposal_binding": "proposals",
                        "payload_binding": f"payload-{i}",
                        "case_hashes": {f"case-{i}": case_hash},
                    }
                ],
                "change": "Fixture source change with explicit paths",
                "verification": "Schema and exact preimage; no scientific approval",
            }
        )
    plan = {
        "schema_version": 1,
        "operation": "apply_reviewed_campaign_owners",
        "repository": "CultureBotAI/MediaIngredientMech",
        "baseline_commit": head,
        "intake_heads": {"worker-01": head},
        "before_inventory": ref(root, "before.json"),
        "after_inventory": {},
        "protected_inputs": ref(root, "protected.json"),
        "bindings": bindings,
        "records": operations,
    }
    repin(root, plan)
    return plan


@pytest.fixture
def case(tmp_path):
    return tmp_path, setup(tmp_path)


def prepare(root):
    return owner.prepare(root, root / "plan.json", root / "acceptance.json")


def test_mixed_application_and_native_completed_proof(case):
    root, plan = case
    before = owner.hashes(owner.inventory(root))
    result = owner.apply(prepare(root), root / "receipt", enabled=True)
    proof = owner.verify_completed(root, root / "plan.json", root / "receipt/application.json")
    assert proof["before_inventory"] == before
    assert proof["after_inventory"] == owner.hashes(owner.inventory(root))
    assert proof["completed_operations"] == ["o0", "o1", "o2"]
    assert proof["approval"] == owner.APPROVAL
    assert proof["records"][2]["shape"] == "promotion"
    assert proof["records"][2]["before_source_record"] == OLD
    assert proof["records"][2]["before_yaml_sha256"] == before[OLD]
    assert proof["records"][1]["before_capture"] is None
    assert not (root / OLD).exists()
    assert (root / "receipt/promotion-0002/retired-owner.yaml").read_bytes() == (
        root / "receipt/owner-before-0002.yaml"
    ).read_bytes()
    assert owner.digest((root / UNTOUCHED).read_bytes()) == before[UNTOUCHED]
    assert (root / CANONICAL).read_bytes() == SSSOM
    assert result["state"] == "complete"
    assert plan["records"][0]["before_yaml_sha256"] != proof["records"][0]["after_yaml_sha256"]


def test_dry_run_and_cli_default_do_not_publish(case):
    root, _ = case
    before = owner.hashes(owner.inventory(root))
    dry = owner.apply(prepare(root), root / "receipt")
    assert dry["applied"] is False and not (root / "receipt").exists()
    command = [
        os.sys.executable,
        str(ROOT / "scripts/apply_unmatched_campaign_owners.py"),
        "--root",
        str(root),
        "--plan",
        str(root / "plan.json"),
        "--acceptance",
        str(root / "acceptance.json"),
        "--receipt-dir",
        str(root / "receipt"),
    ]
    completed = subprocess.run(command, capture_output=True, text=True, check=True)
    assert json.loads(completed.stdout)["applied"] is False
    assert owner.hashes(owner.inventory(root)) == before and not (root / "receipt").exists()


@pytest.mark.parametrize("part", ["plan", "record", "origin", "binding", "acceptance", "inventory"])
def test_unknown_closed_fields_fail(case, part):
    root, plan = case
    if part == "inventory":
        data = json.loads((root / "before.json").read_bytes())
        data["unknown"] = True
        put(root, "different-before.json", data)
        plan["before_inventory"] = ref(root, "different-before.json")
    else:
        target = {
            "plan": plan,
            "record": plan["records"][0],
            "origin": plan["records"][0]["origins"][0],
            "binding": plan["bindings"][0],
        }.get(part)
        if target is not None:
            target["unknown"] = True
    save_contract(root, plan)
    if part == "acceptance":
        data = json.loads((root / "acceptance.json").read_bytes())
        data["unknown"] = True
        put(root, "acceptance.json", data)
    with pytest.raises(ValueError, match="Unexpected fields"):
        prepare(root)


@pytest.mark.parametrize(
    "part", ["preimage", "case", "head", "published_payload", "promotion", "acceptance"]
)
def test_incomplete_or_false_lineage_fails(case, part):
    root, plan = case
    if part == "preimage":
        plan["records"][0]["before_yaml_sha256"] = "0" * 64
    elif part == "case":
        plan["records"][0]["origins"][0]["case_hashes"]["case-0"] = "0" * 64
    elif part == "head":
        plan["records"][0]["origins"][0]["head_sha"] = "0" * 40
    elif part == "published_payload":
        plan["records"][0]["origins"][0]["payload_binding"] = "review"
    elif part == "promotion":
        plan["records"][2]["before_source_record"] = EDIT
        plan["records"][2]["before_yaml_sha256"] = plan["records"][0]["before_yaml_sha256"]
    save_contract(root, plan)
    if part == "acceptance":
        accepted = json.loads((root / "acceptance.json").read_bytes())
        del accepted["accepted_operations"]["o1"]
        put(root, "acceptance.json", accepted)
    with pytest.raises(ValueError):
        prepare(root)


@pytest.mark.parametrize(
    "fault",
    [
        "history_only",
        "history_prefix",
        "identity_collision",
        "name_collision",
        "unknown_yaml",
        "wrong_state",
    ],
)
def test_payload_schema_history_and_owner_guards(case, fault):
    root, plan = case
    index = 2 if fault == "wrong_state" else 0
    entry = plan["records"][index]
    data = owner.record((root / entry["after_capture"]["path"]).read_bytes())
    if fault == "history_only":
        del data["notes"]
    elif fault == "history_prefix":
        data["curation_history"][0]["changes"] = "Altered old history"
    elif fault == "identity_collision":
        data["identifier"] = "CHEBI:99"
    elif fault == "name_collision":
        data["preferred_term"] = "unTOUCHed"
    elif fault == "unknown_yaml":
        data["not_schema"] = True
    else:
        data["mapping_status"] = "UNMAPPED"
    # The accepted integration payload can differ from a worker proposal; its
    # original published bytes remain separately pinned and never overwritten.
    path = "final-corrected.yaml"
    import yaml

    put(root, path, yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=80).encode())
    entry["after_capture"] = ref(root, path)
    repin(root, plan)
    with pytest.raises(ValueError):
        prepare(root)


def test_actual_native_old_owner_chain_refuses_promotion(tmp_path):
    setup(tmp_path, chain_on_old=True)
    with pytest.raises(ValueError, match="prior native owner-chain"):
        prepare(tmp_path)


@pytest.mark.parametrize("alias", ["leaf", "parent", "hardlink"])
def test_evidence_alias_refused(case, alias):
    root, _ = case
    path = root / "intake/review.json"
    if alias == "parent":
        (root / "intake").rename(root / "saved-intake")
        (root / "intake").symlink_to(root / "saved-intake", target_is_directory=True)
    else:
        saved = root / "saved-review.json"
        path.rename(saved)
        if alias == "leaf":
            path.symlink_to(saved)
        else:
            os.link(saved, path)
    with pytest.raises(ValueError, match="alias"):
        prepare(root)


def test_direct_ignored_owner_is_inventory_but_nested_backup_is_not(case):
    root, _ = case
    render(root, "data/ingredients/mapped/backups/Old.yaml", ingredient("CHEBI:777", "Historical"))
    prepare(root)
    put(root, ".gitignore", b"data/ingredients/mapped/Ignored.yaml\n")
    render(
        root,
        "data/ingredients/mapped/Ignored.yaml",
        ingredient("CHEBI:888", "Ignored direct owner"),
    )
    with pytest.raises(ValueError, match="Complete owner inventory differs"):
        prepare(root)


@pytest.mark.parametrize("drift", ["owner", "evidence", "new_destination", "native_receipt"])
def test_late_drift_prevents_owner_mutation(case, drift):
    root, _ = case
    ready = prepare(root)
    if drift == "owner":
        (root / UNTOUCHED).write_bytes((root / UNTOUCHED).read_bytes() + b"# changed\n")
    elif drift == "evidence":
        (root / "intake/review.json").write_bytes(b"{}\n")
    elif drift == "new_destination":
        (root / NEW).write_bytes(b"competitor\n")
    else:
        put(root, native.RECEIPTS_DIR + "/unexpected.json", {})
    old_edit = (root / EDIT).read_bytes()
    with pytest.raises(ValueError):
        owner.apply(ready, root / "receipt", enabled=True)
    assert (root / EDIT).read_bytes() == old_edit
    assert not (root / "receipt/application.json").exists()


def test_receipt_directory_collision_is_preserved(case):
    root, _ = case
    put(root, "receipt/competitor", b"keep")
    with pytest.raises(ValueError, match="already exists"):
        owner.apply(prepare(root), root / "receipt", enabled=True)
    assert (root / "receipt/competitor").read_bytes() == b"keep"


def test_reserved_backups_precede_first_write_and_late_failure_is_honest(case, monkeypatch):
    root, _ = case
    ready = prepare(root)
    before = ready.before[EDIT].content
    original = owner._new_owner

    def fail_second(*args, **kwargs):
        assert (root / "receipt/owner-before-0000.yaml").read_bytes() == before
        assert (root / "receipt/owner-before-0002.yaml").exists()
        assert (root / "receipt/checkpoint" / CANONICAL).read_bytes() == SSSOM
        raise RuntimeError("injected late failure")

    monkeypatch.setattr(owner, "_new_owner", fail_second)
    with pytest.raises(RuntimeError, match="injected late"):
        owner.apply(ready, root / "receipt", enabled=True)
    receipt = json.loads((root / "receipt/application.json").read_bytes())
    assert receipt["state"] == "failed" and receipt["recovery_required"] is True
    assert receipt["completed_operations"] == ["o0"]
    assert (root / EDIT).read_bytes() != before
    assert (root / OLD).exists() and not (root / NEW).exists()
    monkeypatch.setattr(owner, "_new_owner", original)
    with pytest.raises(ValueError, match="Unexpected fields|Not a complete"):
        owner.verify_completed(root, root / "plan.json", root / "receipt/application.json")


def test_exclusive_new_destination_race_preserves_competitor(case, monkeypatch):
    root, _ = case
    ready = prepare(root)
    original = owner.os.link

    def race(src, dest, **kwargs):
        (root / NEW).write_bytes(b"competing owner")
        return original(src, dest, **kwargs)

    monkeypatch.setattr(owner.os, "link", race)
    with pytest.raises(FileExistsError):
        owner.apply(ready, root / "receipt", enabled=True)
    assert (root / NEW).read_bytes() == b"competing owner"
    assert json.loads((root / "receipt/application.json").read_bytes())["state"] == "failed"


def test_exclusive_retirement_race_preserves_both_files(case, monkeypatch):
    root, _ = case
    ready = prepare(root)
    original = owner._rename_exclusive

    def race(*args):
        (root / "receipt/promotion-0002/retired-owner.yaml").write_bytes(b"competitor")
        return original(*args)

    monkeypatch.setattr(owner, "_rename_exclusive", race)
    with pytest.raises(FileExistsError):
        owner.apply(ready, root / "receipt", enabled=True)
    assert (root / OLD).read_bytes() == ready.before[OLD].content
    assert (root / MOVED).exists()
    assert (root / "receipt/promotion-0002/retired-owner.yaml").read_bytes() == b"competitor"
    assert json.loads((root / "receipt/application.json").read_bytes())["state"] == "failed"


def test_completed_verifier_replays_checkpoint_after_canonical_successor(case):
    root, _ = case
    owner.apply(prepare(root), root / "receipt", enabled=True)
    (root / CANONICAL).write_bytes(SSSOM + b"# separate publisher advanced live canonical\n")
    proof = owner.verify_completed(root, root / "plan.json", root / "receipt/application.json")
    assert proof["checkpoint"]["input_sha256"][CANONICAL] == owner.digest(SSSOM)
    assert proof["approval"] == owner.APPROVAL


@pytest.mark.parametrize(
    "drift", ["review", "owner", "backup", "checkpoint", "receipt_alias", "producer"]
)
def test_completed_verifier_rejects_current_or_archived_drift(case, drift):
    root, _ = case
    owner.apply(prepare(root), root / "receipt", enabled=True)
    paths = {
        "review": "intake/review.json",
        "owner": UNTOUCHED,
        "backup": "receipt/owner-before-0002.yaml",
        "checkpoint": "receipt/checkpoint/" + CANONICAL,
        "producer": owner.PRODUCERS[0],
    }
    if drift == "receipt_alias":
        path = root / "receipt/application.json"
        saved = root / "saved-application.json"
        path.rename(saved)
        path.symlink_to(saved)
    else:
        path = root / paths[drift]
        path.write_bytes(path.read_bytes() + b"\n")
    with pytest.raises(ValueError):
        owner.verify_completed(root, root / "plan.json", root / "receipt/application.json")


@pytest.mark.parametrize("role", ["backup", "protected", "retired"])
def test_late_archive_byte_drift_cannot_finish_success(case, monkeypatch, role):
    root, _ = case
    original = owner.finish_receipt

    def corrupt(receipt, path, payload, recheck):
        target = {
            "backup": root / "receipt/owner-before-0000.yaml",
            "protected": root / "receipt/protected" / CANONICAL,
            "retired": root / "receipt/promotion-0002/retired-owner.yaml",
        }[role]
        target.write_bytes(target.read_bytes() + b"# corrupt\n")
        return original(receipt, path, payload, recheck)

    monkeypatch.setattr(owner, "finish_receipt", corrupt)
    with pytest.raises(ValueError, match="changed"):
        owner.apply(prepare(root), root / "receipt", enabled=True)
    receipt = json.loads((root / "receipt/application.json").read_bytes())
    assert receipt["state"] == "failed" and receipt["recovery_required"]


@pytest.mark.parametrize("alias", ["leaf", "parent", "hardlink"])
def test_final_verifier_rechecks_original_proof_roles(case, monkeypatch, alias):
    root, _ = case
    owner.apply(prepare(root), root / "receipt", enabled=True)
    original = owner.verify_mapping_chain

    def late_alias(checkpoint):
        result = original(checkpoint)
        target = root / "intake/review.json"
        if alias == "parent":
            (root / "intake").rename(root / "moved-intake")
            (root / "intake").symlink_to(root / "moved-intake", target_is_directory=True)
        else:
            saved = root / "same-review-bytes"
            target.rename(saved)
            if alias == "leaf":
                target.symlink_to(saved)
            else:
                os.link(saved, target)
        return result

    monkeypatch.setattr(owner, "verify_mapping_chain", late_alias)
    with pytest.raises(ValueError, match="alias"):
        owner.verify_completed(root, root / "plan.json", root / "receipt/application.json")


def test_late_new_owner_parent_swap_cannot_write_into_replacement(case, monkeypatch):
    root, _ = case
    prepared = prepare(root)
    original = owner.os.link
    parent = root / "data/ingredients/mapped"
    archived = root / "original-mapped-directory"

    def swap(src, dest, **kwargs):
        parent.rename(archived)
        parent.mkdir()
        (parent / "competitor.yaml").write_bytes(b"competitor")
        return original(src, dest, **kwargs)

    monkeypatch.setattr(owner.os, "link", swap)
    with pytest.raises((ValueError, FileNotFoundError)):
        owner.apply(prepared, root / "receipt", enabled=True)
    assert (parent / "competitor.yaml").read_bytes() == b"competitor"
    assert not (root / NEW).exists()
    assert (archived / "Untouched.yaml").read_bytes() == prepared.before[UNTOUCHED].content
    assert json.loads((root / "receipt/application.json").read_bytes())["state"] == "failed"


def test_archived_protection_never_excuses_current_review_drift(case):
    root, plan = case
    protected = json.loads((root / "protected.json").read_bytes())
    protected["files"]["intake/review.json"] = ref(root, "intake/review.json")["sha256"]
    put(root, "protected-plus.json", protected)
    plan["protected_inputs"] = ref(root, "protected-plus.json")
    save_contract(root, plan)
    owner.apply(prepare(root), root / "receipt", enabled=True)
    (root / "intake/review.json").write_bytes(b"changed review")
    with pytest.raises(ValueError, match="Input hash differs"):
        owner.verify_completed(root, root / "plan.json", root / "receipt/application.json")


def test_noop_is_rejected_and_selected_case_subset_keeps_full_ledger(case):
    root, plan = case
    plan["records"] = [plan["records"][0]]
    repin(root, plan)
    result = owner.apply(prepare(root), root / "receipt", enabled=True)
    proof = owner.verify_completed(root, root / "plan.json", root / "receipt/application.json")
    assert result["completed_operations"] == ["o0"]
    assert "intake/cases.json" in proof["immutable_input_sha256"]
    assert len(json.loads((root / "intake/cases.json").read_bytes())) == 3
    assert (root / OLD).exists() and not (root / NEW).exists()


def test_casefold_destination_collision_refused_before_write(case):
    root, plan = case
    plan["records"][1]["source_record"] = "data/ingredients/mapped/UNTOUCHED.yaml"
    repin(root, plan)
    with pytest.raises(ValueError, match="Destination collides"):
        prepare(root)


@pytest.mark.parametrize(
    "change", ["addition", "removal", "symlink", "hardlink", "old_source_reappears"]
)
def test_1194_final_owner_membership_is_reenumerated(case, monkeypatch, change):
    root, _ = case
    ready = prepare(root)
    owner.apply(ready, root / "receipt", enabled=True)
    original = owner._validate_records

    def late_change(*args):
        original(*args)
        extra = root / "data/ingredients/unmapped/Unexpected_late.yaml"
        if change == "addition":
            extra.write_bytes(ready.before[OLD].content)
        elif change == "removal":
            (root / UNTOUCHED).unlink()
        elif change == "symlink":
            extra.symlink_to(root / UNTOUCHED)
        elif change == "hardlink":
            os.link(root / UNTOUCHED, extra)
        else:
            (root / OLD).write_bytes(ready.before[OLD].content)

    monkeypatch.setattr(owner, "_validate_records", late_change)
    with pytest.raises((ValueError, FileNotFoundError)):
        owner.verify_completed(root, root / "plan.json", root / "receipt/application.json")


@pytest.mark.parametrize("snapshot", ["checkpoint", "protected"])
@pytest.mark.parametrize("change", ["addition", "removal", "alias"])
def test_1194_final_snapshot_membership_is_reenumerated(case, monkeypatch, snapshot, change):
    root, _ = case
    owner.apply(prepare(root), root / "receipt", enabled=True)
    original = owner.verify_mapping_chain

    def late_change(*args):
        proof = original(*args)
        directory = root / "receipt" / snapshot
        if change == "removal":
            (directory / CANONICAL).unlink()
        elif change == "alias":
            (directory / "unexpected-alias").symlink_to(directory / CANONICAL)
        else:
            (directory / "unexpected-input").write_bytes(b"extra")
        return proof

    monkeypatch.setattr(owner, "verify_mapping_chain", late_change)
    with pytest.raises((ValueError, FileNotFoundError)):
        owner.verify_completed(root, root / "plan.json", root / "receipt/application.json")


@pytest.mark.parametrize(
    "change",
    [
        "none",
        "operator_content",
        "dependency_content",
        "operator_inode",
        "dependency_alias",
        "late_dependency",
    ],
)
def test_1195_loaded_producer_bytes_and_locations_are_frozen(tmp_path, change):
    package = tmp_path / "private-package"
    shutil.copytree(
        ROOT / "src", package / "src", ignore=shutil.ignore_patterns("__pycache__", "*.pyc")
    )
    for name in (
        "scripts/apply_unmatched_campaign_owners.py",
        "MAPPING_SEMANTICS.md",
        "uv.lock",
        "tests/test_campaign_owner_apply.py",
    ):
        put(package, name, (ROOT / name).read_bytes())
    script = put(
        tmp_path,
        "probe.py",
        b"""import importlib.util, json, os, sys
from pathlib import Path
from mediaingredientmech.curate import campaign_owner_apply as owner
package, root, change = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
spec = importlib.util.spec_from_file_location("fixture", package/"tests/test_campaign_owner_apply.py")
fixture = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fixture)
path = package/("src/mediaingredientmech/curate/publication_guard.py" if change.startswith("dependency") or change == "late_dependency" else "src/mediaingredientmech/curate/campaign_owner_apply.py")
def mutate():
    old = path.read_bytes()
    if change.endswith("content") or change == "late_dependency":
        path.write_bytes(old+b"\\n# Changed after operator import.\\n")
    elif change == "operator_inode":
        path.rename(path.with_suffix(".original"))
        path.write_bytes(old)
    elif change == "dependency_alias":
        path.rename(path.with_suffix(".original"))
        path.symlink_to(path.with_suffix(".original"))
if change != "late_dependency":
    mutate()
root.mkdir()
fixture.setup(root)
before = owner.hashes(owner.inventory(root))
try:
    prepared = owner.prepare(root, root/"plan.json", root/"acceptance.json")
    if change == "late_dependency":
        mutate()
    result = owner.apply(prepared, root/"receipt")
    report = {"accepted":True,"applied":result["applied"]}
except (ValueError, OSError) as error:
    report = {"accepted":False,"error":str(error)}
report["owner_bytes_preserved"] = owner.hashes(owner.inventory(root)) == before
report["receipt_exists"] = (root/"receipt").exists()
print(json.dumps(report))
""",
    )
    environment = dict(os.environ, PYTHONPATH=str(package / "src"), PYTHONDONTWRITEBYTECODE="1")
    run = subprocess.run(
        [os.sys.executable, str(script), str(package), str(tmp_path / "repository"), change],
        env=environment,
        check=True,
        capture_output=True,
        text=True,
    )
    result = json.loads(run.stdout)
    assert result["accepted"] is (change == "none")
    assert result["owner_bytes_preserved"] and not result["receipt_exists"]


@pytest.mark.parametrize("linked_owner", [EDIT, NEW, MOVED])
def test_1197_disconnected_or_reused_owner_history_refused_before_write(tmp_path, linked_owner):
    setup(tmp_path, chain_owner=linked_owner, chain_sha="b" * 64)
    before = owner.hashes(owner.inventory(tmp_path))
    with pytest.raises(ValueError, match="disconnected|destination has prior"):
        prepare(tmp_path)
    assert owner.hashes(owner.inventory(tmp_path)) == before
    assert not (tmp_path / "receipt").exists()


def test_1197_matching_native_endpoint_can_continue_without_approval(tmp_path):
    setup(tmp_path, chain_owner=EDIT)
    ready = prepare(tmp_path)
    owner.apply(ready, tmp_path / "receipt", enabled=True)
    proof = owner.verify_completed(
        tmp_path, tmp_path / "plan.json", tmp_path / "receipt/application.json"
    )
    assert proof["records"][0]["before_yaml_sha256"] == owner.digest(ready.before[EDIT].content)
    assert proof["approval"] == owner.APPROVAL


def test_1197_explicit_native_bridge_can_connect_a_current_preimage(tmp_path):
    setup(tmp_path, chain_owner=EDIT, chain_sha="b" * 64, bridge_to_current=True)
    ready = prepare(tmp_path)
    owner.apply(ready, tmp_path / "receipt", enabled=True)
    proof = owner.verify_completed(
        tmp_path, tmp_path / "plan.json", tmp_path / "receipt/application.json"
    )
    assert proof["records"][0]["before_yaml_sha256"] == owner.digest(ready.before[EDIT].content)
    assert proof["approval"] == owner.APPROVAL


@pytest.mark.parametrize("argument", ["root", "plan", "acceptance", "receipt"])
def test_1198_noncanonical_top_level_arguments_refused_before_mutation(case, argument):
    root, _ = case
    before = owner.hashes(owner.inventory(root))
    call_root = root / "intake/.." if argument == "root" else root
    plan = root / ("intake/../plan.json" if argument == "plan" else "plan.json")
    acceptance = root / (
        "intake/../acceptance.json" if argument == "acceptance" else "acceptance.json"
    )
    with pytest.raises(ValueError, match="Noncanonical"):
        ready = owner.prepare(call_root, plan, acceptance)
        owner.apply(ready, root / "intake/../receipt", enabled=True)
    assert owner.hashes(owner.inventory(root)) == before
    assert not (root / "receipt").exists()


def test_native_checkpoint_must_be_accepted_before_application(case):
    root, plan = case
    put(root, "unbound-checkpoint.json", {"schema_version": 1, "files": {}})
    plan["protected_inputs"] = ref(root, "unbound-checkpoint.json")
    save_contract(root, plan)
    before = owner.hashes(owner.inventory(root))
    with pytest.raises(ValueError, match="omit native checkpoint"):
        prepare(root)
    assert owner.hashes(owner.inventory(root)) == before


@pytest.mark.parametrize(
    "dependency",
    [
        "mediaingredientmech.curate.publication_guard",
        "mediaingredientmech.curate.apply_receipt",
        "mediaingredientmech.validation.write_validated",
        "mediaingredientmech.validation.mapping_change_receipts",
        "mediaingredientmech.export.reviewed_sssom",
    ],
)
@pytest.mark.parametrize("mode", ["fresh_capture", "stale_pin"])
def test_1195_cached_dependency_is_reexecuted_privately_from_pinned_bytes(
    tmp_path, dependency, mode
):
    package = tmp_path / "private-package"
    shutil.copytree(
        ROOT / "src", package / "src", ignore=shutil.ignore_patterns("__pycache__", "*.pyc")
    )
    for name in (
        "scripts/apply_unmatched_campaign_owners.py",
        "MAPPING_SEMANTICS.md",
        "uv.lock",
        "tests/test_campaign_owner_apply.py",
    ):
        put(package, name, (ROOT / name).read_bytes())
    script = put(
        tmp_path,
        "cached-probe.py",
        b"""import hashlib, importlib, importlib.util, json, sys
from pathlib import Path
package, root, name, mode = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3], sys.argv[4]
public = importlib.import_module(name)
path = Path(public.__file__)
old = path.read_bytes()
marker = b"\\n_campaign_test_fresh_marker = 'executed newer captured bytes'\\n"
if name.endswith('reviewed_sssom'):
    marker += b"_campaign_test_original_read = read_sssom\\ndef read_sssom(*args, **kwargs):\\n    global _campaign_test_called\\n    _campaign_test_called = True\\n    return _campaign_test_original_read(*args, **kwargs)\\n"
path.write_bytes(old + marker)
from mediaingredientmech.curate import campaign_owner_apply as owner
bound = owner._BOUND_NATIVE[name]
spec = importlib.util.spec_from_file_location('fixture', package/'tests/test_campaign_owner_apply.py')
fixture = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fixture)
root.mkdir()
plan = fixture.setup(root)
if mode == 'stale_pin':
    source = 'src/' + name.replace('.', '/') + '.py'
    (root/source).write_bytes(old)
    for binding in plan['bindings']:
        if binding['role'] == 'producer' and binding['path'] == source:
            binding['sha256'] = hashlib.sha256(old).hexdigest()
    fixture.save_contract(root, plan)
before = owner.hashes(owner.inventory(root))
try:
    ready = owner.prepare(root, root/'plan.json', root/'acceptance.json')
    result = owner.apply(ready, root/'receipt')
    outcome = {'accepted':True, 'applied':result['applied']}
except ValueError as error:
    outcome = {'accepted':False, 'error':str(error)}
outcome.update(public_unchanged=sys.modules[name] is public and not hasattr(public, '_campaign_test_fresh_marker'),
    private_executed=bound is not public and bound._campaign_test_fresh_marker == 'executed newer captured bytes',
    captured_bytes_equal=bound._campaign_executed_source.content == old+marker,
    private_deferred_import_used=bool(getattr(bound, '_campaign_test_called', False)),
    owner_bytes_preserved=owner.hashes(owner.inventory(root)) == before,
    receipt_exists=(root/'receipt').exists())
print(json.dumps(outcome))
""",
    )
    run = subprocess.run(
        [
            os.sys.executable,
            str(script),
            str(package),
            str(tmp_path / "repository"),
            dependency,
            mode,
        ],
        env=dict(os.environ, PYTHONPATH=str(package / "src"), PYTHONDONTWRITEBYTECODE="1"),
        check=True,
        capture_output=True,
        text=True,
    )
    result = json.loads(run.stdout)
    assert result["accepted"] is (mode == "fresh_capture")
    assert (
        result["public_unchanged"] and result["private_executed"] and result["captured_bytes_equal"]
    )
    assert result["owner_bytes_preserved"] and not result["receipt_exists"]
    if mode == "stale_pin":
        assert "Loaded producer differs" in result["error"]
    elif dependency.endswith("reviewed_sssom"):
        assert result["private_deferred_import_used"]


def test_1195_private_capture_leaves_unchanged_public_dependency_untouched():
    from mediaingredientmech.curate import publication_guard

    bound = owner._BOUND_NATIVE["mediaingredientmech.curate.publication_guard"]
    assert owner.FrozenFile is bound.FrozenFile
    assert owner.FrozenFile is not publication_guard.FrozenFile
    assert bound._campaign_executed_source.content == Path(publication_guard.__file__).read_bytes()
    bound._campaign_executed_source.verify()
