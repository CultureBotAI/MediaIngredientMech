import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('binding', Path(__file__).with_name('bind_independent_reviews.py'))
binding = importlib.util.module_from_spec(spec)
spec.loader.exec_module(binding)


class BindingTests(unittest.TestCase):
    def setUp(self):
        self.decision = {'case_id':'case', 'case_input_sha256':'a', 'reasoning':'source-supported'}
        self.review = {'case_id':'case', 'case_input_sha256':'a', 'status':'approve',
                       'decision_sha256':binding.digest(self.decision)}

    def test_exact_reviewed_content(self):
        binding.verify_decision(self.decision, self.review)

    def test_changed_reasoning_rejected(self):
        with self.assertRaises(ValueError):
            binding.verify_decision({**self.decision, 'reasoning':'unsupported'}, self.review)

    def test_open_review_cannot_approve(self):
        with self.assertRaises(ValueError):
            binding.verify_decision(self.decision, {**self.review, 'status':'findings_open'})

    def test_wrong_source_case_hash_rejected(self):
        with self.assertRaises(ValueError):
            binding.verify_decision(self.decision, {**self.review, 'case_input_sha256':'b'})


if __name__ == '__main__':
    unittest.main()
