#!/usr/bin/env python3
"""2026-11-08 #1278: offline required-ID-gate contrast checks.

Inputs: a source root containing the workflow, validator and focused test.
Outputs: durable logs and exit/failure-count receipt under an explicit new path.
Only a copied source tree is changed; no provider, Git publication or session I/O.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--source-root", required=True, type=Path)
parser.add_argument("--output", required=True, type=Path)
args = parser.parse_args()
source = args.source_root.resolve()
out = args.output.resolve()
out.mkdir(exist_ok=False)
tree = out / "source"
for name in [
    ".github/workflows/validate-strict.yaml",
    "scripts/validate_stable_ids.py",
    "src/mediaingredientmech/stable_ids.py",
    "src/mediaingredientmech/__init__.py",
    "tests/test_stable_id_required_gate.py",
]:
    target = tree / name
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source / name, target)
p = tree / ".github/workflows/validate-strict.yaml"
original = p.read_text()
cases = [
    ("control", None, None),
    ("history-disabled", ' --require-history --base "$MIM_ID_BASE"', ""),
    ("shallow-history", "fetch-depth: 0", "fetch-depth: 1"),
    ("missing-ledger-trigger", "    - data/ids/**\n", ""),
    ("restored-control", None, None),
]
results = []
for name, old, new in cases:
    if old is not None and old not in original:
        raise SystemExit("Missing mutation anchor: " + name)
    p.write_text(original if old is None else original.replace(old, new))
    env = dict(
        os.environ, PYTHONPATH=str(tree / "src"), PYTHONPYCACHEPREFIX=str(out / ("cache-" + name))
    )
    command = [
        sys.executable,
        "-m",
        "pytest",
        "--confcutdir=" + str(tree),
        "-o",
        "addopts=",
        "-p",
        "no:cacheprovider",
        str(tree / "tests/test_stable_id_required_gate.py"),
        "-q",
    ]
    result = subprocess.run(
        command, cwd=tree, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    (out / (name + ".log")).write_text(result.stdout)
    match = re.search(r"\b(\d+) failed\b", result.stdout)
    failures = int(match[1]) if match else 0
    status = (
        ("PASS" if result.returncode == 0 else "ERROR")
        if old is None
        else (
            "KILLED"
            if result.returncode == 1 and failures > 0 and "ERROR collecting" not in result.stdout
            else "ERROR"
        )
    )
    results.append(
        {"case": name, "exit_code": result.returncode, "failed_tests": failures, "status": status}
    )
    (out / "results.json").write_text(json.dumps(results, indent=2) + "\n")
    if status == "ERROR":
        raise SystemExit("Unverified mutation/control: " + name)
p.write_text(original)
print(json.dumps(results, indent=2))
