#!/usr/bin/env python3
"""Read-only origin checks; writes only a new local reviewer receipt."""
import datetime
import hashlib
import json
import pathlib
import subprocess

W = pathlib.Path.cwd()
C = W.parents[2]
I = C / 'integration/final-same-target-reconciliation-v4'
O = W / '.temp/peptone-final-dependencies-v1/lineage-review'

def sha(b):
    return hashlib.sha256(b).hexdigest()

def canonical(d):
    return json.dumps(d, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode()

def write(name, d):
    p = O / name
    with p.open('x') as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
        f.write('\n')

lineage_bytes = (I / 'three-external-couplings-v1/lineage.json').read_bytes()
lineage = json.loads(lineage_bytes)
draft_bytes = (I / 'blocked-validation-v1/draft-selection.json').read_bytes()
draft = json.loads(draft_bytes)
cores = []
all_proposals = []
for row in lineage['core_inventory']:
    worker = row['worker']
    repo = C / f'workers/w{worker:02d}/worktree'
    path = row['proposal_core']['git_path']
    actual = subprocess.check_output(['git', '-C', str(repo), 'show', row['head'] + ':' + path])
    frozen = (I / row['proposal_core']['path']).read_bytes()
    assert actual == frozen
    assert sha(actual) == row['proposal_core']['sha256']
    proposals = json.loads(actual)['proposals']
    assert len(proposals) == row['count']
    cores.append({**row, 'git_bytes_equal_frozen_capture': True, 'local_head_observation': subprocess.check_output(['git', '-C', str(repo), 'rev-parse', 'HEAD'], text=True).strip()})
    all_proposals.extend({'worker': worker, 'head': row['head'], 'proposal': p} for p in proposals)
assert len(all_proposals) == 1019
owners = []
for owner in lineage['owners']:
    before = (W / owner['owner_path']).read_bytes()
    assert sha(before) == owner['before']['sha256']
    assert before == (I / owner['before']['path']).read_bytes()
    found = [p for p in all_proposals if p['proposal']['owner_path'] == owner['owner_path']]
    expected = owner['selected_current_origins']
    assert [(p['worker'],p['head'],p['proposal']) for p in found] == [(p['worker'],p['head'],p['proposal']) for p in expected]
    bindings = []
    for origin in expected:
        worker = origin['worker']
        repo = C / f'workers/w{worker:02d}/worktree'
        git_bytes = subprocess.check_output(['git', '-C', str(repo), 'show', origin['head'] + ':' + origin['git_path']])
        assert sha(git_bytes) == origin['payload']['sha256'] == origin['proposal']['after_capture']['sha256']
        assert git_bytes == (I / origin['payload']['path']).read_bytes()
        core = next(c for c in cores if c['worker'] == worker)
        dp = str(pathlib.PurePosixPath(core['proposal_core']['git_path']).parent / 'decisions.json')
        decisions_bytes = subprocess.check_output(['git', '-C', str(repo), 'show', origin['head'] + ':' + dp])
        decisions = json.loads(decisions_bytes)['decisions']
        shard_path = C / f'queue/preliminary-v5/shards/shard-{worker:02d}.json'
        shard_bytes = shard_path.read_bytes()
        shard = json.loads(shard_bytes)
        case_bindings = []
        for case_id in origin['proposal']['case_ids']:
            case = next(c for c in shard['cases'] if c['case_id'] == case_id)
            decision = next(c for c in decisions if c['case_id'] == case_id)
            assert sha(canonical(case)) == decision['case_input_sha256']
            assert origin['proposal']['proposal_id'] in decision['proposal_ids']
            case_bindings.append({'case_id':case_id, 'case_input_sha256':sha(canonical(case)), 'frozen_case':case, 'current_decision':decision, 'decision_object_sha256':sha(canonical(decision))})
        bindings.append({**origin, 'proposal_object_sha256':sha(canonical(origin['proposal'])), 'git_payload_verified':True, 'current_decisions_git_path':dp, 'current_decisions_sha256':sha(decisions_bytes), 'frozen_shard_path':str(shard_path), 'frozen_shard_sha256':sha(shard_bytes), 'cases':case_bindings})
    owners.append({'owner_path':owner['owner_path'], 'before_sha256':sha(before), 'before_current_and_frozen_equal':True, 'selected_origins':bindings})
parent_origin = next(p for p in all_proposals if p['worker'] == 5 and p['proposal']['proposal_id'] == 'W05-FINAL-MAT-039')
repo = C / 'workers/w05/worktree'
parent_git = 'reports/all_unmatched_20261107/worker-05/' + parent_origin['proposal']['after_capture']['path']
parent_bytes = subprocess.check_output(['git','-C',str(repo),'show',parent_origin['head']+':'+parent_git])
assert sha(parent_bytes) == 'c083794668a362203de6430eaa2609c34cd8ef78574a1230aa25b4a64fb55fd7'
shard_path = C / 'queue/preliminary-v5/shards/shard-05.json'
shard = json.loads(shard_path.read_bytes())
parent_case = next(c for c in shard['cases'] if c['case_id'] == parent_origin['proposal']['case_ids'][0])
parent_decisions_path = next(c for c in cores if c['worker']==5)['proposal_core']['git_path'].replace('proposals.json','decisions.json')
parent_decisions = json.loads(subprocess.check_output(['git','-C',str(repo),'show',parent_origin['head']+':'+parent_decisions_path]))
parent_decision = next(c for c in parent_decisions['decisions'] if c['case_id']==parent_case['case_id'])
assert parent_decision['case_input_sha256'] == sha(canonical(parent_case))
incoming=draft['parent_incoming_reference_closure']
assert len(incoming)==19
bound=[x for x in incoming if x['published_w05_proposal']]
assert len(bound)==16 and sum(x['in37'] for x in bound)==3
unbound=[x for x in incoming if not x['published_w05_proposal']]
assert {x['owner_path'] for x in unbound}=={x['owner_path'] for x in owners}
for x in bound:
    proposed=x['published_w05_proposal']
    actual=next(p['proposal'] for p in all_proposals if p['worker']==5 and p['proposal']['proposal_id']==proposed['proposal_id'])
    assert actual['owner_path']==proposed['owner_path'] and actual['before_sha256']==proposed['before_sha256']
    assert actual['after_capture']['sha256']==proposed['payload']['sha256']
    frozen=(I/proposed['payload']['path']).read_bytes()
    assert sha(frozen)==proposed['payload']['sha256']
write('verified-origin-inventory-v1.json', {'reviewer':'/root/peptone_final_lineage','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'read_only':True,'scope':'Exact frozen selected ten-core inventory, corresponding Git blobs, relevant source decisions/shards,19incoming rows. Private/history files outside these explicit inputs are not exhaustively searched and no absence claim applies there. Frozen copies include gitignored files by direct pathlib reads.','coordinator_input':{'lineage_sha256':sha(lineage_bytes),'draft_selection_sha256':sha(draft_bytes)},'core_inventory':cores,'total_selected_proposals':len(all_proposals),'owners':owners,'causal_parent':{**parent_origin,'git_payload_path':parent_git,'payload_sha256':sha(parent_bytes),'case':parent_case,'case_input_sha256':sha(canonical(parent_case)),'current_decision':parent_decision},'incoming_count':len(incoming),'bound_w05_count':len(bound),'bound_in37_count':sum(x['in37'] for x in bound),'remaining':unbound,'whole_owner_or_scientific_approval':False})
print('PASS1019selected,19incoming,16W05bound,3remaining; verified-origin-inventory-v1.json')
