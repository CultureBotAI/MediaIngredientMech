from pathlib import Path
import copy
import datetime
import hashlib
import json
import os
import subprocess
import sys

import yaml
from mediaingredientmech.validation.component_partonomy import load_ingredient_records, validate_component_partonomy

O = Path(__file__).resolve().parent
W = O.parents[2]
R = W / 'reports/all_unmatched_20261107/worker-06'
S = R / 'successor-v5'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def read(p):
    return json.loads(p.read_text())


def digest(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode()).hexdigest()


def save(n, obj):
    with (O / n).open('x') as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
        f.write('\n')


def flatten(value, pointer=''):
    if isinstance(value, dict) and value:
        return {p: v for k, sub in value.items() for p, v in flatten(sub, pointer + '/' + str(k).replace('~', '~0').replace('/', '~1')).items()}
    if isinstance(value, list) and value:
        return {p: v for k, sub in enumerate(value) for p, v in flatten(sub, pointer + '/' + str(k)).items()}
    return {pointer: value}


def trace(before, after, kind):
    b, a = flatten(before), flatten(after)
    rows = []
    for pointer in sorted(a.keys() | b.keys()):
        status = 'UNCHANGED' if pointer in b and pointer in a and b[pointer] == a[pointer] else 'CHANGED' if pointer in b and pointer in a else 'ADDED' if pointer in a else 'REMOVED'
        if status == 'UNCHANGED':
            assessment = 'Exact beforeimage field preserved. Inherited mapping, roles, aliases and history remain historical; no new approval.'
        elif kind == 'payload' and pointer.startswith('/components/'):
            assessment = 'Checked against the exact source row and independently verified native component-form binding; copper remains literal and UNMAPPED.'
        elif kind == 'payload' and pointer.startswith('/component_assertion/'):
            assessment = 'Source-relative seven-input transcription only. COMPLETE does not settle copper, owner continuity or release. Raw source formula, amount/unit, and precise locator are retained.'
        elif kind == 'payload' and pointer == '/notes':
            assessment = 'Original note retained as prefix; added explicit NONINSTALLABLE scope, receiving dose, literal source conflict, historical-owner context and unresolved applicability.'
        elif kind == 'payload' and pointer.startswith('/curation_history/7/'):
            assessment = 'New root-authored LLM-assisted held-draft event; authentic seven-event history prefix remains unchanged and no status promotion is claimed.'
        elif kind == 'payload':
            raise AssertionError(('Unexpected payload delta', pointer))
        else:
            assessment = 'Exact held source-outcome/proposal field reviewed in full, including immutable source/occurrence continuity, noninstallation and informational classification.'
        rows.append({'pointer': pointer, 'status': status, 'before_present': pointer in b, 'after_present': pointer in a, 'before': b.get(pointer), 'after': a.get(pointer), 'assessment': assessment})
    return rows


pre = read(O / 'scientific-prereview-v1.json')
identities = read(O / 'component-identities-v1.json')
confirmed = read(O / 'component-identities-confirmed-v1.json')
held_doc = read(S / 'held-proposals.json')
held = held_doc['held_proposals'][0]
assert held_doc['excluded_from_proposals_json'] is True and len(held_doc['held_proposals']) == 1
assert held['held_proposal_id'] == 'V5-H-A5-M2499'
before_path, after_path = R / held['before_capture']['path'], R / held['after_capture']['path']
assert sha(before_path) == held['before_sha256'] == held['before_capture']['sha256'] == pre['authentic_before_owner']['sha256']
assert before_path.read_bytes() == (W / held['owner_path']).read_bytes()
assert before_path.read_bytes() == subprocess.check_output(['git', 'show', pre['published_before_head'] + ':' + held['owner_path']], cwd=W)
assert sha(after_path) == held['after_capture']['sha256'] == 'd2d1399244a70e70562649af5201f1f1a0ec53f800cb0a1477f1e2f10d11cf07'
before, after = yaml.safe_load(before_path.read_text()), yaml.safe_load(after_path.read_text())
assert before == pre['authentic_before_owner']['full_record']
assert set(after) - set(before) == {'components', 'component_assertion'}
assert set(before) <= set(after)
for key in before:
    if key not in {'notes', 'curation_history'}:
        assert before[key] == after[key], key
assert after['notes'].startswith(before['notes'] + '\n\n')
assert after['curation_history'][:-1] == before['curation_history']
assert len(before['curation_history']) == 7
assert after['curation_history'][-1]['curator'] == 'Codex worker06 /root' and after['curation_history'][-1]['llm_assisted'] is True
assert after['identifier'] == held['identifier'] == 'MICRO:0001349'
assert held['kind'] == 'held_existing_owner_source_draft'
assert held['installable'] is False and held['status'] == 'NONINSTALLABLE_SOURCE_TRANSCRIPTION'
assert 'NONINSTALLABLE' in after['notes'] and 'NOT INSTALLABLE' in after['curation_history'][-1]['changes']
assert after['component_assertion']['method'] == 'RECIPE_TRANSCRIPTION'
assert after['component_assertion']['completeness'] == 'COMPLETE'
assert after['component_assertion']['evidence'][0]['evidence_type'] == 'RECIPE_SOURCE'
assert after['component_assertion']['evidence'][0]['source'] == pre['primary_evidence']['url']
assert len(after['components']) == 7

component_reviews = []
expected_components = []
for i, source_row in enumerate(pre['literal_components']):
    raw = source_row['raw_component']
    part = after['components'][i]
    expected = {'component_name': raw['component_name'], 'reference_scope': 'UNMAPPED', 'concentration_value': str(raw['volume']), 'concentration_unit': {'L': 'L', 'g/L': 'G_PER_L'}[raw['unit']]}
    support = None
    if i != 5:
        match = next(x for x in identities['results'] if x['raw_TOGO_component_name'] == raw['component_name'])
        expected.update({'component_name': match['recommended_component_name'], 'reference_scope': 'MIM_CATALOG', 'component_id': match['component_id']})
        assert sha(W / match['authentic_owner']['path']) == match['authentic_owner']['sha256']
        support = next(x for x in confirmed['results'] if x['component_id'] == match['component_id'])
        assert sha(O / support['raw_capture']['path']) == support['raw_capture']['sha256']
    assert part == expected, (i, part, expected)
    expected_components.append(expected)
    component_reviews.append({'index': i, 'literal_source_pointer': source_row['json_pointer'], 'literal_source_row': raw, 'reviewed_final_component': part, 'native_component_binding': support, 'decision': 'LITERAL_CONFLICT_UNMAPPED' if i == 5 else 'SOURCE_FORM_MATCH_TO_CURRENT_NATIVE_OWNER', 'limits': 'No child whole-owner, role or export approval. Parent applicability remains held.'})
assert 'Na2MoO4 · 2H2O' in after['component_assertion']['evidence'][0]['notes']
assert 'Sodium molybdate dihydrate' == pre['literal_components'][1]['raw_component']['label']

draft_d = read(S / 'author-draft/decisions.json')
decision = draft_d['decisions'][112]
before_decision = pre['published_before_case_outcome']
for key in ['case_id', 'case_input_sha256', 'source', 'occurrence_ids', 'disposition', 'proposal_ids', 'reviewed_source_index']:
    assert decision[key] == before_decision[key]
assert decision['proposal_ids'] == [] and decision['held_proposal_ids'] == [held['held_proposal_id']]
assert decision['owner_records'] == [{'path': held['owner_path'], 'sha256': held['before_sha256']}]
assert decision['missing_requirement'] == held['application_hold']
assert held['case_ids'] == [decision['case_id']] and held['occurrence_ids'] == decision['occurrence_ids']
assert held['source_recipe'] == 'CultureMech:009072'
assert decision['prior_v5_independent_review'] == before_decision['independent_review']
assert decision['independent_review'] == held['independent_review'] == {'status': 'pending', 'evidence_ids': []}
assert decision['successor_scope_classification'] == 'INFO004 informational scope completion; no new unsafe-mapping allegation.'
assert decision['evidence_ids'] == before_decision['evidence_ids'] + ['V5-E-A5-CONTINUITY', 'V5-E-AUTHOR']
proposals = read(S / 'author-draft/proposals.json')['proposals']
assert len(proposals) == 105
assert not any(x.get('owner_path') == held['owner_path'] or x.get('after_capture') == held['after_capture'] or x.get('proposal_id') == held['held_proposal_id'] for x in proposals)
assert decision['case_id'] not in {cid for p in proposals for cid in p['case_ids']}
old_evidence = read(R / 'successor-v4/evidence.json')['evidence']
new_evidence = read(S / 'author-draft/evidence.json')['evidence']
assert new_evidence[:len(old_evidence)] == old_evidence
assert next(x for x in new_evidence if x['evidence_id'] == 'C-E-togo-M2499') == pre['primary_evidence']
for eid in decision['evidence_ids']:
    ev = next(x for x in new_evidence if x['evidence_id'] == eid)
    if ev['capture']['root'] == 'artifact':
        assert sha(R / ev['capture']['path']) == ev['capture']['sha256']

catalog_paths = sorted((W / 'data/ingredients').rglob('*.yaml'))
inventory = [{'path': str(p.relative_to(W)), 'sha256': sha(p)} for p in catalog_paths]
save('final-overlay-catalogue-binding.json', inventory)
catalog = load_ingredient_records(W / 'data/ingredients')
before_violations = validate_component_partonomy(catalog)
assert sum(x['identifier'] == 'MICRO:0001349' for x in catalog) == 1
overlay = [after if x['identifier'] == 'MICRO:0001349' else x for x in catalog]
after_violations = validate_component_partonomy(overlay)
assert not before_violations, [str(x) for x in before_violations]
assert not after_violations, [str(x) for x in after_violations]
save('final-partonomy-v1.json', {'reviewer': '/root/residual_stock_review', 'method': 'Native load_ingredient_records + validate_component_partonomy over the complete current individual catalogue; private in-memory substitution of the one authentic MICRO:0001349 owner with the held draft. No maintained writes or installation implied.', 'native_module': {'path': 'src/mediaingredientmech/validation/component_partonomy.py', 'sha256': sha(W / 'src/mediaingredientmech/validation/component_partonomy.py')}, 'catalogue_records': len(catalog), 'catalogue_inventory_sha256': sha(O / 'final-overlay-catalogue-binding.json'), 'baseline_violations': [str(x) for x in before_violations], 'held_overlay_violations': [str(x) for x in after_violations], 'held_payload_sha256': sha(after_path), 'installable': False})

cmd = [sys.executable, str(W / 'scripts/validate_strict.py'), str(after_path), '--workers', '1', '--out', str(O / 'final-strict-schema.tsv')]
run = subprocess.run(cmd, cwd=O, env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1'), capture_output=True, text=True)
with (O / 'final-strict-schema.log').open('x') as f:
    f.write(run.stdout + run.stderr)
save('final-strict-schema-command.json', {'argv': cmd, 'cwd': str(O), 'PYTHONDONTWRITEBYTECODE': '1', 'pytest_used': False, 'coverage_used': False, 'returncode': run.returncode, 'stdout': run.stdout, 'stderr': run.stderr, 'validator_sha256': sha(W / 'scripts/validate_strict.py'), 'schema_sha256': sha(W / 'src/mediaingredientmech/schema/mediaingredientmech.yaml')})
assert run.returncode == 0

controls = []
bad = copy.deepcopy(after)
bad['components'][5]['component_name'] = 'CuSO4・5H2O'
controls.append({'control': 'Silently repair literal CuSO2 to CuSO4 while remaining UNMAPPED', 'native_partonomy_errors': [str(x) for x in validate_component_partonomy([bad if x['identifier'] == 'MICRO:0001349' else x for x in catalog])], 'source_fact_comparison_rejects': bad['components'] != expected_components, 'lesson': 'Shape/partonomy cannot certify source chemistry; exact primary-row comparison independently rejects normalization.'})
bad = copy.deepcopy(after)
bad['components'][1]['concentration_unit'] = 'G'
controls.append({'control': 'Convert printed stock g/L into batch g using added water as denominator', 'native_partonomy_errors': [str(x) for x in validate_component_partonomy([bad if x['identifier'] == 'MICRO:0001349' else x for x in catalog])], 'source_fact_comparison_rejects': bad['components'] != expected_components, 'lesson': 'The primary explicitly prints g/L, while 1 L water is a separate input; no measured final-volume conversion is authorized.'})
bad_held = copy.deepcopy(held)
bad_held['installable'] = True
controls.append({'control': 'Promote held draft to installable', 'noninstallable_scope_rejects': bad_held['installable'] is not False, 'lesson': 'Native-valid payloads cannot clear unresolved copper or shared-owner applicability.'})
assert all(x.get('source_fact_comparison_rejects', x.get('noninstallable_scope_rejects')) for x in controls)
save('focused-negative-controls-v1.json', {'reviewer': '/root/residual_stock_review', 'method': 'Adversarial copies only in private memory. Original candidate bytes unchanged. Native results and independent source/scope comparisons are reported separately.', 'controls': controls})

fieldtrace = {'payload': trace(before, after, 'payload'), 'source_outcome': trace(before_decision, decision, 'case'), 'held_proposal_full_fields': trace({}, held, 'held_proposal')}
save('final-fieldtrace-v1.json', fieldtrace)
bindings = {str(p.relative_to(W)): sha(p) for p in [S / 'held-proposals.json', before_path, after_path, S / 'author-draft/decisions.json', S / 'author-draft/proposals.json', S / 'author-draft/evidence.json', S / 'changed-payloads.json', S / 'author-assessment.json']}
receipt = {'schema_version': '1.0.0', 'review_id': 'info004-a5-independent-final-science-v1', 'reviewed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'reviewer': '/root/residual_stock_review', 'correction_author': 'Codex worker06 /root', 'llm_assisted': True, 'independence': 'Reviewer authored neither authentic maintained owner nor historical case nor final root candidate. Native identity advisory did not create or edit any candidate.', 'status': 'PASS_BOUNDED_LITERAL_TRANSCRIPTION_REVIEW_WITH_NONINSTALLABLE_OWNER_HOLD', 'classification_preserved': 'W06-S1217-INFO-004 informational scope completion', 'issue': decision['issue_refs'][0], 'published_before_head': pre['published_before_head'], 'scope': {'held_native_payloads': 1, 'source_cases': 1, 'CM_occurrences': 1, 'case_index': 112, 'immediate_inputs': 7, 'native_supported_child_references': 6, 'literal_unmapped_copper_inputs': 1, 'whole_owner_role_export_approval': False, 'installable': False}, 'input_bindings': bindings, 'prereview': {'path': 'scientific-prereview-v1.json', 'sha256': sha(O / 'scientific-prereview-v1.json')}, 'component_identity_reviews': [{'path': n, 'sha256': sha(O / n)} for n in ['component-identities-v1.json', 'component-identities-confirmed-v1.json', 'component-ontology-retry-v1.json']], 'before_payload_sha256': sha(before_path), 'final_payload_sha256': sha(after_path), 'held_proposal_canonical_sha256': digest(held), 'reviewed_full_held_proposal': held, 'source_case_canonical_sha256': digest(decision), 'reviewed_full_source_outcome': decision, 'canonical_algorithm': 'SHA256 of UTF-8 JSON, sorted keys, ensure_ascii=False, separators comma/colon.', 'component_reviews': component_reviews, 'assessments': [{'topic': 'Exact predecessor', 'decision': 'PASS', 'basis': 'Held beforeimage equals current native owner and actual published1d62 bytes. It is an authentic existing-owner draft, not a minted null-before identity.'}, {'topic': 'Complete exact field review', 'decision': 'PASS_WITH_APPLICATION_HOLD', 'basis': 'Read every final record/proposal/case field. Only components, component_assertion, appended notes and one honest LLM-assisted history event change the owner draft. All original identity, aliases, mapping, statistics, roles and historical events remain exact and explicitly unendorsed.'}, {'topic': 'Immediate list and source units', 'decision': 'PASS', 'basis': 'All seven source rows represented with exact stated numeric values; explicit g/L solutes preserved, 1 L distilled water retained as an input. One component uses the also-printed Sodium molybdate dihydrate label, with exact raw Na2MoO4 · 2H2O preserved in assertion notes. Receiving1ml/l and source receiving pH7.1 are confined to notes and not converted into stock concentrations or pH.'}, {'topic': 'Copper and catalogue identity', 'decision': 'HELD', 'basis': 'CuSO2・5H2O remains literal UNMAPPED. Current native owner already links this same source and other BG11 contexts. Missing copper/applicability evidence cannot establish a new owner or authorize applying this list across the shared owner.'}, {'topic': 'Technical gates versus scientific scope', 'decision': 'PASS_WITH_LIMITS', 'basis': 'Closed-schema and complete catalogue overlay partonomy pass. Adversarial copper repair and unit conversion can pass structural partonomy yet fail exact primary-source comparison; technical success confers no application or release approval.'}], 'remaining_genuine_holds': ['Authoritative original/corrected copper specification for M2499 before exact chemical interpretation.', 'Exact formulation applicability across MICRO:0001349 source/history scope, including independently conflicting JCM1357 context.', 'Frozen CultureMech receiving dose unit discrepancy remains an upstream hold; no maintained repair performed.', 'Inherited MICRO exact mapping, TRACE_ELEMENT role, aliases and child-owner deficiencies are not approved by this source-only draft.'], 'field_trace': {'path': 'final-fieldtrace-v1.json', 'sha256': sha(O / 'final-fieldtrace-v1.json')}, 'checks': [{'name': 'Native closed-schema', 'status': 'PASS', 'receipt': 'final-strict-schema-command.json', 'sha256': sha(O / 'final-strict-schema-command.json')}, {'name': 'Native complete catalogue private overlay partonomy', 'status': 'PASS', 'receipt': 'final-partonomy-v1.json', 'sha256': sha(O / 'final-partonomy-v1.json')}, {'name': 'Focused scientific scope negative controls', 'status': 'PASS', 'receipt': 'focused-negative-controls-v1.json', 'sha256': sha(O / 'focused-negative-controls-v1.json')}], 'findings': [], 'limits': ['Receipt binds exact root-authored draft payload and author-draft source outcome; later final-core review metadata requires separate binding.', 'Only case112 A5 science is assessed; PPG and DI-water science remain separate reviewer scopes.', 'No whole-owner, native support, roles, SSSOM/release, coordinator source-case acceptance, maintained write or owner merge is granted.']}
assert sha(after_path) == held['after_capture']['sha256']
assert all(sha(W / path) == value for path, value in bindings.items())
save('final-science-v1.json', receipt)
with (O / 'final-science-v1.md').open('x') as f:
    f.write('The exact held MICRO:0001349 draft passes this bounded source-transcription review. It remains noninstallable. All seven TOGO M2499 inputs are represented; the unresolved copper formula stays literal and UNMAPPED, while six supported forms reference verified current native identities. COMPLETE describes the printed immediate list only.\n\n')
    f.write('The authentic existing-owner beforeimage, historical mappings, aliases, roles and all prior history are preserved. The source’s 1 ml/l receiving dose, explicit stock g/L values and added 1 L distilled water are kept separate; no measured final volume or receiving pH is assigned to the stock. The molybdate component uses the also-printed source label and preserves its exact raw formula in assertion notes.\n\n')
    f.write('Native strict schema and the complete current catalogue with this one held in-memory overlay pass. The controls demonstrate why those gates alone cannot detect a fabricated copper correction or stock-unit reinterpretation. No new finding was identified. Copper identity and applicability across the existing owner’s source history remain genuine holds.\n\n')
    f.write('Exact payload SHA256: `' + sha(after_path) + '`. Full scientific receipt SHA256: `' + sha(O / 'final-science-v1.json') + '`. Exact every-field traces and full source/held-proposal objects are retained separately. Reviewer `/root/residual_stock_review` is distinct from root author. This grants no owner, role, source-case acceptance, export or installation approval.\n')
print(json.dumps({'receipt': str(O / 'final-science-v1.json'), 'sha256': sha(O / 'final-science-v1.json'), 'fieldtrace_sha256': sha(O / 'final-fieldtrace-v1.json'), 'payload_sha256': sha(after_path), 'case_canonical_sha256': digest(decision), 'held_proposal_canonical_sha256': digest(held), 'catalogue_records': len(catalog), 'new_findings': 0, 'installable': False}))
