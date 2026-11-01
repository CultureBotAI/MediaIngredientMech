"""Run isolated fresh-process negative controls; never alter the working gate."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

EVIDENCE = Path(__file__).resolve().parent
ROOT = EVIDENCE.parent / 'step1-mim'
source = (ROOT / 'scripts/check_unified_rejections.py').read_text()
test = ROOT / 'tests/test_unified_source_holds.py'
cases = {
    'positive': None,
    'empty_identity_global_match': (
        'bool(rejected["mim_id"]) and row["mim_id"] == rejected["mim_id"]',
        'row["mim_id"] == rejected["mim_id"]',
    ),
    'source_holds_ignored': (
        'for rejected in rejections:\n',
        'for rejected in rejections:\n                    if not rejected["mim_id"]:\n                        continue\n',
    ),
    'nfc_removed': (
        'unicodedata.normalize("NFC", name).strip().casefold()',
        'name.strip().casefold()',
    ),
    'source_label_removed_from_key': (
        '("source_label", _label_key(row["ingredient_name"]), row["rejected_id"])',
        '(row["mim_id"], row["rejected_id"])',
    ),
    'only_chebi_column_checked': (
        'for column in IDENTITY_COLUMNS:',
        'for column in ("chebi_id",):',
    ),
}
results = []
for name, replacement in cases.items():
    case = EVIDENCE / 'mutations' / name
    (case / 'scripts').mkdir(parents=True, exist_ok=False)
    (case / 'tests').mkdir()
    modified = source
    if replacement:
        old, new = replacement
        assert source.count(old) == 1, (name, source.count(old))
        modified = source.replace(old, new)
    (case / 'scripts/check_unified_rejections.py').write_text(modified)
    shutil.copyfile(test, case / 'tests/test_unified_source_holds.py')
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONPYCACHEPREFIX=str(case / 'pycache'))
    args = [sys.executable, '-m', 'pytest', 'tests/test_unified_source_holds.py',
            '-k', 'not reviewed_source_hold_cohort', '--no-cov', '-q', '--tb=short',
            '--confcutdir', str(case)]
    proc = subprocess.run(args, cwd=case, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    with (case / 'pytest.log').open('x') as stream:
        stream.write(proc.stdout)
    result = {'name': name, 'argv': args, 'cwd': str(case), 'exit_code': proc.returncode,
              'source_sha256': hashlib.sha256(modified.encode()).hexdigest(),
              'log_sha256': hashlib.sha256(proc.stdout.encode()).hexdigest(),
              'summary': proc.stdout.splitlines()[-1]}
    results.append(result)
    print(json.dumps(result))
    assert proc.returncode == (0 if replacement is None else 1), result
assert (ROOT / 'scripts/check_unified_rejections.py').read_text() == source
with (EVIDENCE / 'mutation-results.json').open('x') as stream:
    json.dump({'completed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
               'working_gate_unchanged': True, 'fresh_process_each': True, 'results': results}, stream, indent=2)
    stream.write('\n')
