"""#1450: derive the real patch request; refuse mismatched/unusable selection."""

import hashlib
import importlib.util
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
