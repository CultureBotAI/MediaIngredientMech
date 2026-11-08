import copy,datetime,hashlib,importlib.util,json,subprocess,shutil
from pathlib import Path
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.write_validated import write_validated_ingredient,ValidationFailedError
R=Path.cwd();P=R/'.temp/all-unmatched-worker-08/plain-flour-process-replay-v1';O=R/'reports/all_unmatched_20261107/worker-08/process-replays/plain-flour-v1'
spec=importlib.util.spec_from_file_location('process_replay',O/'provenance/replay.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
controls=[];before,expected,literals,event=m.inputs();C=O/'controls';C.mkdir()
for name in ['wrong-timestamp','wrong-attribution','changed-meaning','duplicate-event','missing-llm-disclosure']:
 e=copy.deepcopy(event)
 if name=='wrong-timestamp':e['timestamp']='2026-11-09T00:00:00+00:00'
 if name=='wrong-attribution':e['curator']='synthetic_wrong_actor'
 if name=='changed-meaning':e['changes']+=' Synthetic extra unsupported claim.'
 rec=m.reconstruct(before,literals,e)
 if name=='duplicate-event':record_curation_event(rec,**event)
 if name=='missing-llm-disclosure':
  rec['curation_history']=copy.deepcopy(before['curation_history']);e['llm_assisted']=False;record_curation_event(rec,**e)
 m.save(C/(name+'.json'),rec)
 try:m.require_equivalent(rec,expected,before)
 except AssertionError as err:controls.append({'name':name,'path':'same complete-equivalence guard','rejected':True,'differences':m.differences(expected,rec),'diagnostic':str(err)})
 else:raise AssertionError(name+' escaped')
for name in ['unknown-field','invalid-history-action']:
 rec=copy.deepcopy(expected)
 if name=='unknown-field':rec['unknown_process_probe']=True
 else:rec['curation_history'][-1]['action']='invalid action'
 m.save(C/(name+'.json'),rec);dest=C/(name+'-must-not-exist.yaml')
 try:write_validated_ingredient(rec,dest)
 except ValidationFailedError as err:
  assert not dest.exists();controls.append({'name':name,'path':'actual native closed-schema writer','rejected':True,'no_output_written':True,'diagnostic':str(err)})
 else:raise AssertionError(name+' escaped')
for name,path in [('selected-payload-as-predecessor',O/'inputs/selected-payload.yaml')]:
 dest=P/'controls'/name
 try:m.replay(dest,predecessor_path=path)
 except AssertionError as err:
  assert not dest.exists();controls.append({'name':name,'path':'actual replay preimage guard','rejected':True,'no_output_written':True,'diagnostic':str(err)})
 else:raise AssertionError(name+' escaped')
try:m.replay(O/'replay')
except AssertionError as err:controls.append({'name':'overwrite-existing-replay','path':'actual replay immutable-output guard','rejected':True,'diagnostic':str(err)})
else:raise AssertionError('overwrite escaped')
assert m.sha(O/'replay/Plain_Flour.yaml')==m.SELECTED_SHA
m.save(O/'controls/receipt.json',{'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','controls':controls,'count':len(controls),'actual_native_functions':True,'scope':'Process/equivalence/immutability checks only; fixture mutations are deliberate negatives and not selected science.','new_scientific_claims':False})
# Existing active selection and every selected scientific payload stay exact.
A=R/'reports/all_unmatched_20261107/worker-08';s=A/'successors/issue-1237-tenvit-v1/selection.json';sel=json.loads(s.read_text());assert m.sha(s)=='fb16bf5c29b981dc7dd60cf8d963a9aea25c12a65d6a0e55e29d84dfb2a26699'
for cap in sel['authoritative_inputs'].values():assert m.sha(A/cap['path'])==cap['sha256']
props=json.loads((A/sel['authoritative_inputs']['proposals.json']['path']).read_text())['proposals'];assert len(props)==114
for p in props:assert m.sha(A/p['after_capture']['path'])==p['after_capture']['sha256']
manifest_results=[]
for root,name in [(A/'successors/issue-1237-tenvit-v1','MANIFEST.sha256'),(R/'.temp/all-unmatched-worker-08/tenvit-dependent-v1','MANIFEST.sha256'),(A/'successors/issue-1227-plain-flour-v1','MANIFEST.sha256')]:
 rows=[]
 for line in (root/name).read_text().splitlines():
  digest,relative=line.split('  ',1);assert m.sha(R/relative)==digest;rows.append(relative)
 manifest_results.append({'path':str((root/name).relative_to(R)),'sha256':m.sha(root/name),'members':len(rows),'all_match':True})
subprocess.run(['git','diff','--exit-code','HEAD','--'],check=True,capture_output=True)
m.save(O/'preservation.json',{'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','head':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'tracked_predecessor_changes':0,'manifest_groups':manifest_results,'source_selector_sha256':m.sha(s),'counts':sel['counts'],'all114_payloads_and_all_core_indices_exact':True,'new_cases':0,'new_proposals':0,'selected_payload_changes':0,'all_other_prior_packets':'No writes; protected by own task-only output paths and retained previous sealed preservation receipts. No broader scientific re-review claimed.'})
shutil.copy2(P/'checks.py',O/'provenance/checks.py');shutil.copy2(P/'receipts/replay.log',O/'provenance/replay.log');shutil.copy2(P/'preflight.py',O/'provenance/preflight-attempt1.py');shutil.copy2(P/'receipts/preflight-attempt1.json',O/'provenance/preflight-attempt1.json')
print(json.dumps({'status':'PASS','controls':len(controls),'manifests':manifest_results,'selected_scientific_payloads_unchanged':len(props)},indent=2))
