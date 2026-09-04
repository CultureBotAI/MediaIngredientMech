"""Tests for scripts/score_causal_graph_readiness.py."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

_REPO_ROOT = Path(__file__).resolve().parent.parent
_SCRIPT_PATH = _REPO_ROOT / "scripts" / "score_causal_graph_readiness.py"

if str(_REPO_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT / "src"))
_SPEC = importlib.util.spec_from_file_location("_score_causal_graph", _SCRIPT_PATH)
_score = importlib.util.module_from_spec(_SPEC)
sys.modules["_score_causal_graph"] = _score
_SPEC.loader.exec_module(_score)  # type: ignore[union-attr]


def _record(**overrides):
    record = {
        "identifier": "CHEBI:1",
        "preferred_term": "Water",
        "mapping_status": "MAPPED",
        "ingredient_type": "SINGLE_INGREDIENT",
        "ontology_mapping": {
            "ontology_id": "CHEBI:1",
            "ontology_label": "water",
            "ontology_source": "CHEBI",
            "mapping_quality": "EXACT_MATCH",
            "evidence": [{"evidence_type": "DATABASE_MATCH", "source": "ChEBI"}],
        },
        "occurrence_statistics": {"total_occurrences": 1, "media_count": 1},
    }
    record.update(overrides)
    return record


def test_role_evidence_outranks_computational_predictions():
    weak = _record(
        physicochemical_roles=[
            {
                "role": "BUFFER",
                "confidence": 0.6,
                "evidence": [
                    {
                        "reference_type": "COMPUTATIONAL_PREDICTION",
                        "reference_text": "inferred from label",
                    }
                ],
            }
        ]
    )
    strong = _record(
        physicochemical_roles=[
            {
                "role": "BUFFER",
                "confidence": 0.95,
                "evidence": [
                    {
                        "reference_type": "PEER_REVIEWED_PUBLICATION",
                        "doi": "10.1128/jb.00123-15",
                        "excerpt": "buffered with Bis-Tris",
                        "curator_note": "The publication explicitly uses Bis-Tris as a buffer.",
                    }
                ],
            }
        ]
    )

    weak_row = _score.score_record(Path("weak.yaml"), weak)
    strong_row = _score.score_record(Path("strong.yaml"), strong)

    assert weak_row.readiness_score < strong_row.readiness_score
    assert weak_row.role_evidence_score < strong_row.role_evidence_score
    assert "role_lacks_external_evidence:physicochemical_roles.BUFFER" in weak_row.issues


@pytest.mark.parametrize("reference_type", ["COMPUTATIONAL_PREDICTION", "MANUAL_CURATION"])
def test_detailed_non_external_role_evidence_still_lacks_external_source(reference_type):
    record = _record(
        nutritional_roles=[
            {
                "role": "CARBON_SOURCE",
                "confidence": 0.9,
                "evidence": [
                    {
                        "reference_type": reference_type,
                        "reference_text": "name-list or manual inference",
                        "url": "https://example.org/model",
                        "excerpt": "predicted carbon source",
                        "curator_note": "The role was inferred without an external source.",
                    }
                ],
            }
        ]
    )

    row = _score.score_record(Path("predicted.yaml"), record)

    assert row.best_role_evidence > _score.CITATION_TYPE_POINTS["COMPUTATIONAL_PREDICTION"]
    assert "role_lacks_external_evidence:nutritional_roles.CARBON_SOURCE" in row.issues


def test_records_without_roles_sort_ahead_of_higher_scoring_role_records(tmp_path):
    ingredients_dir = tmp_path / "ingredients" / "mapped"
    ingredients_dir.mkdir(parents=True)
    no_roles_high_occurrence = _record(
        preferred_term="Needs roles",
        occurrence_statistics={"total_occurrences": 50, "media_count": 50},
    )
    no_roles_low_occurrence = _record(
        preferred_term="Needs roles less often",
        occurrence_statistics={"total_occurrences": 1, "media_count": 1},
    )
    with_roles = _record(
        preferred_term="Has roles",
        occurrence_statistics={"total_occurrences": 100, "media_count": 100},
        nutritional_roles=[
            {
                "role": "CARBON_SOURCE",
                "confidence": 0.9,
                "evidence": [{"reference_type": "DATABASE_ENTRY", "url": "https://example.org"}],
            }
        ],
    )

    (ingredients_dir / "no_roles_high.yaml").write_text(yaml.safe_dump(no_roles_high_occurrence))
    (ingredients_dir / "no_roles_low.yaml").write_text(yaml.safe_dump(no_roles_low_occurrence))
    (ingredients_dir / "with_roles.yaml").write_text(yaml.safe_dump(with_roles))

    rows = _score.rank_records(sorted(ingredients_dir.glob("*.yaml")))

    assert [row.preferred_term for row in rows] == [
        "Needs roles",
        "Needs roles less often",
        "Has roles",
    ]
    assert rows[0].issues == ("no_ingredient_roles",)


def test_component_parent_without_components_is_penalized():
    record = _record(ingredient_type="NAMED_MEDIUM")

    row = _score.score_record(Path("medium.yaml"), record)

    assert row.component_score == 0
    assert "no_component_edges" in row.issues


def test_duplicate_identifier_disposition_penalizes_identity_score():
    record = _record()

    clean = _score.score_record(Path("clean.yaml"), record)
    duplicate = _score.score_record(
        Path("duplicate.yaml"),
        record,
        duplicate_identifier_disposition="NEEDS_OWN_ID",
    )

    assert duplicate.identity_score == clean.identity_score - 3.0
    assert "duplicate_identifier:NEEDS_OWN_ID" in duplicate.issues


def test_rank_records_uses_duplicate_baseline_by_collection(tmp_path):
    ingredients_dir = tmp_path / "ingredients" / "mapped"
    ingredients_dir.mkdir(parents=True)
    record_path = ingredients_dir / "record.yaml"
    record_path.write_text(yaml.safe_dump(_record(identifier="NCIT:C896")))

    rows = _score.rank_records(
        [record_path],
        duplicate_identifier_dispositions={("mapped", "NCIT:C896"): "NEEDS_OWN_ID"},
    )

    assert rows[0].identity_score == 14.0
    assert "duplicate_identifier:NEEDS_OWN_ID" in rows[0].issues


def test_load_duplicate_identifier_dispositions(tmp_path):
    baseline = tmp_path / "baseline.tsv"
    baseline.write_text(
        "identifier\tcollection\trecord_count\tdisposition\n"
        "NCIT:C896\tmapped\t2\tNEEDS_OWN_ID\n",
        encoding="utf-8",
    )

    assert _score.load_duplicate_identifier_dispositions(baseline) == {
        ("mapped", "NCIT:C896"): "NEEDS_OWN_ID"
    }


def test_load_duplicate_identifier_dispositions_rejects_malformed_baseline(tmp_path):
    baseline = tmp_path / "baseline.tsv"
    baseline.write_text("identifier\tcollection\nNCIT:C896\tmapped\n", encoding="utf-8")

    with pytest.raises(ValueError, match="disposition"):
        _score.load_duplicate_identifier_dispositions(baseline)


def test_load_duplicate_identifier_dispositions_rejects_repeated_groups(tmp_path):
    baseline = tmp_path / "baseline.tsv"
    baseline.write_text(
        "identifier\tcollection\tdisposition\n"
        "NCIT:C896\tmapped\tNEEDS_OWN_ID\n"
        "NCIT:C896\tmapped\tUNREVIEWED\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="duplicate row"):
        _score.load_duplicate_identifier_dispositions(baseline)


@pytest.mark.parametrize(
    ("row", "message"),
    [
        ("\tmapped\tNEEDS_OWN_ID\n", "missing an identifier"),
        ("NCIT:C896\tmappped\tNEEDS_OWN_ID\n", "unsupported collection"),
        ("NCIT:C896\tmapped\tNEED_OWN_ID\n", "unsupported disposition"),
    ],
)
def test_load_duplicate_identifier_dispositions_rejects_invalid_rows(tmp_path, row, message):
    baseline = tmp_path / "baseline.tsv"
    baseline.write_text(
        "identifier\tcollection\tdisposition\n" + row,
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match=message):
        _score.load_duplicate_identifier_dispositions(baseline)


def test_rejected_records_are_skipped_by_default(tmp_path):
    active = tmp_path / "active.yaml"
    rejected = tmp_path / "rejected.yaml"
    active.write_text(yaml.safe_dump(_record(preferred_term="Active")))
    rejected.write_text(yaml.safe_dump(_record(mapping_status="REJECTED")))

    rows = _score.rank_records([rejected, active])

    assert [row.path for row in rows] == [active]
    assert _score.rank_records([rejected], include_rejected=True)[0].mapping_status == "REJECTED"


def test_main_defaults_to_mapped_records(tmp_path):
    ingredients_dir = tmp_path / "ingredients"
    mapped_dir = ingredients_dir / "mapped"
    unmapped_dir = ingredients_dir / "unmapped"
    mapped_dir.mkdir(parents=True)
    unmapped_dir.mkdir(parents=True)
    (mapped_dir / "mapped.yaml").write_text(yaml.safe_dump(_record(preferred_term="Mapped")))
    (unmapped_dir / "unmapped.yaml").write_text(
        yaml.safe_dump(_record(preferred_term="Unmapped", mapping_status="UNMAPPED"))
    )

    out = tmp_path / "readiness.tsv"

    assert _score.main(["--ingredients-dir", str(ingredients_dir), "--out", str(out)]) == 0

    lines = out.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 2
    assert "\tMapped\t" in lines[1]


def test_write_tsv_emits_ranked_rows(tmp_path):
    out = tmp_path / "readiness.tsv"
    rows = [
        _score.score_record(tmp_path / "b.yaml", _record(preferred_term="B")),
        _score.score_record(tmp_path / "a.yaml", _record(preferred_term="A")),
    ]

    _score.write_tsv(rows, out, tmp_path)

    lines = out.read_text(encoding="utf-8").splitlines()
    assert lines[0].startswith("rank\treadiness_score\t")
    assert lines[1].split("\t")[:3] == ["1", "27.000", "17.000"]
    assert lines[2].split("\t")[0] == "2"
