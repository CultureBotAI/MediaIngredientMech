from pathlib import Path
from datetime import datetime, timezone
from copy import deepcopy
import hashlib,json,shutil,difflib,dataclasses,subprocess
import yaml
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.write_validated import write_validated_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy

W=Path.cwd();C=W.parents[2];S=W/'.temp/w05-buffer-parts-v1/dependencies-direct-v1';OLD=W/'.temp/w05-buffer-parts-v1/dependencies';PAR=W/'.temp/w05-buffer-parts-v1/parents-direct-v1';CO=C/'preflight/polypeptone-owl-reassessment-v1'
PUB='buffer-parts-v1/dependencies-direct-v1/';AUTHOR='/root/buffer_tris';now=datetime.now(timezone.utc).isoformat()
TIDS={'PC03','PC16','PC17','PC18','PC19'}
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def oh(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def put(p,o):p.parent.mkdir(parents=True,exist_ok=True);assert not p.exists(),p;p.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n')
def cp(p,q):q.parent.mkdir(parents=True,exist_ok=True);assert not q.exists(),q;shutil.copyfile(p,q);assert h(p)==h(q)
def ref(p):return {'root':'artifact','path':PUB+str(p.relative_to(S)),'sha256':h(p)}

assert h(OLD/'MANIFEST.json')=='4bf5f4806299a58ef9d6af22c93beca0f576dee0989ecf438114d3499ef4b514'
assert h(OLD/'HANDOFF.json')=='34b00b366410e10d8a4f06fdcf9fe44dd60bfa13a8223d7d9e963efeb00a71bd'
om=json.loads((OLD/'MANIFEST.json').read_text())
for r in om['members']:assert h(OLD/r['path'])==r['sha256'],r['path']
assert h(CO/'HANDOFF.json')=='ed4b490104249457bbb557767418eff3d19437aab459a5084cb91a2658c41663'
assert h(CO/'MANIFEST.json')=='f9aa228a3dee456ec0da909a3ce1de0288e82aa00f89481527ed502d5c200b32'
cm=json.loads((CO/'MANIFEST.json').read_text())
for r in cm['members']:
 assert h(CO/r['path'])==r['sha256'];cp(CO/r['path'],S/'inputs/coordinator-reassessment'/r['path'])
for n in ['HANDOFF.json','MANIFEST.json']:cp(CO/n,S/'inputs/coordinator-reassessment'/n)
for n in ['HANDOFF.json','MANIFEST.json','SEAL.json','proposals.json','evidence.json','case-deltas.json','source-assessment.json','source-observations.json','source-read-ledger.json','input-bindings.json','chronology.json']:
 cp(OLD/n,S/'inputs/sealed-dependencies'/n)
cp(OLD/'inputs/w03-peer/machine-ledger.json',S/'inputs/all20-original-machine-ledger.json')
cp(OLD/'source-observations.json',S/'source-observations.json')
cp(OLD/'inputs/w03-peer/other/context/original-capture-metadata.json',S/'inputs/original-capture-metadata.json')
for n in ['proposals.json','scientific-plan.json','author-receipt.json','proposed/Peptone.yaml','read/thermo.txt']:
 cp(PAR/n,S/'inputs/final-parent'/n)
for n in ['mesh-D010461-nlm','mesh-M0016245-nlm','mesh-D010461-browser','thermo.pdf']:
 body=(n if n.endswith('.pdf') else n+'.json');receipt=n+'.receipt.json'
 cp(PAR/'captures'/body,S/'inputs/primary'/body);cp(PAR/'captures'/receipt,S/'inputs/primary'/receipt)

parent_proposals=json.loads((PAR/'proposals.json').read_text())['proposals'];pp=next(p for p in parent_proposals if p['proposal_id']=='W05-FINAL-MAT-039');parent=yaml.safe_load((PAR/'proposed/Peptone.yaml').read_text())
assert h(PAR/'proposed/Peptone.yaml')==pp['after_capture']['sha256']=='c083794668a362203de6430eaa2609c34cd8ef78574a1230aa25b4a64fb55fd7'
assert parent['identifier']==parent['ontology_mapping']['ontology_id']=='mesh:D010461' and parent['ontology_mapping']['mapping_quality']=='EXACT_MATCH'
assert parent['preferred_term']=='Peptone'
P=deepcopy(json.loads((OLD/'proposals.json').read_text()));E=deepcopy(json.loads((OLD/'evidence.json').read_text()));D=deepcopy(json.loads((OLD/'case-deltas.json').read_text()));A=deepcopy(json.loads((OLD/'source-assessment.json').read_text()));case=next(d['case_id'] for d in D['case_deltas'] if len(d['union_proposal_ids'])==12)
bindings=[];changed=[];checks=[];events=[]
text=('Retarget only this source-supported generic peptone part from the earlier conditional local identity kgmicrobe.ingredient:peptone to the reviewed direct generic identity mesh:D010461 (Peptones), represented by the Peptone owner. The primary NLM descriptor explicitly includes Peptone; its conventional partial protein-hydrolysis definition and the manufacturer generic description support the ordinary unspecified peptone sense under MAPPING_SEMANTICS section3 exact-term priority. Unknown supplier, lot or digestion detail does not itself establish a different material or require a new process/precipitation assay gate. The raw named-input evidence and material scope are unchanged. The previous local-target event and assertion notes are preserved as superseded routing history. Preserve LABEL_ENUMERATION and COMPLETE relative to the named inputs, all quantities and their absence, raw labels, source occurrences and all other parts. This does not assign Bacto, animal origin, supplier product, formulation equivalence, source-assay admission, roles or export approval. Apply only with the exact reviewed direct Peptone parent in the same phase; no global identifier replacement.')
for p in P['proposals']:
 tid=p['dependency_reassessment']['target_id'];oldp=deepcopy(p);before=OLD/'proposed'/Path(p['owner_path']).name
 assert h(before)==p['after_capture']['sha256'];assert h(W/p['owner_path'])==p['before_sha256']
 cp(before,S/'selected-predecessor'/before.name);record=yaml.safe_load(before.read_text());original=deepcopy(record)
 if tid in TIDS:
  i=p['dependency_reassessment']['claim_key'].split('components[')[1].split(']')[0];i=int(i)
  assert record['components'][i]['component_id']=='kgmicrobe.ingredient:peptone' and record['components'][i]['reference_scope']=='MIM_CATALOG'
  record['components'][i]['component_id']='mesh:D010461'
  record['notes']+=' Direct generic identity successor: '+text
  record['component_assertion']['notes']+=' Direct generic identity successor: '+text
  record['component_assertion']['evidence'].append({'evidence_type':'CURATED_DATASET','source':'https://id.nlm.nih.gov/mesh/D010461','source_record':'NLM descriptor D010461 Peptones, entry term Peptone, preferred concept M0016245; '+tid+' exact raw MicrobeDecoder labels retained in '+PUB+'source-observations.json','notes':'The descriptor and manufacturer generic definition support the reviewed generic Peptone owner identity; the exact source labels support this named part. LLM-assisted applicability assessment by /root/buffer_tris, following separate primary author /root/buffer_hepes and coordinator skeptical reassessment /root/step7d_independent_review. '+text})
  event=record_curation_event(record,curator='Codex worker05 '+AUTHOR,action='RETARGET_DIRECT_GENERIC_PEPTONE',changes=text,previous_status=record['mapping_status'],new_status=record['mapping_status'],llm_assisted=True,llm_model='gpt-6')
  out=S/'proposed'/before.name;write_validated_ingredient(record,out)
  p['after_capture']=ref(out);p['description']='Follow the exact reviewed generic Peptone owner identity mesh:D010461 for the explicitly named generic source part; preserve the full child preparation and all source-specific holds.'
  eids=['W05-DEP-DIRECT-'+tid,'W05-DEP-DIRECT-NLM','W05-DEP-DIRECT-NLM-CONCEPT','W05-DEP-DIRECT-THERMO','W05-DEP-DIRECT-COORDINATOR']
  p['evidence_ids']=list(dict.fromkeys(p['evidence_ids']+eids))
  p['direct_generic_successor']={'author':AUTHOR,'at':event['timestamp'],'predecessor_proposal_object_sha256':oh(oldp),'predecessor_after_capture':oldp['after_capture'],'exact_parent_proposal_id':pp['proposal_id'],'exact_parent_after_capture':pp['after_capture'],'new_part_identifier':'mesh:D010461','source_scope_change':False,'new_case_or_owner':False,'history_and_all_prior_evidence_preserved':True,'guarded_write':'PASS','independent_final_byte_review':'pending'}
  # Earlier metadata remains historical, and active successor metadata explicitly supersedes its destination.
  p['publication_obligations']+=' Direct successor selects mesh:D010461 with exact parent '+pp['after_capture']['sha256']+'; previous conditional local destination is superseded. All source/product/role/export holds remain.'
  row=next(r for r in A['rows'] if r['target_id']==tid);row['predecessor_assessment']=deepcopy(row);row['scientific_assessment']=text;row['after_capture']=p['after_capture'];row['preserved_part']=deepcopy(record['components'][i]);row['curation_event']=event;row['actual_review_read_at']=now;row['source_ids']=list(dict.fromkeys(row['source_ids']+['NLM-D010461','NLM-M0016245','THERMO-GENERIC','COORDINATOR-EXACT-SENSE']));row['exact_parent_after_capture']=pp['after_capture'];row['precise_remaining_requirement']='Exact parent and these five final payload bytes need independent final review and same-phase application. No supplier/lot assay prerequisite is added to the genuinely generic named part.'
  row['disposition']='SUPPORTED_GENERIC_COMPONENT_DIRECT_MESH_CONDITIONAL_ON_REVIEWED_PARENT'
  for k in set(record)|set(original):
   if k not in {'components','notes','component_assertion','curation_history'}:assert record.get(k)==original.get(k),(tid,k)
  assert record['curation_history'][:-1]==original['curation_history'];assert record['component_assertion']['evidence'][:-1]==original['component_assertion']['evidence']
  assert record['component_assertion']['method']==original['component_assertion']['method']=='LABEL_ENUMERATION';assert record['component_assertion']['completeness']==original['component_assertion']['completeness']=='COMPLETE'
  for j,c in enumerate(original['components']):
   exp=deepcopy(c)
   if j==i:exp['component_id']='mesh:D010461'
   assert record['components'][j]==exp
  dp=S/'diffs'/(out.stem+'.diff');dp.parent.mkdir(parents=True,exist_ok=True);dp.write_text(''.join(difflib.unified_diff(before.read_text().splitlines(True),out.read_text().splitlines(True),fromfile=oldp['after_capture']['path'],tofile=p['after_capture']['path'])))
  changed.append(tid);events.append({'target_id':tid,'event':event});checks.append({'target_id':tid,'preserved_authentic_before_sha256':p['before_sha256'],'selected_predecessor_sha256':h(before),'after_sha256':h(out),'all_prior_history_and_evidence_objects_preserved':True,'unchanged_whole_mapping_evidence':True,'unchanged_all_other_components_labels_quantities_occurrences':True,'guarded_schema':'PASS'})
 else:
  assert p==oldp;out=S/'selected-unchanged'/before.name;cp(before,out);assert h(out)==h(before)
 bindings.append({'target_id':tid,'proposal_id':p['proposal_id'],'owner_path':p['owner_path'],'authentic_before_sha256':p['before_sha256'],'selected_after_capture':p['after_capture'],'private_full_payload_path':str(out.relative_to(S)),'payload_changed':tid in TIDS,'prior_proposal_object_sha256':oh(oldp),'new_proposal_object_sha256':oh(p)})
assert set(changed)==TIDS
A['direct_generic_successor']={'author':AUTHOR,'at':now,'changed_targets':sorted(TIDS),'source':'Exact NLM primary captures and sealed coordinator semantic reassessment inspected; prior all20 outcome and130observation accounting retained.','exact_parent_proposal':pp['after_capture'],'prior_packet_manifest_sha256':h(OLD/'MANIFEST.json'),'no_new_cases_or_owners':True,'all_other_10_scientific_rows_unchanged':True,'no_global_retarget':True}
put(S/'source-assessment.json',A);put(S/'proposals.json',P)
for tid in sorted(TIDS):
 E['evidence'].append({'evidence_id':'W05-DEP-DIRECT-'+tid,'kind':'source_snapshot','capture':ref(S/'source-assessment.json'),'url':None,'locator':'rows[target_id='+tid+']; direct_generic_successor','supports_or_contradicts':text,'case_ids':[case],'author':AUTHOR,'assessed_at':now})
for eid,body,kind,loc,support in [
 ('W05-DEP-DIRECT-NLM','mesh-D010461-nlm.json','ontology','Complete active NLM descriptor; browser entry term Peptone independently inspected','Active generic Peptones descriptor; direct generic identity priority applies to the explicit source peptone sense.'),
 ('W05-DEP-DIRECT-NLM-CONCEPT','mesh-M0016245-nlm.json','ontology','Complete preferred concept and material scope note','Conventional partial hydrolysis definition; no source-specific lot/assay gate inferred.'),
 ('W05-DEP-DIRECT-THERMO','thermo.pdf','primary_source','Printed page7 generic peptone definition and variable material/process scope; complete PDF preserved','Independent manufacturer generic partial protein-hydrolysate description. Product differences are preserved, not collapsed into one branded material.')]:
  receipt=json.loads((S/'inputs/primary'/(body.removesuffix('.json')+'.receipt.json' if body.endswith('.json') else body+'.receipt.json')).read_text())
  E['evidence'].append({'evidence_id':eid,'kind':kind,'capture':ref(S/'inputs/primary'/body),'url':receipt['url'],'accessed_at':receipt['accessed_at'],'locator':loc,'supports_or_contradicts':support,'case_ids':[case],'original_capture_author':receipt.get('author','/root/buffer_hepes'),'successor_assessor':AUTHOR})
E['evidence'].append({'evidence_id':'W05-DEP-DIRECT-COORDINATOR','kind':'independent_review','capture':ref(S/'inputs/coordinator-reassessment/HANDOFF.json'),'url':None,'locator':'Complete sealed scientific reassessment; decision.json and ASSESSMENT.md copied exactly','supports_or_contradicts':'Separate /root/step7d_independent_review directs native exact generic sense priority and distinguishes source/product holds; this old comparison does not approve the five new final payload bytes.','case_ids':[case]})
put(S/'evidence.json',E)
delta=next(d for d in D['case_deltas'] if d['case_id']==case);delta['union_evidence_ids']=list(dict.fromkeys(delta['union_evidence_ids']+[e['evidence_id'] for e in E['evidence'] if e['evidence_id'].startswith('W05-DEP-DIRECT-')]))
delta['set_distinct_field']['dependency_direct_reassessment']={'author':AUTHOR,'at':now,'changed_targets':sorted(TIDS),'proposal_ids':[p['proposal_id'] for p in P['proposals'] if p['dependency_reassessment']['target_id'] in TIDS],'parent_proposal_id':pp['proposal_id'],'parent_identifier':'mesh:D010461','parent_exact_after_capture':pp['after_capture'],'source_scope_change':False,'all_20_prior_outcomes_and_130_observations_preserved':True,'precise_scope':text,'prior_dependency_reassessment_retained_as_history':True,'independent_final_review':'pending','source_assessment':ref(S/'source-assessment.json')}
put(S/'case-deltas.json',D)
put(S/'selection-and-bindings.json',{'author':AUTHOR,'at':now,'parent_after_capture':pp['after_capture'],'parent_proposal_id':pp['proposal_id'],'parent_payload_snapshot':ref(S/'inputs/final-parent/proposed/Peptone.yaml'),'prior_packet_verified_members':len(om['members']),'coordinator_packet_verified_members':len(cm['members']),'rows':bindings,'changed_count':5,'unchanged_full_payload_count':10,'new_source_cases':0,'new_owners':0,'all20_claims':ref(S/'inputs/all20-original-machine-ledger.json'),'all130_observations':ref(S/'source-observations.json')})
put(S/'source-read-ledger.json',{'at':now,'reader':AUTHOR,'sources':[{'path':str(p.relative_to(S)),'sha256':h(p),'original_receipt':json.loads((S/'inputs/primary'/(p.name.removesuffix('.json')+'.receipt.json' if p.name.endswith('.json') else p.name+'.receipt.json')).read_text())} for p in (S/'inputs/primary').iterdir() if p.is_file() and not p.name.endswith('.receipt.json')],'read_extent':{'mesh_descriptor':'Complete descriptor JSON plus browser descriptor/entry-term/preferred concept scope text; HTML scripts not substantive evidence.','mesh_concept':'Complete scope-note JSON.','thermo':'Printed pp7-8 generic material and manufacturing description; no supplier product identity transferred.','coordinator':'Complete sealed HANDOFF, decision and ASSESSMENT; all35manifestmembers verified.','old_dependencies':'All449manifestmembers reverified; all15 complete selected payloads parsed and guarded unchanged-field comparisons performed for the5retargets.','source_rows':'All130 original observations carried byte-identically; earlier source scientists and exact capture timestamps remain in preserved predecessor source-read-ledger. No new130-paper retrieval claimed.'},'new_network_fetches':0,'prior_source_authors':['/root/peptone_ambiguous_sources','/root/peptone_other_sources'],'prior_source_skeptic':'/root/peptone_skeptic','parent_author':'/root/buffer_hepes','coordinator_scientific_reviewer':'/root/step7d_independent_review','new_exact_byte_skeptical_review':'pending /root/final_skeptical assignment; no reused approval','chronology':{'coordinator_assessment_sealed':json.loads((CO/'HANDOFF.json').read_text())['at'],'parent_authored_at':json.loads((PAR/'author-receipt.json').read_text())['at'],'child_new_events':events},'full_parent_claim_approval':False})
by={str(p.relative_to(W)):yaml.safe_load(p.read_text()) for p in list((W/'data/ingredients/mapped').glob('*.yaml'))+list((W/'data/ingredients/unmapped').glob('*.yaml'))};by['data/ingredients/mapped/Peptone.yaml']=parent
for b in bindings:by[b['owner_path']]=yaml.safe_load((S/b['private_full_payload_path']).read_text())
v=validate_component_partonomy(by.values());assert not v,[dataclasses.asdict(x) for x in v]
assert sum(c.get('component_id')=='mesh:D010461' for b in bindings for c in by[b['owner_path']]['components'])==5
assert sum(c['component_name'].lower()=='peptone' and c['reference_scope']=='UNMAPPED' for b in bindings for c in by[b['owner_path']]['components'])==10
assert h(W/'data/ingredients/mapped/GYPS.yaml')==h(OLD/'negative-controls/GYPS.yaml')
put(S/'validation/guarded-focused.json',{'at':datetime.now(timezone.utc).isoformat(),'changed_targets':checks,'guarded_schema_passes':5,'unchanged_payloads_byte_identical':10,'component_partonomy_violations':0,'exact_parent_after_capture':pp['after_capture'],'overlay_scope':'In-memory baseline plus15children and exact direct Peptone target. Final complete successor overlay remains root-owned.','counts':{'generic_direct_MeSH_parts':5,'withdrawn_UNMAPPED_peptone_parts':10,'prior_claim_outcomes_preserved':20,'source_observations_preserved':130},'negative_controls':{'GYPS_unchanged':True,'no_retained_conditional_local_reference_in_15_selected_components':True,'no_ten_withdrawals_changed':True,'FAB_and_rumen_repairs_byte_identical':True},'maintained_writes':0,'no_full_owner_source_or_export_approval':True})
print(json.dumps({'parent_sha256':pp['after_capture']['sha256'],'changed_payloads':5,'unchanged_payloads':10,'proposals_sha256':h(S/'proposals.json'),'evidence_sha256':h(S/'evidence.json'),'case_deltas_sha256':h(S/'case-deltas.json'),'native_focused_violations':0},indent=2))
