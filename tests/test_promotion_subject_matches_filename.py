"""A promotion's SSSOM subject must be the record's existing filename stem.

`export_individual_records.FilenameIndex` never renames a record: it reuses the
stem the per-record file already has, because the committed corpus was written by
more than one historical naming rule and no single rule reproduces it.

`promote_resolved_unmapped` used to re-derive the subject with
`sanitize_filename(preferred_term)` instead. For a record whose file predates the
current rule the two disagree, and a promotion then writes an SSSOM subject that
no file matches -- `CrKSO42_X_12_H2O.yaml` against `MIM:CrKSO42_x_12_H2O`.

That is not cosmetic. `CurieNormalizer.resolve()` checks subjects against the
filename-derived record set, so a drifted subject yields UNKNOWN_SUBJECT and
`equivalent_term` refuses to cite the mapping at all -- a mapping that publishes
successfully, passes every SSSOM invariant, and cannot be used. Three of five
promotions landed that way.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "src"))

from export_individual_records import collect_existing_filenames, sanitize_filename


@pytest.fixture(scope="module")
def index():
    return collect_existing_filenames(ROOT / "data" / "ingredients")


def test_the_index_disagrees_with_sanitize_filename_somewhere():
    """If these never diverged the bug would be impossible -- and so would the fix
    be untested. This pins that the hazard is real in the committed corpus."""
    idx = collect_existing_filenames(ROOT / "data" / "ingredients")
    diverge = [t for t, stem in idx.by_preferred_term.items()
               if sanitize_filename(t) != stem]
    assert diverge, "no record disagrees; this test can no longer detect the bug"


def test_every_published_mim_subject_has_a_matching_record_file(index):
    """Read-only audit of the invariant the fix protects.

    Scoped to the records this sweep promoted. The wider corpus still carries
    historical drift tracked in #236/#293/#299, so asserting over all subjects
    would fail for reasons this test is not about.
    """
    sssom = (ROOT / "mappings" / "ingredient_mappings.sssom.tsv").read_text()
    subjects = {ln.split("\t", 1)[0] for ln in sssom.splitlines()
                if ln.startswith("MIM:")}
    stems = {f"MIM:{s}" for s in index.by_preferred_term.values()}
    stems |= {f"MIM:{s}" for s in index.by_identifier.values()}

    promoted = ["MES Hydrat", "CrKSO42 x 12 H2O", "KH2PO3",
                "TitaniumIII chloride", "TAPSO"]
    for term in promoted:
        stem = index.by_preferred_term.get(term)
        assert stem, f"{term} has no per-record file"
        assert f"MIM:{stem}" in subjects, (
            f"{term}: file is {stem}.yaml but no SSSOM subject MIM:{stem}")


@pytest.mark.parametrize("term", [
    "MES Hydrat", "CrKSO42 x 12 H2O", "KH2PO3", "TitaniumIII chloride", "TAPSO",
])
def test_promoted_records_resolve_through_the_normalizer(term, index):
    """The end the drift actually broke: can a consumer cite this mapping?"""
    from mediaingredientmech.curie import CurieNormalizer
    n = CurieNormalizer(
        sssom_path=ROOT / "mappings" / "ingredient_mappings.sssom.tsv",
        alias_path=ROOT / "mappings" / "mim_curie_aliases.tsv")
    stem = index.by_preferred_term[term]
    v = n.resolve(f"MIM:{stem}")
    assert v.ok, f"{term}: {v.problem} — {v.note}"


def test_registry_mint_is_invariant_to_subject_case():
    """Rule B1 lowercases the slug before matching it against the registry mint.

    Worth pinning for the reason #299 found: it means Rule B1 is blind to subject
    case by construction, so it passed while 64 published subjects were being
    case-mangled. See `test_published_mim_subject_case.py`, which pins the
    spellings B1 cannot.
    """
    from reground_mapped_record import check_registry_mint
    assert (check_registry_mint("kgmicrobe.compound:", "CrKSO42_X_12_H2O")
            == check_registry_mint("kgmicrobe.compound:", "CrKSO42_x_12_H2O"))
