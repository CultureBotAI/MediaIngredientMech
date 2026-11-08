"""Bounded S7 proposals only; native history and validated writer, no corpus edit."""
from pathlib import Path
import copy, datetime, difflib, hashlib, json, os, subprocess, sys
R=Path.cwd(); C=R.parents[2]; O=R/'.temp/columbia-controls-successor-v1'
A=R/'reports/all_unmatched_20261107/worker-10'; S=A/'successor-v7'; B=A/'successor-v6/final-core'
sys.path.insert(0,str(R/'src'))
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.write_validated import write_validated_ingredient
import yaml
BASE='c66d6d3665368fe1ae8986fb7c16340a103582c1'
COL='https://github.com/CultureBotAI/MediaIngredientMech/issues/1237#issuecomment-6720201502'
BUF='https://github.com/CultureBotAI/MediaIngredientMech/issues/1237#issuecomment-6720201281'
NEW='sv7-dependent-columbia-unmapped0118-partition'
DIF='sv3-hm-difco-columbia1270'; OX='sv1-bio-columbia_blood_agar_oxoid_m2224'
BUFFER_IDS=['sv1-buffers-tris_hcl_0_2m_ph7_5_dsmz273','sv1-buffers-hepes_2m_ph7_jcm556_1200']
load=lambda p:json.loads(p.read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
canon=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':'),allow_nan=False).encode()).hexdigest()
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(p,d):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x') as f:json.dump(d,f,indent=2,ensure_ascii=False);f.write('\n')
def cap(p):return {'root':'artifact','path':str(p.relative_to(A)),'sha256':sha(p)}
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==BASE
D=load(B/'decisions.json');P=load(B/'proposals.json');E=load(B/'evidence.json'); oldP=copy.deepcopy(P)
by={p['proposal_id']:p for p in P['proposals']}; proofs=[]; at=now()
def write_record(pid,before,after,src,fields,reason,issue):
 event=record_curation_event(after,curator='Codex worker10 /root',action='CORRECTED_SOURCE_SCOPE_PROPOSAL',changes=reason+' Filed before correction: '+issue+' Isolated LLM-assisted proposal only; no maintained application, human-review claim, role or export approval.',previous_status=before['mapping_status'],new_status=after['mapping_status'],llm_assisted=True)
 dest=S/'proposed'/(pid+'.yaml');fd=os.open(dest,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o644)
 class Reserved:
  parent=dest.parent
  def open(self,mode,encoding=None):
   assert mode=='w' and os.fstat(fd).st_nlink==1 and os.fstat(fd).st_ino==dest.stat().st_ino
   return os.fdopen(fd,mode,encoding=encoding)
  def __str__(self):return str(dest)
 write_validated_ingredient(after,Reserved());assert yaml.safe_load(dest.read_text())==after
 with (S/'diffs'/(pid+'.diff')).open('x') as f:f.writelines(difflib.unified_diff(src.read_text().splitlines(True),dest.read_text().splitlines(True),fromfile=str(src.relative_to(R)),tofile=str(dest.relative_to(R))))
 assert after['curation_history'][:-1]==before['curation_history']
 proof={'proposal_id':pid,'before_payload':{'path':str(src.relative_to(R)),'sha256':sha(src)},'after_capture':cap(dest),'changed_existing_fields':fields,'appended_history':event,'history_prefix_exact':True,'before_object_sha256':canon(before),'after_object_sha256':canon(after),'scope':reason}
 proofs.append(proof);return cap(dest)

# Real same-path owner correction: the only new dependent proposal in this batch.
src=S/'inputs/Columbia_Blood_Agar_Base.before.yaml';before=yaml.safe_load(src.read_text());after=copy.deepcopy(before)
assert before['identifier']=='UNMAPPED_0118' and before['mapping_status']=='UNMAPPED' and len(before['curation_history'])==5
assert len(before['synonyms'])==3 and before['synonyms'][0]['synonym_type']=='RAW_TEXT'
for i in [1,2]:assert after['synonyms'][i]['synonym_type']=='CATALOG_VARIANT';after['synonyms'][i]['synonym_type']='REJECTED_LABEL'
partition_note=("Source continuity partition under CENTRAL-21 / BIO-F06/BIO-F07: retain this authentic generic UNMAPPED_0118 owner, its original history, generic RAW_TEXT label and stored occurrence statistics. The retained source strings 'Columbia blood agar base (Oxoid CM331)' and 'Columbia blood agar base (BD-Difco)' are REJECTED_LABEL only on this mixed residual: their previous global resolving ownership is withdrawn, not their product existence. The BD-Difco vendor string is supported for the separate Difco JCM1270 dry-base proposal by the direct JCM1270 recipe, manufacturer BD2009 nominal formula and two vendor-qualified 44 g source contexts. The generic J1270/compound2046 row is routeable only in that exact source context; compound2046 is not globally identified. Four later CM331 rows specify 1 L prepared base before blood and retain exact preparation/quantity holds; this label is not a global alias for dry Oxoid powder. Oxoid source300 retains variable / VARIABLE and printed CM0331 context; source921 M2224 retains 39 g without a historical catalogue assertion. This generic owner receives no vendor formula, supplier, ontology, components, role or guessed preparation. One nominal Oxoid family candidate still requires coordinator composition with both authentic source origins. Exact coupled dependency and source-routing bindings are in successor-v7; no source record or maintained owner is applied by this proposal.")
after['notes']=before['notes']+' '+partition_note
rollback=copy.deepcopy(after);rollback['notes']=before['notes'];rollback['synonyms']=copy.deepcopy(before['synonyms']);assert rollback==before
owner_cap=write_record(NEW,before,after,src,['synonyms[1].synonym_type','synonyms[2].synonym_type','notes'],partition_note,COL)
owner_dependency={'proposal_id':NEW,'kind':'edit_existing_owner','owner_path':'data/ingredients/unmapped/Columbia_Blood_Agar_Base.yaml','before_sha256':sha(src),'after_capture':owner_cap,'case_ids':[D['decisions'][i]['case_id'] for i in [118,178]],'review_state':'pending_exact_full_payload_independent_review','application_state':'not_applied','source_scope':'Genuine same-path mixed-owner partition, causally required by existing W10 Oxoid118 and Difco178; not a new source case or vendor maintained preimage.'}
assert all(any(o['path']==owner_dependency['owner_path'] and o['sha256']==owner_dependency['before_sha256'] for o in D['decisions'][i]['owner_records']) for i in [118,178])

# The new vendor destination stays a null-before proposal; only exact vendor alias and explanatory notes change.
p=by[DIF];src=A/p['after_capture']['path'];before=yaml.safe_load(src.read_text());after=copy.deepcopy(before)
assert p['kind']=='new_owner' and p['before_sha256'] is None and before['synonyms']==[]
assert before['component_assertion']['method']=='CURATED_INTERPRETATION' and before['component_assertion']['completeness']=='COMPLETE' and len(before['components'])==7
alias=copy.deepcopy(yaml.safe_load((S/'inputs/Columbia_Blood_Agar_Base.before.yaml').read_text())['synonyms'][2]);after['synonyms'].append(alias)
difco_note=("CENTRAL-21 bounded source routing: the exact vendor-qualified label 'Columbia blood agar base (BD-Difco)' is retained here as CATALOG_VARIANT with its original CultureMech alias-source provenance, supported by direct JCM1270 and the dated manufacturer BD2009 dry-product table. Two 44 g vendor-qualified contexts and the positively linked generic J1270/compound2046 context support only this nominal dry-base route. The generic Columbia label and providercompound2046 are not global aliases or identities. Seven nominal immediate ingredients, quantities, method/completeness scope, actual-lot uncertainty and all blood/water/receiving-recipe discrepancies are unchanged. Installation must be coupled to the authentic existing UNMAPPED_0118 partition proposal "+NEW+" from maintained before "+owner_dependency['before_sha256']+" to proposed after "+owner_cap['sha256']+". These are dependency bytes, not this new vendor destination's maintained preimage. Whole-owner, role and export approval remains separate.")
after['notes']=before['notes']+' '+difco_note
rollback=copy.deepcopy(after);rollback['notes']=before['notes'];rollback['synonyms']=copy.deepcopy(before['synonyms']);assert rollback==before
p['after_capture']=write_record(DIF,before,after,src,['synonyms','notes'],difco_note,COL)

# Named-stock metadata only: do not change component objects, evidence, method, source, amounts or chemistry.
for pid in BUFFER_IDS:
 p=by[pid];src=A/p['after_capture']['path'];before=yaml.safe_load(src.read_text());after=copy.deepcopy(before)
 assert p['kind']=='new_owner' and p['before_sha256'] is None
 assert after['component_assertion']['method']=='LABEL_ENUMERATION' and after['component_assertion']['completeness']=='PARTIAL'
 assert len(after['components'])==1 and after['components'][0]['reference_scope']=='UNMAPPED'
 after['component_assertion']['completeness']='UNKNOWN'
 reason=('CENTRAL24-COMPLETENESS-001: change only component_assertion.completeness from PARTIAL to UNKNOWN. The cited source names the stock but does not establish complete constituents or explicitly state that additional constituents are omitted. Preserve the one literal UNMAPPED named part, all chemistry, nominal strength and pH, component evidence/method, source/occurrence associations, quantities, solvent/titrant/form uncertainties and original history. Receiving-medium ingredients are not stock formulation evidence. This does not change controls280/938 or named-input Wolfe/Hutner lists.')
 rollback=copy.deepcopy(after);rollback['component_assertion']['completeness']='PARTIAL';assert rollback==before
 p['after_capture']=write_record(pid,before,after,src,['component_assertion.completeness'],reason,BUF)
 assert 'partial source-supported components' in p['description']
 p['description']=p['description'].replace('partial source-supported components','source-named components with UNKNOWN list completeness',1)
 p['publication_holds']=[x.replace('from PARTIAL components','from components with UNKNOWN completeness') for x in p.get('publication_holds',[])]

# Current source-routing ledger is separate from the immutable assigned shard membership.
matrix=load(S/'inputs/columbia-seven-contexts.json');decision=load(S/'inputs/columbia-decision-v3.json');rows=[]
for actual,recommend in zip(matrix['rows'],decision['seven_current_owner_occurrence_partition']):
 assert actual['recipe_id']==recommend['recipe_id'] and actual['source_quantity_preserved']==recommend['source_quantity']
 dry=recommend['exact_dry_identity_route_supported']; b=actual['recipe_capture']; cp=S/'inputs/context-recipes'/b['sha256']
 assert sha(cp)==b['sha256']
 rows.append({'context_id':actual['recipe_id']+':'+actual['occurrence']['component_field']+'/'+actual['occurrence']['component_index'],
  'original_occurrence_row':actual['occurrence'],'source_recipe_capture':cap(cp),'original_recipe_capture_metadata':b,
  'exact_source_quantity':actual['source_quantity_preserved'],'route_supported':dry,'target_proposal_id':DIF if dry else None,
  'material_scope':'source-qualified Difco nominal dry base' if dry else 'Oxoid product provenance only; prepared base before blood',
  'global_generic_label_or_provider_mapping':False,'assigned_W10_case_added':False,'assigned_W10_occurrence_added':False,
  'retained_holds':recommend['retained_holds']+([] if dry else ['Keep original 1 L prepared amount; exact preparation identity/yield unresolved. No dry39g substitution or global CM331 alias.']),
  'same_owner_dependency':owner_dependency,'application_state':'not_applied'})
assert len(rows)==7 and sum(r['route_supported'] for r in rows)==3
foreign=load(S/'inputs/w04-current-origin.json');sourcecase=next(x for x in foreign['original_evidence'] if x['evidence']['evidence_id']=='media-case-074')
foreign_case=load(S/'inputs/w04-captures'/sourcecase['capture_binding']['sha256']);owncase=load(C/'queue/preliminary-v5/shards/shard-10.json')['cases'][118]
assert foreign_case['occurrences'][0]['raw_component']['concentration']=={'unit':'VARIABLE','value':'variable'}
assert owncase['occurrences'][0]['raw_component']['concentration']=={'unit':'G_PER_L','value':'39'}
oxoid={'nominal_family':'Oxoid300/921 four-input nominal dry-base family','owner_dependency':owner_dependency,
 'W10_origin':{'worker':'w10','head':BASE,'proposal_id':OX,'proposal_object_sha256':canon(next(p for p in oldP['proposals'] if p['proposal_id']==OX)),'payload':by[OX]['after_capture'],'original_case':owncase},
 'W04_origin':{'worker':'w04','observed_head':foreign['observed_local_head'],'selected_head':foreign['selected_head'],'proposal_id':foreign['original_proposal']['proposal_id'],'original_proposal':foreign['original_proposal'],'payload_capture':cap(S/'inputs/W04-Oxoid-CM0331.current-origin.yaml'),'original_case':foreign_case,'original_current_decisions':foreign['original_decisions']},
 'existing_coordinator_prototype':cap(S/'inputs/Oxoid39g.coordinator-prototype.yaml'),
 'source_routes':[{'origin':300,'actual_source':'TOGO M2935 / Skirrow, CM0331 printed','raw_quantity':foreign_case['occurrences'][0]['raw_component']['concentration'],'scope':'Supported catalogue-qualified dry product input; no39g receiving dose asserted'},
                  {'origin':921,'actual_source':'TOGO M2224','raw_quantity':owncase['occurrences'][0]['raw_component']['concentration'],'scope':'Supported39g nominal dry input and four printed constituent masses; no historical CM0331 catalogue backfill'}],
 'W10_payload_changed':False,'W04_payload_changed':False,'combined_payload_authored_here':False,
 'single_family_installation_condition':'Coordinator must compose/review one existing Oxoid nominal family candidate with the actual current W04 provenance/history and unchanged W10 origin, coupled to the reviewed0118 dependency. These source origins are not parallel installation instructions. No arbitrary winning identifier, new joint owner or foreign W10 case is minted.',
 'prepared_context_holds':[r['context_id'] for r in rows if not r['route_supported']], 'role_export_approval':False}
save(S/'source-routing.json',{'at':at,'source':'Independent W07 continuity-decision-v3 and complete primary/source captures, now bound to actual worker-produced dependency bytes','same_owner_dependency':owner_dependency,'seven_context_rows':rows,'Oxoid_origin_routes':oxoid,'membership_rule':'Seven later owner-context rows remain separate from the frozen188case/304occurrence W10 assignment. Original W04 case stays foreign. Generic2046 is not globally resolved.','source_records_changed':False})
save(S/'cross-worker-dependencies.json',oxoid)

# Append the real same-owner dependent proposal with exact original source backlinks.
newp={'proposal_id':NEW,'case_ids':owner_dependency['case_ids'],'description':partition_note,'evidence_ids':[],
 'owner_path':owner_dependency['owner_path'],'kind':'edit_existing_owner','before_sha256':owner_dependency['before_sha256'],'after_capture':owner_cap,
 'genuine_dependent_origin':{'author':'Codex worker10 /root','predecessor_head':BASE,'trigger_proposals':[{'proposal_id':pid,'proposal_object_sha256':canon(next(x for x in oldP['proposals'] if x['proposal_id']==pid)),'after_capture':next(x for x in oldP['proposals'] if x['proposal_id']==pid)['after_capture']} for pid in [OX,DIF]],'trigger_case_indices':[118,178],'trigger_case_ids':owner_dependency['case_ids'],'original_owner_records_already_contain_exact_beforeimage':True,'new_source_case':False,'foreign_source_case_claimed':False},
 'identity_consequences':'Retain authentic UNMAPPED_0118 generic identity, classification and all5 history events. No new identifier, vendor mapping, supplier, component or role is grafted.',
 'publication_review_obligations':['Review complete final dependency bytes, then couple any supported vendor application to this exact before/after owner correction.','No mixed-owner history is transplanted onto vendor new destinations; their maintained before hashes remain null.','Retain four prepared-base holds, generic future source ambiguity and all role/export/source limitations.'],
 'independent_review':{'status':'pending','evidence_ids':[]}}
P['proposals'].append(newp)
for i in [118,178]:D['decisions'][i]['proposal_ids'].append(NEW)
proofby={r['proposal_id']:r for r in proofs}
affected={80,118,135,178}; changedids={DIF,OX,*BUFFER_IDS,NEW}
for obj in [p for p in P['proposals'] if p['proposal_id'] in changedids]+[D['decisions'][i] for i in sorted(affected)]:
 old_review=copy.deepcopy(obj.get('independent_review',{'status':'pending','evidence_ids':[]}))
 obj['source_successor_v7']={'predecessor_head':BASE,'author':'Codex worker10 /root','issues':[COL,BUF] if obj.get('proposal_id') in BUFFER_IDS else [COL],
   'prior_independent_review':old_review,'scope':'Bounded Columbia continuity/routing and two named-stock completeness corrections only. Prior scientific and release holds remain; exact full successor bytes require separate independent review.','review_state':'pending','original_source_membership_retained':True,'whole_owner_role_export_approval':False}
 obj['independent_review']={'status':'pending','evidence_ids':[]}
 if obj.get('proposal_id') in [DIF,OX]:
  obj['source_successor_v7']['same_owner_dependency']=copy.deepcopy(owner_dependency)
  obj['source_successor_v7']['routing']=cap(S/'source-routing.json')
  obj['source_successor_v7']['previous_proposal']=copy.deepcopy(next(x for x in oldP['proposals'] if x['proposal_id']==obj['proposal_id']))
 if obj.get('proposal_id') in changedids:obj['review_status_explanation']='Pending author-independent exact full successor payload and dependency review. Existing unaffected source science and all holds are preserved, not blanket-transferred.'
for i in sorted(affected):
 d=D['decisions'][i];issue=BUF if i in [80,135] else COL
 d['source_successor_v7']['issues']=[issue]
 if issue not in d['issue_refs']:d['issue_refs'].append(issue)
 if i in [118,178]:
  d['source_successor_v7']['same_owner_dependency']=copy.deepcopy(owner_dependency)
  d['source_successor_v7']['routing']=cap(S/'source-routing.json')
  d['reasoning']+=' A genuine same-path UNMAPPED_0118 partition proposal is now attached from its original maintained29ed63 preimage. Exact supported vendor dry routes are recorded separately from four held prepared-base contexts; neither the seven later context rows nor the external W04 case changes this frozen source membership. '+('The unchanged M2224 payload is an authentic origin for coordinator composition of one Oxoid nominal family; W04 source300 retains variable quantity and only its printed catalogue.' if i==118 else 'The exact BD-Difco vendor alias is supported for the dry candidate; generic provider2046 remains unresolved outside the positively linked J1270 source context.')
 if i==178:d['missing_requirement']='No scientific fact blocks this bounded alias/partition/routing proposal. Actual guarded application must couple the exact0118 correction and vendor successor; historical lot, receiving-medium discrepancies and whole-owner/role/export review remain separate.'

# Evidence membership is append-only, and references claim only the original W10 cases.
allcaseids=[D['decisions'][i]['case_id'] for i in sorted(affected)]
evidence_specs=[
 ('sv7-filed-columbia',S/'inputs/issue1237-comment6720201502.json','source_snapshot',COL,'Exact filed bounded Columbia implementation decision before correction.'),
 ('sv7-filed-stock-completeness',S/'inputs/issue1237-comment6720201281.json','source_snapshot',BUF,'Exact filed two-control UNKNOWN correction; other controls and full named-input lists excluded.'),
 ('sv7-independent-columbia-decision',S/'inputs/columbia-decision-v3.json','source_snapshot',None,'Immutable author-independent W07 scientific continuity decision with source scope and holds; not final review of these new bytes.'),
 ('sv7-explicit-source-routing',S/'source-routing.json','local_validation',None,'Actual source-route and dependency bindings; seven context rows separate from188assigned cases.'),
 ('sv7-external-oxoid-origins',S/'cross-worker-dependencies.json','source_snapshot',None,'W04 actual current origin and W10 unchanged origin, literal quantities and coordinator single-family composition condition.'),
 ('sv7-input-byteproof',S/'preflight.json','local_validation',None,'2358W07 and50central members verified; exact current source inputs and maintained beforeimage.'),
]
eids=[]
for eid,path,kind,url,summary in evidence_specs:
 E['evidence'].append({'evidence_id':eid,'kind':kind,'capture':cap(path),'url':url,'accessed_at':at,'locator':'Complete exact artifact; original capture retrieval timestamps are preserved within bound inputs','supports_or_contradicts':summary,'case_ids':allcaseids});eids.append(eid)
for obj in [p for p in P['proposals'] if p['proposal_id'] in changedids]+[D['decisions'][i] for i in sorted(affected)]:
 obj.setdefault('evidence_ids',[]).extend(eids)
# New dependency retains original primary evidence applicability rather than invented primary retrieval.
newp['evidence_ids']=sorted(set(newp['evidence_ids']+D['decisions'][118]['evidence_ids']+D['decisions'][178]['evidence_ids']))
save(S/'payload-change-proof.json',{'at':now(),'predecessor_head':BASE,'changed_payloads':proofs,'new_dependent_proposal_id':NEW,
 'changed_original_payload_ids':[DIF,*BUFFER_IDS],'unchanged_Oxoid_payload':by[OX]['after_capture'],'changed_original_metadata_proposal_ids':[DIF,OX,*BUFFER_IDS],
 'affected_case_indices':sorted(affected),'original_histories_exact':True,'no_maintained_or_source_writes':True})
for name,doc in [('decisions.json',D),('proposals.json',P),('evidence.json',E)]:save(S/'author-core'/name,doc)
save(S/'author-freeze.json',{'at':now(),'predecessor_head':BASE,'four_authored_payloads':[{'proposal_id':x['proposal_id'],'after_capture':x['after_capture']} for x in proofs],
 'core':{n:cap(S/'author-core'/n) for n in ['decisions.json','proposals.json','evidence.json']},'proof':cap(S/'payload-change-proof.json'),'routing':cap(S/'source-routing.json'),'review_pending':True})
with (S/'scripts/build_candidates.py').open('xb') as f:f.write(Path(__file__).read_bytes())
print(json.dumps({'status':'AUTHOR_FROZEN','new_dependent':NEW,'four_payloads':[{'proposal_id':x['proposal_id'],'sha256':x['after_capture']['sha256']} for x in proofs],'cases':len(D['decisions']),'proposals':len(P['proposals']),'evidence':len(E['evidence']),'occurrences':sum(len(d['occurrence_ids']) for d in D['decisions']),'affected_case_indices':sorted(affected),'Oxoid_payload_unchanged':True},indent=2))
