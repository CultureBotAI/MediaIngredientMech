"""#1387 replays the genuine legacy graph before crossing the stable boundary."""

import subprocess
from pathlib import Path

import pytest

from mediaingredientmech import identity_projection as identity
from mediaingredientmech.validation import current_semantic_release as current

ROOT = Path(__file__).resolve().parents[1]
# Existing independently verified historical proof, not moving current HEAD.
HISTORY = "4f57a1f3a9ed6b20d2c103c4e7f46d14c6b571f5"


@pytest.fixture(scope="module")
def historical(tmp_path_factory):
    parent = tmp_path_factory.mktemp("current-semantic-real-history")
    root = parent / "checkout"
    subprocess.run(
        ["git", "clone", "--no-hardlinks", "--dissociate", "--no-checkout", str(ROOT), str(root)],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        ["git", "-C", str(root), "checkout", "--detach", HISTORY], check=True, capture_output=True
    )
    assert not (root / ".git/objects/info/alternates").exists()
    scratch = parent / "scratch"
    scratch.mkdir()
    return root, scratch


def test_real_native_legacy_graph_chain_and_identity_projection(historical):
    root, scratch = historical
    proof = current.historical_proof(root, HISTORY, scratch)
    assert proof["result"]["integrity"] == "PASS"
    assert proof["result"]["semantic_release"] == "FAIL"
    assert proof["result"]["blocking_assertions"] > 0
    assert proof["proof"].transition["old_rows"] != proof["proof"].transition["rows"]
    assert (
        identity.sha(proof["proof"].before[identity.SOURCE])
        == "d5f76fc404967477903fafc79eaba86ecfef9e2c391926ec08c3c1af4a5220b6"
    )
    assert (
        identity.sha(proof["proof"].after[identity.SOURCE])
        == "3d9f1ac412209266034319542f225918b78b4e6a8e0658b53ee0689b4fb4dafe"
    )
    assert not list(scratch.iterdir())


def test_rehashed_or_changed_historical_receipt_is_not_a_new_baseline(historical):
    root, scratch = historical
    path = (
        root
        / "reports/sssom_completion_20260921/mapping_changes/issue669-deferred-owned-aliases.json"
    )
    before = path.read_bytes()
    try:
        path.write_bytes(before + b"\n")
        with pytest.raises(ValueError, match="historical committed bytes differ"):
            current.historical_proof(root, HISTORY, scratch)
    finally:
        path.write_bytes(before)


def test_historical_revision_cannot_follow_an_unreviewed_head(historical):
    root, scratch = historical
    with pytest.raises(ValueError, match="historical HEAD differs"):
        current.historical_proof(root, "0" * 40, scratch)
