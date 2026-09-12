"""Regression coverage for hidden hydrate synonym rejection (#251)."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "reject_hidden_hydrate_synonym_collapses.py"


@pytest.fixture(scope="module")
def mod():
    spec = importlib.util.spec_from_file_location(
        "reject_hidden_hydrate_synonym_collapses",
        SCRIPT,
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def mapped_records() -> list[dict]:
    return yaml.safe_load(
        (REPO / "data" / "curated" / "mapped_ingredients.yaml").read_text(encoding="utf-8")
    )["ingredients"]


def test_anhydrous_targets_reject_hydrate_synonyms_but_not_notes(mod) -> None:
    assert (
        mod.false_hydrate_reason(
            mod.ANHYDROUS_KIND,
            "Na2HPO4",
            {"synonym_text": "Na2HPO4 x 2 H2O", "synonym_type": "HYDRATE_FORM"},
        )
        == "hydrate synonym on an anhydrous record"
    )

    assert (
        mod.false_hydrate_reason(
            mod.ANHYDROUS_KIND,
            "Na2HPO4",
            {"synonym_text": "Role: Na2HPO4 x 2 H2O stock"},
        )
        is None
    )


@pytest.mark.parametrize(
    "synonym_text",
    [
        "Na2HPO4 x 2H2O",
        "Na2HPO4 x2 H2O",
        "sodium hydrogen orthophosphate dihydrate",
        "sodium hydrogen orthophosphate hydrate",
    ],
)
def test_specific_hydrate_targets_keep_same_or_unspecified_states(
    mod,
    synonym_text: str,
) -> None:
    assert (
        mod.false_hydrate_reason(
            mod.HYDRATE_KIND,
            "Na2HPO4 x 2 H2O",
            {"synonym_text": synonym_text, "synonym_type": "HYDRATE_FORM"},
        )
        is None
    )


@pytest.mark.parametrize(
    "synonym_text,reason",
    [
        ("Na2HPO4 x 7 H2O", "7 H2O synonym on a 2 H2O record"),
        ("Na2HPO4 x 76 H2O", "malformed hydrate notation"),
        ("Na2HPO4 x n H2O", "variable hydrate synonym on a specific hydrate record"),
    ],
)
def test_specific_hydrate_targets_reject_false_states(
    mod,
    synonym_text: str,
    reason: str,
) -> None:
    assert (
        mod.false_hydrate_reason(
            mod.HYDRATE_KIND,
            "Na2HPO4 x 2 H2O",
            {"synonym_text": synonym_text, "synonym_type": "HYDRATE_FORM"},
        )
        == reason
    )


def test_reject_records_marks_only_false_hydrate_synonyms(mod) -> None:
    records = [
        {
            "identifier": "CHEBI:test",
            "preferred_term": "CoCl2 x 2 H2O",
            "mapping_status": "MAPPED",
            "synonyms": [
                {"synonym_text": "CoCl2 x 2H2O", "synonym_type": "HYDRATE_FORM"},
                {"synonym_text": "CoCl2 x 6H2O", "synonym_type": "HYDRATE_FORM"},
                {"synonym_text": "CoCl2 x n H2O", "synonym_type": "HYDRATE_FORM"},
            ],
        }
    ]

    rejected, false_labels = mod.reject_records(
        records,
        {("CHEBI:test", "CoCl2 x 2 H2O"): mod.HYDRATE_KIND},
    )

    assert rejected == {"CoCl2 x 2 H2O": ["CoCl2 x 6H2O", "CoCl2 x n H2O"]}
    assert false_labels == {"CoCl2 x 2 H2O": ["CoCl2 x 6H2O", "CoCl2 x n H2O"]}
    assert [syn["synonym_type"] for syn in records[0]["synonyms"]] == [
        "HYDRATE_FORM",
        "REJECTED_LABEL",
        "REJECTED_LABEL",
    ]
    assert records[0]["curation_history"][-1]["action"] == ("REJECTED_HIDDEN_HYDRATE_SYNONYMS")


def test_reject_records_returns_already_rejected_false_labels_for_sssom_scrub(mod) -> None:
    records = [
        {
            "identifier": "CHEBI:test",
            "preferred_term": "CoCl2 x 2 H2O",
            "mapping_status": "MAPPED",
            "synonyms": [
                {"synonym_text": "CoCl2 x 6H2O", "synonym_type": "REJECTED_LABEL"},
            ],
        }
    ]

    changed, false_labels = mod.reject_records(
        records,
        {("CHEBI:test", "CoCl2 x 2 H2O"): mod.HYDRATE_KIND},
    )

    assert changed == {}
    assert false_labels == {"CoCl2 x 2 H2O": ["CoCl2 x 6H2O"]}
    assert "curation_history" not in records[0]


def test_scrub_sssom_other_removes_rejected_tokens_from_all_subject_rows(mod) -> None:
    text = (
        "subject_id\tsubject_label\tobject_id\tother\n"
        "MIM:Salt\tSalt\tCHEBI:1\tgood|bad hydrate|CAS:1\n"
        "MIM:Salt\tSalt\tkgmicrobe.compound:salt\tbad hydrate|good\n"
        "MIM:Other\tOther\tCHEBI:2\tbad hydrate|good\n"
    )

    scrubbed, rows, tokens = mod.scrub_sssom_other(text, {"Salt": ["bad hydrate"]})

    assert rows == 2
    assert tokens == 2
    assert scrubbed == (
        "subject_id\tsubject_label\tobject_id\tother\n"
        "MIM:Salt\tSalt\tCHEBI:1\tgood|CAS:1\n"
        "MIM:Salt\tSalt\tkgmicrobe.compound:salt\tgood\n"
        "MIM:Other\tOther\tCHEBI:2\tbad hydrate|good\n"
    )


def test_reviewed_targets_no_longer_publish_false_hydrate_synonyms(
    mod,
    mapped_records: list[dict],
) -> None:
    offenders = []
    for record in mapped_records:
        key = (
            str(record.get("identifier") or ""),
            str(record.get("preferred_term") or ""),
        )
        target_kind = mod.TARGET_KINDS.get(key)
        if target_kind is None:
            continue
        for synonym in record.get("synonyms") or []:
            if not isinstance(synonym, dict):
                continue
            reason = mod.false_hydrate_reason(
                target_kind,
                record.get("preferred_term"),
                synonym,
            )
            if reason:
                offenders.append(
                    (
                        record.get("preferred_term"),
                        synonym.get("synonym_text"),
                        reason,
                    )
                )

    assert offenders == []
