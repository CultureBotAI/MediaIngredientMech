"""Assemble an immutable successor without changing published predecessor bytes.

This is accounting, not scientific approval. The external whole-shard auditor
and separate skeptical reviews remain mandatory.
"""
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PREVIOUS = ROOT.parent


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def rows(path, key):
    value = json.loads(path.read_text())
    return value if isinstance(value, list) else value[key]


def unique(values, key):
    answer = {}
    for value in values:
        if value[key] in answer:
            raise ValueError(f'Duplicate {key}: {value[key]}')
        answer[value[key]] = value
    return answer


def check_successor(original, revised):
    for key in ('case_id','case_input_sha256','source','occurrence_ids'):
        if original[key] != revised[key]:
            raise ValueError(f'Frozen source field changed: {key}')
    if original['proposal_ids']:
        raise ValueError('Outside assigned no-proposal cohort')


def assemble():
    acceptance = json.loads((ROOT/'acceptance.json').read_text())
    for name, expected in acceptance['published_inputs'].items():
        if hashlib.sha256((PREVIOUS/name).read_bytes()).hexdigest() != expected:
            raise ValueError(f'Published predecessor changed: {name}')
    original = rows(PREVIOUS/'decisions.json','decisions')
    originals = unique(original,'case_id')
    successor = deepcopy(originals)
    evidence = rows(PREVIOUS/'evidence.json','evidence')
    proposals = rows(PREVIOUS/'proposals.json','proposals')
    provenance = {}
    for author in ('a','b','c'):
        assignment = json.loads((ROOT/author/'assigned.json').read_text())
        expected = {x['decision']['case_id'] for x in assignment['cases']}
        revised = unique(rows(ROOT/author/'decisions.json','decisions'),'case_id')
        if revised.keys() != expected:
            raise ValueError(f'{author}: incomplete or extra cohort cases')
        for cid, decision in revised.items():
            check_successor(originals[cid], decision)
            successor[cid] = decision
            provenance[cid] = author
        evidence += rows(ROOT/author/'evidence.json','evidence')
        proposals += rows(ROOT/author/'proposals.json','proposals')
    unique(evidence,'evidence_id')
    unique(proposals,'proposal_id')
    if len(provenance) != 145 or len(successor) != 188:
        raise ValueError('Whole-shard or continuation cohort count changed')
    decisions = [successor[d['case_id']] for d in original]
    lineage=[]
    for before, after in zip(original,decisions):
        lineage.append({'case_id':before['case_id'],
            'scope':'reassessed_no_proposal_cohort' if before['case_id'] in provenance else 'unchanged_prior_proposal_case',
            'primary_author':provenance.get(before['case_id']),
            'previous_decision_sha256':canonical_sha(before),
            'successor_decision_sha256':canonical_sha(after),
            'changed_fields':sorted(k for k in set(before)|set(after) if before.get(k)!=after.get(k))})
    return {
        'decisions':{'schema_version':1,'worker_slot':2,'shard_sha256':acceptance['assigned_shard_sha256'],'phase':'shard','decisions':decisions},
        'evidence':{'schema_version':1,'evidence':evidence},
        'proposals':{'schema_version':1,'proposals':proposals},
        'succession':{'created_at':datetime.now(timezone.utc).isoformat(),'predecessor_head':acceptance['baseline_head'],'predecessor_files':acceptance['published_inputs'],'reassessed_count':len(provenance),'unchanged_prior_proposal_cases':len(original)-len(provenance),'cases':lineage,'scientific_approval_established_by_assembly':False},
    }


if __name__=='__main__':
    result=assemble()
    for name in result:
        if (ROOT/(name+'.json')).exists():
            raise FileExistsError('Immutable assembly already exists: '+name)
    for name,value in result.items():
        (ROOT/(name+'.json')).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
    print({name:len(value.get(name,[])) for name,value in result.items()})
