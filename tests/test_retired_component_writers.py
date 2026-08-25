"""The pre-#369 component writers must fail before touching data."""

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = (
    "apply_curated_decompositions",
    "decompose_substrate_combinations",
    "decompose_py_media_and_ground_categories",
)


def _load(name: str):
    spec = importlib.util.spec_from_file_location(
        f"_retired_{name}", ROOT / "scripts" / f"{name}.py"
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize("name", SCRIPTS)
@pytest.mark.parametrize("argv", ([], ["--apply"]))
def test_historical_component_writer_fails_closed(name, argv, monkeypatch, capsys):
    module = _load(name)

    def forbidden(*_args, **_kwargs):
        raise AssertionError("retired writer attempted file I/O")

    monkeypatch.setattr(module.Path, "read_text", forbidden)
    monkeypatch.setattr(module.Path, "open", forbidden)
    assert module.main(argv) == 2
    assert "retired" in capsys.readouterr().err
