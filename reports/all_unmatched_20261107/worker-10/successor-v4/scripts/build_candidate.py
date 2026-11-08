"""Bounded filed completeness correction in report-only storage."""
from pathlib import Path
import copy,datetime,difflib,hashlib,json,os,subprocess,sys,yaml
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.write_validated import write_validated_ingredient,validate_ingredient
R=Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';B=A/'successor-v3';S=A/'successor-v4';P=R/'.temp/all-unmatched-worker-10/successor-v4'
BASE='c9a96da71a1977014680e5a92e600dfc7e3874db';PID='sv1-buffers-carbonate_co2_nominal4percent_togo_m202';BEFORE='fa07901e230c7cc707ddacb6f5ff70def989c7d1ecfa40118ef2497136e0e1ce';ISSUE='https://github.com/CultureBotAI/MediaIngredientMech/issues/1201#issuecomment-6719089745';FINDINGS=['W10-SV2-INHERITED-COMPLETENESS-001','SCI-CARBONATE-COMPLETENESS-001']
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
sha=lambda raw:hashlib.sha256(raw).hexdigest()
canon=lambda x:sha(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode())
load=lambda p:json.loads(p.read_text())
def save(p,d):
 with p.open('x') as f:json.dump(d,f,indent=2,ensure_ascii=False);f.write('\n')
def binding(p):return {'path':str(p.relative_to(R)),'sha256':sha(p.read_bytes())}
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==BASE
Ds=load(B/'decisions.json');Ps=load(B/'proposals.json');Es=load(B/'evidence.json');proposal=next(x for x in Ps['proposals'] if x['proposal_id']==PID)
source=A/proposal['after_capture']['path'];raw=source.read_bytes();assert sha(raw)==BEFORE;before=yaml.safe_load(raw);assert before['identifier']=='kgmicrobe.ingredient:carbonate_co2_nominal4percent_togo_m202';assert before['component_assertion']['method']=='LABEL_ENUMERATION' and before['component_assertion']['completeness']=='PARTIAL';assert len(before['components'])==2 and all(x['reference_scope']=='UNMAPPED' for x in before['components']);assert before['ontology_mapping']['evidence'][0]['evidence_type']=='LLM_SUGGESTION'
with (S/'inputs/previous-carbonate-stock.yaml').open('xb') as f:f.write(raw)
at=now();after=copy.deepcopy(before);after['component_assertion']['completeness']='UNKNOWN'
event=record_curation_event(after,curator='Codex worker10 /root',action='CORRECTED_COMPONENT_COMPLETENESS',changes='Issue #1201, W10-SV2-INHERITED-COMPLETENESS-001 / SCI-CARBONATE-COMPLETENESS-001: changed only component_assertion.completeness from PARTIAL to UNKNOWN. The complete captured TOGO M202 recipe names the stock and its receiving amount but does not establish stock-list closure or explicitly omitted stock constituents. Preserved LABEL_ENUMERATION, both source-named UNMAPPED parts, LLM_SUGGESTION mapping evidence, original sources and history, and the exact case21/187 source association. Solvent, percentage basis, carbonate hydration, CO2 dose/endpoint, stock pH, supplied form and final volume remain unknown; no water or composition is inferred. No identity, role, whole-owner or export approval change. Filed finding: '+ISSUE,previous_status=before['mapping_status'],new_status=before['mapping_status'],llm_assisted=True,timestamp=at)
rollback=copy.deepcopy(after);rollback['component_assertion']['completeness']='PARTIAL';rollback['curation_history'].pop();assert rollback==before
destination=S/'proposed/carbonate_co2_nominal4percent_togo_m202.yaml'
assert not validate_ingredient(after)
fd=os.open(destination,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o644)
class Reserved:
 parent=destination.parent
 def open(self,mode,encoding=None):
  assert mode=='w' and os.fstat(fd).st_nlink==1
  assert os.fstat(fd).st_ino==destination.stat().st_ino
  return os.fdopen(fd,mode,encoding=encoding)
 def __str__(self):return str(destination)
write_validated_ingredient(after,Reserved());assert yaml.safe_load(destination.read_text())==after
after_capture={'root':'artifact','path':str(destination.relative_to(A)),'sha256':sha(destination.read_bytes())}
with (S/'payload.diff').open('x') as f:f.writelines(difflib.unified_diff(raw.decode().splitlines(True),destination.read_text().splitlines(True),fromfile=str(source.relative_to(R)),tofile=str(destination.relative_to(R))))
evidence_by={x['evidence_id']:x for x in Es['evidence']};primary=[]
for eid in ['buffers-primary-2b7e3ee4d3ec3dfb','kg-mdJ209','kg-md1685']:
 e=evidence_by[eid];path=A/e['capture']['path'];assert sha(path.read_bytes())==e['capture']['sha256'];primary.append(copy.deepcopy(e))
togo=load(A/primary[0]['capture']['path']);md=load(A/primary[1]['capture']['path'])
save(S/'source-assessment.json',{'at':at,'author':'Codex worker10 /root','scope':'Only component list completeness under native enum; source association retained','finding_ids':FINDINGS,'issue':ISSUE,'primary_captures_with_original_timestamps':primary,'fresh_http_primary_retrieval':False,'full_source_sections':togo['components'],'full_source_comments':togo['comments'],'source_meta':togo['meta'],'md_buffer_row':md['data']['solutions'][0]['recipe'][11],'assessment':'Complete M202 has receiving-medium and separate salts tables, but neither a closed buffer stock list nor an explicitly omitted stock constituent. Unknown carrier/basis/form is not evidence that an additional constituent is explicitly omitted. UNKNOWN is the supported completeness value. No medium water, nested salts, pH or total volume is assigned to this stock.','schema_binding':binding(R/'src/mediaingredientmech/schema/mediaingredientmech.yaml'),'scope_and_holds':'Two named parts and source association remain supported within prior scope; no whole-owner/source-case/role/export approval is transferred.'})
save(S/'payload-change-proof.json',{'at':at,'predecessor_head':BASE,'proposal_id':PID,'before':proposal['after_capture'],'after':after_capture,'before_full_object_sha256':canon(before),'after_full_object_sha256':canon(after),'allowed_existing_field':'component_assertion.completeness','before_value':'PARTIAL','after_value':'UNKNOWN','appended_history':event,'history_prefix_exact':after['curation_history'][:-1]==before['curation_history'],'complete_object_equal_after_only_authorized_rollback':rollback==before,'components_exact':after['components']==before['components'],'mapping_evidence_exact':after['ontology_mapping']==before['ontology_mapping'],'source_association_changed':False,'native_writer':'write_validated_ingredient on exclusive O_EXCL/O_NOFOLLOW reserved descriptor','schema_errors':[]})
def ev(eid,path,kind,description):return {'evidence_id':eid,'kind':kind,'capture':{'root':'artifact','path':str(path.relative_to(A)),'sha256':sha(path.read_bytes())},'url':None,'accessed_at':at,'locator':'Complete exact artifact','supports_or_contradicts':description,'case_ids':proposal['case_ids']}
new_evidence=[ev('sv4-carbonate-completeness-source',S/'source-assessment.json','source_assessment','Bounded full-primary completeness assessment; original primary capture timestamps retained; no source association withdrawal.'),ev('sv4-carbonate-completeness-diff',S/'payload-change-proof.json','curation_proof','Exact full payload changes only the filed completeness field and one truthful appended history event.'),ev('sv4-carbonate-filed-finding',S/'inputs/issue1201-filed-finding.json','issue_finding','Exact filed1201 finding precedes this correction; prior severity and finding identities preserved.')]
for e in new_evidence:Es['evidence'].append(e)
new_eids=[e['evidence_id'] for e in new_evidence]
successor={'finding_ids':FINDINGS,'issue':ISSUE,'predecessor_head':BASE,'previous_capture':copy.deepcopy(proposal['after_capture']),'selected_capture':after_capture,'scope':'Only completeness PARTIAL to UNKNOWN, one appended history, and exact dependent text/review bindings. All historical metadata_successor/provenance_successor/stock_payload_unchanged objects retain their original-time meaning.','review_state':'pending_exact_independent_review','prior_independent_review':copy.deepcopy(proposal['independent_review']),'source_association_changed':False,'whole_owner_or_export_approval':False}
proposal['after_capture']=after_capture;proposal['description']=proposal['description'].replace('partial source-supported components','source-named components with unknown list completeness');proposal['publication_holds']=[x.replace('from PARTIAL components','from components with UNKNOWN completeness') for x in proposal['publication_holds']];proposal['evidence_ids']+=new_eids;proposal['completeness_successor']=copy.deepcopy(successor);proposal['independent_review']={'status':'pending','evidence_ids':[]};proposal['review_status_explanation']='Pending separate exact completeness/source assessment and full retention checks for this successor. Prior review objects remain historical; no blanket c9a scientific or whole-owner acceptance is transferred.'
for i in [21,187]:
 d=Ds['decisions'][i];assert d['case_id'] in proposal['case_ids'];oldreview=copy.deepcopy(d['independent_review']);d['completeness_successor']=copy.deepcopy(successor);d['completeness_successor']['prior_independent_review']=oldreview;d['evidence_ids']+=new_eids;d['independent_review']={'status':'pending','evidence_ids':[]}
 if ISSUE not in d['issue_refs']:d['issue_refs'].append(ISSUE)
 if i==21:d['completion_reassessment']['quantitative_or_publication_holds']=[x.replace('from PARTIAL components','from components with UNKNOWN completeness') for x in d['completion_reassessment']['quantitative_or_publication_holds']]
core=S/'author-core';core.mkdir()
for name,value in [('decisions.json',Ds),('evidence.json',Es),('proposals.json',Ps)]:save(core/name,value)
save(S/'author-freeze.json',{'at':now(),'predecessor_head':BASE,'payload':after_capture,'author_core':{n:binding(core/n) for n in ['decisions.json','evidence.json','proposals.json']},'proof':binding(S/'payload-change-proof.json'),'source_assessment':binding(S/'source-assessment.json'),'review_pending':True,'candidate_writes_complete':True})
print(json.dumps({'payload':after_capture,'cases':len(Ds['decisions']),'proposals':len(Ps['proposals']),'phase':'author-core frozen for independent review'},indent=2))
