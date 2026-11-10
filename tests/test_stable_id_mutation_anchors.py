"""Keep the current-source stable-ID mutation controls executable (#1302)."""

import ast
import runpy
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "scripts/adhoc/check_stable_id_consumer_mutations_20261108.py"
CASES = runpy.run_path(str(RUNNER))["CASES"]


@pytest.mark.parametrize("case", CASES, ids=[case[0] for case in CASES])
def test_consumer_mutation_has_one_current_anchor_and_valid_target(case):
    name, relative, old, new, test = case
    source = (ROOT / relative).read_text()
    assert source.count(old) == 1, (name, source.count(old))
    assert old != new
    ast.parse(source.replace(old, new, 1), filename=relative)
    test_path, test_name = test.split("::")
    definitions = ast.parse((ROOT / test_path).read_text())
    assert any(
        isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == test_name
        for node in definitions.body
    ), (name, test)
