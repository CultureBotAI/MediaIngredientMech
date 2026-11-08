"""Adversarial admission controls on exact real successor fragments, in a durable fixture."""
from pathlib import Path
import json,hashlib,subprocess,sys,shutil,uuid
R=Path.cwd();B=R/'reports/all_unmatched_20261107/worker-05';O=B/'correction-1193-v1';script=O/'processing/assemble_outcomes.py';config=json.loads((O/'review-bindings.json').read_text())
F=R/'.temp/all-unmatched-worker-05/correction-1193-v1/assembly-controls'/str(uuid.uuid4());FB=F/'reports/all_unmatched_20261107/worker-05';FO=FB/'correction-1193-v1';FO.mkdir(parents=True)
files=['decisions.json','correction-1193-v1/review-bindings.json']+[str(Path('correction-1193-v1')/g/f) for g in config for f in ['decisions.json','evidence.json','proposals.json']]+[rb['review_path'] for rb in config.values()]
for rel in files:
 p=FB/rel;p.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(B/rel,p)
snap={str(p.relative_to(FB)):p.read_bytes() for p in FB.rglob('*') if p.is_file()};results=[]
def restore():
 for rel,raw in snap.items():(FB/rel).write_bytes(raw)
def put(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(name,expected):
 r=subprocess.run([sys.executable,str(script)],cwd=F,capture_output=True,text=True);assert (r.returncode==0)==expected,(name,r.stdout,r.stderr)
 results.append({'control':name,'expected_acceptance':expected,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
def rereview_fixture(g,f):
 # Synthetic reviewer updates isolate the structural invariant under test; they never alter real reviews.
 cfg=json.loads((FO/'review-bindings.json').read_text());rp=FB/cfg[g]['review_path'];rev=json.loads(rp.read_text());h=sha(FO/g/f);rev['reviewed_inputs'][f]=h;cfg[g]['reviewed_fragment_hashes'][f]=h;put(rp,rev);put(FO/'review-bindings.json',cfg)
run('exact independently reviewed successor accepted',True)
source=json.loads((B/'contracts/shard-05.json').read_text())['cases'];cases={x['case_id']:x for x in source};ds=json.loads((FO/'decisions.json').read_text())['decisions']
for d in ds:
 c=cases[d['case_id']];kg=c.get('original_kg_entry',{})
 for key in ['owners','downstream_holds','consumed_name_hits','native_review_rows']:assert d['preserved_source_holds'][key]==kg.get(key,[])
 assert d['source']=={k:c[k] for k in ['source','source_case_id','source_label','raw_source_label']}
results.append({'control':'all188 original raw names and nested negative holds preserved','status':'PASS'})
g='root';p=FO/g/'decisions.json';x=json.loads(p.read_text());x['decisions'][0]['reasoning']+=' Unreviewed mutation.';put(p,x);run('stale independently reviewed fragment rejected',False);restore()
rp=FB/config[g]['review_path'];x=json.loads(rp.read_text());x['open_findings']=[{'status':'open'}];put(rp,x);run('actual open reviewer finding rejected',False);restore()
x=json.loads(rp.read_text());x[config[g]['case_list_key']][0]['status']='pending';put(rp,x);run('pending individual review rejected',False);restore()
x=json.loads(rp.read_text());x[config[g]['case_list_key']].append(x[config[g]['case_list_key']][0]);put(rp,x);run('duplicate reviewed case rejected',False);restore()
x=json.loads(p.read_text());x['decisions'][0]['source']['raw_source_label']+=' altered';put(p,x);rereview_fixture(g,'decisions.json');run('altered source label rejected despite synthetic review hash update',False);restore()
x=json.loads(p.read_text());x['decisions'][0].pop('correction_reassessment');x['decisions'][0].pop('reassessment',None);put(p,x);rereview_fixture(g,'decisions.json');run('missing individual correction reassessment rejected',False);restore()
pp=FO/g/'proposals.json';x=json.loads(pp.read_text());a=next(z for z in x['proposals'] if z['kind']=='edit_existing_owner');a['before_sha256']='0'*64;put(pp,x);rereview_fixture(g,'proposals.json');run('proposal original owner backlink hash mismatch rejected',False);restore()
x=json.loads(pp.read_text());x['proposals'][1]['owner_path']=x['proposals'][0]['owner_path'];put(pp,x);rereview_fixture(g,'proposals.json');run('multiple final payloads for one owner rejected',False);restore()
cfg=json.loads((FO/'review-bindings.json').read_text());cfg[g]['primary_author']=cfg[g]['reviewer'];put(FO/'review-bindings.json',cfg);run('primary author substituted as skeptical reviewer rejected',False);restore()
run('restored exact reviewed successor accepted',True)
(O/'validation/assembly-controls.json').write_text(json.dumps({'status':'PASS','controls':results,'assembler_sha256':sha(script),'fixture_path':str(F.relative_to(R)),'limitations':'Synthetic structural admission controls; no scientific adequacy or release approval inferred.'},indent=2)+'\n');print('PASS',len(results),'real-fixture controls')
