"""Guards for the flat-export coverage gate and the synonyms column (#229).

MIM's product is turning a raw ingredient string into an ontology term, and
consumers do that against `docs/data/all_ingredients.csv`. A merge deletes the
duplicate record and keeps its raw label only as a synonym, adding no SSSOM row
— so `D-lactate` resolved to UNMAPPED_0654 before PR #227 and to nothing after,
while reconcile, roundtrip and duplicate-ids all stayed green. These tests pin
both halves of the fix: the column exists, and the gate fails without it.
"""

import csv
import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).parent.parent
EXPORT = ROOT / "scripts" / "export_lists.py"
CHECK = ROOT / "scripts" / "check_flat_export_coverage.py"


def _load(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def export_lists():
    return _load(EXPORT)


def rec(identifier, term, synonyms=(), status="MAPPED"):
    return {
        "identifier": identifier, "preferred_term": term, "mapping_status": status,
        "synonyms": [{"synonym_text": s, "synonym_type": "RAW_TEXT"} for s in synonyms],
        "ontology_mapping": {"ontology_id": identifier, "ontology_label": term},
        "occurrence_statistics": {"total_occurrences": 0, "media_count": 0},
    }


def test_synonyms_excludes_the_preferred_term_and_dedupes(export_lists):
    r = rec("CHEBI:1", "Glycerol", ["Glycerol", "glycerine", "glycerine"])
    assert export_lists._synonyms(r) == ["glycerine"]


def test_synonyms_handles_records_with_no_synonyms(export_lists):
    assert export_lists._synonyms({"preferred_term": "X"}) == []
    assert export_lists._synonyms({"preferred_term": "X", "synonyms": None}) == []


def test_csv_publishes_a_merged_label(export_lists, tmp_path):
    """The #229 scenario: the raw label survives only as a synonym."""
    out = tmp_path / "all.csv"
    export_lists.export_to_csv([rec("CHEBI:16004", "(R)-lactate", ["D-lactate"])], out)
    rows = list(csv.DictReader(out.open()))
    assert "synonyms" in rows[0]
    assert rows[0]["synonyms"] == "D-lactate"
    assert rows[0]["identifier"] == "CHEBI:16004", "must resolve to the merge target"


def test_csv_synonyms_column_is_appended_last(export_lists, tmp_path):
    """Positional consumers keep working only if the column goes on the end."""
    out = tmp_path / "all.csv"
    export_lists.export_to_csv([rec("CHEBI:1", "X")], out)
    header = out.read_text().splitlines()[0].split(",")
    assert header[-1] == "synonyms"
    assert header[:9] == ["identifier", "ontology_id", "preferred_term", "mapping_status",
                          "ontology_label", "ontology_source", "mapping_quality",
                          "total_occurrences", "media_count"]


def test_json_carries_synonyms_as_a_list(export_lists, tmp_path):
    import json
    out = tmp_path / "all.json"
    export_lists.export_to_json([rec("CHEBI:16004", "(R)-lactate", ["D-lactate"])], out)
    assert json.loads(out.read_text())[0]["synonyms"] == ["D-lactate"]


def test_markdown_deliberately_has_no_synonyms_column(export_lists, tmp_path):
    """A pipe-joined list would collide with the table's own separator."""
    out = tmp_path / "all.md"
    export_lists.export_to_markdown([rec("CHEBI:1", "X", ["y"])], out, "T")
    header = [ln for ln in out.read_text().splitlines() if ln.startswith("| Identifier")][0]
    assert "Synonym" not in header


# --- the gate itself -------------------------------------------------------

def build(tmp_path, records, csv_rows, header=None):
    (tmp_path / "data" / "curated").mkdir(parents=True)
    (tmp_path / "data" / "curated" / "mapped_ingredients.yaml").write_text(
        yaml.safe_dump({"ingredients": records}))
    (tmp_path / "data" / "curated" / "unmapped_ingredients.yaml").write_text(
        yaml.safe_dump({"ingredients": []}))
    (tmp_path / "docs" / "data").mkdir(parents=True)
    cols = header or ["identifier", "preferred_term", "synonyms"]
    lines = [",".join(cols)] + [",".join(r) for r in csv_rows]
    (tmp_path / "docs" / "data" / "all_ingredients.csv").write_text("\n".join(lines) + "\n")
    (tmp_path / "scripts").mkdir(exist_ok=True)
    (tmp_path / "scripts" / CHECK.name).write_text(CHECK.read_text())
    return tmp_path


def run(tmp_path):
    return subprocess.run([sys.executable, str(tmp_path / "scripts" / CHECK.name)],
                          capture_output=True, text=True)


def test_gate_passes_when_every_label_is_published(tmp_path):
    repo = build(tmp_path, [rec("CHEBI:16004", "(R)-lactate", ["D-lactate"])],
                 [["CHEBI:16004", "(R)-lactate", "D-lactate"]])
    assert run(repo).returncode == 0


def test_gate_fails_when_a_synonym_is_unpublished(tmp_path):
    """Exactly the regression: the record is there, the merged label is not."""
    repo = build(tmp_path, [rec("CHEBI:16004", "(R)-lactate", ["D-lactate"])],
                 [["CHEBI:16004", "(R)-lactate", ""]])
    out = run(repo)
    assert out.returncode == 2
    assert "D-lactate" in out.stdout


def test_gate_fails_when_the_synonyms_column_is_missing_entirely(tmp_path):
    """The pre-#229 artifact shape must not read as success."""
    repo = build(tmp_path, [rec("CHEBI:16004", "(R)-lactate", ["D-lactate"])],
                 [["CHEBI:16004", "(R)-lactate"]],
                 header=["identifier", "preferred_term"])
    out = run(repo)
    assert out.returncode == 2
    assert "synonyms" in out.stdout


def test_gate_fails_when_the_flat_artifact_is_absent(tmp_path):
    repo = build(tmp_path, [rec("CHEBI:1", "X")], [])
    (repo / "docs" / "data" / "all_ingredients.csv").unlink()
    assert run(repo).returncode == 2
