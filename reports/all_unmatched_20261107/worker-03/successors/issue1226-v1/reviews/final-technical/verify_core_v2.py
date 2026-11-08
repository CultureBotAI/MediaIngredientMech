"""Detached independent exact final-core accounting, no scientific reapproval."""
from pathlib import Path
import collections,datetime,hashlib,json,subprocess
R=Path.cwd();A=R/'reports/all_unmatched_20261107/worker-03';O=A/'successors/issue1226-v1';B=A/'successors/issue1224-v1/publication-v1';T=R/'.temp/w03-provenance-successor-v1/technical';OUT=T/'final-core-v1';SOURCE=R.parents[2]/'queue/preliminary-v5'
sha=lambda b:hashlib.sha256(b).hexdigest()
can=lambda v:json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()
read=lambda p:json.loads(p.read_bytes())
cache={}
def digest(p):
 assert p.is_file() and not p.is_symlink(),str(p)
 if p not in cache:cache[p]=sha(p.read_bytes())
 return cache[p]
def capture(c):
 root={'artifact':A,'source':SOURCE}[c['root']];path=Path(c['path']);assert not path.is_absolute() and '..' not in path.parts
 p=root/path;assert digest(p)==c['sha256'];return p
oldcases=read(B/'decisions.json');newcases=read(O/'decisions.json');assert (B/'decisions.json').read_bytes()==(O/'decisions.json').read_bytes();assert digest(O/'decisions.json')=='a9984b5afbab4eaecffc8fe73ff4e0b217974626f8cb96fec469980b6a5dd220'
cases={x['case_id']:x for x in newcases['decisions']};assert len(cases)==len(newcases['decisions'])==188
shard_path=SOURCE/'shards/shard-03.json';shard=read(shard_path);frozen={x['case_id']:x for x in shard['cases']};assert len(frozen)==188 and set(frozen)==set(cases);assert digest(shard_path)==newcases['shard_sha256']=='90d5d5df1ae9609c08593c93216d78449f6ac2781f1d5e7e95695751fdd0c228'
oldprops=read(B/'proposals.json')['proposals'];newprops=read(O/'proposals.json')['proposals'];oldp={x['proposal_id']:x for x in oldprops};newp={x['proposal_id']:x for x in newprops};assert len(newprops)==len(newp)==74 and set(newp)==set(oldp)
oldevidence=read(B/'evidence.json')['evidence'];newevidence=read(O/'evidence.json')['evidence'];olde={x['evidence_id']:x for x in oldevidence};newe={x['evidence_id']:x for x in newevidence};assert len(oldevidence)==len(olde)==863 and len(newevidence)==len(newe)==868;assert newevidence[:863]==oldevidence
original_evidence=read(A/'evidence.json')['evidence'];assert len(original_evidence)==852 and all(newe[e['evidence_id']]==e for e in original_evidence)
new_ids=set(newe)-set(olde);assert new_ids=={'w03-prov-1226-payload-bridge','w03-prov-1226-independent-review','w03-prov-1246-controls','w03-prov-1226-retention','w03-prov-1246-repair'}
bridges={b['proposal_id']:b for b in read(O/'payload-bridge.json')['entries']};assert len(bridges)==49
candidate=read(T/'candidate-payload-review-v1.json');candidate_rows={x['proposal_id']:x for x in candidate['payloads']};assert len(candidate_rows)==74
for x in candidate['artifacts']:
 p=Path(x['path']);p=p if p.is_absolute() else R/p;assert digest(p)==x['sha256']
ledger=read(O/'machine-ledger.json');case_ledger={x['case_id']:x for x in ledger['case_rows']};prop_ledger={x['proposal_id']:x for x in ledger['proposal_rows']};assert len(case_ledger)==len(ledger['case_rows'])==188 and len(prop_ledger)==len(ledger['proposal_rows'])==74
case_rows=[]
for cid,d in cases.items():
 assert sha(can(frozen[cid]))==d['case_input_sha256'];assert all(pid in newp and cid in newp[pid]['case_ids'] for pid in d['proposal_ids']);assert all(eid in newe for eid in d['evidence_ids']);assert all(eid in newe for eid in d['independent_review']['evidence_ids'])
 q=case_ledger[cid];assert q['case_input_sha256']==d['case_input_sha256'] and q['unchanged_decision_object_sha256']==sha(can(d)) and q['disposition']==d['disposition'] and q['proposal_ids']==d['proposal_ids']
 case_rows.append({'case_id':cid,'frozen_case_sha256':sha(can(frozen[cid])),'decision_object_sha256':sha(can(d)),'disposition':d['disposition'],'proposal_ids':d['proposal_ids'],'historical_review_and_holds_object_retained':True})
proposal_rows=[]
for pid,p in newp.items():
 old=oldp[pid];b=bridges.get(pid);delta=[k for k in sorted(set(old)|set(p)) if old.get(k)!=p.get(k)];assert delta==(['after_capture','evidence_ids','independent_review'] if b else [])
 assert all(p[k]==old[k] for k in ['kind','case_ids','owner_path','before_sha256']);path=capture(p['after_capture']);assert str(path.relative_to(R))==candidate_rows[pid]['selected_path'] and digest(path)==candidate_rows[pid]['selected_sha256']
 assert all(cid in cases and pid in cases[cid]['proposal_ids'] for cid in p['case_ids']);assert all(eid in newe for eid in p['evidence_ids']);assert all(eid in newe for eid in p['independent_review']['evidence_ids'])
 if b:
  assert old==b['original_proposal'] and p['after_capture']==b['after_capture'];assert p['evidence_ids']==old['evidence_ids']+['w03-prov-1226-payload-bridge','w03-prov-1226-independent-review','w03-prov-1246-controls'];ir=p['independent_review'];assert ir['reviewed_after_sha256']==digest(path) and ir['reviewer']=='/root/provenance_review' and ir['technical_reviewer']=='/root/provenance_controls' and ir['scientific_review'] is False
  assert ir['historical_review_locator']=='payload-bridge.json entries[proposal_id='+pid+'].original_proposal.independent_review'
 else:assert p==old and p['after_capture']==old['after_capture']
 q=prop_ledger[pid];assert q['original_proposal_sha256']==sha(can(old)) and q['successor_proposal_sha256']==sha(can(p)) and q['changed_fields']==delta and q['old_payload']==old['after_capture'] and q['new_payload']==p['after_capture'];assert all(q[k]==p[k] for k in ['kind','owner_path','before_sha256','case_ids'])
 proposal_rows.append({'proposal_id':pid,'current_object_sha256':sha(can(p)),'prior_object_sha256':sha(can(old)),'changed_fields':delta,'selected_payload_path':str(path.relative_to(R)),'selected_payload_sha256':digest(path),'authentic_origin_fields_unchanged':True,'historical_review_retained':True,'scientific_reapproval':False})
assert 'b-proposal-cm0149-form' not in newp
assert newp['w03-oxoid-cm0149-product-1224-v1']==oldp['w03-oxoid-cm0149-product-1224-v1']
changed_cases={cid for pid in bridges for cid in newp[pid]['case_ids']};assert len(changed_cases)==68
evidence_rows=[]
for e in newevidence:
 p=capture(e['capture']);assert all(cid in cases for cid in e.get('case_ids',[]))
 if e['evidence_id'] in new_ids:assert set(e['case_ids'])==changed_cases and e['kind'] in ['local_validation','independent_review']
 evidence_rows.append({'evidence_id':e['evidence_id'],'object_sha256':sha(can(e)),'capture_path':str(p),'capture_sha256':digest(p),'inherited_exact_object':e['evidence_id'] in olde})
# Archived technical sources are exact regular bytes; negative-control links stay descriptors only.
archives=[]
for name,expected in [('technical-review-archive.json',50),('provenance-review-archive.json',None)]:
 d=read(O/'validation'/name);assert d['file_count']==len(d['files']);assert expected is None or d['file_count']==expected;assert d['symlinks_installed']==0
 for x in d['files']:assert digest(R/x['source_path'])==digest(R/x['archived_path'])==x['sha256']
 archives.append({'receipt':name,'sha256':digest(O/'validation'/name),'regular_files':d['file_count'],'symlink_descriptors':len(d.get('symlink_descriptors',[]))})
assert not any(p.is_symlink() for p in (O/'reviews').rglob('*'))
assert digest(T/'HANDOFF-v1.json')==digest(O/'reviews/technical/HANDOFF-v1.json')=='da60cf37b037e33562eb351f2ecbb1695557e31d2fab9d728fd7f1c59ab25c4b'
techmanifest=read(T/'MANIFEST-v1.json')
for x in techmanifest['files']:assert digest(T/x['path'])==digest(O/'reviews/technical'/x['path'])==x['sha256']
review=read(O/'reviews/provenance/payload-phase-v2/HANDOFF.json');assert review['scientific_review'] is False and review['complete_payload_count']==74 and review['reviewed_predecessor_head']=='f6bfbf3c185f705484aa106405f813209146c766';assert len(review['all49'])==49 and {x['proposal_id'] for x in review['all49']}==set(bridges)
for x in review['all49']:assert x['new_sha256']==bridges[x['proposal_id']]['after_payload_sha256'] and x['old_sha256']==bridges[x['proposal_id']]['before_payload_sha256']
structural=read(O/'validation/structural-audit.json');assert structural['structural_accounting']=='PASS' and structural['accounted_case_count']==structural['assigned_shard_case_count']==188 and structural['proposal_count']==74 and structural['evidence_count']==868 and structural['scientific_adequacy_or_approval_established'] is False
assert set(structural['accounted_case_ids'])==set(cases) and structural['out_of_scope_shard_case_ids']==[]
for path,h in structural['input_hashes'].items():assert digest(Path(path))==h
preservation=read(O/'validation/complete-preservation.json');assert preservation['status']=='PASS' and preservation['scientific_approval'] is False and preservation['decisions_sha256']==digest(O/'decisions.json')
for k,v in [('case_count',188),('proposal_count',74),('changed_payload_count',49),('unchanged_payload_count',25),('prior_evidence_count',863),('evidence_count',868)]:assert ledger[k]==v
maintained=read(T/'maintained-inventory-before.json');assert all(digest(R/x['path'])==x['sha256'] for x in maintained['baseline_files'])
head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip();assert head=='f6bfbf3c185f705484aa106405f813209146c766'
for n in ['decisions.json','proposals.json','evidence.json']:assert subprocess.check_output(['git','show',head+':'+str((B/n).relative_to(R))])==(B/n).read_bytes()
report={'reviewer':'/root/provenance_controls','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS_EXACT_FINAL_CORE_ACCOUNTING','source_state':'working_tree successor with exact published predecessor rechecked; no successor commit/head attestation','predecessor_head':head,'scope':'Detached technical accounting followup to candidate HANDOFF-v1. Covers all188 frozen case inputs/outcomes,74 proposal pointers/origins,868 evidence captures and reviewer archives. Exact metadata-only acceptance; source scientific claims/holds inherited unchanged, not independently reapproved.','counts':{'cases':188,'proposals':74,'changed':49,'unchanged':25,'evidence':868,'prior_evidence_objects_retained':863,'original_evidence_objects_retained':852,'new_evidence_objects':5,'cases_with_metadata_corrected_payloads':68,'structural_recorded_input_hashes_rechecked':len(structural['input_hashes']),'maintained_baseline_hashes_rechecked':len(maintained['baseline_files'])},'core_hashes':{n:digest(O/n) for n in ['decisions.json','proposals.json','evidence.json']},'case_coverage':case_rows,'proposal_coverage':proposal_rows,'evidence_coverage':evidence_rows,'archival_checks':archives,'native_structural_receipt':{'path':str((O/'validation/structural-audit.json').relative_to(R)),'sha256':digest(O/'validation/structural-audit.json'),'status':'PASS','direct_input_hash_rechecks':len(structural['input_hashes']),'limitations':structural['limitations'],'rerun':'Not repeated; independent full direct pointer/case/hash checks above; native schema/partonomy candidate checks remain exact unchanged payloads.'},'prior_candidate_handoff':{'path':str((T/'HANDOFF-v1.json').relative_to(R)),'sha256':digest(T/'HANDOFF-v1.json')},'limitations':['No new chemistry, form, stock, quantity, identity, owner, role, source or supported-export approval.','Final complete release/transport manifest and successor published head are later root-owned sealing steps, not attested here.','All written review outputs remain only within private technical/final-core-v1/.'],'input_hashes':[{'path':str(p.relative_to(R)) if p.is_relative_to(R) else str(p),'sha256':digest(p)} for p in [O/'decisions.json',O/'proposals.json',O/'evidence.json',O/'machine-ledger.json',O/'validation/complete-preservation.json',O/'validation/structural-audit.json',O/'payload-bridge.json',O/'reviews/technical/HANDOFF-v1.json',O/'reviews/provenance/payload-phase-v2/HANDOFF.json',shard_path]]}
with (OUT/'assessment.json').open('x') as f:json.dump(report,f,indent=2,ensure_ascii=False);f.write('\n')
print(json.dumps({'status':report['status'],'counts':report['counts'],'core_hashes':report['core_hashes'],'assessment_sha256':sha((OUT/'assessment.json').read_bytes())},indent=2))
