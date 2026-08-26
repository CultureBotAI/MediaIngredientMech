"""A reviewed false alias is provenance, never a resolvable synonym (#464/#470)."""

from __future__ import annotations

import csv
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


export_lists = _load("export_lists_rejected", ROOT / "scripts" / "export_lists.py")
browser_export = _load("browser_export_rejected", ROOT / "scripts" / "browser_export.py")
validator = _load(
    "validate_sssom_invariants_rejected",
    ROOT / "scripts" / "validate_sssom_invariants.py",
)


def _record():
    return {
        "identifier": "CHEBI:1",
        "preferred_term": "Reviewed material",
        "mapping_status": "MAPPED",
        "ontology_mapping": {
            "ontology_id": "CHEBI:1",
            "ontology_label": "Reviewed material",
        },
        "synonyms": [
            {
                "synonym_text": "accepted alias",
                "synonym_type": "EXACT_SYNONYM",
                "source": "review",
            },
            {
                "synonym_text": "false upstream alias",
                "synonym_type": "REJECTED_LABEL",
                "source": "upstream",
            },
        ],
    }


def test_rejected_label_is_absent_from_flat_and_browser_exports(tmp_path):
    record = _record()
    assert export_lists._synonyms(record) == ["accepted alias"]

    out = tmp_path / "labels.csv"
    export_lists.export_label_index([record], out)
    labels = {row["label"] for row in csv.DictReader(out.open())}
    assert "accepted alias" in labels
    assert "false upstream alias" not in labels

    browser = browser_export.extract_ingredient_for_browser(record, "mapped/X.yaml")
    assert browser["synonyms"] == ["accepted alias"]
    assert "false upstream alias" not in browser["searchable"]


def test_rule_e_fires_on_a_synthetic_rejected_label_leak(tmp_path, monkeypatch):
    ingredients = tmp_path / "mapped"
    ingredients.mkdir()
    (ingredients / "Reviewed.yaml").write_text(
        "identifier: CHEBI:1\n"
        "preferred_term: Reviewed material\n"
        "mapping_status: MAPPED\n"
        "synonyms:\n"
        "- synonym_text: false upstream alias\n"
        "  synonym_type: REJECTED_LABEL\n"
        "  source: upstream\n"
    )
    monkeypatch.setattr(validator, "INGREDIENTS_DIR", ingredients)
    validator._subject_to_path.cache_clear()
    validator.rejected_labels.cache_clear()
    rows = [
        {
            "subject_id": "MIM:Reviewed",
            "other": "accepted alias|FALSE UPSTREAM ALIAS",
        }
    ]

    violations = list(validator.evaluate_rule_e(rows))

    assert len(violations) == 1
    assert "false upstream alias" in violations[0][2]
    validator._subject_to_path.cache_clear()
    validator.rejected_labels.cache_clear()


def test_published_sssom_contains_no_curator_rejected_label():
    _, _, rows = validator._read_sssom(validator.DEFAULT_SSSOM)
    violations = list(validator.evaluate_rule_e(rows))
    assert not violations, violations[:3]
