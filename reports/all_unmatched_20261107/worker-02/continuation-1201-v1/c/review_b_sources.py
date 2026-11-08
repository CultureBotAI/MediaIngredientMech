import json,yaml,re,subprocess,hashlib
from pathlib import Path
R=Path('reports/all_unmatched_20261107/worker-02');S=R/'continuation-1201-v1';C=S/'c';B=S/'b'
E={e['evidence_id']:e for f in [R/'evidence.json',B/'evidence.json'] for e in json.loads(f.read_text())['evidence']};D=json.loads((B/'decisions.json').read_text())['decisions'];out=[]
for d in D:
 i=d.get('scope_index',d.get('shard_case_index'))
 if i in [112,117]:continue
 case=json.loads((R/f'b/captures/case-{i}.json').read_text());entries=[]
 for eid in d['evidence_ids']:
  e=E[eid];p=(R if e['capture']['root']=='artifact' else Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5'))/e['capture']['path'];raw=p.read_bytes();assert hashlib.sha256(raw).hexdigest()==e['capture']['sha256'],eid
  if e['kind']!='primary_source':continue
  if not (('togo-' in eid and 'failures' not in eid) or eid.startswith('b2-')):continue
  try:x=json.loads(raw)
  except:continue
  entries.append({'eid':eid,'url':e.get('url'),'full_json':x})
 out.append({'index':i,'case_id':d['case_id'],'frozen_complete_case':case,'primary_jsons':entries})
(C/'review-b-full-sources.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print('Read and hash-verified all linked evidence; complete frozen case objects and primary API JSON saved',len(out))
for x in out:
 print('\nCASE',x['index'],x['frozen_complete_case']['raw_source_label'])
 for o in x['frozen_complete_case']['occurrences']:print(o['recipe_id'],o['component_path'],o['raw_component'])
 print('PRIMARY API',[(e['eid'],e['url']) for e in x['primary_jsons']])
