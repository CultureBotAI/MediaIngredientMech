"""The historical read adapter cannot change live state or new-current inputs."""
from pathlib import Path

import pytest

from tests import pre_mint_state as state


def test_exact_selected_reads_are_frozen_and_current_state_restores(tmp_path, monkeypatch):
    selected = tmp_path / "selected.yaml"
    unrelated = tmp_path / "unrelated.yaml"
    selected.write_bytes(b"new-current record\n")
    unrelated.write_bytes(b"unrelated current record\n")
    monkeypatch.setattr(state, "historical_bytes", lambda root, names: {"selected.yaml": b"old record\n"})
    with state.fixed_base_reads(tmp_path, ["selected.yaml"]) as records:
        assert records == {"selected.yaml": b"old record\n"}
        assert selected.read_bytes() == b"old record\n"
        assert selected.read_text() == "old record\n"
        assert unrelated.read_bytes() == b"unrelated current record\n"
        with pytest.raises(AssertionError, match="read-only"):
            selected.write_text("cannot rewrite evidence")
    assert selected.read_bytes() == b"new-current record\n"


def test_historical_reads_preserve_targeted_corruption_probes(tmp_path, monkeypatch):
    selected = tmp_path / "selected.yaml"
    selected.write_bytes(b"new-current record\n")
    monkeypatch.setattr(state, "historical_bytes", lambda root, names: {"selected.yaml": b"old record\n"})
    with state.fixed_base_reads(tmp_path, ["selected.yaml"]):
        original = Path.read_bytes
        with monkeypatch.context() as probe:
            probe.setattr(Path, "read_bytes", lambda path: original(path) + b"changed bytes\n")
            assert selected.read_bytes() == b"old record\nchanged bytes\n"
        assert selected.read_bytes() == b"old record\n"
    assert selected.read_bytes() == b"new-current record\n"
