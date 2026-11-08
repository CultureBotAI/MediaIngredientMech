"""Read-only frozen comparator route and source binding checks, before final author selection."""
from pathlib import Path
import csv
import datetime
import hashlib
import json
import re
import yaml

C = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
P = C / 'preflight/tenvit-final-application-route-v1'
W = C / 'workers/w08/worktree'
A = W / 'reports/all_unmatched_20261107/worker-08'
O = Path(__file__).resolve().parent
CID = 'CM_NAME:d57e91ffaea6f0ab6ff0f3d6f0b04c26356c832e85dd83e9e2319874fda43506'
TRIGGER = 'CM_OCC:a181b24b7eb91c50c771bd1c1fc3012fd0cf28f45b49f2750c3d43bda9cdd531'
def read(p): return json.loads(Path(p).read_text())
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def canonical(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def ref(p): return {'path':str(p),'sha256':sha(p)}

shards=[C/f'queue/preliminary-v5/shards/shard-{n:02}.json' for n in range(1,11)]
all_cases=[x for p in shards for x in read(p)['cases']]
case=next(x for x in all_cases if x['case_id']==CID)
assert canonical(case)=='1c8fdd449fe96f1f9a8599fe72941fcf09ef4d0e68a5134be4fdf52b416d9868'
assert len(case['occurrences'])==6
occurrences=[]
for x in case['occurrences']:
    f=C/'queue/preliminary-v5'/x['full_recipe_snapshot']
    assert sha(f)==x['source_file_sha256']
    record=yaml.safe_load(f.read_text())
    pointed=record
    for part in x['component_path'].split('/'):
        pointed=pointed[int(part)] if isinstance(pointed,list) else pointed[part]
    assert pointed==x['raw_component']
    assert record['id']==x['recipe_id']
    assert record['media_term']['term']['id'].startswith('nbrc.medium:')
    occurrences.append({'occurrence_id':x['occurrence_id'],'snapshot':ref(f),'component_path':x['component_path'],'source_id':record['media_term']['term']['id'],'recipe_id':record['id'],'trigger':x['occurrence_id']==TRIGGER,'preservation_partition':('comparator_trigger_nominal_ten' if x['occurrence_id']==TRIGGER else 'different_ten_NBRC1226' if record['media_term']['term']['id']=='nbrc.medium:1226' else 'common_nine')})
assert sum(x['trigger'] for x in occurrences)==1
trigger=next(x for x in occurrences if x['trigger'])
assert trigger['source_id']=='nbrc.medium:903' and trigger['recipe_id']=='CultureMech:007503' and trigger['component_path']=='ingredients/9'

props=read(P/'captures/w08/proposals.json')['proposals']
prop=next(x for x in props if x['proposal_id']=='vm1201-prop-nbrc903-vitamin')
assert prop['kind']=='new_owner' and prop['before_sha256'] is None and prop['case_ids']==[CID]
assert prop['source_occurrence_ids']==[TRIGGER]
assert 'current Wolfe stock with KH2PO4' in prop['description']
assert sha(A/prop['after_capture']['path'])==prop['after_capture']['sha256']=='e4a7c5d611dd36f449da97ec674100f58679ab5a5871996e79ca9837e73b2802'

before=yaml.safe_load((P/'captures/before-Wolfes_Vitamin_Mix.yaml').read_text())
w09=yaml.safe_load((P/'captures/candidate-fe607027.yaml').read_text())
assert sha(P/'captures/before-Wolfes_Vitamin_Mix.yaml')==sha(W/'data/ingredients/mapped/Wolfes_Vitamin_Mix.yaml')=='709749bd7c83c38a09400fc1893885ead753847ff9d1cbbe4ec76b431d349738'
assert sha(P/'captures/candidate-fe607027.yaml')=='fe6070272f269fde7683696e4c46a331902ab88baac8c5cc93db7bddf9d0ec1b'
assert w09['curation_history'][:5]==before['curation_history'] and len(w09['curation_history'])==6
assert w09['curation_history'][-1]['curator']=='Codex worker09 /root ten-vitamin source continuity review'
csvrows=list(csv.reader((P/'captures/w09/history/captures/Mixes.csv').open()))
source_rows=csvrows[41:51]
assert [[x['component_name'],x['concentration_value'],'mg/L'] for x in w09['components']]==source_rows
assert all(x['concentration_unit']=='MG_PER_L' for x in w09['components'])
assert csvrows[39]==['X','100','']

matrix=read(P/'ten-child-identity-matrix.json');children=[]
for x in matrix['children']:
    own=x['active_owner'];live=Path(own['path']);capture=P/own['captured_path']
    assert sha(live)==sha(capture)==own['sha256']
    rec=yaml.safe_load(live.read_text());assert rec['identifier']==x['active_identity'] and rec['mapping_status']=='MAPPED'
    children.append({'index':x['candidate_component_index'],'literal':x['literal_component'],'recommended_id':x['recommended_component_id'],'scope':x['recommended_reference_scope'],'active_owner':ref(live),'active_capture':ref(capture),'current_identifier':rec['identifier'],'current_preferred_term':rec['preferred_term'],'reason':x['reason'],'approval_limit':'Active named-entity reference only; not whole referenced-owner scientific approval.'})
assert sum(x['scope']=='MIM_CATALOG' for x in children)==9
assert children[6]['scope']=='UNMAPPED' and children[6]['recommended_id'] is None

family=read(P/'eight-cases-and-scopes.json');family_checks=[]
for x in family['cases']:
    actual=next(r for r in all_cases if r['case_id']==x['case_id'])
    assert actual==x['source_case'] and canonical(actual)==x['case_input_sha256']
    family_checks.append({'case_id':x['case_id'],'worker':x['worker'],'case_input_sha256':canonical(actual),'occurrence_count':len(actual.get('occurrences',[])),'scope':'Mechanical frozen-object linkage only; W06 case science is not imported into this W08 review.'})
assert sum(x['occurrence_count'] for x in family_checks)==71
normalize=lambda s: re.sub(r'[^a-z0-9]','',str(s).casefold())
matches=[x['case_id'] for x in all_cases if any(normalize(x.get(k,''))=='wolfesvitaminmix' for k in ['source_label','raw_source_label','source_case_id'])]
assert not matches

source_refs=[]
for x in read(P/'source-bindings.json')['refs']:
    path=P/x['captured_path'] if x.get('captured_path') else Path(x['path'])
    assert sha(path)==x['sha256']
    source_refs.append({'path':str(path),'sha256':x['sha256'],'review_scope':'Byte binding; does not alone imply content inspection.'})

evs=read(P/'captures/w08/evidence.json')['evidence'];primary=[]
for e in evs:
    if e['evidence_id'] in ['vm-fetch-1962216682ccb735','vm-fetch-7d55379a5f033497','vm-fetch-ede69c87ee45106a','vm-fetch-19ea505c685bcbd1','vm-fetch-2630e40c26a0b155','vm-fetch-571507208cde7532']:
        f=A/e['capture']['path'];assert sha(f)==e['capture']['sha256']
        primary.append({'evidence_id':e['evidence_id'],'capture':ref(f),'original_url':e['url'],'original_accessed_at':e['accessed_at'],'read_scope':'Complete primary HTML body text including basal preparation, nested vitamin and mineral formulas; header/footer navigation also parsed. No current live retrieval claimed.'})
assert len(primary)==6

out={'status':'PASS_PREFLIGHT_ONLY_FINAL_AUTHOR_BYTES_NOT_YET_REVIEWED','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':'worker08:/root/inorganics','author':'worker08:/root','author_task':ref(P/'AUTHOR-TASK-W08.md'),'case_id':CID,'case_input_sha256':canonical(case),'occurrences':occurrences,'culturebot_occurrences_in_assigned_case':0,'original_nbrc903_proposal':prop,'original_nbrc903_proposal_canonical_sha256':canonical(prop),'authentic_comparator_before':ref(P/'captures/before-Wolfes_Vitamin_Mix.yaml'),'authentic_w09_candidate':ref(P/'captures/candidate-fe607027.yaml'),'raw_cb_source':ref(P/'captures/w09/history/captures/Mixes.csv'),'raw_cb_rows_42_51':source_rows,'X_row_40':csvrows[39],'child_reference_checks':children,'family_frozen_object_checks':family_checks,'family_partitions_context_only':family['partitions'],'family_count_claims_preserved_not_scientifically_reapproved':family['counts'],'exact_name_absence_search':{'scope':'All ten explicitly opened frozen shard files, independent of gitignore; three root source-label fields normalized to alphanumeric lowercase only. No corpus-wide substance absence claim.','cases_examined':len(all_cases),'matches':matches,'inputs':[ref(x) for x in shards]},'source_binding_checks':source_refs,'primary_case_reads':primary,'limitations':['Final composed owner/case/proposal/dependency bytes and final native results are pending.','Nine child identities are supported only at named supplied-input scope; inherited aliases, roles and owner/export approval remain held.','Only the actual W08 case is scientifically reassessed here; W06 identities/cases and 84 KG holds are preserved context, not adopted source ownership.','All supported nominal recipe facts remain separate from exact association with the CB cyanocobalamin mg/L/X100 stock.','Initial BeautifulSoup text extraction was unavailable (ModuleNotFoundError); stdlib HTMLParser successfully read the complete source bodies instead.'],'new_findings':[],'maintained_application_authorized':False}
f=O/'preflight-review.json';assert not f.exists();f.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'status':out['status'],'sha256':sha(f),'source_bindings':len(source_refs),'case_occurrences':len(occurrences),'child_references':len(children),'family_case_hashes':len(family_checks)},indent=2))
