from pathlib import Path
import datetime
import hashlib
import json

L = Path(__file__).resolve().parent
W = Path.cwd()
R = W / 'reports/all_unmatched_20261107/worker-05'
C = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def save(name, x):
    p = L / name
    assert not p.exists(), p
    p.write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')

read_items = []
for name in ['inputs/maintained-before.yaml', 'inputs/predecessor.yaml', 'inputs/decisions.json', 'inputs/proposal.json', 'inputs/raw-cases.json', 'inputs/bsa-comment.json']:
    read_items.append({'path': str((L / name).relative_to(W)), 'sha256': sha(L / name), 'scope': 'Complete contents read for the bounded BSA correction.'})
evidence = json.loads((L / 'inputs/evidence-reused.json').read_text())
ids = {'MATERIALS-CAP-a08fb341926e1d0a', 'MATERIALS-CAP-ee722a18f3e26939', 'MATERIALS-CAP-b5dd8b92f4e4ea2c', 'MATERIALS-CAP-776733f8ca9ff0a9', 'MATERIALS-CAP-4b8a987a15a1852d', 'MATERIALS-ARCHIVE-M2400', 'MATERIALS-ARCHIVE-M2401'}
for e in evidence:
    if e['evidence_id'] in ids:
        p = R / e['capture']['path']
        read_items.append({'path': str(p.relative_to(W)), 'sha256': sha(p), 'evidence_id': e['evidence_id'], 'scope': 'Source metadata, complete ingredient tables and all preparation comments for this exact source record; derived GMO annotations are not newly endorsed.', 'original_accessed_at': e.get('accessed_at'), 'timestamp_precision': e.get('timestamp_precision', 'Recorded request time, not this local reread.')})
for name, scope in [
    ('materials/capture-log.json', 'Entry 50 only, JCM201 original request and response path.'),
    ('materials/captures/primary-d6e2d2b11024d04b.txt', 'Complete HTML body; Nothing found is unsuccessful recipe retrieval, not positive evidence.'),
]:
    p = R / name
    read_items.append({'path': str(p.relative_to(W)), 'sha256': sha(p), 'scope': scope})
raw = json.loads((L / 'inputs/raw-cases.json').read_text())
for case in raw:
    for o in case['occurrences']:
        p = C / o['full_recipe_snapshot']
        read_items.append({'path': str(p), 'sha256': sha(p), 'scope': 'Exact full BSA occurrence with evidence, source/recipe notes, all current ingredient/solution boundaries and preparation context. Full historical change serialization and unrelated chemical annotations are not independently re-approved.', 'occurrence_id': o['occurrence_id']})
pre = json.loads((L / 'preflight.json').read_text())
for r in pre['read_contracts']:
    read_items.append({**r, 'scope': 'Relevant identity, supplied-form, schema, audit-trail and isolated native-validation instructions read; unchanged hashes bound at preflight.'})
p = L.parent / 'issues/issue1226.json'
read_items.append({'path': str(p.relative_to(W)), 'sha256': sha(p), 'scope': 'Complete issue body on claim-specific MappingEvidence attribution; this correction adds no MappingEvidence.'})
save('read-ledger.json', {
    'author': '/root/materials_research', 'completed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'items': read_items,
    'scope_note': 'Actual scientific read scope is distinguished from the broader capture and maintained-catalog integrity checks. No new primary-source acquisition or independent self-review is claimed.',
})
selected = ['decisions.json', 'proposals.json', 'evidence.json', 'source-ledger.json', 'proposed/Bovine_Serum_Albumin.yaml', 'finding-dispositions.json', 'lineage-and-diff.json', 'validation.json', 'read-ledger.json', 'HANDOFF.md']
members = [{'path': str(p.relative_to(L)), 'sha256': sha(p), 'bytes': p.stat().st_size} for p in sorted(L.rglob('*')) if p.is_file() and p.name != 'FINAL-MANIFEST.json']
save('FINAL-MANIFEST.json', {
    'schema_version': 1, 'author': '/root/materials_research', 'sealed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'status': 'primary complete; independent review pending',
    'scope': {'proposal_id': 'W05-FINAL-MAT-007', 'case_indices': [11, 20, 70, 118, 120], 'cases': 5, 'occurrences': 7, 'proposals': 1, 'additive_evidence': 3, 'scientifically_changed_case_indices': [70]},
    'selected': {n: sha(L / n) for n in selected},
    'members': members,
    'published_reference_prefix': 'postseal-source-corrections-v1/materials/',
    'base_head': pre['head'],
    'limits': ['No whole-owner or coordinator-union approval.', 'No source/export release.', 'No maintained, prior report, Git or GitHub mutation.', 'Independent reviewer must bind the full new payload and all five decisions separately.'],
})
manifest = L / 'FINAL-MANIFEST.json'
check = json.loads(manifest.read_text())
assert all(sha(L / m['path']) == m['sha256'] for m in check['members'])
print(json.dumps({'manifest': str(manifest.relative_to(W)), 'sha256': sha(manifest), 'members': len(members), 'selected': check['selected']}))
