"""The microbedecoder promotion must publish the stem the record already has (#307).

This is #293's defect in a second script. `test_promotion_subject_matches_filename`
covers `promote_resolved_unmapped`; the same re-derivation survived in
`promote_microbedecoder_residual`, where the script's own docstring records it as
a known defect and warns against re-pointing the tool before it is fixed.

It stayed latent because every row in the pinned manifest is a no-op, so nothing
exercised the path -- which is why the guard here is on the source as well as on
the behaviour.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "src"))

from export_individual_records import collect_existing_filenames, sanitize_filename  # noqa: E402

SCRIPT = ROOT / "scripts" / "promote_microbedecoder_residual.py"


def test_an_existing_stem_wins_over_a_re_derived_one(tmp_path):
    """A legacy stem with a modern preferred_term -- the case that broke #293."""
    tree = tmp_path / "ingredients" / "unmapped"
    tree.mkdir(parents=True)
    (tree / "Phenethylamine_Hydrochloride.yaml").write_text(
        "identifier: UNMAPPED_0001\npreferred_term: 2-phenylethylamine\n", encoding="utf-8"
    )
    index = collect_existing_filenames(tmp_path / "ingredients")
    record = {"identifier": "UNMAPPED_0001", "preferred_term": "2-phenylethylamine"}

    assert index.for_record(record) == "Phenethylamine_Hydrochloride"
    assert sanitize_filename(record["preferred_term"]) != "Phenethylamine_Hydrochloride"


def test_a_record_with_no_file_falls_back_to_the_naming_rule(tmp_path):
    (tmp_path / "ingredients").mkdir()
    index = collect_existing_filenames(tmp_path / "ingredients")
    assert index.for_record({"identifier": "UNMAPPED_9999", "preferred_term": "New"}) is None


def test_the_stem_survives_the_identifier_change_a_promotion_makes(tmp_path):
    """Promotion rewrites `identifier`, so the lookup must hold on preferred_term."""
    tree = tmp_path / "ingredients" / "unmapped"
    tree.mkdir(parents=True)
    (tree / "Legacy_Stem.yaml").write_text(
        "identifier: UNMAPPED_0002\npreferred_term: Some Compound\n", encoding="utf-8"
    )
    index = collect_existing_filenames(tmp_path / "ingredients")
    assert index.for_record(
        {"identifier": "CHEBI:12345", "preferred_term": "Some Compound"}
    ) == "Legacy_Stem"


def test_the_script_no_longer_derives_the_subject_from_preferred_term_alone():
    """Regression guard: the manifest is all no-ops, so nothing else would notice."""
    source = SCRIPT.read_text(encoding="utf-8")
    assert "slug = sanitize_filename(pref)" not in source
    assert "_stems.for_record(rec) or sanitize_filename(pref)" in source


def test_the_index_is_built_before_the_records_are_transformed():
    """Indexing after identifiers are rewritten would defeat the lookup."""
    source = SCRIPT.read_text(encoding="utf-8")
    assert source.index("collect_existing_filenames(") < source.index("_stems.for_record(rec)")
