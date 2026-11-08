"""Bounded author correction; writes only this new successor cohort directory."""
import copy
import datetime
import hashlib
import json
import pathlib
import shutil
import sys

import yaml

sys.path.insert(0, str(pathlib.Path('src').resolve()))
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.write_validated import write_validated_ingredient, validate_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy

R = pathlib.Path('reports/all_unmatched_20261107/worker-08')
O = R / 'successors/issue-1227-v1/research/inorganic_forms'
S = R / 'successors/issue-1227-v1'
A = json.loads((O / 'assignment.json').read_text())
E = {e['evidence_id']: e for e in json.loads((R / 'successors/issue-1201-v1/evidence.json').read_text())['evidence']}
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def objsha(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode()).hexdigest()

def save(name, data):
    p = O / name
    assert p.resolve().is_relative_to(O.resolve())
    assert not p.exists(), f'Refusing to overwrite {p}'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + '\n')
    return {'root': 'artifact', 'path': str(p.relative_to(R)), 'sha256': sha(p)}

def cap(p):
    return {'root': 'artifact', 'path': str(p.relative_to(R)), 'sha256': sha(p)}

def append_unique(row, key, values):
    row.setdefault(key, [])
    for value in values:
        if value not in row[key]:
            row[key].append(value)

P = copy.deepcopy(A['proposals'])
D = copy.deepcopy(A['decisions'])
old_docs = [yaml.safe_load((R / p['after_capture']['path']).read_text()) for p in P]
before_docs = []
for p in P:
    fp = pathlib.Path(p['owner_path'])
    assert (sha(fp) if fp.exists() else None) == p['before_sha256']
    before_docs.append(yaml.safe_load(fp.read_text()) if fp.exists() else None)
    assert sha(R / p['after_capture']['path']) == p['after_capture']['sha256']

# Each tuple is a scientific judgment about this assertion, not an enum-wide rewrite.
SOURCE_FACTS = {
  7: ('if1201-primary-8d21944b91f35c26', 'DSMZ 533 explicitly requires deionized H2O. Deionization denotes a supplied process grade, not a different water molecule or proof of distillation.'),
  8: ('if1201-primary-64f31eb0476579a8', 'DSMZ 1094 trace-element preparation uses 2 N NaOH for EDTA pH adjustment. It does not enumerate the constituents of that NaOH stock.'),
  9: ('if1201-primary-8fe937c1ef6c1c21', 'JCM 1130 adds 26 ml of 10 N NaOH to the VFA mix; JCM 1385 explicitly inherits 1130. The VFA constituents are not constituents of the input NaOH stock.'),
 10: ('if1201-primary-cc603fec73e91848', 'ATCC 929 phenol-red preparation adds 1 ml of 6 N NaOH and 99 ml DI water. The latter is a receiving-mixture input and does not specify the stock carrier.'),
 11: ('if1201-primary-689514d53e5e1369', 'PCR-S11 M2262 adds 1.488 g Na2-EDTA to 40 ml of 0.1 N NaOH. It does not enumerate the NaOH stock carrier. NOS and other occurrences remain conditional comparisons.'),
 12: ('if1201-primary-9b35c1d4f58911cf', 'DSMZ 104 adjusts the receiving medium to pH 7.2 using 8 N NaOH. Its stock ingredient list is not enumerated.'),
 13: ('if1201-primary-ac859ea47d4d9d03', 'JCM 221 reducing solution uses 200 ml of 0.2 N NaOH, boils and cools it under N2/H2 before adding sulfide and cysteine. Those later inputs are outside the NaOH stock.'),
 14: ('if1201-primary-9fd6532d63c338f4', 'M3152 mineral preparation dissolves nitrilotriacetate in 10 ml of 0.5 N NaOH before subsequent dilution and salt addition. No closed NaOH stock formula is supplied.'),
 15: ('if1201-primary-544c5e9dc0318360', 'ATCC 1340 supplies N NaOH (4 g/100 ml), 30 ml, as a separate reducing-agent input. The stock carrier is unspecified; receiving water is not transferred into its composition.'),
 16: ('if1201-primary-d750934e49c5d7a2', 'JCM 574 potassium phosphate buffer combines 16.6 ml of 1 M KH2PO4 with 83.4 ml of 1 M K2HPO4 and an equal volume of water. The individual KH2PO4 stock carrier and hydration are unspecified.'),
 17: ('if1201-primary-d750934e49c5d7a2', 'JCM 574 supplies a 1 M K2HPO4 input stock, 83.4 ml per buffer batch. Later dilution water belongs to the buffer; stock carrier and hydration are unspecified.'),
 18: ('if1201-primary-2dca2ffb29c8ce04', 'M2760 PBBM phosphate-buffer block supplies 10 ml of 1 M Na2HPO4. Neither stock carrier nor salt hydration is specified.'),
 19: ('if1201-primary-689514d53e5e1369', 'M2262 paragraphs 14–15 enumerate NaH2PO4, 6 g, and distilled water, 1 L, for the nominal 50 mM stock. Both literal inputs are retained. Molecular form and a final-volume assertion are not inferred.'),
 20: ('if1201-primary-689514d53e5e1369', 'M2262 paragraphs 17–18 enumerate Na2HPO4, 3.55 g, and distilled water, 500 ml, for the nominal 50 mM stock. Both literal inputs are retained; hydration and exact final volume remain unasserted.'),
 21: ('if1201-primary-689514d53e5e1369', 'M2262 Na-PO4 block specifies 100 ml of each 50 mM input stock and a further pH adjustment to 7.5. Its unnamed adjustment reagent is an explicit omitted input, so PARTIAL remains.'),
 22: ('if1201-primary-c6b92a666534f07e', 'M2231 paragraph 9 enumerates literal K2HPO4·7H2O, 6 g, and deionized water, 1 L. The receiving recipe doses 5 ml of that stock. Both printed inputs are retained; chemical validity of seven waters remains unresolved.'),
 23: ('if1201-primary-8ea073f0e9d75d9e', 'JCM 908 supplies filter-sterilized 10% w/v sodium sulfide nonahydrate stock, 7.5 ml. The source does not close the stock ingredient list or identify its carrier.'),
 24: ('if1201-primary-dd57a72ec921bd3c', 'JCM 713 supplies separately filter-sterilized 24% Na2S·9H2O, 1 ml, to Solution C. Carrier and percent basis are unspecified; no complete stock formula is printed.'),
 25: ('if1201-primary-001df4b85017801c', 'ATCC 1943 supplies 2.5% Na2S·9H2O, 10 ml, prepared under nitrogen and autoclaved. Carrier and percent basis are not enumerated; PBBM is a conditional comparison.'),
 29: ('if1201-primary-83778d5874917c61', 'ATCC 1942 doses 10 ml of its nitrogen-autoclaved 5% nonahydrate stock to obtain 0.5 g/L; this supports its w/v basis. Carrier and complete stock formula are unstated. Other 5% stocks remain conditional comparisons.'),
 30: ('if-case-178', 'Frozen MediaDive ingredient 552 source_record.attribute gives 5.0 g in 100 ml H2O; source_record.amount=10 and unit=ml describe receiving dose. Both literal stock inputs are retained. Conflicting automated ingredient metadata does not settle the salt hydration.'),
 31: ('if1201-primary-63e0756405ba0a74', 'JCM 941 Solution C enumerates literal Na2S2O4·2H2O, 5 g, and distilled water, 40 ml. Both inputs are retained. Nitrogen autoclaving is processing context, not an additional measured constituent; the unusual hydrate remains chemically unresolved.'),
}
# Correct deionized source ID by exact verified source URL (never infer a missing capture).
water_sources = [e for e in E.values() if e.get('url') == 'https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium533.pdf' and e['evidence_id'].startswith('if1201-primary')]
assert len(water_sources) == 1
SOURCE_FACTS[7] = (water_sources[0]['evidence_id'], SOURCE_FACTS[7][1])
NEW_MAPPING = {5, *range(7, 26), 29, 30, 31}
COMPLETE = {19, 20, 22, 30, 31}
UNKNOWN = {*range(8, 19), 23, 24, 25, 29}
assert len(NEW_MAPPING) == 23 and len(UNKNOWN) == 15
refinement = json.loads((S / 'inputs/coordinator-triage/completeness-adjudication-refinement.json').read_text())
ref_by_id = {r['proposal_id']: r for r in refinement['rows']}
assert len(refinement['rows']) == 34
for i in COMPLETE:
    assert ref_by_id[P[i]['proposal_id']]['root_triage_recommendation'] == 'COMPLETE_FOR_LITERAL_PRINTED_INPUT_LIST'
for i in UNKNOWN:
    assert ref_by_id[P[i]['proposal_id']]['recommended_completeness'] == 'UNKNOWN'

replace_prose = {
 'The carrier is not stated, so PARTIAL records only verified solute and mass/volume basis.': 'The carrier is not stated and source closure is unknown; UNKNOWN records the supported solute and mass/volume basis without claiming an explicitly omitted ingredient.',
 'carrier is not given, so PARTIAL remains.': 'carrier is not given and the stock ingredient list is not closed, so completeness is UNKNOWN.',
 'mark composition PARTIAL.': 'mark source-relative completeness UNKNOWN.',
 'bounded partial stock': 'bounded source stock',
}
def prose_fix(x):
    if isinstance(x, str):
        for before, after in replace_prose.items():
            x = x.replace(before, after)
        return x
    if isinstance(x, list):
        return [prose_fix(v) for v in x]
    if isinstance(x, dict):
        return {k: (v if k == 'curation_history' else prose_fix(v)) for k, v in x.items()}
    return x

# New factual assessment binds actual source bytes and original capture times.
facts = []
for i, (eid, fact) in SOURCE_FACTS.items():
    e = E[eid]
    facts.append({'proposal_id': P[i]['proposal_id'], 'case_ids': P[i]['case_ids'], 'source_evidence_id': eid,
                  'capture': e['capture'], 'url': e.get('url'), 'original_accessed_at': e.get('accessed_at'),
                  'locator': e.get('locator'), 'fact': fact,
                  'completeness': 'COMPLETE' if i in COMPLETE else 'UNKNOWN' if i in UNKNOWN else 'PARTIAL' if i == 21 else 'not_applicable'})
facts_cap = save('source-facts.json', {'author': '/root/inorganics', 'assessed_at': NOW, 'rows': facts,
    'scope': 'Source-relative constituent-list judgment. No molecular correction, final-volume inference or cross-source stock equivalence follows.'})

batch7 = R / 'research/inorganic_forms/captures/primary-batch7.json'
assert sha(batch7) == 'c985ded50be0a166b0a0822ccc269a11b78844194e84a5391cb11e5aa4a137eb'
batch_out = O / 'captures/primary-batch7-exact.json'
batch_out.parent.mkdir(parents=True, exist_ok=True)
assert not batch_out.exists()
shutil.copy2(batch7, batch_out)
thermo = {'evidence_id': 'if1227-thermo-full-batch7', 'kind': 'primary_source', 'capture': cap(batch_out),
  'url': 'https://www.thermofisher.com/order/catalog/product/040320.22',
  'accessed_at': '2026-11-08T05:08:47.015262+00:00',
  'locator': 'Thermo 040320.22 full captured section: lines 103–105, 147–154. Exact original batch7 bytes; this is not a new retrieval.',
  'supports_or_contradicts': 'Supplier product explicitly names sodium ammonium hydrogenphosphate tetrahydrate, CAS 7783-13-3, formula H13NNaO8P and mass 209.067. Supports exact supplied tetrahydrate identity. Earlier batch6 evidence remains historical but does not carry the full product identity fields.',
  'case_ids': P[5]['case_ids'], 'proposal_ids': [P[5]['proposal_id']]}

# Coordinator referral is not a new ingredient proposal or adoption of worker05 bytes.
w5a = json.loads(pathlib.Path('.temp/w05-published-head-independent-review-v1/assignments/chemicals_and_root.json').read_text())
w5p = next(p for p in w5a['proposals'] if p['proposal_id'] == 'CHEM-C1193-Tris-HCl-salt')
w5file = pathlib.Path(w5a['artifact_root']) / w5p['after_capture']['path']
assert sha(w5file) == w5p['after_capture']['sha256']
referral_cap = save('coordinator-referrals.json', {'referrals': [{
  'case_id': D[59]['case_id'], 'source_fact': D[59]['reasoning'], 'source_evidence_ids': D[59]['evidence_ids'],
  'candidate_worker': 'worker-05', 'head': w5a['head'], 'proposal_id': w5p['proposal_id'],
  'owner_path': w5p['owner_path'], 'before_sha256': w5p['before_sha256'], 'after_capture': w5p['after_capture'],
  'candidate_identifier': 'cas:1185-53-1', 'candidate_grounding': 'CHEBI:9754 BROAD_MATCH',
  'required_action': 'Coordinator must reconcile the exact W05 salt candidate and this source-specific W08 hydrochloride occurrence under current native identity rules and existing holds. Preserve independent W05 findings, including evidence-category concerns. This referral neither approves W05 nor imports its payload; no duplicate 36th owner is proposed.',
  'scientific_vs_integration': 'The hydrochloride versus free-base distinction is established by supplier evidence. Candidate selection, exact-term adjudication and duplicate reconciliation are integration dependencies, not an unperformed initial source-identity lookup.'}]})

evidence = [thermo]
def add_evidence(eid, capture, kind, locator, support, cases, url=None):
    evidence.append({'evidence_id': eid, 'kind': kind, 'capture': capture, 'url': url,
      'locator': locator, 'supports_or_contradicts': support, 'case_ids': sorted(set(cases))})
add_evidence('if1227-source-relative-completeness', facts_cap, 'local_validation', 'rows by proposal_id; exact primary capture bindings and original access times',
 'Five literal two-input lists are COMPLETE; fifteen concentration-defined input stocks leave source closure UNKNOWN; the PCR pH-adjustment omission remains PARTIAL. Input quantities, forms and source holds are unchanged.', [c for i in SOURCE_FACTS for c in P[i]['case_ids']])
add_evidence('if1227-component-compatibility', cap(O/'compatible-component-candidates.json'), 'local_validation', 'Ignored-inclusive current individual ingredient scan; exact identity/form candidates',
 'Compatible NaOH, nonahydrate, water and nested-stock refs already resolve to active records. Anhydrous phosphate or thiosulfate owners do not establish unspecified source hydration; literal seven-water phosphate and two-water dithionite remain unresolved.', A['case_ids'])
add_evidence('if1227-tris-coordinator-referral', referral_cap, 'local_validation', 'referrals[0]; exact worker05 head and selected payload SHA',
 'Established hydrochloride salt fact is separate from cross-shard candidate reconciliation. No W05 approval or import.', [D[59]['case_id']])
for name, eid, cases, support in [
 ('inputs/issue811-live-comments.json', 'if1227-phosphate-alias-scope', P[0]['case_ids'] + P[32]['case_ids'], 'Comment 6718614306 names KH2HPO4 and K2HPO on K2hpo4, and KH PO and Potassium Phosphate on Kh2po4. Retire unsupported exact/global identity resolution while preserving spelling and provenance.'),
 ('inputs/coordinator-triage/completeness-adjudication-refinement.json', 'if1227-completeness-refinement', A['case_ids'], 'Exact 34-row coordinator refinement, including five literal COMPLETE judgments and five exclusions, determines bounded action scope; native schema meaning was independently applied to actual sources.'),
]:
    add_evidence(eid, cap(S/name), 'local_validation', name, support, cases)

mapping_ledger = []
corrections = []
full_assessments = []
component_ledger = []
after_docs = []
for i, (p, old, before) in enumerate(zip(P, old_docs, before_docs)):
    new = copy.deepcopy(old)
    changes = []
    issues = []
    for j, ev in enumerate(old.get('ontology_mapping', {}).get('evidence', [])):
        inherited = before is not None and ev in before.get('ontology_mapping', {}).get('evidence', [])
        change = i in NEW_MAPPING and ev['evidence_type'] == 'MANUAL_CURATION'
        if change:
            assert not inherited
            new['ontology_mapping']['evidence'][j]['evidence_type'] = 'CURATOR_JUDGMENT'
            reason = ('The mixed-cation tetrahydrate and supplier CAS/formula are primary facts; selecting its distinct CAS identity and asymmetric CHEBI:37586 class parent is an LLM-assisted interpretation. No human-supplied mapping or exact ontology CAS cross-reference is evidenced.' if i == 5 else
                      SOURCE_FACTS[i][1] + ' Selecting this source-qualified local identity under sections 3/6 is LLM-assisted curator judgment, not a human-supplied mapping, literature identity assertion or direct ontology database match.')
            changes.append('Retype ontology_mapping.evidence[' + str(j) + '] from MANUAL_CURATION to CURATOR_JUDGMENT; preserve its exact source and substantive rationale.')
            issues.append('IR001')
        else:
            reason = ('Inherited assertion excluded from the new-authorship correction; preserved verbatim. Its retention is not a new claim that human review occurred.' if inherited else
                      'The selected evidence category is retained for this source-backed assertion; no new human-curation claim is introduced.')
        mapping_ledger.append({'proposal_id': p['proposal_id'], 'path': f'ontology_mapping.evidence[{j}]',
          'before': ev, 'after': new['ontology_mapping']['evidence'][j], 'inherited_from_frozen_owner': inherited,
          'action': 'retyped' if change else 'preserved', 'reason': reason})
    if i in COMPLETE | UNKNOWN:
        new = prose_fix(new)
        target = 'COMPLETE' if i in COMPLETE else 'UNKNOWN'
        assert new['component_assertion']['completeness'] == 'PARTIAL'
        new['component_assertion']['completeness'] = target
        note = SOURCE_FACTS[i][1] + (' Completeness describes the literal printed input list only; it does not approve a disputed chemical identity, a final volume or source membership transfer.' if i in COMPLETE else
              ' UNKNOWN denotes unstated source closure; no carrier is invented and no particular omitted ingredient is asserted.')
        new['notes'] = new.get('notes', '') + ' Issue 1227 source-relative completeness: ' + note
        for ev in new['component_assertion']['evidence']:
            ev['notes'] = ev.get('notes', '') + ' ' + note
        changes.append('Set component_assertion.completeness PARTIAL → ' + target + '. ' + note)
        issues.append('IR006')
    if i in {0, 32}:
        tokens = ['KH2HPO4', 'K2HPO'] if i == 0 else ['KH PO', 'Potassium Phosphate']
        for token in tokens:
            matches = [s for s in new['synonyms'] if s['synonym_text'] == token]
            assert len(matches) == 1 and matches[0]['synonym_type'] != 'REJECTED_LABEL'
            matches[0]['synonym_type'] = 'REJECTED_LABEL'
        why = ('KH2HPO4 is a malformed literal formula and K2HPO is a truncated formula; neither establishes global identity with dipotassium hydrogen phosphate.' if i == 0 else
               'KH PO is an incomplete formula and Potassium Phosphate is a generic family label; neither establishes exact monobasic KH2PO4 identity.')
        changes.append('Retype ' + ', '.join(tokens) + ' as REJECTED_LABEL, preserving original text and provenance. ' + why + ' Preserve prior hydrate, concentration-label and source holds; no source occurrence is chemically corrected.')
        issues.append('IR008')
        append_unique(p, 'evidence_ids', ['if1227-phosphate-alias-scope'])
    if i == 5:
        new['chemical_properties']['retrieval_date'] = thermo['accessed_at']
        changes.append('Bind CAS/formula supplier evidence to full Thermo batch7 capture at its original 2026-11-08T05:08:47.015262+00:00 access time; batch6 was incomplete. Preserve the proposed CAS identity and asymmetric parent predicate.')
        issues.append('IR010')
        append_unique(p, 'evidence_ids', [thermo['evidence_id']])
    if i in SOURCE_FACTS:
        append_unique(p, 'evidence_ids', ['if1227-source-relative-completeness'])
    if old.get('components'):
        append_unique(p, 'evidence_ids', ['if1227-component-compatibility', 'if1227-completeness-refinement'])
    if changes:
        record_curation_event(new, curator='worker-08 /root/inorganics issue-1227 author', action='CORRECTED_ASSERTION_SCOPE',
          changes=' '.join(changes) + ' All inherited history, scientific/source/role/export holds and original before hash remain preserved. This is a proposal, pending independent whole-payload review.',
          previous_status=old['mapping_status'], new_status=old['mapping_status'], llm_assisted=True, timestamp=NOW)
        out = O / 'proposed_owners' / pathlib.Path(p['owner_path']).name
        assert not out.exists()
        write_validated_ingredient(new, out)
        p['after_capture'] = cap(out)
    p = prose_fix(p)
    P[i] = p
    after_docs.append(new)
    corrections.append({'proposal_id': p['proposal_id'], 'case_ids': p['case_ids'], 'original_after_capture': A['proposals'][i]['after_capture'],
      'after_capture': p['after_capture'], 'before_sha256': p['before_sha256'], 'issue_ids': sorted(set(issues)),
      'changes': changes, 'status': 'corrected_proposal_pending_independent_review' if changes else 'retained_exact_selected_payload_pending_independent_review'})
    for j, c in enumerate(new.get('components', [])):
        unresolved = c.get('reference_scope') == 'UNMAPPED'
        if unresolved:
            reason = ({16:'KH2PO4 stock hydration is unspecified; pure anhydrous CHEBI:63036 is not established as the supplied form.',17:'K2HPO4 stock hydration is unspecified; neither anhydrous CHEBI:131527 nor trihydrate owners are a source-proven exact input.',18:'Na2HPO4 stock hydration is unspecified; the catalog has distinct anhydrous and hydrate owners.',19:'The nominal mass/molarity is not independent proof of NaH2PO4 hydration; retain literal source input.',20:'The nominal mass/molarity is not independent proof of Na2HPO4 hydration; retain literal source input.',22:'Literal K2HPO4·7H2O remains chemically unresolved; anhydrous and trihydrate records cannot establish that identity.',30:'MediaDive 552 has conflicting automated chemical metadata, including a wrong unrelated ChEBI target; source stock label does not establish anhydrous or pentahydrate material.',31:'Literal Na2S2O4·2H2O is not the catalog anhydrous sodium dithionite or dithionite anion.'}.get(i))
            assert reason
        else:
            reason = 'Already references the active form-compatible input owner. The reference denotes the stated component only; all independent owner/source holds remain.'
        component_ledger.append({'proposal_id': p['proposal_id'], 'component_index': j, 'component': c,
          'action': 'retained_unresolved_source_form' if unresolved else 'retained_active_catalog_reference', 'reason': reason})
    full_assessments.append({'proposal_id': p['proposal_id'], 'before_sha256': p['before_sha256'],
      'input_after_sha256': A['proposals'][i]['after_capture']['sha256'], 'selected_after_sha256': p['after_capture']['sha256'],
      'whole_payload_read': True, 'full_history_read': True,
      'identity_and_scope': p['description'], 'source_evidence_ids': p['evidence_ids'],
      'component_assessment': SOURCE_FACTS[i][1] if i in SOURCE_FACTS else 'No partonomy assertion on this chemical owner. Existing identity, form, predicate, chemistry, all aliases and full history were reviewed within the assigned correction scope.',
      'correction': changes, 'boundary': 'Author reassessment, not independent approval. No role, membership, SSSOM or publication hold is lifted; retained fields are not globally reapproved.'})

for i, d in enumerate(D):
    for k in ['reasoning', 'applicability', 'no_change_reason', 'missing_requirement']:
        d[k] = prose_fix(d.get(k))
    related = [j for j, p in enumerate(P) if d['case_id'] in p['case_ids']]
    for j in related:
        append_unique(d, 'evidence_ids', [eid for eid in P[j]['evidence_ids'] if eid.startswith('if1227-')])
        if j in COMPLETE | UNKNOWN:
            d['reasoning'] += ' Issue 1227 completeness refinement: ' + P[j]['proposal_id'] + ' is ' + after_docs[j]['component_assertion']['completeness'] + ' relative to its cited source input list. This does not change the case-specific source-form or comparison restrictions.'
    if i == 29:
        d['missing_requirement'] = 'Primary M2231 already resolves the 6 g/L stock label and the 5 ml receiving dose. The remaining scientific requirement is independent material or source-correction evidence establishing whether the literal K2HPO4·7H2O input is correct; do not infer another hydrate from the known stock recipe.'
        append_unique(d, 'issue_refs', ['https://github.com/CultureBotAI/MediaIngredientMech/issues/1227'])
    if i == 59:
        d['missing_requirement'] = 'The hydrochloride salt distinction is established. Coordinator reconciliation of the exact W05 CHEM-C1193-Tris-HCl-salt candidate (head 43f7cf6e8681fa617b5d6d3529d94d537ca01f0d; after SHA 945bd8da0c00306c5e0d9ad2c3eaead1fb3af33e89cdc2e3440e729ec5763c58) remains an integration dependency under current ontology rules and existing holds. Do not create a duplicate owner or treat reconciliation as missing source chemistry.'
        append_unique(d, 'evidence_ids', ['if1227-tris-coordinator-referral'])
    if i in [33, 50, 73]:
        append_unique(d, 'evidence_ids', [thermo['evidence_id']])
        append_unique(d, 'issue_refs', ['https://github.com/CultureBotAI/MediaIngredientMech/issues/1210'])
    if any(j in {0,32} for j in related):
        d['reasoning'] += ' The separate issue 811 successor also rejects the two named unsupported formula/family aliases on this owner while retaining prior source and stock-label repairs.'
        append_unique(d, 'issue_refs', ['https://github.com/CultureBotAI/MediaIngredientMech/issues/811'])
    # Leave historical reviewer identity/status in a separate exact field; no self-review claim.
    d['prior_independent_review'] = copy.deepcopy(d['independent_review'])
    d['independent_review'] = {'status': 'pending', 'evidence_ids': []}

map_cap = save('evidence-category-ledger.json', {'schema_enum': 'MappingEvidence.evidence_type / EvidenceTypeEnum',
  'excluded_enum': 'ComponentAssertion.evidence[].evidence_type / ComponentEvidenceTypeEnum; preserved verbatim types', 'rows': mapping_ledger})
add_evidence('if1227-evidence-category-ledger', map_cap, 'local_validation', 'Every mapping assertion on all 35 selected payloads',
 'Per-assertion provenance distinguishes new LLM-assisted CURATOR_JUDGMENT decisions from inherited assertions and the separate component-evidence enum. No blanket MANUAL_CURATION transformation occurred.', A['case_ids'])
for p in P:
    append_unique(p, 'evidence_ids', ['if1227-evidence-category-ledger'])
for d in D:
    append_unique(d, 'evidence_ids', ['if1227-evidence-category-ledger'])

save('component-reference-ledger.json', {'rows': component_ledger, 'compatible_catalog_capture': cap(O/'compatible-component-candidates.json'),
  'scope': 'All component slots in all 35 selected payloads. Active compatible references were already present. No unrelated candidate, hypothetical hydrate or downstream source mapping was substituted.'})
save('correction-ledger.json', {'author': '/root/inorganics', 'timestamp': NOW, 'rows': corrections})
save('full-payload-assessment.json', {'author': '/root/inorganics', 'independent_approval': False, 'rows': full_assessments})
save('case-assessment.json', {'author': '/root/inorganics', 'independent_approval': False, 'rows': [
 {'case_id': d['case_id'], 'source': d['source'], 'case_input_sha256': d['case_input_sha256'],
  'before_decision_sha256': objsha(old), 'after_decision_sha256': objsha(d), 'source_evidence_ids': d['evidence_ids'],
  'disposition': d['disposition'], 'individual_assessment': d['reasoning'], 'remaining_requirement': d['missing_requirement'],
  'occurrence_ids': d['occurrence_ids'], 'source_read_scope': 'Active complete source outcome and all frozen occurrence contexts reread in this correction. Primary sources used for changed assertions reread with exact captures in source-facts/inspection ledger. Earlier full primary and independent receipts remain historical, not renewed approval.'}
 for d,old in zip(D,A['decisions'])]})
save('decisions.json', D)
save('proposals.json', P)
save('evidence-additions.json', evidence)

# Mechanical validation does not constitute scientific peer approval.
checks = []
def check(label, condition):
    checks.append({'check':label,'passed':bool(condition)})
    assert condition, label
check('exact 80 case IDs', [d['case_id'] for d in D] == A['case_ids'])
check('exact 35 proposal IDs', [p['proposal_id'] for p in P] == A['proposal_ids'])
for d,old in zip(D,A['decisions']):
    for key in ['source','case_input_sha256','occurrence_ids','occurrence_context','preserved_native_decisions','preserved_holds','disposition']:
        check(d['case_id']+' preserve '+key,d.get(key)==old.get(key))
for i,(p,old,new) in enumerate(zip(P,old_docs,after_docs)):
    for key in ['proposal_id','kind','owner_path','before_sha256','case_ids']:
        check(p['proposal_id']+' preserve '+key,p[key]==A['proposals'][i][key])
    check(p['proposal_id']+' after hash',sha(R/p['after_capture']['path'])==p['after_capture']['sha256'])
    check(p['proposal_id']+' strict schema',not validate_ingredient(new))
    check(p['proposal_id']+' components exact',new.get('components')==old.get('components'))
    check(p['proposal_id']+' original history exact prefix',new.get('curation_history',[])[:len(old.get('curation_history',[]))]==old.get('curation_history',[]))
    check(p['proposal_id']+' component evidence types preserved',[x['evidence_type'] for x in new.get('component_assertion',{}).get('evidence',[])]==[x['evidence_type'] for x in old.get('component_assertion',{}).get('evidence',[])])
    check(p['proposal_id']+' primary mapping unchanged',all(new.get('ontology_mapping',{}).get(k)==old.get('ontology_mapping',{}).get(k) for k in ['ontology_id','ontology_label','ontology_source','mapping_quality']))
    for field in ['identifier','preferred_term','mapping_status','occurrence_statistics','nutritional_roles','physicochemical_roles','biological_roles']:
        check(p['proposal_id']+' preserve '+field,new.get(field)==old.get(field))
for e in evidence:
    check(e['evidence_id']+' capture hash',sha(R/e['capture']['path'])==e['capture']['sha256'])
check('23 new mapping assertions retyped individually',sum(x['action']=='retyped' for x in mapping_ledger)==23)
check('five literal COMPLETE',sum(x.get('component_assertion',{}).get('completeness')=='COMPLETE' for x in after_docs)==5)
check('fifteen UNKNOWN',sum(x.get('component_assertion',{}).get('completeness')=='UNKNOWN' for x in after_docs)==15)
check('one preserved PARTIAL',sum(x.get('component_assertion',{}).get('completeness')=='PARTIAL' for x in after_docs)==1)
check('all three Thermo case backlinks',all(thermo['evidence_id'] in next(d for d in D if d['case_id']==c)['evidence_ids'] for c in P[5]['case_ids']))
overlay = {str(p): yaml.safe_load(p.read_text()) for p in pathlib.Path('data/ingredients').rglob('*.yaml')}
active = json.loads((R/'successors/issue-1201-v1/proposals.json').read_text())
active = active['proposals'] if isinstance(active,dict) else active
for p in active:
    overlay[p['owner_path']] = yaml.safe_load((R/p['after_capture']['path']).read_text())
for p,doc in zip(P,after_docs):
    overlay[p['owner_path']] = doc
violations = validate_component_partonomy(overlay.values())
check('full catalog plus active113 with own35 replacements partonomy',not violations)
save('validation.json', {'timestamp':NOW,'checks':checks,'passed':all(x['passed'] for x in checks),
 'counts':{'cases':len(D),'proposals':len(P),'changed_payloads':sum(bool(x['changes']) for x in corrections),'unchanged_payloads':sum(not x['changes'] for x in corrections),'mapping_assertions':len(mapping_ledger),'component_slots':len(component_ledger),'overlay_records':len(overlay)},
 'partonomy_violations':[str(x) for x in violations], 'not_run':'No maintained corpus changes, synchronization, SSSOM generation, downstream build or release gate. Independent scientific review pending.'})
print(json.dumps({'passed':True,'cases':len(D),'proposals':len(P),'changed_payloads':sum(bool(x['changes']) for x in corrections),'checks':len(checks)}))
