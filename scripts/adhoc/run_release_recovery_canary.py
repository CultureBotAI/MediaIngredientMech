#!/usr/bin/env python3
"""Run one retained native correction/publication canary (#1420/#1423/#1425/#1426).

Purpose: reproduce the genuine source-correction and canonical publication gates
on synthetic owners, without provider calls, campaign writes or release approval.
Inputs: this checkout, an explicit Python 3.13 interpreter and Claw checkout.
Outputs: fresh directory containing command, stdout/stderr, result and fixture
receipts. Original failed runs are never overwritten. Added 2026-11-15.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(root: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


PHASES = [
    "adoption_and_first_correction_verified",
    "second_correction_dry_run_apply_commit_verify",
    "captured_claw_generation_and_native_sssom_validation",
    "canonical_prepare_dry_run_apply_verify_with_history_and_holds",
]


def owned_output(root: Path, selected: Path) -> Path:
    """Reject lexical traversal and existing aliases before creating output (#1428)."""
    output = selected.absolute()
    boundary = root / ".temp"
    if ".." in output.parts or not output.is_relative_to(boundary):
        raise ValueError("output must stay beneath this checkout's .temp")
    if any(path.is_symlink() for path in (output, *output.parents)):
        raise ValueError("output cannot traverse a symlink")
    if not output.resolve().is_relative_to(boundary.resolve()) or output.exists():
        raise ValueError("output must be a new physically owned directory")
    return output


def completed_native_evidence(output: Path) -> None:
    """Require the exact executed test and durable native outcomes (#1427)."""
    cases = list(ET.parse(output / "pytest.xml").getroot().iter("testcase"))
    if (
        len(cases) != 1
        or cases[0].get("name")
        != ("test_two_corrections_publish_independent_assertions_and_keep_holds")
        or any(cases[0].find(tag) is not None for tag in ("skipped", "failure", "error"))
    ):
        raise ValueError("exact native canary did not pass")
    fixture = output / "fixtures"
    progress = list(fixture.rglob("combined-progress.json"))
    if len(progress) != 1 or json.loads(progress[0].read_bytes()).get("completed") != PHASES:
        raise ValueError("complete persisted native phases required")
    for pattern, flag in (
        ("additional-source-application/application.json", "release_approval_added"),
        ("*-additional-applied/application.json", "scientific_approval_added"),
        ("additional-assertion-generation/receipt.json", None),
    ):
        paths = list(fixture.rglob(pattern))
        if len(paths) != 1 or not paths[0].stat().st_size:
            raise ValueError("missing or ambiguous native receipt: " + pattern)
        receipt = json.loads(paths[0].read_bytes())
        if receipt.get("state") != "COMPLETE" or (flag and receipt.get(flag) is not False):
            raise ValueError("native receipt is incomplete or grants approval: " + pattern)
    for pattern in (
        "additional-assertion-generation/candidate.sssom.tsv",
        "additional-assertion-generation/generation.json",
        "mappings/stable_sssom_publication.json",
    ):
        paths = list(fixture.rglob(pattern))
        if not paths or any(not path.stat().st_size for path in paths):
            raise ValueError("nonempty persisted native artifact required: " + pattern)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--python", type=Path, required=True)
    parser.add_argument("--claw-root", type=Path, required=True)
    parser.add_argument("--claw-head", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    claw = args.claw_root.absolute()
    try:
        output = owned_output(root, args.output)
    except ValueError as exc:
        parser.error(str(exc))
    if (
        git(root, "remote", "get-url", "origin")
        != "https://github.com/CultureBotAI/MediaIngredientMech.git"
    ):
        parser.error("unexpected MIM origin")
    if (
        git(claw, "remote", "get-url", "origin")
        != "https://github.com/CultureBotAI/culturebotai-claw.git"
    ):
        parser.error("unexpected Claw origin")
    if git(claw, "rev-parse", "HEAD") != args.claw_head:
        parser.error("Claw HEAD differs from explicit input")
    if git(claw, "diff", "--name-only", "HEAD"):
        parser.error("Claw producer contains uncommitted changes")
    for ignored in ((), ("--ignored",)):
        extras = git(
            claw,
            "ls-files",
            "--others",
            "--exclude-standard",
            *ignored,
            "--",
            "src",
            "scripts",
            "plugins",
        ).splitlines()
        if any(name.endswith(".py") for name in extras):
            parser.error("Claw producer contains untracked Python input")
    version = subprocess.check_output(
        [str(args.python), "-I", "-c", "import sys; print(sys.version_info[:2])"], text=True
    ).strip()
    if version != "(3, 13)":
        parser.error("maintained Python 3.13 is required")
    test = "tests/test_additional_mapping_successor_publication.py"
    output.mkdir(parents=True, exist_ok=False)
    overrides = {
        "PYTEST_ADDOPTS": "",
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTHONPYCACHEPREFIX": str(output / "bytecode"),
        "PYTHONPATH": str(root / "src"),
        "CLAW_SRC": str(claw / "src"),
        "MIM_ADDITIONAL_ASSERTION_CLAW_SRC": str(claw / "src"),
    }
    argv = [
        str(args.python),
        "-B",
        "-m",
        "pytest",
        "-q",
        "--no-cov",
        test,
        "--basetemp=" + str(output / "fixtures"),
        "--junitxml=" + str(output / "pytest.xml"),
    ]
    command = {
        "started_at": datetime.now(timezone.utc).isoformat(),
        "cwd": str(root),
        "head": git(root, "rev-parse", "HEAD"),
        "claw_root": str(claw),
        "claw_head": args.claw_head,
        "argv": argv,
        "environment_overrides": overrides,
        "launcher_sha256": sha(Path(__file__)),
        "python_sha256": sha(args.python),
        "source_sha256": {
            str(p.relative_to(root)): sha(p)
            for p in (
                root / test,
                root / "src/mediaingredientmech/curate/curation_successor.py",
                root / "src/mediaingredientmech/curate/stable_sssom_publication.py",
                root / "src/mediaingredientmech/curate/stable_sssom_replay.py",
            )
        },
        "scope": "Synthetic native canary; no real scientific or release approval",
    }
    (output / "COMMAND.json").write_text(json.dumps(command, indent=2) + "\n")
    with (output / "test.log").open("wb") as log:
        process = subprocess.run(
            argv, cwd=root, env={**os.environ, **overrides}, stdout=log, stderr=subprocess.STDOUT
        )
    retained = {}
    for path in sorted((output / "fixtures").rglob("*")):
        if (
            path.is_file()
            and not path.is_symlink()
            and ".git" not in path.parts
            and path.name
            in {
                "receipt.json",
                "application.json",
                "manifest.json",
                "combined-progress.json",
                "candidate.sssom.tsv",
                "ingredient_mappings.sssom.tsv",
                "generation.json",
                "stable_sssom_publication.json",
                "suppressed_aliases.tsv",
            }
        ):
            retained[str(path.relative_to(output))] = {
                "bytes": path.stat().st_size,
                "sha256": sha(path),
            }
    verification_error = None
    try:
        completed_native_evidence(output)
    except (ValueError, OSError, ET.ParseError) as exc:
        verification_error = str(exc)
    passed = process.returncode == 0 and verification_error is None
    result = {
        "finished_at": datetime.now(timezone.utc).isoformat(),
        "exit_code": process.returncode,
        "command_sha256": sha(output / "COMMAND.json"),
        "log_sha256": sha(output / "test.log"),
        "retained_artifacts": retained,
        "status": "PASSED" if passed else "FAILED",
        "verification_error": verification_error,
        "release_approval_added": False,
    }
    (output / "RESULT.json").write_text(json.dumps(result, indent=2) + "\n")
    print(
        json.dumps(
            {
                "result": str(output / "RESULT.json"),
                "status": result["status"],
                "sha256": sha(output / "RESULT.json"),
                "retained_artifacts": len(retained),
            }
        )
    )
    return 0 if passed else (process.returncode or 1)


if __name__ == "__main__":
    sys.exit(main())
