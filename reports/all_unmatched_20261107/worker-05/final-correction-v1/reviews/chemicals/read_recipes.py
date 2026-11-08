from pathlib import Path
import json,sys,yaml,hashlib
A=Path('.temp/w05-final-correction-v1/chemicals');L=Path(__file__).parent;C=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
def reduce(x):
 if isinstance(x,dict):return {k:reduce(v) for k,v in x.items() if k not in ('evidence','curation_history','curation_metadata','references','target_organisms','media_composition','description','source_data','biological_role','notes_role')}
 if isinstance(x,list):return [reduce(v) for v in x]
 return x
R=json.loads((A/'evidence-read-ledger-v1.json').read_text())['frozen_recipes']
for i in range(int(sys.argv[1]),int(sys.argv[2])):
 r=R[i];p=C/r['path']; b=p.read_bytes();assert hashlib.sha256(b).hexdigest()==r['sha256'];d=yaml.safe_load(b)
 print('RECIPE',i,p.name);print(json.dumps(reduce(d),separators=(',',':'),ensure_ascii=False))
 with (L/'read-events.jsonl').open('a') as f:f.write(json.dumps({'path':str(p),'sha256':r['sha256'],'scope':'Full file parsed; complete recipe, stock, concentration, process and notes fields read in semantic projection. Duplicate embedded evidence/history and organism growth claims excluded from scientific approval.'})+'\n')
