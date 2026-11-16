"""Actual isolated replay, including both recorded guard shapes, uses installed roots."""

# ruff: noqa: F811 -- Pytest resolves imported fixtures by parameter name.

import importlib.metadata
import json
import os
import subprocess
import sys
import venv
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

from mediaingredientmech.curate import curation_successor as successor
from mediaingredientmech.curate.publication_guard import FrozenFile
from tests.test_curation_successor_replay_child import replay_child  # noqa: F401
from tests.test_curation_successor_runtime_dependencies import installed  # noqa: F401
from tests.test_stable_id_adoption import ROOT, api, commit

SOURCE = "src/mediaingredientmech/curate/curation_successor.py"
HISTORICAL = (
    (
        "13f4f8494a46dbb3b1084652cbf5a030a60f6c03",
        "a5ac25dbdbbbb0fecb88a3d7fb3a0bc338175be98ac09d71ae8e52644c28cd1b",
    ),
    (
        "f63930804fe143cd0bd4eba0374d9d2be2dd66ba",
        "ed8dcf4328c17fc8e78dab08f357fa53b60bd5c037ca85b3810dc6b3440973c9",
    ),
)


@pytest.mark.parametrize("revision,source_sha", HISTORICAL, ids=("a5", "ed8"))
def test_recorded_guard_inherits_current_runtime_boundary(
    replay_child, monkeypatch, revision, source_sha
):
    root, claw, _, _, _ = replay_child
    raw = subprocess.check_output(
        ["git", "--no-optional-locks", "show", revision + ":" + SOURCE],
        cwd=ROOT,
        env={**os.environ, "GIT_NO_LAZY_FETCH": "1", "GIT_TERMINAL_PROMPT": "0"},
    )
    assert api.sha(raw) == source_sha
    # These are honest fixture inputs captured before execution. No completed
    # receipt is rehashed, and this component test claims no historical endpoint.
    (root / SOURCE).write_bytes(raw)
    commit(root)
    captured = {
        directory: {path: FrozenFile.capture(path) for path in directory.rglob("*.py")}
        for directory in (root, claw)
    }
    pins = {
        directory: {
            str(path.relative_to(directory)): api.sha(f.content) for path, f in files.items()
        }
        for directory, files in captured.items()
    }
    # Include the non-Python members required by the real native capture.
    from mediaingredientmech.curate import stable_sssom_publication as publication

    for name in publication._CAPTURE.files:
        pins[root][name] = api.sha((root / name).read_bytes())
    identities = {root: successor._identity(root)}
    heads = {claw: api.git(claw, "rev-parse", "HEAD").decode().strip()}
    outer = successor._ProducerBytes(pins, identities=identities, heads=heads)
    capture, _ = outer.load(root, "src/mediaingredientmech/curate/stable_publication_producer.py")
    historical = capture.load("mediaingredientmech.curate.curation_successor")
    assert historical._ProducerBytes is not successor._ProducerBytes
    inner = historical._ProducerBytes(pins, identities=identities, heads=heads)
    assert inner.parent is outer
    _, native = inner.load(root, "src/mediaingredientmech/curate/stable_publication_producer.py")
    envelopes, actual = [], []
    shared, raw_run = inner._run, outer._raw_run

    def observe_shared(args, **kwargs):
        if args[0] != "git":
            envelopes.append((args, json.loads(kwargs["input"])))
        return shared(args, **kwargs)

    def observe_actual(args, **kwargs):
        result = raw_run(args, **kwargs)
        if args[0] != "git":
            actual.append((args, json.loads(kwargs["input"]), result))
        return result

    monkeypatch.setattr(inner, "_run", observe_shared)
    monkeypatch.setattr(outer, "_raw_run", observe_actual)
    with pytest.raises(ValueError, match="complete native generation input membership differs"):
        native._replay_generation(
            root,
            claw,
            root.parent / "kg",
            {"outputs": {key: {"path": "unused-" + key} for key in ("sssom", "suppressions")}},
            {"canonical_label_resolution": {}, "source_revisions": {}},
            b"",
            b"",
            b"",
            {str(path): f for path, f in captured[claw].items()},
            [],
        )
    assert len(envelopes) == len(actual) == 1
    old_args, old = envelopes[0]
    args, new, result = actual[0]
    assert args[:5] == [sys.executable, "-I", "-S", "-B", "-c"]
    assert args[-1] == successor._RUNTIME_BOOTSTRAP + old_args[-1] + "\n_runtime_verify()\n"
    assert {key: value for key, value in old.items() if key != "runtime"} == {
        key: value for key, value in new.items() if key != "runtime"
    }
    assert new["runtime"]["files"] and new["runtime"]["modules"]["yaml"]
    assert result.returncode != 0
    assert b"ModuleNotFoundError" not in result.stderr


@pytest.mark.parametrize("selected", ["METADATA", "RECORD", "anchor", "root"])
def test_actual_child_refuses_late_runtime_identity_change(
    replay_child, installed, monkeypatch, selected
):
    root, distributions = installed
    _, _, guard, _, run = replay_child
    marker = root.parent / "STARTUP_EXECUTED"
    hook = f"from pathlib import Path; Path({str(marker)!r}).write_text('unexpected startup')\n"
    (root / "sitecustomize.py").write_text(hook)
    (root / "unexpected.pth").write_text("import pathlib; " + hook.split("; ", 1)[1])
    info, _ = distributions["python-dotenv"]
    original = guard._raw_run
    children = []

    def launch(args, **kwargs):
        if args[0] != "git":
            # This boundary is after the actual parent runtime authentication.
            assert guard._runtime is not None
            if selected == "root":
                saved = root.with_name("original-site-packages")
                root.rename(saved)
                root.mkdir()
                for path in saved.iterdir():
                    path.rename(root / path.name)
            else:
                path = root / (
                    "dotenv/__init__.py" if selected == "anchor" else str(info / selected)
                )
                replacement = root.parent / "same-bytes"
                replacement.write_bytes(path.read_bytes())
                replacement.replace(path)
        result = original(args, **kwargs)
        if args[0] != "git":
            children.append(result)
        return result

    monkeypatch.setattr(guard, "_raw_run", launch)
    with pytest.raises(ValueError, match="installed runtime"):
        run()
    assert len(children) == 1 and children[0].returncode != 0
    assert b"Authenticated replay child: installed runtime" in children[0].stderr
    assert b"complete native generation input membership differs" not in children[0].stderr
    assert not marker.exists()


@pytest.mark.parametrize("change", ["bootstrap", "field", "executable", "shell"])
def test_runtime_boundary_refuses_unknown_launch_before_execution(
    replay_child, monkeypatch, change
):
    _, _, guard, _, _ = replay_child
    args = [sys.executable, "-I", "-S", "-B", "-c", successor._REPLAY_BOOTSTRAP]
    envelope = {
        name: {} for name in ("entry", "input", "files", "code", "identities", "heads", "absences")
    }
    kwargs = {"input": api.encoded(envelope)}
    if change == "bootstrap":
        args[-1] += "\nraise AssertionError('UNEXECUTED_BOOTSTRAP')\n"
    elif change == "field":
        envelope["unknown"] = True
        kwargs["input"] = api.encoded(envelope)
    elif change == "executable":
        args[0] = "/unselected/python"
    else:
        kwargs["shell"] = True
    launched = []
    monkeypatch.setattr(guard, "_raw_run", lambda *a, **k: launched.append(a))
    with pytest.raises(ValueError, match="unsupported authenticated replay"):
        guard._runtime_run(args, **kwargs)
    assert not launched


def test_real_layered_environment_runs_original_child_and_recorded_guard_controls(tmp_path):
    """A literal .pth exposes existing dependencies to the parent, never the child."""
    environment = tmp_path / "layered"
    venv.EnvBuilder(with_pip=False, symlinks=True).create(environment)
    library = (
        environment
        / "lib"
        / f"python{sys.version_info.major}.{sys.version_info.minor}"
        / "site-packages"
    )
    installed_roots = sorted(
        {
            str(Path(distribution.locate_file("")).absolute())
            for distribution in importlib.metadata.distributions()
            if any(str(item).endswith(".dist-info/METADATA") for item in distribution.files or ())
        }
    )
    (library / "installed-dependencies.pth").write_text("\n".join(installed_roots) + "\n")
    command = [
        str(environment / "bin/python3"),
        "-B",
        "-m",
        "pytest",
        "-o",
        "addopts=--strict-markers",
        "-q",
        "-p",
        "no:cacheprovider",
        "--maxfail=1",
        "--basetemp=" + str(tmp_path / "nested-fixtures"),
        "--junitxml=" + str(tmp_path / "pytest.xml"),
        "tests/test_curation_successor_replay_child.py",
        "tests/test_curation_successor_runtime_replay.py::test_recorded_guard_inherits_current_runtime_boundary",
    ]
    (tmp_path / "COMMAND.json").write_text(json.dumps(command, indent=2) + "\n")
    result = subprocess.run(
        command,
        cwd=ROOT,
        capture_output=True,
        env={
            **os.environ,
            "PYTHONDONTWRITEBYTECODE": "1",
            "PYTEST_ADDOPTS": "",
            "PYTHONPATH": os.pathsep.join((str(ROOT / "src"), str(ROOT))),
        },
    )
    (tmp_path / "stdout.log").write_bytes(result.stdout)
    (tmp_path / "stderr.log").write_bytes(result.stderr)
    assert result.returncode == 0, (result.stdout + result.stderr).decode()
    cases = list(ET.parse(tmp_path / "pytest.xml").getroot().iter("testcase"))
    assert len(cases) == 11
    assert not any(
        case.find(tag) is not None for case in cases for tag in ("failure", "error", "skipped")
    )
