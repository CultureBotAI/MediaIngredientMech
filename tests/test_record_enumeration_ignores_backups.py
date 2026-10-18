"""`save_yaml` backups must not be read as records (#698).

`save_yaml(..., backup=True)` -- the default -- copies a file into a gitignored
`backups/` directory beside it before overwriting. `collect_existing_filenames`
enumerated with `rglob("*.yaml")`, so after any scripted edit every edited
record appeared twice with the same identifier and the same preferred_term. Both
continuity keys drop out on a collision by design, `FilenameIndex.for_record`
returned None, and the export fell back to today's naming rule: it *renamed the
records that had just been edited*.

On a case-insensitive filesystem that re-cases the file where git cannot see it,
and a local claw rebuild then publishes a different `MIM:` subject. On a
case-sensitive one it strands the published subject outright. Measured on a
ten-record edit: all ten lost continuity, 8 were renamed, all 8 published
subjects; zero on a checkout with no backups.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "src"))

from export_individual_records import (  # noqa: E402
    collect_existing_filenames,
    iter_record_files,
    sanitize_filename,
)

RECORD = "identifier: CHEBI:64205\npreferred_term: Ca(NO3)2\nmapping_status: MAPPED\n"


def _tree(tmp_path: Path, with_backup: bool) -> Path:
    root = tmp_path / "ingredients"
    (root / "mapped").mkdir(parents=True)
    (root / "unmapped").mkdir()
    (root / "mapped" / "Ca_No32.yaml").write_text(RECORD, encoding="utf-8")
    if with_backup:
        (root / "mapped" / "backups").mkdir()
        (root / "mapped" / "backups" / "Ca_No32_20260920_175906.yaml").write_text(
            RECORD, encoding="utf-8"
        )
    return root


def test_the_legacy_stem_really_differs_from_todays_rule():
    """Otherwise the fallback would be harmless and these tests would prove nothing."""
    assert sanitize_filename("Ca(NO3)2") != "Ca_No32"


def test_a_backup_is_not_enumerated_as_a_record(tmp_path):
    root = _tree(tmp_path, with_backup=True)
    assert [p.name for p in iter_record_files(root)] == ["Ca_No32.yaml"]


def test_a_backup_does_not_cost_a_record_its_filename(tmp_path):
    """The defect itself: with a backup present the stem must still be found."""
    root = _tree(tmp_path, with_backup=True)
    record = {"identifier": "CHEBI:64205", "preferred_term": "Ca(NO3)2"}
    assert collect_existing_filenames(root).for_record(record) == "Ca_No32"


def test_the_index_is_the_same_with_and_without_backups(tmp_path):
    clean = collect_existing_filenames(_tree(tmp_path / "a", with_backup=False))
    dirty = collect_existing_filenames(_tree(tmp_path / "b", with_backup=True))
    assert clean.by_identifier == dirty.by_identifier
    assert clean.by_preferred_term == dirty.by_preferred_term


def test_both_category_directories_are_enumerated(tmp_path):
    root = _tree(tmp_path, with_backup=False)
    (root / "unmapped" / "Thing.yaml").write_text(
        "identifier: UNMAPPED_0001\npreferred_term: Thing\n", encoding="utf-8"
    )
    assert {p.name for p in iter_record_files(root)} == {"Ca_No32.yaml", "Thing.yaml"}


def test_a_missing_tree_enumerates_nothing(tmp_path):
    assert list(iter_record_files(tmp_path / "absent")) == []


def test_the_real_corpus_has_full_filename_continuity():
    """Every record must find its own stem, or the next export renames it."""
    import yaml

    root = ROOT / "data" / "ingredients"
    index = collect_existing_filenames(root)
    shared = [
        path.name
        for path in iter_record_files(root)
        if index.for_record(yaml.safe_load(path.read_text(encoding="utf-8")) or {}) is None
    ]
    # Records that genuinely share BOTH keys with another live record are a
    # curation problem of their own; none exist today, so any entry here is new.
    assert shared == [], f"records with no filename continuity: {shared[:5]}"
