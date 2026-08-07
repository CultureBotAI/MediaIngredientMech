"""Report lookup must survive the case drift between record slug and filename.

`sanitize_filename` and the Edison runner disagree about case on a real subset of
this corpus. The record computes one stem, the report lands under another that
differs only in case:

    adeninyl cobamide  -> adeninyl_cobamide   vs   Adeninyl_Cobamide
    FeSO43 x n H2O     -> FeSO43_x_n_H2O      vs   Feso43_X_N_H2o

An exact-stem lookup does not raise on those; it just doesn't find them. The
research ran, the API was billed, the file is on disk, and the record silently
stays unannotated — indistinguishable from one nobody researched. 13 of 158
reports were in that state before the fallback existed.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location(
    "apply_edison_identity_findings",
    ROOT / "scripts" / "apply_edison_identity_findings.py")
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


@pytest.fixture
def research(tmp_path, monkeypatch):
    d = tmp_path / "ingredients"
    d.mkdir()
    monkeypatch.setattr(mod, "RESEARCH", d)
    return d


def test_index_is_keyed_case_folded(research):
    (research / "Adeninyl_Cobamide-edison-literature.md").write_text("x")
    idx = mod.report_index()
    assert "adeninyl_cobamide" in idx
    # the value is the real path, so the caller can read it
    assert idx["adeninyl_cobamide"].name.startswith("Adeninyl_Cobamide")


def test_exact_case_still_resolves(research):
    (research / "MnII_x_EDTA-edison-literature.md").write_text("x")
    assert "mnii_x_edta" in mod.report_index()


def test_unrelated_stems_do_not_collide(research):
    (research / "Foo-edison-literature.md").write_text("x")
    assert "bar" not in mod.report_index()


def test_other_edison_jobs_are_not_picked_up(research):
    """Only the literature job produces the identity reports this reads."""
    (research / "Foo-edison-precedent.md").write_text("x")
    assert mod.report_index() == {}


def test_a_collision_keeps_one_entry(research, monkeypatch):
    """Two stems differing only by case must not make the index ambiguous.

    Writing both files and asserting on the result is VACUOUS on this machine:
    macOS APFS is case-insensitive, so the second write overwrites the first and
    only one file ever exists. The test would pass without exercising anything.
    So the directory listing is faked to produce the collision a case-sensitive
    filesystem would really present.

    `setdefault` is first-in-glob-order, and `Path.glob` does not sort, so which
    path wins is not guaranteed -- only that exactly one key exists and it maps
    to a real file. The consequence if this regressed is silent and bad: two
    ingredients whose slugs differ only in case quoting each other's report into
    curation history.
    """
    real = research / "Foo_Bar-edison-literature.md"
    real.write_text("x")
    both = [real, research / "foo_bar-edison-literature.md"]

    class CaseSensitiveDir:
        def glob(self, _pattern):
            return iter(both)

    monkeypatch.setattr(mod, "RESEARCH", CaseSensitiveDir())
    idx = mod.report_index()
    assert list(idx) == ["foo_bar"], "one key, not two"
    assert idx["foo_bar"] in both


def test_a_heading_verdict_carries_the_line_beneath_it(research):
    """`## Executive recommendation` alone tells a curator nothing."""
    verdict, _ = mod.summarise(
        "intro\n## Executive recommendation\n\nRetain as UNMAPPED; the label is "
        "a family name.\n\nmore prose")
    assert "Retain as UNMAPPED" in verdict


@pytest.mark.parametrize("text,want", [
    ("| Recommended status | **UNMAPPED** | no row |", "UNMAPPED"),
    ("### Recommended mapping status\nUNMAPPED, family label", "family label"),
    ("- **Recommended status:** `UNMAPPED`", "UNMAPPED"),
])
def test_non_bolded_verdict_shapes_are_found(text, want):
    """49 of 240 reports stated a verdict in one of these shapes and were
    summarised as having none, deferring to a gitignored path instead."""
    verdict, _ = mod.summarise(text)
    assert want in verdict


def test_curie_prefixes_are_canonicalised():
    """Reports write `ChEBI:` and `MeSH:`; those fail this repo's CURIE pattern."""
    _, curies = mod.summarise("see ChEBI:2682 and MeSH:D000666")
    assert curies == ["CHEBI:2682", "MESH:D000666"]


def test_summarise_reports_curies_and_verdict():
    verdict, curies = mod.summarise(
        "blah\n**Recommended disposition: retain `UNMAPPED`.** because\n"
        "we considered CHEBI:33118 and CHEBI:33118 and MESH:D001665.\n")
    assert "retain" in verdict
    assert curies == ["CHEBI:33118", "MESH:D001665"], "must de-duplicate, in order"


def test_summarise_tolerates_a_report_with_no_bolded_verdict():
    verdict, curies = mod.summarise("free prose, no verdict, no curies")
    assert verdict == ""
    assert curies == []


@pytest.mark.parametrize("curie", [
    "MESH:D012313",   # RNA -- how #208's split was settled
    "MESH:C000123",
    "NCIT:C68610",    # Polymyxin B -- a CHEBI-only search called it ungroundable
    "CHEBI:33118",
    "FOODON:03301123",
])
def test_non_numeric_local_parts_are_captured(curie):
    """MeSH and NCIT accessions carry a letter; `\\d+` alone drops them.

    Those are the two ontologies that unblocked records a CHEBI-only search had
    reported as ungroundable, so summarising their reports as "No ontology CURIE
    was proposed" is the most misleading output this tool can produce.
    """
    _, curies = mod.summarise(f"the best candidate is {curie} here")
    assert curies == [curie]


def test_a_bare_number_is_not_mistaken_for_a_curie():
    _, curies = mod.summarise("CAS 145224-94-8 and pH 7.2 and 12345")
    assert curies == []
