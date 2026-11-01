"""Provenance restoration must preserve the bounded nine-row scientific patch."""

import csv
import importlib.util
import json
from copy import deepcopy
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "restore_provenance", ROOT / "scripts/restore_carnitine_mapping_provenance.py"
)
restore = importlib.util.module_from_spec(spec)
spec.loader.exec_module(restore)


def rows(data):
    return list(csv.DictReader(
        (line for line in data.decode().splitlines() if not line.startswith("#")), delimiter="\t"
    ))


@pytest.fixture
def proposal():
    """Build a frozen preimage from the immutable receipt, never the live TSV."""
    prior = json.loads((ROOT / restore.PRIOR).read_text())
    before_rows = [dict(c["after"]) for c in prior["changes"]]
    header = list(before_rows[0])
    data = ("# fixture: frozen-nine-row-patch\n" + "\t".join(header) + "\n" +
            "".join("\t".join(r[k] for k in header) + "\n" for r in before_rows)).encode()
    for pos, change in enumerate(prior["changes"], 1):
        change["after_position"] = change["before_position"] = pos
    prior["after_row_count"] = len(before_rows)
    prior["after_sha256"] = restore.digest(data)
    return prior, data


def test_restores_old_sources_and_390_comment_without_reverting_aliases_or_dates(proposal):
    prior, data = proposal
    after = rows(restore.restore_provenance(data, prior))
    before = rows(data)
    changed = []
    for pos, (old, new, correction) in enumerate(zip(before, after, prior["changes"], strict=True), 1):
        if old["subject_id"] == restore.SUBJECT:
            assert new["source"] == correction["before"]["source"]
            assert new["comment"] == correction["before"]["comment"]
            assert "manifest=" not in new["source"]
            assert {k for k in old if old[k] != new[k]} <= {"source", "comment"}
            assert new["other"] == old["other"]
            assert new["mapping_date"] == old["mapping_date"]
            changed.append(pos)
        else:
            assert new == old
        # Every originally intended row still differs from its pre-correction row.
        assert new != correction["before"]
    assert len(changed) == 2
    parent = next(r for r in after if r["subject_id"] == restore.SUBJECT and r["object_id"] == "CHEBI:17126")
    assert "[#390 " in parent["comment"]
    assert parent["other"] == "DL-carnitine"


def test_rejects_unreviewed_preimage(proposal):
    prior, data = proposal
    with pytest.raises(ValueError, match="Canonical bytes differ"):
        restore.restore_provenance(data + b"\n", prior)


def test_rejects_receipt_row_tampering_even_if_file_hash_is_valid(proposal):
    prior, data = proposal
    changed = deepcopy(prior)
    next(c for c in changed["changes"] if c["after"]["subject_id"] == restore.SUBJECT)["after"]["confidence"] = "0"
    with pytest.raises(ValueError, match="differs from receipt preimage"):
        restore.restore_provenance(data, changed)


def test_restore_preserves_crlf_and_unmodified_bytes(proposal):
    prior, data = proposal
    data = data.replace(b"\n", b"\r\n")
    prior["after_sha256"] = restore.digest(data)
    restored = restore.restore_provenance(data, prior)
    assert restored.count(b"\r\n") == data.count(b"\r\n")
    assert len([1 for old, new in zip(data.splitlines(), restored.splitlines(), strict=True) if old != new]) == 2
