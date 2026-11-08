from pathlib import Path
from datetime import datetime,timezone
import copy,json,hashlib,shutil,yaml
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.write_validated import write_validated_ingredient
W=Path.cwd();S=W/'.temp/w05-buffer-parts-v1';O=S/'polypeptone-final';B=W/'reports/all_unmatched_20261107/worker-05';C=W.parents[2];at=datetime.now(timezone.utc).isoformat();j=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def put(n,x):
 q=O/n;assert not q.exists();q.parent.mkdir(parents=True,exist_ok=True);q.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
expected={'polypeptone-final-grounding-decision-v1':('0e98e7a0bb64b76ae7cf5bc81d04a8e02e5a6f8cade180100a83896f42e583b9','36fc016671b2f50bf1e2a6c56c080f07c1fbedc9c9ccd4163e6a0e45765e35a3'),'polypeptone-grounding-independent-v1':(None,'8a4d4c9a3cd798ab00aba719aef4d02a737270aed804ac8a7a01eb2cbc82964d')};integrity=[]
for n,(hand,manifest) in expected.items():
 d=C/'preflight'/n;assert sha(d/'MANIFEST.json')==manifest
 if hand:assert sha(d/'HANDOFF.json')==hand
 m=j(d/'MANIFEST.json')
 for row in m['members']:assert sha(d/row['path'])==row['sha256']
 shutil.copytree(d,O/'inputs'/n);integrity.append(dict(packet=n,handoff_sha256=sha(d/'HANDOFF.json'),manifest_sha256=manifest,members=len(m['members'])))
put('input-integrity.json',dict(at=at,packets=integrity,final_independent_reviewer=j(C/'preflight/polypeptone-grounding-independent-v1/HANDOFF.json')['reviewer'],scope='Exact sealed coordinator guidance and distinct review, not approval of futureworkerpayload. NewformalFoodOnrestriction question is separate and retained.'))
base=B/'tellurium-polypeptone-v1/core';PS=j(base/'proposals.json')['proposals'];DS=j(base/'decisions.json')['decisions'];p=copy.deepcopy(next(p for p in PS if p['proposal_id']=='W05-FINAL-MAT-030'));oldcap=copy.deepcopy(p['after_capture']);f=B/oldcap['path'];assert sha(f)==oldcap['sha256'];old=yaml.safe_load(f.read_text());r=copy.deepcopy(old)
labels=['Polypeptone peptone (BD-BBL)','Polypeptone Peptone (BD 211910)','Polypeptone (BBL)'];before=[]
why='Issue1202 comment6719869255: this label names the specific documented BD casein/animal-tissue blended product. The present owner denotes the supplier-unspecified named Polypeptone preparation; exact interchangeability with this catalogue product is unproved. Preserve the original literal/source as nonresolving provenance. This does not deny the product or prove chemical difference, import its equal-parts formula, mint a BD owner, merge owners, or approve source/role/export.'
for s in r['synonyms']:
 if s['synonym_text'] in labels:
  before.append(copy.deepcopy(s));assert s['synonym_type']=='CATALOG_VARIANT';s['synonym_type']='REJECTED_LABEL';s['source']+='; '+why
assert len(before)==3
r['notes']+='\n\nConsolidated Polypeptone alias correction: '+why+' The filed FOODON broader-grounding recommendation is being reconciled against newly captured full-OWL formal food-additive membership evidence W05-PARENTS-NEW01. This intermediate alias-only candidate leaves the preceding grounding unchanged pending that bounded scientific triage; it does not describe self-only grounding as final sufficient curation. All five prior Japanese/Hipolypepton rejections, source-vintage boundaries,135/135 statistics and computational role remain exact. The separate M122 quantity discrepancy remains in CultureMech150/408 scope without source or quantity edits.'
record_curation_event(r,curator='Codex W05 /root consolidated Polypeptone correction',action='CORRECTED',changes='Filed1202 comment6719869255: change three BD catalogue labels to provenance-only REJECTED_LABEL on supplier-unspecified named Polypeptone. Preserve their exact text/source prefixes and every previous history event. '+why+' Mapping decision remains explicitly pending formal-restriction triage; no FoodOn parent change in this intermediate candidate.',previous_status=r['mapping_status'],new_status=r['mapping_status'],llm_assisted=True,llm_model='gpt-6')
q=O/'proposed-v1/Polypeptone.yaml';assert not q.exists();write_validated_ingredient(r,q);assert yaml.safe_load(q.read_text())==r
for k in set(old)|set(r):
 if k not in ['synonyms','notes','curation_history']:assert old.get(k)==r.get(k),(k,)
assert r['curation_history'][:-1]==old['curation_history'];assert all(s in r['synonyms'] for s in old['synonyms'] if s['synonym_type']=='REJECTED_LABEL');assert sum(s['synonym_type']=='REJECTED_LABEL' for s in r['synonyms'])==8
p['after_capture']=dict(root='artifact',path='buffer-parts-v1/polypeptone-final/proposed-v1/Polypeptone.yaml',sha256=sha(q));p['description']+=' Consolidated alias correction: '+why;p['polypeptone_final_reassessment']=dict(author='/root',at=at,predecessor_capture=oldcap,issue_ref='https://github.com/CultureBotAI/MediaIngredientMech/issues/1202#issuecomment-6719869255',changed_labels=labels,parent_grounding='pending independent reconciliation of fullOWL formalmembership; interim alias-only payload not finalselection');eid='W05-REMAINING-POLYPEPTONE-ALIASES';p['evidence_ids']=list(dict.fromkeys(p['evidence_ids']+[eid]));deltas=[]
for d0 in DS:
 if d0['case_id'] in p['case_ids']:
  d=copy.deepcopy(d0);d['polypeptone_final_reassessment']=copy.deepcopy(p['polypeptone_final_reassessment']);d['evidence_ids']=list(dict.fromkeys(d['evidence_ids']+[eid]));deltas.append(d)
put('alias-assessment-v1.json',dict(author='/root',at=at,source_scope='Full source W05payload and genuinebeforeimage retained; complete manufacturer printed7 and49 read,49visually inspected; sealed coordinatorauthor+distinctreview read.',assessment=why,original_alias_objects=before,after_alias_objects=[s for s in r['synonyms'] if s['synonym_text'] in labels],before_capture=oldcap,after_capture=p['after_capture'],source_guidance=integrity,grounding_status='not selectedpendingformalrestrictiontriage',allfiveoriginalrejections_unchanged=True,history135_role_unchanged=True,source_quantity_hold='CM150/408; no edit'))
put('decisions-v1.json',dict(decisions=deltas));put('proposals-v1.json',dict(proposals=[p]));put('evidence-v1.json',dict(evidence=[dict(evidence_id=eid,kind='source_snapshot',capture=dict(root='artifact',path='buffer-parts-v1/polypeptone-final/alias-assessment-v1.json',sha256=sha(O/'alias-assessment-v1.json')),url='https://github.com/CultureBotAI/MediaIngredientMech/issues/1202#issuecomment-6719869255',accessed_at=at,locator='Three exactBDcataloguealiases, completebefore/after andseparatecoordinatorauthor/review',supports_or_contradicts=why,case_ids=p['case_ids'])]))
print(json.dumps(dict(payload=p['after_capture'],case_count=len(deltas),old_rejections_preserved=5,new_rejections=3,grounding_changed=False)))
