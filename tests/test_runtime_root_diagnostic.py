"""The #1450 diagnostic retains outcomes and only explicit target operands."""

from __future__ import annotations

import json
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/runtime_root_diagnostic.py"
PRIVATE = "SYNTHETIC_UNRELATED_VALUE_MUST_NOT_BE_SERIALIZED"


def run_case(tmp_path, source):
    test = tmp_path / "test_probe.py"
    test.write_text(source)
    configuration = tmp_path / "pytest.ini"
    configuration.write_text("[pytest]\n")
    command = [
        sys.executable,
        "-B",
        str(SCRIPT),
        str(test),
        "-c",
        str(configuration),
        "-o",
        "addopts=",
        "-p",
        "no:cacheprovider",
        "--tb=long",
        "--maxfail=1",
        "--junitxml=" + str(tmp_path / "result.xml"),
    ]
    result = subprocess.run(command, cwd=tmp_path, capture_output=True, text=True, timeout=30)
    (tmp_path / "stdout.txt").write_text(result.stdout)
    (tmp_path / "stderr.txt").write_text(result.stderr)
    cases = list(ET.parse(tmp_path / "result.xml").getroot().iter("testcase"))
    return (
        result,
        cases,
        list((tmp_path / ".temp/runtime-ci-diagnostic-1450").glob("runtime-root-operands-*.json")),
    )


def guard_case(tmp_path):
    prefix = tmp_path / "fixture-environment"
    library = prefix / f"lib/python{sys.version_info.major}.{sys.version_info.minor}/site-packages"
    library.mkdir(parents=True)
    (prefix / "bin").mkdir()
    (prefix / "bin/python3").symlink_to(Path(sys._base_executable).resolve())
    (prefix / "pyvenv.cfg").write_text(
        f"home = {tmp_path / 'wrong-home'}\n"
        f"version_info = {'.'.join(map(str, sys.version_info[:3]))}\n"
        f"private_field = {PRIVATE}\n"
    )
    return (
        library,
        f"""
from pathlib import Path
import pytest
from mediaingredientmech.curate import curation_successor

def test_guard():
    private_field = {PRIVATE!r}
    with pytest.raises(ValueError, match="complete native generation input membership differs"):
        curation_successor._runtime_root(Path({str(library)!r}), {{"directories": {{}}, "files": {{}}}})
""",
    )


def test_target_failure_remains_failed_and_records_only_operands(tmp_path):
    library, source = guard_case(tmp_path)
    result, cases, outputs = run_case(tmp_path, source)
    assert result.returncode == 1
    assert len(cases) == 1 and cases[0].find("failure") is not None
    assert "dependency library is not an environment of the selected interpreter" in result.stdout
    assert len(outputs) == 1
    raw = outputs[0].read_text()
    record = json.loads(raw)
    assert record["frame"]["function"] == "_runtime_root"
    assert record["frame"]["exception_type"] == "ValueError"
    assert record["captured_frame_operands"]["root"] == str(library)
    assert set(record["captured_frame_operands"]["cfg_fields"]) == {"home", "version_info"}
    assert record["post_failure_resolution"]["home_equals_base_parent"] is False
    assert record["post_failure_resolution"]["versions_equal_selected_version"] is True
    assert record["post_failure_resolution"]["bin_python3_equals_base"] is True
    assert PRIVATE not in raw and "private_field" not in raw
    assert "INTERNALERROR" not in result.stdout + result.stderr


@pytest.mark.parametrize("fail", [False, True], ids=["success", "unrelated-failure"])
def test_non_target_paths_do_not_dump_operands(tmp_path, fail):
    result, cases, outputs = run_case(
        tmp_path,
        f"def test_unrelated():\n    private_field = {PRIVATE!r}\n    assert {not fail!r}\n",
    )
    assert result.returncode == (1 if fail else 0)
    assert len(cases) == 1
    assert (cases[0].find("failure") is not None) is fail
    assert outputs == []
    assert not (tmp_path / ".temp/runtime-ci-diagnostic-1450").exists()


def test_diagnostic_write_error_does_not_replace_original_failure(tmp_path):
    _, source = guard_case(tmp_path)
    (tmp_path / ".temp").mkdir()
    (tmp_path / ".temp/runtime-ci-diagnostic-1450").write_text("Occupied test output path")
    result, cases, outputs = run_case(tmp_path, source)
    assert result.returncode == 1
    assert len(cases) == 1 and cases[0].find("failure") is not None
    assert "dependency library is not an environment of the selected interpreter" in result.stdout
    assert '"diagnostic_error_types": ["FileExistsError"]' in result.stdout
    assert "INTERNALERROR" not in result.stdout + result.stderr
    assert outputs == []
