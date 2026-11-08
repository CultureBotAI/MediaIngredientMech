"""Bind exact successor science to separately authored skeptical review receipts.

Only independent_review metadata is changed. Immutable prebinding snapshots and
the published predecessor remain untouched. This is not whole-owner approval.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent
ARTIFACT = ROOT.parent
SOURCE = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()


def load(path):
    return json.loads(path.read_text())


def verify_ref(ref):
    base = {'artifact':ARTIFACT,'source':SOURCE,'mim':Path.cwd()}[ref['root']]
    rel = Path(ref['path'])
    if rel.is_absolute() or '..' in rel.parts:
        raise ValueError('Review reference escapes its declared root')
    if hashlib.sha256((base/rel).read_bytes()).hexdigest()!=ref['sha256']:
        raise ValueError('Reviewed input changed: '+str(base/rel))


def verify_case(decision, row, reviewer, authors):
    if row['status']!='approve':
        raise ValueError('Review does not approve the scoped case outcome')
    if reviewer in authors:
        raise ValueError('Case author cannot independently review own decision')
    if row['case_id']!=decision['case_id'] or row['case_input_sha256']!=decision['case_input_sha256']:
        raise ValueError('Case input binding changed')
    if row['decision_canonical_sha256']!=digest(decision):
        raise ValueError('Decision differs from exact independently reviewed content')
    if not row.get('reasoning'):
        raise ValueError('A status alone is not a skeptical assessment')


def verify_proposal(proposal,row,reviewer,authors):
    if row['status']!='approve' or reviewer in authors:
        raise ValueError('Missing independent payload approval')
    if row['proposal_id']!=proposal['proposal_id'] or row['after_capture']!=proposal['after_capture']:
        raise ValueError('Reviewed payload binding changed')
    if not row.get('reasoning'):
        raise ValueError('A payload status alone is not a skeptical assessment')
    verify_ref(row['after_capture'])


def main():
    destination=ROOT/'integration/independent-review-coverage.json'
    if destination.exists():raise FileExistsError(destination)
    routing=load(ROOT/'integration/review-routing.json')
    original={d['case_id']:d for d in load(ARTIFACT/'decisions.json')['decisions']}
    old_proposals={p['proposal_id']:p for p in load(ARTIFACT/'proposals.json')['proposals']}
    decisions=load(ROOT/'decisions.json')
    proposals=load(ROOT/'proposals.json')
    evidence=load(ROOT/'evidence.json')
    case_reviews,proposal_reviews={},{}
    review_evidence=[]
    for ref in routing['reviews']:
        path=ROOT/ref['path']
        doc=load(path)
        for item in doc['input_hash_manifest']:verify_ref(item)
        reviewer=doc['reviewer']
        for row in doc['case_reviews']:
            if row['status']=='approve':
                case_reviews.setdefault(row['case_id'],[]).append((row,reviewer,ref['evidence_id']))
        for row in doc['proposal_reviews']:
            if row['status']=='approve':
                proposal_reviews.setdefault(row['proposal_id'],[]).append((row,reviewer,ref['evidence_id']))
        review_evidence.append({'evidence_id':ref['evidence_id'],'kind':'independent_review',
            'capture':{'root':'artifact','path':str(path.relative_to(ARTIFACT)),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()},
            'url':None,'accessed_at':doc['reviewed_at'],
            'locator':'Exact case and payload digests, skeptical reasoning, inspected source evidence and actual reviewer identity are retained in this immutable review.',
            'supports_or_contradicts':'Separate review of the declared source-case/proposal scope; no complete owner, role, merge or export approval.'})
    payload_coverage=[]
    for p in proposals['proposals']:
        pid=p['proposal_id']
        if p==old_proposals.get(pid):
            payload_coverage.append({'proposal_id':pid,'scope':'unchanged_predecessor','after_capture':p['after_capture']})
            continue
        authors=routing['proposal_authors'][pid]
        rows=proposal_reviews.get(pid,[])
        valid=[]
        for row,reviewer,eid in rows:
            verify_proposal(p,row,reviewer,authors)
            valid.append({'reviewer':reviewer,'evidence_id':eid})
        if not valid:raise ValueError('No independent exact payload review: '+pid)
        payload_coverage.append({'proposal_id':pid,'authors':authors,'scope':'successor_payload','after_capture':p['after_capture'],'reviews':valid})
    coverage=[]
    for d in decisions['decisions']:
        cid=d['case_id'];before=digest(d)
        if d==original[cid]:
            coverage.append({'case_id':cid,'scope':'unchanged_predecessor','final_decision_sha256':before,'review_evidence_ids':d['independent_review']['evidence_ids']})
            continue
        authors=routing['case_authors'][cid]
        rows=case_reviews.get(cid,[])
        valid=[]
        for row,reviewer,eid in rows:
            # Superseded review rows may coexist in preserved files; only an exact
            # final decision hash can support the active decision.
            if row['decision_canonical_sha256']!=before:continue
            verify_case(d,row,reviewer,authors)
            valid.append({'reviewer':reviewer,'evidence_id':eid})
        if not valid:raise ValueError('No independent exact case review: '+cid)
        refs=list(dict.fromkeys(x['evidence_id'] for x in valid))
        d['independent_review']={'status':'complete','evidence_ids':refs}
        coverage.append({'case_id':cid,'scope':'successor_case','authors':authors,'reviews':valid,'reviewed_decision_sha256':before,'final_decision_sha256':digest(d)})
    if len(coverage)!=188 or len({x['case_id'] for x in coverage})!=188:
        raise ValueError('Whole-shard coverage changed')
    if len({x['evidence_id'] for x in evidence['evidence']+review_evidence})!=len(evidence['evidence'])+len(review_evidence):
        raise ValueError('Duplicate independent review evidence id')
    evidence['evidence']+=review_evidence
    for name in ('decisions','evidence','proposals'):
        saved=ROOT/'integration'/('pre-binding-'+name+'.json')
        if saved.exists():raise FileExistsError(saved)
        shutil.copyfile(ROOT/(name+'.json'),saved)
    for name,obj in [('decisions',decisions),('evidence',evidence)]:
        (ROOT/(name+'.json')).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
    destination.write_text(json.dumps({'created_at':datetime.now(timezone.utc).isoformat(),'case_count':188,'cases':coverage,'proposals':payload_coverage,'limits':'Case and payload science was separately reviewed. Binding changes review metadata only. All complete-owner and release obligations remain.'},indent=2)+'\n')
    print(json.dumps({'cases':len(coverage),'successor_cases':sum(x['scope']=='successor_case' for x in coverage),'successor_payloads':sum(x['scope']=='successor_payload' for x in payload_coverage)}))


if __name__=='__main__':main()
