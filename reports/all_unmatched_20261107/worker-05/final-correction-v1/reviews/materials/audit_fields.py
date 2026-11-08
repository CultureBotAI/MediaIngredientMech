from pathlib import Path
import json,yaml,hashlib,datetime,collections
from mediaingredientmech.validation.write_validated import validate_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
O=Path(__file__).parent;P=O.parent/'materials';B=Path('reports/all_unmatched_20261107/worker-05')
def load(p):return json.loads(Path(p).read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ch(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def delta(a,b,path=''):
 if type(a)!=type(b):return [{'path':path,'before':a,'after':b}]
 if isinstance(a,dict):
  z=[]
  for k in sorted(a.keys()|b.keys()):
   if k not in a or k not in b:z.append({'path':path+'/'+k,'before':a.get(k),'after':b.get(k)})
   else:z+=delta(a[k],b[k],path+'/'+k)
  return z
 if isinstance(a,list):
  if a==b:return []
  return [{'path':path,'before':a,'after':b}]
 return [] if a==b else [{'path':path,'before':a,'after':b}]
R=load(O/'whole-records.json');out=[];errors=[]
for r in R:
 p=r['proposal'];after=r['record'];prior=r['predecessor'];before=r['before'] or {};er=validate_ingredient(after)
 assert not er,(p['proposal_id'],er)
 for f in ['occurrence_statistics','source_occurrences','nutritional_roles','physicochemical_roles','cellular_metabolic_roles','causal_graphs','culturemech_reference']:
  assert after.get(f)==prior.get(f),(p['proposal_id'],f)
 oldhuman=[x for x in (before.get('ontology_mapping') or {}).get('evidence',[]) if x.get('evidence_type')=='MANUAL_CURATION']
 newhuman=[x for x in (after.get('ontology_mapping') or {}).get('evidence',[]) if x.get('evidence_type')=='MANUAL_CURATION']
 assert all(x in oldhuman for x in newhuman),(p['proposal_id'],newhuman,oldhuman)
 assert newhuman==[x for x in (prior.get('ontology_mapping') or {}).get('evidence',[]) if x.get('evidence_type')=='MANUAL_CURATION' and x in oldhuman]
 out.append({'proposal_id':p['proposal_id'],'before_capture':p.get('before_capture'),'predecessor_capture':p['predecessor_capture'],'after_capture':p['after_capture'],'changes_from_original_before':delta(before,after),'changes_from_selected_predecessor':delta(prior,after),'inherited_human_mapping_evidence':oldhuman,'schema_errors':[]})
# Explicit filesystem globs include ignored maintained records.
base={str(p):yaml.safe_load(p.read_text()) for area in ['mapped','unmapped'] for p in Path('data/ingredients',area).glob('*.yaml')};basehash={p:sha(p) for p in base}
canonical=B/'correction-1193-v1/proposals.json';allprops=load(canonical)['proposals'];overlay=dict(base)
for p in allprops:
 overlay.pop(p['owner_path'],None)
 target=p.get('destination_owner_path') or p['owner_path'];overlay[target]=yaml.safe_load((B/p['after_capture']['path']).read_text())
for x in R:
 p=x['proposal'];overlay.pop(p['owner_path'],None);overlay[p.get('destination_owner_path') or p['owner_path']]=x['record']
def incoming(cat):
 return [{'owner_path':p,'owner_sha256':basehash.get(p),'component_path':f'components/{i}','component':c} for p,r in cat.items() if r.get('mapping_status')!='REJECTED' for i,c in enumerate(r.get('components',[])) if c.get('component_id')=='MICRO:0000178' and c.get('reference_scope')=='MIM_CATALOG']
inb=incoming(base);ino=incoming(overlay);v=validate_component_partonomy(overlay.values());assert not v,v
expected=load(P/'integration-dependencies.json');assert len(inb)==len(expected['fresh_baseline_inbound']);assert {(x['owner_path'],x['component_path'],ch(x['component'])) for x in ino}=={(x['owner_path'],x['component_path'],ch(x['component'])) for x in expected['published_overlay_plus_materials_successors_inbound']}
# Capture every dependency owner as inspection input in the review packet only.
(O/'dependency-before').mkdir(exist_ok=True)
for v in inb:
 path=Path(v['owner_path']);(O/'dependency-before'/path.name).write_bytes(path.read_bytes())
ID={}
for p,r in overlay.items():
 if r.get('mapping_status')!='REJECTED':ID.setdefault(r['identifier'],[]).append(p)
selected_collisions=[{'proposal_id':x['proposal']['proposal_id'],'identifier':x['record']['identifier'],'owner_paths':ID.get(x['record']['identifier'],[])} for x in R if len(ID.get(x['record']['identifier'],[]))>1]
result={'reviewer':'/root/media_research','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'schema_scope':'39 final complete payloads through unchanged validate_ingredient(closed=True); no payload write','schema_pass':True,'field_reviews':out,'baseline_file_count':len(base),'baseline_file_hashes':basehash,'overlay_input':{'path':str(canonical),'sha256':sha(canonical),'original_proposal_count':len(allprops),'materials_replacements':len(R)},'partonomy_scope':'Original selected published proposal overlay plus39 materials successors by removing original owner paths before insertion. Not the later final141 or coordinator union.','partonomy_errors':[],'baseline_peptone_inbound':inb,'overlay_peptone_inbound':ino,'selected_identifier_collisions':selected_collisions,'no_new_human_mapping_evidence':True,'protected_role_count_graph_fields_unchanged':True}
assert not (O/'field-and-structural-audit.json').exists();(O/'field-and-structural-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('schema39 PASS; original overlay',len(allprops),'partonomyPASS; baseline',len(base),'Peptone inbound',len(inb),'then',len(ino),'selected collisions',selected_collisions)
for r in out:print(r['proposal_id'],[d['path'] for d in r['changes_from_selected_predecessor']])
