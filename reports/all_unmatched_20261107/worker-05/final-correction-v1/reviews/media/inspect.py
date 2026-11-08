import json,hashlib,yaml,sys,re
from pathlib import Path
from datetime import datetime,timezone
B=Path('reports/all_unmatched_20261107/worker-05'); P=Path('.temp/w05-final-correction-v1/media'); O=Path('.temp/w05-final-correction-v1/review-media'); C=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
def sha(x):return hashlib.sha256(x).hexdigest()
def load(p):return json.loads(p.read_text())
ps=load(P/'proposals.json')['proposals'];ds=load(P/'decisions.json')['decisions']; es=load(P/'evidence.json')['evidence']; ed={e['evidence_id']:e for e in es}
def cap(c):return B/c['path'] if c['root']=='artifact' else C/'queue/preliminary-v5'/c['path']
def diff(a,b,path=''):
 if type(a)!=type(b):return [path]
 if isinstance(a,dict):return sum([diff(a.get(k),b.get(k),path+'/'+k) for k in sorted(a.keys()|b.keys())],[])
 if isinstance(a,list):
  if a==b:return []
  return sum([diff(a[i] if i<len(a) else None,b[i] if i<len(b) else None,path+'/'+str(i)) for i in range(max(len(a),len(b)))],[])
 return [] if a==b else [path]
if sys.argv[1]=='verify':
 log=[];pr=[]
 for e in es:
  c=e['capture'];f=cap(c);raw=f.read_bytes();assert sha(raw)==c['sha256'],(e['evidence_id'],str(f));log.append(dict(evidence_id=e['evidence_id'],path=str(f),sha256=sha(raw),bytes=len(raw),kind=e['kind']))
 for p in ps:
  af=cap(p['after_capture']);bf=cap(p['predecessor_proposal']['after_capture']);a=yaml.safe_load(af.read_bytes());b=yaml.safe_load(bf.read_bytes());assert sha(af.read_bytes())==p['after_capture']['sha256'];assert sha(bf.read_bytes())==p['predecessor_proposal']['after_capture']['sha256']; before=Path(p['owner_path']); bh=sha(before.read_bytes()) if before.exists() else None;assert bh==p.get('before_sha256'),(p['proposal_id'],bh,p.get('before_sha256'))
  assert a.get('curation_history',[])[:len(b.get('curation_history',[]))]==b.get('curation_history',[]),p['proposal_id']
  pr.append(dict(proposal_id=p['proposal_id'],after_path=str(af),after_sha256=sha(af.read_bytes()),predecessor_path=str(bf),predecessor_sha256=sha(bf.read_bytes()),owner_path=str(before),before_sha256=bh,case_ids=p['case_ids'],changed_paths=diff(b,a),full_after_fields=list(a),all_predecessor_history_events_preserved=True))
 source=load(P/'complete-source-bindings.json'); sh=load(C/'queue/preliminary-v5/shards/shard-05.json');cases=sh['cases'] if isinstance(sh,dict) else sh;sd={x['case_id']:x for x in cases}; dsd={d['case_id']:d for d in ds}
 for x in source['cases']:
  assert x['raw_case']==sd[x['case_id']],x['case_id'];d=dsd[x['case_id']];assert d['case_input_sha256']==x['case_input_sha256'];assert d['occurrence_ids']==[v['occurrence_id'] for v in x['raw_case'].get('occurrences',[])]
 for f in source['full_recipe_files']:assert sha(Path(f['path']).read_bytes())==f['sha256']
 res=dict(reviewer='/root/final_skeptical',created_at=datetime.now(timezone.utc).isoformat(),evidence=log,payloads=pr,source_cases=len(source['cases']),full_recipes=len(source['full_recipe_files']),source_byte_bindings_pass=True,semantic_approval=False)
 (O/'independent-byte-and-delta-audit-v1.json').write_text(json.dumps(res,indent=2)+'\n');print('verified',len(log),'evidence refs',len(pr),'payloads',len(source['cases']),'cases',len(source['full_recipe_files']),'recipes');print(json.dumps([(x['proposal_id'],x['changed_paths']) for x in pr],indent=2))
if sys.argv[1]=='payload':
 for i in map(int,sys.argv[2:]):
  p=ps[i];a=yaml.safe_load(cap(p['after_capture']).read_bytes());print('PAYLOAD',i,json.dumps(a,ensure_ascii=False))
if sys.argv[1]=='cases':
 lo,hi=map(int,sys.argv[2:]);source=load(P/'complete-source-bindings.json');sd={x['case_id']:x for x in source['cases']}
 for d in ds[lo:hi]:
  raw=sd[d['case_id']]['raw_case']; print('CASE',d['case_index'],d['source']); print('ASSESSMENT',d['final_correction_reassessment']['assessment']);print('MISSING',d.get('missing_requirement'));print('RAW',json.dumps(raw,ensure_ascii=False)); print('PRIMARY',[(i,ed[i].get('capture',{}).get('path'),ed[i].get('url')) for i in d['evidence_ids'] if ed[i].get('kind')=='primary_source'])
if sys.argv[1]=='text':
 for i in sys.argv[2:]:
  e=ed[i]; f=cap(e['capture']);t=f.with_suffix('.txt');print('\nSOURCE',i,str(f),e.get('url'));print(t.read_text() if t.exists() else f.read_text(errors='replace'))
