"""Filed calf-blood wording correction; isolated guarded payload and append-only core."""
from pathlib import Path
import copy,datetime,difflib,hashlib,json,os,subprocess,yaml
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.write_validated import write_validated_ingredient,validate_ingredient
R=Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';B=A/'successor-v4/final-core';S=A/'successor-v5'
BASE='82fc29d837a223edb9c436445ec7ea13d2840c7b';PID='sv1-bio-calf_blood_togo_m2854';ISSUE='https://github.com/CultureBotAI/MediaIngredientMech/issues/1237#issuecomment-6719103915'
load=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();canon=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest();now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(p,d):
 with p.open('x') as f:json.dump(d,f,indent=2,ensure_ascii=False);f.write('\n')
def bind(p):return {'root':'artifact','path':str(p.relative_to(A)),'sha256':sha(p)}
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==BASE
D=load(B/'decisions.json');P=load(B/'proposals.json');E=load(B/'evidence.json');prop=next(p for p in P['proposals'] if p['proposal_id']==PID);case=D['decisions'][44]
oldcap=copy.deepcopy(prop['after_capture']);oldpath=A/oldcap['path'];assert sha(oldpath)==oldcap['sha256']=='62f0dc3300c488be2fb9d52f2c65e8e6826715d81177cf8e4ce48af422ed7338'
before=yaml.safe_load(oldpath.read_text());after=copy.deepcopy(before)
oldtext=prop['description'];assert oldtext==case['reasoning']==case['completion_reassessment']['bounded_scientific_conclusion']
assert oldtext.startswith('TOGO M2854 explicitly identifies calf whole blood. Calf age class distinguishes it from serum;')
newtext='The TOGO M2854 source names calf blood, a blood material rather than serum; calf specifies developmental origin. The source does not explicitly say whole or establish defibrination, lysis, supplier or the basis of its literal 10% receiving dose. Those processing and percentage-basis details remain unknown. The known source material scope can be represented without inferring those details.'
assert after['identifier']=='kgmicrobe.ingredient:calf_blood_togo_m2854'
for container,key in [(after,'notes'),(after['ontology_mapping']['evidence'][0],'notes')]:
 assert container[key].startswith(oldtext);container[key]=newtext+container[key][len(oldtext):]
at=now();event=record_curation_event(after,curator='Codex worker10 /root',action='CORRECTED_CALF_BLOOD_EXPLANATION',changes='Issue #1237, W10-SV3-SKEPTIC-CALF-BLOOD-WORDING: corrected only current record and mapping-evidence notes. The source names calf blood, a blood material rather than serum; calf describes developmental origin, not the blood-versus-serum distinction. Removed the assertion that the source explicitly identifies whole blood. It states a literal 10% receiving dose without establishing its basis. Original history remains verbatim. Identifier, broader blood mapping, LLM_SUGGESTION provenance, source-specific applicability, unknown processing and percentage basis, nonresolving generic label and all role/export holds remain unchanged. No product, fraction-processing protocol, alias or identity change is inferred. Filed finding: '+ISSUE,previous_status=before['mapping_status'],new_status=before['mapping_status'],llm_assisted=True,timestamp=at)
rollback=copy.deepcopy(after);rollback['notes']=before['notes'];rollback['ontology_mapping']['evidence'][0]['notes']=before['ontology_mapping']['evidence'][0]['notes'];rollback['curation_history'].pop();assert rollback==before
dest=S/'proposed/Calf_Blood_TOGO_M2854.yaml';assert not validate_ingredient(after)
fd=os.open(dest,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o644)
class Reserved:
 parent=dest.parent
 def open(self,mode,encoding=None):
  assert mode=='w' and os.fstat(fd).st_nlink==1 and os.fstat(fd).st_ino==dest.stat().st_ino
  return os.fdopen(fd,mode,encoding=encoding)
 def __str__(self):return str(dest)
write_validated_ingredient(after,Reserved());assert yaml.safe_load(dest.read_text())==after
with (S/'payload.diff').open('x') as f:f.writelines(difflib.unified_diff(oldpath.read_text().splitlines(True),dest.read_text().splitlines(True),fromfile=str(oldpath.relative_to(R)),tofile=str(dest.relative_to(R))))
primary=next(e for e in E['evidence'] if e['evidence_id']=='bio-primary-aff5f4b09e39e12c');assert sha(A/primary['capture']['path'])==primary['capture']['sha256']=='12f6464a1dcc66a32160e85433034cfd067ea5e930f3ae6d12ce2c60d6af2770';source=load(A/primary['capture']['path'])
save(S/'source-assessment.json',{'at':at,'author':'Codex worker10 /root','scope':'Only calf-blood explanatory wording; retained identity/mapping is not renewed approval','finding_id':'W10-SV3-SKEPTIC-CALF-BLOOD-WORDING','issue':ISSUE,'source':primary,'source_row':source['components'][0]['items'][1],'source_comments':source['comments'],'full_source_read':True,'assessment':newtext,'source_locator':'components[0].items[1], meta.name and comments[0]; complete capture inspected','no_new_primary_http_retrieval':True,'literal_receiving_amount':{'value':10,'unit':'%','basis':'unknown'},'culture_conditions_not_blood_processing':True,'imported_receiving_unit_not_basis_evidence':True,'original_source_timestamp_preserved':True,'unknowns_preserved':['defibrination','lysis','supplier/product','percentage basis','other processing'],'retained_limits':'Original label, occurrence, local identifier, broader blood mapping, nonresolving provenance and role/export holds remain; no whole-owner approval.'})
save(S/'payload-change-proof.json',{'at':at,'predecessor_head':BASE,'proposal_id':PID,'before':oldcap,'after':bind(dest),'old_explanation':oldtext,'new_explanation':newtext,'allowed_existing_fields':['notes','ontology_mapping.evidence[0].notes'],'appended_history':event,'history_prefix_exact':after['curation_history'][:-1]==before['curation_history'],'complete_object_equal_after_only_authorized_rollback':rollback==before,'before_object_sha256':canon(before),'after_object_sha256':canon(after),'native_writer':'write_validated_ingredient with exclusive O_EXCL/O_NOFOLLOW reserved descriptor','identity_mapping_source_occurrences_aliases_roles_unchanged':True})
newids=[]
for eid,path,kind,summary in [('sv5-calf-source-assessment',S/'source-assessment.json','local_validation','Exact full-primary explanatory scope; original primary timestamp retained.'),('sv5-calf-field-diff',S/'payload-change-proof.json','local_validation','Only two current explanatory notes and one appended history change in the payload.'),('sv5-calf-filed-finding',S/'inputs/issue1237-filed-finding.json','source_snapshot','Exact filed finding precedes correction; no GitHub finding closure.')]:
 E['evidence'].append({'evidence_id':eid,'kind':kind,'capture':bind(path),'url':None,'accessed_at':at,'locator':'Complete exact artifact','supports_or_contradicts':summary,'case_ids':prop['case_ids']});newids.append(eid)
marker={'finding_id':'W10-SV3-SKEPTIC-CALF-BLOOD-WORDING','issue':ISSUE,'predecessor_head':BASE,'previous_capture':oldcap,'selected_capture':bind(dest),'author':'Codex worker10 /root','scope':'Current calf blood explanation and truthful appended history only; original history, source identifiers/mapping and all holds retained.','review_state':'pending_exact_independent_review','identity_or_alias_change':False,'whole_owner_or_export_approval':False}
for row in [prop,case]:
 row['wording_successor']=copy.deepcopy(marker);row['wording_successor']['prior_independent_review']=copy.deepcopy(row['independent_review']);row['evidence_ids']+=newids;row['independent_review']={'status':'pending','evidence_ids':[]}
prop['after_capture']=bind(dest);prop['description']=newtext;prop['review_status_explanation']='Pending exact bounded wording and retained-byte review. Prior provenance and scientific observations remain historical; no blanket c9a or successor-v4 approval transfer.'
case['reasoning']=newtext;case['completion_reassessment']['bounded_scientific_conclusion']=newtext;case['issue_refs'].append(ISSUE)
core=S/'author-core';core.mkdir()
for n,d in [('decisions.json',D),('proposals.json',P),('evidence.json',E)]:save(core/n,d)
save(S/'author-freeze.json',{'at':now(),'predecessor_head':BASE,'payload':bind(dest),'author_core':{n:bind(core/n) for n in ['decisions.json','proposals.json','evidence.json']},'proof':bind(S/'payload-change-proof.json'),'source_assessment':bind(S/'source-assessment.json'),'review_pending':True,'candidate_writes_complete':True})
print(json.dumps({'payload':bind(dest),'cases':len(D['decisions']),'proposals':len(P['proposals']),'phase':'Author core frozen for independent review'},indent=2))
