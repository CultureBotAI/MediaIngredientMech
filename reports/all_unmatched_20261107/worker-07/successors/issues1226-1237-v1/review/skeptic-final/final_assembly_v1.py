import hashlib
import json
from pathlib import Path
import subprocess
from datetime import datetime, timezone

R = Path.cwd()
A = R / 'reports/all_unmatched_20261107/worker-07'
N = A / 'successors/issues1226-1237-v1'
S = R / '.temp/worker07-issues1226-1237-v1/skeptic'

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def read(p):
    return json.loads(Path(p).read_text())

def binding(p):
    p = Path(p)
    return {'path': str(p.relative_to(R)), 'sha256': sha(p)}

refs = []
def check_refs(x, context):
    if isinstance(x, dict):
        if 'path' in x and 'sha256' in x:
            p = Path(x['path'])
            if not p.is_absolute():
                p = (A if x.get('root') == 'artifact' else R) / p
            assert p.is_file(), (context, str(p))
            assert sha(p) == x['sha256'], (context, str(p), 'hash drift')
            refs.append({'context': context, 'path': str(p), 'sha256': x['sha256']})
        for k, v in x.items():
            check_refs(v, context + '/' + k)
    elif isinstance(x, list):
        for i, v in enumerate(x):
            check_refs(v, context + '/' + str(i))

H = read(N/'HANDOFF.json')
selector = read(N/'SELECTOR.json')
assert sha(N/'HANDOFF.json') == 'dc6ef3d910e2fe1a8d2b9160e9310019d039039f56f3930b44223ec6ca681791'
assert sha(N/'SELECTOR.json') == '5d54c81f519e0ff01d0617f830634766c407bc0e5f614393ec33c31fe217993b'
for name in ['HANDOFF.json', 'SELECTOR.json', 'supersession.json', 'hold-accounting.json', 'native-review-lineage.json']:
    check_refs(read(N/name), name)

final_bridge = read(S/'final-core-binding-v1.json')
for b in final_bridge['final_cores'] + [final_bridge['selector']]:
    assert sha(R/b['path']) == b['sha256']

old = A/'successors/issue1203-v1'
D = read(N/'decisions.json')['decisions']
E = read(N/'evidence.json')['evidence']
P = read(N/'proposals.json')['proposals']
OD = read(old/'decisions.json')['decisions']
OE = read(old/'evidence.json')['evidence']
OP = read(old/'proposals.json')['proposals']
DP = read(N/'draft-v1/proposals.json')['proposals']
DD = read(N/'draft-v1/decisions.json')['decisions']
assert len(D) == 188 and len(P) == 100 and len(E) == 1503
assert E[:1498] == OE
assert len(OE) == 1498
assert sum(d == o for d, o in zip(D, OD)) == 180
for d, o in zip(D, OD):
    for k in ['case_id', 'case_input_sha256', 'source', 'occurrence_ids', 'disposition', 'proposal_ids']:
        assert d[k] == o[k], (d['case_id'], k)
for d, draft in zip(D, DD):
    assert {k:v for k,v in d.items() if k not in ['evidence_ids', 'independent_review']} == {k:v for k,v in draft.items() if k not in ['evidence_ids', 'independent_review']}
for p, draft in zip(P, DP):
    assert p['proposal_id'] == draft['proposal_id']
    assert p['after_capture'] == draft['after_capture']
    assert {k:v for k,v in p.items() if k != 'successor_review_bindings'} == draft
    check_refs(p['after_capture'], p['proposal_id'])
assert sum(p['after_capture']['sha256'] != op['after_capture']['sha256'] for p,op in zip(P,OP)) == 74

hold = read(N/'hold-accounting.json')
expected = [{k:d.get(k) for k in ['case_id','missing_requirement','integration_hold','issue_refs']} for d in D if d.get('missing_requirement') or d.get('integration_hold')]
assert expected == hold['case_requirements']
assert hold['pending_nominal_union'] == selector['pending_union']
assert len(hold['case_requirements']) == 134

baseline = read(N/'validation/preexisting-tracked-byte-bindings.json')
assert baseline['head'] == H['predecessor_head']
assert len(baseline['files']) == 15884
tracked_drift = [p for p, expected_sha in baseline['files'].items() if not (R/p).is_file() or sha(R/p) != expected_sha]
assert not tracked_drift, tracked_drift
prior = read(S/'baseline-byte-proof-v1.json')
assert prior['head'] == H['predecessor_head']
for b in prior['tracked_inputs_identical_to_head']:
    assert sha(R/b['path']) == b['sha256']
old_native = [b for b in prior['tracked_inputs_identical_to_head'] if b['path'].startswith('reviews/structured/')]
assert len(old_native) == 2044
private = R/'.temp/worker07-issues1226-1237-v1/native-repo'
for b in old_native:
    assert sha(private/b['path']) == b['sha256']

preserved_packets=[]
for b in prior['protected_packets']:
    for key in ['manifest','seal']:
        if key in b:
            assert sha(R/b[key]['path']) == b[key]['sha256']
    preserved_packets.append({'root':b['root'], 'count':b['count'], 'manifest':b['manifest'], 'seal':b.get('seal'), 'status':'same manifest and seal as independently checked baseline'})
facroot=R/'.temp/fac-polypeptone-independent-v1'
facmanifest=read(facroot/'MANIFEST.json')
for row in facmanifest['files']:
    assert sha(facroot/row['path']) == row['sha256']
w10root=R/'.temp/w10-published-head-independent-review-v1'
w10rows=(w10root/'SHA256SUMS').read_text().splitlines()
for row in w10rows:
    h,p=row.split('  ',1)
    assert sha(w10root/p)==h
assert len(facmanifest['files'])==2339 and len(w10rows)==342

native = read(N/'native-review-receipt.json')
assert sha(R/native['public_yaml']) == native['yaml_sha256']
assert sha((R/native['public_yaml']).with_name('review.md')) == native['markdown_sha256']
assert sha(R/native['private_saved_path']/'review.yaml') == native['yaml_sha256']
assert sha(R/native['private_saved_path']/'review.md') == native['markdown_sha256']
nc=read(N/'validation/native-check-v3.json')
assert nc['returncode']==0
assert json.loads(nc['stdout'])=={'repository':'CultureBotAI/MediaIngredientMech','valid_reviews':1023,'coverage':'declared_scopes_only'}
assert native['scientific_review'] is False and native['wrapper_author']=='/root'
lineage=read(N/'native-review-lineage.json')
assert [a['exit_code'] for a in lineage['attempts']]==[1,1,0]
assert native['yaml_sha256']==lineage['attempts'][2]['input']['sha256']

head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
assert head==H['predecessor_head']
dr=read(S/'independent-skeptical-draft-review-v1.json')
report={
 'report_id':'W07-I1226-I1237-INDEPENDENT-FINAL-ASSEMBLY-V1',
 'reviewer':'/root/successor1226_1237_skeptic',
 'completed_at_utc':datetime.now(timezone.utc).isoformat(),
 'independence':'Separate in-process reviewer; authored none of the 74 successor payloads or provenance allowlist. Parent /root authored payloads/native wrapper; /root/provenance1226_analysis authored allowlist; /root/source1237_science independently reviewed five source payloads/eight cases. This reviewer authored only skeptical review evidence.',
 'verdict':'PASS_WITH_LIMITATIONS_FOR_BOUNDED_REPORT_ONLY_CORRECTION_SUCCESSOR',
 'status':'Exact final selector, cores, all 100 payloads, native receipts and immutable handoff reviewed. No remaining blocker to bounded report-only publication; publication-head/remote acceptance remains coordinator-owned.',
 'final_head_observed_before_publication':head,
 'frozen_scientific_base':H['frozen_scientific_base'],
 'final_bindings':[binding(N/f) for f in ['HANDOFF.json','HANDOFF.md','SELECTOR.json','decisions.json','evidence.json','proposals.json','mutation-ledger.json','retention.json','supersession.json','subagent-scopes.json','hold-accounting.json','native-review-receipt.json','native-review-lineage.json','validation/strict-final.json','validation/projected-native-v1.json','validation/native-check-v3.json','validation/prepublication-byte-proof.json']],
 'independent_preceding_receipts':[binding(S/f) for f in ['independent-skeptical-draft-review-v1.json','final-core-binding-v1.json','allowlist-independent-review-v1.json','independent-provenance-recomputation-v1.json','independent-native-projected-check-v1.json','independent-guard-controls-v1.json','baseline-byte-proof-v1.json','new-lead-ledger-partial-001.json']],
 'source_science_receipt':binding(N/'review/science/independent-science-review-v1.json'),
 'coverage':{'case_ids': [d['case_id'] for d in D], 'proposal_ids':[p['proposal_id'] for p in P], 'source_case_scope_updates':dr['reviewed_case_ids'], 'complete_payload_comparisons':100, 'metadata_changed_payloads':74, 'exact_unchanged_payloads':26, 'MappingEvidence_claims_corrected':79, 'original_evidence_prefix_retained':1498, 'final_evidence_entries':1503, 'exact_unchanged_case_objects':180, 'case_disposition_changes':0, 'case_hold_projection_rows':134, 'strict_auditor_input_hashes_independently_rechecked':1209},
 'final_assembly_checks':[
  'Every path/hash pair in HANDOFF, SELECTOR, supersession, hold accounting and native-attempt lineage resolves to exact bytes; all 100 selected payload hashes were rechecked.',
  'Final cores bridge reviewed draft exactly: only actual independent-review attachments added; no subsequent payload or scientific wording changes. Original 1498 evidence entries are the exact final prefix; case IDs, frozen digests, sources, occurrences, disposition categories and proposal routing are unchanged.',
  'All 134 cases with explicit missing requirements or integration holds are reproduced exactly in hold-accounting. Both nominal DSM source origins remain held from independent co-installation and assigned to coordinator root C; no union or winner invented.',
  '79 newly agent-authored MappingEvidence assertions remain claim-specific LLM_SUGGESTION. Historical human evidence, 41 other MappingEvidence objects, all 78 ComponentEvidence objects and canonical SSSOM semantics retain the exact previously reviewed bytes/semantics.',
  'The native private wrapper is explicitly self-review with scientific_review=false; independent science and skeptical receipts carry their actual disjoint scopes. Successful check means 1023 declared review scopes, not 1023 new scientific owner approvals.',
  'Both failed native attempts are retained with actual errors, exact bytes and explicit correction lineage. The misleading failed_v1_retained receipt key is explicitly corrected by immutable native-review-lineage.json; no retrospective timing/review is invented.',
  'All 15884 preexisting tracked files rehashed without drift. Independently compared baseline-selected 6877 files remain identical; all 2044 old native review files also match the private native repository. Complete FAC 2339 and fullW10 342 manifest members rehashed unchanged.',
  'Full final source/native/scientific/physical/role/export/integration holds survive; no whole-owner, alias-owner merge, release or final cross-shard union approval is conveyed.'
 ],
 'native_limits':{'independent_closed_schema_payloads':100,'independent_projected_partonomy_records':3027,'independent_partonomy_errors':0,'private_native_review_check_exit':0,'private_native_declared_scopes':1023,'inherited_alias_collisions':25,'inherited_alias_collisions_touching_selected_owners':16,'alias_disposition':'No introduced alias projection changes; inherited collisions remain unapproved and unresolved.','production_gates':'Not run against maintained corpus; private candidate validation is not an export/release gate pass.'},
 'new_issue_first_lead':{'finding_id':'W07-SKEPTIC-LEDGER-PARTIAL-001','finding':binding(S/'new-lead-ledger-partial-001.json'),'status':'OPEN_INHERITED_MINOR_COORDINATOR_ISSUE_FIRST_TRIAGE','scope':'Two original JCM900 reasoning/applicability sentences still mention separate/PARTIAL draft while selected full immediate-input payload is COMPLETE. Exact historical wording is retained and the explicit current integration note prevents its use to override selected payload. No unfiled correction was authored.','blocks_bounded_filed_corrections':False},
 'preservation':{'tracked_files_rehashed':15884,'tracked_drift':tracked_drift,'old_native_review_files_unchanged_in_both_repositories':2044,'sealed_packets':preserved_packets},
 'remaining_acceptance_conditions':[
  'Parent seals the final manifest including this receipt, commits and pushes only the authorized report successor on the existing branch without force. The exact local and remote head must be bound to committed HANDOFF/manifest/selector in the single publication receipt.',
  'Coordinator independently accepts final published bytes; this prepublication receipt cannot verify a future Git head or remote state.',
  'Coordinator triages the inherited JCM900 ledger wording finding before any separate follow-up correction.',
  'Coordinator root C completes and independently reviews the DSM590/1144 nominal union using both corrected origins and histories; these two proposals are not independently co-installable.',
  'All source-specific missing-evidence and role/owner/export/release holds remain as enumerated in the exact handoff and hold-accounting. No final cross-shard union acceptance is provided.'
 ],
 'reference_hash_checks':refs,
 'approval_limits':'Bounded source-case correction and metadata review only. Earlier whole-owner/release approvals are not transferred to changed payload hashes; unchanged source-case outcomes remain bound rather than freshly reapproved for broader scopes.',
 'failed_probes_preserved':'All earlier local Unicode-path probe, draft path probe, provenance diagnostic v1 and native v1/v2 failures remain historical; only their documented successors provide successful checks.'
}
out=S/'final-assembly-review-v1.json'
assert not out.exists()
out.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'path':str(out.relative_to(R)),'sha256':sha(out),'verdict':report['verdict'],'tracked_files':15884,'case_holds':134,'reference_checks':len(refs)},indent=2))
