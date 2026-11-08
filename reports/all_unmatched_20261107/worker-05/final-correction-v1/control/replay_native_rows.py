"""Read-only native row projection for the three explicitly changed mapping claims."""
from pathlib import Path
import hashlib,json,sys,types,yaml
from datetime import datetime,timezone
W=Path.cwd();S=W/'.temp/w05-final-correction-v1';B=W/'reports/all_unmatched_20261107/worker-05'
builder=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/claw/scripts/build_mim_ingredient_sssom.py')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(builder)=='38d59f42953305f6fc51e4fc24dfc59ee1919bfb961595b67a8afe9f8a46a1bc'
sys.path[:0]=[str(builder.parent),str(builder.parent.parent/'src')]
module=types.ModuleType('w05_native_builder');module.__file__=str(builder);sys.modules[module.__name__]=module
exec(compile(builder.read_bytes(),str(builder),'exec'),module.__dict__)
P=json.loads((S/'assembly-draft-v7/proposals.json').read_text())['proposals']
base={str(p.relative_to(W)):yaml.safe_load(p.read_text()) for p in (W/'data/ingredients').rglob('*.yaml')}
overlay=dict(base)
for p in P:
 overlay.pop(p['owner_path'],None)
 overlay[p.get('destination_owner_path',p['owner_path'])]=yaml.safe_load((B/p['after_capture']['path']).read_text())
owners=module.build_owner_index({module._mim_curie(Path(path).name):r for path,r in overlay.items()})
before_owners=module.build_owner_index({module._mim_curie(Path(path).name):r for path,r in base.items()})
auth=json.loads((S/'chemicals/native-projections-v3.json').read_text());results=[]
for row in auth['projections']:
 p=next(p for p in P if p['proposal_id']==row['proposal_id'])
 path=W/p.get('destination_owner_path',p['owner_path']);after=yaml.safe_load((B/p['after_capture']['path']).read_text())
 before_path=W/row['before_path'];assert sha(before_path)==row['before_sha256']
 before=yaml.safe_load(before_path.read_text());supp=[]
 before_rows=module._row_from_yaml(path,{}, {}, {}, {},record=before,owners=before_owners,suppressions=[])
 after_rows=module._row_from_yaml(path,{}, {}, {}, {},record=after,owners=owners,suppressions=supp)
 signature=lambda rs:[(r['predicate_id'],r['object_id']) for r in rs]
 assert signature(after_rows)==signature(row['after_rows'])
 results.append(dict(proposal_id=p['proposal_id'],selected_after=p['after_capture'],before_path=str(before_path.relative_to(W)),
   before_sha256=sha(before_path),before_rows=before_rows,after_rows=after_rows,
   author_projection_relation_identity_signature_agrees=True,suppression_events=[str(s) for s in supp]))
module._check_producer_bindings()
out=S/'validation/native-row-replay-v1.json';assert not out.exists()
out.write_text(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),reviewer='/root',builder=str(builder),builder_sha256=sha(builder),
 scope='Complete isolated rows using final path-keyed overlay owner index. Optional external dictionaries explicitly empty. No downstream rebuild, generated export, producer/pin/schema/gate mutation or source approval.',
 overlay_owners=len(overlay),author_projection_sha256=sha(S/'chemicals/native-projections-v3.json'),results=results,status='PASS'),indent=2)+'\n')
print(json.dumps(dict(status='PASS',projections=len(results),row_counts=[len(r['after_rows']) for r in results])))
