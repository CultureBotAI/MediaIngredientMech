"""Claim-specific #1226 correction in report artifacts only; never a corpus migration."""
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, copy, re, sys, collections, yaml
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.write_validated import write_validated_ingredient
R=Path.cwd(); A=R/'reports/all_unmatched_20261107/worker-10'; S=A/'successor-v3'; N=S/'enum'; B=A/'successor-v2'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
canon=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
load=lambda p:json.loads(p.read_text())
def save(p,d):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x') as f:json.dump(d,f,indent=2,ensure_ascii=False);f.write('\n')
def authorized_change(record, before, audit, payload_sha, expected_sha):
 if payload_sha!=expected_sha:raise ValueError('stale payload')
 if audit['classification']!='new_agent_record' or audit['type_recommendation']!='LLM_SUGGESTION':raise ValueError('not a confirmed new agent judgment')
 m=re.fullmatch(r'ontology_mapping.evidence\[(\d+)\]',audit['field'])
 if not m:raise ValueError('not MappingEvidence')
 v=audit['full_value'];es=record.get('ontology_mapping',{}).get('evidence',[]);old=before.get('ontology_mapping',{}).get('evidence',[])
 if canon(v)!=audit['complete_claim_sha256']:raise ValueError('claim hash mismatch')
 if v in old:raise ValueError('historical object')
 positions=[i for i,e in enumerate(es) if e==v]
 if len(positions)!=1:raise ValueError('absent or ambiguous complete claim')
 if v.get('evidence_type')!='MANUAL_CURATION' or not audit['author_events'] or not audit['actual_author_review_scopes']:raise ValueError('missing author provenance')
 index=positions[0];record['ontology_mapping']['evidence'][index]['evidence_type']='LLM_SUGGESTION';return index

def guarded_new(record, dest):
 root=(N/'proposed').resolve();target=dest.resolve()
 if not target.is_relative_to(root) or target==root:raise ValueError('outside report-only destination')
 if dest.exists() or dest.is_symlink():raise ValueError('immutable destination already exists')
 write_validated_ingredient(record,dest)
 assert yaml.safe_load(dest.read_text())==record

def controls(rows,base):
 r=rows[0];p=next(p for p in base if p['proposal_id']==r['proposal_id']);d=yaml.safe_load((A/p['after_capture']['path']).read_text());expected=p['after_capture']['sha256'];out=[]
 for name,record,before,audit,actual,exp in [
 ('stale-payload',copy.deepcopy(d),{},copy.deepcopy(r),'0'*64,expected),
 ('historical-human-object',copy.deepcopy(d),{'ontology_mapping':{'evidence':[copy.deepcopy(r['full_value'])]}},copy.deepcopy(r),expected,expected),
 ('component-enum',copy.deepcopy(d),{},dict(copy.deepcopy(r),field='component_assertion.evidence[0]'),expected,expected),
 ('mismatched-complete-value',copy.deepcopy(d),{},dict(copy.deepcopy(r),complete_claim_sha256='0'*64),expected,expected),
 ('duplicate-claim-ambiguity',dict(copy.deepcopy(d),ontology_mapping=dict(copy.deepcopy(d['ontology_mapping']),evidence=[copy.deepcopy(r['full_value']),copy.deepcopy(r['full_value'])])),{},copy.deepcopy(r),expected,expected)]:
  try:authorized_change(record,before,audit,actual,exp)
  except ValueError as e:out.append({'control':name,'refused':True,'reason':str(e)})
  else:raise AssertionError(name)
 for name,dest in [('outside-path',R/'.temp/all-unmatched-worker-10/successor-v3/should-not-write.yaml'),('historical-destination',A/p['after_capture']['path'])]:
  try:guarded_new(d,dest)
  except ValueError as e:out.append({'control':name,'refused':True,'reason':str(e)})
  else:raise AssertionError(name)
 return out

def main():
 core=S/(sys.argv[1] if len(sys.argv)>1 else 'science-v1'); source=load(core/'proposals.json');base=load(B/'proposals.json')['proposals'];rebind=load(N/'w10-current-rebind-v1.json');rows=rebind['rows'];bp={p['proposal_id']:p for p in base};props=source['proposals'];sp={p['proposal_id']:p for p in props}; bridge=load(core/'retirement-bridge.json');oldnew={x['old_proposal_id']:x.get('selected_proposal_id') for x in bridge['rows']};assert set(oldnew)==set(bp)
 save(N/'negative-controls.json',{'at':datetime.now(timezone.utc).isoformat(),'controls':controls(rows,base),'scope':'Private allowlist safety checks; no new maintained gate.'})
 bypid=collections.defaultdict(list)
 for row in rows:bypid[row['proposal_id']].append(row)
 decisions=[]; changes=[];newprops=[]
 for p in props:
  pp=copy.deepcopy(p);path=A/p['after_capture']['path'];assert sha(path)==p['after_capture']['sha256'];before=yaml.safe_load((R/p['owner_path']).read_text()) if p['before_sha256'] else {};d=yaml.safe_load(path.read_text());original=copy.deepcopy(d);altered=[]
  ancestors=[old for old,new in oldnew.items() if new==p['proposal_id']]
  for oldpid in ancestors:
   for row in bypid.get(oldpid,[]):
    es=d.get('ontology_mapping',{}).get('evidence',[]);v=row['full_value'];matches=[i for i,e in enumerate(es) if e==v]; disp={'audit_row_id':row['audit_row_id'],'original_proposal_id':oldpid,'selected_proposal_id':p['proposal_id'],'original_field':row['field'],'original_complete_claim_sha256':row['complete_claim_sha256'],'science_capture':p['after_capture'],'current_owner_path':p['owner_path'],'authentic_before_sha256':p['before_sha256'],'original_full_value':v,'actual_author_events':row['author_events'],'claim_specific_basis':row['claim_basis']}
    if matches:
     index=authorized_change(d,before,row,sha(path),p['after_capture']['sha256']);altered.append(index);disp.update(disposition='retyped_exact_surviving_agent_claim',selected_field=f'ontology_mapping.evidence[{index}]',selected_full_value=copy.deepcopy(d['ontology_mapping']['evidence'][index]))
    else:
     # A source author changed this exact claim only in the authorized scientific correction.
     # Bind its complete successor at the same explicit slot; no inference from a mere string match.
     assert p['after_capture']!=bp[oldpid]['after_capture'],oldpid
     idx=int(re.fullmatch(r'ontology_mapping.evidence\[(\d+)\]',row['field']).group(1));assert idx<len(es),(oldpid,'missing explicit successor claim')
     successor=es[idx];assert successor.get('evidence_type')=='LLM_SUGGESTION',(oldpid,idx,'author must type revised claim honestly')
     assert successor not in before.get('ontology_mapping',{}).get('evidence',[])
     disp.update(disposition='superseded_by_source_reassessed_agent_claim',selected_field=f'ontology_mapping.evidence[{idx}]',selected_full_value=copy.deepcopy(successor),basis='Filed #1237 source correction replaces the complete claim; source-author full-payload correspondence and separate skeptical review are required. Original claim remains immutable historical evidence.')
    disp['selected_complete_claim_sha256']=canon(disp['selected_full_value']);decisions.append(disp)
  if altered:
   rollback=copy.deepcopy(d)
   for i in altered:rollback['ontology_mapping']['evidence'][i]['evidence_type']='MANUAL_CURATION'
   assert rollback==original
   event=record_curation_event(d,curator='Codex worker10 /root claim-specific provenance correction',action='CORRECTED_AGENT_MAPPING_EVIDENCE_PROVENANCE',changes='Issue #1226: retype only the independently audited new agent-authored MappingEvidence judgments at indices '+', '.join(map(str,altered))+' from human-only MANUAL_CURATION to LLM_SUGGESTION. Exact sources, notes, quantities, scientific conclusions, unchanged historical MappingEvidence (authorship not recertified), ComponentEvidenceTypeEnum objects, prior history and all source/role/export holds remain unchanged. This is provenance correction, not renewed scientific or release approval.',previous_status=d.get('mapping_status'),new_status=d.get('mapping_status'),llm_assisted=True)
   dest=N/'proposed'/(p['proposal_id']+'.yaml');guarded_new(d,dest);pp['after_capture']={'root':'artifact','path':str(dest.relative_to(A)),'sha256':sha(dest)};pp['provenance_successor']={'issue':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1226','previous_capture':p['after_capture'],'exact_claim_indices':altered,'scope':'MappingEvidence type and one appended truthful history event only; source science retained.'}
   changes.append({'proposal_id':p['proposal_id'],'previous_capture':p['after_capture'],'new_capture':pp['after_capture'],'indices':altered,'event':event,'all_other_fields_equal':True,'before_sha256':p['before_sha256']})
  newprops.append(pp)
 for oldpid,these in bypid.items():
  if oldnew[oldpid] is None:
   for row in these:decisions.append({'audit_row_id':row['audit_row_id'],'original_proposal_id':oldpid,'selected_proposal_id':None,'original_field':row['field'],'original_complete_claim_sha256':row['complete_claim_sha256'],'original_full_value':row['full_value'],'disposition':'historical_candidate_retired_from_active_selection','basis':'Filed source-continuity finding prevents parallel owner selection. Original bytes and typing preserved as historical, unselected proposal; no claim relabeled or active approval inherited. See complete proposal/case retirement bridge.'})
 assert len(decisions)==len(rows) and len({x['audit_row_id'] for x in decisions})==len(rows)
 for d in decisions:
  if d.get('selected_proposal_id'):d['final_selected_capture']=next(p['after_capture'] for p in newprops if p['proposal_id']==d['selected_proposal_id'])
 for p in newprops:
  d=yaml.safe_load((A/p['after_capture']['path']).read_text());before=yaml.safe_load((R/p['owner_path']).read_text()) if p['before_sha256'] else {};be=before.get('ontology_mapping',{}).get('evidence',[])
  for e in d.get('ontology_mapping',{}).get('evidence',[]):
   if e.get('evidence_type')=='MANUAL_CURATION':assert e in be,(p['proposal_id'],e)
 source['proposals']=newprops;save(N/'proposals-fragment.json',source)
 save(N/'claim-dispositions.json',{'at':datetime.now(timezone.utc).isoformat(),'reviewer':'Codex worker10 /root; metadata author, not independent final skeptic','audit_source':{'path':'successor-v3/enum/w10-original-audit-rows.json','sha256':sha(N/'w10-original-audit-rows.json')},'original_flagged_claims':len(rows),'original_flagged_proposals':len(bypid),'rows':decisions,'historical_exclusions':rebind['unchanged_historical_manual_excluded'],'counts':dict(collections.Counter(x['disposition'] for x in decisions)),'scientific_approval':False})
 save(N/'metadata-change-proof.json',{'at':datetime.now(timezone.utc).isoformat(),'script_sha256':sha(Path(__file__)),'changed_payloads':changes,'new_payload_count':len(changes),'claim_count':sum(len(x['indices']) for x in changes),'scientific_fields_equal':True,'full_payload_provenance_review_pending':True})
 print(json.dumps({'selected_proposals':len(newprops),'metadata_changed_payloads':len(changes),'claim_dispositions':dict(collections.Counter(x['disposition'] for x in decisions))},indent=2))
if __name__=='__main__':main()
