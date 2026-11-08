from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys,types,yaml
W=Path.cwd();B=W/'reports/all_unmatched_20261107/worker-05';P=B/'postseal-source-corrections-v1';OLD=B/'final-correction-v1'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
builder=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/claw/scripts/build_mim_ingredient_sssom.py');assert sha(builder)=='38d59f42953305f6fc51e4fc24dfc59ee1919bfb961595b67a8afe9f8a46a1bc'
sys.path[:0]=[str(builder.parent),str(builder.parent.parent/'src')];module=types.ModuleType('w05_postseal_native_builder');module.__file__=str(builder);sys.modules[module.__name__]=module;exec(compile(builder.read_bytes(),str(builder),'exec'),module.__dict__)
old=json.loads((OLD/'core/proposals.json').read_text())['proposals'];new=json.loads((W/'.temp/w05-postseal-source-corrections-v1/validation/input-proposals.json').read_text())['proposals'];oldi={p['proposal_id']:p for p in old};newi={p['proposal_id']:p for p in new};changes=[dict(proposal_id=p['proposal_id']) for p in new if p['after_capture']!=oldi[p['proposal_id']]['after_capture']]
base={str(p.relative_to(W)):yaml.safe_load(p.read_text()) for p in (W/'data/ingredients').rglob('*.yaml')}
def overlay(ps):
 out=dict(base)
 for p in ps:
  path=B/p['after_capture']['path'];assert sha(path)==p['after_capture']['sha256'];out.pop(p['owner_path'],None);out[p.get('destination_owner_path',p['owner_path'])]=yaml.safe_load(path.read_text())
 return out
def index(records):return module.build_owner_index({module._mim_curie(Path(p).name):r for p,r in records.items()})
before=overlay(old);after=overlay(new);bi=index(before);ai=index(after)
def project(p,owners,capture=None):
 path=W/p.get('destination_owner_path',p['owner_path']);cap=capture or p['after_capture'];record=yaml.safe_load((B/cap['path']).read_text());s=[];rows=module._row_from_yaml(path,{}, {}, {}, {},record=record,owners=owners,suppressions=s);return rows,[str(x) for x in s]
results=[]
for c in changes:
 pid=c['proposal_id'];br,bs=project(oldi[pid],bi);ar,ass=project(newi[pid],ai);assert br==ar,(pid,'unexpected row delta requires review');results.append(dict(proposal_id=pid,before_capture=oldi[pid]['after_capture'],after_capture=newi[pid]['after_capture'],before_rows=br,after_rows=ar,whole_rows_unchanged=True,before_suppressions=bs,after_suppressions=ass))
p=newi['CHEM-C1193-Tris-HCl-salt'];rows,s=project(p,ai);assert [(r['predicate_id'],r['object_id']) for r in rows]==[('skos:broadMatch','CHEBI:9754'),('skos:exactMatch','cas:1185-53-1'),('skos:exactMatch','kgmicrobe.compound:tris_hydrochloride_salt')]
historical=B/'correction-1193-v1/chemicals/proposed/Tris_Hydrochloride_Salt.yaml';assert sha(historical)=='945bd8da0c00306c5e0d9ad2c3eaead1fb3af33e89cdc2e3440e729ec5763c58';hr,hs=project(p,bi,dict(path=str(historical.relative_to(B)),sha256=sha(historical)))
assert [(r['predicate_id'],r['object_id']) for r in hr]==[('skos:closeMatch','CHEBI:9754'),('skos:exactMatch','cas:1185-53-1')]
module._check_producer_bindings();q=P/'validation/native-row-projections.json';assert not q.exists();q.write_text(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),compiler='/root',builder=str(builder),builder_sha256=sha(builder),scope='Isolated in-memory native row inspection with full selected owner indexes and empty optional external dictionaries. No downstream build/export or producer/gate change.',before_overlay_records=len(before),after_overlay_records=len(after),changed_payload_projections=results,tris=dict(proposal_id=p['proposal_id'],current_capture=p['after_capture'],historical_capture=dict(path=str(historical.relative_to(B)),sha256=sha(historical)),historical_source_head='43f7cf6e8681fa617b5d6d3529d94d537ca01f0d',current_already_correct_at='5156d92bec6bd885ca8bae3c5e18bfdce0069176',historical_two_rows=hr,current_three_rows=rows,new_payload_change=False,interpretation='The parent-grade correction and mandatory B1 registry row already exist in the sealed prior successor; current exact bytes are retained.'),status='PASS'),indent=2)+'\n');print(json.dumps(dict(status='PASS',changed_payloads=len(results),current_tris_rows=len(rows))))
