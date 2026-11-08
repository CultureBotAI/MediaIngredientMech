#!/usr/bin/env python3
"""Read-only full first-wins replay for assigned W04 biological MediaDive cases. Independently run by /root/materials; adapted with attribution from W04 chemistry replay and published W09 follow-up replay_lineage.py. New private inputs and outputs only.

Only --write emits files, and only below this script's provenance directory.
No KG imports, network calls, cache deserialization, builds or maintained writes.
"""
from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from datetime import datetime, timezone
from typing import Dict

HERE = Path(__file__).resolve().parent
FOLLOWUP = HERE.parent
REPO = next(p for p in HERE.parents if (p / 'MAPPING_SEMANTICS.md').exists())
AUDIT = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5/inputs/kg-source-audit')
KG = Path('/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe-mim-1788-20261107')
GEN_REL = 'data/raw/mediadive/generations/resolution-admitted-r2'
GEN = KG / GEN_REL
FROZEN = AUDIT / 'snapshots' / GEN_REL
SHA = lambda b: hashlib.sha256(b).hexdigest()
CANON = lambda o: json.dumps(o, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode()
WRITE = '--write' in sys.argv
INPUTS, COPIES = {}, {}


def read(path, expected=None):
    path = Path(path)
    b = path.read_bytes()
    meta = {'path': str(path), 'bytes': len(b), 'sha256': SHA(b)}
    if expected:
        assert all(meta[k] == v for k, v in expected.items() if k in ('bytes', 'sha256')), (str(path), expected, meta)
    INPUTS[str(path)] = meta
    return b


def emit(name, value, raw=False):
    b = value if raw else json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False).encode() + b'\n'
    if WRITE:
        dest = HERE / name
        assert dest.resolve().is_relative_to(HERE)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(b)
    COPIES[name] = {'bytes': len(b), 'sha256': SHA(b)}


def checked_member(name):
    assert not Path(name).is_absolute() and '..' not in Path(name).parts
    return read(GEN / name, manifest['files'][name])


def source_file(relative, functions):
    b = read(KG / relative)
    committed = subprocess.check_output(['git', '-C', str(KG), 'show', revision + ':' + relative])
    assert b == committed, ('producer differs from frozen audit revision', relative)
    tree = ast.parse(b)
    nodes = [n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name in functions]
    assert {n.name for n in nodes} == set(functions)
    emit('captures/code/' + Path(relative).name, b, raw=True)
    return b, tree, [{'function': n.name, 'start_line': n.lineno, 'end_line': n.end_lineno} for n in nodes]


audit_bytes = read(AUDIT / 'source-manifest.json')
audit = json.loads(audit_bytes)
revision = audit['upstream_revision']
assert subprocess.check_output(['git', '-C', str(KG), 'rev-parse', 'HEAD']).decode().strip() == revision
cases = [c for c in json.loads(read(HERE.parents[2] / 'scopes/biological.json'))['source_cases'] if c['source'] == 'mediadive']
assert len(cases) == 11
frozen_manifest = read(FROZEN / 'manifest.json', audit['files']['snapshots/' + GEN_REL + '/manifest.json'])
manifest = json.loads(frozen_manifest)
assert read(GEN / 'manifest.json') == frozen_manifest
pointer = json.loads(read(AUDIT / 'snapshots/data/raw/mediadive/current.json', audit['files']['snapshots/data/raw/mediadive/current.json']))
assert pointer['manifest_sha256'] == SHA(frozen_manifest)
assert manifest['qualification']['admissible'] is True
assert manifest['qualification']['recipe_coverage_complete'] is True
assert json.loads(read(GEN / 'seal.json'))['manifest_sha256'] == SHA(frozen_manifest)
emit('captures/frozen-source-manifest.json', audit_bytes, raw=True)
emit('captures/admitted-generation-manifest.json', frozen_manifest, raw=True)
emit('captures/current-pointer.json', CANON(pointer) + b'\n', raw=True)

compound_bytes = checked_member('compounds.json')
assert compound_bytes == read(FROZEN / 'compounds.json', audit['files']['snapshots/' + GEN_REL + '/compounds.json'])
compounds = json.loads(compound_bytes)
emit('captures/compounds.json', compound_bytes, raw=True)
candidates = json.loads(read(AUDIT / 'queues/source-candidates.json', audit['files']['queues/source-candidates.json']))
for case in cases:
    matches = [c for c in candidates if c['candidate_id'] == case['original_kg_entry']['candidate_id']]
    assert len(matches) == 1 and case['case_id'] == 'KG_CASE:' + matches[0]['candidate_id']
    assert all(case['original_kg_entry'][k] == v for k, v in matches[0].items())
details = json.loads(checked_member('media_detailed.json'))
solutions = json.loads(checked_member('solutions.json'))
catalogue = json.loads(checked_member('catalogue.json'))
states = json.loads(checked_member('endpoint-outcomes.json'))['endpoints']
assert catalogue['status'] == 200 and catalogue['count'] == len(catalogue['data'])
ordered_ids = [str(row['id']) for row in catalogue['data']]
assert len(ordered_ids) == len(set(ordered_ids))
assert list(details) == ordered_ids
emit('captures/catalogue-ordered-ids.json', ordered_ids)

code = {}
b, tree, locations = source_file('kg_microbe/utils/mediadive_bulk_download.py', ['extract_compounds_from_media', 'extract_solutions_from_media'])
code['bulk'] = {'source': str(KG / 'kg_microbe/utils/mediadive_bulk_download.py'), 'sha256': SHA(b), 'functions': locations}
names = {'SOLUTIONS_KEY', 'RECIPE_KEY', 'COMPOUND_ID_KEY', 'ID_KEY'}
definitions = [n for n in tree.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id in names for t in n.targets)]
definitions += [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in {'extract_compounds_from_media', 'extract_solutions_from_media'}]
namespace = {'Dict': Dict}
exec(compile(ast.Module(body=definitions, type_ignores=[]), code['bulk']['source'], 'exec'), namespace)
replayed_compounds = namespace['extract_compounds_from_media'](details)
replayed_solutions = namespace['extract_solutions_from_media'](details)
assert CANON(replayed_compounds) == CANON(compounds)
assert list(replayed_compounds) == list(compounds)
assert CANON(replayed_solutions) == CANON(solutions)
assert list(replayed_solutions) == list(solutions)
for relative, funcs, key in [
    ('kg_microbe/transform_utils/mediadive/acquisition.py', ['_native_payloads', '_rebuild_staging', 'checkpoint_generation'], 'acquisition'),
    ('kg_microbe/transform_utils/mediadive/endpoint_outcomes.py', ['catalogue_scope', 'classify_observation', '_import_source', 'replay', 'validate_native'], 'outcomes'),
    ('scripts/dump_unmapped_mediadive_ingredients.py', ['iter_unmapped_rows', 'main'], 'queue'),
]:
    b, _, locations = source_file(relative, funcs)
    code[key] = {'source': str(KG / relative), 'sha256': SHA(b), 'functions': locations}

# Check latest ledger binding and each retained medium body, not just the target body.
ledger = checked_member('observations.jsonl').splitlines()
latest, previous = {}, None
for number, line in enumerate(ledger, 1):
    event = json.loads(line)
    assert event['sequence'] == number and event['previous_observation_id'] == previous
    assert event['observation_id'] == SHA(CANON({k: v for k, v in event.items() if k != 'observation_id'}))
    latest[event['url']] = event
    previous = event['observation_id']
body_bindings = []
for ident in ordered_ids:
    url = 'https://mediadive.dsmz.de/rest/medium/' + ident
    event, state = latest[url], states[url]
    assert state['state'] == 'nonempty' and state['observation_id'] == event['observation_id']
    assert event['request']['method'] == 'GET' and event['request']['url'] == event['url'] == event['response']['url'] == url
    assert event['response']['status'] == 200 and state['body_sha256'] == event['body']['sha256']
    body = checked_member(event['body']['path'])
    assert SHA(body) == event['body']['sha256'] and len(body) == event['body']['bytes']
    payload = json.loads(body)
    assert payload['status'] == 200 and str(payload['data']['medium']['id']) == ident
    assert CANON(payload['data']) == CANON(details[ident])
    body_bindings.append({'medium_id': ident, 'url': url, 'body_sha256': SHA(body), 'observation_id': event['observation_id']})
emit('captures/all-medium-body-bindings.json', body_bindings)

locators, all_matches = {}, {str(c['original_kg_entry']['source_record']['compound_id']): [] for c in cases}
for medium_index, (medium_key, medium) in enumerate(details.items()):
    for solution_index, solution in enumerate(medium.get('solutions', [])):
        for recipe_index, row in enumerate(solution.get('recipe', [])):
            key = str(row.get('compound_id'))
            if key not in all_matches:
                continue
            match = {'medium_key': medium_key, 'medium_catalogue_index_zero_based': medium_index, 'medium_id': medium['medium']['id'], 'solution_id': solution['id'], 'solution_name': solution['name'], 'solution_index_zero_based': solution_index, 'recipe_index_zero_based': recipe_index, 'recipe_order': row.get('recipe_order'), 'identical_to_flattened_json_value': CANON(row) == CANON(compounds[key]), 'source_row_canonical_sha256': SHA(CANON(row))}
            all_matches[key].append(match)
            locators.setdefault(key, match)
emit('captures/all-target-occurrences.json', all_matches)

associations = []
for case in cases:
    source = case['original_kg_entry']
    key = str(source['source_record']['compound_id'])
    assert source['source_id'] == case['source_case_id'] == 'mediadive.ingredient:' + key
    assert CANON(source['source_record']) == CANON(compounds[key])
    loc = locators[key]
    assert loc['identical_to_flattened_json_value']
    url = 'https://mediadive.dsmz.de/rest/medium/' + loc['medium_key']
    event = latest[url]
    event_path = f"events/{event['sequence']:08d}-{event['observation_id']}.json"
    event_bytes = checked_member(event_path)
    assert json.loads(event_bytes) == event
    imported = event['source']
    original_ledger = checked_member(imported['ledger']).splitlines()
    original_line = original_ledger[imported['line'] - 1]
    assert SHA(original_line) == imported['line_sha256']
    original = json.loads(original_line)
    assert original['request_url'] == url and original['observed_at'] == event['observed_at']
    assert original['body_sha256'] == event['body']['sha256']
    body = checked_member(event['body']['path'])
    emit(f"captures/original-medium-{loc['medium_key']}.body", body, raw=True)
    # Session-bearing request headers are deliberately not republished. Hashes bind the originals.
    emit(f"captures/original-medium-{loc['medium_key']}-event-redacted.json", {**{k: v for k, v in event.items() if k != 'request'}, 'request': {'method': event['request']['method'], 'url': event['request']['url'], 'headers': '[OMITTED: source request headers not needed for scientific attribution]'}, 'redaction': {'original_path': str(GEN / event_path), 'original_sha256': SHA(event_bytes), 'original_ledger_line_sha256': SHA(original_line)}})
    emit(f"captures/original-medium-{loc['medium_key']}-formatted.json", json.loads(body))
    equal = [x for x in all_matches[key] if x['identical_to_flattened_json_value']]
    associations.append({'case_id': case['case_id'], 'source_id': case['source_case_id'], 'source_row': source['source_record'], 'canonical_source_row_sha256': SHA(CANON(source['source_record'])), 'locator': loc, 'json_pointer_in_original_response': f"/data/solutions/{loc['solution_index_zero_based']}/recipe/{loc['recipe_index_zero_based']}", 'url': url, 'observed_at': event['observed_at'], 'body_sha256': event['body']['sha256'], 'event_path': str(GEN / event_path), 'event_sha256': SHA(event_bytes), 'imported_original_ledger_path': str(GEN / imported['ledger']), 'imported_original_ledger_line': imported['line'], 'imported_original_ledger_line_sha256': SHA(original_line), 'provider_medium_metadata': details[loc['medium_key']]['medium'], 'all_occurrences_in_admitted_embedded_media': len(all_matches[key]), 'identical_value_matches': len(equal), 'distinct_solution_ids_among_identical_value_matches': len({x['solution_id'] for x in equal}), 'conclusion': 'Exact selected recipe-row provenance reconstructed by admitted first-wins extraction order, not by amount similarity.'})

emit('source-associations.json', {'scope':'All assigned W04 MediaDive flattened rows; source provenance only, no identity release','associations':associations,'producer_code':code,'limitation':'Full first-wins extraction replay; matching amount alone is not unique source proof. No source or owner hold lifted.'})
emit('input-hashes.json',{'checked_at':datetime.now(timezone.utc).isoformat(),'files':list(INPUTS.values())})
result={'status':'PASS','upstream_revision':revision,'admitted_generation_manifest_sha256':SHA(frozen_manifest),'catalogue_media_count':len(ordered_ids),'raw_medium_bodies_verified':len(body_bindings),'compound_rows_replayed':len(compounds),'solution_rows_replayed':len(solutions),'exact_case_count':len(associations),'source_associations_sha256':COPIES['source-associations.json']['sha256'],'script_sha256':SHA(Path(__file__).read_bytes())}
emit('replay-validation.json',result)
print(json.dumps(result,indent=2))
for a in associations:print(a['source_id'],a['locator'],a['observed_at'])
