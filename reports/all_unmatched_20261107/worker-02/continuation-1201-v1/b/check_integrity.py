from pathlib import Path
import dataclasses,hashlib,json,yaml
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
R=Path('reports/all_unmatched_20261107/worker-02');B=R/'continuation-1201-v1/b'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
D=json.loads((B/'decisions.json').read_text())['decisions'];P=json.loads((B/'proposals.json').read_text())['proposals'];E={e['evidence_id']:e for p in [R/'evidence.json',B/'evidence.json'] for e in json.loads(p.read_text())['evidence']}
errors=[];receipts=[]
for d in D:
 for eid in d['evidence_ids']:
  if eid not in E:errors.append('Missing evidence '+eid);continue
  e=E[eid];c=e['capture']
  if c['root']!='artifact':continue
  p=R/c['path'];h=sha(p)
  if h!=c['sha256']:errors.append('Capture drift '+eid)
  receipts.append({'evidence_id':eid,'path':str(p),'sha256':h})
 for own in d['owner_records']:
  if sha(own['path'])!=own['sha256']:errors.append('Owner drift '+own['path'])
paths={p['owner_path']:p for p in P}
records=[yaml.safe_load(p.read_text()) for p in Path('data/ingredients').rglob('*.yaml') if str(p) not in paths]
ids=set()
for p in P:
 path=R/p['after_capture']['path'];h=sha(path)
 if h!=p['after_capture']['sha256']:errors.append('After drift '+p['proposal_id'])
 y=yaml.safe_load(path.read_text());records.append(y);ids.add(y['identifier'])
violations=[dataclasses.asdict(v) for v in validate_component_partonomy(records) if v.record_id in ids]
out={'status':'PASS' if not(errors or violations) else 'FAIL','decision_count':len(D),'proposal_count':len(P),'errors':errors,'proposal_partonomy_violations':violations,'input_hashes':{n:sha(B/n) for n in ['decisions.json','evidence.json','proposals.json','reassessments.json']},'checked_evidence':list({r['evidence_id']:r for r in receipts}.values()),'scope':'All linked capture hashes/current owner hashes and proposed B-overlay component partonomy. Guarded writes separately performed by author_continuation.py. No maintained surfaces changed.'}
(B/'integrity.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],errors,violations)
