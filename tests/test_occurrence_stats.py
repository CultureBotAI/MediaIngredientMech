"""Guard test: occurrence_statistics stay consistent in the curated collection.

Asserts no record is missing occurrence_statistics, no REJECTED record reports
occurrences, no negative counts, and media_count never exceeds total_occurrences.
"""

import importlib.util
import sys
from pathlib import Path

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
    issues = audit.find_issues(data["ingredients"])
    assert all(len(v) == 0 for v in issues.values()), (
        "occurrence_statistics inconsistencies found:\n"
        + "\n".join(f"  {k}: {v}" for k, v in issues.items() if v)
    )
