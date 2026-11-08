from pathlib import Path
import sys,json,hashlib,subprocess,re
from html.parser import HTMLParser
import yaml
R=Path(__file__).parent
C=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
A=json.loads((C/'assignments/w01-nine-scope-candidates-independent-v1.json').read_text());I=C/'preflight/final-intake-candidate-v1';P=Path(A['packet'])
B={b['worker_slot']:b for b in json.loads((I/'active-bundles-frozen-v1.json').read_text())['bundles']}
class Text(HTMLParser):
 def __init__(self):super().__init__();self.out=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ['script','style']:self.skip+=1
  if t in ['br','p','tr','h1','h2','h3','hr','table']:self.out.append('\n')
  if t in ['td','th']:self.out.append(' | ')
 def handle_endtag(self,t):
  if t in ['script','style']:self.skip-=1
  if t in ['p','tr','h1','h2','h3','table']:self.out.append('\n')
 def handle_data(self,s):
  if not self.skip:self.out.append(s)
def extract(p):
 b=Path(p).read_bytes()
 if b.startswith(b'%PDF'):return subprocess.run(['pdftotext','-layout',str(p),'-'],capture_output=True,text=True,check=True).stdout
 s=b.decode('utf-8',errors='replace')
 if '<html' in s.lower() or '<!doctype' in s.lower():
  q=Text();q.feed(s);s=''.join(q.out);return '\n'.join(re.sub(r'\s+',' ',l).strip() for l in s.splitlines() if l.strip())
 try:
  j=json.loads(s)
  if isinstance(j,dict) and 'content' in j and isinstance(j['content'],list):return '\n'.join(z.get('text','') for z in j['content'] if isinstance(z,dict))
  return json.dumps(j,indent=2,ensure_ascii=False)
 except ValueError:return s
def rows(d):return d if isinstance(d,list) else d.get('decisions',d.get('cases',[]))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
if __name__=='__main__':
 if sys.argv[1]=='sources':
  ix=json.loads((R/'input-bindings-v1.json').read_text())['source_evidence']
  for eid in sys.argv[2:]:
   e=next(e for e in ix if e['evidence_id']==eid);print('\nSOURCE',eid,e.get('url'),e['sha256']);print(extract(e['path']))
 if sys.argv[1]=='resolve':
  out={'candidates':[]};origseen=set()
  for c in A['candidates']:
   row={'candidate_id':c['candidate_id'],'candidate':yaml.safe_load((P/c['candidate']['path']).read_text()),'before':yaml.safe_load((P/c['before_capture']).read_text()) if c.get('before_capture') else None,'originals':[],'case_ids':c['case_ids'],'occurrence_ids':c['occurrence_ids']}
   for o in c['origins']:
    dp=Path(B[o['worker']]['decisions']);dd=rows(json.loads(dp.read_text()));ds=[q for q in dd if q.get('case_id') in o['case_ids']]
    sp=C/f"queue/preliminary-v5/shards/shard-{o['worker']:02}.json";cases=rows(json.loads(sp.read_text()));cs=[q for q in cases if q['case_id'] in o['case_ids']]
    row['originals'].append({'origin':o,'payload':yaml.safe_load((I/o['payload_path']).read_text()),'decisions_path':str(dp),'decisions_sha256':sha(dp),'decisions':ds,'source_shard':str(sp),'source_shard_sha256':sha(sp),'cases':cs})
   out['candidates'].append(row)
  with (R/'resolved-complete-inputs-v1.json').open('x') as f:json.dump(out,f,indent=2,ensure_ascii=False);f.write('\n')
  print('Resolved candidates',len(out['candidates']))
 if sys.argv[1]=='origin_deltas':
  d=json.loads((R/'resolved-complete-inputs-v1.json').read_text());seen=set()
  for c in d['candidates']:
   if sys.argv[2:] and c['candidate_id'] not in sys.argv[2:]:continue
   for o in c['originals']:
    eid=o['origin']['entry_id']
    if eid in seen:continue
    seen.add(eid);print('\nORIGIN',eid)
    before=c['before'] or {}
    for k,v in o['payload'].items():
     if v!=before.get(k):
      if k=='curation_history':v=[event for event in v if event not in before.get(k,[])]
      print(k,json.dumps(v,indent=2,ensure_ascii=False))
    print('COMPLETE DECISIONS',json.dumps(o['decisions'],indent=2,ensure_ascii=False))
