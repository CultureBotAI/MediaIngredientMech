"""Guards for the kg_microbe_node_id drift gate (#554)."""

import csv
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "audit_kg_microbe_node_ids.py"


def rec(identifier, term, kg_microbe_node_id=None, status="MAPPED"):
    record = {
        "identifier": identifier,
        "preferred_term": term,
        "mapping_status": status,
    }
    if kg_microbe_node_id is not None:
        record["kg_microbe_node_id"] = kg_microbe_node_id
    return record


def build(tmp_path, mapped, unmapped=()):
    """A minimal repo tree the script can run against."""
    data_dir = tmp_path / "data" / "curated"
    data_dir.mkdir(parents=True, exist_ok=True)
    for name, records in (("mapped", mapped), ("unmapped", unmapped)):
        (data_dir / f"{name}_ingredients.yaml").write_text(
            yaml.safe_dump({"total_count": len(records), "ingredients": list(records)})
        )
    (tmp_path / "scripts").mkdir(exist_ok=True)
    (tmp_path / "scripts" / SCRIPT.name).write_text(SCRIPT.read_text())
    return tmp_path


def run(tmp_path, *args):
    return subprocess.run(
        [sys.executable, str(tmp_path / "scripts" / SCRIPT.name), *args],
        capture_output=True,
        text=True,
    )


def report_rows(tmp_path):
    report = tmp_path / "reports" / "kg_microbe_node_id_mismatches.tsv"
    with report.open(newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


@pytest.fixture
def repo(tmp_path):
    return build(
        tmp_path,
        [
            rec("CHEBI:1", "Glycerol", "CHEBI:1"),
            rec("CHEBI:2", "Water"),
        ],
    )


def test_check_passes_when_all_present_node_ids_match(repo):
    out = run(repo, "--check")

    assert out.returncode == 0
    assert report_rows(repo) == []


def test_catalog_has_no_same_prefix_node_id_drift():
    out = subprocess.run(
        [sys.executable, str(SCRIPT), "--check"],
        capture_output=True,
        text=True,
    )

    assert out.returncode == 0, out.stdout + out.stderr
    assert "0 same-prefix mismatch(es)" in out.stdout


def test_same_prefix_mismatch_fails(repo):
    path = repo / "data" / "curated" / "mapped_ingredients.yaml"
    doc = yaml.safe_load(path.read_text())
    doc["ingredients"].append(rec("CHEBI:3", "Stale glucose", "CHEBI:4"))
    path.write_text(yaml.safe_dump(doc))

    out = run(repo, "--check")

    assert out.returncode == 2
    assert "same-prefix" in out.stdout
    assert "CHEBI:4 -> CHEBI:3" in out.stdout
    assert report_rows(repo)[0]["mismatch_type"] == "same_prefix"


def test_cross_prefix_mismatches_pass_check_but_are_reported(tmp_path):
    repo = build(tmp_path, [rec("CHEBI:1", "Local anchor", "MIM:Local_anchor")])

    out = run(repo, "--check")

    assert out.returncode == 0
    rows = report_rows(repo)
    assert len(rows) == 1
    assert rows[0]["mismatch_type"] == "cross_prefix"
    assert rows[0]["identifier_prefix"] == "CHEBI"
    assert rows[0]["kg_microbe_prefix"] == "MIM"


def test_unmapped_collection_is_checked(tmp_path):
    repo = build(
        tmp_path,
        [rec("CHEBI:1", "Water", "CHEBI:1")],
        [
            rec(
                "kgmicrobe.compound:1",
                "Thing",
                "kgmicrobe.compound:2",
                status="UNMAPPED",
            )
        ],
    )

    out = run(repo, "--check")

    assert out.returncode == 2
    rows = report_rows(repo)
    assert rows[0]["collection"] == "unmapped"
    assert rows[0]["preferred_term"] == "Thing"


def test_missing_kg_microbe_node_id_is_ignored(repo):
    out = run(repo, "--check")

    assert out.returncode == 0
    assert "0 kg_microbe_node_id mismatch(es)" in out.stdout


def test_report_uses_lf_line_endings(repo):
    assert run(repo, "--check").returncode == 0

    report = repo / "reports" / "kg_microbe_node_id_mismatches.tsv"
    assert b"\r" not in report.read_bytes()


def test_missing_or_corrupt_collection_exits_2_not_traceback(repo):
    (repo / "data" / "curated" / "unmapped_ingredients.yaml").unlink()
    out = run(repo, "--check")
    assert out.returncode == 2 and "Traceback" not in out.stderr

    build(repo, [rec("CHEBI:1", "Water", "CHEBI:1")])
    (repo / "data" / "curated" / "mapped_ingredients.yaml").write_text("{[not yaml")
    out = run(repo, "--check")
    assert out.returncode == 2 and "Traceback" not in out.stderr
