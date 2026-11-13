"""2026-11-12: own current seven-CAS skeptical factual audit and native inspect.

Inputs: actual S3 claims, completed endpoint, seven full rows/current owners and
captured primary/negative evidence. Outputs: own private facts and native input
inspection receipts. No source edits, science vote, tests, generation or replay.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import io
import json
import os
import re
import subprocess
import yaml

D = Path(__file__).resolve().parent
R = D.parents[1]
C = R.parents[1]
PY = C / 'integration/stable-campaign-adoption-worktree/.venv/bin/python3'
P = R / '.temp/seven-cas-dispositions-claims-s3-v1'
HEAD = 'f4b6712d9b8a888c03389149283ee2b7d124bf13'
now = lambda: datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
sha = lambda b: hashlib.sha256(b).hexdigest()
pins = {}
started = now()


def read(name, expected=None):
    name = str(name)
    p = Path(name)
    assert not p.is_absolute() and '..' not in p.parts
    path = R / p
    assert path.resolve() == path
    raw = path.read_bytes()
    pin = sha(raw)
    assert expected is None or pin == expected, name
    assert name not in pins or pins[name] == pin, name
    pins[name] = pin
    return raw


def doc(name, expected=None):
    return json.loads(read(name, expected))


def ref(item):
    return doc(item['path'], item['sha256'])


def save(name, value):
    with (D / name).open('x') as f:
        json.dump(value, f, indent=2, ensure_ascii=False)
        f.write('\n')


def git(*args):
    return subprocess.check_output(['git', '--no-optional-locks', *args], cwd=R, timeout=30)


assert Path.cwd() == R and git('rev-parse', 'HEAD').decode().strip() == HEAD
claims_name = str((P / 'CLAIMS.json').relative_to(R))
claims = doc(claims_name, 'e9d7d989ce3329dc72a627d2f58793d024908f85e70da5780d92c8287bebb7e5')
targets_name = str((P / 'TARGETS.json').relative_to(R))
targets = doc(targets_name, '15537a58cb2d257ae9d957647fb5931ecf04368d33ba2dfaed6407a8a2da51cd')['targets']
required = doc(str((P / 'REQUIRED-REVIEW-INPUTS.json').relative_to(R)), '06dccb695ce4da4dd387c006995bbe7ce177b76a63b26a9bfc3f0bfe4eddda46')
for name, pin in required.items():
    read(name, pin)
hc = '.temp/seven-cas-current-hold-context-v1/'
hold_inputs = doc(hc + 'REVIEW-INPUTS.json', 'b90cde1ff8320d41063b36b1870fda147fd7b07d06d3a0ef43198b0eeb2aba8a')
for name, pin in hold_inputs.items():
    read(name, pin)
hold_copy = doc(hc + 'COPY-RECEIPT.json', '23bc856070b1c7cd325af21a498a4e95020a619baa673f364a9cb511cc01453b')
assert len(hold_copy['copied_files']) == len(hold_inputs) == 42
for item in hold_copy['copied_files']:
    assert item['embedded_references_rewritten'] is False
    assert item['source_sha256'] == item['sha256'] == pins[item['destination']]
    assert len(read(item['destination'])) == item['bytes']
for name in ['AGENTS.md', '.claude/skills/map-media-ingredients/SKILL.md', '.claude/skills/review-sssom-output/SKILL.md', 'docs/record-reviews.md', 'docs/record-review-profile.md', 'docs/REVIEWED_INVALID_CAS_DIAGNOSTICS.md', 'src/mediaingredientmech/curate/stable_sssom_publication.py']:
    read(name)
endpoint = ref(claims['source_correction'])
manifest = ref(endpoint['manifest'])
application = ref(endpoint['receipt'])
request = ref(manifest['request'])
operations = {o['mim_id']: o for o in request['operations']}
assert len(operations) == len(request['operations']) == 14
assert application['state'] == 'COMPLETE' and application['recovery_required'] is False
assert application['release_approval_added'] is False and application['root'] == str(R)
assert application['outputs'] == manifest['outputs']
vd = '.temp/cumulative-source-successor-committed-verification-s3-v1/'
verification = doc(vd + 'stdout.json', '626fae555154ee950330cd85d52e93cc387e68505907340c060220dc5089feb3')
terminal = doc(vd + 'RESULT.json', 'df43dc405dc9afcb48dfc420d2ba860d0bdc775835fe757445a363489473dd0d')
vcopy = doc(vd + 'COPY-RECEIPT.json', '6453ded792ee455683a1a8b9922fce514810b3a7bdca71ea45658be0edbe6712')
assert terminal['native_exit_code'] == terminal['exit_code'] == 0
assert terminal['stdout_sha256'] == pins[vd + 'stdout.json']
assert verification['status'] == 'COMPLETE_CURRENT_SOURCE_SUCCESSOR'
assert verification['current_identity']['head'] == HEAD and verification['root'] == str(R)
assert verification['manifest_sha256'] == sha(json.dumps(manifest, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode())
assert vcopy['source_process_owner'] == vcopy['copier'] == '/root'
canonical = read(claims['canonical']['path'], claims['canonical']['sha256'])
rows = list(csv.DictReader(io.StringIO(''.join(s for s in canonical.decode().splitlines(keepends=True) if not s.startswith('#'))), delimiter='\t'))
history_name = next(n for n, h in claims['evidence_inputs'].items() if h == '36bd9830ae9fdfdf9b03346df11f4d9360e3595ed1049c4ace3f43623dc6e622')
history = {e['mim_id']: e for e in doc(history_name)['entries']}
hold_context = {e['mim_id']: e for e in doc(hc + 'live/HOLD-CONTEXT-ASSESSMENT.json')['entries']}
assert claims['head'] == HEAD and claims['scope'] == 'diagnostic_candidate_only' and claims['scientific_approval'] is False
assert len(claims['entries']) == len(targets) == 7
facts = []
for e, t in zip(claims['entries'], targets, strict=True):
    mid = e['owner']['mim_id']
    raw = read(e['owner']['path'], e['owner']['sha256'])
    owner = yaml.safe_load(raw)
    assert owner['mim_id'] == mid and git('show', HEAD + ':' + e['owner']['path']) == raw
    assert e['row'] == rows[e['row_position'] - 1] == history[mid]['row'] == hold_context[mid]['frozen_row']
    assert history[mid]['inherited_decision']['disposition'] == hold_context[mid]['inherited_disposition'] == 'WITHHOLD'
    assert t['selector'] == e['entry_id'] and t['path'] == claims_name
    assert t['semantic_digest']['sha256'] == sha(json.dumps(e, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode())
    invalid, arithmetic = [], []
    for field in ['object_id', 'other', 'xref']:
        for token in e['row'].get(field, '').split('|'):
            if not token.strip().casefold().startswith('cas:'):
                continue
            rn = token.strip()[4:]
            assert re.fullmatch('[1-9][0-9]{1,6}-[0-9]{2}-[0-9]', rn)
            digits = rn.replace('-', '')
            weighted = sum(i * int(d) for i, d in enumerate(reversed(digits[:-1]), 1))
            arithmetic.append({'field': field, 'token': token, 'weighted_sum': weighted, 'expected_digit': weighted % 10, 'stored_digit': int(digits[-1])})
            if weighted % 10 != int(digits[-1]):
                invalid.append({'field': field, 'token': token})
    assert invalid == e['invalid_tokens'] and invalid
    if mid in {'MIM:0000862', 'MIM:0002227'}:
        assert e['action'] == 'RETIRE_INVALID_CAS' and e['hold'] is None
        op = operations[mid]
        assert op['after_path'] == e['owner']['path'] and manifest['outputs'][op['after_path']] == sha(raw)
        proposal_raw = read(op['proposal']['path'], op['proposal']['sha256'])
        assert yaml.safe_load(proposal_raw) == owner
        bad = e['row']['object_id']
        assert bad in op['rejected_identifiers']
        active = [owner['identifier'], owner['ontology_mapping']['ontology_id'], *owner['legacy_identifiers']]
        assert bad.casefold() not in {v.casefold() for v in active}
        assert owner['chemical_properties']['cas_rn'] != bad[4:]
        before_ref = application['beforeimages'][op['before']['path']]
        before = yaml.safe_load(read(before_ref['path'], before_ref['sha256']))
        assert before['mim_id'] == owner['mim_id']
        assert before['curation_history'] == owner['curation_history'][:len(before['curation_history'])]
        assert op['inherited_holds'] == op['residual_holds']
        for role in ['primary', 'skeptic']:
            rr = op[role]
            read(rr['path'], rr['sha256'])
            read(str(Path(rr['path']).with_name('review.md')), rr['markdown_sha256'])
    else:
        assert e['action'] == 'RETAIN_INVALID_CAS_WITHHOLD' and mid not in operations
        assert manifest['before_inventory'][e['owner']['path']] == manifest['after_inventory'][e['owner']['path']] == e['owner']['sha256'] == history[mid]['owner']['sha256']
        assert e['hold']['issue'].endswith('/753' if mid == 'MIM:0001639' else '/887')
    facts.append({'mim_id': mid, 'entry_id': e['entry_id'], 'row_position': e['row_position'], 'action': e['action'], 'full_historical_row_equal': True, 'current_committed_owner_equal': True, 'permanent_id_preserved': True, 'inherited_scientific_hold': 'WITHHOLD', 'arithmetic': arithmetic, 'owner_sha256': sha(raw)})
save('FACTS.json', {'at': now(), 'head': HEAD, 'scope': 'DETERMINISTIC_CURRENT_FACTS_NOT_SCIENTIFIC_APPROVAL', 'entries': facts, 'canonical_rows': len(rows), 'invalid_tokens': sum(len(f['arithmetic']) for f in facts), 'required_input_count': len(required), 'hold_context_files': len(hold_inputs), 'source_phase_rerun': False})
read(str((D / 'FACTS.json').relative_to(R)))
read(str(Path(__file__).relative_to(R)))
save('INPUT-PINS.json', {'at': now(), 'head': HEAD, 'inputs': pins})
argv = [str(PY), '-B', 'scripts/record_review.py', 'inspect', '--targets', targets_name]
for name in sorted(pins):
    argv.extend(['--input', name])
env = {**os.environ, 'PYTHONPATH': str(R / 'src'), 'PYTHONDONTWRITEBYTECODE': '1'}
save('INSPECT-COMMAND.json', {'at': started, 'argv': argv, 'cwd': str(R), 'owner': '/root/s3_completed_source_audit', 'environment_overlay': {'PYTHONPATH': str(R / 'src'), 'PYTHONDONTWRITEBYTECODE': '1'}})
cp = subprocess.run(argv, cwd=R, env=env, capture_output=True, timeout=120)
for name, raw in [('INSPECT.stdout.json', cp.stdout), ('INSPECT.stderr.txt', cp.stderr)]:
    with (D / name).open('xb') as handle:
        handle.write(raw)
for name, pin in pins.items():
    assert sha((R / name).read_bytes()) == pin
assert git('rev-parse', 'HEAD').decode().strip() == HEAD
save('INSPECT-RESULT.json', {'started_at': started, 'finished_at': now(), 'exit_code': cp.returncode, 'stdout_sha256': sha(cp.stdout), 'stderr_sha256': sha(cp.stderr), 'head': HEAD, 'inputs': len(pins)})
print(json.dumps({'result': str(D / 'INSPECT-RESULT.json'), 'sha256': sha((D / 'INSPECT-RESULT.json').read_bytes()), 'exit_code': cp.returncode, 'inputs': len(pins), 'entries': len(facts)}))
if cp.returncode:
    print(cp.stderr.decode())
raise SystemExit(cp.returncode)
