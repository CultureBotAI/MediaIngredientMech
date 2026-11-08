"""2026-11-08 worker03 evidence-only assembly; never edits maintained data.

Inputs: three disjoint researcher bundles plus the immutable assigned shard.
Outputs: combined campaign contract artifacts and explicit cross-shard owner hints.
Scientific independent-review captures are attached separately after review.
"""
from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'MAPPING_SEMANTICS.md').is_file())
OUT = ROOT / 'reports/all_unmatched_20261107/worker-03'
QUEUE = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def write(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def main():
    shard_path = QUEUE / 'shards/shard-03.json'
    shard = read(shard_path)
    expected = [c['case_id'] for c in shard['cases']]
    batches = {}
    for group in ('broths', 'chemicals', 'materials'):
        batches[group] = {kind: read(OUT / group / f'{kind}.json')[kind]
                          for kind in ('decisions', 'evidence', 'proposals')}
    combined = {kind: [item for batch in batches.values() for item in batch[kind]]
                for kind in ('decisions', 'evidence', 'proposals')}
    for kind, key in [('decisions', 'case_id'), ('evidence', 'evidence_id'), ('proposals', 'proposal_id')]:
        counts = Counter(item[key] for item in combined[kind])
        assert all(n == 1 for n in counts.values()), (kind, 'duplicate IDs')
    assert set(expected) == {c['case_id'] for c in combined['decisions']}
    combined['decisions'].sort(key=lambda d: expected.index(d['case_id']))
    write(OUT / 'decisions.json', {'schema_version': 1, 'worker_slot': 3,
                                  'shard_sha256': sha(shard_path), 'phase': 'shard',
                                  'decisions': combined['decisions']})
    for kind in ('evidence', 'proposals'):
        write(OUT / f'{kind}.json', {'schema_version': 1, kind: combined[kind]})

    proposed_owners = {p['owner_path'] for p in combined['proposals']}
    hints = []
    for path in sorted((QUEUE / 'shards').glob('shard-*.json')):
        other = read(path)
        if other['worker_slot'] == 3:
            continue
        for case in other['cases']:
            for owner in case.get('original_kg_entry', {}).get('owners', []):
                if owner['path'] in proposed_owners:
                    hints.append({'other_worker_slot': other['worker_slot'],
                                  'other_case_id': case['case_id'],
                                  'source_case_id': case['source_case_id'],
                                  'owner_path': owner['path'],
                                  'frozen_owner_sha256': owner['sha256'],
                                  'meaning': 'Shared frozen owner reference only; no identity merge or other-shard review claimed.'})
    write(OUT / 'cross-shard-owner-references.json', {
        'schema_version': 1, 'scope': 'Exact existing-owner references in the immutable ten-shard queue; new-owner and lexical-only conflicts still require coordinator reconciliation.',
        'references': hints,
        'coordinator_observed_actual_proposal_overlaps': [read(OUT / 'context/cross-shard-w01/observation.json')]
        if (OUT / 'context/cross-shard-w01/observation.json').is_file() else []})
    print(json.dumps({kind: len(items) for kind, items in combined.items()}, sort_keys=True))


if __name__ == '__main__':
    main()
