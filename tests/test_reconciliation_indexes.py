"""Navigation snapshots must agree with their declared immutable observations."""

import csv
import subprocess
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
ROUND = ROOT / "reviews/reconciliation/20261011T023739Z-all-mim"


def read_tsv(name):
    with (ROUND / name).open() as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


@pytest.fixture(scope="module")
def snapshot():
    records = read_tsv("records.tsv")
    current = read_tsv("current-findings.tsv")
    paths = {r["review_yaml"] for r in records + current}
    documents = {p: yaml.load((ROOT / p).read_bytes(), Loader=yaml.CSafeLoader) for p in paths}
    return records, current, documents


def test_original_record_index_is_exact_disjoint_snapshot(snapshot):
    records, _, documents = snapshot
    assert len(records) == len({r["path"] for r in records})
    expected = {}
    for path in {r["review_yaml"] for r in records}:
        d = documents[path]
        for target in d["targets"]:
            assert target["path"] not in expected
            findings = [f for f in d["findings"] if target["target_id"] in f["target_ids"]]
            expected[target["path"]] = (
                path,
                target["target_id"],
                sum(f["status"] == "open" for f in findings),
                sum(f["status"] == "deferred" for f in findings),
            )
    assert {
        r["path"]: (
            r["review_yaml"],
            r["target_id"],
            int(r["open_findings"]),
            int(r["deferred_findings"]),
        )
        for r in records
    } == expected


def test_archived_review_bases_match_saved_provenance(snapshot):
    _, _, documents = snapshot
    sources = {d["source"]["git_revision"] for d in documents.values()}
    for row in read_tsv("provenance-bases.tsv"):
        assert row["git_revision"] in sources
        assert row["retained_ref"].startswith("refs/tags/review-source/")
        result = subprocess.run(
            ["git", "rev-parse", "--verify", row["retained_ref"] + "^{commit}"],
            cwd=ROOT,
            check=True,
            text=True,
            capture_output=True,
        )
        assert result.stdout.strip() == row["git_revision"]


def test_current_index_preserves_exact_heads_and_target_scope(snapshot):
    _, current, documents = snapshot
    occurrences = {}
    for path, d in documents.items():
        for finding in d["findings"]:
            key = (d["repository"].lower(), d["review_id"], finding["finding_id"])
            assert key not in occurrences
            occurrences[key] = (path, d, finding)
    replaced = set()
    for _, d, finding in occurrences.values():
        for previous in finding.get("previous_occurrences", []):
            key = (previous["repository"].lower(), previous["review_id"], previous["finding_id"])
            _, old, predecessor = occurrences[key]
            assert predecessor["issue_key"] == finding["issue_key"]
            assert set(predecessor["target_ids"]) <= set(finding["target_ids"])
            assert old["finished_at"] <= d["started_at"]
            replaced.add(key)
    heads = {key: value for key, value in occurrences.items() if key not in replaced}
    # Keep multiple heads if a future snapshot contains competing observations.
    assert len(current) == len(heads)
    expected = {}
    for path, d, f in heads.values():
        targets = {t["target_id"]: t for t in d["targets"]}
        expected[(path, f["finding_id"])] = (
            f["issue_key"],
            f["status"],
            f["severity"],
            f["title"],
            "|".join(targets[t]["path"] for t in f["target_ids"]),
            "|".join(x["path"] for x in f["owner_paths"]),
            "|".join(f.get("external_issues", [])),
        )
    assert {
        (r["review_yaml"], r["finding_id"]): (
            r["issue_key"],
            r["status"],
            r["severity"],
            r["title"],
            r["paths"],
            r["owner_paths"],
            r["existing_issues"],
        )
        for r in current
    } == expected
