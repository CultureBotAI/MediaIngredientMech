"""Independent fresh-process execution-marker replay for existing #1195 addendum."""
from pathlib import Path
import hashlib,importlib,json,sys,importlib.util
D=Path(__file__).resolve().parent
P=D/'cached-dependency-private-package-v2';sys.path.insert(0,str(P/'src'))
name='mediaingredientmech.curate.publication_guard';public=importlib.import_module(name);path=Path(public.__file__);old=path.read_bytes()
marker=b"\n_INDEPENDENT_REVIEW_CAPTURE_MARKER = 'B executed privately'\n";path.write_bytes(old+marker)
from mediaingredientmech.curate import campaign_owner_apply as owner
bound=owner._BOUND_NATIVE[name]
spec=importlib.util.spec_from_file_location('private_dependency_fixture',P/'tests/test_campaign_owner_apply.py');t=importlib.util.module_from_spec(spec);spec.loader.exec_module(t)
results=[]
for stale in [False,True]:
 root=D/'cached-dependency-fixtures-v2'/('stale-A-pin' if stale else 'fresh-B-pin');root.mkdir(parents=True);plan=t.setup(root)
 source='src/'+name.replace('.','/')+'.py'
 if stale:
  (root/source).write_bytes(old)
  for b in plan['bindings']:
   if b['role']=='producer' and b['path']==source:b['sha256']=hashlib.sha256(old).hexdigest()
  t.save_contract(root,plan)
 before=owner.hashes(owner.inventory(root))
 try:
  ready=owner.prepare(root,root/'plan.json',root/'acceptance.json');result=owner.apply(ready,root/'receipt');out={'accepted':True,'applied':result['applied']}
 except Exception as e:out={'accepted':False,'error':type(e).__name__+': '+str(e)}
 out.update(stale=stale,owners_unchanged=owner.hashes(owner.inventory(root))==before,receipt_exists=(root/'receipt').exists());results.append(out)
report={'operator_sha256':hashlib.sha256(Path(owner.__file__).read_bytes()).hexdigest(),'public_cached_A_unchanged':sys.modules[name] is public and not hasattr(public,'_INDEPENDENT_REVIEW_CAPTURE_MARKER'),'private_B_executed':getattr(bound,'_INDEPENDENT_REVIEW_CAPTURE_MARKER',None)=='B executed privately','uses_private_class':owner.FrozenFile is bound.FrozenFile and owner.FrozenFile is not public.FrozenFile,'exact_executed_capture':bound._campaign_executed_source.content==old+marker,'actual_A_sha256':hashlib.sha256(old).hexdigest(),'actual_B_sha256':hashlib.sha256(old+marker).hexdigest(),'results':results,'limitations':'Actual native owner prepare/dry-run in private synthetic repositories; no corpus application or scientific approval.'}
assert all(report[k] for k in ['public_cached_A_unchanged','private_B_executed','uses_private_class','exact_executed_capture'])
assert results[0]['accepted'] and not results[0]['applied'] and not results[1]['accepted']
assert all(x['owners_unchanged'] and not x['receipt_exists'] for x in results)
with (D/'cached-dependency-result-v2.json').open('x') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps(report,indent=2))
