"""Guards for the ChEBI currency check (issue #197).

A local ChEBI build older than kg-microbe's makes real upstream terms fail to
resolve, and `validate-products` then reports them ID_OUT_OF_RANGE — wording that
says "foreign identifier" and invites deleting a valid mapping. Six real terms
(polymyxin B, colistin sulfate, gentamicin, netilmicin, carbomycin, lysostaphin)
were demoted exactly that way in #193 while the local build sat one release
behind.
"""

import gzip
import importlib.util
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent


def _load():
    spec = importlib.util.spec_from_file_location(
        "check_chebi_currency", ROOT / "scripts" / "check_chebi_currency.py"
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def _fake_db(tmp_path: Path, release: str | None) -> Path:
    db = tmp_path / "chebi.db"
    con = sqlite3.connect(db)
    con.execute("create table statements (subject text, predicate text, value text)")
    if release is not None:
        con.execute(
            "insert into statements values ('obo:chebi.owl','owl:versionInfo',?)", (release,)
        )
    con.commit()
    con.close()
    return db


def _fake_owl(tmp_path: Path, body: bytes) -> Path:
    p = tmp_path / "chebi.owl.gz"
    with gzip.open(p, "wb") as fh:
        fh.write(body)
    return p


REAL_HEADER = (
    b'<?xml version="1.0"?>\n<rdf:RDF xmlns="http://purl.obolibrary.org/obo/chebi/">\n'
    b'  <owl:Ontology rdf:about="http://purl.obolibrary.org/obo/chebi.owl">\n'
    b'    <owl:versionIRI rdf:resource="http://purl.obolibrary.org/obo/chebi/253/chebi.owl"/>\n'
)


# --- version extraction ------------------------------------------------------


def test_reads_the_local_release(tmp_path):
    mod = _load()
    assert mod.local_release(_fake_db(tmp_path, "252")) == 252


def test_missing_local_db_is_not_an_error(tmp_path):
    mod = _load()
    assert mod.local_release(tmp_path / "nope.db") is None


def test_local_db_without_a_version_is_not_an_error(tmp_path):
    mod = _load()
    assert mod.local_release(_fake_db(tmp_path, None)) is None


def test_reads_kgmicrobe_release_from_the_versionIRI(tmp_path):
    mod = _load()
    assert mod.kgmicrobe_release(_fake_owl(tmp_path, REAL_HEADER)) == 253


def test_decoy_paths_before_the_versionIRI_do_not_win(tmp_path):
    """The real file contains bare `obo/chebi/2`, `/3` and `/1` in namespace
    declarations BEFORE the versionIRI. A loose `obo/chebi/(\\d+)` matched the
    first of those and silently reported release 2."""
    mod = _load()
    body = (
        b'<rdf:RDF xmlns:a="http://purl.obolibrary.org/obo/chebi/2"\n'
        b'         xmlns:b="http://purl.obolibrary.org/obo/chebi/3"\n'
        b'         xmlns:c="http://purl.obolibrary.org/obo/chebi/1">\n' + REAL_HEADER
    )
    assert mod.kgmicrobe_release(_fake_owl(tmp_path, body)) == 253


def test_missing_kgmicrobe_file_is_not_an_error(tmp_path):
    mod = _load()
    assert mod.kgmicrobe_release(tmp_path / "nope.owl.gz") is None


# --- the comparison ----------------------------------------------------------


def _run(mod, tmp_path, local, upstream, strict=False):
    argv = ["--local-db", str(_fake_db(tmp_path, local)),
            "--kgm-chebi", str(_fake_owl(tmp_path, upstream))]
    if strict:
        argv.append("--strict")
    return mod.main(argv)


def test_current_build_passes(tmp_path):
    mod = _load()
    assert _run(mod, tmp_path, "253", REAL_HEADER, strict=True) == 0


def test_newer_local_build_passes(tmp_path):
    """MIM may legitimately run ahead of kg-microbe; only BEHIND is a problem."""
    mod = _load()
    assert _run(mod, tmp_path, "254", REAL_HEADER, strict=True) == 0


def test_behind_is_advisory_by_default(tmp_path):
    """A multi-GB developer cache must not fail a build, or the check gets skipped."""
    mod = _load()
    assert _run(mod, tmp_path, "252", REAL_HEADER) == 0


def test_behind_fails_under_strict(tmp_path):
    mod = _load()
    assert _run(mod, tmp_path, "252", REAL_HEADER, strict=True) == 1


def test_unknowable_comparison_never_fails(tmp_path, capsys):
    """Neither side present is 'cannot tell', not 'broken' — this runs on
    developer machines where kg-microbe may not be checked out."""
    mod = _load()
    assert mod.main(["--local-db", str(tmp_path / "no.db"),
                     "--kgm-chebi", str(tmp_path / "no.owl.gz"), "--strict"]) == 0
    assert "nothing to compare" in capsys.readouterr().out
