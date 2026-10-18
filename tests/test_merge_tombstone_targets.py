"""Merge tombstones must resolve to their own merge target (#799).

`docs/LABEL_INDEX_CONTRACT.md` tells consumers to follow REJECTED rows, because
a merged record's `identifier` points at its merge target. Four tombstones from
the 2026-09-21 review kept the identity the review had rejected instead, so
`NaNO` resolved to the nano unit prefix. `scripts/fix_tombstone_pointers.py`
(#360) repairs exactly that, but nothing ran it after those merges; CultureMech
refused the label index outright, which blocked its pin refresh. These tests
make MIM refuse it first.
"""

from __future__ import annotations

import contextlib
import csv
import importlib.util
import io
import re
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
_CURIE = r"([A-Za-z][\w.\-]*:[^\s,;'\"()]+)"
# Every wording a MERGED_INTO event uses for its target (#809).
MERGE_TARGET_PATTERNS = (
    re.compile(r"^Merged into " + _CURIE),
    re.compile(r"^Merged into '[^']*' on " + _CURIE),
    re.compile(r"into the existing " + _CURIE),
)


def _merge_target(text: str) -> str | None:
    for pattern in MERGE_TARGET_PATTERNS:
        match = pattern.search(text)
        if match:
            return match.group(1)
    return None


@pytest.fixture(scope="module")
def records() -> list[dict]:
    return [
        yaml.load(path.read_text(encoding="utf-8"), Loader=LOADER)
        for group in ("mapped", "unmapped")
        for path in sorted((ROOT / "data/ingredients" / group).glob("*.yaml"))
    ]


def _tombstones(records):
    for r in records:
        history = r.get("curation_history") or []
        if r.get("mapping_status") == "REJECTED" and any(
            e.get("action") == "MERGED_INTO" for e in history
        ):
            yield r, history


def test_every_merge_tombstone_points_at_a_live_record(records):
    live = {r["identifier"] for r in records if r.get("mapping_status") == "MAPPED"}
    dangling = sorted(
        (r["preferred_term"], r["identifier"])
        for r, _history in _tombstones(records)
        if not str(r["identifier"]).startswith("UNMAPPED_") and r["identifier"] not in live
    )
    assert not dangling, f"merge tombstones on an identity no live record holds: {dangling}"


def test_every_merge_tombstone_points_at_its_own_merge_target(records):
    """Liveness alone would accept a tombstone pointing at the wrong live record
    (#807). The target is the CURIE its last MERGED_INTO event names, unless a
    later REPOINTED_TOMBSTONE_IDENTIFIER event followed the winner elsewhere."""
    wrong, unparsed = [], []
    for r, history in _tombstones(records):
        target = None
        for event in history:
            text = str(event.get("changes", ""))
            if event.get("action") == "MERGED_INTO":
                target = _merge_target(text)
            elif event.get("action") == "REPOINTED_TOMBSTONE_IDENTIFIER" and " -> " in text:
                target = text.split(" -> ", 1)[1].split()[0]
        if target is None:
            unparsed.append(r["preferred_term"])
        elif target != r["identifier"]:
            wrong.append((r["preferred_term"], r["identifier"], target))
    # A new wording must be added above rather than silently skipped (#809).
    assert not unparsed, f"MERGED_INTO target not parseable: {unparsed}"
    assert not wrong, f"tombstones not on their merge target: {wrong}"


def test_no_tombstone_advertises_a_term_its_survivor_does_not_hold(records):
    """The second #360 invariant: a tombstone's ontology_id agrees with its
    survivor, so nothing indexing by ontology_id routes through a rejected term."""
    live = {r["identifier"]: r for r in records if r.get("mapping_status") == "MAPPED"}
    stale = []
    for r, _history in _tombstones(records):
        own = (r.get("ontology_mapping") or {}).get("ontology_id")
        survivor = live.get(r["identifier"])
        theirs = ((survivor or {}).get("ontology_mapping") or {}).get("ontology_id")
        if own and theirs and own != theirs:
            stale.append((r["preferred_term"], own, theirs))
    assert not stale, f"tombstones advertising a term their survivor does not hold: {stale}"


def test_published_rejected_rows_resolve_to_a_live_identifier():
    """The consumer-side check CultureMech applies to every pin (#260)."""
    with (ROOT / "docs/data/label_index.csv").open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    live = {row["identifier"] for row in rows if row["mapping_status"] == "MAPPED"}
    dangling = sorted(
        {
            row["identifier"]
            for row in rows
            if row["mapping_status"] == "REJECTED"
            and not row["identifier"].startswith("UNMAPPED_")
            and row["identifier"] not in live
        }
    )
    assert not dangling


@pytest.mark.parametrize(
    ("term", "old", "target"),
    [
        ("NaNO", "NCIT:C54713", "CHEBI:63005"),
        ("Atrazin", "cas:1924-24-9", "CHEBI:15930"),
        ("EDTA (chelating agent)", "NCIT:C360", "CHEBI:4735"),
        ("Sodium phosphate dibasic", "CHEBI:37583", "CHEBI:34683"),
    ],
)
def test_the_799_tombstones_record_what_they_used_to_assert(records, term, old, target):
    record = next(r for r in records if r["preferred_term"] == term)
    assert record["identifier"] == target
    assert record["mapping_status"] == "REJECTED"
    repoints = [
        e for e in record["curation_history"]
        if e.get("action") == "REPOINTED_TOMBSTONE_IDENTIFIER" and "(#799)" in str(e.get("changes"))
    ]
    assert len(repoints) == 1
    assert str(repoints[0]["changes"]).startswith(f"identifier {old} -> {target} ")


def test_repointer_has_nothing_left_to_do():
    """Re-running #360's repair on the committed corpus must be a no-op."""
    spec = importlib.util.spec_from_file_location(
        "fix_tombstone_pointers", ROOT / "scripts/fix_tombstone_pointers.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        module.main([])
    assert "0 identifier(s) repointed, 0 ontology_id(s) refreshed" in out.getvalue()
