from pathlib import Path
import json,hashlib,datetime,importlib.util,sys,copy
import yaml
from mediaingredientmech.validation.write_validated import validate_ingredient
r=Path('.temp/w05-tellurium-polypeptone-v1/review');p=Path('.temp/w05-tellurium-polypeptone-v1/polypeptone')
builder=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/claw/scripts/build_mim_ingredient_sssom.py')
spec=importlib.util.spec_from_file_location('independent_mim_projection',builder);m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def objsha(d):return hashlib.sha256(json.dumps(d,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
a=p/'proposed/Polypeptone.yaml';b=p/'predecessor/Polypeptone.yaml';da=yaml.safe_load(a.read_text());db=yaml.safe_load(b.read_text())
selected=m._row_from_yaml(a,{},{},{},{},record=da,owners={});prior=m._row_from_yaml(b,{},{},{},{},record=db,owners={})
food=copy.deepcopy(da);food['ontology_mapping'].update(ontology_id='FOODON:03315306',ontology_label='protein hydrolyzates',ontology_source='FOODON',mapping_quality='NARROW_MATCH')
micro=copy.deepcopy(da);micro['identifier']='MICRO:0000179';micro['ontology_mapping'].update(ontology_id='MICRO:0000179',ontology_label='polypeptone',ontology_source='MICRO',mapping_quality='EXACT_MATCH')
options={'foodon_parent_if_source_scope_settled_no_exact_term':m._row_from_yaml(a,{},{},{},{},record=food,owners={}),'micro_exact_if_BD_blend_scope_established':m._row_from_yaml(a,{},{},{},{},record=micro,owners={})}
removed={'Polypepton (Nihon Pharm. Co.)','Polypepton (Nihon Seiyaku)'}
assert len(selected)==len(prior)==1
assert set(prior[0]['other'].split('|'))-set(selected[0]['other'].split('|'))==removed
assert set(selected[0]['other'].split('|'))-set(prior[0]['other'].split('|'))==set()
assert da['curation_history'][:-1]==db['curation_history']
assert set(k for k in da if da[k]!=db[k])=={'curation_history','notes','synonyms'}
changed_synonyms=[{'before':x,'after':y}for x,y in zip(db['synonyms'],da['synonyms'])if x!=y]
assert {x['before']['synonym_text']for x in changed_synonyms}==removed
assert all(x['after']['synonym_type']=='REJECTED_LABEL'for x in changed_synonyms)
assert len(options['foodon_parent_if_source_scope_settled_no_exact_term'])==2
assert len(options['micro_exact_if_BD_blend_scope_established'])==1
errs=[str(x)for x in validate_ingredient(da)]
assert not errs
j={'reviewer':'/root/final_skeptical','completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'builder':{'path':str(builder),'sha256':sha(builder)},'after_payload':{'path':str(a),'sha256':sha(a)},'predecessor_payload':{'path':str(b),'sha256':sha(b)},'complete_closed_schema_errors':errs,'changed_fields':['curation_history','notes','synonyms'],'changed_synonyms':changed_synonyms,'all_other_fields_equal':True,'all_prior_history_equal':True,'all_original_synonym_text_and_original_source_prefixes_retained':all(x['before']['synonym_text']==x['after']['synonym_text']and x['after']['source'].startswith(x['before']['source']) for x in changed_synonyms),'prior_rows':prior,'selected_rows':selected,'native_row_field_differences':{k:{'before':prior[0][k],'after':selected[0][k]}for k in prior[0]if prior[0][k]!=selected[0][k]},'in_memory_unselected_options':options,'selected_mapping_status':'needs_curation; exact registry self-row is a producer consequence, not final scientific grounding approval','limitations':['Exact direct pinned producer invocation with explicit empty owner index; full catalog/ownership conflict validation remains root responsibility.','Hypothetical options are in-memory field projections, not authored or selected YAML candidates and not approved source routes. MICRO exact term has priority only for supported BD blend scope; FOODON broad parent requires a settled preparation with no applicable exact term.','No maintained files, synonym exports, SSSOM or ownership changes performed.']}
out=r/'independent-polypeptone-native-v1.json';assert not out.exists();out.write_text(json.dumps(j,indent=2,ensure_ascii=False)+'\n');print(out,sha(out));print('row counts',len(prior),len(selected),{k:len(v)for k,v in options.items()});print('deltas',list(j['native_row_field_differences']))
