"""One authorized append-only ledger transaction for reviewed MIM issue #1025."""
from __future__ import annotations

import csv
import datetime
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess

from kg_microbe_write import ValidatedWriteTransaction
from plugins.lock_manager import LockManager
from plugins.repository_settings import RepositorySettings

EVIDENCE = Path(__file__).resolve().parent
RUN = EVIDENCE.parent
PRODUCER = RUN / 'claw-source'
EXPECTED_PRODUCER = '0cc221bd0f4eb460030eb2e5d14b91a311ed2965'
PROPOSAL = RUN / 'step1-independent/proposed-source-holds.json'
EXPECTED_PROPOSAL_HASH = '105dfc13469d3f404bd68111c11e032a61eef1f748e7187ee6bded10ea34e76c'
EXPECTED_LEDGER_HASH = '12f2b4119e74b6d4bba4c1e74cee181fdc4c0efb0a3feb07b7a4bf785fab1493'
RELATIVE = Path('mappings/unified_mapping_rejections.tsv')
HEADER = ['ingredient_name', 'rejected_id', 'mim_id', 'reason']


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args], text=True).strip()


def save(name, value):
    with (EVIDENCE / name).open('x', encoding='utf-8') as handle:
        json.dump(value, handle, indent=2, ensure_ascii=False)
        handle.write('\n')


def input_hashes(root):
    paths = list((root / 'data/ingredients/mapped').glob('*.yaml'))
    paths += list((root / 'data/ingredients/unmapped').glob('*.yaml'))
    paths.append(root / 'docs/data/label_index.csv')
    return {str(p.relative_to(root)): sha(p.read_bytes()) for p in sorted(paths)}


target = RepositorySettings.from_environment().get_target('mediaingredientmech')
root = target.path.resolve()
assert root == (RUN / 'step1-mim').resolve()
target.open()
assert git(PRODUCER, 'rev-parse', 'HEAD') == EXPECTED_PRODUCER
assert git(PRODUCER, 'status', '--porcelain') == ''
assert sha(PROPOSAL.read_bytes()) == EXPECTED_PROPOSAL_HASH
proposal = json.loads(PROPOSAL.read_text())
rows = proposal['rows']
assert len(rows) == 33 and all(row['proposed_mim_id'] == '' for row in rows)
assert len({(row['ingredient_name'], row['rejected_id']) for row in rows}) == 33
spec = importlib.util.spec_from_file_location('merged_source_hold_builder', PRODUCER / 'scripts/build_unified_ingredient_mapping.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)

with LockManager().lock('mediaingredientmech', 'apply reviewed source-label holds #1025'):
    before = (root / RELATIVE).read_bytes()
    assert sha(before) == EXPECTED_LEDGER_HASH and before.endswith(b'\n')
    original = list(csv.DictReader(io.StringIO(before.decode()), delimiter='\t'))
    assert len(original) == 57 and all(row['mim_id'] for row in original)
    source_files = input_hashes(root)
    indexes = builder.load_mim_index(root)
    labels = builder.load_mim_label_index(root)
    live = builder.live_records(*indexes)
    owners = [{
        'ingredient_name': row['ingredient_name'], 'rejected_id': row['rejected_id'],
        'owner': builder._anchor_record(row['ingredient_name'], indexes[0], labels, live),
    } for row in rows]
    assert all(item['owner'] is None for item in owners), owners

    addition = io.StringIO(newline='')
    writer = csv.DictWriter(addition, fieldnames=HEADER, delimiter='\t', lineterminator='\n')
    for row in rows:
        context = row['source_contexts'][0]
        source = f"https://github.com/{proposal['source_repository']}/blob/{proposal['source_commit']}/{context['path']}"
        reason = (row['reason'] + f" Source: {source} ({context['selector']}; sha256 {context['sha256']}). "
                  'Reviewed in https://github.com/CultureBotAI/MediaIngredientMech/issues/1025; '
                  'source-hold contract https://github.com/CultureBotAI/culturebotai-claw/pull/698. '
                  'No independently resolved MIM owner; no replacement identity asserted.')
        writer.writerow({'ingredient_name': row['ingredient_name'], 'rejected_id': row['rejected_id'], 'mim_id': '', 'reason': reason})
    proposed = before.decode() + addition.getvalue()
    staging = EVIDENCE / 'staged'
    (staging / RELATIVE.parent).mkdir(parents=True, exist_ok=False)
    with (staging / RELATIVE).open('x', encoding='utf-8', newline='') as handle:
        handle.write(proposed)

    def validate(path, text):
        assert path == root / RELATIVE and text == proposed
        assert text.encode().startswith(before)
        parsed = list(csv.DictReader(io.StringIO(text), delimiter='\t'))
        assert parsed[:57] == original and len(parsed) == 90
        assert all(set(row) == set(HEADER) and all(value is not None for value in row.values()) for row in parsed)
        holds = parsed[57:]
        assert all(row['mim_id'] == '' and row['reason'] for row in holds)
        assert {(r['ingredient_name'], r['rejected_id']) for r in holds} == {(r['ingredient_name'], r['rejected_id']) for r in rows}
        assert len(builder.load_mapping_rejections(staging, indexes[0], label_index=labels, live=live)) == 90

    transaction = ValidatedWriteTransaction(root, validator=validate, journal_dir=EVIDENCE / 'journal')
    transaction.stage(RELATIVE, proposed)
    dry = transaction.commit()
    save('intent.json', {
        'created_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'authorization': 'Parent delegated bounded implementation of pre-filed MIM #1025 after Claw #698 merged.',
        'target': str(root), 'origin': git(root, 'remote', 'get-url', 'origin'),
        'target_head': git(root, 'rev-parse', 'HEAD'), 'target_branch': git(root, 'branch', '--show-current'),
        'status_before': git(root, 'status', '--short'), 'producer_head': EXPECTED_PRODUCER,
        'proposal_sha256': EXPECTED_PROPOSAL_HASH, 'before_sha256': sha(before),
        'proposed_sha256': sha(proposed.encode()), 'original_rows': 57, 'added_source_holds': 33,
        'original_bytes_preserved_as_prefix': True, 'caller_lock': 'mediaingredientmech',
        'dry_run': dry.as_dict(), 'owner_audit': owners, 'identity_input_hashes': source_files,
        'source_contexts': rows,
    })
    # Reserve the completion receipt before mutation; a failed attempt is never overwritten.
    with (EVIDENCE / 'applied.json').open('x', encoding='utf-8') as receipt:
        assert (root / RELATIVE).read_bytes() == before
        assert input_hashes(root) == source_files
        assert sha(PROPOSAL.read_bytes()) == EXPECTED_PROPOSAL_HASH
        applied = transaction.commit(apply=True)
        assert (root / RELATIVE).read_bytes() == proposed.encode()
        assert input_hashes(root) == source_files
        result = {
            'completed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'write_result': applied.as_dict(), 'after_sha256': sha((root / RELATIVE).read_bytes()),
            'identity_inputs_unchanged': True, 'original_rows_unchanged': 57,
            'added_source_holds': 33, 'total_rows': 90,
        }
        json.dump(result, receipt, indent=2)
        receipt.write('\n')
        print(json.dumps(result, indent=2))
