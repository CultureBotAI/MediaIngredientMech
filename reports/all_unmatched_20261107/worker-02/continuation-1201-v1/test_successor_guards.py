import importlib.util
from pathlib import Path
import unittest

spec=importlib.util.spec_from_file_location('successor',Path(__file__).with_name('assemble_successor.py'))
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class SuccessionGuards(unittest.TestCase):
    def setUp(self):
        self.original={'case_id':'one','case_input_sha256':'a','source':{'raw_source_label':'Sol.1'},'occurrence_ids':['x','y'],'proposal_ids':[],'reasoning':'old'}

    def test_supported_reassessment_may_change_reasoning(self):
        module.check_successor(self.original,{**self.original,'reasoning':'new source facts','proposal_ids':['new']})

    def test_cannot_change_raw_source_label(self):
        with self.assertRaises(ValueError):module.check_successor(self.original,{**self.original,'source':{'raw_source_label':'new owner label'}})

    def test_cannot_drop_occurrence(self):
        with self.assertRaises(ValueError):module.check_successor(self.original,{**self.original,'occurrence_ids':['x']})

    def test_cannot_change_frozen_case_digest(self):
        with self.assertRaises(ValueError):module.check_successor(self.original,{**self.original,'case_input_sha256':'b'})

    def test_cannot_revise_outside_cohort(self):
        with self.assertRaises(ValueError):module.check_successor({**self.original,'proposal_ids':['old']},self.original)

    def test_duplicate_case_rejected(self):
        with self.assertRaises(ValueError):module.unique([self.original,self.original],'case_id')


if __name__=='__main__':unittest.main()
