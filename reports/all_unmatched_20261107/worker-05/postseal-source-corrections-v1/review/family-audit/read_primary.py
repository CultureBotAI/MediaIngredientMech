import json,sys,hashlib,subprocess
from pathlib import Path
from html.parser import HTMLParser
B=Path('reports/all_unmatched_20261107/worker-05');P=B/'final-correction-v1';O=Path('.temp/w05-postseal-source-corrections-v1/review/family-audit');C=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
E={e['evidence_id']:e for e in json.loads((P/'core/evidence.json').read_text())['evidence']}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
class Text(HTMLParser):
 def __init__(self):super().__init__();self.parts=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ['script','style']:self.skip+=1
 def handle_endtag(self,t):
  if t in ['script','style'] and self.skip:self.skip-=1
 def handle_data(self,s):
  if not self.skip and s.strip():self.parts.append(s.strip())
rows=[]
for eid in sys.argv[1:]:
 e=E[eid];p=(B if e['capture']['root']=='artifact' else C)/e['capture']['path'];raw=p.read_bytes();assert sha(p)==e['capture']['sha256']
 if raw.startswith(b'%PDF'):
  out=subprocess.run(['pdftotext','-layout',str(p),'-'],check=True,capture_output=True).stdout.decode();method='pdftotext-layout'
 elif p.suffix=='.json' or raw[:1] in [b'{',b'[']:
  out=json.dumps(json.loads(raw),indent=2,ensure_ascii=False);method='complete-json'
 else:
  parser=Text();parser.feed(raw.decode(errors='replace'));out='\n'.join(parser.parts);method='complete-html-text'
 f=O/'read'/f'{eid}.txt';f.parent.mkdir(parents=True,exist_ok=True)
 if f.exists():assert f.read_text()==out
 else:f.write_text(out)
 row=dict(evidence_id=eid,path=str(p),sha256=sha(p),url=e.get('url'),original_accessed_at=e.get('accessed_at'),derived_text=str(f),derived_sha256=sha(f),method=method)
 rows.append(row);print('\nSOURCE',eid,e.get('url'));print(out)
with (O/'primary-read-index.jsonl').open('a') as h:
 for r in rows:h.write(json.dumps(r,ensure_ascii=False)+'\n')
