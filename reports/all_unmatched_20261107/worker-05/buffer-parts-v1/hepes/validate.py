from pathlib import Path
from datetime import datetime, timezone
import json,hashlib,os,subprocess
import yaml
from mediaingredientmech.validation.write_validated import validate_ingredient,write_validated_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy

W=Path.cwd();B=W/'reports/all_unmatched_20261107/worker-05';S=W/'.temp/w05-buffer-parts-v1/hepes';V=S/'validation'
V.mkdir(exist_ok=False)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ps=json.loads((S/'input/selected-proposals.json').read_text())['proposals'];checks=[];records=[]
for p in ps:
    path=B/p['after_capture']['path'];assert sha(path)==p['after_capture']['sha256']
    record=yaml.safe_load(path.read_text());assert 'components' not in record and 'component_assertion' not in record
    errors=validate_ingredient(record);assert not errors
    dest=V/'guarded-readback'/path.name
    write_validated_ingredient(record,dest)
    assert yaml.safe_load(dest.read_text())==record
    records.append(record)
    checks.append(dict(proposal_id=p['proposal_id'],selected_capture=p['after_capture'],guarded_readback=dict(path=str(dest.relative_to(S)),sha256=sha(dest)),closed_schema='PASS',parsed_readback_equal=True,selected_payload_unchanged=True))
violations=validate_component_partonomy(records);assert not violations
cmd=[str(W/'.temp/all-unmatched-worker-05/venv/bin/python'),'scripts/validate_strict.py']+[str((B/p['after_capture']['path']).relative_to(W)) for p in ps]+['--workers','1','--out',str(V/'strict-failures.tsv')]
r=subprocess.run(cmd,capture_output=True,text=True,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONPATH='src'))
(V/'strict.stdout.log').write_text(r.stdout);(V/'strict.stderr.log').write_text(r.stderr)
receipt=dict(at=datetime.now(timezone.utc).isoformat(),author='/root/buffer_hepes',status='PASS' if r.returncode==0 else 'FAIL',selected_payloads=checks,strict_command=cmd,strict_exit_code=r.returncode,native_component_partonomy_violations=[str(x) for x in violations],scope='Two complete unchanged selected source proposal payloads; no maintained writes. Full selected142-proposal baseline overlay and native projection remain root-owned.',implementations=[dict(path=n,sha256=sha(W/n)) for n in ['src/mediaingredientmech/validation/write_validated.py','src/mediaingredientmech/schema/mediaingredientmech.yaml','src/mediaingredientmech/validation/component_partonomy.py','scripts/validate_strict.py']])
(V/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(dict(status=receipt['status'],payloads=len(checks),strict_exit_code=r.returncode)));assert r.returncode==0
