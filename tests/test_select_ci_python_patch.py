"""#1450: derive the real patch request; refuse mismatched/unusable selection."""

import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "select_ci_python_patch", ROOT / "scripts/select_ci_python_patch.py"
)
selector = importlib.util.module_from_spec(spec)
spec.loader.exec_module(selector)


def resolved_by_uv(monkeypatch, path):
    original = subprocess.run
    calls = []

    def run(argv, **kwargs):
        calls.append(argv)
        if argv[0] == "uv":
            return subprocess.CompletedProcess(argv, 0, str(path) + "\n", "")
        return original(argv, **kwargs)

    monkeypatch.setattr(selector.subprocess, "run", run)
    return calls


def test_alias_selection_records_actual_patch_and_binary(monkeypatch, tmp_path):
    binary = Path(sys._base_executable).resolve()
    alias = tmp_path / "python-minor-alias"
    alias.symlink_to(binary)
    calls = resolved_by_uv(monkeypatch, alias)
    request = ".".join(map(str, sys.version_info[:2]))
    result = selector.select_patch(request)
    assert result["actual_patch_request"] == ".".join(map(str, sys.version_info[:3]))
    assert result["maintained_minor_request"] == request
    assert result["selected_path"] == str(alias)
    assert result["resolved_path"] == str(binary)
    assert result["executable_sha256"] == hashlib.sha256(binary.read_bytes()).hexdigest()
    assert calls[1][:3] == [str(binary), "-I", "-S"]


def test_wrong_minor_selection_is_refused(monkeypatch):
    resolved_by_uv(monkeypatch, Path(sys._base_executable).resolve())
    request = f"{sys.version_info.major}.{sys.version_info.minor + 1}"
    with pytest.raises(ValueError, match="differs from the maintained Python"):
        selector.select_patch(request)


@pytest.mark.parametrize("kind", ["relative", "missing"])
def test_unusable_path_is_refused_before_execution(monkeypatch, tmp_path, kind):
    path = Path("unqualified-python") if kind == "relative" else tmp_path / "missing"
    calls = resolved_by_uv(monkeypatch, path)
    with pytest.raises((ValueError, FileNotFoundError)):
        selector.select_patch("3.13")
    assert len(calls) == 1


def test_invalid_maintained_request_is_refused_before_discovery(monkeypatch):
    calls = resolved_by_uv(monkeypatch, Path(sys._base_executable).resolve())
    with pytest.raises(ValueError, match="major.minor"):
        selector.select_patch("3.13\nUV_PYTHON=3.14")
    assert calls == []


def prepare_main(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    request = ".".join(map(str, sys.version_info[:2]))
    (tmp_path / ".python-version").write_text(request + "\n")
    monkeypatch.setenv("UV_PYTHON", request)
    github_env = tmp_path / "github-env"
    github_env.write_text("EXISTING=value\n")
    monkeypatch.setenv("GITHUB_ENV", str(github_env))
    calls = resolved_by_uv(monkeypatch, Path(sys._base_executable).resolve())
    return github_env, calls


def test_main_uses_explicit_receipt_path_and_actual_patch(monkeypatch, tmp_path):
    github_env, _ = prepare_main(monkeypatch, tmp_path)
    output = tmp_path / "caller-chosen" / "selection.json"
    selector.main(["--output", str(output)])
    receipt = json.loads(output.read_text())
    patch = ".".join(map(str, sys.version_info[:3]))
    assert receipt["actual_patch_request"] == patch
    assert receipt["resolved_path"] == str(Path(sys._base_executable).resolve())
    assert github_env.read_text() == "EXISTING=value\nUV_PYTHON=" + patch + "\n"
    assert not (tmp_path / ".temp").exists()


def test_main_refuses_overwrite_without_changing_environment(monkeypatch, tmp_path):
    github_env, _ = prepare_main(monkeypatch, tmp_path)
    output = tmp_path / "existing.json"
    output.write_text("prior receipt\n")
    with pytest.raises(FileExistsError):
        selector.main(["--output", str(output)])
    assert output.read_text() == "prior receipt\n"
    assert github_env.read_text() == "EXISTING=value\n"


def test_main_requires_output_before_discovery(monkeypatch, tmp_path):
    github_env, calls = prepare_main(monkeypatch, tmp_path)
    with pytest.raises(SystemExit) as error:
        selector.main([])
    assert error.value.code == 2
    assert calls == []
    assert github_env.read_text() == "EXISTING=value\n"


def test_main_refuses_maintained_request_drift_before_output(monkeypatch, tmp_path):
    github_env, calls = prepare_main(monkeypatch, tmp_path)
    (tmp_path / ".python-version").write_text("3.99\n")
    output = tmp_path / "new.json"
    with pytest.raises(ValueError, match="differs from maintained"):
        selector.main(["--output", str(output)])
    assert calls == []
    assert not output.exists()
    assert github_env.read_text() == "EXISTING=value\n"
