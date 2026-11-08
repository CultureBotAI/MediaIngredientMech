#!/usr/bin/env python3
"""Issue #1277 (2026-11-08): verify full-inventory refusal regressions.

Inputs: retained #1265 mint helper and its synthetic-Git regression tests.
Outputs: sanitized JSON on stdout; full logs in durable .temp storage.
Each disabled guard exists only in a fresh child interpreter's module loader.
No maintained source, corpus, review, registry or Git state is changed.
Run: uv run --frozen python scripts/adhoc/check_migration_inventory_mutations_1277.py
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEST = "tests/test_stable_id_migration.py"
PROBES = (
    ("before_staging_inventory", "    require_complete_inventory(root)\n    inputs = {}",
     "    inputs = {}", "test_inventory_mismatch_refused_before_any_staging_write"),
    ("before_publication_inventory",
     "def publish(root: Path, stage: Path, inputs: dict, outputs: dict, *, apply: bool):\n    require_complete_inventory(root)\n",
     "def publish(root: Path, stage: Path, inputs: dict, outputs: dict, *, apply: bool):\n",
     "test_inventory_change_after_prepare_refused_before_transaction"),
)
CHILD = r'''
import importlib.abc,importlib.util,json,sys
from pathlib import Path
import pytest
script,old,new,test=json.loads(sys.argv[1])
script=Path(script).resolve()
source=script.read_text()
if source.count(old)!=1:
    sys.stderr.write("mutation anchor is not unique; pytest was not executed\n")
    raise SystemExit(2)
original=importlib.util.spec_from_file_location
class MutatedLoader(importlib.abc.Loader):
    def create_module(self,spec): return None
    def exec_module(self,module):
        exec(compile(source.replace(old,new,1),str(script),"exec"),module.__dict__)
def load(name,location,*args,**kwargs):
    spec=original(name,location,*args,**kwargs)
    if Path(location).resolve()==script:
        spec.loader=MutatedLoader()
    return spec
importlib.util.spec_from_file_location=load
raise SystemExit(pytest.main([test,"-q","--no-cov","--disable-warnings"]))
'''


def main() -> int:
    private = ROOT / ".temp/migration-inventory-mutations-1277"
    private.mkdir(parents=True, exist_ok=True)

    def execute(command):
        result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
        raw = (result.stdout + result.stderr).encode()
        digest = hashlib.sha256(raw).hexdigest()
        target = private / (digest + ".log")
        if target.exists() and target.read_bytes() != raw:
            raise ValueError("Private log hash collision")
        target.write_bytes(raw)
        return result, digest

    results = []
    for label, old, new, test in PROBES:
        selection = TEST + "::" + test
        baseline, baseline_digest = execute([
            sys.executable, "-m", "pytest", selection, "-q", "--no-cov", "--disable-warnings",
        ])
        mutation, mutation_digest = execute([
            sys.executable, "-c", CHILD, json.dumps([
                str(ROOT / "scripts/adhoc/mint_stable_ids_1265.py"), old, new, selection,
            ]),
        ])
        counts = re.findall(r"(?m)^(\d+) failed(?:,.*)?(?: in [0-9.]+s)?$", mutation.stdout)
        failures = int(counts[-1]) if counts else None
        killed = baseline.returncode == 0 and mutation.returncode == 1 and bool(failures)
        results.append({
            "probe": label, "test": selection, "baseline_exit": baseline.returncode,
            "baseline_log_sha256": baseline_digest, "mutation_exit": mutation.returncode,
            "mutation_log_sha256": mutation_digest, "failed_tests": failures,
            "status": "KILLED" if killed else "SURVIVED" if baseline.returncode == 0 and mutation.returncode == 0 else "ERROR",
        })
    print(json.dumps({
        "issue": "https://github.com/CultureBotAI/MediaIngredientMech/issues/1277",
        "date": "2026-11-08", "maintained_files_modified": False,
        "command": "uv run --frozen python scripts/adhoc/check_migration_inventory_mutations_1277.py",
        "probes": results,
    }, indent=2))
    return 0 if all(item["status"] == "KILLED" for item in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
