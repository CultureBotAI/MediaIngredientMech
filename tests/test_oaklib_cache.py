"""One rule for where oaklib's sqlite builds live (#306).

`~/.data/oaklib` is oaklib's default, not its location: oaklib resolves the
cache through pystow, which honours PYSTOW_HOME. Fifteen scripts derived the
path by hand in three spellings, so a developer with PYSTOW_HOME set read a
directory with no builds in it.

The cost is the diagnosis, not the read. `canonical_label` raises
"{cid} has no rdfs:label (absent / wrong id)" when the lookup comes back empty,
so a path problem is announced as a verdict about the identifier — the #197
failure mode that led to 17 valid terms being demoted.
"""

from __future__ import annotations

import importlib
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from mediaingredientmech.utils import oaklib_cache  # noqa: E402


@pytest.fixture
def pystow_home(monkeypatch, tmp_path):
    """Point pystow at a temp root, as a developer with PYSTOW_HOME would."""
    monkeypatch.setenv("PYSTOW_HOME", str(tmp_path))
    import pystow

    importlib.reload(pystow)
    yield tmp_path
    monkeypatch.delenv("PYSTOW_HOME", raising=False)
    importlib.reload(pystow)


def test_the_cache_dir_follows_pystow_home(pystow_home):
    assert str(oaklib_cache.oaklib_cache_dir()).startswith(str(pystow_home))


def test_db_path_lands_inside_the_resolved_cache(pystow_home):
    assert str(oaklib_cache.db_path("CHEBI")).startswith(str(pystow_home))
    assert oaklib_cache.db_path("CHEBI").name == "chebi.db"


def test_the_prefix_is_lowercased_for_the_filename():
    assert oaklib_cache.db_path("NCIT").name == "ncit.db"
    assert oaklib_cache.db_path("ncit").name == "ncit.db"


def test_a_per_prefix_override_wins(monkeypatch, tmp_path):
    """So one ontology can point at a build without relocating the cache."""
    target = tmp_path / "custom.db"
    monkeypatch.setenv("OAK_CHEBI_DB", str(target))
    assert oaklib_cache.db_path("CHEBI") == target
    assert oaklib_cache.db_path("NCIT") != target


def test_the_fallback_is_oaklibs_documented_default(monkeypatch):
    """pystow missing must not break a curation script at import time."""
    real_import = __builtins__["__import__"] if isinstance(__builtins__, dict) else __builtins__.__import__

    def refuse(name, *args, **kwargs):
        if name == "pystow":
            raise ImportError("no pystow")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr("builtins.__import__", refuse)
    assert oaklib_cache.oaklib_cache_dir() == Path.home() / ".data" / "oaklib"


def test_require_db_blames_the_path_not_the_identifier(pystow_home):
    """The whole point of #306: the message must not read as a verdict on an id."""
    with pytest.raises(SystemExit) as excinfo:
        oaklib_cache.require_db("CHEBI")
    message = str(excinfo.value)
    assert "not a bad identifier" in message
    assert str(pystow_home) in message, "the message must name the path actually tried"
    assert "PYSTOW_HOME" in message


def test_require_db_returns_an_existing_build(tmp_path, monkeypatch):
    build = tmp_path / "chebi.db"
    build.write_bytes(b"")
    monkeypatch.setenv("OAK_CHEBI_DB", str(build))
    assert oaklib_cache.require_db("CHEBI") == build


def test_check_chebi_currency_delegates_rather_than_keeping_a_second_copy(pystow_home):
    """It is stdlib-only and imported via sys.path from the justfile, so it takes
    the bootstrap rather than a bare package import -- but it must not re-derive."""
    import check_chebi_currency

    importlib.reload(check_chebi_currency)
    assert str(check_chebi_currency.oaklib_cache_dir()).startswith(str(pystow_home))


def test_no_script_derives_the_oaklib_cache_by_hand():
    """Regression guard. Fifteen scripts had three spellings of this; a plain
    `.data/oaklib` grep misses `Path.home() / ".data" / "oaklib"` entirely, which
    is how the first scope check for #306 under-counted it."""
    pattern = re.compile(r"""(Path\.home\(\)|expanduser\()[^\n]*oaklib""")
    offenders = []
    for directory in ("scripts", "src"):
        for path in (ROOT / directory).rglob("*.py"):
            if path.name == "oaklib_cache.py":
                continue  # the one legitimate home, including its fallback
            for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                if pattern.search(line):
                    offenders.append(f"{path.relative_to(ROOT)}:{number}")
    assert not offenders, f"derive these through oaklib_cache.db_path(): {offenders}"


def test_canonical_label_blames_the_cache_not_the_identifier(monkeypatch, tmp_path):
    """#306's actual harm: a path problem reported as a verdict about an id (#687)."""
    import importlib

    monkeypatch.setenv("OAK_CHEBI_DB", str(tmp_path / "absent.db"))
    module = importlib.import_module("promote_microbedecoder_residual")
    importlib.reload(module)

    with pytest.raises(SystemExit) as excinfo:
        module.canonical_label("CHEBI:17234")
    message = str(excinfo.value)
    assert "not a bad identifier" in message
    assert "no rdfs:label" not in message, "this is the verdict that must not be reached"


def test_opening_a_missing_build_does_not_create_one(monkeypatch, tmp_path):
    """`sqlite3.connect(path)` creates the file, which is how a 0-byte stub is
    born; the guard must fire before any connect happens (#687)."""
    import importlib

    ghost = tmp_path / "ghost.db"
    monkeypatch.setenv("OAK_CHEBI_DB", str(ghost))
    module = importlib.import_module("anchor_cas_hydrate_records")
    importlib.reload(module)

    with pytest.raises(SystemExit) as excinfo:
        module.chebi_label("CHEBI:17234")
    assert "not a bad identifier" in str(excinfo.value)
    assert not ghost.exists(), "a missing build must not be created by opening it"
