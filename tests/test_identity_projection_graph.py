"""#1265 graph proof keeps OPEN assertions and all scientific content unchanged."""
from pathlib import Path

import pytest

from mediaingredientmech import identity_projection as ip
from mediaingredientmech import identity_projection_graph as graph

ROOT = Path(__file__).resolve().parents[1]


def identities():
    old = [{"assertion_id": "old1", "source_record": "owner", "source_record_sha256": "oldhash",
            "assertion_type": "role", "source_position": "1", "assertion_sha256": "samebiology"},
           {"assertion_id": "old2", "source_record": "mapping", "source_record_sha256": "oldmap",
            "assertion_type": "mapping", "source_position": "2", "assertion_sha256": "oldaddress"}]
    new = [dict(old[0], source_record_sha256="newhash"),
           dict(old[1], assertion_id="new2", source_record_sha256="newmap", assertion_sha256="newaddress")]
    decisions = [dict(old[0], resolution_status="OPEN", review_evidence="", review_reason="Missing evidence"),
                 dict(old[1], resolution_status="APPROVED", review_evidence="original-evidence", review_reason="Exact review")]
    return old, new, decisions


def test_identity_projection_never_promotes_negative_disposition():
    old, new, decisions = identities()
    result = graph.project_decisions(old, new, decisions)
    assert result[0]["resolution_status"] == "OPEN"
    assert result[1]["resolution_status"] == "APPROVED"
    for before, after, identity in zip(decisions, result, new, strict=True):
        assert after == dict(before, **identity)


@pytest.mark.parametrize("attack", ["missing", "duplicate", "stale_owner", "stale_payload", "unknown_status"])
def test_graph_review_projection_requires_exact_preexisting_authority(attack):
    old, new, decisions = identities()
    if attack == "missing":
        decisions.pop()
    elif attack == "duplicate":
        decisions.append(decisions[0])
    elif attack == "stale_owner":
        decisions[0]["source_record_sha256"] = "different"
    elif attack == "stale_payload":
        decisions[0]["assertion_sha256"] = "different"
    else:
        decisions[0]["resolution_status"] = "PASSED"
    with pytest.raises(ValueError, match="Identity projection"):
        graph.project_decisions(old, new, decisions)


def test_current_semantic_successor_preserves_full_negative_verdict_and_holds():
    old = ip.document((ROOT / graph.OLD_REVIEW).read_bytes())
    new = ip.document((ROOT / graph.REVIEW).read_bytes())
    assert ip.sha((ROOT / graph.OLD_REVIEW).read_bytes()) == graph.OLD_REVIEW_SHA
    assert old["release_verdict"] == new["release_verdict"] == "FAIL"
    assert new["blocking_finding_ids"] == old["blocking_finding_ids"]
    assert new["evidence_gaps"] == old["evidence_gaps"]
    assert new["inherited_release_holds"] == old["release_holds"]
    before = graph.read_table((ROOT / old["assertion_dispositions"]).read_bytes())
    after = graph.read_table((ROOT / new["assertion_dispositions"]).read_bytes())
    assert len(before) == len(after) == 4519
    for left, right in zip(before, after, strict=True):
        for key in ("resolution_status", "review_reason", "review_evidence", "source_record", "source_position", "assertion_type"):
            assert left[key] == right[key]
    assert sum(row["resolution_status"] == "OPEN" for row in after) == len(new["blocking_assertion_ids"]) > 0


def test_complete_graph_and_negative_review_replay_against_fixed_baseline(tmp_path):
    # #1281 (2026-11-08): CI has no ignored output/mim-kgx-710-full bundle.
    # Share only immutable Git objects, then copy the declared current inputs.
    # Native generation and all proof/path/recheck calls run without mocks.
    import subprocess

    from mediaingredientmech.export.kgx import export_graph

    root = tmp_path / "repository"
    subprocess.run(
        ["git", "clone", "--shared", "--no-checkout", "--quiet", str(ROOT), str(root)],
        check=True, capture_output=True,
    )
    original = ip.document((ROOT / graph.OLD_REVIEW).read_bytes())
    inputs = {
        *ip.record_paths(ROOT), ip.MANIFEST, ip.SOURCE, ip.REGISTRY, ip.LIFECYCLE,
        graph.OLD_REVIEW,
        *(f"data/curated/{group}_ingredients.yaml" for group in ("mapped", "unmapped")),
        *(graph.ARCHIVE + name + ".gz" for name in graph.GRAPH_FILES),
        *(name for name in original["inputs"] if name.startswith("reports/")),
        *(name for name in original["record_inputs"] if name.startswith("reports/")),
    }

    def copy_input(name):
        target = ip.safe_path(root, name)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(ip.safe_path(ROOT, name).read_bytes())

    for name in sorted(inputs):
        copy_input(name)
    isolated_bundle = root / graph.BUNDLE
    assert not isolated_bundle.exists()
    manifest = export_graph(root, isolated_bundle)
    assert set(manifest["inputs"]) <= inputs
    for name in manifest["implementation"]:
        copy_input("src/mediaingredientmech/" + name)

    proof = ip.prove_identity_migration(root)
    outputs = graph.products(proof)
    assert outputs[graph.REVIEW] == (ROOT / graph.REVIEW).read_bytes()
    assert outputs[graph.DISPOSITIONS] == (ROOT / graph.DISPOSITIONS).read_bytes()
    assert len(outputs) == 6
