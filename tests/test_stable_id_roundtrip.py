"""Permanent IDs, not mutable mappings/labels, own round-trip continuity (#1265)."""

import importlib.util
import sys
from pathlib import Path

import click
import pytest
import yaml
from click.testing import CliRunner

ROOT = Path(__file__).parents[1]


def script(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(value, sort_keys=False))


def record(number, label="same", identifier="CHEBI:1", **kwargs):
    return {
        "mim_id": f"MIM:{number:07d}",
        "preferred_term": label,
        "identifier": identifier,
        "mapping_status": "MAPPED",
        **kwargs,
    }


def collection(path, records):
    write(path, {"total_count": len(records), "ingredients": records})


def test_simultaneous_name_mapping_and_category_change_keeps_owned_filename_and_fields(tmp_path):
    module = script("export_individual_records")
    root = tmp_path / "ingredients"
    original = record(1, "original", "UNMAPPED_0001", discussions=[{"discussion_id": "owned"}])
    write(root / "unmapped/Legacy.yaml", original)
    write(
        root / "mapped/Other.yaml",
        record(2, "target", "CHEBI:2", discussions=[{"discussion_id": "other"}]),
    )
    incoming = [record(1, "target", "CHEBI:2"), record(2, "target", "CHEBI:2")]
    source = tmp_path / "collection.yaml"
    collection(source, incoming)
    module.export_collection_to_individual_files(
        source,
        root / "mapped",
        preserved=module.collect_preserved_fields(root),
        existing_names=module.collect_existing_filenames(root),
    )
    one = yaml.safe_load((root / "mapped/Legacy.yaml").read_text())
    two = yaml.safe_load((root / "mapped/Other.yaml").read_text())
    assert one["mim_id"] == "MIM:0000001" and one["discussions"] == original["discussions"]
    assert two["discussions"] == [{"discussion_id": "other"}]


def test_new_id_cannot_steal_existing_filename_or_authored_fields(tmp_path):
    module = script("export_individual_records")
    root = tmp_path / "ingredients"
    write(
        root / "mapped/StableName.yaml", record(1, "old", discussions=[{"discussion_id": "owned"}])
    )
    source = tmp_path / "collection.yaml"
    collection(source, [record(2, "StableName"), record(1, "corrected")])
    stats = module.export_collection_to_individual_files(
        source,
        root / "mapped",
        preserved=module.collect_preserved_fields(root),
        existing_names=module.collect_existing_filenames(root),
    )
    old = yaml.safe_load((root / "mapped/StableName.yaml").read_text())
    new = yaml.safe_load((root / "mapped/StableName_2.yaml").read_text())
    assert old["mim_id"] == "MIM:0000001"
    assert old["discussions"] == [{"discussion_id": "owned"}]
    assert new["mim_id"] == "MIM:0000002" and "discussions" not in new
    assert stats["renamed"] == 0


@pytest.mark.parametrize("collector", ["collect_existing_filenames", "collect_preserved_fields"])
def test_duplicate_existing_ids_fail_before_clear(tmp_path, collector):
    module = script("export_individual_records")
    root = tmp_path / "ingredients"
    write(root / "mapped/First.yaml", record(1))
    write(root / "unmapped/Second.yaml", record(1))
    with pytest.raises(click.ClickException, match="Duplicate existing MIM ID"):
        getattr(module, collector)(root)
    assert (root / "mapped/First.yaml").exists() and (root / "unmapped/Second.yaml").exists()


def test_cross_category_duplicate_incoming_ids_leave_all_files_intact(tmp_path):
    module = script("export_individual_records")
    root = tmp_path / "ingredients"
    curated = tmp_path / "curated"
    original = root / "mapped/Original.yaml"
    write(original, record(1))
    before = original.read_bytes()
    collection(curated / "mapped_ingredients.yaml", [record(1)])
    collection(curated / "unmapped_ingredients.yaml", [record(1, "other", "UNMAPPED_0001")])
    result = CliRunner().invoke(
        module.main, ["--input-dir", str(curated), "--output-dir", str(root)]
    )
    assert result.exit_code != 0 and "Duplicate incoming MIM ID" in result.output
    assert original.read_bytes() == before


def test_missing_incoming_id_cannot_fall_back_to_a_mapping_match(tmp_path):
    module = script("export_individual_records")
    root = tmp_path / "ingredients"
    original = root / "mapped/Original.yaml"
    write(original, record(1))
    before = original.read_bytes()
    incoming = record(1)
    del incoming["mim_id"]
    source = tmp_path / "collection.yaml"
    collection(source, [incoming])
    with pytest.raises(click.ClickException, match="seven-digit"):
        module.export_collection_to_individual_files(
            source, root / "mapped", existing_names=module.collect_existing_filenames(root)
        )
    assert original.read_bytes() == before


def test_aggregate_order_survives_simultaneous_name_and_mapping_change(tmp_path):
    module = script("aggregate_records")
    reference = tmp_path / "collection.yaml"
    collection(reference, [record(1, "old", "CHEBI:1"), record(2, "second", "CHEBI:2")])
    current = [record(2, "second", "CHEBI:2"), record(1, "new", "CHEBI:99")]
    assert [r["mim_id"] for r in module._order_like(current, reference)] == [
        "MIM:0000001",
        "MIM:0000002",
    ]


def test_roundtrip_pairs_duplicate_mapping_and_label_by_permanent_id(tmp_path):
    module = script("verify_roundtrip")
    original = tmp_path / "original"
    again = tmp_path / "again"
    first = record(1, notes="first")
    second = record(2, notes="second")
    for directory, values in [(original, [first, second]), (again, [second, first])]:
        collection(directory / "mapped_ingredients.yaml", values)
        collection(directory / "unmapped_ingredients.yaml", [])
    result = module.verify_round_trip(original, again)
    assert result["errors"] == [] and result["data_diffs"] == 0
    collection(again / "mapped_ingredients.yaml", [record(3, notes="second"), first])
    assert module.verify_round_trip(original, again)["data_diffs"] > 0
