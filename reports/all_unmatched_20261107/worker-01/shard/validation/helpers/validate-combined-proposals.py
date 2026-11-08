"""Validate exact consolidated proposed bytes without writing maintained surfaces."""
from pathlib import Path
import json,yaml,hashlib,datetime,subprocess,sys,dataclasses
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
R=Path.cwd();W=R/'reports/all_unmatched_20261107/worker-01';O=W/'shard';V=O/'validation';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
P=json.loads((O/'proposals.json').read_text())['proposals'];files=[W/p['after_capture']['path'] for p in P]
for f,p in zip(files,P):assert sha(f)==p['after_capture']['sha256']
tag=sys.argv[1];out=V/(tag+'.json');assert not out.exists();tsv=V/(tag+'-strict.tsv')
cmd=[sys.executable,'scripts/validate_strict.py',*[str(p) for p in files],'--workers','2','--out',str(tsv),'--quiet'];r=subprocess.run(cmd,capture_output=True,text=True)
replace={p['owner_path'] for p in P if p['kind']=='edit_existing_owner'}
catalog=[yaml.safe_load(p.read_text()) for p in (R/'data/ingredients').rglob('*.yaml') if str(p.relative_to(R)) not in replace]
proposed=[yaml.safe_load(p.read_text()) for p in files];ids={p['identifier'] for p in proposed};assert len(ids)==len(proposed)
violations=validate_component_partonomy(catalog+proposed);own=[dataclasses.asdict(v) for v in violations if v.record_id in ids]
data={'at':datetime.datetime.now(datetime.UTC).isoformat(),'proposals_sha256':sha(O/'proposals.json'),'proposal_count':len(files),'strict':{'command':cmd,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr,'tsv_path':str(tsv.relative_to(W)),'tsv_sha256':sha(tsv)},'catalog_scope':'Every maintained ingredient YAML through ignore-inclusive rglob, excluding before owners replaced in this isolated overlay; all canonical proposed owners added together. Maintained files untouched.','catalog_count_without_replaced_owners':len(catalog),'proposed_partonomy_violations':own,'unrelated_baseline_partonomy_violation_count':len(violations)-len(own),'result':'PASS' if r.returncode==0 and not own else 'FAIL'}
out.write_text(json.dumps(data,indent=2)+'\n');assert data['result']=='PASS',data;print('combined strict and partonomy PASS',len(files))
