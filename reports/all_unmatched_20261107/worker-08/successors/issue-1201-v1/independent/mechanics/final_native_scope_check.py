"""Independent mechanical native scope and within-shard candidate inventory.

Run from the worker08 worktree. This writes only private reviewer output.
No scientific approval and no maintained mutation is performed.
"""
import collections
import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess
import unicodedata
from decimal import Decimal, InvalidOperation
import yaml

R = Path('reports/all_unmatched_20261107/worker-08')
S = R / 'successors/issue-1201-v1'
P = Path('.temp/all-unmatched-worker-08/issue-1201-v1')
V = P / 'vitamins_mixtures'
PARENT = '7efd3f8b98f9e822431dcb510c2c242a2569cfc7'
BASE = 'e000d66dd26ab053e9b17ce7bf8d3c873c3dde99'

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def read(p):
    return json.loads(Path(p).read_text())

def gitbytes(ref, path):
    return subprocess.check_output(['git', 'show', f'{ref}:{path}'])

def bind(p):
    return {'path': str(p), 'sha256': sha(p)}

proposals = read(S / 'proposals.json')['proposals']
parent = json.loads(gitbytes(PARENT, R / 'proposals.json'))['proposals']
pp = {p['proposal_id']: p for p in proposals}
old = {p['proposal_id']: p for p in parent}
assert len(pp) == len(proposals) == 113
assert len(old) == len(parent) == 46
common = set(pp) & set(old)
assert len(common) == 44
for pid in common:
    assert pp[pid] == old[pid], ('changed inherited row', pid)
expected = set(pp) - set(old)
assert len(expected) == 69
assert set(old) - set(pp) == {'if-reject-tris-hcl-on-base', 'vm-prop-new-60'}
inspection = read(P / 'native-inspection.json')
targetdoc = yaml.safe_load((P / 'native-targets.yaml').read_text())
review = yaml.safe_load((P / 'native-review.yaml').read_text())
assert inspection['targets'] == targetdoc['targets'] == review['targets']
assert inspection['source'] == review['source']
assert inspection['source']['git_revision'] == PARENT
assert review['reviewer']['independence'] == 'self_review'
assert review['verdict'] == 'pass_with_limitations'
assert review['scope']['coverage'] == 'full'
assert review['scope']['population_size'] == 69
assert set(review['scope']['reviewed_target_ids']) == expected
assert len(review['targets']) == 69
assert {t['target_id'] for t in review['targets']} == expected
assert len(review['assessments']) == 69
assert {tuple(a['target_ids']) for a in review['assessments']} == {(i,) for i in expected}
inputs = {i['path']: i for i in inspection['source']['inputs']}
assert len(inputs) == len(inspection['source']['inputs'])
for path, i in inputs.items():
    assert sha(path) == i['sha256'], ('stale native input', path)
assert {i['path'] for i in inputs.values() if i['role'] == 'target'} == {t['path'] for t in review['targets']}
contracts = read(S / 'provenance/current-contract-verification.json')['contracts']
for c in contracts:
    assert sha(c['contract']) == c['sha256'] == inputs[c['contract']]['sha256']
selection = read(P / 'final-selection.json')
proof = read(S / 'validation/peer-receipt-verification.json')
combined = read(S / 'validation/combined-validation.json')
saved_native = Path('reviews/structured') / review['review_id'] / 'review.yaml'
assert saved_native.read_bytes() == (P / 'native-review.yaml').read_bytes()
group_for = {}
for g in selection['groups']:
    assert g['primary_author'] != g['reviewer']
    for p in read(R / g['inputs']['proposals']['path'])['proposals']:
        assert p['proposal_id'] not in group_for
        group_for[p['proposal_id']] = g['name']
assert set(group_for) == expected
for a in review['assessments']:
    pid = a['target_ids'][0]
    assert 'peer-' + group_for[pid] in a['evidence_ids']
assert proof['configuration_sha256'] == sha(P / 'final-selection.json')
for obj, key in [(proof, 'final_input_hashes'), (combined, 'input_hashes')]:
    for path, h in obj[key].items():
        assert sha(path) == h == inputs[path]['sha256']
for e in review['evidence']:
    assert sha(e['reference']) == e['snapshot_sha256'], ('native evidence drift', e['evidence_id'])
for c in review['checks']:
    assert set(c['target_ids']) == expected
    if c['required']:
        assert c['status'] == 'passed'
    else:
        assert c['status'] == 'not_applicable'

aggregates = {}
for f in ['mapped_ingredients.yaml', 'unmapped_ingredients.yaml']:
    path = Path('data/curated') / f
    aggregates[str(path)] = yaml.safe_load(path.read_text())['ingredients']
rows = []
payloads = {}
for p in proposals:
    path = R / p['after_capture']['path']
    assert sha(path) == p['after_capture']['sha256']
    d = yaml.safe_load(path.read_text())
    payloads[p['proposal_id']] = d
    if p['kind'] == 'edit_existing_owner':
        assert sha(p['owner_path']) == p['before_sha256']
        assert hashlib.sha256(gitbytes(BASE, p['owner_path'])).hexdigest() == p['before_sha256']
    else:
        assert p['before_sha256'] is None
        # Direct filesystem existence includes ignored files; no gitignore-filtered search.
        assert not Path(p['owner_path']).exists()
for t in review['targets']:
    p = pp[t['target_id']]
    assert t['path'] == str(R / p['after_capture']['path'])
    assert inputs[t['path']]['sha256'] == p['after_capture']['sha256']
    assert t['kind'] == 'source' and t['record_class'] == 'IngredientRecord'
    row = {'target_id': t['target_id'], 'owner_path': p['owner_path'], 'payload': bind(t['path']), 'kind': p['kind'], 'before_sha256': p['before_sha256'], 'status': 'scope_and_bytes_verified'}
    if p['kind'] == 'edit_existing_owner':
        current = yaml.safe_load(Path(p['owner_path']).read_text())
        ownerpaths = {o['path']: o for o in t['owner_paths']}
        assert p['owner_path'] in ownerpaths
        assert inputs[p['owner_path']]['sha256'] == p['before_sha256']
        agg = 'data/curated/' + ('unmapped_ingredients.yaml' if '/unmapped/' in p['owner_path'] else 'mapped_ingredients.yaml')
        assert agg in ownerpaths
        assert f"identifier={current['identifier']}" in ownerpaths[agg]['role']
        matches = [x for x in aggregates[agg] if x['identifier'] == current['identifier']]
        assert any(x == current for x in matches), ('aggregate selector misses actual preimage', t['target_id'])
        row['actual_preimage_identifier'] = current['identifier']
    else:
        assert not t.get('owner_paths')
        assert p['owner_path'] in t['ownership_note']
        assert 'does not exist' in t['ownership_note'] and 'Proposed new owner only' in t['ownership_note']
    rows.append(row)

# A conservative text/quantity candidate screen, not chemical identity proof.
def name(s):
    s = unicodedata.normalize('NFKC', s or '').lower()
    return re.sub(r'[^a-z0-9]+', '', s)

def quantity(c):
    value, unit = c.get('concentration_value'), c.get('concentration_unit')
    if value is None:
        return None, unit
    try:
        value = Decimal(str(value))
        factor = Decimal(1)
        if unit == 'MG_PER_SOURCE_BATCH': factor, unit = Decimal('.001'), 'G_PER_SOURCE_BATCH'
        elif unit == 'L_PER_SOURCE_BATCH': factor, unit = Decimal('1000'), 'ML_PER_SOURCE_BATCH'
        elif unit == 'G_PER_BATCH': unit = 'G_PER_SOURCE_BATCH'
        elif unit == 'L_PER_BATCH': factor, unit = Decimal('1000'), 'ML_PER_SOURCE_BATCH'
        elif unit == 'ML_PER_BATCH': unit = 'ML_PER_SOURCE_BATCH'
        elif unit == 'MG_PER_L': factor, unit = Decimal('.001'), 'G_PER_L'
        elif unit == 'MILLIMOLAR': factor, unit = Decimal('.001'), 'M'
        elif unit == 'G_PER_100_ML': factor, unit = Decimal('10'), 'G_PER_L'
        elif unit == 'PERCENT_W_V': factor, unit = Decimal('10'), 'G_PER_L'
        return format((value * factor).normalize(), 'f'), unit
    except InvalidOperation:
        return str(value), unit

def signature(d):
    return sorted((name(c.get('component_name')), *quantity(c)) for c in d.get('components', []))

def bounded_alias(n):
    # Candidate-screen spellings only. Do not drop hydrate/stereochemical tokens.
    n = n.replace('hydrochloride', 'hcl')
    return {'calciumpantothenate': 'capantothenate',
            '4aminobenzoicacid': 'paminobenzoicacid'}.get(n, n)

def batch_ratio_signature(d):
    sig = signature(d)
    waters = [c for c in sig if c[0] == 'distilledwater' and c[2] == 'ML_PER_SOURCE_BATCH' and c[1] is not None]
    if len(waters) != 1 or Decimal(waters[0][1]) <= 0:
        return None
    denominator = Decimal(waters[0][1])
    out = []
    for n, val, unit in sig:
        if val is None or unit not in ['G_PER_SOURCE_BATCH', 'ML_PER_SOURCE_BATCH']:
            return None
        try:
            normalized = format((Decimal(val) / denominator).normalize(), 'f')
        except InvalidOperation:
            return None
        out.append((bounded_alias(n), normalized, unit.replace('PER_SOURCE_BATCH', 'PER_ML_LISTED_DISTILLED_WATER')))
    return sorted(out)

idgroups = collections.defaultdict(list)
siggroups = collections.defaultdict(list)
labels = collections.defaultdict(list)
ratios = collections.defaultdict(list)
for pid, d in payloads.items():
    idgroups[d['identifier']].append(pid)
    if d.get('components'):
        siggroups[json.dumps(signature(d), sort_keys=True)].append(pid)
        labels[json.dumps(sorted(name(c.get('component_name')) for c in d['components']))].append(pid)
        ratio = batch_ratio_signature(d)
        if ratio is not None:
            ratios[json.dumps(ratio)].append(pid)

def candidate(pids):
    return [{'proposal_id': pid, 'owner_path': pp[pid]['owner_path'], 'identifier': payloads[pid]['identifier'], 'payload': bind(R / pp[pid]['after_capture']['path']), 'case_ids': pp[pid]['case_ids'], 'component_assertion': payloads[pid].get('component_assertion'), 'components': payloads[pid].get('components'), 'notes': payloads[pid].get('notes'), 'source_context': pp[pid].get('source_scope', pp[pid]['description'])} for pid in pids]

result = {
    'at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'scope': 'Mechanical review of complete native scope, exact byte bindings and conservative within-shard dependency screen; not scientific reapproval of the reviewer\'s own proposals.',
    'bindings': [bind(P / f) for f in ['native-inspection.json', 'native-targets.yaml', 'native-review.yaml', 'final-selection.json']] + [bind(S / f) for f in ['proposals.json', 'assembly-provenance.json', 'provenance/current-contract-verification.json', 'validation/combined-validation.json', 'validation/peer-receipt-verification.json']] + [bind(saved_native)],
    'counts': {'active_proposals': len(pp), 'predecessor_proposals': len(old), 'unchanged_inherited': len(common), 'native_targets': len(rows), 'native_inputs_rehashed': len(inputs), 'edited_target_preimages': sum(r['kind'] == 'edit_existing_owner' for r in rows), 'new_target_paths_directly_checked_absent': sum(r['kind'] != 'edit_existing_owner' for r in rows), 'payloads_with_components': sum(bool(d.get('components')) for d in payloads.values())},
    'status': 'PASS_MECHANICAL_SCOPE', 'targets': rows,
    'native_input_hashes': inspection['source']['inputs'],
    'unchanged_inherited_ids': sorted(common),
    'superseded_predecessor_ids': sorted(set(old) - set(pp)),
    'repeated_primary_identifiers': [{'identifier': key, 'candidates': candidate(v)} for key, v in idgroups.items() if len(v) > 1],
    'normalized_component_quantity_matches': [{'signature': json.loads(key), 'candidates': candidate(v)} for key, v in siggroups.items() if len(v) > 1],
    'same_normalized_component_names_any_quantity': [{'signature': json.loads(key), 'candidates': candidate(v)} for key, v in labels.items() if len(v) > 1],
    'same_input_ratios_per_explicit_distilled_water': [{'signature': json.loads(key), 'candidates': candidate(v)} for key, v in ratios.items() if len(v) > 1],
    'ratio_screen_eligible_payload_count': sum(len(v) for v in ratios.values()),
    'screen_limits': 'All 113 active exact payloads read. Text normalization preserves component form words and digits but cannot prove identity or match every synonym. Quantities normalize specified mass/volume prefixes without inferring omitted batch volumes, carriers or ratio bases. Components of partial assertions do not define the complete material. Equal component lists flag candidates only, not duplicate-owner approval or an owner winner.'
}
out = V / 'final-native-scope-working.json'
out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
print(json.dumps({'status': result['status'], 'counts': result['counts'], 'duplicate_ids': [(x['identifier'], [c['proposal_id'] for c in x['candidates']]) for x in result['repeated_primary_identifiers']], 'same_signatures': [[c['proposal_id'] for c in x['candidates']] for x in result['normalized_component_quantity_matches']], 'same_names': [[c['proposal_id'] for c in x['candidates']] for x in result['same_normalized_component_names_any_quantity']], 'ratio_eligible': result['ratio_screen_eligible_payload_count'], 'same_ratios': [[c['proposal_id'] for c in x['candidates']] for x in result['same_input_ratios_per_explicit_distilled_water']]}))
