"""Independent native execution probes; writes only external fixture roots.

The source writer/publisher and Claw _row_from_yaml are real, with no mocked
validators or transactions. The documented Python API caller lock is held.
No full-corpus producer invocation or scientific approval is claimed.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, importlib.util, io, csv, json, shutil, sys
from plugins.lock_manager import LockManager

OUT=Path(__file__).resolve().parent
RUN=OUT.parents[1]
MIM=RUN/'step3-mim'
CLAW=RUN/'claw-cas-guard'
sys.path.insert(0,str(MIM))
sys.path.insert(0,str(CLAW/'scripts'))
def load(name,path):
 spec=importlib.util.spec_from_file_location(name,path); module=importlib.util.module_from_spec(spec); sys.modules[name]=module; spec.loader.exec_module(module); return module
old_path=RUN/'step3-writer-evidence/initial-stable-source/merge_carnitine_hydrochloride.py'
new_path=MIM/'scripts/merge_carnitine_hydrochloride.py'
old=load('independent_old',old_path)
old.ROOT=MIM; old.FIXTURES=MIM/'tests/fixtures/issue1004-before'
new=load('independent_new',new_path)
native=load('independent_native_sssom',CLAW/'scripts/build_mim_ingredient_sssom.py')
sha=lambda b:hashlib.sha256(b).hexdigest()
production_paths=[MIM/p for p in new.BEFORE]+[new_path,MIM/'tests/test_merge_carnitine_hydrochloride.py',MIM/'src/mediaingredientmech/utils/culturemech_occurrences.py']
production_before={str(p):sha(p.read_bytes()) for p in production_paths}
results=[]
for name,writer,defect in [('old_control',old,None),('fixed_control',new,None),('old_shifted_timestamps',old,'timestamps'),('fixed_shifted_timestamps',new,'timestamps'),('fixed_bad_transaction',new,'transaction'),('fixed_bad_input_binding',new,'input')]:
 root=OUT/'cases'/name; root.mkdir(parents=True)
 for p in writer.BEFORE:
  target=root/p;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(writer.frozen_bytes(p))
 evidence=root/writer.EVIDENCE;shutil.copytree(MIM/writer.EVIDENCE,evidence)
 log=root/'receipts/apply.json'
 with LockManager({'my_id':'independent-review-fixtures'}).lock('mediaingredientmech','step3_independent_fixture_probe'):
  result=writer.apply_sources(root,evidence,log,apply=True)
  receipt_bytes=log.read_bytes(); original=json.loads(receipt_bytes)
  dry_promotion=None
  if name=='fixed_control':
   rows=[]
   for owner in writer.OWNERS: rows+=native._row_from_yaml(root/owner,{},{},{},{})
   fields=writer.table(writer.frozen_bytes(writer.SSSOM))[0]
   stream=io.StringIO(newline='');w=csv.DictWriter(stream,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
   candidate=root/'actual-native-candidate.tsv';candidate.write_text(stream.getvalue())
   dry_promotion=writer.promote(root,candidate,log,root/'receipts/promote.json',candidate_sha256=sha(candidate.read_bytes()))
   assert dry_promotion['changed_rows']==2 and dry_promotion['removed_rows']==4 and not dry_promotion['applied']
   assert len(rows)==2 and {r['subject_id'] for r in rows}=={writer.SUBJECT,writer.COMPONENT_SUBJECT}
   assert not (root/'receipts/promote.json').exists()
  if defect=='timestamps':
   revised=writer.propose_sources({p:writer.frozen_bytes(p) for p in writer.OWNERS},writer.frozen_bytes(writer.LEDGER),writer.frozen_bytes(writer.MEMBERSHIP),timestamp='2026-11-02T00:00:00+00:00')
   for p in writer.OWNERS:(root/p).write_bytes(revised[p])
  elif defect in ('transaction','input'):
   value=json.loads(log.read_bytes())
   if defect=='transaction': value['transaction']['applied']=False
   else:value['input_sha256'][str(root/writer.SURVIVOR)]='0'*64
   log.write_text(json.dumps(value))
  before_second={str(p):sha(p.read_bytes()) for p in [*(root/p for p in writer.BEFORE),log]}
  failure=None;second=None
  try:second=writer.apply_sources(root,evidence,log,apply=True)
  except Exception as exc:failure={'type':type(exc).__name__,'message':str(exc)}
  assert before_second=={p:sha(Path(p).read_bytes()) for p in before_second}
  if defect and writer is new:assert failure and 'receipt' in failure['message']
  else:assert failure is None and second['changed'] is False
  results.append({'case':name,'initial_receipt_sha256':sha(receipt_bytes),'state':original['state'],'original_timestamp':original['timestamp'],'original_receipt_matches_current_owners':all(original['output_sha256'][str(p)]==sha((root/p).read_bytes()) for p in writer.OWNERS),'second_result':second,'failure':failure,'second_call_inputs_unchanged':True,'canonical_unchanged':(root/writer.SSSOM).read_bytes()==writer.frozen_bytes(writer.SSSOM),'actual_native_candidate_dry_promotion':dry_promotion})
assert production_before=={p:sha(Path(p).read_bytes()) for p in production_before}
result={'checked_at':datetime.now(timezone.utc).isoformat(),'scope':__doc__,'writer_before_sha256':sha(old_path.read_bytes()),'writer_fixed_sha256':sha(new_path.read_bytes()),'native_sssom_producer_sha256':sha((CLAW/'scripts/build_mim_ingredient_sssom.py').read_bytes()),'production_before_after_identical':production_before,'cases':results}
(OUT/'results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
