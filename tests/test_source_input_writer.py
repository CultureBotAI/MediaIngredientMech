"""Synthetic authority and physical-output tests for #1431; no native runs."""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import json
import os
import platform
import shutil
import subprocess
import sys
from collections import Counter
from copy import deepcopy
from pathlib import Path

import pytest

from mediaingredientmech.curate import publication_guard as guard
from mediaingredientmech.export import source_input_selection as selection
from mediaingredientmech.review_claims import payload_sha256
from tests.test_source_assembly import inputs, raw_table, rows

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "source_input_writer_test_subject", ROOT / "scripts/assemble_source_inputs.py"
)
writer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(writer)


def raw(value):
    return json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, indent=2).encode()


def pin(value):
    return {"sha256": hashlib.sha256(value).hexdigest(), "bytes": len(value)}


def fixture(*, extra_case=False):
    original = inputs(extra_case=extra_case)
    captures = {}

    def save(path, value, binary=False):
        value = value if binary else raw(value)
        captures[path] = value
        return {"path": path, "sha256": pin(value)["sha256"]}

    cm = original["cm"]
    historical = deepcopy(original["historical_obligations"])
    historical["cases"]["OLD:CM"]["source"] = "culturemech"
    crosswalk = deepcopy(original["reviewed_crosswalk"])
    crosswalk["cases"]["OLD:CM"]["original_sha256"] = payload_sha256(historical["cases"]["OLD:CM"])
    authorities = {}
    authorities["original_case_ledger"] = save(
        "original/cases.json", list(historical["cases"].values())
    )
    authorities["original_origin_ledger"] = save(
        "original/origins.json", list(historical["origins"].values())
    )
    authorities["original_eligibility_intake"] = save(
        "original/accounting.json",
        {
            "case_ledger": authorities["original_case_ledger"],
            "cases": [{"case_id": key} for key in historical["cases"]],
            "origins": [{"origin_id": key} for key in historical["origins"]],
            "extra_literal": {"zero": 0, "empty": ""},
        },
    )
    for name in ("nodes", "occurrences"):
        authorities["kg_" + name] = save("kg/" + name + ".tsv", original["kg"][name], True)
    transport = {
        "files": {
            "source-" + name + ".tsv": authorities["kg_" + name]["sha256"]
            for name in ("nodes", "occurrences")
        },
        "inputs": {
            key: {"path": "/literal/historical/" + key, **pin(captures[authorities[role]["path"]])}
            for key, role in (
                ("cases", "original_case_ledger"),
                ("origins", "original_origin_ledger"),
                ("accounting", "original_eligibility_intake"),
            )
        },
        "counts": {
            "original_cases": len(historical["cases"]),
            "original_origins": len(historical["origins"]),
            "kg_cases": len(original["kg"]["cases"]),
        },
    }
    authorities["kg_transport_manifest"] = save("kg/manifest.json", transport)
    for role in (
        "kg_source_manifest",
        "kg_row_reconciliation",
        "kg_full_node_ledger",
        "kg_full_row_ledger_json",
        "kg_full_row_ledger_tsv",
    ):
        authorities[role] = save(
            "authority/" + role + ".json",
            {"literal": [0, "0", "", None], "holds": ["SOURCE_CLAIM", "IDENTITY_FORM"]},
        )
    prepared, reviewed = "prepared", "reviewed"
    source_raw = raw({"literal": "accepted immutable source"})
    packet = {
        "schema_version": 1,
        "source_manifest_sha256": pin(source_raw)["sha256"],
        "canonical_review_sha256": "a" * 64,
        "cases": cm["cases"],
    }
    binding_rows = [
        {"case_id": c["case_id"], "payload_sha256": payload_sha256(c), "disposition": "WITHHOLD"}
        for c in cm["cases"]
    ]
    bindings = raw_table(list(binding_rows[0]), binding_rows)
    pfiles = {
        "review-packet.json": raw(packet),
        "source-mentions.tsv": cm["ordinary"],
        "source-held-mentions.tsv": cm["held"],
    }
    intake = {
        "status": "PREPARED_PENDING_SOURCE_BINDING_REVIEW",
        "source_contract": "culturemech-direct-ingredients-v3",
        "source_manifest_sha256": pin(source_raw)["sha256"],
        "canonical_review_sha256": "a" * 64,
        "files": {k: pin(v) for k, v in pfiles.items()},
        "counts": {"cases": len(cm["cases"])},
    }
    final = {
        "status": "REVIEWED_SOURCE_INTAKE",
        "source_contract": "culturemech-direct-ingredients-v3",
        "intake_sha256": pin(raw(intake))["sha256"],
        "source_manifest_sha256": pin(source_raw)["sha256"],
        "files": {"binding-dispositions.tsv": pin(bindings)},
        "counts": {"WITHHOLD": len(cm["cases"])},
    }
    member_bytes = {"consumer/prepared/" + k: v for k, v in pfiles.items()}
    member_bytes.update(
        {
            "consumer/prepared/intake.json": raw(intake),
            "consumer/reviewed/reviewed-intake.json": raw(final),
            "consumer/prepared/source/bundle/manifest.json": source_raw,
            "consumer/reviewed/binding-dispositions.tsv": bindings,
            "consumer/review.json": raw({"literal": "historical review"}),
        }
    )
    for name, value in member_bytes.items():
        save("cm/" + name, value, True)
    package = {
        "schema_version": 1,
        "status": "ISOLATED_REVIEWED_INTAKE_VERIFICATION_PACKAGE",
        "consumer_commit": "b" * 40,
        "files": {k: pin(v) for k, v in member_bytes.items()},
        "intake_path": prepared,
        "intake_sha256": pin(raw(intake))["sha256"],
        "review_path": "review.json",
        "reviewed_path": reviewed,
        "reviewed_sha256": pin(raw(final))["sha256"],
        "limitations": ["historical only"],
    }
    authorities["culturemech_package"] = save("cm/package.json", package)

    def original_pin(role):
        return {"path": "/literal/absolute/" + role, **pin(captures[authorities[role]["path"]])}

    providers = {case["source"] for case in original["kg"]["cases"]}
    provider_rows = Counter(r["provider"] for r in rows(original["kg"]["occurrences"]))
    provider_cases = Counter(c["source"] for c in original["kg"]["cases"])
    lanes = {
        "positive_inventory": sum(c["positive_occurrences"] for c in cm["cases"]),
        "context_only": sum(c["context_only_mentions"] for c in cm["cases"]),
        "held": sum(c["held_source_mentions"] for c in cm["cases"]),
    }
    owner = {
        "source_receipt": original_pin("kg_source_manifest"),
        "row_reconciliation": original_pin("kg_row_reconciliation"),
        "ledgers": {
            filename: original_pin(role)
            for role, filename in (
                ("kg_full_node_ledger", "full-node-ledger.json"),
                ("kg_full_row_ledger_json", "full-row-ledger.json"),
                ("kg_full_row_ledger_tsv", "full-row-ledger.tsv"),
            )
        },
        "kg_transport_manifest_sha256": authorities["kg_transport_manifest"]["sha256"],
        "row_counts": {
            "provider_cases": len(original["kg"]["cases"]),
            "kg_source_ids": len(rows(original["kg"]["nodes"])),
            "kg_occurrences": len(rows(original["kg"]["occurrences"])),
        },
        "provider_counts": {
            p: {"cases": provider_cases[p], "occurrences": provider_rows[p]} for p in providers
        },
        "intended_accepted_cm_v3": {
            "transport_package": original_pin("culturemech_package"),
            "expected_counts": lanes,
            "selected": {
                name: {"path": "/original/CM/" + name, **pin(value)}
                for name, value in (
                    ("source_manifest", source_raw),
                    ("prepared_intake", raw(intake)),
                    ("reviewed_intake", raw(final)),
                    ("binding_review", member_bytes["consumer/review.json"]),
                )
            },
        },
    }
    authorities["kg_source_selection"] = save("authority/owner.json", owner)
    scope = {
        "profile": selection.PROFILE,
        "authorities": authorities,
        "artifacts": {role: "output/" + name for role, name in selection.ARTIFACT_NAMES.items()},
    }
    declaration = json.loads(cm["declaration"])
    declaration["original_source_scope"] = deepcopy(scope)
    controls = {
        "declaration": save("controls/declaration.json", writer.encoded(declaration), True),
        "reviewed_crosswalk": save("controls/crosswalk.json", crosswalk),
        "curie_map": save("controls/prefixes.json", original["curie_map"]),
    }
    return {
        "captures": captures,
        "scope": scope,
        "controls": controls,
        "original": historical,
        "crosswalk": crosswalk,
    }


def select(data):
    return selection.select_source_inputs(
        data["captures"],
        selected_scope=data["scope"],
        declaration=data["captures"][data["controls"]["declaration"]["path"]],
        declaration_path="output/projection-declaration.json",
        reviewed_crosswalk=data["captures"][data["controls"]["reviewed_crosswalk"]["path"]],
        curie_map=data["captures"][data["controls"]["curie_map"]["path"]],
    )


def plan_at(root, data):
    for name, value in data["captures"].items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(value)
    plan = {
        "schema_version": 1,
        "head": "test-only",
        "implementation": {},
        "runtime": {},
        "scope": deepcopy(data["scope"]),
        **data["controls"],
        "output_directory": "output",
        "inputs": {name: pin(value) for name, value in data["captures"].items()},
    }
    return plan


def context(plan):
    from mediaingredientmech.export import source_assembly, source_conservation

    return {
        "modules": {
            "source_input_selection": selection,
            "source_assembly": source_assembly,
            "source_conservation": source_conservation,
        },
        "frozen": {},
        "selection_raw": raw(plan),
    }


@pytest.mark.parametrize("extra", [False, True])
def test_complete_raw_authorities_and_literal_payloads(extra):
    data = fixture(extra_case=extra)
    before = deepcopy(data)
    selected = select(data)
    assert selected["historical_obligations"] == data["original"]
    assert selected["reviewed_crosswalk"] == data["crosswalk"]
    assert all(case["holds"] == ["IDENTITY_FORM"] for case in selected["kg"]["cases"])
    assert set(selected["consumed_inputs"]) == set(data["captures"]) - {
        r["path"] for r in data["controls"].values()
    }
    selected["historical_obligations"]["cases"]["OLD:CM"]["holds"].append("changed copy")
    assert data == before


@pytest.mark.parametrize("role", sorted(selection.AUTHORITY_ROLES))
def test_each_independent_authority_pin_refuses_tamper(role):
    data = fixture()
    path = data["scope"]["authorities"][role]["path"]
    data["captures"][path] += b" "
    with pytest.raises(ValueError, match="bytes differ"):
        select(data)


def test_coherent_candidate_forgery_cannot_replace_independent_selection():
    data = fixture()
    original = deepcopy(data["scope"])
    path = data["scope"]["authorities"]["kg_source_selection"]["path"]
    owner = json.loads(data["captures"][path])
    owner["unreviewed_extra"] = "forged"
    data["captures"][path] = raw(owner)
    forged = deepcopy(original)
    forged["authorities"]["kg_source_selection"]["sha256"] = pin(raw(owner))["sha256"]
    declaration_path = data["controls"]["declaration"]["path"]
    declaration = json.loads(data["captures"][declaration_path])
    declaration["original_source_scope"] = forged
    data["captures"][declaration_path] = writer.encoded(declaration)
    assert data["scope"] == original
    with pytest.raises(ValueError, match="bytes differ"):
        select(data)


def test_declaration_cannot_reselect_authorities_or_add_generated_hash():
    data = fixture()
    path = data["controls"]["declaration"]["path"]
    declaration = json.loads(data["captures"][path])
    declaration["original_source_scope"]["artifacts"]["cm_nodes"] = "elsewhere.tsv"
    data["captures"][path] = writer.encoded(declaration)
    with pytest.raises(ValueError, match="independent selected"):
        select(data)
    data = fixture()
    data["scope"]["artifacts"]["cm_nodes"] = {"path": "output/nodes.tsv", "sha256": "a" * 64}
    with pytest.raises(ValueError, match="path"):
        select(data)


@pytest.mark.parametrize("change", ["extra", "missing", "overlap"])
def test_profile_closed_membership(change):
    data = fixture()
    if change == "extra":
        data["scope"]["authorities"]["forged"] = {"path": "x", "sha256": "a" * 64}
    elif change == "missing":
        del data["scope"]["artifacts"]["kg_provider_cases"]
    else:
        data["scope"]["artifacts"]["cm_nodes"] = data["scope"]["authorities"]["kg_nodes"]["path"]
    with pytest.raises(ValueError):
        select(data)


def test_unrelated_captured_input_is_visible_not_silently_consumed():
    data = fixture()
    data["captures"]["unrelated.json"] = b"{}"
    assert "unrelated.json" not in select(data)["consumed_inputs"]


@pytest.mark.parametrize("role", ["culturemech_package", "original_case_ledger", "kg_nodes"])
def test_role_rehash_cannot_disagree_with_original_owner_transport(role):
    data = fixture()
    ref = data["scope"]["authorities"][role]
    data["captures"][ref["path"]] += b" "
    ref["sha256"] = pin(data["captures"][ref["path"]])["sha256"]
    path = data["controls"]["declaration"]["path"]
    declaration = json.loads(data["captures"][path])
    declaration["original_source_scope"] = deepcopy(data["scope"])
    data["captures"][path] = writer.encoded(declaration)
    with pytest.raises(ValueError, match="authority differs|KG family pin differs"):
        select(data)


@pytest.mark.parametrize("bad", [b'{"cases":{},"cases":{}}', b'{"number":NaN}', b'{"broken":'])
def test_supplied_control_json_is_not_silently_repaired(bad):
    data = fixture()
    data["captures"][data["controls"]["reviewed_crosswalk"]["path"]] = bad
    with pytest.raises(ValueError):
        select(data)


def test_dropped_original_obligation_refuses_source_only_completion(tmp_path):
    data = fixture()
    path = data["controls"]["reviewed_crosswalk"]["path"]
    crosswalk = json.loads(data["captures"][path])
    del crosswalk["cases"]["OLD:CM"]
    data["captures"][path] = raw(crosswalk)
    data["controls"]["reviewed_crosswalk"]["sha256"] = pin(raw(crosswalk))["sha256"]
    plan = plan_at(tmp_path, data)
    with pytest.raises(ValueError, match="historical obligation key loss"):
        writer.execute(tmp_path, plan, context(plan), guard)
    assert (
        json.loads((tmp_path / "output/manifest.json").read_bytes())["status"]
        == "FAILED_SOURCE_INPUT_PREPARATION"
    )


@pytest.mark.parametrize("extra", [False, True])
def test_writer_actual_readback_and_complete_manifest(tmp_path, extra):
    data = fixture(extra_case=extra)
    plan = plan_at(tmp_path, data)
    before = {p: (tmp_path / p).read_bytes() for p in data["captures"]}
    manifest = writer.execute(tmp_path, plan, context(plan), guard)
    assert manifest["status"] == "SOURCE_INPUTS_ASSEMBLED_UNREVIEWED"
    assert (
        manifest["scientific_approval"]
        is manifest["native_conservation"]
        is manifest["publication_authorized"]
        is False
    )
    assert {p.name for p in (tmp_path / "output").iterdir()} == writer.NAMES
    for name, expected in manifest["files"].items():
        assert pin((tmp_path / "output" / name).read_bytes()) == expected
    assert (
        json.loads((tmp_path / "output/historical-obligations.json").read_bytes())
        == data["original"]
    )
    assert (tmp_path / "output/obligation-crosswalk.json").read_bytes() == data["captures"][
        data["controls"]["reviewed_crosswalk"]["path"]
    ]
    assert manifest["accounting"]["kg_occurrences"] == 5
    assert manifest["accounting"]["cm_lanes"] == {
        "positive_inventory": 3 + int(extra),
        "context_only": 1,
        "held": 1,
    }
    assert {p: (tmp_path / p).read_bytes() for p in before} == before
    assert "exit_code" not in manifest


@pytest.mark.parametrize("kind", ["extra_input", "bad_pin", "alias", "hardlink", "overlap"])
def test_writer_capture_refusals(tmp_path, kind):
    data = fixture()
    plan = plan_at(tmp_path, data)
    path = next(iter(data["captures"]))
    if kind == "extra_input":
        (tmp_path / "extra").write_bytes(b"{}")
        plan["inputs"]["extra"] = pin(b"{}")
    elif kind == "bad_pin":
        plan["inputs"][path]["sha256"] = "0" * 64
    elif kind == "alias":
        original = tmp_path / path
        moved = original.with_name("moved")
        original.rename(moved)
        original.symlink_to(moved)
    elif kind == "hardlink":
        os.link(tmp_path / path, tmp_path / "linked")
    else:
        plan["output_directory"] = path
    with pytest.raises((ValueError, OSError)):
        writer.execute(tmp_path, plan, context(plan), guard)
    assert not (tmp_path / "output").exists()


@pytest.mark.parametrize("kind", ["existing", "symlink", "ancestor_symlink"])
def test_output_exclusive_directory(tmp_path, kind):
    target = tmp_path / "output"
    if kind == "existing":
        target.mkdir()
    elif kind == "symlink":
        target.symlink_to(tmp_path, target_is_directory=True)
    else:
        (tmp_path / "alias").symlink_to(tmp_path, target_is_directory=True)
        target = tmp_path / "alias/output"
    with pytest.raises((ValueError, OSError)):
        writer.Output(target, guard)


@pytest.mark.parametrize(
    "kind",
    ["directory", "ancestor", "leaf", "symlink", "hardlink", "mode", "bytes", "extra", "missing"],
)
def test_output_drift_refuses_and_preserves_external_targets(tmp_path, kind):
    parent = tmp_path / "parent"
    parent.mkdir()
    output = writer.Output(parent / "output", guard)
    external = tmp_path / "external"
    external.write_bytes(b"untouched")
    leaf = parent / "output/source-nodes.tsv"
    try:
        output.write("source-nodes.tsv", b"original")
        if kind == "directory":
            (parent / "output").rename(parent / "old")
            (parent / "output").mkdir()
        elif kind == "ancestor":
            parent.rename(tmp_path / "old-parent")
            parent.mkdir()
        elif kind == "leaf":
            leaf.unlink()
            leaf.write_bytes(b"replacement")
        elif kind == "symlink":
            leaf.unlink()
            leaf.symlink_to(external)
        elif kind == "hardlink":
            os.link(leaf, tmp_path / "alias")
        elif kind == "mode":
            leaf.chmod(0o640)
        elif kind == "bytes":
            leaf.write_bytes(b"modified")
        elif kind == "extra":
            (parent / "output/extra").write_bytes(b"x")
        else:
            leaf.unlink()
        with pytest.raises((ValueError, OSError, writer.UnsafeOutput)):
            output.verify()
        output.failure(ValueError("detected drift"))
        assert external.read_bytes() == b"untouched"
    finally:
        output.close()


@pytest.mark.parametrize("name", ["source-nodes.tsv", "manifest.json"])
@pytest.mark.parametrize("change", ["mode", "link"])
def test_mode_and_link_changes_during_write_never_become_baseline(
    tmp_path, monkeypatch, name, change
):
    output = writer.Output(tmp_path / "output", guard)
    old_fsync = os.fsync

    def changed(fd):
        old_fsync(fd)
        if change == "mode":
            os.fchmod(fd, 0o640)
        else:
            os.link(tmp_path / "output" / name, tmp_path / "late-hardlink")

    monkeypatch.setattr(writer.os, "fsync", changed)
    try:
        with pytest.raises(writer.UnsafeOutput):
            output.write(name, b"{}")
        assert output.files[name]["state"][2] & 0o777 == 0o600
        with pytest.raises((ValueError, writer.UnsafeOutput)):
            output.verify()
    finally:
        output.close()


def test_partial_write_leaves_no_success_receipt(tmp_path, monkeypatch):
    output = writer.Output(tmp_path / "output", guard)
    original = os.write
    calls = 0

    def partial(fd, value):
        nonlocal calls
        calls += 1
        if calls == 1:
            return original(fd, value[:1])
        raise OSError("synthetic short write")

    monkeypatch.setattr(writer.os, "write", partial)
    try:
        with pytest.raises(OSError):
            output.write("source-nodes.tsv", b"payload")
        output.failure(ValueError("partial"))
        assert (tmp_path / "output/manifest.json").read_bytes() == b""
    finally:
        output.close()


def test_safe_manifest_failure_invalidates_success(tmp_path):
    output = writer.Output(tmp_path / "output", guard)
    try:
        output.write("manifest.json", raw({"status": "SOURCE_INPUTS_ASSEMBLED_UNREVIEWED"}))
        output.failure(ValueError("late input drift"))
        assert (
            json.loads(output.read("manifest.json"))["status"] == "FAILED_SOURCE_INPUT_PREPARATION"
        )
    finally:
        output.close()


def test_unsafe_late_manifest_is_untrusted_and_not_reopened(tmp_path, capsys):
    output = writer.Output(tmp_path / "output", guard)
    try:
        success = raw({"status": "SOURCE_INPUTS_ASSEMBLED_UNREVIEWED"})
        output.write("manifest.json", success)
        (tmp_path / "output").rename(tmp_path / "detached")
        (tmp_path / "output").mkdir()
        replacement = tmp_path / "output/manifest.json"
        replacement.write_bytes(b"external")
        output.failure(ValueError("late lineage loss"))
        assert replacement.read_bytes() == b"external"
        assert (tmp_path / "detached/manifest.json").read_bytes() == success
        assert "no fallback writes" in capsys.readouterr().err
    finally:
        output.close()


def test_input_changed_after_manifest_forces_safe_failure(tmp_path, monkeypatch):
    data = fixture()
    plan = plan_at(tmp_path, data)
    old_write = writer.Output.write

    def change(self, name, value, **kwargs):
        old_write(self, name, value, **kwargs)
        if name == "manifest.json" and not kwargs.get("manifest_replace"):
            (tmp_path / next(iter(data["captures"]))).write_bytes(b"changed")

    monkeypatch.setattr(writer.Output, "write", change)
    with pytest.raises(ValueError, match="Captured input changed"):
        writer.execute(tmp_path, plan, context(plan), guard)
    assert (
        json.loads((tmp_path / "output/manifest.json").read_bytes())["status"]
        == "FAILED_SOURCE_INPUT_PREPARATION"
    )


def test_reader_budget_unchanged_and_oversized_declaration_refuses(tmp_path):
    before = csv.field_size_limit()
    data = fixture()
    path = data["controls"]["declaration"]["path"]
    value = json.loads(data["captures"][path])
    value["original_case_transport"] = "x" * 131073
    data["captures"][path] = writer.encoded(value)
    data["controls"]["declaration"]["sha256"] = pin(data["captures"][path])["sha256"]
    plan = plan_at(tmp_path, data)
    with pytest.raises(ValueError, match="cell"):
        writer.execute(tmp_path, plan, context(plan), guard)
    assert csv.field_size_limit() == before
    assert not (tmp_path / "output").exists()


def test_isolated_cli_uses_exact_committed_sources_and_runtime(tmp_path):
    root = tmp_path / "code"
    root.mkdir()
    for name in writer.CODE:
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / name, path)
    env = {
        **os.environ,
        "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_CONFIG_GLOBAL": os.devnull,
        "GIT_OPTIONAL_LOCKS": "0",
    }
    commands = [
        ["git", "init"],
        ["git", "add", "scripts", "src"],
        [
            "git",
            "-c",
            "user.name=Synthetic fixture",
            "-c",
            "user.email=fixture@example.invalid",
            "-c",
            "commit.gpgsign=false",
            "commit",
            "-m",
            "Synthetic source-input fixture",
        ],
    ]
    for command in commands:
        subprocess.run(command, cwd=root, env=env, check=True, capture_output=True, timeout=30)
    head = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=root,
        env=env,
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    ).stdout.strip()
    data = fixture()
    plan = plan_at(root, data)
    plan.update(
        head=head,
        implementation={name: pin((root / name).read_bytes())["sha256"] for name in writer.CODE},
        runtime={
            "executable": sys.executable,
            "version": platform.python_version(),
            "sha256": pin(Path(sys.executable).resolve().read_bytes())["sha256"],
        },
    )
    plan_raw = raw(plan)
    (root / "selection.json").write_bytes(plan_raw)
    argv = [
        sys.executable,
        "-I",
        "-B",
        str(root / "scripts/assemble_source_inputs.py"),
        "--root",
        str(root),
        "--selection",
        "selection.json",
        "--selection-sha256",
        pin(plan_raw)["sha256"],
    ]
    result = subprocess.run(argv, cwd=root, env=env, capture_output=True, text=True, timeout=30)
    assert result.returncode == 0, result.stderr
    assert json.loads(result.stdout)["status"] == "SOURCE_INPUTS_ASSEMBLED_UNREVIEWED"
    # Import isolation is enforced by the actual -I child, not PYTHONPATH.
    cached = root / "src/mediaingredientmech/export/__pycache__"
    cached.mkdir()
    bytecode = cached / "source_input_selection.cpython-313.pyc"
    bytecode.write_bytes(b"synthetic stale bytecode")
    refused = subprocess.run(argv, cwd=root, env=env, capture_output=True, text=True, timeout=30)
    assert refused.returncode == 1 and "bytecode cache refused" in refused.stderr
    bytecode.unlink()
    injection = (
        "import runpy,sys,types; "
        "sys.modules['mediaingredientmech']=types.ModuleType('mediaingredientmech'); "
        f"sys.argv={argv[3:]!r}; "
        f"runpy.run_path({argv[3]!r},run_name='__main__')"
    )
    refused = subprocess.run(
        [sys.executable, "-I", "-B", "-c", injection],
        cwd=root,
        env=env,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert refused.returncode == 1 and "preloaded MIM code refused" in refused.stderr
    wrong = deepcopy(plan)
    wrong["runtime"]["sha256"] = "0" * 64
    (root / "selection.json").write_bytes(raw(wrong))
    refused = subprocess.run(
        [*argv[:-1], pin(raw(wrong))["sha256"]],
        cwd=root,
        env=env,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert refused.returncode == 1 and "selected runtime differs" in refused.stderr
    (root / "selection.json").write_bytes(plan_raw)
    # The same committed selection cannot conceal an alternate source module.
    module = root / "src/mediaingredientmech/export/source_input_selection.py"
    module.write_bytes(module.read_bytes() + b"\n# changed\n")
    refused = subprocess.run(argv, cwd=root, env=env, capture_output=True, text=True, timeout=30)
    assert refused.returncode == 1 and "implementation bytes differ" in refused.stderr


def test_bootstrap_requires_actual_isolated_flags():
    with pytest.raises(ValueError, match="-I -B"):
        writer.bootstrap(ROOT, ROOT / "unused.json", "0" * 64)


def count_fixture(field=None, value=None):
    """#1553: one selected context case, preserving independently pinned inputs.

    This reproduces the reviewer's tiny positive and six malformed metadata
    cases. Rebinding synthetic metadata is not a replacement of real authority.
    """
    data = fixture()
    cap = data["captures"]
    packet = json.loads(cap["cm/consumer/prepared/review-packet.json"])
    packet["cases"] = packet["cases"][:1]
    case_id = packet["cases"][0]["case_id"]
    cap["cm/consumer/prepared/review-packet.json"] = raw(packet)
    for name in ("source-mentions.tsv", "source-held-mentions.tsv"):
        key = "cm/consumer/prepared/" + name
        fields = next(csv.reader(cap[key].decode().splitlines(), delimiter="\t"))
        cap[key] = raw_table(fields, [row for row in rows(cap[key]) if row["case_id"] == case_id])
    bindings_key = "cm/consumer/reviewed/binding-dispositions.tsv"
    bindings = [row for row in rows(cap[bindings_key]) if row["case_id"] == case_id]
    cap[bindings_key] = raw_table(list(bindings[0]), bindings)
    intake = json.loads(cap["cm/consumer/prepared/intake.json"])
    final = json.loads(cap["cm/consumer/reviewed/reviewed-intake.json"])
    transport = json.loads(cap["kg/manifest.json"])
    owner = json.loads(cap["authority/owner.json"])
    intake["counts"]["cases"] = 1
    final["counts"] = {"WITHHOLD": 1}
    intended = owner["intended_accepted_cm_v3"]
    intended["expected_counts"] = {"positive_inventory": 0, "context_only": 1, "held": 0}
    groups = {
        "intake": intake["counts"],
        "dispositions": final["counts"],
        "transport": transport["counts"],
        "rows": owner["row_counts"],
        "provider": owner["provider_counts"]["microbedecoder"],
        "lanes": intended["expected_counts"],
    }
    if field is not None:
        group, key = field.split(".")
        groups[group][key] = value
    for name in intake["files"]:
        intake["files"][name] = pin(cap["cm/consumer/prepared/" + name])
    cap["cm/consumer/prepared/intake.json"] = raw(intake)
    final["intake_sha256"] = pin(raw(intake))["sha256"]
    final["files"]["binding-dispositions.tsv"] = pin(cap[bindings_key])
    cap["cm/consumer/reviewed/reviewed-intake.json"] = raw(final)
    package = json.loads(cap["cm/package.json"])
    for name in package["files"]:
        package["files"][name] = pin(cap["cm/" + name])
    package["intake_sha256"] = pin(raw(intake))["sha256"]
    package["reviewed_sha256"] = pin(raw(final))["sha256"]
    cap["cm/package.json"] = raw(package)
    cap["kg/manifest.json"] = raw(transport)
    intended["transport_package"].update(pin(cap["cm/package.json"]))
    for name, key in (
        ("prepared_intake", "cm/consumer/prepared/intake.json"),
        ("reviewed_intake", "cm/consumer/reviewed/reviewed-intake.json"),
    ):
        intended["selected"][name].update(pin(cap[key]))
    owner["kg_transport_manifest_sha256"] = pin(cap["kg/manifest.json"])["sha256"]
    cap["authority/owner.json"] = raw(owner)
    for ref in data["scope"]["authorities"].values():
        ref["sha256"] = pin(cap[ref["path"]])["sha256"]
    path = data["controls"]["declaration"]["path"]
    declaration = json.loads(cap[path])
    declaration["original_source_scope"] = deepcopy(data["scope"])
    cap[path] = writer.encoded(declaration)
    data["controls"]["declaration"]["sha256"] = pin(cap[path])["sha256"]
    return data


@pytest.mark.parametrize(
    "field,value",
    [
        ("intake.cases", True),
        ("dispositions.WITHHOLD", True),
        ("transport.original_origins", True),
        ("transport.kg_cases", 4.0),
        ("lanes.context_only", True),
        ("provider.occurrences", True),
    ],
)
def test_1553_six_reviewed_malformed_counts_refuse_before_output(tmp_path, field, value):
    data = count_fixture(field, value)
    plan = plan_at(tmp_path, data)
    with pytest.raises(ValueError, match="metadata counts must be nonnegative integers"):
        writer.execute(tmp_path, plan, context(plan), guard)
    assert not (tmp_path / "output").exists()


@pytest.mark.parametrize(
    "field",
    [
        "intake.cases",
        "dispositions.WITHHOLD",
        "transport.original_cases",
        "transport.original_origins",
        "transport.kg_cases",
        "rows.provider_cases",
        "rows.kg_source_ids",
        "rows.kg_occurrences",
        "provider.cases",
        "provider.occurrences",
        "lanes.positive_inventory",
        "lanes.context_only",
        "lanes.held",
    ],
)
@pytest.mark.parametrize("value", [True, False, 1.0, "1", None, -1])
def test_1553_consumed_count_types_are_not_coerced(field, value):
    with pytest.raises(ValueError, match="metadata counts must be nonnegative integers"):
        select(count_fixture(field, value))


# Exact valid synthetic predecessor data, independently retained for #1553.
COUNT_REPAIR_BASELINE = {
    "cm-case-crosswalk.json": "55aec685059c719d6567988ca9f96eba0427cabfcd8c3809fe9306228cd2b8c8",
    "cm-raw-row-map.json": "6ea037ed880a6dacdcc899a91bb90546a245ababdff778cda89234b6293a6013",
    "cm-reconciliation.tsv": "b567301721532c5e1966bc06af3c0ad7ff4de2932e6bcce5d6f86d2640ea8151",
    "cm-source-nodes.tsv": "be3ff2c42b6804a8cc507cff08784224cea366d2db7965d6758bf053df131500",
    "cm-source-occurrences.tsv": "683c8a009e8ceaeebf8316e705f5cfdc636fa5f3d8c03af76964c5fb3fb4c3ff",
    "combined-position-map.json": "69a4425e5487e200e8450774a402f2fa2d6b120dcf2726049cc0eede7a2967b2",
    "curie-map.json": "b9f3eaef09ed2ef62267c1e96731efdb4a4485d7bb1100a1189ad61d2360aecd",
    "historical-obligations.json": "7783e8134658e7341f9be8bb1d29ba3f236bbe8032f3f029363a2d4878fe37aa",
    "kg-provider-cases.json": "70b3bd29a0965a6b6766bd333e50ff70e0efdb54f8ed662efb5ec022ae29c020",
    "obligation-crosswalk.json": "52bda2ff204b0fc7f5837b4d733767473a71a890a4df881920310125e14c9978",
    "projection-declaration.json": "8fb40ce48d6f3a46a81e3fed951b773f0ab20e9d1fe65e8816619831423adf67",
    "source-nodes.tsv": "9e827ab1504e59beac64c494a6a15f90781ec86deb12cc8b708600d1fd614c34",
    "source-occurrences.tsv": "38d5e844ee63c5aca1a349f6c26b960009ba8e75a8f9d6e3bb04294bd1153c41",
}


def test_1553_valid_integer_zero_one_preserves_predecessor_data(tmp_path):
    data = count_fixture()
    plan = plan_at(tmp_path, data)
    result = writer.execute(tmp_path, plan, context(plan), guard)
    assert result["accounting"]["cm_cases"] == 1
    assert result["accounting"]["cm_lanes"] == {"context_only": 1}
    assert result["scientific_approval"] is result["native_conservation"] is False
    for name, expected in COUNT_REPAIR_BASELINE.items():
        assert pin((tmp_path / "output" / name).read_bytes())["sha256"] == expected


def test_1553_literal_float_zero_null_and_unknown_payloads_survive(tmp_path):
    """Only accounting counts are integers; source quantities remain literal."""
    data = fixture()
    cap = data["captures"]
    ledger = json.loads(cap["original/cases.json"])
    ledger[0]["literal"]["quantities"] = {"amount": 0.125, "zero": 0.0, "unknown": None}
    ledger[0]["occurrence_declaration"] = {"status": "UNKNOWN", "count": None}
    cap["original/cases.json"] = raw(ledger)
    accounting = json.loads(cap["original/accounting.json"])
    accounting["case_ledger"]["sha256"] = pin(cap["original/cases.json"])["sha256"]
    cap["original/accounting.json"] = raw(accounting)
    transport = json.loads(cap["kg/manifest.json"])
    transport["inputs"]["cases"].update(pin(cap["original/cases.json"]))
    transport["inputs"]["accounting"].update(pin(cap["original/accounting.json"]))
    cap["kg/manifest.json"] = raw(transport)
    owner = json.loads(cap["authority/owner.json"])
    owner["kg_transport_manifest_sha256"] = pin(cap["kg/manifest.json"])["sha256"]
    cap["authority/owner.json"] = raw(owner)
    crosswalk_path = data["controls"]["reviewed_crosswalk"]["path"]
    crosswalk = json.loads(cap[crosswalk_path])
    crosswalk["cases"][ledger[0]["case_id"]]["original_sha256"] = payload_sha256(ledger[0])
    cap[crosswalk_path] = raw(crosswalk)
    data["controls"]["reviewed_crosswalk"]["sha256"] = pin(cap[crosswalk_path])["sha256"]
    for ref in data["scope"]["authorities"].values():
        ref["sha256"] = pin(cap[ref["path"]])["sha256"]
    path = data["controls"]["declaration"]["path"]
    declaration = json.loads(cap[path])
    declaration["original_source_scope"] = deepcopy(data["scope"])
    cap[path] = writer.encoded(declaration)
    data["controls"]["declaration"]["sha256"] = pin(cap[path])["sha256"]
    plan = plan_at(tmp_path, data)
    result = writer.execute(tmp_path, plan, context(plan), guard)
    actual = json.loads((tmp_path / "output/kg-provider-cases.json").read_bytes())
    assert writer.encoded(actual[0]) == writer.encoded(ledger[0])
    assert type(actual[0]["literal"]["quantities"]["zero"]) is float
    assert actual[0]["occurrence_declaration"] == {"status": "UNKNOWN", "count": None}
    assert result["scientific_approval"] is result["native_conservation"] is False
