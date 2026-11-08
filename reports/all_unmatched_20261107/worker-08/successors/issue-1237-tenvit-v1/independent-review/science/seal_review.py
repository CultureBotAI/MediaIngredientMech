"""Seal this author's independent review; never writes proposal or catalog bytes."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import yaml

P = Path(__file__).resolve().parent
W = P.parents[3]
C = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
R = C / 'preflight/tenvit-final-application-route-v1'
A = W / 'reports/all_unmatched_20261107/worker-08'
O = A / 'successors/issue-1237-tenvit-v1'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
canonical_sha = lambda d: hashlib.sha256(json.dumps(d, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode()).hexdigest()
def read(p): return json.loads(p.read_text())
def save(name, value):
    with (P/name).open('x') as f:
        json.dump(value, f, indent=2, ensure_ascii=False); f.write('\n')
now = datetime.now(timezone.utc).isoformat()
component_review = read(P/'component-assessment-v1.json')
validation = read(P/'final-validation.json')
assert validation['status'] == 'PASS' and validation['check_count'] == 151
decision = read(O/'author/decision.json'); proposal = read(O/'author/proposal.json')
payload = yaml.safe_load((O/'payloads/Wolfes_Vitamin_Mix.yaml').read_text())
assert sha(O/'payloads/Wolfes_Vitamin_Mix.yaml') == validation['payload_sha256']
assert canonical_sha(decision) == validation['case_canonical_sha256']
ledger = []
def add(path, scope, kind='context', **extra):
    ledger.append({'path':str(path), 'sha256':sha(path), 'inspection_recorded_at':now,
                   'kind':kind, 'actual_read_scope':scope, **extra})

research_ledger = read(O/'research/source-read-ledger.json')
for e in research_ledger['entries']:
    if e['kind'] in ['primary_source', 'raw_source']:
        scope = ('Whole single-page NCMA composition and preparation text via actual pdftotext stdout.' if e['path'].endswith('.pdf') else
                 'Complete CB Wolfe block rows 38–51, adjacent boundary and current raw byte equality; no unrelated CSV formulations assessed.' if e['kind']=='raw_source' else
                 'Actual primary HTML read using independent standard-library text extraction; complete vitamin table, receiving dose and preparation partitions inspected.')
        add(Path(e['path']),scope,e['kind'],original_accessed_at=e['original_accessed_at'],original_url=e.get('url'),new_remote_retrieval=False)
for e in component_review['occurrence_reviews']:
    add(Path(e['path']), 'Complete frozen record read; target pointer, raw component and hash checked. Other ingredient identities are context, not approved.', 'frozen_source_context', locator=e['locator'], occurrence_id=e['occurrence_id'])
matrix = read(R/'ten-child-identity-matrix.json')
for ch in matrix['children']:
    for path in [W/'data/ingredients/mapped'/Path(ch['active_owner']['path']).name,Path(ch['active_owner']['path']),R/ch['active_owner']['captured_path']]:
        add(path,'Entire child record and history inspected; three exact byte-identical copies verified. Approval limited to referenced named identity, never inherited aliases, properties or roles.','catalog_owner_context',component_index=ch['candidate_component_index'])
add(R/'captures/w08/component-ontology-lookup.json','All descriptor rows for ten selected identities read; exact matrix subset verified. Other terms in the extract are outside scope.','primary_ontology_extract',live_database_rehashed=False)
add(R/'captures/w08/exact-form-ontology-lookup.json','Complete CHEBI:16494, CHEBI:748116 and CHEBI:60911 term arrays read for generic versus explicit racemate distinction; unrelated search hits not used.','primary_ontology_extract',live_database_rehashed=False)
for fn in ['shared-CAS_68-19-9_properties.json','shared-CAS_68-19-9_synonyms.json']:
    add(R/'captures/w08'/fn,'Complete supplementary response read. Mixed generic B12/other names are not used to equate generic B12 with cyanocobalamin.','supplementary_registry_response')
for fn in ['AUTHOR-TASK-W08.md','README.md','HANDOFF.json','source-bindings.json','ten-child-identity-matrix.json','candidate-boundary-checks.json','captures/before-Wolfes_Vitamin_Mix.yaml','captures/candidate-fe607027.yaml','captures/w08/selected-payload.yaml','captures/w06/selected-payload.yaml','captures/triage/assessment.json','captures/triage/exact-source-and-candidate-audit.json','captures/triage/HANDOFF.json','captures/w09/ADJUDICATION.json','captures/w09/HANDOFF.json','captures/w09/OPTIONS.json','captures/w09/nominal-ten-vitamin-source-description.json']:
    add(R/fn,'Complete relevant document/object read; distinct original authorship, positive source claims and exact approval limits retained.')
add(R/'eight-cases-and-scopes.json','Full W08 frozen case and six occurrence objects, counts, partitions and family limits read. Other workers are continuity context; not fresh approval of 71 occurrences or 84 KG holds.')
add(R/'captures/w08/component-review.json','Ten selected prior per-component review entries compared exactly to the matrix; prior receipt is context, not automatic new approval.')
add(C/'workers/w09/worktree/.temp/tenvit-continuity-resolution-v1/skeptic/final-assembly-review.json','Entire W09 final peer receipt read. Historical 63/62 occurrence review and 58 unrecovered members are attributed to its authors, not repeated here.')
for fn in ['MAPPING_SEMANTICS.md','.claude/skills/add-media/SKILL.md','.claude/skills/review-yaml-record/SKILL.md','docs/record-reviews.md','docs/record-review-profile.md']:
    add(W/fn,'Identity and component contracts applied; semantics Sections 3 and 6, full focused skills/review profile. Private-only task boundary overrides canonical saving location.','contract')
for fn in ['payloads/Wolfes_Vitamin_Mix.yaml','author/proposal.json','author/decision.json','author/assessment.json','author/child-bindings.json','author/dependency-dispositions.json']:
    add(O/fn,'Whole final object reviewed; all component, provenance, quantity, history, dependency and case fields assessed against exact sources.','final_authored_input')
for p in sorted((O/'research').iterdir()):
    if p.is_file():
        add(p,'Source research record/derived text or archived builder inspected and exact HANDOFF hash verified; independent primary reading supplies science. This prior-author assessment is not an independent approval.','supporting_research_artifact')
save('source-read-ledger.json',{'reviewer':'/root/organics','recorded_at':now,'entries':ledger,
     'remote_requests_this_review':0,
     'failures_and_limits':[
         'An initial local extraction assumed exact-form-ontology-lookup.json had a rows key and raised KeyError. Its actual terms structure was then read directly; no unavailable scientific source was claimed.',
         'Initial source-directory probe at C/inputs failed; the assignment identifies C/queue/preliminary-v5, whose six exact sources were successfully read and hashed.',
         'Some broad console dumps were truncated; selected primary terms, all source tables and relevant author fields were subsequently read in bounded outputs.',
         'Preserved capture timestamps are original retrieval times. Current inspection times are separate; no live ontology release check or live database rehash claimed.',
         'No article behind an ontology cross-reference or inherited PubMed snippet was treated as read primary literature.'
     ]})

field_assessments = {
 'identifier':'Same authentic registry identity retained; no new mint or common nominal owner identity chosen.',
 'preferred_term':'Existing preferred label unchanged; it does not become a global label-based equivalence bridge.',
 'synonyms':'Entire inherited RAW_TEXT synonym object unchanged; no new exact/global alias, occurrence pointer or source remap.',
 'mapping_status':'MAPPED preserved as catalog state, not a release disposition.',
 'occurrence_statistics':'61/61 retained as historical import evidence; no claim to have recovered original 58 unnamed members or recomputed current membership.',
 'curation_history':'All five original events and actual W09 sixth event preserved verbatim as parsed objects; one honestly attributed LLM-assisted root event appended. Historical ten-UNMAPPED statement is explicitly superseded in operative notes.',
 'notes':'CB ten-solute mg/L/X100 scope, no guessed carrier, separate genuine NCMA formula, one precise D/DL hold, generic nominal B12, preparation limits and dependency-only occurrence scope are explicit. No new biological or procurement specificity.',
 'ingredient_type':'Existing STOCK_SOLUTION retained and appropriate for source-defined preparation; no molecular identity collapse.',
 'solution_type':'Existing VITAMIN_MIX retained; this type does not confer functional role approval.',
 'components':'All ten literal names/order/masses/MG_PER_L rows exact; nine supported named-entity bindings and one UNMAPPED calcium form hold. No phosphate, water, titrant or scaled values introduced.',
 'component_assertion':'RECIPE_TRANSCRIPTION truthfully describes source membership and amounts. RECIPE_SOURCE binds exact CB block; added CURATED_DATASET binds documented catalog/primary descriptor adjudication with explicit LLM disclosure. UNKNOWN concerns unestablished full-stock carrier/preparation closure; ten printed solutes are retained.',
 'ontology_mapping':'Entire inherited registry mapping/evidence preserved without renewed approval. Inherited claim that no ontology could represent a preparation is not adopted as scientific authority.',
 'nutritional_roles':'Entire inherited NCMA role object preserved as held context. No transfer of NCMA source equivalence or renewed role/export approval.'
}
assert set(field_assessments)==set(payload)
case_appraisal = ('The single changed six-occurrence case preserves its source label, frozen case hash, all six occurrence IDs and their receiving doses. Four common-nine branches and the NBRC1226 branch remain unchanged. Only NBRC903/CultureMech:007503 in frozen NBRC_904.yaml ingredients/9 triggers the genuine existing-owner comparator dependency. None of those six observations becomes a CB occurrence. The original NBRC903 new_owner/null-before proposal remains immutable reconciliation input. The corrected CB comparator no longer uses the old NCMA phosphate assertion; positive NCMA facts remain separate. Exact CB-to-nominal association and central W06/W08 common nominal owner reconciliation remain held, without inventing distinct substances from source numbers or requiring perfect molecular detail to preserve the nominal recipe.')
input_hashes = {str(p.relative_to(A)):sha(p) for p in [O/'payloads/Wolfes_Vitamin_Mix.yaml',O/'author/proposal.json',O/'author/decision.json',O/'author/assessment.json',O/'author/child-bindings.json',O/'author/dependency-dispositions.json'] + list(sorted((O/'research').glob('*'))) if p.is_file()}
review = {
    'reviewer':'/root/organics','author':'/root','reviewer_worker':'worker08','author_worker':'worker08',
    'independence_basis':'The reviewer did not author this vitamin proposal, its root composition, or the original W09 source correction. Earlier W08 component peer review is declared context; the current primary rows, exact catalog records, complete final payload and case were freshly inspected. Prior organic-product authorship is outside this vitamin scope.',
    'completed_at':now,'status':'complete','verdict':'pass_with_limitations','scientific_review':True,
    'case_ids':[decision['case_id']],'proposal_ids':[proposal['proposal_id']],
    'full_payload_review':True,'open_blocking_findings':[], 'new_findings':[],
    'case_hashes':{decision['case_id']:canonical_sha(decision)},'case_input_hashes':{decision['case_id']:decision['case_input_sha256']},
    'payload_hashes':{proposal['proposal_id']:validation['payload_sha256']},'input_hashes':input_hashes,
    'case_reviews':[{'case_id':decision['case_id'],'outcome':'supported_bounded_dependency_with_preserved_holds','appraisal':case_appraisal,'occurrence_ids':decision['occurrence_ids'],'occurrence_reviews':component_review['occurrence_reviews'],'evidence_ids':proposal['evidence_ids'],'finding_ids':[]}],
    'proposal_reviews':[{'proposal_id':proposal['proposal_id'],'owner_path':proposal['owner_path'],'kind':proposal['kind'],'before_sha256':proposal['before_sha256'],'after_sha256':validation['payload_sha256'],'outcome':'supported_isolated_source_correction_and_nine_component_bindings','appraisal':'The full composed proposal preserves authentic continuity and all unchanged identity/alias/role fields, corrects the active CB source decomposition, and supplies nine independently supported component identities without transferring generic JCM/NBRC B12 specificity. One exact supplied-form hold remains. This is candidate support, not whole-owner or application approval.','field_assessments':field_assessments,'component_reviews':component_review['component_reviews'],'evidence_ids':proposal['evidence_ids'],'finding_ids':[]}],
    'known_issue_scope':[
        {'issue':'1237','finding':'TV-003','disposition':'Exact isolated candidate supplies the supported CB source correction; no maintained application or whole-issue closure claimed.'},
        {'issue':'1237','finding':'CONT-NCMA-WATER-001','disposition':'Actual PDF reconfirms unquantified NCMA water; held separate positive source claim, no NCMA owner correction or closure made here.'},
        {'findings':['TV-001','TV-002','TV-004'],'disposition':'Retained unresolved; no ATCC/product-scale or family routing release.'}
    ],
    'remaining_holds':component_review['remaining_holds'],
    'approval':{'bounded_final_candidate_support':True,'maintained_application':False,'whole_child_owner_fields':False,'global_aliases':False,'roles':False,'exports':False,'joint_nominal_owner_selection':False},
    'checks':{'path':str(P/'final-validation.json'),'sha256':sha(P/'final-validation.json'),'result':'PASS','count':151,'scope':validation['scope']},
    'source_read_ledger':{'path':str(P/'source-read-ledger.json'),'sha256':sha(P/'source-read-ledger.json')},
    'allowed_final_index_metadata_append':{'allowed':True,'scope':'Coordinator may append this exact peer receipt reference and independent_review status/evidence links, retaining prior independent-review provenance, in separately produced final indices. No changes to scientific reasoning, applicability, source identity, occurrence IDs, quantities, holds, proposal identity/preimage/payload or evidence source claims are approved by this exception. Author input bytes remain immutable.','verification':'Root must verify this exact metadata-only boundary when assembling final indices.'},
    'limitations':['One changed case and one complete final payload reviewed; not a fresh scientific rereview of all 188 cases or other selected proposals.','Native strict/partonomy checks were narrow; root owns full overlay and publication gates.','Continuity review scopes and historical Git/receiving-media audits remain attributed to W09/rootB, not claimed as fresh executions here.']
}
save('review.json',review)
save('findings.json',{'reviewer':'/root/organics','author':'/root','at':now,'review_sha256':sha(P/'review.json'),'new_findings':[],'open_blocking_findings':[],'retained_holds':review['remaining_holds'],'whole_owner_or_release_approval':False})
save('HANDOFF.json',{'status':'FROZEN_COMPLETE','reviewer':'/root/organics','author':'/root','at':now,'review_sha256':sha(P/'review.json'),'findings_sha256':sha(P/'findings.json'),'source_read_ledger_sha256':sha(P/'source-read-ledger.json'),'validation_sha256':sha(P/'final-validation.json'),'case_count':1,'occurrence_count':6,'whole_payload_count':1,'component_count':10,'supported_named_bindings':9,'precise_form_holds':1,'new_findings':0,'verdict':'pass_with_limitations','maintained_or_publication_mutation':False})
(P/'HANDOFF.md').write_text('Independent review complete for the root-authored ten-vitamin dependent proposal. The complete final payload and six-occurrence case support the bounded CB correction, nine catalog references and one calcium-pantothenate D/DL hold. All 151 focused checks passed. No new finding.\n\nThe review does not approve inherited child aliases/roles, common nominal owner selection, occurrence transfer, maintained application or downstream release. Exact review and source bindings are in review.json, source-read-ledger.json and HANDOFF.json. Only an explicitly checked metadata-only peer-reference append is allowed in final assembly.\n')
with (P/'MANIFEST.sha256').open('x') as f:
    for p in sorted(P.rglob('*')):
        if p.is_file() and p.name!='MANIFEST.sha256': f.write(sha(p)+'  '+str(p.relative_to(P))+'\n')
print(json.dumps({'review':sha(P/'review.json'),'handoff':sha(P/'HANDOFF.json'),'manifest':sha(P/'MANIFEST.sha256'),'entries':len(ledger)}))
