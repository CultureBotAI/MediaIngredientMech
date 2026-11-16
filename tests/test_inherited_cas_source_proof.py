"""#1439 bounded owner-proof controls; the companion fixture runs real native gates."""

import copy

import pytest

from mediaingredientmech.curate import stable_sssom_publication as publication
from tests.test_stable_id_adoption import api

TOKEN = "cas:138-86-7"
OWNER = "MIM:0000001"
PATH = "data/ingredients/unmapped/a.yaml"
HELD = "data/ingredients/mapped/held.yaml"


@pytest.fixture
def proof():
    old = api.encoded({"identifier": "UNMAPPED_1", "legacy_identifiers": [TOKEN]})
    current = api.encoded({"identifier": "UNMAPPED_1", "legacy_identifiers": []})
    pin = api.sha(current)
    operation = {
        "mim_id": OWNER,
        "before": {"path": PATH, "sha256": api.sha(old)},
        "after_path": PATH,
        "proposal": {"path": "proposal.yaml", "sha256": pin},
        "rejected_identifiers": [TOKEN],
    }
    claims = {
        "source_correction": {"path": "current-endpoint.json", "sha256": "e" * 64},
        "entries": [
            {
                "action": "RETIRE_INVALID_CAS",
                "row": {"object_id": TOKEN},
                "owner": {"mim_id": OWNER, "path": PATH, "sha256": pin},
            },
            {
                "action": "RETAIN_INVALID_CAS_WITHHOLD",
                "owner": {"mim_id": "MIM:0000003", "path": HELD, "sha256": "f" * 64},
            },
        ],
    }
    before = {PATH: api.sha(old), HELD: "f" * 64}
    after = {PATH: pin, HELD: "f" * 64}
    steps = [
        {
            "root": "/first",
            "operations": [operation],
            "before": before,
            "after": after,
            "selected_before": {OWNER: old},
        },
        {
            "root": "/second",
            "operations": [{"mim_id": "MIM:0000002"}],
            "before": copy.deepcopy(after),
            "after": copy.deepcopy(after),
            "selected_before": {},
        },
    ]
    return claims, steps


def test_current_claims_keep_actual_endpoint_binding(proof):
    claims, _ = proof
    manifest = {"cas_dispositions": {"content": claims}}
    assert publication._cas_source_claims(manifest, claims["source_correction"]) == claims
    for selected in (None, {"path": "ancestor.json", "sha256": "e" * 64}):
        with pytest.raises(ValueError, match="genuinely selected"):
            publication._cas_source_claims(manifest, selected)


def test_earlier_actual_withdrawal_and_unchanged_held_owner(proof):
    publication._cas_source_withdrawals(*proof)


@pytest.mark.parametrize(
    "attack,reason",
    [
        ("missing", "actual reviewed corrective"),
        ("unrejected", "actual reviewed corrective"),
        ("historical_mention_only", "actual reviewed corrective"),
        ("noop", "actual reviewed corrective"),
        ("later_selection", "actual reviewed corrective"),
        ("later_before", "unchanged source complement"),
        ("later_after", "postimage"),
        ("wrong_path", "postimage"),
        ("wrong_hash", "postimage"),
        ("wrong_token", "actual reviewed corrective"),
        ("held_selected", "held owner was changed"),
        ("held_before", "unchanged source complement"),
    ],
)
def test_inherited_withdrawal_never_skips_owner_or_hold_changes(proof, attack, reason):
    claims, steps = proof
    op = steps[0]["operations"][0]
    if attack == "missing":
        steps.pop(0)
    elif attack == "unrejected":
        op["rejected_identifiers"] = []
    elif attack == "historical_mention_only":
        raw = api.encoded({"notes": "Old unaccepted hypothesis " + TOKEN})
        steps[0]["selected_before"][OWNER] = raw
        steps[0]["before"][PATH] = op["before"]["sha256"] = api.sha(raw)
    elif attack == "noop":
        op["proposal"]["sha256"] = op["before"]["sha256"]
        claims["entries"][0]["owner"]["sha256"] = op["before"]["sha256"]
        for step in steps:
            step["before"][PATH] = step["after"][PATH] = op["before"]["sha256"]
    elif attack == "later_selection":
        later = copy.deepcopy(op)
        later["rejected_identifiers"] = []
        steps[1]["operations"].append(later)
        steps[1]["selected_before"][OWNER] = steps[0]["selected_before"][OWNER]
    elif attack in {"later_before", "later_after"}:
        steps[1][attack.removeprefix("later_")][PATH] = "0" * 64
    elif attack == "wrong_path":
        claims["entries"][0]["owner"]["path"] = "data/ingredients/mapped/other.yaml"
    elif attack == "wrong_hash":
        claims["entries"][0]["owner"]["sha256"] = "0" * 64
    elif attack == "wrong_token":
        claims["entries"][0]["row"]["object_id"] = "cas:89471-28-0"
    elif attack == "held_selected":
        steps[0]["operations"].append({"mim_id": "MIM:0000003"})
    elif attack == "held_before":
        steps[0]["before"][HELD] = "0" * 64
    else:
        raise AssertionError(attack)
    with pytest.raises(ValueError, match=reason):
        publication._cas_source_withdrawals(claims, steps)
