"""Final aggregate readback; no scientific reinterpretation or author edits."""
from pathlib import Path
import json, hashlib, datetime
R=Path('reports/all_unmatched_20261107/worker-08')
B=R/'successors/issue-1227-v1/final-v2'
S=R/'successors/issue-1227-plain-flour-v1'
O=Path('.temp/all-unmatched-worker-08/plain-flour-method-v1/independent/skeptical')
PID='op1201-plain-flour'
CID='KG_CASE:b9a6261315d83792bc02bfbe425cda2032c8833c7a3b6de3aa665fa62a7fc03e'
checks=[];inputs={}
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
 inputs[str(p)]=sha(p);return json.loads(Path(p).read_text())
def canon(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def check(n,c):checks.append({'check':n,'passed':bool(c)})
sel=read(S/'selection.json');lineage=read(S/'lineage.json');prior_d=read(B/'decisions.json')['decisions'];final_d=read(S/'decisions.json')['decisions'];prior_p=read(B/'proposals.json')['proposals'];final_p=read(S/'proposals.json')['proposals'];prior_e=read(B/'evidence.json')['evidence'];final_e=read(S/'evidence.json')['evidence'];review=read(O/'review.json');ad=read(S/'author/decision.json');ap=read(S/'author/proposal.json')
check('announced final selection hash',sha(S/'selection.json')=='335806d22ce278eaf628930b521d7164f0dee2493a19fbc790ae3c273d179f92')
for name,c in sel['authoritative_inputs'].items():check('selected index exact '+name,sha(R/c['path'])==c['sha256'])
ds={x['case_id']:x for x in final_d};ods={x['case_id']:x for x in prior_d};ps={x['proposal_id']:x for x in final_p};ops={x['proposal_id']:x for x in prior_p};es={x['evidence_id']:x for x in final_e}
check('188 unique cases exact roster/order',[x['case_id'] for x in final_d]==[x['case_id'] for x in prior_d] and len(ds)==188)
check('113 unique proposals exact roster/order',[x['proposal_id'] for x in final_p]==[x['proposal_id'] for x in prior_p] and len(ps)==113)
check('320 exact distinct occurrence IDs',[x['occurrence_ids'] for x in final_d]==[x['occurrence_ids'] for x in prior_d] and sum(len(x['occurrence_ids']) for x in final_d)==320 and len({o for x in final_d for o in x['occurrence_ids']})==320)
check('only one case differs',[c for c in ds if ds[c]!=ods[c]]==[CID])
check('only one proposal differs',[p for p in ps if ps[p]!=ops[p]]==[PID])
check('all1075 original evidence objects preserved',len(prior_e)==1075 and final_e[:1075]==prior_e)
check('1082 unique evidence entries',len(final_e)==len(es)==1082)
expected_add=['w08-final001-science','w08-final001-skeptical','w08-final001-historical-review-referral']
expected_d=json.loads(json.dumps(ad));expected_d['evidence_ids']+=expected_add;expected_d['independent_review']={'status':'complete','evidence_ids':expected_add[:2]}
expected_p=json.loads(json.dumps(ap));expected_p['evidence_ids']+=expected_add
check('case only reviewed bookkeeping additions',ds[CID]==expected_d)
check('proposal only reviewed evidence backlinks',ps[PID]==expected_p)
check('authored case remains reviewed exact input',canon(ad)==review['case_hashes'][CID])
lc={x['case_id']:x for x in lineage['cases']};lp={x['proposal_id']:x for x in lineage['payloads']}
for cid,d in ds.items():
 check('case original source/holds '+cid,all((k in d)==(k in ods[cid]) and d.get(k)==ods[cid].get(k) for k in ['case_input_sha256','source','occurrence_ids','preserved_native_decisions','owner_records']))
 check('case lineage exact '+cid,lc[cid]['before_decision_sha256']==canon(ods[cid]) and lc[cid]['after_decision_sha256']==canon(d) and lc[cid]['case_input_sha256']==d['case_input_sha256'] and lc[cid]['occurrence_ids']==d['occurrence_ids'])
for pid,p in ps.items():
 check('original owner/beforeimage '+pid,p['owner_path']==ops[pid]['owner_path'] and p['before_sha256']==ops[pid]['before_sha256'] and p['kind']==ops[pid]['kind'] and p['case_ids']==ops[pid]['case_ids'])
 cap=p['after_capture'];check('actual whole payload '+pid,sha(R/cap['path'])==cap['sha256'])
 check('payload lineage exact '+pid,lp[pid]['predecessor_capture']==ops[pid]['after_capture'] and lp[pid]['selected_capture']==cap and lp[pid]['original_before_sha256']==p['before_sha256'] and lp[pid]['payload_byte_exact_unchanged']==(pid!=PID) and lp[pid]['proposal_object_unchanged']==(pid!=PID))
 if pid!=PID:check('unrelated candidate object unchanged '+pid,p==ops[pid])
check('selected payload remains independently reviewed bytes',ps[PID]['after_capture']['sha256']==review['payload_hashes'][PID]=='884fee1ea6a5082a51b8769f2a827199b1703972ad80fa48e1bb8d2d09ab3873')
for e in final_e[1075:]:
 cap=e['capture'];check('new actual evidence capture '+e['evidence_id'],cap['root']=='artifact' and sha(R/cap['path'])==cap['sha256']);check('new evidence only exact source case '+e['evidence_id'],e['case_ids']==[CID])
for lane,expected in [('science','eee808bca0310f04b7100ab878f1e6c9c750de08934862027b71c94245f24c08'),('skeptical','08dfb4b4e72ba57cb8d1fccf57441f500d5a08cb2460d3ac5c73d3c3b788cabe')]:
 cap=sel['initial_exact_independent_reviews'][lane];peer=read(R/cap['path']);check('exact immutable peer '+lane,sha(R/cap['path'])==cap['sha256']==expected and peer['payload_hashes'][PID]==ps[PID]['after_capture']['sha256'])
check('referral remains separate exact artifact',sha(O/'coordinator-referral.json')==sha(S/'independent-review/skeptical/coordinator-referral.json')=='1a15fb8cef3e930eab147169252e5ca3327061413cc7ccc5141fc8281fbec225')
check('no owner admission waiver or release',sel['whole_owner_role_export_approval'] is False and sel['maintained_application'] is False and sel['coordinator_final_head_acceptance']=='pending' and 'FAILED/HELD unchanged' in sel['prior_TSB_Bacto_admission'])
check('original capture times and source summaries unchanged',all(es[x['evidence_id']]==x for x in prior_e))
check('all actual evidence refs resolve',all(set(d['evidence_ids'])<=set(es) for d in final_d) and all(set(p['evidence_ids'])<=set(es) for p in final_p))
check('read inputs unchanged',all(sha(p)==h for p,h in inputs.items()))
out={'schema':'w08-plain-flour-final-index-bindings-v1','reviewer':'worker08:/root/inorganics','author':'worker08:/root','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS' if all(x['passed'] for x in checks) else 'FAIL','scope':'Final exact aggregate selection readback only, supplemental to immutable skeptical review; no new scientific approval of unrelated cases or own authored materials.','initial_review':{'path':str(O/'review.json'),'sha256':sha(O/'review.json')},'check_count':len(checks),'failures':[x for x in checks if not x['passed']],'checks':checks,'input_hashes':inputs,'final_case_hash':canon(ds[CID]),'final_proposal_hash':canon(ps[PID]),'payload_sha256':ps[PID]['after_capture']['sha256'],'counts':{'cases':188,'proposals':113,'occurrence_ids':320,'unchanged_cases':187,'unchanged_payloads':112,'preserved_old_evidence_objects':1075,'added_evidence_objects':7},'outcome':'Only the reviewed Plain Flour case/proposal and required peer/referral bookkeeping change. Original source objects, occurrence IDs, beforeimages, unresolved scientific holds and TSB admission hold survive. PF-LINEAGE-001 is separately preserved and does not expand the author correction.','native_checks':'Not rerun here; root owns guarded/native validation and eventual head acceptance.','writes_only':str(O)}
(O/'final-bindings.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['checks','input_hashes']},indent=2))
