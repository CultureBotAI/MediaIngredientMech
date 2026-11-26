"""#1559: legacy occurrence readers must not leak their large-field budget."""

from __future__ import annotations

import csv
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ("build_culturemech_membership", "refresh_occurrence_statistics")


@pytest.fixture(params=SCRIPTS)
def reader(request, monkeypatch):
    previous = csv.field_size_limit()
    monkeypatch.setattr(sys, "path", sys.path.copy())
    spec = importlib.util.spec_from_file_location(
        "csv_state_" + request.param, ROOT / "scripts" / (request.param + ".py")
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
        yield module
    finally:
        csv.field_size_limit(previous)


def read(module, path):
    if module.__name__.endswith("build_culturemech_membership"):
        return module.collect(path, {"CHEBI:1"})
    return module.read_occurrences(path)


def table(path, payload="{}"):
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(["resolved_identifier", "recipe_id", "ingredient_json"])
        writer.writerows([["CHEBI:1", "CultureMech:1", payload]] * 2)
    return path


@pytest.mark.parametrize("script", SCRIPTS)
@pytest.mark.parametrize("prior", [4096, 131072])
def test_import_preserves_caller_csv_limit_in_fresh_process(script, prior):
    program = """
import csv, importlib.util, json, sys
csv.field_size_limit(int(sys.argv[2]))
before = csv.field_size_limit()
spec = importlib.util.spec_from_file_location('fresh_legacy_reader', sys.argv[1])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
print(json.dumps({'before': before, 'after': csv.field_size_limit()}))
"""
    result = subprocess.run(
        [sys.executable, "-B", "-c", program, str(ROOT / "scripts" / (script + ".py")), str(prior)],
        cwd=ROOT,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
        capture_output=True,
        text=True,
        timeout=30,
        check=True,
    )
    assert json.loads(result.stdout) == {"before": prior, "after": prior}


@pytest.mark.parametrize("prior", [4096, 131072])
def test_large_cell_read_uses_existing_budget_and_restores_caller(
    reader, tmp_path, monkeypatch, prior
):
    payload = "\u03bb" * 131073
    path = table(tmp_path / "large.tsv", payload)
    route = reader.mim_identifier_for_occurrence
    seen = []

    def observe(row):
        assert csv.field_size_limit() == 1 << 30
        assert row["ingredient_json"] == payload
        seen.append(row)
        return route(row)

    monkeypatch.setattr(reader, "mim_identifier_for_occurrence", observe)
    csv.field_size_limit(prior)
    result = read(reader, path)
    assert csv.field_size_limit() == prior
    assert len(seen) == 2
    if reader.__name__.endswith("build_culturemech_membership"):
        assert result == ({("CHEBI:1", "CultureMech:1"): 2}, {})
    else:
        assert result == ({"CHEBI:1": (1, 2)}, 2, 1)


@pytest.mark.parametrize("prior", [4096, 131072])
def test_missing_required_column_restores_caller_after_system_exit(reader, tmp_path, prior):
    path = tmp_path / "missing-column.tsv"
    path.write_text("resolved_identifier\nCHEBI:1\n", encoding="utf-8")
    csv.field_size_limit(prior)
    with pytest.raises(SystemExit, match="recipe_id"):
        read(reader, path)
    assert csv.field_size_limit() == prior


def test_decode_failure_restores_caller(reader, tmp_path):
    path = tmp_path / "invalid-utf8.tsv"
    path.write_bytes(b"resolved_identifier\trecipe_id\nCHEBI:1\t\xff\n")
    csv.field_size_limit(4096)
    with pytest.raises(UnicodeDecodeError):
        read(reader, path)
    assert csv.field_size_limit() == 4096


def test_reader_iteration_failure_restores_caller(reader, tmp_path, monkeypatch):
    path = table(tmp_path / "reader-failure.tsv")

    class FailingReader:
        fieldnames = ["resolved_identifier", "recipe_id"]

        def __init__(self, *args, **kwargs):
            assert csv.field_size_limit() == 1 << 30

        def __iter__(self):
            raise csv.Error("synthetic reader failure")

    monkeypatch.setattr(csv, "DictReader", FailingReader)
    csv.field_size_limit(4096)
    with pytest.raises(csv.Error, match="synthetic reader failure"):
        read(reader, path)
    assert csv.field_size_limit() == 4096


def test_row_processing_failure_restores_caller(reader, tmp_path, monkeypatch):
    path = table(tmp_path / "processing-failure.tsv")

    def fail(row):
        assert csv.field_size_limit() == 1 << 30
        raise RuntimeError("synthetic row failure")

    monkeypatch.setattr(reader, "mim_identifier_for_occurrence", fail)
    csv.field_size_limit(4096)
    with pytest.raises(RuntimeError, match="synthetic row failure"):
        read(reader, path)
    assert csv.field_size_limit() == 4096


def test_open_failure_preserves_caller(reader, tmp_path):
    csv.field_size_limit(4096)
    with pytest.raises(FileNotFoundError):
        read(reader, tmp_path / "missing.tsv")
    assert csv.field_size_limit() == 4096
