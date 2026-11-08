"""Bind separately authored skeptical captures to the assembled worker outputs.

The three original research bundles remain unchanged. Only review metadata and
administrative issue references are added to their aggregate copies.
"""
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'MAPPING_SEMANTICS.md').is_file())
OUT = ROOT / 'reports/all_unmatched_20261107/worker-03'
read = lambda p: json.loads(p.read_text())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
write = lambda p, d: p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')

REVIEWS = {
    'broths': 'materials/independent-review-of-broths.json',
    'chemicals': 'broths/independent-review-of-chemicals.json',
    'materials': 'chemicals/independent-review-of-materials.json',
}


def main():
    docs = {k: read(OUT / (k + '.json')) for k in ('decisions', 'evidence', 'proposals')}
    decisions = {d['case_id']: d for d in docs['decisions']['decisions']}
    proposals = {p['proposal_id']: p for p in docs['proposals']['proposals']}
    scopes = read(OUT / 'agent-scopes.json')
    reviewed = []
    for group, capture in REVIEWS.items():
        report = read(OUT / capture)
        assert report['status'] == 'complete'
        assert report['reviewer'] != '/root/' + group
        assert not report.get('open_findings') and not report.get('blocking_findings')
        hashes = report.get('input_hashes') or {Path(k).stem: v for k, v in report['reviewed_core_sha256'].items()}
        for kind in docs:
            assert sha(OUT / group / (kind + '.json')) == hashes[kind], (group, kind)
        original = read(OUT / group / 'decisions.json')['decisions']
        scoped = {d['case_id'] for d in original}
        assert {c['case_id'] for c in report['case_reviews']} == scoped
        assert len(report['case_reviews']) == len(scoped)
        proposal_reviews = {p['proposal_id']: p for p in report['proposal_reviews']}
        original_proposals = read(OUT / group / 'proposals.json')['proposals']
        assert set(proposal_reviews) == {p['proposal_id'] for p in original_proposals}
        for p in original_proposals:
            reviewed_proposal = proposal_reviews[p['proposal_id']]
            reviewed_sha = reviewed_proposal.get('after_sha256') or reviewed_proposal['after_capture']['sha256']
            assert reviewed_sha == p['after_capture']['sha256']
            assert sha(OUT / p['after_capture']['path']) == p['after_capture']['sha256']
        eid = 'root-independent-' + group
        docs['evidence']['evidence'].append({
            'evidence_id': eid, 'kind': 'independent_review', 'url': None,
            'accessed_at': report['reviewed_at'],
            'capture': {'root': 'artifact', 'path': capture, 'sha256': sha(OUT / capture)},
            'locator': 'input_hashes; case_reviews (all assigned IDs); proposal_reviews (all exact payloads); retained initial findings, corrections and limitations',
            'supports_or_contradicts': f"{report['reviewer']} separately assessed every {group} case and proposal against the cited primary and frozen source evidence. Final outcome and any resolved findings are explicit per case; no native publication or inherited-hold approval is inferred.",
            'case_ids': sorted(scoped),
        })
        for cid in scoped:
            decisions[cid]['independent_review'] = {'status': 'complete', 'evidence_ids': [eid],
                'reviewer': report['reviewer'], 'primary_author': '/root/' + group,
                'capture_sha256': sha(OUT / capture)}
        for p in original_proposals:
            proposals[p['proposal_id']]['independent_review'] = {
                'status': 'complete', 'evidence_ids': [eid], 'reviewer': report['reviewer'],
                'reviewed_after_sha256': p['after_capture']['sha256']}
        for scope in scopes['assignments']:
            if scope['primary_research_agent'] == '/root/' + group:
                scope.update(independent_review_status='complete', actual_independent_reviewer=report['reviewer'],
                             independent_review_capture=capture, independent_review_sha256=sha(OUT / capture),
                             reviewed_input_hashes=hashes, proposal_count=len(original_proposals))
        reviewed += sorted(scoped)
    assert len(reviewed) == len(set(reviewed)) == 188
    findings = read(OUT / 'findings-issues.json')['findings']
    owner_for_issue = {
        'bd211065': 'Heart_Infusion_Agar_BD_211065.yaml', 'molasses': 'Sugar_Beet_Molasses.yaml',
        'phb': 'Poly_3-hydroxybutyric_Acid.yaml', 'citrate': 'Citric_Acid_X_H2o.yaml',
        'nh4-s4': 'Nh42so4.yaml',
    }
    for finding in findings:
        related = []
        for d in decisions.values():
            match = (finding['finding_id'] == 'hsm' and d['source']['raw_source_label'] == 'Sterile')
            match |= any(Path(o['path']).name == owner_for_issue.get(finding['finding_id']) for o in d['owner_records'])
            if match:
                d['issue_refs'] = list(dict.fromkeys(d['issue_refs'] + [finding['url']]))
                related.append(d['case_id'])
        finding['case_ids'] = related
    for d in decisions.values():
        if 'm-jcm431_selenite_tungstate_solution' in d['proposal_ids']:
            d['issue_refs'] = list(dict.fromkeys(d['issue_refs'] + [
                'https://github.com/CultureBotAI/MediaIngredientMech/issues/718',
                'https://github.com/CultureBotAI/MediaIngredientMech/issues/1173']))
    review_tracker_path = OUT / 'review-correction-tracker.json'
    if review_tracker_path.is_file():
        tracker = read(review_tracker_path)
        for d in decisions.values():
            d['issue_refs'] = list(dict.fromkeys(d['issue_refs'] + [tracker['url']]))
    write(OUT / 'findings-issues.json', {'schema_version': 1, 'findings': findings,
        'authorization': 'Explicit worker assignment: file deduplicated real findings with evidence and followup; no mentions.',
        'existing_issue_refs': ['https://github.com/CultureBotAI/CultureMech/issues/408',
                               'https://github.com/CultureBotAI/MediaIngredientMech/issues/1165'],
        'integration_state': 'All maintained inputs unchanged; issues remain open for guarded coordinator or upstream action.'})
    for k, d in docs.items():
        write(OUT / (k + '.json'), d)
    write(OUT / 'agent-scopes.json', scopes)
    progress = read(OUT / 'progress.json')
    progress.update(reviewed_case_ids=sorted(reviewed), remaining_case_ids=[], reviewed_count=188,
                    remaining_count=0, primary_draft_count=188,
                    phase='scientific_reviews_complete_final_validation_and_publication_pending',
                    updated_at=datetime.now(timezone.utc).isoformat())
    write(OUT / 'progress.json', progress)
    print(json.dumps({'cases': len(decisions), 'proposals': len(proposals),
                      'evidence': len(docs['evidence']['evidence']),
                      'independent_review_statuses': dict(Counter(d['independent_review']['status'] for d in decisions.values()))}))


if __name__ == '__main__':
    main()
