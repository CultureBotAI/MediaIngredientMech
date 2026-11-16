"""Cheap #1439 prestate checks, independent of the full native chain fixture."""

from __future__ import annotations

import copy
import json
from types import SimpleNamespace

import pytest

from tests import test_inherited_cas_source_chain as chain


@pytest.fixture
def originals():
    return [
        {
            "identifier": "NCIT:C80300",
            "preferred_term": "Exact",
            "mapping_status": "MAPPED",
            "curation_history": [],
        },
        {
            "identifier": "UNMAPPED_1",
            "preferred_term": "Move",
            "mapping_status": "UNMAPPED",
            "synonyms": [{"synonym_text": "Raw Move", "synonym_type": "RAW_TEXT"}],
            "curation_history": [],
        },
    ]


def test_real_initial_mint_derives_cas_alias_without_changing_science(originals):
    untouched = copy.deepcopy(originals)
    records = chain._cas_originals(originals)
    before = copy.deepcopy(records)
    witnesses = chain._initial_mint_witnesses(records)
    assert originals == untouched and records == before
    assert records[1]["identifier"] == chain.RETIRED
    assert records[1]["mapping_status"] == "UNMAPPED"
    assert "ontology_mapping" not in records[1]
    assert all("mim_id" not in r and "legacy_identifiers" not in r for r in records)
    assert witnesses[1]["mim_id"] == "MIM:0000002"
    assert witnesses[1]["legacy_identifiers"] == ["MIM:Move", chain.RETIRED]
    for original, minted in zip(records, witnesses, strict=True):
        chain._assert_mint_projection(original, minted, minted)


@pytest.mark.parametrize(
    "field,value",
    [
        ("legacy_identifiers", [chain.RETIRED]),
        ("legacy_identifiers", []),
        ("legacy_identifiers", None),
        ("mim_id", "MIM:0000002"),
        ("mim_id", None),
    ],
)
def test_already_minted_prestate_refused_before_original_constructor(
    tmp_path, monkeypatch, originals, field, value
):
    originals[1][field] = value
    constructor_calls = []

    def forbidden_constructor(*args, **kwargs):
        constructor_calls.append((args, kwargs))
        pytest.fail("Invalid pre-ID input reached the original fixture constructor")

    def enter_customized_constructor(*args, **kwargs):
        return chain.fixtures.NativeReviewAdoptionFixture(
            tmp_path, monkeypatch, original_records=originals
        )

    # Only fixture entry points are observed; the real migrate_record guard runs.
    monkeypatch.setattr(
        chain.fixtures.NativeReviewAdoptionFixture, "__init__", forbidden_constructor
    )
    monkeypatch.setattr(chain, "SuccessorFixture", enter_customized_constructor)
    with pytest.raises(ValueError, match="Initial mint refuses an already identified record"):
        chain._source_fixture(tmp_path, monkeypatch)
    assert constructor_calls == []


@pytest.mark.parametrize("attack", ["missing_alias", "wrong_alias", "science", "history", "mim_id"])
def test_minted_projection_refuses_alias_or_science_drift(originals, attack):
    records = chain._cas_originals(originals)
    witness = chain._initial_mint_witnesses(records)[1]
    actual = copy.deepcopy(witness)
    if attack == "missing_alias":
        actual["legacy_identifiers"].remove(chain.RETIRED)
    elif attack == "wrong_alias":
        actual["legacy_identifiers"][1] = "cas:000-00-0"
    elif attack == "science":
        actual["chemical_properties"]["cas_rn"] = "000-00-0"
    elif attack == "history":
        actual["curation_history"].insert(0, copy.deepcopy(actual["curation_history"][-1]))
    else:
        actual["mim_id"] = "MIM:0000003"
    with pytest.raises(AssertionError):
        chain._assert_mint_projection(records[1], witness, actual)


def test_original_git_and_archived_prestate_match_real_mint_contract(
    tmp_path, monkeypatch, originals
):
    records = chain._cas_originals(originals)
    witnesses = chain._initial_mint_witnesses(records)
    # Construct input Git trees and ledgers only. No adoption prepare/apply,
    # successor, publication or semantic native chain is invoked here.
    fixture = chain.fixtures.NativeReviewAdoptionFixture(
        tmp_path, monkeypatch, original_records=records
    )
    migration = json.loads((fixture.root / chain.api.MIGRATION).read_bytes())
    legacy_baseline = json.loads((fixture.legacy / "plan.json").read_bytes())["baseline_commit"]
    for path, original, witness, mint in zip(
        fixture.paths, records, witnesses, fixture.mints, strict=True
    ):
        pre_id = chain.api.git(fixture.root, "show", f"{migration['source_commit']}:{path}")
        legacy = chain.api.git(fixture.legacy, "show", f"{legacy_baseline}:{path}")
        assert pre_id == legacy and chain.api.sha(pre_id) == mint["before_sha256"]
        assert chain.api.load_yaml(pre_id) == original
        current = (fixture.root / path).read_bytes()
        assert chain.api.sha(current) == mint["after_sha256"]
        chain._assert_mint_projection(original, witness, chain.api.load_yaml(current))
        if path == chain.RETIRED_OWNER:
            assert (fixture.legacy / "archive/move.yaml").read_bytes() == pre_id
    assert not fixture.stage.exists()
    assert not fixture.receipt.exists()


@pytest.fixture
def withdrawal(originals):
    before = chain._initial_mint_witnesses(chain._cas_originals(originals))[1]
    stamp = "2026-11-12T00:00:00Z"
    after = chain._withdraw_cas(before, stamp)
    holds = [{"issue_key": "retained-quantity", "reason": "Source quantity remains unassessed"}]
    operation = {
        "mim_id": before["mim_id"],
        "before": {"path": chain.OLD_OWNER},
        "after_path": chain.RETIRED_OWNER,
        "delta": chain.successor._delta(before, after),
        "issues": ["https://github.com/CultureBotAI/MediaIngredientMech/issues/1439"],
        "inherited_holds": copy.deepcopy(holds),
        "residual_holds": copy.deepcopy(holds),
        "rejected_identifiers": [chain.RETIRED],
        "rejected_labels": [],
    }
    loaded = SimpleNamespace(root=chain.ROOT, request={"timestamp": stamp})
    return loaded, operation, before, after


def test_explicit_withdrawal_preserves_identity_history_and_hold(withdrawal):
    loaded, operation, before, after = withdrawal
    assert chain.successor._validate_change(loaded, operation, before, after) == operation["delta"]
    assert before["identifier"] == chain.RETIRED and after["identifier"] == "UNMAPPED_1"
    assert before["mim_id"] == after["mim_id"] == "MIM:0000002"
    assert after["legacy_identifiers"] == ["MIM:Move"]
    assert "chemical_properties" not in after
    assert after["mapping_status"] == before["mapping_status"] == "UNMAPPED"
    assert "ontology_mapping" not in after
    assert after["synonyms"] == before["synonyms"]
    assert after["curation_history"][:-1] == before["curation_history"]
    assert operation["inherited_holds"] == operation["residual_holds"]
    assert chain.RETIRED in before["legacy_identifiers"]
    assert before["chemical_properties"]["cas_rn"] == "138-86-7"


@pytest.mark.parametrize(
    "attack,reason",
    [
        ("identifier", "disproved identifier remains resolving"),
        ("alias", "every removed resolving alias"),
        ("ontology", "rejected identifier remains in active ontology mapping"),
        ("hold", "hold retirement is outside successor v1"),
    ],
)
def test_real_successor_guard_refuses_reactivated_cas_or_cleared_hold(withdrawal, attack, reason):
    loaded, operation, before, after = withdrawal
    if attack == "identifier":
        after["identifier"] = chain.RETIRED
    elif attack == "alias":
        after["legacy_identifiers"].append(chain.RETIRED)
    elif attack == "ontology":
        after["ontology_mapping"] = {"ontology_id": chain.RETIRED}
    else:
        operation["residual_holds"] = []
    operation["delta"] = chain.successor._delta(before, after)
    with pytest.raises(ValueError, match=reason):
        chain.successor._validate_change(loaded, operation, before, after)
