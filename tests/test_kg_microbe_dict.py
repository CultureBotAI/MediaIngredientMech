"""The kg-microbe dictionary loader, which had no tests at all until #578.

That absence is the whole story: the loader pointed at a file kg-microbe
deleted on 2026-04-30, a missing file made it return quietly, and the reviewer
then turned P2.5/P4.4 off. Nothing failed, so nothing was noticed for four
months. Every test here that asserts on a warning is guarding that specific
failure mode -- an empty dictionary must always be loud.
"""

from __future__ import annotations

import gzip
import logging
from pathlib import Path

import pytest

from mediaingredientmech.validation.kg_microbe_dict import (
    AMBIGUITY_THRESHOLD,
    ARTIFACT_RELPATH,
    KGMICROBE_ROOT_ENV,
    POLLUTION_SYNONYM_THRESHOLD,
    KgMicrobeDict,
    kgmicrobe_root,
    resolve_default_dict_path,
)

HEADER = (
    "subject_id\tsubject_label\tpredicate_id\tobject_id\tobject_label\t"
    "object_source\tmapping_justification\tsource\tmapping_date\tconfidence\t"
    "comment\tobject_formula\tobject_category"
)


def _row(subject_id, subject_label, predicate, object_id, object_label, formula=""):
    return "\t".join(
        [
            subject_id,
            subject_label,
            predicate,
            object_id,
            object_label,
            "",
            "semapv:LexicalMatching",
            "",
            "2026-09-08",
            "",
            "",
            formula,
            "biolink:ChemicalSubstance",
        ]
    )


def _write_set(path: Path, rows: list[str], *, header: str = HEADER) -> Path:
    """Write a mapping set with the SSSOM ``#`` metadata block the real file carries."""
    body = "\n".join(
        [
            '# curie_map:',
            '#   CHEBI: "http://purl.obolibrary.org/obo/CHEBI_"',
            "# mapping_set_id: \"https://w3id.org/kg-microbe/test\"",
            header,
            *rows,
        ]
    )
    with gzip.open(path, "wt", encoding="utf-8") as handle:
        handle.write(body + "\n")
    return path


@pytest.fixture()
def mapping_set(tmp_path):
    """A small set: two entities, one shared surface form, plus junk to filter."""
    rows = [
        # CHEBI:17234 -- canonical name, one synonym, one xref row (no surface form)
        _row("kgm.name:glucose", "Glucose", "skos:exactMatch", "CHEBI:17234", "Glucose", "C6H12O6"),
        _row("kgm.name:dextrose", "Dextrose", "skos:closeMatch", "CHEBI:17234", "Glucose", "C6H12O6"),
        _row("cas:50-99-7", "", "skos:exactMatch", "CHEBI:17234", "Glucose", "C6H12O6"),
        # An xref row that *does* carry a label; it is still not a surface form.
        _row("kegg.compound:C00293", "Grape sugar", "skos:exactMatch", "CHEBI:17234", "Glucose"),
        # A registry code wearing a name's clothing, and a one-character label
        _row("kgm.name:cas50-99-7", "CAS:50-99-7", "skos:closeMatch", "CHEBI:17234", "Glucose"),
        _row("kgm.name:g", "G", "skos:closeMatch", "CHEBI:17234", "Glucose"),
        # CHEBI:4167 -- shares the surface form "Dextrose" with CHEBI:17234
        _row("kgm.name:d-glucose", "D-glucose", "skos:exactMatch", "CHEBI:4167", "D-glucose"),
        _row("kgm.name:dextrose", "Dextrose", "skos:closeMatch", "CHEBI:4167", "D-glucose"),
        # A non-CHEBI entity, which this loader does not index
        _row("kgm.name:garden_soil", "Garden soil", "skos:exactMatch", "ENVO:00002263", "soil"),
    ]
    return _write_set(tmp_path / "unified.sssom.tsv.gz", rows)


def test_the_per_entity_view_is_rebuilt_from_the_triple_table(mapping_set):
    """object_label is the canonical name; kgm.name subjects supply the surface forms."""
    d = KgMicrobeDict(mapping_set)
    entry = d.get_entry("CHEBI:17234")
    assert entry is not None
    assert entry.canonical_name == "Glucose"
    assert entry.formula == "C6H12O6"
    assert entry.synonyms == {"Dextrose"}


def test_the_canonical_name_is_not_offered_as_a_synonym(mapping_set):
    """P4.4 proposes from `synonyms`; offering the name the record already has is noise."""
    assert "Glucose" not in KgMicrobeDict(mapping_set).get_entry("CHEBI:17234").synonyms


def test_xref_rows_contribute_no_surface_form(mapping_set):
    """Only `kgm.name:*` subjects carry names; an xref's label is not one (#591).

    Probed with a non-empty label, because `lookup_synonym("")` returns early
    and would pass this test without consulting the index at all.
    """
    d = KgMicrobeDict(mapping_set)
    assert d.lookup_synonym("Grape sugar") == set()
    assert "Grape sugar" not in d.get_entry("CHEBI:17234").synonyms
    # The row still contributed its entity, just not a name for it.
    assert d.get_entry("CHEBI:17234").canonical_name == "Glucose"


@pytest.mark.parametrize("junk", ["CAS:50-99-7", "G"])
def test_identifier_shaped_and_too_short_forms_are_dropped(mapping_set, junk):
    assert KgMicrobeDict(mapping_set).lookup_synonym(junk) == set()


def test_the_reverse_index_is_one_to_many_and_case_insensitive(mapping_set):
    """The 1:many shape is what P2.5 reads to spot a disagreement."""
    assert KgMicrobeDict(mapping_set).lookup_synonym("dextrose") == {"CHEBI:17234", "CHEBI:4167"}


def test_only_chebi_objects_are_indexed(mapping_set):
    d = KgMicrobeDict(mapping_set)
    assert d.get_entry("ENVO:00002263") is None
    assert d.size == 2


def test_a_form_under_many_entities_is_ambiguous(tmp_path):
    """P2.5 skips these; a token under six entities cannot arbitrate anything."""
    rows = [
        _row("kgm.name:na", "Sodium ion", "skos:closeMatch", f"CHEBI:{i}", f"thing {i}")
        for i in range(AMBIGUITY_THRESHOLD + 1)
    ]
    d = KgMicrobeDict(_write_set(tmp_path / "ambiguous.sssom.tsv.gz", rows))
    assert d.is_ambiguous("Sodium ion")
    assert not d.is_ambiguous("Dextrose")


def test_a_polluted_entry_keeps_its_name_but_leaves_the_index(tmp_path):
    """Its synonyms are not real, so they must not arbitrate other records' mappings."""
    rows = [_row("kgm.name:polluted", "Polluted", "skos:exactMatch", "CHEBI:9", "Polluted")]
    rows += [
        _row(f"kgm.name:s{i}", f"surface form {i}", "skos:closeMatch", "CHEBI:9", "Polluted")
        for i in range(POLLUTION_SYNONYM_THRESHOLD + 1)
    ]
    d = KgMicrobeDict(_write_set(tmp_path / "polluted.sssom.tsv.gz", rows))
    assert d.get_entry("CHEBI:9").canonical_name == "Polluted"
    assert d.get_entry("CHEBI:9").synonyms == set()
    assert d.lookup_synonym("surface form 3") == set()
    # Still reachable by its own name.
    assert d.lookup_synonym("Polluted") == {"CHEBI:9"}


def test_a_missing_file_is_loud(tmp_path, caplog):
    """The four-month failure: this used to return with no trace at all."""
    with caplog.at_level(logging.WARNING):
        d = KgMicrobeDict(tmp_path / "absent.sssom.tsv.gz")
        assert d.size == 0
    assert "does not exist" in caplog.text
    assert KGMICROBE_ROOT_ENV in caplog.text


def test_an_unlocatable_checkout_is_loud(tmp_path, caplog, monkeypatch):
    monkeypatch.delenv(KGMICROBE_ROOT_ENV, raising=False)
    monkeypatch.setattr(
        "mediaingredientmech.validation.kg_microbe_dict.REPO_ROOT", tmp_path / "nowhere" / "repo"
    )
    with caplog.at_level(logging.WARNING):
        d = KgMicrobeDict()
        assert d.size == 0
    assert "no kg-microbe checkout found" in caplog.text


def test_the_wrong_table_is_loud_rather_than_silently_empty(tmp_path, caplog):
    """The legacy wide TSV would take this path; it must not look like clean data."""
    legacy_header = "chebi_id\tcanonical_name\tsynonyms\tformula"
    path = tmp_path / "legacy.tsv.gz"
    with gzip.open(path, "wt", encoding="utf-8") as handle:
        handle.write(legacy_header + "\nCHEBI:17234\tGlucose\tDextrose\tC6H12O6\n")
    with caplog.at_level(logging.WARNING):
        assert KgMicrobeDict(path).size == 0
    assert "missing the column" in caplog.text


def test_a_header_only_file_yields_an_empty_dictionary_without_claiming_a_defect(
    tmp_path, caplog
):
    """A well-formed but empty set is not a broken one, so no column warning fires.

    The reviewer still refuses to treat the result as clean: it warns on any
    empty dictionary, whatever the reason.
    """
    path = _write_set(tmp_path / "empty.sssom.tsv.gz", [])
    with caplog.at_level(logging.WARNING):
        assert KgMicrobeDict(path).size == 0
    assert "missing the column" not in caplog.text
    assert "does not exist" not in caplog.text


def test_load_is_idempotent(mapping_set):
    d = KgMicrobeDict(mapping_set)
    d.load()
    d.load()
    assert d.size == 2
    assert d.loaded


def test_an_uncompressed_set_reads_too(tmp_path, mapping_set):
    plain = tmp_path / "plain.sssom.tsv"
    with gzip.open(mapping_set, "rt", encoding="utf-8") as src:
        plain.write_text(src.read(), encoding="utf-8")
    assert KgMicrobeDict(plain).size == 2


class TestRootResolution:
    """#580's shape, refused here at the point the fix introduced a new reader."""

    def test_the_environment_variable_wins(self, tmp_path, monkeypatch):
        monkeypatch.setenv(KGMICROBE_ROOT_ENV, str(tmp_path))
        assert kgmicrobe_root() == tmp_path
        assert resolve_default_dict_path() == tmp_path / ARTIFACT_RELPATH

    @pytest.mark.parametrize("blank", ["", "   "])
    def test_an_exported_but_empty_variable_is_treated_as_unset(
        self, tmp_path, monkeypatch, blank
    ):
        """`Path("")` is the working directory, which is never what was meant."""
        monkeypatch.setenv(KGMICROBE_ROOT_ENV, blank)
        monkeypatch.setattr(
            "mediaingredientmech.validation.kg_microbe_dict.REPO_ROOT",
            tmp_path / "nowhere" / "repo",
        )
        assert kgmicrobe_root() is None

    def test_a_tilde_value_is_expanded(self, monkeypatch):
        monkeypatch.setenv(KGMICROBE_ROOT_ENV, "~/kg-microbe")
        root = kgmicrobe_root()
        assert root is not None and "~" not in str(root)
        assert root == Path.home() / "kg-microbe"

    def test_the_sibling_checkout_is_the_fallback(self, tmp_path, monkeypatch):
        monkeypatch.delenv(KGMICROBE_ROOT_ENV, raising=False)
        (tmp_path / "kg-microbe").mkdir()
        monkeypatch.setattr(
            "mediaingredientmech.validation.kg_microbe_dict.REPO_ROOT",
            tmp_path / "MediaIngredientMech",
        )
        assert kgmicrobe_root() == tmp_path / "kg-microbe"


def test_a_narrowmatch_name_row_is_not_a_synonym(tmp_path):
    """A narrower term's name is not an equivalent form of the broader entity (#585).

    No such row exists in today's artifact; this guards the emitter changing.
    """
    rows = [
        _row("kgm.name:salt", "Salt", "skos:exactMatch", "CHEBI:26710", "Salt"),
        _row("kgm.name:rock_salt", "Rock salt", "skos:narrowMatch", "CHEBI:26710", "Salt"),
    ]
    d = KgMicrobeDict(_write_set(tmp_path / "narrow.sssom.tsv.gz", rows))
    assert d.get_entry("CHEBI:26710").synonyms == set()
    assert d.lookup_synonym("Rock salt") == set()


def test_a_corrupt_artifact_degrades_instead_of_aborting_the_review(tmp_path, caplog):
    """One unreadable auxiliary file must not take down an otherwise fine run (#586)."""
    path = tmp_path / "truncated.sssom.tsv.gz"
    good = _write_set(tmp_path / "good.sssom.tsv.gz", [
        _row("kgm.name:glucose", "Glucose", "skos:exactMatch", "CHEBI:17234", "Glucose"),
    ])
    path.write_bytes(good.read_bytes()[: len(good.read_bytes()) // 2])
    with caplog.at_level(logging.WARNING):
        d = KgMicrobeDict(path)
        assert d.size == 0  # degraded, not raised
    assert "could not be read" in caplog.text


def test_a_corrupt_artifact_does_not_serve_a_half_built_index(tmp_path):
    """Whatever was parsed before the truncation must be discarded, not reported."""
    rows = [
        _row(f"kgm.name:e{i}", f"entity {i}", "skos:exactMatch", f"CHEBI:{i}", f"entity {i}")
        for i in range(400)
    ]
    good = _write_set(tmp_path / "big.sssom.tsv.gz", rows)
    truncated = tmp_path / "half.sssom.tsv.gz"
    truncated.write_bytes(good.read_bytes()[: int(len(good.read_bytes()) * 0.6)])
    d = KgMicrobeDict(truncated)
    assert d.size == 0
    assert d.lookup_synonym("entity 1") == set()
