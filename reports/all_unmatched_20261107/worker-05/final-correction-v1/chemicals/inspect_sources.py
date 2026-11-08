"""Private read/extraction ledger; never writes source or maintained paths."""
from pathlib import Path
import json, hashlib, subprocess, re
from html.parser import HTMLParser
class Text(HTMLParser):
 def __init__(self): super().__init__(); self.parts=[];self.skip=0
 def handle_starttag(self,tag,attrs):
  if tag in ('script','style'): self.skip+=1
 def handle_endtag(self,tag):
  if tag in ('script','style'): self.skip=max(0,self.skip-1)
 def handle_data(self,data):
  if not self.skip and data.strip(): self.parts.append(data.strip())

O=Path(__file__).resolve().parent
R=Path('reports/all_unmatched_20261107/worker-05').resolve()
C=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
Q=C/'queue/preliminary-v5'
E=json.loads((O/'input-evidence.json').read_text())
def sha(b): return hashlib.sha256(b).hexdigest()
out=[]
for e in E:
 c=e['capture']; p=(R if c['root']=='artifact' else Q)/c['path']
 b=p.read_bytes(); assert sha(b)==c['sha256'],p
 row={'evidence_id':e['evidence_id'],'kind':e['kind'],'capture':c,'resolved_path':str(p),'accessed_at':e.get('accessed_at'),'url':e.get('url'),'bytes':len(b),'integrity':'verified','scientific_read_status':'pending'}
 if e['kind'] in ['primary_source','ontology']:
  if b.startswith(b'%PDF'): t=subprocess.run(['pdftotext','-layout',str(p),'-'],capture_output=True,text=True,check=True).stdout
  else:
   t=b.decode('utf-8',errors='replace')
   if '<html' in t.lower() or '<!doctype html' in t.lower():
    s=Text();s.feed(t);t=' '.join(s.parts)
  d=O/'read-text'/f"{e['evidence_id']}.txt";d.parent.mkdir(exist_ok=True)
  d.write_text(t); row['derived_read_text']=str(d.relative_to(O));row['text_sha256']=sha(d.read_bytes())
 out.append(row)
(O/'capture-integrity-and-read-index.json').write_text(json.dumps(out,indent=2)+'\n')
print('Verified',len(out),'captures; extracted',sum('derived_read_text' in r for r in out))
