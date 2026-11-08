from pathlib import Path
import json, hashlib, subprocess, datetime, copy
import yaml
R=Path.cwd();C=R.parents[2];A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v7'
P=R/'.temp/columbia-controls-successor-v1/lineage';HEAD='c66d6d3665368fe1ae8986fb7c16340a103582c1'
start=datetime.datetime.now(datetime.timezone.utc).isoformat();reads={}
def sha(b):return hashlib.sha256(b).hexdigest()
def canon(x):return sha(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
def read(p):
 b=p.read_bytes();reads[str(p)]={'sha256':sha(b),'bytes':len(b)};return b
def js(p):return json.loads(read(p))
def git(path):return subprocess.check_output(['git','show',f'{HEAD}:{path}'])
def save(n,x):
 p=P/n;assert not p.exists();p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def diff(a,b,path=''):
 if a==b:return []
 if isinstance(a,dict) and isinstance(b,dict):
  return sum([diff(a[k],b[k],path+'/'+k) if k in a and k in b else [{'path':path+'/'+k,'before':a.get(k),'after':b.get(k)}] for k in sorted(set(a)|set(b))],[])
 return [{'path':path,'before':a,'after':b}]
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==HEAD
freeze=js(S/'author-freeze-v3.json');baseline=js(P/'baseline-fullcore.json');lineage=js(P/'selected-source-lineage.json')
old={k:json.loads(git(f'reports/all_unmatched_20261107/worker-10/successor-v6/final-core/{k}.json')) for k in ['decisions','proposals','evidence']}
new={}
for k in old:
 b=read(S/f'author-core-v3/{k}.json');assert sha(b)==freeze['core'][k+'.json']['sha256'];new[k]=json.loads(b)
od={x['case_id']:x for x in old['decisions']['decisions']};nd={x['case_id']:x for x in new['decisions']['decisions']}
op={x['proposal_id']:x for x in old['proposals']['proposals']};np={x['proposal_id']:x for x in new['proposals']['proposals']}
oe={x['evidence_id']:x for x in old['evidence']['evidence']};ne={x['evidence_id']:x for x in new['evidence']['evidence']}
expectedcases={x['case_id'] for x in od.values() if x['source_index'] in [80,118,135,178]}
newid='sv7-dependent-columbia-unmapped0118-partition'
oxoid='sv1-bio-columbia_blood_agar_oxoid_m2224';difco='sv3-hm-difco-columbia1270'
controls=['sv1-buffers-tris_hcl_0_2m_ph7_5_dsmz273','sv1-buffers-hepes_2m_ph7_jcm556_1200']
changedps={oxoid,difco,*controls}
assert nd.keys()==od.keys() and len(nd)==188
assert set(np)-set(op)=={newid} and set(op)<=set(np) and len(np)==128
assert set(oe)<=set(ne) and len(ne)==1224 and all(ne[e]==x for e,x in oe.items())
assert {c for c in od if od[c]!=nd[c]}==expectedcases
assert {p for p in op if op[p]!=np[p]}==changedps
caseledger=[]
for cid,o in od.items():
 n=nd[cid];d=diff(o,n)
 assert all(n[f]==o[f] for f in ['case_id','case_input_sha256','source','occurrence_ids','source_index'])
 assert set(o['evidence_ids'])<=set(n['evidence_ids']) and set(o['proposal_ids'])<=set(n['proposal_ids'])
 if cid in expectedcases:
  marker=n['source_successor_v7'];assert marker['prior_independent_review']==o['independent_review']
  assert n['independent_review']=={'status':'pending','evidence_ids':[]}
  assert marker['whole_owner_role_export_approval'] is False
  assert set(z['path'].split('/')[1] for z in d)<=set(['evidence_ids','issue_refs','independent_review','source_successor_v7','proposal_ids','reasoning','missing_requirement'])
  if 'reasoning' in {z['path'][1:] for z in d}:assert n['reasoning'].startswith(o['reasoning'])
 caseledger.append({'case_id':cid,'source_index':o['source_index'],'before_sha256':canon(o),'after_sha256':canon(n),'unchanged':o==n,'occurrence_ids':n['occurrence_ids'],'differences':d})
assert sum(len(x['occurrence_ids']) for x in nd.values())==304
for pid,n in np.items():
 assert all(cid in nd and pid in nd[cid]['proposal_ids'] for cid in n['case_ids'])
for cid,n in nd.items():assert all(pid in np and cid in np[pid]['case_ids'] for pid in n['proposal_ids'])
payloadledger=[]
for pid,n in np.items():
 cap=n['after_capture'];b=read(A/cap['path']);assert sha(b)==cap['sha256'];after=yaml.safe_load(b)
 if pid in op:
  o=op[pid];oc=o['after_capture'];ob=read(A/oc['path']);assert sha(ob)==oc['sha256'];assert git(str((A/oc['path']).relative_to(R)))==ob
  before=yaml.safe_load(ob)
  assert n['case_ids']==o['case_ids'] and n.get('before_sha256')==o.get('before_sha256') and n['owner_path']==o['owner_path'] and n['kind']==o['kind']
  if pid not in {difco,*controls}:assert b==ob
  if pid in changedps:
   assert n['source_successor_v7']['prior_independent_review']==o['independent_review']
   assert set(o['evidence_ids'])<=set(n['evidence_ids'])
  if pid in [difco,oxoid]:assert n['source_successor_v7']['previous_proposal']==o
  if pid in controls:
   assert before['component_assertion']['completeness']=='PARTIAL' and after['component_assertion']['completeness']=='UNKNOWN'
   t=copy.deepcopy(after);t['component_assertion']['completeness']='PARTIAL';t['curation_history']=t['curation_history'][:-1];assert t==before
  if pid==difco:
   t=copy.deepcopy(after)
   for k in ['synonyms','notes','curation_history']:
    if k in before:t[k]=before[k]
    else:t.pop(k,None)
   assert t==before
   assert len(after.get('synonyms',[]))==len(before.get('synonyms',[]))+1
   assert after['synonyms'][:-1]==before.get('synonyms',[])
   assert after['synonyms'][-1]=={'synonym_text':'Columbia blood agar base (BD-Difco)','synonym_type':'CATALOG_VARIANT','source':'culturemech:output/ingredient_occurrences.tsv'}
   assert after['notes'].startswith(before['notes'])
 else:
  assert pid==newid and n['kind']=='edit_existing_owner'
  assert n['owner_path']=='data/ingredients/unmapped/Columbia_Blood_Agar_Base.yaml'
  ob=read(R/n['owner_path']);assert ob==git(n['owner_path']) and sha(ob)==n['before_sha256']==lineage['authentic_owner']['sha256'];before=yaml.safe_load(ob)
  t=copy.deepcopy(after)
  for k in ['synonyms','notes','curation_history']:t[k]=before[k]
  assert t==before and after['notes'].startswith(before['notes'])
  assert after['synonyms'][0]==before['synonyms'][0]
  for i in [1,2]:
   q=copy.deepcopy(after['synonyms'][i]);assert q.pop('synonym_type')=='REJECTED_LABEL';v=copy.deepcopy(before['synonyms'][i]);v.pop('synonym_type');assert q==v
  assert len(after['synonyms'])==3
  g=n['genuine_dependent_origin'];assert g['trigger_case_indices']==[118,178] and g['new_source_case'] is False and g['foreign_source_case_claimed'] is False
  for x in g['trigger_proposals']:assert x['proposal_object_sha256']==canon(op[x['proposal_id']]) and x['after_capture']==op[x['proposal_id']]['after_capture']
 if pid in [newid,difco,*controls]:
  assert after['curation_history'][:-1]==before['curation_history'] and len(after['curation_history'])==len(before['curation_history'])+1
  event=after['curation_history'][-1];assert event['llm_assisted'] is True and event['curator']=='Codex worker10 /root'
 payloadledger.append({'proposal_id':pid,'proposal_differences':diff(op[pid],n) if pid in op else [{'new_dependent_proposal':n}],'before_payload_sha256':sha(ob),'after_payload_sha256':sha(b),'payload_unchanged':pid in op and b==ob,'payload_differences':diff(before,after)})
routing=js(S/'source-routing.json');cross=js(S/'cross-worker-dependencies.json')
dependency=routing['same_owner_dependency']
for k in ['proposal_id','kind','owner_path','before_sha256','after_capture','case_ids']:assert dependency[k]==np[newid][k]
assert dependency['review_state']=='pending_exact_full_payload_independent_review' and dependency['application_state']=='not_applied'
assert cross['owner_dependency']==dependency
for cid in np[newid]['case_ids']:assert nd[cid]['source_successor_v7']['same_owner_dependency']==dependency
for pid in [oxoid,difco]:assert np[pid]['source_successor_v7']['same_owner_dependency']==dependency
assert cross['W04_origin']['original_proposal']==lineage['external_W04_origin']['proposal']
assert cross['W04_origin']['original_current_decisions']==lineage['external_W04_origin']['decisions']
assert cross['W04_origin']['original_case']==lineage['external_W04_original_case']
assert cross['W10_origin']['original_case']==next(x for x in lineage['targets'] if x['proposal']['proposal_id']==oxoid)['case_bindings'][0]['complete_original_case']
assert cross['W10_origin']['proposal_object_sha256']==canon(op[oxoid])
assert cross['combined_payload_authored_here'] is False and cross['W04_payload_changed'] is False and cross['W10_payload_changed'] is False
for cap in [cross['W04_origin']['payload_capture'],cross['existing_coordinator_prototype']]:assert sha(read(A/cap['path']))==cap['sha256']
assert cross['W04_origin']['payload_capture']['sha256']==lineage['external_W04_origin']['payload']['sha256']
assert cross['source_routes'][0]['raw_quantity']=={'unit':'VARIABLE','value':'variable'} and cross['source_routes'][1]['raw_quantity']=={'unit':'G_PER_L','value':'39'}
oldrows={x['reviewed_row']['recipe_id']:x for x in lineage['seven_current_source_rows']}
assert len(routing['seven_context_rows'])==7
for row in routing['seven_context_rows']:
 original=oldrows[row['original_occurrence_row']['recipe_id']]['reviewed_row']
 assert row['original_occurrence_row']==original['occurrence']
 assert row['original_recipe_capture_metadata']==original['recipe_capture']
 cap=row['source_recipe_capture'];assert sha(read(A/cap['path']))==cap['sha256']==original['recipe_capture']['sha256']
 assert row['exact_source_quantity']==original['source_quantity_preserved']
 assert row['assigned_W10_case_added'] is False and row['assigned_W10_occurrence_added'] is False
 assert row['route_supported']==('DIFCO_DRY' in original['disposition'])
 assert row['same_owner_dependency']==dependency
 assert row['target_proposal_id']==(difco if row['route_supported'] else None)
evidenceledger=[]
for eid,e in ne.items():
 cap=e['capture'];root={'artifact':A,'source':C/'queue/preliminary-v5'}[cap['root']];assert sha(read(root/cap['path']))==cap['sha256']
 if eid not in oe:
  expected=set(np[newid]['case_ids']) if eid not in ['sv7-filed-stock-completeness','sv7-input-byteproof'] else (expectedcases if eid=='sv7-input-byteproof' else {cid for p in controls for cid in np[p]['case_ids']})
  assert set(e['case_ids'])==expected
  assert all(eid in nd[cid]['evidence_ids'] for cid in expected)
 evidenceledger.append({'evidence_id':eid,'unchanged':eid in oe and e==oe[eid],'object_sha256':canon(e),'capture':cap,'case_ids':e.get('case_ids',[])})
assert subprocess.check_output(['git','diff','--name-only',HEAD],text=True).strip()==''
assert subprocess.check_output(['git','diff','--cached','--name-only',HEAD],text=True).strip()==''
for k,cap in freeze['core'].items():assert sha(read(A/cap['path']))==cap['sha256']
correction=js(S/'historical-enum-correction.json')
v2=json.loads(read(S/'author-core-v2/decisions.json'))
v2d={x['case_id']:x for x in v2['decisions']}
for k in ['proposals','evidence']:assert read(S/f'author-core-v2/{k}.json')==read(S/f'author-core-v3/{k}.json')
assert {cid for cid in nd if nd[cid]!=v2d[cid]}=={cid for cid in expectedcases if nd[cid]['source_index'] in [80,135]}
for row in correction['rows']:
 cid=row['case_id'];assert canon(v2d[cid])==row['before_case_sha256'] and canon(nd[cid])==row['after_case_sha256']
 assert nd[cid]['completion_reassessment']==od[cid]['completion_reassessment']==v2d[cid]['completion_reassessment']
 assert canon(nd[cid]['completion_reassessment'])==row['preserved_completion_reassessment_sha256']
 marker=nd[cid]['source_successor_v7'];assert marker['old_completion_reassessment_is_historical'] is True and marker['active_component_assertion']['completeness']=='UNKNOWN'
 assert marker['active_component_assertion']['selected_capture']==row['selected_payload']==np[nd[cid]['proposal_ids'][0]]['after_capture']
 for k,v in v2d[cid]['source_successor_v7'].items():assert marker[k]==v
 cap=marker['historical_enum_finding']['captured_finding'];assert sha(read(A/cap['path']))==cap['sha256']

snapshot=P/'author-v3-inputs';snapshot.mkdir(exist_ok=False)
for k in new:(snapshot/(k+'.json')).write_bytes((S/f'author-core-v3/{k}.json').read_bytes())
save('author-v3-full-case-bridge.json',caseledger)
save('author-v3-full-proposal-payload-bridge.json',payloadledger)
save('author-v3-full-evidence-bridge.json',evidenceledger)
save('author-v3-read-bindings.json',{'files':reads})
result={'review_id':'worker10-columbia-controls-author-v3-lineage','reviewer':'worker10:/root/bio_research','scientific_review':False,'status':'PASS_WITH_EXPLICIT_COORDINATOR_COMPOSITION_AND_APPLICATION_HOLDS','predecessor_head':HEAD,'author_freeze':{'path':str(S/'author-freeze-v3.json'),'sha256':sha((S/'author-freeze-v3.json').read_bytes())},'core_hashes':{k:freeze['core'][k+'.json']['sha256'] for k in new},'counts':{'cases':188,'unchanged_full_decisions':184,'allowed_changed_decisions':4,'original_occurrences_retained':304,'proposals':128,'old_proposal_ids_retained':127,'new_dependent_proposals':1,'unchanged_full_old_proposal_objects':123,'unchanged_old_payloads':124,'changed_old_payloads':3,'new_existing_owner_payload':1,'evidence':1224,'old_evidence_objects_exact':1218,'new_evidence_objects':6,'context_rows_outside_campaign_membership':7},'timing':{'exact_first_read_utc':None,'qualification':'Author-v2 reading preceded this audit; audit execution is not the full review interval.','audit_execution_started_at':start,'completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat()},'authorship':js(P/'preflight-review-v1.json')['authorship'],'assessments':['All188 complete case and raw source identities/304occurrence lists retained. All184 unaffected decisions exact; only four originally assigned cases change allowed dependency/review/evidence metadata and appended Columbia explanation.','All127 old proposal IDs/case bindings/maintained before hashes retained. 123 full proposal objects and124 payloads unchanged. The three changed payloads retain exact old history and one honest new event.','New0118 uses actual same-path29ed before; generic identity/status/type/stats/RAW_TEXT preserved, two vendor texts/sources retained as rejected resolving labels. No vendor maintained beforeimage is fabricated.','Difco adds exactly one existing vendor synonym and notes/history; seven components and all source-evidence assertions retained. Buffers differ only in PARTIAL->UNKNOWN plus history.','Oxoid37e8 remains byte-exact origin, actualW04 current4a3d/fullproposal/decision/case retained externally. This packet does not author or approve final combinedOxoid candidate. Source300variable and source92139g preserved; coordinator single-family composition condition explicit.','All1218 original evidence objects and case memberships exact; six new evidence objects are scoped to actual Columbia or buffer cases. Earlier overbroad author-v1 metadata and its before-fix finding remain preserved.','Seven complete current-context rows retain exact source objects/recipe captures/times and3supportedDifco/4preparedOxoidheld split without adding a campaigncase or occurrence.','No tracked working/index changes againstc66 observed; own reviewer wrote only permitted private lineage outputs.'],'reviewer_method_diagnostics':[{'prior_attempt':'review_author_v2.py / author-v2-audit.stderr','result':'Own verifier assumed original_occurrence instead of actual original_occurrence_row key; no target defect. Original script/log retained; corrected v3 verifier completes all checks.'}],'inherited_finding_disposition':{'finding_id':'W10-SV7-SKEPTIC-HISTORICAL-COMPLETENESS-001','status':'metadata_correction_verified','scope':'Both80/135 preserve original completion_reassessment and explicitly mark formerPARTIAL historical; activeUNKNOWN points to exact unchanged payload. No new science/issueclosure.'},'findings':[],'limits':['Provenance/implementation/retention scope only; fresh source science belongs to separate reviewer. Prior own source authorship disclosed; no whole-owner or original-science independence overclaim.','Author-stage review markers intentionally pending; finalcore review bindings require separate narrow recheck.','Coordinator must compose/review one existingOxoidfamilycandidate with both authenticorigins and reviewed0118dependency before any installation; no arbitrarywinner or two-owner installation.','Fourpreparedbaseholds, historical-lot/form/quantity uncertainties, genericprovider2046 boundary, source discrepancies and all role/export/application holds remain.','No future published-head approval or Git/GitHub mutation.']}
save('author-v3-lineage-review.json',result)
print(json.dumps({'status':result['status'],'counts':result['counts'],'report_sha256':sha((P/'author-v3-lineage-review.json').read_bytes())},indent=2))
