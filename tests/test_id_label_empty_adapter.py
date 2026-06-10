"""Tests for the id-label validator's empty-adapter detection.

A configured OAK adapter that loads but holds no terms (e.g. OAK's
``sqlite:obo:micro`` selector points at a 0-byte stub whose tables don't exist)
must NOT flag every id under that prefix as a false ``ID_NOT_FOUND``. It is
reclassified as the benign ``SKIPPED_EMPTY_ADAPTER``. These pin that logic with
fake adapters so it stays CI-safe (no OAK / network).
"""

import importlib.util
from pathlib import Path

import pytest

_spec = importlib.util.spec_from_file_location(
    "validate_id_label_correspondence",
    Path(__file__).parent.parent / "scripts" / "validate_id_label_correspondence.py",
)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


class _Adapter:
    """Fake OAK adapter: entities() yields `items` or raises `exc`."""

    def __init__(self, items=(), exc=None):
        self._items, self._exc = list(items), exc

    def entities(self):
        if self._exc:
            raise self._exc
        return iter(self._items)


def test_empty_when_no_entities():
    assert mod.AdapterPool._is_empty(_Adapter(items=[]), "micro") is True


def test_empty_when_no_such_table():
    # uninitialized / 0-byte sqlite stub (OAK's sqlite:obo:micro shape)
    exc = Exception("(sqlite3.OperationalError) no such table: node")
    assert mod.AdapterPool._is_empty(_Adapter(exc=exc), "micro") is True


def test_not_empty_when_populated():
    assert mod.AdapterPool._is_empty(_Adapter(items=["CHEBI:15377"]), "chebi") is False


def test_not_empty_on_other_error():
    # a genuinely broken adapter must NOT be masked as an empty skip.
    assert mod.AdapterPool._is_empty(_Adapter(exc=Exception("disk I/O error")), "chebi") is False


def test_pool_get_returns_empty_sentinel(monkeypatch):
    import oaklib

    exc = Exception("(sqlite3.OperationalError) no such table: rdfs_label_statement")
    monkeypatch.setattr(oaklib, "get_adapter", lambda selector: _Adapter(exc=exc))
    pool = mod.AdapterPool({"MICRO": "sqlite:obo:micro"})
    assert pool.get("MICRO") is mod.EMPTY_ADAPTER
    # case-insensitive: data carries lowercase `micro:`
    assert pool.get("micro") is mod.EMPTY_ADAPTER


def test_empty_adapter_not_an_error_verdict():
    assert "SKIPPED_EMPTY_ADAPTER" not in mod._ERROR_VERDICTS
