"""Independent replay of root's controls, with all fixtures confined here.

The root assembler and native validators are imported read-only. Root's test
Path.cwd binding is redirected solely to prevent its fixed private fixture
path from writing outside this reviewer's authorized directory.
"""
import contextlib, copy, datetime, hashlib, importlib.util, io, json, pathlib, sys, unittest, yaml
ROOT=pathlib.Path.cwd()
S=ROOT/'reports/all_unmatched_20261107/worker-08/successors/issue-1227-v1'
O=S/'independent-review/final_assembly'
sys.path.insert(0,str(S/'scripts'))
import assemble, test_assemble, test_validation, check_identity_obligations as identity
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
class ConfinedPath:
    @staticmethod
    def cwd():return O
test_assemble.Path=ConfinedPath
stream=io.StringIO()
suite=unittest.TestSuite([unittest.defaultTestLoader.loadTestsFromModule(test_assemble),unittest.defaultTestLoader.loadTestsFromModule(test_validation)])
result=unittest.TextTestRunner(stream=stream,verbosity=2).run(suite)
assert result.wasSuccessful(),stream.getvalue()
native=identity.load_rules();native_checks=identity.controls(native)
fixture=O/'identity-fixture-v3';fixture.mkdir(exist_ok=True)
native.INGREDIENTS_DIR=fixture;native._subject_to_path.cache_clear()
record={'identifier':'NCIT:C87433','mapping_status':'MAPPED','ontology_mapping':{'ontology_id':'NCIT:C87433','mapping_quality':'CAS_RN_LOOKUP'}}
path=fixture/'Exact_Cas_Control.yaml';path.write_text(yaml.safe_dump(record))
subject='MIM:Exact_Cas_Control';rows=identity.projected_obligations(subject,record)
assert rows==[{'subject_id':subject,'object_id':'NCIT:C87433','predicate_id':'skos:exactMatch'}]
assert native.record_identifier(subject)=='NCIT:C87433'
assert not list(native.evaluate_rule_d(rows))
assert len(list(native.evaluate_rule_d([dict(rows[0],predicate_id='skos:closeMatch')])))==1
native_checks.append('Independent CAS_RN_LOOKUP own-ID fixture: exact identity positive, deliberately close own-ID negative')
conflict=[dict(subject_id='MIM:Same',object_id='kgmicrobe.ingredient:same',predicate_id='skos:exactMatch'),dict(subject_id='MIM:Same',object_id='kgmicrobe.compound:same',predicate_id='skos:exactMatch')]
assert len(list(native.evaluate_rule_b5(conflict)))==2
native_checks.append('Independent B5 rejects both conflicting ingredient/compound namespace rows')
before=identity.projected_obligations('MIM:Unmapped_Control',{'identifier':'UNMAPPED_1','mapping_status':'UNMAPPED'})
assert before==[]
native_checks.append('Unmapped proposal produces no asserted identity obligation')
checks=['assemble.py','validate_selection.py','prepare_native.py','build_native_review.py','check_identity_obligations.py','build_dispositions.py','build_new_dispositions.py','test_assemble.py','test_validation.py']
report={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':'/root/inorganics','author':'/root','scope':'Independent mechanical controls and helper-source review only. No independent scientific approval of this reviewer\'s inorganic payloads; those require vitamins peer bindings.','status':'PASS','unittest_count':result.testsRun,'unittest_failures':len(result.failures),'unittest_errors':len(result.errors),'native_controls':native_checks,'input_hashes':{str((S/'scripts'/n).relative_to(ROOT)):sha(S/'scripts'/n) for n in checks},'native_dependency_hashes':{n:sha(ROOT/n) for n in ['MAPPING_SEMANTICS.md','scripts/validate_sssom_invariants.py','src/mediaingredientmech/sssom_grading.py']},'write_boundary':str(O.relative_to(ROOT)),'limitation':'Positive/negative controls do not validate the yet-unassembled final selection or final native pair. Exact final-input review remains pending. No maintained SSSOM/export is built or validated.'}
(O/'controls-v3.stdout').write_text(stream.getvalue())
(O/'controls-v3.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['input_hashes','native_dependency_hashes']}))
