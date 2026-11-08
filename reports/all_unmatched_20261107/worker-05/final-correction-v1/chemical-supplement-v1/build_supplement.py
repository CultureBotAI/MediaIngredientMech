from pathlib import Path
from datetime import datetime, timezone
import copy, difflib, hashlib, json, sys, yaml

sys.path.insert(0, str(Path('src').resolve()))
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.write_validated import write_validated_ingredient

O = Path(__file__).resolve().parent
S = O.parent
R = Path('reports/all_unmatched_20261107/worker-05').resolve()
C = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
Q = C / 'queue/preliminary-v5'
NOW = datetime.now(timezone.utc).isoformat()
AUTHOR = '/root/chemicals_research'
PREFIX = 'final-correction-v1/chemical-supplement-v1/'
PID = 'FINAL-CHEM-P-thiamine-hcl-monohydrate'
OWNER = 'data/ingredients/mapped/Thiamine_Hcl_Monohydrate.yaml'
ID = 'kgmicrobe.compound:thiamine_hcl_monohydrate'
INPUTS = {
    'decisions': S/'remediation/chemical-report-v2/decisions-v3.json',
    'proposals': S/'chemicals/proposals-v3.json',
    'evidence': S/'remediation/chemical-report-v1/evidence-v2.json',
    'conclusions': S/'remediation/chemical-report-v3/primary-case-conclusions-v3.json',
    'finding': S/'review-chemicals/finding-003-initial.json',
    'independent_source_crosscheck': S/'review-chemicals/source-crosscheck/review-v1.json',
}

def sha(b): return hashlib.sha256(b).hexdigest()
def objsha(x): return sha(json.dumps(x, sort_keys=True, ensure_ascii=False).encode())
def dump(name, value):
    p = O/name
    assert not p.exists(), p
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')
    return p
def ref(p): return {'root': 'artifact', 'path': PREFIX+str(p.relative_to(O)), 'sha256': sha(p.read_bytes())}
def local_binding(p): return {'path': str(p), 'sha256': sha(p.read_bytes())}
def read(name): return json.loads(INPUTS[name].read_text())

D0, P0, E0, K0 = (read(x) for x in ['decisions', 'proposals', 'evidence', 'conclusions'])
assert (len(D0), len(P0), len(E0), len(K0['case_reviews'])) == (67, 57, 525, 67)
D, P, E, K = copy.deepcopy(D0), copy.deepcopy(P0), copy.deepcopy(E0), copy.deepcopy(K0)
chosen = [D[i] for i in [10, 48]]
CASE_IDS = [d['case_id'] for d in chosen]
OCC_IDS = [x for d in chosen for x in d['occurrence_ids']]
assert len(OCC_IDS) == len(set(OCC_IDS)) == 6
ei = {e['evidence_id']: e for e in E}
sources = [(1550, 'CHEM-CAP-f0c1b4928af89872', '**'),
           (1443, 'CHEM-CAP-1fc151e426d45042', '***'),
           (1444, 'CHEM-CAP-aa10057ea2c6f012', '***'),
           (1445, 'CHEM-CAP-f55e3a4d1efb7d51', '***'),
           (1447, 'CHEM-CAP-77de000b5fa8d1a6', '***'),
           (1507, 'CHEM-CAP-74b89743eed1808f', '****')]
source_eids = [e for _, e, _ in sources]
urls = [ei[e]['url'] for e in source_eids]
frozen = json.loads((Q/'shards/shard-05.json').read_text())['cases']
selected_raw = [next(c for c in frozen if c['case_id'] == cid) for cid in CASE_IDS]
raw_occ = [o for c in selected_raw for o in c['occurrences']]
assert [o['occurrence_id'] for o in raw_occ] == OCC_IDS
read_rows = []
for (number, eid, star), occurrence in zip(sources, raw_occ):
    e = ei[eid]
    primary = R/e['capture']['path']
    assert sha(primary.read_bytes()) == e['capture']['sha256']
    recipe = Q/occurrence['full_recipe_snapshot']
    assert sha(recipe.read_bytes()) == occurrence['source_file_sha256']
    text = S/'chemicals/read-text'/f'{eid}.txt'
    assert text.exists()
    read_rows.append({
        'occurrence': occurrence,
        'primary_evidence_id': eid,
        'primary_capture': e['capture'],
        'source_url': e['url'], 'original_accessed_at': e['accessed_at'],
        'read_at': NOW, 'read_scope': 'Complete NBRC ingredient tables and preparation instructions; complete corresponding frozen recipe snapshot. Existing captured bytes are reused without changing their access time or authorship.',
        'read_text': local_binding(text),
        'frozen_full_recipe': {'root': 'source', 'path': occurrence['full_recipe_snapshot'], 'sha256': occurrence['source_file_sha256']},
        'locator': f'NBRC {number}; {star}Vitamin solution, Thiamine-HCl one-water row, 5 mg; distilled water row, 1 L; adjustment to pH 7.0 with NaOH.',
        'applicability': 'The explicit one-water reagent name supports the same bounded local material. The 5 mg amount is an input to this multivitamin preparation. It is not the neat material concentration or a single-solute stock specification.',
        'receiving_stage': ('The main medium lists 10 ml of the vitamin preparation.' if number != 1507 else 'The main medium receives 50 ml Solution 2; Solution 2 contains 10 ml of this vitamin preparation and 40 ml water plus other inputs.'),
        'unasserted_facts': ['CAS', 'molecular formula', 'molecular structure', 'chloride/protonation stoichiometry', 'reagent supplier', 'supplier catalog number', 'historical lot equivalence'],
        'frozen_normalization_boundary': 'The frozen flattened concentration is retained verbatim as source context, not adopted as a measured or converted concentration of this material. No CultureMech source correction or export hold is released.',
    })

gap = ('Exact CAS, molecular formula, molecular structure, chloride/protonation stoichiometry and supplier catalog identity remain unverified. These facts constrain exact molecular grounding and a specific parent relationship, not the positive source-defined one-water material representation.')
scope = ('One local material denotes the Thiamine-HCl monohydrate explicitly named by NBRC 1550, 1443, 1444, 1445, 1447 and 1507. The six positive source names support a shared bounded reagent identity, without separate owners for medium numbers. NBRC is the recipe authority, not a claimed reagent supplier. This does not identify historical reagent lots or erase the hydration qualifier.')
note = (scope+' '+gap+' The exact raw source forms are retained as sourced RAW_TEXT synonyms. Each recipe lists 5 mg in a multivitamin preparation whose water input is 1 L; those preparation quantities, its pH adjustment and receiving doses do not become properties or components of this single ingredient. No chemical_properties, supplied supplier/catalog, roles or material partonomy are inferred. CHEBI:49105 and CHEBI:132751 are comparison terms, not exact identities or asserted parents for this record. Registry-only grounding records the bounded local form while the specific molecular parent remains unresolved. All frozen source, owner, observation and export holds remain; this isolated proposal does not install an owner or authorize downstream publication.')
record = {
    'identifier': ID,
    'preferred_term': 'Thiamine-HCl monohydrate',
    'ontology_mapping': {
        'ontology_id': ID,
        'ontology_label': 'Thiamine-HCl monohydrate',
        'ontology_source': 'kgmicrobe.compound',
        'mapping_quality': 'FALLBACK_REGISTRY',
        'evidence': [{'evidence_type': 'LLM_SUGGESTION', 'source': url,
                      'notes': f'Primary NBRC {number} recipe explicitly names the one-water Thiamine-HCl material as a 5 mg input to its vitamin preparation. The local identity retains this source-defined form. Neither supplier identity nor CAS, molecular structure, chloride/protonation stoichiometry or parent relation is established. Scientific assessment by Codex /root/chemicals_research; NBRC authorship applies to the source recipe, not this mapping decision.'}
                     for (number, _, _), url in zip(sources, urls)],
    },
    'synonyms': [
        {'synonym_text': D[10]['source']['raw_source_label'], 'synonym_type': 'RAW_TEXT', 'source': '; '.join(urls[:5])},
        {'synonym_text': D[48]['source']['raw_source_label'], 'synonym_type': 'RAW_TEXT', 'source': urls[5]},
    ],
    'mapping_status': 'MAPPED',
    'ingredient_type': 'SINGLE_INGREDIENT',
    'occurrence_statistics': {'total_occurrences': 6, 'media_count': 6},
    'notes': note+' Occurrence statistics are limited to the six assigned frozen occurrences in six distinct recipes; no global source count is claimed.',
}
record_curation_event(record, curator='Codex '+AUTHOR+' bounded chemical supplement',
    action='CREATED_SOURCE_DEFINED_FORM', changes='Report-only correction of W05-FINAL-SKEPTIC-CHEM-003 after its pre-fix referral. '+scope+' '+gap+' Preserved both exact raw source spellings and all six occurrence links in the proposal ledger. Prior no-change decisions remain immutable historical artifacts. No maintained record was edited.',
    new_status='MAPPED', llm_assisted=True, llm_model='gpt-6', timestamp=NOW)
dst = O/'proposed-v1/Thiamine_Hcl_Monohydrate.yaml'
assert not dst.exists() and not Path(OWNER).exists()
write_validated_ingredient(record, dst, target_class='IngredientRecord')
assert yaml.safe_load(dst.read_text()) == record

semantic = {
    'author': AUTHOR, 'at': NOW, 'finding_id': 'W05-FINAL-SKEPTIC-CHEM-003',
    'scope': scope, 'molecular_grounding_limit': gap,
    'case_ids': CASE_IDS, 'occurrence_ids': OCC_IDS,
    'raw_cases': selected_raw,
    'source_case_input_hashes': {d['case_id']: d['case_input_sha256'] for d in chosen},
    'shard': local_binding(Q/'shards/shard-05.json'),
    'source_reads': read_rows,
    'ontology_comparisons': [{**ei[x], 'current_applicability': ('CHEBI:49105 explicitly defines thiamine hydrochloride with one equivalent hydrochloric acid and no source monohydrate assertion.' if x.endswith('14f6b2b7770adbee') else 'CHEBI:132751 explicitly defines thiamine hydrochloride dihydrate; the source material is named with one water.')} for x in ['CHEM-CAP-14f6b2b7770adbee','CHEM-CAP-ba668efabffad3e5']],
    'actual_prior_ontology_searches_reused': [{**ei[x], 'current_interpretation': 'The captured API response contains no matching term. This is bounded search evidence, not proof of universal ontology absence or the source molecular identity.'} for x in ['CHEM-CAP-12d6346a73c5dd24','CHEM-C1193-ols-search-3','CHEM-C1193-ols2-thiamine']],
    'new_discovery_capture': ref(O/'new-primary-discovery-v1.json'),
    'new_discovery_result': 'No exact source-specific monohydrate CAS, structure or supplier match was established. Generic PubChem thiamine records, historical descriptions and patent search results do not identify these NBRC reagents; no chemical field is transferred.',
    'owner_check': ref(O/'owner-and-intake-check-v1.json'),
    'owner_result': 'The complete ten thiamine-related maintained records have cation, hydrochloride, dihydrate, phosphate, generic Vitamin B or stock scopes; none establishes this source-defined one-water material. All 981 frozen selected payloads were parsed and hash-checked, and the 37 coordinator candidate summary was searched recursively. No same-form owner was found. The worktree owner-label search included ignored files. This is a bounded inventory check, not a claim about future unpublished drafts.',
    'cross_shard_dependency': 'No current selected same-form owner or monohydrate component dependency was found in the frozen 981 intake. Coordinator must reconcile any later same-form proposal against this single candidate rather than install parallel owners; no other worker payload is changed.',
    'whole_material_vs_parts': 'The named one-water form is the local material identity. Neither water nor a thiamine moiety is represented as a material component: MAPPING_SEMANTICS section 6 excludes hydrate/form relationships from material partonomy.',
    'scope_exclusions': ['No historical lot equivalence', 'No new role annotation', 'No formula/CAS or exact parent grounding', 'No stock concentration conversion', 'No source/export hold release'],
}
semantic_path = dump('primary-assessment-and-read-ledger-v1.json', semantic)
new_evidence = [
    {'evidence_id': 'FINAL-CHEM-SUPPLEMENT-OWNER-CHECK', 'kind': 'source_snapshot', 'capture': ref(O/'owner-and-intake-check-v1.json'), 'locator': 'Complete maintained thiamine owner records, frozen 981 payloads and 37 coordinator candidate summary; ignored-inclusive worktree owner-label search.', 'supports_or_contradicts': semantic['owner_result'], 'case_ids': CASE_IDS, 'accessed_at': NOW},
    {'evidence_id': 'FINAL-CHEM-SUPPLEMENT-PRIMARY-READ', 'kind': 'source_snapshot', 'capture': ref(semantic_path), 'locator': 'source_reads and raw_cases: six complete NBRC recipe contexts and exact original occurrence/source hashes; ontology_comparisons and bounded searches.', 'supports_or_contradicts': scope+' '+gap, 'case_ids': CASE_IDS, 'accessed_at': NOW},
    {'evidence_id': 'FINAL-CHEM-SUPPLEMENT-DISCOVERY', 'kind': 'unsuccessful_search', 'capture': ref(O/'new-primary-discovery-v1.json'), 'locator': 'Two actual domain-filtered primary-source web queries recorded with search result bytes and timestamp.', 'supports_or_contradicts': semantic['new_discovery_result'], 'case_ids': CASE_IDS, 'accessed_at': json.loads((O/'new-primary-discovery-v1.json').read_text()).get('accessed_at', NOW)},
]
E.extend(new_evidence)
new_eids = [e['evidence_id'] for e in new_evidence]
proposal = {
    'proposal_id': PID, 'case_ids': CASE_IDS, 'description': scope+' '+gap,
    'evidence_ids': source_eids+['CHEM-CAP-14f6b2b7770adbee','CHEM-CAP-ba668efabffad3e5','CHEM-CAP-12d6346a73c5dd24','CHEM-C1193-ols-search-3','CHEM-C1193-ols2-thiamine']+new_eids,
    'owner_path': OWNER, 'kind': 'new_owner', 'before_sha256': None,
    'after_capture': ref(dst), 'applies_to_occurrence_ids': OCC_IDS,
    'identity_consequence': 'One local source-defined Thiamine-HCl monohydrate material for the six explicit one-water occurrences; no source-number split.',
    'predicate_consequence': 'Registry identity only. No exact CHEBI:49105 or CHEBI:132751 identity or parent relation is inferred. A specific molecular parent remains a separate unresolved grounding task.',
    'publication_obligations': 'Preserve all source/owner/observation/export holds. Coordinator performs complete integrated native review, checks future same-form owner overlap and synchronizes only after integration authorization. This private candidate is not installed.',
    'replaces_proposal_ids': [],
    'occurrence_application_note': 'All six exact occurrence IDs listed here name the same one-water reagent. The five middle-dot spellings and one dot-operator spelling are retained. The 5 mg source quantity belongs to each nested vitamin stock and is not adopted as neat reagent concentration.',
    'final_correction': {'author': AUTHOR, 'timestamp': NOW, 'finding_id': 'W05-FINAL-SKEPTIC-CHEM-003', 'native_guarded_write': 'PASS', 'independent_review': 'pending', 'changes': ['Create one bounded local source-defined monohydrate material after actual same-form owner checks. No predecessor owner or existing payload is overwritten.']},
}
P.append(proposal)
for i in [10, 48]:
    d, old = D[i], D0[i]
    d['disposition'] = 'curation_proposal'
    d['reasoning'] = scope+' '+gap+' The exact source-form evidence supports feasible local curation under section 3. Lack of CAS or molecular structure does not justify retaining a no-change disposition for this bounded material.'
    d['applicability'] = ('The five NBRC 1550/1443/1444/1445/1447 frozen occurrences' if i == 10 else 'The NBRC 1507 frozen occurrence')+' explicitly name a one-water Thiamine-HCl reagent. Preserve the original literal, occurrence IDs and frozen flattened quantities as source context. Each primary recipe lists 5 mg within its vitamin preparation; this is not a single-solute stock or a claim that the frozen g/L normalization is correct. One shared local material candidate serves both source spelling cases.'
    d['proposal_ids'] = [PID]
    d['no_change_reason'] = None
    d['missing_requirement'] = None
    d['remaining_grounding_uncertainty'] = gap
    d['evidence_ids'] += [x for x in new_eids if x not in d['evidence_ids']]
    d['prior_correction_reassessment'] = copy.deepcopy(old['correction_reassessment'])
    d['correction_reassessment'] = {'status': 'complete', 'trigger': 'W05-FINAL-SKEPTIC-CHEM-003: source-defined local material identity is feasible despite incomplete molecular grounding.', 'reviewed_at': NOW, 'primary_author': AUTHOR, 'prior_proposal_ids': old['proposal_ids'], 'outcome': 'one shared bounded local monohydrate material proposed', 'scientific_gap': gap, 'search_evidence_ids': old['correction_reassessment']['search_evidence_ids']+new_eids, 'prior_case_sha256': objsha(old), 'preserved_holds': 'Original preserved_source_holds, case_input_sha256 and occurrence_ids are unchanged.', 'performed_searches': old['correction_reassessment']['performed_searches']+[{'evidence_id': e['evidence_id'], 'finding': e['supports_or_contradicts']} for e in new_evidence]}
    d['prior_final_correction_review'] = copy.deepcopy(old['final_correction_review'])
    d['final_correction_review'] = {'author': AUTHOR, 'timestamp': NOW, 'prior_decision_sha256': objsha(old), 'scope': 'Bounded supplement for the complete two source cases and one new local material candidate. Original source and hold objects are unchanged; prior other-case review remains unchanged.', 'proposal_ids': [PID], 'conditional_proposal_ids': [], 'whole_owner_approval': False, 'finding_id': 'W05-FINAL-SKEPTIC-CHEM-003'}
    d['native_review_applicability'] = 'Coordinator native review must include the new local material candidate, its six exact occurrence routes and this bounded molecular-grounding limit. Existing thiamine owners are comparison records, not proposed mutations.'
    d['independent_review'] = {'status': 'pending', 'evidence_ids': []}
    k = K['case_reviews'][i]
    assert k['case_id'] == d['case_id']
    k['assessment'] = d['reasoning']+' '+d['applicability']
    k['decision_object_sha256'] = objsha(d)
    k['evidence_ids'] = d['evidence_ids']
    k['payloads'] = [{'proposal_id': PID, 'after_capture': ref(dst)}]
    k['supplement_author'] = AUTHOR
    k['supplement_at'] = NOW
K['candidate_count'] = len(P)
K['supplement'] = {'author': AUTHOR, 'at': NOW, 'predecessor': local_binding(INPUTS['conclusions']), 'changed_lane_indices': [10,48], 'preserved_all_other_case_reviews': True, 'preserved_root_corrected_bottom_layer_and_mkp_conclusions': True}

for n, x in [('decisions-v1.json',D),('proposals-v1.json',P),('evidence-v1.json',E),('primary-case-conclusions-v1.json',K)]: dump(n,x)
lineage = {'author': AUTHOR, 'at': NOW, 'finding': local_binding(INPUTS['finding']), 'reported_before_fix': True, 'inputs': {k: local_binding(v) for k,v in INPUTS.items()}, 'new_proposal_id': PID, 'new_owner_has_no_predecessor': True, 'unchanged_prior_proposal_count': len(P0), 'unchanged_prior_evidence_count': len(E0), 'changed_decisions': [], 'new_payload': ref(dst), 'new_payload_guarded_write': 'PASS', 'new_payload_parsed_roundtrip_equal': True, 'no_maintained_or_git_mutation': True}
for i in [10,48]:
    lineage['changed_decisions'].append({'lane_index': i, 'case_id': D[i]['case_id'], 'before_object_sha256': objsha(D0[i]), 'after_object_sha256': objsha(D[i]), 'unchanged_case_input_sha256': D[i]['case_input_sha256'], 'unchanged_occurrence_ids': D[i]['occurrence_ids'], 'unchanged_source_holds_sha256': objsha(D[i]['preserved_source_holds'])})
for key,newname in [('decisions','decisions-v1.json'),('proposals','proposals-v1.json'),('evidence','evidence-v1.json'),('conclusions','primary-case-conclusions-v1.json')]:
    diff = ''.join(difflib.unified_diff(INPUTS[key].read_text().splitlines(True),(O/newname).read_text().splitlines(True),fromfile=str(INPUTS[key]),tofile=str(O/newname)))
    p = O/'diffs-v1'/f'{key}.diff'; p.parent.mkdir(exist_ok=True); assert not p.exists(); p.write_text(diff)
lineage['diffs'] = [ref(p) for p in sorted((O/'diffs-v1').glob('*.diff'))]
dump('ancestry-and-remediation-v1.json', lineage)
print(json.dumps({'counts': [len(D),len(P),len(E)], 'new_payload': ref(dst), 'core_hashes': {n: sha((O/n).read_bytes()) for n in ['decisions-v1.json','proposals-v1.json','evidence-v1.json','primary-case-conclusions-v1.json']}}))
