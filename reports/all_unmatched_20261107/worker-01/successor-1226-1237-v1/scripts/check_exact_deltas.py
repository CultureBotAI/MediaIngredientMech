"""Independent read-only full object allowlist, prefix and negative-control audit."""
import copy
import datetime
import hashlib
import json
from pathlib import Path
import re
import sys

import yaml

D = Path(__file__).resolve().parents[1]
W = Path(__file__).resolve().parents[5]


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def locate(record, selector):
    match = re.fullmatch(r'ontology_mapping\.evidence\[(\d+)\]', selector)
    assert match, selector
    return record['ontology_mapping']['evidence'][int(match.group(1))]


def diff(a, b, prefix=''):
    if type(a) != type(b):
        return [{'path': prefix, 'old': a, 'new': b}]
    if isinstance(a, dict):
        out = []
        for key in sorted(a.keys() | b.keys()):
            path = f'{prefix}.{key}' if prefix else key
            if key not in a or key not in b:
                out.append({'path': path, 'old': a.get(key), 'new': b.get(key)})
            else:
                out.extend(diff(a[key], b[key], path))
        return out
    if isinstance(a, list):
        if len(a) != len(b):
            return [{'path': prefix, 'old': a, 'new': b}]
        return [d for i, (x,y) in enumerate(zip(a,b)) for d in diff(x,y,f'{prefix}[{i}]')]
    return [] if a == b else [{'path': prefix, 'old': a, 'new': b}]


def expect_before(old, row):
    assert locate(old, row['field']) == row['full_value'], ('stale full object', row['audit_row_id'])
    assert row['classification'] == 'new_agent_record'
    assert row['suggested_native_type'] == 'LLM_SUGGESTION'
    assert locate(old, row['field'])['evidence_type'] == 'MANUAL_CURATION'


def core_comparison(old, new, rows):
    """Only exact enumerated enum changes plus one truthful new event may differ."""
    expected = copy.deepcopy(old)
    for row in rows:
        expect_before(old, row)
        locate(expected, row['field'])['evidence_type'] = 'LLM_SUGGESTION'
    old_history = old.get('curation_history', [])
    new_history = new.get('curation_history', [])
    assert new_history[:-1] == old_history and len(new_history) == len(old_history)+1, 'history prefix/count'
    event = new_history[-1]
    assert event['llm_assisted'] is True and '1226' in event['changes'] and 'Codex' in event['curator']
    expected['curation_history'] = new_history
    return diff(expected, new)


def reject(fn):
    try:
        fn()
    except (AssertionError, KeyError, IndexError):
        return True
    return False


def main():
    output = Path(sys.argv[1])
    assert not output.exists()
    a = json.loads((D/'inputs/w01-full-provenance-allowlist-v2.json').read_text())
    b = json.loads((D/'inputs/current-worker-bindings.json').read_text())
    w = next(r for r in b['workers'] if r['worker'] == 1)
    grouped = {}
    for row in a['rows']:
        grouped.setdefault(row['proposal_id'], []).append(row)
    assert len(a['rows']) == 76 and len(grouped) == 66
    assert len({(r['proposal_id'],r['field']) for r in a['rows']}) == 76
    results = []
    first_typing = None
    for pin in w['all_selected_payloads']:
        pid = pin['entry_id'].split('::',1)[1]
        oldpath = Path(pin['path'])
        newpath = D/'payloads'/(pid+'.yaml')
        assert sha(oldpath) == pin['sha256']
        old = yaml.safe_load(oldpath.read_text())
        new = yaml.safe_load(newpath.read_text())
        rows = grouped.get(pid, [])
        science = any(r['also_science_scope'] for r in rows)
        if rows:
            remainder = core_comparison(old,new,rows)
            assert science or not remainder, (pid,remainder)
            for row in rows:
                expected = copy.deepcopy(row['full_value'])
                expected['evidence_type'] = 'LLM_SUGGESTION'
                # Scientific notes may change only in the four explicit scope.
                if not science:
                    assert locate(new,row['field']) == expected
            if not science and first_typing is None:
                first_typing = (old,new,rows)
        else:
            assert oldpath.read_bytes() == newpath.read_bytes(), pid
            remainder = []
        results.append({'proposal_id':pid,'old_path':str(oldpath.relative_to(W)),'old_sha256':sha(oldpath),'new_path':str(newpath.relative_to(W)),'new_sha256':sha(newpath),'typing_entry_count':len(rows),'science_scope':science,'unchanged_bytes':not rows,'science_deltas_separate_from_typing_and_event':remainder})
    old,new,rows = first_typing
    controls = []
    badrow = copy.deepcopy(rows[0]);badrow['full_value']['notes'] = 'stale note counterexample'
    controls.append({'control':'stale full evidence object','rejected':reject(lambda:expect_before(old,badrow))})
    for name, mutation in [
        ('unlisted inherited note',lambda x:locate(x,rows[0]['field']).__setitem__('notes','unrelated note edit')),
        ('new unsupported role',lambda x:x.__setitem__('roles',[{'role':'carbon_source'}])),
        ('component evidence enum changed',lambda x:x.setdefault('component_assertion',{}).__setitem__('evidence',[{'evidence_type':'LLM_SUGGESTION','source':'control'}])),
        ('negative label removed',lambda x:x.__setitem__('synonyms',[])),
    ]:
        bad=copy.deepcopy(new);mutation(bad)
        controls.append({'control':name,'rejected':bool(core_comparison(old,bad,rows))})
    bad=copy.deepcopy(new);bad['curation_history'][0]['curator']='false prior author'
    controls.append({'control':'rewritten historical prefix','rejected':reject(lambda:core_comparison(old,bad,rows))})
    assert all(c['rejected'] for c in controls),controls
    result={'reviewer':'Codex /root (worker01), independent of both payload authors','checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'result':'PASS','allowlist_sha256':sha(D/'inputs/w01-full-provenance-allowlist-v2.json'),'total_payloads':len(results),'changed_payloads':len(grouped),'typing_entries':len(a['rows']),'typing_only_payloads':sum(not x['science_scope'] and not x['unchanged_bytes'] for x in results),'science_payloads':sum(x['science_scope'] for x in results),'byte_identical_payloads':sum(x['unchanged_bytes'] for x in results),'records':results,'negative_controls':controls,'limitations':['Four scientific field deltas are exposed completely here and require primary-science review, not accepted by this mechanical comparison.'],'approval':False}
    with output.open('x') as f:json.dump(result,f,indent=2,ensure_ascii=False);f.write('\n')
    print(json.dumps({k:result[k] for k in ['result','total_payloads','changed_payloads','typing_entries','typing_only_payloads','science_payloads','byte_identical_payloads']}))


if __name__ == '__main__':main()
