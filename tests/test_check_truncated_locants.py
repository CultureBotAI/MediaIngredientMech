"""Historical tombstones must not hide malformed active names (#313)."""
from __future__ import annotations

import csv
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location(
    "check_truncated_locants", ROOT / "scripts" / "check_truncated_locants.py"
)
assert SPEC is not None and SPEC.loader is not None
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


@pytest.fixture
def records(tmp_path, monkeypatch):
    monkeypatch.setattr(checker, "INGREDIENTS", tmp_path)

    def write(directory, name, label, status):
        path = tmp_path / directory / f"{name}.yaml"
        path.parent.mkdir(parents=True, exist_ok=True)
        record = {"identifier": "CHEBI:41189", "preferred_term": label}
        if status is not None:
            record["mapping_status"] = status
        path.write_text(json.dumps(record), encoding="utf-8")
        return path

    return write


@pytest.mark.parametrize("directory", ["mapped", "unmapped"])
@pytest.mark.parametrize("label", ["4-Diamino-6", "4-diol"])
def test_rejected_historical_labels_are_preserved_and_do_not_fail(
    records, directory, label, capsys
):
    path = records(directory, "historical", label, "REJECTED")
    before = path.read_bytes()

    assert checker.main([]) == 0
    assert "labels with a truncated locant list: 0" in capsys.readouterr().out
    assert path.read_bytes() == before


@pytest.mark.parametrize("directory", ["mapped", "unmapped"])
@pytest.mark.parametrize(
    "status", ["MAPPED", "UNMAPPED", "AMBIGUOUS", "NEEDS_EXPERT", None, "", "rejected", "UNKNOWN"]
)
def test_every_status_except_exact_rejected_still_fails(records, directory, status):
    records(directory, "current", "2-tetrachloroethane", status)

    assert checker.main(["--quiet"]) == 1


def test_tsv_retains_active_findings_alongside_rejected_tombstones(records, tmp_path):
    records("mapped", "active", "2-dimethylsuccinic acid", "MAPPED")
    records("unmapped", "retired", "4-diol", "REJECTED")
    report = tmp_path / "findings.tsv"

    assert checker.main(["--quiet", "--tsv", str(report)]) == 1
    with report.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    assert len(rows) == 1
    assert rows[0]["slug"] == "active"
    assert rows[0]["locants_found"] == "1"
    assert rows[0]["locants_needed"] == "2"


@pytest.mark.parametrize("label", ["4-Diamino-6", "4-diol", "2-dimethylsuccinic acid"])
def test_truncated_active_labels_keep_their_lexical_detection(label):
    assert checker.scan_label(label)


@pytest.mark.parametrize(
    "label",
    [
        "1,4-Butanediol",
        "2,3-dimethylsuccinic acid",
        "1,1,2,2-tetrachloroethane",
        "1-Pentanol",
        "3-octanone",
        "1-hexanol",
        "dimethyl sulfoxide",
    ],
)
def test_full_locants_and_valid_alkane_names_remain_valid(label):
    assert checker.scan_label(label) == []
