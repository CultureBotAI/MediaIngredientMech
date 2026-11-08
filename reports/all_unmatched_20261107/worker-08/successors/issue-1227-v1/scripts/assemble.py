"""2026-11-08: assemble exact reviewed W08 corrections; never curate records.

Inputs are immutable parent indices, three disjoint author packets and separate
peer receipts. Output is a new full successor selection, with original case and
owner beforeimages. This helper proves accounting, not scientific correctness.
"""
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path.cwd()
ARTIFACT = ROOT / 'reports/all_unmatched_20261107/worker-08'
OUT = ARTIFACT / 'successors/issue-1227-v1'
SELECTION = OUT / 'final-v2'
SELECTION_CONFIG = OUT / 'provenance/final-selection-v2.json'


def read(path):
    return json.loads(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def digest(row):
    return hashlib.sha256(json.dumps(row, sort_keys=True, separators=(',', ':'),
                                    ensure_ascii=False, allow_nan=False).encode()).hexdigest()


def unique(rows, key):
    result = {r[key]: r for r in rows}
    assert len(result) == len(rows), ('duplicate', key)
    return result


def checked_capture(ref, root):
    assert ref['root'] == 'artifact'
    rel = Path(ref['path'])
    assert not rel.is_absolute() and '..' not in rel.parts, 'unsafe capture path'
    p = root / rel
    assert not any(q.is_symlink() for q in [p, *p.parents] if q != root.parent), 'symlink capture'
    assert sha(p) == ref['sha256'], ('capture hash', str(p))
    return p


def assemble(parent, groups, artifact=ARTIFACT, root_evidence=()):
    old_d = unique(parent['decisions']['decisions'], 'case_id')
    old_p = unique(parent['proposals']['proposals'], 'proposal_id')
    evidence = copy.deepcopy(parent['evidence']['evidence'])
    ev = unique(evidence, 'evidence_id')
    for e in root_evidence:
        assert e['evidence_id'] not in ev, 'duplicate root evidence'
        checked_capture(e['capture'], artifact)
        evidence.append(copy.deepcopy(e)); ev[e['evidence_id']] = e
    decisions, proposals, covered, prop_covered, provenance = {}, {}, set(), set(), []
    for g in groups:
        assert g['author'] != g['reviewer'], 'self review'
        ds = unique(g['decisions'], 'case_id')
        ps = unique(g['proposals'], 'proposal_id')
        assert set(ds) == set(g['case_ids']), 'author case coverage'
        assert set(ps) == set(g['proposal_ids']), 'author payload coverage'
        assert set(ds) <= set(old_d) and not set(ds) & covered, 'case overlap/out of scope'
        assert set(ps) <= set(old_p) and not set(ps) & prop_covered, 'payload overlap/out of scope'
        peer = g['peer']
        assert peer['reviewer'] == g['reviewer'] and peer['author'] == g['author'], 'peer identity'
        assert set(peer['case_ids']) == set(ds), 'peer case coverage'
        assert set(peer['proposal_ids']) == set(ps), 'peer payload coverage'
        assert peer['open_blocking_findings'] == [], 'unresolved peer finding'
        assert peer['full_payload_review'] is True, 'delta-only peer review'
        for ref in g['bound_inputs']:
            checked_capture(ref, artifact)
        for ref in g.get('inputs', {}).values():
            assert peer['input_hashes'].get(ref['path']) == ref['sha256'], ('peer input binding', ref['path'])
        checked_capture(g['peer_capture'], artifact)
        for e in g['evidence']:
            if e['evidence_id'] in ev:
                assert e == ev[e['evidence_id']], ('mutated inherited evidence', e['evidence_id'])
            else:
                evidence.append(copy.deepcopy(e)); ev[e['evidence_id']] = e
        eid = 'w08-1227-peer-' + g['name']
        assert eid not in ev
        e = dict(evidence_id=eid, kind='independent_review', capture=g['peer_capture'], url=None,
                 locator='Whole-payload and complete source-outcome review; exact final input hashes and case/payload assessments',
                 supports_or_contradicts=f"{g['reviewer']} independently assessed {g['author']}'s complete selected payloads and source outcomes. Bounded proposals only; no whole-owner release, role, source-hold or cross-shard acceptance.",
                 case_ids=list(ds))
        evidence.append(e); ev[eid] = e
        for cid, row in ds.items():
            old = old_d[cid]
            for key in ['source', 'case_input_sha256', 'occurrence_ids', 'preserved_native_decisions']:
                assert row.get(key) == old.get(key), ('frozen case/hold mutation', cid, key)
            assert set(old['proposal_ids']) <= set(row['proposal_ids']), ('lost original proposal backlink', cid)
            assert peer['case_hashes'][cid] == digest(row), ('stale peer case', cid)
            row = copy.deepcopy(row)
            row['prior_independent_reviews'] = [old['independent_review']]
            row['independent_review'] = dict(status='complete', evidence_ids=[eid])
            decisions[cid] = row
        for pid, row in ps.items():
            old = old_p[pid]
            for key in ['owner_path', 'kind', 'before_sha256']:
                assert row[key] == old[key], ('owner beforeimage mutation', pid, key)
            assert set(old['case_ids']) <= set(row['case_ids']) <= set(ds), ('lost/outside proposal cases', pid)
            checked_capture(row['after_capture'], artifact)
            assert peer['payload_hashes'][pid] == row['after_capture']['sha256'], ('stale peer payload', pid)
            proposals[pid] = copy.deepcopy(row)
        covered |= set(ds); prop_covered |= set(ps)
        provenance.append({k: g[k] for k in ['name', 'author', 'reviewer', 'case_ids', 'proposal_ids', 'bound_inputs', 'peer_capture']})
    assert covered == set(old_d), 'missing cases'
    assert prop_covered == set(old_p), 'missing payloads'
    assert len({p['owner_path'] for p in proposals.values()}) == len(proposals), 'duplicate owner'
    for pid, p in proposals.items():
        assert set(p['case_ids']) == {cid for cid, d in decisions.items() if pid in d['proposal_ids']}, ('backlink mismatch', pid)
        assert set(p['evidence_ids']) <= set(ev), ('unknown proposal evidence', pid)
    for cid, d in decisions.items():
        assert set(d['proposal_ids']) <= set(proposals), ('unknown proposal', cid)
        assert set(d['evidence_ids']) <= set(ev), ('unknown case evidence', cid)
    changes = [dict(proposal_id=pid, predecessor=old_p[pid]['after_capture'], successor=p['after_capture'],
                    payload_changed=p['after_capture']['sha256'] != old_p[pid]['after_capture']['sha256'],
                    original_before_sha256=p['before_sha256'], case_ids=p['case_ids']) for pid, p in proposals.items()]
    ddoc = copy.deepcopy(parent['decisions']); ddoc['decisions'] = [decisions[c] for c in old_d]
    return {'decisions.json': ddoc, 'proposals.json': dict(schema_version=1, proposals=[proposals[p] for p in old_p]),
            'evidence.json': dict(schema_version=1, evidence=evidence),
            'assembly-provenance.json': dict(parent_head='b90a2fd4681d20e2586481b7b9b1114a78281b94', groups=provenance,
                payload_selection=changes, cases=len(decisions), proposals=len(proposals), evidence=len(evidence),
                changed_payloads=sum(x['payload_changed'] for x in changes),
                unchanged_payloads=sum(not x['payload_changed'] for x in changes),
                approval_boundary='Isolated scientifically reviewed proposals with explicit holds. Coordinator final-head and cross-shard review required; no release approval.')}


def main():
    config = read(SELECTION_CONFIG)
    parent = {}
    for name, ref in config['parent_inputs'].items():
        parent[name] = read(checked_capture(ref, ARTIFACT))
    groups = []
    for g in config['groups']:
        item = copy.deepcopy(g)
        for name in ['decisions', 'proposals', 'evidence']:
            doc = read(checked_capture(g['inputs'][name], ARTIFACT))
            item[name] = doc[name] if isinstance(doc, dict) else doc
        item['peer'] = read(checked_capture(g['peer_capture'], ARTIFACT))
        groups.append(item)
    root_evidence = read(checked_capture(config['root_evidence'], ARTIFACT))['evidence'] if config.get('root_evidence') else []
    results = assemble(parent, groups, root_evidence=root_evidence)
    assert results['assembly-provenance.json']['cases'] == 188
    assert results['assembly-provenance.json']['proposals'] == 113
    SELECTION.mkdir(exist_ok=False)
    for name in results:
        assert not (SELECTION / name).exists(), ('immutable output exists', name)
    for name, doc in results.items():
        (SELECTION / name).write_text(json.dumps(doc, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps({k: v for k, v in results['assembly-provenance.json'].items() if k not in ['groups', 'payload_selection']}))


if __name__ == '__main__':
    main()
