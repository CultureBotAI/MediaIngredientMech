"""Author the separately reasoned provenance assembly assessment in native format."""
from pathlib import Path
import datetime
import hashlib
import importlib.util
import json
import yaml

R = Path.cwd()
A = R/'.temp/w03-provenance-successor-v1/assembly'
O = R/'reports/all_unmatched_20261107/worker-03/successors/issue1226-v1'
spec = importlib.util.spec_from_file_location('native_review', R/'scripts/record_review.py')
native = importlib.util.module_from_spec(spec)
spec.loader.exec_module(native)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
rel = lambda p: str(p.relative_to(R))
now = datetime.datetime.now(datetime.timezone.utc)
timestamp = now.isoformat().replace('+00:00', 'Z')
review_id = now.strftime('%Y%m%dT%H%M%SZ')+'-w03-provenance-successor-assembly-v1'
targets = []
for target_id, name, label in [('decisions', 'decisions.json', 'All 188 unchanged source decisions'),
                               ('proposals', 'proposals.json', 'All 74 selected proposals and exact review bindings'),
                               ('evidence', 'evidence.json', 'All 868 evidence entries and exact captures')]:
    targets.append({'target_id': target_id, 'path': rel(O/name), 'label': label, 'kind': 'source',
                    'ownership_note': 'Worker03 report-only selector; no maintained owner application or scientific approval.'})
targets.append({'target_id': 'helper', 'path': '.temp/w03-provenance-successor-v1/provenance_writer_v2.py',
                'label': 'Exact immutable private helper-v2 #1246 repair', 'kind': 'source',
                'ownership_note': 'Task-private producer only; native campaign operator and maintained code unchanged.'})
proof = json.loads((A/'payload-scope-verification-v1.json').read_text())
extra = [r['new_path'] for r in proof['all74_payload_rows']]
extra += [rel(p) for p in [A/'payload-scope-verification-v1.json', A/'final-core-verification-v1.json',
                          A/'helper-repair-adjudication-v1.json', A/'preflight-inputs-v1.json',
                          A/'remote-predecessor-observation-v1.json', O/'payload-bridge.json',
                          O/'validation/complete-preservation.json', O/'validation/native-payloads.json',
                          O/'reviews/provenance/payload-phase-v2/HANDOFF.json',
                          O/'reviews/provenance/payload-phase-v2/review.yaml',
                          O/'reviews/technical/HANDOFF-v1.json']]
extra += ['MAPPING_SEMANTICS.md', 'src/mediaingredientmech/schema/mediaingredientmech.yaml',
          'docs/record-reviews.md', 'docs/record-review-profile.md', 'conf/record_review.yaml',
          '.claude/skills/reconcile-review-records/SKILL.md']
inspection = native.inspect_source(R, targets, extra)
with (A/'native-inspect-v1.json').open('x') as f:
    json.dump(inspection, f, indent=2); f.write('\n')
evidence = []
for eid, path, summary in [
    ('core', A/'final-core-verification-v1.json', 'Independent full selector and exact capture verification, all188 case rows, all74 proposal rows and all868 evidence rows; original tracked and ignored-inclusive maintained files preserved.'),
    ('payloads', A/'payload-scope-verification-v1.json', 'Independent full-value rollback proves exactly49 enum replacements and49 history appends;25 byte-identical payloads and all exclusions preserved.'),
    ('guard', A/'helper-repair-adjudication-v1.json', 'Direct code review plus original36 test-function AST retention and37-test peer execution supports exact private helper repair.'),
    ('peer', O/'reviews/provenance/payload-phase-v2/HANDOFF.json', 'Separate provenance reviewer assessed all49 actual corrected payloads with scientific_review=false; this receipt is correctly bound in changed proposal metadata.'),
    ('technical', O/'reviews/technical/HANDOFF-v1.json', 'Separate technical reviewer checked all74 native schema records and unchanged2996-record partonomy overlay, meaningful negative reference control, guards and original baseline.')]:
    evidence.append({'evidence_id': eid, 'kind': 'prior_review' if eid in {'peer', 'technical'} else 'validation',
                     'reference': rel(path), 'locator': 'Entire bounded receipt and its per-target rows',
                     'accessed_at': timestamp, 'support': 'supports', 'summary': summary, 'snapshot_sha256': sha(path)})
review = {'schema_version': '1.0.0', 'review_id': review_id, 'kind': 'repository',
          'repository': inspection['repository'], 'title': 'Independent exact W03 #1226/#1246 successor assembly review',
          'started_at': json.loads((A/'preflight-inputs-v1.json').read_text())['at'].replace('+00:00', 'Z'),
          'finished_at': timestamp,
          'reviewer': {'identity': '/root/provenance_assembly', 'kind': 'agent', 'independence': 'independent',
                       'independence_basis': 'Separate in-process agent with no authorship of the successor, private writer, source proposals or other reviewers receipts. Independently read task, schema, helper diff, actual payloads and exact final core; executed separate full-value/capture/accounting checks. No source science or own-origin approval is granted.'},
          'skill': 'reconcile-review-records', 'completion': 'completed', 'verdict': 'pass_with_limitations',
          'native_verdict': 'EXACT_CORE_AND_PAYLOAD_METADATA_SUCCESSOR_ACCEPTABLE_PENDING_DETACHED_SEAL_VERIFICATION',
          'scientific_review': False,
          'summary': 'The exact complete selector preserves all188 source-decision bytes, updates49 of74 selected payloads only by one mapping-evidence type plus one truthful appended event each, and retains863 predecessor evidence objects with5 new metadata-review receipts. All25 unchanged payloads, three inherited manual objects, two correct Oxoid objects and authentic new-owner/retirement provenance survive. The v2 private writer binds old bytes before writing. No new confirmed finding in this bounded review; final HANDOFF/manifest/transport and eventual committed/remote bytes require detached verification.',
          'source': inspection['source'],
          'scope': {'description': 'Four exact report interfaces covering all188 source decisions, all74 payload proposals and868 evidence entries, plus the task-private helper repair. This is metadata/preservation assembly review, not scientific reassessment.',
                    'selection': 'Entire final issue1226-v1 core at declared hashes; no sampling. Full per-case and per-payload accounting retained in final-core-verification-v1.json.',
                    'coverage': 'full', 'population_size': 4, 'reviewed_target_ids': ['decisions', 'proposals', 'evidence', 'helper'],
                    'exclusions': [{'target': 'Scientific validity and whole-owner/role/export/coalescence approval', 'reason': 'All scientific assertions and existing holds are inherited unchanged; this review has no new primary-source science scope.'},
                                   {'target': 'Final HANDOFF/MANIFEST/SHA256SUMS and future commit/remote head', 'reason': 'Not yet created at this core review; separate immutable seal/publication receipts required.'}]},
          'targets': targets,
          'checks': [
              {'check_id': 'independent-core', 'name': 'Full exact core, capture and baseline preservation', 'status': 'passed', 'required': True, 'summary': '188 cases,74 proposals,868 captures;863 old evidence objects preserved;15702 regular tracked files plus1 tracked symlink and3028 ignored-inclusive maintained files unchanged.', 'target_ids': ['decisions', 'proposals', 'evidence'], 'command': 'PYTHONDONTWRITEBYTECODE=1 .temp/all-unmatched-worker-03/env/bin/python .temp/w03-provenance-successor-v1/assembly/verify_final_core_v1.py reports/all_unmatched_20261107/worker-03/successors/issue1226-v1', 'exit_code': 0, 'expected_exit_code': 0, 'evidence_ids': ['core']},
              {'check_id': 'independent-payloads', 'name': 'Full payload rollback and exclusion check', 'status': 'passed', 'required': True, 'summary': '49 enum substitutions plus49 append-only history objects;25 byte-identical; all44 issue-first checkpoint members retained.', 'target_ids': ['proposals'], 'command': 'PYTHONDONTWRITEBYTECODE=1 .temp/all-unmatched-worker-03/env/bin/python .temp/w03-provenance-successor-v1/assembly/verify_payload_scope_v1.py', 'exit_code': 0, 'expected_exit_code': 0, 'evidence_ids': ['payloads']},
              {'check_id': 'guard-review', 'name': 'Independent exact code and peer-control adjudication', 'status': 'passed', 'required': True, 'summary': 'All36 original test ASTs unchanged; explicit37th control establishes no native write and no output on before-byte mismatch. Direct code inspection confirms receipt uses validated bytes.', 'target_ids': ['helper'], 'evidence_ids': ['guard', 'technical'], 'scope_note': 'No redundant unchanged control execution by this assembly reviewer; actual peer log and full tests inspected.'}],
          'evidence': evidence,
          'assessments': [
              {'assessment_id': 'case-scope', 'area': 'scope', 'topic': 'Historical source-review and holds retained', 'outcome': 'supported', 'summary': 'Every source decision and entire decisions file are byte-identical. The68 cases linking changed payloads lack an old reviewed_after_sha256 claim; their actual source-scoped historical reviews remain valid as history, not new payload approval.', 'target_ids': ['decisions'], 'evidence_ids': ['core']},
              {'assessment_id': 'payload-provenance', 'area': 'provenance', 'topic': 'Narrow correction and authentic review bindings', 'outcome': 'supported', 'summary': 'All49 changed proposals bind actual new bytes and separate provenance-only review; full old proposal/reviewer objects remain in bridge. Every other field survives full rollback. Three human manual objects and unchanged genuine new-owner Oxoid/nullbefore remain excluded; retired mixed RCM is inactive.', 'target_ids': ['proposals'], 'evidence_ids': ['core', 'payloads', 'peer', 'technical']},
              {'assessment_id': 'capture-retention', 'area': 'consistency', 'topic': 'Complete evidence/accounting transport inputs', 'outcome': 'supported', 'summary': 'All868 evidence capture bytes resolve under declared roots and match pinned hashes, with863 unchanged predecessor objects and5 distinct new provenance/validation objects. No original source capture is repurposed as new scientific inspection.', 'target_ids': ['evidence'], 'evidence_ids': ['core']},
              {'assessment_id': 'private-helper', 'area': 'provenance', 'topic': 'Issue-first private helper repair #1246', 'outcome': 'supported', 'summary': 'Fresh source bytes are validated, compared to prepared.old_bytes before native writing, and used for receipt before hash. Original helper,23/36 failed runs and false receipt fixture remain immutable;37 meaningful peer controls pass.', 'target_ids': ['helper'], 'evidence_ids': ['guard', 'technical', 'payloads']}],
          'findings': [], 'actions': [],
          'limitations': ['No scientific identity/form/stock/product/component/quantity/role or supported-export approval is renewed. This metadata review does not claim unread primary papers were inspected.',
                          'All W03-origin scientific rows are author-related at campaign level; no independent scientific self-approval or final cross-shard merge approval follows.',
                          'Native schema/partonomy PASS supplies structural evidence only. Exact field equality establishes retention, not truth of inherited chemistry.',
                          'Native YAML serialization reflows scalars in changed payloads. Retention is semantic object/history-prefix equality for49; exact bytes are retained for25 unaffected payloads.',
                          'Helper boundary assumes a single-author private task; no atomicity or hostile-concurrency guarantee.',
                          'Ignored files were included within data/ingredients,data/curated,mappings. No absence claim for historical/private files outside those roots; credentials were not scanned.',
                          'Native review pair is validated/rendered and virtually parsed under canonical path in the allowed private review directory. Canonical save and repository-wide review scan are not performed because this task permits writes only under this private output directory.',
                          'Issue1246 repair is supported only for exact helper v2; issue1226 scope is49 W03 entries only. No GitHub issue closure or other workers correction is claimed.',
                          'Final seal and publication checks remain separate; this review does not assert that candidate bytes are already committed.'],
          'notes': ['Preserved reviewer emission error: initial inline checkpoint verification used wrong symlink descriptor key and produced no proof; corrected read-only check was rerun successfully. No source/payload mutation or failed test hidden.',
                    'The final-core diagnostic review_scope summary key is null where the proposal uses review_scope rather than scope; the actual full independent_review object was read and scientific_review=false explicitly verified. This does not change the selector or review metadata.'],
          'links': ['https://github.com/CultureBotAI/MediaIngredientMech/issues/1226', 'https://github.com/CultureBotAI/MediaIngredientMech/issues/1246']}
native.validate_review(review)
native.assert_current_source(R, review)
raw = yaml.safe_dump(review, sort_keys=False, allow_unicode=True, width=100).encode()
markdown = native.render_markdown(review).encode()
native.parse_review_bundle('reviews/structured/'+review_id+'/review.yaml', raw, markdown)
with (A/'review.yaml').open('xb') as f: f.write(raw)
with (A/'review.md').open('xb') as f: f.write(markdown)
with (A/'native-review-validation-v1.json').open('x') as f:
    json.dump({'status': 'PASS', 'review_id': review_id, 'review_sha256': sha(A/'review.yaml'),
               'markdown_sha256': sha(A/'review.md'), 'native_calls': ['inspect_source', 'validate_review', 'assert_current_source', 'render_markdown', 'parse_review_bundle (virtual canonical path)'],
               'canonical_save_performed': False, 'scientific_review': False}, f, indent=2); f.write('\n')
print(json.dumps({'review_id': review_id, 'review_sha256': sha(A/'review.yaml'), 'markdown_sha256': sha(A/'review.md')}))
