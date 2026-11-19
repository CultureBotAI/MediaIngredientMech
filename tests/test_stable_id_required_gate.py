"""#1278: the existing required job must reject a schema-valid ledger rewrite."""

import shlex
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/validate-strict.yaml"


def history_command():
    workflow = yaml.load(WORKFLOW.read_text(), Loader=yaml.BaseLoader)
    steps = workflow["jobs"]["validate-strict"]["steps"]
    commands = [
        step["run"] for step in steps if "scripts/validate_stable_ids.py" in step.get("run", "")
    ]
    assert len(commands) == 1
    return shlex.split(commands[0])


def test_required_job_fetches_history_and_uses_trusted_event_base():
    workflow = yaml.load(WORKFLOW.read_text(), Loader=yaml.BaseLoader)
    assert "data/ids/**" in workflow["on"]["push"]["paths"]
    steps = workflow["jobs"]["validate-strict"]["steps"]
    checkout = next(s for s in steps if s.get("uses", "").startswith("actions/checkout@"))
    assert checkout["with"]["fetch-depth"] == "0"
    assert workflow["env"]["MIM_ID_BASE"] == (
        "${{ github.event.pull_request.base.sha || github.event.merge_group.base_sha || "
        "github.event.before || (github.event_name == 'workflow_dispatch' && github.sha) || 'INVALID-ID-BASE' }}"
    )
    command = history_command()
    assert "--require-history" in command
    assert command[command.index("--base") + 1] == "$MIM_ID_BASE"


def test_required_command_rejects_same_schema_registry_rewrite(tmp_path):
    from mediaingredientmech.stable_ids import Mint, Registry, dump_lifecycle, dump_registry

    registry = Registry((Mint("MIM:0000001", "Fixture", "2026-11-08"),))
    ids = tmp_path / "data/ids"
    ids.mkdir(parents=True)
    ledger = ids / "mim_id_registry.tsv"
    ledger.write_bytes(dump_registry(registry))
    (ids / "mim_id_lifecycle.tsv").write_bytes(dump_lifecycle(registry))
    (tmp_path / "data/ingredients/unmapped").mkdir(parents=True)
    mapped = tmp_path / "data/ingredients/mapped"
    mapped.mkdir(parents=True)
    (mapped / "fixture.yaml").write_text(
        "mim_id: MIM:0000001\npreferred_term: Fixture\nidentifier: CHEBI:1\n"
    )
    for args in [
        ("init",),
        ("config", "user.name", "Fixture"),
        ("config", "user.email", "fixture@example.invalid"),
        ("add", "data"),
        ("commit", "-qm", "trusted minted inventory"),
    ]:
        subprocess.run(["git", *args], cwd=tmp_path, check=True, capture_output=True)
    base = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=tmp_path, text=True).strip()
    parts = history_command()
    script_index = parts.index("scripts/validate_stable_ids.py")
    command = [
        sys.executable,
        str(ROOT / parts[script_index]),
        *[base if p == "$MIM_ID_BASE" else p for p in parts[script_index + 1 :]],
        "--root",
        str(tmp_path),
    ]
    control = subprocess.run(command, capture_output=True, text=True)
    assert control.returncode == 0, control.stderr
    ledger.write_bytes(ledger.read_bytes().replace(b"2026-11-08", b"2026-11-09"))
    current = subprocess.run(
        [sys.executable, str(ROOT / "scripts/validate_stable_ids.py"), "--root", str(tmp_path)],
        capture_output=True,
        text=True,
    )
    assert current.returncode == 0, current.stderr
    rewritten = subprocess.run(command, capture_output=True, text=True)
    assert rewritten.returncode == 1
    assert "rewrites or removes" in rewritten.stderr
