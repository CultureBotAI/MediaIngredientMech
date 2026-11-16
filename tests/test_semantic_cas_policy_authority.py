"""#1437 refuses unauthenticated executable CAS bytes before running them."""

from types import SimpleNamespace

import pytest

from mediaingredientmech import identity_projection
from mediaingredientmech.validation import semantic_transition as transition
from tests.test_semantic_transition_cas import CURRENT_POLICY, OLD_POLICY


@pytest.mark.parametrize("approved", [OLD_POLICY, CURRENT_POLICY])
@pytest.mark.parametrize("attack", ["rehashed", "wrong_raw", "snapshot"])
def test_untrusted_policy_is_rejected_before_its_top_level_code(approved, attack):
    raw = b'raise RuntimeError("UNAUTHENTICATED_CAS_POLICY_EXECUTED")\n'
    declared = identity_projection.sha(raw) if attack == "rehashed" else approved
    snapshot = declared
    if attack == "snapshot":
        snapshot = "0" * 64
    root = "/synthetic-captured-claw"
    name = "src/kg_microbe_utils/stable_mim.py"
    absolute = root + "/" + name
    seen = []

    def read(actual_root, ref):
        seen.append((actual_root, ref))
        assert actual_root == root
        assert ref == {"path": name, "sha256": declared}
        return raw

    generation = {
        "cas_dispositions": {"path": "never-read-request.json", "sha256": "1" * 64},
        "claw": {"root": root, "files": {absolute: declared}},
    }
    manifest = {
        "cas_dispositions": {},
        "producer_import_snapshot": {absolute: snapshot},
    }
    reason = (
        "CAS producer binding differs" if attack == "snapshot" else "reviewed adapter authority"
    )
    # No native dependency is mocked: the actual _cas boundary must refuse
    # before either the sentinel or the deliberately absent later inputs.
    with pytest.raises(ValueError, match=reason):
        transition._cas(
            SimpleNamespace(read=read), "/synthetic-root", generation, manifest, b"", [], {}, {}
        )
    assert len(seen) == (0 if attack == "snapshot" else 1)
