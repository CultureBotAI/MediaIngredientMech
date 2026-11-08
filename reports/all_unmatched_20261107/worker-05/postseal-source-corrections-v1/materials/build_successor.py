"""Create the isolated BSA source-context successor; never write maintained inputs."""
from pathlib import Path
import copy
import datetime
import difflib
import hashlib
import json
import sys

import yaml

W = Path.cwd()
sys.path.insert(0, str(W / 'src'))
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.write_validated import write_validated_ingredient

L = Path(__file__).resolve().parent
R = W / 'reports/all_unmatched_20261107/worker-05'
C = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
PREFIX = 'postseal-source-corrections-v1/materials/'
AUTHOR = '/root/materials_research'
AT = datetime.datetime.now(datetime.timezone.utc).isoformat()
COMMENT_URL = 'https://github.com/CultureBotAI/MediaIngredientMech/issues/1193#issuecomment-6718748704'
SOURCE_URL = 'https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M194'

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def object_sha(x):
    return hashlib.sha256(json.dumps(x, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest()

def save(name, x):
    p = L / name
    assert not p.exists(), p
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')

def capture(name):
    return {'root': 'artifact', 'path': PREFIX + name, 'sha256': sha(L / name)}

def changes(a, b, path=''):
    if type(a) is not type(b):
        return [{'path': path, 'before': a, 'after': b}]
    if isinstance(a, dict):
        out = []
        for k in sorted(set(a) | set(b)):
            if k not in a or k not in b:
                out.append({'path': path + '/' + k, 'before': a.get(k), 'after': b.get(k)})
            else:
                out.extend(changes(a[k], b[k], path + '/' + k))
        return out
    if isinstance(a, list):
        out = []
        for i in range(max(len(a), len(b))):
            if i >= len(a) or i >= len(b):
                out.append({'path': path + '/' + str(i), 'before': a[i] if i < len(a) else None, 'after': b[i] if i < len(b) else None})
            else:
                out.extend(changes(a[i], b[i], path + '/' + str(i)))
        return out
    return [] if a == b else [{'path': path, 'before': a, 'after': b}]

old_d = json.loads((L / 'inputs/decisions.json').read_text())
old_p = json.loads((L / 'inputs/proposal.json').read_text())
raw = {x['case_id']: x for x in json.loads((L / 'inputs/raw-cases.json').read_text())}
es = json.loads((L / 'inputs/evidence-reused.json').read_text())
emap = {e['evidence_id']: e for e in es}
old_y = yaml.safe_load((L / 'inputs/predecessor.yaml').read_text())
before_y = yaml.safe_load((L / 'inputs/maintained-before.yaml').read_text())
assert sha(L / 'inputs/predecessor.yaml') == old_p['after_capture']['sha256']
assert sha(W / old_p['owner_path']) == old_p['before_sha256']
assert old_y['supplied_form'][5] == {
    'name': 'Bovine albumin, Fraction V',
    'notes': 'Exact source case 70; Fraction V explicitly stated; manufacturer/catalog and final ADC/OADC volume not established.'}

new_y = copy.deepcopy(old_y)
new_y['supplied_form'][5]['notes'] = (
    'Exact source case 70, CultureMech:008529: TOGO M194 BSK Medium, with original-source '
    'metadata JCM201, explicitly lists Bovine albumin, Fraction V as a 50 g batch input. '
    'Manufacturer/catalogue and exact final BSK preparation volume are not established; '
    'no 50 g/L concentration is asserted. The formulation is TOGO-provider-backed; the '
    'pinned JCM201 response contains no recipe. Source: ' + SOURCE_URL + '. '
    'Capture SHA256 84717c209dda5e9fc18a4ee5b1456ee655f243d31013b41b0d118ff17d03bdb9.'
)
event = record_curation_event(
    new_y,
    curator=AUTHOR + ' (W05 postseal isolated proposal)',
    action='CORRECTED_SOURCE_CONTEXT',
    changes=(
        'Resolve W06-TU-004 at ' + COMMENT_URL + ': replace the irrelevant ADC/OADC '
        'context in supplied_form[5].notes with TOGO M194/JCM201 BSK context. Preserve '
        'literal Fraction V and the source 50 g batch amount without inventing a final '
        'volume or 50 g/L concentration. All other supplied forms, identifiers, mapping '
        'evidence, synonyms, occurrence counts, prior history and holds are unchanged. '
        'This is an isolated W05 proposal, not a coordinator union or maintained write; '
        'JCM220/MediaDive3888 #1222 WITHHOLD and inherited A7030 claim limitations remain.'
    ),
    previous_status=old_y['mapping_status'], new_status=old_y['mapping_status'],
    llm_assisted=True, llm_model='gpt-6', timestamp=AT,
)
after_path = L / 'proposed/Bovine_Serum_Albumin.yaml'
assert not after_path.exists()
write_validated_ingredient(new_y, after_path, schema_path=W / 'src/mediaingredientmech/schema/mediaingredientmech.yaml')
assert yaml.safe_load(after_path.read_text()) == new_y
delta = changes(old_y, new_y)
assert [x['path'] for x in delta] == ['/curation_history/7', '/supplied_form/5/notes']
assert new_y['curation_history'][:-1] == old_y['curation_history']
diff = ''.join(difflib.unified_diff((L / 'inputs/predecessor.yaml').read_text().splitlines(True), after_path.read_text().splitlines(True), fromfile='sealed/W05-FINAL-MAT-007/Bovine_Serum_Albumin.yaml', tofile=PREFIX + 'proposed/Bovine_Serum_Albumin.yaml'))
(L / 'predecessor-to-successor.diff').write_text(diff)

conclusions = {
    11: 'TOGO M2879 and M2880 each explicitly list 2.5 g Bovine albumin fraction V in the ADC composition, separately from the 50 ml ADC receiving dose. Keep the existing Fraction V supplied-form context. The water input is not proof of exact final stock volume, and a named Difco supplement is not proof of a specific albumin catalogue. The M2879 provider table versus quoted study ADC/OADC conflict remains a source hold.',
    20: 'TOGO M1946 (original-source metadata NBRC1219) explicitly lists 50 g Bovine albumin (Fraction V) in the OADC preparation. Keep this separate from the 100 ml receiving dose. The listed 1 L water is a stock input, not an independently established exact final volume. Preserve the frozen TOGO-versus-NBRC main-water source-version distinction and the unknown albumin catalogue.',
    70: 'TOGO M194 is BSK Medium with original-source metadata JCM201. Its complete component table explicitly lists Bovine albumin, Fraction V, 50 g, as a main batch input. The recipe has 900 ml water, a 200 ml 7% gelatin input, 100 ml CMRL product and later final 6% rabbit-serum supplementation; these do not establish an exact final preparation volume. Correct only the irrelevant ADC/OADC wording to BSK context. Retain Fraction V, 50 g, unknown manufacturer/catalogue and unknown final volume; do not assert 50 g/L. The pinned JCM201 response says Nothing found, so it supplies no original-page corroboration.',
    118: 'TOGO M2407 explicitly lists 50 g Bovine Albumin (Fraction V) in the OADC Enrichment composition, separately from the 100 ml receiving dose. Preserve the grade and OADC scope. The water input is not an exact final stock volume, and the named Difco enrichment does not independently identify an albumin catalogue.',
    120: 'The preserved original M2400 and M2401 API records each list 2.5 g Bovine albumin fraction in their ADC composition, without a fraction number. Retain the unnumbered supplied form; neither the other Fraction V cases nor the ADC label licenses inserting V. The historical archive has a batch fetch timestamp, not exact per-row acquisition times. No successful current retrieval or catalogue identity is inferred.',
}
source_ids = {
    11: ['MATERIALS-CAP-a08fb341926e1d0a', 'MATERIALS-CAP-ee722a18f3e26939'],
    20: ['MATERIALS-CAP-b5dd8b92f4e4ea2c'],
    70: ['MATERIALS-CAP-776733f8ca9ff0a9', 'MATERIALS-ATTEMPT-d63e2a0487c298bb'],
    118: ['MATERIALS-CAP-4b8a987a15a1852d'],
    120: ['MATERIALS-ARCHIVE-M2400', 'MATERIALS-ARCHIVE-M2401'],
}
sources = []
for eid in dict.fromkeys(eid for ids in source_ids.values() for eid in ids):
    e = emap[eid]
    sources.append({
        'evidence_id': eid, 'capture': e['capture'], 'url': e.get('url'),
        'original_accessed_at': e.get('accessed_at'), 'timestamp_precision': e.get('timestamp_precision', 'Recorded source request timestamp; reused without a new remote request.'),
        'read_at': AT,
        'actual_read_scope': ('Retrieval-log entry 50 and complete linked HTML body; response says Nothing found, not positive recipe evidence.' if e['kind'] == 'unsuccessful_search' else 'Complete recipe component tables, source metadata and preparation comments; derived GMO role/property annotations are not new scientific evidence.'),
        'historical_source_bytes_unchanged': True,
    })
rows = []
for d in old_d:
    case = raw[d['case_id']]
    occs = []
    for o in case['occurrences']:
        f = C / o['full_recipe_snapshot']
        assert sha(f) == o['source_file_sha256']
        occs.append({
            'occurrence_id': o['occurrence_id'], 'recipe_id': o['recipe_id'],
            'component_path': o['component_path'], 'full_recipe_snapshot': {'root': 'source', 'path': o['full_recipe_snapshot'], 'sha256': sha(f)},
            'raw_component': o['raw_component'], 'recipe_source_identifiers': o['recipe_source_identifiers'],
            'actual_read_scope': 'Exact full BSA occurrence including its evidence; complete current ingredient/solution structure, source notes and preparation context. Historical changes and unrelated chemical groundings are preserved, not recertified.',
        })
    rows.append({
        'case_id': d['case_id'], 'case_index': d['case_index'], 'case_input_sha256': d['case_input_sha256'],
        'predecessor_decision_object_sha256': object_sha(d), 'proposal_id': old_p['proposal_id'],
        'assessment': conclusions[d['case_index']], 'source_evidence_ids': source_ids[d['case_index']],
        'occurrences': occs, 'scientific_change': d['case_index'] == 70,
        'boundaries': 'Source-specific supplied-form provenance only. No BSA-to-whole-medium identity, product equivalence, component coupling, role or export admission follows.',
    })
source_ledger = {
    'author': AUTHOR, 'assessed_at': AT, 'scope': 'Primary BSA context correction, not an independent review.',
    'case_count': 5, 'occurrence_count': 7, 'proposal_count': 1,
    'case_assessments': rows, 'source_captures': sources,
    'BSA_current_and_predecessor_full_reads': [capture('inputs/maintained-before.yaml'), capture('inputs/predecessor.yaml')],
    'raw_case_and_decision_full_reads': [capture('inputs/raw-cases.json'), capture('inputs/decisions.json'), capture('inputs/proposal.json')],
    'historical_time_distinction': 'The frozen M194 occurrence quotes a 2026-10-08T21:23:12.010583+00:00 capture; the independently retained W05 source request is 2026-11-08T05:08:10.564549+00:00. Both reference the identical 84717c... body. Neither timestamp is replaced by this local reread time.',
    'limits': [
        'No new remote source request was made for this historical source-context correction.',
        'The 29 inherited relevant evidence objects are retained exactly in inputs/evidence-reused.json; their hash check is not a new scientific approval of all linked historical reports.',
        'The current generic BSA owner and complete selected predecessor were read, but inherited A7030 processing/purity and generic family grounding are unchanged and not newly endorsed.',
        'The coordinator reconciled BSA union is not adopted. Its #1222 JCM220/MediaDive3888 WITHHOLD is a separate dependency and is not overwritten by this W05-only payload.',
        'Original source histories, all five frozen case boundaries and all seven occurrence IDs remain immutable. No additional campaign ownership is claimed.',
    ],
}
save('source-ledger.json', source_ledger)

new_e = [
    {
        'evidence_id': 'POSTSEAL-MATERIALS-BSK-PRIMARY',
        'capture': capture('captures/TOGO_M194-original.json'), 'kind': 'primary_source',
        'url': SOURCE_URL, 'accessed_at': emap['MATERIALS-CAP-776733f8ca9ff0a9']['accessed_at'],
        'locator': 'meta.name, meta.original_media_id; components[0].items[7]; complete component table and preparation comments',
        'supports_or_contradicts': conclusions[70], 'case_ids': [old_d[2]['case_id']],
        'original_evidence_id': 'MATERIALS-CAP-776733f8ca9ff0a9', 'local_reuse_at': AT,
        'supersedes_claim_only': 'The ADC/OADC context in predecessor supplied_form[5].notes; all prior capture bytes and records remain unchanged.',
    },
    {
        'evidence_id': 'POSTSEAL-MATERIALS-BSK-FILED-FINDING',
        'capture': capture('inputs/bsa-comment.json'), 'kind': 'source_snapshot',
        'url': COMMENT_URL, 'accessed_at': '2026-11-08T08:26:20.474545+00:00',
        'locator': 'Issue 1193 comment 6718748704, W06-TU-004; not primary scientific evidence',
        'supports_or_contradicts': 'The already filed bounded context defect requests BSK context, literal Fraction V, 50 g source amount, unknown final volume and preservation of #1222/A7030 limitations.',
        'case_ids': [old_d[2]['case_id']],
    },
    {
        'evidence_id': 'POSTSEAL-MATERIALS-BSA-ASSESSMENT',
        'capture': capture('source-ledger.json'), 'kind': 'source_snapshot',
        'locator': 'All five case_assessments, seven exact occurrences and source_captures',
        'supports_or_contradicts': 'Attributed primary interpretation of the BSA source contexts. Case 70 changes to BSK; the other four cases retain their source-qualified grade/unnumbered-fraction conclusions. This assessment is not independent approval.',
        'case_ids': [d['case_id'] for d in old_d],
    },
]
save('evidence.json', new_e)

new_d = copy.deepcopy(old_d)
for d, prior in zip(new_d, old_d):
    d['postseal_reassessment'] = {
        'author': AUTHOR, 'at': AT, 'finding_id': 'W06-TU-004',
        'predecessor_decision_object_sha256': object_sha(prior),
        'science_changed': d['case_index'] == 70,
        'scientific_conclusion': conclusions[d['case_index']],
        'historical_independent_review': copy.deepcopy(prior['independent_review']),
        'inherited_metadata_limit': 'Earlier reassessment, fragment hashes and final_assembly_provenance describe their historical versions. They are retained as lineage and do not bind or approve this changed whole payload.',
        'after_capture': capture('proposed/Bovine_Serum_Albumin.yaml'),
    }
    d['independent_review'] = {'status': 'pending', 'evidence_ids': [], 'scope': 'New whole BSA payload and all five linked cases require independent review; prior complete review remains historical only.'}
    d['evidence_ids'].append('POSTSEAL-MATERIALS-BSA-ASSESSMENT')
    if d['case_index'] == 70:
        d['reasoning'] = conclusions[70]
        d['applicability'] = 'Bound to CultureMech:008529, TOGO M194 BSK, occurrence CM_OCC:553f0c2bb6a0ed4037dcdff9eb7e97c2cbcd332c9d0ee7c301545ead26ab2f85 at ingredients/6. ' + conclusions[70]
        d['evidence_ids'].extend(['POSTSEAL-MATERIALS-BSK-PRIMARY', 'POSTSEAL-MATERIALS-BSK-FILED-FINDING'])
        d['issue_refs'].append(COMMENT_URL)
    else:
        assert d['reasoning'] == prior['reasoning'] and d['applicability'] == prior['applicability']
    for key in ['case_id', 'case_input_sha256', 'source', 'occurrence_ids', 'disposition', 'proposal_ids', 'owner_records', 'preserved_source_holds', 'preserved_downstream_holds']:
        assert d[key] == prior[key], key
save('decisions.json', new_d)

new_p = copy.deepcopy(old_p)
new_p['description'] = ('Retain the five source-specific BSA supplied forms on the existing generic owner, correcting only case 70 supplied_form[5].notes from ADC/OADC to TOGO M194/JCM201 BSK context, with literal Fraction V and 50 g batch input. Exact final volume and manufacturer/catalogue remain unknown. All other scientific payload fields are unchanged; one truthful history event is appended. This is a W05-only successor, not adoption or approval of the coordinator union.')
new_p['after_capture'] = capture('proposed/Bovine_Serum_Albumin.yaml')
new_p['evidence_ids'].extend(e['evidence_id'] for e in new_e)
new_p['postseal_predecessor'] = {
    'proposal_id': old_p['proposal_id'], 'proposal_object_sha256': object_sha(old_p),
    'base_head': '5156d92bec6bd885ca8bae3c5e18bfdce0069176',
    'after_capture': old_p['after_capture'], 'exact_local_copy': capture('inputs/predecessor.yaml'),
    'finding_id': 'W06-TU-004', 'issue_comment': COMMENT_URL,
    'changed_fields': ['/supplied_form/5/notes', '/curation_history/7'],
    'author': AUTHOR, 'at': AT,
    'conditional_integration_dependency': 'Keep the existing independently reviewed #1222 JCM220/MediaDive3888 WITHHOLD on any future coordinator union and preserve every other worker origin. This isolated W05 payload does not contain or supersede that union.',
}
new_p['independent_review'] = {'status': 'pending', 'evidence_ids': [], 'scope': 'Exact new full YAML and all five linked decisions; no historical review transfers to changed bytes.'}
save('proposals.json', [new_p])

save('lineage-and-diff.json', {
    'author': AUTHOR, 'at': AT, 'proposal_id': old_p['proposal_id'],
    'before_sha256': old_p['before_sha256'], 'predecessor_capture': old_p['after_capture'],
    'after_capture': new_p['after_capture'], 'semantic_delta': delta,
    'text_diff_capture': capture('predecessor-to-successor.diff'),
    'history_preserved_as_prefix': True, 'other_payload_fields_equal': True,
    'case_deltas': [{'case_id': d['case_id'], 'case_index': d['case_index'], 'before_object_sha256': object_sha(prior), 'after_object_sha256': object_sha(d), 'changes': changes(prior, d)} for prior, d in zip(old_d, new_d)],
    'proposal_metadata_delta': changes(old_p, new_p),
    'mapping_evidence_attribution': 'No MappingEvidence is added or retagged. This agent interpretation is disclosed in supplied-form notes, the LLM-assisted history and attributed primary assessment; inherited mapping evidence remains historical. Issue 1226 does not require inventing an ontology-mapping assertion for a context-only correction.',
    'native_guarded_writer': {'function': 'mediaingredientmech.validation.write_validated.write_validated_ingredient', 'schema_path': 'src/mediaingredientmech/schema/mediaingredientmech.yaml', 'schema_sha256': sha(W / 'src/mediaingredientmech/schema/mediaingredientmech.yaml'), 'status': 'passed'},
})
save('finding-dispositions.json', {
    'author': AUTHOR, 'at': AT, 'findings': [{
        'finding_id': 'W06-TU-004', 'filed_before_fix': COMMENT_URL,
        'status': 'primary correction prepared; independent review pending',
        'reproduction': {'capture': capture('inputs/predecessor.yaml'), 'pointer': '/supplied_form/5/notes', 'value': old_y['supplied_form'][5]['notes']},
        'remedy': {'capture': new_p['after_capture'], 'pointer': '/supplied_form/5/notes', 'value': new_y['supplied_form'][5]['notes']},
        'evidence_ids': [e['evidence_id'] for e in new_e],
        'limits': ['No 50 g/L or exact final volume.', 'No new supplier/catalogue identity.', 'No change to the other four BSA source cases.', '#1222 quantity WITHHOLD and A7030 processing/purity limits remain separate.', 'No owner, role, component or export admission.'],
    }], 'new_scientific_findings': []
})
save('native-targets-after.json', {'targets': [{
    'target_id': 'W05-POSTSEAL-BSA', 'path': str(after_path.relative_to(W)),
    'kind': 'source', 'record_class': 'Ingredient', 'label': 'bovine serum albumin',
    'selector': 'Complete W05-FINAL-MAT-007 successor; bounded source-context correction at supplied_form[5].notes',
    'ownership_note': 'Existing maintained owner data/ingredients/mapped/Bovine_Serum_Albumin.yaml; isolated report-only proposal, independent review pending.',
}]})
print(json.dumps({'cases': len(new_d), 'occurrences': sum(len(d['occurrence_ids']) for d in new_d), 'new_evidence': len(new_e), 'proposals': 1, 'after_sha256': sha(after_path), 'semantic_changed_paths': [x['path'] for x in delta]}))
