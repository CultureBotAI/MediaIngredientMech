"""Build isolated immutable full Mc dependent selection from exact predecessor."""
import copy, hashlib, json, shutil
from pathlib import Path
R=Path.cwd(); P=R/'.temp/mc-dependent-successor-v1'; A=R/'reports/all_unmatched_20261107/worker-08'; O=A/'successors/issue-1237-mc-dependent-v1'; OLD=A/'successors/issue-1237-tenvit-v1'
CID='CM_NAME:d57e91ffaea6f0ab6ff0f3d6f0b04c26356c832e85dd83e9e2319874fda43506'; PID='mc1237-prop-mc-vitamins-dependent'; HEAD='a0190fed72b8f5119432003d1f9c84b8c1de7a48'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def canon(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def save(p,x):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x') as f:json.dump(x,f,ensure_ascii=False,indent=2);f.write('\n')
def ref(p):return {'root':'artifact','path':str(p.relative_to(A)),'sha256':sha(p)}
# Exact full thesis captures stay durable/private; bounded published facts suffice.
idx=read(O/'inputs/source-ref-index.json'); reloc=[]
for row in idx['selected_captures']:
 src=R/row['published_path']
 if src.name not in ('mc-thesis2014.pdf','mc-thesis2014.txt'):continue
 dst=P/'primary'/src.name;dst.parent.mkdir(parents=True,exist_ok=True)
 assert sha(src)==row['sha256'];assert not dst.exists();shutil.move(src,dst);assert sha(dst)==row['sha256']
 reloc.append({'previous_unpublished_copy_path':row['published_path'],'private_exact_capture':str(dst),'sha256':sha(dst),'original_path':row['original_path'],'published_full_text':False})
 row['private_capture_path']=str(dst);row['unpublished_prior_copy_path']=row.pop('published_path');row['publication_status']='Exact bytes preserved privately; public factual summary and URL/hash/time only.'
save(O/'inputs/source-ref-index-v2.json',idx)
save(O/'inputs/thesis-publication-scope.json',{'source_url':'https://etheses.whiterose.ac.uk/7951/1/JMBorgia%20-Thesis%202014.pdf','original_acquired_at':'2026-11-08T09:54:47.947617+00:00','read_scope':'Printed pages28–29 only, not whole-paper inspection.','scope':'Native Mc correction is based on literal Mc MixesDL and current D-specific ontology; thesis independently corroborates nominal protocol, not spreadsheet import genealogy or exclusive Mc/CB ownership.','facts':'Borgia2014 describes a McCas100X ten-vitamin stock with DL calcium pantothenate5mg and B12 0.1mg added to1L autoclaved distilledwater. Source-local anaerobic handling and receiving dose are not transferred into the Mc spreadsheet owner.','relocations':reloc,'historical_receipts':'Original author source-readback/index and peer assessments retain the earlier exact copy locations as observations. This addendum supplies their current private locations without rewriting those receipts or source bytes.'})
for role in ['science','lineage']:
 src=P/role;assert (src/'review.json').exists();shutil.copytree(src,O/'independent-review'/role)
for name in ['source_readback.py','assemble.py']:shutil.copy2(P/'provenance'/name,O/'provenance'/name)
d=read(OLD/'decisions.json');p=read(OLD/'proposals.json');e=read(OLD/'evidence.json');dp=copy.deepcopy(d);pp=copy.deepcopy(p);ep=copy.deepcopy(e)
ad=read(O/'author/decision.json');ap=read(O/'author/proposal.json')
rows=[('mc1237-author-assessment','author/assessment.json','local_validation','Exact whole-record delta and native helper/writer authorship; author is not independent scientific reviewer.'),('mc1237-source-readback','author/source-readback.json','local_validation','Actual bounded primary reads, literal Mc source block and conflicted CAS row; original acquisition times, no unread paper claim. Thesis relocation is supplied by mc1237-publication-scope.'),('mc1237-filed-003','inputs/issue1237-comment-6720042215-retry.json','local_validation','Exact issue-first SCI-TENVIT-003 comment read before author correction.'),('mc1237-filed-continuity','inputs/issue1237-comment-6720201812-retry.json','local_validation','Exact issue-first subsequent nominal continuity and bounded correction direction.'),('mc1237-original-route-envelope','inputs/w09-continuity/source-routing-and-origin-bindings.json','local_validation','Preserved eight-case71CM84separateKGsix-exclusion envelope; W04 cross-owner routing remains pending.'),('mc1237-dependency','author/dependency.json','local_validation','Genuine Mc existing-owner correction caused by existing NBRC903 comparator, zeroMc campaign occurrences; original CB and NBRC903 origins stay unchanged.'),('mc1237-source-index','inputs/source-ref-index-v2.json','local_validation','Exact primary/source/ref bindings;442 upstream manifest members verified; full thesis private-only.'),('mc1237-publication-scope','inputs/thesis-publication-scope.json','local_validation','Exact thesis bytes preserved privately, bounded factual support published with original source URL/hash/time.'),('mc1237-science','independent-review/science/review.json','independent_review','Actual author-independent whole final payload and six-occurrence source case assessment by worker08:/root/organics.'),('mc1237-lineage','independent-review/lineage/review.json','independent_review','Actual separate dependency/history/preservation review by worker08:/root/vitamins; prior CB authorship disclosed, no scientific approval.')]
for eid,path,kind,summary in rows:ep['evidence'].append({'evidence_id':eid,'capture':ref(O/path),'kind':kind,'url':None,'locator':'Complete exact artifact within declared assessment scope','supports_or_contradicts':summary,'case_ids':[CID]})
# First-hand reproducible source inputs; other source/occurrence captures remain in unchanged prior ledger.
for eid,path,kind,url,access,scope in [('mc1237-mixes','inputs/w09-continuity/mc-primary/captures/Mixes.csv','source_snapshot',None,None,'Complete Mc block, ten literal names/amounts/units andX100; source ledger observation time is not a new HTTP acquisition.'),('mc1237-cas-crosswalk','inputs/w09-continuity/mc-primary/captures/compounds_to_cas.csv','source_snapshot',None,None,'Complete crosswalk row92 is internally D/DL-conflicted, not same-form child proof.'),('mc1237-chebi31345','inputs/w09-continuity/primary/captures/ols31345-retry.capture','primary_source','https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345','2026-11-08T09:54:28.169665+00:00','Full term D-specific names/structure/CAS; supports withdrawal of DL-to-D resolving reference, not whole-child approval.')]:
 row={'evidence_id':eid,'capture':ref(O/path),'kind':kind,'url':url,'locator':scope,'supports_or_contradicts':scope,'case_ids':[CID]}
 if access:row['accessed_at']=access
 ep['evidence'].append(row)
newids=[x['evidence_id'] for x in ep['evidence'][len(e['evidence']):]]
for x in [ad,ap]:x['evidence_ids'] += [eid for eid in newids if eid not in x['evidence_ids']]
ad['independent_review']={'status':'complete','evidence_ids':['mc1237-science','mc1237-lineage']}
dp['decisions']=[ad if x['case_id']==CID else x for x in d['decisions']];pp['proposals'].append(ap)
assert len(dp['decisions'])==188 and len(pp['proposals'])==115
assert pp['proposals'][:114]==p['proposals'] and ep['evidence'][:1101]==e['evidence']
caserows=[]
for old,new in zip(d['decisions'],dp['decisions']):
 assert old['case_id']==new['case_id'] and ((old==new)==(old['case_id']!=CID))
 for k in ['case_input_sha256','source','occurrence_ids','disposition','missing_requirement','no_change_reason']:assert old[k]==new[k]
 caserows.append({'case_id':new['case_id'],'before_sha256':canon(old),'after_sha256':canon(new),'unchanged':old==new,'case_input_sha256':new['case_input_sha256'],'occurrence_ids':new['occurrence_ids']})
payloadrows=[]
for old in p['proposals']:
 assert sha(A/old['after_capture']['path'])==old['after_capture']['sha256']
 payloadrows.append({'proposal_id':old['proposal_id'],'owner_path':old['owner_path'],'original_before_sha256':old['before_sha256'],'selected_capture':old['after_capture'],'original_proposal_object_sha256':canon(old),'unchanged_proposal_object':True,'unchanged_payload':True})
payloadrows.append({'proposal_id':PID,'owner_path':ap['owner_path'],'original_before_sha256':ap['before_sha256'],'selected_capture':ap['after_capture'],'new_authentic_dependent_origin':True,'kind':'edit_existing_owner','unchanged_payload':False})
occ=[oid for c in dp['decisions'] for oid in c['occurrence_ids']];assert len(occ)==len(set(occ))==320
save(O/'decisions.json',dp);save(O/'proposals.json',pp);save(O/'evidence.json',ep)
counts={'cases':188,'proposals':115,'occurrence_ids':320,'evidence':len(ep['evidence']),'unchanged_original_payloads':114,'changed_original_payloads':0,'new_dependent_payloads':1,'new_owner_proposals':0,'changed_cases':1,'unchanged_cases':187,'new_cases':0,'mc_campaign_occurrences':0}
save(O/'lineage.json',{'predecessor_head':HEAD,'original_selection':ref(OLD/'selection.json'),'counts':counts,'original_evidence_prefix_preserved':1101,'cases':caserows,'payloads':payloadrows,'external_source_envelope_counts':read(O/'author/dependency.json')['source_envelope_counts'],'existing_CB_payload_unchanged':True,'original_NBRC903_new_owner_unchanged':True,'release_approval':False})
save(O/'selection.json',{'selection_id':'worker08-mc-dependent-successor-v1','predecessor_head':HEAD,'predecessor_selection':ref(OLD/'selection.json'),'authoritative_inputs':{n:ref(O/n) for n in ['decisions.json','proposals.json','evidence.json','lineage.json']},'frozen_shard_sha256':dp['shard_sha256'],'counts':counts,'new_dependent_proposal':PID,'changed_case_id':CID,'payload':ap['after_capture'],'dependency':ref(O/'author/dependency.json'),'effective_source_ref_index':ref(O/'inputs/source-ref-index-v2.json'),'thesis_publication_scope':ref(O/'inputs/thesis-publication-scope.json'),'cross_owner_routing':'PENDING_W04_CROSS_OWNER_DECISION','external_source_envelope_counts':read(O/'author/dependency.json')['source_envelope_counts'],'original_nbrc903_origin_unchanged':True,'CB_payload_unchanged':True,'independent_reviews':{role:ref(O/'independent-review'/role/'review.json') for role in ['science','lineage']},'coordinator_final_head_acceptance':'pending','maintained_application':False,'whole_owner_role_export_approval':False,'prior_TSB_Bacto_admission':'FAILED/HELD unchanged','scope':'Only isolated Mc DL-to-D component-reference correction plus honest source-scope notes/history. One authentic new dependent edit;114oldpayloads remain exact. Positive nominal commonrecipe does not select exclusive Mc/CB owner or install source-number duplicates. All prior source/form/role/export and18planningholds remain.'})
print(json.dumps({'selection':ref(O/'selection.json'),'counts':counts},indent=2))
