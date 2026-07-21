"""Regression guard: exporting collections must not wipe per-record-authored fields.

`discussions` is written into per-record files by culturebotai-claw's kgscan
tool and is never carried in the curated collection. Because the exporter
projects the collection onto the per-record tree (clearing files first), a naive
projection silently deleted every discussion on each `just export-individual`.
These tests pin the preserve-and-merge behaviour that fixes that.
"""

import importlib.util
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "src"))


def _load_exporter():
    spec = importlib.util.spec_from_file_location(
        "export_individual_records", ROOT / "scripts" / "export_individual_records.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _write_collection(path: Path, records: list[dict]) -> None:
    path.write_text(
        yaml.safe_dump(
            {
                "generation_date": "2026-07-21T00:00:00+00:00",
                "total_count": len(records),
                "mapped_count": sum(1 for r in records if r.get("mapping_status") == "MAPPED"),
                "unmapped_count": sum(1 for r in records if r.get("mapping_status") != "MAPPED"),
                "ingredients": records,
            },
            sort_keys=False,
        )
    )


def _discussion(did: str) -> list[dict]:
    return [{"discussion_id": did, "kind": "KNOWLEDGE_GAP", "status": "OPEN"}]


def test_collect_preserved_fields_indexes_by_identifier(tmp_path):
    exp = _load_exporter()
    root = tmp_path / "ingredients"
    (root / "mapped").mkdir(parents=True)
    (root / "mapped" / "A.yaml").write_text(
        yaml.safe_dump({"identifier": "CHEBI:1", "preferred_term": "a",
                        "mapping_status": "MAPPED", "discussions": _discussion("kgscan-a")})
    )
    (root / "mapped" / "B.yaml").write_text(
        yaml.safe_dump({"identifier": "CHEBI:2", "preferred_term": "b",
                        "mapping_status": "MAPPED"})  # no discussions
    )
    idx = exp.collect_preserved_fields(root)
    assert set(idx) == {"CHEBI:1"}
    assert idx["CHEBI:1"]["discussions"] == _discussion("kgscan-a")


def test_export_reattaches_discussions_absent_from_collection(tmp_path):
    """The end-to-end case: the collection lacks discussions, the old per-record
    file has them, and export must not drop them."""
    exp = _load_exporter()
    curated = tmp_path / "curated"
    curated.mkdir()
    ingredients = tmp_path / "ingredients"
    (ingredients / "mapped").mkdir(parents=True)

    # Pre-existing per-record file carrying a discussion.
    (ingredients / "mapped" / "Glucose.yaml").write_text(
        yaml.safe_dump({"identifier": "CHEBI:17234", "preferred_term": "glucose",
                        "mapping_status": "MAPPED", "discussions": _discussion("kgscan-glu")})
    )
    # Collection copy of the same record has NO discussions.
    _write_collection(
        curated / "mapped_ingredients.yaml",
        [{"identifier": "CHEBI:17234", "preferred_term": "glucose", "mapping_status": "MAPPED"}],
    )

    preserved = exp.collect_preserved_fields(ingredients)
    exp.export_collection_to_individual_files(
        curated / "mapped_ingredients.yaml",
        ingredients / "mapped",
        preserved=preserved,
    )

    out = yaml.safe_load((ingredients / "mapped" / "Glucose.yaml").read_text())
    assert out["discussions"] == _discussion("kgscan-glu"), "export wiped the discussion"


def test_export_does_not_resurrect_a_removed_discussion(tmp_path):
    """Preservation is rebuilt from current disk each run, so removing a
    discussion from the per-record file (and re-indexing) makes it stay gone."""
    exp = _load_exporter()
    curated = tmp_path / "curated"
    curated.mkdir()
    ingredients = tmp_path / "ingredients"
    (ingredients / "mapped").mkdir(parents=True)

    # The per-record file has already had its discussion removed.
    (ingredients / "mapped" / "Glucose.yaml").write_text(
        yaml.safe_dump({"identifier": "CHEBI:17234", "preferred_term": "glucose",
                        "mapping_status": "MAPPED"})
    )
    _write_collection(
        curated / "mapped_ingredients.yaml",
        [{"identifier": "CHEBI:17234", "preferred_term": "glucose", "mapping_status": "MAPPED"}],
    )

    preserved = exp.collect_preserved_fields(ingredients)
    exp.export_collection_to_individual_files(
        curated / "mapped_ingredients.yaml",
        ingredients / "mapped",
        preserved=preserved,
    )

    out = yaml.safe_load((ingredients / "mapped" / "Glucose.yaml").read_text())
    assert "discussions" not in out


def test_collection_discussions_win_over_stale_per_record(tmp_path):
    """If the collection ever does carry discussions, they take precedence —
    preservation only fills gaps."""
    exp = _load_exporter()
    curated = tmp_path / "curated"
    curated.mkdir()
    ingredients = tmp_path / "ingredients"
    (ingredients / "mapped").mkdir(parents=True)

    (ingredients / "mapped" / "Glucose.yaml").write_text(
        yaml.safe_dump({"identifier": "CHEBI:17234", "preferred_term": "glucose",
                        "mapping_status": "MAPPED", "discussions": _discussion("stale")})
    )
    _write_collection(
        curated / "mapped_ingredients.yaml",
        [{"identifier": "CHEBI:17234", "preferred_term": "glucose",
          "mapping_status": "MAPPED", "discussions": _discussion("fresh")}],
    )

    preserved = exp.collect_preserved_fields(ingredients)
    exp.export_collection_to_individual_files(
        curated / "mapped_ingredients.yaml",
        ingredients / "mapped",
        preserved=preserved,
    )

    out = yaml.safe_load((ingredients / "mapped" / "Glucose.yaml").read_text())
    assert out["discussions"] == _discussion("fresh")
