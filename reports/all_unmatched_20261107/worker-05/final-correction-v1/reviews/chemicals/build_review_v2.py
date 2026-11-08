from pathlib import Path
import ast, copy, datetime, hashlib, json, yaml

N = Path('.temp/w05-final-correction-v1')
L, A, B = N / 'review-chemicals', N / 'chemicals', N / 'chemical-supplement-v1'
C = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
R = Path('reports/all_unmatched_20261107/worker-05')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def obj(x): return hashlib.sha256(json.dumps(x, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode()).hexdigest()
def read(p): return json.loads(p.read_text())
def save(name, value):
    p = L / name
    assert not p.exists(), p
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    return p
def path(c):
    if c['root'] == 'source': return C / 'queue/preliminary-v5' / c['path']
    if c['path'].startswith('final-correction-v1/'): return N / Path(c['path']).relative_to('final-correction-v1')
    return R / c['path']
def changes(a, b, at=''):
    if type(a) != type(b): return [at]
    if isinstance(a, dict):
        return [p for k in sorted(a.keys() | b.keys()) for p in ([at + '/' + k] if k not in a or k not in b else changes(a[k], b[k], at + '/' + k))]
    if isinstance(a, list):
        if len(a) != len(b): return [at + '/length']
        return [p for i, (x, y) in enumerate(zip(a, b)) for p in changes(x, y, at + '/' + str(i))]
    return [] if a == b else [at]

dp, ep, pp, sp = B / 'decisions-v2.json', B / 'evidence-v1.json', B / 'proposals-v1.json', B / 'primary-case-conclusions-v2.json'
D, E, P, S = map(read, [dp, ep, pp, sp])
D0 = read(N / 'remediation/chemical-report-v2/decisions-v3.json')
E0 = read(N / 'remediation/chemical-report-v1/evidence-v2.json')
P0 = read(A / 'proposals-v3.json')
S0 = read(N / 'remediation/chemical-report-v3/primary-case-conclusions-v3.json')
v1p = L / 'main-review-v1.json'
v1, oldaudit = read(v1p), read(L / 'binding-audit-v1.json')
assert len(D) == 67 and len(E) == 528 and len(P) == 58
assert P[:57] == P0 and E[:525] == E0
assert [i for i, (x, y) in enumerate(zip(D0, D)) if x != y] == [10, 48]
assert [i for i, (x, y) in enumerate(zip(S0['case_reviews'], S['case_reviews'])) if x != y] == [10, 48]
assert changes(read(B / 'decisions-v1.json'), D) == ['/10/disposition', '/48/disposition']
auditor = C / 'scripts/audit_worker_outcomes_v1.py'
allowed = next(ast.literal_eval(x.value) for x in ast.walk(ast.parse(auditor.read_text())) if isinstance(x, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'dispositions' for t in x.targets))
assert all(d['disposition'] in allowed for d in D)
for i, (before, after) in enumerate(zip(D0, D)):
    for key in ['case_id', 'case_input_sha256', 'occurrence_ids', 'preserved_source_holds']:
        assert before[key] == after[key], (i, key)
for i in [10, 48]:
    assert D[i]['disposition'] == 'new_distinct_ingredient_proposal'
    assert D[i]['no_change_reason'] is None and D[i]['missing_requirement'] is None
index = read(B / 'current-conclusion-bindings-v1.json')
historical = read(A / 'decisions-v2.json')
assert len(index['bindings']) == 67
for i, b in enumerate(index['bindings']):
    assert b['case_id'] == D[i]['case_id']
    assert b['current_decision_object_sha256'] == obj(D[i])
    embedded = S['case_reviews'][i]['decision_object_sha256']
    assert b['conclusion_embedded_sha256'] == embedded
    if i in [10, 48]:
        assert embedded == hashlib.sha256(json.dumps(D[i], sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    elif i in [56, 61, 63]:
        assert embedded == obj(historical[i])
    else:
        assert embedded == obj(D[i])
assert [d['case_id'] for d in D] == [r['case_id'] for r in v1['case_reviews']]
capture_checks = []
for e in E:
    f = path(e['capture'])
    assert sha(f) == e['capture']['sha256'], (e['evidence_id'], str(f))
    assert e.get('supports_or_contradicts')
    capture_checks.append({'evidence_id': e['evidence_id'], 'capture': e['capture'], 'resolved_path': str(f), 'actual_sha256': sha(f), 'scope': 'Byte integrity; scientific reading is attributed separately.'})
payload_checks = []
for i, p in enumerate(P):
    f = path(p['after_capture'])
    assert sha(f) == p['after_capture']['sha256']
    after = yaml.safe_load(f.read_text())
    if i < 57:
        prior = oldaudit['payload_checks'][i]
        assert p['proposal_id'] == prior['proposal_id'] and p['after_capture'] == prior['after_capture']
        if p.get('predecessor_after_capture'):
            pc = p['predecessor_after_capture']; assert sha(path(pc)) == pc['sha256']
            before = yaml.safe_load(path(pc).read_text())
        else:
            before = yaml.safe_load(Path(p['owner_path']).read_text())
        assert after['curation_history'][:len(before['curation_history'])] == before['curation_history']
        if p.get('before_sha256'): assert sha(Path(p['owner_path'])) == p['before_sha256']
        payload_checks.append(copy.deepcopy(prior))
    else:
        assert p['kind'] == 'new_owner' and p['before_sha256'] is None
        assert not Path(p['owner_path']).exists()
        assert after['identifier'] == 'kgmicrobe.compound:thiamine_hcl_monohydrate'
        assert after['ontology_mapping']['ontology_id'] == after['identifier']
        assert after['ontology_mapping']['mapping_quality'] == 'FALLBACK_REGISTRY'
        assert all(e['evidence_type'] == 'LLM_SUGGESTION' for e in after['ontology_mapping']['evidence'])
        assert not {'chemical_properties', 'components', 'component_assertion', 'supplied_form'} & after.keys()
        assert after['occurrence_statistics'] == {'total_occurrences': 6, 'media_count': 6}
        assert set(p['applies_to_occurrence_ids']) == set(D[10]['occurrence_ids'] + D[48]['occurrence_ids'])
        payload_checks.append({'proposal_id': p['proposal_id'], 'after_capture': p['after_capture'], 'owner_path': p['owner_path'], 'before_sha256': None, 'prior_history_preserved': 'New owner; no predecessor history exists.', 'field_changes_from_predecessor': ['new isolated record'], 'all_six_occurrence_routes_exact': True})
recipes = read(A / 'evidence-read-ledger-v1.json')['frozen_recipes']
for r in recipes: assert sha(C / 'queue/preliminary-v5' / r['path']) == r['sha256']
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
audit = {'reviewer': '/root/materials_research', 'at': now, 'status': 'PASS', 'errors': [], 'inputs': [{'path': str(p), 'sha256': sha(p)} for p in [dp, ep, pp, sp, v1p, L / 'binding-audit-v1.json', B / 'disposition-remediation-v2.json', L / 'monohydrate-owner-check-v1.json']], 'counts': {'cases': 67, 'payloads': 58, 'evidence_entries': 528, 'frozen_recipes': len(recipes)}, 'case_checks': [{'case_id': d['case_id'], 'selected_decision_object_sha256': obj(d), 'case_input_sha256': d['case_input_sha256'], 'occurrence_ids': d['occurrence_ids'], 'preserved_holds_sha256': obj(d['preserved_source_holds'])} for d in D], 'payload_checks': payload_checks, 'capture_checks': capture_checks, 'delta': {'unchanged_prior_payload_objects': 57, 'unchanged_prior_evidence_objects': 525, 'changed_decision_indices': [10, 48], 'changed_source_conclusion_indices': [10, 48], 'supplement_enum_fix_fields': changes(read(B / 'decisions-v1.json'), D), 'all_67_native_dispositions_valid': True, 'bottom_layer_and_mkp_amendments_unchanged': True}, 'limits': ['Hashes, enum checks and preservation are not scientific approval.', 'Original review remains immutable and records the review state before the monohydrate correction.', 'The author and coordinator own their closed-schema/overlay receipts; this reviewer ran the existing native inspect operation on all 58 exact paths. No maintained file, export or gate was changed.']}
auditp = save('binding-audit-v2.json', audit)
byE = {e['evidence_id']: e for e in E}
def binding(eid): return {k: byE[eid][k] for k in ['evidence_id', 'capture', 'kind', 'url', 'accessed_at', 'locator'] if k in byE[eid]}
review = copy.deepcopy(v1)
review.update(at=now, completed_at=now, status='complete', open_findings=0, review_completed=True)
review['completion_meaning'] = 'All 67 assigned chemical/prior-root cases and all 58 selected candidate payloads have received an attributed scientific review. This closes the report-review defects, not the documented molecular, family, source, owner or export holds.'
review['predecessor_review'] = {'path': str(v1p), 'sha256': sha(v1p), 'status_at_creation': 'needs_revision'}
review['selected_cumulative_inputs'] = {name: {'path': str(p), 'sha256': sha(p)} for name, p in [('decisions', dp), ('evidence', ep), ('proposals', pp), ('source_conclusions', sp)]}
review['reviewed_inputs'].update({str(p): sha(p) for p in [dp, ep, pp, sp, auditp, B / 'primary-assessment-and-read-ledger-v1.json', B / 'ancestry-and-remediation-v1.json', B / 'disposition-remediation-v2.json', B / 'native-projection-v1.json', L / 'monohydrate-owner-check-v1.json', Path('MAPPING_SEMANTICS.md'), L / 'native-inspect-v2.json']})
review['reviewed_inputs'].update({str(B / 'current-conclusion-bindings-v1.json'): sha(B / 'current-conclusion-bindings-v1.json'), str(B / 'FINAL-MANIFEST-v1.json'): sha(B / 'FINAL-MANIFEST-v1.json')})
review['source_conclusion_binding_basis'] = {'index': {'path': str(B / 'current-conclusion-bindings-v1.json'), 'sha256': sha(B / 'current-conclusion-bindings-v1.json')}, 'all_67_current_canonical_hashes_independently_verified': True, 'historical_embedded_hashes': {'indices': [56, 61, 63], 'basis': 'Original chemicals/decisions-v2.json before the root enum-only ASSEMBLY-002 amendment.'}, 'default_separator_embedded_hashes': {'indices': [10, 48], 'basis': 'Selected supplement decisions-v2.json with json.dumps default separators.'}, 'final_review_basis': 'Every case selected_decision_object_sha256 below binds the actual selected cumulative D using compact canonical JSON; no historical embedded hash is presented as that current binding.'}
review['scope']['payloads'] = 58
review['scope']['additional_source_defined_material'] = 1
review['scope']['source_read_scope'] = review['scope']['source_read_scope'].replace('All525 evidence', 'All 528 evidence') + ' The parent reviewer independently reread all six complete NBRC monohydrate recipe tables and their source/occurrence bindings, both ontology comparators, the full new payload, and the two amended decisions. The 57 previous payload bytes remain exact.'
read_by_id = {r['evidence_id']: r for r in review['read_primary_evidence']}
extra_reads = ['CHEM-CAP-f0c1b4928af89872', 'CHEM-CAP-1fc151e426d45042', 'CHEM-CAP-aa10057ea2c6f012', 'CHEM-CAP-f55e3a4d1efb7d51', 'CHEM-CAP-77de000b5fa8d1a6', 'CHEM-CAP-74b89743eed1808f', 'CHEM-CAP-14f6b2b7770adbee', 'CHEM-CAP-ba668efabffad3e5']
for eid in extra_reads:
    row = read_by_id.setdefault(eid, {**binding(eid), 'read_by': []})
    if '/root/materials_research' not in row['read_by']: row['read_by'].append('/root/materials_research')
review['read_primary_evidence'] = [read_by_id[k] for k in sorted(read_by_id)]
for i, (r, d) in enumerate(zip(review['case_reviews'], D)):
    r['selected_decision_object_sha256'] = obj(d)
    r['selected_source_conclusion_object_sha256'] = obj(S['case_reviews'][i])
    r['proposal_ids'] = d['proposal_ids']
    r['exact_selected_captures'] = [binding(eid) for eid in d['evidence_ids']]
    r['primary_crosschecks_actually_read'] = [{'evidence_id': eid, 'read_by': read_by_id[eid]['read_by']} for eid in d['evidence_ids'] if eid in read_by_id]
    if i in [10, 48]:
        r['status'] = 'review_complete_with_stated_limits'
        r['assessment'] = ('NBRC 1550, 1443, 1444, 1445 and 1447 each explicitly name the one-water Thiamine-HCl reagent. ' if i == 10 else 'NBRC 1507 independently names the one-water Thiamine-HCl reagent within its nested vitamin preparation. ') + 'One shared local source-defined material is supported together with the companion spelling case. The exact six occurrence routes and both raw spellings are preserved. The 5 mg input and 1 L water belong to a multivitamin recipe, not a single-solute stock or this material\'s chemical properties. The new record correctly asserts no CAS, formula, structure, chloride stoichiometry, supplier, parent relation or material components. Independent maintained/frozen/coordinator owner checks found no existing same-form owner in that bounded inventory. Molecular grounding and all source/export holds remain unresolved; they do not block this partial material representation.'
for i, p in enumerate(P[:57]):
    assert review['payload_reviews'][i]['selected_proposal_object_sha256'] == obj(p)
review['payload_reviews'][44]['assessment'] = 'Solid Tris hydrochloride CAS 1185-53-1 remains separate from free Tris. The exact YAML stores NARROW_MATCH; the pinned native builder emits skos:broadMatch to CHEBI:9754 plus the CAS and local registry identity rows. All three rows were inspected. No export or installation is approved.'
review['payload_reviews'][53]['assessment'] = 'The DSMZ 78 nominal 95% ethanol handle preserves twelve applicable source occurrences: eleven flat occurrences plus the DSMZ 212a occurrence. The receiving-stock facts and exact routes are retained. Neither aqueous 95% v/v ontology identity nor a different product is established; the conditional family hold remains.'
p = P[-1]
review['payload_reviews'].append({'proposal_id': p['proposal_id'], 'case_ids': p['case_ids'], 'selected_proposal_object_sha256': obj(p), 'after_capture': p['after_capture'], 'owner_path': p['owner_path'], 'before_sha256': None, 'predecessor_after_capture': None, 'assessment': 'The complete new record preserves one source-defined Thiamine-HCl monohydrate material for six explicit NBRC reagent occurrences. Both raw spellings remain sourced synonyms. Registry-only identity, SINGLE_INGREDIENT scope and six assigned occurrences are supported; no historical lot equivalence, molecular CAS/formula, parent, supplier, role or partonomy is invented. All six source recipes name 5 mg within multivitamin stocks, so their water, pH and doses correctly remain recipe context. Duplicate checks include ignored files, all maintained owners, frozen 981 payloads and the actual 37 pending coordinator payloads. No existing same-form owner was identified in those inventories. The six new mapping judgments are correctly attributed LLM_SUGGESTION, and the history records the actual author.', 'status': 'bounded_candidate_review_complete', 'exact_selected_captures': [binding(eid) for eid in p['evidence_ids']], 'whole_payload_read': True, 'applies_to_occurrence_ids': p['applies_to_occurrence_ids'], 'limits': 'Exact molecular grounding, historical supplier/lot identity, later same-form reconciliation and all frozen source/export holds remain. Native ManualMappingCuration projection text is a builder convention, not evidence of human authorship.', 'holds_released': False})
for f in review['finding_dispositions']:
    if f['finding_id'] == 'W05-FINAL-SKEPTIC-CHEM-003':
        f.update(status='resolved_after_exact_rereview', assessment='The independently checked supplement adds one bounded local monohydrate material, shared by the two source spelling cases and six exact occurrences. It preserves the positive one-water source identity without CAS, structure, chloride stoichiometry, supplier or parent claims. All original holds remain. The other 57 payloads and 525 evidence objects are unchanged.', remediation={'decisions': review['selected_cumulative_inputs']['decisions'], 'proposal_id': p['proposal_id'], 'after_capture': p['after_capture'], 'owner_check': {'path': str(L / 'monohydrate-owner-check-v1.json'), 'sha256': sha(L / 'monohydrate-owner-check-v1.json')}})
    if f['finding_id'] == 'FILED-1238-SOLID-TRIS':
        f['assessment'] = 'Solid Tris hydrochloride retains CAS 1185-53-1 and stores NARROW_MATCH. The pinned native builder emits skos:broadMatch to Tris, plus exact CAS and local identity rows. This complete three-row projection is supported; the stored grade and emitted predicate are distinct fields. The correction remains separate from nominal buffer component claims.'
    if f['finding_id'] == 'W05-FINAL-ASSEMBLY-002':
        f['dependent_binding_disposition'] = 'The additive uniform current-conclusion-bindings-v1 index correctly explains three retained pre-enum decision hashes and two default-separator supplement hashes. All 67 current canonical hashes and every stated historical/serialization basis were independently verified. Scientific prose and exact payloads remain unchanged.'
for number, assessment, related in [
    (4, 'The final review now states twelve DSMZ ethanol routes, explicitly eleven flat occurrences plus the DSMZ 212a context. Exact matrix and case bindings were already correct. This corrects only review prose and asserts no family equivalence or difference.', None),
    (5, 'The two final review sentences now distinguish stored NARROW_MATCH from emitted skos:broadMatch. Exact candidate YAML and the complete three-row projection already had the supported values; only review prose changed.', None),
    (6, 'The immutable supplement successor changes only the two invalid disposition values to new_distinct_ingredient_proposal and updates their source-conclusion hash bindings. All scientific text, payloads, evidence, raw routes and holds are unchanged. The exact auditor AST confirms all 67 dispositions are valid.', 'W05-FINAL-ASSEMBLY-002')]:
    fp = L / f'finding-{number:03d}-initial.json'
    review['finding_dispositions'].append({'finding_id': f'W05-FINAL-SKEPTIC-CHEM-{number:03d}', 'status': 'resolved_after_exact_rereview', 'assessment': assessment, 'initial_finding': {'path': str(fp), 'sha256': sha(fp)}, 'deduplicated_cause': related, 'holds_released': False})
review['limits'][0] = 'Completion applies to this report-only scientific review. It does not approve installation, source remapping, inherited whole-owner claims or downstream export. Final assembled/native review remains coordinator-owned.'
review['limits'].append('CHEM-004 and CHEM-005 were reviewer-authored prose defects. Both initial reproductions remain immutable; final assembly review independently checks the corrected sentences. CHEM-006 is a separate supplement occurrence of the existing ASSEMBLY-002 enum cause.')
review['limits'].append('Source-conclusion embedded hashes have explicitly retained historical or default-separator bases in five cases. The additive index and this review provide independently verified current compact canonical bindings for all 67 cases; the old embedded values are not silently reinterpreted.')
review['binding_audit'] = {'path': str(auditp), 'sha256': sha(auditp)}
review['native_inspection'] = {'path': str(L / 'native-inspect-v2.json'), 'sha256': sha(L / 'native-inspect-v2.json'), 'exit_code': 0, 'scope': 'Existing native review tool inspected all 58 exact candidate paths. No save to maintained structured reviews.'}
assert len(review['case_reviews']) == 67 and len(review['payload_reviews']) == 58
assert all(r['exact_selected_captures'] and r['primary_crosschecks_actually_read'] for r in review['case_reviews'])
assert all(r['whole_payload_read'] for r in review['payload_reviews'])
reviewp = save('main-review-v2.json', review)
print(json.dumps({'review': {'path': str(reviewp), 'sha256': sha(reviewp)}, 'audit': {'path': str(auditp), 'sha256': sha(auditp)}, 'cases': 67, 'payloads': 58, 'evidence_entries': 528, 'open_findings': 0}, indent=2))
