"""Guards for the ChEBI currency check (issue #197).

A local ChEBI build older than kg-microbe's makes real upstream terms fail to
resolve, and `validate-products` then reports them missing. "Not in this build"
is not "not real", and six real terms were deleted on that misreading in #193.
Until #210 the CHEBI ceiling sat at 300000 — below ChEBI's own range — so those
terms were reported ID_OUT_OF_RANGE, wording that asserts "foreign identifier";
at 1000000 they report ID_NOT_FOUND, still fatal but no longer accusatory.

The tests assert STDOUT, not just exit codes. An earlier version checked only
`== 0`, which is also what the script returns when it cannot parse anything — so
if both parsers regressed to None, the tests still passed.
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


def _fake_db(tmp_path: Path, version: str | None, name: str = "chebi.db") -> Path:
    db = tmp_path / name
    con = sqlite3.connect(db)
    con.execute("create table statements (subject text, predicate text, value text)")
    if version is not None:
        con.execute(
            "insert into statements values ('obo:chebi.owl','owl:versionInfo',?)", (version,)
        )
    con.commit()
    con.close()
    return db


def _fake_owl(tmp_path: Path, body: bytes, name: str = "chebi.owl.gz") -> Path:
    p = tmp_path / name
    with gzip.open(p, "wb") as fh:
        fh.write(body)
    return p


REAL_HEADER = (
    b'<?xml version="1.0"?>\n'
    b'<rdf:RDF xmlns:a="http://purl.obolibrary.org/obo/chebi/2"\n'
    b'         xmlns:b="http://purl.obolibrary.org/obo/chebi/3"\n'
    b'         xmlns:c="http://purl.obolibrary.org/obo/chebi/1">\n'
    b'  <owl:Ontology rdf:about="http://purl.obolibrary.org/obo/chebi.owl">\n'
    b'    <owl:versionIRI rdf:resource="http://purl.obolibrary.org/obo/chebi/253/chebi.owl"/>\n'
)


def _run(mod, tmp_path, local, upstream_bytes, capsys, strict=False):
    argv = ["--local-db", str(_fake_db(tmp_path, local)),
            "--kgm-chebi", str(_fake_owl(tmp_path, upstream_bytes)),
            "--no-network"]
    if strict:
        argv.append("--strict")
    rc = mod.main(argv)
    return rc, capsys.readouterr().out


# --- version extraction ------------------------------------------------------


def test_reads_the_local_release(tmp_path):
    mod = _load()
    assert mod.local_release(_fake_db(tmp_path, "252")) == (252, "")


def test_decoy_paths_before_the_versionIRI_do_not_win(tmp_path):
    """The real header carries bare `obo/chebi/2`, `/3`, `/1` in namespace
    declarations BEFORE the versionIRI. A loose pattern reported release 2."""
    mod = _load()
    assert mod.kgmicrobe_release(_fake_owl(tmp_path, REAL_HEADER))[0] == 253


def test_a_versionIRI_pointing_at_a_subset_is_not_a_release(tmp_path):
    """The pattern requires the full `NNN/chebi.owl` form, which the comment
    claims. `.../obo/chebi/7/subsets/foo.owl` previously returned 7."""
    mod = _load()
    body = b'<owl:versionIRI rdf:resource="http://purl.obolibrary.org/obo/chebi/7/subsets/foo.owl"/>'
    assert mod.kgmicrobe_release(_fake_owl(tmp_path, body))[0] is None


def test_a_date_shaped_versionInfo_is_rejected_not_coerced(tmp_path):
    """Stripping non-digits turned '2026-08-01' into 20260801, which compares as
    hugely NEWER — a confident false OK from the one tool whose job is to prevent
    false reassurance about currency."""
    mod = _load()
    release, why = mod.local_release(_fake_db(tmp_path, "2026-08-01"))
    assert release is None
    assert "not a release integer" in why


def test_a_dotted_version_is_rejected(tmp_path):
    mod = _load()
    assert mod.local_release(_fake_db(tmp_path, "252.1"))[0] is None


def test_a_truncated_gzip_does_not_raise(tmp_path):
    """A partially-downloaded chebi.owl.gz is an ordinary state and must not
    traceback out of an advisory check — gzip raises EOFError, not OSError."""
    mod = _load()
    good = _fake_owl(tmp_path, REAL_HEADER)
    truncated = tmp_path / "cut.owl.gz"
    truncated.write_bytes(good.read_bytes()[:40])

    release, why = mod.kgmicrobe_release(truncated)
    assert release is None
    assert "unreadable" in why


# --- the two None reasons are distinguished ----------------------------------


def test_absent_and_unparseable_give_different_reasons(tmp_path):
    """Both used to print 'not readable at', sending people to look at a file
    that is sitting right there."""
    mod = _load()
    _, absent = mod.kgmicrobe_release(tmp_path / "nope.owl.gz")
    _, no_iri = mod.kgmicrobe_release(_fake_owl(tmp_path, b"<rdf:RDF/>", name="b.owl.gz"))

    assert "not found" in absent
    assert "no versionIRI" in no_iri
    assert absent != no_iri


# --- the comparison, asserting output not just exit codes --------------------


def test_current_build_reports_ok(tmp_path, capsys):
    mod = _load()
    rc, out = _run(mod, tmp_path, "253", REAL_HEADER, capsys, strict=True)
    assert rc == 0
    assert "local build = 253, kg-microbe = 253" in out
    assert "OK:" in out


def test_newer_local_build_reports_ok(tmp_path, capsys):
    """MIM may legitimately run ahead; only BEHIND is a problem."""
    mod = _load()
    rc, out = _run(mod, tmp_path, "254", REAL_HEADER, capsys, strict=True)
    assert rc == 0 and "OK:" in out


def test_behind_says_so_and_is_advisory_by_default(tmp_path, capsys):
    mod = _load()
    rc, out = _run(mod, tmp_path, "252", REAL_HEADER, capsys)
    assert rc == 0
    assert "BEHIND by 1" in out


def test_behind_fails_under_strict(tmp_path, capsys):
    mod = _load()
    rc, out = _run(mod, tmp_path, "252", REAL_HEADER, capsys, strict=True)
    assert rc == 1 and "BEHIND by 1" in out


def test_unknowable_comparison_never_fails(tmp_path, capsys):
    mod = _load()
    rc = mod.main(["--local-db", str(tmp_path / "no.db"),
                   "--kgm-chebi", str(tmp_path / "no.owl.gz"), "--strict", "--no-network"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "cannot determine" in out
    assert "no local build" in out


# --- path resolution ---------------------------------------------------------


def test_cache_dir_follows_pystow_not_home(monkeypatch, tmp_path):
    """oaklib resolves its cache through pystow, which honours PYSTOW_HOME.
    Deriving it from $HOME means a refresh deletes the wrong path — and reports
    success having downloaded nothing."""
    mod = _load()
    monkeypatch.setenv("PYSTOW_HOME", str(tmp_path))
    import pystow, importlib
    importlib.reload(pystow)
    try:
        assert str(mod.oaklib_cache_dir()).startswith(str(tmp_path))
    finally:
        monkeypatch.delenv("PYSTOW_HOME", raising=False)
        importlib.reload(pystow)


def test_kgmicrobe_default_is_a_sibling_not_a_hardcoded_home():
    """It named one developer's home directory, making the check a permanent
    silent no-op for everyone else."""
    mod = _load()
    assert "/Users/" not in str(mod.default_kgm_chebi())
    assert mod.default_kgm_chebi().parts[-4:] == ("kg-microbe", "data", "raw", "chebi.owl.gz")
