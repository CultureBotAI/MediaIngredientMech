"""Apply eight source-reviewed, organism-scoped cellular-role repairs for #710.

Each affected assertion must still equal the captured prediction-only input.
This script does not approve any other role or refresh aggregate artifacts.
"""

from copy import deepcopy
import hashlib
import json
from pathlib import Path
import sys

import yaml

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from mediaingredientmech.validation.write_validated import (  # noqa: E402
    validate_ingredient,
    write_validated_ingredient,
)


def digest(value):
    return hashlib.sha256(value).hexdigest()


def main():
    plan = json.loads((HERE / "cellular-role-plan.json").read_text())
    prepared = []
    for item in plan["records"]:
        path = ROOT / item["source_path"]
        assert digest(path.read_bytes()) == item["before_sha256"], path
        before = yaml.safe_load(path.read_text())
        assert before["cellular_metabolic_roles"] == [item["before_assertion"]], path
        after = deepcopy(before)
        after["cellular_metabolic_roles"] = [item["after_assertion"]]
        after["curation_history"].append(
            {
                "timestamp": "2026-09-22T02:06:34+00:00",
                "curator": "codex_issue_710_semantic_evidence_review",
                "action": "CORRECTED_ROLE_EVIDENCE",
                "changes": (
                    "Added inspected primary-publication support and bounded organism/"
                    "condition context to the cellular metabolic role (#710). "
                    "Retained original computational provenance and confidence. "
                    "See reports/semantic_review_20260921/resolution/roles/"
                    "cellular-role-plan.json for the assertion-specific interpretation."
                ),
                "llm_assisted": True,
                "llm_model": "gpt-6",
            }
        )
        errors = validate_ingredient(after)
        assert not errors, (path, [e.message for e in errors])
        prepared.append((item, path, after))
    for item, path, after in prepared:
        write_validated_ingredient(after, path)
        item["after_sha256"] = digest(path.read_bytes())
    plan["applied"] = True
    (HERE / "cellular-role-plan.json").write_text(json.dumps(plan, indent=2) + "\n")
    print(f"Validated and repaired {len(prepared)} cellular role assertions")


if __name__ == "__main__":
    main()
