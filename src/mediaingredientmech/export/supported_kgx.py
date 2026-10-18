"""Export only explicitly approved assertions, preserving excluded science separately.

PASS applies to the reviewed assertion subset. It never changes the full graph's
semantic verdict, and raw ingredient annotations remain exclusively in the backlog.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import io
import json
import os
import tarfile
import tempfile
from pathlib import Path

import yaml

from mediaingredientmech.export.kgx import EDGE_COLUMNS, NODE_COLUMNS
from mediaingredientmech.validation.semantic_release import local, require, rows, sha
from mediaingredientmech.validation.semantic_release import validate as validate_full_review


def _json(value) -> bytes:
    return (json.dumps(value, ensure_ascii=True, sort_keys=True, indent=2) + "\n").encode()


def _tsv(columns, records) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.writer(
        stream, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_NONE, quotechar=None
    )
    writer.writerow(columns)
    for record in records:
        values = [str(record.get(column, "")) for column in columns]
        require(
            all(not any(c in value for c in ("\t", "\r", "\n", "\x00")) for value in values),
            "Unsupported TSV control character",
        )
        writer.writerow(values)
    return stream.getvalue().encode()


def _key(row):
    return row["source_record"], row["assertion_type"], row["source_position"]


def _supported(edge):
    """A disposition cannot override a currently explicit unsupported-evidence flag."""
    claim = json.loads(edge["assertion_json"])
    kind = edge["assertion_type"]
    if kind.endswith("_roles"):
        evidence = claim.get("evidence") or []
        require(
            bool(evidence)
            and not all(e.get("reference_type") == "COMPUTATIONAL_PREDICTION" for e in evidence),
            "Approved subset contains an unsupported role",
        )
        if kind == "cellular_metabolic_roles":
            require(
                bool(claim.get("metabolic_context")),
                "Approved cellular role lacks organism context",
            )
    elif kind == "component":
        require(
            claim["component_assertion"]["method"]
            not in {"ABBREVIATION_EXPANSION", "CURATED_INTERPRETATION"},
            "Approved subset contains an unverified component interpretation",
        )
    elif kind == "recipe_reference":
        require(
            claim["relationship"] != "CANDIDATE_UNVERIFIED",
            "Approved subset contains an unverified recipe candidate",
        )


def _state(root: Path, report_path: Path):
    verdict = validate_full_review(root, report_path)
    report = json.loads(report_path.read_text())
    bundle = local(root, report["bundle"])
    nodes = rows(bundle / "mim_nodes.tsv", kgx=True)
    edges = rows(bundle / "mim_edges.tsv", kgx=True)
    dispositions = rows(local(root, report["assertion_dispositions"]))
    decisions = {_key(row): row for row in dispositions}
    require(len(decisions) == len(dispositions), "Duplicate current assertion decision")
    selected, excluded = [], []
    for edge in edges:
        decision = decisions[_key(edge)]
        if decision["resolution_status"] == "APPROVED":
            _supported(edge)
            selected.append(edge)
        else:
            excluded.append({"edge": edge, "review": decision})
    require(bool(selected), "Cannot publish an empty approved assertion subset")
    return report, verdict, nodes, selected, excluded


def _safe_nodes(nodes, selected):
    """Source labels identify records; ontology identity lives only in approved edges."""
    source = {node["id"]: node for node in nodes}
    result = {}
    for identifier, node in source.items():
        if node["node_kind"] == "ingredient":
            result[identifier] = {
                "id": identifier,
                "name": node["name"],
                "category": "biolink:NamedThing",
                "provided_by": "MIM:ingredients",
                "node_kind": "ingredient",
                "source_record": node["source_record"],
            }
    needed = {edge[endpoint] for edge in selected for endpoint in ("subject", "object")}
    labels: dict[str, set[str]] = {}
    for edge in selected:
        claim = json.loads(edge["assertion_json"])
        kind = edge["assertion_type"]
        if kind == "mapping":
            identifier, label = claim["object_id"], claim["object_label"]
        elif kind == "component":
            identifier, label = edge["object"], claim["component"]["component_name"]
        elif kind == "environment":
            identifier, label = edge["object"], claim.get("environment_label", "")
        elif kind == "recipe_reference":
            identifier, label = edge["object"], claim.get("medium_name", "")
        else:
            identifier, label = edge["object"], claim["role"]
        if label:
            labels.setdefault(identifier, set()).add(label)
    for identifier in sorted(needed - result.keys()):
        original = source[identifier]
        result[identifier] = {
            "id": identifier,
            "name": min(labels.get(identifier) or {identifier}),
            "category": "biolink:NamedThing",
            "provided_by": "MIM:ingredients",
            "node_kind": original["node_kind"],
        }
    return [result[identifier] for identifier in sorted(result)]


def _supported_sssom(root, selected):
    source = root / "mappings/ingredient_mappings.sssom.tsv"
    lines = source.read_text().splitlines(keepends=True)
    metadata = yaml.safe_load("".join(line[1:] for line in lines if line.startswith("#")))
    source_id = metadata.get(
        "mapping_set_id", "https://w3id.org/sssom/mappings/culturebotai_mim_ingredient"
    )
    metadata["mapping_set_id"] = str(source_id).rstrip("/") + "/supported"
    metadata["mapping_set_description"] = (
        "MediaIngredientMech mappings individually approved by the current content-bound semantic review. "
        "This reviewed subset excludes unresolved mappings; it does not approve the full source graph."
    )
    mapping_edges = sorted(
        (edge for edge in selected if edge["assertion_type"] == "mapping"),
        key=lambda edge: int(edge["source_position"]),
    )
    mapping_rows = [json.loads(edge["assertion_json"]) for edge in mapping_edges]
    columns = list(
        csv.DictReader(
            (line for line in lines if not line.startswith("#")), delimiter="\t"
        ).fieldnames
        or []
    )
    require(bool(columns), "Source SSSOM header is missing")
    stream = io.StringIO(newline="")
    stream.write(
        "".join(
            "# " + line + "\n" for line in yaml.safe_dump(metadata, sort_keys=False).splitlines()
        )
    )
    writer = csv.DictWriter(stream, fieldnames=columns, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(mapping_rows)
    return stream.getvalue().encode(), len(mapping_rows), metadata["mapping_set_id"]


def _expected(root: Path, report_path: Path) -> tuple[dict, dict[str, bytes]]:
    root = root.resolve()
    report_path = (root / report_path).resolve()
    require(report_path.is_relative_to(root), "Full review report must be inside the repository")
    report, verdict, full_nodes, selected, excluded = _state(root, report_path)
    selected = sorted(selected, key=lambda edge: edge["id"])
    safe_nodes = _safe_nodes(full_nodes, selected)
    sssom, mapping_count, mapping_set_id = _supported_sssom(root, selected)
    report_name = str(report_path.relative_to(root))
    source_report_sha = sha(report_path)
    backlog = {
        "schema_version": 1,
        "scope": "raw_full_graph_nodes_and_unapproved_assertions",
        "full_report": report_name,
        "full_report_sha256": source_report_sha,
        "full_release_verdict": verdict["semantic_release"],
        "full_bundle": report["bundle"],
        "node_policy": "All original raw source nodes are preserved here, including unreviewed record annotations. They are not part of the supported graph archive.",
        "nodes": sorted(full_nodes, key=lambda node: node["id"]),
        "assertions": sorted(excluded, key=lambda item: item["edge"]["id"]),
    }
    files = {
        "mim_nodes.tsv": _tsv(NODE_COLUMNS, safe_nodes),
        "mim_edges.tsv": _tsv(EDGE_COLUMNS, selected),
        "unsupported-backlog.json": _json(backlog),
        "ingredient_mappings.sssom.tsv": sssom,
    }
    manifest = {
        "schema_version": 1,
        "scope": "reviewed_assertion_subset",
        "release_verdict": "PASS",
        "full_release_verdict": verdict["semantic_release"],
        "full_report": report_name,
        "full_report_sha256": source_report_sha,
        "full_bundle": report["bundle"],
        "full_bundle_manifest_sha256": sha(local(root, report["bundle"] + "/manifest.json")),
        "curie_map": json.loads(local(root, report["bundle"] + "/manifest.json").read_text()).get(
            "curie_map", {}
        ),
        "assertion_dispositions": report["assertion_dispositions"],
        "assertion_dispositions_sha256": sha(local(root, report["assertion_dispositions"])),
        "counts": {
            "nodes": len(safe_nodes),
            "edges": len(selected),
            "sssom_rows": mapping_count,
            "active_ingredient_record_nodes": sum(
                node["node_kind"] == "ingredient" for node in safe_nodes
            ),
            "full_nodes": len(full_nodes),
            "full_edges": len(selected) + len(excluded),
            "backlog_raw_nodes": len(full_nodes),
            "backlog_unapproved_edges": len(excluded),
        },
        "members": {
            name: {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}
            for name, data in files.items()
            if name in {"mim_nodes.tsv", "mim_edges.tsv"}
        },
        "sssom": {
            "path": "ingredient_mappings.sssom.tsv",
            "mapping_set_id": mapping_set_id,
            "rows": mapping_count,
            "sha256": hashlib.sha256(sssom).hexdigest(),
            "bytes": len(sssom),
        },
        "backlog": {
            "path": "unsupported-backlog.json",
            "sha256": hashlib.sha256(files["unsupported-backlog.json"]).hexdigest(),
            "bytes": len(files["unsupported-backlog.json"]),
        },
        "archive_members": ["manifest.json", "mim_nodes.tsv", "mim_edges.tsv"],
        "implementation": {
            "export/supported_kgx.py": sha(Path(__file__)),
            "validation/semantic_release.py": sha(
                Path(__file__).parents[1] / "validation/semantic_release.py"
            ),
        },
        "limitations": [
            "PASS certifies only the explicitly approved assertion subset; the full graph retains its separate verdict.",
            "Ingredient nodes are source-record references with source labels, not approvals of all ingredient annotations or chemical identity.",
            "All node categories are NamedThing; chemical identity, roles, components, and hierarchy are asserted only by selected approved edges.",
            "Excluded assertions and all original raw node annotations are retained in the separate hash-bound backlog, outside the graph archive.",
        ],
    }
    files["manifest.json"] = _json(manifest)
    return manifest, files


def _archive(files) -> bytes:
    stream = io.BytesIO()
    with gzip.GzipFile(fileobj=stream, mode="wb", filename="", mtime=0) as gz:
        with tarfile.open(fileobj=gz, mode="w", format=tarfile.USTAR_FORMAT) as tar:
            for name in ("manifest.json", "mim_nodes.tsv", "mim_edges.tsv"):
                info = tarfile.TarInfo(name)
                info.size, info.mtime, info.mode = len(files[name]), 0, 0o644
                tar.addfile(info, io.BytesIO(files[name]))
    return stream.getvalue()


def validate_supported(root: Path, report_path: Path, output: Path) -> dict:
    """Recheck source science decisions, exact selection, sanitization, and archive."""
    manifest, expected = _expected(root, report_path)
    for name, data in expected.items():
        require(
            (output / name).read_bytes() == data,
            f"Supported release differs from reviewed selection: {name}",
        )
    archive_path = output / "mim-kgx.tar.gz"
    require(
        archive_path.read_bytes() == _archive(expected),
        "Supported archive differs from reviewed deterministic content",
    )
    with tarfile.open(archive_path, "r:gz") as archive:
        members = archive.getmembers()
        require(
            [member.name for member in members] == manifest["archive_members"],
            "Unexpected supported archive member",
        )
        for member in members:
            require(member.isfile(), "Supported archive contains a non-file member")
            stream = archive.extractfile(member)
            require(
                stream is not None and stream.read() == expected[member.name],
                "Supported archive content mismatch",
            )
    return {
        "integrity": "PASS",
        "semantic_release": "PASS",
        "scope": manifest["scope"],
        "full_release_verdict": manifest["full_release_verdict"],
        "counts": manifest["counts"],
        "archive_sha256": sha(archive_path),
    }


def export_supported(root: Path, report_path: Path, output: Path) -> dict:
    """Publish a reviewed subset and separate backlog into a new directory."""
    root, output = root.resolve(), output.resolve()
    report_path = (root / report_path).resolve()
    require(not output.exists(), f"Output already exists: {output}")
    manifest, files = _expected(root, report_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".mim-supported-", dir=output.parent) as temporary:
        staging = Path(temporary) / "bundle"
        staging.mkdir()
        for name, data in files.items():
            (staging / name).write_bytes(data)
        (staging / "mim-kgx.tar.gz").write_bytes(_archive(files))
        validate_supported(root, report_path, staging)
        require(not output.exists(), f"Output appeared while building: {output}")
        os.rename(staging, output)
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()
    result = (
        validate_supported(args.root, args.report, args.output)
        if args.validate_only
        else export_supported(args.root, args.report, args.output)
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
