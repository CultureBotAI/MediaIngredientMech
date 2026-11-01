"""The #1003 repair must reject only the old amide name, without identity drift."""

import copy
import csv
import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def load_script(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


mod = load_script("reject_carnitinamide_synonym")


@pytest.fixture
def record():
    return {
        "identifier": "kgmicrobe.compound:carnitine_hydrochloride",
        "preferred_term": "Carnitine Hydrochloride", "mapping_status": "MAPPED",
        "ontology_mapping": {
            "ontology_id": "CHEBI:17126", "ontology_label": "carnitine",
            "ontology_source": "CHEBI", "mapping_quality": "NARROW_MATCH",
        },
        "synonyms": [{"synonym_text": mod.ALIAS, "synonym_type": "EXACT_SYNONYM",
                      "source": "chebi_synonym_review"},
                     {"synonym_text": "raw carnitine salt label", "synonym_type": "RELATED_SYNONYM",
                      "source": "source observation"}],
        "occurrence_statistics": {"total_occurrences": 14, "media_count": 14},
        "curation_history": [{"timestamp": "2026-07-05T00:00:00Z", "curator": "prior",
                              "action": "CORRECTED", "changes": "Removed the wrong amide mapping"}],
    }


def test_preserves_substance_fields_and_raw_provenance(record):
    before = copy.deepcopy(record)
    result = mod.corrected_record(record, timestamp="2026-11-01T00:00:00Z")
    assert record == before
    for key in before.keys() - {"synonyms", "curation_history"}:
        assert result[key] == before[key]
    assert result["synonyms"][0] == {**before["synonyms"][0], "synonym_type": "REJECTED_LABEL"}
    assert result["synonyms"][1:] == before["synonyms"][1:]
    assert result["curation_history"][:-1] == before["curation_history"]
    assert result["curation_history"][-1]["llm_assisted"] is True
    assert result["curation_history"][-1]["curator"] == "reject_carnitinamide_synonym.py"
    assert mod.corrected_record(result) is None


def test_rejected_amide_cannot_resolve_but_other_source_label_survives(record, tmp_path):
    exporter = load_script("export_lists")
    path = tmp_path / "label_index.csv"
    exporter.export_label_index([record], path)
    with path.open() as handle:
        assert mod.ALIAS in {r["label"] for r in csv.DictReader(handle)}
    exporter.export_label_index([mod.corrected_record(record)], path)
    with path.open() as handle:
        labels = {r["label"] for r in csv.DictReader(handle)}
    assert mod.ALIAS not in labels
    assert "raw carnitine salt label" in labels
    assert "Carnitine Hydrochloride" in labels


@pytest.mark.parametrize("section,key,value", [
    (None, "identifier", "CHEBI:48601"),
    (None, "preferred_term", "DL-Carnitine hydrochloride"),
    ("ontology_mapping", "ontology_id", "CHEBI:48601"),
    ("ontology_mapping", "mapping_quality", "EXACT_MATCH"),
])
def test_refuses_changed_identity(record, section, key, value):
    (record if section is None else record[section])[key] = value
    with pytest.raises(ValueError):
        mod.corrected_record(record)


@pytest.mark.parametrize("kind", ["missing", "duplicate", "source_changed", "already_rejected"])
def test_refuses_ambiguous_or_unreviewed_synonym_state(record, kind):
    if kind == "missing":
        record["synonyms"].pop(0)
    elif kind == "duplicate":
        record["synonyms"].append(copy.deepcopy(record["synonyms"][0]))
    elif kind == "source_changed":
        record["synonyms"][0]["source"] = "different provenance"
    else:
        record["synonyms"][0]["synonym_type"] = "REJECTED_LABEL"
    with pytest.raises(ValueError):
        mod.corrected_record(record)


def test_native_schema_gate_rejects_unknown_fields(record):
    record["invented_approval"] = True
    with pytest.raises(ValueError, match="closed-schema"):
        mod.corrected_record(record)
