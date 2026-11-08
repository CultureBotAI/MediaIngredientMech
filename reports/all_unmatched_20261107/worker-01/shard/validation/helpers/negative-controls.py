from pathlib import Path
import json,copy,subprocess,datetime,hashlib
R=Path.cwd();W=R/'reports/all_unmatched_20261107/worker-01';O=W/'shard';T=R/'.temp/all-unmatched-worker-01/shard/negative-controls-v1';T.mkdir(exist_ok=True);(O/'validation').mkdir(exist_ok=True);Q=R.parents[2]/'queue/preliminary-v5';script=R.parents[2]/'scripts/audit_worker_outcomes_v1.py';py=R/'.temp/all-unmatched-worker-01/shard-venv/bin/python';rows=[]
for label in ['missing-case','bad-original-digest','capture-traversal','proposal-before-mismatch']:
 ds=json.load(open(O/'decisions.json'));es=json.load(open(O/'evidence.json'));ps=json.load(open(O/'proposals.json'))
 if label=='missing-case':ds['decisions'].pop()
 if label=='bad-original-digest':ds['decisions'][0]['case_input_sha256']='0'*64
 if label=='capture-traversal':es['evidence'][0]['capture']['path']='../forbidden'
 if label=='proposal-before-mismatch':next(p for p in ps['proposals'] if p['kind']=='edit_existing_owner')['before_sha256']='0'*64
 dd=T/label;dd.mkdir(exist_ok=True)
 for n,d in [('decisions',ds),('evidence',es),('proposals',ps)]:(dd/(n+'.json')).write_text(json.dumps(d)+'\n')
 out=O/'validation'/('negative-'+label+'-v1.json');assert not out.exists()
 cmd=[str(py),str(script),'--shard',str(Q/'shards/shard-01.json'),'--decisions',str(dd/'decisions.json'),'--evidence',str(dd/'evidence.json'),'--proposals',str(dd/'proposals.json'),'--artifact-root',str(W),'--source-root',str(Q),'--mim-root',str(R),'--output',str(out)]
 cp=subprocess.run(cmd,text=True,capture_output=True);row={'control':label,'command':cmd,'exit_code':cp.returncode,'stdout':cp.stdout,'stderr':cp.stderr,'expected_rejected':True,'rejected':cp.returncode!=0};assert row['rejected'];rows.append(row)
receipt={'executed_at':datetime.datetime.now(datetime.UTC).isoformat(),'auditor_sha256':hashlib.sha256(script.read_bytes()).hexdigest(),'actual_negative_controls':rows,'status':'PASS','scientific_approval_established':False};(O/'validation/negative-controls-v1.json').write_text(json.dumps(receipt,indent=2)+'\n');print('4 actual negative controls rejected')
