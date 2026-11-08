#!/usr/bin/env python3
"""Isolated author proposals for BIO-F02/F03/F04/F05/F08; never edits inputs."""
import copy, csv, dataclasses, datetime, difflib, hashlib, json, pathlib, subprocess, sys, time
import yaml
sys.path.insert(0, str(pathlib.Path('src').resolve()))
from mediaingredientmech.validation.write_validated import write_validated_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy

A=pathlib.Path('reports/all_unmatched_20261107/worker-10')
O=A/'successor-v3/serums'
P=pathlib.Path('.temp/all-unmatched-worker-10/successor-v3/serums')
C=pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
Q=C/'queue/preliminary-v5'
W=C/'workers/w05/worktree'
T=W/'.temp/final-preparation-comparison-v1'
CM=pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/CultureMech')
start=datetime.datetime.now(datetime.timezone.utc).isoformat(); tick=time.monotonic()
def sha(b): return hashlib.sha256(b).hexdigest()
def canon(j): return sha(json.dumps(j,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode())
def read(p): return json.loads(p.read_text())
def write(name,j):
 p=O/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(j,indent=2,ensure_ascii=False)+'\n');return p
def binding(p): return {'path':str(p),'sha256':sha(p.read_bytes())}
def artifact(p):return {'root':'artifact','path':str(p.relative_to(A)),'sha256':sha(p.read_bytes())}

selected=read(P/'selected.json'); oldps=read(A/'successor-v2/proposals.json')['proposals'];oldDs=read(A/'successor-v2/decisions.json')['decisions'];oldEs=read(A/'successor-v2/evidence.json')['evidence'];byE={e['evidence_id']:e for e in oldEs}
scope=[19,28,40,42,53,61,98,105,109,129,158,181]
ds=[copy.deepcopy(d) for d in oldDs if d['source_index'] in scope];cases=read(Q/'shards/shard-10.json')['cases'];bycase={d['source_index']:d for d in ds};cid=lambda i:bycase[i]['case_id']
newE=[];newP=[];bridges=[];diffs=[];claims=[];checks=[];allnewrecords=[]

# Exact frozen cases, all recipe bodies, component paths and original occurrence IDs.
context=[]
for d in ds:
 i=d['source_index'];case=cases[i];assert canon(case)==d['case_input_sha256'];occs=[]
 for occ in case.get('occurrences',[]):
  fp=Q/occ['full_recipe_snapshot'];b=fp.read_bytes();assert sha(b)==occ['source_file_sha256'];full=yaml.safe_load(b)
  cur=full
  for bit in occ['component_path'].split('/'):cur=cur[int(bit)] if isinstance(cur,list) else cur[bit]
  assert cur==occ['raw_component']
  occs.append({'occurrence_id':occ['occurrence_id'],'component_path':occ['component_path'],'snapshot':binding(fp),'full_recipe':full,'raw_component':cur})
 context.append({'source_index':i,'case':case,'case_canonical_sha256':canon(case),'selected_decision_before':d,'selected_decision_before_canonical_sha256':canon(d),'full_frozen_occurrences':occs})
write('source-contexts.json',{'cases':context,'case_count':len(context),'occurrence_count':sum(len(x['full_frozen_occurrences']) for x in context)})

# Context reports are attributed comparisons, never substituted for primary evidence.
refs=[A/'successor-v3/inputs/issue1237-live.json',C/'preflight/family-findings-triage-v1/findings-matrix-v2.json',C/'preflight/family-findings-triage-v1/current-origin-byte-check.json',C/'preflight/family-findings-triage-v1/bio-primary-index.json',C/'preflight/family-findings-triage-v1/w05-owner-continuity-readback.json',T/'primary-biologicals/comparison-v2.json',T/'primary-biologicals/findings-v1.json',T/'primary-biologicals/unresolved-options-v3.json',T/'primary-biologicals/evidence-v1.json',T/'skeptical-review/final-scientific-review.json',pathlib.Path('MAPPING_SEMANTICS.md'),pathlib.Path('.claude/skills/add-media/SKILL.md'),pathlib.Path('.claude/skills/manage-identifiers/SKILL.md'),pathlib.Path('docs/record-reviews.md')]
refbindings=[binding(p) for p in refs]
comparison=read(T/'primary-biologicals/comparison-v2.json');opts=read(T/'primary-biologicals/unresolved-options-v3.json');entry_ids={893,904,906,908,914,916,919,922,970,971}
write('prior-review-context.json',{'bindings':refbindings,'selected_entry_assessments':[x for x in comparison['entry_assessments'] if x['entry_index'] in entry_ids],'relevant_unresolved_pair_options':[x for x in opts['unresolved_pairs'] if entry_ids.intersection(x['entry_indices'])],'attribution':'W05 primary-biologicals and its separate materials_research skeptic; comparison context, not inherited approval. This successor scientist is /root/buffers_research, not the original biological/KG serum author. Prior worker10 broad integration audits included payload hashes; they are not independent approval of these new corrections.'})

# Reuse original primary captures exactly, with actual original access times.
primary_index=read(P/'read-index.json')
for eid in ['bio-primary-ed74f668f50cd885','bio-primary-c99e9f1a3c385f8f']:
 e=byE[eid];assert sha((A/e['capture']['path']).read_bytes())==e['capture']['sha256']
 primary_index.append({'id':eid,'url':e['url'],'time':e['accessed_at'],'capture':e['capture'],'use':'Calf whole-owner contextual audit; DSM1245 inactivated calf versus MediaDive derived fetal wording retained separately, not recertified as equivalent.'})
write('reused-primary-bindings.json',{'bindings':primary_index,'policy':'Existing bytes remain at original artifact paths. Accessed_at is original retrieval time, not a new fetch. Read derivatives are private only.'})
for e in read(P/'reused-w05-primary.json'):
 name=pathlib.Path(e['path']).name;p=O/'captures'/name;assert sha(p.read_bytes())==e['sha256']
 indices=[109] if 'spiroplasma' in name else [19,28]
 newE.append({'evidence_id':'sv3-serums-'+e['evidence_ref'].lower(),'kind':'primary_source','url':e['url'],'accessed_at':e['accessed_at'],'capture':artifact(p),'locator':e['locator'],'supports_or_contradicts':('Current ATCC source version explicitly reformulated MD2611; new product and 55 C protocol cannot be backfilled into frozen M2578.' if indices==[109] else 'Supplier capture supports bounded product/process context; gamma and heat are compatible. It does not establish historical10109-155 heat status.'),'case_ids':[cid(i) for i in indices],'capture_reuse':{'original_worker':'W05 primary-biologicals','original_evidence_ref':e['evidence_ref'],'original_path':str(W/e['path']),'original_sha256':e['sha256'],'metadata_capture':artifact(O/'captures'/pathlib.Path(e['metadata_path']).name),'no_new_retrieval_claim':True}})
for e in read(O/'primary-retrievals.json'):
 assert e['exit_code']==0 and e['http_status']=='200'
 newE.append({'evidence_id':'sv3-serums-primary-'+e['name'],'kind':'primary_source','url':e['url'],'accessed_at':e['accessed_at'],'capture':e['capture'],'locator':'Complete primary recipe including material rows and instructions.','supports_or_contradicts':('M2240 literal calf serum(Gibco) lacks catalog/heat protocol; derived GMO heat-inactivated label is not the missing supplier/source bridge.' if e['name']=='togo-m2240' else 'DSM78d explicitly permits fetal OR newborn calf serum; it cannot be globally narrowed to JCM1303 heat-inactivated serum.'),'case_ids':[cid(158)]})

# Recheck ignored-inclusive maintained owner/alias universe and preserve exact baselines.
cmd=['rg','--no-ignore','--hidden','-l','-i','serum','data/ingredients'];r=subprocess.run(cmd,capture_output=True,text=True);assert r.returncode==0
owners=[]
for s in r.stdout.splitlines():
 p=pathlib.Path(s)
 if p.suffix not in ('.yaml','.yml'):continue
 b=p.read_bytes();j=yaml.safe_load(b);owners.append({'path':str(p),'sha256':sha(b),'record':j})
write('owner-lookup.json',{'command':cmd,'exit_code':r.returncode,'ignored_files_included':True,'scope':'Maintained per-record surfaces; all matching complete records parsed. No absence claim about outside-maintained private proposals.','owners':owners})

# Read complete current local counterpart records, separately from historical source tree.
audit=read(O/'calf-owner-occurrence-audit.json')
for row in audit['current_local_selected_rows']:
 p=CM/'data/normalized_yaml'/row['source_path'];b=p.read_bytes();j=yaml.safe_load(b);dest=O/'captures'/('cm-current-'+p.name);dest.write_bytes(b)
 row['full_current_recipe_capture']=artifact(dest);row['full_current_recipe']=j
historical_failure=subprocess.run(['git','-C',str(CM),'show','15a4da5c08:output/ingredient_occurrences.tsv'],capture_output=True,text=True)
audit['historical_generated_table_attempt']={'command':['git','-C',str(CM),'show','15a4da5c08:output/ingredient_occurrences.tsv'],'exit_code':historical_failure.returncode,'stderr':historical_failure.stderr}
audit['assessment']={'historical_exact_label_records':len(audit['historical_records']),'current_local_rows':len(audit['current_local_selected_rows']),'source_groups':[
 {'source':'JCM1303 / MD2061','historical_recipes':['CultureMech:002467','CultureMech:014364'],'primary_evidence_ids':['kg-md2061','kg-medium_J1303','sv1-kg-jcm-1303'],'conclusion':'Authentic owner creation source; heat-inactivated calf serum and filter-sterilized addition. Schedule, exact developmental subclass and supplier unstated.'},
 {'source':'CCAP C49/C50','historical_recipes':['CultureMech:000359','CultureMech:000361','CultureMech:014768','CultureMech:014888'],'primary_evidence_ids':['bio-primary-4f3e58e1079577a9','bio-primary-449dcf117e8bc4b8'],'conclusion':'Literal calf rows lose positive fetal, sterile, gamma-irradiated Invitrogen10109-155 specification. Candidate occurrence routing can use these primary facts, but full Bovine_Calf_Serum must not be narrowed wholesale.'},
 {'source':'DSM78d','historical_recipes':['CultureMech:001930','CultureMech:014442'],'primary_evidence_ids':['sv3-serums-primary-dsmz78d'],'conclusion':'Fetal OR newborn disjunction. The selected option for each historical use is not established. Do not assign JCM1303 treatment or a single developmental age.'},
 {'source':'TOGO M2240','historical_recipes':['CultureMech:008829'],'primary_evidence_ids':['sv3-serums-primary-togo-m2240'],'conclusion':'Raw calf serum(Gibco),1%v/v, no catalog or heat protocol. Derived GMO label says heat-inactivated, but cannot alone establish exact JCM1303 supplied preparation.'},
 {'source':'Current local KOMODO1245 and1245_18691','current_recipes':['CultureMech:004002','CultureMech:004003'],'primary_evidence_ids':['bio-primary-ed74f668f50cd885','bio-primary-c99e9f1a3c385f8f'],'conclusion':'Additional current local rows, absent from the historical exact-label reconstruction. Current normalized records keep calf99.70 separate from heat-inactivated fetal100.00; they do not license a global JCM1303 narrowing. DSM1245 explicitly inactivated calf without heat mechanism; do not infer untreated or heat method.'}],
 'recommendation':'Retire the isolated parallel JCM1303 new-owner proposal from active selection now. Preserve source MD2061 and known preparation at case158 as supported evidence. Owner reconciliation requires an explicit occurrence partition with ambiguous DSM78d option and Gibco product bridge retained; no missing heat schedule blocks naming the material itself.',
 'options':['Preserve the broad existing owner and attach occurrence-specific heat/filter facts without claiming separate ingredient identity; requires a supported occurrence/annotation representation and binding review.','After an explicit source/occurrence partition, reconcile the authentic MD2061 lineage through the existing owner, preserving every broader/Gibco history/alias and routing excluded occurrences separately.','If a curator establishes distinct material identities, prepare a separately reviewed split with complete history/occurrence bridges; do not treat missing metadata as proof.'],
 'missing_facts':['Which fetal/newborn choice applies to each DSM78d occurrence.','Gibco product/catalog/protocol and source applicability for M2240; no arbitrary mapping from its derived GMO label.','Reviewed owner boundary and exact routing of JCM1303, CCAP, DSM78d, Gibco and later KOMODO occurrences; existing eight-count is historical, not an authorization to discard later/source-specific uses.']}
write('calf-owner-occurrence-audit.json',audit)

def add_ev(eid,path,kind,support,indices):
 newE.append({'evidence_id':eid,'kind':kind,'capture':artifact(O/path),'url':None,'locator':'Complete artifact; exact per-case bindings retained.','supports_or_contradicts':support,'case_ids':[cid(i) for i in indices]})
add_ev('sv3-serums-contexts','source-contexts.json','source_snapshot','Original complete cases and all23 full frozen recipe contexts, canonical and byte hashes verified.',scope)
add_ev('sv3-serums-owner-lookup','owner-lookup.json','source_snapshot','Ignored-inclusive current maintained owner/alias lookup, exact complete owner bytes and history.',scope)
add_ev('sv3-serums-calf-occurrence-audit','calf-owner-occurrence-audit.json','source_snapshot','Whole known Bovine_Calf_Serum/Gibco occurrence scope; historical tree and current local table kept distinct, source-bound mixed contexts prevent wholesale narrowing or parallel same-source owner.',[158])
add_ev('sv3-serums-prior-context','prior-review-context.json','source_snapshot','Exact attributed issue1237/W05 findings/options/skeptic context, not scientific or publication approval.',scope)

fixes={
 'sv1-bio-gamma_irradiated_fetal_calf_serum_10109_155':('BIO-F04','This product is distinct from heat-treated FBS.','Heat-treatment status of the historical10109-155 product is not specified. Gamma irradiation does not exclude heat treatment; compatibility with another preparation remains unresolved without a product/process bridge.'),
 'sv1-bio-filtered_rabbit_serum_56c_30min_jcm946':('BIO-F05','heated56C30min and prior filter sterilization.','heated56C30min and filter sterilization before addition to the cooled base. The relative order of heating and filtration is not stated.'),
 'sv1-bio-newborn_calf_serum_komodo1021':('BIO-F05','linked DSMZ1021 permits fetal OR newborn, without overriding the selected newborn row.','linked DSMZ1021 requires sterile fetal OR newborn serum, without overriding the selected newborn row. Sterility is retained for this selected newborn preparation; no particular sterilization method or heat schedule is inferred.'),
 'sv1-bio-sterile_bovine_serum_56c_45min_dsmz840':('BIO-F04','The age remains unspecified; this is not fetal serum.','Developmental age remains unspecified and therefore does not exclude fetal serum. The explicit56C45min protocol differs from explicit56C30min and56C60min protocols; an unstated schedule does not establish a difference.'),
 'sv1-bio-heat_inactivated_fbs_atcc1827':('BIO-F04','Treatment schedule is unstated and remains distinct from separately documented30/60minute products.','Treatment schedule is unstated; the relationship to preparations with explicit30/45/60minute schedules remains unresolved. Absence of a schedule proves neither equality nor difference.'),
 'sv1-bio-horse_serum_56c_30min_atcc243':('BIO-F04','This treatment-specific preparation is distinct from active/filter-only equine serum and from unknown-schedule products.','The explicit heat-inactivated state is retained and differs from an explicitly active state. Filtration alone and missing heat schedules do not establish non-heat treatment or a different preparation; those relationships remain unresolved.'),
 'sv1-bio-fetal_bovine_serum_56c_60min_m2964':('BIO-F04','the one-hour process remains distinct from30minute and unknown-schedule FBS.','the explicit56C60minute process differs from explicit56C30minute and56C45minute processes. Preparations with unstated heat schedules may overlap; their exact relationship remains unresolved.')}
version_note='Source-version boundary: this candidate applies only to the fetal option in frozen TOGO M2578 (original primary capture2026-11-08T05:07:01.392375+00:00, SHA256338404e0a53706393f5e37a882b4c66001800a343ab21515fdc28691b6e0f684). That version permits newborn calf serum instead and does not specify a heat schedule. The same linked ATCC0988 URL captured2026-11-08T06:50:20.343881+00:00 (SHA2560233e1b2ca08c89365c67ce6e8e01f2a0d9fa3e20a45c91dc95363feb3c10c9a) explicitly says reformulated as MD2611, names ATCC30-2020, and instructs55C for1hour plus15minutes warmup. Its additive solution is filter sterilized. These current positive facts are not backfilled into the older TOGO material; applying this owner to the current version requires a reviewed version/product/protocol bridge. The frozen transcription is not declared false.'
swine_note='Reconcile the authentic MediaDive ingredient960 lineage through existing Swine_Serum/UNMAPPED_0536. MediaDive lists1076b, and DSMZ1076b names heat-inactivated swine serum17ml separately from fetal bovine serum. The17ml is a receiving-medium dose, not a stock concentration. Heating temperature/time and supplier remain unstated. All original owner history is preserved. The separate Porcine_Serum/MD967 record is not declared untreated, merged or repurposed; the relationship of its unspecified processing to this preparation remains unresolved.'
common_hold='Source-qualified naming is not proof of a distinct preparation. Preserve unresolved cross-source relationships and evaluate a common named partial scope or exact product/protocol bridge before simultaneous installation. No role/export or whole-owner approval; all inherited holds remain.'
calf_old='sv1-kg-calf-serum1303'; replacements={}; guard=[]

def replace_strings(obj,old,new):
 if isinstance(obj,str):return obj.replace(old,new)
 if isinstance(obj,list):return [replace_strings(v,old,new) for v in obj]
 if isinstance(obj,dict):return {k:(v if k=='curation_history' else replace_strings(v,old,new)) for k,v in obj.items()}
 return obj

for orig in selected:
 pid=orig['proposal_id'];before=copy.deepcopy(orig);fp=A/orig['after_capture']['path'];b=fp.read_bytes();assert sha(b)==orig['after_capture']['sha256'];r=yaml.safe_load(b)
 related=[d['source_index'] for d in ds if pid in d['proposal_ids']]
 if pid==calf_old:
  claim=copy.deepcopy(r['ontology_mapping']['evidence'][0]);claims.append({'old_proposal_id':pid,'new_proposal_id':None,'pointer':'/ontology_mapping/evidence/0','before_claim':claim,'before_claim_sha256':canon(claim),'after_claim':None,'after_claim_sha256':None,'correspondence':'Claim and original bytes preserved historically; parallel proposal retired from active selection, no replacement MappingEvidence authored.'})
  bridges.append({'old_proposal_id':pid,'old_proposal_object_sha256':canon(orig),'old_payload':orig['after_capture'],'case_ids':orig['case_ids'],'source_indices':related,'status':'retired_from_active_selection_no_replacement','new_proposal_id':None,'reason':'BIO-F03 authentic MD2061 owner continuity and demonstrated broader mixed occurrence scope; retain supported JCM1303 preparation facts without a silently installable duplicate.','prerequisites':audit['assessment']['missing_facts'],'options':audit['assessment']['options'],'old_artifacts_preserved':True})
  replacements[pid]=None;continue
 np=copy.deepcopy(orig);newpid='sv3-serums-'+pid.replace('sv1-bio-','').replace('sv1-kg-','');np['proposal_id']=newpid;replacements[pid]=newpid
 finding='BIO-F08' if 'spiroplasma' in pid else 'BIO-F02' if 'swine' in pid else fixes[pid][0]
 oldrecord=copy.deepcopy(r);oldclaim=copy.deepcopy(r['ontology_mapping']['evidence'][0])
 if pid in fixes:
  _,old,new=fixes[pid];assert old in np['description'];np=replace_strings(np,old,new);r=replace_strings(r,old,new)
  r['ontology_mapping']['evidence'][0]['evidence_type']='LLM_SUGGESTION'
  if 'newborn_calf' in pid:r['preferred_term']='Sterile newborn calf serum (KOMODO1021 selected variant; DSMZ1021)'
 elif 'spiroplasma' in pid:
  np['description']+=' '+version_note;r['notes']+=' '+version_note
  r['ontology_mapping']['evidence'].append({'evidence_type':'LLM_SUGGESTION','source':'https://www.atcc.org/~/media/D078A95CAFED4ADE877F47632F4E2EB5.ashx','notes':version_note+' This is version provenance, not exact ontology identity.'})
 else:
  owner=pathlib.Path('data/ingredients/unmapped/Swine_Serum.yaml');r=yaml.safe_load(owner.read_bytes());oldrecord=copy.deepcopy(r)
  r['identifier']=oldclaim_id= yaml.safe_load(b)['identifier'];r['preferred_term']='Heat-inactivated swine serum (DSMZ1076b; MediaDive960)';r['mapping_status']='MAPPED'
  r['ontology_mapping']={'ontology_id':r['identifier'],'ontology_label':r['preferred_term'],'ontology_source':'kgmicrobe.ingredient','mapping_quality':'FALLBACK_REGISTRY','evidence':[{'evidence_type':'LLM_SUGGESTION','source':'https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1076b.pdf','notes':swine_note}]}
  r['supplied_form']=[{'name':'Heat-inactivated swine serum (DSMZ1076b)','form':'heat-inactivated serum','notes':swine_note}]
  r['notes']+=' '+swine_note+' The inherited raw Swine serum synonym is preserved as genuine source history, not newly certified as a universal heat-inactivated alias. Application and export are held pending source-specific owned-name/routing review; do not silently activate this broader label.'
  np.update({'kind':'edit_existing_owner','owner_path':str(owner),'before_sha256':sha(owner.read_bytes()),'destination_path':'data/ingredients/mapped/Swine_Serum.yaml','description':swine_note,'identity_consequences':'Promote existing UNMAPPED_0536 through authentic MD960 lineage, preserving original stem/history and the prior isolated candidate local identity. No second owner and no Porcine_Serum merge.','predicate_consequences':'FALLBACK_REGISTRY only; no exact external serum equivalence.'})
  np['publication_holds']=np.get('publication_holds',[])+['APPLICATION/EXPORT HOLD: inherited raw Swine serum label remains unchanged; review its broader resolving scope and source-specific owner routing before applying promotion or enabling global resolution.']
  np['cross_partition_binding']='Historical bio53/KG181 shared DSMZ1076b association is retained. The new existing-owner promotion and its exact bytes require new independent review; original reviews do not transfer.'
 r['notes']+=' '+common_hold
 history=copy.deepcopy(r.get('curation_history',[]));r.setdefault('curation_history',[]).append({'timestamp':start,'curator':'worker10_successor_v3_serums_Codex_root_buffers_research','action':'CORRECTED' if finding!='BIO-F02' else 'PROMOTED','changes':finding+' source-bound successor correction: '+np['description']+' Prior isolated proposal '+pid+' remains immutable; this event records proposal authorship only. Earlier history is retained verbatim, including superseded wording.','previous_status':'UNMAPPED' if finding=='BIO-F02' else 'MAPPED','new_status':'MAPPED','llm_assisted':True})
 assert r['curation_history'][:-1]==history
 dest=O/'proposed_owners'/('Swine_Serum.yaml' if finding=='BIO-F02' else pathlib.Path(orig['owner_path']).name)
 write_validated_ingredient(r,dest);assert yaml.safe_load(dest.read_bytes())==r
 np['after_capture']=artifact(dest);np['supersedes']={'proposal_id':pid,'proposal_object_sha256':canon(orig),'payload':orig['after_capture'],'selected_core':'successor-v2/proposals.json','reason':finding,'replace_selected_proposal_not_add_second_owner':True}
 np['publication_holds']=np.get('publication_holds',[])+[common_hold]
 relevantE=['sv3-serums-contexts','sv3-serums-owner-lookup','sv3-serums-prior-context']+[e['evidence_id'] for e in newE if e['kind']=='primary_source' and set(e.get('case_ids',[])).intersection(np['case_ids'])]
 np['evidence_ids']=list(dict.fromkeys(np['evidence_ids']+relevantE));np['independent_review']={'status':'pending','evidence_ids':[]}
 np['source_reassessment']={'finding':finding,'authorship':'Codex /root/buffers_research; source successor author, not independent skeptic of these bytes','selected_scope':'bounded_proposal_with_publication_holds','original_cases_retained':np['case_ids'],'all_case_occurrences_retained':{d['case_id']:d['occurrence_ids'] for d in ds if d['case_id'] in np['case_ids']}}
 np['applicable_occurrence_ids']=(['CM_OCC:dbf4dd5af4921d5dd1386bf0f37c43a46f50e5c478dc37f276666f67103855c5'] if finding=='BIO-F08' else [oid for d in ds if d['case_id'] in np['case_ids'] for oid in d['occurrence_ids']])
 np['source_reassessment']['occurrence_scope_note']='All-case occurrence preservation is separate from this proposal admitted subset. Other case109 source families remain bound only to their unchanged original proposals.' if finding=='BIO-F08' else 'All listed original source occurrences support this bounded material; KG source cases have no fabricated CM occurrence IDs.'
 newP.append(np);allnewrecords.append(r);guard.append({'proposal_id':newpid,'after_capture':np['after_capture'],'guarded_write':'PASS','readback_equal':True,'history_prefix_preserved':True})
 bridges.append({'old_proposal_id':pid,'old_proposal_object_sha256':canon(orig),'old_payload':orig['after_capture'],'case_ids':orig['case_ids'],'source_indices':related,'status':'superseded_by_bounded_successor','new_proposal_id':newpid,'new_payload':np['after_capture'],'old_artifacts_preserved':True,'finding':finding})
 diffs.append({'old_proposal_id':pid,'new_proposal_id':newpid,'payload_before':orig['after_capture'],'maintained_preimage':binding(pathlib.Path(np['owner_path'])) if finding=='BIO-F02' else None,'payload_after':np['after_capture'],'literal_yaml_diff':''.join(difflib.unified_diff(b.decode().splitlines(True),dest.read_text().splitlines(True),fromfile=str(fp),tofile=str(dest))),'semantic_before_record':oldrecord,'semantic_after_record':r})
 for n,claim in enumerate(r['ontology_mapping']['evidence']):
  previous=oldclaim if n==0 else None
  claims.append({'old_proposal_id':pid,'new_proposal_id':newpid,'pointer':f'/ontology_mapping/evidence/{n}','before_claim':previous,'before_claim_sha256':canon(previous) if previous else None,'after_claim':claim,'after_claim_sha256':canon(claim),'correspondence':'unchanged original claim; later root audited enum pass allowed' if claim==previous else 'revised/new LLM-assisted claim; LLM_SUGGESTION','same_source_semantics_only':finding})

for d in ds:
 i=d['source_index'];old=next(x for x in oldDs if x['case_id']==d['case_id']);pids=old['proposal_ids'];notes=[]
 for pid in pids:
  if pid in fixes:
   f,a,b=fixes[pid];d=replace_strings(d,a,b);notes.append(f)
 if i==109:
  d['reasoning']+=' '+version_note;d['applicability']+=' '+version_note
 if i in [53,181]:
  d['reasoning']=swine_note;d['applicability']='Only MD960/DSMZ1076b and the four original SP4-Z occurrences are bound to the existing Swine_Serum promotion. Inherited raw-alias application/export hold remains; no generic Porcine treatment or species-only equivalence is inferred.';d['disposition']='existing_identity_or_alias'
 if i==158:
  d['disposition']='unresolved';d['reasoning']='JCM1303 positively supports heat-inactivated bovine calf serum among filter-sterilized additions. Its MD2061 creation lineage already belongs to Bovine_Calf_Serum. Whole known occurrence audit establishes additional CCAP gamma-irradiated fetal product, DSM78d fetal/newborn alternatives, Gibco M2240 without product/protocol bridge, and later KOMODO contexts. A missing heat schedule does not block this known partial preparation. The unresolved issue is owner boundary and occurrence partition: retire the parallel source-number new-owner proposal without narrowing the existing owner or calling it untreated.'
  d['applicability']='KG case158/MD2061 retains its exact JCM1303 evidence. No CultureMech occurrence is automatically rerouted from the broader owner. All nine historical exact-label records and eleven current local rows are enumerated in the audit, including the Gibco alias. Historical8/8 statistics are preserved as historical values.'
  d['missing_requirement']='; '.join(audit['assessment']['missing_facts']);d['no_change_reason']='No active payload: a parallel owner would duplicate authentic MD2061 continuity, while whole-owner narrowing would misrepresent unresolved broader usages. Concrete occurrence partition and alternatives are supplied; no ontology/heat-schedule prerequisite is invented.'
 d['proposal_ids']=[replacements.get(x,x) for x in pids if replacements.get(x,x) is not None]
 if 'completion_reassessment' in d:
  cr=d['completion_reassessment'];cr['proposal_ids']=d['proposal_ids']
  if 'bounded_scientific_conclusion' in cr:cr['bounded_scientific_conclusion']=d['reasoning']
  if i==158:cr.update({'status':'source_preparation_supported_owner_continuity_unresolved','scientific_missing_fact':d['missing_requirement'],'ordinary_curation_deferred':False})
 d['evidence_ids']=list(dict.fromkeys(d['evidence_ids']+['sv3-serums-contexts','sv3-serums-owner-lookup','sv3-serums-prior-context']+[e['evidence_id'] for e in newE if d['case_id'] in e.get('case_ids',[]) and e['kind']=='primary_source']+(['sv3-serums-calf-occurrence-audit'] if i==158 else [])))
 d['issue_refs']=list(dict.fromkeys(d.get('issue_refs',[])+['https://github.com/CultureBotAI/MediaIngredientMech/issues/1237']))
 d['independent_review']={'status':'pending','evidence_ids':[]};d['review_authorship']='Codex /root/buffers_research successor-v3 serum correction author; original bio/KG histories and source snapshots preserved. Requires separate skeptical review.'
 d['successor_v3_reassessment']={'old_decision_sha256':canon(old),'old_selected_core':'successor-v2/decisions.json','old_proposal_ids':pids,'new_proposal_ids':d['proposal_ids'],'retired_without_replacement':[x for x in pids if x in replacements and replacements[x] is None],'source_case_and_occurrences_unchanged':True,'publication_approval':False,'reason':'BIO-F02/F03/F04/F05/F08 bounded corrections; previous approval does not transfer.'}
 assert d['case_input_sha256']==old['case_input_sha256'] and d['occurrence_ids']==old['occurrence_ids'];bycase[i]=d

write('decision-fragment.json',{'decisions':[bycase[i] for i in scope]})
write('proposals-fragment.json',{'proposals':newP,'retired_proposal_ids':[calf_old],'superseded_proposal_ids':[p['proposal_id'] for p in selected if p['proposal_id']!=calf_old]})
write('evidence-fragment.json',{'evidence':newE})
write('retirement-supersession-bridge.json',{'bridges':bridges,'active_old_scope_count':len(selected),'active_successor_scope_count':len(newP),'retired_without_replacement':[calf_old],'unchanged_other_case109_proposals':['sv1-bio-heat_inactivated_fbs_dsmz1076b','sv1-bio-heat_inactivated_fbs_nbrc400'],'no_forced_total_count':True})
write('mapping-claim-correspondence.json',{'claims':claims,'policy':'No global enum replacement; newly authored/revised MappingEvidence is LLM_SUGGESTION. All historical events remain verbatim. Original M2578 mapping claim is unchanged for root claim-specific enum correction.'})
write('literal-before-after-diffs.json',{'payloads':diffs,'decisions':[{'source_index':i,'before':next(x for x in oldDs if x['source_index']==i),'after':bycase[i]} for i in scope]})
violations=validate_component_partonomy(allnewrecords)
write('author-validation.json',{'started_at':start,'completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'runtime_seconds':time.monotonic()-tick,'guarded_payloads':guard,'partonomy_violations':[dataclasses.asdict(x) for x in violations],'partonomy_scope':'Only nine authored serum payloads; none has component assertions. Not a full-catalog or downstream approval.','case_count':len(ds),'frozen_occurrence_count':sum(len(x['full_frozen_occurrences']) for x in context),'all_original_selected_payload_hashes_verified':True,'all_selected_case_hashes_and_full_snapshot_component_objects_verified':True,'publication_approval':False})
print(json.dumps({'proposals':len(newP),'decisions':len(ds),'evidence':len(newE),'retired':calf_old,'partonomy_errors':len(violations),'runtime_seconds':time.monotonic()-tick}))
