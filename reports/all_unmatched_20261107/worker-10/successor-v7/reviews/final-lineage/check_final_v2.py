from pathlib import Path
import json,hashlib,datetime,copy,subprocess
R=Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v7'
O=R/'.temp/columbia-controls-successor-v1';P=O/'final-lineage';L=O/'lineage'
start=datetime.datetime.now(datetime.timezone.utc).isoformat();reads={}
def sha(b):return hashlib.sha256(b).hexdigest()
def canon(x):return sha(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
def read(p):
 b=p.read_bytes();reads[str(p)]={'sha256':sha(b),'bytes':len(b)};return b
def js(p):return json.loads(read(p))
def cap(c):
 root=A if c['root']=='artifact' else R.parents[2]/'queue/preliminary-v5';b=read(root/c['path']);assert sha(b)==c['sha256'];return b
def save(n,x):
 p=P/n;assert not p.exists();p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def changedkeys(a,b):return {k for k in set(a)|set(b) if a.get(k)!=b.get(k)}
selector=js(S/'selection.json');assert reads[str(S/'selection.json')]['sha256']=='cb5c0eef5787728757aa0d7e2d2e56adc3a634af95d83b7ff23b81bacf11b38e'
finalizer=js(S/'finalization-binding.json');bridge=js(S/'complete-bridge.json');accounting=js(S/'accounting.json')
author_report=js(L/'author-v3-lineage-review.json');assert sha((L/'author-v3-lineage-review.json').read_bytes())=='f23a8f9ec284124108932287118e66fe95b7e4632c83a5cc1a01351e9f07d7e0'
af=json.loads(cap(finalizer['reviewed_author_freeze']));assert finalizer['reviewed_author_freeze']['sha256']==author_report['author_freeze']['sha256']
author={};final={};keys={'decisions':'case_id','proposals':'proposal_id','evidence':'evidence_id'}
for k in keys:
 b=read(L/f'author-v3-inputs/{k}.json');assert sha(b)==af['core'][k+'.json']['sha256'];assert cap(af['core'][k+'.json'])==b
 author[k]={x[keys[k]]:x for x in json.loads(b)[k]}
 assert selector['authoritative_core'][k+'.json']==finalizer['final_core'][k+'.json']
 final[k]={x[keys[k]]:x for x in json.loads(cap(selector['authoritative_core'][k+'.json']))[k]}
assert len(final['decisions'])==188 and len(final['proposals'])==128 and len(final['evidence'])==1229
assert final['decisions'].keys()==author['decisions'].keys() and final['proposals'].keys()==author['proposals'].keys()
assert set(author['evidence'])<=set(final['evidence']) and all(final['evidence'][k]==v for k,v in author['evidence'].items())
new_eids=set(final['evidence'])-set(author['evidence']);assert new_eids==set(finalizer['new_evidence_ids']) and len(new_eids)==5
receipts=finalizer['review_receipts'];reports=[json.loads(cap(c)) for c in receipts]
assert reports[0]['reviewer']=='worker10:/root/preparation_skeptic (AI)' and reports[0]['status']=='PASS_BOUNDED_CORRECTION'
assert reports[1]['scientific_review'] is False and reports[1]['reviewer']=='worker10:/root/bio_research'
assert reports[2]['scientific_review'] is False and reports[2]['reviewer']=='worker10:/root/buffers_research'
assert reports[1]==author_report
changes=[];active=[]
for kind in ['decisions','proposals']:
 for ident,b in author[kind].items():
  f=final[kind][ident];delta=changedkeys(b,f)
  if delta:
   assert delta<=set(['evidence_ids','independent_review','source_successor_v7','review_status_explanation'])
   assert set(f['evidence_ids'])-set(b['evidence_ids'])<=new_eids and set(b['evidence_ids'])<=set(f['evidence_ids'])
   assert f['independent_review']=={'status':'complete','evidence_ids':['sv7-independent-science','sv7-independent-lineage','sv7-independent-technical']}
   m=f['source_successor_v7'];before=b['source_successor_v7']
   assert changedkeys(before,m)<=set(['scope','review_state','same_owner_dependency','routing','actual_review_receipts','historical_enum_finding'])
   assert m['review_state']=='complete_bounded_exact_payload_and_metadata_review' and m['actual_review_receipts']==receipts
   assert m['prior_independent_review']==before['prior_independent_review']
   assert m['whole_owner_role_export_approval'] is False
   if 'historical_enum_finding' in m:
    t=copy.deepcopy(m['historical_enum_finding']);t.pop('recheck_receipts');t['correction_state']=before['historical_enum_finding']['correction_state'];assert t==before['historical_enum_finding']
    assert m['historical_enum_finding']['recheck_receipts']==receipts
   active.append({'kind':kind,'id':ident,'review_state':m['review_state'],'review_evidence_ids':f['independent_review']['evidence_ids']})
  changes.append({'kind':kind,'id':ident,'author_sha256':canon(b),'final_sha256':canon(f),'changed_fields':sorted(delta)})
assert sum(x['kind']=='decisions' for x in active)==4 and sum(x['kind']=='proposals' for x in active)==5
routing=js(S/'source-routing-final.json');cross=js(S/'cross-worker-dependencies-final.json')
arouting=js(S/'source-routing.json');across=js(S/'cross-worker-dependencies.json')
dep=routing['same_owner_dependency'];adep=arouting['same_owner_dependency'];t=copy.deepcopy(dep);t.pop('exact_review_receipts');t['review_state']=adep['review_state'];assert t==adep
assert dep['review_state']=='complete_bounded_full_payload_review_application_not_approved' and dep['application_state']=='not_applied' and dep['exact_review_receipts']==receipts
assert cross['owner_dependency']==dep
for name,old,new,dkey in [('routing',arouting,routing,'same_owner_dependency'),('cross',across,cross,'owner_dependency')]:
 t=copy.deepcopy(new);t.pop('finalization');t[dkey]=old[dkey]
 if name=='routing':
  assert t['Oxoid_origin_routes']['owner_dependency']==dep
  t['Oxoid_origin_routes']['owner_dependency']=old['Oxoid_origin_routes']['owner_dependency']
  assert len(t['seven_context_rows'])==7
  for row,prev in zip(t['seven_context_rows'],old['seven_context_rows']):
   assert row['same_owner_dependency']==dep;row['same_owner_dependency']=prev['same_owner_dependency']
 assert t==old
 assert new['finalization']['review_receipts']==receipts;cap(new['finalization']['author_ledger'])
assert sum(x['route_supported'] for x in routing['seven_context_rows'])==3
assert sum(not x['route_supported'] for x in routing['seven_context_rows'])==4
for kind in ['decisions','proposals']:
 for x in final[kind].values():
  m=x.get('source_successor_v7',{})
  if 'same_owner_dependency' in m:assert m['same_owner_dependency']==dep and m['routing']==selector['source_routing']
for c in [selector['complete_bridge'],selector['source_routing'],selector['foreign_read_only_origins'],selector['predecessor_selector'],bridge['prior_complete_bridge'],bridge['prior_c9_bridge']]:cap(c)
assert selector['genuine_new_dependent_origin']==final['proposals'][dep['proposal_id']]['genuine_dependent_origin']
assert selector['retired_original_proposal_ids']==[] and selector['application_or_release_approval'] is False and selector['external_Oxoid_combination_installable_here'] is False
assert cross['combined_payload_authored_here'] is False and cross['role_export_approval'] is False
assert all(x['assigned_W10_case_added'] is False and x['assigned_W10_occurrence_added'] is False for x in routing['seven_context_rows'])
payloads=[]
selected={x['proposal_id']:x for x in selector['selected_payloads']}
assert selected.keys()==final['proposals'].keys()
for pid,p in final['proposals'].items():
 a=author['proposals'][pid];assert p['after_capture']==a['after_capture'];cap(p['after_capture'])
 assert all(selected[pid][k]==p[k] for k in ['owner_path','case_ids','before_sha256','after_capture'])
 assert all(c in final['decisions'] and pid in final['decisions'][c]['proposal_ids'] for c in p['case_ids'])
 payloads.append({'proposal_id':pid,'after_capture':p['after_capture'],'unchanged_from_author_v3':True})
for cid,d in final['decisions'].items():
 assert all(pid in final['proposals'] and cid in final['proposals'][pid]['case_ids'] for pid in d['proposal_ids'])
assert sum(len(d['occurrence_ids']) for d in final['decisions'].values())==304
baseline=js(L/'baseline-fullcore.json');bd={x['case_id']:x for x in baseline['decisions']};bp={x['proposal_id']:x for x in baseline['proposals']}
assert len(bridge['case_rows'])==188 and len(bridge['proposal_rows'])==128
for row in bridge['case_rows']:
 d=final['decisions'][row['case_id']];o=bd[row['case_id']]
 assert row['before_object_sha256']==o['sha256'] and row['after_object_sha256']==canon(d)
 assert row['whole_object_unchanged']==(o['sha256']==canon(d)) and row['occurrence_ids']==d['occurrence_ids']==o['occurrence_ids']
 assert row['case_input_sha256']==d['case_input_sha256']==o['case_input_sha256']
 assert row['selected_proposal_ids']==d['proposal_ids'] and row['owner_records']==d['owner_records']
for row in bridge['proposal_rows']:
 p=final['proposals'][row['proposal_id']];o=bp.get(row['proposal_id'])
 assert row['after_object_sha256']==canon(p) and row['selected_capture']==p['after_capture']
 assert row['maintained_before_sha256']==p.get('before_sha256') and row['case_ids']==p['case_ids']
 assert row['before_object_sha256']==(o['proposal_sha256'] if o else None)
 assert row['previous_capture']==(o['after_capture'] if o else None)
 assert row['payload_unchanged']==bool(o and o['after_capture']['sha256']==p['after_capture']['sha256'])
assert accounting==selector['counts']==bridge['counts']
assert accounting['unchanged_original_payloads']==sum(bp[pid]['after_capture']['sha256']==p['after_capture']['sha256'] for pid,p in final['proposals'].items() if pid in bp)==124
assert accounting['unchanged_case_objects']==sum(bd[cid]['sha256']==canon(d) for cid,d in final['decisions'].items())==184
assert accounting['unchanged_original_proposal_objects']==sum(bp[pid]['proposal_sha256']==canon(p) for pid,p in final['proposals'].items() if pid in bp)==123
for e in final['evidence'].values():cap(e['capture'])
assert all(final['evidence'][e['evidence_id']]['capture']==e['capture'] and canon(final['evidence'][e['evidence_id']])==e['sha256'] for e in baseline['evidence'])
for c in finalizer['four_payloads_unchanged_from_review']:cap(c['after_capture'])
for k in keys:cap(selector['authoritative_core'][k+'.json'])
save('final-core-diff-ledger.json',changes)
save('final-selected-payloads.json',payloads)
save('review-input-bindings.json',reads)
report={'review_id':'worker10-columbia-controls-final-core-lineage-v1','reviewer':'worker10:/root/bio_research','scientific_review':False,'status':'PASS_BOUNDED_FINAL_METADATA_AND_RETENTION','reviewed_selector':{'path':str(S/'selection.json'),'sha256':sha((S/'selection.json').read_bytes())},'final_core':selector['authoritative_core'],'timing':{'exact_first_read_utc':None,'qualification':'Final metadata reading preceded execution; exact first-reading start not recorded. The audit timestamps are not the full reading interval.','audit_execution_started_at':start,'completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat()},'authorship_disclosure':author_report['authorship'],'scope':'Exhaustive full-core byte/object retention and final review-binding metadata only. No fresh source-science judgment, native-suite rerun or published-head approval.','counts':accounting,'author_v3_review':{'path':str(L/'author-v3-lineage-review.json'),'sha256':sha((L/'author-v3-lineage-review.json').read_bytes())},'checks':['All188 final case identities/304occurrence lists and128proposalIDs/ownerbefore/casebindings match reviewedauthorv3.','All128selectedpayloads, including4reviewed candidates, are byte-exact to authorv3;124originalpayloads remain exactc66.','All1224author-v3evidence objects remain exact;5actualreview/final-routing entries bring1229. All1218originalc66evidence objects/captures remain exact.','Only4case and5proposal review/evidence/marker fields changed atfinalization. All184otherdecisions and123otheroriginalproposalobjects remain exactc66.','Everycomplete-bridge case/proposal hash,selectedcapture,beforehash,occurrence count and selector/accounting count verified independently.','Active0118dependency/routing now binds actual3review receipts. Authorpending values survive only in explicitlyhistorical predecessorobjects or authorartifacts; no activepending claim masquerades as completedscience.','Finalrouting differs onlyreviewbindings:7contextrows/3Difcodry/4preparedOxoidholds andsourcecapturemetadataexact. No foreigncase,prototypeowner or newsourceoccurrenceimport.','ActualW04 origin and externalprototype remain unchangedread-only dependencies; singleOxoidfamily composition and installation remain coordinatorconditions.','Ownpriorauthorship is disclosed; other reviewers science/technical scopes are distinct. HistoricalPARTIAL clarification and alloriginalsource/history/role/exportholds preserved.'],'active_review_bindings':active,'reviewer_method_diagnostics':[{'attempt':'check_final.py / check.stderr','cause':'Own checker normalized top-level and seven-row dependency markers but omitted the same expected marker in Oxoid_origin_routes. Exact diff verified only receipt/review-state changes; corrected checker explicitly checks that embedded marker too. No target finding.'}],'findings':[],'limitations':['No original-science independence claimed for my prior W10 biology/Oxoid/BD-manual source authorship. This is independent of rootfinal metadata assembly only.','Fresh science is attributed to preparation_skeptic; technical reviewer discloses originalbuffersauthorship.','No maintained/sourceapplication, role/exportapproval, finalcombinedOxoidinstallation or futureheadapproval.','Only O/final-lineage written; previous O/lineage remains unchanged.']}
save('final-core-lineage-review-v1.json',report)
print(json.dumps({'status':report['status'],'report_sha256':sha((P/'final-core-lineage-review-v1.json').read_bytes()),'counts':accounting},indent=2))
