"""Bind completed independent scientific review notes to exact final input bytes.
Run only after all proposal and per-case notes have been manually reviewed.
"""
import datetime, hashlib, json
from pathlib import Path
import yaml

BASE = Path('reports/all_unmatched_20261107/worker-04')
SOURCE = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
def digest(data): return hashlib.sha256(data).hexdigest()
def canonical(value): return digest(json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode())
def read(path): return json.loads(path.read_text())
def check_capture(c):
    p = (BASE if c['root'] == 'artifact' else SOURCE) / c['path']
    assert p.is_file(), p
    assert digest(p.read_bytes()) == c['sha256'], p

assignment = read(BASE/'fragments/media-assignment.json')
inputs = {}
for name in ('media-decisions', 'media-evidence', 'media-proposals'):
    p = BASE/'fragments'/f'{name}.json'
    inputs[name] = {'path': str(p.relative_to(BASE)), 'sha256': digest(p.read_bytes())}
decisions = read(BASE/inputs['media-decisions']['path'])['decisions']
evidence = read(BASE/inputs['media-evidence']['path'])['evidence']
proposals = read(BASE/inputs['media-proposals']['path'])['proposals']
notes = read(BASE/'fragments/chemistry-media-review-notes.json')
proposal_notes = read(BASE/'fragments/chemistry-media-proposal-review-notes.json')
assert len(decisions) == len(assignment['cases']) == len(assignment['indices']) == 63
assert len(notes) == 63
emap = {e['evidence_id']: e for e in evidence}
pmap = {p['proposal_id']: p for p in proposals}
assert len(emap) == len(evidence)
assert len(pmap) == len(proposals)
assert set(proposal_notes) == set(pmap), (set(pmap)-set(proposal_notes), set(proposal_notes)-set(pmap))
for e in evidence: check_capture(e['capture'])
case_reviews = []
for index, case, decision in zip(assignment['indices'], assignment['cases'], decisions):
    assert case['case_id'] == decision['case_id']
    assert canonical(case) == decision['case_input_sha256'], index
    for key in ('source', 'source_case_id', 'source_label', 'raw_source_label'):
        assert decision['source'][key] == case[key], (index,key)
    assert decision['occurrence_ids'] == [o['occurrence_id'] for o in case.get('occurrences',[])], index
    assert notes[str(index)] and not notes[str(index)].startswith('OPEN'), index
    for eid in decision['evidence_ids']: assert eid in emap, (index,eid)
    for pid in decision['proposal_ids']: assert pid in pmap and case['case_id'] in pmap[pid]['case_ids']
    for occurrence in case.get('occurrences',[]):
        path = occurrence.get('full_recipe_snapshot')
        if path: assert digest((SOURCE/path).read_bytes()) == occurrence['source_file_sha256']
    case_reviews.append({'case_id': case['case_id'], 'assigned_index': index,
        'source_label': case['source_label'], 'case_input_sha256': decision['case_input_sha256'],
        'decision_sha256': canonical(decision), 'status': 'complete',
        'review_note': notes[str(index)],
        'reviewed_evidence': [{'evidence_id': eid, 'capture': emap[eid]['capture']} for eid in decision['evidence_ids']],
        'proposal_ids': decision['proposal_ids'],
        'publication_scope': 'Review of complete source-bound case disposition and proposed delta. Inherited owner assertions and withheld source/export identities are not approved by this review.'})
proposal_reviews = []
for p in proposals:
    check_capture(p['after_capture'])
    payload = yaml.safe_load((BASE/p['after_capture']['path']).read_text())
    assert isinstance(payload, dict) and payload.get('identifier')
    if p.get('before_sha256'): assert digest(Path(p['owner_path']).read_bytes()) == p['before_sha256']
    for eid in p['evidence_ids']: assert eid in emap
    proposal_reviews.append({'proposal_id': p['proposal_id'], 'owner_path': p['owner_path'],
        'after_capture': p['after_capture'], 'before_sha256': p.get('before_sha256'),
        'status': 'complete_for_delta', 'review_note': proposal_notes[p['proposal_id']]})
prior = read(BASE/'independent-review/media-reviewed-by-chemistry-v1.json')
findings = []
for finding in prior['findings']:
    finding = dict(finding)
    finding['status'] = 'resolved'
    finding['resolution'] = notes[str(finding['assigned_index'])]
    finding['prior_review'] = 'independent-review/media-reviewed-by-chemistry-v1.json'
    findings.append(finding)
findings.extend(read(BASE/'fragments/chemistry-media-review-supplemental-findings.json'))
# Detect a concurrent author change before recording an exact-hash review.
for item in inputs.values(): assert digest((BASE/item['path']).read_bytes()) == item['sha256']
review = {'schema_version': '1.0', 'reviewer': 'worker04/chemistry; independent authorship from media primary review',
    'reviewed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'status': 'complete',
    'scope': {'case_count': len(case_reviews), 'proposal_count': len(proposal_reviews),
              'evidence_capture_count': len(evidence), 'all_cases_reviewed': True, 'sampling': False},
    'inputs': inputs, 'case_reviews': case_reviews, 'proposal_reviews': proposal_reviews, 'findings': findings,
    'verification': {'all_capture_hashes': 'PASS', 'all_case_digests_and_source_fields': 'PASS',
                     'all_occurrences_and_full_recipe_hashes': 'PASS', 'all_before_and_after_payload_hashes': 'PASS',
                     'all_proposed_yaml_parsed': 'PASS', 'all_evidence_and_proposal_backlinks': 'PASS'},
    'limits': 'All63 case dispositions and every isolated proposal were skeptically reviewed against complete source context and applicable primary evidence. Acceptance applies to the documented deltas and precise unresolved-source requirements. It does not release inherited owner assertions, source identities or downstream mapping holds. Native schema, OAK and partonomy gates, complete-payload publication review, cross-shard reconciliation and integration remain coordinator responsibilities. No maintained data or SSSOM was edited.'}
out = BASE/'independent-review/media-reviewed-by-chemistry-v2.json'
assert not out.exists(), 'Preserve existing immutable review; increment version instead.'
out.write_text(json.dumps(review, indent=2, ensure_ascii=False)+'\n')
print(json.dumps({'path': str(out), 'sha256': digest(out.read_bytes()), 'scope': review['scope'], 'inputs': inputs}, indent=2))
