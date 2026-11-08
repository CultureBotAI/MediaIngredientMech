"""Attach independently assessed final publisher followups for two source-only cases.

Run after assemble.py and attach_reviews.py. Author cores and earlier reviews
remain immutable; no outcome, owner or proposal is replaced by this supplement.
"""
import datetime
import hashlib
import json
from pathlib import Path

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'MAPPING_SEMANTICS.md').is_file())
OUT = ROOT / 'reports/all_unmatched_20261107/worker-03'
read = lambda p: json.loads(p.read_text())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
write = lambda p, d: p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
A = 'KG_CASE:33c13b23fafbf9588be9c5570e87b1ec40a840bd1da2c1616a3cd9f3913d1478'
G = 'KG_CASE:4fb6d439270ed94097d3ade71c3f52468c7b915b2bcff39b0fadcbc4b223aa19'


def main():
    capture_path = 'context/bergey-final-primary-followup.json'
    review_path = 'validation/bergey-supplement-review.json'
    capture = read(OUT / capture_path)
    review = read(OUT / review_path)
    # The separate reviewer receipt itself documents scope, capture hashes and
    # unchanged unresolved verdict; root additionally binds its exact bytes.
    assert review['reviewer'] == '/root/final_review'
    assert review['status'] == 'complete' and not review['open_findings']
    assert set(review['case_ids']) == {A, G}
    assert review['capture']['sha256'] == sha(OUT / capture_path)
    first_time = capture['first']['accessed_at'].replace(' UTC', '+00:00').replace(' ', 'T')
    followup_time = capture['followup']['accessed_at'].replace(' UTC', '+00:00').replace(' ', 'T')
    evidence = read(OUT / 'evidence.json')
    decisions = read(OUT / 'decisions.json')
    assert not any(e['evidence_id'].startswith('root-bergey-') for e in evidence['evidence'])
    new = [
        {'evidence_id': 'root-bergey-gardnerella-abstract', 'kind': 'primary_source',
         'url': 'https://onlinelibrary.wiley.com/doi/10.1002/9781118960608.gbm00020',
         'accessed_at': first_time, 'case_ids': [G],
         'locator': 'first.result: exact DOI Gardnerella publisher page, Abstract lines82–89; not full chapter substrate passage',
         'supports_or_contradicts': 'Publisher abstract discusses several carbohydrate examples. It does not identify which substance the frozen generic sugar token denotes; no maltose/starch identity is inferred.'},
        {'evidence_id': 'root-bergey-gardnerella-fulltext-attempt', 'kind': 'unsuccessful_search',
         'url': 'https://onlinelibrary.wiley.com/doi/full/10.1002/9781118960608.gbm00020',
         'accessed_at': followup_time, 'case_ids': [G],
         'locator': 'followup.result: publisher Read the full text link redirected to /doi/abs/; returned abstract and references, not full substrate passage',
         'supports_or_contradicts': 'This exact publisher full-text request did not retrieve the required passage. Bounded access limitation only, not proof that the chapter is unavailable elsewhere.'},
        {'evidence_id': 'root-bergey-alkaliflexus-attempts', 'kind': 'unsuccessful_search',
         'url': 'https://onlinelibrary.wiley.com/doi/10.1002/9781118960608.gbm00239',
         'accessed_at': followup_time, 'case_ids': [A],
         'locator': 'first.result DOI-specific search and /doi/ open; followup.result /doi/abs/403 and /doi/full/ inaccessible',
         'supports_or_contradicts': 'Exact DOI searches and three publisher paths did not retrieve the original Alkaliflexus substrate passage. A mirrored abstract/search result is not used to identify the source sugar. Bounded failed access, not a global absence claim.'},
    ]
    for e in new:
        e['capture'] = {'root': 'artifact', 'path': capture_path, 'sha256': sha(OUT / capture_path)}
    independent_id = 'root-bergey-independent-review'
    new.append({'evidence_id': independent_id, 'kind': 'independent_review', 'url': None,
                'capture': {'root': 'artifact', 'path': review_path, 'sha256': sha(OUT / review_path)},
                'locator': 'Exact two source-case assessments, new publisher capture hash, applicability and unchanged unresolved outcomes',
                'supports_or_contradicts': 'A separate non-author reviewer assessed the final publisher followups and confirmed that neither generic source sugar has a supported exact substrate identity. Original author cores and earlier reviews are preserved.',
                'case_ids': [A, G]})
    evidence['evidence'] += new
    for d in decisions['decisions']:
        if d['case_id'] in {A, G}:
            assert d['disposition'] == 'unresolved' and not d['proposal_ids']
            d['evidence_ids'] += [e['evidence_id'] for e in new[:-1] if d['case_id'] in e['case_ids']]
            d['independent_review']['evidence_ids'].append(independent_id)
            d['independent_review']['additional_reviewers'] = ['/root/final_review']
            d['supplemental_assessments'] = [{
                'author': '/root', 'independent_reviewer': '/root/final_review',
                'capture': capture_path, 'review': review_path,
                'outcome_effect': 'No change: exact source substrate remains unresolved; original full passage not retrieved in these bounded attempts.',
                'access_state_supersession': ('The original reasoning records failed initial DOI opens. The later Gardnerella publisher abstract was retrieved; its full-text link still returned the abstract. This supersedes only the earlier access-state clause, not the original frozen provenance or unresolved identity.'
                    if d['case_id'] == G else 'Initial DOI and later publisher route attempts failed; no original full substrate passage retrieved in the bounded review.'),
            }]
    write(OUT / 'evidence.json', evidence)
    write(OUT / 'decisions.json', decisions)
    print(json.dumps({'case_outcomes_changed': 0, 'proposal_payloads_changed': 0,
                      'additional_evidence': len(new), 'total_evidence': len(evidence['evidence'])}))


if __name__ == '__main__':
    main()
