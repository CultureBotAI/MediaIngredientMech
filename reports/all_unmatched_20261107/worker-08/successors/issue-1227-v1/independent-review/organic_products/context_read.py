import json,pathlib,yaml,hashlib,sys,datetime
R=pathlib.Path('reports/all_unmatched_20261107/worker-08');O=R/'successors/issue-1227-v1/independent-review/organic_products';Q=pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
E=json.loads((R/'successors/issue-1201-v1/evidence.json').read_text())['evidence'];rows=[];seen=set()
for e in E:
 if e['evidence_id'].startswith('op-context-') and e['capture']['path'] not in seen:seen.add(e['capture']['path']);rows.append(e)
# Inspect complete recipe scientific fields. Imported bookkeeping, role inferences and external ontology enrichments are not primary chemistry evidence.
strings={}
def intern(x):
 if isinstance(x,str) and len(x)>60:
  if x not in strings:strings[x]='T'+str(len(strings)+1);print('TEXT',strings[x],x)
  return '$'+strings[x]
 if isinstance(x,list):return [intern(v) for v in x]
 if isinstance(x,dict):return {k:intern(v) for k,v in x.items()}
 return x
def clean(x):
 if isinstance(x,list):return [clean(v) for v in x]
 if isinstance(x,dict):return {k:clean(v) for k,v in x.items() if k not in ['curation_history','evidence','references','target_organisms','mediaingredientmech_chebi_term','term']}
 return x
prior=None
for i in range(int(sys.argv[1]),min(int(sys.argv[2]),len(rows))):
 e=rows[i];p=Q/e['capture']['path'];assert hashlib.sha256(p.read_bytes()).hexdigest()==e['capture']['sha256'];x=yaml.safe_load(p.read_text());y=clean(x)
 if 'nldm_' in p.name and prior is not None:
  out={k:v for k,v in y.items() if prior.get(k)!=v};out['COMPARED_TO_FIRST_NLDM_IN_BATCH']=True;out['removed_keys']=[k for k in prior if k not in y]
 else:out=y
 if 'nldm_' in p.name and prior is None:prior=y
 print('CONTEXT',i,e['evidence_id'],p.name,json.dumps(intern(out),ensure_ascii=False,separators=(',',':')))
 with (O/'read-events.jsonl').open('a') as f:f.write(json.dumps({'kind':'complete_recipe_scientific_context','path':str(p),'sha256':e['capture']['sha256'],'evidence_id':e['evidence_id'],'scope_rendered':'All recipe fields except bookkeeping history, references/evidence boilerplate, target organism annotations and imported ontology term enrichments. All ingredient/solution amounts, names, notes, recipes and preparation fields inspected.'})+'\n')
