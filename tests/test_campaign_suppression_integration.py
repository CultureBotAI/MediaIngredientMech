"""Real six-owner source→Claw→four-event publisher fixture under #1259.

Authentic W07 source/proposal/owner evidence and genuine historical34/27 are
used. Only the private activation and actual-transition reviewer are mechanical
fixture artifacts; they are never scientific authorization for the real corpus.
No source verifier, native generator, receipt maker or publisher is replaced.
"""

import copy
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

from mediaingredientmech import campaign_publication as c
from mediaingredientmech.curate import campaign_owner_apply as owner

ROOT = Path(__file__).absolute().parents[1]


def helpers():
    spec = importlib.util.spec_from_file_location(
        "suppression_fixture_helpers", ROOT / "tests/test_campaign_suppressions.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def git(root, *args):
    return subprocess.check_output(["git", *args], cwd=root, text=True).strip()


def real_case(root, *, prior_native=False):
    h = helpers()
    original_root = os.environ.get("CAMPAIGN_SUPPRESSION_REVIEW_ROOT")
    history_root = os.environ.get("CAMPAIGN_HISTORY_ROOT")
    claw = os.environ.get("CLAW_ROOT")
    intake_root = os.environ.get("CAMPAIGN_SUPPRESSION_INTAKE_ROOT")
    if not all((original_root, history_root, claw, intake_root)):
        pytest.skip("Actual W07, historical27, pinned Claw and immutable intake roots required")
    original_root, history_root, claw, intake_root = map(
        Path, (original_root, history_root, claw, intake_root)
    )
    assert git(claw, "rev-parse", "HEAD") == c.PRODUCER_REVISION
    if prior_native:
        spec = importlib.util.spec_from_file_location(
            "prior_native_fixture", ROOT / "tests/test_campaign_demotion_integration.py"
        )
        prior = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(prior)
        _, _, prior_path, prior_destination, _ = prior.prepare_native_case(root, history_root)
        assert c.publish(root, prior_path, prior_destination, apply=True)["status"] == "complete"
        assert len(c.native.verify_mapping_chain(root)["receipts"]) == 28
        git(root, "add", ".")
        git(
            root,
            "-c",
            "user.name=Fixture",
            "-c",
            "user.email=fixture@example.invalid",
            "commit",
            "-qm",
            "Completed prior native fixture transaction",
        )
        assert c.validate(root, prior_path)["status"] == "verified"
        history_root = root
    original_review, original_document = h.original_bundle(root)

    def original(path):
        return (root / original_review["inputs"]["review-inputs/" + path]["path"]).read_bytes()

    decision = c.read_json(original("conditional-decisions.json"))
    bindings = json.loads((intake_root / "owner-plan.draft.json").read_bytes())["bindings"]
    materialization = {
        f["destination"]: f
        for f in json.loads((intake_root / "materialization-index.draft.json").read_bytes())[
            "files"
        ]
    }
    all_bindings = {b["binding_id"]: b for b in bindings}
    operations, originals = [], {}
    for pair in decision["pairs"]:
        for binding in pair["complete_owner_bindings"]:
            _, path = c._record_path(binding["proposed"]["original_path"])
            originals[path] = binding
            if binding["before"]:
                h.put(root, path, original(binding["before"]["capture"]))
            if binding["operation"]:
                op = copy.deepcopy(binding["operation"])
                op["after_capture"] = h.put(
                    root,
                    "intake/final/" + Path(path).name,
                    original(binding["proposed"]["capture"]),
                )
                operations.append(op)
    for bucket in ("mapped", "unmapped"):
        (root / "data/ingredients" / bucket).mkdir(parents=True, exist_ok=True)
    for path, frozen in {**owner.LOADED_PRODUCERS, **c.LOADED_PRODUCERS}.items():
        h.put(root, path, frozen.content)
    h.put(root, c.MAKER, (ROOT / c.MAKER).read_bytes())
    h.put(root, "pyproject.toml", (ROOT / "pyproject.toml").read_bytes())
    checkpoint = c.native.verify_mapping_chain(history_root)
    assert len(checkpoint["receipts"]) == (28 if prior_native else 27)
    for path, expected in checkpoint["input_hashes"].items():
        raw = (history_root / path).read_bytes()
        assert c.sha(raw) == expected
        h.put(root, path, raw)
    before = {
        key: (history_root / path).read_bytes()
        for key, path in (
            ("canonical", c.SOURCE),
            ("policy", c.POLICY),
            ("sidecar", c.SIDECAR),
            ("baseline", c.BASELINE),
        )
    }
    for key, path in (
        ("canonical", c.SOURCE),
        ("policy", c.POLICY),
        ("sidecar", c.SIDECAR),
        ("baseline", c.BASELINE),
    ):
        h.put(root, path, before[key])
    needed = {
        o[key]
        for op in operations
        for o in op["origins"]
        for key in ("proposal_binding", "payload_binding")
    }
    needed.add(next(b["binding_id"] for b in bindings if b["role"] == "case_ledger"))
    selected = []
    for name in sorted(needed):
        b = copy.deepcopy(all_bindings[name])
        item = materialization[b["path"]]
        raw = Path(item["source"]).read_bytes()
        assert c.sha(raw) == b["sha256"] == item["sha256"]
        h.put(root, b["path"], raw)
        selected.append(b)
    for role in sorted(owner.ROLES - {b["role"] for b in selected} - {"producer"}):
        # Explicit private activation metadata, not fabricated source science.
        ref = h.put(
            root,
            "intake/mechanical-" + role + ".json",
            {"scope": "PRIVATE MECHANICAL INTEGRATION FIXTURE ONLY", "role": role},
        )
        selected.append(
            {
                "binding_id": "fixture-" + role,
                "role": role,
                **ref,
                "published_head": None,
                "published_path": None,
            }
        )
    for path, frozen in owner.LOADED_PRODUCERS.items():
        selected.append(
            {
                "binding_id": "producer-" + path,
                "role": "producer",
                "path": path,
                "sha256": c.sha(frozen.content),
                "published_head": None,
                "published_path": None,
            }
        )
    git(root, "init", "-q")
    # Read existing authentic published objects through private alternates.
    campaign = intake_root.parents[1]
    object_roots = set()
    for slot in {o["worker_slot"] for op in operations for o in op["origins"]}:
        repository = campaign / "workers" / slot.replace("worker-", "w") / "worktree"
        value = Path(git(repository, "rev-parse", "--git-path", "objects"))
        object_roots.add(str(value if value.is_absolute() else (repository / value).resolve()))
    (root / ".git/objects/info/alternates").write_text("\n".join(sorted(object_roots)) + "\n")
    for b in selected:
        if b["published_head"]:
            assert (
                subprocess.check_output(
                    ["git", "show", f'{b["published_head"]}:{b["published_path"]}'], cwd=root
                )
                == (root / b["path"]).read_bytes()
            )
    before_inventory = owner.hashes(owner.inventory(root))
    after_inventory = dict(before_inventory)
    for op in operations:
        after_inventory[op["source_record"]] = op["after_capture"]["sha256"]
    protected = dict(checkpoint["input_hashes"])
    protected.update({p: c.sha((root / p).read_bytes()) for p in (c.POLICY, c.SIDECAR, c.BASELINE)})
    plan = {
        "schema_version": 1,
        "operation": "apply_reviewed_campaign_owners",
        "repository": "CultureBotAI/MediaIngredientMech",
        "baseline_commit": "",
        "intake_heads": {
            o["worker_slot"]: o["head_sha"] for op in operations for o in op["origins"]
        },
        "before_inventory": h.put(
            root, "intake/before.json", {"schema_version": 1, "owners": before_inventory}
        ),
        "after_inventory": h.put(
            root, "intake/after.json", {"schema_version": 1, "owners": after_inventory}
        ),
        "protected_inputs": h.put(
            root, "intake/protected.json", {"schema_version": 1, "files": protected}
        ),
        "bindings": selected,
        "records": operations,
    }
    git(root, "add", ".")
    git(
        root,
        "-c",
        "user.name=Fixture",
        "-c",
        "user.email=fixture@example.invalid",
        "commit",
        "-qm",
        "Private authentic-input suppression fixture baseline",
    )
    plan["baseline_commit"] = git(root, "rev-parse", "HEAD")
    plan_ref = h.put(root, "intake/plan.json", plan)
    acceptance = {
        "schema_version": 1,
        "scope": "source_application_only",
        "plan_sha256": plan_ref["sha256"],
        "baseline_commit": plan["baseline_commit"],
        "intake_heads": plan["intake_heads"],
        "binding_sha256": {b["binding_id"]: b["sha256"] for b in selected},
        "accepted_operations": {
            op["operation_id"]: op["after_capture"]["sha256"] for op in operations
        },
        "review_bindings": [b["binding_id"] for b in selected if b["role"] == "review"],
    }
    h.put(root, "intake/acceptance.json", acceptance)
    receipt_relative = "source-receipt-suppression" if prior_native else "source-receipt"
    owner_receipt = root / receipt_relative / "application.json"
    owner.apply(
        owner.prepare(root, root / "intake/plan.json", root / "intake/acceptance.json"),
        owner_receipt.parent,
        enabled=True,
    )
    proof = owner.verify_completed(root, root / "intake/plan.json", owner_receipt)
    assert len(proof["records"]) == 6
    kg = root / "private-kg"
    if not kg.exists():
        kg.mkdir()
        git(kg, "init", "-q")
        git(
            kg,
            "-c",
            "user.name=Fixture",
            "-c",
            "user.email=fixture@example.invalid",
            "commit",
            "--allow-empty",
            "-qm",
            "Empty fixture enrichment",
        )
    output = root / "reports/generated"
    output.mkdir(parents=True)
    paths = {
        "candidate": output / "candidate.tsv",
        "sidecar": output / "sidecar.tsv",
        "manifest": output / "manifest.json",
    }
    temporary = root / "temporary"
    temporary.mkdir(exist_ok=True)
    executable_dir = root / "native-tools"
    executable_dir.mkdir()
    (executable_dir / "sssom").symlink_to(Path(sys.executable).parent / "sssom")
    env = dict(
        os.environ,
        MEDIAINGREDIENTMECH_ROOT=str(root),
        KGMICROBE_ROOT=str(kg),
        TMPDIR=str(temporary),
        OPENCLAW_WORKSPACE=str(root / "private-openclaw"),
        PYTHONDONTWRITEBYTECODE="1",
        PATH=str(executable_dir) + ":/usr/bin:/bin",
        HTTPS_PROXY="http://127.0.0.1:9",
        HTTP_PROXY="http://127.0.0.1:9",
        NO_PROXY="",
    )
    command = [
        sys.executable,
        "-B",
        str(claw / "scripts/build_mim_ingredient_sssom.py"),
        "--output",
        str(paths["candidate"]),
        "--suppressed-aliases-output",
        str(paths["sidecar"]),
        "--generation-manifest-output",
        str(paths["manifest"]),
        "--prior-stamps-from",
        str(root / c.SOURCE),
    ]
    run = subprocess.run(command, cwd=root, env=env, capture_output=True, text=True)
    h.put(root, "reports/generated/run.log", (run.stdout + run.stderr).encode())
    h.put(
        root,
        "reports/generated/run.json",
        {
            "argv": command,
            "exit_code": run.returncode,
            "label_provider_condition": "Native documented stored-label fallback: runoak unavailable and explicit unavailable local proxy; no native function replacement",
            "source_receipt_sha256": c.sha(owner_receipt.read_bytes()),
        },
    )
    assert run.returncode == 0, run.stdout + run.stderr
    candidate = paths["candidate"].read_bytes()
    diagnostic = paths["sidecar"].read_bytes()
    selected_subjects = {c.subject(op["source_record"]) for op in operations}
    old_rows = c.table(before["canonical"])[2]
    new_rows = c.table(candidate)[2]
    old_slots = {
        c.slot(r): i for i, r in enumerate(old_rows, 1) if r["subject_id"] in selected_subjects
    }
    new_slots = {
        c.slot(r): i for i, r in enumerate(new_rows, 1) if r["subject_id"] in selected_subjects
    }
    by_subject = {c.subject(op["source_record"]): op["source_record"] for op in operations}
    publication = {
        "schema_version": 2,
        "kind": "unmatched_campaign_publication_v2",
        "issue": c.ISSUE,
        "approval": "NONE",
        "batch": "issue1174-private-four-suppression",
        "scope": "Private real native integration only; no production/source scientific approval",
        "owner_plan": plan_ref,
        "owner_receipt": {
            "path": owner_receipt.relative_to(root).as_posix(),
            "sha256": c.sha(owner_receipt.read_bytes()),
        },
        "publication_producers": {p: c.sha(f.content) for p, f in c.LOADED_PRODUCERS.items()},
        "before": {k: h.put(root, "reports/publication-before/" + k, v) for k, v in before.items()},
        "generation": {
            **{
                k: {"path": v.relative_to(root).as_posix(), "sha256": c.sha(v.read_bytes())}
                for k, v in paths.items()
            },
            "producer_root": str(claw),
            "kg_root": str(kg),
        },
        "receipt_prefix": checkpoint["receipt_inputs"],
        "native_context": {p: c.sha((root / p).read_bytes()) for p in c.native.HISTORICAL_CONTEXT},
        "rows": [
            {
                "owner": by_subject[key[0]],
                "before_position": old_slots.get(key),
                "native_position": new_slots.get(key),
                "preserve_fields": [],
            }
            for key in sorted(old_slots.keys() | new_slots.keys())
        ],
    }
    canonical, _ = c.row_projection(
        before["canonical"], candidate, proof["records"], publication["rows"]
    )
    capture = c.Capture(root)
    candidate, diagnostic, _ = c._generation(
        capture, publication, before["canonical"], proof["after_inventory"]
    )
    needs = [r for r in c._suppression_table(diagnostic)[0] if r["subject_id"] in selected_subjects]
    assert len(needs) == 4
    case = (
        root,
        capture,
        publication,
        before,
        proof,
        diagnostic,
        canonical,
        needs,
        original_review,
        original_document,
    )
    h.reviewed_selection(case)
    publication_ref = h.put(root, "reports/publication-plan.json", publication)
    destination = root / (
        "reports/publication-suppression" if prior_native else "reports/publication"
    )
    destination.mkdir()
    return publication, root / publication_ref["path"], destination, before, proof


def test_real_four_suppressions_source_generation_publication_and_historical_replay(tmp_path):
    plan, path, destination, before, proof = real_case(tmp_path)
    result = c.publish(tmp_path, path, destination, apply=True)
    assert result["status"] == "complete"
    sidecar = (tmp_path / c.SIDECAR).read_bytes()
    assert sidecar.startswith(before["sidecar"]) and len(c._suppression_table(sidecar)[0]) == 38
    assert (tmp_path / c.BASELINE).read_bytes() == before["baseline"]
    assert (destination / "sidecar-before.tsv").read_bytes() == before["sidecar"]
    old_policy, new_policy = json.loads(before["policy"]), json.loads(
        (tmp_path / c.POLICY).read_bytes()
    )
    assert new_policy["source_owner_sha256"] == old_policy["source_owner_sha256"]
    assert len(new_policy["source_owner_sha256"]) == 2955
    assert all(
        new_policy[k] == v for k, v in old_policy.items() if k not in {"artifacts", c.UPDATE}
    )
    update = new_policy[c.UPDATE][-1]
    assert update["schema_version"] == 2 and "mapping_receipt" not in update
    assert update["native_mapping_receipt"] == {
        "path": result["receipt_path"],
        "sha256": result["receipt_sha256"],
    }
    receipt = c.read_json((tmp_path / result["receipt_path"]).read_bytes())
    selected = {c.subject(op["source_record"]) for op in proof["records"]}
    old_table, new_table = c.table(before["canonical"]), c.table((tmp_path / c.SOURCE).read_bytes())
    for index, row in enumerate(old_table[2]):
        if row["subject_id"] not in selected:
            destination_index = receipt["position_map"][index] - 1
            assert new_table[2][destination_index] == row
            assert new_table[3][destination_index] == old_table[3][index]
    assert len(c.native.verify_mapping_chain(tmp_path)["receipts"]) == 28
    assert owner.hashes(owner.inventory(tmp_path)) == proof["after_inventory"]
    assert c.validate(tmp_path, path)["status"] == "verified"
    git(
        tmp_path,
        "-c",
        "user.name=Fixture",
        "-c",
        "user.email=fixture@example.invalid",
        "commit",
        "--allow-empty",
        "-qm",
        "Later historical replay checkpoint",
    )
    assert c.validate(tmp_path, path)["status"] == "verified"


def test_real_completed_native_suffix_then_suppression_preserves_original_27(tmp_path):
    plan, path, destination, before, proof = real_case(tmp_path, prior_native=True)
    assert len(plan["receipt_prefix"]) == 28
    native_proof = c.native.verify_mapping_chain(tmp_path)
    assert [r["sequence"] for r in native_proof["receipts"]] == list(range(1, 29))
    last = tmp_path / native_proof["receipt_paths"][-1]
    original = tmp_path / native_proof["receipt_paths"][0]
    for fault in (
        "tampered-original",
        "disconnected-suffix",
        "missing-suffix",
        "undeclared-suffix",
    ):
        old_original, old_last, old_plan = (
            original.read_bytes(),
            last.read_bytes(),
            path.read_bytes(),
        )
        try:
            if fault == "tampered-original":
                original.write_bytes(old_original + b"\n")
            elif fault == "disconnected-suffix":
                value = c.read_json(old_last)
                value["before_sha256"] = "f" * 64
                last.write_bytes(c.encoded(value))
            elif fault == "missing-suffix":
                last.unlink()
            else:
                value = copy.deepcopy(plan)
                value["receipt_prefix"].pop(last.relative_to(tmp_path).as_posix())
                path.write_bytes(c.encoded(value))
            with pytest.raises((ValueError, FileNotFoundError)):
                c.prepare(tmp_path, path)
            assert not (destination / "publication.json").exists()
            assert all(
                (tmp_path / p).read_bytes() == before[k]
                for k, p in (("canonical", c.SOURCE), ("policy", c.POLICY), ("sidecar", c.SIDECAR))
            )
        finally:
            original.write_bytes(old_original)
            last.write_bytes(old_last)
            path.write_bytes(old_plan)
    assert c.publish(tmp_path, path, destination, apply=True)["status"] == "complete"
    completed = c.native.verify_mapping_chain(tmp_path)
    assert len(completed["receipts"]) == 29
    assert all(completed["receipt_inputs"].get(p) == h for p, h in plan["receipt_prefix"].items())
    assert (tmp_path / c.SIDECAR).read_bytes().startswith(before["sidecar"])
    assert len(c._suppression_table((tmp_path / c.SIDECAR).read_bytes())[0]) == 38
    assert c.validate(tmp_path, path)["status"] == "verified"


@pytest.mark.parametrize("fault", ["existing-third-backup", "aliased-sidecar"])
def test_third_destination_preflight_refuses_without_publication(tmp_path, fault):
    plan, path, destination, before, _ = real_case(tmp_path)
    if fault == "existing-third-backup":
        (destination / "sidecar-before.tsv").write_bytes(b"unrelated existing artifact\n")
    else:
        os.link(tmp_path / c.SIDECAR, tmp_path / "sidecar-hardlink.tsv")
    with pytest.raises(ValueError):
        c.publish(tmp_path, path, destination, apply=True)
    assert all(
        (tmp_path / p).read_bytes() == before[key]
        for key, p in (("canonical", c.SOURCE), ("policy", c.POLICY), ("sidecar", c.SIDECAR))
    )
    assert not (destination / "publication.json").exists()
    assert not (tmp_path / c.native.RECEIPTS_DIR / (plan["batch"] + ".json")).exists()


@pytest.mark.parametrize(
    "fault",
    [
        "review-after-canonical",
        "third-destination-failure",
        "sidecar-backup-before-finish",
        "sidecar-backup-after-finish",
        "owner-membership-after-finish",
        "head-after-finish",
    ],
)
def test_real_third_target_and_review_boundaries_clear_success_receipts(
    tmp_path, monkeypatch, fault
):
    plan, path, destination, before, _ = real_case(tmp_path)
    original_publish, original_finish = c.publish_validated, c.finish_receipt
    touched = False

    def publication(current, render, check):
        nonlocal touched
        if fault == "third-destination-failure" and current.path == tmp_path / c.SIDECAR:
            touched = True
            raise RuntimeError("injected third-destination failure")
        result = original_publish(current, render, check)
        if fault == "review-after-canonical" and current.path == tmp_path / c.SOURCE:
            touched = True
            selection = c.read_json((tmp_path / plan["suppression_review"]["path"]).read_bytes())
            review_file = tmp_path / selection["transition_review"]["yaml"]["path"]
            review_file.write_bytes(
                review_file.read_bytes() + b"\n# changed after canonical write\n"
            )
        return result

    def completion(*args, **kwargs):
        nonlocal touched
        backup = destination / "sidecar-before.tsv"
        if fault == "sidecar-backup-before-finish":
            touched = True
            backup.write_bytes(b"same-inode corruption\n")
        result = original_finish(*args, **kwargs)
        if fault == "sidecar-backup-after-finish":
            touched = True
            backup.write_bytes(b"late same-inode corruption\n")
        elif fault == "owner-membership-after-finish":
            touched = True
            (tmp_path / "data/ingredients/mapped/Unexpected.yaml").write_bytes(
                b"identifier: CHEBI:1\npreferred_term: Unexpected\nmapping_status: MAPPED\n"
            )
        elif fault == "head-after-finish":
            touched = True
            git(
                tmp_path,
                "-c",
                "user.name=Fixture",
                "-c",
                "user.email=fixture@example.invalid",
                "commit",
                "--allow-empty",
                "-qm",
                "Injected intervening commit",
            )
        return result

    monkeypatch.setattr(c, "publish_validated", publication)
    monkeypatch.setattr(c, "finish_receipt", completion)
    with pytest.raises((ValueError, RuntimeError)):
        c.publish(tmp_path, path, destination, apply=True)
    assert touched
    assert (destination / "publication.json").read_bytes() == b""
    assert (tmp_path / c.native.RECEIPTS_DIR / (plan["batch"] + ".json")).read_bytes() == b""
    assert (tmp_path / c.BASELINE).read_bytes() == before["baseline"]
    for name, expected in plan["receipt_prefix"].items():
        assert c.sha((tmp_path / name).read_bytes()) == expected
    if fault in {"review-after-canonical", "third-destination-failure"}:
        assert (tmp_path / c.SIDECAR).read_bytes() == before["sidecar"]
    if not fault.startswith("sidecar-backup"):
        assert (destination / "sidecar-before.tsv").read_bytes() == before["sidecar"]
