#!/usr/bin/env python3
"""#1281, 2026-11-08: prove full graph replay has no local-output prerequisite.

Input: tests/test_identity_projection_graph.py and the current native corpus,
exporter and immutable historical proof. Output: fresh-process control and
missing-native-export mutation logs plus hashes in the requested report directory.
Copies and native Git/graph fixtures stay under repository .temp; no maintained
source/corpus edits, remote Git operations, providers or network calls occur.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEST = "tests/test_identity_projection_graph.py"
SELECTED = "test_complete_graph_and_negative_review_replay_against_fixed_baseline"
EXPORT_SETUP = '    manifest = export_graph(root, isolated_bundle)\n    assert set(manifest["inputs"]) <= inputs\n    for name in manifest["implementation"]:\n        copy_input("src/mediaingredientmech/" + name)\n'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    output = args.output.resolve()
    output.relative_to(ROOT / "reports/stable_ids_1265_20261108")
    output.mkdir(parents=True, exist_ok=False)
    copies = ROOT / ".temp" / ("hermetic-graph-1281-" + output.name)
    copies.mkdir(parents=True, exist_ok=False)
    source = (ROOT / TEST).read_text()
    assert source.count(EXPORT_SETUP) == 1, "Native export setup changed; inspect the mutation"
    anchor = "ROOT = Path(__file__).resolve().parents[1]"
    assert source.count(anchor) == 1
    isolated_source = source.replace(anchor, f"ROOT = Path({str(ROOT)!r})")
    inputs = {TEST: digest(ROOT / TEST),
              "src/mediaingredientmech/identity_projection_graph.py": digest(
                  ROOT / "src/mediaingredientmech/identity_projection_graph.py"),
              "src/mediaingredientmech/export/kgx.py": digest(
                  ROOT / "src/mediaingredientmech/export/kgx.py")}
    results = []
    for name in ("control", "native_export_removed"):
        tree = copies / name
        tree.mkdir()
        case = tree / "test_graph.py"
        case.write_text(isolated_source if name == "control" else
                        isolated_source.replace(EXPORT_SETUP, ""))
        env = dict(os.environ, PYTHONPATH=str(ROOT / "src"),
                   PYTHONDONTWRITEBYTECODE="1",
                   PYTHONPYCACHEPREFIX=str(tree / "bytecode"))
        command = [sys.executable, "-B", "-m", "pytest", "-q", "-c", "/dev/null",
                   "-p", "no:cacheprovider", "--confcutdir", str(tree),
                   "--basetemp", str(tree / "pytest"), str(case) + "::" + SELECTED]
        run = subprocess.run(command, cwd=tree, env=env, text=True,
                             capture_output=True, timeout=600)
        raw = run.stdout + run.stderr
        (output / (name + ".log")).write_text(
            raw.replace(str(ROOT), "<repo>").replace(str(Path.home()), "<home>"))
        expected = (run.returncode == 0 if name == "control" else
                    run.returncode == 1 and "FileNotFoundError" in raw
                    and "output/mim-kgx-710-full/manifest.json" in raw)
        results.append({"case": name, "exit_code": run.returncode,
                        "expected_result": expected, "log": name + ".log"})
        receipt = {"issue": "https://github.com/CultureBotAI/MediaIngredientMech/issues/1281",
                   "observed_at": datetime.now(timezone.utc).isoformat(),
                   "source_head": subprocess.check_output(
                       ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
                   "input_sha256": inputs,
                   "helper_sha256": digest(Path(__file__)), "results": results,
                   "source_or_corpus_mutations": False,
                   "network_or_provider_calls": False}
        (output / "results.json").write_text(json.dumps(receipt, indent=2) + "\n")
        print(json.dumps(results[-1]), flush=True)
        if not expected:
            raise SystemExit("Unexpected result; inspect " + name + ".log")
    assert all(digest(ROOT / name) == value for name, value in inputs.items())


if __name__ == "__main__":
    main()
