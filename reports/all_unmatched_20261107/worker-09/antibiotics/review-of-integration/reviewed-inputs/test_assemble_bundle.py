"""Failure controls for mechanical assembly; no test establishes scientific adequacy."""
import copy,unittest
from assemble_bundle import check_cases,digest
class AssemblyControls(unittest.TestCase):
 def setUp(self):
  self.case={'case_id':'x','source':'s','source_case_id':'s1','source_label':'','raw_source_label':'','occurrences':[{'occurrence_id':'o'}]}
  self.decision={'case_id':'x','source':{k:self.case[k] for k in ('source','source_case_id','source_label','raw_source_label')},'case_input_sha256':digest(self.case),'occurrence_ids':['o']}
 def test_positive(self):check_cases([self.case],[self.decision])
 def test_omitted(self):
  with self.assertRaises(ValueError):check_cases([self.case],[])
 def test_duplicate(self):
  with self.assertRaises(ValueError):check_cases([self.case],[self.decision,self.decision])
 def test_hash_change(self):
  d=copy.deepcopy(self.decision);d['case_input_sha256']='0'*64
  with self.assertRaises(ValueError):check_cases([self.case],[d])
 def test_blank_label_rewrite(self):
  d=copy.deepcopy(self.decision);d['source']['raw_source_label']='invented'
  with self.assertRaises(ValueError):check_cases([self.case],[d])
 def test_occurrence_loss(self):
  d=copy.deepcopy(self.decision);d['occurrence_ids']=[]
  with self.assertRaises(ValueError):check_cases([self.case],[d])
if __name__=='__main__':unittest.main()
