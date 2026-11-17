"""#1431: standalone exports load without LinkML; companions still require it."""

import os
import subprocess
import sys
from pathlib import Path

import pytest

from tests.test_occurrence_coverage import write_bundle

ROOT = Path(__file__).resolve().parents[1]
BOOT = """
import importlib.abc
import json
from pathlib import Path
import runpy
import sys

root, fixture = map(Path, sys.argv[1:3])
sys.path.insert(0, str(root / 'src'))

class NoLinkML(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname == 'linkml' or fullname.startswith('linkml.'):
            raise ModuleNotFoundError('test: LinkML unavailable', name=fullname)

sys.meta_path.insert(0, NoLinkML())
"""


def run_without_validator(code, fixture):
    result = subprocess.run(
        [sys.executable, "-B", "-c", BOOT + code, str(ROOT), str(fixture)],
        cwd=ROOT,
        env={**os.environ, "PYTHONPATH": str(ROOT / "src")},
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert result.returncode == 0, result.stdout + result.stderr


@pytest.mark.parametrize(
    "consumer,invocation,count_key",
    [
        ("export_lists", "api['export_to_json']([record], output)", "total_occurrences"),
        ("generate_index_files", "api['generate_json_index']([record], output)", "occurrences"),
        (
            "browser_export",
            "output.write_text(json.dumps([api['extract_ingredient_for_browser'](record, 'record.yaml')]))",
            "total_occurrences",
        ),
    ],
)
def test_lightweight_exports_preserve_missing_and_zero_without_linkml(
    tmp_path, consumer, invocation, count_key
):
    run_without_validator(
        f"""
from mediaingredientmech.occurrence_coverage import default_coverage
assert default_coverage(fixture) is None
api = runpy.run_path(str(root / 'scripts' / '{consumer}.py'))
record = {{'mim_id': 'MIM:0000001', 'identifier': 'UNMAPPED_1',
           'preferred_term': 'material', 'mapping_status': 'UNMAPPED'}}
output = fixture / 'output.json'
for known in (False, True):
    if known:
        record['occurrence_statistics'] = {{'media_count': 0, 'total_occurrences': 0}}
    {invocation}
    actual = json.loads(output.read_text())[0]
    assert actual['{count_key}'] == (0 if known else None), actual
    assert actual['occurrence_statistics_state'] == ('RECORDED' if known else 'MISSING')
assert not any(name == 'linkml' or name.startswith('linkml.') for name in sys.modules)
""",
        tmp_path,
    )


def test_present_companion_refuses_missing_validator_in_fresh_process(tmp_path):
    write_bundle(tmp_path)
    run_without_validator(
        """
from mediaingredientmech.occurrence_coverage import default_coverage
try:
    default_coverage(fixture)
except ModuleNotFoundError as exc:
    assert exc.name == 'linkml', repr(exc)
else:
    raise AssertionError('Companion accepted without its validator')
""",
        tmp_path,
    )
