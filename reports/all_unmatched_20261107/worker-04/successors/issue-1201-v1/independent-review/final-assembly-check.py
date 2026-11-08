"""Independent read-only successor assembly comparison; writes private receipt only."""
from pathlib import Path
import copy, datetime, hashlib, json, subprocess

S = Path(__file__).resolve().parents[1]
W = S.parents[1]
R = S.parents[4]
Q = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
dig = lambda x: hashlib.sha256(json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode()).hexdigest()
read = lambda p: json.loads(p.read_text())
old = read(W / 'decisions.json')['decisions']
ds = read(S / 'decisions.json')['decisions']
frozen = read(W / 'provenance/shard-04.json')['cases']
assert len(old) == len(ds) == len(frozen) == 188
prior = {d['case_id']: d for d in old}
byid = {d['case_id']: d for d in ds}
assert list(prior) == list(byid) == [c['case_id'] for c in frozen]
recipepaths = {}
occurrences = 0
for c in frozen:
    d = byid[c['case_id']]
    assert d['case_input_sha256'] == dig(c)
    assert d['source'] == {k: c[k] for k in ['source', 'source_case_id', 'source_label', 'raw_source_label']}
    assert d['occurrence_ids'] == [o['occurrence_id'] for o in c.get('occurrences', [])]
    occurrences += len(d['occurrence_ids'])
    for o in c.get('occurrences', []):
        path = Q / o['full_recipe_snapshot']
        assert sha(path) == o['source_file_sha256']
        recipepaths[str(path)] = o['source_file_sha256']
    for k in prior[d['case_id']]:
        if 'hold' in k:
            assert d[k] == prior[d['case_id']][k]
assembly = read(S / 'validation/assembly-bindings.json')
selected = read(S / 'independent-review/review-selection.json')
expected = copy.deepcopy(prior)
authorcases = set()
payloads = {}
newes = {}
reassess = []
reviews = []
for g in ['biological', 'chemistry', 'media']:
    sel = selected[g]
    rp = S / sel['path']
    assert sha(rp) == sel['sha256']
    r = read(rp)
    assert r['status'] == 'complete' and r['scientific_disposition'] == 'accepted_narrow_scope'
    parts = {}
    for k in ['reassessments', 'decisions', 'evidence', 'proposals']:
        path = S / f'fragments/{g}-{k}.json'
        assert sha(path) == r['reviewed_fragment_hashes'][str(path.relative_to(S))]
        parts[k] = read(path)[k]
    reviewed = {x['case_id'] for x in r['case_reviews']}
    assert {x['case_id'] for x in parts['reassessments'] + parts['decisions']} <= reviewed
    pr = {p['proposal_id']: p for p in r['payload_reviews']}
    assert len(pr) == len(r['payload_reviews'])
    assert set(pr) == {p['proposal_id'] for p in parts['proposals']}
    for p in parts['proposals']:
        rr = pr[p['proposal_id']]
        assert rr['full_payload_read'] is True
        assert rr['path'] == p['after_capture']['path']
        assert rr['sha256'] == p['after_capture']['sha256'] == sha(W / rr['path'])
    for d in parts['decisions']:
        cid = d['case_id']
        assert cid not in authorcases
        authorcases.add(cid)
        e = copy.deepcopy(d)
        e['independent_review'] = {'status': 'complete', 'evidence_ids': ['I1201-INDEPENDENT-' + g]}
        e['successor_assessment'] = {
            'issue': 'https://github.com/CultureBotAI/MediaIngredientMech/issues/1201',
            'predecessor_head': '0d2c73e5aee5adb88782537755472d9ca0c5c3cd',
            'predecessor_decision_sha256': dig(prior[cid]),
            'author_fragment_decision_sha256': dig(d),
            'scope': 'Source-specific assessment/proposal binding; all native holds and no-role/no-release scope retained.',
        }
        expected[cid] = e
    for a in parts['reassessments']:
        h = next(a[k] for k in ['old_decision_sha256', 'predecessor_decision_sha256', 'published_decision_sha256'] if k in a)
        assert h == dig(prior[a['case_id']])
    reassess += parts['reassessments']
    for p in parts['proposals']:
        assert p['proposal_id'] not in payloads
        payloads[p['proposal_id']] = p
    for e in parts['evidence']:
        assert e['evidence_id'] not in newes
        newes[e['evidence_id']] = e
    reviews.append({'group': g, 'path': str(rp.relative_to(W)), 'sha256': sha(rp), 'cases': len(reviewed), 'payloads': len(pr)})
assert [expected[d['case_id']] for d in old] == ds
assert set(assembly['changed_cases']) == authorcases
assert len(reassess) == 108 == len({x['case_id'] for x in reassess})
assert {x['case_id'] for x in reassess} == {x['case_id'] for x in old if not x['proposal_ids']}
assert read(S / 'reassessments.json')['reassessments'] == reassess
ps = read(S / 'proposals.json')['proposals']
origps = {p['proposal_id']: p for p in read(W / 'proposals.json')['proposals']}
activeps = copy.deepcopy(origps)
superseded = []
for p in payloads.values():
    for oid in p.get('supersedes_proposal_ids', []):
        o = activeps.pop(oid)
        assert set(o['case_ids']) <= set(p['case_ids'])
        assert o['owner_path'] == p['owner_path'] and o['before_sha256'] == p['before_sha256']
        superseded.append(oid)
    activeps[p['proposal_id']] = p
assert {p['proposal_id']: p for p in ps} == activeps
assert len(ps) == len(activeps) == len({p['owner_path'] for p in ps})
existingcount = 0
for p in ps:
    assert sha(W / p['after_capture']['path']) == p['after_capture']['sha256']
    if p['kind'] == 'edit_existing_owner':
        b = subprocess.check_output(['git', 'show', 'e000d66dd26ab053e9b17ce7bf8d3c873c3dde99:' + p['owner_path']], cwd=R)
        assert hashlib.sha256(b).hexdigest() == p['before_sha256']
        assert (R / p['owner_path']).read_bytes() == b
        existingcount += 1
    else:
        assert p['before_sha256'] is None
    for cid in p['case_ids']:
        assert p['proposal_id'] in byid[cid]['proposal_ids']
es = read(S / 'evidence.json')['evidence']
ebyid = {e['evidence_id']: e for e in es}
assert len(es) == len(ebyid)
for e in read(W / 'evidence.json')['evidence']:
    assert ebyid[e['evidence_id']] == e
for eid, e in newes.items():
    assert ebyid[eid] == e
captures = {}
for e in es:
    cap = e['capture']
    path = (W if cap['root'] == 'artifact' else Q) / cap['path']
    assert sha(path) == cap['sha256']
    captures[str(path)] = cap['sha256']
for d in ds:
    for eid in d['evidence_ids'] + d['independent_review']['evidence_ids']:
        assert eid in ebyid
    for pid in d['proposal_ids']:
        assert pid in activeps and d['case_id'] in activeps[pid]['case_ids']
summary = {
    'checked_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'status': 'PASS',
    'cases': len(ds), 'occurrences': occurrences, 'full_recipe_snapshot_paths': len(recipepaths),
    'changed_cases': len(authorcases), 'unchanged_predecessor_decisions': len(ds) - len(authorcases),
    'all_108_reassessed': True, 'only_permitted_assembly_decision_mutations': True,
    'new_fragment_evidence_records': len(newes), 'evidence_records': len(es),
    'unique_capture_paths_checked': len(captures), 'active_proposals': len(ps),
    'successor_proposals': len(payloads), 'superseded_predecessor_proposals': superseded,
    'existing_owner_original_before_bytes_checked': existingcount, 'selected_reviews': reviews,
    'fragment_hashes': {str(p.relative_to(S)): sha(p) for p in (S / 'fragments').glob('*.json')},
    'active_hashes': {x: sha(S / x) for x in ['decisions.json', 'evidence.json', 'proposals.json', 'reassessments.json', 'validation/assembly-bindings.json', 'independent-review/review-selection.json']},
}
out = R / '.temp/all-unmatched-worker-04/issue-1201-v1/process-controls/final-assembly-read-only-check.json'
out.write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps({k: v for k, v in summary.items() if k not in ['fragment_hashes', 'active_hashes', 'selected_reviews']}, indent=2))
