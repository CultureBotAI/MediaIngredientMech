"""Read-only exact source/currentness audit for the assigned nine candidates."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess

W = Path.cwd()
O = W / '.temp/nine-scope-candidates-independent-v1/root'
C = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
I = C / 'preflight/final-intake-candidate-v1'
A = C / 'assignments/w01-nine-scope-candidates-independent-v1.json'
a = json.loads(A.read_text())
P = Path(a['packet'])
s = json.loads(Path(a['final_candidate_summary']).read_text())


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args])


def save(name, data):
    with (O / name).open('x') as f:
        f.write(json.dumps(data, indent=2, ensure_ascii=False) + '\n')


origins = {}
for r in a['candidates']:
    for entry in r['origins']:
        if entry['entry_id'] in origins:
            assert origins[entry['entry_id']]['payload_sha256'] == entry['payload_sha256']
        origins[entry['entry_id']] = entry
origin_checks = []
for oid, e in sorted(origins.items()):
    frozen = I / e['payload_path']
    prefix = f"snapshot/workers/w{e['worker']:02d}/"
    assert e['payload_path'].startswith(prefix)
    rel = e['payload_path'][len(prefix):]
    repo = C / f"workers/w{e['worker']:02d}/worktree"
    local_head = git(repo, 'rev-parse', 'HEAD').decode().strip()
    at_selected = hashlib.sha256(git(repo, 'show', f"{e['head']}:{rel}")).hexdigest()
    at_current = hashlib.sha256(git(repo, 'show', f'HEAD:{rel}')).hexdigest()
    assert sha(frozen) == at_selected == e['payload_sha256']
    origin_checks.append({
        'entry_id': oid, 'selected_head': e['head'], 'local_observed_head': local_head,
        'repository': str(repo), 'repository_path': rel,
        'frozen_path': str(frozen), 'selected_sha256': at_selected,
        'current_git_blob_sha256': at_current,
        'current_worktree_sha256': sha(repo/rel),
        'selected_bytes_current': at_current == sha(repo/rel) == at_selected,
        'case_bindings': e['case_bindings'],
    })
before_checks = []
for r in a['candidates']:
    if not r['before_capture']:
        before_checks.append({'candidate_id': r['candidate_id'], 'before': None, 'operation': 'new', 'original_owner_lineage_is_not_new_owner_prior_state': True})
        continue
    frozen = I / 'snapshot/baseline' / r['owner_path']
    current = C / 'integration/worktree' / r['owner_path']
    values = {
        'candidate_before_capture': sha(P/r['before_capture']),
        'frozen_baseline': sha(frozen),
        'integration_worktree_current': sha(current),
        'baseline_git_blob': hashlib.sha256(git(C/'integration/worktree','show',f"e000d66dd26ab053e9b17ce7bf8d3c873c3dde99:{r['owner_path']}")).hexdigest(),
    }
    assert all(h == r['before_sha256'] for h in values.values())
    before_checks.append({'candidate_id': r['candidate_id'], 'owner_path': r['owner_path'], 'expected_sha256': r['before_sha256'], 'actuals': values})

input_checks = []
for path, expected in s['input_sha256'].items():
    q = Path(path)
    actual = sha(q)
    input_checks.append({'path': path, 'expected_sha256': expected, 'actual_sha256': actual, 'matches': actual == expected})
save('all-author-input-bindings-v1.json', {'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'bindings':input_checks,'scope':'Hash integrity of declared input paths, not a claim to have scientifically read every line.'})

comments = {}
for r in a['candidates']:
    for label, obj in r.get('issue_conclusions', {}).items():
        q = Path(obj['path'])
        assert sha(q) == obj['sha256']
        raw = json.loads(q.read_text())
        assert raw['body'] == obj['body']
        comments[obj['url']] = {**obj, 'assignment_embedded_body_matches_original_readback': True}
save('root-issue-conclusions-v1.json', {'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'comments':list(comments.values()),'scope':'Exact coordinator issue-comment capture content read, not fresh issue-state or approval claim.'})

refs = [f'refs/heads/review/all-unmatched-w{n:02d}-source-review-20261107' for n in range(1,11)]
argv = ['git','ls-remote','origin',*refs]
remote = subprocess.run(argv,cwd=W,capture_output=True,text=True)
assert remote.returncode == 0, remote.stderr
remote_heads = {line.split()[1]:line.split()[0] for line in remote.stdout.splitlines()}
head_checks = []
for n in range(1,11):
    repo=C/f'workers/w{n:02d}/worktree'
    local=git(repo,'rev-parse','HEAD').decode().strip()
    ref=refs[n-1]
    selected=s['selected_intake_heads'][str(n)]
    head_checks.append({'worker':n,'selected_head':selected,'current_local_head':local,'current_remote_head':remote_heads.get(ref),'selected_head_current':local==remote_heads.get(ref)==selected,'later_intake_accepted':False if local!=selected else 'not_a_later_head','assigned_origin_entries':[x['entry_id'] for x in origin_checks if x['entry_id'].startswith(f'w{n:02d}::')]})

save('source-currentness-and-beforeimages-v1.json', {
    'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'assignment':{'path':str(A),'sha256':sha(A)},
    'origin_checks':origin_checks,'authentic_before_checks':before_checks,
    'all_declared_author_input_binding_count':len(input_checks),
    'declared_input_hash_mismatches':[x for x in input_checks if not x['matches']],
    'heads':head_checks,'read_only_remote_command':argv,'remote_stdout':remote.stdout,
    'local_origin_bytes_match_selected':all(x['selected_bytes_current'] for x in origin_checks),
    'later_head_intake_acceptance':False,
    'scope':'Selected original bytes and authentic existing owner beforeimages verified. Later worker commits are observation only, not acceptance. No fetch, checkout, branch or GitHub mutation.',
    'program':{'path':str(O/'verify_sources_v1.py'),'sha256':sha(O/'verify_sources_v1.py')},
})
print(json.dumps({'origins':len(origin_checks),'candidates':len(before_checks),'input_bindings':len(input_checks),'input_mismatches':sum(not x['matches'] for x in input_checks),'selected_origin_bytes_current':all(x['selected_bytes_current'] for x in origin_checks),'heads':head_checks},indent=2))
