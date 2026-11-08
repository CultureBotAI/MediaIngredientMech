"""Meaningful corrupt-input controls for the successor assembler (2026-11-08)."""
import copy
import json
from pathlib import Path
import unittest
import assemble as a


class AssemblyControls(unittest.TestCase):
    def setUp(self):
        self.root = Path.cwd() / '.temp/all-unmatched-worker-08/issue-1227-v1/test-fixture'
        self.root.mkdir(parents=True, exist_ok=True)
        (self.root / 'payload.yaml').write_text('identifier: TEST:1\n')
        (self.root / 'peer.json').write_text('{"fixture": true}\n')
        ref = dict(root='artifact', path='payload.yaml', sha256=a.sha(self.root / 'payload.yaml'))
        peerref = dict(root='artifact', path='peer.json', sha256=a.sha(self.root / 'peer.json'))
        d = dict(case_id='C1', source={'raw_source_label': 'a literal'}, case_input_sha256='frozen',
                 occurrence_ids=['O1', 'O2'], preserved_native_decisions=[{'status': 'WITHHOLD'}],
                 proposal_ids=['P1'], evidence_ids=['E1'], independent_review={'status': 'complete', 'evidence_ids': ['old']})
        p = dict(proposal_id='P1', owner_path='data/ingredients/mapped/A.yaml', kind='edit_existing_owner',
                 before_sha256='original', case_ids=['C1'], evidence_ids=['E1'], after_capture=ref)
        e = dict(evidence_id='E1', accessed_at='original-time', supports_or_contradicts='source assertion')
        self.parent = dict(decisions={'decisions': [d]}, proposals={'proposals': [p]}, evidence={'evidence': [e]})
        self.groups = [dict(name='test', author='author-A', reviewer='reviewer-B', case_ids=['C1'],
            proposal_ids=['P1'], decisions=[copy.deepcopy(d)], proposals=[copy.deepcopy(p)], evidence=[copy.deepcopy(e)],
            bound_inputs=[ref], peer_capture=peerref, peer=dict(author='author-A', reviewer='reviewer-B',
            case_ids=['C1'], proposal_ids=['P1'], open_blocking_findings=[], full_payload_review=True,
            case_hashes={'C1': a.digest(d)}, payload_hashes={'P1': ref['sha256']}))]

    def run_assembly(self):
        return a.assemble(self.parent, self.groups, self.root)

    def reject(self, mutation):
        mutation()
        with self.assertRaises(AssertionError):
            self.run_assembly()

    def test_positive_retains_frozen_cases_holds_and_evidence(self):
        result = self.run_assembly()
        self.assertEqual(result['decisions.json']['decisions'][0]['occurrence_ids'], ['O1', 'O2'])
        self.assertEqual(result['evidence.json']['evidence'][0], self.parent['evidence']['evidence'][0])
        self.assertEqual(result['assembly-provenance.json']['unchanged_payloads'], 1)

    def test_self_review(self):
        self.reject(lambda: self.groups[0].update(reviewer='author-A'))

    def test_delta_only_peer(self):
        self.reject(lambda: self.groups[0]['peer'].update(full_payload_review=False))

    def test_stale_peer_payload(self):
        self.reject(lambda: self.groups[0]['peer']['payload_hashes'].update(P1='stale'))

    def test_stale_peer_case(self):
        self.reject(lambda: self.groups[0]['decisions'][0].update(reasoning='changed since review'))

    def test_lost_occurrence(self):
        self.reject(lambda: self.groups[0]['decisions'][0].update(occurrence_ids=['O1']))

    def test_lost_hold(self):
        self.reject(lambda: self.groups[0]['decisions'][0].update(preserved_native_decisions=[]))

    def test_beforeimage_replacement(self):
        self.reject(lambda: self.groups[0]['proposals'][0].update(before_sha256='wrong'))

    def test_missing_peer_case(self):
        self.reject(lambda: self.groups[0]['peer'].update(case_ids=[]))

    def test_unresolved_peer_finding(self):
        self.reject(lambda: self.groups[0]['peer'].update(open_blocking_findings=['unfixed']))

    def test_mutated_historical_evidence_timestamp(self):
        self.reject(lambda: self.groups[0]['evidence'][0].update(accessed_at='new-time'))

    def test_duplicate_group(self):
        self.reject(lambda: self.groups.append(copy.deepcopy(self.groups[0])))

    def test_missing_group(self):
        self.reject(lambda: self.groups.clear())

    def test_missing_backlink(self):
        self.reject(lambda: self.groups[0]['decisions'][0].update(proposal_ids=[]))

    def test_capture_corruption(self):
        self.reject(lambda: (self.root / 'payload.yaml').write_text('changed\n'))

    def test_capture_traversal(self):
        self.reject(lambda: self.groups[0]['proposals'][0]['after_capture'].update(path='../outside'))

    def test_root_primary_evidence_is_hash_bound(self):
        e = dict(evidence_id='root-primary', capture=self.groups[0]['bound_inputs'][0])
        result = a.assemble(self.parent, self.groups, self.root, [e])
        self.assertIn('root-primary', {x['evidence_id'] for x in result['evidence.json']['evidence']})

    def test_root_primary_cannot_replace_inherited_evidence(self):
        with self.assertRaises(AssertionError):
            a.assemble(self.parent, self.groups, self.root, [dict(evidence_id='E1', capture=self.groups[0]['bound_inputs'][0])])

    def test_peer_evidence_index_must_match(self):
        ref = self.groups[0]['bound_inputs'][0]
        self.groups[0]['inputs'] = {'evidence': ref}
        self.groups[0]['peer']['input_hashes'] = {ref['path']: ref['sha256']}
        self.run_assembly()
        self.reject(lambda: self.groups[0]['peer']['input_hashes'].update({ref['path']: 'stale'}))


if __name__ == '__main__':
    unittest.main(verbosity=2)
