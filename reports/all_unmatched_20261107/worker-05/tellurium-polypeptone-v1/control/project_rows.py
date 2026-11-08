from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys,types,yaml
W=Path.cwd();B=W/'reports/all_unmatched_20261107/worker-05';P=B/'tellurium-polypeptone-v1';O=B/'postseal-source-corrections-v1';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
builder=W.parents[4]/'.temp/kgm-unmapped-20261107/claw/scripts/build_mim_ingredient_sssom.py'
# W.parents[4] is MediaIngredientMech; verify the exact pinned producer rather than infer availability.
assert builder.is_file(),builder
assert sha(builder)=='38d59f42953305f6fc51e4fc24dfc59ee1919bfb961595b67a8afe9f8a46a1bc'
sys.path[:0]=[str(builder.parent),str(builder.parent.parent/'src')];mod=types.ModuleType('w05_tellurium_polypeptone_native');mod.__file__=str(builder);sys.modules[mod.__name__]=mod;exec(compile(builder.read_bytes(),str(builder),'exec'),mod.__dict__)
old=json.loads((O/'core/proposals.json').read_text())['proposals'];new=json.loads((P/'validation/input-proposals.json').read_text())['proposals'];oi={p['proposal_id']:p for p in old};ni={p['proposal_id']:p for p in new}
baseline={str(p.relative_to(W)):yaml.safe_load(p.read_text()) for p in (W/'data/ingredients').rglob('*.yaml')}
def overlay(ps):
 out=dict(baseline)
 for p in ps:
  f=B/p['after_capture']['path'];assert sha(f)==p['after_capture']['sha256'];out.pop(p['owner_path'],None);out[p.get('destination_owner_path',p['owner_path'])]=yaml.safe_load(f.read_text())
 return out
def ix(records):return mod.build_owner_index({mod._mim_curie(Path(p).name):r for p,r in records.items()})
before=overlay(old);after=overlay(new);bi=ix(before);ai=ix(after)
def project(p,owners,cap=None):
 f=B/(cap or p['after_capture'])['path'];r=yaml.safe_load(f.read_text());s=[];rows=mod._row_from_yaml(W/p.get('destination_owner_path',p['owner_path']),{}, {}, {}, {},record=r,owners=owners,suppressions=s);return rows,[str(x) for x in s]
results=[]
for pid in ['CHEM-C1193-tellurium-dioxide','W05-FINAL-MAT-030','W05-FINAL-MAT-029']:
 br,bs=project(oi[pid],bi);ar,ass=project(ni[pid],ai);results.append(dict(proposal_id=pid,before_capture=oi[pid]['after_capture'],after_capture=ni[pid]['after_capture'],before_rows=br,after_rows=ar,before_suppressions=bs,after_suppressions=ass,payload_unchanged=oi[pid]['after_capture']['sha256']==ni[pid]['after_capture']['sha256']))
 if pid in ['CHEM-C1193-tellurium-dioxide','W05-FINAL-MAT-029']:assert br==ar,(pid,'unchanged source rows differ')
keys=lambda rs:[(r['predicate_id'],r['object_id']) for r in rs]
assert keys(results[0]['after_rows'])==[('skos:broadMatch','CHEBI:33305'),('skos:exactMatch','cas:7446-07-3'),('skos:exactMatch','kgmicrobe.compound:tellurium_dioxide')]
assert keys(results[1]['before_rows'])==[('skos:exactMatch','kgmicrobe.ingredient:polypeptone')]
assert keys(results[1]['after_rows'])==[('skos:exactMatch','kgmicrobe.ingredient:polypeptone')]
# The known missing parent is explicitly unresolved for the combined owner; no hypothetical option is substituted for the selected origin.
blocked=['Polypepton (Nihon Pharm. Co.)','Polypepton (Nihon Seiyaku)','Hipolypepton','Hipolypepton (Nihon seiyaku)','Hipolypepton*']
for row in results[1]['after_rows']:
 for label in blocked:assert label not in row['other'].split('|'),(label,row)
orig=B/'correction-1193-v1/chemicals/proposed/Tellurium_Dioxide.yaml';assert sha(orig)=='d25ae183c58c8616ecff3fd43dfb4615cb30d4df94e8a17399f09c2de3b20e98';hr,hs=project(ni['CHEM-C1193-tellurium-dioxide'],bi,dict(path=str(orig.relative_to(B))))
assert keys(hr)==[('skos:closeMatch','CHEBI:33305'),('skos:exactMatch','cas:7446-07-3')]
mod._check_producer_bindings();q=P/'validation/native-row-projections.json';assert not q.exists();q.write_text(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),compiler='/root',builder=dict(path=str(builder),sha256=sha(builder)),scope='Isolated full selected owner-index projection, empty optional external dictionaries; no downstream export/producer change.',before_overlay_records=len(before),after_overlay_records=len(after),reviewed_projections=results,historical_tellurium=dict(capture=dict(path=str(orig.relative_to(B)),sha256=sha(orig)),rows=hr,suppressions=hs,interpretation='Original43 grade was corrected before base76bca688. Current exactpayload/history are retained; no new grade repair invented.'),polypeptone_excluded_resolver_tokens=blocked,status='PASS'),indent=2)+'\n');print(json.dumps(dict(status='PASS',tellurium_rows=len(results[0]['after_rows']),polypeptone_rows=len(results[1]['after_rows']),hipolypepton_rows=len(results[2]['after_rows']))))
