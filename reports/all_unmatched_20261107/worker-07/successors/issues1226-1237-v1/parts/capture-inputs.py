"""Read-only input binding; output only inside this new report successor."""
import datetime, hashlib, json, subprocess
from pathlib import Path

R=Path('reports/all_unmatched_20261107/worker-07')
S=R/'successors/issues1226-1237-v1'
C=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def put(p, data):
    assert not p.exists(), p
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_bytes(data)
def jput(p,obj):put(p,(json.dumps(obj,indent=2,ensure_ascii=False)+'\n').encode())
head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
assert head=='ddef7355bf7814bd3b1a23b9d61327bea3ac75fe'
paths=subprocess.check_output(['git','ls-files','-z'],text=True).split('\0')
tracked={p:sha(Path(p)) for p in paths if p and Path(p).is_file()}
jput(S/'validation/preexisting-tracked-byte-bindings.json',{'head':head,'files':tracked,'scope':'All tracked files before this successor; including all prior reports, source cores, native reviews and maintained surfaces.'})
ps=json.loads((R/'successors/issue1203-v1/proposals.json').read_text())['proposals']
selected=[]
for p in ps:
    f=R/p['after_capture']['path']; assert sha(f)==p['after_capture']['sha256']
    selected.append({'proposal_id':p['proposal_id'],'owner_path':p['owner_path'],'selected_capture':p['after_capture']})
assert len(selected)==100
audit=C/'workers/w02/worktree/.temp/campaign-evidence-provenance-audit-v1'
inputs=[(audit/'HANDOFF.md','c1e269ffc8a4762a2d64e4a0681226e15b802d46bee20ee4030fd088fd2d2d5f'),
 (audit/'provenance/entry-provenance-ledger-v1.json','98bfa525356aa223a08fcd2be11d9dc7476231aa6cd9efa4db1f85b2e66109e2'),
 (audit/'provenance/native-type-suggestions-v1.json','9ca6b04f03fdaabd65dacd90a160cf9f51dc549e607b5f5634616469532f1b33'),
 (C/'preflight/family-findings-triage-v1/findings-matrix-v2.json',None)]
bindings=[]
for p,want in inputs:
    got=sha(p); assert want is None or got==want
    bindings.append({'path':str(p),'sha256':got,'bytes':p.stat().st_size})
    if p.name in ['HANDOFF.md','findings-matrix-v2.json']:
        put(S/'captures'/('audit-'+p.name if p.name=='HANDOFF.md' else p.name),p.read_bytes())
core={n:sha(R/'successors/issue1203-v1'/n) for n in ['decisions.json','evidence.json','proposals.json','occurrence-dispositions.json']}
jput(S/'input-bindings.json',{'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'head':head,'scientific_predecessor':'fbfa032435ea1c399ae9b98bfedadb9ed639430d','frozen_base':'e000d66dd26ab053e9b17ce7bf8d3c873c3dde99','core':core,'selected':selected,'external_inputs':bindings,'contracts':{p:sha(Path(p)) for p in ['AGENTS.md','MAPPING_SEMANTICS.md','src/mediaingredientmech/schema/mediaingredientmech.yaml','.claude/skills/add-media/SKILL.md','.claude/skills/curate-yaml-record/SKILL.md','docs/record-reviews.md','docs/record-review-profile.md']}})
print(json.dumps({'selected':len(selected),'tracked_files':len(tracked),'external_hashes_verified':len(bindings),'core':core}))
