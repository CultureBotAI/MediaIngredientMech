import sys,json,re,hashlib,subprocess,datetime
from pathlib import Path
from html import unescape
R=Path('reports/all_unmatched_20261107/worker-08');I=R/'successors/issue-1227-v1/research/inorganic_forms';O=R/'successors/issue-1227-v1/independent-review/inorganic_forms'
D=json.loads((I/'decisions.json').read_text());P=json.loads((I/'proposals.json').read_text());E=json.loads((R/'successors/issue-1201-v1/evidence.json').read_text())['evidence']+json.loads((I/'evidence-additions.json').read_text());used=set(sum([d['evidence_ids'] for d in D],[])+sum([p['evidence_ids'] for p in P],[]));ES={e['evidence_id']:e for e in E if e['evidence_id'] in used}
unique={}
for e in ES.values():
 if e['kind'] in ['primary_source','ontology','unsuccessful_search']:
  unique.setdefault(e['capture']['path'],[]).append(e)
U=list(unique.items())
if sys.argv[1]=='index':
 for j,(p,es) in enumerate(U):print(j,p,[e['evidence_id'] for e in es])
 sys.exit()
def compact(a):
 if isinstance(a,dict) and 'components' in a and 'comments' in a:
  return {'meta':a.get('meta'),'components':[{k:([{ik:iv for ik,iv in it.items() if ik in ['component_name','volume','unit']} for it in v] if k=='items' else v) for k,v in b.items()} for b in a['components']],'comments':a['comments']}
 return a
for j in map(int,sys.argv[1:]):
 p,es=U[j];f=R/p;b=f.read_bytes();h=hashlib.sha256(b).hexdigest();assert all(e['capture']['sha256']==h for e in es)
 if b.startswith(b'%PDF'):t=subprocess.run(['pdftotext','-layout',str(f),'-'],capture_output=True,text=True,check=True).stdout;mode='Entire direct PDF extracted text'
 else:
  t=b.decode();mode='Entire captured response text'
  try:
   a=json.loads(t);t=a if isinstance(a,str) else json.dumps(compact(a),ensure_ascii=False,indent=1);mode='Actual JSON response; TOGO metadata labels/roles omitted, every literal component, quantity and complete comments retained' if isinstance(a,dict) and 'components' in a and 'comments' in a else mode
  except ValueError:pass
  t=re.sub(r'<script\b[^>]*>.*?</script>|<style\b[^>]*>.*?</style>','',t,flags=re.S|re.I);t=unescape(re.sub('<[^>]+>',' ',t));t=re.sub(r'[ \t]+',' ',t)
 print('\nSOURCE',j,p,[e['evidence_id'] for e in es]);print(t)
 with (O/'read-log.jsonl').open('a') as g:g.write(json.dumps(dict(at=datetime.datetime.now(datetime.timezone.utc).isoformat(),path=str(f),sha256=h,scope=mode,evidence_ids=[e['evidence_id'] for e in es]))+'\n')
