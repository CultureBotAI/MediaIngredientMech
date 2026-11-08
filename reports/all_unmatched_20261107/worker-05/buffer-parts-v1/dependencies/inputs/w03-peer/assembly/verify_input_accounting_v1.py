from pathlib import Path
import hashlib,json,subprocess,datetime,re,os
import yaml
R=Path.cwd(); O=R/'.temp/peptone-consumer-independent-v1'; A=O/'assembly'; C=R.parents[2]
sha=lambda b:hashlib.sha256(b).hexdigest()
read=lambda p:json.loads(Path(p).read_text())
checks=[]
def check(name,actual,expected=True,**extra):
 ok=actual==expected; checks.append({'check':name,'pass':ok,'actual':actual,'expected':expected,**extra}); return ok
def filecheck(p,want,name):
 p=Path(p); got=sha(p.read_bytes()) if p.is_file() else None
 return check(name,got,want,path=str(p))
def manifest(root,mp,expected_count):
 m=read(mp); rows=m['files']; check(str(mp)+':count',len(rows),expected_count)
 check(str(mp)+':unique_paths',len({x['path'] for x in rows}),len(rows))
 for e in rows:
  p=root/e['path'];check('member_path_contained',p.resolve().is_relative_to(root.resolve()),True,path=str(p));check('member_not_symlink',p.is_symlink(),False,path=str(p));filecheck(p,e['sha256'],'manifest_member')
  if 'bytes' in e:check('manifest_member_size',p.stat().st_size,e['bytes'],path=str(p))
 actual={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and p.name not in {'MANIFEST.json','SEAL.json'}}
 # All regular ignored paths count; only root seals excluded.
 actual={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file()}-{'MANIFEST.json','SEAL.json'}
 check('manifest_complete_regular_files',sorted(actual),sorted(x['path'] for x in rows),root=str(root),ignored_files_included=True)
 return rows
head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip();status=subprocess.check_output(['git','status','--short','--untracked-files=no'],text=True)
check('current_local_head',head,'fe31a02850932a7bdf2fe65c93cb636a86f82a2c');check('tracked_worktree_clean',status,'')
receipt=read(O/'context/input-receipt.json');check('receipt_head',receipt['head'],head)
for e in receipt['copies']:
 filecheck(e['source_path'],e['sha256'],'receipt_original');filecheck(R/e['captured_path'],e['sha256'],'receipt_capture')
for e in receipt['prior_seals_to_preserve']:filecheck(R/e['path'],e['sha256'],'prior_seal_preserved')
plan=C/'preflight/final-component-dependency-plan-v1';route=C/'preflight/final-component-dependency-plan-v2'
manifest(plan,O/'context/plan-v1/MANIFEST.json',98);manifest(route,O/'context/route-MANIFEST.json',28)
seal=read(O/'context/plan-v1/SEAL.json');filecheck(plan/'MANIFEST.json',seal['manifest_sha256'],'plan_seal_manifest');filecheck(plan/'HANDOFF.json',seal['handoff_sha256'],'plan_seal_handoff')
refs=read(O/'context/plan-v1/source-evidence-refcheck-32.json');check('evidence_refcheck_count',len(refs),32)
for e in refs:filecheck(e['path'],e['sha256'],'evidence_refcheck')
pins=read(O/'context/plan-v1/plan-input-pins.json')
for p,h in pins.items():filecheck(p,h,'plan_input_pin')
claims=read(O/'context/claims-20.json');owners=read(O/'context/owner-bindings-20.json');targets=read(O/'targets.json')['targets'];schema=read(O/'validation/native-record-schema.json');inspect=read(O/'validation/native-inspect-v1.json')
original=[x for x in read(O/'context/plan-v1/minimal-couplings-28.json') if (x.get('before_component') or x.get('component') or {}).get('component_id')=='MICRO:0000178']
check('original_peptone_selection_count',len(original),20);check('selection_keys_exact',[x['claim_key'] for x in claims],[x['claim_key'] for x in original])
check('claim_enrichment_only',[{k:v for k,v in x.items() if k not in {'review_target_id','captured_owner','owner_kind'}} for x in claims],original)
ids=['PC%02d'%i for i in range(1,21)]
for label,found in [('claims',[x['review_target_id'] for x in claims]),('owners',[x['target_id'] for x in owners]),('targets',[x['target_id'] for x in targets]),('schema',[x['target_id'] for x in schema['rows']]),('inspect',[x['target_id'] for x in inspect['targets']])]:check(label+'_target_ids',found,ids)
check('new_owner_count',sum(x['new_owner'] for x in owners),1);check('existing_owner_count',sum(not x['new_owner'] for x in owners),19)
sourcebindings={x['origin_id']:x for x in read(O/'context/plan-v1/source-bindings.json')}
owner_accounting=[]
for row,b,t,s in zip(claims,owners,targets,schema['rows']):
 path,index=row['claim_key'].split('#components[');idx=int(index[:-1]);cap=R/row['captured_owner']['captured_path'];rec=yaml.safe_load(cap.read_text());h=sha(cap.read_bytes())
 check('owner_binding_path',b['owner_path'],path);check('owner_binding_index',b['component_index'],idx);check('owner_binding_claim',b['claim_key'],row['claim_key']);check('owner_capture_binding',b['capture'],row['captured_owner']);check('owner_sha256',b['owner_sha256'],h);check('complete_component_retained',b['complete_component'],rec['components'][idx]);check('complete_assertion_retained',b['component_assertion'],rec.get('component_assertion'));check('source_component_exact',rec['components'][idx],row.get('before_component') or row['component'])
 check('old_id',rec['components'][idx].get('component_id'),'MICRO:0000178');check('old_reference_scope',rec['components'][idx].get('reference_scope'),'MIM_CATALOG')
 filecheck(row['captured_owner']['source_path'],h,'current_original_unchanged');check('captured_sha',h,row['captured_owner']['sha256']);check('schema_target_hash',s['sha256'],h);check('schema_errors_empty',s['errors'],[]);check('native_target_path',t['path'],row['captured_owner']['captured_path']);check('native_target_selector',t['selector'],'components[%d]'%idx)
 check('native_target_owner_path',t['owner_paths'][0]['path'],path)
 if not b['new_owner']:
  check('existing_before_hash',row['before_owner_sha256'],h);check('existing_owner_before_binding',b['before_sha256'],h);filecheck(R/path,h,'current_maintained_beforeimage');filecheck(C/'preflight/final-intake-candidate-v1/snapshot/baseline'/path,h,'frozen_baseline_beforeimage')
 else:
  check('new_owner_path',path,'data/ingredients/mapped/togo_m2491_mrssi_base.yaml');check('genuine_null_beforepath',row['before_owner_path'],None);check('genuine_null_beforehash',row['before_owner_sha256'],None);check('genuine_null_binding_beforehash',b['before_sha256'],None);check('unapplied_new_owner_current_path_absent',(R/path).exists(),False);check('unapplied_new_owner_baseline_path_absent',(C/'preflight/final-intake-candidate-v1/snapshot/baseline'/path).exists(),False)
  sb=sourcebindings[row['source_published_origin']];check('new_owner_payload_binding',sb['payload_sha256'],h);check('new_owner_head_binding',sb['head'],row['source_head']);blob=subprocess.check_output(['git','show',sb['head']+':'+sb['git_path']]);check('new_owner_published_git_blob',sha(blob),h)
 owner_accounting.append({'target_id':b['target_id'],'claim_key':row['claim_key'],'owner_sha256':h,'before_sha256':row['before_owner_sha256'],'new_owner':b['new_owner'],'exact_component':rec['components'][idx],'mechanical_binding_only':True})
check('native_inspection_targets_exact',inspect['targets'],targets);check('native_inspection_head',inspect['source']['git_revision'],head);check('native_inspection_status',inspect['status'],'inspection_only')
for e in inspect['source']['inputs']:filecheck(R/e['path'],e['sha256'],'native_inspection_input')
check('native_schema_targets_count',schema['targets'],20);check('native_schema_all_valid_reported',schema['all_valid'],True);check('native_schema_not_science',schema['scientific_approval'],False)
probe=read(O/'context/native-dependency-probe.json');reuse=read(O/'validation/native-probe-reuse.json');filecheck(R/reuse['receipt_path'],reuse['receipt_sha256'],'native_probe_exact');filecheck(probe['native_module'],probe['native_module_sha256'],'native_probe_integration_module_unchanged');filecheck(R/'src/mediaingredientmech/validation/component_partonomy.py',probe['native_module_sha256'],'native_probe_current_module_unchanged');check('native_probe_reused_cases_exact',reuse['read_actual_recorded_cases'],probe['cases']);check('native_probe_was_not_rerun',reuse['rerun'],False)
causal=read(O/'context/authentic-causal-case.json');filecheck(causal['source_path'],causal['source_sha256'],'causal_original_shard');shard=read(causal['source_path']);case=causal['case']
# Match the full frozen object recursively; do not turn its peptones observation into child recipes.
def dicts(x):
 if isinstance(x,dict):
  yield x
  for v in x.values():yield from dicts(v)
 elif isinstance(x,list):
  for v in x:yield from dicts(v)
found=[x for x in dicts(shard) if x.get('case_id')==case['case_id']];check('causal_case_single_exact_object',found,[case]);casehash=sha(json.dumps(case,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode());check('causal_case_canonical_hash',casehash,causal['case_input_sha256'])
for e in read(O/'context/combined-candidate-readback.json')['rows']:filecheck(e['path'],e['sha256'],'context_combined_candidate_unchanged')
filecheck(O/'other/MANIFEST.json','cc5354fd0920fbd1c7569ab451b149ce44602d6d87e2309733f51134eb9294c8','own_source_subreview_seal_unchanged');filecheck(O/'other/HANDOFF.json','5ce316133ee3fd79800a65b3e06a8cabd088f947e4d7fc39d41b672fcb22147b','own_source_subreview_handoff_unchanged');manifest(O/'other',O/'other/MANIFEST.json',32)
check('final_current_head',subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),head);check('final_tracked_clean',subprocess.check_output(['git','status','--short','--untracked-files=no'],text=True),'')
report={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':'/root/peptone_other_sources','expanded_scope':'Independent technical assembly review only; this reviewer authored other/ ten-claim source assessment and does not independently scientifically approve those same rows or any whole owner.','status':'PASS' if all(x['pass'] for x in checks) else 'FAIL','checks':checks,'owner_accounting':owner_accounting,'counts':{'checks':len(checks),'failed':sum(not x['pass'] for x in checks),'plan_manifest':98,'route_manifest':28,'evidence_refcheck':32,'receipt_copies':len(receipt['copies']),'prior_seals':len(receipt['prior_seals_to_preserve']),'plan_input_pins':len(pins),'claims':20,'existing_beforeimages':19,'true_new_proposals':1},'search_boundary':'Direct declared file checks and pathlib recursive enumeration of the two plan packets and sealed other/ include ignored regular files. New-owner absence is limited to its exact current and frozen maintained path; no global private/history absence claim. No credentials scanned.','native_scope':'Read and hash-bound the actual native inspection, 20 schema result rows and six reused exact partonomy counterfactual cases; schema result is shape validation, not science. No unchanged expensive validation rerun. Native final structured review/manifest pending root assembly.','pending':['Root final machine-ledger, native structured review and seal mechanical review'],'network_access':False,'scientific_reapproval':False,'candidate_acceptance':False,'whole_owner_role_export_approval':False}
with (A/'input-accounting-v1.json').open('x') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps({'status':report['status'],'counts':report['counts'],'failures':[x for x in checks if not x['pass']]}))
