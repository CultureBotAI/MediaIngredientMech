"""Resume after retained artifact-output placement diagnostic; native auditor unchanged."""
from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,os
W=Path.cwd();C=W.parents[2];B=W/'reports/all_unmatched_20261107/worker-05';P=B/'buffer-parts-v1';Q=B/'dependency-route-a-confirmation-v1';V=Q/'validation';V.mkdir(parents=True,exist_ok=False)
S=W/'.temp/w05-dependency-route-a-confirmation-v1';py=str(W/'.temp/all-unmatched-worker-05/venv/bin/python');env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONPATH='src')
def run(n,cmd):
 r=subprocess.run(cmd,text=True,capture_output=True,env=env)
 for suffix,text in [('stdout.log',r.stdout),('stderr.log',r.stderr),('receipt.json',json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),command=cmd,exit_code=r.returncode),indent=2)+'\n')]:
  q=V/(n+'.'+suffix);assert not q.exists();q.write_text(text)
 print(n,r.returncode,r.stdout[:1000]);assert r.returncode==0,r.stderr
contract=json.loads((B/'contracts/frozen-baseline.json').read_text());shard=contract['queue']['shards']['5']['path']
run('exact-accounting',[py,str(C/'scripts/audit_worker_outcomes_v1.py'),'--shard',shard,'--decisions',str(P/'core/decisions.json'),'--evidence',str(P/'core/evidence.json'),'--proposals',str(P/'core/proposals.json'),'--artifact-root',str(B),'--source-root',str(Path(shard).parent.parent),'--mim-root',str(W),'--output',str(V/'exact-accounting.json')])
run('lineage',[py,str(B/'final-correction-v1/control/audit_lineage.py'),'--core',str(P/'core'),'--out',str(V/'original-lineage-audit.json')])
