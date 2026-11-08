"""Isolated selected-proposal validation. Never writes maintained ingredients or exports."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys,subprocess,yaml,collections
from mediaingredientmech.validation.write_validated import write_validated_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
R=Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v2';core=S/(sys.argv[1] if len(sys.argv)>1 else 'assembly-v1');N=S/(sys.argv[2] if len(sys.argv)>2 else 'validation-draft-v1');N.mkdir(parents=True,exist_ok=True);scratch=R/'.temp/all-unmatched-worker-10/successor-v2'/N.name;scratch.mkdir(parents=True,exist_ok=True);sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();load=lambda p:json.loads(p.read_text())
def save(p,d):
 with p.open('x') as f:json.dump(d,f,indent=2);f.write('\n')
D=load(core/'decisions.json')['decisions'];P=load(core/'proposals.json')['proposals'];owners=sorted({x['path'] for d in D for x in d['owner_records']});payloads=[A/p['after_capture']['path'] for p in P];cmd=['.temp/all-unmatched-worker-10/venv/bin/python','scripts/validate_strict.py',*owners,*[str(p.relative_to(R)) for p in payloads],'--workers','1','--out',str((N/'strict-failures.tsv').relative_to(R))];proc=subprocess.run(cmd,text=True,capture_output=True)
for n,t in [('strict.stdout',proc.stdout),('strict.stderr',proc.stderr)]:
 with (N/n).open('x') as f:f.write(t)
save(N/'strict-command.json',{'at':datetime.now(timezone.utc).isoformat(),'argv':cmd,'exit_code':proc.returncode,'owners':len(owners),'payloads':len(payloads)});assert proc.returncode==0
copies=[]
for p,f in zip(P,payloads):
 assert sha(f)==p['after_capture']['sha256'];d=yaml.safe_load(f.read_text());dest=scratch/(p['proposal_id']+'.yaml');assert not dest.exists();write_validated_ingredient(d,dest);assert yaml.safe_load(dest.read_text())==d;assert sha(f)==p['after_capture']['sha256'];copies.append({'proposal_id':p['proposal_id'],'source_sha256':sha(f),'scratch_sha256':sha(dest),'semantic_roundtrip_equal':True})
save(N/'guarded-roundtrip.json',{'at':datetime.now(timezone.utc).isoformat(),'writer':'write_validated_ingredient','scope':'Private scratch copies only; dictionary equality after native guarded serialization; no aggregate/SSSOM/export rebuild claimed.','copies':copies})
records={str(f.relative_to(R)):yaml.safe_load(f.read_text()) for f in sorted((R/'data/ingredients').rglob('*.yaml'))};baseline=validate_component_partonomy(list(records.values()));assert not baseline
for p,f in zip(P,payloads):
 if p['kind']=='edit_existing_owner':assert sha(R/p['owner_path'])==p['before_sha256'];records.pop(p['owner_path'])
 dest=p.get('destination_path',p['owner_path']);assert dest not in records;records[dest]=yaml.safe_load(f.read_text())
violations=validate_component_partonomy(list(records.values()));save(N/'partonomy.json',{'at':datetime.now(timezone.utc).isoformat(),'baseline_records':2956,'baseline_violations':[],'projected_records':len(records),'selected_payloads':len(P),'violations':[str(x) for x in violations],'scope':'Whole frozen catalog plus complete selected replacements/additions in memory. No application or release approval.'});assert not violations
ids=collections.defaultdict(list)
for p,f in zip(P,payloads):ids[yaml.safe_load(f.read_text())['identifier']].append(p['proposal_id'])
assert all(len(v)==1 for v in ids.values());assert len({p['owner_path'] for p in P})==len(P)
# A meaningful negative control verifies invalid fields cannot be written by the native guard.
bad=dict(yaml.safe_load(payloads[0].read_text()));bad['invalid_successor_probe']=True;refused=False;dest=scratch/'must-not-exist-invalid.yaml'
try:write_validated_ingredient(bad,dest)
except Exception as exc:refused=True;err=type(exc).__name__+': '+str(exc)
assert refused and not dest.exists();save(N/'negative-control.json',{'unknown_field_refused':True,'destination_absent':True,'error':err,'scientific_validation':False})
save(N/'validation-receipt.json',{'at':datetime.now(timezone.utc).isoformat(),'status':'PASS','core_hashes':{n:sha(core/n) for n in ['decisions.json','evidence.json','proposals.json']},'strict_exit_code':proc.returncode,'owners':len(owners),'payloads':len(P),'guarded_copies':len(copies),'partonomy_records':len(records),'partonomy_violations':0,'negative_control_refused':True,'script_sha256':sha(Path(__file__)),'approval':False})
print(json.dumps({'status':'PASS','owners':len(owners),'payloads':len(P),'projected_records':len(records)},indent=2))
