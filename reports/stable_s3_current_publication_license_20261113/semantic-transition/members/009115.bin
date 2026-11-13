import pathlib,json,hashlib,importlib.util,datetime
R=pathlib.Path.cwd();O=R/'.temp/gyps-native-origin-v1';T=O/'technical-review';p=O/'scripts/verify_representation_v1.py'
spec=importlib.util.spec_from_file_location('actual_private_representation_guard',p);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
positive=mod.verify(json.loads((O/'proposals.json').read_bytes()))
bad=json.loads((T/'false-assignment-fixture-v1/intake/proposals.json').read_bytes())
try:mod.verify(bad)
except ValueError as e:rejection=str(e)
else:raise AssertionError('actual privateguard acceptedfalseassignment')
report={'reviewer':'/root/gyps_native_technical','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'root_guard_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'actual_ledger_sha256':hashlib.sha256((O/'proposals.json').read_bytes()).hexdigest(),'positive_actual_guard':positive,'exact_counterfactual_ledger_sha256':hashlib.sha256((T/'false-assignment-fixture-v1/intake/proposals.json').read_bytes()).hexdigest(),'native_and_crosswalk_counterfactual_result':'PASS_STRUCTURAL_ONLY','private_semantic_result':'REFUSED','private_semantic_message':rejection,'interpretation':'The same exact private counterfeitledger passes nativeglobalhash binding and is refused by the actual task-specific semanticguard. Do not reportthis as native refusal or change nativegates.','actual_inputs_changed':False}
q=T/'actual-private-guard-boundary-v1.json';q.write_text(json.dumps(report,indent=2)+'\n');print(hashlib.sha256(q.read_bytes()).hexdigest())
