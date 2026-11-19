#!/usr/bin/env python3
"""2026-11-08, #1270: prove the public freshness wrapper checks actual stamp bytes.

Inputs: current proof module and focused regressions. Output: source-copy control
and mutation logs under .temp; no changes to working implementation or corpus.
"""
from pathlib import Path
import json
import os
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / '.temp/freshness-stamp-mutation-1270'
DEST.mkdir(parents=True, exist_ok=False)
TREE = DEST / 'source'
shutil.copytree(ROOT / 'src', TREE / 'src', ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
(TREE / 'tests').mkdir()
for name in ['__init__.py', 'test_identity_projection.py', 'test_identity_projection_frozen.py']:
    shutil.copyfile(ROOT / 'tests' / name, TREE / 'tests' / name)
(TREE / 'scripts').mkdir()
shutil.copyfile(ROOT / 'scripts/check_unified_freshness.py', TREE / 'scripts/check_unified_freshness.py')
path = TREE / 'src/mediaingredientmech/identity_projection_frozen.py'
original = path.read_text()
needle = 'stamped = stamped_snapshot(before, after, stamped_digest, stamped_count)'
if needle not in original:
    raise SystemExit('Expected wrapper gate not found')
results = []
for name in ['control', 'ignore-actual-stamped-digest']:
    if name != 'control':
        path.write_text(original.replace(needle, 'stamped = before'))
    env = dict(os.environ, PYTHONPATH=str(TREE / 'src'), PYTHONPYCACHEPREFIX=str(DEST / ('cache-' + name)))
    with (DEST / (name + '.log')).open('w') as stream:
        completed = subprocess.run([sys.executable, '-m', 'pytest', '-q', '-o', 'addopts=',
            '--confcutdir', str(TREE), str(TREE / 'tests/test_identity_projection_frozen.py')],
            cwd=TREE, env=env, stdout=stream, stderr=subprocess.STDOUT)
    results.append({'case': name, 'exit_code': completed.returncode})
    if (completed.returncode == 0) != (name == 'control'):
        raise SystemExit('Unexpected mutation result')
(DEST / 'results.json').write_text(json.dumps(results, indent=2)+'\n')
print(json.dumps(results, indent=2))
