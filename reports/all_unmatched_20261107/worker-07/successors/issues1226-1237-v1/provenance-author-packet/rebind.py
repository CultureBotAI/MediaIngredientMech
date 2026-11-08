"""Read-only author-side W07 MappingEvidence rebind; does not mutate payloads."""
from __future__ import annotations
import collections
import datetime
import hashlib
import json
import re
import subprocess
from pathlib import Path
import yaml

OUT = Path(__file__).resolve().parent
REPO = OUT.parents[2]
ART = REPO / 'reports/all_unmatched_20261107/worker-07'
AUDIT = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/workers/w02/worktree/.temp/campaign-evidence-provenance-audit-v1')
HEAD = 'ddef7355bf7814bd3b1a23b9d61327bea3ac75fe'
BASE = 'e000d66dd26ab053e9b17ce7bf8d3c873c3dde99'
AUTHOR = '/root/provenance1226_analysis'

def sha(raw): return hashlib.sha256(raw).hexdigest()
def canon(value): return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False)
def value_sha(value): return sha(canon(value).encode())
def typed(value):
    if isinstance(value, (datetime.date, datetime.datetime)):
        return {'$yaml_scalar_type': type(value).__name__, 'value': value.isoformat()}
    if isinstance(value, dict): return {str(k): typed(v) for k, v in value.items()}
    if isinstance(value, list): return [typed(v) for v in value]
    return value
class UniqueLoader(yaml.SafeLoader): pass
def unique_mapping(loader, node, deep=False):
    loader.flatten_mapping(node)
    result = {}
    for k, v in node.value:
        key = loader.construct_object(k, deep=deep)
        if key in result: raise ValueError('Duplicate YAML key: ' + str(key))
        result[key] = loader.construct_object(v, deep=deep)
    return result
UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)
def parse(raw): return typed(yaml.load(raw, Loader=UniqueLoader))
def save(name, value):
    dest = OUT / name
    if dest.exists(): raise ValueError('Refuse overwrite ' + str(dest))
    dest.write_text(json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False, allow_nan=False) + '\n')
def git(*args): return subprocess.check_output(['git', *args], cwd=REPO)
def binding(path): return {'path': str(path), 'sha256': sha(path.read_bytes())}
def multiset_delta(before, after):
    # Exact complete-object, duplicate-aware matching: same-index first, then queues.
    matches = {i:i for i in range(min(len(before), len(after))) if before[i] == after[i]}
    remain = collections.defaultdict(collections.deque)
    for i, value in enumerate(before):
        if i not in matches.values(): remain[canon(value)].append(i)
    for i, value in enumerate(after):
        if i not in matches and remain[canon(value)]: matches[i] = remain[canon(value)].popleft()
    return matches

def main():
    assert git('rev-parse', 'HEAD').decode().strip() == HEAD
    required = {
        'HANDOFF.md': 'c1e269ffc8a4762a2d64e4a0681226e15b802d46bee20ee4030fd088fd2d2d5f',
        'provenance/entry-provenance-ledger-v1.json': '98bfa525356aa223a08fcd2be11d9dc7476231aa6cd9efa4db1f85b2e66109e2',
        'provenance/native-type-suggestions-v1.json': '9ca6b04f03fdaabd65dacd90a160cf9f51dc549e607b5f5634616469532f1b33',
    }
    for name, digest in required.items(): assert sha((AUDIT/name).read_bytes()) == digest
    frozen_ledger = json.loads((AUDIT/'provenance/entry-provenance-ledger-v1.json').read_text())
    matrix = json.loads((AUDIT/'provenance/native-type-suggestions-v1.json').read_text())
    frozen = [r for r in frozen_ledger['rows'] if r['worker'] == 7]
    matrix_rows = {r['audit_row_id']: r for r in matrix['rows'] if r['worker'] == 7}
    ppath = ART/'successors/issue1203-v1/proposals.json'
    proposals = json.loads(ppath.read_text())['proposals']
    assert len(proposals) == 100
    assert sha(ppath.read_bytes()) == '9ac4fb31e9116535336ba5d68953cdf1338098c531638107bcce31b74f1c3f1d'
    pmap = {p['proposal_id']: p for p in proposals}
    inputs, current, baselines, scopes = {}, {}, {}, []
    manual, inherited, components, nonmanual, unexpected = [], [], [], [], []
    for p in proposals:
        pid = p['proposal_id']; path = ART/p['after_capture']['path']; raw = path.read_bytes()
        assert sha(raw) == p['after_capture']['sha256']
        assert git('show', HEAD+':'+str(path.relative_to(REPO))) == raw
        after = parse(raw); current[pid] = after; inputs[str(path)] = binding(path)
        before = {}
        if p['kind'] == 'edit_existing_owner':
            braw = git('show', BASE+':'+p['owner_path'])
            assert sha(braw) == p['before_sha256']
            before = parse(braw)
        baselines[pid] = before
        am = after.get('ontology_mapping', {}).get('evidence', [])
        bm = before.get('ontology_mapping', {}).get('evidence', [])
        matches = multiset_delta(bm, am)
        hc = collections.Counter(canon(x) for x in before.get('curation_history', []))
        added_history = []
        for h in after.get('curation_history', []):
            if hc[canon(h)]: hc[canon(h)] -= 1
            else: added_history.append(h)
        scope = {'proposal_id':pid, 'payload':binding(path), 'owner_path':p['owner_path'],
                 'baseline_sha256':p.get('before_sha256'), 'baseline_git_object':BASE+':'+p['owner_path'] if before else None,
                 'all_mapping_evidence_count':len(am), 'mapping_evidence':[],
                 'added_history':added_history, 'after_history_sha256':value_sha(after.get('curation_history',[]))}
        for i, e in enumerate(am):
            entry = {'proposal_id':pid, 'owner_path':p['owner_path'], 'payload':binding(path),
                     'pointer':'/ontology_mapping/evidence/'+str(i), 'index':i,
                     'full_object':e, 'full_object_sha256':value_sha(e),
                     'duplicate_ordinal_1based':sum(x == e for x in am[:i+1]),
                     'duplicate_total':sum(x == e for x in am),
                     'baseline_match_index':matches.get(i), 'unchanged_from_scientific_base':i in matches}
            scope['mapping_evidence'].append(entry)
            if e.get('evidence_type') == 'MANUAL_CURATION':
                manual.append(entry)
                if i in matches:
                    entry['disposition'] = 'EXCLUDE_INHERITED_COMPLETE_OBJECT'
                    entry['reason'] = 'Exact complete object retained from authentic frozen base; new campaign history does not establish authorship of that older assertion. Preserve without retyping or asserting new human authentication.'
                    inherited.append(entry)
            else:
                entry['disposition'] = 'OUTSIDE_FILED_HUMAN_ENUM_CORRECTION'
                nonmanual.append(entry)
        ca = after.get('component_assertion')
        if ca:
            components.append({'proposal_id':pid, 'payload':binding(path), 'pointer':'/component_assertion',
                               'complete_object':ca, 'complete_object_sha256':value_sha(ca),
                               'evidence_type':ca.get('evidence_type'), 'enum':'ComponentEvidenceTypeEnum',
                               'disposition':'EXCLUDE_SEPARATE_COMPONENT_ENUM',
                               'baseline_equal':ca == before.get('component_assertion')})
        scopes.append(scope)
    by_locator = {(x['proposal_id'], x['index']): x for x in manual}
    allowlist=[]; refs={}; used=set()
    for r in frozen:
        pid=r['proposal_id']; p=pmap[pid]; a=current[pid]; before=baselines[pid]
        idx=int(re.fullmatch(r'ontology_mapping\.evidence\[(\d+)\]',r['field']).group(1))
        entry=by_locator[(pid,idx)];used.add((pid,idx))
        assert entry['payload']['sha256']==r['payload_sha256']
        assert entry['full_object']==r['full_value']
        assert entry['full_object_sha256']==r['full_value_sha256']
        assert not entry['unchanged_from_scientific_base']
        assert matrix_rows[r['audit_row_id']]['suggested_native_type']==r['suggested_native_type']=='LLM_SUGGESTION'
        assert matrix_rows[r['audit_row_id']]['full_value_sha256']==entry['full_object_sha256']
        assert sha(Path(r['payload_path']).read_bytes())==r['payload_sha256']
        if r['baseline_path']:
            assert sha(Path(r['baseline_path']).read_bytes())==r['baseline_sha256']==p['before_sha256']
        ah=next(x for x in scopes if x['proposal_id']==pid)['added_history']
        for h in r['author_evidence']['added_curation_history']: assert h in ah
        for ref in r['author_evidence']['linked_review_reports']:
            q=Path(ref['path']);assert sha(q.read_bytes())==ref['sha256']; refs[str(q)]=ref
        # Full statements include local preparation/identity applicability judgments;
        # even the CHEBI:190300 row mixes database statements with exact-form decisions.
        reason = ('The full statement at '+entry['pointer']+' is agent interpretation of the cited source for '+p['owner_path']+
                  '. Its complete content includes an identity, source applicability, preparation boundary or form-specific inference, not only a copied database assertion. '+
                  'Its exact new history and original reviewer chain establish agent authorship. Use LLM_SUGGESTION; source URL or ontology authorship alone does not establish human-supplied MIM evidence.')
        item={**entry, 'type_pointer':entry['pointer']+'/evidence_type', 'enum':'EvidenceTypeEnum',
              'before_value':'MANUAL_CURATION','suggested_value':'LLM_SUGGESTION',
              'mapping_context_sha256':value_sha({k:v for k,v in a['ontology_mapping'].items() if k!='evidence'}),
              'mapping_context':{k:v for k,v in a['ontology_mapping'].items() if k!='evidence'},
              'audit_row_id':r['audit_row_id'],'audit_row_sha256':value_sha(r),'audit_source_head':r['source_head'],
              'audit_ledger':binding(AUDIT/'provenance/entry-provenance-ledger-v1.json'),
              'audit_matrix_row':matrix_rows[r['audit_row_id']],
              'reason':reason,'audit_claim_specific_type_basis':r['claim_specific_type_basis'],
              'authorship_events':r['author_evidence']['added_curation_history'],
              'linked_historical_review_bindings':r['author_evidence']['linked_review_reports'],
              'allowed_mutation':'Only the exact evidence_type scalar plus separately declared truthful append-only history; do not alter source, notes, dates, other enums or scientific fields through this allowlist.',
              'applicability_gate':'Recheck exact complete object, owner bytes and mapping attachment immediately before type-only mutation. Source correction that changes other fields needs its own reviewed allowlist and new final-byte binding.',
              'scientific_review':False,'independent_approval':False}
        allowlist.append(item)
    for entry in manual:
        if (entry['proposal_id'],entry['index']) not in used and not entry['unchanged_from_scientific_base']:
            unexpected.append(entry)
    assert len(allowlist)==79 and len({x['proposal_id'] for x in allowlist})==74
    assert len(inherited)==1 and not unexpected
    inputs[str(ppath)]=binding(ppath)
    for n in required:inputs[str(AUDIT/n)]=binding(AUDIT/n)
    for n in ['AGENTS.md','MAPPING_SEMANTICS.md','src/mediaingredientmech/schema/mediaingredientmech.yaml','.claude/skills/curate-yaml-record/SKILL.md']:
        inputs[str(REPO/n)]=binding(REPO/n)
    issue=ART/'successors/issues1226-1237-v1/captures/issue-1226.json';inputs[str(issue)]=binding(issue)
    context={'author':AUTHOR,'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
             'head':HEAD,'scientific_base':BASE,'scope':'Author-side claim-specific evidence typing and exact current-object rebind; not independent review or scientific approval.',
             'issue':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1226',
             'scientific_review':False,'independent_approval':False,
             'object_hash_serialization':'UTF-8 JSON sorted keys, separators comma and colon, ensure_ascii=False, no added newline; YAML date/datetime tagged as in frozen audit.',
             'counts':{'selected_proposals':len(proposals),'mapping_evidence_objects':sum(len(x['mapping_evidence']) for x in scopes),
                       'manual_mapping_evidence_objects':len(manual),'allowed_type_corrections':len(allowlist),
                       'affected_proposals':len({x['proposal_id'] for x in allowlist}),
                       'inherited_manual_objects_excluded':len(inherited),'other_mapping_objects_excluded':len(nonmanual),
                       'component_assertions_excluded':len(components),'unexpected_new_manual_objects':len(unexpected)},
             'limitations':['No chemical decisions, input source claims or role/export/owner approvals renewed.',
                            'No candidate, corpus, source capture, old review or other worker bytes changed.',
                            'Hutner source union belongs to coordinator; retyping both preserved source origins is not a winner or co-installation decision.',
                            '74 and79 are exact current provenance counts, not forced final successor counts.',
                            'Independent final-byte review required after parent author changes.']}
    save('allowlist-v1.json',{**context,'rows':allowlist})
    save('exclusions-v1.json',{**context,'inherited_manual':inherited,'nonmanual_mapping':nonmanual,'component_assertions':components,'unexpected_new_manual':unexpected})
    save('all-current-payload-scopes-v1.json',{**context,'proposals':scopes})
    save('input-bindings-v1.json',{**context,'inputs':list(inputs.values()),'historical_reviewer_references':list(refs.values())})
    save('summary-v1.json',context)
    print(json.dumps(context,indent=2))

if __name__=='__main__':main()
