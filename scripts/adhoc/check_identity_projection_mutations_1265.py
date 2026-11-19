#!/usr/bin/env python3
"""Issue #1265 (2026-11-08): prove identity-boundary regression sensitivity.

Inputs: current identity-projection modules and focused pytest cases. Outputs:
JSON probe statuses on stdout. Each mutation exists only in a fresh child Python
module namespace; no source file, record, historical review or cache is edited.
No provider or network access. Run: uv run --frozen python <this file>.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
PROBES = (
    ("duplicate_yaml_key_guard", "mediaingredientmech.identity_projection",
     'require(key not in result, "duplicate YAML record key")', "pass",
     "tests/test_identity_projection.py::test_rehashed_duplicate_scientific_yaml_key_is_refused"),
    ("complete_mint_inventory_authority", "mediaingredientmech.identity_projection_bundle",
     "inventory.validate(sources[inventory.INVENTORY], manifest, registry)", "None",
     "tests/test_identity_projection_bundle.py::test_coherently_shifted_complete_mint_inventory_is_not_portable_authority"),
    ("freshness_prior_drift", "mediaingredientmech.identity_projection_frozen",
     "and stamped[name] in (before[name], after[name])", "and True",
     "tests/test_identity_projection_frozen.py::test_frozen_initial_transition_independent_of_subsequent_current_edits"),
    ("freshness_later_drift", "mediaingredientmech.identity_projection_frozen",
     "and current[name] == after[name]", "and True",
     "tests/test_identity_projection_frozen.py::test_frozen_initial_transition_independent_of_subsequent_current_edits"),
    ("record_science_guard", "mediaingredientmech.identity_projection",
     "exact(restored, old)", "True",
     "tests/test_identity_projection.py::test_rehashed_record_mutations_are_not_identity_only[biology]"),
    ("sssom_subject_only_guard", "mediaingredientmech.identity_projection",
     'new_row == dict(old_row, subject_id=aliases[old_row["subject_id"]])', "True",
     "tests/test_identity_projection.py::test_rehashed_mapping_mutation_refused"),
    ("negative_hold_preservation", "mediaingredientmech.identity_projection_graph",
     "        projected.append(\n", '        decision = dict(decision, resolution_status="APPROVED")\n        projected.append(\n',
     "tests/test_identity_projection_graph.py::test_identity_projection_never_promotes_negative_disposition"),
)
CHILD = r'''
import importlib.util,json,sys
import pytest
name, old, new, test = json.loads(sys.argv[1])
spec = importlib.util.find_spec(name)
source = open(spec.origin).read()
if source.count(old) != 1:
    sys.stderr.write("mutation anchor is not unique; pytest was not executed\n")
    raise SystemExit(2)
module = importlib.util.module_from_spec(spec)
sys.modules[name] = module
exec(compile(source.replace(old,new,1),spec.origin,"exec"),module.__dict__)
raise SystemExit(pytest.main([test,"-q","--no-cov"]))
'''


def mutation_status(baseline_exit: int, mutation_exit: int, failed_tests: int | None) -> str:
    if baseline_exit != 0:
        return "ERROR"
    if mutation_exit == 1 and failed_tests is not None and failed_tests > 0:
        return "KILLED"
    if mutation_exit == 0:
        return "SURVIVED"
    return "ERROR"


def mutation_was_killed(baseline_exit: int, mutation_exit: int, failed_tests: int | None) -> bool:
    return mutation_status(baseline_exit, mutation_exit, failed_tests) == "KILLED"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--probe", choices=[probe[0] for probe in PROBES])
    args = parser.parse_args()
    results = []
    private = ROOT / ".temp/stable-id-projection-mutations"
    private.mkdir(parents=True, exist_ok=True)
    for label, module, old, new, test in PROBES:
        if args.probe and args.probe != label:
            continue
        baseline = subprocess.run([sys.executable, "-m", "pytest", test, "-q", "--no-cov", "--disable-warnings"], cwd=ROOT, text=True, capture_output=True, check=False)
        baseline_raw = (baseline.stdout + baseline.stderr).encode()
        baseline_digest = hashlib.sha256(baseline_raw).hexdigest()
        baseline_log = private / (baseline_digest + ".log")
        if not baseline_log.exists():
            baseline_log.write_bytes(baseline_raw)
        elif baseline_log.read_bytes() != baseline_raw:
            raise ValueError("Private baseline log hash collision")
        result = subprocess.run([sys.executable, "-c", CHILD, json.dumps([module, old, new, test])],
                                cwd=ROOT, text=True, capture_output=True, check=False)
        raw = (result.stdout + result.stderr).encode()
        digest = hashlib.sha256(raw).hexdigest()
        log = private / (digest + ".log")
        if log.exists():
            if log.read_bytes() != raw:
                raise ValueError("Private mutation log hash collision")
        else:
            log.write_bytes(raw)
        summaries = re.findall(r"(?m)^(\d+) failed(?:,.*)?(?: in [0-9.]+s)?$", result.stdout)
        failed_tests = int(summaries[-1]) if summaries else None
        results.append({"probe": label, "test": test,
                        "command": ["uv", "run", "--frozen", "python",
                                    "scripts/adhoc/check_identity_projection_mutations_1265.py", "--probe", label],
                        "baseline_exit_code": baseline.returncode, "baseline_output_sha256": baseline_digest,
                        "exit_code": result.returncode, "failed_tests": failed_tests,
                        "status": mutation_status(baseline.returncode, result.returncode, failed_tests),
                        "mutation_killed": mutation_was_killed(baseline.returncode, result.returncode, failed_tests),
                        "full_output_sha256": digest})
    print(json.dumps({"issue": "https://github.com/CultureBotAI/MediaIngredientMech/issues/1265",
                      "findings": ["https://github.com/CultureBotAI/MediaIngredientMech/issues/1269",
                                   "https://github.com/CultureBotAI/MediaIngredientMech/issues/1273",
                                   "https://github.com/CultureBotAI/MediaIngredientMech/issues/1274"],
                      "date": "2026-11-08", "source_files_modified": False, "probes": results}, indent=2))
    if not all(result["mutation_killed"] for result in results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
