"""Guard tests for per-record filename collisions in the exporter.

A merge tombstone deliberately keeps its winner's identifier (the documented
`Calcium D-Pantothenate` pattern). After the #315 merges, `Sodium tartrate` and
`Na-tartrate` both held `CHEBI:63017`, and the export dropped to 2496 files for
2497 records — caught only by the round-trip CI check.

**The cause was case-insensitivity, not the shared identifier.** Both records
resolved to the stable stem `Sodium_Tartrate`; the second then fell back to
`sanitize_filename("Sodium tartrate")` = `Sodium_tartrate`, a *different* Python
string that is the *same file* on APFS. The `taken` set compared
case-sensitively, so nothing noticed, and one record silently overwrote the
other. Same class as #299.

`test_filenames_that_differ_only_by_case_do_not_collide` is therefore the test
that actually fails without the fix. The other two assert properties that
already held and are worth keeping so the shared-identifier fallback cannot
regress into the loss it protects against.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "src"))


def _load():
    spec = importlib.util.spec_from_file_location(
        "export_individual_records", ROOT / "scripts" / "export_individual_records.py"
    )
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    # Register before exec: the module defines dataclasses, and dataclasses
    # resolves annotations via sys.modules[cls.__module__].
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def _write_collection(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(
        {"total_count": len(records), "ingredients": records}, sort_keys=False),
        encoding="utf-8")


def _export(mod, tmp_path: Path, records: list[dict]) -> list[str]:
    curated, out = tmp_path / "curated", tmp_path / "ingredients"
    _write_collection(curated / "mapped_ingredients.yaml", records)
    mod.export_collection_to_individual_files(
        collection_path=curated / "mapped_ingredients.yaml",
        output_dir=out / "mapped",
        dry_run=False,
        preserved=mod.collect_preserved_fields(out),
        existing_names=mod.collect_existing_filenames(out),
    )
    return sorted(p.stem for p in (out / "mapped").glob("*.yaml"))


def test_records_sharing_an_identifier_get_distinct_files(tmp_path):
    """The merge-tombstone shape: same identifier, different preferred_term."""
    mod = _load()
    records = [
        {"identifier": "CHEBI:63017", "preferred_term": "Sodium tartrate",
         "mapping_status": "MAPPED"},
        {"identifier": "CHEBI:63017", "preferred_term": "Na-tartrate",
         "mapping_status": "REJECTED"},
    ]
    stems = _export(mod, tmp_path, records)
    assert len(stems) == 2, f"a record was lost: {stems}"


def test_export_recovers_from_a_previously_lost_file(tmp_path):
    """Losing a file must not be sticky.

    With one file already missing, `collect_existing_filenames` sees a single
    file for the shared identifier and treats the mapping as unambiguous, handing
    both records that one stem. The fallback has to recover rather than lose the
    record again on every run. This held before the fix and is asserted so it
    keeps holding.
    """
    mod = _load()
    records = [
        {"identifier": "CHEBI:63017", "preferred_term": "Sodium tartrate",
         "mapping_status": "MAPPED"},
        {"identifier": "CHEBI:63017", "preferred_term": "Na-tartrate",
         "mapping_status": "REJECTED"},
    ]
    first = _export(mod, tmp_path, records)
    assert len(first) == 2

    (tmp_path / "ingredients" / "mapped" / "Na-tartrate.yaml").unlink()
    recovered = _export(mod, tmp_path, records)
    assert len(recovered) == 2, f"lost record did not come back: {recovered}"


def test_filenames_that_differ_only_by_case_do_not_collide(tmp_path):
    """`Sodium_Tartrate` and `Sodium_tartrate` are one file on macOS/APFS."""
    mod = _load()
    records = [
        {"identifier": "CHEBI:1", "preferred_term": "Sodium Tartrate",
         "mapping_status": "MAPPED"},
        {"identifier": "CHEBI:2", "preferred_term": "Sodium tartrate",
         "mapping_status": "MAPPED"},
    ]
    stems = _export(mod, tmp_path, records)
    assert len({s.lower() for s in stems}) == 2, f"case-only collision: {stems}"
