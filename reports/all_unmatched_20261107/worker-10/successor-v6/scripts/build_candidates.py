"""Five qualified source-assertion corrections through the native guarded writer."""
from pathlib import Path
import copy,datetime,difflib,hashlib,json,os,subprocess,yaml
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.write_validated import validate_ingredient,write_validated_ingredient
R=Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';B=A/'successor-v5/final-core';S=A/'successor-v6';P=R/'.temp/all-unmatched-worker-10/successor-v6'
BASE='3e190a0f6c5a978ca8ed7e3bc7b6a2d66935548b';ISSUE='https://github.com/CultureBotAI/MediaIngredientMech/issues/1201#issuecomment-6719268125';DIFCO='sv3-hm-difco-columbia1270'
load=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();canon=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest();now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(p,d):
 with p.open('x') as f:json.dump(d,f,indent=2,ensure_ascii=False);f.write('\n')
def bind(p):return {'root':'artifact','path':str(p.relative_to(A)),'sha256':sha(p)}
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==BASE
D=load(B/'decisions.json');Ps=load(B/'proposals.json');E=load(B/'evidence.json');tr=load(S/'inputs/triage-TRIAGE-v2.json');pre=load(S/'preflight.json');rows=[];at=now()
HCL_NOTE='Component-list completeness is UNKNOWN: the cited receiving recipes name and dose HCl but do not establish the complete acid-reagent formulation or explicitly identify omitted constituents. Separately listed receiving-stock water is not evidence of the acid reagent carrier.'
DIFCO_NOTE='CURATED_INTERPRETATION covers the seven immediate ingredient names in the nominal Difco Columbia Blood Agar Base formula published in the BD Difco & BBL Manual, second edition (2009), printed page 158 / PDF page 170. COMPLETE applies only to that nominal constituent-name list: all seven listed immediate ingredients are represented. This is not a complete molecular composition, an exact historical JCM1270 lot formulation, or a quantitative recipe transcription. The manufacturer performance-adjustment/supplementation footnote and unknown actual JCM lot remain explicit limitations. Component quantities and dry-mass ratios are not asserted. Blood and reconstitution water are not dry-base components. Existing mixed-owner partition and owner/role/export holds remain.'
for name in ['bd2009-p158.png','bd2009-title.txt','bd2009-printed155-159.txt']:
 with (S/'inputs'/name).open('xb') as f:f.write((P/'inputs'/name).read_bytes())
for t in tr['rows']:
 pid=t['proposal_id'];prop=next(p for p in Ps['proposals'] if p['proposal_id']==pid);oldcap=copy.deepcopy(prop['after_capture']);path=A/oldcap['path'];assert sha(path)==oldcap['sha256']==t['payload_sha256'];before=yaml.safe_load(path.read_text());after=copy.deepcopy(before);a=after['component_assertion'];assert a==t['current_assertion'] and a['completeness']=='PARTIAL' and a['method']=='LABEL_ENUMERATION'
 fields=['component_assertion.completeness','component_assertion.notes'];findings=['W09-W10-SKEPTIC-COMPONENT-CLOSURE']
 if pid==DIFCO:
  assert len(after['components'])==7;a['method']='CURATED_INTERPRETATION';a['completeness']='COMPLETE';a['notes']=DIFCO_NOTE;fields.insert(0,'component_assertion.method');findings.insert(0,'W09-W10-SKEPTIC-DIFCO-COMPONENT-METHOD');explanation=DIFCO_NOTE
 else:
  assert len(after['components'])==1 and after['components'][0]['component_name']=='HCl' and after['components'][0]['reference_scope']=='UNMAPPED';a['completeness']='UNKNOWN';a['notes']=a['notes']+' '+HCL_NOTE;explanation=HCL_NOTE
 changes=('Issue #1201, '+', '.join(findings)+': corrected only the component assertion fields '+', '.join(fields)+'. '+explanation+' Preserved all component objects, names, identities, quantities, sources, original history, supplied-form and source-case scope, and every remaining overlap/partition/role/export hold. This is an LLM-assisted source-relative assertion correction, not human scientific review, a new owner decision or release approval. Filed qualified triage: '+ISSUE)
 event=record_curation_event(after,curator='Codex worker10 /root',action='CORRECTED_SOURCE_RELATIVE_COMPONENT_ASSERTION',changes=changes,previous_status=before['mapping_status'],new_status=before['mapping_status'],llm_assisted=True,timestamp=now())
 rollback=copy.deepcopy(after);rollback['component_assertion']=copy.deepcopy(before['component_assertion']);rollback['curation_history'].pop();assert rollback==before;assert a['evidence']==before['component_assertion']['evidence'];assert not validate_ingredient(after)
 dest=S/'proposed'/(pid+'.yaml');fd=os.open(dest,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o644)
 class Reserved:
  parent=dest.parent
  def open(self,mode,encoding=None):
   assert mode=='w' and os.fstat(fd).st_nlink==1 and os.fstat(fd).st_ino==dest.stat().st_ino
   return os.fdopen(fd,mode,encoding=encoding)
  def __str__(self):return str(dest)
 write_validated_ingredient(after,Reserved());assert yaml.safe_load(dest.read_text())==after
 with (S/'diffs'/(pid+'.diff')).open('x') as f:f.writelines(difflib.unified_diff(path.read_text().splitlines(True),dest.read_text().splitlines(True),fromfile=str(path.relative_to(R)),tofile=str(dest.relative_to(R))))
 cases=[i for i,d in enumerate(D['decisions']) if pid in d['proposal_ids']]
 row={'proposal_id':pid,'case_indices':cases,'case_ids':prop['case_ids'],'before':oldcap,'after':bind(dest),'changed_existing_fields':fields,'before_assertion':before['component_assertion'],'after_assertion':a,'appended_history':event,'history_prefix_exact':after['curation_history'][:-1]==before['curation_history'],'components_mapping_form_quantities_sources_exact':True,'complete_object_equal_after_authorized_rollback':rollback==before,'before_object_sha256':canon(before),'after_object_sha256':canon(after),'primary_bindings':t['primary_evidence'],'conclusion':explanation,'finding_ids':findings};rows.append(row)
 marker={'finding_ids':findings,'issue':ISSUE,'predecessor_head':BASE,'previous_capture':oldcap,'selected_capture':bind(dest),'author':'Codex worker10 /root','active_assertion_scope':explanation,'scope':'Only component method/completeness/necessary assertion explanation and truthful history; exact current dependencies. All original identity, quantity, source and unresolved holds retained.','review_state':'pending_exact_independent_review','source_case_association_changed':False,'whole_owner_or_export_approval':False}
 prop['after_capture']=bind(dest)
 if pid!=DIFCO:
  assert 'partial source-supported components' in prop['description'];prop['description']=prop['description'].replace('partial source-supported components','source-named components with unknown list completeness',1)
  prop['publication_holds']=[x.replace('from PARTIAL components','from components with UNKNOWN completeness') for x in prop['publication_holds']]
 prop['review_status_explanation']='Pending exact five-payload assertion review. Original W09 finding IDs and the qualified HCl/Difco split are preserved; prior identity/source/role/export judgments and carbonate/calf reviews are not blanket-transferred.'
 for obj in [prop]+[D['decisions'][i] for i in cases]:
  obj['component_assertion_successor']=copy.deepcopy(marker);obj['component_assertion_successor']['prior_independent_review']=copy.deepcopy(obj['independent_review']);obj['independent_review']={'status':'pending','evidence_ids':[]}
 for i in cases:
  d=D['decisions'][i]
  if pid==DIFCO:
   old='Retain PARTIAL names-only components and no dry mass-ratio inference.';new='Use CURATED_INTERPRETATION with COMPLETE limited to the seven immediate names in the nominal 2009 manufacturer list; historical JCM lot, performance adjustments and quantitative ratios remain unverified. No dry mass-ratio inference.';assert old in d['reasoning'];d['reasoning']=d['reasoning'].replace(old,new,1)
  else:
   assert d['successor_v3_reassessment']['old_completion_reassessment_is_historical'] is True
   d['component_assertion_successor']['historical_completion_reassessment_preserved']='The old completion_reassessment is explicitly historical and remains byte-exact, including its former PARTIAL wording. Current completeness is UNKNOWN as stated in active_assertion_scope; no historical wording is promoted as the current enum.'
  if ISSUE not in d['issue_refs']:d['issue_refs'].append(ISSUE)
save(S/'payload-change-proof.json',{'at':at,'predecessor_head':BASE,'rows':rows,'only_five_selected_payloads_changed':True,'native_writer':'write_validated_ingredient with exclusive O_EXCL/O_NOFOLLOW reserved descriptors','all_original_histories_components_and_sources_exact':True})
save(S/'source-assessment.json',{'at':at,'author':'Codex worker10 /root','scope':'Source-relative assertion method/completeness only; no new identity/owner/role/export decision','original_finding_ids':['W09-W10-SKEPTIC-DIFCO-COMPONENT-METHOD','W09-W10-SKEPTIC-COMPONENT-CLOSURE'],'issue':ISSUE,'qualified_split':'Four HCl UNKNOWN; Difco CURATED_INTERPRETATION and COMPLETE only for the expressly nominal 2009 seven immediate ingredient-name list. Original blanket five-target UNKNOWN suggestion is preserved historically but not adopted.','rows':[{'proposal_id':x['proposal_id'],'case_indices':x['case_indices'],'primary_bindings':x['primary_bindings'],'assessment':x['conclusion']} for x in rows],'primary_bodies':pre['primary_bodies'],'primary_review_scope':'All 12 non-PDF recipe bodies inspected through complete recipe tables/steps/comments; irrelevant web navigation and semantic enrichment do not support these claims. BD PDF title and Columbia section pp155-159 extracted, with printed158/PDF170 table/footnote visually inspected from an independently rendered full-page image.','bd_pdf_sha256':'e5e836a75f13283d477467b20ffc0d332531e0f3a0effb5d64a7147a6985c0b7','bd_original_accessed_at':'2026-11-08T06:55:09.048187+00:00','bd_visual':bind(S/'inputs/bd2009-p158.png'),'bd_section_text':bind(S/'inputs/bd2009-printed155-159.txt'),'bd_title_text':bind(S/'inputs/bd2009-title.txt'),'nominal_names':[x['component_name'] for x in yaml.safe_load((S/'proposed'/(DIFCO+'.yaml')).read_text())['components']],'nominal_closure_not_lot_closure':True,'no_quantitative_parts_added':True,'hcl_receiving_water_not_acid_carrier_evidence':True,'no_new_primary_http_retrieval':True,'original_primary_timestamps_preserved':True,'historical_completion_reassessments_not_rewritten':True})
eids=[];allcaseids=sorted({cid for x in rows for cid in x['case_ids']})
for eid,path,kind,summary in [('sv6-source-assertion-assessment',S/'source-assessment.json','local_validation','Qualified five-target primary assertion assessment; exact original capture timestamps and 13 bodies retained.'),('sv6-exact-assertion-diffs',S/'payload-change-proof.json','local_validation','Exact allowed field and history changes; all component objects, sources and other record fields unchanged.'),('sv6-filed-qualified-findings',S/'inputs/issue1201-filed-finding.json','source_snapshot','Exact filed comment preserves original W09 finding IDs and qualified split before correction.')]:
 E['evidence'].append({'evidence_id':eid,'kind':kind,'capture':bind(path),'url':None,'accessed_at':at,'locator':'Complete exact artifact','supports_or_contradicts':summary,'case_ids':allcaseids});eids.append(eid)
for obj in [p for p in Ps['proposals'] if p['proposal_id'] in {x['proposal_id'] for x in rows}]+[D['decisions'][i] for i in sorted({i for x in rows for i in x['case_indices']})]:obj['evidence_ids']+=eids
core=S/'author-core';core.mkdir()
for n,d in [('decisions.json',D),('proposals.json',Ps),('evidence.json',E)]:save(core/n,d)
save(S/'author-freeze.json',{'at':now(),'predecessor_head':BASE,'payloads':[{'proposal_id':x['proposal_id'],'capture':x['after']} for x in rows],'author_core':{n:bind(core/n) for n in ['decisions.json','proposals.json','evidence.json']},'proof':bind(S/'payload-change-proof.json'),'source_assessment':bind(S/'source-assessment.json'),'review_pending':True,'candidate_writes_complete':True})
print(json.dumps({'payloads':[{'proposal_id':x['proposal_id'],'capture':x['after']} for x in rows],'case_indices':sorted({i for x in rows for i in x['case_indices']}),'phase':'author-core frozen'},indent=2))
