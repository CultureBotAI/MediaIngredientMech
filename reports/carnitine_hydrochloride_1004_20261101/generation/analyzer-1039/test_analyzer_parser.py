"""Run-owned #1039 regressions against immutable captured products.

Historical full-artifact counts here bind the fixture bytes; they are not live
corpus-size assumptions. No test executes analyzer.main or writes to the repo.
"""

from __future__ import annotations

import csv
import gzip
import hashlib
import importlib.util
import io
import json
import os
import sys
from pathlib import Path

import pytest
import yaml

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
SOURCE = Path(os.environ.get("ANALYZER_1039_SOURCE", RUN / "analyze_step3_final.py"))
HASH_NAMES = ("#N2", "#N2O", "#argon", "#Ar")


@pytest.fixture(scope="module")
def analyzer():
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location("run_owned_analyzer_1039", SOURCE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def fixture_bytes():
    manifest = json.loads((HERE / "fixture-manifest.json").read_text())
    result = {}
    for name, entry in manifest["fixtures"].items():
        packed = (HERE / "fixtures" / name).read_bytes()
        assert hashlib.sha256(packed).hexdigest() == entry["sha256"]
        raw = gzip.decompress(packed)
        assert hashlib.sha256(raw).hexdigest() == entry["uncompressed_sha256"]
        assert len(raw) == entry["bytes"]
        result[name] = raw
    return result


def test_plain_unified_keeps_all_four_hash_names_and_seven_occurrences(analyzer, fixture_bytes):
    raw = fixture_bytes["unified-after.tsv.gz"]
    expected = list(csv.DictReader(io.StringIO(raw.decode()), delimiter="\t"))
    fields, rows = analyzer.table(raw, format="plain")
    assert rows == expected
    assert len(fields) == 10
    assert len(rows) == 4170
    assert sum(int(row["occurrence_count"]) for row in rows) == 209330
    assert {row["ingredient_name"]: int(row["occurrence_count"]) for row in rows if row["ingredient_name"].startswith("#")} == {"#N2": 3, "#N2O": 2, "#argon": 1, "#Ar": 1}


def bind_unified(analyzer, monkeypatch, fixture_bytes, after=None):
    def read_before(path):
        assert path == "UNIFIED_INGREDIENT_MAPPING.tsv"
        return fixture_bytes["unified-before.tsv.gz"]

    def read_current(path):
        assert path == "UNIFIED_INGREDIENT_MAPPING.tsv"
        return fixture_bytes["unified-after.tsv.gz"] if after is None else after

    monkeypatch.setattr(analyzer, "old", read_before)
    monkeypatch.setattr(analyzer, "current", read_current)
    return {analyzer.SURVIVOR: yaml.safe_load(fixture_bytes["salt-owner-after.yaml.gz"])}


def test_native_unified_comparison_reports_complete_fixture_population(analyzer, monkeypatch, fixture_bytes):
    records = bind_unified(analyzer, monkeypatch, fixture_bytes)
    result = analyzer.unified_check(records)
    assert result["rows"] == 4170
    assert result["unchanged_rows"] == 4169
    assert result["changed_rows"] == 1
    assert result["occurrences_before"] == result["occurrences_after"] == 209330
    assert result["every_occurrence_cell_preserved"]
    assert result["unrelated_raw_bytes_preserved"]


def change_hash_row(raw, name, field, value):
    lines = raw.splitlines(keepends=True)
    fields = lines[0].decode().rstrip("\n").split("\t")
    matched = [index for index, line in enumerate(lines) if line.startswith((name + "\t").encode())]
    assert len(matched) == 1
    index = matched[0]
    if field == "REMOVE":
        del lines[index]
    elif field == "DUPLICATE":
        lines.insert(index + 1, lines[index])
    else:
        values = lines[index].decode().rstrip("\n").split("\t")
        values[fields.index(field)] = value
        lines[index] = ("\t".join(values) + "\n").encode()
    return b"".join(lines)


@pytest.mark.parametrize("name", HASH_NAMES)
@pytest.mark.parametrize("field,value", [("occurrence_count", "999"), ("cas_rn", "not-the-original-value")])
def test_hash_row_change_is_detected_in_parsed_scope(analyzer, monkeypatch, fixture_bytes, name, field, value):
    changed = change_hash_row(fixture_bytes["unified-after.tsv.gz"], name, field, value)
    records = bind_unified(analyzer, monkeypatch, fixture_bytes, changed)
    with pytest.raises(ValueError, match="Unified changed more than the one approved name"):
        analyzer.unified_check(records)


@pytest.mark.parametrize("name", HASH_NAMES)
def test_hash_row_removal_is_a_population_change(analyzer, monkeypatch, fixture_bytes, name):
    changed = change_hash_row(fixture_bytes["unified-after.tsv.gz"], name, "REMOVE", "")
    records = bind_unified(analyzer, monkeypatch, fixture_bytes, changed)
    with pytest.raises(ValueError, match="Unified ingredient population changed"):
        analyzer.unified_check(records)


def test_hash_row_duplicate_is_not_silently_filtered(analyzer, monkeypatch, fixture_bytes):
    changed = change_hash_row(fixture_bytes["unified-after.tsv.gz"], "#N2", "DUPLICATE", "")
    records = bind_unified(analyzer, monkeypatch, fixture_bytes, changed)
    with pytest.raises(ValueError, match="Duplicate unified ingredient name"):
        analyzer.unified_check(records)


def test_native_sssom_metadata_prelude_still_parses(analyzer, fixture_bytes):
    raw = fixture_bytes["canonical-after.sssom.tsv.gz"]
    assert raw.startswith(b"# curie_map:")
    fields, rows = analyzer.table(raw, format="sssom")
    assert fields[0] == "subject_id"
    assert len(rows) == 2982
    salt = next(row for row in rows if row["subject_id"] == analyzer.SUBJECT)
    assert salt["object_id"] == "NCIT:C216679"


@pytest.mark.parametrize("format", ["sssom", "commented-membership"])
def test_comment_enabled_transport_preserves_hash_data_after_header(analyzer, format):
    # This is a transport-only fixture, not a claim that '#literal' is a CURIE.
    raw = b"# example: metadata\nname\tvalue\n#literal\t2\nordinary\t3\n"
    fields, rows = analyzer.table(raw, format=format)
    assert fields == ["name", "value"]
    assert rows == [{"name": "#literal", "value": "2"}, {"name": "ordinary", "value": "3"}]


def test_membership_prelude_is_explicit_and_preserved_as_metadata(analyzer):
    raw = b"# source=immutable-test\nmim_identifier\trecipe_id\toccurrences\nNCIT:C216679\tCultureMech:015654\t1\n"
    fields, rows = analyzer.table(raw, format="commented-membership")
    assert fields == ["mim_identifier", "recipe_id", "occurrences"]
    assert rows == [{"mim_identifier": "NCIT:C216679", "recipe_id": "CultureMech:015654", "occurrences": "1"}]


def test_plain_header_and_name_can_both_begin_with_hash(analyzer):
    fields, rows = analyzer.table(b"#name\tcount\n#N2\t3\n", format="plain")
    assert fields == ["#name", "count"]
    assert rows == [{"#name": "#N2", "count": "3"}]


def test_rejection_ledger_is_plain_tsv(analyzer):
    raw = b"ingredient_name\trejected_id\tmim_id\treason\n#gas\tCHEBI:1\tNCIT:1\tfixture\n"
    _, rows = analyzer.table(raw, format="plain")
    assert rows[0]["ingredient_name"] == "#gas"


def test_format_is_required_and_unknown_format_is_rejected(analyzer):
    with pytest.raises(TypeError):
        analyzer.table(b"name\tcount\nname\t1\n")
    with pytest.raises(ValueError, match="Unknown TSV format"):
        analyzer.table(b"name\tcount\nname\t1\n", format="guess")


def test_plain_malformed_row_remains_rejected(analyzer):
    with pytest.raises(ValueError, match="Malformed TSV"):
        analyzer.table(b"name\tcount\n#not-a-complete-row\n", format="plain")
