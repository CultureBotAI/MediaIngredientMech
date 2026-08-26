"""Regression coverage for worktree-safe composite QC orchestration (#462)."""

from __future__ import annotations

import importlib.util
import os
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "run_shared_evidence_validator.py"


def _load_adapter():
    spec = importlib.util.spec_from_file_location("run_shared_evidence_validator", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _git(*args: str, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=cwd,
        check=True,
        capture_output=True,
        text=True,
        env={**os.environ, "GIT_CONFIG_NOSYSTEM": "1"},
    )


def _make_primary_and_worktree(tmp_path: Path) -> tuple[Path, Path, Path]:
    group = tmp_path / "group"
    primary = group / "MediaIngredientMech"
    primary.mkdir(parents=True)
    shutil.copy2(ROOT / "justfile", primary / "justfile")
    _git("init", cwd=primary)
    _git("config", "user.email", "worktree-test@example.org", cwd=primary)
    _git("config", "user.name", "Worktree Test", cwd=primary)
    _git("add", "justfile", cwd=primary)
    _git("commit", "-m", "fixture", cwd=primary)
    worktree = tmp_path / "linked-worktree"
    _git("worktree", "add", "--detach", str(worktree), cwd=primary)
    claw = group / "culturebotai-claw"
    return primary, worktree, claw


def test_resolver_finds_claw_beside_primary_checkout_from_linked_worktree(tmp_path: Path) -> None:
    adapter = _load_adapter()
    _, worktree, claw = _make_primary_and_worktree(tmp_path)
    validator = claw / "scripts" / "validate_evidence_references.py"
    validator.parent.mkdir(parents=True)
    validator.write_text("def main(): return 0\n", encoding="utf-8")

    assert adapter.resolve_validator(worktree, env={}) == validator


def test_bad_explicit_override_fails_loudly_instead_of_falling_back(tmp_path: Path) -> None:
    adapter = _load_adapter()
    _, worktree, claw = _make_primary_and_worktree(tmp_path)
    valid = claw / "scripts" / "validate_evidence_references.py"
    valid.parent.mkdir(parents=True)
    valid.write_text("def main(): return 0\n", encoding="utf-8")

    with pytest.raises(adapter.SharedValidatorNotFound, match="CLAW_ROOT points to"):
        adapter.resolve_validator(worktree, env={"CLAW_ROOT": str(tmp_path / "missing")})


def test_adapter_binds_inputs_and_reports_to_active_worktree(tmp_path: Path) -> None:
    adapter = _load_adapter()
    mim = tmp_path / "active-mim-worktree"
    mim.mkdir()
    claw = tmp_path / "claw"
    validator = claw / "scripts" / "validate_evidence_references.py"
    validator.parent.mkdir(parents=True)
    validator.write_text(
        "from pathlib import Path\n"
        "REPO_ROOT = Path(__file__).resolve().parent.parent\n"
        "MIM_ROOT = REPO_ROOT.parent / 'MediaIngredientMech'\n"
        "CACHE_DIR = MIM_ROOT / 'references_cache'\n"
        "INGREDIENTS = MIM_ROOT / 'data' / 'ingredients'\n"
        "OUT_DIR = REPO_ROOT / 'workspace' / 'reports'\n"
        "OUT_TSV = OUT_DIR / 'evidence_reference_validation.tsv'\n"
        "OUT_MD = OUT_DIR / 'evidence_reference_validation.md'\n"
        "def main():\n"
        "    OUT_DIR.mkdir(parents=True, exist_ok=True)\n"
        "    OUT_TSV.write_text(str(MIM_ROOT), encoding='utf-8')\n"
        "    OUT_MD.write_text(str(INGREDIENTS), encoding='utf-8')\n"
        "    return 0\n",
        encoding="utf-8",
    )

    assert adapter.run(mim, env={"CLAW_ROOT": str(claw)}) == 0
    reports = mim / "workspace" / "reports"
    assert (reports / "evidence_reference_validation.tsv").read_text() == str(mim)
    assert (reports / "evidence_reference_validation.md").read_text() == str(
        mim / "data" / "ingredients"
    )
    assert not (claw / "workspace").exists()


def test_composite_recipe_is_frozen_from_unactivated_temporary_worktree(tmp_path: Path) -> None:
    just = shutil.which("just")
    if just is None:
        pytest.skip("just is not installed")
    _, worktree, _ = _make_primary_and_worktree(tmp_path)
    env = os.environ.copy()
    env.pop("VIRTUAL_ENV", None)

    result = subprocess.run(
        [just, "--dry-run", "qc"],
        cwd=worktree,
        env=env,
        check=True,
        capture_output=True,
        text=True,
    )

    commands = result.stdout + result.stderr
    assert "python3 scripts/" not in commands
    for script in (
        "validate_all.py",
        "validate_strict.py",
        "run_shared_evidence_validator.py",
        "validate_sssom_invariants.py",
        "aggregate_records.py",
        "verify_roundtrip.py",
        "export_individual_records.py",
        "audit_duplicate_identifiers.py",
        "validate_component_partonomy.py",
        "check_flat_export_coverage.py",
        "check_instruction_refs.py",
        "check_curation_targets.py",
    ):
        assert f"uv run --frozen python scripts/{script}" in commands


def test_evidence_ci_uses_the_same_active_checkout_adapter() -> None:
    workflow = (ROOT / ".github" / "workflows" / "qc-evidence.yaml").read_text(
        encoding="utf-8"
    )

    assert "working-directory: MediaIngredientMech" in workflow
    assert "CLAW_ROOT: ${{ github.workspace }}/culturebotai-claw" in workflow
    assert "uv run --frozen python scripts/run_shared_evidence_validator.py" in workflow
    assert "MediaIngredientMech/workspace/reports/evidence_reference_validation.tsv" in workflow
    assert "culturebotai-claw/workspace/reports/evidence_reference_validation.tsv" not in workflow
