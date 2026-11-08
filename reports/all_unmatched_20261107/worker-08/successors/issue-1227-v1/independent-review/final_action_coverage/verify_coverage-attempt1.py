"""Read-only final action accounting. This is not a scientific peer review."""
import collections
import datetime
import hashlib
import json
import re
from pathlib import Path
import yaml

B = Path('reports/all_unmatched_20261107/worker-08')
S = B / 'successors/issue-1227-v1'
R = S / 'independent-review/final_action_coverage'
inputs = {}
checks = []

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def read(p):
    inputs[str(p.relative_to(B))] = sha(p)
    return json.loads(p.read_text())

def rows(p, key):
    x = read(p)
    return x[key] if isinstance(x, dict) else x

def cap(p):
    return dict(root='artifact', path=str(p.relative_to(B)), sha256=sha(p))

def check(label, result, detail=None):
    checks.append(dict(check=label, passed=bool(result), detail=detail))

def write(name, value):
    p = R / name
    assert not p.exists(), p
    p.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')

def at_pointer(obj, pointer):
    for key in pointer.strip('/').split('/'):
        obj = obj[int(key)] if isinstance(obj, list) else obj[key]
    return obj

selection = read(S / 'provenance/final-selection-v2.json')
validation = read(S / 'validation/combined-validation.json')
assembly = read(S / 'final-v2/assembly-provenance.json')
decisions = rows(S / 'final-v2/decisions.json', 'decisions')
proposals = rows(S / 'final-v2/proposals.json', 'proposals')
parent_p = rows(B / selection['parent_inputs']['proposals']['path'], 'proposals')
parent_d = rows(B / selection['parent_inputs']['decisions']['path'], 'decisions')
P = {p['proposal_id']: p for p in proposals}
P0 = {p['proposal_id']: p for p in parent_p}
D0 = {d['case_id']: d for d in parent_d}
matrix_path = S / 'inputs/coordinator-triage/all113-payload-action-matrix.json'
matrix = read(matrix_path)
refinement_path = S / 'inputs/coordinator-triage/completeness-adjudication-refinement.json'
refinement = read(refinement_path)
dispositions_path = S / 'issue-dispositions.json'
dispositions = read(dispositions_path)
by_finding = {x['finding_id']: x for x in dispositions['findings']}
cohort_for = {}
peers = {}
group_rows = []
for g in selection['groups']:
    peer = read(B / g['peer_capture']['path'])
    peers[g['name']] = peer
    check(g['name'] + ' peer hash', sha(B / g['peer_capture']['path']) == g['peer_capture']['sha256'])
    check(g['name'] + ' peer scope', set(peer['case_ids']) == set(g['case_ids']) and set(peer['proposal_ids']) == set(g['proposal_ids']))
    check(g['name'] + ' peer has no open blocking findings', not peer['open_blocking_findings'])
    for c in g['inputs'].values():
        check(g['name'] + ' exact selected index ' + c['path'], sha(B / c['path']) == c['sha256'] and peer['input_hashes'].get(c['path']) == c['sha256'])
    for pid in g['proposal_ids']:
        cohort_for[pid] = g['name']
        check(pid + ' exact peer payload', peer['payload_hashes'][pid] == P[pid]['after_capture']['sha256'])
    group_rows.append(dict(name=g['name'], case_count=len(g['case_ids']), proposal_count=len(g['proposal_ids']),
        inputs=g['inputs'], peer_capture=g['peer_capture'], author=g['author'], reviewer=g['reviewer']))

for path, digest in validation['input_hashes'].items():
    check('root validation exact input ' + path, sha(Path(path)) == digest)
check('exact188 cases /113 proposals and unchanged ID sets', len(decisions) == 188 and len(proposals) == 113 and set(P) == set(P0) and {d['case_id'] for d in decisions} == set(D0))
payloads = {}
old_payloads = {}
payload_rows = []
for pid, p in P.items():
    f = B / p['after_capture']['path']
    oldf = B / P0[pid]['after_capture']['path']
    check(pid + ' selected and predecessor capture hashes', sha(f) == p['after_capture']['sha256'] and sha(oldf) == P0[pid]['after_capture']['sha256'])
    x = yaml.safe_load(f.read_text())
    z = yaml.safe_load(oldf.read_text())
    payloads[pid] = x
    old_payloads[pid] = z
    payload_rows.append(dict(proposal_id=pid, cohort=cohort_for[pid], owner_path=p['owner_path'],
        case_ids=p['case_ids'], predecessor=P0[pid]['after_capture'], selected=p['after_capture'],
        changed=p['after_capture']['sha256'] != P0[pid]['after_capture']['sha256'],
        peer_capture=next(g['peer_capture'] for g in selection['groups'] if g['name'] == cohort_for[pid])))
changed_count = sum(x['changed'] for x in payload_rows)
check('95 changed /18 unchanged payload bytes', changed_count == 95 and len(payload_rows) - changed_count == 18)
check('assembly counts match recomputation', assembly['changed_payloads'] == changed_count and assembly['unchanged_payloads'] == 18 and assembly['cases'] == 188 and assembly['proposals'] == 113)

# Mapping evidence: compare actual selected payload objects to the predecessor objects.
ledger_paths = {
    'inorganic_forms': S / 'research/inorganic_forms/evidence-category-ledger.json',
    'organic_products': S / 'research/organic_products/category-correction-ledger.json',
    'vitamins_mixtures': S / 'research/vitamins_mixtures/final-v2/evidence-category-corrections.json',
}
ledger_entries = {}
for cohort, path in ledger_paths.items():
    data = read(path)
    data = data if isinstance(data, list) else data.get('entries', data.get('rows'))
    for i, a in enumerate(data):
        ptr = a.get('json_pointer', a.get('path'))
        if ptr and not ptr.startswith('/'):
            ptr = '/' + re.sub(r'\[(\d+)\]', r'/\1', ptr).replace('.', '/')
        ledger_entries[(a['proposal_id'], ptr)] = (path, i, a)
mapping_rows = []
actual_type_changes = []
for pid in P:
    before = old_payloads[pid].get('ontology_mapping', {}).get('evidence', [])
    after = payloads[pid].get('ontology_mapping', {}).get('evidence', [])
    for i, e in enumerate(before):
        if i < len(after) and e.get('evidence_type') != after[i].get('evidence_type'):
            actual_type_changes.append((pid, f'/ontology_mapping/evidence/{i}'))
for a in validation['mapping_evidence_corrections']:
    pid, ptr = a['proposal_id'], a['pointer']
    check(pid + ptr + ' exact category before/after', at_pointer(old_payloads[pid], ptr) == a['before'] and at_pointer(payloads[pid], ptr) == a['after'])
    ledger_path, i, row = ledger_entries[(pid, ptr)]
    check(pid + ptr + ' ledger agrees', row.get('before', row.get('old_entry')) == a['before'] and row.get('after', row.get('new_entry')) == a['after'])
    mapping_rows.append(dict(proposal_id=pid, case_ids=P[pid]['case_ids'], pointer=ptr,
        before_type=a['before']['evidence_type'], after_type=a['after']['evidence_type'],
        source_before=a['before'].get('source'), source_after=a['after'].get('source'),
        before_assertion_sha256=hashlib.sha256(json.dumps(a['before'], sort_keys=True, separators=(',', ':')).encode()).hexdigest(),
        after_assertion_sha256=hashlib.sha256(json.dumps(a['after'], sort_keys=True, separators=(',', ':')).encode()).hexdigest(),
        selected_capture=P[pid]['after_capture'], ledger=cap(ledger_path), ledger_row=i,
        peer_capture=next(g['peer_capture'] for g in selection['groups'] if g['name'] == cohort_for[pid])))
check('all95 category type deltas covered exactly', set(actual_type_changes) == {(x['proposal_id'], x['pointer']) for x in mapping_rows} and len(mapping_rows) == 95)
check('88 category-affected payloads', len({x['proposal_id'] for x in mapping_rows}) == 88)
retained_human = []
for a in validation['inherited_human_evidence']:
    pid, i = a['proposal_id'], a['index']
    check(pid + ' inherited human evidence preserved', old_payloads[pid]['ontology_mapping']['evidence'][i] == payloads[pid]['ontology_mapping']['evidence'][i] == a['evidence'])
    retained_human.append(dict(proposal_id=pid, pointer=f'/ontology_mapping/evidence/{i}', selected_capture=P[pid]['after_capture'], scope=a['scope']))

# Exact original32 proposal follow-ups, with all component adjudication locators.
component_path = S / 'research/vitamins_mixtures/final-v2/component-adjudications.json'
components = read(component_path)
followup_ids = {a['proposal_id'] for a in matrix if any(r['finding_id'] == 'W08-IR-003' for r in a['action_rows'])}
check('exact32 component followup issue bindings', len(followup_ids) == 32 and followup_ids == {p['proposal_id'] for p in by_finding['W08-IR-003']['successor_payload_bindings']})
component_rows = []
for pid in sorted(followup_ids):
    slots = [(i, a) for i, a in enumerate(components) if a['proposal_id'] == pid]
    check(pid + ' all source component slots accounted', {a['component_index'] for _, a in slots} == set(range(len(payloads[pid].get('components', [])))))
    for _, a in slots:
        check(pid + f" component[{a['component_index']}] selected after agrees", a['after'] == payloads[pid]['components'][a['component_index']])
    component_rows.append(dict(proposal_id=pid, case_ids=P[pid]['case_ids'], selected_capture=P[pid]['after_capture'],
        adjudication_ledger=cap(component_path), ledger_rows=[i for i, _ in slots],
        outcome_counts=dict(collections.Counter(a['outcome'] for _, a in slots)),
        unresolved_components=[dict(index=a['component_index'], component=a['after'], reason=a['reason'], source_evidence_ids=a.get('source_evidence_ids', [])) for _, a in slots if a['after'].get('reference_scope') == 'UNMAPPED'],
        explicit_dependency_or_external_refs=[dict(index=a['component_index'], component=a['after'], reason=a['reason']) for _, a in slots if a['outcome'] in {'conditional_selected_overlay_reference', 'grounded_exact_external_entity'}],
        peer_capture=next(g['peer_capture'] for g in selection['groups'] if g['name'] == cohort_for[pid])))

# Source-relative34 refinement: five excluded rows are separate adjudications.
complete_rows = []
for i, a in enumerate(refinement['rows']):
    pid = a['proposal_id']
    recommendation = a['root_triage_recommendation']
    actual = payloads[pid]['component_assertion']['completeness']
    if recommendation == 'UNKNOWN':
        bucket = 'UNKNOWN'
        expected = 'UNKNOWN'
    elif recommendation == 'COMPLETE_FOR_LITERAL_PRINTED_INPUT_LIST':
        bucket = 'literal_source_COMPLETE'
        expected = 'COMPLETE'
    else:
        bucket = 'separate_exclusion'
        expected = 'PARTIAL'
    check(pid + ' final source-relative completeness', actual == expected)
    complete_rows.append(dict(proposal_id=pid, case_ids=P[pid]['case_ids'], selected_capture=P[pid]['after_capture'],
        bucket=bucket, actual=actual, original_recommendation=a.get('recommended_completeness'),
        authoritative_refinement=recommendation, refinement_reason=a['root_triage_reason'],
        refinement=cap(refinement_path), refinement_row=i, original_primary_anchors=a.get('primary_anchors', []),
        final_assertion_notes=payloads[pid]['component_assertion'].get('notes'),
        peer_capture=next(g['peer_capture'] for g in selection['groups'] if g['name'] == cohort_for[pid])))
split = dict(collections.Counter(x['bucket'] for x in complete_rows))
check('exact34 completeness accounting', len(complete_rows) == 34 and split == {'UNKNOWN': 24, 'literal_source_COMPLETE': 5, 'separate_exclusion': 5})

expected_routes = {'W08-IR-001': 1226, 'W08-IR-003': 1201, 'W08-IR-004': 1201,
    'W08-IR-008': 811, 'W08-IR-010': 1210,
    **{f'W08-IR-{i:03d}': 1227 for i in [2, 5, 6, 7, 9, 11, 12]}}
route_rows = []
for finding in dispositions['findings']:
    fid = finding['finding_id']
    check(fid + ' exact issue route', finding['issue'] == expected_routes[fid])
    for peer_cap in finding['peer_receipts']:
        check(fid + ' exact selected peer reference', peer_cap in [g['peer_capture'] for g in selection['groups']] and sha(B / peer_cap['path']) == peer_cap['sha256'])
    for p in finding['successor_payload_bindings']:
        check(fid + ' selected payload binding ' + p['proposal_id'], p['after_capture'] == P[p['proposal_id']]['after_capture'])
    route_rows.append(dict(finding_id=fid, issue=finding['issue'], issue_url=f"https://github.com/CultureBotAI/MediaIngredientMech/issues/{finding['issue']}",
        status=finding['status'], bounded_disposition=finding['bounded_disposition'],
        proposal_ids=[p['proposal_id'] for p in finding['successor_payload_bindings']],
        case_ids=[c['case_id'] for c in finding['successor_case_bindings']], peer_receipts=finding['peer_receipts'],
        disposition_ledger=cap(dispositions_path), locator=f"findings[finding_id={fid}]",
        maintained_or_release_approval=finding['maintained_or_release_approval'], github_issue_closed=finding['github_issue_closed']))
check('all12 exact routes and no1173 misuse', len(route_rows) == 12 and {x['finding_id']: x['issue'] for x in route_rows} == expected_routes and all(x['issue'] != 1173 for x in route_rows))

# Retain every case's operative factual requirements and all native decisions.
case_holds = []
for d in decisions:
    original = D0[d['case_id']]
    check(d['case_id'] + ' source/native identity preserved', all(d.get(k) == original.get(k) for k in ['source', 'case_input_sha256', 'occurrence_ids', 'preserved_native_decisions']))
    case_holds.append({k: d.get(k) for k in ['case_id', 'source', 'case_input_sha256', 'occurrence_ids', 'proposal_ids', 'disposition', 'reasoning', 'missing_requirement', 'no_change_reason', 'preserved_native_decisions']})
proposal_holds = []
for pid, p in P.items():
    x = payloads[pid]
    proposal_holds.append(dict(proposal_id=pid, selected_capture=p['after_capture'], case_ids=p['case_ids'],
        publication_review_obligations=p['publication_review_obligations'], cross_shard_conflict=p.get('cross_shard_conflict'),
        unresolved_component_fields=[dict(index=i, component=c) for i, c in enumerate(x.get('components', [])) if c.get('reference_scope') == 'UNMAPPED'],
        notes_locator=dict(capture=p['after_capture'], pointer='/notes'),
        component_assertion=x.get('component_assertion'),
        scientific_peer=next(g['peer_capture'] for g in selection['groups'] if g['name'] == cohort_for[pid])))

write('mapping-evidence-coverage.json', dict(entries=mapping_rows, retained_inherited_human=retained_human))
write('component-followup-coverage.json', dict(entries=component_rows, original_requested_proposal_count=32,
    scope='Mechanical reconciliation of exact original32 IDs and all adjudicated slots; no scientific approval of own organic proposals or inherited owner claims.'))
write('completeness-coverage.json', dict(counts=split, entries=complete_rows,
    scope='The five literal-source COMPLETE declarations are not claims of finished molecular composition. Five exclusions are separately assessed PARTIAL outcomes, not automatic enum changes.'))
write('issue-routing-coverage.json', dict(entries=route_rows, scope='Local exact routing and disposition accounting; no live GitHub state or issue closure claim.'))
write('payload-selection-coverage.json', dict(entries=payload_rows))
write('remaining-holds.json', dict(cases=case_holds, proposals=proposal_holds,
    owner_admission_status=validation['owner_admission_status'], owner_admission_failures=validation['owner_admission_failures'],
    approval_boundary=selection['approval_boundary'],
    scope='Preserved operative case statements and component/owner obligations. Their scientific adequacy rests on the selected independent cohort receipts, not this accounting check. Known inherited role/alias/chemistry and source holds remain linked to those complete receipts.'))
write('checks.json', checks)
failures = [x for x in checks if not x['passed']]
report = dict(reviewer='worker08:/root/organics', at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    kind='mechanical_action_coverage', scientific_review=False, self_science_approval=False,
    status='PASS_WITH_RETAINED_HOLDS' if not failures else 'BOOKKEEPING_FINDINGS',
    scope='Final issue1227 action accounting only. No network, native rerun, maintained change, author correction or issue mutation.',
    input_hashes=inputs, groups=group_rows,
    counts=dict(cases=len(decisions), proposals=len(proposals), changed_payloads=changed_count,
        unchanged_payloads=len(payload_rows)-changed_count, mapping_evidence_entries=len(mapping_rows),
        mapping_evidence_payloads=len({x['proposal_id'] for x in mapping_rows}),
        original_component_followup_proposals=len(component_rows), completeness_total=len(complete_rows),
        completeness=split, issue_routes=len(route_rows), cases_with_remaining_requirements=sum(bool(d['missing_requirement']) for d in decisions)),
    root_validation=dict(capture=cap(S / 'validation/combined-validation.json'),
        bounded_correction_status=validation['bounded_correction_validation_status'],
        owner_admission_status=validation['owner_admission_status'], owner_admission_failures=validation['owner_admission_failures'],
        strict_exit_code=validation['strict_exit_code'], baseline_partonomy_violations=len(validation['baseline_partonomy_violations']),
        overlay_partonomy_violations=len(validation['overlay_partonomy_violations']), scientific_approval=False, release_approval=False),
    coverage_artifacts={name: cap(R / name) for name in ['mapping-evidence-coverage.json', 'component-followup-coverage.json', 'completeness-coverage.json', 'issue-routing-coverage.json', 'payload-selection-coverage.json', 'remaining-holds.json', 'checks.json']},
    check_count=len(checks), failures=failures,
    excluded_preliminary_concern='Organic review-v2 is the current selected independent receipt and binds organic author-v3 indices and exact R2A bytes. Differing review and author version numbers are not a mismatch. This was checked and excluded before the final verdict.',
    limitations=['This accounting does not newly approve any scientific identity, source equivalence, role, alias, whole owner, source membership or export.',
        'The TSB primary-identity collision remains an explicit owner-admission hold; the bounded grade/evidence correction is separately validated.',
        'No live issue state was fetched; issue URLs preserve the coordinator routing already authorized and captured.',
        'The full selected peer receipts, rather than the author version labels, govern scientific coverage.'])
write('receipt.json', report)
print(json.dumps(dict(status=report['status'], counts=report['counts'], checks=len(checks), failures=failures,
    receipt_sha256=sha(R / 'receipt.json')), indent=2))
