"""Immutable successor core;113 exact original proposals plus authentic new dependency."""
import copy,datetime,hashlib,json,shutil
from pathlib import Path
R=Path.cwd();P=R/'.temp/all-unmatched-worker-08/tenvit-dependent-v1';A=R/'reports/all_unmatched_20261107/worker-08';OLD=A/'successors/issue-1227-plain-flour-v1';O=A/'successors/issue-1237-tenvit-v1'
CID='CM_NAME:d57e91ffaea6f0ab6ff0f3d6f0b04c26356c832e85dd83e9e2319874fda43506';PID='vm1237-prop-wolfe-cb-dependent'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def canon(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def save(p,x):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x') as f:json.dump(x,f,ensure_ascii=False,indent=2);f.write('\n')
def ref(p):return {'root':'artifact','path':str(p.relative_to(A)),'sha256':sha(p)}
for role,folder in [('science','independent-components'),('skeptical','independent-skeptical')]:
 src=P/folder;assert (src/'review.json').exists();shutil.copytree(src,O/'independent-review'/role)
d=read(OLD/'decisions.json');p=read(OLD/'proposals.json');e=read(OLD/'evidence.json');dp=copy.deepcopy(d);pp=copy.deepcopy(p);ep=copy.deepcopy(e)
ad=read(O/'author/decision.json');ap=read(O/'author/proposal.json')
rows=[('vm1237-author-assessment','author/assessment.json','local_validation','Exact complete before/W09/composed delta; author is not independent reviewer.'),('vm1237-nominal-source','research/nominal-recipe-evidence.json','local_validation','Structured positive JCM197/NBRC837/NBRC903 ten-vitamin masses and1L water-input recipe; explicit preparation partitions, generic B12 and unknown pantothenate retained. Separate positive NCMA11-solute/unquantified-water claim.'),('vm1237-child-bindings','author/child-bindings.json','local_validation','Current complete owner bytes and primary descriptor checked for nine named CB inputs; calcium pantothenate D/DL hold.'),('vm1237-filed-comment','inputs/issue1237-comment6719499726.json','local_validation','Exact issue-first coordinator source conclusion; read before authoring.'),('vm1237-dependency-dispositions','author/dependency-dispositions.json','local_validation','Authentic new existing-owner dependency; original NBRC903 null-before proposal preserved; no CB occurrences or W06 cases claimed; central nominal duplicate reconciliation remains.'),('vm1237-primary-readback','research/source-read-ledger.json','local_validation','Actual primary reads and original acquisition times, no new remote retrieval claim.'),('vm1237-source-partitions','research/occurrence-partitions.json','local_validation','All six original W08 source occurrences, only NBRC903 triggers comparator; five other branches unchanged.'),('vm1237-science','independent-review/science/review.json','independent_review','Author-independent entire composed payload and six-occurrence source-case review by worker08:/root/organics; no whole referenced child owner approval.'),('vm1237-skeptical','independent-review/skeptical/review.json','independent_review','Separate exact whole payload/case/dependency/lineage review by worker08:/root/inorganics.')]
for eid,path,kind,text in rows:ep['evidence'].append({'evidence_id':eid,'capture':ref(O/path),'kind':kind,'url':None,'locator':'Full immutable artifact; bounded claim and exact source contexts within','supports_or_contradicts':text,'case_ids':[CID]})
# Archive byte-identical inspected external primary captures as local publishable evidence.
(O/'primary').mkdir()
raws=[]
for i,row in enumerate(read(O/'research/source-read-ledger.json')['entries']):
 if row.get('kind') not in ['primary_source','source_snapshot','raw_source']:continue
 src=Path(row['path']);assert sha(src)==row['sha256'];dst=O/'primary'/f'capture-{i:02d}{src.suffix}';shutil.copy2(src,dst)
 eid=f'vm1237-primary-{i:02d}';url=row.get('url');entry={'evidence_id':eid,'capture':ref(dst),'kind':'primary_source' if url else 'source_snapshot','url':url,'locator':row['read_scope'],'supports_or_contradicts':'Actual inspected primary bytes; source-specific applicability and preparation partitions in vm1237-nominal-source/primary-readback. No molecular form or stock equality inferred.','case_ids':[CID]}
 entry['original_acquisition_at']=row.get('original_accessed_at')
 if url:entry['accessed_at']=row['original_accessed_at']
 ep['evidence'].append(entry);raws.append({'original_path':str(src),'published_capture':ref(dst),'original_accessed_at':row.get('original_accessed_at'),'evidence_id':eid})
newids=[x['evidence_id'] for x in ep['evidence'][len(e['evidence']):]]
for x in [ad,ap]:x['evidence_ids']+= [eid for eid in newids if eid not in x['evidence_ids']]
ad['independent_review']={'status':'complete','evidence_ids':['vm1237-science','vm1237-skeptical']}
dp['decisions']=[ad if x['case_id']==CID else x for x in d['decisions']];pp['proposals'].append(ap)
assert len(dp['decisions'])==188 and len(pp['proposals'])==114
assert pp['proposals'][:113]==p['proposals'] and ep['evidence'][:len(e['evidence'])]==e['evidence']
caserows=[]
for old,new in zip(d['decisions'],dp['decisions']):
 assert old['case_id']==new['case_id'] and ((old==new)==(old['case_id']!=CID))
 for k in ['case_input_sha256','source','occurrence_ids','disposition','missing_requirement','no_change_reason']:assert old[k]==new[k]
 caserows.append({'case_id':new['case_id'],'before_sha256':canon(old),'after_sha256':canon(new),'unchanged':old==new,'case_input_sha256':new['case_input_sha256'],'occurrence_ids':new['occurrence_ids']})
payloadrows=[]
for old in p['proposals']:
 assert sha(A/old['after_capture']['path'])==old['after_capture']['sha256'];payloadrows.append({'proposal_id':old['proposal_id'],'owner_path':old['owner_path'],'original_before_sha256':old['before_sha256'],'selected_capture':old['after_capture'],'original_proposal_object_sha256':canon(old),'unchanged_proposal_object':True,'unchanged_payload':True})
payloadrows.append({'proposal_id':PID,'owner_path':ap['owner_path'],'original_before_sha256':ap['before_sha256'],'selected_capture':ap['after_capture'],'new_authentic_dependent_origin':True,'unchanged_payload':False})
occ=[oid for c in dp['decisions'] for oid in c['occurrence_ids']];assert len(occ)==len(set(occ))==320
save(O/'decisions.json',dp);save(O/'proposals.json',pp);save(O/'evidence.json',ep);save(O/'primary/capture-bindings.json',raws)
save(O/'lineage.json',{'predecessor_head':'79d44c84fe550741bbd8de00c119c48560f30bc1','original_selection':ref(OLD/'selection.json'),'case_count':188,'proposal_count':114,'occurrence_count':320,'unchanged_original_proposals_and_payloads':113,'new_dependent_proposals':1,'unchanged_cases':187,'changed_cases':1,'original_evidence_prefix_preserved':len(e['evidence']),'evidence_count':len(ep['evidence']),'cases':caserows,'payloads':payloadrows,'release_approval':False})
save(O/'selection.json',{'selection_id':'worker08-tenvit-dependent-successor-v1','predecessor_head':'79d44c84fe550741bbd8de00c119c48560f30bc1','predecessor_selection':ref(OLD/'selection.json'),'authoritative_inputs':{n:ref(O/n) for n in ['decisions.json','proposals.json','evidence.json','lineage.json']},'frozen_shard_sha256':dp['shard_sha256'],'counts':{'cases':188,'proposals':114,'occurrence_ids':320,'evidence':len(ep['evidence']),'unchanged_original_payloads':113,'new_dependent_payloads':1,'changed_cases':1,'unchanged_cases':187},'new_dependent_proposal':PID,'changed_case_id':CID,'payload':ap['after_capture'],'nominal_duplicate_reconciliation':ref(O/'author/dependency-dispositions.json'),'original_nbrc903_origin_unchanged':True,'cb_campaign_occurrences':0,'independent_reviews':{role:ref(O/'independent-review'/role/'review.json') for role in ['science','skeptical']},'coordinator_final_head_acceptance':'pending','maintained_application':False,'whole_owner_role_export_approval':False,'prior_TSB_Bacto_admission':'FAILED/HELD unchanged','scope':'Separate report-only existing-owner comparator correction. Existing113 selected payloads remain exact with original limitations; nominal W08/W06 candidates require central reconciliation and are not installed as duplicate source-number owners.'})
shutil.copy2(P/'assemble.py',O/'provenance/assemble.py')
print(json.dumps({'selector':ref(O/'selection.json'),'counts':read(O/'selection.json')['counts'],'raw_capture_count':len(raws)},indent=2))
