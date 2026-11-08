"""New complete selector, one changed payload; every predecessor is immutable."""
import copy,datetime,hashlib,json,shutil
from pathlib import Path

ROOT=Path.cwd();P=ROOT/'.temp/all-unmatched-worker-08/plain-flour-method-v1'
A=ROOT/'reports/all_unmatched_20261107/worker-08';OLD=A/'successors/issue-1227-v1/final-v2';O=A/'successors/issue-1227-plain-flour-v1'
PID='op1201-plain-flour';CID='KG_CASE:b9a6261315d83792bc02bfbe425cda2032c8833c7a3b6de3aa665fa62a7fc03e'
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def canon(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def save(p,x):
    p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x') as f:json.dump(x,f,indent=2,ensure_ascii=False);f.write('\n')
def cap(p):return {'root':'artifact','path':str(p.relative_to(A)),'sha256':sha(p)}
peer_expected={'science':'eee808bca0310f04b7100ab878f1e6c9c750de08934862027b71c94245f24c08','skeptical':'08dfb4b4e72ba57cb8d1fccf57441f500d5a08cb2460d3ac5c73d3c3b788cabe'}
for role,expected in peer_expected.items():
    src=P/'independent'/role
    assert sha(src/'review.json')==expected
    review=read(src/'review.json');assert review['verdict']=='pass_with_limitations' and review['full_payload_review']
    assert review['payload_hashes'][PID]=='884fee1ea6a5082a51b8769f2a827199b1703972ad80fa48e1bb8d2d09ab3873'
    shutil.copytree(src,O/'independent-review'/role)
d=read(OLD/'decisions.json');p=read(OLD/'proposals.json');e=read(OLD/'evidence.json')
dp=copy.deepcopy(d);pp=copy.deepcopy(p);ep=copy.deepcopy(e)
ad=read(O/'author/decision.json');ap=read(O/'author/proposal.json')
peerids=['w08-final001-science','w08-final001-skeptical']
ad['independent_review']={'status':'complete','evidence_ids':peerids}
ad['evidence_ids']+=peerids+['w08-final001-historical-review-referral'];ap['evidence_ids']+=peerids+['w08-final001-historical-review-referral']
dp['decisions']=[ad if x['case_id']==CID else x for x in d['decisions']]
pp['proposals']=[ap if x['proposal_id']==PID else x for x in p['proposals']]
additions=[
 ('w08-final001-label-resolution','research/primary-label-resolution.json','local_validation','New explicit native primary-label resolution of adopted generic flour; source Plain flour is not claimed as an ontology synonym or CAS lookup.'),
 ('w08-final001-author-assessment','author/assessment.json','local_validation','Full author material-scope/label-method reassessment and exact before/after binding; not independent approval.'),
 ('w08-final001-filed-comment','inputs/issue1227-comment6719268318.json','local_validation','Exact public issue1227 comment6719268318 read before correction; no GitHub mutation.'),
 ('w08-final001-root-finding','inputs/finding-001-plain-flour-method.json','local_validation','Exact coordinator-confirmed W08-FINAL-001 finding at published1701ccf; original target/predicate not rejected.'),
 ('w08-final001-science','independent-review/science/review.json','independent_review','Separate actual full-payload and source-case scientific review by worker08:/root/vitamins; all material/source/role/export holds retained.'),
 ('w08-final001-skeptical','independent-review/skeptical/review.json','independent_review','Separate actual skeptical full-payload/source-case review by worker08:/root/inorganics. Prior OP review miss disclosed; successor authored by root.'),
 ('w08-final001-historical-review-referral','independent-review/skeptical/coordinator-referral.json','local_validation','PF-LINEAGE-001 identifies unsupported supermarket wording in historical reviewer prose only. Original review preserved; no additional author payload fix or scope expansion.'),
]
for eid,path,kind,support in additions:
    ep['evidence'].append({'evidence_id':eid,'capture':cap(O/path),'kind':kind,'url':None,'locator':'Complete immutable artifact; exact scoped source-case/owner assessment or finding specified within','supports_or_contradicts':support,'case_ids':[CID]})
assert len(dp['decisions'])==188 and len(pp['proposals'])==113 and len(ep['evidence'])==1082
assert ep['evidence'][:len(e['evidence'])]==e['evidence']
case_rows=[]
for old,new in zip(d['decisions'],dp['decisions']):
    assert old['case_id']==new['case_id']
    same=old==new
    assert same==(old['case_id']!=CID)
    for k in ['case_input_sha256','source','occurrence_ids','owner_records','preserved_native_decisions','disposition','applicability','missing_requirement','no_change_reason','proposal_ids']:
        assert old.get(k)==new.get(k),(old['case_id'],k)
    case_rows.append({'case_id':old['case_id'],'before_decision_sha256':canon(old),'after_decision_sha256':canon(new),'unchanged':same,'case_input_sha256':new['case_input_sha256'],'occurrence_ids':new['occurrence_ids'],'scientific_review_scope':'new entire single-case review'if not same else'exact predecessor decision/review continuity only'})
payload_rows=[]
for old,new in zip(p['proposals'],pp['proposals']):
    assert old['proposal_id']==new['proposal_id']
    for k in ['owner_path','before_sha256','case_ids','kind']:assert old[k]==new[k]
    for prop in [old,new]:assert sha(A/prop['after_capture']['path'])==prop['after_capture']['sha256']
    same=old['after_capture']==new['after_capture'];assert same==(old['proposal_id']!=PID)
    if same:assert old==new
    payload_rows.append({'proposal_id':old['proposal_id'],'owner_path':old['owner_path'],'original_before_sha256':old['before_sha256'],'predecessor_capture':old['after_capture'],'selected_capture':new['after_capture'],'payload_byte_exact_unchanged':same,'proposal_object_unchanged':old==new,'review_scope':'new full payload science and skepticism'if not same else'exact predecessor payload/review continuity only'})
occ=[x for row in dp['decisions'] for x in row['occurrence_ids']];assert len(occ)==len(set(occ))==320
save(O/'decisions.json',dp);save(O/'proposals.json',pp);save(O/'evidence.json',ep)
save(O/'lineage.json',{'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'predecessor_head':'1701ccf2049022866adfcebcc9bba9b6492407c6','case_count':188,'proposal_count':113,'occurrence_count':320,'changed_case_count':1,'changed_payload_count':1,'unchanged_case_count':187,'unchanged_payload_count':112,'original_evidence_entries_preserved':len(e['evidence']),'cases':case_rows,'payloads':payload_rows,'all_prior_beforeimages_source_objects_occurrence_ids_and_embedded_holds_preserved':True,'scope':'Hash continuity and accounting do not grant fresh scientific or release approval to unchanged payloads.'})
save(O/'selection.json',{'selection_id':'worker08-plain-flour-method-successor-v1','predecessor_head':'1701ccf2049022866adfcebcc9bba9b6492407c6','supersedes_selection_only':'successors/issue-1227-v1/final-v2; all bytes retained as historical evidence','authoritative_inputs':{n:cap(O/n) for n in ['decisions.json','proposals.json','evidence.json','lineage.json']},'frozen_shard_sha256':dp['shard_sha256'],'counts':{'cases':188,'proposals':113,'occurrence_ids':320,'evidence':len(ep['evidence']),'changed_payloads':1,'unchanged_payloads':112,'changed_cases':1,'unchanged_cases':187},'changed_proposal_id':PID,'changed_case_id':CID,'changed_payload':ap['after_capture'],'unchanged_other_payload_proof':cap(O/'lineage.json'),'initial_exact_independent_reviews':{role:cap(O/'independent-review'/role/'review.json') for role in peer_expected},'final_index_readback':'Separate final-bindings receipts will bind these exact final indices without an evidence self-hash cycle.','coordinator_final_head_acceptance':'pending','whole_owner_role_export_approval':False,'maintained_application':False,'prior_TSB_Bacto_admission':'FAILED/HELD unchanged; new preferred flour label grants no admission waiver.'})
shutil.copy2(P/'assemble.py',O/'provenance/assemble.py')
print(json.dumps({'selector':cap(O/'selection.json'),'payload':ap['after_capture'],'counts':read(O/'selection.json')['counts']},indent=2))
