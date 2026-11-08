"""Regression controls for historical preservation and exact evidence/alias guards."""
import copy
import unittest
from validate_selection import preserved_history, truthful_mapping_evidence, literal_nonresolving, disallow_active_collision, official_exact_term, complete_preservation_scope
from validate_selection import record_reviewed_admission_failure, read, OUT


class ValidationControls(unittest.TestCase):
    def test_append_history_preserves_role(self):
        old = {'curation_history': [{'action': 'CREATED', 'llm_assisted': False}], 'roles': ['retained']}
        new = copy.deepcopy(old); new['curation_history'].append({'action': 'CORRECTED', 'llm_assisted': True})
        preserved_history(old, new, True)

    def test_history_rewrite_rejected(self):
        with self.assertRaises(AssertionError):
            preserved_history({'curation_history': [{'llm_assisted': False}]}, {'curation_history': [{'llm_assisted': True}, {}]}, True)

    def test_missing_history_rejected(self):
        with self.assertRaises(AssertionError): preserved_history({}, {}, True)

    def test_role_addition_rejected(self):
        with self.assertRaises(AssertionError): preserved_history({}, {'roles': ['approved']}, False)

    def test_native_role_facet_change_rejected(self):
        with self.assertRaises(AssertionError): preserved_history({}, {'nutritional_roles': [{'role': 'VITAMIN_SOURCE'}]}, False)

    def test_occurrence_rewrite_rejected(self):
        with self.assertRaises(AssertionError): preserved_history({'occurrence_statistics': {'total_occurrences': 5}}, {'occurrence_statistics': {'total_occurrences': 6}}, False)

    def test_correct_mapping_category_preserves_source(self):
        truthful_mapping_evidence({'evidence_type': 'MANUAL_CURATION', 'source': 'same'}, {'evidence_type': 'LLM_SUGGESTION', 'source': 'same'})

    def test_human_mislabel_rejected(self):
        with self.assertRaises(AssertionError): truthful_mapping_evidence({'source': 'same'}, {'evidence_type': 'MANUAL_CURATION', 'source': 'same'})

    def test_lost_citation_rejected(self):
        with self.assertRaises(AssertionError): truthful_mapping_evidence({'source': 'old'}, {'evidence_type': 'DATABASE_MATCH', 'source': 'changed'})

    def test_native_rejected_literal_preserved(self):
        literal_nonresolving({'synonyms': [{'synonym_text': 'KH2HPO4', 'synonym_type': 'REJECTED_LABEL'}]}, 'KH2HPO4')

    def test_resolving_alias_rejected(self):
        with self.assertRaises(AssertionError): literal_nonresolving({'synonyms': [{'synonym_text': 'KH2HPO4', 'synonym_type': 'RAW_TEXT'}]}, 'KH2HPO4')

    def test_deleted_literal_rejected(self):
        with self.assertRaises(AssertionError): literal_nonresolving({'synonyms': []}, 'KH2HPO4')

    def test_existing_owner_does_not_collide_with_itself(self):
        disallow_active_collision({'own': {'identifier': 'X:1', 'mapping_status': 'MAPPED'}}, 'own', 'X:1')

    def test_promotion_to_existing_active_owner_rejected(self):
        with self.assertRaises(AssertionError):
            disallow_active_collision({'another': {'identifier': 'X:1', 'mapping_status': 'MAPPED'}}, 'own', 'X:1')

    def test_official_label_positive(self):
        official_exact_term([{'obo_id': 'MICRO:1', 'label': 'expected', 'is_obsolete': False}], 'MICRO:1', 'expected')

    def test_other_term_with_same_label_rejected(self):
        with self.assertRaises(AssertionError): official_exact_term([{'obo_id': 'MICRO:2', 'label': 'expected'}], 'MICRO:1', 'expected')

    def test_wrong_primary_label_rejected(self):
        with self.assertRaises(AssertionError): official_exact_term([{'obo_id': 'MICRO:1', 'label': 'wrong'}], 'MICRO:1', 'expected')

    def test_obsolete_exact_term_rejected(self):
        with self.assertRaises(AssertionError): official_exact_term([{'obo_id': 'MICRO:1', 'label': 'expected', 'is_obsolete': True}], 'MICRO:1', 'expected')


class PreservationReceiptControls(unittest.TestCase):
    def setUp(self):
        self.before = {'files': [{}, {}], 'tracked_count': 3}
        self.receipt = {'status': 'PASS', 'failure_count': 0, 'groups': {
            'initial_hashed_working_files': {'checks': 2, 'passed': 2, 'failed': 0},
            'supplemental_ten_baseline_entries': {'checks': 1, 'passed': 1, 'failed': 0},
            'w05_all_manifest_members': {'checks': 2, 'passed': 2, 'failed': 0}}}

    def test_complete_original_and_supplemental_scope(self):
        complete_preservation_scope(self.before, self.receipt)

    def test_omitted_supplement_cannot_be_called_complete(self):
        self.receipt['groups']['supplemental_ten_baseline_entries'].update(checks=0, passed=0)
        with self.assertRaises(AssertionError): complete_preservation_scope(self.before, self.receipt)

    def test_nested_failure_cannot_hide_under_top_level_pass(self):
        self.receipt['groups']['w05_all_manifest_members'].update(failed=1, passed=1)
        with self.assertRaises(AssertionError): complete_preservation_scope(self.before, self.receipt)

    def test_partial_original_capture_cannot_be_called_verified(self):
        self.receipt['groups']['initial_hashed_working_files'].update(checks=1, passed=1)
        with self.assertRaises(AssertionError): complete_preservation_scope(self.before, self.receipt)


class AdmissionFailureControls(unittest.TestCase):
    def setUp(self):
        self.review = read(OUT / 'independent-review/final_assembly/trypticase-admission-review-v1.json')
        self.proposal = copy.deepcopy(self.review['exact_selected_proposal'])
        self.prior = copy.deepcopy(self.review['predecessor_proposal'])
        self.hashes = {p: x['current_sha256'] for p, x in self.review['baseline_owner_checks'].items()}
        self.failure = ('changed identity collides', 'MICRO:0000113', ['data/ingredients/mapped/Bacto_Tryptic_Soy_Broth.yaml'])

    def record(self):
        return record_reviewed_admission_failure(self.proposal, self.prior, self.hashes, self.review, self.failure)

    def test_exact_reviewed_collision_remains_failed_and_held(self):
        actual = self.record()
        self.assertEqual(actual['gate_status'], 'failed')
        self.assertEqual(actual['maintained_admission'], 'HELD')

    def test_new_collision_not_exempted(self):
        self.proposal['proposal_id'] = 'different-owner'
        with self.assertRaises(AssertionError): self.record()

    def test_changed_selected_bytes_rejected(self):
        self.proposal['after_capture']['sha256'] = 'different'
        with self.assertRaises(AssertionError): self.record()

    def test_changed_predecessor_rejected(self):
        self.prior['after_capture']['sha256'] = 'different'
        with self.assertRaises(AssertionError): self.record()

    def test_changed_collider_rejected(self):
        self.hashes['data/ingredients/mapped/Bacto_Tryptic_Soy_Broth.yaml'] = 'different'
        with self.assertRaises(AssertionError): self.record()

    def test_extra_collider_rejected(self):
        self.failure[2].append('another.yaml')
        with self.assertRaises(AssertionError): self.record()

    def test_missing_owner_binding_rejected(self):
        self.hashes.pop('data/ingredients/unmapped/Trypticase_Soy_Broth.yaml')
        with self.assertRaises(AssertionError): self.record()


if __name__ == '__main__': unittest.main(verbosity=2)
