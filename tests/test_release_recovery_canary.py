"""Retained canary evidence and physical output boundaries (#1427/#1428)."""

import importlib.util
import json
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

SPEC = importlib.util.spec_from_file_location(
    "recovery_canary", Path(__file__).parents[1] / "scripts/adhoc/run_release_recovery_canary.py"
)
canary = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(canary)


def test_output_requires_physical_owned_fresh_directory(tmp_path):
    root = tmp_path / "repo"
    root.mkdir()
    good = root / ".temp" / "new"
    assert canary.owned_output(root, good) == good
    with pytest.raises(ValueError):
        canary.owned_output(root, root / ".temp" / ".." / ".." / "outside")
    elsewhere = tmp_path / "elsewhere"
    elsewhere.mkdir()
    (root / ".temp").symlink_to(elsewhere, target_is_directory=True)
    with pytest.raises(ValueError, match="symlink"):
        canary.owned_output(root, good)


def proof(output):
    output.mkdir()
    (output / "pytest.xml").write_text(
        '<testsuites><testsuite><testcase name="test_two_corrections_publish_independent_assertions_and_keep_holds"/>'
        "</testsuite></testsuites>"
    )
    fixtures = output / "fixtures"
    fixtures.mkdir()
    (fixtures / "combined-progress.json").write_text(json.dumps({"completed": canary.PHASES}))
    for folder, name, value in (
        (
            "additional-source-application",
            "application.json",
            {"state": "COMPLETE", "release_approval_added": False},
        ),
        (
            "publication1-additional-applied",
            "application.json",
            {"state": "COMPLETE", "scientific_approval_added": False},
        ),
        ("additional-assertion-generation", "receipt.json", {"state": "COMPLETE"}),
        ("additional-assertion-generation", "candidate.sssom.tsv", "synthetic row"),
        ("additional-assertion-generation", "generation.json", {"synthetic": True}),
        ("mappings", "stable_sssom_publication.json", {"synthetic": True}),
    ):
        target = fixtures / folder / name
        target.parent.mkdir(exist_ok=True)
        target.write_text(json.dumps(value))


def test_complete_evidence_is_required(tmp_path):
    output = tmp_path / "complete"
    proof(output)
    canary.completed_native_evidence(output)
    (output / "fixtures/publication1-additional-applied/application.json").unlink()
    with pytest.raises(ValueError, match="receipt"):
        canary.completed_native_evidence(output)


@pytest.mark.parametrize("missing", ["phases", "execution", "skip", "artifact"])
def test_collection_or_partial_evidence_is_not_completion(tmp_path, missing):
    output = tmp_path / "incomplete"
    proof(output)
    if missing == "phases":
        (output / "fixtures/combined-progress.json").write_text(
            json.dumps({"completed": canary.PHASES[:-1]})
        )
    elif missing == "execution":
        (output / "pytest.xml").write_text('<testsuites><testsuite tests="0"/></testsuites>')
    elif missing == "skip":
        path = output / "pytest.xml"
        path.write_text(path.read_text().replace("/>", "><skipped/></testcase>"))
    else:
        (output / "fixtures/additional-assertion-generation/candidate.sssom.tsv").write_text("")
    with pytest.raises(ValueError):
        canary.completed_native_evidence(output)


def test_zero_exit_without_native_execution_is_failed(tmp_path, monkeypatch):
    root, claw = tmp_path / "repo", tmp_path / "claw"
    root.mkdir()
    output = root / ".temp" / "probe"
    launcher = root / "scripts/adhoc/run_release_recovery_canary.py"
    for path in (
        launcher,
        root / "tests/test_additional_mapping_successor_publication.py",
        *(
            root / "src/mediaingredientmech/curate" / name
            for name in (
                "curation_successor.py",
                "stable_sssom_publication.py",
                "stable_sssom_replay.py",
            )
        ),
    ):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("# Explicit test-only command fixture\n")
    monkeypatch.setattr(canary, "__file__", str(launcher))

    def fake_git(path, *args):
        if args[0] == "remote":
            name = "MediaIngredientMech" if path == root else "culturebotai-claw"
            return "https://github.com/CultureBotAI/" + name + ".git"
        return "a" * 40 if args[0] == "rev-parse" else ""

    monkeypatch.setattr(canary, "git", fake_git)
    monkeypatch.setattr(canary.subprocess, "check_output", lambda *a, **k: "(3, 13)")

    def collected(*args, **kwargs):
        assert kwargs["env"]["PYTEST_ADDOPTS"] == ""
        (output / "pytest.xml").write_text('<testsuites><testsuite tests="0"/></testsuites>')
        return SimpleNamespace(returncode=0)

    monkeypatch.setenv("PYTEST_ADDOPTS", "--collect-only")
    monkeypatch.setattr(canary.subprocess, "run", collected)
    monkeypatch.setattr(
        sys,
        "argv",
        [
            str(launcher),
            "--python",
            sys.executable,
            "--claw-root",
            str(claw),
            "--claw-head",
            "a" * 40,
            "--output",
            str(output),
        ],
    )
    assert canary.main() == 1
    result = json.loads((output / "RESULT.json").read_bytes())
    assert result["status"] == "FAILED" and result["retained_artifacts"] == {}
