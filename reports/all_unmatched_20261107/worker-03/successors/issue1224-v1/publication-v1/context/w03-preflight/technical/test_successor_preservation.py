"""Controls exercise core origin/preservation fail-closed obligations."""
from pathlib import Path
from copy import deepcopy
import json,sys,unittest
sys.path.insert(0,str(Path(__file__).parent))
from check_successor_preservation import check_objects,CASE,OLD,NEW,DEST,EXPECTED_PAYLOAD
ROOT=Path.cwd()/'reports/all_unmatched_20261107/worker-03'
class PreservationControls(unittest.TestCase):
 def setUp(self):
  self.old=[json.loads((ROOT/(n+'.json')).read_text()) for n in ['decisions','proposals','evidence']]
  self.new=deepcopy(self.old);d=next(r for r in self.new[0]['decisions'] if r['case_id']==CASE);p=next(r for r in self.new[1]['proposals'] if r['proposal_id']==OLD)
  self.ret={'retired_proposal':deepcopy(p),'retired_decision':deepcopy(d)}
  d['proposal_ids']=[NEW];d['independent_review']={'status':'pending','evidence_ids':[]};p.update(proposal_id=NEW,kind='new_owner',before_sha256=None,owner_path=DEST);p['after_capture']['sha256']=EXPECTED_PAYLOAD
 def check(self):return check_objects(*self.old,*self.new,self.ret)
 def fails(self):
  with self.assertRaises(ValueError):self.check()
 def test_legitimate_shape_passes(self):self.assertEqual(self.check()['unchanged_other_case_count'],187)
 def test_other_case_edit_fails(self):self.new[0]['decisions'][0]['reasoning']='tampered';self.fails()
 def test_other_proposal_edit_fails(self):self.new[1]['proposals'][0]['description']='tampered';self.fails()
 def test_original_evidence_edit_fails(self):self.new[2]['evidence'][0]['locator']='tampered';self.fails()
 def test_original_evidence_removed_fails(self):self.new[2]['evidence'].pop();self.fails()
 def test_duplicate_case_fails(self):self.new[0]['decisions'].append(deepcopy(self.new[0]['decisions'][0]));self.fails()
 def test_retired_proposal_active_fails(self):self.new[1]['proposals'].append(deepcopy(self.ret['retired_proposal']));self.fails()
 def test_retired_object_reflag_fails(self):self.ret['retired_proposal']['kind']='new_owner';self.fails()
 def test_retired_decision_rewrite_fails(self):self.ret['retired_decision']['proposal_ids']=[];self.fails()
 def test_new_owner_fabricated_before_fails(self):next(p for p in self.new[1]['proposals'] if p['proposal_id']==NEW)['before_sha256']='0'*64;self.fails()
 def test_wrong_payload_fails(self):next(p for p in self.new[1]['proposals'] if p['proposal_id']==NEW)['after_capture']['sha256']='0'*64;self.fails()
 def test_second_case_origin_fails(self):self.new[0]['decisions'][0]['proposal_ids'].append(NEW);self.fails()
 def test_missing_new_origin_fails(self):next(r for r in self.new[0]['decisions'] if r['case_id']==CASE)['proposal_ids']=[];self.fails()
 def test_frozen_identity_fields_fail(self):
  for field,value in [('case_input_sha256','0'*64),('source',{}),('occurrence_ids',[]),('owner_records',[]),('native_owner_review_rows',[{}]),('preserved_original_kg_entry_downstream_holds',[{}]),('hold_scope_note','clear')]:
   with self.subTest(field=field):
    d=next(r for r in self.new[0]['decisions'] if r['case_id']==CASE);prior=d[field];d[field]=value;self.fails();d[field]=prior
if __name__=='__main__':unittest.main()
