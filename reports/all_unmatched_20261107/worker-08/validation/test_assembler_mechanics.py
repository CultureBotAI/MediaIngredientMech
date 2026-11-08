"""Failure-oriented controls for worker08's private fragment assembler.

This tests assembly mechanics, not scientific adequacy or independent approval.
The reviewer authored the inorganic primary fragment. Every execution redirects
the imported assembler to disposable copies under the repository's .temp/ tree.
No maintained records, scientific fragments, or final bundle files are edited.
"""
from __future__ import annotations

import argparse
import contextlib
import copy
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import traceback
from datetime import datetime, timezone


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def object_digest(value):
    data = json.dumps(value, sort_keys=True, separators=(',', ':'),
                      ensure_ascii=False, allow_nan=False).encode()
    return hashlib.sha256(data).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')


def build_synthetic(base):
    """Minimal mechanical fixture; never represented as scientific evidence."""
    cases = []
    for index in range(3):
        cases.append(dict(case_id=f'CONTROL:{index}', source='synthetic_control',
                          source_case_id=str(index), source_label=f'Control {index}',
                          raw_source_label=f'Control {index}',
                          occurrences=[dict(occurrence_id=f'CONTROL_OCC:{index}')]))
    write(base / 'provenance/shard-08.json', dict(cases=cases))
    groups = []
    for name, subset in [('a', cases[:2]), ('b', cases[2:])]:
        decisions = [dict(case_id=c['case_id'], case_input_sha256=object_digest(c),
                          source={key: c[key] for key in
                                  ('source', 'source_case_id', 'source_label', 'raw_source_label')},
                          occurrence_ids=[o['occurrence_id'] for o in c['occurrences']],
                          reasoning='SYNTHETIC ASSEMBLER CONTROL ONLY',
                          independent_review=dict(status='pending', evidence_ids=[]))
                     for c in subset]
        paths = {kind: f'{name}/{kind}.json' for kind in ('decisions', 'evidence', 'proposals')}
        write(base / paths['decisions'], dict(decisions=decisions))
        write(base / paths['evidence'], dict(evidence=[dict(evidence_id=f'CONTROL_E:{name}')]))
        write(base / paths['proposals'], dict(proposals=[dict(proposal_id=f'CONTROL_P:{name}')]))
        write(base / f'{name}/review.json', dict(control_only=True))
        groups.append(dict(name=name, **paths,
                           reviewed_fragment_sha256={key: digest(base / value)
                                                     for key, value in paths.items()},
                           reviewed_case_ids=[c['case_id'] for c in subset],
                           primary_author=f'primary-{name}', reviewer=f'reviewer-{name}',
                           final_review_paths=[f'{name}/review.json']))
    return dict(groups=groups)


def paths_for(config):
    result = {'provenance/shard-08.json'}
    for group in config['groups']:
        result.update(group[key] for key in ('decisions', 'evidence', 'proposals'))
        result.update(group['final_review_paths'])
    return sorted(result)


def revise(base, config, key, callback, update_hash=True, group_index=0):
    group = config['groups'][group_index]
    path = base / group[key]
    document = read(path)
    callback(document[key])
    write(path, document)
    if update_hash:
        group['reviewed_fragment_sha256'][key] = digest(path)


def mutate_stale_hash(base, config):
    revise(base, config, 'decisions',
           lambda rows: rows[0].update(reasoning=rows[0]['reasoning'] + ' STALE CONTROL'),
           update_hash=False)


def mutate_omitted_case(base, config):
    # Update the selected-case roster AND fragment hash so only full shard
    # coverage can catch this omission, rather than an earlier hash/roster gate.
    group = config['groups'][0]
    removed = read(base / group['decisions'])['decisions'][0]['case_id']
    revise(base, config, 'decisions', lambda rows: rows.pop(0))
    group['reviewed_case_ids'].remove(removed)


def mutate_occurrence(base, config):
    revise(base, config, 'decisions',
           lambda rows: rows[0]['occurrence_ids'].append('CONTROL:WRONG_FROZEN_OCCURRENCE'))


def mutate_source(base, config):
    revise(base, config, 'decisions',
           lambda rows: rows[0]['source'].update(source_label='CONTROL:WRONG_FROZEN_SOURCE'))


def mutate_case_digest(base, config):
    revise(base, config, 'decisions',
           lambda rows: rows[0].update(case_input_sha256='0' * 64))


def mutate_duplicate_evidence(base, config):
    revise(base, config, 'evidence', lambda rows: rows.append(copy.deepcopy(rows[0])))


def mutate_duplicate_proposal(base, config):
    for index, group in enumerate(config['groups']):
        if read(base / group['proposals'])['proposals']:
            revise(base, config, 'proposals', lambda rows: rows.append(copy.deepcopy(rows[0])),
                   group_index=index)
            return
    raise AssertionError('Control needs at least one proposal in selected final inputs')


def mutate_self_review(base, config):
    config['groups'][0]['reviewer'] = config['groups'][0]['primary_author']


CONTROLS = [
    ('valid_control', None),
    ('stale_fragment_hash', mutate_stale_hash),
    ('omitted_frozen_case_after_roster_update', mutate_omitted_case),
    ('wrong_frozen_occurrence', mutate_occurrence),
    ('wrong_frozen_source', mutate_source),
    ('wrong_frozen_case_digest', mutate_case_digest),
    ('duplicate_evidence_id', mutate_duplicate_evidence),
    ('duplicate_proposal_id', mutate_duplicate_proposal),
    ('self_review', mutate_self_review),
]


def run_one(assembler_path, pristine, selected, stage, name, mutation):
    out = stage / name / 'report-root'
    shutil.copytree(pristine, out)
    config = copy.deepcopy(selected)
    if mutation:
        mutation(out, config)
    config_path = stage / name / 'selection.json'
    write(config_path, config)
    spec = importlib.util.spec_from_file_location(f'worker08_assembler_control_{name}', assembler_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.OUT = out
    module.CONFIG = config_path
    output = io.StringIO()
    failure = None
    with contextlib.redirect_stdout(output):
        try:
            module.main()
        except Exception as exc:
            failure = dict(type=type(exc).__name__, message=str(exc),
                           traceback=traceback.format_exc())
    names = ['decisions.json', 'evidence.json', 'proposals.json', 'assembly-provenance.json']
    existing = [key for key in names if (out / key).exists()]
    row = dict(control=name, expected='reject_before_any_output' if mutation else 'accept',
               observed_exception=failure, stdout=output.getvalue().strip(),
               output_files_created=existing)
    if mutation:
        row['passed'] = bool(failure and failure['type'] == 'AssertionError' and not existing)
    else:
        row['passed'] = failure is None and len(existing) == 4
        if row['passed']:
            assembled = read(out / 'decisions.json')['decisions']
            original = {d['case_id']: d for group in selected['groups']
                        for d in read(pristine / group['decisions'])['decisions']}
            for entry in assembled:
                before = copy.deepcopy(original[entry['case_id']])
                after = copy.deepcopy(entry)
                before.pop('independent_review')
                after.pop('independent_review')
                assert after == before, 'Assembler rewrote scientific fields'
                assert entry['independent_review']['status'] == 'complete'
                assert entry['independent_review']['evidence_ids']
            expected_proposals = [p for group in selected['groups']
                                  for p in read(pristine / group['proposals'])['proposals']]
            assert read(out / 'proposals.json')['proposals'] == expected_proposals
            row['scientific_fields_unchanged'] = True
            row['proposal_objects_unchanged'] = True
            row['output_sha256'] = {key: digest(out / key) for key in names}
    return row


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['synthetic', 'final'], default='final')
    parser.add_argument('--repo-root', type=Path, default=Path(__file__).resolve().parents[4])
    args = parser.parse_args()
    root = args.repo_root.resolve()
    assembler = root / '.temp/all-unmatched-worker-08/assemble_bundle.py'
    actual_out = root / 'reports/all_unmatched_20261107/worker-08'
    selection = root / '.temp/all-unmatched-worker-08/final-fragment-selection.json'
    run_id = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    stage = root / '.temp/all-unmatched-worker-08/inorganics/assembler-mechanics' / run_id
    pristine = stage / 'pristine'
    pristine.mkdir(parents=True)
    original_hashes = {str(assembler.relative_to(root)): digest(assembler)}
    if args.mode == 'synthetic':
        selected = build_synthetic(pristine)
    else:
        selected = read(selection)
        original_hashes[str(selection.relative_to(root))] = digest(selection)
        for relative in paths_for(selected):
            source = actual_out / relative
            target = pristine / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
            original_hashes[str(source.relative_to(root))] = digest(source)
    rows = [run_one(assembler, pristine, selected, stage, name, mutation)
            for name, mutation in CONTROLS]
    unchanged = all(digest(root / path) == expected for path, expected in original_hashes.items())
    report = dict(schema_version=1, reviewer='/root/inorganics',
                  scope='Assembler mechanics only; reviewer authored inorganic primary science.',
                  mode=args.mode, completed_at=datetime.now(timezone.utc).isoformat(),
                  harness_sha256=digest(__file__), assembler_sha256=digest(assembler),
                  original_inputs_sha256=original_hashes,
                  original_inputs_unchanged=unchanged,
                  selected_fragment_hashes={g['name']: g['reviewed_fragment_sha256']
                                            for g in selected['groups']},
                  selected_case_count=len(read(pristine / 'provenance/shard-08.json')['cases']),
                  private_fixture_path=str(stage.relative_to(root)), controls=rows,
                  passed=unchanged and all(row['passed'] for row in rows),
                  limitations=['Synthetic mode is only a harness control; final mode is required for real selection acceptance.',
                               'No scientific adequacy, primary-source validity, or reviewer receipt truth is established by these mechanics.',
                               'No maintained data, final fragments, final bundle outputs, or assembler source is modified.'])
    path = actual_out / f'validation/assembler-mechanics-{args.mode}.json'
    write(path, report)
    print(json.dumps(dict(mode=args.mode, controls=len(rows), passed=report['passed'],
                         original_inputs_unchanged=unchanged, log=str(path.relative_to(root)),
                         log_sha256=digest(path)), indent=2))
    if not report['passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
