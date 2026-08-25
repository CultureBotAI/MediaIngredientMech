"""`just curie-validate` must read the artifact, not just the normalizer (#439).

The recipe was documented as "Assert the published SSSOM satisfies the CURIE
standard" while running only `pytest tests/test_curie_normalizer.py`. It passed
19/19 on 2026-08-21 against a published file with 11 subjects violating
`curie.py`'s own `_CURIE_RE` -- the very pattern those tests exercise.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_SPEC = importlib.util.spec_from_file_location(
    "validate_published_curies", ROOT / "scripts" / "validate_published_curies.py"
)
checker = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = checker
_SPEC.loader.exec_module(checker)


def test_the_published_set_is_clean():
    rows = checker.read_rows(checker.DEFAULT_SSSOM)

    assert rows, "fixture: the published SSSOM has rows"
    assert checker.check(rows) == []


def test_an_unescaped_paren_is_caught():
    """The exact shape that shipped: `MIM:(R)-lactate`."""
    bad = checker.check([{"subject_id": "MIM:(R)-lactate", "object_id": "CHEBI:16004"}])

    assert len(bad) == 1
    assert bad[0][1] == "subject_id"
    assert "_CURIE_RE" in bad[0][3]


def test_the_escaped_form_of_the_same_subject_passes():
    assert checker.check(
        [{"subject_id": "MIM:~28R~29-lactate", "object_id": "CHEBI:16004"}]
    ) == []


def test_an_unknown_prefix_is_caught():
    bad = checker.check([{"subject_id": "MIM:Thing", "object_id": "NOTAPREFIX:1"}])

    assert len(bad) == 1
    assert "unrecognised prefix" in bad[0][3]


def test_an_empty_cell_is_caught():
    bad = checker.check([{"subject_id": "MIM:Thing", "object_id": ""}])

    assert [b[3] for b in bad] == ["empty"]


def test_every_object_prefix_in_use_is_recognised():
    """A prefix the artifact uses but PREFIX_RANK lacks would make the check
    fail for the wrong reason -- pin that the table is complete."""
    rows = checker.read_rows(checker.DEFAULT_SSSOM)
    in_use = {r["object_id"].split(":", 1)[0] for r in rows if ":" in r["object_id"]}

    assert in_use <= checker.KNOWN_PREFIXES, sorted(in_use - checker.KNOWN_PREFIXES)
