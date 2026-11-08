"""Private independent assessment, not a payload writer or release gate."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import yaml

P = Path(__file__).resolve().parent
W = P.parents[3]
C = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
R = C / 'preflight/tenvit-final-application-route-v1'
Q = C / 'queue/preliminary-v5'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
canon = lambda d: hashlib.sha256(json.dumps(d, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode()).hexdigest()
now = datetime.now(timezone.utc).isoformat()
matrix = json.loads((R / 'ten-child-identity-matrix.json').read_text())
bindings = json.loads((P / 'initial-bindings.json').read_text())
appraisals = [
    'The source explicitly names pyridoxine HCl. CHEBI:30961 is pyridoxine hydrochloride, with C8H11NO3.HCl and chloride-bearing structure. This preserves the stated salt instead of replacing it with pyridoxine base. The printed 10 mg/L is unchanged; no hydration, supplier or purity claim is added.',
    'The source positional name 4-Aminobenzoic acid matches the primary exact synonym and para-substituted acid structure of CHEBI:30753. The catalog preferred p-aminobenzoic acid names that same position. Binding the 5 mg/L input does not endorse inherited zwitterion, concentration or unrelated raw aliases on the child.',
    'The source says only Lipoic acid. CHEBI:16494 has that canonical label and generic, stereo-unspecified free-acid descriptor. CHEBI:748116 separately has DL synonyms and an explicit racemate superclass; CB does not select it. Nonstereochemical SMILES does not prove a racemate. The catalog filename/preferred DL wording and inherited generic/racemic merge history remain unapproved; this component reference denotes only the generic CHEBI:16494 named input at 5 mg/L.',
    'Nicotinic Acid matches CHEBI:15940, pyridine-3-carboxylic acid, with C6H5NO2 and acid structure. Neither nicotinamide nor a sodium/nicotinate salt is selected. The 5 mg/L printed input is retained; child aliases and role evidence are not transferred.',
    'Riboflavin matches the canonical CHEBI:17015 name and ribityl-flavin structure. The conventional named compound is supported; neither flavin mononucleotide nor a supplied stock concentration is inferred. The 5 mg/L input remains literal, without purity or procurement claims.',
    'The explicit thiamine HCl label is a primary synonym of CHEBI:49105, thiamine hydrochloride, whose chloride-hydrochloride/dichloride descriptors preserve the salt. It is not free thiamine or thiamine pyrophosphate. The 5 mg/L amount and literal capitalization remain unchanged.',
    'The source calcium pantothenate does not specify D versus DL. The proposed catalog candidate CHEBI:31345 carries two stereospecific pantothenate moieties and D-specific descriptors despite its generic label and inherited DL aliases. These facts do not establish that CB used the D form. Retain the 5 mg/L literal component as UNMAPPED with no component_id; this is a supplied-form hold, not an ontology-absence claim.',
    'The source biochemical name biotin is the canonical CHEBI:15956 name, supported by its structure and nomenclature. The named-input reference preserves the 2 mg/L row; it does not establish a supplier, grade or arbitrary biotin analogue. Inherited roles and stock-like raw labels remain outside approval.',
    'Folic Acid matches canonical CHEBI:27470 and its pteroyl-L-glutamic acid descriptor. It does not support the inherited folinic-acid alias on that child. The new reference is limited to the printed 2 mg/L folic-acid input, with no alias, salt or role assertion.',
    'CB explicitly prints Cyanocobalamin, unlike the generic Vitamin B12 in JCM/NBRC. CHEBI:17439 has cyanocobalamin as a primary synonym of cyanocob(III)alamin and a cyano-ligand structure; the active catalog owner has the same identifier. Bind only this 0.1 mg/L named input. The supplementary PubChem CAS response mixes generic B12 and other names and is not used as independent proof that generic B12 means cyanocobalamin.'
]
entries = []
for x, b, appraisal in zip(matrix['children'], bindings['children'], appraisals, strict=True):
    rows = x['primary_ontology_rows']
    entries.append({
        'index': x['candidate_component_index'], 'literal_component': x['literal_component'],
        'outcome': 'retain_precise_D_DL_hold' if x['candidate_component_index'] == 6 else 'source_compatible_MIM_CATALOG_identity',
        'component_id': None if x['candidate_component_index'] == 6 else x['active_identity'],
        'reference_scope': 'UNMAPPED' if x['candidate_component_index'] == 6 else 'MIM_CATALOG',
        'appraisal': appraisal, 'catalog_bindings': b['paths'], 'catalog_hashes': b['hashes'],
        'primary_evidence_path': str(R / 'captures/w08/component-ontology-lookup.json'),
        'primary_evidence_sha256': sha(R / 'captures/w08/component-ontology-lookup.json'),
        'primary_locator': f"/rows[subject={x['active_identity']}]", 'primary_rows_sha256': canon(rows),
        'raw_locator': f'Mixes.csv line {42 + x["candidate_component_index"]}',
        'source_read': True, 'complete_child_record_read': True, 'whole_child_owner_approved': False,
    })

cases = json.loads((R / 'eight-cases-and-scopes.json').read_text())['cases']
case = next(c for c in cases if c['worker'] == 8)
assert canon(case['source_case']) == case['case_input_sha256']
occurrences = []
for o in case['source_case']['occurrences']:
    path = Q / o['full_recipe_snapshot']
    assert sha(path) == o['source_file_sha256']
    data = yaml.safe_load(path.read_text())
    actual = data
    for part in o['component_path'].split('/'):
        actual = actual[int(part)] if isinstance(actual, list) else actual[part]
    assert actual == o['raw_component']
    branch = ('NBRC903_comparator_trigger_only' if o['occurrence_id'].endswith('cdd531')
              else 'unchanged_NBRC1226_branch' if '1227' in o['source_file'] else 'unchanged_common_nine_branch')
    occurrences.append({'occurrence_id': o['occurrence_id'], 'path': str(path), 'sha256': sha(path),
                        'locator': o['component_path'], 'raw_component': actual, 'source_id': data['media_term']['term']['id'],
                        'branch': branch, 'complete_frozen_record_read': True,
                        'approval': 'No route to the corrected CB owner; source-specific branch and receiving dose preserved.'})

review = {
    'at': now, 'reviewer': '/root/organics', 'author': '/root',
    'independence': 'Worker08 peer did not author the new root candidate. Earlier component review is retained context; current ten rows, primary extracts and exact owners were freshly read. This is not whole-child-owner approval.',
    'status': 'component_review_complete_final_candidate_pending', 'component_reviews': entries,
    'counts': {'literal_inputs': 10, 'source_compatible_catalog_bindings': 9, 'precise_form_holds': 1},
    'before_and_W09_candidate_assessment': {
        'before_sha256': bindings['before_sha256'], 'w09_sha256': bindings['w09_candidate_sha256'],
        'full_objects_read': True,
        'appraisal': 'The same owner path/identifier has authentic earlier CultureBotHT lineage; the W09 candidate replaces only the active source decomposition and associated notes/history with the ten literal CB inputs. Its ten UNMAPPED references are a historical intermediate, not evidence of ontology absence. All nine other fields and five original history events remain exact. The final composed candidate must preserve these and the W09 sixth event while adding truthful component evidence and an LLM-assisted event.',
        'retained_unapproved_fields': ['ontology_mapping', 'synonyms', 'nutritional_roles', 'occurrence_statistics beyond historical preservation'],
        'source_scope': 'CB concentrations and separate X100 metadata; no water, phosphate or preparation inferred. The actual NCMA PDF supports its separate eleven-solute formula including 900 mg/L phosphate and unquantified distilled-water instruction.'
    },
    'case_id': case['case_id'], 'case_input_sha256': case['case_input_sha256'], 'occurrence_reviews': occurrences,
    'nominal_comparison': 'The inspected JCM197/NBRC837/NBRC903 primary tables support the same ten nominal masses plus one litre of distilled-water input. JCM197 expressly gases trace vitamins with N2; the NBRC instructions support filtration and anaerobic addition without that stock-gas assertion. Generic B12 and unqualified calcium pantothenate remain literal. No final-volume conversion, exact CB equivalence or proven chemical difference is inferred.',
    'remaining_holds': [
        'Calcium pantothenate D/DL supplied form.',
        'Generic JCM/NBRC B12 vitamer and exact nominal-to-CB owner association.',
        'Nominal preparation joint-owner reconciliation, not separate identities merely from source numbers.',
        'Historical 61 occurrence statistic remains historical; original 58 unnamed import members are not newly verified.',
        'All family source, dose, nested, J887, ATCC/X1, product, role and downstream admission holds; this review does not release 71 occurrences, 84 KG holds or the 65-context upper bound.',
        'Inherited child aliases, chemical claims, mappings and roles outside the nine precise referenced identities are not approved.'
    ],
    'new_findings': [], 'final_candidate_approved': False,
    'limitations': ['No fresh live ontology service or live database rehash; reviewed the exact preserved primary descriptor extracts.', 'No unread literature cited by ontology or owner records was treated as inspected primary evidence.', 'Frozen case contexts are not new biological validity or whole-recipe assessments.']
}
(P / 'component-assessment-v1.json').write_text(json.dumps(review, indent=2, ensure_ascii=False) + '\n')
print(json.dumps({'status': review['status'], 'components': len(entries), 'occurrences': len(occurrences), 'sha256': sha(P / 'component-assessment-v1.json')}))
