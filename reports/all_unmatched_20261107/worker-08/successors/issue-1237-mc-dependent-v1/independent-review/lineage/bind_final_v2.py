"""Read-only final selector binding. Writes only a new lineage receipt."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import json,hashlib,subprocess,yaml
W=Path.cwd(); P=Path(__file__).resolve().parent
A=W/'reports/all_unmatched_20261107/worker-08'; O=A/'successors/issue-1237-mc-dependent-v1'; OLD=A/'successors/issue-1237-tenvit-v1'
CID='CM_NAME:d57e91ffaea6f0ab6ff0f3d6f0b04c26356c832e85dd83e9e2319874fda43506'; PID='mc1237-prop-mc-vitamins-dependent'
H='a0190fed72b8f5119432003d1f9c84b8c1de7a48'; BEFORE='59c53dfe4e273ebfc7c3fe86fd4244978868ff1879dcde97af64bbeb61c07123'
checks=[]; refs=[]
def sha(b):return hashlib.sha256(b).hexdigest()
def canon(x):return sha(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
def raw(p):
 p=Path(p); b=p.read_bytes(); refs.append({'path':str(p),'sha256':sha(b)}); return b
def j(p):return json.loads(raw(p))
def ref(p):return {'path':str(p),'sha256':sha(raw(p))}
def ck(name,ok):checks.append({'check':name,'pass':bool(ok)}); assert ok,name
def dump(name,v):
 with (P/name).open('x') as f:json.dump(v,f,indent=2,ensure_ascii=False);f.write('\n')
base=j(P/'baseline-bindings.json'); review=j(P/'review.json')
ck('Sealed author-stage lineage review exact',sha(raw(P/'review.json'))=='82501cb11bd358747028340706e503512f9a5ca23272d20c8a3c5201111b6fb2')
s=j(O/'selection.json'); l=j(O/'lineage.json')
ck('Exact announced immutable final selector',sha(raw(O/'selection.json'))=='33f0f1f5166e75283a3e0488f6172844002919cc2461a04f2089f8c4f8fedab8')
ck('Actual predecessor head and selected predecessor retained',s['predecessor_head']==H and s['predecessor_selection']=={'root':'artifact','path':'successors/issue-1237-tenvit-v1/selection.json','sha256':'fb16bf5c29b981dc7dd60cf8d963a9aea25c12a65d6a0e55e29d84dfb2a26699'} and sha(raw(A/s['predecessor_selection']['path']))==s['predecessor_selection']['sha256'])
for pin in s['authoritative_inputs'].values():ck('Final full core pin '+pin['path'],sha(raw(A/pin['path']))==pin['sha256'])
oldsel=j(OLD/'selection.json')
for pin in oldsel['authoritative_inputs'].values():
 b=raw(A/pin['path']); ck('Authentic committed predecessor core '+pin['path'],sha(b)==pin['sha256'] and b==subprocess.check_output(['git','show',H+':'+str((A/pin['path']).relative_to(W))]))
d=j(O/'decisions.json')['decisions']; p=j(O/'proposals.json')['proposals']; e=j(O/'evidence.json')['evidence']
od=j(OLD/'decisions.json')['decisions']; op=j(OLD/'proposals.json')['proposals']; oe=j(OLD/'evidence.json')['evidence']
dm={x['case_id']:x for x in d}; odm={x['case_id']:x for x in od}; pm={x['proposal_id']:x for x in p}; opm={x['proposal_id']:x for x in op}
ck('All188 cases and original exact order retained',len(d)==len(dm)==188 and [x['case_id'] for x in d]==[x['case_id'] for x in od])
ck('Exact115 unique origins with one genuinely new dependent edit',len(p)==len(pm)==115 and set(pm)-set(opm)=={PID} and set(opm)-set(pm)==set())
ck('All320 occurrence identities and ordering retained',sum(len(x['occurrence_ids']) for x in d)==320 and [x['occurrence_ids'] for x in d]==[x['occurrence_ids'] for x in od])
case_rows=[]
for row in d:
 old=odm[row['case_id']]; unchanged=row==old
 ck('Exact case preservation or sole authorized dependency '+row['case_id'],unchanged==(row['case_id']!=CID))
 ck('Frozen source fields '+row['case_id'],all(row[k]==old[k] for k in ['case_id','case_input_sha256','source','occurrence_ids','disposition','no_change_reason','missing_requirement']))
 case_rows.append({'case_id':row['case_id'],'before_canonical_sha256':canon(old),'after_canonical_sha256':canon(row),'unchanged':unchanged,'case_input_sha256':row['case_input_sha256'],'occurrence_ids':row['occurrence_ids']})
ck('All old1101 evidence rows retained exact and only13 appended',len(e)==1114 and e[:1101]==oe and canon(oe)==base['evidence_canonical_prefix_sha256'])
ck('Unique final evidence IDs',len({x['evidence_id'] for x in e})==1114)
payload_rows=[]
for row in p:
 cap=row['after_capture']; actual=sha(raw(A/cap['path'])); ck('Actual final payload pin '+row['proposal_id'],actual==cap['sha256'])
 if row['proposal_id'] in opm: ck('Full original proposal object exact '+row['proposal_id'],row==opm[row['proposal_id']])
 payload_rows.append({'proposal_id':row['proposal_id'],'canonical_sha256':canon(row),'owner_path':row['owner_path'],'kind':row['kind'],'before_sha256':row['before_sha256'],'after_capture':cap,'original_proposal_object_unchanged':row==opm.get(row['proposal_id'])})
authd=j(O/'author/decision.json'); authp=j(O/'author/proposal.json'); finald=dm[CID]; finalp=pm[PID]
ck('Authored proposal and case still exact sealed inputs',sha(raw(O/'author/proposal.json'))==review['proposal']['sha256'] and sha(raw(O/'author/decision.json'))==review['decision']['sha256'])
ck('Final changed case scientific and source core exact',set(authd)==set(finald) and all(authd[k]==finald[k] for k in authd if k not in {'evidence_ids','independent_review'}))
ck('Final new proposal scientific source and lineage core exact',set(authp)==set(finalp) and all(authp[k]==finalp[k] for k in authp if k!='evidence_ids'))
extra=['mc1237-source-index','mc1237-publication-scope','mc1237-science','mc1237-lineage','mc1237-mixes','mc1237-cas-crosswalk','mc1237-chebi31345']
ck('Only seven actual evidence links appended',finald['evidence_ids']==authd['evidence_ids']+extra and finalp['evidence_ids']==authp['evidence_ids']+extra)
ck('Actual peer completion metadata only',finald['independent_review']=={'status':'complete','evidence_ids':['mc1237-science','mc1237-lineage']})
ck('All final case and proposal evidence references resolve',all(set(x['evidence_ids'])<={y['evidence_id'] for y in e} for x in d+p))
ck('New original Mc preimage actual and non-null',finalp['kind']=='edit_existing_owner' and finalp['before_sha256']==BEFORE==sha(raw(W/finalp['owner_path']))==sha(raw(O/'beforeimages/Mc_vitamins.yaml')))
ck('Mc payload remains exact reviewed bytes',finalp['after_capture']['sha256']==review['payload']['sha256']=='996fc2bfc69284abcbbe75fba6b069bc41fabb3e35c73d5a493de30ab153bcf3')
before=yaml.safe_load(raw(W/finalp['owner_path'])); after=yaml.safe_load(raw(A/finalp['after_capture']['path']))
ck('Actual four-event history prefix and fifth current event retained',len(after['curation_history'])==5 and after['curation_history'][:4]==before['curation_history'] and canon(before['curation_history'])==base['mc_history_canonical_sha256'])
ck('Distinct new origin invents zero cases or Mc occurrences',finalp['case_ids']==[CID] and finalp['source_occurrence_ids']==['CM_OCC:a181b24b7eb91c50c771bd1c1fc3012fd0cf28f45b49f2750c3d43bda9cdd531'] and finalp['mc_campaign_occurrence_count']==0)
ck('Earlier genuine CB dependent owner remains exact',pm['vm1237-prop-wolfe-cb-dependent']==opm['vm1237-prop-wolfe-cb-dependent'] and pm['vm1237-prop-wolfe-cb-dependent']['after_capture']['sha256']=='b64eccf46c271520c27c73bc0a5863e2bc56447d1acf7461a90e3d72f9f4384f')
ck('Earlier NBRC903 new-owner provenance remains exact',pm['vm1201-prop-nbrc903-vitamin']==opm['vm1201-prop-nbrc903-vitamin'] and pm['vm1201-prop-nbrc903-vitamin']['kind']=='new_owner' and pm['vm1201-prop-nbrc903-vitamin']['before_sha256'] is None)
for ev in e[1101:]:ck('Appended exact evidence capture '+ev['evidence_id'],sha(raw(A/ev['capture']['path']))==ev['capture']['sha256'])
for kind,r in s['independent_reviews'].items():ck('Actual peer receipt pin '+kind,sha(raw(A/r['path']))==r['sha256'])
ck('Copied lineage receipt exact original bytes',raw(A/s['independent_reviews']['lineage']['path'])==raw(P/'review.json'))
science=j(A/s['independent_reviews']['science']['path'])
ck('Separate science receipt binds exact authored case and payload',science['reviewer_identity']=='worker08:/root/organics' and science['author_identity']=='worker08:/root' and science['case_ids']==[CID] and science['proposal_ids']==[PID] and science['case_hashes'][CID]==canon(authd) and science['payload_hashes'][PID]==finalp['after_capture']['sha256'] and science['open_blocking_findings']==[])
env=O/'inputs/w09-continuity/source-routing-and-origin-bindings.json'; inh=O/'inputs/w09-continuity/source-routing-inherited.json'
route=j(env); inherited=j(inh)
ck('Exact full external envelope and inherited objects retained',sha(raw(env))==base['W09_routing']['sha256'] and sha(raw(inh))==base['W09_inherited_envelope']['sha256'])
ck('All8 current source cases remain in unchanged external route',len(route['cases'])==8 and [x['case_id'] for x in route['cases']]==[x['case_id'] for x in base['routing_cases']])
ck('Actual71 occurrence objects and6 exclusions preserved',len(inherited['occurrences'])==71 and all(canon(o['full_frozen_occurrence'])==o['occurrence_object_canonical_sha256'] for o in inherited['occurrences']) and sum(o['relation'].startswith('excluded_') for o in inherited['occurrences'])==6)
ck('Actual84 separate KG holds exact',len(inherited['kg_cases'][0]['downstream_holds'])==84 and canon(inherited['kg_cases'][0]['downstream_holds'])==base['KG84_hold_list_canonical_sha256'])
ck('Actual envelope partition still exact',dict(Counter(o['relation'] for o in inherited['occurrences']))==route['partitions'])
ck('Final selector external envelope counts truthful',s['external_source_envelope_counts']==route['counts']=={'cases':8,'CM_occurrences':71,'separate_KG_holds':84,'excluded_contexts':6,'nominal_context_upper_bound':65})
for k in ['effective_source_ref_index','thesis_publication_scope','dependency']:ck('Final selected adjunct pin '+k,sha(raw(A/s[k]['path']))==s[k]['sha256'])
rel=j(A/s['thesis_publication_scope']['path']); idx=j(A/s['effective_source_ref_index']['path']); oldidx=j(O/'inputs/source-ref-index.json')
ck('Only two source location records updated',len(idx['selected_captures'])==len(oldidx['selected_captures']) and sum(a!=b for a,b in zip(idx['selected_captures'],oldidx['selected_captures'],strict=True))==2 and all(idx[k]==oldidx[k] for k in oldidx if k!='selected_captures'))
for r in rel['relocations']:
 ck('Thesis exact private bytes and original preserved '+Path(r['private_exact_capture']).suffix,sha(raw(r['private_exact_capture']))==sha(raw(r['original_path']))==r['sha256'])
 oldpath=W/r['previous_unpublished_copy_path']; ck('Exact former public fulltext path absent without ignoring hidden files '+oldpath.name,not oldpath.exists() and not oldpath.is_symlink())
 matches=[x for x in idx['selected_captures'] if x['original_path']==r['original_path']]
 ck('Effective index points to actual private thesis '+oldpath.name,len(matches)==1 and matches[0]['private_capture_path']==r['private_exact_capture'] and matches[0]['sha256']==r['sha256'] and 'published_path' not in matches[0])
ck('Thesis acquisition and bounded read scope explicit',rel['original_acquired_at']=='2026-11-08T09:54:47.947617+00:00' and rel['read_scope']=='Printed pages28–29 only, not whole-paper inspection.')
for r in idx['selected_captures']:
 dest=Path(r['private_capture_path']) if 'private_capture_path' in r else W/r['published_path']
 ck('Effective source-copy pin '+dest.name,sha(raw(dest))==r['sha256'])
counts={'cases':len(d),'proposals':len(p),'occurrence_ids':sum(len(x['occurrence_ids']) for x in d),'evidence':len(e),'unchanged_original_payloads':len(op),'changed_original_payloads':0,'new_dependent_payloads':1,'new_owner_proposals':0,'changed_cases':sum(dm[k]!=odm[k] for k in dm),'unchanged_cases':sum(dm[k]==odm[k] for k in dm),'new_cases':0,'mc_campaign_occurrences':finalp['mc_campaign_occurrence_count']}
ck('Final declared counts exact actual populations',s['counts']==l['counts']==counts)
lc={x['case_id']:x for x in l['cases']}
ck('Complete188-case lineage table exact',len(lc)==188 and all(lc[x['case_id']]['before_sha256']==x['before_canonical_sha256'] and lc[x['case_id']]['after_sha256']==x['after_canonical_sha256'] and lc[x['case_id']]['unchanged']==x['unchanged'] and lc[x['case_id']]['case_input_sha256']==x['case_input_sha256'] and lc[x['case_id']]['occurrence_ids']==x['occurrence_ids'] for x in case_rows))
lp={x['proposal_id']:x for x in l['payloads']}
ck('Complete115-proposal lineage table exact',len(lp)==115 and all(lp[x['proposal_id']]['selected_capture']==x['after_capture'] and lp[x['proposal_id']]['original_before_sha256']==x['before_sha256'] for x in payload_rows))
ck('Nonterminal scopes retained in final selector',s['cross_owner_routing']=='PENDING_W04_CROSS_OWNER_DECISION' and s['coordinator_final_head_acceptance']=='pending' and s['maintained_application'] is False and s['whole_owner_role_export_approval'] is False and s['prior_TSB_Bacto_admission']=='FAILED/HELD unchanged' and l['release_approval'] is False)
receipt={'at':datetime.now(timezone.utc).isoformat(),'reviewer':'worker08:/root/vitamins','assembly_author':'worker08:/root','status':'PASS_WITH_SCOPE_LIMITS','review_type':'final_selector_lineage_binding','scientific_review':False,
 'independence':'No authoring of Mc payload or selector. Earlier W08 source/CB authorship remains disclosed; these checks do not independently approve that science.',
 'selection':ref(O/'selection.json'),'authoritative_inputs':s['authoritative_inputs'],'prior_review':ref(P/'review.json'),'final_counts':counts,'external_source_envelope_counts':route['counts'],
 'case_ids':[CID],'proposal_ids':[PID],'author_case_sha256':sha(raw(O/'author/decision.json')),'author_proposal_sha256':sha(raw(O/'author/proposal.json')),'final_case_canonical_sha256':canon(finald),'final_proposal_canonical_sha256':canon(finalp),'new_payload_sha256':finalp['after_capture']['sha256'],
 'case_bindings':case_rows,'proposal_bindings':payload_rows,'old_evidence_canonical_prefix_sha256':canon(e[:1101]),'appended_evidence_ids':[x['evidence_id'] for x in e[1101:]],
 'checks':checks,'check_count':len(checks),'failures':[],'findings':[],'open_blocking_findings':[],
 'retained_attempts':[ref(P/'final-binding-attempt1.json'),ref(P/'bind_final.py')],
 'input_refs':list({(r['path'],r['sha256']):r for r in refs}.values()),
 'assessment':'All188 existing cases retain exact frozen source fields and320 occurrence identities.187 case objects are exact; the sole changed case differs from its reviewed authored version only by seven appended evidence links and actual completed peer metadata. All114 older proposal objects and payloads remain exact, including CB and NBRC903; one new genuine Mc edit has the actual maintained59c53 preimage. The1101 older evidence rows remain exact and13 evidence entries are appended. Original4 Mc history events survive in the same reviewed996fc2 payload. The full8/71/84/6 external envelope remains exact by original objects/capture pins, without65-context route approval. Thesis full bytes remain identical privately, with a truthful location-only successor and original acquisition metadata.',
 'limitations':['No fresh chemical, source-science, native-schema or SSSOM validation is claimed. Other187 cases and114 payloads have preservation coverage, not renewed scientific appraisal.','The external route intentionally remains the exact earlier reference snapshot. Its W08 source-case scientific core remains unchanged; final bookkeeping is bound here rather than rewriting upstream historical receipts.','This receipt does not elect Mc or CB, approve duplicates/merges, release source/role/export holds, apply maintained changes, or grant coordinator final-head acceptance.'],
 'maintained_application':False,'source_route_approval':False,'owner_merge_approval':False,'role_export_approval':False}
dump('final-bindings.json',receipt)
print(json.dumps({'status':receipt['status'],'checks':len(checks),'counts':counts,'receipt_sha256':sha((P/'final-bindings.json').read_bytes())}))
