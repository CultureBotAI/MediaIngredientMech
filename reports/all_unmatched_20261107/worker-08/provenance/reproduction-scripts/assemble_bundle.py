"""2026-11-08: assemble reviewed worker08 fragments without scientific rewriting.

Inputs are the exact frozen shard and a curator-authored selection of final
fragment/reviewer files. Outputs stay under this worker's report root. The
campaign auditor, not this assembler, supplies structural acceptance.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'reports/all_unmatched_20261107/worker-08'
CONFIG = ROOT / '.temp/all-unmatched-worker-08/final-fragment-selection.json'


def read(path):
    return json.loads(path.read_text())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def case_digest(case):
    return hashlib.sha256(json.dumps(case, sort_keys=True, separators=(',', ':'),
                                    ensure_ascii=False, allow_nan=False).encode()).hexdigest()


def main():
    config = read(CONFIG)
    shard_path = OUT / 'provenance/shard-08.json'
    shard = read(shard_path)
    original = {case['case_id']: case for case in shard['cases']}
    decisions, evidence, proposals, provenance = [], [], [], []
    for group in config['groups']:
        paths = {key: OUT / group[key] for key in ('decisions', 'evidence', 'proposals')}
        hashes = {key: digest(path) for key, path in paths.items()}
        assert hashes == group['reviewed_fragment_sha256'], group['name']
        fragment = read(paths['decisions'])['decisions']
        ids = {entry['case_id'] for entry in fragment}
        assert ids == set(group['reviewed_case_ids']), group['name']
        assert group['reviewer'] != group['primary_author']
        review_ids = []
        for index, review_path in enumerate(group['final_review_paths']):
            path = OUT / review_path
            assert path.is_file() and path.stat().st_size > 0
            eid = f"w08-independent-{group['name']}-{index + 1}"
            review_ids.append(eid)
            evidence.append(dict(evidence_id=eid, kind='independent_review',
                capture=dict(root='artifact', path=review_path, sha256=digest(path)),
                url=None, locator='Exact input hashes, per-case assessments, proposal checks and finding dispositions',
                supports_or_contradicts=f"Separate skeptical review by {group['reviewer']} of this complete assigned subset; scope and limitations remain in the capture.",
                case_ids=sorted(ids)))
        for entry in fragment:
            case = original[entry['case_id']]
            assert entry['case_input_sha256'] == case_digest(case)
            assert entry['source'] == {key: case[key] for key in ('source', 'source_case_id', 'source_label', 'raw_source_label')}
            assert sorted(entry['occurrence_ids']) == sorted(o['occurrence_id'] for o in case.get('occurrences', []))
            final = copy.deepcopy(entry)
            final['independent_review'] = dict(status='complete', evidence_ids=review_ids)
            decisions.append(final)
        evidence.extend(read(paths['evidence'])['evidence'])
        proposals.extend(read(paths['proposals'])['proposals'])
        provenance.append(dict(group=group['name'], primary_author=group['primary_author'],
            reviewer=group['reviewer'], paths={key: group[key] for key in paths}, sha256=hashes,
            final_review_paths=group['final_review_paths'], case_count=len(fragment)))
    assert len(decisions) == len(original) == len({d['case_id'] for d in decisions})
    assert {d['case_id'] for d in decisions} == set(original)
    assert len(evidence) == len({e['evidence_id'] for e in evidence})
    assert len(proposals) == len({p['proposal_id'] for p in proposals})
    order = {c['case_id']: index for index, c in enumerate(shard['cases'])}
    decisions.sort(key=lambda d: order[d['case_id']])
    outputs = {
        'decisions.json': dict(schema_version=1, worker_slot=8, shard_sha256=digest(shard_path),
                               phase='shard', decisions=decisions),
        'evidence.json': dict(schema_version=1, evidence=evidence),
        'proposals.json': dict(schema_version=1, proposals=proposals),
        'assembly-provenance.json': dict(schema_version=1, fragments=provenance,
            scientific_text_rewritten=False,
            change='Only independent_review metadata is attached to original per-case scientific assessments.'),
    }
    for name, content in outputs.items():
        (OUT / name).write_text(json.dumps(content, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps(dict(decisions=len(decisions), evidence=len(evidence), proposals=len(proposals))))


if __name__ == '__main__':
    main()
