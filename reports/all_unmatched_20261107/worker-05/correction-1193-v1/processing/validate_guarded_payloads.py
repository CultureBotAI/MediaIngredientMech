"""Replay exact isolated candidates through the native guarded writer, never to maintained paths."""
from pathlib import Path
import datetime, hashlib, json, sys, uuid
import yaml
R = Path.cwd()
B = R / 'reports/all_unmatched_20261107/worker-05'
N = B / 'correction-1193-v1'
sys.path.insert(0, str(R / 'src'))
from mediaingredientmech.validation.write_validated import write_validated_ingredient
manifest = N / 'proposals.json'
manifest_bytes = manifest.read_bytes()
manifest_hash = hashlib.sha256(manifest_bytes).hexdigest()
P = json.loads(manifest_bytes)['proposals']
run = R / '.temp/all-unmatched-worker-05/correction-1193-v1/guarded-replays' / str(uuid.uuid4())
rows = []
for p in P:
    source = B / p['after_capture']['path']
    source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    assert source_hash == p['after_capture']['sha256'], p['proposal_id']
    record = yaml.safe_load(source.read_text())
    destination = run / (hashlib.sha256(p['proposal_id'].encode()).hexdigest() + '.yaml')
    write_validated_ingredient(record, destination, target_class='IngredientRecord')
    assert yaml.safe_load(destination.read_text()) == record, p['proposal_id']
    assert hashlib.sha256(source.read_bytes()).hexdigest() == source_hash
    rows.append({'proposal_id': p['proposal_id'], 'source_capture': p['after_capture'],
                 'guarded_output': str(destination.relative_to(R)),
                 'guarded_output_sha256': hashlib.sha256(destination.read_bytes()).hexdigest(),
                 'logical_roundtrip_equal': True})
assert manifest.read_bytes() == manifest_bytes, 'Proposal manifest changed during guarded replay'
receipt = {'status': 'PASS', 'checked_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'proposal_manifest_sha256': manifest_hash,
           'proposal_count': len(P), 'rows': rows,
           'limitations': 'Exact reviewed source bytes are unchanged. Native guarded writer outputs are private validation fixtures only; no maintained writes or scientific/release approval.'}
(N / 'validation/guarded-writer.json').write_text(json.dumps(receipt, indent=2) + '\n')
print('PASS', len(P), 'exact candidates through native guarded writer and logical YAML roundtrip')
