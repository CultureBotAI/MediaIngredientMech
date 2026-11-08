import json,hashlib,pathlib,importlib.util,sys
from datetime import datetime,timezone
import yaml
R=pathlib.Path.cwd();S=R/'.temp/w05-buffer-parts-v1';B=R/'reports/all_unmatched_20261107/worker-05'
def h(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def oh(v):return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def read(p):return json.loads(pathlib.Path(p).read_text())
def cap(c):
 q=c['path'];p=S/q.split('buffer-parts-v1/',1)[1] if q.startswith('buffer-parts-v1/') else B/q
 assert h(p)==c['sha256'],str(p)
 return p
bp={p['proposal_id']:p for p in read(B/'tellurium-polypeptone-v1/core/proposals.json')['proposals']}
bd={d['case_id']:d for d in read(B/'tellurium-polypeptone-v1/core/decisions.json')['decisions']}
builder=pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/claw/scripts/build_mim_ingredient_sssom.py');assert h(builder)==h(B/'final-correction-v1/inputs/pinned-native-row-builder.py');sys.path.insert(0,str(builder.parent));sp=importlib.util.spec_from_file_location('review_mim_builder',builder);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
out={'reviewer':'/root/final_skeptical','at':datetime.now(timezone.utc).isoformat(),'native_builder_sha256':h(builder),'payload_checks':[],'decision_checks':[],'evidence_capture_checks':[]}
for lane,pfile,dfile,efile in [('parents','final/proposals.json','final/decisions.json','final/evidence.json'),('media','proposals-v2.json','decisions-v2.json','evidence-v2.json')]:
 for p in read(S/lane/pfile)['proposals']:
  oldp=bp[p['proposal_id']];oldf=cap(oldp['after_capture']);newf=cap(p['after_capture']);a=yaml.safe_load(oldf.read_text());b=yaml.safe_load(newf.read_text())
  changed=[k for k in a.keys()|b.keys() if a.get(k)!=b.get(k)]
  preserved={k:a.get(k)==b.get(k) for k in ['occurrence_statistics','nutritional_roles','biological_roles','roles','causal_graphs','synonyms','merged','chemical_properties','supplied_form']}
  assert all(preserved.values()),(p['proposal_id'],preserved)
  assert b.get('curation_history',[])[:len(a.get('curation_history',[]))]==a.get('curation_history',[])
  assert b.get('ontology_mapping',{}).get('evidence',[])[:len(a.get('ontology_mapping',{}).get('evidence',[]))]==a.get('ontology_mapping',{}).get('evidence',[])
  changes=[]
  if lane=='media':
   assert len(a.get('components',[]))==len(b.get('components',[]))
   for i,(x,y) in enumerate(zip(a.get('components',[]),b.get('components',[]))):
    assert {k:v for k,v in x.items() if k not in ['reference_scope','component_id']}=={k:v for k,v in y.items() if k not in ['reference_scope','component_id']}
    if x!=y:changes.append({'index':i,'before':x,'after':y})
  rows=m._row_from_yaml(newf,{},{},{},{},record=b,owners={});oldrows=m._row_from_yaml(oldf,{},{},{},{},record=a,owners={})
  out['payload_checks'].append({'lane':lane,'proposal_id':p['proposal_id'],'proposal_object_sha256':oh(p),'before_capture':oldp['after_capture'],'after_capture':p['after_capture'],'changed_top_fields':changed,'protected_fields_identical':preserved,'old_history_exact_prefix':True,'mapping_evidence_old_prefix_identical':True,'component_changes':changes,'complete_native_before':oldrows,'complete_native_after':rows})
 for d in read(S/lane/dfile)['decisions']:
  old=bd[d['case_id']];changed=[k for k in old.keys()|d.keys() if old.get(k)!=d.get(k)]
  protected={k:old.get(k)==d.get(k) for k in ['case_id','source','source_case_id','input_case_sha256','occurrence_ids','source_holds','owner_holds','export_hold','negative_evidence','inherited_negatives','quarantine'] if k in old or k in d}
  assert all(protected.values())
  out['decision_checks'].append({'lane':lane,'case_id':d['case_id'],'before_object_sha256':oh(old),'selected_decision_object_sha256':oh(d),'changed_top_fields':changed,'protected_fields_equal':protected})
 for e in read(S/lane/efile)['evidence']:
  f=cap(e['capture']);out['evidence_capture_checks'].append({'lane':lane,'evidence_id':e['evidence_id'],'kind':e['kind'],'path':str(f.relative_to(R)),'sha256':h(f),'capture_verified':True})
hits=[];count=0
for p in (R/'data/ingredients').rglob('*.yaml'):
 d=yaml.safe_load(p.read_text());count+=1
 if d.get('identifier')=='MICRO:0000181':hits.append({'path':str(p.relative_to(R)),'sha256':h(p),'mapping_status':d.get('mapping_status')})
selectedhits=[]
for p in bp.values():
 d=yaml.safe_load(cap(p['after_capture']).read_text())
 if d.get('identifier')=='MICRO:0000181':selectedhits.append(p['proposal_id'])
out['bounded_duplicate_check']={'method':'Path.rglob all individual YAML and all published selected W05 proposal YAML; includes ignored paths','maintained_scanned':count,'selected_scanned':len(bp),'maintained_MICRO181_hits':hits,'selected_MICRO181_hits':selectedhits,'limit':'No cross-worker merge, tombstone or global source membership conclusion.'}
assert not hits and not selectedhits
f=S/'review/parents-media-independent-checks-v1.json';assert not f.exists();f.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n');print(f.relative_to(R),h(f));print('payloads',len(out['payload_checks']),'decisions',len(out['decision_checks']),'evidence',len(out['evidence_capture_checks']))
