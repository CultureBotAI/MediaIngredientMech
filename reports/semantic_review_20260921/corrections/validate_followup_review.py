"""Check current review integrity and optionally require semantic approval."""

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent


def validate(report):
    for path, expected in report["inputs"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected, path
    paths = {
        str(p.relative_to(ROOT))
        for group in ("mapped", "unmapped")
        for p in (ROOT / "data/ingredients" / group).glob("*.yaml")
    }
    assert paths == set(report["record_inputs"]), "Incomplete record coverage"
    for path, expected in report["record_inputs"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected, path
    assert report["record_count"] == len(paths)
    with (HERE / "current_records.tsv").open() as stream:
        records = list(csv.DictReader(stream, delimiter="\t"))
    assert {r["source_record"] for r in records} == paths
    assert dict(Counter(r["mapping_status"] for r in records)) == report["statuses"]
    with (HERE / "blocker_dispositions.tsv").open() as stream:
        dispositions = list(csv.DictReader(stream, delimiter="\t"))
    assert dict(Counter(r["disposition"] for r in dispositions)) == report["blocker_dispositions"]
    bundle = ROOT / "output/mim-kgx-20260921-identity-corrections"
    graph = json.loads((bundle / "manifest.json").read_text())
    assert report["graph_counts"] == graph["counts"]
    counts = {"prediction_only": 0, "empty": 0, "cellular_without_context": 0}
    with (bundle / "mim_edges.tsv").open() as stream:
        for edge in csv.DictReader(stream, delimiter="\t", quoting=csv.QUOTE_NONE):
            if not edge["assertion_type"].endswith("_roles"):
                continue
            assertion = json.loads(edge["assertion_json"])
            evidence = assertion.get("evidence") or []
            counts["empty"] += not evidence
            counts["prediction_only"] += bool(evidence) and all(
                item.get("reference_type") == "COMPUTATIONAL_PREDICTION" for item in evidence
            )
            counts["cellular_without_context"] += edge[
                "assertion_type"
            ] == "cellular_metabolic_roles" and not assertion.get("metabolic_context")
    assert counts == report["role_evidence"], "Role evidence counts disagree with graph"
    unresolved = report["blocker_dispositions"].get("WITHDRAWN_PENDING_SOURCE", 0) or any(
        report["role_evidence"].values()
    )
    assert (
        not unresolved or report["release_verdict"] == "FAIL"
    ), "Unresolved findings cannot receive semantic approval"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--require-pass", action="store_true")
    args = ap.parse_args()
    report = json.loads((HERE / "current-review.json").read_text())
    validate(report)
    print("Review integrity PASS; semantic release verdict " + report["release_verdict"])
    if args.require_pass and report["release_verdict"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
