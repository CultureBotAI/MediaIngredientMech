"""The on-disk index that stops a review re-parsing 610,248 rows (#589).

Parsing the artifact costs seconds and hundreds of megabytes; a single-record
review needs a handful of lookups from it. The parse is a pure function of the
artifact's bytes, so it happens once and is kept in a SQLite index keyed by the
artifact's content hash.

Two code paths now answer the same questions, which is the risk this file
exists to cover: the first test asserts they cannot disagree, and the rest
assert the cache is actually used, actually invalidated, and never fatal.
"""

from __future__ import annotations

import gzip
import logging
import os
import sqlite3

import pytest

from mediaingredientmech.validation.kg_microbe_dict import (
    CACHE_DIR_ENV,
    CACHE_SCHEMA_VERSION,
    KgMicrobeDict,
    cache_dir,
)

from .test_kg_microbe_dict import _row, _write_set


@pytest.fixture()
def mapping_set(tmp_path):
    rows = [
        _row("kgm.name:glucose", "Glucose", "skos:exactMatch", "CHEBI:17234", "Glucose", "C6H12O6"),
        _row("kgm.name:dextrose", "Dextrose", "skos:closeMatch", "CHEBI:17234", "Glucose", "C6H12O6"),
        _row("kgm.name:d-glucose", "D-glucose", "skos:exactMatch", "CHEBI:4167", "D-glucose"),
        _row("kgm.name:dextrose", "Dextrose", "skos:closeMatch", "CHEBI:4167", "D-glucose"),
        # Mixed case and a non-ASCII form: SQLite's NOCASE folds ASCII only,
        # so the lowercasing must stay in Python on both paths.
        _row("kgm.name:kochsalz", "Kochsalz", "skos:closeMatch", "CHEBI:26710", "NaCl"),
        _row("kgm.name:nasalz", "Natriumchlorür", "skos:closeMatch", "CHEBI:26710", "NaCl"),
    ]
    return _write_set(tmp_path / "unified.sssom.tsv.gz", rows)


PROBES = ["Glucose", "glucose", "Dextrose", "DEXTROSE", "Kochsalz", "kochsalz",
          "Natriumchlorür", "NATRIUMCHLORÜR", "absent", ""]


def test_the_cached_and_uncached_paths_cannot_disagree(mapping_set):
    """Two implementations of one contract: pin them to each other."""
    fresh = KgMicrobeDict(mapping_set, use_cache=False)
    fresh.load()
    cached = KgMicrobeDict(mapping_set)
    cached.load()          # builds and writes
    warm = KgMicrobeDict(mapping_set)
    warm.load()            # reads it back
    assert warm._db is not None, "expected the warm instance to be served from the index"

    for d in (cached, warm):
        assert d.size == fresh.size
        for probe in PROBES:
            assert d.lookup_synonym(probe) == fresh.lookup_synonym(probe), probe
            assert d.is_ambiguous(probe) == fresh.is_ambiguous(probe), probe
        for chebi in ("CHEBI:17234", "CHEBI:4167", "CHEBI:26710", "CHEBI:9999"):
            got, want = d.get_entry(chebi), fresh.get_entry(chebi)
            assert (got is None) == (want is None), chebi
            if want is not None:
                assert got.canonical_name == want.canonical_name
                assert got.formula == want.formula
                assert got.synonyms == want.synonyms, chebi


def test_a_warm_load_does_not_parse_the_artifact_again(mapping_set, monkeypatch):
    """The whole point: the second run must not repeat the work."""
    KgMicrobeDict(mapping_set).load()

    def explode(*args, **kwargs):  # pragma: no cover - must never run
        raise AssertionError("the artifact was parsed despite a usable cache")

    monkeypatch.setattr(KgMicrobeDict, "_ingest_rows", explode)
    warm = KgMicrobeDict(mapping_set)
    assert warm.size == 3
    assert warm.get_entry("CHEBI:17234").synonyms == {"Dextrose"}


def test_the_index_is_keyed_on_content_so_a_changed_artifact_rebuilds(tmp_path, mapping_set):
    """Keyed on the bytes, not the name or mtime, so a stale hit is impossible."""
    first = KgMicrobeDict(mapping_set)
    assert first.size == 3

    with gzip.open(mapping_set, "rt", encoding="utf-8") as handle:
        text = handle.read()
    extra = _row("kgm.name:sucrose", "Sucrose", "skos:exactMatch", "CHEBI:17992", "Sucrose")
    with gzip.open(mapping_set, "wt", encoding="utf-8") as handle:
        handle.write(text + extra + "\n")

    assert KgMicrobeDict(mapping_set).size == 4


def test_writing_a_new_index_reaps_older_artifact_indexes(tmp_path, mapping_set):
    """A content-keyed cache must still stay bounded as kg-microbe republishes."""
    KgMicrobeDict(mapping_set).load()
    old_cache = next(cache_dir().glob("*.sqlite"))
    os.utime(old_cache, (1, 1))

    unrelated = cache_dir() / "do-not-touch.sqlite"
    unrelated.write_text("not a kg-microbe dictionary", encoding="utf-8")

    with gzip.open(mapping_set, "rt", encoding="utf-8") as handle:
        text = handle.read()
    extra = _row("kgm.name:sucrose", "Sucrose", "skos:exactMatch", "CHEBI:17992", "Sucrose")
    with gzip.open(mapping_set, "wt", encoding="utf-8") as handle:
        handle.write(text + extra + "\n")

    KgMicrobeDict(mapping_set).load()

    assert not old_cache.exists()
    assert unrelated.exists()
    assert len(list(cache_dir().glob("kgm-dict-v*.sqlite"))) == 1


def test_a_warm_load_reaps_older_artifact_indexes(mapping_set):
    KgMicrobeDict(mapping_set).load()
    current_cache = next(cache_dir().glob("kgm-dict-v*.sqlite"))

    old_cache = cache_dir() / f"kgm-dict-v0-{'0' * 32}.sqlite"
    old_cache.write_text("superseded schema", encoding="utf-8")
    os.utime(old_cache, (1, 1))

    warm = KgMicrobeDict(mapping_set)
    warm.load()

    assert warm._db is not None
    assert current_cache.exists()
    assert not old_cache.exists()


def test_an_identical_artifact_at_another_path_reuses_the_index(tmp_path, mapping_set):
    """Content-keyed, so a re-published but unchanged artifact is not re-parsed."""
    KgMicrobeDict(mapping_set).load()
    twin = tmp_path / "copy.sssom.tsv.gz"
    twin.write_bytes(mapping_set.read_bytes())
    other = KgMicrobeDict(twin)
    other.load()
    assert other._db is not None
    assert other.size == 3


def test_a_corrupt_index_is_discarded_and_rebuilt(mapping_set, caplog):
    """A bad cache must cost a rebuild, never a failed review."""
    KgMicrobeDict(mapping_set).load()
    written = sorted(cache_dir().glob("*.sqlite"))
    assert len(written) == 1
    written[0].write_bytes(b"this is not a database")

    with caplog.at_level(logging.WARNING):
        recovered = KgMicrobeDict(mapping_set)
        assert recovered.size == 3
    assert "unusable dictionary cache" in caplog.text
    # Rebuilt, so the next run is fast again.
    assert sorted(cache_dir().glob("*.sqlite"))


def test_use_cache_false_neither_reads_nor_writes(mapping_set):
    d = KgMicrobeDict(mapping_set, use_cache=False)
    assert d.size == 3
    assert d._db is None
    assert not list(cache_dir().glob("*.sqlite"))


def test_an_unwritable_cache_directory_is_not_fatal(mapping_set, monkeypatch, tmp_path, caplog):
    """A cache is an optimisation; losing it must not cost the review."""
    blocked = tmp_path / "blocked"
    blocked.write_text("not a directory", encoding="utf-8")
    monkeypatch.setenv(CACHE_DIR_ENV, str(blocked / "sub"))
    with caplog.at_level(logging.WARNING):
        d = KgMicrobeDict(mapping_set)
        assert d.size == 3           # answers are still correct
        assert d.get_entry("CHEBI:17234").synonyms == {"Dextrose"}
    assert "could not write dictionary cache" in caplog.text


def test_the_schema_version_is_in_the_filename(mapping_set):
    """An index built by an older parser must not be read by a newer one."""
    KgMicrobeDict(mapping_set).load()
    names = [p.name for p in cache_dir().glob("*.sqlite")]
    assert names and all(f"-v{CACHE_SCHEMA_VERSION}-" in n for n in names)


def test_a_missing_artifact_writes_no_index(tmp_path):
    d = KgMicrobeDict(tmp_path / "absent.sssom.tsv.gz")
    assert d.size == 0
    assert not list(cache_dir().glob("*.sqlite"))


class TestCacheDir:
    def test_the_override_wins(self, tmp_path, monkeypatch):
        monkeypatch.setenv(CACHE_DIR_ENV, str(tmp_path / "here"))
        assert cache_dir() == tmp_path / "here"

    def test_xdg_is_next(self, tmp_path, monkeypatch):
        monkeypatch.delenv(CACHE_DIR_ENV, raising=False)
        monkeypatch.setenv("XDG_CACHE_HOME", str(tmp_path))
        assert cache_dir() == tmp_path / "mediaingredientmech"

    def test_the_default_is_a_dot_cache_under_home(self, monkeypatch):
        """A dot-directory cache, which the machine-path guard allows."""
        monkeypatch.delenv(CACHE_DIR_ENV, raising=False)
        monkeypatch.delenv("XDG_CACHE_HOME", raising=False)
        resolved = cache_dir()
        assert resolved.parent.name == ".cache"
        assert resolved.name == "mediaingredientmech"


def test_the_index_is_a_readable_database(mapping_set):
    """Guards the format itself, so a schema change is a deliberate act."""
    KgMicrobeDict(mapping_set).load()
    path = sorted(cache_dir().glob("*.sqlite"))[0]
    db = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    tables = {name for (name,) in db.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    assert {"entity", "synonym"} <= tables
    db.close()


def test_the_warm_path_reports_the_same_quarantine_set(tmp_path):
    """The `polluted` column is load-bearing, not decoration (self-review of #597)."""
    from mediaingredientmech.validation.kg_microbe_dict import POLLUTION_SYNONYM_THRESHOLD

    rows = [_row("kgm.name:p", "Polluted", "skos:exactMatch", "CHEBI:9", "Polluted")]
    rows += [
        _row(f"kgm.name:s{i}", f"surface form {i}", "skos:closeMatch", "CHEBI:9", "Polluted")
        for i in range(POLLUTION_SYNONYM_THRESHOLD + 1)
    ]
    path = _write_set(tmp_path / "polluted.sssom.tsv.gz", rows)

    cold = KgMicrobeDict(path)
    cold.load()
    warm = KgMicrobeDict(path)
    warm.load()

    assert warm._db is not None
    assert warm._polluted_entries == cold._polluted_entries == {"CHEBI:9"}
    assert warm.get_entry("CHEBI:9").synonyms == set()
    assert warm.lookup_synonym("surface form 3") == set()
    assert warm.lookup_synonym("Polluted") == {"CHEBI:9"}


def test_close_releases_the_index(mapping_set):
    KgMicrobeDict(mapping_set).load()
    with KgMicrobeDict(mapping_set) as d:
        assert d.size == 3
        assert d._db is not None
    assert d._db is None
