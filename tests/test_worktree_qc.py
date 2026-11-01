"""Worktree-safe QC and the pinned evidence runner (Claw #687, MIM #462).

Fixtures create local Git repositories and an observable validator dispatcher;
they perform no research, source fetching or scientific evidence validation.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "run_shared_evidence_validator.py"


def _git(*args: str, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-c", "core.hooksPath=/dev/null", "-c", "commit.gpgsign=false", *args],
        cwd=cwd, check=True, capture_output=True, text=True,
        env={key: value for key, value in os.environ.items() if not key.startswith("GIT_")},
    )


def _init(root: Path, identity: str) -> None:
    root.mkdir(parents=True)
    _git("init", "-b", "main", cwd=root)
    _git("config", "user.email", "fixture@example.invalid", cwd=root)
    _git("config", "user.name", "Offline fixture", cwd=root)
    _git("remote", "add", "origin", f"https://github.com/{identity}.git", cwd=root)


def _make_primary_and_worktree(tmp_path: Path) -> tuple[Path, Path, Path]:
    group = tmp_path / "group"
    primary = group / "MediaIngredientMech"
    _init(primary, "CultureBotAI/MediaIngredientMech")
    shutil.copy2(ROOT / "justfile", primary / "justfile")
    _git("add", "justfile", cwd=primary)
    _git("commit", "-m", "fixture", cwd=primary)
    worktree = tmp_path / "linked-worktree"
    _git("worktree", "add", "--detach", str(worktree), cwd=primary)
    return primary, worktree, group / "culturebotai-claw"


@pytest.fixture
def pinned_repositories(tmp_path: Path) -> tuple[Path, Path]:
    claw = tmp_path / "claw"
    _init(claw, "CultureBotAI/culturebotai-claw")
    files = {
        "src/kg_microbe_fleet/fleet.yaml": "fixture: pinned\n",
        "src/kg_microbe_fleet/__init__.py": (
            "from types import SimpleNamespace\n"
            "def load_fleet_manifest(path):\n"
            "    assert path.read_text() == 'fixture: pinned\\n'\n"
            "    mech = SimpleNamespace(key='mediaingredientmech', github='CultureBotAI/MediaIngredientMech')\n"
            "    return SimpleNamespace(mechs={'mediaingredientmech': mech})\n"
        ),
        "plugins/__init__.py": "",
        "plugins/repository_settings.py": (
            "class RepositoryTarget:\n"
            "    def __init__(self, key, root, identity): pass\n"
            "    def open(self): return self\n"
        ),
        "src/kg_microbe_evidence/__init__.py": "",
        "src/kg_microbe_evidence/__main__.py": (
            "import json, os\nfrom pathlib import Path\n"
            "def main(argv):\n"
            "    root = Path(argv[argv.index('--root') + 1])\n"
            "    report = root / 'workspace/reports/fixture.json'\n"
            "    report.parent.mkdir(parents=True, exist_ok=True)\n"
            "    data = {'argv': argv, 'payload': (root / 'payload.txt').read_text()}\n"
            "    report.write_text(json.dumps(data))\n"
            "    print(json.dumps(data))\n"
            "    return int(os.environ.get('EVIDENCE_FIXTURE_EXIT', '0'))\n"
        ),
    }
    for name, text in files.items():
        path = claw / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    _git("add", ".", cwd=claw)
    _git("commit", "-m", "Pinned offline dispatcher", cwd=claw)
    pin = _git("rev-parse", "HEAD", cwd=claw).stdout.strip()

    primary = tmp_path / "primary"
    _init(primary, "CultureBotAI/MediaIngredientMech")
    (primary / "scripts").mkdir()
    shutil.copyfile(SCRIPT, primary / "scripts/run_shared_evidence_validator.py")
    (primary / "scripts/.vendored_canon_ref").write_text(pin + "\n")
    (primary / "payload.txt").write_text("primary checkout")
    _git("add", ".", cwd=primary)
    _git("commit", "-m", "Offline consumer", cwd=primary)
    return primary, claw


def _invoke(root: Path, claw: Path, *args: str, overrides=None):
    environment = os.environ.copy()
    environment.pop("CLAW_SRC", None)
    environment["CLAW_ROOT"] = str(claw)
    environment.update(overrides or {})
    return subprocess.run(
        [sys.executable, "-I", str(root / "scripts/run_shared_evidence_validator.py"), *args],
        env=environment, capture_output=True, text=True, timeout=30,
    )


def test_pinned_runner_binds_inputs_and_reports_to_active_worktree(pinned_repositories, tmp_path):
    primary, claw = pinned_repositories
    active = tmp_path / "active"
    _git("worktree", "add", "--detach", str(active), cwd=primary)
    (active / "payload.txt").write_text("active worktree")
    result = _invoke(active, claw, "--strict")
    assert result.returncode == 0, result.stderr
    observed = json.loads(result.stdout)
    assert observed == {
        "argv": ["--mech", "mediaingredientmech", "--root", str(active), "--strict"],
        "payload": "active worktree",
    }
    assert json.loads((active / "workspace/reports/fixture.json").read_text()) == observed
    assert (primary / "payload.txt").read_text() == "primary checkout"
    assert not (primary / "workspace").exists()
    assert not (claw / "workspace").exists()


def test_missing_explicit_claw_root_has_no_sibling_or_legacy_fallback(pinned_repositories):
    primary, claw = pinned_repositories
    result = _invoke(primary, claw, overrides={"CLAW_ROOT": "", "CLAW_SRC": str(claw / "src")})
    assert result.returncode == 2 and "Set CLAW_ROOT" in result.stderr
    assert not result.stdout


def test_wrong_canonical_revision_is_refused(pinned_repositories):
    primary, claw = pinned_repositories
    _git("commit", "--allow-empty", "-m", "Unpinned revision", cwd=claw)
    result = _invoke(primary, claw)
    assert result.returncode == 2 and "HEAD does not match" in result.stderr
    assert not (primary / "workspace").exists()


def test_shared_validation_failure_is_not_swallowed(pinned_repositories):
    primary, claw = pinned_repositories
    result = _invoke(primary, claw, "--strict", overrides={"EVIDENCE_FIXTURE_EXIT": "2"})
    assert result.returncode == 2
    assert "--strict" in json.loads(result.stdout)["argv"]


def test_composite_recipe_is_frozen_from_unactivated_temporary_worktree(tmp_path: Path) -> None:
    just = shutil.which("just")
    if just is None:
        pytest.skip("just is not installed")
    _, worktree, _ = _make_primary_and_worktree(tmp_path)
    env = os.environ.copy()
    env.pop("VIRTUAL_ENV", None)
    result = subprocess.run(
        [just, "--dry-run", "qc"], cwd=worktree, env=env,
        check=True, capture_output=True, text=True,
    )
    commands = result.stdout + result.stderr
    assert "python3 scripts/" not in commands
    for script in (
        "validate_all.py", "validate_strict.py", "run_shared_evidence_validator.py",
        "validate_sssom_invariants.py", "aggregate_records.py", "verify_roundtrip.py",
        "export_individual_records.py", "audit_duplicate_identifiers.py",
        "validate_component_partonomy.py", "check_flat_export_coverage.py",
        "check_instruction_refs.py", "check_curation_targets.py",
    ):
        assert f"uv run --frozen python scripts/{script}" in commands


def test_evidence_ci_uses_the_same_active_checkout_adapter() -> None:
    workflow = yaml.safe_load((ROOT / ".github/workflows/qc-evidence.yaml").read_text())
    steps = workflow["jobs"]["qc"]["steps"]
    validation = next(step for step in steps if "--strict" in step.get("run", ""))
    assert validation["working-directory"] == "mech"
    assert validation["env"] == {"CLAW_ROOT": "${{ github.workspace }}/claw"}
    assert validation["run"] == (
        "uv run --project ../claw --frozen python -I scripts/run_shared_evidence_validator.py --strict"
    )
    assert any(step.get("run") == "uv sync --project claw --locked" for step in steps)
    summary = steps[-1]
    assert summary["if"] == "always()"
    assert "mech/workspace/reports/evidence_reference_validation.md" in summary["run"]
