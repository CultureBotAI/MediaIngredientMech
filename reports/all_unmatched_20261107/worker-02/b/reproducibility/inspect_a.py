import json,yaml,hashlib,sys
from pathlib import Path
src=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5');root=Path('reports/all_unmatched_20261107/worker-02');d=json.loads((root/'a/decisions.json').read_text())['decisions'];e={x['evidence_id']:x for x in json.loads((root/'a/evidence.json').read_text())['evidence']};cs=json.loads(Path('.temp/all-unmatched-worker-02/cases-a.json').read_text());out=[]
for i,(c,v) in enumerate(zip(cs,d)):
 z={'index':i,'case':c,'decision':v,'full_recipe_contexts':[],'primary_components':[]}
 for o in c['occurrences']:
  p=src/o['full_recipe_snapshot'];assert hashlib.sha256(p.read_bytes()).hexdigest()==o['source_file_sha256'];r=yaml.safe_load(p.read_text());z['full_recipe_contexts'].append({'occurrence':o,'complete_recipe':r})
 for eid in v['evidence_ids']:
  ev=e[eid]
  if ev['kind']=='primary_source' and 'togo-' in ev['capture']['path']:
   q=json.loads((root/ev['capture']['path']).read_text())
   if 'components' in q:
    hits=[]
    for g in q['components']:
     for item in g.get('items',[]):
      if item.get('component_name')==c['source_label']:hits.append({'group':g.get('subcomponent_name'),'item':item})
    z['primary_components'].append({'evidence_id':eid,'meta':q.get('meta'),'hits':hits,'comments':q.get('comments',[])})
 out.append(z)
p=Path('.temp/all-unmatched-worker-02/b/review-a-contexts.json');p.write_text(json.dumps(out,ensure_ascii=False,indent=2));print(len(out),'complete cases/recipes bound to original hashes')
lo=int(sys.argv[1]);hi=int(sys.argv[2])
for z in out[lo:hi]:
 c=z['case'];print('\nCASE',z['index'],c['source_label'],'occ',len(c['occurrences']));print('RAW',[o['raw_component'] for o in c['occurrences']]);print('API',[(x['meta'],[{k:h['item'].get(k) for k in ['component_name','label','volume','unit','conc_value','conc_unit','reference_media_id']} for h in x['hits']]) for x in z['primary_components']]);print('RECIPE_NOTES',[x['complete_recipe'].get('notes') for x in z['full_recipe_contexts']])
