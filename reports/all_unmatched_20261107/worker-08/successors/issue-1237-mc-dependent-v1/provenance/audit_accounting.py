import copy,hashlib,importlib.util,json,shutil
from pathlib import Path
R=Path.cwd();C=R.parents[2];P=R/'.temp/mc-dependent-successor-v1';A=R/'reports/all_unmatched_20261107/worker-08';O=A/'successors/issue-1237-mc-dependent-v1';F=P/'accounting-controls';F.mkdir()
spec=importlib.util.spec_from_file_location('native_audit',C/'scripts/audit_worker_outcomes_v1.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
def read(p):return json.loads(p.read_text())
def save(p,x):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x') as f:json.dump(x,f,indent=2);f.write('\n')
def call(d,p):return m.audit(C/'queue/preliminary-v5/shards/shard-08.json',d,O/'evidence.json',p,A,C/'queue/preliminary-v5',mim_root=R)
res=call(O/'decisions.json',O/'proposals.json');save(O/'structural-audit.json',res)
checks=[]
def check(name,mut,fragment):
 d=read(O/'decisions.json');p=read(O/'proposals.json');mut(d,p);fd=F/(name+'-decisions.json');fp=F/(name+'-proposals.json');save(fd,d);save(fp,p)
 try:call(fd,fp)
 except Exception as e:
  msg=str(e);assert fragment in msg,(name,msg);checks.append({'name':name,'native_rejected':True,'message':msg,'expected':fragment})
 else:raise AssertionError(name+' accepted')
check('stale-real-before',lambda d,p:p['proposals'][-1].update(before_sha256='0'*64),'not bound to verified owner bytes')
check('duplicate-origin',lambda d,p:p['proposals'].append(copy.deepcopy(p['proposals'][-1])),'duplicate proposal_id')
check('invented-source-case',lambda d,p:p['proposals'][-1].update(case_ids=['CM_NAME:invented']),'unassigned case')
check('invented-source-occurrence',lambda d,p:next(x for x in d['decisions'] if x['case_id']==p['proposals'][-1]['case_ids'][0])['occurrence_ids'].append('CM_OCC:invented'),'missing/changed occurrence')
check('wrong-new-owner-origin',lambda d,p:p['proposals'][-1].update(kind='new_owner'),'new owner has a before hash')
check('missing-new-case-backlink',lambda d,p:next(x for x in d['decisions'] if x['case_id']==p['proposals'][-1]['case_ids'][0])['proposal_ids'].remove(p['proposals'][-1]['proposal_id']),'missing case backlinks')
save(O/'accounting-controls.json',{'status':'PASS','native_auditor_sha256':hashlib.sha256((C/'scripts/audit_worker_outcomes_v1.py').read_bytes()).hexdigest(),'actual_checks':checks,'native_actual_inputs':{'cases':res['accounted_case_count'],'proposals':res['proposal_count'],'evidence':res['evidence_count']},'approval':False})
shutil.copy2(P/'provenance/audit_accounting.py',O/'provenance/audit_accounting.py')
print(json.dumps({'status':'PASS','cases':res['accounted_case_count'],'proposals':res['proposal_count'],'evidence':res['evidence_count'],'controls':len(checks)}))
