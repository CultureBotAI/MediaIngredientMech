#!/usr/bin/env python3
"""Retain exact pre-ID graph validation inputs for #1265 (2026-11-08).

Inputs: the fixed source Git commit and its immutable scientific review.
Outputs: durable .temp source archive, original graph artifacts and exit-code log.
No provider calls or current scientific approvals are produced.
"""
from pathlib import Path
import json
import os
import subprocess
import sys

BASE = '0dac278466699129a083343a921c2e0ca18a9ab4'
ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / '.temp/pre-id-baseline-1265'
if DEST.exists():
    raise SystemExit('Refusing to overwrite retained baseline')
DEST.mkdir(parents=True)
archive = subprocess.Popen(['git', 'archive', BASE], cwd=ROOT, stdout=subprocess.PIPE)
extract = subprocess.run(['tar', '-x', '-C', str(DEST)], stdin=archive.stdout, check=False)
archive.stdout.close()
if archive.wait() or extract.returncode:
    raise SystemExit('Baseline extraction failed')
env = dict(os.environ, PYTHONPATH=str(DEST / 'src'))
commands = [
    ['-m', 'mediaingredientmech.export.kgx', '--repo-root', '.', '--output', 'output/mim-kgx-710-full'],
    ['-m', 'mediaingredientmech.validation.semantic_release', '--root', '.', '--report',
     'reports/semantic_review_20260921/resolution/current-review.json'],
]
results = []
for number, command in enumerate(commands):
    log = DEST / f'replay-{number}.log'
    with log.open('w') as stream:
        completed = subprocess.run([sys.executable, *command], cwd=DEST, env=env,
                                   stdout=stream, stderr=subprocess.STDOUT, check=False)
    results.append({'command': command, 'exit_code': completed.returncode, 'log': log.name})
    (DEST / 'replay.json').write_text(json.dumps({'source_commit': BASE, 'results': results}, indent=2)+'\n')
    if completed.returncode:
        raise SystemExit(completed.returncode)
print(json.dumps({'baseline': '.temp/pre-id-baseline-1265', 'results': results}, indent=2))
