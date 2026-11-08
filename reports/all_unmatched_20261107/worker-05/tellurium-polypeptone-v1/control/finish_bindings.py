from pathlib import Path
from datetime import datetime, timezone
import json, hashlib

W = Path.cwd()
S = W / '.temp/w05-tellurium-polypeptone-v1'
P = W / 'reports/all_unmatched_20261107/worker-05/tellurium-polypeptone-v1'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
j = lambda p: json.loads(p.read_text())
binding = lambda p: dict(path=str(p.relative_to(W)), sha256=sha(p))
write = lambda p, obj: p.write_text(json.dumps(obj, indent=2) + '\n')
out = P / 'selected-origin-bindings.json'
assert not out.exists()
finding = S / 'final-assembly-review-v1/new-findings-v1.json'
assert j(finding)['findings'][0]['finding_id'] == 'W05-TELLURIUM-POLYPEPTONE-ASSEMBLY-001'
assembly = j(P / 'core/assembly-receipt.json')
authors = {'tellurium': '/root/chemicals_research', 'polypeptone': '/root/polypeptone_supplement'}
manifests = {'tellurium': P/'tellurium/FINAL-MANIFEST-v1.json', 'polypeptone': P/'polypeptone/MANIFEST.json'}
rows = []
for row in assembly['fragment_bindings']:
    assert sha(W / row['path']) == row['sha256']
    rows.append(dict(**row, author=authors[row['lane']], primary_manifest=binding(manifests[row['lane']])))
payloads = []
for row in assembly['proposal_reviews']:
    for version in ['before_capture', 'after_capture']:
        p = P.parent / row[version]['path']
        assert sha(p) == row[version]['sha256']
    payloads.append(row)
write(out, dict(
    at=datetime.now(timezone.utc).isoformat(), compiler='/root',
    finding_id='W05-TELLURIUM-POLYPEPTONE-ASSEMBLY-001',
    finding_reported_before_fix=binding(finding),
    preserved_source_ledger=binding(P/'source-ledger.json'),
    canonical_assembly=binding(P/'core/assembly-receipt.json'),
    selected_primary_fragments=rows, selected_payload_bindings=payloads,
    independent_review=binding(P/'review/main-review.json'),
    clarification='The preserved source-ledger primary_scopes.bindings is a historical file index, not the final selection rule. Its original Polypeptone decisions/proposals/evidence.json and Tellurium authoring-v1 entries remain historical. Only the six final fragments enumerated here are selected; Polypeptone decisions-v2/proposals-v2/evidence-v2 are authoritative. Existing canonical core and scientific selection were already correct. This append-only clarification changes no scientific objects, payloads, captures, timestamps, native review or source-ledger bytes.',
    scope='Report index clarification only; independent re-review required. No scientific approval or finding closure inferred.'
))
receipt = P/'validation/native-retained-review-check.json'
assert not receipt.exists()
stdout = P/'validation/native-retained-review-check.stdout.log'
stderr = P/'validation/native-retained-review-check.stderr.log'
result = j(stdout)
assert result['valid_reviews'] == 1024 and result['coverage'] == 'declared_scopes_only'
write(receipt, dict(
    observed_at=datetime.now(timezone.utc).isoformat(), exit_code=0,
    exit_observation='Completed tool exec session 6203, polled after context continuation; actual process returned exit_code 0.',
    command=['.temp/all-unmatched-worker-05/venv/bin/python', 'scripts/record_review.py', 'check', '--base', '76bca688b4f55e8bdf791079df8d4156cded6c4c', '--require-reviews'],
    environment={'PYTHONDONTWRITEBYTECODE':'1','PYTHONPATH':'src'},
    result=result, stdout=binding(stdout), stderr=binding(stderr),
    stderr_note='topClass deprecation warning only; no review validation error.',
    scope='Native persistence and declared review scopes only; does not approve owner integration or export.'
))
print(json.dumps({'selected_origin_bindings': binding(out), 'native_check': binding(receipt)}))
