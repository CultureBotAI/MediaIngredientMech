"""Independent bounded checks of the actual report-only EBIOS metadata."""
from pathlib import Path
from datetime import datetime, timezone
import json
import verify_published_retirement as v

T = Path(__file__).resolve().parent
W = T.parents[2]
P = T / 'packet'
native, cw = v.load_runtime(T / 'native-repo', T / 'native/crosswalk.py', v.PRODUCER_PINS)
EXPECTED = cw.read_json((P / 'source-origin-retirement.json').read_bytes())

def statement_check(statement, strict_author_type=False):
    # These native primitives/exact equality are the actual published branch's
    # grammar comparison, separately from its indispensable Git publication proof.
    cw.closed(statement, EXPECTED.keys(), 'retirement statement')
    cw.hash_value(statement['origin_proposal_sha256'])
    cw.text(statement['reason'])
    cw.require(statement == EXPECTED, 'published retirement claim differs')
    if strict_author_type:
        cw.require(type(statement['schema_version']) is int, 'not integer version')

def core_and_copies(packet=None):
    packet = packet or {name: cw.read_json((P / name).read_bytes()) for name in [
        'selector.json', 'source-case-reconciliation.json', 'original/proposal.json',
        'original/case-decision.json', 'original/evidence.json']}
    selector = packet['selector.json']; note = packet['source-case-reconciliation.json']
    cores = {}
    for key, ref in selector['original_full_core_selection'].items():
        raw = (W / ref['path']).read_bytes()
        cw.require(v.digest(raw) == ref['sha256'], 'raw selected ledger hash differs')
        cw.require(raw == native.git(W, 'show', v.BASE + ':' + ref['path']), 'selected ledger is not original Git bytes')
        cores[key] = cw.read_json(raw)
    proposals = cores['proposals']['proposals']; decisions = cores['decisions']['decisions']; evidence = cores['evidence']['evidence']
    counts = {'cases': len(decisions), 'CM_occurrence_ids': len({o for d in decisions for o in d['occurrence_ids']}),
              'proposals': len(proposals), 'evidence_objects': len(evidence)}
    cw.require(counts == selector['original_counts_retained'] == {
        'cases': 188, 'CM_occurrence_ids': 322, 'proposals': 117, 'evidence_objects': 1830}, 'counts differ')
    proposal, = [p for p in proposals if p['proposal_id'] == v.PID]
    decision, = [d for d in decisions if d['case_id'] == v.CASE]
    cw.require(proposal == packet['original/proposal.json'] and cw.object_hash(proposal) == v.PROPOSAL_SHA, 'full proposal differs')
    cw.require(decision == packet['original/case-decision.json'] and cw.object_hash(decision) == note['unchanged_original_decision_object_sha256'], 'full case differs')
    cw.require(proposal['kind'] == note['original_kind'] == 'new_owner'
               and proposal['before_sha256'] is note['original_before_sha256'] is None, 'invented edit/preimage')
    cw.require(decision['case_input_sha256'] == note['case_input_sha256'] == v.CASE_SHA
               and decision['occurrence_ids'] == note['original_occurrence_ids']
               and len(decision['occurrence_ids']) == 1, 'case/occurrence changed')
    ids = set(proposal['evidence_ids']) | set(decision['evidence_ids'])
    actual = [e for e in evidence if e['evidence_id'] in ids]
    cw.require(len(actual) == 8 and actual == packet['original/evidence.json']['evidence'], 'full evidence differs')
    cw.require({e['evidence_id']: cw.object_hash(e) for e in actual} == note['unchanged_original_evidence_object_sha256'], 'evidence provenance differs')
    payload = (P / 'original/payload.yaml').read_bytes()
    cw.require(payload == (W / v.PAYLOAD).read_bytes() == native.git(W, 'show', v.BASE + ':' + v.PAYLOAD)
               and v.digest(payload) == v.PAYLOAD_SHA, 'payload differs')
    family = cw.read_json((P / 'context/family-review-HANDOFF.json').read_bytes())
    cw.require(note['held_limits'] == selector['source_family_lot_role_export_holds'] == family['remaining_limits'], 'family hold changed')
    cw.require(note['family_candidate'] == selector['reviewed_family_candidate'] == family['candidate'], 'family candidate differs')
    cw.require(note['authentic_promotion_beforeimage'] == family['beforeimage'], 'promotion beforeimage differs')
    cw.require(note['fresh_scientific_review'] is False and note['maintained_owner_role_export_application_approval'] is False,
               'approval inflation')
    return counts

def run():
    outputs = cw.read_json((T / 'author/author-write-receipt.json').read_bytes())['outputs']
    prefix = v.PREFIX + 'successors/ebios-no-install-v1/'
    for r in outputs:
        raw = (W / r['path']).read_bytes()
        cw.require(v.digest(raw) == r['sha256'] and raw == (P / r['path'].removeprefix(prefix)).read_bytes(), 'author output drift')
    cw.require(len(outputs) == 12, 'output scope differs')
    statement_check(EXPECTED, True)
    counts = core_and_copies()
    origin, binding = v.source_context(W, v.BASE, native, cw)
    proof = cw.Proofs(W, native)
    cw._verify_origin(origin, binding, proof)
    proof.recheck()
    try:
        cw.validate_resolution_crosswalk([origin], [v.resolution_context(W, v.BASE, cw)],
                                         root=W, origin_bindings=[binding], native_plan=None)
    except ValueError as exc:
        cw.require(str(exc) == 'published proof is not a regular Git blob', 'unexpected precommit refusal')
        refusal = str(exc)
    else:
        raise ValueError('unpublished statement unexpectedly proved at old source head')
    native._check_loaded_producers()
    return {'reviewed_at': datetime.now(timezone.utc).isoformat(), 'author_outputs': 12,
            'counts': counts, 'source_git_proof': {'status': 'PASS', 'head': v.BASE,
            'proposal_object_sha256': v.PROPOSAL_SHA, 'payload_sha256': v.PAYLOAD_SHA},
            'prepublication_full_retirement_attempt': {'status': 'EXPECTED_REFUSAL', 'reason': refusal,
            'meaning': 'New retirement statement is not published at the old source head; no completed bridge is claimed.'},
            'scientific_review': False, 'full_campaign_prepare': False}

if __name__ == '__main__':
    print(json.dumps(run(), indent=2, ensure_ascii=False))
