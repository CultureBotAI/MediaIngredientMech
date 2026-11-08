"""Read-only validation of exact proposed bytes; never writes maintained ingredients."""
from pathlib import Path
import json,hashlib,subprocess,sys,datetime,yaml,dataclasses
ROOT=Path.cwd(); OUT=ROOT/'reports/all_unmatched_20261107/worker-05'
sys.path.insert(0,str(ROOT/'src'))
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
proposals=[p for name in ['root','chemicals','materials','media'] for p in json.loads((OUT/name/'proposals.json').read_text())['proposals']]
paths=[OUT/p['after_capture']['path'] for p in proposals]
assert len(set(p['owner_path'] for p in proposals))==len(proposals)
for p,after in zip(proposals,paths):
 assert hashlib.sha256(after.read_bytes()).hexdigest()==p['after_capture']['sha256'],p['proposal_id']
 assert hashlib.sha256((ROOT/p['owner_path']).read_bytes()).hexdigest()==p['before_sha256'],p['proposal_id']
cmd=[sys.executable,'scripts/validate_strict.py',*map(str,paths),'--workers','1','--out',str(OUT/'validation/proposed-schema-errors.tsv')]
r=subprocess.run(cmd,capture_output=True,text=True)
(OUT/'validation/proposed-schema.log').write_text(r.stdout+r.stderr)
records={p.as_posix():yaml.safe_load(p.read_text()) for folder in ['mapped','unmapped'] for p in Path('data/ingredients',folder).glob('*.yaml')}
before=validate_component_partonomy(records.values())
for p,after in zip(proposals,paths):records[p['owner_path']]=yaml.safe_load(after.read_text())
after=validate_component_partonomy(records.values());new=[v for v in after if v not in before]
receipt={'validated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'proposal_count':len(proposals),'schema_command':cmd,'schema_exit_code':r.returncode,'schema_status':'PASS' if r.returncode==0 else 'FAIL','partonomy':{'baseline_violations':[dataclasses.asdict(v) for v in before],'proposed_violations':[dataclasses.asdict(v) for v in after],'new_violations':[dataclasses.asdict(v) for v in new],'status':'PASS' if not new else 'FAIL'},'payloads':proposals,'limitations':'Proposed bytes substituted only in memory. No native export, release admission or whole-owner scientific approval is claimed.'}
(OUT/'validation/proposed-validation.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k not in ['payloads','schema_command']},indent=2));sys.exit(bool(r.returncode or new))
