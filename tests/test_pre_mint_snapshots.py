"""Only exact inventoried archival collections use the pre-ID schema (#1265)."""

import json
import shutil
from pathlib import Path

import pytest

from mediaingredientmech.validation import historical_snapshots as snapshots
from mediaingredientmech.validation.write_validated import validate_ingredient

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = json.loads((snapshots.SCHEMA_DIR / "pre_mint_snapshot_inventory.json").read_text())


@pytest.mark.parametrize("name", sorted(INVENTORY["files"]))
def test_original_backlog_snapshot_retains_frozen_schema(name):
    import yaml

    path = ROOT / name
    schema = snapshots.historical_schema(path, ROOT)
    assert schema.name == "pre_mint_ingredient_snapshot.yaml"
    assert validate_ingredient(yaml.safe_load(path.read_text()), schema_path=schema) == []


def test_modified_snapshot_does_not_escape_current_id_requirements(tmp_path):
    name = next(iter(INVENTORY["files"]))
    path = tmp_path / name
    path.parent.mkdir(parents=True)
    path.write_bytes((ROOT / name).read_bytes() + b"\n")
    with pytest.raises(ValueError, match="snapshot was modified"):
        snapshots.historical_schema(path, tmp_path)


def test_unknown_live_record_cannot_select_legacy_schema(tmp_path):
    path = tmp_path / "data/ingredients/unmapped/New.yaml"
    path.parent.mkdir(parents=True)
    path.write_text("identifier: UNMAPPED_1\npreferred_term: New\nmapping_status: UNMAPPED\n")
    assert snapshots.historical_schema(path, tmp_path) is None
    import yaml

    assert any(
        "mim_id" in error.message for error in validate_ingredient(yaml.safe_load(path.read_text()))
    )


@pytest.mark.parametrize("name", ["pre_mint_ingredient_snapshot.yaml", "mech_shared.yaml"])
def test_frozen_schema_tamper_is_refused(tmp_path, monkeypatch, name):
    schema_dir = tmp_path / "schema"
    schema_dir.mkdir()
    for filename in [
        "pre_mint_snapshot_inventory.json",
        "pre_mint_ingredient_snapshot.yaml",
        "mech_shared.yaml",
    ]:
        shutil.copyfile(snapshots.SCHEMA_DIR / filename, schema_dir / filename)
    path = schema_dir / name
    path.write_bytes(path.read_bytes() + b"\n")
    monkeypatch.setattr(snapshots, "SCHEMA_DIR", schema_dir)
    with pytest.raises(ValueError, match="schema differs"):
        snapshots.historical_schema(ROOT / next(iter(INVENTORY["files"])), ROOT)


def test_frozen_schemas_are_not_live_schema_discovery_candidates():
    live_schemas = set(ROOT.glob("src/*/schema/*.yaml"))
    assert snapshots.SCHEMA_DIR.name == "historical"
    assert (snapshots.SCHEMA_DIR / "pre_mint_ingredient_snapshot.yaml") not in live_schemas
    assert (snapshots.SCHEMA_DIR / "mech_shared.yaml") not in live_schemas
    assert ROOT / "src/mediaingredientmech/schema/mediaingredientmech.yaml" in live_schemas
    assert ROOT / "src/mediaingredientmech/schema/mech_shared.yaml" in live_schemas
