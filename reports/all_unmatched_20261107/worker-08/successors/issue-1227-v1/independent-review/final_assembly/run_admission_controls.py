"""Independently exercise exact failed-admission handling, with no corpus edits."""
import copy, datetime, hashlib, io, json, pathlib, sys, unittest
ROOT=pathlib.Path.cwd()
S=ROOT/'reports/all_unmatched_20261107/worker-08/successors/issue-1227-v1'
O=S/'independent-review/final_assembly'
sys.path.insert(0,str(S/'scripts'))
import test_validation as tests
import validate_selection as v
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
stream=io.StringIO()
result=unittest.TextTestRunner(stream=stream,verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(tests.AdmissionFailureControls))
assert result.wasSuccessful(),stream.getvalue()
review=json.loads((O/'trypticase-admission-review-v1.json').read_text())
p=review['exact_selected_proposal']; prior=review['predecessor_proposal']
hashes={k:x['current_sha256'] for k,x in review['baseline_owner_checks'].items()}
failure=('changed identity collides','MICRO:0000113',['data/ingredients/mapped/Bacto_Tryptic_Soy_Broth.yaml'])
additional=[]
for name,badreview,badfailure in [
 ('A passed admission cannot be imported',dict(review,maintained_admission='PASS'),failure),
 ('A different colliding identifier cannot be imported',review,('changed identity collides','MICRO:other',failure[2]))]:
 try:v.record_reviewed_admission_failure(p,prior,hashes,badreview,badfailure)
 except AssertionError:additional.append({'control':name,'passed':True})
 else:raise AssertionError(name)
catalog={failure[2][0]:{'identifier':'MICRO:0000113','mapping_status':'MAPPED'}}
try:v.disallow_active_collision(catalog,p['owner_path'],'MICRO:0000113')
except AssertionError as error:
 assert error.args[0]==failure
 additional.append({'control':'Original collision gate still rejects the exact reviewed collision','passed':True})
else:raise AssertionError('collision gate was relaxed')
r={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':'/root/inorganics','author':'/root','status':'PASS','root_unit_controls':result.testsRun,'root_unit_failures':len(result.failures),'root_unit_errors':len(result.errors),'additional_controls':additional,'input_hashes':{str(p.relative_to(ROOT)):sha(p) for p in [S/'scripts/validate_selection.py',S/'scripts/test_validation.py',O/'trypticase-admission-review-v1.json']},'scope':'Exact failed/HELD admission recording only. No winner, new identity, maintained mutation or admission approval.'}
for name,content in [('admission-controls.stdout',stream.getvalue()),('admission-controls.json',json.dumps(r,indent=2)+'\n')]:
 path=O/name
 assert not path.exists()
 path.write_text(content)
print(json.dumps(r))
