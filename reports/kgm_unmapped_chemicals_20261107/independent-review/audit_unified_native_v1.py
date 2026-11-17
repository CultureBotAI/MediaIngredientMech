from pathlib import Path
import hashlib,json,os,subprocess,csv,io,datetime,importlib.util
T=Path(__file__).resolve().parents[1];W=T/'worktree';R=T/'reviewer'/'unified-native-review-v1';R.mkdir(exist_ok=False);ROOT=T.parents[1];C=ROOT.parent/'CultureMech';K=T/'claw';N=W/'reports/kgm_unmapped_chemicals_20261107/unified-generation';tr=json.loads((N/'traced-rebuild.json').read_bytes());h=lambda b:hashlib.sha256(b).hexdigest()
roots={'mim':W,'culturemech':C,'culturemech_comparison':C,'claw':K}
def inputs():
 result={}
 for key,pinned in tr['inputs'].items():
  kind,rel=key.split(':',1);result[key]=h((roots[kind]/rel).read_bytes())
 return result
before=inputs();assert before==tr['inputs']
expected=set()
for cat in ('mapped','unmapped'):
 expected|={'mim:'+str(p.relative_to(W)) for p in (W/'data/ingredients'/cat).glob('*.yaml')}
expected|={'mim:docs/data/label_index.csv','mim:mappings/unified_mapping_rejections.tsv'}
expected|={'culturemech:'+str(p.relative_to(C)) for p in (C/'data/normalized_yaml').rglob('*.yaml')}
expected|={'culturemech_comparison:output/ingredients_list.tsv','culturemech_comparison:output/ingredient_occurrences.tsv','claw:scripts/build_unified_ingredient_mapping.py','claw:plugins/ingredient_name_normalizer.py'}
expected|={'claw:'+str(p.relative_to(K)) for p in (K/'src/kg_microbe_fleet').rglob('*.py')};assert expected==set(before)
cmd=[str(T/'env/bin/python'),'-B',str(K/'scripts/build_unified_ingredient_mapping.py'),'--culturemech',str(C),'--mim',str(W),'--output',str(R/'native-replay.tsv'),'--format','tsv']
env=os.environ.copy();env.update({'CULTUREMECH_ROOT':str(C),'MEDIAINGREDIENTMECH_ROOT':str(W),'PYTHONDONTWRITEBYTECODE':'1'});run=subprocess.run(cmd,env=env,capture_output=True);(R/'native-replay.log').write_bytes(run.stdout+run.stderr);assert run.returncode==0,run.stderr.decode();assert inputs()==before
candidate=(N/'candidate.tsv').read_bytes(); assert (R/'native-replay.tsv').read_bytes()==candidate==(W/'UNIFIED_INGREDIENT_MAPPING.tsv').read_bytes()
old=subprocess.check_output(['git','show',tr['baseline']+':UNIFIED_INGREDIENT_MAPPING.tsv'],cwd=W);a=list(csv.DictReader(io.StringIO(old.decode()),delimiter='\t'));b=list(csv.DictReader(io.StringIO(candidate.decode()),delimiter='\t')); assert len(a)==len(b)==4170
cells=[{'line':i+2,'ingredient':y['ingredient_name'],'column':k,'before':x[k],'after':y[k]} for i,(x,y) in enumerate(zip(a,b,strict=True)) for k in x if x[k]!=y[k]]
assert cells==[{k:v for k,v in x.items() if k in cells[0]} for x in tr['changed_cells']]
assert len(cells)==13 and len({x['line'] for x in cells})==8
assert all(x['column']=='synonyms' or x['ingredient']=='Na acetate x 3 H2O' for x in cells)
assert [(x['ingredient_name'],x['occurrence_count'],x['example_media']) for x in a]==[(x['ingredient_name'],x['occurrence_count'],x['example_media']) for x in b]
sp=importlib.util.spec_from_file_location('freshness_readonly',W/'scripts/check_unified_freshness.py'); m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);digest,count=m.inputs_digest(W/'data/ingredients');prov=json.loads((W/'UNIFIED_INGREDIENT_MAPPING.provenance.json').read_bytes());assert prov['mim_inputs_digest']==digest and prov['mim_record_count']==count==2956 and prov['artifact_sha256']==h(candidate)
assert (W/'UNIFIED_INGREDIENT_MAPPING.provenance.json').read_bytes()==(N/'candidate.provenance.json').read_bytes()
result={'reviewer':'/root/step7d_independent_review','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'result':'PASS','source_head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=W).decode().strip(),'native_replay_command':cmd,'native_replay_exit':run.returncode,'input_count':len(before),'input_membership_exact':True,'all_input_hashes_match_author_trace_before_and_after':True,'native_replay_exact_maintained_and_candidate':True,'rows':len(a),'changed_cells':cells,'membership_order_occurrences_examples_unchanged':True,'snapshot_sha256':h(candidate),'provenance_sha256':h((W/'UNIFIED_INGREDIENT_MAPPING.provenance.json').read_bytes()),'native_mim_digest':digest,'science_scope':'All13 changed cells derive from the source-confirmed sodium acetate trihydrate alias; MAPPED in unified is not a scientific release disposition. No role/other identity or downstream adoption approval.','limitations':['Working tree only; final committed head and full required checks still pending.','Read-only replay writes only this private reviewer directory.']}
(R/'assessment.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ('changed_cells','native_replay_command')},indent=2))
