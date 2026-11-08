from pathlib import Path
import json,hashlib,sys,yaml,re
W=Path.cwd(); A=W/'.temp/w05-final-correction-v1/chemicals'; L=Path(__file__).parent
C=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def clean(x):
    if isinstance(x,dict):return {k:clean(v) for k,v in x.items() if k not in ['properties','roles','gmo','gmo_id']}
    if isinstance(x,list):return [clean(v) for v in x]
    return x
def view_text(p):
    s=p.read_text()
    try:return json.dumps(clean(json.loads(s)),ensure_ascii=False,separators=(',',':'))
    except ValueError:return s
def log(p,scope):
    with (L/'read-events.jsonl').open('a') as f:f.write(json.dumps({'path':str(p.resolve()),'sha256':sha(p),'scope':scope})+'\n')
if sys.argv[1]=='texts':
    for n in sys.argv[2:]:
        p=A/'read-text'/f'{n}.txt';print('SOURCE',n);print(view_text(p));log(p,'Complete extracted recipe, preparation or identity fields; TOGO enrichment properties/roles excluded from scientific scope.')
if sys.argv[1]=='cases':
    D=json.loads((A/'decisions-v2.json').read_text());S=json.loads((C/'shards/shard-05.json').read_text())['cases'];by={c['case_id']:c for c in S}
    for i in range(int(sys.argv[2]),int(sys.argv[3])):
        d=D[i];c=by[d['case_id']]; print('CASE',i,d.get('case_index'),d['case_id']);print(json.dumps(c,ensure_ascii=False,separators=(',',':')))
if sys.argv[1]=='recipes':
    R=json.loads((A/'evidence-read-ledger-v1.json').read_text())['frozen_recipes']
    for i in range(int(sys.argv[2]),int(sys.argv[3])):
        r=R[i];p=C/r['path'];d=yaml.safe_load(p.read_text());assert sha(p)==r['sha256'];print('RECIPE',i,r['path'],r['case_indices']);print(json.dumps(d,ensure_ascii=False,separators=(',',':')));log(p,'Full frozen recipe loaded and printed for review; biological and role assertions are not approved.')
