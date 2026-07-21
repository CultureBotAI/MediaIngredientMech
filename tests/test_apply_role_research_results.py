"""Tests for scripts/apply_role_research_results.py — Step 7b MIM applier."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest
import yaml


_REPO_ROOT = Path(__file__).resolve().parent.parent
_SCRIPT_PATH = _REPO_ROOT / "scripts" / "apply_role_research_results.py"

if str(_REPO_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT / "src"))
_SPEC = importlib.util.spec_from_file_location("_apply_roles", _SCRIPT_PATH)
_apply = importlib.util.module_from_spec(_SPEC)
sys.modules["_apply_roles"] = _apply
_SPEC.loader.exec_module(_apply)  # type: ignore[union-attr]


def _write_batch(tmp_path: Path, proposals: list[dict]) -> Path:
    p = tmp_path / "batch.json"
    p.write_text(json.dumps({"proposals": proposals}))
    return p


def _write_ingredient(tmp_path: Path, slug: str, doc: dict) -> Path:
    (tmp_path / "data" / "ingredients" / "mapped").mkdir(parents=True, exist_ok=True)
    p = tmp_path / "data" / "ingredients" / "mapped" / f"{slug}.yaml"
    p.write_text(yaml.safe_dump(doc))
    return p


# ---------------- batch loader ----------------


def test_load_batch_requires_proposals_key(tmp_path):
    p = tmp_path / "bad.json"
    p.write_text('{"other": []}')
    with pytest.raises(SystemExit, match="proposals"):
        _apply._load_batch(p)


def test_load_batch_requires_list(tmp_path):
    p = tmp_path / "bad.json"
    p.write_text('{"proposals": "not a list"}')
    with pytest.raises(SystemExit, match="must be a list"):
        _apply._load_batch(p)


def test_load_batch_accepts_valid_shape(tmp_path):
    p = _write_batch(tmp_path, [{"ingredient_identifier": "CHEBI:17561"}])
    proposals = _apply._load_batch(p)
    assert len(proposals) == 1
    assert proposals[0]["ingredient_identifier"] == "CHEBI:17561"


# ---------------- _build_assignment ----------------


def test_build_assignment_shape():
    a = _apply._build_assignment(
        "AMINO_ACID_SOURCE", 0.95, None,
        [{"reference_type": "PEER_REVIEWED_PUBLICATION", "doi": "10.1234/x", "reference_text": "cite"}],
    )
    assert a == {
        "role": "AMINO_ACID_SOURCE", "confidence": 0.95,
        "evidence": [{"reference_type": "PEER_REVIEWED_PUBLICATION", "doi": "10.1234/x", "reference_text": "cite"}],
    }


def test_build_assignment_carries_metabolic_context_when_given():
    a = _apply._build_assignment("SUBSTRATE", 0.9, "methylotrophs only", [])
    assert a["metabolic_context"] == "methylotrophs only"
    assert a["evidence"] == []


def test_build_assignment_drops_empty_evidence_dicts():
    a = _apply._build_assignment("BUFFER", 0.9, None, [{}, {"doi": "10.1/x"}])
    # Empty {} filtered; the {"doi": ...} kept.
    assert len(a["evidence"]) == 1
    assert a["evidence"][0]["doi"] == "10.1/x"


# ---------------- _apply_proposal ----------------


def _min_proposal_cysteine():
    return {
        "ingredient_identifier": "CHEBI:17561",
        "source_run": "research/ingredients/roles/L-cysteine-edison-literature.md",
        "role_assignments": {
            "nutritional_roles": [
                {"role": "AMINO_ACID_SOURCE", "confidence": 0.95,
                 "evidence": [{"reference_type": "PEER_REVIEWED_PUBLICATION",
                               "doi": "10.1128/jb.00456-20", "reference_text": "Smith 2020"}]},
                {"role": "SULFUR_SOURCE", "confidence": 0.9, "evidence": []},
            ],
            "physicochemical_roles": [
                {"role": "REDUCING_AGENT", "confidence": 0.85,
                 "evidence": [{"pmid": "12345678"}]},
            ],
            "cellular_metabolic_roles": [
                {"role": "SUBSTRATE", "confidence": 0.9,
                 "metabolic_context": "assimilatory sulfate reduction",
                 "evidence": []},
            ],
        },
    }


def test_apply_proposal_writes_all_three_facets():
    record = {"identifier": "CHEBI:17561", "preferred_term": "L-cysteine"}
    applied, reasons, dirty = _apply._apply_proposal(
        record, _min_proposal_cysteine(), "edison-deep-research", dry_run=False,
    )
    assert applied == 4  # 2 nut + 1 phys + 1 cell-met
    assert reasons == []
    assert dirty is True

    assert len(record["nutritional_roles"]) == 2
    assert record["nutritional_roles"][0]["role"] == "AMINO_ACID_SOURCE"
    assert record["nutritional_roles"][0]["evidence"][0]["doi"] == "10.1128/jb.00456-20"
    # SULFUR_SOURCE had empty evidence → fabricated COMPUTATIONAL_PREDICTION citation.
    sulfur = record["nutritional_roles"][1]
    assert sulfur["role"] == "SULFUR_SOURCE"
    assert sulfur["evidence"][0]["reference_type"] == "COMPUTATIONAL_PREDICTION"
    assert "L-cysteine-edison-literature.md" in sulfur["evidence"][0]["reference_text"]

    assert len(record["physicochemical_roles"]) == 1
    assert record["physicochemical_roles"][0]["role"] == "REDUCING_AGENT"
    assert record["physicochemical_roles"][0]["evidence"][0]["pmid"] == "12345678"
    # Schema-legal: metabolic_context is NOT on physicochemical roles.
    assert "metabolic_context" not in record["physicochemical_roles"][0]

    assert len(record["cellular_metabolic_roles"]) == 1
    cell_met = record["cellular_metabolic_roles"][0]
    assert cell_met["role"] == "SUBSTRATE"
    assert cell_met["metabolic_context"] == "assimilatory sulfate reduction"

    # Curation-history event appended, listing exactly the fields touched.
    history = record["curation_history"]
    assert len(history) == 1
    assert history[0]["curator"] == "edison-deep-research"
    assert history[0]["action"] == "ANNOTATED"
    for slot in ("nutritional_roles", "physicochemical_roles", "cellular_metabolic_roles"):
        assert slot in history[0]["changes"]


def test_apply_proposal_drops_illegal_metabolic_context_on_non_cellular_facet():
    """metabolic_context on a physicochemical role must be silently dropped, not raise."""
    record = {"identifier": "CHEBI:17561"}
    proposal = {
        "role_assignments": {
            "physicochemical_roles": [
                {"role": "BUFFER", "confidence": 0.9,
                 "metabolic_context": "nope, not schema-legal here"},  # should be dropped
            ],
        },
    }
    applied, reasons, dirty = _apply._apply_proposal(record, proposal, "edison-deep-research", dry_run=False)
    assert applied == 1
    assert "metabolic_context" not in record["physicochemical_roles"][0]


def test_apply_proposal_rejects_wrong_facet_role_name():
    """A role name that belongs to another facet is skipped with a reason string."""
    record = {"identifier": "CHEBI:17561"}
    proposal = {
        "role_assignments": {
            # BUFFER is physicochemical, not nutritional.
            "nutritional_roles": [{"role": "BUFFER", "confidence": 0.9}],
        },
    }
    applied, reasons, dirty = _apply._apply_proposal(record, proposal, "edison-deep-research", dry_run=False)
    assert applied == 0
    assert dirty is False
    assert any("belongs to physicochemical_roles" in r for r in reasons)


def test_apply_proposal_rejects_role_that_is_no_facet_value():
    """A token that is not a value of ANY facet enum must be skipped, not written.

    facet_slot_for raises for a typo / hallucinated name / retired value
    (MINERAL, SALT). Writing it would produce a schema-invalid record that only
    the downstream validator would catch.
    """
    record = {"identifier": "CHEBI:1", "preferred_term": "x"}
    proposal = {
        "role_assignments": {
            "nutritional_roles": [{"role": "BOGUS_ROLE", "confidence": 0.9}],
        },
    }
    applied, reasons, dirty = _apply._apply_proposal(record, proposal, "edison-deep-research", dry_run=False)
    assert applied == 0
    assert dirty is False
    assert "nutritional_roles" not in record
    assert any("not a permissible value" in r for r in reasons)


def test_apply_proposal_rejects_retired_mineral_role():
    """MINERAL was retired in #128 and is not a facet value; it must not be written."""
    record = {"identifier": "CHEBI:1", "preferred_term": "x"}
    proposal = {
        "role_assignments": {"nutritional_roles": [{"role": "MINERAL", "confidence": 0.9}]},
    }
    applied, reasons, dirty = _apply._apply_proposal(record, proposal, "edison-deep-research", dry_run=False)
    assert applied == 0 and dirty is False
    assert "nutritional_roles" not in record


def test_apply_proposal_never_overwrites_populated_facet():
    """Facet slots that already carry any entries are skipped for that facet only."""
    record = {
        "identifier": "CHEBI:17561",
        "nutritional_roles": [{"role": "CARBON_SOURCE", "confidence": 1.0}],  # pre-existing
    }
    proposal = {
        "role_assignments": {
            "nutritional_roles": [{"role": "AMINO_ACID_SOURCE", "confidence": 0.95}],
            "physicochemical_roles": [{"role": "BUFFER", "confidence": 0.9}],
        },
    }
    applied, reasons, dirty = _apply._apply_proposal(record, proposal, "edison-deep-research", dry_run=False)
    assert applied == 1  # only the physicochemical
    assert any("nutritional_roles: already populated" in r for r in reasons)
    # Pre-existing preserved untouched.
    assert record["nutritional_roles"] == [{"role": "CARBON_SOURCE", "confidence": 1.0}]
    # Physicochemical newly added.
    assert record["physicochemical_roles"][0]["role"] == "BUFFER"


def test_apply_proposal_empty_role_assignments_is_noop():
    record = {"identifier": "CHEBI:17561"}
    applied, reasons, dirty = _apply._apply_proposal(
        record, {"role_assignments": {}}, "edison-deep-research", dry_run=False,
    )
    assert applied == 0
    assert reasons == []
    assert dirty is False
    assert "curation_history" not in record  # no event on no-op


def test_apply_proposal_dry_run_writes_nothing_to_record():
    record = {"identifier": "CHEBI:17561"}
    proposal = {
        "role_assignments": {
            "nutritional_roles": [{"role": "AMINO_ACID_SOURCE", "confidence": 0.9,
                                    "evidence": [{"doi": "10.1234/x"}]}],
        },
    }
    applied, _, dirty = _apply._apply_proposal(record, proposal, "edison-deep-research", dry_run=True)
    assert applied == 1  # still counted
    assert record.get("nutritional_roles") is None
    assert "curation_history" not in record
    assert dirty is False


def test_apply_proposal_rejects_non_dict_role_entries():
    record = {"identifier": "CHEBI:17561"}
    proposal = {
        "role_assignments": {
            "nutritional_roles": ["not-a-dict", None, {"role": "AMINO_ACID_SOURCE", "confidence": 0.9}],
        },
    }
    applied, _, _ = _apply._apply_proposal(record, proposal, "edison-deep-research", dry_run=False)
    assert applied == 1


def test_apply_proposal_role_without_role_field_is_skipped():
    record = {"identifier": "CHEBI:17561"}
    proposal = {
        "role_assignments": {
            "nutritional_roles": [
                {"confidence": 0.9, "evidence": []},  # no role field — skip
                {"role": "AMINO_ACID_SOURCE", "confidence": 0.9},  # ok
            ],
        },
    }
    applied, _, _ = _apply._apply_proposal(record, proposal, "edison-deep-research", dry_run=False)
    assert applied == 1


# ---------------- resolver ----------------


def test_resolve_ingredient_path_uses_explicit_path(monkeypatch, tmp_path):
    yml = _write_ingredient(tmp_path, "L-cysteine", {"identifier": "CHEBI:17561"})
    monkeypatch.setattr(_apply, "INGREDIENTS_DIR", tmp_path / "data" / "ingredients")
    monkeypatch.setattr(_apply, "REPO_ROOT", tmp_path)
    got = _apply._resolve_ingredient_path({
        "ingredient_path": str(yml.relative_to(tmp_path)),
    })
    assert got == yml


def test_resolve_ingredient_path_uses_local_part_of_curie(monkeypatch, tmp_path):
    yml = _write_ingredient(tmp_path, "17561", {"identifier": "CHEBI:17561"})
    monkeypatch.setattr(_apply, "INGREDIENTS_DIR", tmp_path / "data" / "ingredients")
    monkeypatch.setattr(_apply, "REPO_ROOT", tmp_path)
    got = _apply._resolve_ingredient_path({"ingredient_identifier": "CHEBI:17561"})
    assert got == yml


def test_resolve_ingredient_path_returns_none_on_miss(monkeypatch, tmp_path):
    (tmp_path / "data" / "ingredients" / "mapped").mkdir(parents=True)
    monkeypatch.setattr(_apply, "INGREDIENTS_DIR", tmp_path / "data" / "ingredients")
    monkeypatch.setattr(_apply, "REPO_ROOT", tmp_path)
    got = _apply._resolve_ingredient_path({"ingredient_identifier": "CHEBI:99999999"})
    assert got is None


# ---------------- CLI end-to-end ----------------


def test_main_dry_run_produces_summary(tmp_path, monkeypatch, capsys):
    """End-to-end CLI dry-run against a tiny synthetic MIM tree."""
    yml = _write_ingredient(tmp_path, "L-cysteine", {
        "identifier": "CHEBI:17561", "preferred_term": "L-cysteine",
        "mapping_status": "MAPPED",
    })
    batch = _write_batch(tmp_path, [{
        "ingredient_identifier": "CHEBI:17561",
        "ingredient_path": str(yml.relative_to(tmp_path)),
        "source_run": "research/ingredients/roles/L-cysteine-edison-literature.md",
        "role_assignments": {
            "nutritional_roles": [
                {"role": "AMINO_ACID_SOURCE", "confidence": 0.95,
                 "evidence": [{"doi": "10.1234/x", "reference_type": "PEER_REVIEWED_PUBLICATION"}]},
            ],
        },
    }])
    monkeypatch.setattr(_apply, "INGREDIENTS_DIR", tmp_path / "data" / "ingredients")
    monkeypatch.setattr(_apply, "REPO_ROOT", tmp_path)
    rc = _apply.main([str(batch), "--dry-run"])
    assert rc == 0
    out = capsys.readouterr().out
    assert "Loaded 1 proposals" in out
    assert "Role assignments applied: 1" in out
    assert "[dry-run]" in out
    # File not mutated.
    assert yaml.safe_load(yml.read_text()) == {
        "identifier": "CHEBI:17561", "preferred_term": "L-cysteine", "mapping_status": "MAPPED",
    }


def test_main_real_write(tmp_path, monkeypatch, capsys):
    """Full CLI (not dry-run) writes the facet slots + curation_history back to disk."""
    yml = _write_ingredient(tmp_path, "L-cysteine", {
        "identifier": "CHEBI:17561", "preferred_term": "L-cysteine",
        "mapping_status": "MAPPED",
    })
    batch = _write_batch(tmp_path, [{
        "ingredient_identifier": "CHEBI:17561",
        "ingredient_path": str(yml.relative_to(tmp_path)),
        "source_run": "research/ingredients/roles/L-cysteine-edison-literature.md",
        "role_assignments": {
            "nutritional_roles": [
                {"role": "AMINO_ACID_SOURCE", "confidence": 0.95,
                 "evidence": [{"doi": "10.1234/x", "reference_type": "PEER_REVIEWED_PUBLICATION"}]},
            ],
        },
    }])
    monkeypatch.setattr(_apply, "INGREDIENTS_DIR", tmp_path / "data" / "ingredients")
    monkeypatch.setattr(_apply, "REPO_ROOT", tmp_path)
    rc = _apply.main([str(batch)])
    assert rc == 0

    round_tripped = yaml.safe_load(yml.read_text())
    assert round_tripped["nutritional_roles"][0]["role"] == "AMINO_ACID_SOURCE"
    assert round_tripped["nutritional_roles"][0]["evidence"][0]["doi"] == "10.1234/x"
    assert round_tripped["curation_history"][0]["curator"] == "edison-deep-research"
    assert "nutritional_roles" in round_tripped["curation_history"][0]["changes"]

    out = capsys.readouterr().out
    assert "Ingredient records written: 1" in out
