"""Required checks must report on every PR and its actual merge queue candidate."""

import os
import re
import subprocess
from copy import deepcopy
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PIN = (ROOT / "scripts" / ".vendored_canon_ref").read_text().strip()
# Job/check names are an external ruleset contract. Renames require coordinated
# settings changes; deriving this list from the workflows would hide a deletion.
REQUIRED_JOBS = {
    "curation-history.yaml": {"history": "history"},
    "instruction-refs.yaml": {"instruction-refs": "instruction-refs"},
    "label-correspondence.yaml": {"id-label-gate": "id-label-gate"},
    "qc-component-partonomy.yaml": {"qc": "qc-component-partonomy"},
    "qc-duplicate-ids.yaml": {"qc": "qc-duplicate-ids"},
    "qc-evidence.yaml": {"qc": "qc-evidence"},
    "qc-flat-coverage.yaml": {"qc": "qc-flat-coverage"},
    "qc-roundtrip.yaml": {"roundtrip": "roundtrip"},
    "qc-sssom.yaml": {"qc": "qc-sssom"},
    "quality.yaml": {"check": "check"},
    "tests.yaml": {"pytest": "pytest"},
    "validate-strict.yaml": {"validate-strict": "validate-strict"},
    "vendored-sync.yaml": {"vendored-sync": "vendored-sync"},
}


def _load(name):
    return yaml.safe_load((ROOT / ".github" / "workflows" / name).read_text())


def _assert_native_adoption_dependency(document, job):
    """#1323: pytest captures pinned source without replacing the MIM checkout."""
    steps = job["steps"]
    checkouts = [step for step in steps if step.get("uses", "").startswith("actions/checkout@")]
    assert len(checkouts) == 2, "pytest needs its candidate and one native dependency"
    dependencies = [step for step in checkouts
                    if step.get("with", {}).get("repository") == "CultureBotAI/culturebotai-claw"]
    assert len(dependencies) == 1, "pytest needs the real native Claw source"
    dependency = dependencies[0]
    candidate = next(step for step in checkouts if step is not dependency)
    assert candidate.get("with", {}).get("path") in (None, "."), "keep the candidate at the job root"
    assert candidate.get("with", {}).get("fetch-depth") == 0, "retain the full candidate history"
    options = dependency["with"]
    assert re.fullmatch(r"[0-9a-f]{40}", VALIDATOR_PIN)
    assert options.get("ref") == "${{ steps.native-claw-pin.outputs.ref }}", "native source must read the existing pin"
    assert options.get("path") == ".temp/native-claw", "native source must be isolated and ignored"
    assert options.get("persist-credentials") is False
    readers = [step for step in steps if step.get("id") == "native-claw-pin"]
    runners = [step for step in steps if step.get("name") == "Run pytest"]
    assert len(readers) == len(runners) == 1, "one pin reader and complete pytest invocation required"
    reader, runner = readers[0], runners[0]
    assert steps.index(candidate) < steps.index(reader) < steps.index(dependency) < steps.index(runner)
    assert reader.get("shell") == "bash"
    assert runner.get("env", {}).get("CLAW_SRC") == "${{ github.workspace }}/.temp/native-claw/src"
    assert runner.get("run") == "uv run --with pytest --with pytest-cov pytest", "retain every native and pure test"
    assert "CLAW_SRC" not in document.get("env", {}) and "CLAW_SRC" not in job.get("env", {})
    assert "PYTHONPATH" not in runner.get("env", {}), "source capture must not broaden package imports"
    for step in (candidate, reader, dependency, runner):
        assert "if" not in step and not step.get("continue-on-error"), "native setup and tests cannot silently skip"


def _assert_required_workflow(document, expected_jobs):
    events = document.get("on", document.get(True, {}))
    assert "pull_request" in events, "missing PR trigger"
    assert events["pull_request"] in (None, {}), "required PR checks cannot be filtered"
    assert events.get("merge_group") == {"types": ["checks_requested"]}, "missing queue trigger"
    for job_id, check_name in expected_jobs.items():
        job = document["jobs"][job_id]
        assert job.get("name", job_id) == check_name, "required check renamed"
        assert "if" not in job, "required job cannot skip the candidate"
        assert not job.get("continue-on-error"), "required job must fail on errors"
        if expected_jobs == {"pytest": "pytest"}:
            _assert_native_adoption_dependency(document, job)
        for step in job.get("steps", []):
            if step.get("uses", "").startswith("actions/checkout@"):
                options = step.get("with", {})
                if options.get("repository") == "CultureBotAI/culturebotai-claw":
                    if expected_jobs == {"pytest": "pytest"}:
                        # This distinct layout was checked above. The evidence
                        # validator keeps every original assertion below.
                        continue
                    assert re.fullmatch(r"[0-9a-f]{40}", VALIDATOR_PIN)
                    assert options.get("ref") == "${{ steps.claw-pin.outputs.ref }}", "validator must read the consumer pin"
                    assert options.get("path") == "claw", "validator must be separate"
                    pin_steps = [other for other in job["steps"] if other.get("id") == "claw-pin"]
                    assert len(pin_steps) == 1, "validator needs exactly one pin reader"
                    assert job["steps"].index(pin_steps[0]) < job["steps"].index(step), "read pin before checkout"
                    assert any(
                        other.get("uses", "").startswith("actions/checkout@")
                        and other.get("with") == {"path": "mech", "persist-credentials": False}
                        for other in job["steps"]
                    ), "validator requires the separate event-bound MIM candidate"
                else:
                    assert options.get("repository") in (None, "${{ github.repository }}")
                    assert "ref" not in options, "must check out the event's candidate"
    concurrency = document.get("concurrency")
    if concurrency:
        assert "github.run_id" in concurrency["group"], "queue runs need distinct groups"
        assert concurrency["cancel-in-progress"] == "${{ github.event_name == 'pull_request' }}"


@pytest.mark.parametrize("workflow", REQUIRED_JOBS)
def test_required_workflow_runs_for_pr_and_merge_group(workflow):
    _assert_required_workflow(_load(workflow), REQUIRED_JOBS[workflow])


@pytest.mark.parametrize("defect", ["queue", "paths", "skip", "cancel", "checkout"])
def test_the_guard_rejects_a_broken_workflow(defect):
    name = "vendored-sync.yaml"
    document = _load(name)
    _assert_required_workflow(document, REQUIRED_JOBS[name])  # unmutated control
    broken = deepcopy(document)
    events = broken.get("on", broken.get(True))
    job = broken["jobs"]["vendored-sync"]
    if defect == "queue":
        del events["merge_group"]
    elif defect == "paths":
        events["pull_request"] = {"paths": ["src/**"]}
    elif defect == "skip":
        job["if"] = "github.event_name == 'pull_request'"
    elif defect == "cancel":
        broken["concurrency"]["cancel-in-progress"] = True
    else:
        job["steps"][0]["with"] = {"ref": "main"}
    with pytest.raises(AssertionError):
        _assert_required_workflow(broken, REQUIRED_JOBS[name])


def test_required_job_names_are_unambiguous():
    names = [
        _load(workflow)["jobs"][job_id].get("name", job_id)
        for workflow, jobs in REQUIRED_JOBS.items()
        for job_id in jobs
    ]
    assert len(names) == len(set(names)), "different required workflows report the same check"


@pytest.mark.parametrize("defect", ["unpinned", "mutable", "hardcoded", "overlap", "candidate-ref", "pin-order", "pin-reader"])
def test_evidence_validator_cannot_drift_or_replace_candidate(defect):
    name = "qc-evidence.yaml"
    document = _load(name)
    _assert_required_workflow(document, REQUIRED_JOBS[name])
    broken = deepcopy(document)
    steps = broken["jobs"]["qc"]["steps"]
    candidate, validator = [step for step in steps if step.get("uses", "").startswith("actions/checkout@")]
    if defect == "unpinned":
        del validator["with"]["ref"]
    elif defect == "mutable":
        validator["with"]["ref"] = "main"
    elif defect == "hardcoded":
        validator["with"]["ref"] = VALIDATOR_PIN
    elif defect == "overlap":
        validator["with"]["path"] = candidate["with"]["path"]
    elif defect in {"pin-order", "pin-reader"}:
        reader = next(step for step in steps if step.get("id") == "claw-pin")
        steps.remove(reader)
        if defect == "pin-order":
            steps.append(reader)
    else:
        candidate["with"]["ref"] = "main"
    with pytest.raises(AssertionError):
        _assert_required_workflow(broken, REQUIRED_JOBS[name])


def _run_evidence_pin_reader(root, pin):
    path = root / "mech/scripts/.vendored_canon_ref"
    path.parent.mkdir(parents=True)
    if pin is not None:
        path.write_bytes(pin)
    reader = next(step for step in _load("qc-evidence.yaml")["jobs"]["qc"]["steps"]
                  if step.get("id") == "claw-pin")
    output = root / "github-output"
    result = subprocess.run(
        ["bash", "-c", reader["run"]], cwd=root, capture_output=True, text=True,
        env={**os.environ, "GITHUB_OUTPUT": str(output)}, timeout=15,
    )
    return result, output


def test_evidence_pin_reader_uses_each_actual_consumer_pin(tmp_path):
    for index, pin in enumerate([b"a" * 40 + b"\n", b"b" * 40]):
        result, output = _run_evidence_pin_reader(tmp_path / str(index), pin)
        assert result.returncode == 0, result.stderr
        assert output.read_text() == "ref=" + pin.decode().strip() + "\n"


@pytest.mark.parametrize("pin", [None, b"main\n", b"A" * 40, b"a" * 40 + b"\nother=x"])
def test_evidence_pin_reader_rejects_missing_mutable_or_malformed_pin(tmp_path, pin):
    result, output = _run_evidence_pin_reader(tmp_path, pin)
    assert result.returncode != 0
    assert not output.exists()


@pytest.mark.parametrize("defect", ["dependency", "mutable", "hardcoded", "overlap", "pin-order",
                                  "pin-reader", "source-env", "broad-path", "skip", "test-filter"])
def test_native_adoption_dependency_cannot_drift_or_skip(defect):
    document = _load("tests.yaml")
    _assert_required_workflow(document, REQUIRED_JOBS["tests.yaml"])
    broken = deepcopy(document)
    job = broken["jobs"]["pytest"]
    steps = job["steps"]
    dependency = next(step for step in steps
                      if step.get("with", {}).get("repository") == "CultureBotAI/culturebotai-claw")
    reader = next(step for step in steps if step.get("id") == "native-claw-pin")
    runner = next(step for step in steps if step.get("name") == "Run pytest")
    if defect == "dependency":
        steps.remove(dependency)
    elif defect == "mutable":
        dependency["with"]["ref"] = "main"
    elif defect == "hardcoded":
        dependency["with"]["ref"] = VALIDATOR_PIN
    elif defect == "overlap":
        dependency["with"]["path"] = "."
    elif defect in {"pin-order", "pin-reader"}:
        steps.remove(reader)
        if defect == "pin-order":
            steps.append(reader)
    elif defect == "source-env":
        del runner["env"]["CLAW_SRC"]
    elif defect == "broad-path":
        runner["env"]["PYTHONPATH"] = ".temp/native-claw/src"
    elif defect == "skip":
        dependency["if"] = "false"
    else:
        runner["run"] += " -k 'not stable_id_adoption'"
    with pytest.raises(AssertionError):
        _assert_required_workflow(broken, REQUIRED_JOBS["tests.yaml"])


def _run_native_pin_reader(root, pin, *, symlink=False):
    path = root / "scripts/.vendored_canon_ref"
    path.parent.mkdir(parents=True)
    if symlink:
        target = root / "real-pin"
        target.write_bytes(pin)
        path.symlink_to(target)
    elif pin is not None:
        path.write_bytes(pin)
    reader = next(step for step in _load("tests.yaml")["jobs"]["pytest"]["steps"]
                  if step.get("id") == "native-claw-pin")
    output = root / "github-output"
    result = subprocess.run(
        ["bash", "-c", reader["run"]], cwd=root, capture_output=True, text=True,
        env={**os.environ, "GITHUB_OUTPUT": str(output)}, timeout=15,
    )
    return result, output


def test_native_pin_reader_uses_each_actual_consumer_pin(tmp_path):
    for index, pin in enumerate([b"a" * 40 + b"\n", b"b" * 40]):
        result, output = _run_native_pin_reader(tmp_path / str(index), pin)
        assert result.returncode == 0, result.stderr
        assert output.read_text() == "ref=" + pin.decode().strip() + "\n"


@pytest.mark.parametrize("pin", [None, b"main\n", b"A" * 40, b"a" * 40 + b"\nother=x"])
def test_native_pin_reader_rejects_missing_mutable_or_malformed_pin(tmp_path, pin):
    result, output = _run_native_pin_reader(tmp_path, pin)
    assert result.returncode != 0
    assert not output.exists()


def test_native_pin_reader_refuses_symlink(tmp_path):
    result, output = _run_native_pin_reader(tmp_path, b"a" * 40, symlink=True)
    assert result.returncode != 0
    assert not output.exists()
