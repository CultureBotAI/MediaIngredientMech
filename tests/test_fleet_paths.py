"""Reading a sibling checkout's root from its fleet environment variable (#580).

Two values slip past `os.environ.get(var, default)`: an exported-but-empty
one, which becomes `Path("")` and therefore the working directory, and a
`~`-prefixed one, which becomes a literal directory named `~`. Both fail
quietly -- the script reads a file that is not there rather than saying so.

The last test is the one that matters over time: it refuses the fragile shape
anywhere in the repository, so this cannot be reintroduced by the next script
that needs a sibling checkout.
"""

from __future__ import annotations

import logging
import re
from pathlib import Path

import pytest

from mediaingredientmech.utils.fleet_paths import checkout_root

ROOT = Path(__file__).resolve().parents[1]
CHECKED_ROOTS = (ROOT / "scripts", ROOT / "src")
EXCLUDED_DIRS = {"ATTIC", "__pycache__"}
# fleet_paths.py quotes the fragile shape in its own docstring, as the thing it
# exists to replace. Excluding it by name keeps that explanation readable
# without weakening the pattern for everyone else.
EXCLUDED_FILES = {"fleet_paths.py"}

VAR = "MIM_TEST_CHECKOUT_ROOT"
FALLBACK = Path("/fallback/CultureMech")


def test_a_set_variable_wins(monkeypatch):
    monkeypatch.setenv(VAR, "/somewhere/CultureMech")
    assert checkout_root(VAR, FALLBACK) == Path("/somewhere/CultureMech")


def test_an_unset_variable_falls_back(monkeypatch):
    monkeypatch.delenv(VAR, raising=False)
    assert checkout_root(VAR, FALLBACK) == FALLBACK


@pytest.mark.parametrize("blank", ["", " ", "\t", "\n"])
def test_an_exported_but_empty_variable_falls_back(monkeypatch, blank):
    """`Path("")` is `.`, so the fragile form silently reads the working directory."""
    monkeypatch.setenv(VAR, blank)
    assert checkout_root(VAR, FALLBACK) == FALLBACK


def test_a_tilde_value_is_expanded(monkeypatch):
    monkeypatch.setenv(VAR, "~/checkouts/CultureMech")
    resolved = checkout_root(VAR, FALLBACK)
    assert "~" not in str(resolved)
    assert resolved == Path.home() / "checkouts" / "CultureMech"


def test_surrounding_whitespace_is_stripped(monkeypatch):
    """A trailing newline is what a `$(...)` capture in a wrapper leaves behind."""
    monkeypatch.setenv(VAR, "  /somewhere/CultureMech\n")
    assert checkout_root(VAR, FALLBACK) == Path("/somewhere/CultureMech")


def test_a_tilde_fallback_is_expanded_too(monkeypatch):
    monkeypatch.delenv(VAR, raising=False)
    assert checkout_root(VAR, Path("~/CultureMech")) == Path.home() / "CultureMech"


def test_existence_is_not_required(monkeypatch, tmp_path):
    """Callers report a missing checkout in their own terms; this only resolves."""
    missing = tmp_path / "nope"
    monkeypatch.setenv(VAR, str(missing))
    assert checkout_root(VAR, FALLBACK) == missing


# `Path(os.environ.get("X", default))` -- the shape that swallows an empty value.
_FRAGILE = re.compile(
    r"""Path\(\s*os\.environ\.get\(\s*['"][A-Z0-9_]+['"]\s*,""",
    re.VERBOSE,
)


def _python_files() -> list[Path]:
    return sorted(
        path
        for root in CHECKED_ROOTS
        for path in root.rglob("*.py")
        if not EXCLUDED_DIRS.intersection(path.relative_to(ROOT).parts)
        and path.name not in EXCLUDED_FILES
    )


def test_the_guard_recognises_the_fragile_shape():
    """Driven by the literal defect, so a loosened pattern goes red on its own."""
    assert _FRAGILE.search(
        'CULTUREMECH_ROOT = Path(os.environ.get("CULTUREMECH_ROOT", REPO_ROOT.parent / "X"))'
    )


@pytest.mark.parametrize(
    "snippet",
    [
        'value = os.environ.get("CULTUREMECH_ROOT")',  # no default: caller must branch
        'root = checkout_root("CULTUREMECH_ROOT", REPO_ROOT.parent / "CultureMech")',
        'name = os.environ.get("USER", "nobody")',  # not a path
    ],
)
def test_the_guard_allows_the_safe_forms(snippet):
    assert not _FRAGILE.search(snippet)


@pytest.mark.parametrize("path", _python_files(), ids=lambda p: p.name)
def test_no_module_builds_a_path_from_environ_get_with_a_default(path):
    assert not _FRAGILE.search(path.read_text(encoding="utf-8")), (
        f"{path.name} wraps os.environ.get(..., default) in Path(): an exported-but-empty "
        f"value resolves to the working directory. Use "
        f"mediaingredientmech.utils.fleet_paths.checkout_root instead (#580)"
    )


class TestDeprecatedNames:
    """One checkout, two variable names — the standard one must win (#593)."""

    OLD = "MIM_TEST_CHECKOUT_DIR"

    def test_the_standard_name_wins_when_both_are_set(self, monkeypatch, caplog):
        monkeypatch.setenv(VAR, "/new/CultureMech")
        monkeypatch.setenv(self.OLD, "/old/CultureMech")
        with caplog.at_level(logging.WARNING):
            assert checkout_root(VAR, FALLBACK, deprecated=(self.OLD,)) == Path(
                "/new/CultureMech"
            )
        assert caplog.text == ""  # nothing was ignored, so nothing to say

    def test_the_deprecated_name_still_works_and_warns(self, monkeypatch, caplog):
        """It is documented in docs/WORKFLOWS.md, so it cannot just stop working."""
        monkeypatch.delenv(VAR, raising=False)
        monkeypatch.setenv(self.OLD, "/old/CultureMech")
        with caplog.at_level(logging.WARNING):
            assert checkout_root(VAR, FALLBACK, deprecated=(self.OLD,)) == Path(
                "/old/CultureMech"
            )
        assert self.OLD in caplog.text
        assert VAR in caplog.text

    def test_an_empty_deprecated_name_is_skipped(self, monkeypatch):
        monkeypatch.delenv(VAR, raising=False)
        monkeypatch.setenv(self.OLD, "")
        assert checkout_root(VAR, FALLBACK, deprecated=(self.OLD,)) == FALLBACK

    def test_neither_set_falls_back_without_warning(self, monkeypatch, caplog):
        monkeypatch.delenv(VAR, raising=False)
        monkeypatch.delenv(self.OLD, raising=False)
        with caplog.at_level(logging.WARNING):
            assert checkout_root(VAR, FALLBACK, deprecated=(self.OLD,)) == FALLBACK
        assert caplog.text == ""

    def test_a_deprecated_value_is_expanded_too(self, monkeypatch):
        monkeypatch.delenv(VAR, raising=False)
        monkeypatch.setenv(self.OLD, "~/CultureMech")
        assert checkout_root(VAR, FALLBACK, deprecated=(self.OLD,)) == (
            Path.home() / "CultureMech"
        )
