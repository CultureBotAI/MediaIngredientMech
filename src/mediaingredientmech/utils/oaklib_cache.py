"""Where oaklib actually caches its sqlite builds (#306).

`~/.data/oaklib` is oaklib's *default*, not its location. oaklib resolves the
cache through pystow, which honours ``PYSTOW_HOME``, so a developer who has set
it gets a different directory — and a script that derives the path from ``$HOME``
reads somewhere no build exists.

That is worse than a missing file, because of what the caller then reports.
`promote_microbedecoder_residual.canonical_label` raises
``SystemExit(f"{cid} has no rdfs:label (absent / wrong id)")`` when the lookup
returns nothing, so a path problem is announced as a verdict about the
identifier. #197 is what that costs: a tool stating a confident wrong conclusion
about an id led someone to demote 17 valid terms.

Seven scripts derived this path by hand, in three spellings
(``Path.home() / ".data/oaklib"``, ``expanduser("~/.data/oaklib/x.db")``, and an
f-string sqlite URL). This is the one rule they now share.

Note this is a different question from #573's machine-independence guard, which
deliberately *allows* a dot-directory under home as "a tool cache, not a
checkout". Such a path is portable and still wrong: portability asks whether it
runs on another machine, this asks whether it is where oaklib put the data.
"""

from __future__ import annotations

import os
from pathlib import Path

__all__ = ["OAK_DB_ENV", "db_path", "oaklib_cache_dir"]

#: Per-prefix override, e.g. ``OAK_CHEBI_DB``. Checked before the cache dir so a
#: caller can point one ontology at a build without relocating the whole cache.
OAK_DB_ENV = "OAK_{prefix}_DB"


def oaklib_cache_dir() -> Path:
    """
    Return the directory oaklib caches its sqlite builds in.

    Resolved through pystow, which oaklib itself uses (``oaklib/constants.py``),
    so this honours ``PYSTOW_HOME``. Falls back to oaklib's documented default
    when pystow is absent or refuses, because a wrong-but-conventional path is a
    better failure than an import error in a curation script.

    :return: The cache directory, which is not guaranteed to exist.
    """
    try:
        import pystow

        return Path(pystow.module("oaklib").base)
    except Exception:
        return Path.home() / ".data" / "oaklib"


def db_path(prefix: str) -> Path:
    """
    Return the semsql build path for one ontology prefix.

    :param prefix: An ontology prefix such as ``CHEBI`` — case-insensitive.
    :return: ``<cache>/<prefix lowercased>.db``, or the per-prefix env override.
    """
    override = os.environ.get(OAK_DB_ENV.format(prefix=prefix.upper()))
    if override:
        return Path(override)
    return oaklib_cache_dir() / f"{prefix.lower()}.db"


def require_db(prefix: str) -> Path:
    """
    Return the build path for `prefix`, or exit naming the path that was tried.

    The point is the message. Callers that let a missing build fall through to a
    label lookup report "no rdfs:label (absent / wrong id)", which blames the
    identifier for a path problem (#306, #197).

    :param prefix: An ontology prefix such as ``CHEBI``.
    :return: An existing build path.
    :raises SystemExit: When no build exists at the resolved path.
    """
    path = db_path(prefix)
    if path.is_file():
        return path
    raise SystemExit(
        f"No {prefix.upper()} semsql build at {path}.\n"
        f"  This is a missing or misconfigured cache, not a bad identifier.\n"
        f"  The cache directory resolves through pystow (PYSTOW_HOME"
        f"{'=' + os.environ['PYSTOW_HOME'] if os.environ.get('PYSTOW_HOME') else ' unset'}).\n"
        f"  Build it with `runoak -i sqlite:obo:{prefix.lower()} info {prefix.upper()}:0000000`, "
        f"or point {OAK_DB_ENV.format(prefix=prefix.upper())} at an existing file."
    )
