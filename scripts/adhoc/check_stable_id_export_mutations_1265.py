#!/usr/bin/env python3
"""Offline source-copy regressions for #1265 migration/export distinctions.

2026-11-08; inputs: current source and focused tests. Outputs: durable .temp
mutation logs and JSON receipt. Never modifies the working implementation.
"""
from pathlib import Path
import json
import os
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / '.temp/stable-id-export-mutations'
DEST.mkdir(parents=True, exist_ok=False)
TREE = DEST / 'source'
for folder in ('src', 'scripts'):
    shutil.copytree(ROOT / folder, TREE / folder, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
(TREE / 'tests').mkdir()
shutil.copytree(ROOT / 'tests/fixtures', TREE / 'tests/fixtures')
TESTS = ['test_stable_id_migration.py', 'test_stable_id_exports.py', 'test_kgx_export.py']
for name in TESTS:
    shutil.copyfile(ROOT / 'tests' / name, TREE / 'tests' / name)
mutants = [
    ('omit-placeholder-alias', 'scripts/adhoc/mint_stable_ids_1265.py',
     'mim_curie_for_stem(Path(path).stem), record["identifier"],',
     'mim_curie_for_stem(Path(path).stem),'),
    ('change-mapping-status', 'scripts/adhoc/mint_stable_ids_1265.py',
     '    result = deepcopy(record)', '    result = deepcopy(record)\n    result["mapping_status"] = "MAPPED"'),
    ('unmapped-derived-identity', 'src/mediaingredientmech/export/kgx.py',
     '        elif status in {"UNMAPPED", "AMBIGUOUS"}:\n            identifier = record["mim_id"]',
     '        elif status in {"UNMAPPED", "AMBIGUOUS"}:\n            identifier = "MIM.unmapped:" + record["identifier"]'),
    ('sssom-filename-owner', 'scripts/validate_sssom_invariants.py',
     'subject = record.get("mim_id") or f"MIM:{escaped}"', 'subject = f"MIM:{escaped}"'),
    ('numeric-local-registry-slug', 'scripts/validate_sssom_invariants.py',
     '    if re.fullmatch(r"MIM:[0-9]{7}", subject_id):',
     '    if False and re.fullmatch(r"MIM:[0-9]{7}", subject_id):'),
    ('omit-flat-id', 'scripts/export_lists.py',
     '"mim_id": ing.get("mim_id", ""),', '"mim_id": "",'),
    ('jsonld-mapping-identity', 'src/mediaingredientmech/schema/mediaingredientmech.yaml',
     '      mim_id:\n        identifier: true', '      mim_id:\n        identifier: false'),
]
command = [sys.executable, '-m', 'pytest', '-q', '-o', 'addopts=', '--confcutdir', str(TREE),
           *[str(TREE / 'tests' / name) for name in TESTS]]
results = []
for name, relative, old, new in [('control', None, None, None), *mutants]:
    path = TREE / relative if relative else None
    original = path.read_text() if path else None
    if path:
        if old not in original:
            raise SystemExit(f'Mutation target absent: {name}')
        path.write_text(original.replace(old, new))
    env = dict(os.environ, PYTHONPATH=str(TREE / 'src'), PYTHONPYCACHEPREFIX=str(DEST / ('cache-' + name)))
    with (DEST / f'{name}.log').open('w') as stream:
        result = subprocess.run(command, cwd=TREE, env=env, stdout=stream, stderr=subprocess.STDOUT)
    if path:
        path.write_text(original)
    results.append({'mutation': name, 'exit_code': result.returncode,
                    'expected': 'pass' if name == 'control' else 'fail'})
    (DEST / 'results.json').write_text(json.dumps(results, indent=2) + '\n')
    if (result.returncode == 0) != (name == 'control'):
        raise SystemExit(f'Unexpected mutation result: {name}')
print(json.dumps(results, indent=2))
