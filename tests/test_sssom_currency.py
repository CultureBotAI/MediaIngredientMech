"""Guard test: the SSSOM mapping set stays in sync with the curated collection.

The SSSOM has no full generator (its provenance columns encode pipeline-run state
absent from the curated YAML), so it is reconciled by scripts/reconcile_sssom.py.
This asserts there is zero drift — no mapped record missing from the set, no
orphaned/REJECTED subject still present, and no subject pointing at a superseded
ontology_id. It complements test_role_plausibility and the SSSOM invariant gate.
"""

import importlib.util
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "src"))


def _load_reconciler():
    spec = importlib.util.spec_from_file_location(
        "reconcile_sssom", ROOT / "scripts" / "reconcile_sssom.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_sssom_in_sync_with_curated():
    rec = _load_reconciler()
    curated = yaml.safe_load((ROOT / "data" / "curated" / "mapped_ingredients.yaml").read_text())
    _, _, _, rows = rec._read_sssom()
    drift = rec.find_drift(curated, rows)
    assert drift == {"gaps": [], "orphans": [], "stale": []}, (
        "SSSOM has drifted from the curated data. Reconcile with "
        "`python scripts/reconcile_sssom.py --apply --date <YYYY-MM-DD>`.\n"
        f"  gaps={drift['gaps']}\n  orphans={drift['orphans']}\n  stale={drift['stale']}"
    )
