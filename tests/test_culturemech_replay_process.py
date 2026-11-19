"""Actual child-startup refusals; synthetic scripts are executor-only fixtures.

The integrated positive uses the real CM producer in test_culturemech_native_replay.
These sentinel scripts prove a bad frozen target never reaches execution.
"""

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

from mediaingredientmech.export import culturemech_replay_process as runner


@pytest.fixture
def probe(tmp_path):
    producer = tmp_path / "producer"
    producer.mkdir()
    script = producer / "verify.py"
    script.write_text(
        "import json, os, sys\nfrom pathlib import Path\n"
        "Path(sys.argv[3], 'executed').write_text('sentinel')\n"
        "print(json.dumps({'isolated': sys.flags.isolated, 'no_site': sys.flags.no_site, "
        "'bytecode': sys.dont_write_bytecode, 'home': os.environ.get('HOME')}))\n"
    )
    bundle = tmp_path / "bundle"
    bundle.mkdir()
    plan = runner.prepare_plan(script, bundle, "a" * 64)
    return producer, script, bundle, plan


def child(plan, producer):
    """Enter the real bootstrap after parent freeze, bypassing no child guard."""
    return subprocess.run(
        [
            str(Path(sys.executable).resolve()),
            "-I",
            "-S",
            "-B",
            "-c",
            runner.BOOTSTRAP,
            json.dumps(plan),
        ],
        cwd=producer,
        env=runner.ENVIRONMENT.copy(),
        text=True,
        capture_output=True,
        timeout=15,
    )


def refused(result, bundle, expected):
    assert result.returncode == 125
    assert "MIM_CM_BOOTSTRAP_REFUSAL:" in result.stderr
    assert expected in result.stderr
    assert not (bundle / "executed").exists()


def test_actual_isolated_child_ignores_python_startup_and_has_no_home(probe, tmp_path, monkeypatch):
    producer, _script, bundle, plan = probe
    poison = tmp_path / "poison"
    poison.mkdir()
    marker = tmp_path / "startup-executed"
    (poison / "sitecustomize.py").write_text(f"open({str(marker)!r}, 'w').write('bad')\n")
    monkeypatch.setenv("PYTHONPATH", str(poison))
    monkeypatch.setenv("PYTHONHOME", str(poison))
    result = runner.execute_plan(plan, cwd=producer)
    assert result.returncode == 0
    assert json.loads(result.stdout) == {
        "isolated": 1,
        "no_site": 1,
        "bytecode": True,
        "home": None,
    }
    assert (bundle / "executed").read_text() == "sentinel"
    assert not marker.exists()


def test_same_byte_script_replacement_refused_by_child_before_execution(probe):
    producer, script, bundle, plan = probe
    raw = script.read_bytes()
    replacement = script.with_name("replacement")
    replacement.write_bytes(raw)
    replacement.replace(script)
    refused(child(plan, producer), bundle, "frozen file changed")


def test_ancestor_replacement_refused_by_child_before_execution(probe):
    producer, script, bundle, plan = probe
    raw = script.read_bytes()
    producer.rename(producer.with_name("old-producer"))
    producer.mkdir()
    script.write_bytes(raw)
    refused(child(plan, producer), bundle, "frozen ancestor changed")


@pytest.mark.parametrize("mutation", ["symlink", "hardlink", "content"])
def test_source_alias_and_content_changes_refused_before_execution(probe, mutation):
    producer, script, bundle, plan = probe
    if mutation == "symlink":
        destination = script.with_name("real-file")
        script.rename(destination)
        script.symlink_to(destination)
    elif mutation == "hardlink":
        os.link(script, script.with_name("alias"))
    else:
        script.write_text(script.read_text() + "# changed\n")
    refused(
        child(plan, producer),
        bundle,
        "nonregular/aliased source" if mutation != "content" else "frozen file changed",
    )


@pytest.mark.parametrize(
    "mutation,diagnostic",
    [
        ("extra", "invalid payload fields"),
        ("argv", "non-verifier invocation"),
        ("identity", "invalid file identity"),
        ("executable", "interpreter differs"),
    ],
)
def test_closed_child_payload_refuses_forged_invocations(probe, mutation, diagnostic):
    producer, _script, bundle, plan = probe
    if mutation == "extra":
        plan["trust_me"] = True
    elif mutation == "argv":
        plan["argv"][1] = "build"
    elif mutation == "identity":
        plan["script"]["identity"]["st_ino"] = True
    else:
        plan["executable"]["path"] = "/not/the/running/interpreter"
    refused(child(plan, producer), bundle, diagnostic)


def test_runtime_hardlinks_are_qualified_without_allowing_source_aliases(tmp_path):
    runtime = tmp_path / "controlled-runtime-image"
    runtime.write_bytes(b"controlled identity fixture, not executed")
    os.link(runtime, runtime.with_name("runtime-package-link"))
    frozen, raw = runner.freeze_file(runtime, source=False)
    assert frozen["identity"]["st_nlink"] == 2
    assert runner.check_frozen(frozen, source=False) == raw
    with pytest.raises(ValueError, match="aliased source"):
        runner.freeze_file(runtime, source=True)
    runtime.write_bytes(b"changed runtime fixture")
    with pytest.raises(ValueError, match="frozen file"):
        runner.check_frozen(frozen, source=False)


def test_executor_times_out_its_own_controlled_child(probe, monkeypatch):
    producer, script, bundle, _plan = probe
    script.write_text("import time\ntime.sleep(5)\n")
    plan = runner.prepare_plan(script, bundle, "a" * 64)
    monkeypatch.setattr(runner, "TIMEOUT_SECONDS", 0.05)
    with pytest.raises(subprocess.TimeoutExpired):
        runner.execute_plan(plan, cwd=producer)
    assert not (bundle / "executed").exists()


def test_historical_facade_rejects_other_command_and_cwd(probe):
    producer, _script, bundle, plan = probe
    facade = runner.VerifierProcess(plan, "qualified-python", producer)
    with pytest.raises(ValueError, match="unexpected historical child argv"):
        facade.run(["qualified-python", "anything-else"])
    command = ["qualified-python", "scripts/ingredient_release_bundle.py", *plan["argv"][1:]]
    with pytest.raises(ValueError, match="unexpected child cwd"):
        facade.run(command, cwd=bundle, text=True, capture_output=True, check=True)
    assert not (bundle / "executed").exists()
