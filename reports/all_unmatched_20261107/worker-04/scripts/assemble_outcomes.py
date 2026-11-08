"""Assemble reviewed fragments without altering their frozen source/proposal fields."""
import json,hashlib,datetime,collections
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]; ART=ROOT/'reports/all_unmatched_20261107/worker-04'
SHARD=ART/'provenance/shard-04.json'; shard=json.loads(SHARD.read_text()); sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
review_files={'chemistry':'chemistry-reviewed-by-biological-v1.json','biological':'biological-reviewed-by-media-v2.json','media':'media-reviewed-by-chemistry-v2.json'}
all_dec=[];all_ev=[];all_pr=[];bindings=[]
for group,review_file in review_files.items():
    rp=ART/'independent-review'/review_file; review=json.loads(rp.read_text())
    assert review['status']=='complete',(group,review['status'])
    # The two reviewers serialize input bindings differently; both are checked exactly.
    hashes={('fragments/'+k if '/' not in k else k):v for k,v in review.get('reviewed_fragment_hashes',{}).items()}
    if not hashes:
        hashes={v['path']:v['sha256'] for v in review['inputs'].values()}
    fragments={}
    for kind in ['decisions','evidence','proposals']:
        rel=f'fragments/{group}-{kind}.json';p=ART/rel
        assert hashes.get(rel)==sha(p),(rel,hashes.get(rel),sha(p))
        fragments[kind]=json.loads(p.read_text())[kind]
    reviews=review['case_reviews'];reviewed={r['case_id'] for r in reviews}
    assert len(reviewed)==len(reviews)==len(fragments['decisions'])
    assert reviewed=={x['case_id'] for x in fragments['decisions']}
    rid=f'independent-{group}-final'
    all_ev.extend(fragments['evidence'])
    all_ev.append({'evidence_id':rid,'capture':{'root':'artifact','path':str(rp.relative_to(ART)),'sha256':sha(rp)},'locator':'Complete per-case notes, findings/dispositions, final fragment and exact proposed-payload hashes','supports_or_contradicts':'Separate skeptical review of every assigned case and proposed delta by a different in-process agent; source, owner and export holds remain.','kind':'independent_review','url':None,'case_ids':sorted(reviewed)})
    for d in fragments['decisions']:
        d['independent_review']={'status':'complete','evidence_ids':[rid]}
        d['publication_scope']='Source-case disposition and proposed delta only; all frozen source-specific holds persist; no maintained owner/export approval.'
        all_dec.append(d)
    all_pr.extend(fragments['proposals'])
    bindings.append({'group':group,'review':str(rp.relative_to(ART)),'review_sha256':sha(rp),'fragment_hashes':hashes,'cases':len(reviewed),'proposals':len(fragments['proposals'])})
# Preserve exact shard order. Source objects themselves are never rewritten.
cases=shard['cases'];order={x['case_id']:i for i,x in enumerate(cases)}
assert len(all_dec)==len(cases)==len({d['case_id'] for d in all_dec})==188
assert {d['case_id'] for d in all_dec}==set(order)
all_dec.sort(key=lambda d:order[d['case_id']])
assert len({e['evidence_id'] for e in all_ev})==len(all_ev)
assert len({p['proposal_id'] for p in all_pr})==len(all_pr)
normalizations=[]
for evidence in all_ev:
    if 'case_ids' in evidence and len(evidence['case_ids'])!=len(set(evidence['case_ids'])):
        before=list(evidence['case_ids']);evidence['case_ids']=list(dict.fromkeys(before))
        normalizations.append({'evidence_id':evidence['evidence_id'],'field':'case_ids','before':before,'after':evidence['case_ids'],'reason':'Remove duplicate references only; unchanged applicability set and capture bytes. Frozen author fragment and independent review remain untouched.'})
issues_path=ART/'issues/filed-findings.json'
if issues_path.exists():
    for issue in json.loads(issues_path.read_text())['issues']:
        for d in all_dec:
            if d['case_id'] in issue['case_ids']:
                d['issue_refs']=list(dict.fromkeys(d['issue_refs']+[issue['url']]))
for name,data in [('decisions',{'schema_version':1,'worker_slot':4,'shard_sha256':sha(SHARD),'phase':'shard','decisions':all_dec}),('evidence',{'schema_version':1,'evidence':all_ev}),('proposals',{'schema_version':1,'proposals':all_pr})]:
    (ART/f'{name}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
(ART/'validation/assembly-bindings.json').write_text(json.dumps({'assembled_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'bindings':bindings,'reference_normalizations':normalizations,'permitted_assembly_changes':['independent_review status/evidence references','explicit retained publication scope','issue_refs for filed exact case findings','deduplicate evidence case_ids references without changing their set'],'case_count':len(all_dec),'evidence_count':len(all_ev),'proposal_count':len(all_pr),'sources':dict(collections.Counter(d['source']['source'] for d in all_dec)),'dispositions':dict(collections.Counter(d['disposition'] for d in all_dec))},indent=2)+'\n')
print(len(all_dec),'decisions',len(all_ev),'evidence',len(all_pr),'proposals')
