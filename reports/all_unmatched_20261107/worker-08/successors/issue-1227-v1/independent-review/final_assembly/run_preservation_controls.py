"""Replay the new preservation controls without author or corpus mutations."""
import datetime, hashlib, io, json, pathlib, sys, unittest
ROOT = pathlib.Path.cwd()
S = ROOT / 'reports/all_unmatched_20261107/worker-08/successors/issue-1227-v1'
O = S / 'independent-review/final_assembly'
sys.path.insert(0, str(S / 'scripts'))
import test_validation
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
stream = io.StringIO()
suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_validation.PreservationReceiptControls)
result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
report = dict(at=datetime.datetime.now(datetime.timezone.utc).isoformat(), reviewer='/root/inorganics',
    author='/root', status='PASS' if result.wasSuccessful() else 'FAIL', tests=result.testsRun,
    failures=len(result.failures), errors=len(result.errors),
    scope='Four added preservation controls only: complete scope positive, omitted supplement, hidden nested failure and incomplete original scope negatives. Earlier control receipts remain unchanged.',
    input_hashes={str(p.relative_to(ROOT)): sha(p) for p in [S/'scripts/test_validation.py', S/'scripts/validate_selection.py']})
for name, content in [('preservation-controls-v2.stdout', stream.getvalue()), ('preservation-controls-v2.json', json.dumps(report, indent=2)+'\n')]:
    path=O/name
    assert not path.exists()
    path.write_text(content)
assert result.wasSuccessful(), stream.getvalue()
print(json.dumps(report))
