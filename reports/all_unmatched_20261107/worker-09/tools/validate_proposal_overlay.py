"""Read-only worker09 proposal guards; never writes maintained data."""
import collections, dataclasses, datetime, hashlib, itertools, json, sys
from pathlib import Path
import yaml
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'MAPPING_SEMANTICS.md').is_file())
sys.path.insert(0,str(ROOT/'src'))
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
OUT=ROOT/'reports/all_unmatched_20261107/worker-09'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
proposals=[]
for group in ('antibiotics','salts','materials'):
 proposals.extend(json.loads((OUT/group/'proposals.json').read_text())['proposals'])
baseline={str(p.relative_to(ROOT)):yaml.safe_load(p.read_text()) for d in ('mapped','unmapped') for p in (ROOT/'data/ingredients'/d).glob('*.yaml')}
overlay=dict(baseline); failures=[]; checks=[]
counts=collections.Counter(p['owner_path'] for p in proposals)
for path,count in counts.items():
 if count!=1:failures.append({'owner':path,'problem':'multiple proposal payloads'})
for p in proposals:
 path=p['owner_path']; after=OUT/p['after_capture']['path']; data=yaml.safe_load(after.read_text()); before=baseline.get(path)
 if sha(after)!=p['after_capture']['sha256']:failures.append({'proposal':p['proposal_id'],'problem':'after hash mismatch'})
 if p['kind']=='edit_existing_owner':
  if before is None or sha(ROOT/path)!=p['before_sha256']:failures.append({'proposal':p['proposal_id'],'problem':'before hash mismatch'})
  old_history=(before or {}).get('curation_history',[]); new_history=data.get('curation_history',[])
  if new_history[:len(old_history)]!=old_history or len(new_history)<=len(old_history):failures.append({'proposal':p['proposal_id'],'problem':'history not append-only with new event'})
 else:
  if before is not None:failures.append({'proposal':p['proposal_id'],'problem':'new owner path exists'})
  clashes=[name for name,record in baseline.items() if record.get('mapping_status')!='REJECTED' and record.get('identifier')==data.get('identifier')]
  if clashes:failures.append({'proposal':p['proposal_id'],'problem':'new identifier already owned','paths':clashes})
 if not data.get('curation_history') or not data['curation_history'][-1].get('llm_assisted'):failures.append({'proposal':p['proposal_id'],'problem':'missing LLM-assisted history'})
 overlay[path]=data
 checks.append({'proposal_id':p['proposal_id'],'owner_path':path,'after_sha256':sha(after),'identifier':data['identifier'],'before_identifier':(before or {}).get('identifier')})
def collision_pairs(records):
 byid=collections.defaultdict(list)
 for path,record in records.items():
  if record.get('mapping_status')!='REJECTED':byid[record.get('identifier')].append(path)
 return {(identifier,a,b) for identifier,paths in byid.items() for a,b in itertools.combinations(sorted(paths),2)}
introduced_collisions=collision_pairs(overlay)-collision_pairs(baseline)
for identifier,a,b in sorted(introduced_collisions):failures.append({'problem':'introduced active identifier collision','identifier':identifier,'paths':[a,b]})
old=set(validate_component_partonomy(baseline.values()));new=set(validate_component_partonomy(overlay.values())); introduced=new-old
for x in introduced:failures.append({'problem':'introduced partonomy violation',**dataclasses.asdict(x)})
protected=json.loads((OUT/'common/protected-input-hashes.json').read_text())['files']
changed=[p for p,h in protected.items() if not (ROOT/p).is_file() or sha(ROOT/p)!=h]
if changed:failures.append({'problem':'protected baseline files changed','paths':changed})
result={'status':'PASS' if not failures else 'FAIL','checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'proposal_count':len(proposals),'baseline_record_count':len(baseline),'protected_file_count':len(protected),'protected_files_changed':changed,'baseline_partonomy_violation_count':len(old),'overlay_partonomy_violation_count':len(new),'introduced_partonomy_violations':[dataclasses.asdict(x) for x in sorted(introduced,key=str)],'checks':checks,'failures':failures,'scientific_adequacy_or_approval_established':False}
dest=Path(sys.argv[1]);dest.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ('status','proposal_count','protected_file_count','baseline_partonomy_violation_count','overlay_partonomy_violation_count','failures')}));sys.exit(bool(failures))
