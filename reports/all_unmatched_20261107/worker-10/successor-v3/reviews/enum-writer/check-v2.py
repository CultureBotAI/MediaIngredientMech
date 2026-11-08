"""Independent read-only function/input audit; never invoke writer main or positive writes."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,copy,runpy,collections,yaml
R=Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v3';D=S/'reviews/enum-writer';N=S/'enum'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
canon=lambda d:hashlib.sha256(json.dumps(d,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
load=lambda p:json.loads(p.read_text())
def save(p,d):
 with p.open('x') as f:json.dump(d,f,indent=2,ensure_ascii=False);f.write('\n')
started=datetime.now(timezone.utc).isoformat()
helper=R/'.temp/all-unmatched-worker-10/successor-v3/enum_successor.py'
assert sha(helper)=='62ad7f3f485e12454b60c55e8a2c859f530fdfd5b236c6af637fd6021ec35623'
inputs=[helper,N/'negative-controls-preflight-v2.json',N/'w10-current-rebind-v1.json',S/'science-v1/proposals.json',S/'science-v1/retirement-bridge.json',S/'serums/mapping-claim-correspondence.json',S/'hcl-manual/mapping-claim-correspondence.json',A/'successor-v2/proposals.json']
(D/'inputs-v2').mkdir(exist_ok=True)
receipt=[]
for i,p in enumerate(inputs):
 dest=D/'inputs-v2'/f'{i:02d}-{p.name}'
 with dest.open('xb') as f:f.write(p.read_bytes())
 receipt.append({'original_path':str(p.relative_to(R)),'snapshot_path':str(dest.relative_to(R)),'sha256':sha(p)})
m=runpy.run_path(str(helper),run_name='independent_review_no_main')
base=load(A/'successor-v2/proposals.json')['proposals'];bp={p['proposal_id']:p for p in base}
source=load(S/'science-v1/proposals.json');sp={p['proposal_id']:p for p in source['proposals']}
rebind=load(N/'w10-current-rebind-v1.json');rows=rebind['rows']
bridge=load(S/'science-v1/retirement-bridge.json');oldnew={r['old_proposal_id']:r.get('selected_proposal_id') for r in bridge['rows']}
assert len(oldnew)==len(bridge['rows'])==len(base) and set(oldnew)==set(bp)
for r in bridge['rows']:
 p=bp[r['old_proposal_id']];assert r['old_proposal_sha256']==canon(p);assert r['old_payload']==p['after_capture'];assert r['old_before_sha256']==p['before_sha256'];assert r['old_owner_path']==p['owner_path'];assert r['old_case_ids']==p['case_ids']
 if r['selected_proposal_id']:
  q=sp[r['selected_proposal_id']];assert r['selected_payload']==q['after_capture'];assert r['selected_owner_path']==q['owner_path'];assert r['selected_before_sha256']==q['before_sha256']
controls=m['controls'](rows,base)
assert controls==load(N/'negative-controls-preflight-v2.json')['controls']
correspondences=[];full_bindings=[]
for c in load(S/'serums/mapping-claim-correspondence.json')['claims']:
 if c.get('before_claim') is not None:
  p=bp[c['old_proposal_id']];old=yaml.safe_load((A/p['after_capture']['path']).read_text());assert c['before_claim'] in old.get('ontology_mapping',{}).get('evidence',[]);assert canon(c['before_claim'])==c['before_claim_sha256']
 if c.get('after_claim') is not None:
  p=sp[c['new_proposal_id']];new=yaml.safe_load((A/p['after_capture']['path']).read_text());idx=int(c['pointer'].rsplit('/',1)[1]);assert new['ontology_mapping']['evidence'][idx]==c['after_claim'];assert canon(c['after_claim'])==c['after_claim_sha256']
 if c.get('before_claim') is not None and c.get('after_claim') is not None:
  correspondences.append(dict(c,successor_index=int(c['pointer'].rsplit('/',1)[1])))
for entry in load(S/'hcl-manual/mapping-claim-correspondence.json')['entries']:
 oldpid=entry['original_proposal_id'];newpid=entry['successor_proposal_id'];assert bp[oldpid]['after_capture']==entry['old_payload'];assert sp[newpid]['after_capture']==entry['successor_payload']
 for key in ['old_payload','successor_payload']:assert sha(A/entry[key]['path'])==entry[key]['sha256']
 full_bindings.append({'old_proposal_id':oldpid,'new_proposal_id':newpid,'before_payload':entry['old_payload'],'after_payload':entry['successor_payload'],'exact_binding':True})
 for c in entry['claim_correspondences']:
  old=yaml.safe_load((A/entry['old_payload']['path']).read_text());new=yaml.safe_load((A/entry['successor_payload']['path']).read_text());assert old['ontology_mapping']['evidence'][c['original_index']]==c['original_claim'];assert new['ontology_mapping']['evidence'][c['successor_index']]==c['successor_claim']
  correspondences.append({'old_proposal_id':oldpid,'new_proposal_id':newpid,'before_claim':c['original_claim'],'after_claim':c['successor_claim'],'successor_index':c['successor_index']})
# Extra full-object/identity controls on the correspondence resolver; no writes.
c=next(x for x in correspondences if x['before_claim']!=x['after_claim']);v=c['before_claim'];es=[copy.deepcopy(c['after_claim'])];cc=dict(copy.deepcopy(c),successor_index=0)
extra=[]
for name,oid,nid,vals,cs in [
 ('wrong-original-proposal',c['old_proposal_id']+'-wrong',c['new_proposal_id'],es,[cc]),
 ('wrong-successor-proposal',c['old_proposal_id'],c['new_proposal_id']+'-wrong',es,[cc]),
 ('ambiguous-correspondence',c['old_proposal_id'],c['new_proposal_id'],es,[cc,copy.deepcopy(cc)]),
 ('different-full-successor',c['old_proposal_id'],c['new_proposal_id'],[dict(es[0],notes='unrelated')],[cc])]:
 try:m['explicit_successor'](oid,nid,v,vals,cs)
 except ValueError as e:extra.append({'control':name,'refused':True,'reason':str(e)})
 else:raise AssertionError(name)
shift=dict(copy.deepcopy(cc),successor_index=1);idx,_=m['explicit_successor'](c['old_proposal_id'],c['new_proposal_id'],v,[{'unrelated':True},copy.deepcopy(c['after_claim'])],[shift]);assert idx==1
per_rows=[];per_payload=[];final_mem={};count=collections.Counter();before_hashes={}
for p in source['proposals']:
 path=A/p['after_capture']['path'];assert sha(path)==p['after_capture']['sha256'];before=m['owner_preimage'](p);before_hashes[p['owner_path']]=p['before_sha256'];original=yaml.safe_load(path.read_text());d=copy.deepcopy(original);changed=[]
 for oldpid in [x for x,y in oldnew.items() if y==p['proposal_id']]:
  for row in [r for r in rows if r['proposal_id']==oldpid]:
   assert row['current_capture']==bp[oldpid]['after_capture'] and row['owner_path']==bp[oldpid]['owner_path'] and row['before_sha256']==bp[oldpid]['before_sha256'];assert sha(A/row['current_capture']['path'])==row['current_capture']['sha256'];m['owner_preimage'](bp[oldpid]);assert canon(row['full_value'])==row['complete_claim_sha256']
   es=d.get('ontology_mapping',{}).get('evidence',[]);v=row['full_value']
   if v in es:
    idx=m['authorized_change'](d,before,row,sha(path),p['after_capture']['sha256']);changed.append(idx);disposition='retyped_exact_surviving_agent_claim'
   else:
    assert p['after_capture']!=bp[oldpid]['after_capture'];idx,corr=m['explicit_successor'](oldpid,p['proposal_id'],v,es,correspondences);assert es[idx] not in before.get('ontology_mapping',{}).get('evidence',[]);disposition='superseded_by_source_reassessed_agent_claim'
   count[disposition]+=1;per_rows.append({'audit_row_id':row['audit_row_id'],'old_proposal_id':oldpid,'selected_proposal_id':p['proposal_id'],'disposition':disposition,'index':idx,'original_full_claim_sha256':canon(v),'selected_full_claim_sha256':canon(d['ontology_mapping']['evidence'][idx]),'selected_payload':p['after_capture'],'all_context_hashes_verified':True})
 rollback=copy.deepcopy(d)
 for idx in changed:rollback['ontology_mapping']['evidence'][idx]['evidence_type']='MANUAL_CURATION'
 assert rollback==original
 old_history=copy.deepcopy(d.get('curation_history',[]))
 if changed:
  event=m['record_curation_event'](d,curator='Independent in-memory implementation control',action='CORRECTED_AGENT_MAPPING_EVIDENCE_PROVENANCE',changes='In-memory test only, never saved as a proposal.',previous_status=d.get('mapping_status'),new_status=d.get('mapping_status'),llm_assisted=True)
  assert d['curation_history'][:-1]==old_history and len(d['curation_history'])==len(old_history)+1
  history_only=copy.deepcopy(d);history_only['curation_history']=old_history
  if 'curation_history' not in original:history_only.pop('curation_history')
  for idx in changed:history_only['ontology_mapping']['evidence'][idx]['evidence_type']='MANUAL_CURATION'
  assert history_only==original
 final_mem[p['proposal_id']]=d
 for e in d.get('ontology_mapping',{}).get('evidence',[]):
  if e.get('evidence_type')=='MANUAL_CURATION':assert e in before.get('ontology_mapping',{}).get('evidence',[])
 per_payload.append({'proposal_id':p['proposal_id'],'payload':p['after_capture'],'before_sha256':p['before_sha256'],'owner_path':p['owner_path'],'changed_indices':changed,'all_non_enum_fields_exact_before_history_append':True,'history_prefix_exact':True})
for row in rows:
 if oldnew[row['proposal_id']] is None:
  count['historical_candidate_retired_from_active_selection']+=1;per_rows.append({'audit_row_id':row['audit_row_id'],'old_proposal_id':row['proposal_id'],'selected_proposal_id':None,'disposition':'historical_candidate_retired_from_active_selection','original_full_claim_sha256':canon(row['full_value'])})
assert len(per_rows)==len(rows)==len({r['audit_row_id'] for r in per_rows})
historical=[]
for ex in rebind['unchanged_historical_manual_excluded']:
 p=bp[ex['proposal_id']];before=m['owner_preimage'](p);selected=final_mem[oldnew[ex['proposal_id']]];v=ex.get('full_value',ex.get('claim'));print('HIST_KEYS',list(ex))
 if v is None:
  idx=int(ex['field'].split('[')[1].split(']')[0]);v=yaml.safe_load((A/p['after_capture']['path']).read_text())['ontology_mapping']['evidence'][idx]
 assert v in before['ontology_mapping']['evidence'] and v in selected['ontology_mapping']['evidence'];historical.append({'proposal_id':ex['proposal_id'],'full_claim_sha256':canon(v),'exact_in_authentic_before_and_selected':True,'authorship_certified_human':False})
for item in receipt:assert sha(R/item['original_path'])==item['sha256']
finished=datetime.now(timezone.utc).isoformat()
result={'audit_execution_started_at':started,'audit_execution_finished_at':finished,'script_sha256':sha(helper),'review_check_script_sha256':sha(Path(__file__)),'input_receipt':receipt,'scope':'Read-only source/input inspection plus in-memory function execution only. main() and positive writer never called.','supplied_refusal_controls':controls,'additional_refusal_controls':extra,'explicit_shifted_index_control_passed':True,'source_full_payload_correspondence_checks':full_bindings,'counts':{'original_proposals':len(base),'selected_proposals':len(source['proposals']),'original_allowlisted_claims':len(rows),'claim_dispositions':dict(count),'payloads_with_in_memory_retypes':sum(bool(p['changed_indices']) for p in per_payload),'in_memory_retyped_claims':sum(len(p['changed_indices']) for p in per_payload),'historical_exclusions':len(historical)},'rows':per_rows,'payload_checks':per_payload,'historical_exclusions':historical,'unchanged_inputs_at_finish':True,'helper_main_executed':False,'payload_writes':0}
save(D/'function-checks-v2.json',result)
print(json.dumps(result['counts'],indent=2));print('OUTPUT_SHA',sha(D/'function-checks-v2.json'))
