"""Independent refusal controls; fixtures remain in this technical directory."""
from pathlib import Path
import copy,hashlib,importlib.util,json,unittest,datetime
import yaml
R=Path.cwd();OUT=R/'.temp/w03-provenance-successor-v1/technical';FILE=R/'.temp/w03-provenance-successor-v1/provenance_writer.py'
spec=importlib.util.spec_from_file_location('w03_provenance_writer_v1_under_test',FILE);W=importlib.util.module_from_spec(spec);spec.loader.exec_module(W)
STAMP=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ');FIX=OUT/('fixtures-v1-'+STAMP);FIX.mkdir()
BASE=W.Repair();NEW=next(k for k,v in BASE.rows.items() if v['proposal_kind']=='new_owner');EDIT=next(k for k,v in BASE.rows.items() if v['proposal_kind']=='edit_existing_owner')
def data(pid=NEW):
 row=copy.deepcopy(BASE.rows[pid]);pr=copy.deepcopy(BASE.proposals[pid]);raw=(R/row['published_payload_path']).read_bytes();before=(R/row['authentic_before_path']).read_bytes() if row['authentic_before_path'] else None;return row,pr,raw,before

def rebound_changed_record(row,pr,record):
 raw=yaml.safe_dump(record,sort_keys=False,allow_unicode=True).encode();h=W.sha(raw);row['payload']['sha256']=h;pr['after_capture']['sha256']=h;return raw

class RefusalControls(unittest.TestCase):
 def fixture(self):
  p=FIX/self._testMethodName;p.mkdir();return p
 def prepare(self):return BASE.prepare(NEW)
 def test_valid_native_write_and_retention(self):
  p=self.prepare();root=self.fixture();out=root/'valid.yaml';receipt=BASE.write(p,root,out);actual=yaml.safe_load(out.read_text());self.assertEqual(actual,p['after_record']);self.assertEqual(actual['curation_history'][:-1],p['before_record']['curation_history']);self.assertEqual(receipt['before_payload_sha256'],W.sha(p['old_bytes']));self.assertEqual(W.retained_projection(actual),W.retained_projection(p['before_record']))
 def test_unlisted_inherited_marine_proposal(self):
  with self.assertRaises(ValueError):BASE.prepare('b-proposal-marine-aliases')
 def test_already_correct_oxoid_excluded(self):
  with self.assertRaises(ValueError):BASE.prepare('w03-oxoid-cm0149-product-1224-v1')
 def test_retired_rcm_excluded(self):
  with self.assertRaises(ValueError):BASE.prepare('b-proposal-cm0149-form')
 def test_unlisted_field_index(self):
  row,pr,raw,b=data();row['field']='ontology_mapping.evidence[1].evidence_type'
  with self.assertRaisesRegex(ValueError,'unlisted field'):W.verify_binding(row,pr,raw,b)
 def test_unlisted_substitution(self):
  row,pr,raw,b=data();row['change']['to']='RECIPE_SOURCE'
  with self.assertRaisesRegex(ValueError,'unlisted substitution'):W.verify_binding(row,pr,raw,b)
 def test_payload_bytes_drift(self):
  row,pr,raw,b=data()
  with self.assertRaisesRegex(ValueError,'old payload bytes differ'):W.verify_binding(row,pr,raw+b'\n',b)
 def test_complete_object_pin_even_if_payload_hash_rebound(self):
  row,pr,raw,b=data();record=yaml.safe_load(raw);record['ontology_mapping']['evidence'][0]['notes']+=' unauthorized';raw=rebound_changed_record(row,pr,record)
  with self.assertRaisesRegex(ValueError,'complete object drift'):W.verify_binding(row,pr,raw,b)
 def test_parent_pin_even_if_payload_hash_rebound(self):
  row,pr,raw,b=data();record=yaml.safe_load(raw);record['ontology_mapping']['mapping_quality']='BROAD_MATCH';raw=rebound_changed_record(row,pr,record)
  with self.assertRaisesRegex(ValueError,'parent mapping drift'):W.verify_binding(row,pr,raw,b)
 def test_history_prefix_pin_even_if_payload_hash_rebound(self):
  row,pr,raw,b=data();record=yaml.safe_load(raw);record['curation_history'][0]['curator']='forged';raw=rebound_changed_record(row,pr,record)
  with self.assertRaisesRegex(ValueError,'history prefix drift'):W.verify_binding(row,pr,raw,b)
 def test_authentic_before_bytes_drift(self):
  row,pr,raw,b=data(EDIT)
  with self.assertRaisesRegex(ValueError,'authentic beforeimage drift'):W.verify_binding(row,pr,raw,b+b'\n')
 def test_inherited_object_even_if_before_hash_rebound(self):
  row,pr,raw,b=data(EDIT);before=yaml.safe_load(b);before.setdefault('ontology_mapping',{}).setdefault('evidence',[]).append(copy.deepcopy(row['complete_mapping_evidence_object']));b=yaml.safe_dump(before,sort_keys=False).encode();row['authentic_before']['sha256']=W.sha(b);pr['before_sha256']=W.sha(b)
  with self.assertRaisesRegex(ValueError,'inherited evidence excluded'):W.verify_binding(row,pr,raw,b)
 def test_repeated_application_to_corrected_record(self):
  row,pr,raw,b=data();record=yaml.safe_load(raw);record['ontology_mapping']['evidence'][0]['evidence_type']='LLM_SUGGESTION';raw=rebound_changed_record(row,pr,record)
  with self.assertRaises(ValueError):W.verify_binding(row,pr,raw,b)
 def test_unlisted_scientific_postimage_change(self):
  p=self.prepare();p['after_record']['notes']='unauthorized change';root=self.fixture();out=root/'invalid.yaml'
  with self.assertRaisesRegex(ValueError,'prepared output/history mutated'):BASE.write(p,root,out)
  self.assertFalse(out.exists())
 def test_prepared_old_bytes_must_match_actual_current_bytes(self):
  p=self.prepare();p['old_bytes']=b'tampered old bytes';root=self.fixture();out=root/'invalid.yaml'
  with self.assertRaises(ValueError):BASE.write(p,root,out)
  self.assertFalse(out.exists())
 def test_history_event_mutation(self):
  p=self.prepare();p['event']['previous_status']='UNMAPPED';root=self.fixture();out=root/'invalid.yaml'
  with self.assertRaises(ValueError):BASE.write(p,root,out)
  self.assertFalse(out.exists())
 def test_existing_destination(self):
  p=self.prepare();root=self.fixture();out=root/'existing.yaml';out.write_bytes(b'sentinel')
  with self.assertRaises(ValueError):BASE.write(p,root,out)
  self.assertEqual(out.read_bytes(),b'sentinel')
 def test_destination_symlink(self):
  p=self.prepare();root=self.fixture();target=root/'target';target.write_bytes(b'sentinel');out=root/'alias.yaml';out.symlink_to(target)
  with self.assertRaises(ValueError):BASE.write(p,root,out)
  self.assertEqual(target.read_bytes(),b'sentinel')
 def test_symlink_parent_inside_permitted_root(self):
  p=self.prepare();root=self.fixture();target=root/'target';target.mkdir();alias=root/'alias';alias.symlink_to(target,target_is_directory=True);out=alias/'out.yaml'
  with self.assertRaises(ValueError):BASE.write(p,root,out)
  self.assertFalse((target/'out.yaml').exists())
 def test_case_aliased_destination(self):
  p=self.prepare();root=self.fixture();target=root/'Alias.YAML';target.write_bytes(b'sentinel');out=root/'alias.yaml'
  with self.assertRaises(ValueError):BASE.write(p,root,out)
  self.assertEqual(target.read_bytes(),b'sentinel')
 def test_lexical_escape(self):
  p=self.prepare();root=self.fixture();out=root/'..'/'escaped.yaml'
  with self.assertRaisesRegex(ValueError,'lexical traversal'):BASE.write(p,root,out)
  self.assertFalse((root.parent/'escaped.yaml').exists())
 def test_maintained_output_boundary(self):
  with self.assertRaisesRegex(ValueError,'outside declared'):W.check_destination(R/'data/ingredients/mapped',R/'data/ingredients/mapped/forbidden-test-write.yaml')
 def test_schema_invalid_candidate_refused(self):
  row,pr,raw,b=data();record=yaml.safe_load(raw);record['unlisted_schema_field']='invalid'
  with self.assertRaisesRegex(ValueError,'native schema rejected'):W.corrected_record(row,record)

if __name__=='__main__':
 result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(RefusalControls))
 receipt={'writer_sha256':hashlib.sha256(FILE.read_bytes()).hexdigest(),'fixture_root':str(FIX.relative_to(R)),'tests_run':result.testsRun,'failures':[{'test':str(t),'traceback':e} for t,e in result.failures],'errors':[{'test':str(t),'traceback':e} for t,e in result.errors],'success':result.wasSuccessful(),'scope':'Independent bounded guard controls; actual corpus/old reports untouched. All fixtures retained.'}
 with (OUT/('controls-v1-'+STAMP+'.json')).open('x') as f:json.dump(receipt,f,indent=2);f.write('\n')
 raise SystemExit(0 if result.wasSuccessful() else 1)
