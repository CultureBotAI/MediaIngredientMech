#!/usr/bin/env python3
"""2026-11-08, #1265: replay exact native exports after stable-ID source freeze.

Inputs: current corpus, immutable historical scientific reviews, ID proof.
Outputs: fresh owned output directories, durable logs and JSON command receipt.
Prior task-owned outputs are retained under .temp; no original review is changed.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--run-name', required=True)
args = parser.parse_args()
if not args.run_name.replace('-', '').isalnum():
    raise SystemExit('run name must be alphanumeric with optional hyphens')
dest = ROOT / '.temp' / args.run_name
dest.mkdir(exist_ok=False)
for name in ('mim-kgx-710-full', 'mim-kgx-710-supported', 'mim-reviewed-sssom', 'mim-reviewed-ingredient-bundle'):
    source = ROOT / 'output' / name
    if source.exists():
        source.rename(dest / ('prior-' + name))
report = 'reports/stable_ids_1265_20261108/'
commands = [
 ['-m', 'mediaingredientmech.export.kgx', '--output', 'output/mim-kgx-710-full'],
 ['-m', 'mediaingredientmech.identity_projection', '--graph', '--replace-derived'],
 ['-m', 'mediaingredientmech.identity_projection', '--graph', '--check'],
 ['-m', 'mediaingredientmech.export.reviewed_sssom', '--review', report+'mapping-review.json', '--output', 'output/mim-reviewed-sssom'],
 ['-m', 'mediaingredientmech.export.reviewed_sssom', '--review', report+'mapping-review.json', '--output', 'output/mim-reviewed-sssom', '--validate-only'],
 ['scripts/validate_reviewed_sssom_schema.py', 'output/mim-reviewed-sssom'],
 ['-m', 'mediaingredientmech.export.ingredient_bundle', 'export', '--review', report+'companion-review.json', '--output', 'output/mim-reviewed-ingredient-bundle'],
 ['-m', 'mediaingredientmech.export.supported_kgx', '--root', '.', '--report', report+'semantic-review.json', '--output', 'output/mim-kgx-710-supported'],
 ['-m', 'mediaingredientmech.export.supported_kgx', '--root', '.', '--report', report+'semantic-review.json', '--output', 'output/mim-kgx-710-supported', '--validate-only'],
]
results = []
for number, command in enumerate(commands):
    log = dest / f'{number:02}.log'
    with log.open('w') as stream:
        result = subprocess.run([sys.executable, *command], cwd=ROOT, stdout=stream, stderr=subprocess.STDOUT)
    results.append({'command': ['python', *command], 'exit_code': result.returncode, 'log': log.name})
    (dest / 'results.json').write_text(json.dumps({'issue':1265, 'results': results}, indent=2)+'\n')
    print(f'{number}: exit {result.returncode}', flush=True)
    if result.returncode:
        raise SystemExit(result.returncode)
