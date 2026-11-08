"""Bind authored decisions to actual independent reviews; never infer approval.

This one-shot integration checks the reviewed original decision digests, the
three separately reviewed cross-author links and the three composed payloads.
It changes only independent_review metadata on the assembled decisions.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent
SOURCE = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest()


def verify_decision(decision, review):
    if review.get('status', review.get('review_outcome')) != 'approve':
        raise ValueError('Independent review does not approve this scoped outcome')
    expected = review.get('decision_canonical_sha256', review.get('decision_sha256'))
    if digest(decision) != expected:
        raise ValueError(f"Reviewed decision changed: {decision['case_id']}")
    if decision['case_id'] != review['case_id'] or decision['case_input_sha256'] != review['case_input_sha256']:
        raise ValueError('Reviewed case identity changed')


def load(name):
    return json.loads((ROOT / name).read_text())


def verify_refs(refs):
    for ref in refs:
        root = {'artifact': ROOT, 'source': SOURCE, 'mim': Path.cwd()}[ref.get('root', 'artifact')]
        path = root / ref['path']
        if hashlib.sha256(path.read_bytes()).hexdigest() != ref['sha256']:
            raise ValueError(f'Reviewed input changed: {path}')


def run():
    dest = ROOT / 'integration/independent-review-coverage.json'
    if dest.exists():
        raise FileExistsError(dest)
    original = {}
    authors = {}
    for a in ('a', 'b', 'c'):
        for d in load(f'{a}/decisions.json')['decisions']:
            original[d['case_id']] = d
            authors[d['case_id']] = a
    documents = {
        'w02-review-b-of-a': 'b/review-a/review.json',
        'w02-review-a-of-c': 'a/independent-review-c.json',
        'w02-review-c-of-b': 'c/independent-review-b.json',
        'w02-review-a-of-b65': 'a/independent-review-b65.json',
        'w02-review-b-of-c166': 'b/review-a/additional-review-c166.json',
        'w02-review-b-root-links': 'b/review-a/root-links-final.json',
        'w02-review-c-shared': 'c/independent-review-shared.json',
    }
    reviewed = {k: load(p) for k, p in documents.items()}
    for key in ('w02-review-a-of-c', 'w02-review-c-of-b', 'w02-review-a-of-b65', 'w02-review-c-shared'):
        verify_refs(reviewed[key]['input_hash_manifest'])
    bh = load('b/review-a/input-hashes.json')
    verify_refs(bh['inputs'] + bh['proposal_payloads'])
    verify_refs(reviewed['w02-review-b-root-links']['input_files'])
    case_reviews = {}
    for key, field in [('w02-review-b-of-a','reviews'), ('w02-review-a-of-c','case_reviews'), ('w02-review-c-of-b','case_reviews')]:
        for row in reviewed[key][field]:
            if row.get('status',row.get('review_outcome')) == 'approve':
                verify_decision(original[row['case_id']], row)
                case_reviews[row['case_id']] = (key, row)
    c166 = reviewed['w02-review-b-of-c166']
    verify_decision(original[c166['case_id']], c166)
    case_reviews[c166['case_id']] = ('w02-review-b-of-c166', c166)
    b65 = reviewed['w02-review-a-of-b65']
    case_reviews[b65['case_id']] = ('w02-review-a-of-b65', b65)
    decisions, evidence, proposals = load('decisions.json'), load('evidence.json'), load('proposals.json')
    links = {r['case_id']: r for r in reviewed['w02-review-b-root-links']['reviews']}
    shared = {r['proposal_id']: r for r in reviewed['w02-review-c-shared']['proposal_reviews']}
    for p in proposals['proposals']:
        if p['proposal_id'] in shared:
            row = shared[p['proposal_id']]
            assert row['status'] == 'approve' and row['after_capture'] == p['after_capture']
            verify_refs([row['after_capture']])
    for name in ('decisions', 'evidence', 'proposals'):
        shutil.copyfile(ROOT / f'{name}.json', ROOT / 'integration' / f'pre-review-binding-{name}.json')
    now = datetime.now(timezone.utc).isoformat()
    coverage = []
    for d in decisions['decisions']:
        cid = d['case_id']
        key, review = case_reviews[cid]
        reviewer = reviewed[key]['reviewer']
        if reviewer.endswith('research_' + authors[cid]):
            raise ValueError('Self-review cannot supply independent approval')
        refs = [key]
        before = digest(d)
        if cid in links:
            assert before == links[cid]['root_decision_canonical_sha256']
            refs.append('w02-review-b-root-links')
        elif cid == b65['case_id']:
            verify_decision(d, b65)
        else:
            differences = {k for k in set(d) | set(original[cid]) if d.get(k) != original[cid].get(k)}
            if differences - {'proposal_ids'}:
                raise ValueError(f'Unreviewed root changes: {cid}: {differences}')
        for pid in d['proposal_ids']:
            if pid in shared:
                assert cid in shared[pid]['case_ids']
                refs.append('w02-review-c-shared')
        d['independent_review'] = {'status':'complete', 'evidence_ids':list(dict.fromkeys(refs))}
        coverage.append({'case_id':cid,'primary_author':authors[cid], 'independent_reviewer':reviewer,
                         'review_evidence_ids':d['independent_review']['evidence_ids'],
                         'authored_decision_sha256':digest(original[cid]),
                         'reviewed_assembled_decision_sha256':before,
                         'final_decision_sha256':digest(d)})
    for key, path in documents.items():
        evidence['evidence'].append({'evidence_id':key,'kind':'independent_review',
            'capture':{'root':'artifact','path':path,'sha256':hashlib.sha256((ROOT/path).read_bytes()).hexdigest()},
            'url':None,'accessed_at':now,
            'locator':'Exact reviewed decision/proposal digests and per-case reasoning; review scopes and author independence are explicit in the capture.',
            'supports_or_contradicts':'Independent scoped scientific assessment, including retained unresolved requirements. This does not approve entire owner records or publication.'})
    for name, value in [('decisions', decisions), ('evidence', evidence)]:
        (ROOT / f'{name}.json').write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
    dest.write_text(json.dumps({'created_at':now,'case_count':len(coverage),'cases':coverage,
        'limits':'Every scientific decision has a distinct author/reviewer. Final binding changes review metadata only. All owner/export holds remain.'},indent=2)+'\n')
    print({'independently_reviewed':len(coverage),'evidence_entries':len(evidence['evidence'])})


if __name__ == '__main__':
    run()
