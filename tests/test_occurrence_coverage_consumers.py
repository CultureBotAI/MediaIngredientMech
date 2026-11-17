"""#1431 producer contracts: unknown, missing and true zero stay distinct."""

import csv
import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from mediaingredientmech.occurrence_coverage import load_coverage
from tests.test_occurrence_coverage import write_bundle

ROOT = Path(__file__).resolve().parents[1]


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def fixture(tmp_path):
    root, unknown, _, bundle, _ = write_bundle(tmp_path)
    coverage = load_coverage(bundle, root)
    zero = {
        "mim_id": "MIM:0000002",
        "identifier": "cas:2-00-0",
        "preferred_term": "known zero",
        "mapping_status": "MAPPED",
        "occurrence_statistics": {"media_count": 0, "total_occurrences": 0},
    }
    missing = {
        "mim_id": "MIM:0000003",
        "identifier": "cas:3-00-0",
        "preferred_term": "undeclared missing",
        "mapping_status": "MAPPED",
    }
    return root, [unknown, zero, missing], coverage


def test_list_json_csv_roundtrip_has_provenance_and_keeps_zero(tmp_path):
    _, records, coverage = fixture(tmp_path)
    mod = module("export_lists")
    jp = tmp_path / "list.json"
    cp = tmp_path / "list.csv"
    mod.export_to_json(records, jp, coverage=coverage)
    mod.export_to_csv(records, cp, coverage=coverage)
    js = json.loads(jp.read_text())
    cs = list(csv.DictReader(cp.open()))
    assert [r["total_occurrences"] for r in js] == [None, 0, None]
    assert [r["occurrence_statistics_state"] for r in js] == ["UNKNOWN", "RECORDED", "MISSING"]
    assert [r["total_occurrences"] for r in cs] == ["", "0", ""]
    assert (
        json.loads(cs[0]["occurrence_statistics_provenance"])
        == js[0]["occurrence_statistics_provenance"]
    )
    assert cs[0]["occurrence_statistics_reason"]


def test_browser_keeps_unknown_and_separate_missing(tmp_path):
    _, records, coverage = fixture(tmp_path)
    mod = module("browser_export")
    rows = [
        mod.extract_ingredient_for_browser(r, f"mapped/{i}.yaml", coverage=coverage)
        for i, r in enumerate(records)
    ]
    assert [r["media_count"] for r in rows] == [None, 0, None]
    assert [r["occurrence_statistics_state"] for r in rows] == ["UNKNOWN", "RECORDED", "MISSING"]
    assert rows[0]["occurrence_statistics_provenance"]["coverage_sha256"] == coverage.sha256


def test_curated_indexes_subtotal_is_not_exhaustive(tmp_path):
    _, records, coverage = fixture(tmp_path)
    mod = module("generate_index_files")
    jp = tmp_path / "index.json"
    cp = tmp_path / "index.csv"
    md = tmp_path / "index.md"
    mod.generate_json_index(records, jp, coverage=coverage)
    mod.generate_csv_index(records, cp, coverage=coverage)
    mod.generate_markdown_index(records, md, "fixture", coverage=coverage)
    assert [r["occurrences"] for r in json.loads(jp.read_text())] == [None, 0, None]
    assert [r["occurrences"] for r in csv.DictReader(cp.open())] == ["", "0", ""]
    assert "Known-count occurrence subtotal" in md.read_text()
    assert "owners without known counts**: 2" in md.read_text()
    assert "**Total Occurrences**" not in md.read_text()
    assert "Unknown" in md.read_text()


def test_visualization_currency_requires_state_and_null(tmp_path):
    _, records, coverage = fixture(tmp_path)
    mod = module("check_visualization_currency")
    rows = [mod.visualization_metadata(r, "mapped", r["mim_id"], coverage) for r in records]
    assert [r["total_occurrences"] for r in rows] == [None, 0, None]
    live = {records[0]["mim_id"]: rows[0]}
    bad = {"id": records[0]["mim_id"], **rows[0], "total_occurrences": 0}
    assert mod.audit_entries([bad], live)["metadata_mismatches"]
    good = {"id": records[0]["mim_id"], **rows[0]}
    assert not any(mod.audit_entries([good], live).values())


def test_role_ranking_never_promotes_unknown_to_zero(tmp_path):
    _, records, coverage = fixture(tmp_path)
    # The bound unknown owner remains byte-identical; role info was not in its
    # declaration, so use a standalone missing fixture for this ranking test.
    rows = [
        dict(r, nutritional_roles=[{"role": "carbon_source", "confidence": 1.0}]) for r in records
    ]
    mod = module("generate_role_statistics")
    stats = mod.analyze_ingredients(SimpleNamespace(records=rows))
    assert stats["owners_without_known_counts"] == 2
    assert stats["top_ingredients"][0]["preferred_term"] == "known zero"
    assert [r["occurrence_count"] for r in stats["top_ingredients"]] == [0, None, None]
    mod.generate_report(stats, tmp_path / "roles.yaml")
    import yaml

    report = yaml.safe_load((tmp_path / "roles.yaml").read_text())
    assert report["summary"]["role_owners_without_known_occurrence_counts"] == 2
    mod.print_summary(report)  # nullable formatting must not crash


def test_audit_requires_explicit_binding_not_blanket_exemption(tmp_path):
    _, records, coverage = fixture(tmp_path)
    audit = module("audit_occurrence_stats")
    issues = audit.find_issues(records, coverage)
    assert issues["missing"] == [(records[2]["identifier"], records[2]["preferred_term"])]
    assert sum(map(len, issues.values())) == 1
    assert len(audit.find_issues(records)["missing"]) == 2
    assert audit.find_issues(
        [{"occurrence_statistics": {"media_count": True, "total_occurrences": 1}}]
    )["invalid_type"]
    assert audit.find_issues(
        [{"occurrence_statistics": {"media_count": 0, "total_occurrences": -1}}]
    )["negative"]
    assert audit.find_issues(
        [{"occurrence_statistics": {"media_count": 2, "total_occurrences": 1}}]
    )["media_gt_occ"]
    assert audit.find_issues(
        [
            {
                "mapping_status": "REJECTED",
                "occurrence_statistics": {"media_count": 1, "total_occurrences": 1},
            }
        ]
    )["rejected_nonzero"]


def test_actual_visualization_producer_matches_coverage_currency(tmp_path):
    import pandas as pd

    root, records, _ = fixture(tmp_path)
    mod = module("generate_ingredient_umap")
    df = pd.DataFrame([{"ingredient_id": records[0]["mim_id"], "umap_x": 0.0, "umap_y": 1.0}])
    nodes = mod.build_visualization_data(df, root)
    assert len(nodes) == 1
    assert nodes[0]["total_occurrences"] is None
    assert nodes[0]["occurrence_statistics_state"] == "UNKNOWN"
    currency = module("check_visualization_currency")
    assert not any(currency.audit_entries(nodes, currency.live_records(root)).values())


def test_invalid_counts_do_not_silently_drop_visualization_owner(tmp_path):
    import pandas as pd
    import yaml

    root = tmp_path / "data" / "ingredients"
    (root / "mapped").mkdir(parents=True)
    record = {
        "mim_id": "MIM:0000001",
        "identifier": "CHEBI:1",
        "preferred_term": "X",
        "mapping_status": "MAPPED",
        "occurrence_statistics": {"total_occurrences": 1},
    }
    (root / "mapped" / "bad.yaml").write_text(yaml.safe_dump(record))
    df = pd.DataFrame([{"ingredient_id": record["mim_id"], "umap_x": 0.0, "umap_y": 1.0}])
    with pytest.raises(ValueError):
        module("generate_ingredient_umap").build_visualization_data(df, root)


def test_audit_cli_accepts_only_explicit_validated_unknown(tmp_path):
    import subprocess
    import sys

    import yaml

    root, record, _, bundle, _ = write_bundle(tmp_path)
    curated = tmp_path / "data" / "curated"
    curated.mkdir()
    (curated / "mapped_ingredients.yaml").write_text(yaml.safe_dump({"ingredients": [record]}))
    argv = [sys.executable, str(ROOT / "scripts" / "audit_occurrence_stats.py")]
    approved = subprocess.run(argv, cwd=tmp_path, capture_output=True, text=True, timeout=30)
    assert approved.returncode == 0, approved.stdout + approved.stderr
    assert "missing: 0" in approved.stdout
    bundle.unlink()
    undeclared = subprocess.run(argv, cwd=tmp_path, capture_output=True, text=True, timeout=30)
    assert undeclared.returncode == 1, undeclared.stdout + undeclared.stderr
    assert "missing: 1" in undeclared.stdout
