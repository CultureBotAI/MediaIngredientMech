"""Read-only verification against the worker's frozen baseline capture."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'MAPPING_SEMANTICS.md').is_file())
OUT = ROOT / 'reports/all_unmatched_20261107/worker-03'
BASE = 'e000d66dd26ab053e9b17ce7bf8d3c873c3dde99'
baseline_path = OUT / 'validation/baseline-integrity.json'
baseline = json.loads(baseline_path.read_text())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
errors = []
actual_owners = {str(p.relative_to(ROOT)) for folder in ('mapped', 'unmapped')
                 for p in (ROOT / 'data/ingredients' / folder).glob('*.yaml')}
baseline_owners = {p for p in baseline['maintained_surfaces'] if p.startswith(('data/ingredients/mapped/', 'data/ingredients/unmapped/'))}
assert actual_owners == baseline_owners, sorted(actual_owners ^ baseline_owners)
for key in ('recipe_snapshots', 'kg_owner_records', 'maintained_surfaces'):
    root = Path(baseline['source_root']) if key == 'recipe_snapshots' else ROOT
    for path, digest in baseline[key].items():
        if sha(root / path) != digest:
            errors.append({'group': key, 'path': path})
status = subprocess.run(['git', 'diff', '--name-only', BASE, '--', 'data', 'mappings',
                         'docs/data', 'conf', 'UNIFIED_INGREDIENT_MAPPING.tsv',
                         'UNIFIED_INGREDIENT_MAPPING.provenance.json', 'qc-evidence.yaml', 'uv.lock'],
                        cwd=ROOT, check=True, capture_output=True, text=True).stdout.splitlines()
assert not status, status
assert not errors, errors
print(json.dumps({'status': 'PASS', 'checked_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  'base_commit': BASE, 'baseline_capture_sha256': sha(baseline_path),
                  'checked_counts': {k: len(baseline[k]) for k in ('recipe_snapshots', 'kg_owner_records', 'maintained_surfaces')},
                  'changed_baseline_inputs': errors, 'maintained_paths_changed_since_base': status,
                  'scientific_approval': False}, indent=2))
