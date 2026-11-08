"""Bind final canonical and native reports to the actual independent scientific reviews."""
import argparse, hashlib, importlib.util, json, re, traceback
from datetime import datetime, timezone
from pathlib import Path
import yaml
W=Path.cwd();S=W/'.temp/w05-final-correction-v1';O=S/'review-assembly';B=W/'reports/all_unmatched_20261107/worker-05'
ap=argparse.ArgumentParser();ap.add_argument('--core',type=Path,required=True);ap.add_argument('--review-bindings',type=Path,required=True);ap.add_argument('--native',type=Path,required=True);ap.add_argument('--output',required=True);args=ap.parse_args()
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def objsha(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def actor(s):
    found=re.findall(r'/root(?:/[a-z_0-9]+)+',s)
    assert len(found)==1,s
    return found[0]
result=dict(reviewer='/root/final_skeptical',at=datetime.now(timezone.utc).isoformat(),scope='Final exact canonical/native scientific-review linkage and attribution; original science remains with the named disjoint reviewers.',errors=[])
out=O/args.output;assert not out.exists()
try:
    ds=load(args.core/'decisions.json')['decisions'];ps=load(args.core/'proposals.json')['proposals'];es=load(args.core/'evidence.json')['evidence'];line=load(args.core/'proposal-lineage.json')['rows'];ar=load(args.core/'assembly-receipt.json')
    dd={d['case_id']:d for d in ds};pp={p['proposal_id']:p for p in ps};ee={e['evidence_id']:e for e in es};ll={r['proposal_id']:r for r in line}
    oldds=load(B/'correction-1193-v1/decisions.json')['decisions'];assert [d['case_id'] for d in ds]==[d['case_id'] for d in oldds]
    rb=load(args.review_bindings);reviews={};cases=[];payloads=[];coverage={};expected_reviews={'media':'/root/final_skeptical','materials':'/root/media_research','chemicals':'/root/materials_research'};expected_authors={'media':'/root/media_research','materials':'/root/materials_research','chemicals':'/root/chemicals_research'}
    for lane,b in rb.items():
        p=W/b['path'];assert sha(p)==b['sha256'];r=load(p);reviews[lane]=r
        assert actor(b['reviewer'])==expected_reviews[lane]
        assert actor(r['reviewer'])==expected_reviews[lane]
        assert actor(r['primary_author'])==expected_authors[lane]
        assert expected_reviews[lane]!=expected_authors[lane]
        cs=r['case_reviews'];qs=r['payload_reviews'];assert len({c['case_id'] for c in cs})==len(cs)
        assert {c['case_id'] for c in cs}=={cid for cid,lane2 in ar['case_lane'].items() if lane2==lane}
        assert {p['proposal_id'] for p in qs}=={pid for pid,lane2 in ar['proposal_lane'].items() if lane2==lane}
        e=ee[b['evidence_id']];assert e['capture']['sha256']==b['sha256'] and e['kind']=='independent_review'
        for c in cs:
            d=dd[c['case_id']];h=c.get('selected_decision_object_sha256',c.get('decision_object_sha256'))
            assert h and h==d['final_assembly_provenance']['selected_decision_object_sha256'],(lane,c['case_id'],'decision binding')
            assert c['case_input_sha256']==d['case_input_sha256']
            assert d['independent_review']['status']=='complete' and b['evidence_id'] in d['independent_review']['evidence_ids']
            assert c['assessment'].strip()
            cases.append(dict(case_id=c['case_id'],lane=lane,actual_scientific_reviewer=expected_reviews[lane],primary_author=expected_authors[lane],assessment=c['assessment'],review_entry_sha256=objsha(c),selected_fragment_decision_sha256=h,canonical_decision_sha256=objsha(d)))
        for q in qs:
            p=pp[q['proposal_id']];cap=q.get('after_capture') or q.get('selected_after_capture') or q.get('lineage',{}).get('after_capture')
            assert cap==p['after_capture'] and sha(B/cap['path'])==cap['sha256']
            assert q['assessment'].strip()
            payloads.append(dict(proposal_id=q['proposal_id'],lane=lane,actual_scientific_reviewer=expected_reviews[lane],primary_author=expected_authors[lane],assessment=q['assessment'],review_entry_sha256=objsha(q),selected_capture=cap))
        coverage[lane]=dict(cases=len(cs),payloads=len(qs),reviewer=expected_reviews[lane],primary_author=expected_authors[lane],review_path=b['path'],review_sha256=b['sha256'],completed_at=b['completed_at'])
    assert len(cases)==len(ds) and len(payloads)==len(ps)
    native=yaml.safe_load(args.native.read_text());nt={t['target_id']:t for t in native['targets']};nas={}
    for x in native['assessments']:
        for tid in x['target_ids']:assert tid not in nas;nas[tid]=x
    assert set(nas)==set(nt) and len(nt)==len(ds)+len(ps)
    cm={c['case_id']:c for c in cases};pm={p['proposal_id']:p for p in payloads}
    for i,d in enumerate(ds):
        tid=f'CASE-{i+1:03d}';t=nt[tid]
        assert t['selector']==d['case_id'] and W/t['path']==(args.core/'decisions.json').resolve()
        assert nas[tid]['summary']==cm[d['case_id']]['assessment']
        assert expected_reviews[ar['case_lane'][d['case_id']]] in nas[tid]['details']
    for p in ps:
        tid=ll[p['proposal_id']]['predecessor_proposal_id'] or p['proposal_id'];t=nt[tid]
        assert sha(W/t['path'])==p['after_capture']['sha256']
        assert nas[tid]['summary']==pm[p['proposal_id']]['assessment']
        if p.get('integration_disposition')=='PENDING_COORDINATOR_FAMILY_DECISION':assert nas[tid]['outcome']=='concern'
    original=yaml.safe_load((B/'final-correction-v1/inputs/external-w08-review/native/review.yaml').read_text());nf={f['finding_id']:f for f in native['findings']};of={f['finding_id']:f for f in original['findings']}
    assert set(of)==set(nf)
    finding_checks=[]
    for fid,f in of.items():
        assert set(f['target_ids'])<=set(nf[fid]['target_ids'])<=set(nt)
        if fid in ['W05-CR-F01','W05-CR-F02','W05-CR-F03','W05-CR-F08']:assert nf[fid]['status']=='deferred'
        finding_checks.append(dict(finding_id=fid,original_targets=f['target_ids'],current_targets=nf[fid]['target_ids'],status=nf[fid]['status'],disposition=nf[fid].get('disposition_reason')))
    assert native['completion']=='completed' and native['verdict']=='needs_curation'
    assert native['reviewer']['independence']=='self_review'
    spec=importlib.util.spec_from_file_location('review_assembly_native',W/'scripts/record_review.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    mod.validate_review(native);mod.assert_current_source(W,native)
    md=args.native.with_suffix('.md');assert md.is_file() and md.read_text()==mod.render_markdown(native)
    replay=load(O/'independent-native-replay-v1/native-validation.json')
    assert sha(args.core/'proposals.json')==replay['inputs']['proposals']['sha256'] and replay['status']=='PASS'
    result.update(status='PASS',canonical_hashes={f:sha(args.core/f) for f in ['decisions.json','evidence.json','proposals.json','proposal-lineage.json','assembly-receipt.json']},review_bindings=dict(path=str(args.review_bindings),sha256=sha(args.review_bindings)),coverage=coverage,case_bindings=cases,payload_bindings=payloads,original_findings=finding_checks,native=dict(path=str(args.native),sha256=sha(args.native),markdown_path=str(md),markdown_sha256=sha(md),targets=len(nt),assessments=len(nas),native_validator='PASS',current_source_hashes='PASS',derived_markdown='PASS'),unchanged_independently_validated_payload_sha256=sha(args.core/'proposals.json'),limitations=['This verifies truthful assembly and preserves attribution; scientific statements above are quoted from the named reviewers, not reauthored by this assembly reviewer.','Needs-curation and deferred scopes remain; no owner application, source release, roles or export approval.','Future payload/core/native changes invalidate this exact-byte receipt unless independently rereviewed.'])
except Exception:
    result['status']='FAIL';result['errors'].append(traceback.format_exc())
out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:result.get(k) for k in ['status','coverage','native','errors']},indent=2))
raise SystemExit(result['status']!='PASS')
