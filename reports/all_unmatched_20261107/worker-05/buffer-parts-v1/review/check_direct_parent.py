import json,hashlib,importlib.util,sys
from pathlib import Path
from datetime import datetime,timezone
import yaml
R=Path.cwd();S=R/'.temp/w05-buffer-parts-v1';Q=S/'review';B=R/'reports/all_unmatched_20261107/worker-05'
def h(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def j(p):return json.loads(Path(p).read_text())
def oh(v):return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def b(p):return {'path':str(Path(p).relative_to(R)),'sha256':h(p)}
f=S/'parents-direct-v1/proposed/Peptone.yaml';old=S/'parents/proposed-v2/Peptone.yaml';a=yaml.safe_load(old.read_text());z=yaml.safe_load(f.read_text())
assert z['identifier']=='mesh:D010461';m=z['ontology_mapping'];assert [m[k] for k in ['ontology_id','ontology_label','ontology_source','mapping_quality']]==['mesh:D010461','Peptones','MESH','EXACT_MATCH']
assert z['curation_history'][:-1]==a['curation_history'];assert m['evidence'][:len(a['ontology_mapping']['evidence'])]==a['ontology_mapping']['evidence']
assert len(m['evidence'])-len(a['ontology_mapping']['evidence'])==3
assert all(x['evidence_type']=='LLM_SUGGESTION' for x in m['evidence'][-3:])
protected={k:a.get(k)==z.get(k) for k in a.keys()|z.keys() if k not in ['identifier','ontology_mapping','curation_history','notes']};assert all(protected.values())
builder=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/claw/scripts/build_mim_ingredient_sssom.py');assert h(builder)==h(B/'final-correction-v1/inputs/pinned-native-row-builder.py');sys.path.insert(0,str(builder.parent));spec=importlib.util.spec_from_file_location('review_direct_builder',builder);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
rows=mod._row_from_yaml(f,{},{},{},{},record=z,owners={});assert len(rows)==1 and rows[0]['object_id']=='mesh:D010461' and rows[0]['predicate_id']=='skos:exactMatch'
hits=[];n=0
for p in (R/'data/ingredients').rglob('*.yaml'):
 d=yaml.safe_load(p.read_text());n+=1
 if d.get('identifier')=='mesh:D010461':hits.append(b(p))
assert not hits
ds=j(S/'parents-direct-v1/decisions.json')['decisions'];oldDs={d['case_id']:d for d in j(S/'parents/final/decisions.json')['decisions']};dc=[]
for d in ds:
 oldd=oldDs[d['case_id']];ch=[k for k in d.keys()|oldd.keys() if d.get(k)!=oldd.get(k)];assert all(d.get(k)==oldd.get(k) for k in ['case_id','case_input_sha256','source','occurrence_ids','disposition','owner_records','proposal_ids'])
 dc.append({'case_id':d['case_id'],'object_sha256':oh(d),'changed_fields':ch})
v={'reviewer':'/root/final_skeptical','at':datetime.now(timezone.utc).isoformat(),'before':b(old),'after':b(f),'protected_fields':protected,'old_history_and_evidence_exact_prefix':True,'new_mapping_evidence':m['evidence'][-3:],'complete_native_rows':rows,'builder':b(builder),'maintained_search':{'count':n,'all_paths_including_ignored':True,'direct_identifier_hits':hits},'decision_checks':dc,'scientific_interpretation':b(Q/'ontology-interpretation-reassessment-v1.json'),'assessment':'Complete final Peptone payload read. The direct ordinary generic material sense is supported by NLM definition/entry term and manufacturer material description; source labels have no independently established different specified preparation. Current notes clearly supersede prior assay-gate/FoodOn inference while retaining the actual earlier history and evidence. No process, manufacturer, nutrient role or source-occurrence approval is added. Exact one-row native identity agrees with selected semantics; generic references require separate final byte review.','status':'EXACT_PAYLOAD_SCIENCE_PASS_PENDING_FINAL_MANIFEST_AND_COMPOSITION'}
p=Q/'direct-parent-independent-review-v1.json';assert not p.exists();p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n');print(h(p),h(f))
