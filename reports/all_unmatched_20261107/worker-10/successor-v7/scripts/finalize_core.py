"""Append actual completed review bindings; no payload or historical-core rewrite."""
from pathlib import Path
import json,hashlib,datetime,copy,shutil,subprocess
R=Path.cwd();C=R.parents[2];A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v7';O=R/'.temp/columbia-controls-successor-v1';F=S/'final-core';F.mkdir()
load=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();oh=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest();now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(p,x):
 with p.open('x') as f:json.dump(x,f,indent=2,ensure_ascii=False);f.write('\n')
def cap(p):return {'root':'artifact','path':str(p.relative_to(A)),'sha256':sha(p)}
review_defs=[('science','scientific-review-v1.json','sv7-independent-science'),('lineage','author-v3-lineage-review.json','sv7-independent-lineage'),('technical','author-technical-review-v1.json','sv7-independent-technical')]
for sub,_,_ in review_defs:
 dest=S/'reviews'/sub
 assert not dest.exists() or not list(dest.iterdir())
 if dest.exists():dest.rmdir()
 shutil.copytree(O/sub,dest)
 for p in (O/sub).rglob('*'):
  if p.is_file():assert sha(p)==sha(dest/p.relative_to(O/sub))
SCI=cap(S/'reviews/science/scientific-review-v1.json');LIN=cap(S/'reviews/lineage/author-v3-lineage-review.json');TECH=cap(S/'reviews/technical/author-technical-review-v1.json')
sc=load(A/SCI['path']);assert sc['status']=='PASS_BOUNDED_CORRECTION' and not sc['open_new_findings']
assert not load(A/LIN['path'])['findings'] and not load(A/TECH['path'])['findings']
scopes={'author':'worker10:/root','native_assembler':'worker10:/root','scientist':{'identity':sc['reviewer'],'scope':'Complete four changed candidate records, unchanged W10 Oxoid origin, primary sources and bounded source routing.','report':SCI,'authorship_disclosure':sc['authorship_and_independence']},'lineage_reviewer':{'identity':'worker10:/root/bio_research','scope':'Full188case/304occurrence/128proposal lineage and authentic preimages; original bio author supplies metadata review only.','report':LIN,'authorship_disclosure':load(A/LIN['path'])['authorship']},'technical_reviewer':{'identity':'worker10:/root/buffers_research','scope':'Native closed schema, guarded/helper roundtrips, full overlay, identifiers/aliases/projections and retained chemistry; original buffer author supplies technical review only.','report':TECH,'authorship_disclosure':load(A/TECH['path'])['independence']},'not_human_review':True,'root_wrapper_is_self_review':True}
save(S/'subagent-scopes.json',scopes)
# New active routing copies: historical author ledgers remain exact.
def reviewed_dep(obj):
 if isinstance(obj,dict):
  if obj.get('proposal_id')=='sv7-dependent-columbia-unmapped0118-partition' and 'review_state' in obj:
   obj['review_state']='complete_bounded_full_payload_review_application_not_approved';obj['exact_review_receipts']=[SCI,LIN,TECH]
  for v in obj.values():reviewed_dep(v)
 elif isinstance(obj,list):
  for v in obj:reviewed_dep(v)
for old,new in [('source-routing.json','source-routing-final.json'),('cross-worker-dependencies.json','cross-worker-dependencies-final.json')]:
 x=load(S/old);reviewed_dep(x);x['finalization']={'at':now(),'author_ledger':cap(S/old),'scope':'Review bindings only; all original source rows, quantities, origin captures and holds unchanged.','review_receipts':[SCI,LIN,TECH]};save(S/new,x)
Ddoc=load(S/'author-core-v3/decisions.json');Pdoc=load(S/'author-core-v3/proposals.json');Edoc=load(S/'author-core-v3/evidence.json');D=Ddoc['decisions'];P=Pdoc['proposals'];E=Edoc['evidence'];proof=load(S/'payload-change-proof.json');indices=proof['affected_case_indices'];caseids=[D[i]['case_id'] for i in indices];colids=[D[i]['case_id'] for i in [118,178]]
new_ev=[]
for sub,name,eid in review_defs:
 new_ev.append({'evidence_id':eid,'kind':'independent_review','capture':cap(S/'reviews'/sub/name),'url':None,'accessed_at':now(),'locator':'Complete exact report and preserved actual reviewer scope; original review times are inside.','supports_or_contradicts':scopes['scientist' if sub=='science' else 'lineage_reviewer' if sub=='lineage' else 'technical_reviewer']['scope'],'case_ids':caseids})
for name,eid in [('source-routing-final.json','sv7-reviewed-source-routing'),('cross-worker-dependencies-final.json','sv7-reviewed-external-origin-bindings')]:
 new_ev.append({'evidence_id':eid,'kind':'local_validation','capture':cap(S/name),'url':None,'accessed_at':now(),'locator':'Exact final review-dependent binding; prior author ledger is retained.','supports_or_contradicts':'Actual0118 dependency, seven separated context rows, W04 current original origin and one-family coordinator composition condition. No application or foreign case claimed.','case_ids':colids})
E.extend(new_ev);rids=[x[2] for x in review_defs];colrids=[x['evidence_id'] for x in new_ev[3:]]
changedids=set(proof['changed_original_metadata_proposal_ids']+[proof['new_dependent_proposal_id']])
for row in [D[i] for i in indices]+[p for p in P if p['proposal_id'] in changedids]:
 applicable=rids+(colrids if any(x in colids for x in row.get('case_ids',[row.get('case_id')])) else [])
 row['evidence_ids']+=applicable;row['independent_review']={'status':'complete','evidence_ids':rids}
 st=row['source_successor_v7'];st['review_state']='complete_bounded_exact_payload_and_metadata_review';st['actual_review_receipts']=[SCI,LIN,TECH]
 st['scope']='Bounded Columbia continuity/routing and two named-stock completeness corrections. Complete exact candidates independently reviewed; prior unaffected science and every source/whole-owner/role/export hold remain. Published-head integration review remains with coordinator.'
 if 'same_owner_dependency' in st:reviewed_dep(st['same_owner_dependency'])
 if 'routing' in st:st['routing']=cap(S/'source-routing-final.json')
 if 'historical_enum_finding' in st:
  st['historical_enum_finding']['correction_state']='exact_author_v3_correction_independently_rechecked';st['historical_enum_finding']['recheck_receipts']=[SCI,LIN,TECH]
 if 'review_status_explanation' in row:row['review_status_explanation']='Complete exact candidate and source-dependent metadata review, with actual independent science and disclosed original-author technical/lineage roles. Historical pending records remain in immutable author cores. No integration, whole-owner, role or export approval.'
for name,doc in [('decisions.json',Ddoc),('proposals.json',Pdoc),('evidence.json',Edoc)]:save(F/name,doc)
oldD=load(A/'successor-v6/final-core/decisions.json')['decisions'];oldP=load(A/'successor-v6/final-core/proposals.json')['proposals'];oldE=load(A/'successor-v6/final-core/evidence.json')['evidence'];oldBy={p['proposal_id']:p for p in oldP};newBy={p['proposal_id']:p for p in P}
assert E[:len(oldE)]==oldE
for i,(a,b) in enumerate(zip(oldD,D)):
 assert all(a[k]==b[k] for k in ['case_id','case_input_sha256','source','occurrence_ids','owner_records'])
 if i not in indices:assert a==b
for p in oldP:
 q=newBy[p['proposal_id']]
 if p['proposal_id'] not in changedids:assert p==q
 assert p['case_ids']==q['case_ids'] and p['before_sha256']==q['before_sha256'] and p['owner_path']==q['owner_path']
for p in P:assert sha(A/p['after_capture']['path'])==p['after_capture']['sha256']
counts={'cases':len(D),'occurrences':sum(len(d['occurrence_ids']) for d in D),'proposals':len(P),'evidence':len(E),'original_proposal_ids_retained':len(oldP),'new_dependent_existing_owner_proposals':1,'new_vendor_identities':0,'changed_original_payloads':sum(oldBy[p['proposal_id']]['after_capture']['sha256']!=p['after_capture']['sha256'] for p in P if p['proposal_id'] in oldBy),'unchanged_original_payloads':sum(oldBy[p['proposal_id']]['after_capture']['sha256']==p['after_capture']['sha256'] for p in P if p['proposal_id'] in oldBy),'changed_original_proposal_metadata':sum(p!=newBy[p['proposal_id']] for p in oldP),'unchanged_original_proposal_objects':sum(p==newBy[p['proposal_id']] for p in oldP),'changed_case_objects':sum(a!=b for a,b in zip(oldD,D)),'unchanged_case_objects':sum(a==b for a,b in zip(oldD,D)),'retained_original_evidence_objects':len(oldE),'foreign_read_only_origins':1,'additional_context_rows_not_assigned_occurrences':7,'supported_Difco_context_routes':3,'held_prepared_Oxoid_context_routes':4}
assert (counts['cases'],counts['occurrences'],counts['proposals'],counts['unchanged_original_payloads'])==(188,304,128,124)
save(S/'accounting.json',counts)
bridge={'at':now(),'predecessor_head':load(S/'preflight.json')['predecessor_head'],'predecessor_selector':cap(A/'successor-v6/selection.json'),'prior_complete_bridge':cap(A/'successor-v6/complete-bridge.json'),'prior_c9_bridge':cap(A/'successor-v6/combined-c9-bridge.json'),'counts':counts,'case_rows':[{'index':i,'case_id':b['case_id'],'source':b['source'],'case_input_sha256':b['case_input_sha256'],'occurrence_ids':b['occurrence_ids'],'owner_records':b['owner_records'],'before_object_sha256':oh(a),'after_object_sha256':oh(b),'whole_object_unchanged':a==b,'previous_proposal_ids':a['proposal_ids'],'selected_proposal_ids':b['proposal_ids'],'fresh_scope':'bounded dependency/current review metadata only' if i in indices else 'exact original retained decision; no blanket fresh approval'} for i,(a,b) in enumerate(zip(oldD,D))],'proposal_rows':[{'proposal_id':p['proposal_id'],'origin':'genuine new existing-owner dependent correction' if p['proposal_id'] not in oldBy else 'original W10 proposal retained','before_object_sha256':oh(oldBy[p['proposal_id']]) if p['proposal_id'] in oldBy else None,'after_object_sha256':oh(p),'previous_capture':oldBy[p['proposal_id']]['after_capture'] if p['proposal_id'] in oldBy else None,'selected_capture':p['after_capture'],'owner_path':p['owner_path'],'maintained_before_sha256':p['before_sha256'],'case_ids':p['case_ids'],'payload_unchanged':oldBy[p['proposal_id']]['after_capture']['sha256']==p['after_capture']['sha256'] if p['proposal_id'] in oldBy else False} for p in P],'all_old_evidence_prefix_exact':True,'retired_original_proposals':[],'all_prior_history_and_seals_preserved':True,'whole_owner_role_export_approval':False}
save(S/'complete-bridge.json',bridge)
selection={'at':now(),'predecessor_head':bridge['predecessor_head'],'predecessor_selector':bridge['predecessor_selector'],'authoritative_core':{name:cap(F/name) for name in ['decisions.json','proposals.json','evidence.json']},'artifact_root':str(A.relative_to(R)),'source_root':'campaign queue/preliminary-v5','selected_payloads':[{k:p[k] for k in ['proposal_id','owner_path','before_sha256','after_capture','case_ids']}|{'destination_path':p.get('destination_path',p['owner_path'])} for p in P],'counts':counts,'complete_bridge':cap(S/'complete-bridge.json'),'source_routing':cap(S/'source-routing-final.json'),'foreign_read_only_origins':cap(S/'cross-worker-dependencies-final.json'),'genuine_new_dependent_origin':newBy[proof['new_dependent_proposal_id']]['genuine_dependent_origin'],'retired_original_proposal_ids':[],'external_Oxoid_combination_installable_here':False,'application_or_release_approval':False,'holds':['Coordinator must compose/review one Oxoid nominal family candidate with both authentic source origins; unchanged W04/W10 proposals are not dual installation instructions.','Four prepared1L CM331 context rows remain held; no global raw generic/provider identity.','All source, quantity, species/processing, chemistry, owner, role and export holds inherited.']}
save(S/'selection.json',selection)
save(S/'finalization-binding.json',{'at':now(),'reviewed_author_freeze':cap(S/'author-freeze-v3.json'),'final_core':selection['authoritative_core'],'four_payloads_unchanged_from_review':proof['changed_payloads'],'only_final_changes':'Actual independent review metadata/evidence refs and corresponding active reviewed-dependency ledgers; no changed scientific claim, original history, source membership or payload bytes.','review_receipts':[SCI,LIN,TECH],'new_evidence_ids':[e['evidence_id'] for e in new_ev]})
save(S/'issue-linked-correction.json',{'at':now(),'filed_before_correction':[cap(S/'inputs/issue1237-comment6720201281.json'),cap(S/'inputs/issue1237-comment6720201502.json')],'before_fix_triage':[cap(S/'inputs/columbia-decision-v3.json')],'draft_root_finding':cap(S/'author-draft-binding-finding.json'),'draft_skeptical_finding':cap(S/'inputs/historical-completeness-finding-v1.json'),'historical_enum_correction':cap(S/'historical-enum-correction.json'),'independent_rechecks':[SCI,LIN,TECH],'no_GitHub_mutation_or_issue_closure':True,'root_published_head_review_still_required':True})
shutil.copy2(Path(__file__),S/'scripts'/Path(__file__).name)
print(json.dumps({'selection':cap(S/'selection.json'),'counts':counts},indent=2))
