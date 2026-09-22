"""The supported release is an exact reviewed subset with a lossless separate backlog."""

import csv
import hashlib
import importlib.util
import json
import tarfile
from pathlib import Path

import pytest
import yaml

from mediaingredientmech.export.kgx import export_graph
from mediaingredientmech.export.supported_kgx import export_supported, validate_supported
from mediaingredientmech.validation.semantic_release import current_assertions, rows


def _hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


@pytest.fixture
def full_failed_review(tmp_path):
    # Reuse the complete full-gate fixture, then add one genuinely unapproved claim.
    spec = importlib.util.spec_from_file_location(
        "semantic_release_fixture", Path(__file__).with_name("test_semantic_release.py")
    )
    fixture_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fixture_module)
    root, report_path = fixture_module.reviewed_bundle.__wrapped__(tmp_path)
    record_path = root / "data/ingredients/mapped/Water.yaml"
    record = yaml.safe_load(record_path.read_text())
    record["nutritional_roles"] = [
        {
            "role": "CARBON_SOURCE",
            "evidence": [
                {
                    "reference_type": "COMPUTATIONAL_PREDICTION",
                    "reference_text": "Unsupported test prediction",
                }
            ],
        }
    ]
    record_path.write_text(yaml.safe_dump(record))
    (root / "data/curated/mapped_ingredients.yaml").write_text(
        yaml.safe_dump({"ingredients": [record]})
    )
    export_graph(root, root / "full")
    report = json.loads(report_path.read_text())
    report["bundle"] = "full"
    report["record_inputs"] = {name: _hash(root / name) for name in report["record_inputs"]}
    with (root / "mappings/ingredient_mappings.sssom.tsv").open() as stream:
        mappings = list(
            csv.DictReader((line for line in stream if not line.startswith("#")), delimiter="\t")
        )
    records = {name: yaml.safe_load((root / name).read_text()) for name in report["record_inputs"]}
    current = current_assertions(
        records,
        mappings,
        report["record_inputs"],
        _hash(root / "mappings/ingredient_mappings.sssom.tsv"),
    )
    decisions = [
        {
            **identity,
            "resolution_status": "APPROVED" if identity["assertion_type"] == "mapping" else "OPEN",
            "review_reason": (
                "Synthetic approved mapping"
                if identity["assertion_type"] == "mapping"
                else "Prediction lacks support"
            ),
            "review_evidence": "evidence.md",
        }
        for identity in current
    ]
    with (root / "assertions.tsv").open("w") as stream:
        writer = csv.DictWriter(
            stream, fieldnames=list(decisions[0]), delimiter="\t", lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(decisions)
    report["inputs"].pop("bundle/manifest.json")
    report["inputs"]["full/manifest.json"] = _hash(root / "full/manifest.json")
    report["inputs"]["assertions.tsv"] = _hash(root / "assertions.tsv")
    report["blocking_assertion_ids"] = sorted(
        row["assertion_id"] for row in decisions if row["resolution_status"] == "OPEN"
    )
    report["evidence_gaps"] = {"prediction_only_roles": 1}
    report["release_verdict"] = "FAIL"
    report_path.write_text(json.dumps(report))
    return root, report_path


def test_supported_subset_keeps_full_failure_and_backlog(full_failed_review):
    root, report = full_failed_review
    output = root / "supported"
    manifest = export_supported(root, report, output)
    assert manifest["release_verdict"] == "PASS"
    assert manifest["full_release_verdict"] == "FAIL"
    assert manifest["counts"] == {
        "nodes": 3,
        "edges": 1,
        "sssom_rows": 1,
        "active_ingredient_record_nodes": 2,
        "full_nodes": 4,
        "full_edges": 2,
        "backlog_raw_nodes": 4,
        "backlog_unapproved_edges": 1,
    }
    edges = rows(output / "mim_edges.tsv", kgx=True)
    assert edges[0]["assertion_type"] == "mapping"
    text = (output / "ingredient_mappings.sssom.tsv").read_text()
    metadata = yaml.safe_load(
        "\n".join(line[1:] for line in text.splitlines() if line.startswith("#"))
    )
    assert metadata["mapping_set_id"].endswith("/supported")
    mappings = list(
        csv.DictReader(
            (line for line in text.splitlines() if not line.startswith("#")), delimiter="\t"
        )
    )
    assert mappings == [json.loads(edges[0]["assertion_json"])]
    nodes = rows(output / "mim_nodes.tsv", kgx=True)
    assert all(node["category"] == "biolink:NamedThing" for node in nodes)
    for node in nodes:
        assert all(
            not node[field]
            for field in (
                "record_identifier",
                "mapping_status",
                "ingredient_type",
                "record_json",
                "review_json",
                "definition_json",
            )
        )
    backlog = json.loads((output / "unsupported-backlog.json").read_text())
    assert backlog["assertions"][0]["edge"]["assertion_type"] == "nutritional_roles"
    raw = next(node for node in backlog["nodes"] if node["id"] == "MIM:water")
    assert "Unsupported test prediction" in raw["record_json"]
    with tarfile.open(output / "mim-kgx.tar.gz") as archive:
        assert archive.getnames() == ["manifest.json", "mim_nodes.tsv", "mim_edges.tsv"]
        assert b"Unsupported test prediction" not in archive.extractfile("mim_nodes.tsv").read()
    assert validate_supported(root, report, output)["semantic_release"] == "PASS"


def test_supported_archive_is_reproducible(full_failed_review):
    root, report = full_failed_review
    export_supported(root, report, root / "first")
    export_supported(root, report, root / "second")
    assert (root / "first/mim-kgx.tar.gz").read_bytes() == (
        root / "second/mim-kgx.tar.gz"
    ).read_bytes()


@pytest.mark.parametrize(
    "mutation", ["include_unapproved", "omit_approved", "raw_node_leak", "omit_backlog", "archive"]
)
def test_selection_leak_and_backlog_tampering_are_rejected(full_failed_review, mutation):
    root, report = full_failed_review
    output = root / "supported"
    export_supported(root, report, output)
    if mutation == "include_unapproved":
        (output / "mim_edges.tsv").write_bytes((root / "full/mim_edges.tsv").read_bytes())
    elif mutation == "omit_approved":
        path = output / "mim_edges.tsv"
        path.write_text(path.read_text().splitlines()[0] + "\n")
    elif mutation == "raw_node_leak":
        (output / "mim_nodes.tsv").write_bytes((root / "full/mim_nodes.tsv").read_bytes())
    elif mutation == "omit_backlog":
        path = output / "unsupported-backlog.json"
        data = json.loads(path.read_text())
        data["assertions"] = []
        path.write_text(json.dumps(data))
    else:
        (output / "mim-kgx.tar.gz").write_bytes((root / "full/mim-kgx.tar.gz").read_bytes())
    with pytest.raises(ValueError, match="Supported"):
        validate_supported(root, report, output)


def test_stale_full_report_inputs_block_subset_release(full_failed_review):
    root, report = full_failed_review
    output = root / "supported"
    export_supported(root, report, output)
    (root / "evidence.md").write_text("Altered review evidence")
    with pytest.raises(ValueError, match="Stale review input"):
        validate_supported(root, report, output)


def test_approved_label_cannot_override_known_prediction_gap(full_failed_review):
    root, report_path = full_failed_review
    decisions = rows(root / "assertions.tsv")
    for row in decisions:
        row["resolution_status"] = "APPROVED"
    with (root / "assertions.tsv").open("w") as stream:
        writer = csv.DictWriter(
            stream, fieldnames=list(decisions[0]), delimiter="\t", lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(decisions)
    report = json.loads(report_path.read_text())
    report["inputs"]["assertions.tsv"] = _hash(root / "assertions.tsv")
    report["blocking_assertion_ids"] = []
    report_path.write_text(json.dumps(report))
    with pytest.raises(ValueError, match="unsupported role"):
        export_supported(root, report_path, root / "unsupported")
