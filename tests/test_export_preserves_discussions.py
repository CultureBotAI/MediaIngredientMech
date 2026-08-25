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

import pytest
import yaml

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "src"))


def _load_exporter():
    spec = importlib.util.spec_from_file_location(
        "export_individual_records", ROOT / "scripts" / "export_individual_records.py"
    )
    mod = importlib.util.module_from_spec(spec)
    # Register before exec: a @dataclass under `from __future__ import annotations`
    # resolves its module via sys.modules during class creation, which is absent
    # for a spec_from_file_location load unless we register it here.
    sys.modules[spec.name] = mod
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
        yaml.safe_dump(
            {
                "identifier": "CHEBI:1",
                "preferred_term": "a",
                "mapping_status": "MAPPED",
                "discussions": _discussion("kgscan-a"),
            }
        )
    )
    (root / "mapped" / "B.yaml").write_text(
        yaml.safe_dump(
            {"identifier": "CHEBI:2", "preferred_term": "b", "mapping_status": "MAPPED"}
        )  # no discussions
    )
    idx = exp.collect_preserved_fields(root)
    assert set(idx.by_identifier) == {"CHEBI:1"}
    assert idx.by_identifier["CHEBI:1"]["discussions"] == _discussion("kgscan-a")
    # Indexed by preferred_term too, for identifier-changing moves.
    assert idx.by_preferred_term["a"]["discussions"] == _discussion("kgscan-a")


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
        yaml.safe_dump(
            {
                "identifier": "CHEBI:17234",
                "preferred_term": "glucose",
                "mapping_status": "MAPPED",
                "discussions": _discussion("kgscan-glu"),
            }
        )
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
        yaml.safe_dump(
            {"identifier": "CHEBI:17234", "preferred_term": "glucose", "mapping_status": "MAPPED"}
        )
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
        yaml.safe_dump(
            {
                "identifier": "CHEBI:17234",
                "preferred_term": "glucose",
                "mapping_status": "MAPPED",
                "discussions": _discussion("stale"),
            }
        )
    )
    _write_collection(
        curated / "mapped_ingredients.yaml",
        [
            {
                "identifier": "CHEBI:17234",
                "preferred_term": "glucose",
                "mapping_status": "MAPPED",
                "discussions": _discussion("fresh"),
            }
        ],
    )

    preserved = exp.collect_preserved_fields(ingredients)
    exp.export_collection_to_individual_files(
        curated / "mapped_ingredients.yaml",
        ingredients / "mapped",
        preserved=preserved,
    )

    out = yaml.safe_load((ingredients / "mapped" / "Glucose.yaml").read_text())
    assert out["discussions"] == _discussion("fresh")


def test_export_preserves_discussions_across_identifier_change_on_promotion(tmp_path):
    """The move the identifier key alone misses: promotion changes semantic identity.

    The old per-record file is UNMAPPED_0001 in unmapped/; the collection has
    promoted it to CHEBI:17234 in mapped/. Identifier-keyed lookup misses (old id
    != new id), so preservation must fall back to the stable preferred_term.
    """
    exp = _load_exporter()
    curated = tmp_path / "curated"
    curated.mkdir()
    ingredients = tmp_path / "ingredients"
    (ingredients / "unmapped").mkdir(parents=True)
    (ingredients / "mapped").mkdir()

    (ingredients / "unmapped" / "Glucose.yaml").write_text(
        yaml.safe_dump(
            {
                "identifier": "UNMAPPED_0001",
                "preferred_term": "glucose",
                "mapping_status": "UNMAPPED",
                "discussions": _discussion("kgscan-glu"),
            }
        )
    )
    _write_collection(
        curated / "mapped_ingredients.yaml",
        [{"identifier": "CHEBI:17234", "preferred_term": "glucose", "mapping_status": "MAPPED"}],
    )
    _write_collection(curated / "unmapped_ingredients.yaml", [])

    preserved = exp.collect_preserved_fields(ingredients)
    exp.export_collection_to_individual_files(
        curated / "mapped_ingredients.yaml", ingredients / "mapped", preserved=preserved
    )

    out = yaml.safe_load((ingredients / "mapped" / "Glucose.yaml").read_text())
    assert out["discussions"] == _discussion("kgscan-glu"), "promotion lost the discussion"


def test_preferred_term_collision_is_not_indexed(tmp_path):
    """Two authored records sharing a preferred_term must not attribute to either."""
    exp = _load_exporter()
    root = tmp_path / "ingredients"
    (root / "mapped").mkdir(parents=True)
    (root / "mapped" / "A.yaml").write_text(
        yaml.safe_dump(
            {
                "identifier": "CHEBI:1",
                "preferred_term": "dup",
                "mapping_status": "MAPPED",
                "discussions": _discussion("kgscan-a"),
            }
        )
    )
    (root / "mapped" / "B.yaml").write_text(
        yaml.safe_dump(
            {
                "identifier": "CHEBI:2",
                "preferred_term": "dup",
                "mapping_status": "MAPPED",
                "discussions": _discussion("kgscan-b"),
            }
        )
    )
    idx = exp.collect_preserved_fields(root)
    # Both still resolvable by their (unique) identifiers...
    assert set(idx.by_identifier) == {"CHEBI:1", "CHEBI:2"}
    # ...but the ambiguous term is dropped, so a promotion of either does not
    # silently graft the wrong record's discussion.
    assert "dup" not in idx.by_preferred_term


def test_shared_identifier_is_not_used_to_move_authored_fields_between_siblings(tmp_path):
    """A semantic identifier shared by two forms cannot address either record."""
    exp = _load_exporter()
    root = tmp_path / "ingredients"
    (root / "mapped").mkdir(parents=True)
    (root / "mapped" / "Anhydrous.yaml").write_text(
        yaml.safe_dump(
            {
                "identifier": "CHEBI:1",
                "preferred_term": "salt",
                "mapping_status": "MAPPED",
                "discussions": _discussion("dry"),
            }
        )
    )
    (root / "mapped" / "Hydrate.yaml").write_text(
        yaml.safe_dump(
            {
                "identifier": "CHEBI:1",
                "preferred_term": "salt hydrate",
                "mapping_status": "MAPPED",
                "discussions": _discussion("wet"),
            }
        )
    )

    idx = exp.collect_preserved_fields(root)

    assert "CHEBI:1" not in idx.by_identifier
    assert idx.for_record({"identifier": "CHEBI:1", "preferred_term": "salt"})[
        "discussions"
    ] == _discussion("dry")
    assert idx.for_record({"identifier": "CHEBI:1", "preferred_term": "salt hydrate"})[
        "discussions"
    ] == _discussion("wet")


def test_incoming_remap_cannot_graft_discussion_by_newly_shared_identifier(tmp_path):
    """Incoming ambiguity overrides an identifier that was unique on old disk."""
    exp = _load_exporter()
    ingredients = tmp_path / "ingredients"
    mapped = ingredients / "mapped"
    mapped.mkdir(parents=True)
    (mapped / "A.yaml").write_text(
        yaml.safe_dump(
            {
                "identifier": "CHEBI:1",
                "preferred_term": "a",
                "mapping_status": "MAPPED",
                "discussions": _discussion("from-a"),
            }
        )
    )
    (mapped / "B.yaml").write_text(
        yaml.safe_dump(
            {
                "identifier": "CHEBI:2",
                "preferred_term": "b",
                "mapping_status": "MAPPED",
                "discussions": _discussion("from-b"),
            }
        )
    )
    collection = tmp_path / "mapped_ingredients.yaml"
    _write_collection(
        collection,
        [
            {"identifier": "CHEBI:1", "preferred_term": "a", "mapping_status": "MAPPED"},
            {"identifier": "CHEBI:1", "preferred_term": "b", "mapping_status": "MAPPED"},
        ],
    )

    preserved = exp.collect_preserved_fields(ingredients)
    existing_names = exp.collect_existing_filenames(ingredients)
    exp.export_collection_to_individual_files(
        collection,
        mapped,
        preserved=preserved,
        existing_names=existing_names,
    )

    assert yaml.safe_load((mapped / "A.yaml").read_text())["discussions"] == _discussion("from-a")
    assert yaml.safe_load((mapped / "B.yaml").read_text())["discussions"] == _discussion("from-b")


def test_unique_identifier_reassignment_fails_before_clearing_old_records(tmp_path):
    """Conflicting identifier/term continuity must not choose the wrong record.

    The incoming record keeps A's term but takes B's identifier while B is
    retired from the collection. Identifier-first lookup would otherwise write
    the record as B.yaml, graft B's discussion, and delete A.yaml.
    """
    exp = _load_exporter()
    ingredients = tmp_path / "ingredients"
    mapped = ingredients / "mapped"
    mapped.mkdir(parents=True)
    (mapped / "A.yaml").write_text(
        yaml.safe_dump(
            {
                "identifier": "CHEBI:1",
                "preferred_term": "a",
                "mapping_status": "MAPPED",
                "discussions": _discussion("authored-a"),
            }
        )
    )
    (mapped / "B.yaml").write_text(
        yaml.safe_dump(
            {
                "identifier": "CHEBI:2",
                "preferred_term": "b",
                "mapping_status": "MAPPED",
                "discussions": _discussion("authored-b"),
            }
        )
    )
    collection = tmp_path / "mapped_ingredients.yaml"
    _write_collection(
        collection,
        [{"identifier": "CHEBI:2", "preferred_term": "a", "mapping_status": "MAPPED"}],
    )

    preserved = exp.collect_preserved_fields(ingredients)
    existing_names = exp.collect_existing_filenames(ingredients)
    with pytest.raises(exp.click.ClickException, match="Refusing to clear"):
        exp.export_collection_to_individual_files(
            collection,
            mapped,
            preserved=preserved,
            existing_names=existing_names,
        )

    assert yaml.safe_load((mapped / "A.yaml").read_text())["discussions"] == _discussion(
        "authored-a"
    )
    assert yaml.safe_load((mapped / "B.yaml").read_text())["discussions"] == _discussion(
        "authored-b"
    )
