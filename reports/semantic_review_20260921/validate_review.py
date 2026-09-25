"""Verify review freshness/coverage; optionally enforce semantic release approval."""

import argparse
import csv
import hashlib
import io
import json
from pathlib import Path


def sha(data):
    return hashlib.sha256(data).hexdigest()


def packed(value):
    return json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":")).encode()


def rows(path, kgx=False):
    with path.open() as stream:
        return list(
            csv.DictReader(
                stream, delimiter="\t", quoting=csv.QUOTE_NONE if kgx else csv.QUOTE_MINIMAL
            )
        )


def validate(root, report):
    manifest = json.loads((report / "manifest.json").read_text())
    for name, expected in manifest["inputs"].items():
        assert sha((root / name).read_bytes()) == expected, f"Stale review input: {name}"
    for name, expected in manifest["members"].items():
        assert (
            sha((report / name).read_bytes()) == expected["sha256"]
        ), f"Changed review member: {name}"
        assert len(rows(report / name)) == expected["rows"], name
    bundle = root / "output/mim-kgx-20260921"
    assert sha((bundle / "mim-kgx.tar.gz").read_bytes()) == manifest["kgx_archive_sha256"]
    records = rows(report / "records.tsv")
    assert (
        len({r["source_record"] for r in records}) == len(records) == manifest["counts"]["records"]
    )
    paths = {
        str(p.relative_to(root))
        for group in ("mapped", "unmapped")
        for p in (root / "data/ingredients" / group).glob("*.yaml")
    }
    assert paths == {r["source_record"] for r in records}, "Record review coverage"
    record_index = {r["source_record"]: r for r in records}
    for row in records:
        data = (root / row["source_record"]).read_bytes()
        assert sha(data) == row["record_sha256"]
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert (
            blob == row["baseline_git_blob"]
        ), "Changed record cannot inherit a historical approval"
        assert sha((root / row["review_report"]).read_bytes()) == row["report_sha256"]
    nodes, edges = rows(bundle / "mim_nodes.tsv", True), rows(bundle / "mim_edges.tsv", True)
    node_reviews = rows(report / "kgx_nodes.tsv")
    edge_reviews = rows(report / "kgx_assertions.tsv")
    assert len(node_reviews) == len(nodes) == manifest["counts"]["kgx_nodes"]
    assert len(edge_reviews) == len(edges) == manifest["counts"]["kgx_assertions"]
    node_index = {r["node_id"]: r for r in node_reviews}
    edge_index = {r["edge_id"]: r for r in edge_reviews}
    assert set(node_index) == {r["id"] for r in nodes} and len(node_index) == len(nodes)
    assert set(edge_index) == {r["id"] for r in edges} and len(edge_index) == len(edges)
    for node in nodes:
        assert sha(packed(node)) == node_index[node["id"]]["node_sha256"]
    for edge in edges:
        review = edge_index[edge["id"]]
        assert sha(edge["assertion_json"].encode()) == review["assertion_sha256"]
        assert all(
            edge[k] == review[k] for k in ("subject", "predicate", "object", "assertion_type")
        )
        assert record_index[review["source_record"]]["record_sha256"] == review["record_sha256"]
    raw = (root / "mappings/ingredient_mappings.sssom.tsv").read_bytes()
    assert sha(raw) == manifest["sssom_sha256"]
    mappings = list(
        csv.DictReader(
            io.StringIO(
                b"".join(
                    l for l in raw.splitlines(keepends=True) if not l.startswith(b"#")
                ).decode()
            ),
            delimiter="\t",
        )
    )
    mapping_reviews = rows(report / "sssom.tsv")
    index = {(r["subject_id"], r["predicate_id"], r["object_id"]): r for r in mapping_reviews}
    assert len(index) == len(mapping_reviews) == len(mappings) == manifest["counts"]["sssom_rows"]
    for mapping in mappings:
        review = index[(mapping["subject_id"], mapping["predicate_id"], mapping["object_id"])]
        assert sha(packed(mapping)) == review["row_sha256"]
    # Independently check the semantic projection, not only source/data hashes.
    projection = {
        json.loads(e["assertion_json"])["subject_id"]
        + "\t"
        + json.loads(e["assertion_json"])["object_id"]: e
        for e in edges
        if e["assertion_type"] == "mapping"
    }
    assert len(projection) == len(mappings)
    for m in mappings:
        e = projection[m["subject_id"] + "\t" + m["object_id"]]
        subject, obj = m["subject_id"], m["object_id"]
        pred = m["predicate_id"]
        relation = pred
        if pred == "skos:broadMatch":
            predicate = "biolink:broad_match"
        elif pred.endswith("narrowMatch"):
            subject, obj, predicate = obj, subject, "biolink:broad_match"
            relation = "skos:broadMatch"
        else:
            predicate = {
                "skos:exactMatch": "biolink:exact_match",
                "skos:closeMatch": "biolink:close_match",
            }[pred]
        assert (e["subject"], e["predicate"], e["object"], e["relation"]) == (
            subject,
            predicate,
            obj,
            relation,
        )
    unresolved = any(
        r["verdict"] == "needs_curation" for r in records if r["mapping_status"] != "REJECTED"
    )
    assert (
        not unresolved or manifest["semantic_release_verdict"] == "FAIL"
    ), "Unresolved curation cannot yield a passing release"
    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--report", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--require-pass", action="store_true")
    args = parser.parse_args()
    result = validate(args.root, args.report)
    print(
        json.dumps(
            {
                "review_integrity": "PASS",
                "coverage": result["counts"],
                "semantic_release_verdict": result["semantic_release_verdict"],
            },
            indent=2,
        )
    )
    raise SystemExit(1 if args.require_pass and result["semantic_release_verdict"] != "PASS" else 0)
