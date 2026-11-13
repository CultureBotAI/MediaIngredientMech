"""2026-11-12: correct the preserved MeSH extraction's URI-year mismatch.
Read only the exact selected MeSH subjects in the existing 2026 NTriples archive.
Save source/currentness/selection/script hashes and statements; no content edits.
"""
import datetime as dt, gzip, hashlib, json
from pathlib import Path
N=Path(__file__).resolve().parent
old=N/'other-ontology-capture-v1/RECEIPT.json'
r=json.loads(old.read_text()); s=next(x for x in r['source_records'] if x['source'].endswith('.nt.gz'))
D=N/'mesh-year-subject-capture-v2'; D.mkdir(exist_ok=False)
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(8*1024*1024),b''): h.update(b)
 return h.hexdigest()
def save(n,v):
 p=D/n
 with p.open('x') as f: json.dump(v,f,ensure_ascii=False,indent=2);f.write('\n')
 return dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size)
p=Path(s['source']); b=p.stat(); h=sha(p); assert h==s['source_sha256']
uris={('<http://id.nlm.nih.gov/mesh/2026/'+t.split(':')[1]+'>').encode():t for t in s['targets']}; facts={t:[] for t in s['targets']}
with gzip.open(p,'rb') as f:
 for line in f:
  target=uris.get(line.split(b' ',1)[0])
  if target: facts[target].append(line.decode().rstrip('\n'))
a=p.stat(); assert (b.st_size,b.st_mtime_ns,h)==(a.st_size,a.st_mtime_ns,sha(p))
out=save('facts.json',facts)
receipt=save('RECEIPT.json',dict(at=dt.datetime.now(dt.timezone.utc).isoformat(),source=str(p),source_sha256=h,bytes=b.st_size,mtime_ns=b.st_mtime_ns,unchanged_before_after=True,query='Single read-only gzip pass: exact subject URI http://id.nlm.nih.gov/mesh/2026/<selected-local-id>.',targets=s['targets'],empty_targets=[k for k,v in facts.items() if not v],facts=out,script=dict(path=str(Path(__file__)),sha256=sha(Path(__file__))),prior_failed_extraction=dict(path=str(old),sha256=sha(old),reason='Original exact-subject selector omitted archive /2026/ URI segment; empty extraction is not absent ontology terms.'),limits=['Target declarations do not independently establish source identity.','No maintained mutation or native scientific approval.']))
print(json.dumps(receipt));print('empty_targets', [k for k,v in facts.items() if not v])
