"""Publish additive report metadata only; all existing W02 source bytes are inputs."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import subprocess
import sys

O = Path(__file__).resolve().parent
W = O.parents[1]
C = W.parents[2]
R = W / 'reports/all_unmatched_20261107/worker-02/successors/ebios-no-install-v1'
sys.path.insert(0, str(W / 'src'))
from mediaingredientmech.curate.publication_guard import FrozenFile
from mediaingredientmech.ingredient_bundle_refresh import publish_new_files

BASE = '0c659aa4c121a5b1832bff699c28e30da577ca08'
OID = 'w02::a2-proposal-nbrc1132-asahi-ebios-tablets'
PID = OID.split('::', 1)[1]
PROPOSAL_SHA = '47b497f7e9b2f764683bddb7479a891be28fa772716d84dd127238033fb34587'
PAYLOAD_SHA = '3275012aad49e7d7e353507d106a3a26c8b2313fad80e5e587ade3bec857bc3c'
CASE = 'CM_NAME:22e6006ce3bb10066c3c593c4736919fa6cd47f8f2d2a5347ffe92535e5237ff'
CORE = W / 'reports/all_unmatched_20261107/worker-02/seven-preparation-types-v1/selected-v3'
FAMILY = C / 'workers/w08/worktree/.temp/ebios-candidate-independent-v1'
CODE = C / 'integration/final-application-accounting-v3/crosswalk.py'
held = []

def freeze(p):
    f = FrozenFile.capture(p)
    held.append(f)
    return f.content

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def encode(obj):
    return (json.dumps(obj, indent=2, ensure_ascii=False, allow_nan=False) + '\n').encode()

def objhash(obj):
    return sha(json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode())

def git(*args):
    return subprocess.check_output(['git', '-C', str(W), *args])

def ref(p, raw):
    return {'path': str(p.relative_to(W)) if p.is_relative_to(W) else str(p), 'sha256': sha(raw)}

assert git('rev-parse', 'HEAD').decode().strip() == BASE
assert git('status', '--short').decode().strip() == ''
crosswalk_raw = freeze(CODE)
assert sha(crosswalk_raw) == '6b247656ec34a5280a7b10ba1dea6a67edfc12fa0aab004cbb2ec9575a650753'
spec = importlib.util.spec_from_file_location('ebios_reviewed_crosswalk', CODE)
crosswalk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(crosswalk)
core = {}
for name in ['proposals', 'decisions', 'evidence', 'review-binding']:
    p = CORE / (name + '.json')
    raw = freeze(p)
    assert raw == git('show', BASE + ':' + str(p.relative_to(W)))
    core[name] = {'ref': ref(p, raw), 'object': crosswalk.read_json(raw)}
proposals = core['proposals']['object']['proposals']
decisions = core['decisions']['object']['decisions']
evidence = core['evidence']['object']['evidence']
proposal = next(p for p in proposals if p['proposal_id'] == PID)
decision = next(d for d in decisions if d['case_id'] == CASE)
assert objhash(proposal) == PROPOSAL_SHA
assert proposal['kind'] == 'new_owner' and proposal['before_sha256'] is None
payload_path = W / 'reports/all_unmatched_20261107/worker-02' / proposal['after_capture']['path']
payload = freeze(payload_path)
assert sha(payload) == PAYLOAD_SHA and payload == git('show', BASE + ':' + str(payload_path.relative_to(W)))
evidence_ids = set(proposal['evidence_ids']) | set(decision['evidence_ids'])
original_evidence = [e for e in evidence if e['evidence_id'] in evidence_ids]
assert {e['evidence_id'] for e in original_evidence} == evidence_ids
assert len(proposals) == 117 and len(decisions) == 188 and len(evidence) == 1830
occurrences = {o for d in decisions for o in d['occurrence_ids']}
assert len(occurrences) == 322

family_handoff_raw = freeze(FAMILY / 'HANDOFF.json')
assert sha(family_handoff_raw) == '76a4ba5d9cfcfa93c5150406daecc8b21d05cbd9838fbb50ebe626e65debfe5b'
family_manifest_raw = freeze(FAMILY / 'MANIFEST.json')
assert sha(family_manifest_raw) == 'afa45f56ebe1b4eea86a8dde3597bd1f9f156b497ea1275c1a91a12158398b96'
family = crosswalk.read_json(family_handoff_raw)
candidate_path = Path(family['candidate']['author_path'])
assert sha(freeze(candidate_path)) == 'a5b147248539b039caa788e4d208afdebd24c59b218082a1b5b06f266184f09a'
before_path = W / family['beforeimage']['owner_path']
before = freeze(before_path)
assert sha(before) == '130f1d9a20d6e16b9a10939a7251242d290bc8b13eb2a140be697e7b86cf87a4'
audit_path = C / 'integration/final-native-intake-v1/native-origin-kind-preimage-conflicts.json'
audit = freeze(audit_path)
assert sha(audit) == '2b691533c6ee0f394af8cbcf70b785879ff09b43610e67fc837fdfa26c2f885b'
comment_path = O / 'inputs/issue1237-comment6720520960.json'
comment = freeze(comment_path)
assert crosswalk.read_json(comment)['id'] == 6720520960

reason = (
    'Withdraw only the standalone new_owner installation of w02::a2-proposal-nbrc1132-asahi-ebios-tablets. '
    'The unchanged complete W02 proposal, original payload, raw source case, occurrence and evidence remain '
    'reconciliation evidence for the independently reviewed EBIOS tablet-family candidate '
    'a5b147248539b039caa788e4d208afdebd24c59b218082a1b5b06f266184f09a. That candidate concerns promotion '
    'of authentic data/ingredients/unmapped/EBIOS.yaml through the genuine W01 and W06 existing-owner edit origins. '
    'This retirement creates no successor source proposal, edit or preimage; it removes no case or occurrence '
    'and grants no source-route, formulation/version/lot, role, owner-application or export approval. '
    'The original W02 new_owner kind and null preimage remain historical facts. '
    'Disposition filed before this statement at https://github.com/CultureBotAI/MediaIngredientMech/issues/1237#issuecomment-6720520960.'
)
statement = {'schema_version': 1, 'kind': 'source_origin_retirement', 'origin_id': OID,
             'origin_proposal_sha256': PROPOSAL_SHA, 'successors': {}, 'reason': reason}
crosswalk.closed(statement, {'schema_version', 'kind', 'origin_id', 'origin_proposal_sha256', 'successors', 'reason'}, 'retirement statement')
assert type(statement['schema_version']) is int and statement['schema_version'] == 1
assert statement['successors'] == {} and crosswalk.hash_value(statement['origin_proposal_sha256']) == PROPOSAL_SHA
crosswalk.text(statement['reason'])
statement_raw = encode(statement)
now = datetime.now(timezone.utc).isoformat()
source_note = {'schema_version': 1, 'authored_at': now, 'author': 'Codex worker02 /root', 'llm_assisted': True,
    'action': 'WITHDRAW_STANDALONE_NEW_OWNER_INSTALLATION_ONLY',
    'filed_comment': 'https://github.com/CultureBotAI/MediaIngredientMech/issues/1237#issuecomment-6720520960',
    'origin_id': OID, 'original_proposal_object_sha256': PROPOSAL_SHA,
    'original_kind': proposal['kind'], 'original_before_sha256': None,
    'original_case_id': CASE, 'case_input_sha256': decision['case_input_sha256'],
    'original_occurrence_ids': decision['occurrence_ids'],
    'unchanged_original_decision_object_sha256': objhash(decision),
    'unchanged_original_evidence_object_sha256': {e['evidence_id']: objhash(e) for e in original_evidence},
    'installation_override': 'The retirement overrides only standalone installation of the original W02 new-owner proposal. It does not rewrite or drop the historical decision, case, evidence, source label or payload.',
    'reconciliation_use': 'Retain the complete W02 contribution in the exact reviewed three-origin tablet-family reconciliation; the native promotion consumes genuine W01/W06 edit origins only. Empty successors is an explicit withdrawal, not a replacement source proposal.',
    'historical_reasoning_qualification': 'Older unresolved EBIOS/P2G comparison remains a preserved historical observation. The separately reviewed tablet-family source association supplies the later bounded reconciliation; no old review is relabelled as approval of new bytes.',
    'family_candidate': family['candidate'], 'authentic_promotion_beforeimage': family['beforeimage'],
    'family_review_handoff_sha256': sha(family_handoff_raw), 'family_source_counts': family['counts'],
    'held_limits': family['remaining_limits'], 'fresh_scientific_review': False,
    'source_case_or_occurrence_count_drop': 0, 'invented_edit_or_successor_or_preimage': False,
    'maintained_owner_role_export_application_approval': False}
selector = {'schema_version': 1, 'selector_id': 'W02-EBIOS-NO-INSTALL-V1', 'authored_at': now,
    'author': 'Codex worker02 /root', 'publication_base_head': BASE,
    'selection_kind': 'Additive source-author retirement metadata; original full scientific core selection retained',
    'original_full_core_selection': {k: v['ref'] for k, v in core.items()},
    'original_counts_retained': {'cases': 188, 'CM_occurrence_ids': 322, 'proposals': 117, 'evidence_objects': 1830},
    'retirements': [{'path': 'source-origin-retirement.json', 'sha256': sha(statement_raw), 'origin_id': OID,
                     'origin_proposal_sha256': PROPOSAL_SHA, 'successors': {}}],
    'source_case_reconciliation': {'path': 'source-case-reconciliation.json', 'sha256': sha(encode(source_note))},
    'retirement_overrides_standalone_installation_only': True,
    'unchanged_original_payload': ref(payload_path, payload),
    'original_source_evidence_contribution_retained': True,
    'reviewed_family_candidate': family['candidate'],
    'genuine_promotion_origins_context_only': [o for o in family['origins'] if o['origin_id'] != OID],
    'no_new_successor_proposal_or_fake_edit': True,
    'publication_binding_rule': 'After ordinary publication, bind this statement and the unchanged original proposal ledger/payload at the actual new selected W02 head. The empty-successor native retirement bridge uses that selected origin head; no publication at old0c is claimed.',
    'source_family_lot_role_export_holds': family['remaining_limits'],
    'new_case_or_occurrence_or_scientific_approval': False,
    'full_campaign_prepare_or_application_claim': False,
    'final_published_head_review': 'Separate coordinator responsibility; this author selector is not that review.'}
readme = f'''# W02 EBIOS no-install source retirement

This additive statement withdraws only the distinct new-owner installation for `{OID}`. The complete original proposal remains a genuine `new_owner` with a null preimage. Its object SHA256 is `{PROPOSAL_SHA}` and its exact original payload SHA256 is `{PAYLOAD_SHA}`.

`source-origin-retirement.json` uses the reviewed native schema and an empty successor map. No replacement source proposal or existing-owner edit is fabricated. `source-case-reconciliation.json` keeps the full W02 source contribution and one original occurrence available as evidence for the independently reviewed EBIOS tablet-family reconciliation. The actual promotion concerns the existing unmapped EBIOS beforeimage and the genuine W01/W06 edit origins.

The 188 original cases, 322 CM occurrence IDs, 117 proposals and 1,830 evidence objects remain in their exact existing selected core files. The additive selector overrides standalone installation of this one creation only. It does not delete a source case, substitute a new identity, rewrite an old review or promote scientific/release status. Historical formulation/version/lot, child, role, source-route and export limits remain.

The exact filed disposition was read before authoring: issue1237 comment6720520960. The distinct W08 whole-candidate review is context and bounded scientific support, not new science authored by this metadata task. Technical, lineage and skeptical reviewers inspect the complete metadata and its exact input bindings. Their native bounded proof does not claim full-campaign prepare or application.

Publication is ordinary and additive on the existing W02 branch. Its actual resulting head and remote readback are recorded in the later private publication receipt; no self-referential commit SHA is invented in this prepublication packet. After publication, the unchanged original proposal and payload must be bound at the new selected W02 head for the native empty-successor retirement branch.
'''
outputs = {
    'source-origin-retirement.json': statement_raw,
    'source-case-reconciliation.json': encode(source_note), 'selector.json': encode(selector),
    'README.md': readme.encode(),
    'original/proposal.json': encode(proposal), 'original/payload.yaml': payload,
    'original/case-decision.json': encode(decision), 'original/evidence.json': encode({'evidence': original_evidence}),
    'context/family-review-HANDOFF.json': family_handoff_raw,
    'context/family-review-MANIFEST.json': family_manifest_raw,
    'context/native-origin-kind-preimage-conflicts.json': audit,
    'context/issue1237-comment6720520960.json': comment,
}
for p in [R, R / 'original', R / 'context']:
    p.mkdir(parents=True, exist_ok=True)

def recheck():
    assert git('rev-parse', 'HEAD').decode().strip() == BASE
    for f in held:
        f.verify()

publish_new_files([(R / name, raw) for name, raw in outputs.items()], recheck)
recheck()
receipt = {'at': now, 'author': 'Codex worker02 /root', 'status': 'ADDITIVE_METADATA_WRITTEN_FOR_INDEPENDENT_REVIEW',
    'native_writer': 'mediaingredientmech.ingredient_bundle_refresh.publish_new_files with FrozenFile inputs',
    'crosswalk_contract': ref(CODE, crosswalk_raw),
    'held_inputs': [{'path': str(f.path), 'sha256': sha(f.content)} for f in held],
    'outputs': [{'path': str((R / n).relative_to(W)), 'sha256': sha(raw), 'bytes': len(raw)} for n, raw in outputs.items()],
    'full_native_published_retirement_check': 'Pending actual ordinary commit; no published bridge or campaign prepare is claimed now.',
    'old_source_core_or_payload_changes': False, 'candidate_or_maintained_changes': False,
    'preserved_six_review_handoff_sha256': sha((W / '.temp/positive-six-candidates-independent-v1/HANDOFF.json').read_bytes())}
with (O / 'author-write-receipt.json').open('x') as f:
    f.write(json.dumps(receipt, indent=2, ensure_ascii=False) + '\n')
print(json.dumps({'report_path': str(R), 'statement_sha256': sha(statement_raw), 'outputs': len(outputs)}, indent=2))
