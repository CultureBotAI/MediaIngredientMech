"""Guard test: no chemically-implausible role assignments in the curated data.

Runs the narrow-definition role plausibility audit (scripts/audit_role_plausibility.py)
over the curated collection and asserts it finds nothing. Catches regressions like a
mineral salt tagged BUFFER or a chelator tagged AMINO_ACID_SOURCE.
"""

import importlib.util
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "src"))


def _load_audit():
    spec = importlib.util.spec_from_file_location(
        "audit_role_plausibility", ROOT / "scripts" / "audit_role_plausibility.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_no_implausible_role_assignments():
    audit = _load_audit()
    data = yaml.safe_load((ROOT / "data" / "curated" / "mapped_ingredients.yaml").read_text())
    flagged = audit.find_implausible(data)
    assert flagged == [], (
        "Chemically-implausible role assignments found:\n"
        + "\n".join(
            f"  [{slot}.{role}] {name} ({ident}) <- {srcs}"
            for role, slot, name, ident, srcs in flagged
        )
    )
