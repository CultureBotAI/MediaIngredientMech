"""Rebuild unified output, prove no change, then guarded-publish its native provenance."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import importlib.util
import io
import json
import os
import subprocess
import sys

RUN = Path(__file__).resolve().parent
if len(sys.argv) != 4:
    raise SystemExit('usage: guarded_unified_lithium.py MIM_CHILD CLAW_CHILD NEW_EVIDENCE_CHILD')
step, producer, evidence_name = sys.argv[1:]
for name in (step, producer, evidence_name):
    if Path(name).name != name or name in ('.', '..'):
        raise SystemExit('locations must be named children of this run')
MIM = RUN / step
CLAW = RUN / producer
PIN = Path(os.environ['CLAW_ROOT']).resolve()
CULTURE = Path(os.environ['CULTUREMECH_ROOT']).resolve()
assert Path(os.environ['MEDIAINGREDIENTMECH_ROOT']).resolve() == MIM.resolve()
assert MIM.name == 'step4-mim'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def code_snapshot():
    paths = [Path(__file__), RUN / 'approved-plan.txt']
    for directory in (MIM / 'scripts', MIM / 'src', CLAW / 'scripts', CLAW / 'src', CLAW / 'plugins', PIN / 'src', PIN / 'plugins'):
        paths.extend(directory.rglob('*.py'))
    return {str(p): sha(p) for p in sorted(set(paths))}

# Bind repository code before imports, including the actual pinned runtime.
code_before = code_snapshot()
from plugins.repository_settings import RepositorySettings
from plugins.lock_manager import LockManager
assert code_snapshot() == code_before, 'runtime code changed while importing'
settings = RepositorySettings.from_environment()
assert settings.get_target('mediaingredientmech').path == MIM.resolve()
assert settings.get_target('culturemech').path == CULTURE
if subprocess.check_output(['git', 'status', '--porcelain', '--untracked-files=all'], cwd=CLAW, text=True).strip():
    raise SystemExit('producer must be a clean isolated checkout')
evidence = RUN / evidence_name
evidence.mkdir(exist_ok=False)
candidate = evidence / 'unified-candidate.tsv'
canonical = MIM / 'UNIFIED_INGREDIENT_MAPPING.tsv'
provenance = MIM / 'UNIFIED_INGREDIENT_MAPPING.provenance.json'
staged_provenance = evidence / 'unified-provenance-candidate.json'

def inputs():
    paths = list((CULTURE / 'data/normalized_yaml').rglob('*.yaml'))
    for category in ('mapped', 'unmapped'):
        paths.extend((MIM / 'data/ingredients' / category).glob('*.yaml'))
    paths.extend([MIM / 'docs/data/label_index.csv', MIM / 'mappings/unified_mapping_rejections.tsv'])
    return code_snapshot() | {str(p): sha(p) for p in sorted(set(paths))}

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

with LockManager({'my_id': 'codex-approved-plan'}).lock('mediaingredientmech', 'approved_unified_rebuild'):
    before = canonical.read_bytes()
    before_provenance = provenance.read_bytes()
    snapshot = inputs()
    assert code_snapshot() == code_before, 'runtime code changed before execution'
    publisher_path = MIM / 'scripts/promote_heptahydrate_ncit.py'
    publisher = load('approved_step4_unified_publisher', publisher_path)
    stamper = load('approved_step4_unified_stamper', MIM / 'scripts/check_unified_freshness.py')
    assert inputs() == snapshot, 'inputs changed during imports'
    subprocess.run([sys.executable, str(CLAW / 'scripts/build_unified_ingredient_mapping.py'), '--culturemech', str(CULTURE), '--mim', str(MIM), '--output', str(candidate), '--format', 'tsv'], check=True, cwd=MIM)
    proposed = candidate.read_bytes()
    subprocess.run([sys.executable, str(MIM / 'scripts/check_unified_rejections.py'), '--artifact', str(candidate)], check=True, cwd=MIM)
    assert candidate.read_bytes() == proposed, 'candidate changed during validation'
    assert proposed == before, 'Step4 must not change any unified bytes'
    rows = list(csv.DictReader(io.StringIO(proposed.decode(), newline=''), delimiter='\t'))
    assert len({row['ingredient_name'] for row in rows}) == len(rows)
    assert not [r for r in rows if r['mapping_status'] == 'REJECTED' and not r['mim_id']]
    assert not [r for r in rows if r['mim_id'].startswith('kgmicrobe.compound:') and any(r[c].startswith('CHEBI:') for c in ('culturemech_term_id', 'chebi_id', 'kg_microbe_node_id'))]
    assert inputs() == snapshot and canonical.read_bytes() == before
    # The unchanged canonical is byte-identical to the newly built, checked output.
    # Render provenance with the maintained native producer, to a new staging path.
    stamp = stamper.stamp(canonical, staged_provenance, MIM / 'data/ingredients')
    stamped_bytes = staged_provenance.read_bytes()
    assert json.loads(stamped_bytes) == stamp
    assert stamp['artifact_sha256'] == hashlib.sha256(proposed).hexdigest()
    assert stamp['artifact_rows'] == len(rows)
    assert (stamp['mim_inputs_digest'], stamp['mim_record_count']) == stamper.inputs_digest(MIM / 'data/ingredients')
    captured = {Path(path): Path(path).read_bytes() for path in snapshot}
    assert all(hashlib.sha256(data).hexdigest() == snapshot[str(path)] for path, data in captured.items())
    captured.update({canonical: before, provenance: before_provenance, candidate: proposed, staged_provenance: stamped_bytes})
    receipt = {
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'operation': 'native_unified_zero_change_rebuild_with_guarded_provenance_publication',
        'before_sha256': hashlib.sha256(before).hexdigest(),
        'after_sha256': hashlib.sha256(proposed).hexdigest(),
        'canonical_bytes_unchanged': True, 'canonical_written': False,
        'bounded_changed_rows': [], 'input_sha256': snapshot,
        'native_publisher_sha256': sha(publisher_path),
        'provenance_before_sha256': hashlib.sha256(before_provenance).hexdigest(),
        'provenance_after_sha256': hashlib.sha256(stamped_bytes).hexdigest(),
        'rows': len(rows), 'occurrences': sum(int(r['occurrence_count']) for r in rows),
        'rejected_empty_identity': 0, 'local_compound_chebi_leaks': 0,
        'scientific_approval_added': False,
        'mim_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=MIM, text=True).strip(),
        'claw_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=CLAW, text=True).strip(),
        'runtime_claw_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=PIN, text=True).strip(),
        'culturemech_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=CULTURE, text=True).strip(),
    }
    def recheck():
        assert inputs() == snapshot, 'input paths or bytes changed before publication'
    result = publisher.publish(MIM, {provenance.relative_to(MIM): stamped_bytes}, captured,
        evidence / 'unified-generation-receipt.json',
        {evidence / 'unified-before.tsv': before, evidence / 'unified-provenance-before.json': before_provenance},
        receipt, apply=True, validate_scope=recheck)
    assert canonical.read_bytes() == before and provenance.read_bytes() == stamped_bytes
    print(json.dumps({k: v for k, v in result.items() if k != 'input_sha256'}, indent=2))
