"""No script may hardcode a path that only exists on one machine (#573).

A literal `/Users/<name>/...` runs on one laptop and, when that checkout
moves, nowhere. The same is true of `Path.home() / "Documents/..."` and
`expanduser("~/Documents/...")`, which are the same path with the prefix cut
off; claw's guard missed that shape for a month (culturebotai-claw#365), so
this one refuses it from the start. Derive paths from the file's own location
(`Path(__file__).resolve().parent.parent`) and take another checkout's root
from its fleet environment variable.

A dot-directory under home (`~/.data/oaklib`, `/Users/x/.cache`) is a tool
cache, not a checkout, and stays allowed.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]

# Both trees that ship code. `src/` was outside the guard when it was written,
# and it was where the live offender sat: the kg-microbe dictionary loader
# pointed at one laptop's home directory, which is exactly this shape
# (MediaIngredientMech#579).
CHECKED_ROOTS = (ROOT / "scripts", ROOT / "src")

# `ATTIC/` is archived, not maintained, and keeps its hardcoded paths on
# purpose. It is excluded by name rather than by living outside the globs, so
# the exemption survives someone moving it (#579).
EXCLUDED_DIRS = {"ATTIC", "__pycache__"}

_MACHINE_PATH = re.compile(
    r"""(
        /(?:Users|home)/[^/\s'"]+/(?!\.)          # /Users/name/x, not /Users/name/.cache
      | Documents/
      | Path\.home\(\)\s*/\s*['"](?!\.)          # Path.home() / "x", not / ".cache"
      | expanduser\(\s*['"]~/(?!\.)              # expanduser("~/x"), not "~/.cache"
    )""",
    re.VERBOSE,
)


def has_machine_path(source: str) -> bool:
    return _MACHINE_PATH.search(source) is not None


def _scripts() -> list[Path]:
    """Every maintained Python file, recursively, minus the archived tree."""
    return sorted(
        path
        for root in CHECKED_ROOTS
        for path in root.rglob("*.py")
        if not EXCLUDED_DIRS.intersection(path.relative_to(ROOT).parts)
    )


def test_there_are_scripts_to_check():
    """Guards the parametrization: an empty glob would pass everything."""
    assert len(_scripts()) >= 10, f"only {len(_scripts())} scripts found"


def test_both_trees_are_actually_covered():
    """`rglob` over one root would still satisfy the count check above."""
    covered = {root for root in CHECKED_ROOTS for path in _scripts() if root in path.parents}
    assert covered == set(CHECKED_ROOTS), f"only checking {sorted(str(c) for c in covered)}"


def test_nested_files_are_reached():
    """The original glob was non-recursive, so a subpackage was exempt."""
    assert any(len(p.relative_to(ROOT).parts) > 3 for p in _scripts())


@pytest.mark.parametrize(
    "snippet",
    [
        'OUTPUT_DIR = Path("/Users/someone/Documents/VIMSS/ontology/X/data")',
        "root = Path.home() / 'Documents/VIMSS/ontology/X'",
        'root = os.path.expanduser("~/Documents/X")',
        'p = "/home/someone/checkouts/X/kb"',
    ],
)
def test_the_guard_recognises_each_shape(snippet):
    """Driven by an input the guard must refuse, so a loosened regex goes red."""
    assert has_machine_path(snippet), snippet


@pytest.mark.parametrize(
    "snippet",
    [
        'CACHE = Path.home() / ".data" / "oaklib" / "chebi.db"',
        'db = os.path.expanduser("~/.cache/x.db")',
        "# see /Users/someone/.claude/plans/notes.md",
        "ROOT = Path(__file__).resolve().parent.parent",
    ],
)
def test_the_guard_allows_caches_and_derived_paths(snippet):
    assert not has_machine_path(snippet), snippet


@pytest.mark.parametrize("path", _scripts(), ids=lambda p: p.name)
def test_no_script_hardcodes_a_machine_path(path):
    assert not has_machine_path(path.read_text(encoding="utf-8")), (
        f"{path.name} embeds a path that exists on one machine; derive it from "
        f"the file's own location or take the other checkout's root from its "
        f"environment variable"
    )
