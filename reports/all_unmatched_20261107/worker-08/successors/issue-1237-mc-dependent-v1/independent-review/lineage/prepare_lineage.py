"""Independent lineage proposal only; no payload, selector or science authorship."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import json,hashlib,subprocess,yaml
W=Path.cwd();P=Path(__file__).absolute().parent
C=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
R=C/'workers/w09/worktree/.temp/tenvit-mc-continuity-decision-v1'
A=W/'reports/all_unmatched_20261107/worker-08';O=A/'successors/issue-1237-tenvit-v1'
H='a0190fed72b8f5119432003d1f9c84b8c1de7a48';H6='0d7fde51fb3109b10424dd3bcf4091c05aa900e7'
CID='CM_NAME:d57e91ffaea6f0ab6ff0f3d6f0b04c26356c832e85dd83e9e2319874fda43506'
TRIGGER='CM_OCC:a181b24b7eb91c50c771bd1c1fc3012fd0cf28f45b49f2750c3d43bda9cdd531'
refs=[];checks=[]
def sha(b):return hashlib.sha256(b).hexdigest()
def canon(x):return sha(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
def read(p):
 p=Path(p);b=p.read_bytes();refs.append({'path':str(p),'sha256':sha(b)});return b
def rj(p):return json.loads(read(p))
def rf(p):b=read(p);return {'path':str(p),'sha256':sha(b)}
def gb(head,path):
 b=subprocess.check_output(['git','show',head+':'+path],cwd=W);refs.append({'head':head,'path':path,'sha256':sha(b)});return b
def check(name,ok):checks.append({'check':name,'pass':bool(ok)});assert ok,name
def dump(name,v):
 with (P/name).open('x') as f:json.dump(v,f,indent=2,ensure_ascii=False);f.write('\n')
at=datetime.now(timezone.utc).isoformat()
handoff=rj(R/'HANDOFF.json');decision=rj(R/'decision-v2.json');suggestions=rj(R/'candidate-suggestions.json')
routing=rj(R/'source-routing-and-origin-bindings.json');inherited=rj(R/'source-routing-inherited.json')
check('Active W09 decision and route pins',sha(read(R/'decision-v2.json'))==handoff['active_decision']['sha256'] and sha(read(R/'source-routing-and-origin-bindings.json'))==handoff['routing']['sha256'])
check('Candidate-suggestion and inherited envelope pins',sha(read(R/'candidate-suggestions.json'))==handoff['candidate_suggestions']['sha256'] and sha(read(R/'source-routing-inherited.json'))==routing['inherited_route']['sha256'])
ownerpath='data/ingredients/mapped/Mc_vitamins.yaml';ownerraw=read(W/ownerpath);owner=yaml.safe_load(ownerraw)
check('Authentic maintained and committed Mc beforeimage',sha(ownerraw)=='59c53dfe4e273ebfc7c3fe86fd4244978868ff1879dcde97af64bbeb61c07123' and ownerraw==gb(H,ownerpath)==read(R/'inputs/owners/Mc_vitamins.yaml'))
check('Four-event history exact W09 anchor',len(owner['curation_history'])==4 and canon(owner['curation_history'])==suggestions['anchor']['original_history_canonical_sha256'])
check('Authentic owner identifier and historical count',owner['identifier']=='kgmicrobe.ingredient:mc_vitamins' and owner['occurrence_statistics']=={'total_occurrences':22,'media_count':22})
selection=rj(O/'selection.json');decisions=rj(O/'decisions.json')['decisions'];proposals=rj(O/'proposals.json')['proposals'];evidence=rj(O/'evidence.json')['evidence']
check('Exact current W08 selector',sha(read(O/'selection.json'))=='fb16bf5c29b981dc7dd60cf8d963a9aea25c12a65d6a0e55e29d84dfb2a26699')
for v in selection['authoritative_inputs'].values():check('Current core pin '+v['path'],sha(read(A/v['path']))==v['sha256'])
check('Current188/114/1101 population',len(decisions)==188 and len(proposals)==114 and len(evidence)==1101)
current=next(d for d in decisions if d['case_id']==CID)
shard8=rj(C/'queue/preliminary-v5/shards/shard-08.json')['cases'];shard6=rj(C/'queue/preliminary-v5/shards/shard-06.json')['cases']
cases={d['case_id']:d for d in shard6+shard8}
case=cases[CID]
check('Authentic frozen case input',canon(case)==current['case_input_sha256']=='1c8fdd449fe96f1f9a8599fe72941fcf09ef4d0e68a5134be4fdf52b416d9868')
source6=json.loads(gb(H6,'reports/all_unmatched_20261107/worker-06/successor-v5/decisions.json'))['decisions']
currentcases={d['case_id']:d for d in source6+decisions};cledger=[]
for c in routing['cases']:
 cid=c['case_id'];check('Routing complete current decision '+cid,c['complete_current_decision']==currentcases[cid] and canon(currentcases[cid])==c['current_decision_sha256'])
 check('Routing frozen case '+cid,canon(cases[cid])==c['frozen_case_sha256'])
 cledger.append({'case_id':cid,'case_input_sha256':canon(cases[cid]),'current_decision_sha256':canon(currentcases[cid]),'occurrence_ids':currentcases[cid]['occurrence_ids'],'dependency_only':True,'routing_release':False})
check('Eight-case71CM84KG6exclusion envelope unchanged',routing['counts']==inherited['counts']=={'cases':8,'CM_occurrences':71,'separate_KG_holds':84,'excluded_contexts':6,'nominal_context_upper_bound':65})
check('Actual71CM occurrence objects',len(inherited['occurrences'])==len({o['occurrence_id'] for o in inherited['occurrences']})==71)
check('Actual84 separateKG hold objects',len(inherited['kg_cases'])==1 and len(inherited['kg_cases'][0]['downstream_holds'])==84)
check('Actual occurrence partition',dict(Counter(o['relation'] for o in inherited['occurrences']))==routing['partitions'])
occ=[]
for o in inherited['occurrences']:
 check('Frozen occurrence canonical pin '+o['occurrence_id'],canon(o['full_frozen_occurrence'])==o['occurrence_object_canonical_sha256'])
 recipe=Path(o['complete_source_recipe']['source_path']);raw=read(recipe)
 check('Complete frozen recipe pin '+o['occurrence_id'],sha(raw)==o['complete_source_recipe']['sha256'])
 node=yaml.safe_load(raw)
 for tok in o['full_frozen_occurrence']['component_path'].split('/'):
  node=node[int(tok)] if isinstance(node,list) else node[tok]
 check('Actual raw recipe pointer '+o['occurrence_id'],node==o['full_frozen_occurrence']['raw_component'])
 occ.append({'case_id':o['case_id'],'occurrence_id':o['occurrence_id'],'canonical_sha256':canon(o['full_frozen_occurrence']),'source_path':str(recipe),'source_sha256':sha(raw),'component_path':o['full_frozen_occurrence']['component_path'],'relation':o['relation'],'owner_continuity_release':o['owner_continuity_release']})
six=[o for o in occ if o['case_id']==CID]
check('Six exact mixed-case occurrences and one NBRC903 trigger',[o['occurrence_id'] for o in six]==current['occurrence_ids'] and len(six)==6 and [o['occurrence_id'] for o in six if o['relation']=='nominal_NBRC903_context']==[TRIGGER])
payloads=[]
for p in proposals:
 check('Existing origin payload pin '+p['proposal_id'],sha(read(A/p['after_capture']['path']))==p['after_capture']['sha256'])
 payloads.append({'proposal_id':p['proposal_id'],'canonical_proposal_sha256':canon(p),'owner_path':p['owner_path'],'kind':p['kind'],'before_sha256':p['before_sha256'],'after_capture':p['after_capture']})
check('No preexisting Mc proposed owner in complete114 selection',all(p['owner_path']!=ownerpath for p in proposals))
check('Authentic three tenvit origin captures',all(sha(gb(o['head'],o['payload_path']))==o['payload_sha256']==sha(read(R/o['private_payload'])) for o in routing['origins']))
dump('baseline-bindings.json',{'at':at,'reviewer':'worker08:/root/vitamins','scope':'Lineage and source-boundary metadata; no renewed source science or prior own CB approval.',
 'w08_head':H,'current_selection':rf(O/'selection.json'),'case_bindings':[{'case_id':d['case_id'],'canonical_sha256':canon(d)} for d in decisions],
 'proposal_bindings':payloads,'evidence_index':rf(O/'evidence.json'),'evidence_canonical_prefix_sha256':canon(evidence),
 'mc_beforeimage':rf(W/ownerpath),'mc_history_canonical_sha256':canon(owner['curation_history']),'mc_history_events':owner['curation_history'],
 'routing_cases':cledger,'all71_occurrence_bindings':occ,'KG84_hold_list_canonical_sha256':canon(inherited['kg_cases'][0]['downstream_holds']),
 'W09_active_handoff':rf(R/'HANDOFF.json'),'W09_active_decision':rf(R/'decision-v2.json'),'W09_routing':rf(R/'source-routing-and-origin-bindings.json'),'W09_inherited_envelope':rf(R/'source-routing-inherited.json'),
 'checks':checks,'check_count':len(checks),'failures':[]})
dump('binding-recommendation.json',{'status':'supported_metadata_route_pending_exact_author_bytes','reviewer':'worker08:/root/vitamins',
 'independence':'Not author of the forthcoming Mc edit or selector. Prior W08 vitamin/source research and CB technical work disclosed; neither is independently reapproved here.',
 'new_origin_required':{'kind':'edit_existing_owner','owner_path':ownerpath,'before_sha256':sha(ownerraw),'identifier_unchanged':owner['identifier'],'proposal_id':'A distinct new Mc-dependent proposal ID chosen by accountable author; do not relabel an original NBRC903 or CB proposal.',
 'case_ids':[CID],'source_occurrence_ids':[TRIGGER],'case_input_sha256':current['case_input_sha256'],'source_scope':'Dependency correction exposed by the NBRC903 nominal-ten comparison; no statement that the actual NBRC occurrence is an Mc or CB stock.',
 'new_source_case_count':0,'new_claimed_Mc_campaign_occurrence_count':0,'preserved_Mc_historical_count':22,'prior_four_history_events_must_be_exact':True},
 'necessary_case_delta':{'case_id':CID,'preserve_fields':['case_id','case_input_sha256','source','occurrence_ids','disposition','no_change_reason','missing_requirement'],
 'preserve_all_existing_proposal_ids':current['proposal_ids'],'append_new_proposal_id':True,'owner_records_append_only':{'path':ownerpath,'sha256':sha(ownerraw)},
 'prose':'Append bounded dependency rationale and explicit current nominal overlap without rewriting source forms, doses, child holds or claiming an installed owner. Mc-only table stays Mc-only. Existing older comparison statements remain historical and explicitly superseded where applicable.',
 'evidence_and_peer_bookkeeping':'Append new evidence and separate exact final peer binding; retain all earlier references and prior review lineage.'},
 'whole_shard_preservation':{'cases':188,'case_occurrences':320,'old_proposal_objects_exact':114,'old_evidence_rows_exact_prefix':1101,'expected_new_total_proposals':115,'unchanged_other_cases':187},
 'routing_envelope':{'source':rf(R/'source-routing-and-origin-bindings.json'),'full_objects':rf(R/'source-routing-inherited.json'),'counts':routing['counts'],'partitions':routing['partitions'],'all_six_exclusions_preserved':True,'separate_KG_holds_preserved':84,'owner_route_release':False},
 'nonterminal_integration':'W04/coordinator source routing and final cross-owner association remain pending. Common nominal preparation is supported by the active W09 decision; unknown lots or unspecified child forms do not create an indefinite nominal-recipe hold. Neither Mc nor CB is selected as an exclusive winner; do not install them as newly justified duplicates or merge maintained owners.',
 'retained_original_origins':[{'proposal_id':p['proposal_id'],'kind':p['kind'],'before_sha256':p['before_sha256'],'after_capture':p['after_capture']} for p in proposals if p['proposal_id'] in ['vm1201-prop-nbrc903-vitamin','vm1237-prop-wolfe-cb-dependent']],
 'final_review_pending':['entire authored Mc payload and four-event history prefix','exact changed decision and new proposal','all188 cases114 old origins and1101 old evidence prefix','frozen W09 active decision/current envelope capture references'],
 'new_findings':[],'scientific_approval':False,'source_route_approval':False,'owner_merge_approval':False,'role_export_approval':False,'authoring_performed':False})
refs_by_key={(r.get('head'),r['path']):r for r in refs};dump('input-refs.json',list(refs_by_key.values()))
print(json.dumps({'checks':len(checks),'baseline_sha256':sha((P/'baseline-bindings.json').read_bytes()),'recommendation_sha256':sha((P/'binding-recommendation.json').read_bytes()),'reference_count':len(refs_by_key)}))
