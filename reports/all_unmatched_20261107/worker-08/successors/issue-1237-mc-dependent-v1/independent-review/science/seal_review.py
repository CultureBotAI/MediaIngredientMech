from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import yaml

P = Path(__file__).resolve().parent
W = P.parents[2]
C = W.parents[2]
A = W / 'reports/all_unmatched_20261107/worker-08'
O = A / 'successors/issue-1237-mc-dependent-v1'
R = C / 'workers/w09/worktree/.temp/tenvit-mc-continuity-decision-v1'
now = datetime.now(timezone.utc).isoformat()

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def canon(x): return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode()).hexdigest()
def read(p): return json.loads(p.read_text())
def dump(name,obj):
    with (P/name).open('x') as f: json.dump(obj,f,ensure_ascii=False,indent=2); f.write('\n')

checks=[]
def check(name,condition,detail=None):
    checks.append({'check':name,'passed':bool(condition),'detail':detail})
    if not condition: raise AssertionError(name)

beforepath=W/'data/ingredients/mapped/Mc_vitamins.yaml'
afterpath=O/'payloads/Mc_vitamins.yaml'
before=yaml.safe_load(beforepath.read_text());after=yaml.safe_load(afterpath.read_text())
proposal=read(O/'author/proposal.json');decision=read(O/'author/decision.json')
pid=proposal['proposal_id'];cid=decision['case_id']
check('exact frozen candidate',sha(afterpath)=='996fc2bfc69284abcbbe75fba6b069bc41fabb3e35c73d5a493de30ab153bcf3')
check('exact authored proposal',sha(O/'author/proposal.json')=='f185a4c3cba0d31fdb138dd4b9c35d1dd40649be90ca610a22938d981327d3f3')
check('exact authored decision',sha(O/'author/decision.json')=='b9636f1a786e3847199c3ada039eebb64f20775a5d1eda321aafee5a4b211840')
check('authentic existing-owner preimage',sha(beforepath)==sha(O/'beforeimages/Mc_vitamins.yaml')==proposal['before_sha256']=='59c53dfe4e273ebfc7c3fe86fd4244978868ff1879dcde97af64bbeb61c07123')
check('no new owner identity',proposal['kind']=='edit_existing_owner' and proposal['owner_path']=='data/ingredients/mapped/Mc_vitamins.yaml')
check('proposal binds exact payload',proposal['after_capture']['sha256']==sha(afterpath))
check('exact top-level field set',set(before)==set(after))
allowed={'components','component_assertion','notes','curation_history'}
check('only allowed four top-level fields changed',{k for k in before if before[k]!=after[k]}==allowed)
for k in set(before)-allowed:check('unchanged owner field '+k,before[k]==after[k])
check('four original history entries preserved',after['curation_history'][:-1]==before['curation_history'] and len(after['curation_history'])==5)
check('truthful author event',after['curation_history'][-1]['llm_assisted'] is True and after['curation_history'][-1]['curator'].startswith('worker08:/root '))
check('old crosswalk note retained verbatim in history',before['component_assertion']['evidence'][1]['notes'] in after['curation_history'][-1]['changes'])
check('original notes retained as prefix',after['notes'].startswith(before['notes']))
for i,(b,a) in enumerate(zip(before['components'],after['components'])):
    for k in ['component_name','concentration_value','concentration_unit']:check(f'component {i} literal {k}',b[k]==a[k])
    if i!=6:check(f'component {i} entire object unchanged',b==a)
check('ten components only',len(before['components'])==len(after['components'])==10)
check('unsupported D component ID omitted','component_id' not in after['components'][6])
check('literal DL remains UNMAPPED',after['components'][6]['reference_scope']=='UNMAPPED')
check('same exact recipe method and completeness',all(before['component_assertion'][k]==after['component_assertion'][k] for k in ['method','completeness']))
check('original direct recipe evidence unchanged',before['component_assertion']['evidence'][0]==after['component_assertion']['evidence'][0])
for k in ['evidence_type','source','source_record']:check('historical crosswalk source preserved '+k,before['component_assertion']['evidence'][1][k]==after['component_assertion']['evidence'][1][k])

case=next(c for c in read(A/'provenance/shard-08.json')['cases'] if c['case_id']==cid)
check('frozen full case digest',canon(case)==decision['case_input_sha256'])
check('all six occurrence identifiers exact',[o['occurrence_id'] for o in case['occurrences']]==decision['occurrence_ids'])
old=next(c for c in read(A/'successors/issue-1237-tenvit-v1/decisions.json')['decisions'] if c['case_id']==cid)
allowed_case={'reasoning','applicability','proposal_ids','prior_independent_reviews','issue_refs','evidence_ids','independent_review','owner_records'}
check('case changes are bounded',{k for k in set(old)|set(decision) if old.get(k)!=decision.get(k)}==allowed_case)
for k in set(old)-allowed_case:check('unchanged case field '+k,old[k]==decision[k])
for k in ['reasoning','applicability','proposal_ids','evidence_ids','issue_refs','owner_records']:
    if isinstance(old[k],str):check('case prefix retained '+k,decision[k].startswith(old[k]))
    else:check('case list prefix retained '+k,decision[k][:len(old[k])]==old[k])
check('only one new proposal backlink',decision['proposal_ids']==old['proposal_ids']+[pid])
trigger='CM_OCC:a181b24b7eb91c50c771bd1c1fc3012fd0cf28f45b49f2750c3d43bda9cdd531'
check('only NBRC903 trigger',proposal['source_occurrence_ids']==[trigger])
check('zero Mc campaign occurrences',proposal['mc_campaign_occurrence_count']==0)

source_index=read(O/'inputs/source-ref-index.json')
for row in source_index['selected_captures']:
    original=Path(row['original_path']);copy=W/row['published_path']
    check('copied source exact '+str(copy.relative_to(O)),sha(original)==sha(copy)==row['sha256'])

evidence=read(A/'successors/issue-1237-tenvit-v1/evidence.json')['evidence']
evidence_by_id={e['evidence_id']:e for e in evidence}
eids=['vm-fetch-1962216682ccb735','vm-fetch-7d55379a5f033497','vm-fetch-ede69c87ee45106a','vm-fetch-19ea505c685bcbd1','vm-fetch-2630e40c26a0b155','vm-fetch-571507208cde7532']
occurrence_reviews=[];source_rows=[]
for i,occ in enumerate(case['occurrences']):
    p=C/'queue/preliminary-v5'/occ['full_recipe_snapshot'];raw=yaml.safe_load(p.read_text())
    check('frozen source file '+p.name,sha(p)==occ['source_file_sha256'])
    component=raw['ingredients'][int(occ['component_path'].split('/')[1])]
    check('frozen component '+p.name,component==occ['raw_component'])
    e=evidence_by_id[eids[i]];capture=A/e['capture']['path'];check('primary capture '+eids[i],sha(capture)==e['capture']['sha256'])
    source_rows.append({'evidence_id':eids[i],'path':str(capture),'sha256':sha(capture),'url':e['url'],'original_accessed_at':e['accessed_at'],'inspection_at':now,'locator':'Complete primary composition and nested vitamin table plus surrounding preparation read; no unrelated mineral grounding approval.'})
    istrigger=occ['occurrence_id']==trigger
    branch='NBRC903 ten-vitamin comparator' if istrigger else ('NBRC1226 different ten-vitamin branch' if i==2 else 'Common nine-vitamin branch')
    occurrence_reviews.append({'occurrence_id':occ['occurrence_id'],'recipe_id':occ['recipe_id'],'raw_source_file':str(p),'raw_source_sha256':sha(p),'raw_component':component,'source_evidence_id':eids[i],'branch':branch,'appraisal':('NBRC903 is the sole causal dependency trigger. Its 10 ml receiving amount, generic calcium/B12 labels, ten nominal masses and 1 L water input remain source-bound. It is not newly mapped to Mc.' if istrigger else ('The 1 ml receiving dose and B12 5 mg/pABA 1 mg/lipoic acid 5 mg batch remain separate from NBRC903; no Mc association.' if i==2 else 'The nine-vitamin recipe has B12 0.01 mg and pABA 1 mg, without lipoic acid. Its original receiving dose remains unchanged; this Mc dependency does not expand to this occurrence.'))})

field_appraisals={
 'identifier':'Existing kgmicrobe.ingredient:mc_vitamins remains the authentic record identity; no new identity or preferred owner election.',
 'preferred_term':'Mc_vitamins unchanged, consistent with owning Mixes block.',
 'synonyms':'The sole original RAW_TEXT culturebotht label remains byte-equivalent as an object; no new global alias or resolver activation.',
 'mapping_status':'MAPPED unchanged. This bounded correction is not a release decision.',
 'occurrence_statistics':'Original 22/22 unchanged; independently corroborated by raw Medias and consolidated source entries. Zero Mc campaign occurrences fabricated.',
 'curation_history':'All four original objects remain exact; one current, author-named LLM-assisted correction retains the withdrawn crosswalk note verbatim.',
 'notes':'Original prefix preserved. Added text correctly limits component closure to the ten printed Mc inputs, distinguishes nominal recipe support from pending association, and preserves physical/form/source/role/export limits.',
 'ingredient_type':'STOCK_SOLUTION unchanged, consistent with the source-defined Mc mixture; no pure-chemical identity asserted.',
 'solution_type':'VITAMIN_MIX unchanged; no subtype inferred from the ontology correction.',
 'components':'All ten names/order/quantities/units preserved; nine entire objects unchanged. Only literal DL calcium loses D-specific resolving ID and becomes UNMAPPED with explicit conflict provenance.',
 'component_assertion':'RECIPE_TRANSCRIPTION/COMPLETE retained, now expressly relative to the printed immediate ten-solute Mc table. No solvent, final volume, phosphate, gas, titrant, water input or X100 conversion invented. Dataset evidence truthfully describes ontology/crosswalk support and explicitly identifies LLM interpretation.',
 'ontology_mapping':'Full existing FALLBACK_REGISTRY object remains unchanged. This review does not recertify historical exhaustive-search claims or the inherited phrase that no ontology term could denote a stock.',
 'nutritional_roles':'Full inherited role object and evidence preserved. No confidence, mechanistic or whole-owner role approval is added.'}
check('every entire owner field individually appraised',set(field_appraisals)==set(after))

source_assessment=read(P/'source-assessment-v1.json')
inputs={str(p.relative_to(A)):sha(p) for p in [O/'payloads/Mc_vitamins.yaml',O/'author/proposal.json',O/'author/decision.json',O/'author/assessment.json',O/'author/dependency.json',O/'beforeimages/Mc_vitamins.yaml',O/'inputs/source-ref-index.json',O/'inputs/issue1237-comment-6720042215-retry.json',O/'inputs/issue1237-comment-6720201812-retry.json',A/'provenance/shard-08.json',A/'successors/issue-1237-tenvit-v1/decisions.json',A/'successors/issue-1237-tenvit-v1/evidence.json']}
dump('source-read-ledger-final.json',{'reviewer':'worker08:/root/organics','inspection_at':now,'initial_owning_source_ledger':{'path':'source-read-ledger-v1.json','sha256':sha(P/'source-read-ledger-v1.json')},'six_occurrence_primary_sources':source_rows,'six_raw_contexts':occurrence_reviews,'local_path_correction':'Frozen raw snapshot paths are relative to queue/preliminary-v5, not directly to campaign root. The initial direct-root path attempt failed; all actual snapshots were subsequently found, read and rehashed.','new_network_requests':0})
dump('findings.json',{'reviewer':'worker08:/root/organics','author':'worker08:/root','new_scientific_findings':[],'open_blocking_findings':[],'existing_finding_dispositions':[{'finding_id':'SCI-TENVIT-003','status':'RESOLVED_IN_EXACT_ISOLATED_PROPOSAL_NOT_MAINTAINED','payload_sha256':sha(afterpath),'field':'/components/6','reproduction':'The beforeimage names calcium D,L-pantothenate but resolves CHEBI:31345. The owning recipe confirms DL and the primary ontology/manufacturer show D-specific identity. The candidate omits component_id, sets UNMAPPED and preserves the literal quantity and form.','limits':'No same-form child is asserted; actual purchase and whole-stock association remain unresolved.'}],'publication_observation':{'status':'REPORTED_TO_ROOT_SEPARATE_FROM_SCIENCE','description':'The candidate packet currently copies the full thesis PDF and full derived text. Retain privately and publish bounded factual support with exact original URL/time/hash before publication. No candidate science change is requested.'},'retained_holds':source_assessment['remaining_holds']})
dump('validation.json',{'status':'PASS','checks':checks,'check_count':len(checks),'scope':'Independent source/hash/object-delta readback only; not a rerun of native schema, partonomy or downstream admission gates.','at':now})
dump('review.json',{
 'reviewer':'/root/organics','author':'/root','reviewer_identity':'worker08:/root/organics','author_identity':'worker08:/root',
 'status':'PASS_BOUNDED_SCIENTIFIC_CORRECTION','at':now,
 'independence':source_assessment['independence'], 'full_payload_review':True,
 'case_ids':[cid],'proposal_ids':[pid],'case_hashes':{cid:canon(decision)},'payload_hashes':{pid:sha(afterpath)},'input_hashes':inputs,
 'open_blocking_findings':[],
 'case_reviews':[{'case_id':cid,'case_input_sha256':decision['case_input_sha256'],'decision_sha256':canon(decision),'outcome':'SUPPORTED_WITH_ALL_SOURCE_AND_ROUTING_HOLDS','appraisal':'Full six-occurrence source case read against frozen contexts and all six primary NBRC captures. Only NBRC903 triggers a genuine edit-existing-owner dependency; no fabricated Mc source case and no new occurrence mapping. Earlier reasoning remains as history, with current supersession and pending W04 routing explicit.','occurrence_reviews':occurrence_reviews,'source_evidence_ids':eids,'finding_ids':['SCI-TENVIT-003']}],
 'proposal_reviews':[{'proposal_id':pid,'before_sha256':proposal['before_sha256'],'after_sha256':sha(afterpath),'whole_payload_read':True,'outcome':'SUPPORTED_BOUNDED_DEPENDENT_CORRECTION','field_appraisals':field_appraisals,'component_appraisals':source_assessment['component_appraisals'],'finding_ids':['SCI-TENVIT-003'],'qualification':'Original nine resolving references are preserved within their existing scopes. This is not scientific approval of all inherited fields in referenced child owners, imported role evidence or release eligibility.'}],
 'retained_holds':source_assessment['remaining_holds'],
 'source_read_ledger':{'path':'source-read-ledger-final.json','sha256':sha(P/'source-read-ledger-final.json')},
 'validation':{'path':'validation.json','sha256':sha(P/'validation.json'),'checks':len(checks)},
 'known_finding_dispositions':{'path':'findings.json','sha256':sha(P/'findings.json')},
 'metadata_only_final_binding_boundary':'After this seal, final assembly may append this peer/evidence metadata to the selected decision/proposal and replace full thesis publication copies with bounded evidence plus private retention. No payload or scientific wording change is covered without re-review. A separate final-bindings receipt must bind the actual final indices.',
 'not_approved':['Maintained application','Downstream release','Exclusive Mc versus CB owner selection','Owner merge','New global aliases','JCM/NBRC exact stock mapping or child stereochemistry/vitamer transfer','Unrelated child-owner chemical/CAS/role claims']})
dump('HANDOFF.json',{'reviewer':'worker08:/root/organics','status':'SEALED_BOUNDED_SCIENCE_PASS','review':{'path':'review.json','sha256':sha(P/'review.json')},'findings':{'path':'findings.json','sha256':sha(P/'findings.json')},'source_read_ledger':{'path':'source-read-ledger-final.json','sha256':sha(P/'source-read-ledger-final.json')},'candidate_sha256':sha(afterpath),'validation_check_count':len(checks),'next':'Root final indices and private thesis-retention packaging require separate exact binding readback. No maintained edit, routing or release approval.'})
print(json.dumps({'status':'PASS','checks':len(checks),'review_sha256':sha(P/'review.json'),'handoff_sha256':sha(P/'HANDOFF.json')},indent=2))
