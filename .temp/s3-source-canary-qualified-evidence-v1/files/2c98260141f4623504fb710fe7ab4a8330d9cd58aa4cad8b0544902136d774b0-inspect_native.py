"""2026-11-12: native primary-review input inspection for four actual source cases.

Reads exact request/inspection/evidence pins; invokes the unchanged repository
record_review.main inspect entrypoint in-process to avoid OS argument-size limits.
Only this unique private directory receives receipts. This authors no science vote.
"""
from pathlib import Path
from datetime import datetime, timezone
import contextlib
import hashlib
import io
import json
import os
import runpy
import sys

HERE = Path(__file__).absolute().parent
TC = HERE.parents[1]
C = TC.parents[1]
PY = C / 'integration/stable-campaign-adoption-worktree/.venv/bin/python3'
REQ = TC / '.temp/real-canary-source-binding-request-v1'
sha = lambda b: hashlib.sha256(b).hexdigest()
stamp = lambda: datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')


def write(name, value):
    with (HERE / name).open('x') as f:
        json.dump(value, f, ensure_ascii=False, indent=2)
        f.write('\n')


def main():
    assert sys.executable == str(PY) and sys.version_info[:2] == (3, 13)
    assert os.environ['PYTHONPATH'] == str(TC / 'src')
    started = stamp()
    expected = {
        'REQUEST.json': 'b6c76f85aea1ab4bd6585b202fb2d69dc3016c7561272fa0ed252c85892938f8',
        'TARGETS.json': 'ad146736026fa40c98d3f7fd5d6a9a0b9c485adf6297a674c11287137fb13d62',
        'PAYLOADS.json': '0556b24df914dd84b4ed47164cca44e18c0b4cf9c9177c1e85ca3d987a1c79b8',
        'INSPECTION.json': 'dc7c987cb4d632caa4157f08d4b1d5afa49898c8130ac1eeab7a85eb73b2aa29',
        'REVIEW-INPUTS.json': '261ec0b51124ae6c5696b8596625f903974d43fd6854d568e8ea18fa8b9852b4',
    }
    refs = json.loads((REQ / 'REVIEW-INPUTS.json').read_bytes())
    union = dict(refs['native_returned_inputs'])
    for name, digest in refs['supplemental_inputs_required_when_used'].items():
        assert name not in union or union[name] == digest
        union[name] = digest
    for name, digest in expected.items():
        union[str((REQ / name).relative_to(TC))] = digest
    for name in [
        'schema/record_review.yaml', 'scripts/record_review.py',
        'conf/record_review.yaml', 'src/mediaingredientmech/export/source_bindings.py',
        'src/mediaingredientmech/stable_ids.py',
        str(Path(__file__).relative_to(TC)),
    ]:
        union[name] = sha((TC / name).read_bytes())
    for name, digest in union.items():
        assert sha((TC / name).read_bytes()) == digest, name
    write('INPUTS.json', dict(sorted(union.items())))
    args = ['--repo-root', str(TC), '--schema', str(TC / 'schema/record_review.yaml'),
            'inspect', '--targets', str(REQ / 'TARGETS.json')]
    for name in sorted(union):
        args.extend(['--input', name])
    args.extend(['--input', str((HERE / 'INPUTS.json').relative_to(TC))])
    write('INSPECT-COMMAND.json', {
        'started_at': started, 'runtime': str(PY), 'cwd': str(TC),
        'PYTHONPATH': os.environ['PYTHONPATH'],
        'entrypoint': 'scripts/record_review.py:main', 'argv': args,
        'reason_for_in_process_native_cli': 'Exact native CLI with more than 3000 input paths; no alternate inspector or safety override.',
        'prior_setup_failure': {'tool_chunk': 'cadab3', 'exit_code': 1,
            'detail': 'Read-only input-list setup guessed curate/stable_ids.py; no native invocation occurred. Ignored-inclusive file discovery b46bfa resolved src/mediaingredientmech/stable_ids.py.'},
    })
    module = runpy.run_path(str(TC / 'scripts/record_review.py'), run_name='native_source_primary_review_inspect')
    output = io.StringIO()
    err = io.StringIO()
    with contextlib.redirect_stdout(output), contextlib.redirect_stderr(err):
        code = module['main'](args)
    with (HERE / 'inspection.json').open('x') as f:
        f.write(output.getvalue())
    with (HERE / 'inspection.stderr').open('x') as f:
        f.write(err.getvalue())
    write('INSPECT-RESULT.json', {'started_at': started, 'finished_at': stamp(),
        'exit_code': code, 'stdout_sha256': sha(output.getvalue().encode()),
        'stderr_sha256': sha(err.getvalue().encode()), 'stderr': err.getvalue()})
    assert code == 0, err.getvalue()
    result = json.loads(output.getvalue())
    assert result['source']['git_revision'] == '6677f1e1679bec82f5af5e125454d4b7852780e9'
    assert result['targets'] == json.loads((REQ / 'TARGETS.json').read_bytes())['targets']
    print(json.dumps({'status': 'NATIVE_INSPECT_COMPLETED_NOT_A_SCIENTIFIC_VOTE',
        'input_count': len(result['source']['inputs']), 'targets': len(result['targets']),
        'inspection_sha256': sha(output.getvalue().encode()), 'exit_code': code}))


if __name__ == '__main__':
    main()
