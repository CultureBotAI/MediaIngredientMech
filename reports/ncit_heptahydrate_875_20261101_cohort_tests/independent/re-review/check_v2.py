"""Independent source-preservation checks and fresh-process negative replays."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,subprocess,sys
OUT=Path(__file__).resolve().parent
RUN=OUT.parents[1]
ROOT=RUN/'step2-mim'
AUTHOR=RUN/'step2-test-repair-1034'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
test='tests/test_repair_heptahydrate_membership.py'
assert sha(ROOT/test)=='a615daeb6276bcf32a3d879efa9b09a4c1c379751ee8a9330f66fb9ab7b384b3'
baseline=json.loads((AUTHOR/'baseline.json').read_text())
for rel,h in baseline['preserved_hashes'].items():assert sha(ROOT/rel)==h,rel
prior=json.loads((RUN/'step2-independent/final-0bbe5e6816dc-membership.json').read_text())
different={p:{'old':h,'current':sha(ROOT/p)} for p,h in prior['file_sha256'].items() if sha(ROOT/p)!=h}
assert list(different)==[test],different
for p,h in prior['native_pair_sha256'].items():assert sha(ROOT/p)==h,p
mutations=json.loads((AUTHOR/'mutation-results.json').read_text())
env=dict(os.environ)
env['PYTHONDONTWRITEBYTECODE']='1'
env['PYTHONPATH']=str(ROOT/'src')+os.pathsep+str(RUN/'claw-source/src')
replays=[]
(OUT/'pytest-tmp-v2').mkdir(exist_ok=True)
for case in mutations['cases']:
    assert sha(AUTHOR/case['log'])==case['log_sha256']
    if case['changed_copy']:assert sha(AUTHOR/case['changed_copy'])==case['changed_copy_sha256']
    argv=case['argv'][:]
    argv[argv.index('--basetemp')+1]=str(OUT/'pytest-tmp-v2'/case['name'])
    env['PYTHONPYCACHEPREFIX']=str(OUT/'fresh-pycache'/case['name'])
    run=subprocess.run(argv,cwd=ROOT,env=env,capture_output=True,text=True)
    log=OUT/(case['name']+'-v2.log');log.write_text(run.stdout+run.stderr)
    assert run.returncode==case['expected_exit_code'],run.stdout+run.stderr
    assert case['expected_summary'] in run.stdout,run.stdout
    replays.append({'case':case['name'],'argv':argv,'exit_code':run.returncode,'summary':case['expected_summary'],'log_sha256':sha(log)})
for rel,h in baseline['preserved_hashes'].items():assert sha(ROOT/rel)==h,rel
out={'at':datetime.now(timezone.utc).isoformat(),'verdict':'PASS_PRELIMINARY_TEST_FIX_REVIEW','source_sha256':sha(ROOT/test),'protected_files_verified':len(baseline['preserved_hashes']),'prior_inputs_unchanged':len(prior['file_sha256'])-len(different),'expected_prior_input_change':different,'native_pair_hashes_preserved':prior['native_pair_sha256'],'fresh_process_replays':replays,'status':subprocess.check_output(['git','-C',str(ROOT),'status','--short'],text=True).strip(),'production_changes':False,'final_head_review_pending':True}
(OUT/'verification-v2.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
