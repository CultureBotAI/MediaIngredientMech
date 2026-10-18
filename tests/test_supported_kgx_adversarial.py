"""Rehashed, internally consistent corruption must not become a supported release."""

import csv
import gzip
import hashlib
import importlib.util
import io
import json
import tarfile
from pathlib import Path

import pytest

from mediaingredientmech.export.supported_kgx import export_supported, validate_supported
from mediaingredientmech.validation.semantic_release import rows


@pytest.fixture
def reviewed_subset(tmp_path):
    spec = importlib.util.spec_from_file_location(
        "supported_release_fixture", Path(__file__).with_name("test_supported_kgx.py")
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    root, report = module.full_failed_review.__wrapped__(tmp_path)
    output = root / "supported"
    export_supported(root, report, output)
    return root, report, output


def write_rows(path, records):
    with path.open("w") as stream:
        writer = csv.DictWriter(
            stream,
            fieldnames=list(records[0]),
            delimiter="\t",
            lineterminator="\n",
            quoting=csv.QUOTE_NONE,
            quotechar=None,
        )
        writer.writeheader()
        writer.writerows(records)


def rehash_and_repack(output):
    """Model an attacker updating hashes, counts, and the archive after tampering."""
    manifest_path = output / "manifest.json"
    manifest = json.loads(manifest_path.read_text())
    for name, entry in manifest["members"].items():
        data = (output / name).read_bytes()
        entry.update(sha256=hashlib.sha256(data).hexdigest(), bytes=len(data))
    for field in ("backlog", "sssom"):
        entry = manifest[field]
        data = (output / entry["path"]).read_bytes()
        entry.update(sha256=hashlib.sha256(data).hexdigest(), bytes=len(data))
    nodes = rows(output / "mim_nodes.tsv", kgx=True)
    edges = rows(output / "mim_edges.tsv", kgx=True)
    backlog = json.loads((output / "unsupported-backlog.json").read_text())
    manifest["counts"].update(
        nodes=len(nodes),
        edges=len(edges),
        backlog_raw_nodes=len(backlog["nodes"]),
        backlog_unapproved_edges=len(backlog["assertions"]),
    )
    manifest_path.write_text(json.dumps(manifest, sort_keys=True, indent=2) + "\n")
    with (output / "mim-kgx.tar.gz").open("wb") as stream:
        with gzip.GzipFile(fileobj=stream, mode="wb", filename="", mtime=0) as compressed:
            with tarfile.open(fileobj=compressed, mode="w", format=tarfile.USTAR_FORMAT) as archive:
                for name in manifest["archive_members"]:
                    data = (output / name).read_bytes()
                    member = tarfile.TarInfo(name)
                    member.size, member.mtime, member.mode = len(data), 0, 0o644
                    archive.addfile(member, io.BytesIO(data))
    for name, entry in manifest["members"].items():
        assert hashlib.sha256((output / name).read_bytes()).hexdigest() == entry["sha256"]
    return manifest


@pytest.mark.parametrize(
    "attack",
    [
        "raw_annotation_leak",
        "unreviewed_edge_added",
        "approved_edge_dropped",
        "backlog_record_lost",
        "backlog_assertion_lost",
        "false_sssom_target",
        "backlog_in_archive",
    ],
)
def test_rehashed_corruption_cannot_certify_itself(reviewed_subset, attack):
    root, report, output = reviewed_subset
    if attack == "raw_annotation_leak":
        nodes = rows(output / "mim_nodes.tsv", kgx=True)
        raw = next(
            node
            for node in rows(root / "full/mim_nodes.tsv", kgx=True)
            if node["id"] == "MIM:water"
        )
        next(node for node in nodes if node["id"] == "MIM:water")["record_json"] = raw[
            "record_json"
        ]
        write_rows(output / "mim_nodes.tsv", nodes)
    elif attack == "unreviewed_edge_added":
        (output / "mim_edges.tsv").write_bytes((root / "full/mim_edges.tsv").read_bytes())
        nodes = rows(output / "mim_nodes.tsv", kgx=True)
        ids = {node["id"] for node in nodes}
        for raw in rows(root / "full/mim_nodes.tsv", kgx=True):
            if raw["id"] not in ids:
                node = dict.fromkeys(nodes[0], "")
                node.update(
                    id=raw["id"],
                    name=raw["name"],
                    category="biolink:NamedThing",
                    node_kind=raw["node_kind"],
                )
                nodes.append(node)
        write_rows(output / "mim_nodes.tsv", nodes)
    elif attack == "approved_edge_dropped":
        path = output / "mim_edges.tsv"
        path.write_text(path.read_text().splitlines()[0] + "\n")
    elif attack.startswith("backlog_") and attack != "backlog_in_archive":
        path = output / "unsupported-backlog.json"
        backlog = json.loads(path.read_text())
        backlog["nodes" if attack == "backlog_record_lost" else "assertions"].pop()
        path.write_text(json.dumps(backlog))
    elif attack == "false_sssom_target":
        path = output / "ingredient_mappings.sssom.tsv"
        text = path.read_text()
        assert "CHEBI:15377" in text
        path.write_text(text.replace("CHEBI:15377", "CHEBI:78018"))
    else:
        path = output / "manifest.json"
        manifest = json.loads(path.read_text())
        manifest["archive_members"].append("unsupported-backlog.json")
        path.write_text(json.dumps(manifest))
    rehash_and_repack(output)
    with pytest.raises(ValueError, match="Supported release differs from reviewed selection"):
        validate_supported(root, report, output)


def test_changed_archive_headers_fail_even_with_identical_members(reviewed_subset):
    root, report, output = reviewed_subset
    archive_path = output / "mim-kgx.tar.gz"
    with tarfile.open(archive_path, "r:gz") as original:
        content = [(member.name, original.extractfile(member).read()) for member in original]
    with tarfile.open(archive_path, "w:gz") as changed:
        for name, data in content:
            member = tarfile.TarInfo(name)
            member.size, member.mode, member.mtime = len(data), 0o644, 12345
            changed.addfile(member, io.BytesIO(data))
    with pytest.raises(ValueError, match="Supported archive differs"):
        validate_supported(root, report, output)
