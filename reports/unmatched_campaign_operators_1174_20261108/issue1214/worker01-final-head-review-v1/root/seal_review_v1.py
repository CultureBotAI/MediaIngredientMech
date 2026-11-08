"""Seal the private, read-only PR1205 review and preserve all probe evidence."""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess

WORKER = Path.cwd()
OUT = WORKER / '.temp/infrastructure-pr1205-final-head-review-v1'
TARGET = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/integration/worktree')
HEAD = '4c8a987da40d48cceeb4390550f1ff7545927a0b'
BASE = 'e000d66dd26ab053e9b17ce7bf8d3c873c3dde99'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
read = lambda p: json.loads(p.read_text())

transport = read(OUT / 'skeptical/skeptical-final-head-review-v1.json')
archive = read(OUT / 'archive/archive-review-v1.json')
bindings = read(OUT / 'skeptical/complete-diff-and-bindings-v1.json')
publisher = read(OUT / 'publisher/review.json')
finding = read(OUT / 'publisher/finding-001-backup-integrity.json')
skeptical_finding = read(OUT / 'skeptical/skeptical-backup-finding-addendum-v1.json')
live = read(OUT / 'root/final-live-state-v1.json')
assert live['pr']['headRefOid'] == live['integration_head'] == HEAD
assert live['pr']['baseRefOid'] == BASE
assert live['worker_head'] == '26445f23b5a905ac26d864acfbd658570c88769c'
assert not live['worker_status'] and not live['integration_status']
assert len(bindings['seven_final_code_bindings']) == 7
for item in bindings['seven_final_code_bindings']:
    current = TARGET / item['path']
    committed = subprocess.check_output(['git', '-C', str(TARGET), 'show', HEAD + ':' + item['path']])
    assert current.read_bytes() == committed
    assert sha(current) == item['sha256'] and item['matches_archived_final_review']
assert archive['counts']['unique_files'] == 240
assert archive['counts']['source_entries'] == 319
assert not archive['findings'] and not archive['integrity']['archive_errors']
assert finding['finding_id'] == skeptical_finding['finding']['id'] == 'IR-PR1205-PUBLISHER-001'
assert (OUT / 'publisher/backup-integrity-probe-result.json').read_bytes() == (OUT / 'skeptical/backup-integrity-probe-result.json').read_bytes()

proof_paths = [
    'root/local-state.json', 'root/final-live-state-v1.json', 'root/pr1205-start.json',
    'root/diff-name-status.tsv', 'root/complete.diff', 'root/commit-history.txt',
    'root/owner-operator-review-v1.json',
    'skeptical/skeptical-final-head-review-v1.json',
    'skeptical/complete-diff-and-bindings-v1.json',
    'skeptical/skeptical-backup-finding-addendum-v1.json',
    'archive/archive-review-v1.json', 'archive/audit-summary-v1.json',
    'publisher/review.json', 'publisher/finding-001-backup-integrity.json',
    'publisher/finding-001-backup-integrity-addendum-v1.json',
    'publisher/backup-integrity-probe-result.json',
    'skeptical/backup-integrity-probe-result.json',
]
proofs = [{'path': p, 'sha256': sha(OUT / p)} for p in proof_paths]
result = {
    'schema_version': 1,
    'sealed_at': datetime.datetime.now(datetime.UTC).isoformat(),
    'result': 'review_complete_with_one_open_P2_local_finding',
    'pr': 'https://github.com/CultureBotAI/MediaIngredientMech/pull/1205',
    'reviewed_head': HEAD,
    'base': BASE,
    'read_only_target': str(TARGET),
    'private_review_root': str(OUT),
    'worker01_preserved_head': live['worker_head'],
    'reviewers': [
        {'identity': '/root', 'scope': 'Complete owner operator, owner tests and CLI; publisher backup-path cross-check; synthesis and final input verification.'},
        {'identity': '/root/primary_context', 'scope': 'Complete publisher, its two CLIs and tests; archived regression evidence; original three-case private backup probe.'},
        {'identity': '/root/issue_context', 'scope': 'Every archive selection mapping, original copy, deduplication group, archive inventory, privacy/exclusion check and retained failure/review history.'},
        {'identity': '/root/skeptical_review', 'scope': 'Independent live head/base, complete diff, baseline preservation, all final snapshot bindings; separate private reproduction of the backup finding.'},
    ],
    'independence': 'Worker01 root and these in-process reviewers authored neither new operator. Archived author/reviewer identities are retained separately. This is not a human expert sign-off or a new external session.',
    'head_and_diff': {
        'current_local_remote_pr_head_and_base_match': True,
        'pr_state': live['pr']['state'],
        'pr_is_draft': live['pr']['isDraft'],
        'all_changes_are_additions': True,
        'total_changed_paths': 249,
        'new_code_test_cli_paths': 7,
        'archive_paths_including_readme_and_selection': 242,
        'all_baseline_regular_files_unchanged': 14405,
        'both_baseline_symlink_targets_unchanged': True,
        'maintained_data_workflows_pins_thresholds_and_existing_gates_unchanged': True,
        'no_code_delta_since_exact_archived_final_rereview': True,
        'final_commit_adds_archive_only': True,
    },
    'seven_exact_code_bindings': bindings['seven_final_code_bindings'],
    'archive': {
        'declared_selection_is_authoritative': True,
        'selection_sha256': archive['selection']['sha256'],
        **archive['counts'],
        'all_originals_and_copies_match': True,
        'all_archive_bytes_match_head': True,
        'duplicate_groups_explicit_and_consistent': True,
        'ignored_and_hidden_files_included': True,
        'private_account_runtime_capture_or_fixture_git_tree_found': False,
        'historical_fixture_git_references_preserved_but_not_copied': 323,
        'failed_probes_and_limitations_retained_honestly': True,
        'scope_limit': 'Archive contents and bounded credential/runtime-signature checks were examined; this is not a universal secret-absence guarantee. Historical paths can refer to deliberately excluded fixtures and require reconstruction for replay.',
    },
    'regression_review': {
        'issues': [1194, 1195, 1197, 1198, 1200],
        'assessment': 'Original failures, intermediate unsuccessful repairs, final exact-source regression assertions and repaired independent evidence were reconciled. Existing fixes remain supported within their documented scopes. The new backup-content gap is separately recorded.',
        'new_executions': 'Only the narrow private three-case backup probe and a separate skeptical reproduction. Both used exact head code with existing synthetic owner-proof and external-generation stubs; actual publication, output guards, receipt replay and validation ran.',
        'not_rerun': ['Full repository suite', 'Full QC', 'Archived 88-test owner suite', 'Archived 106-test publisher suite', 'Archived native generation or actual campaign publication'],
    },
    'findings': [{
        'id': finding['finding_id'],
        'priority': 'P2',
        'status': 'open_locally_filed_and_independently_reproduced',
        'path': 'publisher/finding-001-backup-integrity.json',
        'sha256': sha(OUT / 'publisher/finding-001-backup-integrity.json'),
        'summary': 'Either reserved recovery backup can be overwritten in place before completion without refusal. Publication returns complete and standalone projected-state validation returns verified.',
        'impact_boundary': 'Recovery-copy integrity only. Immutable plan beforeimages remain correct; no incorrect canonical projection, owner identity or scientific approval bypass was demonstrated.',
        'required_followup': 'Coordinator should disposition the bounded backup-content guard and regression coverage. No repair or GitHub filing was performed by worker01.',
    }],
    'limitations': [
        'No scientific source-case, owner, ontology, alias, role, mapping, supported-export, publication, release or merge approval.',
        'No full suite, full QC or all-green CI assertion. Their ongoing coordinator workflows are separate; saved live CI observations are point-in-time context only.',
        'Infrastructure review and exact-byte agreement do not imply absence of every possible defect.',
        'The source operator is recoverable rather than transactional; explicit recovery remains required for failed partial application.',
        'The source acceptance contract binds a supplied ledger and accepted bytes; the coordinator still establishes full campaign completeness and scientific adequacy.',
        'The skeptical first probe setup used a symlinked package and was correctly refused; that failed harness attempt is retained, followed by the successful exact copied-input reproduction.',
    ],
    'mutations': {
        'integration_code_data_or_git': False,
        'published_worker_files_or_head': False,
        'github': False,
        'commits_pushes_checkouts_or_merges': False,
        'external_sessions_paid_providers_or_session_controls': False,
        'only_writes': 'New private review artifacts, exact input copies and synthetic probe fixtures under the requested worker .temp directory.',
    },
    'proofs': proofs,
    'bundle_manifest': 'MANIFEST.json',
    'next_step': 'Await coordinator collection and disposition of the local finding.',
}
review_path = OUT / 'REVIEW.json'
assert not review_path.exists()
review_path.write_text(json.dumps(result, indent=2) + '\n')

lines = [
    '# PR1205 private independent review', '',
    f'Reviewed head `{HEAD}` against base `{BASE}`. Live PR, remote refs and the local integration checkout matched these exact commits at the final capture. The accepted worker01 head remains `{live["worker_head"]}`.', '',
    '**Result: review complete with one open P2 finding.** Exact-head transport, complete diff, final snapshot bindings and archive selection checks passed. The substantive publisher review found a recovery-backup content gap, reproduced independently in two private environments.', '',
    '`IR-PR1205-PUBLISHER-001`: changing either `canonical-before.tsv` or `policy-before.json` in place immediately before the real final receipt routine leaves the same inode and is not rejected. Publication returns `complete`; its log says `complete`; separate validation returns `verified`. The original accepted plan beforeimages remain correct, so this is a recovery-copy integrity defect. It does not demonstrate an incorrect canonical projection or a scientific approval bypass. See [finding](publisher/finding-001-backup-integrity.json), [exact line/digest addendum](publisher/finding-001-backup-integrity-addendum-v1.json), and [independent reproduction](skeptical/skeptical-backup-finding-addendum-v1.json).', '',
    'The complete diff contains 249 additions: seven code/test/CLI files and 242 archive files including README and SELECTION. All seven functional files match the final reviewed snapshots. The three CLIs are stored under an older archive directory because identical bytes were explicitly deduplicated; their final snapshot manifests bind those same hashes. No code changed after the archived final re-review. All 14,405 baseline regular files and both tracked symlink targets remain unchanged, including maintained data, workflows, pins and existing gates.', '',
    'SELECTION declares 319 original-path mappings to 240 unique selected files, totaling 9,117,270 bytes. Every original was available and matched its selected copy. The 79 duplicate mappings across 45 groups are explicit and consistent. The complete ignored-inclusive archive inventory found no private account/runtime captures or fixture Git trees. Historical manifests retain references to excluded fixtures, and the README explains that distinction. Failed probes, incomplete repairs and stale-fixture refusals remain available with honest scope limitations.', '',
    'The fixes associated with #1194, #1195, #1197, #1198 and #1200 have relevant positive/negative regression assertions and bound repaired evidence. Archived test results remain attributed to their actual authors and reviewers. This review did not repeat the full suite or full QC; new execution was limited to the narrow backup probe and its independent reproduction. The private probe stubs owner proof and external generation, while exercising the real publisher, reservation guards, projection, policy, native receipt replay and completion checks.', '',
    'Reviewer scopes and all exact input/evidence hashes are recorded in [REVIEW.json](REVIEW.json). The owner operator was reviewed by worker01 `/root`; publisher by `/root/primary_context`; archive by `/root/issue_context`; head transport and an independent backup reproduction by `/root/skeptical_review`. None authored either new operator.', '',
    'No maintained code/data, published worker artifact, branch, PR or GitHub issue was changed. CI, full QC, full-suite completion and scientific/publication approval remain separate. This immutable private bundle awaits coordinator collection.', '',
]
(OUT / 'REVIEW.md').write_text('\n'.join(lines))

manifest_path = OUT / 'MANIFEST.json'
assert not manifest_path.exists()
files = []
for p in sorted(OUT.rglob('*')):
    if p.is_symlink():
        raise AssertionError(f'Unexpected symlink in sealed private review: {p}')
    if p.is_file():
        files.append({'path': str(p.relative_to(OUT)), 'sha256': sha(p), 'bytes': p.stat().st_size})
manifest = {'schema_version': 1, 'sealed_at': datetime.datetime.now(datetime.UTC).isoformat(),
    'review_sha256': sha(review_path), 'head': HEAD, 'base': BASE,
    'scope': 'All regular files in this private review, including exact-code copies and retained synthetic probe fixtures. Hidden and ignored files included. The manifest excludes itself; nothing here is published to Git or GitHub.',
    'file_count': len(files), 'files': files}
manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')
for item in files:
    assert sha(OUT / item['path']) == item['sha256']
print(json.dumps({'review': str(review_path), 'review_sha256': sha(review_path),
                  'manifest_sha256': sha(manifest_path), 'manifest_files': len(files),
                  'result': result['result']}, indent=2))
