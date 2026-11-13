"""2026-11-12: finite read-only capture of selected non-ChEBI local ontology facts.
Inputs: actual frozen candidate selection, existing OAK/BTO SQLite and MeSH NTriples.
Outputs: exact target facts, queries, source hashes/currentness and limitations.
No downloads, provider calls, KG rebuild, annotation-wide query, or maintained edit.
"""
from pathlib import Path
import collections,datetime as dt,gzip,hashlib,json,sqlite3
N=Path(__file__).resolve().parent;O=N.parent/'actual-candidate-science-primary-v1'
R=json.loads((O/'ROWS.json').read_text());D=N/'other-ontology-capture-v1';D.mkdir(exist_ok=False)
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
 return h.hexdigest()
def save(n,x):
 p=D/n
 with p.open('x') as f:json.dump(x,f,ensure_ascii=False,indent=2);f.write('\n')
 return {'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size}
targets=collections.defaultdict(set)
for r in R:
 if r.get('proposed_row'):
  t=r['proposed_row']['object_id'];targets[t.split(':')[0]].add(t)
sources={p:Path('/Users/marcin/.data/oaklib')/(p.lower()+'.db') for p in ['NCIT','FOODON','ENVO','UBERON']}
sources['BTO']=Path('/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/bto.db')
records=[];query='SELECT * FROM statements WHERE subject = ? ORDER BY predicate, object, value, datatype, language, graph'
for prefix,p in sources.items():
 before=p.stat();h=sha(p);wal=Path(str(p)+'-wal');assert not wal.exists(),str(wal)
 c=sqlite3.connect(p.as_uri()+'?mode=ro',uri=True);c.row_factory=sqlite3.Row
 facts={t:[dict(a) for a in c.execute(query,(t,))] for t in sorted(targets[prefix])}
 metadata=[dict(a) for a in c.execute("SELECT * FROM statements WHERE predicate IN ('owl:versionIRI','owl:versionInfo') ORDER BY subject,predicate,value,object")]
 c.close();after=p.stat();assert (before.st_size,before.st_mtime_ns,h)==(after.st_size,after.st_mtime_ns,sha(p));assert not wal.exists()
 rec={'source':str(p),'source_sha256':h,'bytes':before.st_size,'mtime_ns':before.st_mtime_ns,'query':query,'read_only':True,'unchanged_before_after':True,'targets':sorted(targets[prefix]),'metadata':metadata,'facts':save(prefix+'-facts.json',facts),'empty_targets':[t for t,v in facts.items() if not v]};records.append(rec)
 print(json.dumps({'prefix':prefix,'target_count':len(facts),'empty':rec['empty_targets']}),flush=True)
p=Path('/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/mesh2026.nt.gz')
before=p.stat();h=sha(p);uris={('<http://id.nlm.nih.gov/mesh/'+t.split(':')[1]+'>').encode():t for t in targets['mesh']};facts={t:[] for t in targets['mesh']}
with gzip.open(p,'rb') as f:
 for line in f:
  subject=line.split(b' ',1)[0]
  if subject in uris:facts[uris[subject]].append(line.decode().rstrip('\n'))
after=p.stat();assert (before.st_size,before.st_mtime_ns,h)==(after.st_size,after.st_mtime_ns,sha(p))
records.append({'source':str(p),'source_sha256':h,'bytes':before.st_size,'mtime_ns':before.st_mtime_ns,'query':'Single gzip stream; exact NTriples subject byte equality to http://id.nlm.nih.gov/mesh/<selected-local-id>. No name inference.','read_only':True,'unchanged_before_after':True,'targets':sorted(targets['mesh']),'facts':save('mesh-facts.json',facts),'empty_targets':[t for t,v in facts.items() if not v]})
result=save('RECEIPT.json',{'at':dt.datetime.now(dt.timezone.utc).isoformat(),'source_records':records,'selection':{'path':str(O/'ROWS.json'),'sha256':sha(O/'ROWS.json')},'script':{'path':str(Path(__file__)),'sha256':sha(Path(__file__))},'limits':['Captured ontology declarations do not independently establish source material scope or source-entity bindings.','Stored releases are recorded, not claimed latest upstream.','No science/native approval, downloads, maintained edits or KG rebuild.']})
print(json.dumps(result),flush=True)
