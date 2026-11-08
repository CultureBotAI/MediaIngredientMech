from pathlib import Path
from datetime import datetime,timezone
import copy,hashlib,json,shutil,subprocess
import yaml
from mediaingredientmech.validation.write_validated import write_validated_ingredient

W=Path.cwd();C=W.parents[2];S=Path(__file__).resolve().parent;OLD=S.parent/'parents';B=W/'reports/all_unmatched_20261107/worker-05'
PUB='buffer-parts-v1/parents-direct-v1/';AT=datetime.now(timezone.utc).isoformat();AUTHOR='/root/buffer_hepes'
CID='KG_CASE:ba039f9e4a33baf69eb111ceb979cf6c9ad8fe788c13488f256336508ce94151';PID='W05-FINAL-MAT-039'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
objsha=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def write(name,d):
 p=S/name;assert not p.exists(),p;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def cp(a,b):
 assert not b.exists(),b;b.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a,b);assert sha(a)==sha(b)

assert sha(OLD/'MANIFEST.json')=='cad389701303a87ea2b7d0a59dd86d5b213d87e73a6cde9f6c1531a3f4500915'
for member in json.loads((OLD/'MANIFEST.json').read_text())['members']:assert sha(OLD/member['path'])==member['sha256']
coor=C/'preflight/polypeptone-owl-reassessment-v1'
assert sha(coor/'HANDOFF.json')=='ed4b490104249457bbb557767418eff3d19437aab459a5084cb91a2658c41663'
assert sha(coor/'MANIFEST.json')=='f9aa228a3dee456ec0da909a3ce1de0288e82aa00f89481527ed502d5c200b32'
for member in json.loads((coor/'MANIFEST.json').read_text())['members']:
 f=coor/member['path'];assert sha(f)==member['sha256'];cp(f,S/'input/coordinator-reassessment'/member['path'])
for n in ['HANDOFF.json','MANIFEST.json']:cp(coor/n,S/'input/coordinator-reassessment'/n)
for n in ['final/proposals.json','final/decisions.json','final/evidence-v2.json','final/case-deltas.json','input/frozen-cases.json','input/current-selected/Peptone.yaml','input/original-before/Peptone.yaml','proposed-v2/Peptone.yaml','proposed/Soy_Peptone.yaml']:
 cp(OLD/n,S/'input/sealed-parents'/n)
for name in ['mesh-D010461-nlm','mesh-M0016245-nlm','mesh-D010461-ols','mesh-D010461-browser','mesh-D011492-nlm','mesh-M0017860-nlm']:
 for suffix in ['.json','.receipt.json']:cp(OLD/'captures'/(name+suffix),S/'captures'/(name+suffix))
for name in ['thermo.pdf','thermo.pdf.receipt.json']:cp(OLD/'captures'/name,S/'captures'/name)
cp(OLD/'read/thermo.txt',S/'read/thermo.txt')

conclusion=(
 'Use the ordinary generic Peptone identity mesh:D010461 (Peptones) under MAPPING_SEMANTICS section3 exact-term and unspecified-sense priority. '
 'The active primary NLM descriptor explicitly supplies Peptone as an entry term and a conventional water-soluble partial protein-hydrolysis material definition, independently consistent with the manufacturer generic peptone description. '
 'The earlier requirement for a source-specific acid-or-enzyme/precipitation certificate was overstated: the general possibility of base hydrolysis does not establish a different actual preparation or sense for this unqualified owner. '
 'This is generic material identity, not identity with every supplier product or a newly verified assay preparation. '
 'The earlier FoodOn inference was also overstated: its actual member_of external category relation is not a has-role, food-use, regulatory-approval or lot-eligibility requirement, and the axiom alone does not refute a material broader mapping. '
 'The closer direct generic MeSH term, rather than that invented gate, determines the corrected identity choice. '
 'Retain all earlier evidence and histories as authentic superseded interpretation; preserve raw plural and rejected truncated label, occurrence statistics, provisional roles and all frozen source/owner/export holds. '
 'Five reviewed generic dependent references and the separate RCM reference must follow this actual identifier in independently authored source-specific successors; no global replacement, named-product merge or source-observation redirect is authorized.'
)
write('scientific-plan.json',dict(at=AT,author=AUTHOR,independent_agreement=True,current_selected_peptone_sha256=sha(OLD/'proposed-v2/Peptone.yaml'),native_basis='MAPPING_SEMANTICS section3 steps1/4 take precedence over fallback; exact generic material terminology is separate from unverified source-assay/supplier details.',conclusion=conclusion,source_facts=['NLM D010461 is active, label Peptones, entry term Peptone, preferred concept M0016245.', 'Manufacturer p7 describes generic peptones as water-soluble partial protein-hydrolysis products with variable source/process/product profiles.', 'The frozen two observations use unqualified peptones and do not establish a contrary actual preparation.', 'FoodOn official relations guide uses member_of for external product-category associations; OWL existential membership does not entail a has-role or classification of the source as the target itself.'],not_inferred=['No manufactured lot, specific enzyme, mammalian/vegetable origin, nutritional/clinical role, or whole-source assay identity is established.', 'The two MeSH descriptors are sibling entries under Proteins in the inspected tree; no MeSH subclass edge is invented.', 'No old evidence entry is retyped as human or rewritten.'],proposed_field_changes=['identifier: mesh:D010461','ontology_mapping.ontology_id: mesh:D010461','ontology_mapping.ontology_label: Peptones','ontology_mapping.ontology_source: MESH','ontology_mapping.mapping_quality: EXACT_MATCH','append three claim-specific LLM_SUGGESTION evidence objects','append one truthful correction event and current-scope notes'],unchanged=['Complete Soy payload and proposal object', 'Existing source-case membership and holds', 'Bacto tombstone continuity proposal and sealed parents201 files'],coordinator_receipt=dict(path='input/coordinator-reassessment/HANDOFF.json',sha256=sha(coor/'HANDOFF.json'),reviewer='/root/step7d_independent_review'),independent_final_review='Pending exact new payload and composed source decisions; the coordinator comparison is not whole-owner approval.'))

ps=json.loads((OLD/'final/proposals.json').read_text())['proposals'];ds=json.loads((OLD/'final/decisions.json').read_text())['decisions'];op=next(p for p in ps if p['proposal_id']==PID);r=yaml.safe_load((OLD/'proposed-v2/Peptone.yaml').read_text());before=copy.deepcopy(r)
r['identifier']='mesh:D010461';r['ontology_mapping'].update(ontology_id='mesh:D010461',ontology_label='Peptones',ontology_source='MESH',mapping_quality='EXACT_MATCH')
ne=[
 dict(evidence_type='LLM_SUGGESTION',source='https://id.nlm.nih.gov/mesh/D010461',notes='The complete active NLM Peptones descriptor, its explicit Peptone entry term and preferred concept M0016245 support the ordinary generic material identity. Under native section3, this supported unspecified sense takes precedence over a local fallback. The conventional partial-hydrolysis/solubility description does not create a new lot-specific assay gate when no different actual source preparation is established. This is not supplier-product or source-assay approval.'),
 dict(evidence_type='LLM_SUGGESTION',source='https://assets.thermofisher.com/TFS-Assets/BPD/brochures/peptones-supplements-feeds-technical-reference-guide.pdf',notes='Printed page7 independently identifies generic peptones as water-soluble partial protein-hydrolysis products while explaining variable feedstocks and product profiles. Mention of possible acid, base or enzyme processing is not positive evidence that the unqualified assigned owner denotes a different preparation from the ordinary MeSH Peptones sense. Earlier process/precipitation-gate inference is superseded; no numeric composition or role is imported.'),
 dict(evidence_type='LLM_SUGGESTION',source='https://foodon.org/design/foodon-relations/',notes='The official member_of guidance connects products to external product-type categories rather than asserting subclass identity in agency classifications. The verified FoodOn03315306 existential member_of axiom is real, but does not by itself impose food-use, has-role, regulatory approval or lot eligibility on a MIM material broader mapping. Earlier stronger negative applicability wording is retained historically and superseded here. Selection of direct generic mesh:D010461 follows the closer supported material term, not an invented FoodOn gate.')
]
r['ontology_mapping']['evidence'].extend(ne)
r['curation_history'].append(dict(timestamp=AT,curator='Codex /root/buffer_hepes; W05 direct generic Peptone reassessment',action='CORRECTED_GENERIC_PEPTONE_IDENTITY',changes=conclusion+' Isolated guarded successor; no maintained or downstream application.',previous_status=r['mapping_status'],new_status=r['mapping_status'],llm_assisted=True,llm_model='gpt-6'))
r['notes']+='\n\nDirect generic Peptone reassessment, superseding earlier broader-only and eligibility-gate interpretations while preserving their history: '+conclusion+' Exact successor independent review remains required.'
dest=S/'proposed/Peptone.yaml';assert not dest.exists();write_validated_ingredient(r,dest);assert yaml.safe_load(dest.read_text())==r
assert r['curation_history'][:-1]==before['curation_history'] and r['ontology_mapping']['evidence'][:-len(ne)]==before['ontology_mapping']['evidence']
changed=[k for k in set(r)|set(before) if r.get(k)!=before.get(k)];assert set(changed)=={'identifier','ontology_mapping','curation_history','notes'}

# Ignore-independent whole current-tree and selected-proposal primary-ID checks; no universal absence claim.
target='mesh:D010461';maintained=[]
for f in sorted((W/'data/ingredients').rglob('*.yaml')):
 x=yaml.safe_load(f.read_text()) or {}
 if str(x.get('identifier','')).casefold()==target.casefold():maintained.append(dict(path=str(f.relative_to(W)),sha256=sha(f),mapping_status=x.get('mapping_status')))
core=json.loads((B/'tellurium-polypeptone-v1/core/proposals.json').read_text())['proposals'];current=[]
for p in core:
 f=B/p['after_capture']['path'];assert sha(f)==p['after_capture']['sha256'];x=yaml.safe_load(f.read_text())
 if str(x.get('identifier','')).casefold()==target.casefold():current.append(dict(proposal_id=p['proposal_id'],owner_path=p['owner_path'],capture=p['after_capture']))
assert not maintained and not current
inv=C/'preflight/soy-identifier-dependency-preflight-v1/committed-selection-inventory.json';inventory=json.loads(inv.read_text());ih=[x for x in inventory['payloads'] if str(x.get('identifier','')).casefold()==target.casefold()];assert not ih
write('owner-search.json',dict(at=AT,author=AUTHOR,target=target,ignored_files_included=True,maintained_count=len(list((W/'data/ingredients').rglob('*.yaml'))),maintained_hits=maintained,current_W05_selected_count=len(core),current_W05_selected_hits=current,coordinator_inventory=dict(path=str(inv),sha256=sha(inv),selected_payloads=len(inventory['payloads']),hits=ih),limit='Current W05 maintained tree and exact named proposal selectors; root checks later advancing heads and final composed overlays.'))

evidence=[]
for eid,f,kind,locator,support,url,access in [
 ('W05-DIRECT-PEPTONE-NLM-DESCRIPTOR',S/'captures/mesh-D010461-nlm.json','ontology','Full active NLM descriptor, preferred concept pointer and Peptone term.','Supports ordinary generic descriptor identity; not a product, lot or assay approval.','https://id.nlm.nih.gov/mesh/D010461',json.loads((S/'captures/mesh-D010461-nlm.receipt.json').read_text())['accessed_at']),
 ('W05-DIRECT-PEPTONE-NLM-CONCEPT',S/'captures/mesh-M0016245-nlm.json','ontology','Full primary preferred concept M0016245 and conventional material scope.','Generic partial protein-hydrolysate sense; no new lot-specific precipitation certificate required.','https://id.nlm.nih.gov/mesh/M0016245',json.loads((S/'captures/mesh-M0016245-nlm.receipt.json').read_text())['accessed_at']),
 ('W05-DIRECT-PEPTONE-THERMO',S/'captures/thermo.pdf','primary_source','Manufacturer guide printed page7; full exact PDF preserved.','Independent generic material description, variable product profiles, no contrary actual assigned preparation.','https://assets.thermofisher.com/TFS-Assets/BPD/brochures/peptones-supplements-feeds-technical-reference-guide.pdf',json.loads((S/'captures/thermo.pdf.receipt.json').read_text())['accessed_at']),
 ('W05-DIRECT-PEPTONE-FOODON-RELATIONS',S/'input/coordinator-reassessment/captures/web-foodon-nlm-response.json','primary_source','Exact successful web response; FoodOn relations member_of row and full primary NLM source extracts.','External category membership is not a food-use, has-role or lot gate.','https://foodon.org/design/foodon-relations/',None),
 ('W05-DIRECT-PEPTONE-OWL-SEMANTICS',S/'input/coordinator-reassessment/captures/web-w3c-semantics-response.json','primary_source','Exact successful W3C primary web response, class-expression and subclass semantics.','Existential member relation does not itself assert source membership in filler class or a has-role.','https://www.w3.org/TR/owl2-direct-semantics/',None),
 ('W05-DIRECT-PEPTONE-COORDINATOR-REASSESSMENT',S/'input/coordinator-reassessment/HANDOFF.json','source_snapshot','Sealed full coordinator reassessment, 35 manifest members rehashed.','Independent terminology comparison by /root/step7d_independent_review; not source-case, candidate or release approval.',None,None),
 ('W05-DIRECT-PEPTONE-SCIENCE',S/'scientific-plan.json','source_snapshot','Current independent author reasoning and explicit correction of earlier overstatement.','One Peptone identity successor; Soy and tombstone remain unchanged.',None,None),
 ('W05-DIRECT-PEPTONE-OWNER-SEARCH',S/'owner-search.json','source_snapshot','All maintained records and specified exact selectors; ignored files included.','No competing primary mesh:D010461 found in this bounded scan; no owner merge.',None,None)
]:
 e=dict(evidence_id=eid,capture=dict(root='artifact',path=PUB+str(f.relative_to(S)),sha256=sha(f)),kind=kind,locator=locator,supports_or_contradicts=support,case_ids=[CID],url=url)
 if access:e['accessed_at']=access
 if eid in ['W05-DIRECT-PEPTONE-FOODON-RELATIONS','W05-DIRECT-PEPTONE-OWL-SEMANTICS']:e['original_capture_attribution']=dict(reviewer='/root/step7d_independent_review',successful_web_response_absolute_retrieval_time='not recorded in response; not inferred from separate failed shell receipt',current_assessor=AUTHOR)
 if eid=='W05-DIRECT-PEPTONE-THERMO':e['original_capture_attribution']=dict(author='/root/polypeptone_supplement',reused_exact_bytes_and_original_time=True)
 evidence.append(e)
eids=[e['evidence_id'] for e in evidence]
np=copy.deepcopy(op);np['direct_term_predecessor_capture']=copy.deepcopy(op['after_capture']);np['direct_term_predecessor_description']=op['description'];np.update(description=conclusion,after_capture=dict(root='artifact',path=PUB+'proposed/Peptone.yaml',sha256=sha(dest)),direct_term_successor_author=AUTHOR,direct_term_successor_at=AT,identity_consequence='Existing ordinary generic Peptone owner uses mesh:D010461. Supplier-specific products, source assay materials and raw organism observations retain their own boundaries and holds.',predicate_consequence='Native single exactMatch mesh:D010461 replaces prior broader Protein Hydrolysates plus local registry rows. Source-specific five generic child references and RCM require separately authored exact-identifier continuity; no global retarget.',independent_review=dict(status='pending exact direct-term successor and full composed source decision; previous reviews remain historical',evidence_ids=[]))
np['evidence_ids']=list(dict.fromkeys(op['evidence_ids']+eids));outps=[np if p['proposal_id']==PID else copy.deepcopy(p) for p in ps]
newds=[];deltas=[]
for d in ds:
 nd=copy.deepcopy(d)
 if d['case_id']==CID:
  nd['reasoning']='The ordinary generic Peptone owner is supported as exact mesh:D010461 Peptones under native section3. NLM explicitly supplies Peptone and its conventional partial-hydrolysate material definition, independently consistent with the manufacturer generic description. Earlier process/precipitation and FoodOn use-gate interpretations were overstated; no actual contrary assigned preparation is established. Exact generic identity does not determine either frozen source assay supplier or approve its organism role. Preserve both observations, plural/raw provenance, truncated-token rejection, all source/role/owner/export holds and separately authored component dependencies.'
  nd['parents_direct_reassessment']=dict(author=AUTHOR,at=AT,status='primary complete; exact final independent review pending',predecessor_decision_sha256=objsha(d),selected_proposal_id=PID,primary_identifier='mesh:D010461',ontology_id='mesh:D010461',ontology_label='Peptones',mapping_quality='EXACT_MATCH',supersedes_fields=['parents_reassessment.selected_parent','parents_reassessment.selected_mapping_quality','parents_reassessment.primary_identifier','parents_reassessment.direct_exact_term_assessed','parents_reassessment.conclusion'],prior_interpretations_preserved=True,correction_of_overstatement='The ordinary generic source sense is supported without new lot-specific process/precipitation evidence; FoodOn external membership is not a food-use or role gate.',source_case_and_occurrence_membership_unchanged=True,all_inherited_holds_unchanged=True,dependent_reference_scope='Only separately reviewed five generic child components and RCM against actual final identifier; root authors and reviews those successors.',new_owner_or_release_approval=False)
  nd['evidence_ids']=list(dict.fromkeys(d['evidence_ids']+eids))
  fields={k:nd[k] for k in nd if nd.get(k)!=d.get(k)};assert set(fields)=={'reasoning','parents_direct_reassessment','evidence_ids'}
  deltas.append(dict(case_id=CID,base_decision_sha256=objsha(d),changed_fields=fields,additive_arrays=['evidence_ids'],all_earlier_case_fields_preserved=True))
 newds.append(nd)
assert next(p for p in outps if p['proposal_id']=='W05-FINAL-MAT-032')==next(p for p in ps if p['proposal_id']=='W05-FINAL-MAT-032')
assert next(d for d in newds if d['case_id']!=CID)==next(d for d in ds if d['case_id']!=CID)
write('proposals.json',dict(schema_version=1,proposals=outps));write('decisions.json',dict(schema_version=1,decisions=newds));write('evidence.json',dict(schema_version=1,evidence=evidence));write('case-deltas.json',dict(schema_version=1,author=AUTHOR,base_selected_decisions=dict(path='buffer-parts-v1/parents/final/decisions.json',sha256=sha(OLD/'final/decisions.json')),deltas=deltas))
write('author-receipt.json',dict(at=AT,author=AUTHOR,base_head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),prior_sealed_parent_manifest=sha(OLD/'MANIFEST.json'),coordinator_handoff_sha256=sha(coor/'HANDOFF.json'),changed_payloads=1,carried_unchanged_payloads=1,source_cases=2,new_source_cases=0,proposal_id=PID,authentic_before=op['before_capture'],predecessor_capture=op['after_capture'],after_capture=np['after_capture'],changed_top_level_fields=sorted(changed),prior_history_events_preserved=len(before['curation_history']),new_history_events=1,prior_evidence_objects_preserved=len(before['ontology_mapping']['evidence']),new_mapping_evidence_types=[x['evidence_type'] for x in ne],all_other_fields_unchanged=True,soy_proposal_and_source_decision_unchanged=True,tombstone_packet_unchanged=True,independent_final_review_pending=True))
print(json.dumps(dict(after_capture=np['after_capture'],new_evidence=len(evidence),unchanged_Soy=True),indent=2))
