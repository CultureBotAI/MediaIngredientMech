"""Assemble attributed review results; does not alter any reviewed bytes."""
import datetime
import hashlib
import json
from pathlib import Path

W = Path.cwd()
O = W / '.temp/nine-scope-candidates-independent-v1'
C = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
A = C / 'assignments/w01-nine-scope-candidates-independent-v1.json'


def read(name):
    return json.loads((O / name).read_text())


def bind(name):
    p = Path(name)
    if not p.is_absolute():
        p = O / p
    return {'path': str(p), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}


def save(name, value):
    with (O / name).open('x') as f:
        f.write(json.dumps(value, indent=2, ensure_ascii=False) + '\n')


a = json.loads(A.read_text())
p = Path(a['packet'])
science = read('science/science-review-v1.json')
technical = read('technical/REVIEW-v4.json')
skeptical = read('skeptical/final-nine-review-v1.json')
accounting = read('root/complete-nine-accounting-v1.json')
source_state = read('root/source-currentness-and-beforeimages-v1.json')
matrix = []
assessments = {r['candidate_id']:r for r in science['candidate_matrix']}
assert len(assessments) == len(a['candidates']) == 9
for r in a['candidates']:
    sid = r['candidate_id']
    sr = assessments[sid]
    actual = bind(p / r['candidate']['path'])
    assert actual['sha256'] == r['candidate']['sha256'] == sr['candidate']['sha256']
    assert set(sr['case_ids']) == set(r['case_ids'])
    assert set(sr['occurrence_ids']) == set(r['occurrence_ids'])
    matrix.append({
        'candidate_id': sid,
        'owner_path': r['owner_path'],
        'operation': r['operation'],
        'exact_candidate': actual,
        'authentic_before': sr['authentic_before'],
        'original_proposals': sr['original_proposals'],
        'case_ids': r['case_ids'],
        'exposed_occurrence_ids': r['occurrence_ids'],
        'bounded_scientific_disposition': sr['verdict'],
        'supported_correction': sr['supported_correction'],
        'primary_reasoning': sr['primary_science'],
        'source_evidence_ids': sr['source_evidence_ids'],
        'inherited_claims_not_approved': sr['inherited_claims_not_approved'],
        'exact_remaining_requirements': sr['exact_remaining_requirements'],
        'technical_assessment': technical['assessments'][sid],
        'open_exact_finding_ids': ['W01-NINE-PROVENANCE-001'] if sid=='TARGET-024' else [],
        'full_candidate_acceptance': False,
        'whole_owner_approval': False, 'role_approval': False, 'export_approval': False,
        'review_attribution': {
            'primary': bind('science/science-review-v1.json'),
            'technical': bind('technical/REVIEW-v4.json'),
            'independent_skeptic': bind('skeptical/final-nine-review-v1.json'),
        },
    })
assert len({x for r in matrix for x in r['case_ids']}) == 14
assert len({x for r in matrix for x in r['exposed_occurrence_ids']}) == 22

handoff = {
    'schema_version': 'worker01-nine-scope-independent-handoff-v1',
    'created_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'review_result': 'COMPLETE_BOUNDED_REVIEW_WITH_EXISTING_1226_PROVENANCE_HOLD',
    'unqualified_whole_candidate_acceptance': False,
    'author': '/root/next23_context; coordinator candidate author, not a reviewer in this packet',
    'reviewers': [
        {'identity':'OpenAI Codex worker01 /root', 'scope':'Assignment, author seal, complete declared input integrity, original source currentness, authentic beforeimages, accounting and final assembly; direct science reads are itemized in root-assessment-scope-v1.json.', 'human':False, 'candidate_author':False},
        {'identity':'OpenAI Codex worker01 /root/primary_context', 'scope':'Independent full-nine primary scientific review of complete selected payloads, authentic beforeimages, all unique worker origins and applicable primary captures.', 'human':False, 'candidate_author':False},
        {'identity':'OpenAI Codex worker01 /root/issue_context', 'scope':'Independent full-nine schema/history/provenance/guard review; full37-row native partonomy projection;13 coordinator MappingEvidence corrections and33 byte reuses; scoped native Soy alias checks.', 'human':False, 'candidate_author':False},
        {'identity':'OpenAI Codex worker01 /root/skeptical_review', 'scope':'Separate whole-nine skeptical scientific challenge and final synthesis; independent seal/origin/case/occurrence checks; separate reproduction of the retained1226 entry; report-precision re-review.', 'human':False, 'candidate_author':False},
    ],
    'assignment': bind(A),
    'author_seal': read('root/author-seal-verification-v1.json'),
    'counts': accounting['counts'],
    'count_interpretation': accounting['meaning'],
    'full_accounting': bind('root/complete-nine-accounting-v1.json'),
    'matrix': matrix,
    'active_reviews': [bind(x) for x in [
        'science/science-review-v1.json',
        'science/source-cue-semantics-addendum-v1.json',
        'technical/REVIEW-v4.json',
        'technical/review-v4.yaml',
        'technical/review-v4.md',
        'technical/native-review-completion-v1.json',
        'skeptical/final-nine-review-v1.json',
    ]],
    'active_report_rule': 'Read the sealed primary report with the separately bound source-cue semantics addendum: short_extract values are normalized/paraphrased cues, not guaranteed verbatim quotations. The active technical document is v4; earlier failed native serialization/selector attempts remain intact. No historical source or review is overwritten.',
    'native_results': {
        'nine_strict_candidate_schemas':'PASS',
        'full_projected_partonomy':technical['full_projection'],
        'metadata_correction':technical['evidence_correction'],
        'first_publication_history_prefixes':'Preserved for all candidate rows;13 newly authored coordinator evidence objects change type/notes with an appended correction event, without blanket inherited-object replacement.',
        'soy_three_rejected_tokens':'Native resolver, pinned producer and supported-export alias gate reject all three; exact Soybean peptone positive control passes.',
        'guard_negative_controls':'Private changed-input and existing-output sentinels are rejected. Unknown schema field and nonexistent MIM part are rejected in memory.',
        'full_repository_tests':'Not run; no CI result claimed.',
        'receipts':[bind(x) for x in ['technical/native-full-projection-v1.json','technical/mapping-evidence-and-reuse-v1.json','technical/soy-native-alias-probe-v1.json','technical/native-review-completion-v1.json']],
    },
    'open_findings': [{
        'canonical_finding_id':'W01-NINE-PROVENANCE-001',
        'independent_reproduction_alias':'W01-NINE-TECH-001',
        'unique_condition_count':1,
        'severity':'major / native P2',
        'status':'OPEN_EXISTING_ISSUE_DEPENDENCY_NO_REMEDIATION',
        'existing_issue':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1226',
        'candidate_id':'TARGET-024',
        'field':'ontology_mapping.evidence[0].evidence_type',
        'actual':'MANUAL_CURATION',
        'source':'https://mediadive.dsmz.de/rest/ingredient/75',
        'counterexample':'Absent from authentic before; exact entry introduced by W05 materials agent with GPT-6/LLM-assisted authorship and carried into current coordinator candidate unchanged. Human-supplied MappingEvidence provenance is unsupported.',
        'bounded_followup':'Coordinator/W02 should disposition this exact entry under existing1226 before a guarded successor correction, preserve the source URL, meaning, history and original bytes, use the truthful type justified for its actual authorship, then independently review the exact successor. No global enum replacement or ComponentEvidenceType reinterpretation.',
        'independent_receipts':[bind('skeptical/finding-W01-NINE-PROVENANCE-001-v1.json'),bind('technical/finding-retained-worker-evidence-1226-v1.json')],
        'not_a_new_wrong_identity_finding':True,
        'coordinator_13_entry_correction_remains_supported':True,
    }],
    'report_only_observation': {
        'finding_id':'W01-NINE-REPORT-001',
        'original_finding':bind('skeptical/finding-W01-NINE-REPORT-001-v1.json'),
        'correction':bind('science/source-cue-semantics-addendum-v1.json'),
        'disposition':'Resolved in active review interpretation by append-only clarification; final skeptical receipt supplies re-review. Candidate/source science unchanged.',
        'github_issue_created':False,
    },
    'currentness': {
        'receipt':bind('root/source-currentness-and-beforeimages-v1.json'),
        'unique_original_proposals_current':13,
        'all_declared_author_input_hashes_verified':7260,
        'hash_mismatches':len(source_state['declared_input_hash_mismatches']),
        'later_heads_pending':[x for x in source_state['heads'] if not x['selected_head_current']],
        'later_W06_W07_intake_accepted':False,
        'none_of_nine_has_W06_or_W07_origin':all(not any(x['entry_id'].startswith(('w06::','w07::')) for x in r['origins']) for r in a['candidates']),
        'no_silent_repin':'Assignment, summary and final candidate hashes remain the exact user-pinned bytes. Any later candidate change requires an explicit changed-byte review; this review cannot transfer acceptance to it.',
    },
    'preservation': {
        'worker01_source_head':'26445f23b5a905ac26d864acfbd658570c88769c',
        'prior26family_manifest':bind(W/'.temp/final-preparation-comparison-v1/MANIFEST.json'),
        'start_receipt':bind('root/start-and-inputs-v1.json'),
        'maintained_catalog_boundary':bind('technical/final-maintained-boundary-v1.json'),
        'candidate_fixes':False, 'maintained_writes':False, 'git_mutations':False,
        'github_mutations':False, 'paid_provider_calls':False, 'new_external_sessions':False,
    },
    'failed_attempts_and_limits': [
        'Author SIGINT/KeyboardInterrupt attempt, empty publication-v2 and failed tests/format/cache attempts remain in the sealed author archive. Numeric exit130 was user/parent reported; no literal status receipt was independently located in the ignored-inclusive packet search.',
        'Native review serialization failures (YAML aliases, issue-key syntax and missing exact selectors) remain immutable; active v4 native validate/render both exit0.',
        'Primary source-cue normalization/quotation ambiguity is explicitly clarified by an append-only addendum; exact sources remain unchanged.',
        'Root read-only helper shape errors and truncated displays are documented. Omitted display text is not credited as scientific reading.',
        'Complete source objects and original capture provenance remain bound; unrelated receiving-medium fields, inherited role assertions, shared occurrence allocation and every historic ontology assertion are not globally approved.',
        'The one retained worker evidence counterexample does not classify all inherited MappingEvidence. The campaign-wide audit remains separately owned by W02.',
        'Complete known named partial-material scopes remain feasible. Missing molecular species or later administrative integration is not made a blanket scientific hold.',
        'No native producer/schema/gate modification, whole-repository suite, maintained overlay application, owner merge, publication or export approval occurred.',
    ],
    'coordinator_followup':'Collect this immutable packet; deduplicate the single inherited1226 counterexample with W02, preserve all source-specific holds, independently review any changed successor bytes, and separately reconcile later worker intake. No application is authorized by this review.',
    'whole_owner_approval':False, 'role_approval':False, 'export_approval':False, 'merge_approval':False,
    'program':bind('root/build_final_handoff_v1.py'),
}
save('HANDOFF.json',handoff)
lines = [
    '# Worker01 independent nine-candidate review', '',
    '**Review complete; unqualified whole-candidate acceptance remains withheld.** All nine bounded scientific corrections are supported. One exact retained worker evidence-provenance defect remains under existing#1226.', '',
    'Coverage:9 complete candidates,8 authentic beforeimages,13 distinct original worker proposals,14 source cases and22 exposed CM occurrence IDs. Repeated dependency context is not a new observation or22 admitted mappings.', '',
    '| Candidate | Bounded reviewed result |', '|---|---|',
    '|TARGET-005 Catalase|Successful TOGO M109 versus failed direct JCM117 attribution is truthful; C9322 and historical C-10 remain separately scoped.|',
    '|TARGET-006 Clarified rumen fluid|Species-unspecified processed-fluid scope; cow-only and source-specific protocol identities are not generalized.|',
    '|TARGET-017 Phytone|Specific MICRO0001795 product identity supported; erroneous Hordeum annotation is not copied as source biology.|',
    '|TARGET-024 Soy peptone|Three Phytone tokens are nonresolving; generic partial scope is bounded. Retained W05 MANUAL_CURATION source75 entry remains open under#1226.|',
    '|TARGET-032 BD-Difco RCM|Authentic owner continuity and cited approximate nine-part formula preserved without Oxoid or historical-version conflation.|',
    '|Three DEP-R1193 rumen parents|Literal ungrounded rumen-fluid parts replace unsupported clarification claims; other source/history/quantity fields remain intact.|',
    '|NEW-OXOID-CM0149|Genuine new catalog product history; no invented beforeimage or backdated formula. W03 history remains source lineage.|', '',
    'Native checks pass:9 strict schemas; all37 author rows projected over2,956 baseline owners to2,957 owners with zero partonomy errors;13 coordinator MappingEvidence corrections across4 files;33 exact file reuses; focused alias and guard positive/negative controls. The native review document validates and renders successfully. No full repository suite or CI result is claimed.', '',
    'The inherited#1226 finding has two independent reproductions of one condition. It is separate from the13 corrected coordinator entries. Root/W02 owns future disposition and any guarded correction; no payload was fixed here.', '',
    'The author HANDOFF and393-file manifest were verified before final disposition. All7,260 declared input hashes match. Original W01 head26445f23 is preserved. Later W06/W07 heads are observed but pending intake, and neither authored an origin of these nine candidates.', '',
    'The active science report includes its separately sealed source-cue clarification. Original failed attempts, tests, reviews and captures remain intact. Source-specific species, product revision, inherited alias/role and shared-membership holds remain explicit in HANDOFF.json. No owner, role, export or merge approval is granted.', '',
    'Author seal: MANIFEST SHA2566c89863e292bf1b4333be602bf4a355c0219766456d16e1f574bb5412d956df9; HANDOFF SHA256fb4cb8972c815667e925b056cdb7797d1635b291a9fb3ba936061bdcfa3dac96.', '',
    'Review handoff SHA256: `' + bind('HANDOFF.json')['sha256'] + '`', '',
    'Await coordinator collection. No candidate/source/Git/GitHub mutations or additional external sessions.', '',
]
with (O/'HANDOFF.md').open('x') as f:
    f.write('\n'.join(lines))
print(json.dumps({'handoff':bind('HANDOFF.json'),'readable':bind('HANDOFF.md'),'counts':handoff['counts']},indent=2))
