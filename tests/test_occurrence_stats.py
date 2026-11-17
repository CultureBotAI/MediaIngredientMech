"""Guard test: occurrence_statistics stay consistent in the curated collection.

Asserts every record has valid counts or explicit verified UNKNOWN coverage; no REJECTED record reports
occurrences, no negative counts, and media_count never exceeds total_occurrences.
"""

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "src"))


def _load_audit():
    spec = importlib.util.spec_from_file_location(
        "audit_occurrence_stats", ROOT / "scripts" / "audit_occurrence_stats.py"
    )
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_occurrence_stats_consistent():
    audit = _load_audit()
    data = yaml.safe_load((ROOT / "data" / "curated" / "mapped_ingredients.yaml").read_text())
    issues = audit.find_issues(data["ingredients"], audit.default_coverage(ROOT))
    assert all(len(v) == 0 for v in issues.values()), (
        "occurrence_statistics inconsistencies found:\n"
        + "\n".join(f"  {k}: {v}" for k, v in issues.items() if v)
    )


def test_backfill_refuses_unproven_zero_and_preserves_shared_identifier_siblings():
    audit = _load_audit()
    dry = {
        "identifier": "CHEBI:1",
        "preferred_term": "salt",
        "mapping_status": "MAPPED",
        "occurrence_statistics": {"total_occurrences": 4, "media_count": 2},
    }
    wet = {
        "identifier": "CHEBI:1",
        "preferred_term": "salt hydrate",
        "mapping_status": "MAPPED",
    }
    records = [dry, wet]
    issues = audit.find_issues(records)

    assert issues["missing"] == [("CHEBI:1", "salt hydrate")]
    with pytest.raises(ValueError, match="Cannot infer zero"):
        audit.backfill_missing(records, issues["missing"])
    assert dry["occurrence_statistics"] == {"total_occurrences": 4, "media_count": 2}
    assert "occurrence_statistics" not in wet
