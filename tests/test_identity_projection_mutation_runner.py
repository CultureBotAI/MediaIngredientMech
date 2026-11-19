"""A mutation setup failure must never be reported as a killed regression."""
import importlib.util
from pathlib import Path

import pytest

spec = importlib.util.spec_from_file_location("projection_mutation_runner", Path(__file__).parents[1] / "scripts/adhoc/check_identity_projection_mutations_1265.py")
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


@pytest.mark.parametrize("baseline,mutation,failures,expected", [
    (0, 1, 1, True), (0, 1, None, False), (0, 1, 0, False),
    (1, 1, 1, False), (0, 2, 1, False), (0, 0, 0, False),
])
def test_only_a_passing_baseline_and_real_mutated_test_failure_count_as_killed(baseline, mutation, failures, expected):
    assert runner.mutation_was_killed(baseline, mutation, failures) is expected


def test_missing_mutation_anchor_is_error_before_pytest():
    import json
    import subprocess
    import sys
    result = subprocess.run([sys.executable, "-c", runner.CHILD, json.dumps([
        "mediaingredientmech.identity_projection_inventory", "MISSING_ANCHOR_1274", "None",
        "tests/not_a_real_test.py",
    ])], capture_output=True, text=True, check=False)
    assert result.returncode == 2
    assert "pytest was not executed" in result.stderr
    assert runner.mutation_status(0, result.returncode, None) == "ERROR"
