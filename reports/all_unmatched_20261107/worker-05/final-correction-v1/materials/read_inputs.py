"""Read frozen inputs and create review aids, never maintain ingredient data."""
import json, pathlib, hashlib, subprocess, datetime, re
from html.parser import HTMLParser
import yaml
L = pathlib.Path(__file__).resolve().parent
W = pathlib.Path.cwd()
C = pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
O = W/'reports/all_unmatched_20261107/worker-05'
A = json.loads((C/'workers/w08/worktree/.temp/w05-published-head-independent-review-v1/assignments/materials.json').read_text())
E = json.loads((O/'correction-1193-v1/materials/evidence.json').read_text())['evidence']
P = json.loads((O/'correction-1193-v1/materials/proposals.json').read_text())['proposals']
records=[]
def sha(b): return hashlib.sha256(b).hexdigest()
def capture(c): return (O if c['root']=='artifact' else pathlib.Path(A['source_root']))/c['path']
class Visible(HTMLParser):
 def __init__(self): super().__init__(); self.parts=[]; self.skip=0
 def handle_starttag(self,t,a):
  if t in ('script','style'): self.skip+=1
 def handle_endtag(self,t):
  if t in ('script','style'): self.skip=max(0,self.skip-1)
 def handle_data(self,s):
  if not self.skip and s.strip(): self.parts.append(s.strip())
def visible(b,path):
 if b.startswith(b'%PDF'):
  return subprocess.run(['/opt/homebrew/bin/pdftotext','-layout',str(path),'-'],check=True,capture_output=True).stdout.decode()
 text=b.decode('utf-8',errors='replace')
 if '<html' in text.lower() or '<!doctype' in text.lower():
  h=Visible();h.feed(text);return '\n'.join(h.parts)
 try:
  j=json.loads(text)
  # Do not omit scientific fields; remove whitespace only.
  return json.dumps(j,ensure_ascii=False,separators=(',',':'))
 except Exception:return text
def remember(path,kind,ids=None):
 b=path.read_bytes();records.append({'path':str(path),'sha256':sha(b),'bytes':len(b),'read_method':kind,'ids':ids or []});return b
out=L/'read-aids';out.mkdir(exist_ok=True)
unique={}
for e in E:
 p=capture(e['capture'])
 if not p.exists(): raise FileNotFoundError(p)
 b=remember(p,'capture integrity and complete byte read',[e['evidence_id']])
 assert sha(b)==e['capture']['sha256'],p
 if e['kind'] in ('primary_source','ontology'):
  unique.setdefault(str(p),{'path':p,'evidence':[]})['evidence'].append(e['evidence_id'])
for i,v in enumerate(unique.values()):
 p=v['path'];b=p.read_bytes();t=visible(b,p)
 (out/f'primary-{i:03d}.txt').write_text(t)
 v.update(index=i,sha256=sha(b),text_sha256=sha(t.encode()),text_path=str(out/f'primary-{i:03d}.txt'),characters=len(t));v['path']=str(p)
(L/'primary-index.json').write_text(json.dumps(list(unique.values()),indent=2)+'\n')
contexts=[]
for c in A['cases']:
 d=next(x for x in A['decisions'] if x['case_id']==c['case_id'])
 for occ in c.get('occurrences',[]):
  p=pathlib.Path(A['source_root'])/occ['full_recipe_snapshot'];b=remember(p,'full recipe parse; contextual fields inspected via review aid',[occ['occurrence_id']]);assert sha(b)==occ['source_file_sha256']
  y=yaml.safe_load(b)
  contexts.append({'case_id':c['case_id'],'case_index':d['case_index'],'occurrence':occ,'full_recipe':y,'sha256':sha(b)})
(out/'all-case-contexts.json').write_text(json.dumps(contexts,indent=2,ensure_ascii=False)+'\n')
# Original owners are read in full; differing fields are displayed for scientific comparison.
diffs=[]
for p in P:
 aft=O/p['after_capture']['path'];ab=remember(aft,'complete published payload read',[p['proposal_id']]);assert sha(ab)==p['after_capture']['sha256']
 rec=yaml.safe_load(ab);before=None
 if p['before_sha256']:
  bp=W/p['owner_path'];bb=remember(bp,'complete original owner parse and changed-field comparison',[p['proposal_id']]);assert sha(bb)==p['before_sha256'],p['owner_path'];before=yaml.safe_load(bb)
 changes={k:{'before':(before or {}).get(k),'published':rec.get(k)} for k in set(rec)|set(before or {}) if (before or {}).get(k)!=rec.get(k)}
 diffs.append({'proposal_id':p['proposal_id'],'owner_path':p['owner_path'],'changes':changes})
(out/'original-to-published.json').write_text(json.dumps(diffs,indent=2,ensure_ascii=False)+'\n')
(L/'input-byte-read-ledger.json').write_text(json.dumps({'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'author':'/root/materials_research','limitation':'This records actual byte reads, extraction and parsing. It is not by itself an assertion that every byte was manually scientifically assessed. Primary conclusion ledger records assessed scope.','reads':records},indent=2)+'\n')
print(json.dumps({'evidence_records_verified':len(E),'unique_primary_ontology_captures':len(unique),'case_count':len(A['cases']),'context_occurrences':len(contexts),'proposal_count':len(P),'errors':0}))
