"""Publish native receipt18 after replaying all prior links and exact bounded output."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import importlib.util
import json
import os
import sys

ROOT = Path.cwd().resolve()
RUN = Path(__file__).resolve().parent
assert ROOT == RUN / 'step4-mim'
PIN = Path(os.environ['CLAW_ROOT']).resolve()
folder = ROOT / 'reports/sssom_completion_20260921/mapping_changes'
script = folder / 'make_receipt.py'
assembler = folder.parent / 'assemble_review.py'
stage = ROOT / 'output/step4-receipt-stage'
batch = 'issue1005-lithium-glycerophosphate-identity'
before = RUN / 'step4-application/source-apply.before-ingredient_mappings.sssom.tsv'
apply_log = RUN / 'step4-application/source-apply.json'
current = ROOT / 'mappings/ingredient_mappings.sssom.tsv'
owner = ROOT / 'data/ingredients/mapped/Sn-Glycerol_3-phosphate_Lithium_Salt.yaml'
subject = 'MIM:Sn-Glycerol_3-phosphate_Lithium_Salt'
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--candidate', type=Path, required=True)
parser.add_argument('--promotion-log', type=Path, required=True)
args = parser.parse_args()
candidate = args.candidate.absolute()
promotion_log = args.promotion_log.absolute()
baseline_path = ROOT / 'mappings/other_cross_record_baseline.tsv'
audit_path = RUN / 'step4-application/receipt-publication.json'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def codes():
    paths = [Path(__file__), script, assembler]
    for directory in (ROOT / 'src', ROOT / 'scripts', PIN / 'src', PIN / 'plugins'):
        paths.extend(directory.rglob('*.py'))
    return {str(p): sha(p) for p in sorted(set(paths))}

code_before = codes()
from plugins.lock_manager import LockManager
from mediaingredientmech.ingredient_bundle_refresh import publish_new_files
assert codes() == code_before, 'code changed while loading runtime'

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

with LockManager({'my_id': 'codex-approved-plan'}).lock('mediaingredientmech', 'mapping_receipt_1005'):
    stage.mkdir(parents=True, exist_ok=False)
    existing = sorted(folder.glob('*.json'))
    receipts = sorted([json.loads(path.read_bytes()) for path in existing], key=lambda r: r['sequence'])
    assert [r['sequence'] for r in receipts] == list(range(1, 18))
    assert receipts[-1]['after_sha256'] == sha(before)
    replay_inputs = [folder.parent / name for name in ('baseline-mapping-review.json', 'trait-synonym-refresh.json', 'parent-name-refresh.json')]
    snapshot = {path: sha(path) for path in [*existing, *replay_inputs, before, apply_log, current, owner, RUN / 'approved-plan.txt']}
    snapshot.update({Path(path): value for path, value in code_before.items()})
    maker = load('native_step4_make_receipt', script)
    replay = load('native_step4_assembler', assembler)
    writer = load('native_step4_lithium_writer', ROOT / 'scripts/curate_lithium_glycerophosphate.py')
    assert codes() == code_before
    bound, source = writer.source_receipt(ROOT, apply_log, owner.read_bytes())
    snapshot.update({p: hashlib.sha256(data).hexdigest() for p, data in bound.items()})
    # Reuse the guarded writer's exact completed-promotion contract. A source
    # receipt alone does not bind the canonical row payload or baseline result.
    promotion_inputs = [candidate, promotion_log, baseline_path,
        writer.backups(promotion_log)[writer.SSSOM],
        writer.backups(promotion_log)[writer.BASELINE]]
    snapshot.update({p: sha(p) for p in promotion_inputs})
    completion = writer.promote(ROOT, candidate, apply_log, promotion_log,
        apply=False, candidate_sha256=snapshot[candidate])
    assert completion['changed'] is False and completion['applied'] is False, 'promotion is not complete'
    baseline, traits, parents = [json.loads(path.read_bytes()) for path in replay_inputs]
    assert traits['after_sha256'] == parents['before_sha256']
    refreshed = {r['source_position']: r['after'] for r in traits['changes']}
    for item in parents['changes']:
        if item['source_position'] in refreshed:
            assert refreshed[item['source_position']] == item['before']
        refreshed[item['source_position']] = item['after']
    _, _, reconstructed = replay.walk_mapping_changes(receipts,
        start_sha256=parents['after_sha256'], reviewed_sha256=sha(before),
        baseline_rows=baseline['rows'], refreshed_rows=refreshed)
    assert reconstructed == maker.rows_of(before.read_bytes()), 'prior17 links differ from actual preimage'
    maker.HERE = stage
    sys.argv = [str(script), '--batch', batch, '--sequence', '18', '--issue',
        'https://github.com/CultureBotAI/MediaIngredientMech/issues/1005', '--scope',
        'Approved distinct lithium-salt local identity, supplier-only free-acid CAS metadata, withdrawal of backfilled free-acid chemistry and false CAS identity row, and retirement of the generic alias; no scientific approval added.',
        '--before-sssom', str(before), '--apply-log', str(apply_log)]
    maker.main()
    generated = stage / (batch + '.json')
    generated_bytes = generated.read_bytes()
    receipt = json.loads(generated_bytes)
    snapshot[generated] = hashlib.sha256(generated_bytes).hexdigest()
    assert (receipt['changed_rows'], receipt['removed_rows'], receipt['added_rows']) == (2, 1, 0)
    assert receipt['touched_subjects'] == [subject]
    assert receipt['after_row_count'] == receipt['before_row_count'] - 1
    assert receipt['approval'].startswith('NONE:') and receipt['records'] == source['records']
    assert len(receipt['records']) == 1 and receipt['records'][0]['after_yaml_sha256'] == sha(owner)
    assert receipt['before_sha256'] == sha(before) and receipt['after_sha256'] == sha(current)
    _, _, final = replay.walk_mapping_changes([*receipts, receipt],
        start_sha256=parents['after_sha256'], reviewed_sha256=sha(current),
        baseline_rows=baseline['rows'], refreshed_rows=refreshed)
    assert final == maker.rows_of(current.read_bytes()), 'full18-link replay differs from current output'
    def others(path):
        return [line for line in path.read_bytes().splitlines(keepends=True)
            if not line.startswith((subject + '\t').encode())
            and not line.startswith((b'# mapping_date:', b'# mapping_set_version:'))]
    assert others(before) == others(current), 'unrelated SSSOM bytes changed'
    destination = folder / generated.name
    def recheck():
        assert codes() == code_before, 'code path set or bytes changed'
        assert snapshot == {p: sha(p) for p in snapshot}, 'receipt input bytes changed'
        assert set(folder.glob('*.json')) - {destination} == set(existing), 'receipt chain path set changed'
    audit = {'timestamp': datetime.now(timezone.utc).isoformat(), 'native_producer': str(script),
        'producer_sha256': sha(script), 'published': str(destination), 'receipt_sha256': hashlib.sha256(generated_bytes).hexdigest(),
        'previous_receipts_unchanged': {str(p): snapshot[p] for p in existing},
        'input_sha256': {str(p): value for p, value in snapshot.items()},
        'before_sha256': sha(before), 'after_sha256': sha(current), 'changed': 2, 'removed': 1, 'added': 0,
        'prior17_replay': 'PASS', 'full18_replay': 'PASS', 'other_sssom_bytes_identical': True,
        'scientific_approval_added': False}
    audit['promotion_receipt_sha256'] = snapshot[promotion_log]
    audit['candidate_sha256'] = snapshot[candidate]
    audit['completed_native_promotion'] = 'PASS; exact canonical, baseline, receipt and preimages'
    audit_bytes = (json.dumps(audit, indent=2) + '\n').encode()
    # Reserve both outputs before writing either; retain competing outputs.
    publish_new_files([(destination, generated_bytes), (audit_path, audit_bytes)], recheck)
    assert destination.read_bytes() == generated_bytes and audit_path.read_bytes() == audit_bytes
    print(json.dumps({k: v for k, v in audit.items() if k not in ('input_sha256', 'previous_receipts_unchanged')}, indent=2))
