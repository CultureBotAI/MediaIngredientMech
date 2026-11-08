from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, os, subprocess, sys, types
import yaml
from mediaingredientmech.validation.write_validated import validate_ingredient, write_validated_ingredient

W = Path.cwd(); S = W / '.temp/w05-buffer-parts-v1/parents'; B = W / 'reports/all_unmatched_20261107/worker-05'
V = S / 'validation-soy'; V.mkdir(exist_ok=False)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
p = next(x for x in json.loads((S / 'proposals.json').read_text())['proposals'] if x['proposal_id'] == 'W05-FINAL-MAT-032')
f = S / 'proposed/Soy_Peptone.yaml'; r = yaml.safe_load(f.read_text())
assert sha(f) == p['after_capture']['sha256'] and not validate_ingredient(r)
write_validated_ingredient(r, V / 'guarded-readback/Soy_Peptone.yaml')
assert yaml.safe_load((V / 'guarded-readback/Soy_Peptone.yaml').read_text()) == r
cmd = [str(W / '.temp/all-unmatched-worker-05/venv/bin/python'), 'scripts/validate_strict.py', str(f), '--workers', '1', '--out', str(V / 'strict-failures.tsv')]
proc = subprocess.run(cmd, capture_output=True, text=True, env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONPATH='src'))
(V / 'strict.stdout.log').write_text(proc.stdout); (V / 'strict.stderr.log').write_text(proc.stderr)
assert proc.returncode == 0
builder = W.parents[4] / '.temp/kgm-unmapped-20261107/claw/scripts/build_mim_ingredient_sssom.py'
assert sha(builder) == '38d59f42953305f6fc51e4fc24dfc59ee1919bfb961595b67a8afe9f8a46a1bc'
sys.path[:0] = [str(builder.parent), str(builder.parent.parent / 'src')]
mod = types.ModuleType('parents_soy_projection'); mod.__file__ = str(builder); sys.modules[mod.__name__] = mod
exec(compile(builder.read_bytes(), str(builder), 'exec'), mod.__dict__)
records = {str(q.relative_to(W)): yaml.safe_load(q.read_text()) for q in (W / 'data/ingredients').rglob('*.yaml')}
ps = json.loads((B / 'tellurium-polypeptone-v1/core/proposals.json').read_text())['proposals']
for q in ps:
    src = B / q['after_capture']['path']; assert sha(src) == q['after_capture']['sha256']
    records.pop(q['owner_path'], None); records[q.get('destination_owner_path', q['owner_path'])] = yaml.safe_load(src.read_text())
records[p['owner_path']] = r
owners = mod.build_owner_index({mod._mim_curie(Path(n).name): v for n, v in records.items()})
supp = []; rows = mod._row_from_yaml(W / p['owner_path'], {}, {}, {}, {}, record=r, owners=owners, suppressions=supp)
assert [(x['predicate_id'], x['object_id']) for x in rows] == [('skos:exactMatch', 'MICRO:0000181')]
blocked = ['Phytone peptone', 'Phytone peptone (BD-BBL)', 'Soytone (BD-Difco) or Phytone peptone (BD-BBL)', 'Soytone', 'Bacto Soytone', 'Properties: Undefined component']
for row in rows:
    assert not set(blocked) & set(row['other'].split('|'))
mod._check_producer_bindings()
receipt = dict(at=datetime.now(timezone.utc).isoformat(), author='/root/buffer_hepes', status='PASS', proposal_id=p['proposal_id'], after_capture=p['after_capture'], guarded_validation='PASS', strict_command=cmd, strict_exit_code=proc.returncode, builder=dict(path=str(builder), sha256=sha(builder)), full_current_W05_owner_index_records=len(records), native_rows=rows, suppressions=[str(x) for x in supp], rejected_aliases_absent=blocked, scope='Selected Soy payload only; current full W05 proposal overlay supplies the owner index. Peptone candidate remains unselected pending scientific scope triage. This technical projection is not whole-owner, source or export approval.')
(V / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(dict(status='PASS', rows=len(rows), soy_sha256=sha(f))))
