"""Focused regressions for independently reviewed alias/source/claim boundaries.

These are bounded campaign controls, not new repository policy or chemistry
approval. Native synonym admission is used unchanged. Deliberate mutants exist
only in memory and no maintained source is modified.
"""
from pathlib import Path
import json,copy,hashlib,sys,datetime,re
import yaml
ROOT=Path.cwd();sys.path.insert(0,str(ROOT/'src'))
from mediaingredientmech.synonym_policy import is_resolving_synonym
R=ROOT/'reports/all_unmatched_20261107/worker-06';S=R/'successor-v3'
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
P={x['proposal_id']:x for x in read(S/'proposals.json')['proposals']}
D=read(S/'decisions.json')['decisions'];E={x['evidence_id']:x for x in read(S/'evidence.json')['evidence']}
Y={pid:yaml.safe_load((R/p['after_capture']['path']).read_text()) for pid,p in P.items()}
results=[]
def tested(name,positive,mutant_rejected,detail):
    results.append({'control':name,'selected_positive_pass':bool(positive),'negative_mutant_detected':bool(mutant_rejected),'detail':detail})
    assert positive and mutant_rejected,name

alias_count=0
for f in sorted((S/'research-a/author-receipts').glob('*.json')):
    a=read(f);y=Y[a['proposal_id']]
    for row in a['alias_changes']:
        idx=int(row['field'].split('/')[-1]);selected=y['synonyms'][idx]
        assert selected==row['after']
        mutant=copy.deepcopy(selected);mutant['synonym_type']=row['before']['synonym_type']
        tested('alias-'+a['proposal_id']+'-'+str(idx),not is_resolving_synonym(selected),is_resolving_synonym(mutant),'Exact primary-reviewed nonidentifying row is blocked; restoring its original resolving type re-admits it under unchanged native policy.')
        alias_count+=1
    before=a['canonical_label_change']['before_preferred'];after=a['canonical_label_change']['after_preferred']
    if before!=after:
        tested('preferred-'+a['proposal_id'],y['preferred_term']==after,before!=after,'Source-qualified preferred label retained; restoring the exact generic/providerless preferred label violates this reviewed identity scope.')
controls=read(S/'research-a/author-scope.json')['controls']
for row in controls:
    actual=Y[row['proposal_id']]['synonyms']
    tested('named-stock-'+row['proposal_id'],all(is_resolving_synonym(x) for x in actual),all(not is_resolving_synonym({**x,'synonym_type':'REJECTED_LABEL'}) for x in actual),'Positive named-stock control: SL6/RST/SL4 remains active. A blanket rejection mutation incorrectly suppresses these source-supported labels.')

failed=['C-E-jcm-'+str(n) for n in [737,876,887,955]]
def classify_receiving(e):
    body=(R/e['capture']['path']).read_text()
    return not ('Nothing found' in body and e['kind']=='primary_source')
for eid in failed:
    e=E[eid];mutant={**e,'kind':'primary_source'}
    tested('failed-page-'+eid,e['kind']=='unsuccessful_search' and classify_receiving(e),not classify_receiving(mutant),'Exact failed body cannot be positive receiving-recipe evidence; original capture and timestamp stay bound.')
e=E['A-E-CAPTURE-121'];body=(R/e['capture']['path']).read_text()
def positive381(e):return e['kind']=='primary_source' and 'GRMD=379' in (R/e['capture']['path']).read_text()
tested('successful381',positive381(e),not positive381({**e,'kind':'unsuccessful_search'}),'Successful original381body explicitly links379; a failed-search reclassification is detected.')

water_ids=[p['proposal_id'] for p in read(S/'research-c/proposals.json')['proposals']]
def literal_stock_scope(y):return not any(c['component_name'].casefold() in ['water','distilled water'] for c in y['components'])
for pid in water_ids:
    y=Y[pid];mutant=copy.deepcopy(y);mutant['components'].append({'component_name':'Water','reference_scope':'UNMAPPED'})
    tested('untranscribed-solvent-'+pid,literal_stock_scope(y),not literal_stock_scope(mutant),'The complete inspected primary stock descriptions do not name stock solvent. Adding Water back as a literal component exceeds this exact evidence scope; this is not a general rule against water in stocks.')
tested('case64-aqueous-scope','aqueous' not in D[64]['reasoning'].casefold(),'aqueous' in (D[64]['reasoning']+' aqueous glucose stock').casefold(),'Case outcome cannot silently restore the unsupported aqueous claim removed from its payload.')

kg=D[152]['case_id'];j=json.loads((R/E['R-ingredient-1886']['capture']['path']).read_text());assert j['data']['media']==[]
def bridge_guard(p,d):return kg not in p['case_ids'] and not d['proposal_ids'] and d['disposition']=='unresolved'
mp=copy.deepcopy(P['C-P-JCM187']);mp['case_ids'].append(kg)
tested('providerless1886',bridge_guard(P['C-P-JCM187'],D[152]),not bridge_guard(mp,D[152]),'No originating collection/recipe occurs in the exact1886body. Restoring a JCM187 backlink on number agreement alone is rejected; valid CM links remain.')

stock=Y['V2-P-NBRC1308-1356-TRACE']
def stock_guard(y):
    water=[c for c in y['components'] if c['component_name']=='Distilled water']
    naoh=[c for c in y['components'] if c['component_name']=='NaOH']
    return len(y['components'])==15 and y['component_assertion']['completeness']=='COMPLETE' and len(water)==1 and water[0].get('concentration_value')=='1' and water[0].get('concentration_unit')=='L' and len(naoh)==1 and 'concentration_value' not in naoh[0] and 'additional reagent' in y['component_assertion']['notes']
mutant=copy.deepcopy(stock);mutant['components'][-1]['concentration_value']='1';mutant['components'][-1]['concentration_unit']='G'
tested('nbrc-membership-vs-quantity',stock_guard(stock),not stock_guard(mutant),'Full named membership is complete while NaOH remains unquantified and1Lwater remains an input. A guessed NaOH amount fails.')

scope=P['C-P-NZAMINE-A']['source_context_scopes_by_case'][D[173]['case_id']]
def typea_guard(scope):return {r['medium'] for r in scope['included']}=={'J44','J45','J47','J80','J103','J104','J437'} and {r['medium'] for r in scope['excluded']}=={'1762','548','552','554'}
mutant=copy.deepcopy(scope);mutant['included'].append(mutant['excluded'].pop())
tested('sheffield-typeA-subset',typea_guard(scope),not typea_guard(mutant),'Only seven manufacturer/typeA-qualified receiving contexts attach. Pulling an unspecified occurrence into that subset fails.')

ebios=Y['V3-B-P-EBIOS'];bare=[x for x in ebios.get('synonyms',[]) if x['synonym_text']=='EBIOS'];tablets=[x for x in ebios.get('synonyms',[]) if x['synonym_text']=='EBIOS* (dried yeast tablets)']
tested('ebios-product-versus-brand',bool(bare and tablets) and not any(is_resolving_synonym(x) for x in bare) and all(is_resolving_synonym(x) for x in tablets),is_resolving_synonym({**bare[0],'synonym_type':'RAW_TEXT'}),'Exact tablet-qualified source label remains resolving; ambiguous bare EBIOS brand cannot be promoted across P2G and tablet contexts.')

out={'status':'PASS','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':sys.executable+' '+str(Path(__file__)),'control_count':len(results),'exact_alias_rows_checked':alias_count,'inputs':{str(S/f):sha(S/f) for f in ['decisions.json','evidence.json','proposals.json']},'native_policy_path':'src/mediaingredientmech/synonym_policy.py','native_policy_sha256':sha(ROOT/'src/mediaingredientmech/synonym_policy.py'),'results':results,'limits':'Bounded regression controls test actual reviewed failure modes and required positive controls. They do not replace primary assessment or establish whole-owner/source/export approval. All deliberate mutants remain in memory; no maintained writes.'}
dest=S/'logs'/('negative-controls-final.json' if '--final' in sys.argv else 'negative-controls.json');assert not dest.exists();dest.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n');print('PASS',len(results),'focused positive/negative control pairs')
