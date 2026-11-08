"""Private actual-producer replay controls; no corpus/producer/provider writes."""
import copy
import json
import socket
from datetime import datetime, timezone
from pathlib import Path

from mediaingredientmech import campaign_publication as p
from mediaingredientmech.curate.campaign_owner_apply import inventory, hashes

ROOT = Path.cwd()
OUT = ROOT / '.temp/campaign-publication-native-controls-v4'
SOURCE = ROOT / '.temp/campaign-publication-native-smoke-v2'
ORIGINAL = json.loads((SOURCE / 'fixture-provenance.json').read_bytes())
T = ROOT.parents[3] / 'kgm-unmapped-20261107'
# This explicit path is a captured historical fixture, not the live canonical.
BEFORE_PATH = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/worktree/reports/kgm_unmapped_chemicals_20261107/sodium-acetate/publication/canonical-before.tsv')
BEFORE = BEFORE_PATH.read_bytes()
assert p.sha(BEFORE) == ORIGINAL['before_sha256']
INITIAL = hashes(inventory(ROOT))
NATIVE = json.loads((SOURCE / 'manifest.json').read_bytes())
INPUTS = {
    x['path']: p.sha(Path(x['path']).read_bytes())
    for x in NATIVE['source_inputs'] if x['sha256'] is not None
}
network_attempts = []

def no_network(*args, **kwargs):
    network_attempts.append(str(args[:1]))
    raise AssertionError('Network is forbidden in this replay')

socket.socket.connect = no_network
socket.create_connection = no_network
results = []

def run(name, mutation=None, expected=None):
    folder = OUT / name
    folder.mkdir()
    candidate = (SOURCE / 'candidate.tsv').read_bytes()
    sidecar = (SOURCE / 'sidecar.tsv').read_bytes()
    manifest = copy.deepcopy(NATIVE)
    if mutation:
        candidate, sidecar = mutation(manifest, candidate, sidecar)
    plan = copy.deepcopy(ORIGINAL['plan'])
    for role, filename, raw in [('candidate','candidate.tsv',candidate), ('sidecar','sidecar.tsv',sidecar)]:
        (folder / filename).write_bytes(raw)
        plan['generation'][role] = {'path': str((folder / filename).relative_to(ROOT)), 'sha256': p.sha(raw)}
    manifest['artifacts'] = [
        {'role': role, 'path': str(ROOT / plan['generation'][key]['path']), 'sha256': plan['generation'][key]['sha256']}
        for key, role in [('candidate','sssom'),('sidecar','suppressed_aliases')]]
    raw = p.encoded(manifest)
    (folder / 'manifest.json').write_bytes(raw)
    plan['generation']['manifest'] = {'path': str((folder / 'manifest.json').relative_to(ROOT)), 'sha256': p.sha(raw)}
    capture = p.Capture(ROOT)
    try:
        replayed = p._generation(capture, plan, BEFORE, INITIAL)
        capture.verify()
    except Exception as error:
        if expected is None or expected not in str(error):
            raise
        result = {'name': name, 'status': 'expected_refusal', 'error': str(error)}
    else:
        assert expected is None, name + ' unexpectedly accepted'
        result = {'name': name, 'status': 'PASS', 'native_rows': len(p.table(replayed[0])[2]), 'captured_inputs': len(capture.files), 'absent_inputs': len(capture.absent)}
    result['plan'] = plan
    (folder / 'result.json').write_bytes(p.encoded(result))
    results.append(result)

def change_manifest(fn):
    def mutate(m,c,s):
        fn(m)
        return c,s
    return mutate

run('positive')
run('unknown-field', change_manifest(lambda m: m.update(unrecognized=True)), 'fields')
run('missing-owner', change_manifest(lambda m: m['mapped_record_paths'].pop()), 'mapped membership differs')
run('missing-source', change_manifest(lambda m: m['source_inputs'].pop(next(i for i,x in enumerate(m['source_inputs']) if '/data/ingredients/mapped/' in x['path']))), 'omitted current owners')
run('stale-input', change_manifest(lambda m: m['source_inputs'][next(i for i,x in enumerate(m['source_inputs']) if '/data/ingredients/mapped/' in x['path'])].update(sha256='0'*64)), 'digest differs')
run('wrong-producer', change_manifest(lambda m: m['source_revisions'].update(claw='0'*40)), 'unreviewed producer revision')
run('wrong-kg-revision', change_manifest(lambda m: m['source_revisions'].update(kg_microbe='0'*40)), 'kg-microbe revision moved')
run('unknown-revision-field', change_manifest(lambda m: m['source_revisions'].update(unknown='0'*40)), 'fields')
run('missing-import', change_manifest(lambda m: m['producer_import_snapshot'].pop(next(iter(m['producer_import_snapshot'])))), 'producer graph differs')
run('wrong-stamp-source', change_manifest(lambda m: m.update(prior_stamp_sources=[])), 'unsupported stamp history')

def forged_cell(m,c,s):
    lines = c.decode().splitlines(keepends=True)
    header = next(i for i,l in enumerate(lines) if not l.startswith('#'))
    fields = lines[header].rstrip('\n').split('\t')
    row = lines[header+1].rstrip('\n').split('\t')
    row[fields.index('object_id')] = 'CHEBI:999999999'
    lines[header+1] = '\t'.join(row)+'\n'
    return ''.join(lines).encode(),s
run('forged-native-cell', forged_cell, 'native row replay differs')

def forged_sidecar(m,c,s):
    lines = s.decode().splitlines(keepends=True)
    fields = lines[0].rstrip('\n').split('\t')
    row = lines[1].rstrip('\n').split('\t')
    row[fields.index('owner_subject_ids')] = '["MIM:invented"]'
    lines[1] = '\t'.join(row)+'\n'
    return c,''.join(lines).encode()
run('forged-credit', forged_sidecar, 'native suppression replay differs')
assert not network_attempts
assert hashes(inventory(ROOT)) == INITIAL
assert {name: p.sha(Path(name).read_bytes()) for name in INPUTS} == INPUTS
report = {'status':'PASS', 'observed_at':datetime.now(timezone.utc).isoformat(), 'module_sha256':p.sha(Path(p.__file__).read_bytes()), 'runner_sha256':p.sha(Path(__file__).read_bytes()), 'fixture_provenance_sha256':p.sha((SOURCE/'fixture-provenance.json').read_bytes()), 'controls':len(results), 'expected_refusals':sum(x['status']=='expected_refusal' for x in results), 'results':results, 'source_inventory':INITIAL, 'input_sha256_before_and_after':INPUTS, 'network_attempts':network_attempts, 'production_publication':False, 'scientific_approval':False}
(OUT/'results.json').write_bytes(p.encoded(report))
print(json.dumps({k:report[k] for k in ('status','controls','expected_refusals','module_sha256','production_publication','scientific_approval')}))
