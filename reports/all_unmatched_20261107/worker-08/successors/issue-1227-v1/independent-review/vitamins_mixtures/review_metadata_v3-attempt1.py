"""Independently bind the one-field evidence-provenance successor."""
import copy
import datetime
import hashlib
import json
from pathlib import Path

B = Path('reports/all_unmatched_20261107/worker-08')
S = B / 'successors/issue-1227-v1'
M = S / 'research/vitamins_mixtures'
R = S / 'independent-review/vitamins_mixtures'
now = datetime.datetime.now(datetime.timezone.utc).isoformat()

def rd(path):
    return json.loads(path.read_text())

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write(name, value):
    path = R / name
    assert not path.exists(), path
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')

def capture(path):
    return dict(root='artifact', path=str(path.relative_to(B)), sha256=sha(path))

prior_path = R / 'review.json'
assert sha(prior_path) == '76eb1a87e41dcfe0053692f8315a23661e2ccc1a17bba34b0d9feff6ba133ef4'
prior = rd(prior_path)
h = rd(M / 'final-v3/HANDOFF.json')
assert sha(M / 'final-v3/HANDOFF.json') == '6b3f39e93c30f11790a423cb0eb92923c07b10002749090c38eb1d3f23de4920'
before = rd(M / 'final-v2/evidence-additions.json')
after = rd(M / 'final-v3/evidence-additions.json')
expected = copy.deepcopy(before)
target = next(e for e in expected['evidence'] if e['evidence_id'] == 'vm1227-v2-dl-ontology')
assert target['kind'] == 'ontology' and target['url'] is None
target['kind'] = 'local_validation'
assert after == expected
for c in h['selected_indices'].values():
    assert sha(B / c['path']) == c['sha256']
assert h['selected_indices']['decisions']['sha256'] == prior['input_hashes'][h['selected_indices']['decisions']['path']]
assert h['selected_indices']['proposals']['sha256'] == prior['input_hashes'][h['selected_indices']['proposals']['path']]
remediation = rd(M / 'final-v3/metadata-remediation.json')
for path, digest in remediation['all_final_v2_files_preserved'].items():
    assert sha(B / path) == digest, path
for path, digest in prior['input_hashes'].items():
    assert sha(B / path) == digest, path
proposals = rd(B / h['selected_indices']['proposals']['path'])['proposals']
for p in proposals:
    assert sha(B / p['after_capture']['path']) == prior['payload_hashes'][p['proposal_id']]

# Focused evidence rules are evaluated independently, without changing the gate.
allowed = {'primary_source', 'source_snapshot', 'ontology', 'native_record_review',
           'independent_review', 'unsuccessful_search', 'local_validation'}
checked = []
for e in after['evidence']:
    assert e['kind'] in allowed
    assert e['locator'] and e['supports_or_contradicts']
    u = e.get('url')
    assert u is None or isinstance(u, str) and u.startswith(('https://', 'http://'))
    if u is not None:
        assert e.get('accessed_at')
    if e['kind'] in {'ontology', 'primary_source'}:
        assert u is not None
    assert e['capture']['root'] == 'artifact'
    assert sha(B / e['capture']['path']) == e['capture']['sha256']
    checked.append(e['evidence_id'])
live = next(e for e in after['evidence'] if e['evidence_id'] == 'vm1227-v2-live-lipoic-ontology')
assert live == next(e for e in before['evidence'] if e['evidence_id'] == live['evidence_id'])
validation = dict(at=now, reviewer='/root/organics', author='/root/vitamins',
    status='PASS', selected_indices=h['selected_indices'], prior_review=capture(prior_path),
    exact_diff=[dict(evidence_id=target['evidence_id'], field='kind', before='ontology', after='local_validation')],
    all_other_evidence_fields_unchanged=True, all_prior_input_hashes_valid=True,
    all_final_v2_files_preserved=True, all_57_case_hashes_unchanged=True,
    all_47_payload_hashes_reverified=True, evidence_rules_and_capture_hashes_checked=checked,
    scientific_and_native_revalidation='Not repeated: all case, payload and primary capture bytes are unchanged. Prior complete scientific and native receipts remain valid for those exact inputs. This focused check covers metadata only; root full accounting remains separate.')
write('metadata-successor-validation-v3.json', validation)

ledger = rd(R / 'source-read-ledger.json')
changed = 0
for e in ledger['entries']:
    if e.get('evidence_id') == target['evidence_id']:
        assert e['kind'] == 'ontology'
        e['kind'] = 'local_validation'
        changed += 1
assert changed == 1
ledger['metadata_successor'] = dict(at=now, original_read_ledger=capture(R / 'source-read-ledger.json'),
    description='Only the local query receipt kind is corrected. Original source access times, read locators, actual reading limitations and capture hashes remain unchanged.')
write('source-read-ledger-v3.json', ledger)

findings = rd(R / 'findings.json')
findings['findings'].append(dict(finding_id='W08-1227-ASSEMBLY-001', severity='minor',
    status='resolved_after_exact_metadata_successor_review', at=now,
    coordinator_route=capture(S / 'COORDINATOR-ASSEMBLY-FINDING-v1.json'),
    original_observation=capture(R / 'metadata-provenance-review-v3.json'),
    validation=capture(R / 'metadata-successor-validation-v3.json'),
    resolution='The captured hash-bound local ChEBI/NCIt inspection and query receipt is now local_validation with its original null URL and local inspection time. The separate current official OLS ontology entry retains its real URL and original access time. No source access event or scientific identity is invented; all case, payload, scientific and release boundaries are unchanged.'))
write('findings-v3.json', findings)

review = copy.deepcopy(prior)
review.update(at=now, version='final-v3-metadata-only', predecessor_review=capture(prior_path),
    selected_indices=h['selected_indices'], findings_receipt='findings-v3.json',
    source_read_ledger='source-read-ledger-v3.json',
    metadata_validation_receipt='metadata-successor-validation-v3.json',
    metadata_review=dict(finding_id='W08-1227-ASSEMBLY-001', status='resolved',
        scope='One evidence category field only. All 57 individual case appraisals, 47 whole-payload appraisals, 300 component and 49 category assessments remain the previously completed independent review of unchanged scientific bytes. No new scientific or release approval.'))
for path in [M / 'final-v3/HANDOFF.json', M / 'final-v3/evidence-additions.json',
             M / 'final-v3/metadata-remediation.json', M / 'final-v3/metadata-validation.json',
             S / 'COORDINATOR-ASSEMBLY-FINDING-v1.json', R / 'metadata-successor-validation-v3.json',
             R / 'metadata-provenance-review-v3.json', prior_path]:
    review['input_hashes'][str(path.relative_to(B))] = sha(path)
assert review['case_hashes'] == prior['case_hashes'] and review['payload_hashes'] == prior['payload_hashes']
assert review['case_reviews'] == prior['case_reviews'] and review['proposal_reviews'] == prior['proposal_reviews']
assert not review['open_blocking_findings']
write('review-v3.json', review)
write('progress-v3.json', dict(at=now, status='complete_metadata_successor_review', cases=57,
    payloads=47, unchanged_scientific_review=True, open_blocking_findings=[],
    review=capture(R / 'review-v3.json')))
handoff = R / 'HANDOFF-v3.md'
assert not handoff.exists()
handoff.write_text(f'''# Metadata successor review handoff

The one-field evidence correction is independently verified. `vm1227-v2-dl-ontology` now uses `local_validation` for the actual local database-query receipt. Its null URL, original inspection time and exact capture remain unchanged. The separate official OLS evidence retains its real URL and original access time.

`review-v3.json` SHA-256: `{sha(R / 'review-v3.json')}`.

Selected evidence index: `{h['selected_indices']['evidence_additions']['sha256']}`. The final-v2 decisions and proposals remain selected, with all 57 cases and 47 payload hashes unchanged. All original scientific appraisals, known unapproved fields, source/native/export holds and conditional dependencies remain operative. No scientific/native rerun or release approval is implied.

The predecessor `review.json` and every final-v2 author file are preserved. The new focused check verified all 22 evidence rows and hashes; root performs the complete combined accounting separately.
''')
assert sha(prior_path) == '76eb1a87e41dcfe0053692f8315a23661e2ccc1a17bba34b0d9feff6ba133ef4'
print(json.dumps(dict(review_sha256=sha(R / 'review-v3.json'),
    input_hashes=len(review['input_hashes']), cases=len(review['case_ids']),
    payloads=len(review['proposal_ids']), changed_evidence_fields=1, status='PASS')))
