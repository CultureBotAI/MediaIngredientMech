"""Read-only final selection bridge; write new private receipts only.

Run from the W08 worktree with the maintained Python runtime and -B.
This is an accounting/readback successor to the sealed scientific review.
It does not recertify historical science or execute native validators.
"""
from pathlib import Path
import hashlib
import json
import datetime

W = Path.cwd()
A = W / 'reports/all_unmatched_20261107/worker-08'
O = A / 'successors/issue-1237-tenvit-v1'
OLD = A / 'successors/issue-1227-plain-flour-v1'
P = W / '.temp/all-unmatched-worker-08/tenvit-dependent-v1/independent-components'
checks = []
inputs = {}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    path = Path(path)
    data = path.read_bytes()
    inputs[str(path)] = digest(data)
    return data


def load(path):
    return json.loads(read(path))


def canon(obj):
    return digest(json.dumps(obj, sort_keys=True, separators=(',', ':'),
                             ensure_ascii=False, allow_nan=False).encode())


def check(name, condition, detail=None):
    checks.append({'name': name, 'passed': bool(condition), 'detail': detail})


def capture(cap):
    check('artifact capture root: ' + cap['path'], cap['root'] == 'artifact')
    data = read(A / cap['path'])
    check('artifact capture hash: ' + cap['path'], digest(data) == cap['sha256'])
    return data


def index(rows, key):
    out = {row[key]: row for row in rows}
    check('unique ' + key, len(out) == len(rows))
    return out


def differences(before, after):
    return [{'field': k, 'before': before.get(k), 'after': after.get(k)}
            for k in sorted(before.keys() | after.keys())
            if before.get(k) != after.get(k)]


selection = load(O / 'selection.json')
check('pinned final selection', inputs[str(O / 'selection.json')] ==
      'fb16bf5c29b981dc7dd60cf8d963a9aea25c12a65d6a0e55e29d84dfb2a26699')
old_selection = json.loads(capture(selection['predecessor_selection']))
for cap in selection['authoritative_inputs'].values():
    capture(cap)
for cap in old_selection['authoritative_inputs'].values():
    capture(cap)

new_dec = load(O / 'decisions.json')
old_dec = load(OLD / 'decisions.json')
new_prop = load(O / 'proposals.json')
old_prop = load(OLD / 'proposals.json')
new_evid = load(O / 'evidence.json')
old_evid = load(OLD / 'evidence.json')
lineage = load(O / 'lineage.json')
author_case = load(O / 'author/decision.json')
author_prop = load(O / 'author/proposal.json')
sealed_review = load(P / 'review.json')
sealed_ledger = load(P / 'source-read-ledger.json')
read(P / 'HANDOFF.json')
manifest_bytes = read(P / 'MANIFEST.sha256')
manifest_rows = []
for line in manifest_bytes.decode().splitlines():
    expected, name = line.split('  ', 1)
    actual = digest(read(P / name))
    check('sealed initial artifact preserved: ' + name, expected == actual)
    manifest_rows.append({'path': name, 'sha256': actual})
check('sealed initial manifest preserved', digest(manifest_bytes) ==
      '5b0da692c4fbd010a2732646ce7e7bf9471e6fc6beb5e0ed4f94c5f449d5bc80')

for label, now, old, rowkey in [
    ('decisions', new_dec, old_dec, 'decisions'),
    ('proposals', new_prop, old_prop, 'proposals'),
    ('evidence', new_evid, old_evid, 'evidence')]:
    check(label + ' envelope preserved',
          {k: v for k, v in now.items() if k != rowkey} ==
          {k: v for k, v in old.items() if k != rowkey})

dc = index(new_dec['decisions'], 'case_id')
odc = index(old_dec['decisions'], 'case_id')
pp = index(new_prop['proposals'], 'proposal_id')
opp = index(old_prop['proposals'], 'proposal_id')
ee = index(new_evid['evidence'], 'evidence_id')
oee = index(old_evid['evidence'], 'evidence_id')
lc = index(lineage['cases'], 'case_id')
lp = index(lineage['payloads'], 'proposal_id')
cid = selection['changed_case_id']
pid = selection['new_dependent_proposal']
check('188 cases, no new source case', len(dc) == 188 and dc.keys() == odc.keys())
check('case order preserved', list(dc) == list(odc))
check('114 proposals, only dependent addition', len(pp) == 114 and
      set(pp) - set(opp) == {pid} and set(opp).issubset(pp))
check('113 predecessor proposal order preserved', list(pp)[:113] == list(opp))
check('lineage complete case coverage', lc.keys() == dc.keys())
check('lineage complete proposal coverage', lp.keys() == pp.keys())

case_rows = []
for key, now in dc.items():
    old = odc[key]
    row = lc[key]
    expected_unchanged = key != cid
    check('case bridge ' + key, (now == old) == expected_unchanged)
    check('frozen source identity ' + key, all(now[k] == old[k] for k in
          ('case_id', 'case_input_sha256', 'source', 'occurrence_ids')))
    check('case lineage hash ' + key,
          row['before_sha256'] == canon(old) and row['after_sha256'] == canon(now)
          and row['unchanged'] == expected_unchanged
          and row['case_input_sha256'] == now['case_input_sha256']
          and row['occurrence_ids'] == now['occurrence_ids'])
    check('case evidence/proposal references ' + key,
          set(now['evidence_ids']).issubset(ee) and
          set(now['proposal_ids']).issubset(pp))
    case_rows.append({'case_id': key, 'before_sha256': canon(old),
                      'after_sha256': canon(now), 'unchanged': expected_unchanged,
                      'case_input_sha256': now['case_input_sha256'],
                      'occurrence_ids': now['occurrence_ids'],
                      'review_scope': 'exact predecessor object preservation' if
                      expected_unchanged else 'sealed science plus allowed metadata append'})

case_diff = differences(author_case, dc[cid])
prop_diff = differences(author_prop, pp[pid])
check('case only allowed metadata fields', {d['field'] for d in case_diff} ==
      {'evidence_ids', 'independent_review'})
check('proposal only evidence metadata field', {d['field'] for d in prop_diff} ==
      {'evidence_ids'})
check('author case evidence prefix preserved',
      dc[cid]['evidence_ids'][:len(author_case['evidence_ids'])] == author_case['evidence_ids'])
check('author proposal evidence prefix preserved',
      pp[pid]['evidence_ids'][:len(author_prop['evidence_ids'])] == author_prop['evidence_ids'])
expected_append = ['vm1237-source-partitions', 'vm1237-science', 'vm1237-skeptical'] + [
    f'vm1237-primary-{i:02d}' for i in range(10)]
check('case exact allowed evidence append',
      dc[cid]['evidence_ids'][len(author_case['evidence_ids']):] == expected_append)
check('proposal exact allowed evidence append',
      pp[pid]['evidence_ids'][len(author_prop['evidence_ids']):] == expected_append)
check('exact new peer status', dc[cid]['independent_review'] ==
      {'status': 'complete', 'evidence_ids': ['vm1237-science', 'vm1237-skeptical']})
check('sealed case scientific hash', sealed_review['case_hashes'][cid] == canon(author_case))
check('original peer provenance retained',
      dc[cid].get('prior_independent_reviews') == author_case.get('prior_independent_reviews'))

proposal_rows = []
for key, now in pp.items():
    data = capture(now['after_capture'])
    row = lp[key]
    check('proposal lineage capture ' + key,
          row['owner_path'] == now['owner_path'] and
          row['original_before_sha256'] == now['before_sha256'] and
          row['selected_capture'] == now['after_capture'])
    check('proposal evidence/case references ' + key,
          set(now['evidence_ids']).issubset(ee) and set(now['case_ids']).issubset(dc))
    old = opp.get(key)
    if old is not None:
        check('entire predecessor proposal preserved ' + key, now == old)
        check('old payload exact bytes ' + key, data == capture(old['after_capture']))
        check('unchanged lineage proof ' + key,
              row['original_proposal_object_sha256'] == canon(old) and
              row['unchanged_proposal_object'] is True and row['unchanged_payload'] is True)
    else:
        check('new dependent origin explicit', row['new_authentic_dependent_origin'] is True
              and row['unchanged_payload'] is False)
    proposal_rows.append({'proposal_id': key, 'owner_path': now['owner_path'],
                          'before_sha256': now['before_sha256'],
                          'proposal_object_sha256': canon(now),
                          'predecessor_proposal_object_sha256': canon(old) if old else None,
                          'after_capture': now['after_capture'],
                          'unchanged_predecessor_object_and_payload': old is not None,
                          'scope': 'mechanical preservation; no renewed science approval'
                          if old else 'sealed author-independent vitamin science'})
check('new payload bound to sealed science',
      sealed_review['payload_hashes'][pid] == pp[pid]['after_capture']['sha256'] ==
      selection['payload']['sha256'])
capture(selection['payload'])
check('real existing-owner preimage remains exact',
      digest(read(W / pp[pid]['owner_path'])) == pp[pid]['before_sha256'])
check('NBRC903 authentic new-owner origin unchanged',
      pp['vm1201-prop-nbrc903-vitamin'] == opp['vm1201-prop-nbrc903-vitamin'] and
      pp['vm1201-prop-nbrc903-vitamin']['before_sha256'] is None)

old_count = len(old_evid['evidence'])
check('1082 evidence prefix exact', old_count == 1082 and
      new_evid['evidence'][:old_count] == old_evid['evidence'])
suffix = new_evid['evidence'][old_count:]
check('1101 evidence with 19 additions', len(ee) == 1101 and len(suffix) == 19)
new_ids = {e['evidence_id'] for e in suffix}
check('all new evidence linked to changed case and proposal',
      new_ids.issubset(dc[cid]['evidence_ids']) and new_ids == set(pp[pid]['evidence_ids']))
for e in suffix:
    capture(e['capture'])
    check('new evidence exact case applicability ' + e['evidence_id'], e['case_ids'] == [cid])
for role, cap in selection['independent_reviews'].items():
    peer = json.loads(capture(cap))
    check('peer payload binding ' + role,
          peer['payload_hashes'][pid] == pp[pid]['after_capture']['sha256'])
    check('peer author-case binding ' + role, peer['case_hashes'][cid] == canon(author_case))
    check('peer complete and no blockers ' + role,
          peer['full_payload_review'] is True and peer['open_blocking_findings'] == [])
capture(selection['nominal_duplicate_reconciliation'])

ledger_by_path = {e['path']: e for e in sealed_ledger['entries']}
bindings = load(O / 'primary/capture-bindings.json')
check('ten copied primary captures', len(bindings) == 10)
primary_rows = []
for b in bindings:
    cap = b['published_capture']
    original = read(Path(b['original_path']))
    copied = capture(cap)
    prior = ledger_by_path[b['original_path']]
    current = ee[b['evidence_id']]
    check('original/copy/sealed hash ' + b['evidence_id'], original == copied and
          digest(original) == prior['sha256'] == cap['sha256'])
    check('primary capture exact evidence binding ' + b['evidence_id'], current['capture'] == cap)
    check('original acquisition time preserved ' + b['evidence_id'],
          prior['original_accessed_at'] == b['original_accessed_at'] ==
          current['original_acquisition_at'])
    check('original source URL preserved ' + b['evidence_id'],
          current['url'] == prior['original_url'])
    if current['kind'] == 'primary_source':
        check('primary accessed_at not restamped ' + b['evidence_id'],
              current['accessed_at'] == prior['original_accessed_at'])
    else:
        check('CB local snapshot no invented remote time',
              current['kind'] == 'source_snapshot' and current['url'] is None and
              'accessed_at' not in current)
    primary_rows.append({**b, 'original_sha256': digest(original),
                         'original_url': prior['original_url'],
                         'original_scientific_read_scope': prior['actual_read_scope'],
                         'readback_scope': 'Raw byte equality, capture linkage and original time; '
                                           'no new remote acquisition.'})

occ = [o for c in dc.values() for o in c['occurrence_ids']]
check('320 unique occurrence IDs preserved', len(occ) == len(set(occ)) == 320 and
      set(occ) == {o for c in odc.values() for o in c['occurrence_ids']})
counts = {'cases': len(dc), 'proposals': len(pp), 'occurrence_ids': len(set(occ)),
          'evidence': len(ee), 'unchanged_original_payloads': len(opp),
          'new_dependent_payloads': len(pp) - len(opp),
          'changed_cases': sum(dc[k] != odc[k] for k in dc),
          'unchanged_cases': sum(dc[k] == odc[k] for k in dc)}
check('selection counts reproduced', counts == selection['counts'])
check('lineage counts reproduced', [lineage[k] for k in
      ['case_count', 'proposal_count', 'occurrence_count',
       'unchanged_original_proposals_and_payloads', 'new_dependent_proposals',
       'unchanged_cases', 'changed_cases', 'original_evidence_prefix_preserved', 'evidence_count']]
      == [188, 114, 320, 113, 1, 187, 1, 1082, 1101])
check('no source occurrence is claimed as CB', selection['cb_campaign_occurrences'] == 0
      and pp[pid]['cb_campaign_occurrence_count'] == 0 and len(pp[pid]['source_occurrence_ids']) == 1)
check('no application or role/export approval',
      selection['maintained_application'] is False and
      selection['whole_owner_role_export_approval'] is False and
      lineage['release_approval'] is False and
      selection['prior_TSB_Bacto_admission'] == 'FAILED/HELD unchanged')

for name, old_sha in list(inputs.items()):
    check('input stable through readback: ' + name, digest(Path(name).read_bytes()) == old_sha)

failures = [c for c in checks if not c['passed']]
stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
receipt = {
    'reviewer': '/root/organics', 'author': '/root', 'worker': 'worker08',
    'completed_at': stamp, 'status': 'PASS' if not failures else 'FAIL',
    'scope': 'Final-index mechanical readback and exact rebind to separately sealed scientific review. '
             'The 113 unchanged payloads and 187 unchanged cases receive preservation checks only, '
             'not new scientific approval. Historical organic authorship is excluded from self-approval.',
    'scientific_review_receipt': {'path': str(P / 'review.json'),
                                 'sha256': digest((P / 'review.json').read_bytes())},
    'selection': {'path': str(O / 'selection.json'), 'sha256': inputs[str(O / 'selection.json')]},
    'counts': counts, 'checks_total': len(checks), 'checks_passed': len(checks) - len(failures),
    'failures': failures, 'new_findings': [], 'input_hashes': inputs,
    'case_hashes': {k: canon(v) for k, v in dc.items()},
    'payload_hashes': {k: v['after_capture']['sha256'] for k, v in pp.items()},
    'author_to_final_case_metadata_delta': case_diff,
    'author_to_final_proposal_metadata_delta': prop_diff,
    'evidence_prefix': {'preserved_count': old_count, 'added_count': len(suffix),
                        'exact_predecessor_objects': True, 'addition_ids': [e['evidence_id'] for e in suffix]},
    'primary_captures': primary_rows,
    'preserved_initial_manifest': {'path': str(P / 'MANIFEST.sha256'),
                                   'sha256': digest(manifest_bytes), 'entries': manifest_rows},
    'case_reviews': case_rows, 'proposal_reviews': proposal_rows,
    'limits_and_remaining_holds': [
        'No native/schema/SSSOM/Claw checks were rerun by this accounting task; native assembly remains separate.',
        'Nine CB catalog references retain source-compatible identity only; calcium pantothenate D/DL stays UNMAPPED.',
        'CB cyanocobalamin is not substituted for generic JCM/NBRC vitamin B12; X100 is not applied as a quantity multiplier.',
        'The NBRC903 occurrence alone triggers a comparator correction, with zero CB campaign occurrences.',
        'Original NBRC903 null-before proposal and all other 113 predecessor payloads are unchanged reconciliation inputs.',
        'W08 NBRC903 and W06 JCM197 nominal duplicate reconciliation remains central; no owner installation or winner selected.',
        'All inherited scientific, alias, role, source, application and export holds remain, including TSB/Bacto FAILED/HELD.',
        'No unrelated case or complete child owner receives scientific approval; coordinator final-head acceptance remains pending.'
    ],
    'inspection_limitations': [
        "An exploratory console read assumed lineage key 'proposals' and raised KeyError; actual key 'payloads' was then read. No artifact was changed or validation claim based on that failed exploration.",
        'Prior large console lineage output was truncated. This script parses every case/payload lineage row and records explicit per-ID checks; it does not claim fresh narrative scientific review of unchanged rows.'
    ],
    'no_remote_retrieval': True, 'no_native_rerun': True,
    'no_maintained_or_prior_artifact_writes': True,
    'final_native_assembly_review': 'not yet requested or performed'
}
for name, value in [('final-bindings-checks.json', {'checks': checks, 'failed': failures}),
                    ('final-bindings.json', receipt)]:
    with (P / name).open('x') as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False, allow_nan=False)
        stream.write('\n')
print(json.dumps({'status': receipt['status'], 'checks': len(checks), 'failed': failures,
                  'counts': counts, 'receipt_sha256': digest((P / 'final-bindings.json').read_bytes())}, indent=2))
raise SystemExit(bool(failures))
