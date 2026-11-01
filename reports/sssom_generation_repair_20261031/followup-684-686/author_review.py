from pathlib import Path
import copy
import datetime
import hashlib
import json
import shlex
import yaml

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
MIM = RUN / 'mim'
REPORT = MIM / 'reports/sssom_generation_repair_20261031/followup-684-686'
REPO = 'CultureBotAI/MediaIngredientMech'
PRIOR = '20261031T233012Z-sssom-native-repair-mechanical'
now = lambda: datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
accessed = now()
inspection = json.loads((RUN / 'logs/followup_review_inspect.log').read_text())
prior = yaml.safe_load((MIM / 'reviews/structured' / PRIOR / 'review.yaml').read_text())
for item in inspection['source']['inputs']:
    assert hashlib.sha256((MIM / item['path']).read_bytes()).hexdigest() == item['sha256'], item['path']
evidence = []
checks = []

def ev(eid, path, summary, kind='validation', support='supports'):
    path = Path(path)
    if not path.is_absolute():
        path = REPORT / path
    evidence.append(dict(evidence_id=eid, kind=kind,
        reference=str(path.relative_to(MIM)), accessed_at=accessed, support=support,
        summary=summary, snapshot_sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
    return eid

def check(name, targets, summary, required=True, expected=0):
    meta = json.loads((REPORT / 'logs' / f'{name}.json').read_text())
    log = REPORT / 'logs' / f'{name}.log'
    assert hashlib.sha256(log.read_bytes()).hexdigest() == meta['log_sha256']
    matched = meta['exit_code'] == expected
    eid = ev('log-' + name, log, summary, support='supports' if matched else 'context_only')
    checks.append(dict(check_id=name, name=name.replace('_', ' '), status='passed' if matched else 'failed',
        required=required, summary=summary, target_ids=targets,
        command='cd ' + shlex.quote(meta['cwd']) + ' && ' + shlex.join(meta['argv']),
        exit_code=meta['exit_code'], expected_exit_code=expected, evidence_ids=[eid],
        scope_note=f"Actual run {meta['started_at']} through {meta['finished_at']}; original log at {meta['log']}."))

check('followup_generate_candidate', ['candidate'], 'Unmodified native builder at committed 9294730, verified target and owned lock, generated 2,980 rows at a new path. Generator source SHA is identical before and after invocation.')
check('followup_candidate_invariants', ['candidate'], 'Strict native rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L pass with header-only reject TSV. Default-path B4 skip is supplemented separately.')
check('followup_candidate_schema', ['candidate'], 'SSSOM JSON Schema, prefix completeness and strict CURIE validation pass; native extension notices retained.')
check('followup_candidate_curie', ['candidate'], '2,980 rows / 5,960 CURIEs pass native syntax and prefix checks.')
check('followup_candidate_products', ['candidate'], 'Unchanged configured native label policy passes: 2,216 canonical, four synonym, four exception pairs; 3,736 no-adapter skips remain.')
check('followup_compare_candidates_final', ['canonical', 'candidate'], 'Final comparison proves exactly one alias replacement since the previous repaired candidate; 2,979 rows identical; no row dates, headers, predicates or other fields change. Original 41 diagnostic dispositions remain satisfied and native drift is zero.')
check('followup_full_qc', ['canonical'], 'Full native just qc passes on unchanged maintained data, including roundtrip and flat coverage. Candidate validation is separate.')
check('followup_baseline_curie', ['canonical'], 'Canonical 2,987 rows / 5,974 CURIEs pass; 20 tests passed and one skipped.')
check('followup_baseline_reconcile', ['canonical'], 'Canonical GAP, ORPHAN, STALE, PREDICATE and GRADE counts are all zero.')
check('followup_baseline_products', ['canonical'], 'Full product enforcement passes with 101 nonblocking warnings and 5,314 no-adapter skips.')
check('followup_baseline_subjects', ['canonical'], 'Native checker retains 18 non-gating subject/filename warnings among 2,611 subjects and 2,953 record files.', False)
check('followup_candidate_b4_actual', ['candidate'], 'Native B4 with actual read-only KG transforms reports zero findings; missing BTO/MICRO transforms and absent-ID skips remain.', False)
check('followup_baseline_b4_actual', ['canonical'], 'Actual-path native B4 reports zero canonical findings with the same limits.', False)
check('followup_rule_f_integration', ['candidate'], 'Native YAML extraction and CLI writer retain two dateless synthetic records alongside one dated record. Unmodified native Rule F returns both dateless subjects and writes two rejects; Rule G returns zero.')
check('followup_focused_restored', ['candidate'], 'All 84 focused regression tests pass on final source restored after mutation checks.')
check('followup_lint', ['candidate'], 'Repository-pinned Ruff passes for the final code.')
check('followup_mypy', ['candidate'], 'Native maintained type-check command passes.')
check('followup_full_tests', ['candidate'], 'Full CLAW CI-style suite passes on exact final head; this checks code behavior, not scientific approval.')
if (REPORT / 'logs/followup_safety_coverage.json').exists():
    check('followup_safety_coverage', ['candidate'], 'Native safety-module coverage gate passes.')
check('followup684_mutation', ['candidate'], 'Reverting registry namespace repair produces the expected test failure.', False, 1)
check('followup686_mutation_mapping_date', ['candidate'], 'Reverting the header mapping_date behavior produces the expected regression failure.', False, 1)
check('followup686_mutation_mapping_set_version', ['candidate'], 'Reverting the header mapping_set_version behavior produces the expected regression failure.', False, 1)
check('followup_compare_candidates', ['candidate'], 'Initial diagnostic helper assertion omitted the legitimate historical-stamp removal on the new alias; it failed before writing comparisons. Final helper explicitly verifies that removal.', False)
ev('prior-review', MIM / 'reviews/structured' / PRIOR / 'review.yaml', 'Immutable prior review; all affected candidate target IDs and original issue keys are preserved.', 'prior_review', 'context_only')
ev('comparison', 'candidate-comparison.json', 'Exact separate comparisons with previous repaired candidate, original rejected candidate and canonical mapping.', 'record_content')
ev('previous-changes', 'previous-candidate-changes.json', 'Removed compound alias and added ingredient alias, with corresponding source/comment changes and blank validation_method on the new triple. Curated identifier and parent relation unchanged.', 'record_content')
ev('remediation', 'original-41-remediation.json', 'All 28 B5, eleven K and two G original diagnostics retain exact selectors and current outcomes.', 'record_content')
ev('inputs', 'validation-inputs.json', 'Exact current input revisions/hashes, including MIM records, aggregate/canonical/release inputs, KG unified mapping, comparison-only CM/Mediadive data and ontology DBs.', 'record_content')
ev('generation', 'generation-result.json', 'Committed generator head 9294730aeb19d269899177678db87406f4251555 and identical before/after source hashes bind this fresh native candidate.', 'validation')
ev('date-contract', 'date-contract.json', 'Explicit issue 686 decision: preserve blank dates for native Rule F in mixed sets; no clock fallback; reject all-dateless or malformed emitted dates before writing.', 'authority')
ev('rule-f-proof', 'rule-f-integration/receipt.json', 'Real native extraction/writer plus native validator proof, with exact synthetic row/reject hashes.', 'validation')
ev('independent-review', 'adversarial-review-code.json', 'Independent adversarial review of exact 9294730 found no new defects, with scientific and rule-coverage limitations retained.', 'prior_review')
ev('preservation', 'post-validation-preservation.json', 'Original repositories, current scientific inputs and all 87 pre-existing evidence files remain unchanged; separate live PR file overlap remains empty.', 'validation')
ev('holds', 'historical-rule-k-holds.json', 'Eleven historical corresponding canonical rows remain WITHHOLD; mechanical fixes do not clear release holds.', 'prior_review', 'context_only')
ev('semantics', MIM / 'MAPPING_SEMANTICS.md', 'Identity/predicate/synonym contracts and per-row curator reject process.', 'authority')
ev('pinned-release', MIM / 'reports/sssom_completion_20260921/review.json', 'Pinned scientific release input remains unchanged; not a new approval.', 'prior_review', 'context_only')
for target in inspection['targets']:
    ev('target-' + target['target_id'], MIM / target['path'], 'Exact inspected ' + target['label'] + '.', 'record_content')

findings = []
for old in prior['findings']:
    f = copy.deepcopy(old)
    f.update(previous_occurrences=[dict(repository=REPO, review_id=PRIOR, finding_id=old['finding_id'])],
        evidence_ids=['prior-review', 'remediation', 'comparison', 'log-followup_candidate_invariants', 'generation'],
        description='Reconfirmed on the newly generated exact 9294730 candidate. All original affected candidate selectors are retained below; removed historical rows intentionally lack a current counterpart. ' + old['disposition_reason'],
        disposition_reason='The new candidate independently satisfies every original diagnostic disposition, with native invariants passing. The additional stock B1 alias intentionally changes namespace and receives no copied validation stamp; all maintained primary identities and parent predicates remain unchanged. Historical scientific holds are not cleared.')
    findings.append(f)

assessments = [
    dict(assessment_id='canonical-preserved', area='consistency', topic='Canonical source remains unchanged and passes native QC', outcome='supported', target_ids=['canonical'],
        evidence_ids=['target-canonical', 'preservation', 'log-followup_full_qc', 'log-followup_baseline_reconcile', 'log-followup_baseline_products'],
        summary='Canonical remains 2,987 rows at its prior hash; MIM records, aggregates, unified mapping, release review and original source checkouts are preserved. Full native QC and source validators pass.'),
    dict(assessment_id='candidate-current', area='consistency', topic='Final-head diagnostic candidate and exact delta', outcome='supported', target_ids=['candidate'],
        evidence_ids=['target-candidate', 'generation', 'comparison', 'previous-changes', 'remediation', 'log-followup_candidate_invariants', 'log-followup_candidate_products'],
        summary='Candidate contains 2,980 rows. Versus prior repaired output, 2,979 are identical; the stock B1 alias changes compound to ingredient namespace, object_source/comment follow that namespace, and its historical UNKNOWN_TERM stamp is not copied to a new triple. No date, header, predicate or other-token changes. All original 41 diagnostics remain resolved and native drift is zero.'),
    dict(assessment_id='date-diagnostics', area='provenance', topic='Issue 686 native date and curator-review contract', outcome='supported', target_ids=['candidate'],
        evidence_ids=['date-contract', 'rule-f-proof', 'log-followup_rule_f_integration', 'log-followup_focused_restored', 'independent-review'],
        summary='ASCII calendar-valid histories determine maximum row dates. Mixed dateless rows remain explicit blanks for native Rule F rejection; an all-dateless set or malformed nonempty emitted dates are reported completely before writing. This run has no date changes; synthetic native integration proves both missing-date rejects without altering real source data.'),
    dict(assessment_id='code-validation', area='consistency', topic='Final generator checks and independent review', outcome='supported', target_ids=['candidate'],
        evidence_ids=['independent-review', 'log-followup_focused_restored', 'log-followup_lint', 'log-followup_mypy', 'log-followup_full_tests'],
        summary='Committed final generator passes focused tests, detected mutations, native lint/type checks, full CI-style suite and independent adversarial review. This assessment is mechanical and grants no scientific status.'),
    dict(assessment_id='limits-preserved', area='scope', topic='Historical holds and incomplete adapter coverage retained', outcome='supported', target_ids=['canonical', 'candidate'],
        evidence_ids=['holds', 'pinned-release', 'log-followup_candidate_products', 'log-followup_baseline_products', 'log-followup_baseline_subjects', 'log-followup_candidate_b4_actual'],
        summary='Candidate is not promoted. Scientific WITHHOLD decisions and prior validation stamps remain historical. Baseline retains 101 label warnings, 5,314 no-adapter skips and 18 non-gating subject warnings; candidate retains 3,736 no-adapter skips. Actual-path B4 omits BTO/MICRO and absent IDs under native semantics.'),
]
finished = now()
rid = finished.replace('-', '').replace(':', '') + '-sssom-followup-684-686'
review = dict(schema_version='1.0.0', review_id=rid, kind='repository', repository=REPO,
    title='SSSOM follow-up 684–686: final-head mechanical verification with source and review preservation',
    started_at=(HERE / 'review-started-at.txt').read_text().strip(), finished_at=finished,
    reviewer=dict(identity='Codex validation agent /root/sssom_validation', kind='agent', independence='not_applicable',
        independence_basis='Validation/provenance task separate from generator implementation; this agent advised the date contract and authored earlier K tests. Independent code review is separately attributed. No scientific-review independence claimed.'),
    skill='.claude/skills/review-sssom-output/SKILL.md', completion='completed', verdict='pass_with_limitations',
    native_verdict='Current final-head diagnostic candidate passes native checks; original findings remain resolved; scientific holds unchanged', scientific_review=False,
    summary='Canonical 2,987 rows remain unchanged. A new 2,980-row candidate from committed 9294730 passes native checks; exactly one generated stock alias namespace changes relative to the prior repaired output, with no inherited stamp for that new triple. All original 41 diagnostic outcomes remain satisfied. No promotion or scientific status change.',
    source=inspection['source'], scope=dict(description='Bounded mechanical successor review of exact canonical and final 9294730 diagnostic output.',
        selection='Two exact TSV targets with all rows evaluated by applicable native gates; original B5/K/G candidate finding identities and affected selectors retained.',
        coverage='full', population_size=2, reviewed_target_ids=['canonical', 'candidate'], exclusions=copy.deepcopy(prior['scope']['exclusions'])),
    targets=inspection['targets'], checks=checks, evidence=evidence, assessments=assessments, findings=findings, actions=[],
    limitations=[
        'Mechanical verification does not approve identities, relation scope, historical validation stamps or scientific release claims. Candidate is not promoted.',
        'CultureMech ingredient outputs and KG Mediadive nodes are comparison-only inputs; raw generation consumes maintained MIM records, copied residual classifications and actual KG unified mappings plus ontology labels. No bulk import.',
        'Actual-path B4 retains native absent-ID skips and missing BTO/MICRO transforms. Configured label no-adapter skips, 101 baseline warnings and 18 subject warnings remain.',
        'Generated full candidates and large inputs remain local diagnostic artifacts. Saved working-tree hashes attest inspected bytes and do not claim full outputs are committed.',
        'Canonical-versus-candidate differences are broader than this follow-up. This is not an approved replacement for canonical or the supported/withheld partition.',
        'Native B5 groups by subject and slug, not subject alone; targeted regression tests and exact delta review cover the different-slug namespace defect without silently redefining the downstream validator.',
        'The first comparison helper run failed an overstrict stamp assertion; an intermediate summary reused a loop variable. Both setup receipts are retained; final comparison explicitly verifies the alias and blank stamp, with all native validators unaffected.'
    ],
    related_reviews=[dict(repository=REPO, review_id=PRIOR, relationship='Reconfirms the same three original finding keys on a newly generated final-head candidate; prior review bytes remain immutable.')],
    links=['https://github.com/CultureBotAI/culturebotai-claw/issues/' + str(n) for n in range(679, 687)],
    tags=['sssom', 'mechanical-review', 'append-only-evidence', 'historical-holds-preserved'])
(HERE / 'completed-review.json').write_text(json.dumps(review, indent=2) + '\n')
paths = dict(review_id=rid, review_yaml=str(MIM / 'reviews/structured' / rid / 'review.yaml'),
             review_markdown=str(MIM / 'reviews/structured' / rid / 'review.md'), report=str(REPORT))
(HERE / 'review-result.json').write_text(json.dumps(paths, indent=2) + '\n')
print(json.dumps(paths, indent=2))
