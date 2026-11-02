from pathlib import Path
import collections, datetime, hashlib, json, os, subprocess, sys
import yaml

E = Path(__file__).resolve().parent
RUN = E.parent.parent
F = E / 'squash-fixture'
W = RUN / 'step7c'
HEAD = '89f070ef3a5f8ed02c787b4ecea3cef62238ce63'
BASE = '54eadef802d2ff159bf4ba9bec51492fe3bb99d4'

def sha(data): return hashlib.sha256(data).hexdigest()
def save(name, data):
    with (E/name).open('x') as out: json.dump(data, out, indent=2); out.write('\n')
def git(root,*args): return subprocess.check_output(['git',*args],cwd=root).decode().strip()
def context(root):
    files=subprocess.check_output(['git','ls-files','-z'],cwd=root).decode().split('\0')
    return {'head':git(root,'rev-parse','HEAD'),'tree':git(root,'rev-parse','HEAD^{tree}'),
        'status':git(root,'status','--porcelain'),
        'files':{p:sha((root/p).read_bytes()) for p in files if p and (root/p).is_file()}}
before=context(F); wb=context(W)
assert wb['head']==HEAD and not wb['status'] and before['tree']==wb['tree'] and not before['status']
save('before.json',{'fixture':before,'maintained_worktree':wb})
env=dict(os.environ)
for k in list(env):
    if k.endswith('_ROOT') or k in ('CLAW_SRC','OPENCLAW_WORKSPACE','RECORD_REVIEW_BASE'):
        env.pop(k,None)
old=RUN.parent.parent/'output/sssom-generation-20261031T213407Z'
env.update(PYTHONDONTWRITEBYTECODE='1', PYTHONPATH=str(F/'src')+':'+str(old/'test-deps'),
    UV_PROJECT_ENVIRONMENT=str(RUN/'envs/mim'),UV_NO_SYNC='1',UV_OFFLINE='1',UV_PYTHON='3.13',
    UV_CACHE_DIR=str(E/'uv-cache'),PATH=str(RUN/'envs/mim/bin')+':'+os.environ['PATH'])
save('runtime.json',{'environment':{k:env[k] for k in ('PYTHONDONTWRITEBYTECODE','PYTHONPATH','UV_PROJECT_ENVIRONMENT','UV_NO_SYNC','UV_OFFLINE','UV_PYTHON','UV_CACHE_DIR')},
    'python':subprocess.check_output([str(RUN/'envs/mim/bin/python'),'--version']).decode().strip(),
    'platform':sys.platform,'qualification':'Existing Python environment reused offline; no setup, install, remote checkout, Ubuntu runner or uploads reproduced. No sibling-root or generator-profile bindings.'})
steps=[]
def execute(name,command,workflow=None):
    start=datetime.datetime.now(datetime.timezone.utc).isoformat();p=E/f'{len(steps)+1:02d}.log'
    with p.open('x') as out: r=subprocess.run(['bash','-e','-o','pipefail','-c',command],cwd=F,env=env,stdout=out,stderr=subprocess.STDOUT)
    d={'name':name,'command':command,'workflow':workflow,'started_at':start,'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':r.returncode,'log':str(p),'log_sha256':sha(p.read_bytes())}
    steps.append(d);save(f'{len(steps):02d}-receipt.json',d);print(json.dumps({'name':name,'exit_code':r.returncode}),flush=True)
    assert r.returncode==0, d
execute('Verify the committed source/promotion evidence packet','python -B reports/step7c_mapping_751_313_235_20261102/verify_source_promotion_evidence.py --repository "'+str(F)+'"')
for name in ('qc-supported-kgx.yaml','qc-reviewed-sssom.yaml'):
    p=F/'.github/workflows'/name;doc=yaml.safe_load(p.read_bytes())
    for job in doc['jobs'].values():
        for s in job['steps']:
            if 'run' not in s or s['name']=='Install locked runtime': continue
            execute(s['name'],s['run'],{'path':str(p.relative_to(F)),'sha256':sha(p.read_bytes())})
after=context(F);wa=context(W)
assert before==after and wb==wa
absent={}
for h in ('26938f4bd9d9ff9adea4e0aa02d5dffbd368c4b7','de31ae2f73e532e827e7e293230eddf6347b357f','bb3edec5cb723c866dd588791c9420745a837f8e',HEAD):
    r=subprocess.run(['git','cat-file','-e',h+'^{commit}'],cwd=F,capture_output=True);assert r.returncode!=0;absent[h]=r.returncode
mapping=json.loads((F/'reports/sssom_completion_20260921/review.json').read_text())
selected={str(d['source_position']):d for d in mapping['decisions'] if d['source_position'] in (38,113,114,115,233,2229,2920,2921)}
assert len(selected)==8 and all(d['disposition']=='WITHHOLD' for d in selected.values())
semantic=json.loads((F/'reports/semantic_review_20260921/resolution/current-review.json').read_text())
companion=json.loads((F/'reports/step7c_mapping_751_313_235_20261102/refresh-v2/companion-review.json').read_text())
outputs={str(p.relative_to(F)):{'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in sorted((F/'output').rglob('*')) if p.is_file()}
result={'status':'PASS','source_head':HEAD,'synthetic_head':before['head'],'tree':before['tree'],'durable_base':BASE,
    'base_is_sole_parent':git(F,'rev-parse','HEAD^')==BASE,'feature_commit_absence_exit_codes':absent,
    'no_alternates':not (F/'.git/objects/info/alternates').exists(),'steps':steps,
    'fixture_and_maintained_worktree_unchanged':before==after and wb==wa,
    'selected_mapping_decisions':selected,'mapping_counts':dict(collections.Counter(d['disposition'] for d in mapping['decisions'])),
    'semantic_release_verdict':semantic['release_verdict'],'semantic_blocking_findings':len(semantic['blocking_finding_ids']),
    'semantic_blocking_assertions':len(semantic['blocking_assertion_ids']),
    'companion_owners':len(companion['record_inputs']),'companion_claims':len(companion['decisions']),
    'outputs':outputs,'scientific_approval_added':False,'supervisor_binding':None,
    'limitations':['Not the full local suite or remote CI.','Packet verifies selected source/promotion evidence only; external generator archive deliberately omitted.','No production source writer/generator re-execution; downstream mapping/semantic/ingredient native consumer chains replayed.','Final native review additions after C4 need their own input stability check.']}
save('result.json',result)
print(json.dumps({k:v for k,v in result.items() if k not in ('steps','selected_mapping_decisions','outputs')},indent=2),flush=True)
