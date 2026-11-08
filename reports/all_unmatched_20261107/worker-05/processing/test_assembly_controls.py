"""Adversarial controls on real reviewed fragments, isolated under durable .temp.
These test review-completion admission only; the whole-shard auditor checks captures.
"""
from pathlib import Path
import json,sys,subprocess,shutil,uuid,hashlib
R=Path.cwd();O=R/'reports/all_unmatched_20261107/worker-05';script=O/'processing/assemble_outcomes.py';config=json.loads((O/'review-bindings.json').read_text())
F=R/'.temp/all-unmatched-worker-05/assembly-controls'/str(uuid.uuid4());F.mkdir(parents=True);dest=F/'reports/all_unmatched_20261107/worker-05';dest.mkdir(parents=True)
files=['review-bindings.json','subagent-scopes.json','progress.json','issues/created-fatty.json']
files += [g+'/'+f for g in config for f in ['decisions.json','evidence.json','proposals.json']]
files += [v['review_path'] for v in config.values()]
for name in files:
 p=dest/name;p.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(O/name,p)
(dest/'validation').mkdir()
results=[]
def run(name,expected):
 p=subprocess.run([sys.executable,str(script)],cwd=F,capture_output=True,text=True)
 assert (p.returncode==0)==expected,(name,p.stdout,p.stderr)
 results.append({'control':name,'expected_acceptance':expected,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
run('real reviewed complete fragments accepted',True)
assembled=json.loads((dest/'decisions.json').read_text())['decisions']
source=json.loads((O/'contracts/shard-05.json').read_text())['cases'];by={c['case_id']:c for c in source}
assert all(d['preserved_source_holds']['owners']==by[d['case_id']].get('original_kg_entry',{}).get('owners',[]) for d in assembled)
results.append({'control':'all frozen nested owner holds preserved byte-equivalent as JSON values','result':'PASS'})
# Direct manifest status is decisive even when the binding incorrectly says complete.
p=dest/config['materials']['review_path'];original=p.read_bytes();d=json.loads(original);d['review_status']='findings_open';p.write_text(json.dumps(d));run('open actual reviewer manifest rejected',False);p.write_bytes(original)
p=dest/config['root']['review_path'];original=p.read_bytes();d=json.loads(original);d['case_reviews'].append(d['case_reviews'][0]);p.write_text(json.dumps(d));run('duplicate review case rejected',False);p.write_bytes(original)
p=dest/'media/decisions.json';original=p.read_bytes();d=json.loads(original);d['decisions'][0]['reasoning']+=' Unreviewed mutation.';p.write_text(json.dumps(d));run('stale reviewed fragment rejected',False);p.write_bytes(original)
p=dest/config['media']['review_path'];original=p.read_bytes();d=json.loads(original);d['case_reviews'][0]['status']='pending';p.write_text(json.dumps(d));run('pending individual case rejected',False);p.write_bytes(original)
run('restored exact reviewed inputs accepted',True)
(O/'validation/assembly-controls.json').write_text(json.dumps({'status':'PASS','controls':results,'assembler_sha256':hashlib.sha256(script.read_bytes()).hexdigest(),'fixture_path':str(F.relative_to(R))},indent=2)+'\n');print('PASS',len(results),'real-fixture controls')
