"""Regression guard: exporting collections must not rename existing records.

The exporter clears the per-record tree and rewrites it from the collection, so
before this guard the filename was re-derived from `preferred_term` on every run.
That made the naming rule retroactive: a change to `sanitize_filename` renamed
the whole corpus, and every `MIM:<stem>` SSSOM subject derived from a filename
went with it. On a case-insensitive filesystem git reported no change at all, so
389 of 2,252 records were being silently re-cased on each `just export-individual`
(issue #147).

The committed corpus was written by more than one historical naming rule, so no
single rule reproduces it — reusing the name a record already has is the fix.
These tests pin that, plus the chemical-casing behaviour for genuinely new
records.
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
    # Register before exec: a @dataclass under `from __future__ import annotations`
    # resolves its module via sys.modules during class creation.
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def _write_collection(path: Path, records: list[dict]) -> None:
    path.write_text(
        yaml.safe_dump(
            {
                "generation_date": "2026-07-30T00:00:00+00:00",
                "total_count": len(records),
                "ingredients": records,
            },
            sort_keys=False,
        )
    )


def _record(identifier: str, term: str, **extra) -> dict:
    return {"identifier": identifier, "preferred_term": term, **extra}


# --- the naming rule itself -------------------------------------------------


def test_sanitize_filename_preserves_chemical_casing():
    """str.capitalize() turned NaCl into Nacl; formulas carry meaning here."""
    exp = _load_exporter()
    assert exp.sanitize_filename("NaCl (99%)") == "NaCl_99"
    assert exp.sanitize_filename("TAPSO") == "TAPSO"
    assert exp.sanitize_filename("KI") == "KI"
    assert exp.sanitize_filename("MnCl2 x 4 H2O") == "MnCl2_x_4_H2O"


def test_sanitize_filename_matches_documented_examples():
    exp = _load_exporter()
    assert exp.sanitize_filename("sodium chloride") == "Sodium_chloride"
    assert exp.sanitize_filename("D-glucose") == "D-glucose"
    assert exp.sanitize_filename("(-)-Epinephrine") == "Epinephrine"
    assert exp.sanitize_filename("(R)-3-hydroxybutyrate") == "R-3-hydroxybutyrate"


def test_sanitize_filename_uppercases_leading_character():
    exp = _load_exporter()
    assert exp.sanitize_filename("peptone") == "Peptone"


# --- the stability index ----------------------------------------------------


def test_index_finds_existing_stem_by_identifier(tmp_path):
    exp = _load_exporter()
    root = tmp_path / "ingredients"
    (root / "mapped").mkdir(parents=True)
    (root / "mapped" / "Weird_Legacy_Name.yaml").write_text(
        yaml.safe_dump(_record("CHEBI:1", "Glucose"))
    )

    index = exp.collect_existing_filenames(root)
    assert index.for_record(_record("CHEBI:1", "Renamed Display Term")) == "Weird_Legacy_Name"


def test_index_finds_existing_stem_by_preferred_term_when_identifier_changed(tmp_path):
    """Promotion UNMAPPED_NNNN -> CHEBI:x changes the primary key itself."""
    exp = _load_exporter()
    root = tmp_path / "ingredients"
    (root / "unmapped").mkdir(parents=True)
    (root / "unmapped" / "Some_Compound.yaml").write_text(
        yaml.safe_dump(_record("UNMAPPED_0001", "Some compound"))
    )

    index = exp.collect_existing_filenames(root)
    assert index.for_record(_record("CHEBI:99", "Some compound")) == "Some_Compound"


def test_index_drops_ambiguous_keys(tmp_path):
    """Duplicate identifiers/terms cannot pick one name; fall through instead."""
    exp = _load_exporter()
    root = tmp_path / "ingredients"
    (root / "mapped").mkdir(parents=True)
    (root / "mapped" / "First.yaml").write_text(yaml.safe_dump(_record("CHEBI:7", "Shared term")))
    (root / "mapped" / "Second.yaml").write_text(yaml.safe_dump(_record("CHEBI:7", "Shared term")))

    index = exp.collect_existing_filenames(root)
    assert index.for_record(_record("CHEBI:7", "Shared term")) is None


def test_index_is_empty_for_missing_root(tmp_path):
    exp = _load_exporter()
    index = exp.collect_existing_filenames(tmp_path / "nope")
    assert index.for_record(_record("CHEBI:1", "Anything")) is None


# --- end-to-end: an export must not rename ----------------------------------


def test_export_keeps_existing_filename_even_when_rule_would_differ(tmp_path):
    """The core #147 guard: a legacy name survives a re-export untouched."""
    exp = _load_exporter()
    root = tmp_path / "ingredients"
    out = root / "mapped"
    out.mkdir(parents=True)
    # A name today's rule would never generate from this preferred_term.
    (out / "14-B-D-Galactobiose.yaml").write_text(
        yaml.safe_dump(_record("CHEBI:5", "1,4-B-D-Galactobiose"))
    )

    collection = tmp_path / "mapped_ingredients.yaml"
    _write_collection(collection, [_record("CHEBI:5", "1,4-B-D-Galactobiose")])

    index = exp.collect_existing_filenames(root)
    stats = exp.export_collection_to_individual_files(collection, out, existing_names=index)

    assert [p.name for p in sorted(out.glob("*.yaml"))] == ["14-B-D-Galactobiose.yaml"]
    assert stats["renamed"] == 0


def test_export_names_new_records_from_the_rule(tmp_path):
    exp = _load_exporter()
    out = tmp_path / "ingredients" / "mapped"
    out.mkdir(parents=True)

    collection = tmp_path / "mapped_ingredients.yaml"
    _write_collection(collection, [_record("CHEBI:6", "brand new compound")])

    index = exp.collect_existing_filenames(tmp_path / "ingredients")
    exp.export_collection_to_individual_files(collection, out, existing_names=index)

    assert (out / "Brand_new_compound.yaml").exists()


def test_export_is_idempotent_across_repeated_runs(tmp_path):
    """Two exports in a row must produce byte-identical filenames."""
    exp = _load_exporter()
    root = tmp_path / "ingredients"
    out = root / "mapped"
    out.mkdir(parents=True)

    collection = tmp_path / "mapped_ingredients.yaml"
    _write_collection(
        collection,
        [_record("CHEBI:8", "NaCl"), _record("CHEBI:9", "1,4-Butanediol")],
    )

    for _ in range(3):
        index = exp.collect_existing_filenames(root)
        exp.export_collection_to_individual_files(collection, out, existing_names=index)
        assert sorted(p.name for p in out.glob("*.yaml")) == [
            "14-Butanediol.yaml",
            "NaCl.yaml",
        ]


def test_export_still_suffixes_genuine_collisions(tmp_path):
    exp = _load_exporter()
    root = tmp_path / "ingredients"
    out = root / "mapped"
    out.mkdir(parents=True)

    collection = tmp_path / "mapped_ingredients.yaml"
    _write_collection(
        collection,
        [_record("CHEBI:10", "Same name"), _record("CHEBI:11", "Same name")],
    )

    index = exp.collect_existing_filenames(root)
    stats = exp.export_collection_to_individual_files(collection, out, existing_names=index)

    assert sorted(p.name for p in out.glob("*.yaml")) == ["Same_name.yaml", "Same_name_2.yaml"]
    assert stats["collisions"] == 1
