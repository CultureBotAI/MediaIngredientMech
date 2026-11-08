from pathlib import Path
from datetime import datetime, timezone
import collections, dataclasses, hashlib, importlib.util, json, subprocess, sys, yaml

sys.path.insert(0,str(Path('src').resolve()))
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy

O=Path(__file__).resolve().parent; S=O.parent
R=Path('reports/all_unmatched_20261107/worker-05').resolve()
C=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
Q=C/'queue/preliminary-v5'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def objsha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
def dump(n,x):
 p=O/n; assert not p.exists(); p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def resolve(c):
 if c['root']=='source': return Q/c['path']
 assert c['root']=='artifact', c
 p=Path(c['path'])
 if str(p).startswith('final-correction-v1/'):
  local=S/p.relative_to('final-correction-v1')
  if local.exists(): return local
 return R/p
D=json.loads((O/'decisions-v1.json').read_text()); P=json.loads((O/'proposals-v1.json').read_text()); E=json.loads((O/'evidence-v1.json').read_text()); K=json.loads((O/'primary-case-conclusions-v1.json').read_text())
D0=json.loads((S/'remediation/chemical-report-v2/decisions-v3.json').read_text()); P0=json.loads((S/'chemicals/proposals-v3.json').read_text()); E0=json.loads((S/'remediation/chemical-report-v1/evidence-v2.json').read_text()); K0=json.loads((S/'remediation/chemical-report-v3/primary-case-conclusions-v3.json').read_text())
assert (len(D),len(P),len(E))==(67,58,528)
assert P[:57]==P0 and E[:525]==E0
assert [i for i,(a,b) in enumerate(zip(D,D0)) if a!=b]==[10,48]
assert [i for i,(a,b) in enumerate(zip(K['case_reviews'],K0['case_reviews'])) if a!=b]==[10,48]
assert len({d['case_id'] for d in D})==67 and len({p['proposal_id'] for p in P})==58
assert len({e['evidence_id'] for e in E})==528
assert len({p['owner_path'] for p in P})==58
eids={e['evidence_id'] for e in E}; pids={p['proposal_id'] for p in P}
for d,old in zip(D,D0):
 for key in ['case_id','case_input_sha256','occurrence_ids','source','preserved_source_holds']:
  assert d[key]==old[key], (d['case_id'],key)
 assert set(d['evidence_ids'])<=eids and set(d['proposal_ids'])<=pids
captures=[]
for e in E:
 path=resolve(e['capture']); assert sha(path)==e['capture']['sha256'], path
 captures.append({'evidence_id':e['evidence_id'],'path':str(path),'sha256':sha(path)})
records={str(p):yaml.safe_load(p.read_text()) for p in Path('data/ingredients').rglob('*.yaml')}
baseline_count=len(records)
def duplicates(rs): return {k:v for k,v in collections.Counter(r['identifier'] for r in rs.values() if r['mapping_status']!='REJECTED').items() if v>1}
before_dup=duplicates(records)
baseline_violations=validate_component_partonomy(records.values())
targets=[]; checks=[]
for p in P:
 path=resolve(p['after_capture']); assert sha(path)==p['after_capture']['sha256']; new=yaml.safe_load(path.read_text()); targets.append(str(path))
 if p['before_sha256']:
  assert sha(Path(p['owner_path']))==p['before_sha256']; old=records.pop(p['owner_path']); assert new['curation_history'][:len(old['curation_history'])]==old['curation_history']
 else: assert p['owner_path'] not in records and not Path(p['owner_path']).exists()
 dst=p.get('destination_owner_path',p['owner_path']); assert dst not in records; assert dst.split('/')[2]==new['mapping_status'].lower(); records[dst]=new
 linked=[d for d in D if d['case_id'] in p['case_ids']]; assert len(linked)==len(p['case_ids']); assert all(p['proposal_id'] in d['proposal_ids'] for d in linked)
 assert set(p.get('applies_to_occurrence_ids',[]))<={x for d in linked for x in d['occurrence_ids']}
 assert set(p['evidence_ids'])<=eids
 checks.append({'proposal_id':p['proposal_id'],'after_capture':p['after_capture'],'before_sha256':p['before_sha256'],'case_and_occurrence_routes_valid':True})
new=P[-1]; rec=records[new['owner_path']]
assert len(rec['synonyms'])==2 and {x['synonym_text'] for x in rec['synonyms']}=={D[i]['source']['raw_source_label'] for i in [10,48]}
assert new['applies_to_occurrence_ids']==D[10]['occurrence_ids']+D[48]['occurrence_ids']
assert all(k not in rec for k in ['chemical_properties','components','component_assertion','supplied_form','solution_type','nutritional_roles','functional_roles'])
assert rec['identifier']==rec['ontology_mapping']['ontology_id']=='kgmicrobe.compound:thiamine_hcl_monohydrate'
assert all(e['evidence_type']=='LLM_SUGGESTION' for e in rec['ontology_mapping']['evidence'])
assert rec['curation_history'][0]['llm_assisted'] is True
after=validate_component_partonomy(records.values()); after_dup=duplicates(records)
introduced={k:v for k,v in after_dup.items() if v>before_dup.get(k,1)}
builder=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/claw/scripts/build_mim_ingredient_sssom.py')
spec=importlib.util.spec_from_file_location('mim_supplement_native_builder',builder); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
owners=mod.build_owner_index({mod._mim_curie(Path(path).name):r for path,r in records.items() if r['mapping_status']=='MAPPED'})
rows=mod._row_from_yaml(Path(new['owner_path']),{},{},{},{},record=rec,owners=owners)
assert len(rows)==1 and rows[0]['predicate_id']=='skos:exactMatch' and rows[0]['object_id']==rec['identifier'],rows
assert 'CAS:' not in rows[0]['other'] and all(x['synonym_text'] in rows[0]['other'] for x in rec['synonyms'])
dump('native-projection-v1.json',{'author':'/root/chemicals_research','at':datetime.now(timezone.utc).isoformat(),'builder':str(builder),'builder_sha256':sha(builder),'proposal_id':new['proposal_id'],'after_capture':new['after_capture'],'before_rows':[],'after_rows':rows,'scope':'Isolated projection of the new candidate against this lane substituted into the maintained baseline; no export, gate, owner or application change. External label/source dictionaries are empty. Registry-only exact row does not validate unknown molecular grounding.'})
cmd=[sys.executable,'scripts/validate_strict.py',*targets,'--workers','1','--out',str(O/'strict-errors-v1.tsv')]
run=subprocess.run(cmd,capture_output=True,text=True); (O/'strict-validation-v1.log').write_text(run.stdout+run.stderr)
dump('integrity-validation-v1.json',{'author':'/root/chemicals_research','at':datetime.now(timezone.utc).isoformat(),'counts':{'cases':len(D),'proposals':len(P),'evidence':len(E),'maintained_baseline':baseline_count},'changed_case_indices':[10,48],'unchanged_prior_proposals':57,'unchanged_prior_evidence':525,'unchanged_other_case_conclusions':65,'all_source_case_hashes_raw_names_occurrences_and_holds_unchanged':True,'original_bottom_layer_and_mkp_remediations_preserved':True,'strict_exit_code':run.returncode,'strict_command':cmd,'baseline_partonomy_violations':[dataclasses.asdict(x) for x in baseline_violations],'substituted_partonomy_violations':[dataclasses.asdict(x) for x in after],'introduced_identifier_collisions':introduced,'proposal_checks':checks,'evidence_capture_checks':captures,'files':{n:sha(O/n) for n in ['decisions-v1.json','proposals-v1.json','evidence-v1.json','primary-case-conclusions-v1.json','ancestry-and-remediation-v1.json','native-projection-v1.json']},'limits':'Structural validation of all 58 candidates is not scientific or simultaneous family-installation approval. The previous conditional HEPES/Wolfe/ethanol matrix remains unchanged. Root must validate the complete integrated overlay and obtain independent supplement review.'})
print(json.dumps({'strict_exit_code':run.returncode,'substituted_partonomy_violations':len(after),'introduced_identifier_collisions':introduced,'new_native_rows':rows}))
sys.exit(bool(run.returncode or after or introduced))
