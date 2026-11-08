"""#1174: real source transitions, exclusive publication and retained evidence.

All fixtures are private repositories. Their acceptance is mechanical fixture
data, never a scientific approval for the maintained corpus.
"""

from __future__ import annotations

import copy
import json
import os
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
    "# mapping_set_id: https://example.org/fixture\n# predicate_semantics: skos\n"
    "subject_id\tsubject_label\tpredicate_id\tobject_id\tobject_label\tother\n"
    "MIM:Existing\tExisting\tskos:exactMatch\tCHEBI:1\tExisting\t\n"
).encode()


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
    return dict(
        timestamp="2026-11-07T00:00:00Z",
        curator="fixture",
        action=action,
        changes="Explicit fixture change",
        new_status=status,
        llm_assisted=False,
    )


def ingredient(identifier, term, status="MAPPED"):
    return dict(
        identifier=identifier,
        preferred_term=term,
        mapping_status=status,
        curation_history=[event(status=status)],
    )


def render(root, name, payload):
    path = root / name
    write_validated_ingredient(payload, path, target_class="IngredientRecord")
    return path


def save_contract(root, plan):
    path = put(root, "plan.json", plan)
    accepted = dict(
        schema_version=1,
        scope="source_application_only",
        plan_sha256=owner.digest(path.read_bytes()),
        baseline_commit=plan["baseline_commit"],
        intake_heads=plan["intake_heads"],
        binding_sha256={b["binding_id"]: b["sha256"] for b in plan["bindings"]},
        accepted_operations={
            r["operation_id"]: r["after_capture"]["sha256"] for r in plan["records"]
        },
        review_bindings=["review"],
    )
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


def setup(root, *, chain_on_old=False):
    for path in owner.PRODUCERS:
        put(root, path, (ROOT / path).read_bytes())
    old_edit = ingredient("CHEBI:1", "Existing")
    old_stock = ingredient("UNMAPPED_0001", "Stock old", "UNMAPPED")
    render(root, EDIT, old_edit)
    render(root, OLD, old_stock)
    render(root, UNTOUCHED, ingredient("CHEBI:99", "Untouched"))
    put(root, CANONICAL, SSSOM)
    if chain_on_old:
        from mediaingredientmech.export.reviewed_sssom import read_sssom

        rows = read_sssom(root / CANONICAL)[2]
        s = owner.digest(SSSOM)
        put(root, native.BASELINE, dict(schema_version=1, source_sha256=s, rows=rows))
        for name in (native.TRAIT_REFRESH, native.PARENT_REFRESH):
            put(
                root,
                name,
                dict(
                    schema_version=1,
                    before_sha256=s,
                    after_sha256=s,
                    row_count=1,
                    changed_rows=0,
                    changes=[],
                ),
            )
        put(
            root,
            native.RECEIPTS_DIR + "/link-1.json",
            dict(
                schema_version=1,
                batch="fixture",
                sequence=1,
                approval="NONE: fixture",
                before_sha256=s,
                after_sha256=s,
                before_row_count=1,
                after_row_count=1,
                position_map=[1],
                changes=[],
                changed_rows=0,
                added_rows=0,
                removed_rows=0,
                records=[
                    dict(
                        source_record=OLD,
                        shape="existing",
                        before_yaml_sha256=ref(root, OLD)["sha256"],
                        after_yaml_sha256=ref(root, OLD)["sha256"],
                    )
                ],
            ),
        )
        assert native.verify_mapping_chain(root)["owner_chains"][OLD]
    before = owner.hashes(owner.inventory(root))
    put(root, "before.json", {"schema_version": 1, "owners": before})
    put(root, "protected.json", {"schema_version": 1, "files": {CANONICAL: owner.digest(SSSOM)}})
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
            dict(
                proposal_id=f"p{i}",
                case_ids=[f"case-{i}"],
                kind="new_owner" if kind == "create" else "edit_existing_owner",
                owner_path=source or dest,
                before_sha256=before.get(source),
                after_capture={"root": "artifact", **ref(root, name)},
            )
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
            dict(
                operation_id=f"o{i}",
                kind=kind,
                before_source_record=source,
                source_record=dest,
                before_yaml_sha256=before.get(source),
                after_capture=ref(root, f"intake/payload-{i}.yaml"),
                origins=[
                    dict(
                        worker_slot="worker-01",
                        head_sha=head,
                        proposal_id=f"p{i}",
                        proposal_binding="proposals",
                        payload_binding=f"payload-{i}",
                        case_hashes={f"case-{i}": case_hash},
                    )
                ],
                change="Fixture source change with explicit paths",
                verification="Schema and exact preimage; no scientific approval",
            )
        )
    plan = dict(
        schema_version=1,
        operation="apply_reviewed_campaign_owners",
        repository="CultureBotAI/MediaIngredientMech",
        baseline_commit=head,
        intake_heads={"worker-01": head},
        before_inventory=ref(root, "before.json"),
        after_inventory={},
        protected_inputs=ref(root, "protected.json"),
        bindings=bindings,
        records=operations,
    )
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
