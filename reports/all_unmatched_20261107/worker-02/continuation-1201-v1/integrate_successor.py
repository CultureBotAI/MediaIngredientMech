"""Assemble a new version from stable authored outcomes and explicit compositions.

This only changes isolated outcome ledgers. Reciprocal proposal links follow
explicit authored case references; no name matching or scientific inference is
used. The result remains pending final independent-review binding.
"""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
from assemble_successor import assemble, canonical_sha

S=Path(__file__).resolve().parent


def load(p):return json.loads(p.read_text())


def integrate():
    result=assemble()
    decisions={d['case_id']:d for d in result['decisions']['decisions']}
    proposals={p['proposal_id']:p for p in result['proposals']['proposals']}
    composed=load(S/'integration/composed-proposals-v2.json')['proposals']
    updates=load(S/'integration/composed-case-updates-v4.json')['updates']
    for p in composed:
        for fragment in p['supersedes_proposals']:
            current=proposals.pop(fragment['proposal_id'])
            if current!=fragment:
                raise ValueError('Composed fragment changed after exact capture/review: '+fragment['proposal_id'])
        proposals[p['proposal_id']]=p
    for row in updates:
        cid=row['case_id']
        if decisions[cid]!=row['previous_decision']:
            raise ValueError('Authored source decision changed since composition: '+cid)
        decisions[cid]=row['successor_decision']
    # Cross-author source applicability was explicitly authored by the source
    # case owner. These are reciprocal metadata, never automatic substance joins.
    allowed={
        ('CM_NAME:d6d904fb14e9456fb0b5b287dd66bed162e2625456a33c33e66ed0328bf152b5','c2-proposal-desiccated-ox-bile'),
        ('CM_NAME:e1620e7f16610573b53e17ac40af2fa247bab678628651f8b09e3024a04c4d77','c2-proposal-emjh-enrichment'),
        ('KG_CASE:55268b66b04a59d2f2c6487270ae15e4a4686148d8fff29fd66b248269821cd8','a2-proposal-manganese-sulfate-variable-hydrate'),
    }
    original=load(S.parent/'decisions.json')['decisions']
    # A46 now shares the B concentrated-acid description, after skeptical review
    # rejected source-ID-only duplicate substance identities.
    allowed.add((original[46]['case_id'],'b2-proposal-concentrated_sulfuric_acid_assay_unspecified'))
    backlinks=[]
    for cid,d in decisions.items():
        for pid in d['proposal_ids']:
            p=proposals[pid]
            if cid not in p['case_ids']:
                if (cid,pid) not in allowed:
                    raise ValueError('Undeclared cross-author backlink: '+cid+' -> '+pid)
                p['case_ids'].append(cid)
                p['evidence_ids']=list(dict.fromkeys(p['evidence_ids']+d['evidence_ids']))
                backlinks.append({'case_id':cid,'proposal_id':pid,'after_capture_unchanged':p['after_capture'],'case_decision_sha256':canonical_sha(d),'scope':'Reciprocal metadata for an explicitly authored source-case link; independent source applicability and exact payload review required.'})
    result['decisions']['decisions']=[decisions[d['case_id']] for d in original]
    result['proposals']['proposals']=list(proposals.values())
    result['evidence']['evidence']+=load(S/'integration/composition-evidence.json')['evidence']
    for row in result['succession']['cases']:
        after=decisions[row['case_id']]
        before=next(d for d in original if d['case_id']==row['case_id'])
        row['successor_decision_sha256']=canonical_sha(after)
        row['changed_fields']=sorted(k for k in set(before)|set(after) if before.get(k)!=after.get(k))
        if any(u['case_id']==row['case_id'] for u in updates):
            row['integration_author']='/root'
            row['scope']='reassessed_cohort_with_composed_backlink' if not before['proposal_ids'] else 'prior_proposal_case_with_explicit_successor_backlink'
    result['succession']['unchanged_prior_proposal_cases']=sum(d==decisions[d['case_id']] for d in original if d['proposal_ids'])
    result['succession']['changed_prior_proposal_cases']=sum(d!=decisions[d['case_id']] for d in original if d['proposal_ids'])
    result['cross-author-backlinks']={'created_at':datetime.now(timezone.utc).isoformat(),'backlinks':backlinks,'note':'All affected source decisions and exact payloads must be reviewed independently; this accounting script grants no scientific approval.'}
    return result


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
    args.out.mkdir(exist_ok=False)
    result=integrate()
    for name,value in result.items():(args.out/(name+'.json')).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'decisions':len(result['decisions']['decisions']),'evidence':len(result['evidence']['evidence']),'proposals':len(result['proposals']['proposals']),'explicit_cross_author_links':len(result['cross-author-backlinks']['backlinks'])}))


if __name__=='__main__':main()
