"""Current YAML, not common text alone, must authorize graph publication (#684)."""

from __future__ import annotations

import copy
import gzip
import json
import os
import shutil
import subprocess
import sys
from fnmatch import fnmatchcase
from pathlib import Path

import pytest
import yaml

from mediaingredientmech import graph_embedding_receipts as receipts
from mediaingredientmech.text_map_inputs import iter_inputs
from scripts.check_graph_receipts import check_graph_receipts

REPO = Path(__file__).resolve().parents[1]
CHECKER = REPO / "scripts" / "check_graph_receipts.py"


@pytest.fixture
def graph_site(tmp_path):
    corpus = tmp_path / "data" / "ingredients"
    for category in ("mapped", "unmapped"):
        (corpus / category).mkdir(parents=True)
    for stem, status, node in (
        ("first", "UNMAPPED", "mediadive.ingredient:1"),
        ("second", "UNMAPPED", "mediadive.ingredient:2"),
        ("missing", "UNMAPPED", "mediadive.ingredient:missing"),
        ("rejected", "REJECTED", "mediadive.ingredient:rejected"),
    ):
        (corpus / "unmapped" / (stem + ".yaml")).write_text(
            yaml.safe_dump(
                {
                    "identifier": "UNMAPPED_" + stem,
                    "preferred_term": stem,
                    "ingredient_type": "SINGLE_INGREDIENT",
                    "mapping_status": status,
                    "notes": "Imported source " + node,
                }
            )
        )
    raw = tmp_path / "fixture.tsv.gz"
    raw.write_bytes(
        gzip.compress(b"node\td1\td2\nmediadive.ingredient:1\t1\t0\nmediadive.ingredient:2\t0\t1\n")
    )
    reader = receipts.GraphSource(raw, ["mediadive.ingredient"])
    vectors = dict(reader)
    ledger = [
        {
            "identifier": "MIM:" + stem,
            "source_nodes": ["mediadive.ingredient:" + str(index)],
            "status": "projected",
            "match_method": "history_reference",
            "source_path": "unmapped/" + stem + ".yaml",
        }
        for index, stem in enumerate(("first", "second"), 1)
    ]
    ledger.append(
        {
            "identifier": "MIM:missing",
            "source_nodes": [],
            "status": "missing_vector",
            "match_method": "no_match",
            "source_path": "unmapped/missing.yaml",
        }
    )
    points = [
        {
            "id": row["identifier"],
            "umap_x": index,
            "umap_y": -index,
            "embedding_method": row["match_method"],
            "embedding_source_node": row["source_nodes"][0],
        }
        for index, row in enumerate(ledger[:2])
    ]
    coverage = {
        "eligible": 3,
        "projected": 2,
        "eligible_records": 3,
        "embedded_records": 2,
        "missing_records": ["MIM:missing"],
        "omitted": 1,
        "synthetic_records": 0,
        "rejected_records": ["unmapped/rejected.yaml"],
    }
    for basename, method in (("ingredient_umap", "pacmap"), ("ingredient_graph", "sfdp")):
        projection = {
            "method": method,
            "implementation": "pacmap.PaCMAP" if method == "pacmap" else "graphviz.sfdp",
            "normalization": "none",
            "parameters": {},
            "library_versions": {"fixture": "1"},
        }
        if method == "pacmap":
            projection["effective_pairs"] = {"neighbors": 1, "mid_near": 0, "further": 1}
        else:
            projection["graph"] = {
                "construction": "symmetric_union_knn",
                "dot_sha256": "a" * 64,
                "graphviz_version": "fixture",
                "arguments": ["-Tplain"],
                "effective_k": 1,
                "edges": 1,
            }
        metadata = receipts.make_receipt(
            source=reader.receipt,
            corpus=receipts.corpus_receipt(corpus.glob("*/*.yaml"), corpus),
            ledger=copy.deepcopy(ledger),
            matrix=receipts.matrix_receipt(list(vectors.values()), [row["id"] for row in points]),
            projection=projection,
            coverage=copy.deepcopy(coverage),
        )
        target = tmp_path / "docs" / "data" / (basename + ".json")
        target.parent.mkdir(parents=True, exist_ok=True)
        staged = tmp_path / (basename + ".json")
        staged.write_text(json.dumps(points))
        receipts.publish_artifacts({target: staged}, target.with_suffix(".metadata.json"), metadata)
    (tmp_path / "conf").mkdir()
    (tmp_path / "conf" / "text_map.yaml").write_text("enabled: false\n")
    return tmp_path


def cli(root):
    return subprocess.run(
        [sys.executable, "-S", str(CHECKER), "--root", str(root)], capture_output=True, text=True
    )


def site_bytes(root):
    return {
        str(path.relative_to(root)): path.read_bytes()
        for path in (root / "docs").rglob("*")
        if path.is_file()
    }


def test_complete_both_graphs_pass_without_site_packages_or_source_vectors(graph_site):
    (graph_site / "fixture.tsv.gz").unlink()
    before = site_bytes(graph_site)
    result = cli(graph_site)
    assert result.returncode == 0, result.stderr
    checked = json.loads(result.stdout)["verified_graphs"]
    assert len(checked) == 2
    assert [row["points"] for row in checked] == [2, 2]
    assert [row["corpus_count"] for row in checked] == [4, 4]
    assert site_bytes(graph_site) == before


def test_graph_notes_change_with_identical_complete_common_inputs_is_refused(graph_site):
    before = list(iter_inputs(graph_site))
    source = graph_site / "data/ingredients/unmapped/first.yaml"
    source.write_text(
        source.read_text().replace("mediadive.ingredient:1", "mediadive.ingredient:2")
    )
    assert list(iter_inputs(graph_site)) == before
    previous_site = site_bytes(graph_site)
    result = cli(graph_site)
    assert result.returncode == 1
    assert "graph corpus changed" in result.stderr
    assert site_bytes(graph_site) == previous_site


@pytest.mark.parametrize("change", ["ignored_addition", "removed", "rejected_changed"])
def test_complete_corpus_includes_ignored_and_rejected_files(graph_site, change):
    corpus = graph_site / "data/ingredients/unmapped"
    if change == "ignored_addition":
        (graph_site / ".gitignore").write_text("data/ingredients/unmapped/new.yaml\n")
        (corpus / "new.yaml").write_text((corpus / "first.yaml").read_text())
    elif change == "removed":
        (corpus / "missing.yaml").unlink()
    else:
        with (corpus / "rejected.yaml").open("a") as stream:
            stream.write("# source correction\n")
    with pytest.raises(ValueError, match="graph corpus changed"):
        check_graph_receipts(graph_site)


@pytest.mark.parametrize("basename", ["ingredient_umap", "ingredient_graph"])
@pytest.mark.parametrize(
    "change",
    ["missing_receipt", "tampered", "wrong_output", "reordered", "boolean", "lookup", "coverage"],
)
def test_both_graph_outputs_and_semantics_are_bound(graph_site, basename, change):
    output = graph_site / "docs/data" / (basename + ".json")
    metadata = output.with_suffix(".metadata.json")
    receipt = json.loads(metadata.read_text())
    points = json.loads(output.read_text())
    if change == "missing_receipt":
        metadata.unlink()
    elif change == "tampered":
        output.write_text(output.read_text() + " ")
    elif change == "wrong_output":
        other = output.with_name("wrong.json")
        other.write_bytes(output.read_bytes())
        receipt["outputs"] = {other.name: receipts.file_sha256(other)}
        metadata.write_text(json.dumps(receipt))
    else:
        if change == "reordered":
            points.reverse()
        elif change == "boolean":
            points[0]["umap_x"] = True
        elif change == "lookup":
            points[0]["embedding_source_node"] = "mediadive.ingredient:wrong"
        else:
            receipt["coverage"]["rejected_records"] = []
        output.write_text(json.dumps(points))
        receipt["outputs"][output.name] = receipts.file_sha256(output)
        metadata.write_text(json.dumps(receipt))
    previous = site_bytes(graph_site)
    result = cli(graph_site)
    assert result.returncode == 1, result.stdout
    assert "graph publication refused" in result.stderr
    assert site_bytes(graph_site) == previous


def test_deployment_gate_and_required_paths_are_before_site_writes():
    workflow = yaml.safe_load((REPO / ".github/workflows/generate-pages.yaml").read_text())
    triggers = workflow.get("on", workflow.get(True))["push"]["paths"]
    for changed in (
        "data/ingredients/unmapped/changed.yaml",
        "data/ingredients/mapped/changed.yaml",
        "scripts/check_graph_receipts.py",
        "src/mediaingredientmech/graph_embedding_receipts.py",
        "docs/data/ingredient_graph.metadata.json",
    ):
        assert any(fnmatchcase(changed, pattern) for pattern in triggers), changed
    steps = workflow["jobs"]["deploy"]["steps"]
    gate = next(
        i
        for i, step in enumerate(steps)
        if step.get("run", "").strip() == "python scripts/check_graph_receipts.py"
    )
    for i, step in enumerate(steps):
        if "stage_text_map.py" in step.get("run", "") or "upload-pages-artifact" in step.get(
            "uses", ""
        ):
            assert gate < i


@pytest.mark.skipif(shutil.which("just") is None, reason="actual just is required")
@pytest.mark.parametrize("recipe", ["build-docs", "check-visualizations"])
def test_actual_local_recipes_refuse_stale_graph_before_other_commands(
    graph_site, tmp_path, recipe
):
    source = graph_site / "data/ingredients/unmapped/first.yaml"
    source.write_text(
        source.read_text().replace("mediadive.ingredient:1", "mediadive.ingredient:2")
    )
    command_log = tmp_path / "commands.jsonl"
    binary = tmp_path / "bin"
    binary.mkdir()
    uv = binary / "uv"
    uv.write_text(
        f"#!{sys.executable}\nimport json, subprocess, sys\n"
        f"with open({str(command_log)!r}, 'a') as stream: stream.write(json.dumps(sys.argv[1:])+'\\n')\n"
        "if sys.argv[1:] == ['run', 'python', 'scripts/check_graph_receipts.py']:\n"
        f"    raise SystemExit(subprocess.call([{sys.executable!r}, '-S', {str(CHECKER)!r}, '--root', {str(graph_site)!r}]))\n"
        "raise SystemExit('unexpected publication command before graph gate')\n"
    )
    uv.chmod(0o755)
    before = site_bytes(graph_site)
    result = subprocess.run(
        [shutil.which("just"), "--justfile", str(REPO / "justfile"), recipe],
        cwd=REPO,
        env={**os.environ, "PATH": str(binary) + os.pathsep + os.environ["PATH"]},
        text=True,
        capture_output=True,
    )
    assert result.returncode != 0
    assert "graph corpus changed" in result.stderr
    assert [json.loads(line) for line in command_log.read_text().splitlines()] == [
        ["run", "python", "scripts/check_graph_receipts.py"]
    ]
    assert site_bytes(graph_site) == before
