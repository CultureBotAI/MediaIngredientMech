import json,pathlib,hashlib,copy,importlib.util,sys
from datetime import datetime,timezone
import yaml
from mediaingredientmech.synonym_policy import preferred_term_owners
R=pathlib.Path.cwd();S=R/'.temp/w05-buffer-parts-v1';B=R/'reports/all_unmatched_20261107/worker-05'
def h(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(pathlib.Path(p).read_text())
p=S/'parents/tombstone';bf=p/'before/Bacto_Soytone.yaml';vf=p/'proposed/Bacto_Soytone.yaml';af=p/'proposed-v2/Bacto_Soytone.yaml'
a=yaml.safe_load(bf.read_text());v=yaml.safe_load(vf.read_text());b=yaml.safe_load(af.read_text())
assert bf.read_bytes()==(R/'data/ingredients/mapped/Bacto_Soytone.yaml').read_bytes()
assert h(bf)=='b9c7e1b675da46d8733749a16b9c56f07618bb63ab5ecd71bdef1bf1cc2d2535'
assert b['representative']=='' and 'representative' in b and b['mapping_status']=='REJECTED'
assert b['curation_history'][:-1]==a['curation_history']
assert b['ontology_mapping']['evidence'][:-1]==a['ontology_mapping']['evidence']
assert {k:x for k,x in b.items() if k not in ['representative','curation_history','notes','ontology_mapping']}=={k:x for k,x in a.items() if k not in ['representative','curation_history','notes','ontology_mapping']}
assert {k:x for k,x in b['ontology_mapping'].items() if k!='evidence'}=={k:x for k,x in a['ontology_mapping'].items() if k!='evidence'}
expected=copy.deepcopy(v);expected['ontology_mapping']['evidence'][2]['notes']=expected['ontology_mapping']['evidence'][2]['notes'].replace('historical human evidence','historical evidence');assert b==expected
records={str(x.relative_to(R/'data/ingredients')):yaml.safe_load(x.read_text()) for x in (R/'data/ingredients').rglob('*.yaml')}
ps=read(B/'tellurium-polypeptone-v1/core/proposals.json')['proposals']
for q in ps:
 records[str(pathlib.Path(q['owner_path']).relative_to('data/ingredients'))]=yaml.safe_load((B/q['after_capture']['path']).read_text())
for q in read(S/'parents/final/proposals.json')['proposals']:
 records[str(pathlib.Path(q['owner_path']).relative_to('data/ingredients'))]=yaml.safe_load((S/q['after_capture']['path'].split('buffer-parts-v1/',1)[1]).read_text())
mapped={'MIM:'+pathlib.Path(k).stem:d for k,d in records.items() if k.startswith('mapped/')};key='MIM:Bacto_Soytone';mapped[key]=a
old=sorted(preferred_term_owners(mapped)['bacto soytone']);removed=copy.deepcopy(a);removed.pop('representative');mapped[key]=removed;fallback=sorted(preferred_term_owners(mapped)['bacto soytone']);mapped[key]=b;new=sorted(preferred_term_owners(mapped)['bacto soytone'])
assert old==fallback and new==['MIM:Bacto_Soytone'] and len(old)>1
builder=pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/claw/scripts/build_mim_ingredient_sssom.py');sys.path.insert(0,str(builder.parent));sp=importlib.util.spec_from_file_location('tombstone_builder',builder);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
oldrows=m._row_from_yaml(bf,{},{},{},{},record=a,owners={});newrows=m._row_from_yaml(af,{},{},{},{},record=b,owners={});assert oldrows==newrows==[]
out={'reviewer':'/root/final_skeptical','at':datetime.now(timezone.utc).isoformat(),'before':{'path':str(bf.relative_to(R)),'sha256':h(bf)},'original_unselected':{'path':str(vf.relative_to(R)),'sha256':h(vf)},'selected':{'path':str(af.relative_to(R)),'sha256':h(af)},'authentic_before_matches_maintained_bytes':True,'old_history_and_evidence_exact_prefix':True,'identity_status_names_counts_roles_preserved':True,'v1_to_v2_only_new_unsupported_human_phrase_removed':True,'native_policy':{'path':'src/mediaingredientmech/synonym_policy.py','sha256':h(R/'src/mediaingredientmech/synonym_policy.py')},'native_regression_definition':{'path':'tests/test_sssom_other_cross_record.py','sha256':h(R/'tests/test_sssom_other_cross_record.py'),'actual_read_lines':'294-307; test definition read, not executed'},'actual_inmemory_native_ownership':{'before':old,'field_removed':fallback,'explicit_empty':new},'complete_native_rows':{'before':oldrows,'after':newrows},'builder_sha256':h(builder),'scientific_assessment':'The explicit unresolved redirect avoids assigning the historical Bacto product name to multiple current shared-ID owners or to the generic Soy term. The manufacturer differentiates the named products; no same-product bridge is established. Preserving a rejected tombstone with unresolved representative is supported. This does not restore an active Bacto owner or undo historical occurrence transfer.','limitations':['Owner membership and a future scientifically established branded representative remain root-owned.','All original mapping identifiers/evidence remain historical tombstone provenance, not newly approved live identity.','Final full-overlay/native batch checks are separate.']}
f=S/'review/tombstone-independent-review-v1.json';assert not f.exists();f.write_text(json.dumps(out,indent=2)+'\n');print(f.relative_to(R),h(f))
