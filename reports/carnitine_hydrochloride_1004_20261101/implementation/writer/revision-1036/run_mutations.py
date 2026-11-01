"""Fresh-process controls in isolated copies; never edit maintained source."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import datetime
import hashlib
import json
import os
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[1] / 'step3-mim'
OWNED = json.loads((HERE / 'stable-source.json').read_text())

def sha(data):
    return hashlib.sha256(data).hexdigest()

for name, entry in OWNED.items():
    assert sha((SOURCE / name).read_bytes()) == entry['sha256'], name

mutants = [
    ('completed_receipt_binding_removed', 'scripts/merge_carnitine_hydrochloride.py',
     '        validate_completed_receipt(root, evidence, log, current)',
     '        pass  # mutant omits original receipt binding', 1,
     'test_completed_source_noop_requires_original_receipt_and_all_preimages'),
    ('callback_removed', 'scripts/merge_carnitine_hydrochloride.py',
     'validate_scope=lambda: validate_scope(root)', 'validate_scope=None', 2,
     'test_native_valid_competing_owner_is_rechecked_before_commit and True'),
    ('history_erased', 'scripts/merge_carnitine_hydrochloride.py',
     '        record_curation_event(record, curator=',
     '        record["curation_history"] = []\n        record_curation_event(record, curator=', 1,
     'test_exact_source_proposal_preserves_history_and_scientific_boundaries'),
    ('free_chemistry_retained', 'scripts/merge_carnitine_hydrochloride.py',
     '    tombstone.pop("chemical_properties")', '    pass  # mutant retains free chemistry', 1,
     'test_exact_source_proposal_preserves_history_and_scientific_boundaries'),
    ('membership_migration_omitted', 'scripts/merge_carnitine_hydrochloride.py',
     '    output[MEMBERSHIP] = corrected_membership(membership)', '    output[MEMBERSHIP] = membership', 1,
     'test_historical_membership_migration_preserves_exact_pairs_and_unrelated_bytes'),
    ('amide_ledger_rejection_omitted', 'scripts/merge_carnitine_hydrochloride.py',
     '.encode() + amide)', '.encode())', 1,
     'test_ledger_preserves_other_bytes_and_scopes_both_rejections'),
    ('candidate_claim_checks_removed', 'scripts/merge_carnitine_hydrochloride.py',
     '        if any(row.get(k) != v for k, v in expected.items()):', '        if False:', 1,
     'test_bad_native_candidate_refuses_before_promotion'),
    ('completed_anchor_check_removed', 'scripts/merge_carnitine_hydrochloride.py',
     '        validate_completed_anchors(inputs[root / SSSOM], inputs[root / BASELINE], current)',
     '        pass  # mutant omits completed anchor check', 1,
     'test_source_noop_accepts_complete_promotion_but_rejects_canonical_drift'),
    ('reservation_rechecks_removed', 'scripts/promote_heptahydrate_ncit.py',
     None, None, 1,
     'test_native_reservation_replacements_never_false_complete and sources and None'),
]

def run_one(item):
    name, target, old, new, count, selection = item
    work = HERE / 'mutations' / name
    work.mkdir(parents=True)
    (work / 'scripts').mkdir()
    (work / 'tests').mkdir()
    for path in ('scripts/merge_carnitine_hydrochloride.py', 'scripts/promote_heptahydrate_ncit.py',
                 'scripts/bump_sssom_header.py', 'tests/test_merge_carnitine_hydrochloride.py'):
        shutil.copyfile(SOURCE / path, work / path)
    if (SOURCE / 'scripts/__init__.py').exists():
        shutil.copyfile(SOURCE / 'scripts/__init__.py', work / 'scripts/__init__.py')
    (work / 'tests/fixtures').symlink_to(SOURCE / 'tests/fixtures', target_is_directory=True)
    (work / 'reports').symlink_to(SOURCE / 'reports', target_is_directory=True)
    (work / 'src').symlink_to(SOURCE / 'src', target_is_directory=True)
    (work / 'pytest.ini').write_text('[pytest]\naddopts =\n')
    path = work / target
    original = path.read_text()
    if old is None:
        start = original.index('def recheck_reserved(')
        end = original.index('\ndef publish(', start)
        changed = original[:start] + 'def recheck_reserved(reservations):\n    return None\n\n' + original[end:]
    else:
        assert original.count(old) == count, name
        changed = original.replace(old, new)
    path.write_text(changed)
    argv = [sys.executable, '-m', 'pytest', '-q', '-c', str(work / 'pytest.ini'),
            str(work / 'tests/test_merge_carnitine_hydrochloride.py'), '-k', selection]
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = subprocess.run(argv, cwd=work, env=os.environ.copy(), text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    log = HERE / 'mutations' / (name + '.log')
    with log.open('x') as stream:
        stream.write(result.stdout)
    receipt = {'name': name, 'argv': argv, 'started_at': started,
               'finished_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
               'source_sha256': sha(original.encode()), 'mutant_sha256': sha(changed.encode()),
               'exit_code': result.returncode, 'log_sha256': sha(result.stdout.encode()),
               'detected': result.returncode == 1 and 'FAILED tests/test_merge_carnitine_hydrochloride.py::' in result.stdout
                           and 'ERROR collecting' not in result.stdout}
    with (HERE / 'mutations' / (name + '.json')).open('x') as stream:
        json.dump(receipt, stream, indent=2); stream.write('\n')
    return receipt

with ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(run_one, mutants))
for name, entry in OWNED.items():
    assert sha((SOURCE / name).read_bytes()) == entry['sha256'], name
with (HERE / 'mutation-results.json').open('x') as stream:
    json.dump({'results': results, 'source_unchanged': True}, stream, indent=2); stream.write('\n')
print(json.dumps([{'name': x['name'], 'detected': x['detected'], 'exit_code': x['exit_code']} for x in results], indent=2))
assert all(x['detected'] for x in results)
