"""Read-only exact-base views for historical review replay (#1265, 2026-11-08).

Inputs are explicitly listed repository-relative files at the fixed pre-mint
commit; outputs are in-memory read streams. No live file or historical evidence
is changed and no approval/hash is refreshed. New-current tests use live state.
"""
from __future__ import annotations

import io
from contextlib import contextmanager
from functools import lru_cache
from pathlib import Path

import pytest

from mediaingredientmech.identity_projection import BASE_COMMIT, git_files, record_paths

SOURCE_COMMIT = "0dac278466699129a083343a921c2e0ca18a9ab4"


@lru_cache(maxsize=8)
def historical_bytes(root: Path, names: tuple[str, ...]) -> dict[str, bytes]:
    assert BASE_COMMIT == SOURCE_COMMIT
    return git_files(root, list(names))


@contextmanager
def fixed_base_reads(root: Path, names):
    """Overlay only explicit fixed-base paths, preserving callers' mutation probes."""
    root = root.resolve()
    contents = historical_bytes(root, tuple(sorted(names)))
    selected = {root / name: raw for name, raw in contents.items()}
    original_open = Path.open

    def read_snapshot(path, mode="r", buffering=-1, encoding=None, errors=None, newline=None):
        if path not in selected:
            return original_open(path, mode, buffering, encoding, errors, newline)
        if mode not in {"r", "rb", "rt"}:
            raise AssertionError("Historical replay inputs are read-only")
        raw = selected[path]
        if "b" in mode:
            return io.BytesIO(raw)
        return io.TextIOWrapper(io.BytesIO(raw), encoding=encoding, errors=errors, newline=newline)

    with pytest.MonkeyPatch.context() as patch:
        patch.setattr(Path, "open", read_snapshot)
        yield contents


@pytest.fixture
def pre_mint_catalogue():
    root = Path(__file__).resolve().parents[1]
    names = record_paths(root, historical=True) + ["mappings/ingredient_mappings.sssom.tsv"]
    with fixed_base_reads(root, names) as contents:
        yield contents
