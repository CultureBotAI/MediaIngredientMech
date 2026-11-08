"""Exact final selected-core binding checks; no scientific or native rerun."""
import hashlib,json,datetime,subprocess,traceback
from pathlib import Path
R=Path.cwd(); A=R/'reports/all_unmatched_20261107/worker-08'
O=A/'successors/issue-1237-mc-dependent-v1'; OLD=A/'successors/issue-1237-tenvit-v1'
P=R/'.temp/mc-dependent-successor-v1/final-review'
CID='CM_NAME:d57e91ffaea6f0ab6ff0f3d6f0b04c26356c832e85dd83e9e2319874fda43506'
PID='mc1237-prop-mc-vitamins-dependent'
CHECKS=[]; INPUTS={}
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def canonical(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def check(ok,description):
 if not ok:raise AssertionError(description)
 CHECKS.append(description)
def read(p):
 INPUTS[str(p)]=sha(p);return json.loads(Path(p).read_text())
def capture(ref):
 check(ref['root']=='artifact','artifact capture scope')
 p=A/ref['path']; check(p.is_file() and not p.is_symlink() and p.resolve().is_relative_to(A.resolve()),'regular artifact capture '+ref['path'])
 check(sha(p)==ref['sha256'],'exact capture '+ref['path']); INPUTS[str(p)]=sha(p); return p
def main():
 selection=read(O/'selection.json')
 check(sha(O/'selection.json')=='33f0f1f5166e75283a3e0488f6172844002919cc2461a04f2089f8c4f8fedab8','final exact selector')
 for ref in selection['authoritative_inputs'].values():capture(ref)
 for key in ['predecessor_selection','payload','dependency','effective_source_ref_index','thesis_publication_scope']:capture(selection[key])
 newp=read(O/'proposals.json')['proposals'];oldp=read(OLD/'proposals.json')['proposals']
 newd=read(O/'decisions.json')['decisions'];oldd=read(OLD/'decisions.json')['decisions']
 newe=read(O/'evidence.json')['evidence'];olde=read(OLD/'evidence.json')['evidence']
 check(len(newp)==115 and len(oldp)==114 and newp[:-1]==oldp,'all114 ordered original proposal objects exact plus one')
 check(newp[-1]['proposal_id']==PID,'new dependent is sole added proposal')
 check(len(newd)==len(oldd)==188 and [x['case_id'] for x in newd]==[x['case_id'] for x in oldd],'188 identical ordered case IDs')
 dm={x['case_id']:x for x in newd};oldm={x['case_id']:x for x in oldd};pm={x['proposal_id']:x for x in newp}
 check(len(dm)==188 and len(pm)==115,'unique cases and proposals')
 for cid,d in dm.items():
  check(cid==CID or d==oldm[cid],'unchanged source decision '+cid)
  for key in ['case_input_sha256','source','occurrence_ids']:check(d[key]==oldm[cid][key],'preserved frozen '+key+' '+cid)
 occurrences=[o for d in newd for o in d['occurrence_ids']]
 check(len(occurrences)==len(set(occurrences))==320,'320 exact unique occurrence IDs')
 check(len(newe)==1114 and len(olde)==1101 and newe[:1101]==olde,'all1101 prior evidence objects exact prefix')
 eids={e['evidence_id'] for e in newe};check(len(eids)==1114,'unique1114 evidence IDs')
 for p in newp:
  capture(p['after_capture'])
  check(set(p['case_ids'])<=set(dm) and set(p['evidence_ids'])<=eids,'proposal backreferences '+p['proposal_id'])
 for d in newd:check(set(d['evidence_ids'])<=eids and set(d['proposal_ids'])<=set(pm),'case backreferences '+d['case_id'])
 for e in newe[1101:]:capture(e['capture']);check(e['case_ids']==[CID],'new evidence exact case scope '+e['evidence_id'])
 ap=read(O/'author/proposal.json');ad=read(O/'author/decision.json')
 check({k:v for k,v in pm[PID].items() if k!='evidence_ids'}=={k:v for k,v in ap.items() if k!='evidence_ids'},'final proposal only evidence metadata append')
 check(pm[PID]['evidence_ids'][:len(ap['evidence_ids'])]==ap['evidence_ids'],'proposal evidence prefix')
 check({k:v for k,v in dm[CID].items() if k not in ['evidence_ids','independent_review']}=={k:v for k,v in ad.items() if k not in ['evidence_ids','independent_review']},'final changed case only evidence/peer metadata updates')
 check(dm[CID]['evidence_ids'][:len(ad['evidence_ids'])]==ad['evidence_ids'],'case evidence prefix')
 check(dm[CID]['independent_review']=={'status':'complete','evidence_ids':['mc1237-science','mc1237-lineage']},'actual separate peer bookkeeping')
 peers={}
 for name,ref in selection['independent_reviews'].items():
  path=capture(ref); peer=read(path);peers[name]=peer
  check(peer['case_ids']==[CID] and peer['proposal_ids']==[PID],'peer exact reviewed scope '+name)
  check(peer['payload_hashes'][PID]==pm[PID]['after_capture']['sha256'],'peer exact payload '+name)
  check(peer['case_hashes'][CID]==canonical(ad),'peer author-stage case canonical digest '+name)
  check(not peer['open_blocking_findings'],'peer no open blocker '+name)
 check(peers['science']['reviewer_identity']=='worker08:/root/organics' and peers['science']['author_identity']=='worker08:/root','science authorship separation')
 check(peers['lineage']['reviewer']=='worker08:/root/vitamins' and peers['lineage']['author']=='worker08:/root','lineage authorship separation')
 check(peers['science']['full_payload_review'] is True and peers['lineage']['full_payload_read'] is True,'actual whole payload peer scopes')
 lin=read(O/'lineage.json')
 check(lin['counts']==selection['counts'],'lineage count claims')
 for row in lin['cases']:
  cid=row['case_id'];check(row['before_sha256']==canonical(oldm[cid]) and row['after_sha256']==canonical(dm[cid]),'case lineage '+cid)
  check(row['unchanged']==(cid!=CID),'case lineage disposition '+cid)
 for row in lin['payloads']:
  pid=row['proposal_id'];check(row['selected_capture']==pm[pid]['after_capture'] and row['original_before_sha256']==pm[pid]['before_sha256'],'payload lineage '+pid)
  if pid!=PID:check(row['original_proposal_object_sha256']==canonical(pm[pid]) and row['unchanged_proposal_object'] is True and row['unchanged_payload'] is True,'original proposal lineage '+pid)
 check(pm['vm1201-prop-nbrc903-vitamin']['before_sha256'] is None and pm['vm1201-prop-nbrc903-vitamin']['kind']=='new_owner','NBRC903 authentic null-before unchanged')
 check(pm['vm1237-prop-wolfe-cb-dependent']==next(x for x in oldp if x['proposal_id']=='vm1237-prop-wolfe-cb-dependent'),'CB whole proposal unchanged')
 check(pm[PID]['before_sha256']=='59c53dfe4e273ebfc7c3fe86fd4244978868ff1879dcde97af64bbeb61c07123' and pm[PID]['kind']=='edit_existing_owner','new Mc authentic nonnull-before')
 check(selection['cross_owner_routing']=='PENDING_W04_CROSS_OWNER_DECISION' and selection['whole_owner_role_export_approval'] is False and selection['maintained_application'] is False,'routing and approval holds')
 check(selection['prior_TSB_Bacto_admission']=='FAILED/HELD unchanged','prior failed admission retained')
 scope=read(O/'inputs/thesis-publication-scope.json');index=read(O/'inputs/source-ref-index-v2.json')
 relocations={x['previous_unpublished_copy_path']:x for x in scope['relocations']}
 for entry in index['selected_captures']:
  check(sha(entry['original_path'])==entry['sha256'],'original source-copy digest '+entry['original_path'])
  if entry.get('published_path'):
   check(sha(R/entry['published_path'])==entry['sha256'],'current published source-copy digest '+entry['published_path'])
  elif entry.get('private_capture_path'):
   check(sha(entry['private_capture_path'])==entry['sha256'],'private source-copy digest '+entry['private_capture_path'])
  else:raise AssertionError(('unrecognized selected source destination',entry))
 for row in scope['relocations']:
  check(sha(row['private_exact_capture'])==sha(row['original_path'])==row['sha256'],'exact private fulltext preservation')
  check(not (R/row['previous_unpublished_copy_path']).exists() and row['published_full_text'] is False,'fulltext not republished at previous path')
 check(scope['original_acquired_at']=='2026-11-08T09:54:47.947617+00:00','original thesis acquisition time retained')
 check(subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()=='a0190fed72b8f5119432003d1f9c84b8c1de7a48','entry head unchanged')
 result={'status':'PASS_FINAL_SELECTED_CORE_WITH_SCOPE_LIMITS','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':'worker08:/root/inorganics','author':'worker08:/root','selection_sha256':sha(O/'selection.json'),'checks':CHECKS,'counts':selection['counts'],'case_hashes':{cid:canonical(d) for cid,d in dm.items()},'payload_hashes':{pid:p['after_capture']['sha256'] for pid,p in pm.items()},'input_hashes':INPUTS,'technical_receipt':{'path':str(P/'projection-attempt-v3/receipt.json'),'sha256':sha(P/'projection-attempt-v3/receipt.json')},'scope':'Final full core metadata/payload transport, original origins and peer binding only. Scientific conclusions remain those of separate peers. No independent scientific approval of own earlier inorganic proposals. No new source/native test rerun in this script.','source_route_approval':False,'owner_role_export_approval':False,'native_pair':'Pending actual final pair; separate final assembly receipt will bind those exact bytes.'}
 with (P/'selection-bindings.json').open('x') as f:json.dump(result,f,indent=2,ensure_ascii=False);f.write('\n')
 print(json.dumps({'status':result['status'],'checks':len(CHECKS),'receipt_sha256':sha(P/'selection-bindings.json')}))
if __name__=='__main__':
 try:main()
 except BaseException as e:
  with (P/'selection-check-failure.json').open('x') as f:json.dump({'type':type(e).__name__,'message':str(e),'traceback':traceback.format_exc(),'checks':CHECKS},f,indent=2);f.write('\n')
  raise
