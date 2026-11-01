"""Fresh-process proofs that the preserved #1039 parser loses real TSV rows."""

from __future__ import annotations

import ast
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
SOURCE = RUN / "analyze_step3_final.py"
ORIGINAL = HERE / "original/analyze_step3_final.py"
TESTS = HERE / "test_analyzer_parser.py"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, text):
    with path.open("x") as stream:
        stream.write(text)


def main():
    destination = HERE / "negative-controls"
    destination.mkdir(exist_ok=False)
    frozen = sha(SOURCE)
    assert frozen == sha(HERE / "fixed/analyze_step3_final.py")
    assert sha(ORIGINAL) == "38790edcb9f5a8fb6439827ed74905a7b1aaaa0fda1c3c32ed5749bb5b66958a"
    artifact = RUN / "step3-mim/UNIFIED_INGREDIENT_MAPPING.tsv"
    artifact_before = sha(artifact)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    original_probe = """import gzip, importlib.util, json, sys
from pathlib import Path
sys.dont_write_bytecode = True
source, fixture = map(Path, sys.argv[1:])
spec = importlib.util.spec_from_file_location('original_analyzer_1039_probe', source)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
fields, rows = module.table(gzip.decompress(fixture.read_bytes()))
counts = {'rows': len(rows), 'occurrences': sum(int(row['occurrence_count']) for row in rows)}
print(json.dumps(counts), flush=True)
assert counts == {'rows': 4170, 'occurrences': 209330}, 'Original parser loses hash-prefixed data: ' + repr(counts)
"""
    original_command = [sys.executable, "-c", original_probe, str(ORIGINAL), str(HERE / "fixtures/unified-after.tsv.gz")]
    original = subprocess.run(original_command, env=env, text=True, capture_output=True)
    write(destination / "original-parser.stdout", original.stdout)
    write(destination / "original-parser.stderr", original.stderr)
    assert original.returncode == 1
    assert json.loads(original.stdout) == {"rows": 4166, "occurrences": 209323}
    assert "AssertionError: Original parser loses hash-prefixed data" in original.stderr
    assert "ImportError" not in original.stderr and "ModuleNotFoundError" not in original.stderr

    fixed_text = SOURCE.read_text()
    fixed_tree, old_tree = ast.parse(fixed_text), ast.parse(ORIGINAL.read_text())
    fixed_table = next(node for node in fixed_tree.body if isinstance(node, ast.FunctionDef) and node.name == "table")
    old_table = next(node for node in old_tree.body if isinstance(node, ast.FunctionDef) and node.name == "table")
    old_assignment = ast.get_source_segment(ORIGINAL.read_text(), old_table.body[0])
    reader = next(node for node in fixed_table.body if isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id == "reader" for target in node.targets))
    # Retain the new keyword-only API, but restore the exact original global
    # hash-line stripping assignment. Failures must be behavioral, not an API
    # TypeError or an import/setup failure.
    start = fixed_table.body[1].lineno - 1  # after the function docstring
    stop = reader.lineno - 1
    lines = fixed_text.splitlines(keepends=True)
    mutated = "".join([*lines[:start], "    " + old_assignment + "\n", *lines[stop:]])
    ast.parse(mutated)
    mutant = destination / "old-parser-with-current-api.py"
    write(mutant, mutated)
    mutation_env = dict(env, ANALYZER_1039_SOURCE=str(mutant), PYTHONPYCACHEPREFIX=str(destination / "unused-bytecode-cache"))
    mutant_command = [sys.executable, "-m", "pytest", "-q", "-o", "addopts=", "-p", "no:cacheprovider", str(TESTS)]
    mutant_result = subprocess.run(mutant_command, env=mutation_env, text=True, capture_output=True, cwd=RUN / "step3-mim")
    write(destination / "mutant-tests.stdout", mutant_result.stdout)
    write(destination / "mutant-tests.stderr", mutant_result.stderr)
    assert mutant_result.returncode == 1
    assert re.search(r"21 failed, 2 passed", mutant_result.stdout), mutant_result.stdout[-2000:]
    assert "ERROR collecting" not in mutant_result.stdout
    assert "ModuleNotFoundError" not in mutant_result.stdout + mutant_result.stderr
    assert "unexpected keyword argument" not in mutant_result.stdout + mutant_result.stderr
    assert sha(SOURCE) == frozen == sha(HERE / "fixed/analyze_step3_final.py")
    assert sha(artifact) == artifact_before
    result = {
        "issue": "https://github.com/CultureBotAI/MediaIngredientMech/issues/1039",
        "original_parser": {"sha256": sha(ORIGINAL), "return_code": original.returncode, "counts": json.loads(original.stdout), "failure": "assertion on expected full native counts", "fresh_process": True},
        "old_parser_current_api_mutant": {"sha256": sha(mutant), "return_code": mutant_result.returncode, "failed": 21, "passed": 2, "setup_or_api_failure": False, "fresh_process": True},
        "fixed_analyzer_sha256": frozen,
        "fixed_source_unchanged": True,
        "production_unified_sha256": artifact_before,
        "production_unified_unchanged": True,
        "note": "The original raw-byte preservation guard already rejected mutations to excluded lines. The fix repairs population/count reporting and makes those rows visible to parsed semantic checks; it does not repair an altered production artifact.",
        "logs": {path.name: sha(path) for path in sorted(destination.iterdir()) if path.is_file()},
    }
    write(destination / "receipt.json", json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
