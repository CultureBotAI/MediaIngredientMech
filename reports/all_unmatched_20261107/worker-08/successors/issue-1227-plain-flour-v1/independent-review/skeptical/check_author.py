"""Independent bounded author-byte and predecessor-lineage checks only."""
import datetime
import hashlib
import json
from pathlib import Path
import yaml

R = Path('reports/all_unmatched_20261107/worker-08')
B = R/'successors/issue-1227-v1/final-v2'
S = R/'successors/issue-1227-plain-flour-v1'
O = Path('.temp/all-unmatched-worker-08/plain-flour-method-v1/independent/skeptical')
PID = 'op1201-plain-flour'
CID = 'KG_CASE:b9a6261315d83792bc02bfbe425cda2032c8833c7a3b6de3aa665fa62a7fc03e'
checks = []
inputs = {}
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
    inputs[str(p)] = sha(p)
    return json.loads(Path(p).read_text())
def yy(p):
    inputs[str(p)] = sha(p)
    return yaml.safe_load(Path(p).read_text())
def check(name, condition): checks.append({'check':name,'passed':bool(condition)})
def canon(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()

oldps = read(B/'proposals.json')['proposals']
oldds = read(B/'decisions.json')['decisions']
oldp = next(x for x in oldps if x['proposal_id']==PID)
oldd = next(x for x in oldds if x['case_id']==CID)
p = read(S/'author/proposal.json'); d = read(S/'author/decision.json')
a = read(S/'author/assessment.json'); label = read(S/'research/primary-label-resolution.json')
old = yy(R/oldp['after_capture']['path']); new = yy(R/p['after_capture']['path'])
before = yy(Path(p['owner_path']))
query = read(O/'independent-label-query.json')
check('announced successor hash', sha(R/p['after_capture']['path']) == p['after_capture']['sha256'] == '884fee1ea6a5082a51b8769f2a827199b1703972ad80fa48e1bb8d2d09ab3873')
check('original frozen before hash retained', sha(p['owner_path']) == p['before_sha256'] == oldp['before_sha256'] == 'becb2e4860868161607a709d6c4b5cbef56c2b4a3e06c9a4fc9214e35e4e9a8e')
check('exact selected predecessor retained', sha(R/oldp['after_capture']['path']) == oldp['after_capture']['sha256'] == 'aa8390f17f1ed9f9c083fd6b487ee1c40228e754072b7e390b97dfb2fd6eae83')
check('only five allowed top-level field deltas', {k for k in set(old)|set(new) if old.get(k)!=new.get(k)} == {'preferred_term','notes','ontology_mapping','curation_history'})
for k in ['identifier','synonyms','mapping_status','occurrence_statistics','ingredient_type']:
    check('whole-payload unchanged '+k, new[k]==old[k])
check('old five history events preserved', len(old['curation_history'])==5 and len(new['curation_history'])==6 and new['curation_history'][:5]==old['curation_history'])
check('original three baseline events retained', new['curation_history'][:3]==before['curation_history'])
ev = new['curation_history'][-1]
check('new truthful root event and mapped transition', ev['curator']=='worker08:/root W08-FINAL-001 proposal correction' and ev['llm_assisted'] is True and ev['previous_status']==ev['new_status']=='MAPPED' and 'earlier EXACT_MATCH' in ev['changes'] and 'new native primary-label resolution' in ev['changes'])
check('notes append without rewriting history', new['notes'].startswith(old['notes']))
check('primary label adopted', new['preferred_term']==new['ontology_mapping']['ontology_label']==label['native_adapter_label']=='flour')
check('same ontology own identity and grade', new['identifier']==new['ontology_mapping']['ontology_id']==old['identifier']=='FOODON:00004510' and new['ontology_mapping']['mapping_quality']==old['ontology_mapping']['mapping_quality']=='EXACT_MATCH')
check('only mapping evidence changed', {k:v for k,v in old['ontology_mapping'].items() if k!='evidence'} == {k:v for k,v in new['ontology_mapping'].items() if k!='evidence'})
check('fact and agent interpretation distinct', [e['evidence_type'] for e in new['ontology_mapping']['evidence']]==['DATABASE_MATCH','LLM_SUGGESTION'])
check('database provenance retained', new['ontology_mapping']['evidence'][0]['source']==old['ontology_mapping']['evidence'][0]['source'])
check('no new role/component/structure/CAS assertions', all(k not in new and k not in old for k in ['components','roles','chemical_properties','supplied_form']))
check('new primary-label query independently reproduced', query['database']['sha256']==label['database']['sha256'] and query['rows']==label['rows'])
check('exact unique primary label rather than synonym fallback', [r['subject'] for r in query['rows'] if r['predicate']=='rdfs:label' and r['value']=='flour']==['FOODON:00004510'] and not any(r['value']=='plain flour' for r in query['rows']))
check('old primary capture/time retained', label['original_primary_capture']['sha256']=='48c4ece85b7193af6fee377601cc481e86a02b92ae637534a9fd1baf53315c98' and label['original_primary_accessed_at']=='2026-11-08T05:57:13.916914+00:00' and label['CAS_lookup_performed'] is False and label['raw_source_label_is_established_ontology_synonym'] is False)
check('proposal stable original assignment', all(p[k]==oldp[k] for k in ['proposal_id','case_ids','owner_path','kind','before_sha256']))
check('old evidence backlinks retained and four new added', p['evidence_ids'][:len(oldp['evidence_ids'])]==oldp['evidence_ids'] and len(p['evidence_ids'])==len(oldp['evidence_ids'])+4)
for k in ['case_id','case_input_sha256','source','occurrence_ids','disposition','applicability','proposal_ids','no_change_reason','missing_requirement','owner_records','preserved_native_decisions']:
    check('case source/hold field unchanged '+k,d[k]==oldd[k])
check('prior peer acceptance made historical, current review pending', d['independent_review']=={'status':'pending','evidence_ids':[]} and d['prior_independent_reviews']==oldd['prior_independent_reviews']+[oldd['independent_review']] and 'worker08:/root;' in d['primary_reviewer'])
check('current author no release approval', a['scientific_release_approval'] is False)
check('baseline188/113/320 precise scope', len(oldds)==188 and len(oldps)==113 and sum(len(r['occurrence_ids']) for r in oldds)==320 and len({o for r in oldds for o in r['occurrence_ids']})==320)
for row in oldps:
    cap=row['after_capture']; check('predecessor payload unchanged '+row['proposal_id'],sha(R/cap['path'])==cap['sha256'])
for row in oldps:
    if row['proposal_id']!=PID:
        obj=yy(R/row['after_capture']['path'])
        check('no second selected flour identity '+row['proposal_id'],obj['identifier']!='FOODON:00004510')
check('all input bytes unchanged through check',all(sha(k)==v for k,v in inputs.items()))
result={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS' if all(x['passed'] for x in checks) else 'FAIL','checks':checks,'check_count':len(checks),'failures':[x for x in checks if not x['passed']],'input_hashes':inputs,'authored_case_hash':canon(d),'payload_hash':p['after_capture']['sha256'],'final_113_188_assembly':'Not yet supplied; this receipt binds the author candidate and exact unchanged predecessor inputs. Final assembly requires separate readback.','scope':'No maintained edits, exports, native expensive validation replay, or approval of unrelated science.'}
(O/'author-validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['checks','input_hashes']},indent=2))
