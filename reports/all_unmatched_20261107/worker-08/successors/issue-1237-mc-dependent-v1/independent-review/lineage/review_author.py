"""Exact authored Mc dependency lineage review; no scientific or native gate approval."""
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, subprocess, yaml
W=Path.cwd(); P=Path(__file__).resolve().parent
A=W/'reports/all_unmatched_20261107/worker-08'
O=A/'successors/issue-1237-mc-dependent-v1'
OLD=A/'successors/issue-1237-tenvit-v1'
CID='CM_NAME:d57e91ffaea6f0ab6ff0f3d6f0b04c26356c832e85dd83e9e2319874fda43506'
TRIGGER='CM_OCC:a181b24b7eb91c50c771bd1c1fc3012fd0cf28f45b49f2750c3d43bda9cdd531'
PID='mc1237-prop-mc-vitamins-dependent'
BEFORE='59c53dfe4e273ebfc7c3fe86fd4244978868ff1879dcde97af64bbeb61c07123'
H='a0190fed72b8f5119432003d1f9c84b8c1de7a48'
checks=[]; refs=[]
def sha(b): return hashlib.sha256(b).hexdigest()
def canon(x): return sha(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
def raw(p):
 p=Path(p); b=p.read_bytes(); refs.append({'path':str(p),'sha256':sha(b)}); return b
def j(p): return json.loads(raw(p))
def ref(p): return {'path':str(p),'sha256':sha(raw(p))}
def ck(name,ok): checks.append({'check':name,'pass':bool(ok)}); assert ok,name
def dump(name,obj):
 with (P/name).open('x') as f: json.dump(obj,f,indent=2,ensure_ascii=False); f.write('\n')
base=j(P/'baseline-bindings.json'); recommendation=j(P/'binding-recommendation.json')
ck('Preparation receipt remains exact',sha(raw(P/'baseline-bindings.json'))=='1424dd3fe569dab84e17bf656a7883f4cbf936eadce3b53e23008844fbee0a34')
ck('Preparation recommendation remains exact',sha(raw(P/'binding-recommendation.json'))=='5d1474a96c0c96ab132c7679ca7304905c534751b1a24da4fd406ab26238b96d')
afterraw=raw(O/'payloads/Mc_vitamins.yaml'); after=yaml.safe_load(afterraw)
proposal=j(O/'author/proposal.json'); decision=j(O/'author/decision.json')
for path,pin in [('payloads/Mc_vitamins.yaml','996fc2bfc69284abcbbe75fba6b069bc41fabb3e35c73d5a493de30ab153bcf3'),('author/proposal.json','f185a4c3cba0d31fdb138dd4b9c35d1dd40649be90ca610a22938d981327d3f3'),('author/decision.json','b9636f1a786e3847199c3ada039eebb64f20775a5d1eda321aafee5a4b211840')]: ck('Announced final author pin '+path,sha(raw(O/path))==pin)
before_raw=raw(W/'data/ingredients/mapped/Mc_vitamins.yaml'); before=yaml.safe_load(before_raw)
committed=subprocess.check_output(['git','show',H+':data/ingredients/mapped/Mc_vitamins.yaml'])
ck('Non-null original preimage is maintained and committed owner',sha(before_raw)==BEFORE and before_raw==committed==raw(O/'beforeimages/Mc_vitamins.yaml'))
ck('All original four history events preserved exactly',len(before['curation_history'])==4 and after['curation_history'][:4]==before['curation_history'] and canon(before['curation_history'])==base['mc_history_canonical_sha256'] and len(after['curation_history'])==5)
event=after['curation_history'][-1]
ck('New truthful current-author event does not impersonate earlier author',event['curator']=='worker08:/root SCI-TENVIT-003 dependent source proposal' and event['action']=='CORRECTED' and event['llm_assisted'] is True and event['previous_status']==event['new_status']=='MAPPED' and event['timestamp']=='2026-11-08T10:16:10.968674+00:00')
delta=[k for k in set(before)|set(after) if before.get(k)!=after.get(k)]
ck('Only bounded four top-level fields changed',set(delta)=={'curation_history','notes','components','component_assertion'})
unchanged=['identifier','preferred_term','synonyms','mapping_status','occurrence_statistics','ingredient_type','solution_type','ontology_mapping','nutritional_roles']
for k in unchanged: ck('Unchanged full field '+k,before[k]==after[k])
ck('Same ten complete literal names quantities units and order',len(before['components'])==len(after['components'])==10 and [[x[k] for k in ('component_name','concentration_value','concentration_unit')] for x in before['components']]==[[x[k] for k in ('component_name','concentration_value','concentration_unit')] for x in after['components']])
for n in range(10):
 if n!=6: ck('Unchanged entire component '+str(n),before['components'][n]==after['components'][n])
ca=after['components'][6]
ck('Filed reference withdrawal has no substitute invented form',ca['reference_scope']=='UNMAPPED' and 'component_id' not in ca and set(ca)=={'component_name','reference_scope','concentration_value','concentration_unit','source'})
oldassert=before['component_assertion']; newassert=after['component_assertion']
ck('Method and source-relative completeness retained',newassert['method']==oldassert['method']=='RECIPE_TRANSCRIPTION' and newassert['completeness']==oldassert['completeness']=='COMPLETE')
ck('Original recipe evidence unchanged',newassert['evidence'][0]==oldassert['evidence'][0])
ck('Crosswalk attribution identifiers and category preserved',all(newassert['evidence'][1][k]==oldassert['evidence'][1][k] for k in ('evidence_type','source','source_record')))
ck('Original blanket crosswalk note retained verbatim as history',oldassert['evidence'][1]['notes'] in event['changes'])
ck('One appended explicitly scoped evidence object',len(newassert['evidence'])==3 and newassert['evidence'][2]['source']=='https://www.ebi.ac.uk/chebi/CHEBI:31345' and 'not a new recipe input, owner identity or role assertion' in newassert['evidence'][2]['notes'])
ck('Original owner narrative retained',after['notes'].startswith(before['notes']))
ck('Mc table source boundary is explicit',all(t in newassert['notes'] for t in ['only the CultureBotHT Mc_vitamins','not a claim about carrier','do not inherit Mc D,L or per-litre','No water, phosphate, gas, titrant or X100 rescaling']))
old_decisions=j(OLD/'decisions.json')['decisions']; old=next(d for d in old_decisions if d['case_id']==CID)
old_proposals=j(OLD/'proposals.json')['proposals']; old_evidence=j(OLD/'evidence.json')['evidence']
ck('Original active populations and exact evidence prefix still baseline',len(old_decisions)==188 and len(old_proposals)==114 and len(old_evidence)==1101 and canon(old_evidence)==base['evidence_canonical_prefix_sha256'])
for k in ['case_id','case_input_sha256','source','occurrence_ids','disposition','no_change_reason','missing_requirement','publication_scope']: ck('Frozen case field preserved '+k,decision[k]==old[k])
ck('Six occurrence identities remain and one genuine trigger only',len(decision['occurrence_ids'])==6 and TRIGGER in decision['occurrence_ids'] and proposal['source_occurrence_ids']==[TRIGGER])
ck('Old four proposal links exact prefix plus genuine Mc origin',decision['proposal_ids']==old['proposal_ids']+[PID])
ck('Old case evidence exact prefix plus six new dependency records',decision['evidence_ids']==old['evidence_ids']+proposal['evidence_ids'] and len(proposal['evidence_ids'])==6)
ck('Existing owner preimages retained and authentic Mc appended',decision['owner_records']==old['owner_records']+[{'path':'data/ingredients/mapped/Mc_vitamins.yaml','sha256':BEFORE}])
ck('Original issue links retained',decision['issue_refs'][:len(old['issue_refs'])]==old['issue_refs'])
ck('Original reasoning and applicability retained as prefix',decision['reasoning'].startswith(old['reasoning']) and decision['applicability'].startswith(old['applicability']))
ck('Earlier peer record moved into prior lineage without approval reuse',decision['prior_independent_reviews']==old['prior_independent_reviews']+[old['independent_review']] and decision['independent_review']=={'status':'pending','evidence_ids':[]})
case_delta=[k for k in set(old)|set(decision) if old.get(k)!=decision.get(k)]
ck('Only justified case dependency fields changed',set(case_delta)=={'reasoning','applicability','evidence_ids','proposal_ids','owner_records','issue_refs','independent_review','prior_independent_reviews'})
ck('A new existing-owner origin retains correct original path and preimage',proposal['proposal_id']==PID and proposal['kind']=='edit_existing_owner' and proposal['owner_path']=='data/ingredients/mapped/Mc_vitamins.yaml' and proposal['before_sha256']==BEFORE and proposal['after_capture']=={'root':'artifact','path':'successors/issue-1237-mc-dependent-v1/payloads/Mc_vitamins.yaml','sha256':sha(afterraw)} and proposal['case_ids']==[CID])
ck('No new Mc source occurrence or winner claimed',proposal['mc_campaign_occurrence_count']==0 and 'Neither Mc nor CB is declared the exclusive owner' in proposal['description'] and 'pending the bounded W04/coordinator decision' in proposal['description'])
dep=j(O/'author/dependency.json'); assessment=j(O/'author/assessment.json')
ck('Dependency object is exact full proposal',dep['new_proposal']==proposal)
ck('Dependency six-case boundary exact',dep['all_six_occurrence_ids']==old['occurrence_ids'] and dep['trigger_occurrence']==TRIGGER and dep['source_envelope_counts']==recommendation['routing_envelope']['counts'] and dep['routing_status']=='PENDING_W04_CROSS_OWNER_DECISION')
ck('Author assessment describes actual delta',set(assessment['changed_top_level_fields'])==set(delta) and set(assessment['unchanged_top_level_fields'])==set(unchanged) and assessment['whole_owner_role_export_approval'] is False)
index=j(O/'inputs/source-ref-index.json')
for r in index['selected_captures']:
 ck('Exact original and copied source binding '+Path(r['published_path']).name,sha(raw(r['original_path']))==r['sha256']==sha(raw(W/r['published_path'])))
for r in index['native_contracts']: ck('Original native contract pin '+r['path'],sha(raw(W/r['path']))==r['sha256'])
route=j(O/'inputs/w09-continuity/source-routing-and-origin-bindings.json'); inherited=j(O/'inputs/w09-continuity/source-routing-inherited.json')
ck('Full inherited route unchanged by reference',sha(raw(O/'inputs/w09-continuity/source-routing-and-origin-bindings.json'))==base['W09_routing']['sha256'] and sha(raw(O/'inputs/w09-continuity/source-routing-inherited.json'))==base['W09_inherited_envelope']['sha256'])
ck('Actual envelope counts and separate KG list match baseline',route['counts']==dep['source_envelope_counts'] and canon(inherited['kg_cases'][0]['downstream_holds'])==base['KG84_hold_list_canonical_sha256'])
ck('Old114 exact origin objects and payloads remain untouched',all(canon(p)==b['canonical_proposal_sha256'] and sha(raw(A/p['after_capture']['path']))==b['after_capture']['sha256'] for p,b in zip(old_proposals,base['proposal_bindings'],strict=True)))
for p in [W/'MAPPING_SEMANTICS.md',W/'docs/record-reviews.md',W/'.claude/skills/reconcile-review-records/SKILL.md',P.parent/'inputs/issue1237-comment-6720042215-retry.json',P.parent/'inputs/issue1237-comment-6720201812-retry.json']: raw(p)
input_refs=list({(r['path'],r['sha256']):r for r in refs}.values())
dump('author-comparisons.json',{'at':datetime.now(timezone.utc).isoformat(),'reviewer':'worker08:/root/vitamins','checks':checks,'check_count':len(checks),'failures':[],'top_level_delta':sorted(delta),'case_delta':sorted(case_delta),'input_refs':input_refs})
review={
 'at':datetime.now(timezone.utc).isoformat(),'reviewer':'worker08:/root/vitamins','author':'worker08:/root','status':'PASS_WITH_SCOPE_LIMITS','review_type':'independent_lineage_and_dependency_binding','scientific_review':False,
 'independence':'Reviewer did not author this Mc payload, dependency proposal or changed case. Prior W08 vitamin/source research and CB technical validation are disclosed and are not independently reapproved here.',
 'case_ids':[CID],'proposal_ids':[PID],'full_payload_read':True,'beforeimage':ref(W/'data/ingredients/mapped/Mc_vitamins.yaml'),'payload':ref(O/'payloads/Mc_vitamins.yaml'),'proposal':ref(O/'author/proposal.json'),'decision':ref(O/'author/decision.json'),
 'case_hashes':{CID:canon(decision)},'payload_hashes':{PID:sha(afterraw)},'input_hashes':{r['path']:r['sha256'] for r in input_refs},
 'assessments':[
 {'area':'authentic_existing_owner','outcome':'supported','details':'The non-null 59c53 preimage is byte-identical to the maintained owner, the committed a0190fe owner and published beforeimage. Original identifier, raw synonym, mapping, roles, source statistics22 and all four complete history objects survive. The appended fifth event is attributed to current worker08 root and declares LLM assistance.'},
 {'area':'bounded_payload_delta','outcome':'supported_with_science_scope_limit','details':'Entire before/after payloads were read. All ten literal component names, order, concentration strings and units survive; nine other component objects are exact. Only the filed D/L-versus-D component reference is withdrawn, with UNMAPPED and literal source retained. The original blanket crosswalk note survives verbatim in history; operative note is qualified. Mc-only COMPLETE printed-list scope does not transfer DL, per-litre, carrier, gas or final-volume claims to JCM/NBRC. This comparison verifies implementation lineage, not a new independent judgment of the other nine chemical references.'},
 {'area':'genuine_dependency_case','outcome':'supported','details':'The proposal is a new edit_existing_owner origin tied to the existing six-occurrence Vitamin solution** case, with only its actual NBRC903 occurrence as trigger. Frozen case hash, source label, all six IDs and source partition are exact. Zero Mc campaign occurrences are claimed; no fabricated Mc case, actual occurrence association or exclusive owner winner is introduced.'},
 {'area':'historical_origin_preservation','outcome':'supported','details':'All original114 active proposal objects and their payload bytes remain exact at this author-review point, including the new-owner NBRC903 null beforeimage and genuine earlier CB dependent edit. The old1101 evidence rows remain exact. The new case preserves four prior proposal links and moves its prior peer receipt into explicit historical lineage; final peer status is pending.'},
 {'area':'external_tenvit_envelope','outcome':'preserved_pending_coordinator','details':'Exact original W09 active decision, HANDOFF, full route and inherited complete envelope are copied without restamping acquisition. Preparation review bound all8 current case objects,71 frozen CM occurrences/recipe pointers,84 separate KG hold objects and6 excluded contexts. This review rebinds the identical envelope and original source copies; it does not reinterpret65 nominal contexts as accepted owner routing.'},
 {'area':'nonterminal_cross_owner_routing','outcome':'retained','details':'Current W09 supports a common nominal Mc/JCM/NBRC recipe and explicitly recognizes generic CB nominal overlap. The authored Mc dependency preserves that positive nominal conclusion while leaving final cross-owner association pending W04/coordinator. No duplicate installation, merge, inherited role/export approval or independent approval of the reviewer\'s earlier CB work follows.'}
 ],
 'checks':{'author_metadata_check_count':len(checks),'all_pass':True,'comparison_receipt':ref(P/'author-comparisons.json'),'earlier_preparation_receipt':ref(P/'baseline-bindings.json'),'earlier_preparation_check_count':base['check_count']},
 'findings':[],'open_blocking_findings':[],
 'limitations':['Final115-proposal/188-case selector has not yet been reviewed; a separate final-bindings receipt must compare all114 original objects/payloads,187 other cases and1101 old evidence rows against the final assembled selection.','No native validator, SSSOM gate, live source retrieval or chemical/component revalidation performed in this lineage task. Source-copy hashing is not claimed as a fresh reading of every primary paper.','No final routing, maintained application, merge, role/export or whole-owner scientific approval. Filed SCI-TENVIT-003 is addressed by the isolated proposal; coordinator finding closure and source integration remain separate.'],
 'authoring_performed':False,'source_route_approval':False,'owner_merge_approval':False,'role_export_approval':False}
dump('review.json',review)
print(json.dumps({'status':review['status'],'checks':len(checks),'review_sha256':sha((P/'review.json').read_bytes()),'comparisons_sha256':sha((P/'author-comparisons.json').read_bytes())}))
