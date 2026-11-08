from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import yaml

W = Path.cwd()
S = W / '.temp/w05-postseal-source-corrections-v1'
R = S / 'final-assembly-review-v1'
B = W / 'reports/all_unmatched_20261107/worker-05'
P = B / 'postseal-source-corrections-v1'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
j = lambda p: json.loads(p.read_text())
ref = lambda p: {'path': str(p.relative_to(W)), 'sha256': sha(p)}
now = lambda: datetime.now(timezone.utc).isoformat()

assert not (R / 'FINAL-MANIFEST-v1.json').exists()
a = j(R / 'assembly-checks-v1.json')
for row in a['inputs']:
    assert sha(W / row['path']) == row['sha256'], row
child = R / 'preservation-child'
cm = j(child / 'MANIFEST.json')
for row in cm['files']:
    p = child / row['path']
    assert sha(p) == row['sha256'] and p.stat().st_size == row['bytes'], row
cr = j(child / 'main-receipt.json')
assert cr['status'] == 'PASS' and not cr['findings']
assert sha(child / 'main-receipt.json') == 'f68dadd4d3c7fa2b6e96f2f72b7ade40a6aaf2a0ce60dfe382e4be3606344898'

# Compare the complete retained diagnostic with the corrected assertion receipt.
d = j(S / 'validation/native-row-projections-diagnostic-v1.json')
n = j(P / 'validation/native-row-projections.json')
assert n['status'] == 'PASS' and n['tris'] == d['tris']
assert sha(Path(n['builder'])) == n['builder_sha256'] == d['builder_sha256']
old_by = {x['proposal_id']: x for x in d['changed_payload_projections']}
projections = []
total_deltas = 0
for x in n['changed_payload_projections']:
    prior = old_by[x['proposal_id']]
    for key, value in prior.items():
        assert x[key] == value, (x['proposal_id'], key)
    before_path, after_path = [B / x[k]['path'] for k in ('before_capture', 'after_capture')]
    for key, path in [('before_capture', before_path), ('after_capture', after_path)]:
        assert sha(path) == x[key]['sha256']
    before, after = [yaml.safe_load(p.read_text()) for p in (before_path, after_path)]
    bc, ac = [z['curation_history'][-1]['curator'] for z in (before, after)]
    assert x['before_curator'] == bc and x['after_curator'] == ac
    actual = []
    assert len(x['before_rows']) == len(x['after_rows'])
    for i, (br, ar) in enumerate(zip(x['before_rows'], x['after_rows'])):
        assert br.keys() == ar.keys()
        delta = [k for k in br if br[k] != ar[k]]
        assert delta in ([], ['source']), delta
        if delta:
            assert br['source'].replace('MIM:curator=' + bc, 'MIM:curator=' + ac) == ar['source']
            actual.append({'row_index': i, 'field': 'source', 'before': br['source'], 'after': ar['source']})
    recorded = [{k: z[k] for k in ('row_index', 'field', 'before', 'after')} for z in x['exact_allowed_source_attribution_changes']]
    assert recorded == actual
    assert x['before_suppressions'] == x['after_suppressions']
    assert x['all_other_row_fields_equal']
    total_deltas += len(actual)
    projections.append({'proposal_id': x['proposal_id'], 'exact_curator_token_changes': actual,
                        'all_other_cells_and_suppressions_equal': True,
                        'before_capture': x['before_capture'], 'after_capture': x['after_capture']})
assert len(projections) == 5 and total_deltas == 4

check_path = P / 'validation/native-retained-review-check.json'
check = j(check_path)
assert check['exit_code'] == 0 and check['result']['valid_reviews'] == 1023
assert check['result']['coverage'] == 'declared_scopes_only'
for kind in ('stdout', 'stderr'):
    path = P / f'validation/native-retained-review-check.{kind}.log'
    assert sha(path) == check[kind + '_sha256']
assert json.loads((P / 'validation/native-retained-review-check.stdout.log').read_text()) == check['result']

# Re-authenticate the final full predecessor manifest and maintained baseline.
old_root = B / 'final-correction-v1'
old_manifest = j(old_root / 'MANIFEST.json')
for row in old_manifest['files']:
    path = old_root / row['path']
    assert sha(path) == row['sha256'] and path.stat().st_size == row['bytes']
for row in old_manifest['native_review']:
    assert sha(W / row['path']) == row['sha256']
baseline_path = W / '.temp/w05-final-correction-v1/control/maintained-baseline-preservation-start.json'
baseline = j(baseline_path)
record_paths = {row['path'] for row in baseline['records']}
assert record_paths == {str(p.relative_to(W)) for p in (W / 'data/ingredients').rglob('*.yaml')}
for row in baseline['records']:
    assert sha(W / row['path']) == row['sha256']
root_preservation = j(P / 'validation/preservation-final.json')
for row in root_preservation['contracts']:
    assert sha(W / row['path']) == row['sha256']
for row in root_preservation['shards']:
    assert sha(Path(row['path'])) == row['sha256']

mirror = j(P / 'validation/publication-mirror-bindings.json')
for row in mirror['bindings']:
    assert sha(W / row['private_path']) == sha(W / row['public_path']) == row['sha256']

# Exact bounded README remedy; the historical bad prose stays immutable.
before = (R / 'README-before-finding-001.md').read_text()
after = (P / 'README.md').read_text()
assert before.replace('UN8', '180').replace('UN5', '137') == after
assert (P / 'report-remediation-v1/README-before.md').read_text() == before
supp = j(P / 'report-remediation-v1/supplemental-finding-register.json')
assert supp['finding_id'] == 'W05-POSTSEAL-ASSEMBLY-REVIEW-001' and supp['reported_before_fix']
assert sha(W / supp['reproduction']['path']) == supp['reproduction']['sha256']
assert sha(P / 'report-remediation-v1' / supp['remediation']['path']) == supp['remediation']['sha256']
assert sha(W / supp['fixed_generator']['path']) == supp['fixed_generator']['sha256']

closure = {
    'reviewer': '/root/final_skeptical', 'completed_at': now(), 'status': 'PASS',
    'scope': 'Final closure after preserved preliminary assembly checks. No new source payload or chemical claim authored.',
    'native_projection_assessments': projections,
    'projection_conclusion': 'Exactly four last-curator source-token changes; complete diagnostic row arrays retained unchanged in the corrected receipt. All other cells and suppressions equal. Marine row entirely unchanged. Native builder unchanged.',
    'native_projection_limit': 'Independent comparison and source-history authentication of root-produced rows; no second invocation of the full owner-index builder. The separately attributed child independently invoked the native builder for the complete unchanged Tris payload.',
    'native_retained_check': check,
    'preservation': {'public_predecessor_manifest_members_verified': len(old_manifest['files']),
                     'maintained_record_paths_and_hashes_equal': len(record_paths),
                     'includes_ignored_files': True, 'all_private_public_mirror_bindings_verified': len(mirror['bindings']),
                     'disjoint_child': ref(child / 'main-receipt.json'), 'child_manifest': ref(child / 'MANIFEST.json')},
    'readme_rereview': a['finding_rereview'],
    'inputs': [ref(p) for p in [P / 'validation/native-row-projections.json',
        S / 'validation/native-row-projections-diagnostic-v1.json', S / 'review/projection-diagnostic-review-v1.json',
        check_path, P / 'validation/native-retained-review-check.stdout.log', P / 'validation/native-retained-review-check.stderr.log',
        P / 'validation/preservation-final.json', old_root / 'MANIFEST.json', baseline_path,
        P / 'validation/publication-mirror-bindings.json', P / 'report-remediation-v1/supplemental-finding-register.json',
        P / 'control/seal_packet.py', P / 'control/write_handoff.py', P / 'control/write_summary_v2.py']],
    'findings': [],
}
(R / 'closure-checks-v1.json').write_text(json.dumps(closure, indent=2) + '\n')

science = j(P / 'review/main-review.json')
inputs = a['inputs'] + closure['inputs'] + [ref(R / 'assembly-checks-v1.json'), ref(R / 'closure-checks-v1.json'),
    ref(R / 'new-findings-v1.json'), ref(child / 'main-receipt.json'), ref(child / 'MANIFEST.json'),
    ref(child / 'original-lineage-fields-v1.json'), ref(P / 'review/FINAL-MANIFEST-v1.json')]
main = {
    'schema': 'worker05-postseal-final-assembly-independent-review-v1',
    'reviewer': '/root/final_skeptical', 'completed_at': now(),
    'review_type': 'Independent final exact-byte assembly and attribution review, with sealed scientific judgments cited under their actual scopes.',
    'status': 'PASS_REPORT_CORRECTNESS_WITH_RETAINED_HOLDS', 'native_verdict': 'needs_curation',
    'base_head': '5156d92bec6bd885ca8bae3c5e18bfdce0069176',
    'original_source_head': '43f7cf6e8681fa617b5d6d3529d94d537ca01f0d',
    'counts': a['counts'], 'case_assembly_checks': a['case_assembly_checks'],
    'complete_changed_payload_bindings': [{'proposal_id': x['proposal_id'], 'after_capture': x['after_capture'],
        'scientific_reviewer': x['reviewer'] if 'reviewer' in x else '/root/final_skeptical',
        'scientific_assessment_verbatim': x['assessment']} for x in science['payload_reviews']],
    'primary_scopes': cr['primary_source_authorship'],
    'scientific_review': ref(P / 'review/main-review.json'),
    'separate_family_and_tris_scientific_review': science['separate_child_review'],
    'separate_family_and_tris_scope': 'Actual reviewer /root/final_skeptical/preservation_audit: all26 family rows/28finding IDs,59frozen entries,18unchanged W05payloads/20cases/53occurrences; complete unchanged Tris salt scientifically reviewed with independent native3row reproduction. Other family payloads have explicit family-applicability scope, not new whole-owner approval.',
    'separate_final_preservation_audit': {'reviewer': cr['reviewer'], 'receipt': ref(child / 'main-receipt.json'),
        'manifest': ref(child / 'MANIFEST.json'), 'scope': cr['scope'], 'checks': cr['checks']},
    'native_review_assessment': {
        'targets': 15, 'partition': {'changed_case_decisions': 8, 'complete_changed_payloads': 5, 'family_applicability_ledger': 1, 'complete_unchanged_tris_payload': 1},
        'individual_science_attribution': 'Case and payload summaries and JSON details reproduce the exact sealed independent assessments. Family/Tris evidence separately credits the actual child reviewer. Root is identified as the self-reviewing native-envelope compiler, not an independent scientist.',
        'checks': 'Native schema, all20 source hashes, evidence hashes and exact Markdown rendering independently verified. Retained native check completed exit0 with1023 valid reviews and declared_scopes_only coverage.',
        'source_projection_rereview': ref(R / 'closure-checks-v1.json'),
        'limits': 'No universal native or scientific approval of all142 payloads is inferred from15 targets. Existing earlier scientific reviews retain exact attribution and limitations. Full142 structural/schema/component validation does not replace science.'},
    'preservation_assessment': 'All180 unchanged decisions,137 unchanged proposals,1537 prior evidence objects, all188 frozen raw source/hold objects and original18finding objects/dispositions remain exact. All138 original proposal lineages preserve histories, negatives, roles, counts and graphs. All1879 campaign cases retain unique ownership. Old5156/43 report trees, prior native bundles, original1857 evidence and390member22-family comparison are independently preserved; final2938member predecessor manifest rehashed.',
    'finding_dispositions': [dict(a['finding_rereview'], supplemental_register=ref(P / 'report-remediation-v1/supplemental-finding-register.json'))],
    'source_finding_dispositions_retained': science['finding_dispositions'],
    'checks': a['checks'], 'closure_receipt': ref(R / 'closure-checks-v1.json'), 'input_hashes': inputs,
    'limits': [
        'Scientific evidence is the separately sealed8decision/5complete-payload review and attributed family/Tris child review; hash checks establish preservation and binding only.',
        'BSA remains literal50g input with unknown finalvolume, catalogue and inherited holds; no50g/L inference. Marine COMPLETE is relative to16nominal printed dry inputs, with approximate/performance adjustment qualifier, no lot closure or guessed salt form.',
        'Three rumen parent parts remain literal UNMAPPED/noID; no unsupported clarified/untreated inference. Supported separate JCM266 clarification remains intact and held as recorded.',
        'HEPES/Wolfe/ethanol conditional comparisons and all source/owner/role/export holds remain. Missing facts establish neither equality nor difference. No other-worker union, owner merge, identifier winner or tombstone approved.',
        'The final report manifest, copied review packet and postpush handoff may be added after this receipt. Any alteration of bound source/core/native/README/validation inputs requires a successor review.',
        'No published successor commit is asserted before root verifies an ordinary commit/push. Root owns coordinator acceptance, maintained owner application and export approval.'
    ],
    'publication_control_assessment': 'Read the bounded seal and postpush handoff scripts. The seal records exact members/nativepair without self-referential commit claims; the handoff requires matching remote/head, ancestor preservation, exact committed tree bytes and only authorized added report/review paths. These scripts are root-owned and were not executed by this reviewer.',
}
(R / 'FINAL-ASSEMBLY-REVIEW-v1.json').write_text(json.dumps(main, indent=2) + '\n')
main_ref = ref(R / 'FINAL-ASSEMBLY-REVIEW-v1.json')
(R / 'HANDOFF.md').write_text(f"Independent final assembly review passed with existing source, owner and export holds retained. Reviewer: `/root/final_skeptical`. Completed: `{main['completed_at']}`.\n\nThe exact canonical set contains188decisions,142proposals and1551evidence entries. Eight decision objects and five full payloads changed;180decisions,137proposals and all1537previous evidence objects remain exact. All138original proposal lineages and all1879campaign ownership boundaries are preserved. The independent preservation child and sealed source-science packet retain their actual attribution and limits.\n\nThe native15target bundle accurately separates8decisions,5complete changed payloads, the family ledger and complete unchanged Tris salt. Schema/source/evidence hashes and Markdown rendering pass; retained native check reports1023valid reviews, declared scopes only. All142payload validation and3029record component overlay remain bound to the canonical inputs. Four native source cells change only their authentic last-curator token; all other cells are unchanged.\n\n`W05-POSTSEAL-ASSEMBLY-REVIEW-001` was reported before fix. The exact README successor changes only UN8→180 and UN5→137. Before bytes, generator, finding, remediation and rereview are preserved. No remaining assembly findings were identified. Native verdict remains `needs_curation`; this is no final-owner/export approval.\n\nMain receipt: `FINAL-ASSEMBLY-REVIEW-v1.json`, SHA256 `{main_ref['sha256']}`. Root may copy this sealed packet and add the report manifest, then ordinary commit/push and exact-head handoff. No future head is inferred here.\n")
files = [{'path': str(p.relative_to(R)), 'sha256': sha(p), 'bytes': p.stat().st_size}
         for p in sorted(R.rglob('*')) if p.is_file() and p.name != 'FINAL-MANIFEST-v1.json']
manifest = {'schema': 'worker05-postseal-final-assembly-review-manifest-v1',
            'reviewer': '/root/final_skeptical', 'sealed_at': now(), 'status': main['status'],
            'main_review': {'path': 'FINAL-ASSEMBLY-REVIEW-v1.json', 'sha256': main_ref['sha256']},
            'scope': main['review_type'], 'files': files, 'self_exclusion': 'This manifest excludes itself.'}
(R / 'FINAL-MANIFEST-v1.json').write_text(json.dumps(manifest, indent=2) + '\n')
print(json.dumps({'main': main_ref, 'manifest': ref(R / 'FINAL-MANIFEST-v1.json'),
                  'handoff': ref(R / 'HANDOFF.md'), 'completed_at': main['completed_at'],
                  'members': len(files), 'status': main['status']}, indent=2))
