"""Immutable correction of an unpublished review-summary count; inputs unchanged."""
from pathlib import Path
import datetime
import hashlib
import importlib.util
import json
import yaml

R = Path.cwd()
A = R/'.temp/w03-provenance-successor-v1/assembly'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(A/'review.yaml') == 'cb5276968ec13a85d300555ae439f7861fd839d1ea304a31c8f80c689c51098f'
assert sha(A/'review.md') == 'd6f0167a3ec1212932a2905712c3176572c45b10b951e50ec52abca8c1452935'
spec = importlib.util.spec_from_file_location('native_review', R/'scripts/record_review.py')
native = importlib.util.module_from_spec(spec)
spec.loader.exec_module(native)
review = yaml.safe_load((A/'review.yaml').read_text())
native.assert_current_source(R, review)
proof = json.loads((A/'final-core-verification-v1.json').read_text())
regular = proof['original_tracked_regular_files']
links = proof['original_tracked_symlinks']
total = proof['original_tracked_blobs_unchanged']
assert regular + links == total
now = datetime.datetime.now(datetime.timezone.utc)
timestamp = now.isoformat().replace('+00:00', 'Z')
review['review_id'] = now.strftime('%Y%m%dT%H%M%SZ')+'-w03-provenance-successor-assembly-v2'
review['finished_at'] = timestamp
check = next(c for c in review['checks'] if c['check_id'] == 'independent-core')
old_summary = check['summary']
check['summary'] = f'188 cases,74 proposals,868 captures;863 old evidence objects preserved;{regular} regular tracked files plus{links} tracked symlinks ({total} total tracked blobs) and3028 ignored-inclusive maintained files unchanged.'
extra = [x['path'] for x in review['source']['inputs']]
extra += [str((A/n).relative_to(R)) for n in ['review.yaml', 'review.md', 'finding-private-draft-count-v1.json']]
inspection = native.inspect_source(R, review['targets'], extra)
review['source'] = inspection['source']
review['notes'].append('This immutable v2 corrects only the private unpublished v1 review summary count from15702 regular+1 symlink to the independently computed15701 regular+2 symlinks=15703 tracked blobs. The original proof was correct and all selected source/payload inputs are unchanged. V1 remains retained as an unaccepted drafting artifact; parent classified this as a review-summary transcription error, not a source/payload/writer finding requiring a new external issue.')
review['evidence'].append({'evidence_id': 'draft-count-correction', 'kind': 'prior_review',
                           'reference': str((A/'finding-private-draft-count-v1.json').relative_to(R)),
                           'locator': 'Exact original draft hashes and independently computed Git mode counts',
                           'accessed_at': timestamp, 'support': 'context_only',
                           'summary': 'V1 summary transcription error preserved before immutable correction; original complete proof had15701 regular files and2 symlinks.',
                           'snapshot_sha256': sha(A/'finding-private-draft-count-v1.json')})
native.validate_review(review)
native.assert_current_source(R, review)
raw = yaml.safe_dump(review, sort_keys=False, allow_unicode=True, width=100).encode()
markdown = native.render_markdown(review).encode()
native.parse_review_bundle('reviews/structured/'+review['review_id']+'/review.yaml', raw, markdown)
with (A/'review-v2.yaml').open('xb') as f: f.write(raw)
with (A/'review-v2.md').open('xb') as f: f.write(markdown)
with (A/'native-review-validation-v2.json').open('x') as f:
    json.dump({'status': 'PASS', 'review_id': review['review_id'], 'review_sha256': sha(A/'review-v2.yaml'),
               'markdown_sha256': sha(A/'review-v2.md'), 'native_calls': ['inspect_source', 'validate_review', 'assert_current_source', 'render_markdown', 'parse_review_bundle (virtual canonical path)'],
               'canonical_save_performed': False, 'scientific_review': False,
               'count_proof': {'regular': regular, 'symlinks': links, 'total': total},
               'prior_unaccepted_draft_summary': old_summary,
               'correction_summary': check['summary'], 'selected_input_bytes_unchanged': True}, f, indent=2); f.write('\n')
print(json.dumps({'review_id': review['review_id'], 'review_sha256': sha(A/'review-v2.yaml'), 'markdown_sha256': sha(A/'review-v2.md')}))
