import datetime
import hashlib
import json
from pathlib import Path
import yaml

R = Path.cwd()
A = R / 'reports/all_unmatched_20261107/worker-10'
S = A / 'successor-v2'
C = R.parents[2]
Q = C / 'queue/preliminary-v5'
P = R / '.temp/all-unmatched-worker-10/successor-v2/skeptic'
H = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
J = lambda p: json.loads(Path(p).read_text())
Y = lambda p: yaml.safe_load(Path(p).read_text())
CH = lambda x: hashlib.sha256(json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest()
checks = []
inputs = {}
def inp(p):
    p = Path(p)
    inputs[str(p)] = H(p)
    return p
def check(name, condition, evidence=None):
    checks.append({'name': name, 'pass': bool(condition), 'evidence': evidence})
def capture(c):
    root = {'artifact': A, 'source': Q, 'repository': R, 'repo': R}[c['root']]
    p = root / c['path']
    inp(p)
    check('capture hash: '+c['path'], H(p) == c['sha256'])

cases = J(inp(Q / 'shards/shard-10.json'))['cases']
oldD = {x['case_id']: x for x in J(inp(A/'successor-v1/decisions.json'))['decisions']}
oldP = {x['proposal_id']: x for x in J(inp(A/'successor-v1/proposals.json'))['proposals']}
oldE = {x['evidence_id']: x for x in J(inp(A/'successor-v1/evidence.json'))['evidence']}
newD = [J(inp(S/g/'decision-fragment.json')) for g in ['isp4','carbonate']]
ip = J(inp(S/'isp4/proposals-fragment.json'))['proposals'][0]
cp = J(inp(S/'carbonate/proposal-fragment.json'))
newP = [ip, cp]
newE = sum([J(inp(S/g/'evidence-fragment.json'))['evidence'] for g in ['isp4','carbonate']], [])
for x in newE:
    capture(x['capture'])
check('new evidence IDs unique and absent from old ledger', len({x['evidence_id'] for x in newE})==len(newE) and not(set(oldE)&{x['evidence_id'] for x in newE}))
allE = oldE | {x['evidence_id']:x for x in newE}
for d, idx in zip(newD, [143, 187]):
    before = oldD[d['case_id']]
    check('case and full raw case hash '+str(idx), d['case_id'] == cases[idx]['case_id'] and d['case_input_sha256'] == CH(cases[idx]))
    for key in ['case_id','case_input_sha256','source','occurrence_ids','disposition','no_change_reason','owner_records','source_index','release_authorization','preserved_hold_scope']:
        check('retained case field '+str(idx)+' '+key, d.get(key)==before.get(key))
    check('prior evidence preserved '+str(idx),set(before['evidence_ids'])<=set(d['evidence_ids']))
    check('valid evidence backlinks '+str(idx),set(d['evidence_ids'])<=set(allE))
for p in newP:
    capture(p['after_capture'])
    check('valid proposal evidence '+p['proposal_id'],set(p['evidence_ids'])<=set(allE))

before = Y(inp(R/ip['owner_path']))
prior = Y(inp(A/'kg/proposed/isp4-remove-salt-parent.yaml'))
isp = Y(inp(A/ip['after_capture']['path']))
check('ISP4 authentic maintained preimage', H(R/ip['owner_path'])==ip['before_sha256']=='76a430265f543685167823888f68629d2cbfc652f6faced54387692517118178')
check('ISP4 preserves authentic history and parent removal history', isp['curation_history'][:len(prior['curation_history'])]==prior['curation_history'] and prior['curation_history'][:len(before['curation_history'])]==before['curation_history'] and len(isp['curation_history'])==len(prior['curation_history'])+1)
for k in ['preferred_term','synonyms','occurrence_statistics','ingredient_type']:
    check('ISP4 authentic field '+k, isp[k]==before[k])
check('ISP4 own local identity no chemical parent',isp['identifier']=='kgmicrobe.ingredient:inorganic_salts_starch_agar' and isp['ontology_mapping']['ontology_id']==isp['identifier'] and isp['ontology_mapping']['mapping_quality']=='FALLBACK_REGISTRY')
expected = [('Soluble starch','10.0','G','UNMAPPED',None),('K2HPO4','1.0','G','UNMAPPED',None),('MgSO4 x 7 H2O','1.0','G','MIM_CATALOG','CHEBI:31795'),('NaCl','1.0','G','MIM_CATALOG','CHEBI:26710'),('(NH4)2SO4','2.0','G','MIM_CATALOG','CHEBI:62946'),('CaCO3','2.0','G','MIM_CATALOG','CHEBI:3311'),('Trace salts solution (JCM 58)','1.0','ML','UNMAPPED',None),('Agar','20.0','G','MIM_CATALOG','CHEBI:2509'),('Distilled water','1.0','L','MIM_CATALOG','CHEBI:15377')]
actual = [tuple(x.get(k) for k in ['component_name','concentration_value','concentration_unit','reference_scope','component_id']) for x in isp['components']]
check('ISP4 exact independently transcribed nine immediate input tuples',actual==expected,actual)
check('ISP4 complete source-list assertion',isp['component_assertion']['method']=='RECIPE_TRANSCRIPTION' and isp['component_assertion']['completeness']=='COMPLETE')
check('ISP4 no manual human evidence claim',all(x.get('evidence_type')!='MANUAL_CURATION' for x in isp['ontology_mapping']['evidence']+isp['component_assertion']['evidence']))
lookup = J(inp(S/'isp4/component-owner-lookups.json'))
for x in lookup['records']:
    p=inp(R/x['path'])
    check('native component record snapshot '+x['path'],H(p)==x['sha256'] and Y(p)==x['record'])

stock = oldP[cp['proposal_id']]
check('carbonate unchanged stock payload, identity and original metadata', all(cp.get(k)==stock.get(k) for k in ['proposal_id','owner_path','kind','after_capture','before_sha256','identity_predicate_consequences','publication_review_obligations','cross_shard_conflicts','publication_holds','independent_review']))
check('carbonate exactly case21 and case187 binding',cp['case_ids']==[cases[21]['case_id'],cases[187]['case_id']])
check('carbonate original evidence retained',set(stock['evidence_ids'])<=set(cp['evidence_ids']))
check('carbonate one existing stock and old pure alias rejection',newD[1]['proposal_ids']==['kg-carbonate-buffer-alias',cp['proposal_id']])
capture(oldP['kg-carbonate-buffer-alias']['after_capture'])
stockY=Y(inp(A/cp['after_capture']['path']))
aliasY=Y(inp(A/oldP['kg-carbonate-buffer-alias']['after_capture']['path']))
check('carbonate stock retains partial two named components',stockY['component_assertion']['completeness']=='PARTIAL' and len(stockY['components'])==2 and all(x['reference_scope']=='UNMAPPED' and 'concentration_value' not in x for x in stockY['components']))
check('carbonate buffer alias remains rejected on pure owner',any(x['synonym_text']=='Na2CO3-CO2 buffer' and x['synonym_type']=='REJECTED_LABEL' for x in aliasY['synonyms']))
md=J(inp(A/'kg/captures/mdJ209.json'))
mi=J(inp(A/'kg/captures/md1685.json'))
to=J(inp(A/'buffers/captures/2b7e3ee4d3ec3dfb08be.json'))
check('ingredient1685 exact J209 bridge',mi['data']['id']==1685 and mi['data']['media']==['J209'])
check('frozen KG case187 exact J209 recipe object',cases[187]['original_kg_entry']['source_record']==md['data']['solutions'][0]['recipe'][11])
check('TOGO positive same source recipe lineage',to['meta']['original_media_id']=='JCM_M209' and to['meta']['src_url']==md['data']['medium']['link'] and to['meta']['name']==md['data']['medium']['name']=='M98-5')
check('TOGO exact100mL nominal4 percent buffer',all(to['components'][0]['items'][3][k]==v for k,v in {'component_name':'4% Na2CO3--CO2 buffer','volume':100,'unit':'ml','conc_value':4,'conc_unit':'%'}.items()))
for g, f in [('isp4','author-assessment.json'),('carbonate','primary-assessment-v1.json')]: inp(S/g/f)
for p in [S/'isp4/ontology-followup-v2.json',S/'isp4/guarded-write.json',S/'isp4/partonomy.json',S/'carbonate/validation-v1.json']:
    if p.exists():inp(p)
result={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'inputs_sha256':inputs,'new_evidence_count':len(newE),'checks':checks,'failures':[x for x in checks if not x['pass']], 'case21_preserved_decision_sha256':CH(oldD[cases[21]['case_id']]),'changed_decision_object_hashes':{x['case_id']:CH(x) for x in newD},'selected_proposal_object_hashes':{x['proposal_id']:CH(x) for x in newP}, 'limit':'Exact fragment binding and structural invariants supplement separately reasoned scientific review; full root core accounting is separate.'}
(P/'fragment-verification-v1.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'checks':len(checks),'failures':result['failures'],'new_evidence_count':len(newE),'report_sha256':H(P/'fragment-verification-v1.json')}))
