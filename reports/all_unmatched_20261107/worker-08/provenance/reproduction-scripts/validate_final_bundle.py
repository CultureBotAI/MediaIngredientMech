"""Read-only combined proposal/schema/partonomy and maintained-surface checks."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import sys
import yaml
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'reports/all_unmatched_20261107/worker-08'
VALIDATION = OUT / 'validation'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    proposals = json.loads((OUT / 'proposals.json').read_text())['proposals']
    owners = {}
    payload_paths = []
    catalog = {str(p.relative_to(ROOT)): yaml.safe_load(p.read_text())
               for p in sorted((ROOT / 'data/ingredients').rglob('*.yaml'))}
    baseline = validate_component_partonomy(catalog.values())
    original_identifiers = {r['identifier'] for r in catalog.values()}
    new_ids = set()
    receipt = []
    for proposal in proposals:
        path = proposal['owner_path']
        assert path not in owners, ('duplicate proposed owner', path)
        owners[path] = proposal['proposal_id']
        capture = proposal['after_capture']
        assert capture['root'] == 'artifact'
        payload = OUT / capture['path']
        assert sha(payload) == capture['sha256']
        record = yaml.safe_load(payload.read_text())
        if proposal['kind'] == 'edit_existing_owner':
            assert sha(ROOT / path) == proposal['before_sha256']
            raw = subprocess.check_output(['git', 'show', 'e000d66dd26ab053e9b17ce7bf8d3c873c3dde99:' + path], cwd=ROOT)
            assert hashlib.sha256(raw).hexdigest() == proposal['before_sha256']
        else:
            assert proposal['kind'] == 'new_owner'
            assert not (ROOT / path).exists()
            assert record['identifier'] not in original_identifiers | new_ids
            new_ids.add(record['identifier'])
        catalog[path] = record
        payload_paths.append(str(payload.relative_to(ROOT)))
        receipt.append({'proposal_id': proposal['proposal_id'], 'kind': proposal['kind'],
                        'owner_path': path, 'after_sha256': capture['sha256'],
                        'identifier': record['identifier']})
    overlay = validate_component_partonomy(catalog.values())
    cmd = [sys.executable, 'scripts/validate_strict.py', '--workers', '2', '--out',
           str(VALIDATION / 'final-proposals-strict.tsv'), *payload_paths]
    result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    (VALIDATION / 'final-proposals-strict.log').write_text(result.stdout + result.stderr)
    before = json.loads((OUT / 'provenance/maintained-surfaces-before.json').read_text())
    paths = set()
    for dirname in ['data/ingredients', 'data/curated', 'mappings', 'docs/data']:
        paths.update(p for p in (ROOT / dirname).rglob('*') if p.is_file())
    paths.update(p for p in ROOT.glob('UNIFIED_INGREDIENT_MAPPING*') if p.is_file())
    after = {str(p.relative_to(ROOT)): sha(p) for p in sorted(paths)}
    changed = sorted(k for k in after.keys() & before['files'].keys() if after[k] != before['files'][k])
    added = sorted(after.keys() - before['files'].keys())
    removed = sorted(before['files'].keys() - after.keys())
    d = dict(at=datetime.now(timezone.utc).isoformat(), proposal_count=len(proposals),
             new_owner_count=len(new_ids), edited_owner_count=len(proposals)-len(new_ids),
             proposals=receipt, strict_command=cmd, strict_exit_code=result.returncode,
             baseline_record_count=len(catalog)-len(new_ids), overlay_record_count=len(catalog),
             baseline_partonomy_violations=list(map(str, baseline)),
             overlay_partonomy_violations=list(map(str, overlay)),
             maintained_files_checked=len(after), maintained_changed=changed,
             maintained_added=added, maintained_removed=removed,
             ignored_files_included=True, maintained_surfaces_unchanged=not(changed or added or removed),
             scientific_or_export_approval=False)
    (VALIDATION / 'combined-validation.json').write_text(json.dumps(d, indent=2)+'\n')
    print(json.dumps({k:v for k,v in d.items() if k not in ['proposals','strict_command']}, indent=2))
    assert result.returncode == 0 and not baseline and not overlay
    assert not(changed or added or removed)

if __name__ == '__main__':
    main()
