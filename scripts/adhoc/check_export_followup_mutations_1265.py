#!/usr/bin/env python3
"""Offline export regression mutations for #1265/#1267, 2026-11-08.

Inputs: current export sources and tests/test_stable_id_exports.py. Outputs:
fresh-process pytest logs, input hashes and results under the requested report
directory; disposable source copies under repository .temp. No embeddings,
models, network, maintained-source edits, Git operations or corpus writes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEST = 'tests/test_stable_id_exports.py'
CASES = [
    ('ambiguous_waiver_first_owner', 'scripts/validate_sssom_invariants.py',
     'if len(aliases.get(row["subject_id"], ())) == 1',
     'if len(aliases.get(row["subject_id"], ())) >= 1',
     'ambiguous_legacy_alias_cannot_transfer_synonym_waiver'),
    ('embedding_filename_identity', 'scripts/embed_records.py',
     'record_id = validate_id(rec.get("mim_id"))',
     'record_id = record_key_for_stem(path.stem)', 'embedding_record_identity'),
    ('embedding_filename_url', 'scripts/embed_records.py',
     'detail_url = "ingredient/" + record_id.replace(":", "_")',
     'detail_url = "records/ingredient/" + slug_for_source(category, path) + ".html"',
     'embedding_record_identity'),
    ('embedding_missing_id_fallback', 'scripts/embed_records.py',
     'record_id = validate_id(rec.get("mim_id"))',
     'record_id = validate_id(rec.get("mim_id") or "MIM:0000001")',
     'embedding_collection_refuses'),
    ('text_map_keeps_slug_identity', 'scripts/adhoc/project_text_map_ids_1265.py',
     "        point['id'] = identifier", '        pass', 'text_map_projection_changes'),
    ('text_map_keeps_old_address', 'scripts/adhoc/project_text_map_ids_1265.py',
     "        point['url'] = 'ingredient/' + identifier.replace(':', '_')", '        pass',
     'text_map_projection_changes'),
    ('text_map_changes_coordinates', 'scripts/adhoc/project_text_map_ids_1265.py',
     "        point['id'] = identifier", "        point['id'] = identifier\n        point['x'] = 0.0",
     'text_map_projection_changes'),
    ('text_map_unknown_owner_fallback', 'scripts/adhoc/project_text_map_ids_1265.py',
     "        identifier = index[point['url']]",
     "        identifier = index.get(point['url'], 'MIM:0000001')",
     'text_map_projection_refuses_unknown_or_ambiguous_owners and unknown_url'),
    ('text_map_duplicate_identity', 'scripts/adhoc/project_text_map_ids_1265.py',
     '        if identifier in seen:', '        if False:',
     'text_map_projection_refuses_unknown_or_ambiguous_owners and duplicate_id'),
    ('text_map_duplicate_url', 'scripts/adhoc/project_text_map_ids_1265.py',
     '        if url in index:', '        if False:',
     'text_map_projection_refuses_unknown_or_ambiguous_owners and duplicate_url'),
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    output.relative_to(ROOT / 'reports/stable_ids_1265_20261108')
    output.mkdir(parents=True, exist_ok=False)
    copies = ROOT / '.temp' / ('export-followup-' + output.name)
    copies.mkdir(parents=True, exist_ok=False)
    seed = copies / 'control'
    shutil.copytree(ROOT / 'src', seed / 'src', ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    sources = sorted({relative for _, relative, _, _, _ in CASES} | {TEST})
    for relative in sources:
        path = seed / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / relative, path)
    hashes = {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in sources}
    results = []
    control_selection = 'ambiguous_legacy_alias_cannot_transfer_synonym_waiver or embedding_ or text_map_projection_'
    for name, relative, old, new, selected in [('control', '', '', '', control_selection), *CASES]:
        tree = seed if name == 'control' else copies / name
        if name != 'control':
            shutil.copytree(seed, tree, ignore=shutil.ignore_patterns('__pycache__', '.pytest_cache'))
            target = tree / relative
            original = target.read_text()
            assert original.count(old) == 1, (name, original.count(old))
            target.write_text(original.replace(old, new, 1))
        env = dict(os.environ, PYTHONPATH=str(tree / 'src'),
                   PYTHONPYCACHEPREFIX=str(copies / ('bytecode-' + name)))
        cmd = [sys.executable, '-m', 'pytest', '-q', '-c', '/dev/null', '-p', 'no:cacheprovider',
               '--confcutdir', str(tree), '--basetemp', str(copies / ('pytest-' + name)),
               TEST, '-k', selected]
        run = subprocess.run(cmd, cwd=tree, env=env, text=True, capture_output=True, timeout=120)
        log = output / (name + '.log')
        sanitized = (run.stdout + run.stderr).replace(str(ROOT), '<repo>').replace(str(Path.home()), '<home>')
        log.write_text(sanitized)
        expected = run.returncode == 0 if name == 'control' else run.returncode == 1 and ' failed' in run.stdout
        results.append({'case': name, 'selection': selected, 'exit_code': run.returncode,
                        'expected_result': expected, 'log': log.name})
        receipt = {'issues': [1265, 1267], 'observed_at': datetime.now(timezone.utc).isoformat(),
                   'input_sha256': hashes, 'results': results, 'maintained_source_edits': False,
                   'models_or_network': 'NOT USED'}
        (output / 'results.json').write_text(json.dumps(receipt, indent=2) + '\n')
        print(json.dumps(results[-1]), flush=True)
        if not expected:
            raise SystemExit(f'Unexpected mutation result: {name}; see {log.name}')
    assert all(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest
               for name, digest in hashes.items()), 'Maintained inputs changed during mutation run'


if __name__ == '__main__':
    main()
