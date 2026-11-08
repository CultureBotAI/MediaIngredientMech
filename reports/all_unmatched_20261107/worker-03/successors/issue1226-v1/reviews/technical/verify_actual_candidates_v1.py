"""Independent exact candidate/bridge audit; writes technical receipt only."""
from pathlib import Path
import copy,datetime,hashlib,json,sys
import yaml
R=Path.cwd();O=R/'reports/all_unmatched_20261107/worker-03/successors/issue1226-v1';T=R/'.temp/w03-provenance-successor-v1/technical';A=R/'reports/all_unmatched_20261107/worker-03';S=R.parents[2]/'preflight/w03-current-provenance-allowlist-v1';CUR=A/'successors/issue1224-v1/publication-v1'
sys.path.insert(0,str(R/'src'))
from mediaingredientmech.validation.write_validated import validate_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
from mediaingredientmech.synonym_policy import is_resolving_synonym
sha=lambda b:hashlib.sha256(b).hexdigest()
can=lambda v:json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()
read=lambda p:json.loads(p.read_bytes())
def regular(p):
 assert p.is_file() and not p.is_symlink(),str(p)
 return p.read_bytes()
allowbytes=regular(S/'repair-allowlist.json');assert sha(allowbytes)=='9b8283520ab7f9911f4997d62a85aea798f634bd8e8ed69c60dd77a26cdeec9d'
allow={x['proposal_id']:x for x in json.loads(allowbytes)['rows']}
proposals=read(CUR/'proposals.json')['proposals'];props={p['proposal_id']:p for p in proposals};assert len(props)==len(proposals)==74
cases=read(CUR/'decisions.json')['decisions'];assert len(cases)==188 and len({x['case_id'] for x in cases})==188
case_map={x['case_id']:x for x in cases}
bridge_doc=read(O/'payload-bridge.json');entries=bridge_doc['entries'];bridges={b['proposal_id']:b for b in entries};assert len(bridges)==len(entries)==49 and set(bridges)==set(allow)
assert bridge_doc['selected_predecessor_head']=='f6bfbf3c185f705484aa106405f813209146c766'
assert bridge_doc['writer_sha256']==sha(regular(R/'.temp/w03-provenance-successor-v1/provenance_writer_v2.py'))=='3b15bce56791af306b5db44f44b73d489f5203a23f36f4959084e10a402fc66a'
assert bridge_doc['allowlist_sha256']==sha(allowbytes)
ret=read(O/'scientific-field-retention.json');ret_rows={x['proposal_id']:x for x in ret['proposal_rows']};assert len(ret['proposal_rows'])==len(ret_rows)==74 and set(ret_rows)==set(props)
now=datetime.datetime.now(datetime.timezone.utc);issue=read(R/'.temp/w03-provenance-successor-v1/context/issue1246.json');issue_time=datetime.datetime.fromisoformat(issue['created_at'].replace('Z','+00:00'))
rows=[];before_records={};after_records={};old_manual=[];new_manual=[];authentic_before=[]
for pid,p in props.items():
 src=A/p['after_capture']['path'];raw=regular(src);old=yaml.safe_load(raw);assert sha(raw)==p['after_capture']['sha256'];before_records[p['owner_path']]=old
 b=bridges.get(pid);dest=R/b['new_payload_path'] if b else src;newraw=regular(dest);new=yaml.safe_load(newraw)
 assert not validate_ingredient(new),(pid,validate_ingredient(new))
 if b:
  a=allow[pid];assert a['published_payload_path']==str(src.relative_to(R));assert sha(raw)==a['payload']['sha256']==b['before_payload_sha256'];assert sha(newraw)==b['after_payload_sha256']==b['after_capture']['sha256']
  assert b['after_capture']['root']=='artifact' and A/b['after_capture']['path']==dest
  assert b['original_proposal']==p and b['original_authorship_and_reviews']==a['author_evidence'] and b['authentic_before']==a['authentic_before']
  assert a['case_ids']==p['case_ids'] and all(case_map[k]['case_input_sha256']==v for k,v in a['case_input_sha256'].items())
  assert old['identifier']==a['current_identifier'] and old['mapping_status']==a['current_mapping_status']
  oldobj=old['ontology_mapping']['evidence'][0];newobj=new['ontology_mapping']['evidence'][0]
  assert oldobj==a['complete_mapping_evidence_object']==b['old_object'];assert sha(can(oldobj))==a['complete_object_canonical_sha256']==b['old_object_sha256']
  expected_obj=copy.deepcopy(oldobj);assert expected_obj['evidence_type']=='MANUAL_CURATION';expected_obj['evidence_type']='LLM_SUGGESTION';assert newobj==expected_obj==b['new_object'] and sha(can(newobj))==b['new_object_sha256']
  parent={k:v for k,v in old['ontology_mapping'].items() if k!='evidence'};assert parent==a['parent_context']==b['parent_context'];assert sha(can(parent))==a['parent_context_sha256'];assert parent=={k:v for k,v in new['ontology_mapping'].items() if k!='evidence'}
  assert sha(can(old['curation_history']))==a['history_prefix_sha256']==b['before_history_sha256'];event=b['appended_history'];expected=copy.deepcopy(old);expected['ontology_mapping']['evidence'][0]['evidence_type']='LLM_SUGGESTION';expected['curation_history'].append(event);assert new==expected
  assert set(event)=={'timestamp','curator','action','changes','previous_status','new_status','llm_assisted'}
  assert event['action']=='CORRECTED_EVIDENCE_PROVENANCE' and event['llm_assisted'] is True and event['curator']=='codex-worker03 /root provenance successor';assert event['previous_status']==event['new_status']==old['mapping_status'];assert 'issues/1226' in event['changes'] and a['audit_row_id'] in event['changes']
  ts=datetime.datetime.fromisoformat(event['timestamp']);assert issue_time<ts<=now
  assert new['curation_history'][:-1]==old['curation_history'] and len(new['curation_history'])==len(old['curation_history'])+1
  proj=copy.deepcopy(new);proj['ontology_mapping']['evidence'][0]['evidence_type']='PROJECTION_ENUM';proj.pop('curation_history');assert sha(can(proj))==b['scientific_projection_sha256']
  if a['authentic_before'] is not None:
   beforebytes=regular(R/a['authentic_before_path']);assert sha(beforebytes)==a['authentic_before']['sha256']==p['before_sha256'];assert beforebytes==regular(S/a['authentic_before']['path']);before=yaml.safe_load(beforebytes);assert oldobj not in before.get('ontology_mapping',{}).get('evidence',[])
   assert {k:v for k,v in before.get('ontology_mapping',{}).items() if k!='evidence'}==a['before_parent_context'];authentic_before.append({'proposal_id':pid,'path':a['authentic_before_path'],'sha256':sha(beforebytes)})
  else:assert p['kind']=='new_owner' and p['before_sha256'] is None and not (R/p['owner_path']).exists()
 else:assert newraw==raw
 rr=ret_rows[pid];assert rr['changed']==bool(b) and rr['old_sha256']==sha(raw) and rr['new_sha256']==sha(newraw) and rr['entire_science_and_all_other_fields_retained'] is True and rr['new_native_schema_errors']==[]
 for idx,e in enumerate(old.get('ontology_mapping',{}).get('evidence',[])):
  if e['evidence_type']=='MANUAL_CURATION':old_manual.append((pid,idx,e))
 for idx,e in enumerate(new.get('ontology_mapping',{}).get('evidence',[])):
  if e['evidence_type']=='MANUAL_CURATION':new_manual.append((pid,idx,e))
 rows.append({'proposal_id':pid,'old_path':str(src.relative_to(R)),'old_sha256':sha(raw),'selected_path':str(dest.relative_to(R)),'selected_sha256':sha(newraw),'changed':bool(b),'only_allowed_semantic_delta':bool(b),'all_other_fields_and_prior_history_retained':True,'schema_errors':[],'source_science_reapproved':False})
 after_records[p['owner_path']]=new
assert len(before_records)==len(after_records)==74
assert len(old_manual)==52 and len(new_manual)==3
assert {(p,i) for p,i,e in new_manual}=={('b-proposal-marine-aliases',0),('c-copper-trihydrate-alias',4),('m-arabinan_source_alias',2)}
assert all(x in old_manual for x in new_manual)
assert 'b-proposal-cm0149-form' not in props
ox=next(x for x in rows if x['proposal_id']=='w03-oxoid-cm0149-product-1224-v1');assert ox['selected_sha256']==ox['old_sha256']=='1ec7554da19d5a6ab2259ee79d178a95511a923e611f4fc176af498248ab76ae' and not ox['changed']
expected_paths={str((R/b['new_payload_path']).relative_to(O/'payloads')) for b in entries};actual_paths={str(p.relative_to(O/'payloads')) for p in (O/'payloads').rglob('*') if p.is_file()};assert actual_paths==expected_paths and len(actual_paths)==49;assert not any(p.is_symlink() for p in (O/'payloads').rglob('*'))
manifest=read(S/'MANIFEST.json');assert len(manifest['files'])==122
for x in manifest['files']:assert regular(S/x['path'])==regular(O/'context/allowlist'/x['path']) and sha(regular(S/x['path']))==x['sha256']
assert regular(S/'MANIFEST.json')==regular(O/'context/allowlist/MANIFEST.json')
baseline={str(p.relative_to(R)):yaml.safe_load(p.read_bytes()) for kind in ['mapped','unmapped'] for p in (R/'data/ingredients'/kind).glob('*.yaml')};assert len(baseline)==2956
old_overlay=baseline|before_records;new_overlay=baseline|after_records;assert len(old_overlay)==len(new_overlay)==2996
part_before=[str(v) for v in validate_component_partonomy(old_overlay.values())];part_after=[str(v) for v in validate_component_partonomy(new_overlay.values())];assert part_before==part_after==[]
def identity(d):
 return [(k,v.get('identifier'),v.get('mapping_status'),v.get('ontology_mapping',{}).get('ontology_id'),v.get('ontology_mapping',{}).get('mapping_quality'),[(s.get('synonym_text'),s.get('synonym_type')) for s in v.get('synonyms',[]) if is_resolving_synonym(s)]) for k,v in sorted(d.items())]
assert identity(old_overlay)==identity(new_overlay)
native=read(O/'validation/native-payloads.json');assert native['changed_schema_records']==49 and native['complete_schema_records']==74 and native['baseline_native_owner_count']==2956 and native['complete_proposal_overlay_count']==2996 and native['before_partonomy_violations']==part_before and native['after_partonomy_violations']==part_after
# Meaningful in-memory negative reference control. It creates no output record.
control=copy.deepcopy(next(v for v in after_records.values() if v.get('components')));control['components'][0]['reference_scope']='MIM_CATALOG';control['components'][0]['component_id']='kgmicrobe.ingredient:guard_reference_absent_w03_1246';assert all(v.get('identifier')!='kgmicrobe.ingredient:guard_reference_absent_w03_1246' for v in new_overlay.values());control_errors=[str(v) for v in validate_component_partonomy([*new_overlay.values(),control])];assert any(v.startswith('UNRESOLVED_MIM_REFERENCE\t') for v in control_errors)
prior_inventory=read(T/'maintained-inventory-before.json');maintained_changed=[]
for x in prior_inventory['baseline_files']:
 p=R/x['path']
 if not p.is_file() or p.is_symlink() or sha(p.read_bytes())!=x['sha256']:maintained_changed.append(x['path'])
assert not maintained_changed
old_inv={x['path']:x['sha256'] for x in prior_inventory['ignored_inclusive_root_inventory']['regular_files']};current_inv={};symlinks=[]
for prefix in prior_inventory['ignored_inclusive_root_inventory']['declared_roots']:
 for p in (R/prefix).rglob('*'):
  if p.is_symlink():symlinks.append(str(p.relative_to(R)))
  elif p.is_file():current_inv[str(p.relative_to(R))]=sha(p.read_bytes())
assert old_inv==current_inv and not symlinks
report={'reviewer':'/root/provenance_controls','at':now.isoformat(),'status':'PASS_EXACT_CANDIDATE_PAYLOAD_TECHNICAL_SCOPE','scientific_review':False,'scope':'49 exact metadata replacements and complete74 candidate payload selection; preexisting188-case source selection checked, final new core not yet available or approved. No source-science, whole-owner, role, supported-export or release approval.','counts':{'old_source_cases':188,'payloads':74,'enum_replacements':49,'history_appends':49,'unchanged_payloads':25,'authentic_existing_beforeimages':len(authentic_before),'new_owner_null_beforeimages':49-len(authentic_before),'remaining_inherited_manual':3,'packet_manifest_members':122},'payloads':rows,'authentic_beforeimages':authentic_before,'inherited_manual_objects':[{'proposal_id':p,'index':i,'complete_object':e} for p,i,e in new_manual],'native_checks':{'closed_schema_records':74,'partonomy_baseline_records':2956,'partonomy_complete_overlay_records':2996,'before_violations':part_before,'after_violations':part_after,'identity_and_resolving_alias_projection_unchanged':True,'in_memory_negative_component_control':{'expected':'UNRESOLVED_MIM_REFERENCE','actual':control_errors,'record_written':False},'limitations':'Partonomy resolves one-or-more active identity claims and allows baseline duplicate IDs; it does not prove unique owner identity, chemical forms, source applicability or source-scoped scientific approval.'},'maintained_retention':{'baseline_files_rehashed':len(prior_inventory['baseline_files']),'changed':maintained_changed,'ignored_inclusive_root_regular_files':len(current_inv),'inventory_unchanged':True,'declared_roots':prior_inventory['ignored_inclusive_root_inventory']['declared_roots']},'artifacts':[{'path':str(p.relative_to(R)),'sha256':sha(regular(p))} for p in [O/'payload-bridge.json',O/'scientific-field-retention.json',O/'validation/native-payloads.json',R/'.temp/w03-provenance-successor-v1/provenance_writer_v2.py',R/'.temp/w03-provenance-successor-v1/build_candidates_v2.py',S/'repair-allowlist.json',CUR/'decisions.json',CUR/'proposals.json',CUR/'evidence.json']]}
p=T/'candidate-payload-review-v1.json'
with p.open('x') as f:json.dump(report,f,indent=2,ensure_ascii=False);f.write('\n')
print(json.dumps({'path':str(p.relative_to(R)),'sha256':sha(p.read_bytes()),'counts':report['counts'],'status':report['status']},indent=2))
