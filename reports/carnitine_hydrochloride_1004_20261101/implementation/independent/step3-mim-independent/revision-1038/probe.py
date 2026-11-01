"""Replay actual candidate and native prior-stamp behavior without production writes."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,importlib.util,io,json,sys
from plugins.lock_manager import LockManager
OUT=Path(__file__).resolve().parent;RUN=OUT.parents[1];MIM=RUN/'step3-mim';CLAW=RUN/'claw-cas-guard'
sys.path.insert(0,str(MIM));sys.path.insert(0,str(CLAW/'scripts'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def load(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m);return m
oldpath=RUN/'step3-writer-evidence/revision-1036/merge_carnitine_hydrochloride.py'
newpath=MIM/'scripts/merge_carnitine_hydrochloride.py'
old=load('independent_1038_before',oldpath);old.ROOT=MIM;old.FIXTURES=MIM/'tests/fixtures/issue1004-before'
new=load('independent_1038_after',newpath)
actual=MIM/'output/step3-native-candidate/candidate.sssom.tsv'
assert sha(actual)=='02b40e540b0663944500071e5725004ec0610e46bf3dd0b83cd4987820af7736'
source_log=RUN/'step3-application/source-apply.json'
inputs=[actual,source_log,*[MIM/p for p in new.BEFORE]]
snapshot={str(p):sha(p) for p in inputs}
subjects={new.SUBJECT,new.COMPONENT_SUBJECT,new.RETIRED_SUBJECT}
fields,actualrows=new.table(actual.read_bytes());selected=[r for r in actualrows if r['subject_id'] in subjects]
assert len(selected)==2
before=(RUN/'step3-application/source-apply.before-ingredient_mappings.sssom.tsv').read_bytes()
oldrows=new.table(before)[1];oldnldm=next(r for r in oldrows if r['subject_id']==new.COMPONENT_SUBJECT)
expected_stamp=oldnldm['validation_method'];assert expected_stamp=='manual:promote_resolved_unmapped|PROMOTED|2026-08-06'
native=load('independent_1038_native',CLAW/'scripts/build_mim_ingredient_sssom.py')
rows=[]
for p in new.OWNERS:rows.extend(native._row_from_yaml(MIM/p,{},{},{},{}))
assert all(r['validation_method']=='' for r in rows)
prior=native._load_existing_validation_method(RUN/'step3-application/source-apply.before-ingredient_mappings.sssom.tsv')
outcomes=native.apply_replayed_stamps(rows,prior)
assert rows==selected and outcomes['replayed']==1
results=[]
with LockManager({'my_id':'independent-review'}).lock('mediaingredientmech','1038_independent_dry_review'):
 for name,w in [('original_actual_candidate',old),('repaired_actual_candidate',new)]:
  err=None;result=None
  try:result=w.promote(MIM,actual,source_log,OUT/(name+'.json'),candidate_sha256=sha(actual))
  except Exception as exc:err={'type':type(exc).__name__,'message':str(exc)}
  if w is old:assert err and 'Candidate differs' in err['message']
  else:assert result['changed_rows']==2 and result['removed_rows']==4 and result['applied'] is False
  assert not (OUT/(name+'.json')).exists()
  results.append({'case':name,'error':err,'dry_result':result})
 owners={p:(MIM/p).read_bytes() for p in new.OWNERS}
 after=new.promoted_sssom(before,actual.read_bytes(),owners)
 afterrows=new.table(after)[1]
 assert len(afterrows)==len(oldrows)-4
 assert [r for r in oldrows if r['subject_id'] not in subjects]==[r for r in afterrows if r['subject_id'] not in subjects]
 nldm=next(r for r in afterrows if r['subject_id']==new.COMPONENT_SUBJECT)
 nldm_delta=[k for k in oldnldm if oldnldm[k]!=nldm[k]]
 assert set(nldm_delta)=={'source','mapping_date'} and nldm['validation_method']==expected_stamp
 for name,subject,stamp in [('nldm_empty',new.COMPONENT_SUBJECT,''),('nldm_arbitrary',new.COMPONENT_SUBJECT,'OAK|APPROVED|2026-11-01'),('nldm_changed_date',new.COMPONENT_SUBJECT,'manual:promote_resolved_unmapped|PROMOTED|2026-08-07'),('ncit_old_nldm_stamp',new.SUBJECT,expected_stamp),('ncit_arbitrary_stamp',new.SUBJECT,'OAK|APPROVED|2026-11-01')]:
  altered=[dict(r) for r in selected]
  next(r for r in altered if r['subject_id']==subject)['validation_method']=stamp
  b=io.StringIO(newline='');s=csv.DictWriter(b,fieldnames=fields,delimiter='\t',lineterminator='\n');s.writeheader();s.writerows(altered)
  err=None
  try:new.promoted_sssom(before,b.getvalue().encode(),owners)
  except Exception as exc:err={'type':type(exc).__name__,'message':str(exc)}
  assert err and 'Candidate differs' in err['message'];results.append({'case':name,'error':err})
assert snapshot=={p:sha(Path(p)) for p in snapshot}
result={'at':datetime.now(timezone.utc).isoformat(),'verdict':'PASS_REPAIRED_NATIVE_PRIOR_STAMP_CONTRACT','writer_before_sha256':sha(oldpath),'writer_after_sha256':sha(newpath),'test_sha256':sha(MIM/'tests/test_merge_carnitine_hydrochloride.py'),'native_producer_sha256':sha(CLAW/'scripts/build_mim_ingredient_sssom.py'),'actual_inputs_unchanged':snapshot,'native_stamp_replay':outcomes,'nldm_output_delta_fields':nldm_delta,'proposed_canonical_sha256':hashlib.sha256(after).hexdigest(),'proposed_canonical_rows':len(afterrows),'cases':results,'scientific_or_release_approval':False,'production_writes':False}
(OUT/'results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
