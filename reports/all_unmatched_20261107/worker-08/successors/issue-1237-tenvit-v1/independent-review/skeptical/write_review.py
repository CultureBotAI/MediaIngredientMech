"""Read-only checks and an independently authored, bounded scientific receipt."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import yaml

W = Path.cwd()
C = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
P = C / 'preflight/tenvit-final-application-route-v1'
A = W / 'reports/all_unmatched_20261107/worker-08'
S = A / 'successors/issue-1237-tenvit-v1'
O = W / '.temp/all-unmatched-worker-08/tenvit-dependent-v1/independent-skeptical'
D9 = C / 'workers/w09/worktree/.temp/tenvit-continuity-resolution-v1'
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def canonical(o):
    return hashlib.sha256(json.dumps(o, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode()).hexdigest()

def js(p):
    return json.loads(Path(p).read_text())

def ref(p):
    p = Path(p).resolve()
    if p.is_relative_to(A):
        return {'root': 'artifact', 'path': str(p.relative_to(A)), 'sha256': sha(p)}
    return {'path': str(p), 'sha256': sha(p)}

def write(name, obj):
    p = O / name
    assert not p.exists(), f'Preserve previous receipt: {p}'
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False, allow_nan=False) + '\n')
    return ref(p)

checks = []
def ck(name, condition, detail=None):
    row = {'check': name, 'pass': bool(condition)}
    if detail is not None:
        row['detail'] = detail
    checks.append(row)
    assert condition, name

before_path = S / 'beforeimages/Wolfes_Vitamin_Mix.yaml'
w09_path = S / 'inputs/coordinator-route/captures/candidate-fe607027.yaml'
payload_path = S / 'payloads/Wolfes_Vitamin_Mix.yaml'
before = yaml.safe_load(before_path.read_text())
w09 = yaml.safe_load(w09_path.read_text())
payload = yaml.safe_load(payload_path.read_text())
proposal = js(S / 'author/proposal.json')
decision = js(S / 'author/decision.json')
assessment = js(S / 'author/assessment.json')
bindings = js(S / 'author/child-bindings.json')
dependency = js(S / 'author/dependency-dispositions.json')
preflight = js(O / 'preflight-review.json')
nominal = js(S / 'research/nominal-recipe-evidence.json')
partitions = js(S / 'research/occurrence-partitions.json')
old_decisions = js(A / 'successors/issue-1227-plain-flour-v1/decisions.json')['decisions']
old = next(x for x in old_decisions if x['case_id'] == decision['case_id'])
old_proposals = js(A / 'successors/issue-1227-plain-flour-v1/proposals.json')['proposals']
old_nbrc = next(x for x in old_proposals if x['proposal_id'] == 'vm1201-prop-nbrc903-vitamin')
cid = decision['case_id']
pid = proposal['proposal_id']
trigger = 'CM_OCC:a181b24b7eb91c50c771bd1c1fc3012fd0cf28f45b49f2750c3d43bda9cdd531'

for name, path, expected in [
    ('authentic beforeimage', before_path, '709749bd7c83c38a09400fc1893885ead753847ff9d1cbbe4ec76b431d349738'),
    ('W09 exact candidate', w09_path, 'fe6070272f269fde7683696e4c46a331902ab88baac8c5cc93db7bddf9d0ec1b'),
    ('final author payload', payload_path, 'b64eccf46c271520c27c73bc0a5863e2bc56447d1acf7461a90e3d72f9f4384f'),
    ('final author proposal', S / 'author/proposal.json', '73e8fdf31d13a2891482f2ec3ab3b51910a9f902cceea8adef30008071550cb7'),
    ('final author decision', S / 'author/decision.json', 'f1475252112e3608db55f9e441b9d93248c1e73701bf0dbf9ecf32ea5b0d4d29'),
]:
    ck(name, sha(path) == expected)

ck('entire original five-event history prefix', payload['curation_history'][:5] == before['curation_history'])
ck('entire W09 six-event history prefix', payload['curation_history'][:6] == w09['curation_history'])
ck('exact W09 authorship and event retained', payload['curation_history'][5] == assessment['W09_event_preserved'])
ck('one real W08 event appended', len(payload['curation_history']) == 7 and payload['curation_history'][6] == assessment['W08_event'])
ck('W08 event is distinct, truthfully LLM assisted', payload['curation_history'][6]['curator'].startswith('worker08:/root ') and payload['curation_history'][6]['llm_assisted'] is True)
ck('unchanged top-level field inventory', set(payload) == set(before))
allowed_fields = {'curation_history', 'notes', 'components', 'component_assertion'}
ck('only four authorized top-level fields changed', {k for k in before if before[k] != payload[k]} == allowed_fields)
for key in sorted(set(before) - allowed_fields):
    ck('unchanged full field: ' + key, payload[key] == before[key])
ck('historical counts not recomputed', payload['occurrence_statistics'] == {'total_occurrences': 61, 'media_count': 61})
ck('ten CB parts only', len(payload['components']) == len(w09['components']) == 10)
expected_ids = ['CHEBI:30961', 'CHEBI:30753', 'CHEBI:16494', 'CHEBI:15940', 'CHEBI:17015', 'CHEBI:49105', None, 'CHEBI:15956', 'CHEBI:27470', 'CHEBI:17439']
for i, (part, precursor, child) in enumerate(zip(payload['components'], w09['components'], bindings['owner_checks'], strict=True)):
    ck(f'part {i}: exact original name/value/unit', all(part[k] == precursor[k] for k in ['component_name', 'concentration_value', 'concentration_unit']))
    ck(f'part {i}: exact expected ID', part.get('component_id') == expected_ids[i])
    ck(f'part {i}: exact scope', part['reference_scope'] == ('UNMAPPED' if i == 6 else 'MIM_CATALOG'))
    ck(f'part {i}: author evidence binds actual object', part == child['selected_component'])
    ck(f'part {i}: active integration owner hash', sha(C / 'integration/worktree' / child['current_owner']['path']) == child['current_owner']['sha256'])
    ck(f'part {i}: preserved primary source literal', [part['component_name'], part['concentration_value'], 'mg/L'] == preflight['raw_cb_rows_42_51'][i])
ck('calcium has no hidden component ID', 'component_id' not in payload['components'][6])
ck('RECIPE_TRANSCRIPTION and UNKNOWN retained', payload['component_assertion']['method'] == 'RECIPE_TRANSCRIPTION' and payload['component_assertion']['completeness'] == 'UNKNOWN')
ck('original source evidence locator retained', all(payload['component_assertion']['evidence'][0][k] == w09['component_assertion']['evidence'][0][k] for k in ['evidence_type', 'source', 'source_record']))
ck('new component evidence has correct enum and LLM scope', payload['component_assertion']['evidence'][1]['evidence_type'] == 'CURATED_DATASET' and 'assisted by an LLM' in payload['component_assertion']['evidence'][1]['notes'])
ck('proposal is authentic existing-owner dependency', proposal['kind'] == 'edit_existing_owner' and proposal['owner_path'] == 'data/ingredients/mapped/Wolfes_Vitamin_Mix.yaml' and proposal['before_sha256'] == sha(before_path))
ck('proposal after reference exact', proposal['after_capture'] == ref(payload_path))
ck('only real W08 case ID used', proposal['case_ids'] == [cid])
ck('only actual NBRC903 trigger used', proposal['source_occurrence_ids'] == [trigger])
ck('no CB observation invented', proposal['cb_campaign_occurrence_count'] == dependency['cb_campaign_occurrences'] == 0)
ck('new proposal exact dependency copy', dependency['new_dependent_proposal'] == proposal)
ck('original NBRC903 proposal exact preserved object', dependency['original_nbrc903_proposal'] == old_nbrc)
ck('NBRC903 remains new owner with null before', old_nbrc['kind'] == 'new_owner' and old_nbrc['before_sha256'] is None)
ck('NBRC903 original payload remains byte exact', sha(A / old_nbrc['after_capture']['path']) == old_nbrc['after_capture']['sha256'] == 'e4a7c5d611dd36f449da97ec674100f58679ab5a5871996e79ca9837e73b2802')
case_allowed = {'proposal_ids', 'issue_refs', 'evidence_ids', 'reasoning', 'applicability', 'owner_records', 'independent_review', 'prior_independent_reviews'}
ck('case change only explicitly necessary keys', {k for k in old.keys() | decision.keys() if old.get(k) != decision.get(k)} == case_allowed)
ck('all six exact occurrences retained', decision['occurrence_ids'] == old['occurrence_ids'] and len(decision['occurrence_ids']) == 6)
ck('frozen case digest unchanged', decision['case_input_sha256'] == old['case_input_sha256'] == preflight['case_input_sha256'])
ck('new proposal backlink is additive', decision['proposal_ids'] == old['proposal_ids'] + [pid])
ck('original owner contexts preserved plus real comparator', decision['owner_records'] == old['owner_records'] + [{'path': proposal['owner_path'], 'sha256': proposal['before_sha256']}])
ck('old evidence IDs retained', decision['evidence_ids'][:len(old['evidence_ids'])] == old['evidence_ids'])
ck('new proposal evidence bound in changed case', set(proposal['evidence_ids']) <= set(decision['evidence_ids']))
ck('prior independent reviews preserved', decision['prior_independent_reviews'] == old['prior_independent_reviews'] + [old['independent_review']])
ck('author correctly leaves current review pending', decision['independent_review'] == {'status': 'pending', 'evidence_ids': []})
ck('all six source partitions retain frozen pointers', [x['occurrence_id'] for x in partitions['occurrences']] == decision['occurrence_ids'])
ck('one trigger partition and zero CB partition claims', sum(x['comparator_correction_trigger'] for x in partitions['occurrences']) == 1 and all(not x['CB_occurrence_asserted'] for x in partitions['occurrences']))
for source_name, source in nominal['nominal_recipe_sources'].items():
    ck(source_name + ': all source input facts bound', sha(source['capture']['path']) == source['capture']['sha256'] and len(source['inputs']) == 11)
    ck(source_name + ': water input not final volume', source['inputs'][-1]['basis'] == 'listed_water_input' and source['final_stock_volume'] is None and source['no_inferred_final_concentration'])
ck('NCMA water not numerically invented', nominal['NCMA_separate_positive_source']['carrier'] == {'name': 'distilled water', 'quantity': None, 'unit': None})
ck('NCMA genuine eleven-solute positive source retained', len(nominal['NCMA_separate_positive_source']['inputs']) == 11 and nominal['NCMA_separate_positive_source']['inputs'][-1]['printed_amount'] == '900')
ck('CB X remains metadata', nominal['CultureBotHT_source']['metadata']['X'] == '100' and nominal['CultureBotHT_source']['solvent'] is None)
for public in sorted((S / 'research').iterdir()):
    if public.is_file():
        private = W / '.temp/all-unmatched-worker-08/tenvit-dependent-v1/source-research' / public.name
        ck('source assessor bytes copied unchanged: ' + public.name, sha(public) == sha(private))

check_ref = write('author-byte-checks.json', {'at': NOW, 'status': 'PASS', 'reviewer': 'worker08:/root/inorganics', 'checks': checks, 'count': len(checks), 'scope': 'Read-only exact-byte and parsed-object checks; scientific appraisal is separately stated in review.json. No native validator rerun or maintained application.'})

# Read-scope log records this reviewer's actual prior tool reads, not merely the
# source assessor's file list. Original access times are copied as provenance.
source_entries = []
for item in preflight['primary_case_reads']:
    source_entries.append({'capture': item['capture'], 'url': item['original_url'], 'original_accessed_at': item['original_accessed_at'], 'read_scope': item['read_scope'], 'locator': 'Full primary recipe and vitamin/other-stock tables; vitamin table is the scoped formulation claim', 'scientifically_inspected': True})
for key in ['JCM197', 'NBRC837']:
    item = nominal['nominal_recipe_sources'][key]
    source_entries.append({'capture': item['capture'], 'url': item['url'], 'original_accessed_at': item['original_accessed_at'], 'read_scope': 'Complete primary HTML body text, all component tables and preparation instructions independently read through stdlib HTMLParser; compared stock versus receiving-medium instructions.', 'locator': item['locator'], 'scientifically_inspected': True})
ncma = nominal['NCMA_separate_positive_source']
source_entries.append({'capture': ncma['capture'], 'url': ncma['url'], 'original_accessed_at': ncma['original_accessed_at'], 'read_scope': 'Complete single-page primary PDF read through actual pdftotext extraction, including the composition-per-liter table and final water/filter-sterilization sentence.', 'locator': ncma['locator'], 'scientifically_inspected': True})
cb = nominal['CultureBotHT_source']
source_entries.append({'capture': cb['capture'], 'original_accessed_at': cb['original_accessed_at'], 'original_capture_metadata': cb['original_capture_metadata'], 'read_scope': 'Complete exact Wolfe generic block, CSV lines 38–51, plus adjacent block delimiters. Other unrelated CSV mixtures were not reviewed.', 'locator': cb['locator'], 'scientifically_inspected': True})
for row in preflight['occurrences']:
    source_entries.append({'capture': row['snapshot'], 'locator': row['component_path'], 'read_scope': 'Complete frozen recipe YAML inspected, including exact target occurrence, source metadata, nested vitamin formula and parent/stock preparation. Other ingredient fields were context, not independently approved.', 'scientifically_inspected': True})
context_reads = [
    (P / 'AUTHOR-TASK-W08.md', 'Entire authorization/routing document'),
    (W / 'MAPPING_SEMANTICS.md', 'Sections 3 and 6; identity, scope and component rules'),
    (W / '.claude/skills/review-yaml-record/SKILL.md', 'Entire read-only review workflow'),
    (W / 'docs/record-reviews.md', 'Entire native review guide'),
    (P / 'captures/w09/ADJUDICATION.json', 'All ten claim dispositions and boundaries'),
    (P / 'captures/w09/OPTIONS.json', 'Entire source-continuity alternatives and limits'),
    (P / 'captures/w09/nominal-ten-vitamin-source-description.json', 'All eleven nominal input rows and three source-specific preparations; historical context, not substituted for primary captures'),
    (P / 'captures/triage/assessment.json', 'Entire rootB continuity appraisal; original author/reviewer retained'),
    (P / 'captures/triage/exact-source-and-candidate-audit.json', 'Entire prior audit; historical native checks attributed to prior reviewer rather than rerun'),
    (P / 'captures/triage/HANDOFF.json', 'Entire prior handoff'),
    (D9 / 'history/REPORT.md', 'Entire historical continuity report; original April membership not reconstructed by this reviewer'),
    (D9 / 'skeptic/final-assembly-review.json', 'Entire W09 skeptical assembly receipt; no assertion this reviewer reran its native checks'),
    (P / 'ten-child-identity-matrix.json', 'Every child candidate, scope and complete compact primary ontology row set, including formula/SMILES/labels/synonyms. Database was not newly queried or rehashed.'),
    (P / 'eight-cases-and-scopes.json', 'All eight case identifiers, occurrence partitions and dispositions. Only assigned W08 six contexts independently scientifically reassessed; W06 receiving contexts not approved.'),
    (P / 'captures/w08/selected-payload.yaml', 'Entire original NBRC903 candidate including all components, mappings, aliases and history'),
]
for path in [before_path, w09_path, payload_path] + sorted((S / 'author').glob('*.json')):
    context_reads.append((path, 'Entire record or substantive JSON fields inspected; primary rows read in compact bounded output where full rendering would truncate.'))
for name in ['nominal-recipe-evidence.json', 'occurrence-partitions.json', 'comparison-assessment.json', 'source-read-ledger.json', 'HANDOFF.json']:
    context_reads.append((S / 'research' / name, 'Full scientific content and source/provenance boundaries read; source assessor is an author, not an independent final reviewer.'))
ledger = write('source-read-ledger.json', {
    'at': NOW, 'reviewer': 'worker08:/root/inorganics',
    'method': 'Fresh local primary source and full target payload inspection through tools; no new network calls. Hash-only bindings are explicitly separated.',
    'primary_and_frozen_source_reads': source_entries,
    'context_and_full_payload_reads': [{'input': ref(p), 'read_scope': scope} for p, scope in context_reads],
    'hash_only_scope': {'receipt': ref(O / 'preflight-review.json'), 'description': 'All 58 route-source byte bindings and all eight frozen case hashes were rechecked; this alone does not mean all W06 sources or whole referenced child owners were scientifically reviewed.'},
    'actual_limitations': ['Initial BeautifulSoup import failed with ModuleNotFoundError; stdlib HTMLParser succeeded and actual complete primary bodies were inspected.', 'Initial oversized output truncated; substantive fields were reread in bounded compact outputs.', 'No new network or live database access; original capture access timestamps remain unchanged.', 'The ten child current owner files were parsed and hash-checked for named-entity existence and identities, not approved in every inherited field.', 'Final assembled indices and native review pair are not yet present and require separate final readback.']
})

child_reasons = [
    'The raw HCl salt name and ChEBI formula/label identify pyridoxine hydrochloride, not the free base or an inferred hydrate.',
    'The explicit 4-amino locant and acid name match the para acid structure; no aminobenzoate salt or positional-isomer substitution.',
    'CHEBI:16494 has generic lipoic-acid structure without stereochemistry. The inherited DL filename is not a racemate proof and is not approved.',
    'Explicit nicotinic acid matches the acid structure, without replacing it with nicotinamide or a nicotinate salt.',
    'Explicit Riboflavin matches the named ontology entity; this is not procurement, lot or role certification.',
    'Explicit thiamine HCl matches the hydrochloride descriptor, preserving salt specificity and making no monohydrate assumption.',
    'Calcium pantothenate does not select D or DL. The inspected current CHEBI:31345 structure is D-specific, so retaining no component_id is the appropriate precise limit.',
    'Explicit biotin matches the named ontology entity, without adding a source-stated stereochemical or procurement qualification.',
    'Explicit Folic Acid matches the named acid entity; this does not authorize a folate salt substitution.',
    'The CB source explicitly prints Cyanocobalamin. CHEBI:17439 is supported for this component only; nominal JCM/NBRC Vitamin B12 stays unspecified.'
]
component_reviews = []
for row, reason in zip(bindings['owner_checks'], child_reasons, strict=True):
    component_reviews.append({'index': row['index'], 'component_name': row['selected_component']['component_name'], 'component_id': row['selected_component'].get('component_id'), 'scope': row['selected_component']['reference_scope'], 'status': 'RETAIN_PRECISE_UNMAPPED_HOLD' if row['index'] == 6 else 'SUPPORTED_NAMED_INPUT_REFERENCE', 'appraisal': reason, 'current_owner': row['current_owner'], 'primary_rows_canonical_sha256': canonical(row['primary_rows']), 'whole_child_owner_approval': False})
occurrence_reviews = []
for row in partitions['occurrences']:
    if row['primary_recipe_key'] == 'NBRC903':
        reason = 'The exact NBRC903 vitamin table provides ten named masses and one litre distilled-water input. It is the sole occurrence whose original proposal invoked the current Wolfe phosphate comparison. The separate dependent edit corrects that comparator, without mapping this occurrence to CB or changing its 10 mL/L receiving dose.'
    elif row['primary_recipe_key'] == 'NBRC1226':
        reason = 'The complete NBRC1226 vitamin table has B12 5 mg, pABA 1 mg and lipoic acid 5 mg per listed water-input batch. Its distinct source formula and 1 mL/L receiving occurrence remain outside the comparator change.'
    else:
        reason = 'The complete source vitamin table has nine named vitamins, generic B12 0.01 mg and pABA 1 mg with no lipoic row, plus one litre water input. The existing common-nine branch and literal receiving dose are preserved; no CB routing follows.'
    occurrence_reviews.append({'occurrence_id': row['occurrence_id'], 'recipe_id': row['recipe_id'], 'source_identifier': row['source_identifier'], 'frozen_recipe': row['frozen_recipe'], 'component_path': row['component_path'], 'partition': row['partition'], 'comparator_trigger': row['comparator_correction_trigger'], 'appraisal': reason, 'CB_occurrence_assigned': False})

findings_ref = write('findings.json', {'at': NOW, 'reviewer': 'worker08:/root/inorganics', 'new_findings': [], 'open_blocking_findings_for_this_bounded_correction': [], 'existing_lineage': ['TV-003 current-source correction is supported at proposed-byte scope; it is not a GitHub closure or maintained application.', 'CONT-NCMA-WATER-001 remains a separate existing boundary: NCMA has unquantified distilled-water addition, not literal 1.0 L/L.', 'TV-001, TV-002 and TV-004 source/owner association holds remain.'], 'scope': 'No new necessary author change found after actual full candidate, beforeimage, source and changed-case inspection.'})

input_files = [S / 'author' / name for name in ['assessment.json', 'child-bindings.json', 'dependency-dispositions.json', 'proposal.json', 'decision.json']]
input_files += [S / 'research' / name for name in ['nominal-recipe-evidence.json', 'occurrence-partitions.json', 'comparison-assessment.json', 'source-read-ledger.json', 'HANDOFF.json']]
input_files += [before_path, w09_path, payload_path]
review = {
    'at': NOW, 'status': 'PASS', 'verdict': 'SUPPORTED_BOUNDED_CORRECTION_WITH_ALL_HOLDS',
    'reviewer': '/root/inorganics', 'reviewer_worker': 'worker08', 'author': '/root', 'author_worker': 'worker08',
    'independence_disclosure': 'This reviewer authored the separate W08 inorganic cohort and previously independently reviewed W08 vitamin proposals, including this mixed case. This reviewer did not author the current Wolfe correction or earlier NBRC903 vitamin proposal. Root is the current author; vitamins supplies source research as the prior vitamin author, not independent final approval. The present conclusion follows fresh full target/source reads and an independent exact-byte check.',
    'full_payload_review': True, 'case_ids': [cid], 'proposal_ids': [pid],
    'case_hashes': {cid: canonical(decision)}, 'case_input_hashes': {cid: decision['case_input_sha256']},
    'payload_hashes': {pid: sha(payload_path)}, 'proposal_hashes': {pid: canonical(proposal)},
    'input_hashes': {str(p.relative_to(A)): sha(p) for p in input_files},
    'case_reviews': [{'case_id': cid, 'status': 'SUPPORTED_WITH_PRESERVED_HOLDS', 'appraisal': 'All six frozen occurrences are preserved in their three source-formula partitions. Only NBRC903 triggers the authentic existing-owner comparator dependency. The changed case adds evidence, the real nonnull comparator preimage and a separate proposal while preserving all old proposal links and prior independent-review lineage. It does not assert CB membership, adopt W06 cases or resolve an exact common stock owner.', 'occurrence_reviews': occurrence_reviews, 'source_evidence_ids': proposal['evidence_ids'], 'finding_ids': []}],
    'proposal_reviews': [{'proposal_id': pid, 'after_sha256': sha(payload_path), 'status': 'SUPPORTED_BOUNDED_EXISTING_OWNER_CORRECTION', 'whole_payload_appraisal': 'The complete supplied candidate accurately replaces the unbridged active NCMA assertion with the CB ten-solute definition. All ten literal names, order, numeric strings and MG_PER_L units are preserved; X100 is metadata only. UNKNOWN is justified by unspecified carrier/preparation closure. Nine named-entity catalog references are source-compatible and calcium pantothenate remains ungrounded for a concrete stereochemistry limit. The authentic five-event history plus actual W09 event are preserved, followed by a separately identified honest W08 LLM event. Identity, preferred label, raw alias, mapping object, 61/61 statistics, type and inherited nutritional role objects are unchanged. No quantified water, phosphate, rescaling, alias release or hidden whole-owner approval is introduced.', 'component_reviews': component_reviews, 'before_sha256': sha(before_path), 'source_evidence_ids': proposal['evidence_ids'], 'finding_ids': []}],
    'dependency_review': {'status': 'SUPPORTED_AUTHENTIC_ROUTE_WITH_RECONCILIATION_HELD', 'original_nbrc903_proposal_id': old_nbrc['proposal_id'], 'original_kind': old_nbrc['kind'], 'original_before_sha256': old_nbrc['before_sha256'], 'original_after_sha256': old_nbrc['after_capture']['sha256'], 'original_canonical_sha256': canonical(old_nbrc), 'appraisal': 'The published NBRC903 candidate really invoked the Wolfe phosphate list; the new edit therefore has an authentic causal route. The new existing-owner edit retains the 709749bd preimage rather than converting or relabeling the NBRC903 new-owner/null-before original. W06 C-P-JCM197 and W08 vm1201-prop-nbrc903-vitamin are central reconciliation inputs for the same nominal input recipe; missing vitamer/preparation detail proves neither equal nor distinct CB substance. Neither candidate is selected as a winner and no duplicate installation or W06 ownership transfer is authorized.'},
    'source_partition_appraisal': 'The actual JCM197/NBRC837/NBRC903 tables support ten vitamin masses and one litre distilled water as an input batch. JCM197 stock N2 gassing is not transferred to NBRC recipes; parent gas, pH, reducing agents and mineral KOH instructions remain separate. Generic B12 is not cyanocobalamin. The genuine NCMA eleven-solute/phosphate formula remains positive separate evidence; its water is unquantified. The old W09 source report is preserved historical context, while the new nominal facts use three explicit source recipes and actual printed values.',
    'retained_concerns': [
        'The inherited ontology_mapping DATABASE_MATCH/absence rationale is unchanged and not newly approved by this component-source correction.',
        'The inherited NCMA-based VITAMIN_SOURCE role remains byte-preserved with no renewed source-equivalence or role approval.',
        'The original historical count 61 is preserved; later 62/63 sources do not reconstruct missing April membership.',
        'The earlier NBRC903 exact JCM197 alias is retained in the original candidate only as a held integration input; this review does not release it or approve a second source-number owner.',
        'The eight-case family, 71 CM contexts, 84 separate KG holds and six exclusions remain context. The 65 nominal-context bound is not mapping approval.',
        'Child references do not approve inherited aliases, chemical properties, procurement details, roles or all child-owner fields. Generic lipoic acid is not a racemate claim.',
        'All unrelated owner/source/role/export holds, including the Trypticase/Bacto admission failure, remain outside this bounded correction.'
    ],
    'open_blocking_findings': [], 'findings': [],
    'mechanical_checks': check_ref, 'primary_read_log': ledger, 'finding_receipt': findings_ref,
    'final_assembly_boundary': {'status': 'PENDING_SEPARATE_READBACK', 'allowed_metadata_only_additions': ['Append completed independent review evidence IDs to this changed case and new proposal, preserving the authored scientific content and all prior reviews.', 'Add corresponding reviewer evidence objects and dependency/source indices.', 'Preserve all 113 original proposal objects and payloads, all 187 unrelated decisions, all prior evidence objects and all frozen 320 occurrence links when building the aggregate. Add exactly this one dependent proposal.'], 'forbidden_without_rereview': ['Changing the target payload, scientific case prose, source partitions, authentic beforeimage, original NBRC903 kind/origin, any literal source amount or any hold.']},
    'limitations': ['No live network or ontology refresh; actual supplied primary captures and exact current owner hashes were inspected.', 'The source assessor is not treated as independent final review.', 'No fresh full W06 case review, W09 historical 62/63 receiving audit, full referenced-child-owner approval, native validator rerun or final aggregate readback is claimed.', 'This result approves the bounded isolated proposal for coordinator consideration only; it does not approve maintained application, exports, exact shared-owner associations, issue closure or role release.'],
    'maintained_application_authorized': False, 'whole_owner_approval': False, 'role_export_approval': False
}
review_ref = write('review.json', review)
handoff = write('HANDOFF.json', {'at': NOW, 'status': 'FROZEN_INITIAL_EXACT_AUTHOR_REVIEW', 'review': review_ref, 'checks': check_ref, 'source_read_ledger': ledger, 'findings': findings_ref, 'payload_sha256': sha(payload_path), 'case_id': cid, 'proposal_id': pid, 'new_findings': [], 'next': 'Root may attach this immutable review and assemble the full aggregate. Final selected indices and native pair need a separate readback; this receipt is not rewritten.'})
print(json.dumps({'status': 'PASS', 'checks': len(checks), 'review': review_ref, 'handoff': handoff}, indent=2))
