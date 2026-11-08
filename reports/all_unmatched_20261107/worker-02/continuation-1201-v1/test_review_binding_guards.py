from copy import deepcopy
import unittest
from bind_successor_reviews import digest,verify_case


class ReviewBindingGuards(unittest.TestCase):
    def setUp(self):
        self.decision={'case_id':'case1','case_input_sha256':'a'*64,'reasoning':'Source supports a scoped stock only.'}
        self.row={'case_id':'case1','case_input_sha256':'a'*64,'decision_canonical_sha256':digest(self.decision),'status':'approve','reasoning':'Inspected source concentration and whole-stock boundary.'}

    def test_exact_separate_review_accepted(self):
        verify_case(self.decision,self.row,'reviewer',['author'])

    def test_author_cannot_approve(self):
        with self.assertRaises(ValueError):verify_case(self.decision,self.row,'author',['author'])

    def test_changed_science_rejected(self):
        d={**self.decision,'reasoning':'Different claim'}
        with self.assertRaises(ValueError):verify_case(d,self.row,'reviewer',['author'])

    def test_open_finding_not_approval(self):
        with self.assertRaises(ValueError):verify_case(self.decision,{**self.row,'status':'findings_open'},'reviewer',['author'])

    def test_case_swap_rejected(self):
        with self.assertRaises(ValueError):verify_case(self.decision,{**self.row,'case_id':'other'},'reviewer',['author'])

    def test_blank_assessment_rejected(self):
        with self.assertRaises(ValueError):verify_case(self.decision,{**self.row,'reasoning':''},'reviewer',['author'])


if __name__=='__main__':unittest.main()
