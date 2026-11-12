"""Finite corrective-delta counterexamples; these are not native approvals."""

import copy
from types import SimpleNamespace

import pytest

from mediaingredientmech.curate import curation_successor as successor
from tests.test_stable_id_adoption import ROOT, api


def proposed():
    """Make an exact synthetic owner-scoped external-identity withdrawal."""
    before = {
        "identifier": "NCIT:C80300",
        "preferred_term": "Example",
        "mapping_status": "MAPPED",
        "mim_id": "MIM:0000001",
        "legacy_identifiers": ["MIM:Example", "NCIT:C80300"],
        "ontology_mapping": {
            "ontology_id": "NCIT:C80300",
            "ontology_label": "Maltose Monohydrate",
            "ontology_source": "NCIT",
            "mapping_quality": "EXACT_MATCH",
        },
        "synonyms": [{"synonym_text": "disproved species", "synonym_type": "RAW_TEXT"}],
        "curation_history": [],
        "notes": "Original raw-source provenance.",
    }
    after = copy.deepcopy(before)
    after.update(
        identifier="UNMAPPED_0418",
        mapping_status="UNMAPPED",
        legacy_identifiers=["MIM:Example", "UNMAPPED_0418"],
        notes=before["notes"] + " Reviewed identity withdrawal; no source hold cleared.",
    )
    after.pop("ontology_mapping")
    after["synonyms"][0]["synonym_type"] = "REJECTED_LABEL"
    api.record_curation_event(
        after,
        curator="original-proposal-author",
        timestamp="2026-11-11T00:00:00Z",
        action="MANUAL_CURATION",
        changes="Withdraw the unsupported identity; preserve exact original claims in beforeimage and request delta.",
        previous_status="MAPPED",
        new_status="UNMAPPED",
        llm_assisted=True,
        llm_model="synthetic-test",
    )
    hold = {"issue_key": "synthetic-quantity-hold", "reason": "Source quantity remains unassessed"}
    operation = {
        "mim_id": "MIM:0000001",
        "before": {"path": "data/ingredients/mapped/Example.yaml"},
        "after_path": "data/ingredients/unmapped/Example.yaml",
        "delta": successor._delta(before, after),
        "issues": ["https://github.com/CultureBotAI/MediaIngredientMech/issues/1373"],
        "inherited_holds": [hold],
        "residual_holds": [copy.deepcopy(hold)],
        "rejected_identifiers": ["NCIT:C80300"],
        "rejected_labels": ["disproved species"],
    }
    loaded = SimpleNamespace(
        root=ROOT, request={"timestamp": "2026-11-12T00:00:00Z", "curator": "later-coordinator"}
    )
    return loaded, operation, before, after


def test_exact_rejection_retains_original_event_notes_placeholder_and_hold():
    """Later batching preserves a genuine earlier proposal's author and time."""
    loaded, operation, before, after = proposed()
    original = copy.deepcopy(after)
    assert successor._validate_change(loaded, operation, before, after) == operation["delta"]
    assert after == original
    assert after["mim_id"] == before["mim_id"]
    assert "NCIT:C80300" not in after["legacy_identifiers"]
    assert operation["residual_holds"] == operation["inherited_holds"]


@pytest.mark.parametrize(
    "case",
    [
        "permanent-id",
        "undeclared-delta",
        "event-prefix",
        "future-event",
        "event-status",
        "hold-clearance",
        "resolving-rejection",
        "rejected-grounding",
        "new-permanent-alias",
        "lost-raw-token",
        "searchable-rejection",
        "filename",
        "preferred-label",
        "source-accounting",
        "invalid-schema",
    ],
)
def test_corrective_delta_cannot_expand_authority_or_lose_provenance(case):
    """Even re-declared deltas must satisfy identity/history/source invariants."""
    loaded, operation, before, after = proposed()
    if case == "permanent-id":
        after["mim_id"] = "MIM:0000002"
    elif case == "undeclared-delta":
        after["notes"] += " Not declared."
    elif case == "event-prefix":
        before["curation_history"] = [copy.deepcopy(after["curation_history"][0])]
    elif case == "future-event":
        after["curation_history"][-1]["timestamp"] = "2027-01-01T00:00:00Z"
    elif case == "event-status":
        after["curation_history"][-1]["previous_status"] = "UNMAPPED"
    elif case == "hold-clearance":
        operation["residual_holds"] = []
    elif case == "resolving-rejection":
        after["legacy_identifiers"].append("NCIT:C80300")
    elif case == "rejected-grounding":
        after["ontology_mapping"] = copy.deepcopy(before["ontology_mapping"])
    elif case == "new-permanent-alias":
        after["legacy_identifiers"].append("MIM:0000099")
    elif case == "lost-raw-token":
        after["synonyms"] = []
    elif case == "searchable-rejection":
        after["synonyms"][0]["synonym_type"] = "RAW_TEXT"
    elif case == "filename":
        operation["after_path"] = "data/ingredients/unmapped/Other.yaml"
    elif case == "preferred-label":
        after["preferred_term"] = "Another identity"
    elif case == "source-accounting":
        after["media_count"] = 999
    elif case == "invalid-schema":
        after["chemical_properties"] = {"not_a_schema_field": True}
    if case != "undeclared-delta":
        operation["delta"] = successor._delta(before, after)
    with pytest.raises(ValueError):
        successor._validate_change(loaded, operation, before, after)


def test_native_withdrawal_relocates_owner_without_retiring_permanent_identity(
    tmp_path, monkeypatch
):
    """A paired-reviewed withdrawal uses real retirement and retains all raw history."""
    import yaml

    from tests.test_curation_successor import SuccessorFixture, ref
    from tests.test_curation_successor_transition import maintained, prepared
    from tests.test_stable_id_adoption import write

    f = SuccessorFixture(tmp_path, monkeypatch)
    op = f.request["operations"][0]
    old = op["before"]["path"]
    before = api.load_yaml(f.before[old])
    after = copy.deepcopy(before)
    rejected = before["identifier"]
    after.update(
        identifier="UNMAPPED_0418",
        mapping_status="UNMAPPED",
        legacy_identifiers=[x for x in before["legacy_identifiers"] if x != rejected]
        + ["UNMAPPED_0418"],
    )
    after.pop("ontology_mapping")
    api.record_curation_event(
        after,
        curator="independent-original-author",
        timestamp="2026-11-11T00:00:00Z",
        action="MANUAL_CURATION",
        changes="Synthetic reviewed owner-scoped identity withdrawal, not global retirement; retain beforeimage and original holds.",
        previous_status="MAPPED",
        new_status="UNMAPPED",
        llm_assisted=True,
        llm_model="synthetic-fixture",
    )
    f.proposal.write_text(yaml.safe_dump(after, sort_keys=False))
    op.update(
        after_path="data/ingredients/unmapped/Exact.yaml",
        proposal=ref(f.target, f.proposal),
        delta=successor._delta(before, after),
        rejected_identifiers=[rejected],
    )
    write(f.path, f.request)
    original = maintained(f.predecessor)
    before_ledgers = {name: (f.target / name).read_bytes() for name in successor.LEDGERS}
    stage, acceptance, manifest = prepared(f)
    receipt = f.target / ".temp/withdrawal-application"
    actual = successor.apply(f.target, stage, acceptance, receipt, enabled=True)
    assert actual["state"] == "COMPLETE" and actual["recovery_required"] is False
    assert not (f.target / old).exists()
    current = api.load_yaml((f.target / op["after_path"]).read_bytes())
    assert current == after and current["mim_id"] == before["mim_id"]
    assert rejected not in current["legacy_identifiers"] and "ontology_mapping" not in current
    assert (f.target / actual["retired_sources"][old]["path"]).read_bytes() == f.before[old]
    assert {name: (f.target / name).read_bytes() for name in successor.LEDGERS} == before_ledgers
    assert maintained(f.predecessor) == original
    assert (
        successor.verify_completed(f.target, stage, receipt / "application.json")["status"]
        == "COMPLETE_CURRENT_SOURCE_SUCCESSOR"
    )
    assert manifest["moves"] == {old: op["after_path"]}
