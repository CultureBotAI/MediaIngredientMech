"""Read-only prepublication membership, revision and content stability audit."""
from pathlib import Path
from datetime import datetime,timezone
import gzip,hashlib,importlib.util,json,os,subprocess,sys
D=Path(__file__).resolve().parent
W=D.parent/'step7d'
TRACE=D/'unified-trace-resumption-v2'
OUTPUT=D/'prepublication-input-stability-v1.json'
EXPECTED_HEAD='8417aaf3a057d855ae5d0b78a587ef1cb57bf28f'
EXPECTED_TRACER='a9a5a07911700a911ec14f1b13bd6e0057a60a94e8ddf8d58c76e0ba567186de'
def sha(raw):return hashlib.sha256(raw).hexdigest()
def digest(path):return sha(path.read_bytes())
def git(root,*args):return subprocess.check_output(['git','-C',str(root),*args],env={**os.environ,'GIT_OPTIONAL_LOCKS':'0'},text=True)
def context(root):return {'path':str(root),'revision':git(root,'rev-parse','HEAD').strip(),'branch':git(root,'branch','--show-current').strip(),'status_porcelain_v1':git(root,'status','--porcelain=v1','--untracked-files=all')}
def write(result,exit_code):
 result['finished_at']=datetime.now(timezone.utc).isoformat()
 with OUTPUT.open('x') as f:json.dump(result,f,indent=2,sort_keys=True);f.write('\n')
 print(json.dumps({'result':result['result'],'receipt':str(OUTPUT),'receipt_sha256':digest(OUTPUT),'drift':result.get('drift',[]),'native_input_count':result.get('native_input_count'),'owner_count':result.get('owner_count')}))
 raise SystemExit(exit_code)
def main():
 if OUTPUT.exists():raise RuntimeError('Refuse replacing evidence receipt')
 started=datetime.now(timezone.utc).isoformat()
 module_path=D/'trace_unified_snapshot.py';module_raw=module_path.read_bytes()
 assert sha(module_raw)==EXPECTED_TRACER,'Native trace helper hash drift'
 spec=importlib.util.spec_from_file_location('prepublication_native_trace_scope',module_path)
 native=importlib.util.module_from_spec(spec);sys.modules[spec.name]=native;exec(compile(module_raw,str(module_path),'exec'),native.__dict__)
 refs={p:digest(TRACE/p) for p in ['native-input-inventory.json.gz','executed-code-inputs.json','after-pair-input-hashes.json','trace-receipt.json']}
 before_raw=gzip.decompress((TRACE/'native-input-inventory.json.gz').read_bytes());expected=json.loads(before_raw)
 code_expected=json.loads((TRACE/'executed-code-inputs.json').read_bytes())
 pair_expected=json.loads((TRACE/'after-pair-input-hashes.json').read_bytes())
 plan_raw=(D/'owner-plan.json').read_bytes();assert sha(plan_raw)==native.PLAN_SHA
 plan=json.loads(plan_raw)
 result={'schema':'mim-prepublication-native-input-stability/v1','started_at':started,'result':'PENDING','requested_head':EXPECTED_HEAD,'reviewed_inventory_reference':str(TRACE/'native-input-inventory.json.gz'),'reference_sha256':refs,'trace_helper_sha256':sha(module_raw),'plan_sha256':sha(plan_raw),'maintained_writes':False,'source_writes':False,'generation_performed':False,'tests_performed':False,'network_calls':False,'git_mutations':False,'drift':[]}
 contexts_before={name:context(root) for name,root in [('mim',W),('claw',native.C),('culturemech',native.CULTURE)]}
 result['repository_context_before']=contexts_before
 expected_revs={'mim':EXPECTED_HEAD,'claw':native.PRODUCER,'culturemech':native.CULTURE_REV}
 for name,rev in expected_revs.items():
  if contexts_before[name]['revision']!=rev:result['drift'].append({'kind':'revision','repository':name,'expected':rev,'actual':contexts_before[name]['revision']})
 if contexts_before['mim']['status_porcelain_v1']:result['drift'].append({'kind':'mim_dirty','status':contexts_before['mim']['status_porcelain_v1']})
 actual_paths=native.native_input_paths();expected_paths={Path(p) for p in expected}
 result['native_input_count']=len(actual_paths);result['expected_native_input_count']=len(expected)
 result['input_membership']={'extra':sorted(map(str,actual_paths-expected_paths)),'missing':sorted(map(str,expected_paths-actual_paths)),'ignored_files_included':True,'method':'Actual unchanged native_input_paths: pathlib glob/rglob does not consult gitignore; original native scope is preserved.'}
 if actual_paths!=expected_paths:result['drift'].append({'kind':'native_input_membership','details':result['input_membership']})
 if result['drift']:result['result']='FAIL_DRIFT_STOP';write(result,2)
 assert len(expected)==18882
 observed=native.inventory(actual_paths)
 diffs=[{'path':p,'expected':expected[p],'actual':observed[p]} for p in expected if expected[p]!=observed[p]]
 if diffs:result['drift'].append({'kind':'native_input_bytes','files':diffs})
 observed_encoded=native.enc(observed)
 result['content_verification']={'algorithm':'SHA-256 of complete bytes for every native path; no mtime shortcut','compared_inputs':len(observed),'matched_inputs':len(observed)-len(diffs),'reviewed_uncompressed_inventory_sha256':sha(before_raw),'current_serialized_inventory_sha256':sha(observed_encoded),'canonical_serialized_inventory_equal':observed_encoded==native.enc(expected)}
 owners={p:{'expected_sha256':item['after_sha256'],'current_sha256':observed[str(W/p)]['sha256']} for p,item in plan['owners'].items()}
 result['owner_count']=len(owners);result['selected_owner_sha256']=owners
 assert len(owners)==38
 for p,item in owners.items():
  if item['expected_sha256']!=item['current_sha256']:result['drift'].append({'kind':'selected_owner','path':p,**item})
 pair={p:{'expected_sha256':value,'current_sha256':observed[p]['sha256']} for p,value in pair_expected.items()}
 result['snapshot_pair']=pair
 for p,item in pair.items():
  if item['expected_sha256']!=item['current_sha256']:result['drift'].append({'kind':'snapshot_pair','path':p,**item})
 code_actual={p:sha(native.regular(Path(p))) for p in code_expected}
 result['executed_code_input_count']=len(code_actual);result['executed_code_sha256']=code_actual
 for p,value in code_expected.items():
  if code_actual[p]!=value:result['drift'].append({'kind':'executed_code','path':p,'expected_sha256':value,'current_sha256':code_actual[p]})
 if result['drift']:result['result']='FAIL_DRIFT_STOP';write(result,2)
 # Recapture membership and bytes to catch changes during the audit itself.
 final_paths=native.native_input_paths();result['membership_stable_during_audit']=final_paths==actual_paths
 if final_paths!=actual_paths:result['drift'].append({'kind':'membership_changed_during_audit','extra':sorted(map(str,final_paths-actual_paths)),'missing':sorted(map(str,actual_paths-final_paths))})
 else:
  final_inventory=native.inventory(final_paths);changed=[p for p in observed if observed[p]!=final_inventory[p]]
  result['bytes_stable_during_audit']=not changed
  result['final_serialized_inventory_sha256']=sha(native.enc(final_inventory))
  if changed:result['drift'].append({'kind':'bytes_changed_during_audit','paths':changed})
 code_final={p:sha(native.regular(Path(p))) for p in code_expected}
 if code_final!=code_actual:result['drift'].append({'kind':'code_changed_during_audit','paths':[p for p in code_actual if code_final[p]!=code_actual[p]]})
 contexts_after={name:context(root) for name,root in [('mim',W),('claw',native.C),('culturemech',native.CULTURE)]};result['repository_context_after']=contexts_after
 if contexts_before!=contexts_after:result['drift'].append({'kind':'repository_context_changed_during_audit','before':contexts_before,'after':contexts_after})
 final_refs={p:digest(TRACE/p) for p in refs}
 if final_refs!=refs or module_path.read_bytes()!=module_raw or (D/'owner-plan.json').read_bytes()!=plan_raw:result['drift'].append({'kind':'evidence_changed_during_audit'})
 result['audit_script_sha256']=digest(Path(__file__))
 result['result']='FAIL_DRIFT_STOP' if result['drift'] else 'PASS_ALL_INPUT_BYTES_MEMBERSHIP_REVISIONS_OWNERS_PAIR_STABLE'
 write(result,2 if result['drift'] else 0)
if __name__=='__main__':main()
