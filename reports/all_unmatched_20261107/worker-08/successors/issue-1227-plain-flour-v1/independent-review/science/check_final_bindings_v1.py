import pathlib,json,hashlib,datetime
R=pathlib.Path('.').resolve();A=R/'reports/all_unmatched_20261107/worker-08';N=A/'successors/issue-1227-plain-flour-v1';P=A/'successors/issue-1227-v1/final-v2';O=R/'.temp/all-unmatched-worker-08/plain-flour-method-v1/independent/science'; checks=[]
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
canon=lambda d:hashlib.sha256(json.dumps(d,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def check(n,v,detail=None):
 checks.append({'check':n,'passed':bool(v),'detail':detail});assert v,n
def read(p):return json.loads(p.read_text())
s=read(N/'selection.json');check('selection exact announced hash',h(N/'selection.json')=='335806d22ce278eaf628930b521d7164f0dee2493a19fbc790ae3c273d179f92')
for key,pin in s['authoritative_inputs'].items():check('selection input pin '+key,h(A/pin['path'])==pin['sha256'])
od=read(P/'decisions.json')['decisions'];nd=read(N/'decisions.json')['decisions'];op=read(P/'proposals.json')['proposals'];np=read(N/'proposals.json')['proposals'];oe=read(P/'evidence.json')['evidence'];ne=read(N/'evidence.json')['evidence'];lin=read(N/'lineage.json');cid=s['changed_case_id'];pid=s['changed_proposal_id'];caseproof=[];payloadproof=[]
check('188 case identities same order',len(nd)==len(od)==188 and [x['case_id'] for x in nd]==[x['case_id'] for x in od])
check('113 proposal identities same order',len(np)==len(op)==113 and [x['proposal_id'] for x in np]==[x['proposal_id'] for x in op])
check('1075 historical evidence objects exact unchanged prefix',len(oe)==1075 and ne[:len(oe)]==oe)
check('1082 final evidence IDs unique',len(ne)==1082 and len({e['evidence_id'] for e in ne})==len(ne))
check('original 320 occurrence IDs retained',[(x['case_id'],x['occurrence_ids']) for x in nd]==[(x['case_id'],x['occurrence_ids']) for x in od] and sum(len(x['occurrence_ids']) for x in nd)==320 and len({o for x in nd for o in x['occurrence_ids']})==320)
ld={c['case_id']:c for c in lin['cases']};lp={p['proposal_id']:p for p in lin['proposals']}
check('lineage complete exact identity coverage',set(ld)=={c['case_id'] for c in nd} and set(lp)=={p['proposal_id'] for p in np})
for old,new in zip(od,nd):
 changed=new['case_id']==cid
 check('case preserved or sole authorized change '+new['case_id'],changed or old==new)
 for k in ['case_input_sha256','source','occurrence_ids','owner_records','preserved_native_decisions']:check('frozen field '+new['case_id']+' '+k,old[k]==new[k])
 check('lineage case hashes '+new['case_id'],ld[new['case_id']]['before_decision_sha256']==canon(old) and ld[new['case_id']]['after_decision_sha256']==canon(new))
 caseproof.append({'case_id':new['case_id'],'before_canonical_sha256':canon(old),'after_canonical_sha256':canon(new),'unchanged':old==new,'scope':'full scientific appraisal only for Plain Flour; exact continuity for other cases'})
for old,new in zip(op,np):
 changed=new['proposal_id']==pid;cap=new['after_capture']; oldcap=old['after_capture']
 check('selected payload actual hash '+new['proposal_id'],h(A/cap['path'])==cap['sha256'])
 check('original payload still retained '+new['proposal_id'],h(A/oldcap['path'])==oldcap['sha256'])
 check('proposal unchanged except one authorized '+new['proposal_id'],changed or old==new)
 check('owner path/preimage/case links unchanged '+new['proposal_id'],all(old[k]==new[k] for k in ['owner_path','before_sha256','case_ids','kind']))
 check('lineage proposal payload bindings '+new['proposal_id'],lp[new['proposal_id']]['predecessor_capture']==oldcap and lp[new['proposal_id']]['selected_capture']==cap)
 payloadproof.append({'proposal_id':new['proposal_id'],'original_capture':oldcap,'selected_capture':cap,'unchanged':old==new,'scope':'full scientific appraisal only for Plain Flour; actual byte hash continuity for others'})
fd=next(x for x in nd if x['case_id']==cid);fp=next(x for x in np if x['proposal_id']==pid);ad=read(N/'author/decision.json');ap=read(N/'author/proposal.json')
check('final case scientific content equals reviewed author object',all(fd.get(k)==ad.get(k) for k in (set(fd)|set(ad))-{'independent_review','evidence_ids'}))
check('final proposal scientific content equals reviewed author object',all(fp.get(k)==ap.get(k) for k in (set(fp)|set(ap))-{'evidence_ids'}))
added=['w08-final001-science','w08-final001-skeptical','w08-final001-historical-review-referral']
check('only actual review and referral references added',fd['evidence_ids']==ad['evidence_ids']+added and fp['evidence_ids']==ap['evidence_ids']+added)
check('final independent-review bookkeeping is actual separate scientific/skeptical receipts',fd['independent_review']=={'status':'complete','evidence_ids':['w08-final001-science','w08-final001-skeptical']})
check('scientific receipt byte exact public/private',h(N/'independent-review/science/review.json')==h(O/'review.json')=='eee808bca0310f04b7100ab878f1e6c9c750de08934862027b71c94245f24c08')
for e in ne[1075:]:check('new evidence capture pin '+e['evidence_id'],h(A/e['capture']['path'])==e['capture']['sha256'])
check('payload scientific receipt remains bound to exact selected bytes',read(O/'review.json')['payload_hashes'][pid]==fp['after_capture']['sha256']=='884fee1ea6a5082a51b8769f2a827199b1703972ad80fa48e1bb8d2d09ab3873')
check('selection holds explicit',s['coordinator_final_head_acceptance']=='pending' and s['whole_owner_role_export_approval'] is False and s['maintained_application'] is False and 'FAILED/HELD' in s['prior_TSB_Bacto_admission'])
paths=[N/'selection.json',N/'decisions.json',N/'proposals.json',N/'evidence.json',N/'lineage.json',N/'author/decision.json',N/'author/proposal.json',N/'payloads/Plain_Flour.yaml',P/'decisions.json',P/'proposals.json',P/'evidence.json',O/'review.json',N/'independent-review/science/review.json',N/'independent-review/skeptical/review.json',N/'independent-review/skeptical/coordinator-referral.json',pathlib.Path(__file__).resolve()]
receipt={'schema':'w08-final001-scientific-final-index-bindings-v1','reviewer':'worker08:/root/vitamins','author':'worker08:/root','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'complete','verdict':'pass_with_limitations','scope':'Exact final index readback, metadata and byte continuity. Original one-case/one-payload scientific verdict preserved; no fresh scientific approval of unrelated cases/owners.','input_hashes':{str(p.relative_to(R)):h(p) for p in paths},'case_id':cid,'proposal_id':pid,'final_case_canonical_sha256':canon(fd),'final_proposal_canonical_sha256':canon(fp),'selected_payload_sha256':fp['after_capture']['sha256'],'checks':checks,'all_passed':True,'case_continuity':caseproof,'payload_continuity':payloadproof,'counts':{'cases':len(nd),'changed_cases':sum(x!=y for x,y in zip(od,nd)),'proposals':len(np),'changed_payloads':sum(x['after_capture']!=y['after_capture'] for x,y in zip(op,np)),'unchanged_payloads':112,'occurrence_ids':320,'historical_evidence_exact_prefix':len(oe),'final_evidence':len(ne)},'actual_readback':'Read the entire final Plain Flour case and proposal, all seven appended evidence rows, the selection, and the complete historical-review referral. The latter correctly disavows the unsupported historical supermarket quotation; it does not add a product identity. Final source/material reasoning equals the independently reviewed author scientific content.','lineage_scope':'Parsed and programmatically compared every case/proposal/evidence-prefix object and rehashed all selected and predecessor payloads. A first exploratory full-lineage console print was truncated; no claim of rereading unrelated scientific records is based on that output.','limitations':['Schema/native/SSSOM/full-overlay validation remains the root and separate technical reviewer scope.','One changed case and payload were actually scientifically reassessed; 187 cases and112 other payloads receive continuity checks only.','Original source/owner/role/export holds, failed TSB admission and pending coordinator acceptance remain.','No original review, author data, public index or maintained file was modified.']}
p=O/'final-bindings.json';assert not p.exists();p.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'path':str(p.relative_to(R)),'sha256':h(p),'checks':len(checks),'counts':receipt['counts']}))
