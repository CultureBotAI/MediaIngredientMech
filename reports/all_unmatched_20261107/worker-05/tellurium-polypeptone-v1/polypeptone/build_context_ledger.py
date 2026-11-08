from pathlib import Path
from datetime import datetime, timezone
import json, gzip, hashlib, re, collections
S = Path('.temp/w05-tellurium-polypeptone-v1/polypeptone')
B = Path('reports/all_unmatched_20261107/worker-05')
original = B / 'correction-1193-v1/materials/complete-context-reinspection.json.gz'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
jsha = lambda x: hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
x = json.loads(gzip.decompress(original.read_bytes()))
oi, owner = next((i,o) for i,o in enumerate(x['owners']) if o['path'].endswith('/Polypeptone.yaml'))
rows = owner['exact_resolving_label_occurrences']
assert len(rows) == 150
recipes = {r['source_path']:x['current_complete_recipes'][r['source_path']] for r in rows}
recipe_out = S/'input/complete-150-context-recipes.json'
recipe_out.write_text(json.dumps({'original_capture':str(original.relative_to(B)),'original_capture_sha256':sha(original),'original_inspected_at':x['inspected_at'],'canonical_json_hash_method':'UTF8 json.dumps(sort_keys=True,separators=(comma,colon),ensure_ascii=False)','complete_recipes':recipes},ensure_ascii=False,indent=2)+'\n')
direct_routes = {32:86,55:130,72:181,73:182,77:189,82:197,94:222,96:239,98:264,99:273,103:2,104:323,106:423,107:535,108:86,109:838,110:98,111:99,149:1467}
fresh = {int(p.stem.removeprefix('jcm')):p for p in (S/'captures').glob('jcm*.html')}
result=[]
for i,r in enumerate(rows):
    rec=recipes[r['source_path']]['complete_recipe']
    ing=json.loads(r['ingredient_json'])
    component=rec[r['component_field']][int(r['component_index'])]
    label=r['preferred_term']; low=label.lower()
    lexical=('hipolypepton' if low.startswith('hipolypepton') else 'japanese_polypepton' if 'nihon' in low else 'bd_bbl_qualified' if 'bd' in low or 'bbl' in low else 'generic_polypeptone')
    qualifier_fields=[]
    def walk(v,p=''):
        if isinstance(v,dict):
            for k,z in v.items(): walk(z,p+'/'+k)
        elif isinstance(v,list):
            for n,z in enumerate(v):walk(z,p+'/'+str(n))
        elif isinstance(v,str) and re.search(r'(?i)nihon|wako|bbl|bd[ -]?211910|bd-bbl',v):qualifier_fields.append({'json_pointer':p,'exact_value':v})
    walk(ing)
    route=direct_routes.get(i)
    route_basis='explicit raw-Japanese recipe source relationship' if route else None
    term_id=rec.get('media_term',{}).get('term',{}).get('id','')
    if not route:
        m=re.fullmatch(r'mediadive\.medium:J(\d+)',term_id)
        if m: route=int(m[1]);route_basis='complete recipe media_term.term.id'
    if not route and r['record_class']=='SolutionRecipe':
        m=re.search(r'Main sol[._ ]+J(\d+)\b',r['recipe_label']) or re.search(r'_Main_sol_J(\d+)\b',r['source_path'])
        if m:route=int(m[1]);route_basis='complete solution source name; parent-route lead, not equivalence or source approval'
    cap=[];observation=None
    if route in fresh:
        p=fresh[route]; receipt=json.loads((p.parent/(p.name+'.receipt.json')).read_text())
        cap.append({'path':'captures/'+p.name,'sha256':sha(p),'accessed_at':receipt['accessed_at'],'url':receipt['url']})
        if route in [130,181,182,99]:observation='Current JCM names Hipolypepton (FUJIFILM Wako), conflicting with a historical Nihon Polypepton assertion where present; no historical SKU equivalence or source substitution inferred.'
        elif route in [2,98]:
            observation='JCM endpoint returned Nothing found. Fresh MediaDive J'+str(route)+' retains Polypeptone with Nihon Pharm. Co. attribute; supplier-qualified source label, not SKU or formulation bridge.'
            p=S/'captures'/f'mediadiveJ{route}.json';receipt=json.loads((p.parent/(p.name+'.receipt.json')).read_text());cap.append({'path':'captures/'+p.name,'sha256':sha(p),'accessed_at':receipt['accessed_at'],'url':receipt['url']})
        elif route in [86,189,197,222,239,264,273,323,423,535,838,1467]:observation='Current JCM preserves the Nihon-qualified Polypepton label. It does not provide a catalogue code, product-vintage specification, or equivalence to BD Polypeptone / a particular Hipolypepton SKU.'
        else:observation='Parent-recipe reference inspected as context only; no product membership assigned from a recipe number.'
    if lexical=='hipolypepton':disposition='Preserve existing Hipolypepton exclusion from Polypeptone; no new assignment to any owner or contemporary product version.'
    elif lexical=='japanese_polypepton':disposition='Withdraw global resolving alias to this unsettled Polypeptone owner; preserve exact source label and supplier-qualified historical occurrence. Product-vintage/SKU bridge remains unresolved.'
    elif lexical=='bd_bbl_qualified':disposition='BD/BBL source-qualified comparison lead; dated Thermo catalogue supports the named blend, but this context row is not a newly assigned W05 source case or new source/owner release approval.'
    else:disposition='Generic lexical label is not automatic BD membership. Preserve any embedded qualifiers and exact source relationships; retain supplier/product routing hold unless its own source scope is independently settled.'
    result.append({'context_row_index':i,'context_id':f'W05-POLY-CONTEXT-{i:03d}','original_occurrence_row':r,'original_context_json_pointer':f'/owners/{oi}/exact_resolving_label_occurrences/{i}','original_row_canonical_sha256':jsha(r),'ingredient_json_exact_string_sha256':hashlib.sha256(r['ingredient_json'].encode()).hexdigest(),'ingredient_json_parsed':ing,'recipe_component':component,'ingredient_matches_embedded_recipe_component':ing==component,'complete_recipe_binding':{'path':'input/complete-150-context-recipes.json','json_key':r['source_path'],'original_recipe_file_sha256':recipes[r['source_path']]['sha256'],'embedded_recipe_canonical_sha256':jsha(rec)},'lexical_group_only':lexical,'embedded_ingredient_qualifier_fields':qualifier_fields,'source_medium_term':rec.get('media_term'),'source_references':rec.get('references',[]),'source_recipe_notes':rec.get('notes'),'jcm_route_lead':route,'jcm_route_basis':route_basis,'fresh_primary_captures':cap,'fresh_primary_observation':observation,'membership_disposition':disposition,'quantity_disposition':'Exact inherited concentration/units, stock-versus-medium record shape and all raw source fields preserved; no concentration validation, conversion or final-dose endorsement.','approval':{'new_case_adopted':False,'source_mapping_approved':False,'owner_approved':False,'export_approved':False}})
out={'author':'/root/polypeptone_supplement','created_at':datetime.now(timezone.utc).isoformat(),'scope':'All 150 historical owner-context occurrence rows, not 150 assigned campaign cases and not a refresh of historical135 statistics. Lexical counts do not establish product identity.','original_capture':str(original.relative_to(B)),'original_capture_sha256':sha(original),'original_inspected_at':x['inspected_at'],'original_occurrence_table_sha256':x['occurrence_table_sha256'],'complete_recipe_capture':{'path':str(recipe_out.relative_to(S)),'sha256':sha(recipe_out)},'counts':dict(collections.Counter(r['lexical_group_only'] for r in result)),'total':len(result),'unique_recipe_paths':len(recipes),'rows':result}
(S/'context-ledger.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'counts':out['counts'],'total':out['total'],'recipes':len(recipes),'component_discrepancies':[r['context_row_index'] for r in result if not r['ingredient_matches_embedded_recipe_component']],'sha256':sha(S/'context-ledger.json')},indent=2))
