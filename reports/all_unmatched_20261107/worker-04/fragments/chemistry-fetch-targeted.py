"""Targeted exact-source and ontology discovery captures, 2026-11-08."""
import importlib.util,json,pathlib,concurrent.futures,re,urllib.parse,yaml
spec=importlib.util.spec_from_file_location('capture','reports/all_unmatched_20261107/worker-04/fragments/chemistry-fetch.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
d=json.load(open('reports/all_unmatched_20261107/worker-04/fragments/chemistry-assignment.json'))
base=pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
queries=['retinol','barium carbonate','D-glutamate','ammonium heptamolybdate tetrahydrate','ammonium heptamolybdate dihydrate','sodium tungstate monohydrate','sodium tungstate hexahydrate','trisodium citrate pentahydrate','trisodium citrate trihydrate','potassium glutamate','ammonium tartrate','sodium alpha ketoglutarate','ardacin B','grisamine','actinomycetin','iron dicitrate','TAPS','magnesium hydrogen citrate']
jobs=[('ols-search-'+str(i)+'.json','https://www.ebi.ac.uk/ols4/api/search?q='+urllib.parse.quote(q)+'&ontology=chebi,ncit&rows=20') for i,q in enumerate(queries)]
seen={x[0] for x in jobs}
for c in d['cases']:
 for o in c.get('occurrences',[]):
  txt=(base/o['full_recipe_snapshot']).read_text()
  for mid in set(re.findall(r'https://togomedium.org/(?:medium/|sparqlist/api/gmdb_medium_by_gmid\?gm_id=)M([0-9]+)',txt)):
   name=f'togo-{mid}.json'
   if name not in seen and not (m.ROOT/name).exists(): jobs.append((name,f'https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M{mid}'));seen.add(name)
  for rid in set(re.findall(r'GRMD=([0-9]+)',txt)):
   name=f'jcm-{rid}.html'
   if name not in seen:jobs.append((name,f'https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD={rid}'));seen.add(name)
  for sid in set(re.findall(r'https://mediadive.dsmz.de/rest/solution/([0-9]+)',txt)):
   name=f'mediadive-solution-{sid}.json'
   if name not in seen:jobs.append((name,f'https://mediadive.dsmz.de/rest/solution/{sid}'));seen.add(name)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as p: receipts=list(p.map(m.capture,jobs))
(m.ROOT/'targeted-retrieval-receipts.json').write_text(json.dumps({'queries':queries,'receipts':receipts},indent=2)+'\n')
print('Captured',len(receipts),'responses; errors',[r for r in receipts if 'error' in r])
