import json,sys,subprocess,hashlib,re
from pathlib import Path
B=Path('reports/all_unmatched_20261107/worker-05');O=Path('.temp/w05-final-correction-v1/review-media');es={x['evidence_id']:x for x in json.loads(Path('.temp/w05-final-correction-v1/media/evidence.json').read_text())['evidence']}
rows=[]
quiet='--quiet' in sys.argv
for eid in [a for a in sys.argv[1:] if a!='--quiet']:
 e=es[eid];f=B/e['capture']['path'];raw=f.read_bytes();method=''
 if raw.startswith(b'%PDF'):out=subprocess.run(['pdftotext','-layout',str(f),'-'],check=True,capture_output=True).stdout.decode();method='pdftotext-layout'
 elif f.suffix=='.json':
  j=json.loads(raw)
  if isinstance(j,dict) and isinstance(j.get('result'),str):out=j['result'];method='captured-tool-result'
  elif isinstance(j,list) and eid.startswith('MEDIA-ARCHIVE-'):
   mid=eid.replace('MEDIA-ARCHIVE-','');out=json.dumps([x for x in j if x.get('record',{}).get('meta',{}).get('gm','').endswith('/'+mid)],ensure_ascii=False,indent=2);method='full-matching-original-TOGO-record'
  else:out=json.dumps(j,ensure_ascii=False,indent=2);method='json'
 elif f.with_suffix('.txt').exists():out=f.with_suffix('.txt').read_text();method='captured-text-companion'
 else:
  from html.parser import HTMLParser
  class Extract(HTMLParser):
   def __init__(self):super().__init__();self.parts=[];self.skip=0
   def handle_starttag(self,tag,attrs):
    if tag in ('script','style'):self.skip+=1
   def handle_endtag(self,tag):
    if tag in ('script','style') and self.skip:self.skip-=1
   def handle_data(self,data):
    if not self.skip and data.strip():self.parts.append(data.strip())
  parser=Extract();parser.feed(raw.decode(errors='replace'));out='\n'.join(parser.parts);method='stdlib-html-text'
 td=O/'primary-text';td.mkdir(exist_ok=True);tf=td/(eid+'.txt')
 if not tf.exists():tf.write_text(out)
 else:assert tf.read_text()==out
 rows.append(dict(evidence_id=eid,source_path=str(f),sha256=hashlib.sha256(raw).hexdigest(),original_accessed_at=e.get('accessed_at'),url=e.get('url'),text_path=str(tf),text_sha256=hashlib.sha256(out.encode()).hexdigest(),method=method))
 if not quiet:print('\nSOURCE',eid,e.get('url'));print(out)
idx=O/'primary-text'/'read-index.jsonl'
with idx.open('a') as h:
 for r in rows:h.write(json.dumps(r)+'\n')
