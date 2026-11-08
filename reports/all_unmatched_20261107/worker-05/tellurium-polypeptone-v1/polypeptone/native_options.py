from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys,types,yaml,copy
from mediaingredientmech.validation.write_validated import validate_ingredient
S=Path('.temp/w05-tellurium-polypeptone-v1/polypeptone');B=Path('reports/all_unmatched_20261107/worker-05');sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
builder=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/claw/scripts/build_mim_ingredient_sssom.py');assert sha(builder)=='38d59f42953305f6fc51e4fc24dfc59ee1919bfb961595b67a8afe9f8a46a1bc'
sys.path[:0]=[str(builder.parent),str(builder.parent.parent/'src')];m=types.ModuleType('w05_poly_options');m.__file__=str(builder);sys.modules[m.__name__]=m;exec(compile(builder.read_bytes(),str(builder),'exec'),m.__dict__)
ps=json.loads((B/'postseal-source-corrections-v1/core/proposals.json').read_text())['proposals'];base={str(p):yaml.safe_load(p.read_text()) for p in Path('data/ingredients').rglob('*.yaml')};records=dict(base)
for p in ps:
 f=B/p['after_capture']['path'];assert sha(f)==p['after_capture']['sha256'];records.pop(p['owner_path'],None);records[p.get('destination_owner_path',p['owner_path'])]=yaml.safe_load(f.read_text())
owner='data/ingredients/mapped/Polypeptone.yaml';before=records[owner];selected=yaml.safe_load((S/'proposed/Polypeptone.yaml').read_text());records[owner]=selected
def project(r):
 trial=dict(records);trial[owner]=r;index=m.build_owner_index({m._mim_curie(Path(p).name):x for p,x in trial.items()});supp=[];rows=m._row_from_yaml(Path(owner),{},{},{},{},record=r,owners=index,suppressions=supp);return rows,[str(s) for s in supp]
br,bs=project(before);sr,ss=project(selected)
foodon=copy.deepcopy(selected);foodon['ontology_mapping'].update(ontology_id='FOODON:03315306',ontology_label='protein hydrolyzates',ontology_source='FOODON',mapping_quality='NARROW_MATCH');foodon['ontology_mapping']['evidence'].append({'evidence_type':'LLM_SUGGESTION','source':'https://www.ebi.ac.uk/ols4/ontologies/foodon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FFOODON_03315306','notes':'Conditional scientific interpretation for a settled named protein-hydrolysate preparation; not selected owner scope or final grounding approval.'})
micro=copy.deepcopy(selected);micro['identifier']='MICRO:0000179';micro['ontology_mapping'].update(ontology_id='MICRO:0000179',ontology_label='polypeptone',ontology_source='MICRO',mapping_quality='EXACT_MATCH');micro['ontology_mapping']['evidence'].append({'evidence_type':'LLM_SUGGESTION','source':'https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000179','notes':'Conditional interpretation if coordinator settles the BD blend owner scope; explicit definition and BD provenance reviewed, not label-only. Not selected or applied.'})
fr,fs=project(foodon);mr,ms=project(micro)
keys=lambda rows:[(r['predicate_id'],r['object_id']) for r in rows]
assert keys(br)==keys(sr)==[('skos:exactMatch','kgmicrobe.ingredient:polypeptone')]
assert keys(fr)==[('skos:broadMatch','FOODON:03315306'),('skos:exactMatch','kgmicrobe.ingredient:polypeptone')]
assert keys(mr)==[('skos:exactMatch','MICRO:0000179')]
blocked=['Polypepton (Nihon Pharm. Co.)','Polypepton (Nihon Seiyaku)','Hipolypepton','Hipolypepton (Nihon seiyaku)','Hipolypepton*']
for r in sr:
 for label in blocked:assert label not in r.get('other','').split('|')
errors={n:[str(e) for e in validate_ingredient(r)] for n,r in [('selected',selected),('conditional_foodon',foodon),('conditional_micro',micro)]};assert not any(errors.values()),errors
m._check_producer_bindings()
out={'author':'/root/polypeptone_supplement','run_at':datetime.now(timezone.utc).isoformat(),'status':'PASS','producer':{'path':str(builder),'sha256':sha(builder)},'owner_index_scope':'All maintained ingredient records with all current selected W05 proposals overlaid in memory; proposed owner replacement then conditional single-record options, no output surfaces written.','baseline_record_count':len(base),'selected_proposal_count':len(ps),'shadow_record_count':len(records),'selected_payload_sha256':sha(S/'proposed/Polypeptone.yaml'),'before_rows':br,'selected_after_rows':sr,'selected_suppressions':ss,'conditional_foodon_rows':fr,'conditional_foodon_suppressions':fs,'conditional_micro_rows':mr,'conditional_micro_suppressions':ms,'strict_schema_errors':errors,'blocked_aliases_absent_from_selected_other':blocked,'interpretation':'Only selected_after_rows correspond to the selected source payload. FOODON/MICRO rows are explicitly conditional projections, not rival owner proposals, integration decisions or export approval. Final grounding POLYPEPTONE-001 remains open. Named component obligations remain in the conditional scope matrix.'}
p=S/'native-options.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'PASS','selected_rows':len(sr),'conditional_foodon_rows':len(fr),'conditional_micro_rows':len(mr),'selected_proposals':len(ps)},indent=2))
