from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,os,hashlib
W=Path.cwd();S=W/'.temp/w05-buffer-parts-v1';B=W/'reports/all_unmatched_20261107/worker-05';P=B/'buffer-parts-v1';C=W.parents[2];j=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();py=str(W/'.temp/all-unmatched-worker-05/venv/bin/python');env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONPATH='src');V=P/'validation'
base=j(B/'contracts/frozen-baseline.json');shard=base['queue']['shards']['5']['path']
# Original exact contract artifact/source roots are retained.
contract=j(B/'contracts/frozen-baseline.json')
source_root=Path(shard).parent.parent
commands=[('final-structural-audit',[py,str(C/'scripts/audit_worker_outcomes_v1.py'),'--shard',shard,'--decisions',str(P/'core/decisions.json'),'--evidence',str(P/'core/evidence.json'),'--proposals',str(P/'core/proposals.json'),'--artifact-root',str(B),'--source-root',str(source_root),'--mim-root',str(W),'--output',str(V/'final-structural-audit.json')]),('lineage',[py,str(B/'final-correction-v1/control/audit_lineage.py'),'--core',str(P/'core'),'--out',str(V/'original-lineage-audit.json')])]
for name,cmd in commands:
 r=subprocess.run(cmd,text=True,capture_output=True,env=env);(V/(name+'.stdout.log')).write_text(r.stdout);(V/(name+'.stderr.log')).write_text(r.stderr);(V/(name+'.receipt.json')).write_text(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),command=cmd,exit_code=r.returncode),indent=2)+'\n');print(name,r.returncode,r.stdout[:1200]);assert r.returncode==0,r.stdout+r.stderr
