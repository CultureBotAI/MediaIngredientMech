"""Read-only strict schema, actual before bytes, identity and full-corpus partonomy checks."""
from pathlib import Path
import json,hashlib,subprocess,sys,datetime,yaml,dataclasses,collections
R=Path.cwd();B=R/'reports/all_unmatched_20261107/worker-05';O=B/'correction-1193-v1';V=O/'validation';V.mkdir(exist_ok=True)
sys.path.insert(0,str(R/'src'))
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
BASE='e000d66dd26ab053e9b17ce7bf8d3c873c3dde99'
P=json.loads((O/'proposals.json').read_text())['proposals']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert len({p['owner_path'] for p in P})==len(P),'More than one final payload for one owner'
assert len({p.get('destination_owner_path',p['owner_path']) for p in P})==len(P),'Destination path collision'
records={p.as_posix():yaml.safe_load(p.read_text()) for folder in ['mapped','unmapped'] for p in Path('data/ingredients',folder).glob('*.yaml')}
def duplicates(rows):return {k:v for k,v in collections.Counter(r['identifier'] for r in rows.values() if r.get('mapping_status')!='REJECTED').items() if v>1}
before_duplicates=duplicates(records);before=validate_component_partonomy(records.values());payloads=[];negative_checks=[]
for p in P:
 after=B/p['after_capture']['path'];assert sha(after)==p['after_capture']['sha256'],p['proposal_id'];payloads.append(after)
 rec=yaml.safe_load(after.read_text());owner=Path(p['owner_path']);destination=p.get('destination_owner_path',p['owner_path'])
 if p['kind']=='edit_existing_owner':
  raw=subprocess.check_output(['git','show',BASE+':'+str(owner)]);assert raw==owner.read_bytes(),p['proposal_id'];assert sha(owner)==p['before_sha256'];old=records.pop(str(owner))
  assert len(rec.get('curation_history',[]))>len(old.get('curation_history',[])),('Missing new history',p['proposal_id'])
  # A rejected label must not become resolving or vanish while revising another claim.
  rejected={s['synonym_text'] for s in old.get('synonyms',[]) if s.get('synonym_type')=='REJECTED_LABEL'}
  retained={s['synonym_text'] for s in rec.get('synonyms',[]) if s.get('synonym_type')=='REJECTED_LABEL'}
  assert rejected<=retained,('Lost inherited negative labels',p['proposal_id'],rejected-retained)
  negative_checks.append({'proposal_id':p['proposal_id'],'before_rejected_labels':sorted(rejected),'retained':True})
  if destination!=str(owner):assert not Path(destination).exists(),('Promotion destination exists',destination)
 else:
  assert p['kind']=='new_owner' and p['before_sha256'] is None and not owner.exists(),p['proposal_id']
  assert rec.get('curation_history'),('New owner needs provenance',p['proposal_id'])
 assert destination not in records,('Duplicate destination',destination)
 records[destination]=rec
cmd=[sys.executable,'scripts/validate_strict.py',*map(str,payloads),'--workers','1','--out',str(V/'proposed-schema-errors.tsv')]
r=subprocess.run(cmd,capture_output=True,text=True);(V/'proposed-schema.log').write_text(r.stdout+r.stderr)
after=validate_component_partonomy(records.values());new=[v for v in after if v not in before];after_duplicates=duplicates(records);new_duplicates={k:v for k,v in after_duplicates.items() if v>before_duplicates.get(k,1)}
receipt={'validated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'proposal_count':len(P),'schema_command':cmd,'schema_exit_code':r.returncode,'schema_status':'PASS' if r.returncode==0 else 'FAIL','partonomy':{'baseline_violations':[dataclasses.asdict(v) for v in before],'proposed_violations':[dataclasses.asdict(v) for v in after],'new_violations':[dataclasses.asdict(v) for v in new],'status':'PASS' if not new else 'FAIL'},'active_identifier_collisions':{'baseline':before_duplicates,'proposed':after_duplicates,'introduced':new_duplicates},'inherited_negative_label_checks':negative_checks,'payloads':P,'limitations':'Exact candidate substitutions and new-owner additions in memory only. Maintained sources, mappings and selectors unchanged. Structural validation is not scientific approval.'}
(V/'proposed-validation.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n');print(json.dumps({k:v for k,v in receipt.items() if k not in ['payloads','schema_command','inherited_negative_label_checks']},indent=2));sys.exit(bool(r.returncode or new or new_duplicates))
