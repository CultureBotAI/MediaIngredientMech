"""Author evidence and reproducible checks, confined to this cohort directory."""
from pathlib import Path
from collections import Counter
import copy, datetime, hashlib, json, sqlite3, subprocess, sys
import yaml
from mediaingredientmech.validation.write_validated import validate_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
from mediaingredientmech.synonym_policy import is_resolving_synonym

R=Path('reports/all_unmatched_20261107/worker-08')
S=R/'successors/issue-1227-v1'
M=S/'research/vitamins_mixtures'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def save(n,x):(M/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def cap(p):return dict(root='artifact',path=str(p.relative_to(R)),sha256=sha(p))
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
A=read(M/'assignment.json'); P=read(M/'proposals.json');D=read(M/'decisions.json')
old={p['proposal_id']:p for p in A['proposals']};records={};checks=[];receipts=[]
def check(name,condition,detail=None):
    checks.append(dict(name=name,passed=bool(condition),detail=detail));assert condition,(name,detail)
check('complete proposal IDs',set(old)=={p['proposal_id'] for p in P} and len(P)==47)
check('complete case IDs',{d['case_id'] for d in D}==set(A['case_ids']) and len(D)==57)
for p in P:
    prev=old[p['proposal_id']];prior=yaml.safe_load((R/prev['after_capture']['path']).read_text());f=R/p['after_capture']['path'];rec=yaml.safe_load(f.read_text());records[p['proposal_id']]=rec
    assert sha(f)==p['after_capture']['sha256']
    assert all(p[k]==prev[k] for k in ['proposal_id','kind','owner_path','before_sha256','case_ids'])
    assert not validate_ingredient(rec),p['proposal_id']
    h=prior.get('curation_history',[]);assert rec.get('curation_history',[])[:len(h)]==h
    changed=p['after_capture']!=prev['after_capture']
    if changed:assert len(rec['curation_history'])==len(h)+1 and rec['curation_history'][-1]['llm_assisted'] is True
    for k in ['roles','community_organism_roles','nutritional_roles','physicochemical_roles','cellular_metabolic_roles','causal_graphs','occurrence_statistics','chemical_properties']:assert rec.get(k)==prior.get(k),(p['proposal_id'],k)
    if p['before_sha256']:
        raw=subprocess.check_output(['git','show','e000d66dd26ab053e9b17ce7bf8d3c873c3dde99:'+p['owner_path']]);assert hashlib.sha256(raw).hexdigest()==p['before_sha256'];assert sha(p['owner_path'])==p['before_sha256']
        inherited=(yaml.safe_load(raw).get('ontology_mapping') or {}).get('evidence',[])
    else:inherited=[]
    for e in (rec.get('ontology_mapping') or {}).get('evidence',[]):
        if e['evidence_type']=='MANUAL_CURATION':assert e in inherited
    if p['proposal_id']!='vm-prop-linsmaier-skoog':
        assert len(rec.get('components',[]))==len(prior.get('components',[]))
        for c,b in zip(rec.get('components',[]),prior.get('components',[])):
            for k in ['concentration_value','concentration_unit','concentration_range']:assert c.get(k)==b.get(k)
    receipts.append(dict(proposal_id=p['proposal_id'],selected_payload=cap(f),changed=changed,strict_schema='PASS',history_prefix_preserved=True,roles_counts_chemistry_preserved=True,original_before_sha256=p['before_sha256']))
check('47 schema-valid payloads, audit/history/roles/quantities preserved',len(receipts)==47)
for d,prev in zip(D,A['decisions']):
    assert all(d.get(k)==prev.get(k) for k in ['case_id','case_input_sha256','source','occurrence_ids','preserved_native_decisions','proposal_ids','disposition','missing_requirement','no_change_reason','owner_records'])
check('all57 frozen case, source, occurrence, dispositions and held requirements preserved',True)
cats=read(M/'evidence-category-corrections.json')
for c in cats:
    b,a=copy.deepcopy(c['before']),copy.deepcopy(c['after']);assert b.pop('evidence_type')=='MANUAL_CURATION';assert a.pop('evidence_type')=='CURATOR_JUDGMENT';assert a==b
check('49 assertion-level category changes preserve all other evidence fields',len(cats)==49)
rejected=[]
for pid in ['vm-prop-jcm403-vitamin','vm-prop-jcm403-b12']:
    r=records[pid];assert r['preferred_term'].startswith('JCM 403 ')
    for s in r['synonyms']:assert s['synonym_type']=='REJECTED_LABEL' and not is_resolving_synonym(s);rejected.append(s['synonym_text'])
check('six JCM403 providerless pointers remain nonresolving provenance',len(rejected)==6,rejected)
comp=read(M/'completeness-adjudications.json')
check('seven UNKNOWN and four retained PARTIAL exclusions',Counter(x['after'] for x in comp)=={'UNKNOWN':7,'PARTIAL':4})
assert records['vm1201-prop-nbrc1356-mineral-base1']['component_assertion']['method']=='CURATED_INTERPRETATION'
check('supernatant water interpretation separated from charged salts',len(records['vm1201-prop-nbrc1356-mineral-base1']['components'])==1)
for pid in ['vm-prop-jcm403-b12','vm-prop-linsmaier-skoog']:
    assert records[pid]['mapping_status']=='MAPPED' and records[pid]['ontology_mapping']['mapping_quality']=='FALLBACK_REGISTRY'
    assert records[pid]['ontology_mapping']['ontology_id']==records[pid]['identifier']
check('two guarded native placeholder promotions retain original owner path',True)
base=read(R/'successors/issue-1201-v1/proposals.json')['proposals'];overlay={p['proposal_id']:p for p in base};overlay.update({p['proposal_id']:p for p in P})
catalog={str(f):yaml.safe_load(f.read_text()) for f in Path('data/ingredients').rglob('*.yaml')}
catalog_count=len(catalog)
for p in overlay.values():catalog[p['owner_path']]=yaml.safe_load((R/p['after_capture']['path']).read_text())
di=read(M/'conditional-deionized-water-dependency.json');di_path=R/di['target_after_capture']['path'];assert sha(di_path)==di['target_after_capture']['sha256'];catalog[overlay[di['target_proposal_id']]['owner_path']]=yaml.safe_load(di_path.read_text())
part=list(map(str,validate_component_partonomy(catalog.values())))
check('full113 selected-proposal overlay native partonomy',not part,part)
for p in P:
    if p['proposal_id'] in ['vm-prop-jcm403-b12','vm-prop-linsmaier-skoog']:
        collisions=[f for f,r in catalog.items() if f!=p['owner_path'] and r.get('mapping_status')!='REJECTED' and r['identifier']==records[p['proposal_id']]['identifier']];assert not collisions
check('promoted registry identifiers have no active overlay identity collision',True)
# Persist the supplementary primary ontology lookup actually inspected.
db=Path('/Users/marcin/.data/oaklib/chebi.db');con=sqlite3.connect('file:'+str(db)+'?mode=ro',uri=True)
terms={i:con.execute("select predicate,value,object from statements where subject=? and (predicate like '%label' or predicate like '%formula' or predicate like '%Synonym')",(i,)).fetchall() for i in ['CHEBI:32599','CHEBI:78292']}
save('supplementary-ontology-lookup.json',dict(database=str(db),sha256=sha(db),terms=terms,scope='Anhydrous MgSO4 and sodium ferric EDTA source-form identity; no role/owner approval.'))
# Rebind the all113 duplicate inventory to final own bytes without changing its scientific assessment.
dupe=read(M/'promotion-selected-proposal-comparison.json');dupe['own_successors_index']['sha256']=sha(M/'proposals.json')
for row in dupe['rows']:
    if row['proposal_id'] in records:
        p=next(p for p in P if p['proposal_id']==row['proposal_id']);row['capture']=p['after_capture']
save('promotion-selected-proposal-comparison.json',dupe)
tri=read(S/'inputs/coordinator-triage/completeness-adjudication-refinement.json')
save('full34-refinement-dispositions.json',dict(input=cap(S/'inputs/coordinator-triage/completeness-adjudication-refinement.json'),counts=tri['counts'],rows=[dict(proposal_id=x['proposal_id'],recommendation=x['root_triage_recommendation'],source_anchors=x.get('primary_anchors',[]),author_scope='this_cohort' if x['proposal_id'] in records else 'other_author_cohort_not_self_approved',actual_completeness=records[x['proposal_id']].get('component_assertion',{}).get('completeness') if x['proposal_id'] in records else None,reason=x['reason']) for x in tri['rows']]))
save('issue-dispositions.json',dict(author='/root/vitamins',issues=[dict(finding='IR001',issue=1226,status='corrected_in_isolated_proposals',entries=49,payloads=42,detail='Each newly authored mapping entry is a registry identity judgment, CURATOR_JUDGMENT; inherited human assertions and ComponentEvidence categories remain.'),dict(finding='IR002',issue=1227,status='corrected_in_isolated_proposals',detail='Two JCM403 preferred names qualified; six raw pointers retained as nonresolving REJECTED_LABEL.'),dict(finding='IR003',issue=1201,status='completed_supported_component_references',detail='236 compatible references, including three explicit conditional overlay edges; all component-specific remaining form/preparation limits are recorded. No role/export/withheld release.'),dict(finding='IR004',issue=1201,status='existing_placeholder_promotions_proposed',detail='JCM403 B12 and DuchefaL0230 reuse exact existing owners; ignored-inclusive catalog and all113 selected proposals compared. L0230 fifteen dry-product inputs at manufacturer nominal mg/L basis.'),dict(finding='IR005',issue=1227,status='corrected_in_isolated_proposal',detail='Supernatant water is CURATED_INTERPRETATION; charged salts are not retained-solute quantities.'),dict(finding='IR006',issue=1227,status='full_refinement_scope_accounted',detail='All34 row dispositions accounted; own7 UNKNOWN and4 PARTIAL exclusions. The other23 remain with their assigned authors and independent reviewers.')],known_mapping_concern=dict(entity='CHEBI:9532',issues=[319,320,268],native_hold_position=2792,disposition='Existing named TPP entity referenced without importing its conflicting inherited chloride property packet; known concern and WITHHOLD remain, no new issue or owner correction.'),independent_review='pending'))
E={e['evidence_id']:e for e in read(R/'successors/issue-1201-v1/evidence.json')['evidence']}
logs=[json.loads(l) for l in (M/'inspection-log.jsonl').read_text().splitlines()];logged={l['path'] for l in logs}
keys={k for d in A['decisions'] for k in d['evidence_ids']}|{k for p in A['proposals'] for k in p['evidence_ids']}
ledger=[]
for k in sorted(keys):
    e=E[k];c=e.get('capture');path=R/c['path'] if c and c.get('root')=='artifact' else None
    if not path:continue
    assert sha(path)==c['sha256']
    status='current_content_read' if str(path) in logged else 'retained_predecessor_evidence_no_new_claim'
    locator='Recorded individual display in inspection-log.jsonl; bounded fact extractions are not raw responses.'
    if (e.get('url') or '').startswith('https://mediadive.dsmz.de/rest/solution/'):
        status='current_recipe_and_preparation_content_read';locator='All recipe labels, source amounts/units, attributes, conditions and steps; compact projection in mediadive-source-read-addendum.json overrides earlier truncated raw display.'
    if k=='vm-fetch-38e9fbc285a50d42':status='current_relevant_primary_passage_read';locator='Materials and methods > D. vulgaris growth conditions: Thauer vitamins 1 ml/L and reference42; entire unrelated article not reread.'
    if k=='vm-fetch-cbd3704d6abef0bc':status='current_relevant_primary_passage_read';locator='TOGO M2445 paragraph11: 1 ml B12 0.1mg/ml filter sterilized, separate3ml methanol; ATCC2883 complete primary PDF also read.'
    if k=='vm1201-common9-comparison':status='current_content_read';locator='All seven primary binding and component tables displayed; original raw NBRC1356/1169/1308/1050/1086/1274/925 also individually read.'
    ledger.append(dict(evidence_id=k,capture=c,kind=e['kind'],inspection=status,locator=locator,accessed_at=e.get('accessed_at'),url=e.get('url')))
save('source-read-ledger.json',dict(at=now,entries=ledger,inspection_log=cap(M/'inspection-log.jsonl'),source_context=cap(R/'research/vitamins_mixtures/source-contexts.json'),scope='This bounded correction rereads relevant primary formulation/candidate evidence and all57 final dispositions/all47 selected payloads. Frozen contexts and case identity remain unchanged. Historical retrieval denials and removed full-paper archives retain their original receipts; no new paid/external session or inaccessible-paper claim.'))
save('case-assessments.json',[dict(case_id=d['case_id'],case_input_sha256=d['case_input_sha256'],source=d['source'],occurrence_ids=d['occurrence_ids'],proposal_ids=d['proposal_ids'],disposition=d['disposition'],appraisal=d['reasoning'],applicability=d['applicability'],precise_remaining_requirement=d['missing_requirement'],source_evidence_ids=d['evidence_ids'],holds_preserved=True,author_only=True) for d in D])
save('validation.json',dict(at=now,checks=checks,payloads=receipts,maintained_catalog_records=catalog_count,overlay_records=len(catalog),overlay_proposals=len(overlay),partonomy_violations=part,status='PASS',scientific_approval=False,independent_review='pending'))
files=[('vm1227-component-adjudication','component-adjudications.json','Every component index: literal form, native reference, candidate hash, precise retained limits and conditional overlay status.'),('vm1227-payload-assessment','payload-assessments.json','Every47 selected payload: full source assertion, changes, original/final hash, preserved roles/history/counts.'),('vm1227-category-ledger','evidence-category-corrections.json','49 per-entry category corrections, exact original fields and reasons.'),('vm1227-promotion-comparison','promotion-selected-proposal-comparison.json','All113 selected candidates and source/formulation duplicate adjudication for two placeholder promotions.'),('vm1227-component-ontology','component-ontology-lookup.json','Primary local ChEBI identity/formula/synonym lookup with database hash.'),('vm1227-supplementary-ontology','supplementary-ontology-lookup.json','Anhydrous MgSO4 and sodium ferric EDTA form identity.'),('vm1227-completeness','completeness-adjudications.json','Seven UNKNOWN and four explicit PARTIAL exclusions.'),('vm1227-dependency-jcm197','conditional-component-dependencies.json','Exact final NBRC903 payload and primary JCM197 formulation bridge; conditional integration only.'),('vm1227-dependency-diwater','conditional-deionized-water-dependency.json','Exact stable deionized-water successor and DSMZ533/ATCC1249 source-grade bridge.'),('vm1227-source-read-ledger','source-read-ledger.json','Actual inspection scope, original primary captures and bounded derivative semantics.'),('vm1227-native-validation','validation.json','Author schema, full catalog-overlay partonomy and preservation checks; no peer approval.')]
save('evidence-additions.json',dict(schema_version=1,evidence=[dict(evidence_id=i,kind='local_validation',capture=cap(M/n),url=None,locator=loc,supports_or_contradicts=loc) for i,n,loc in files]))
print(json.dumps(dict(status='PASS',cases=len(D),proposals=len(P),checks=len(checks),schema_errors=0,partonomy_errors=len(part))))
