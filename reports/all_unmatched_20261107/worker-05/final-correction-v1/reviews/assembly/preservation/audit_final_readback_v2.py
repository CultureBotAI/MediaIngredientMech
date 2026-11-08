from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,subprocess,collections,yaml

W=Path.cwd();C=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
B=W/'reports/all_unmatched_20261107/worker-05';P=B/'final-correction-v1';N=B/'correction-1193-v1'
S=W/'.temp/w05-final-correction-v1';F=W/'.temp/final-preparation-comparison-v1';O=S/'review-assembly/preservation'
H='43f7cf6e8681fa617b5d6d3529d94d537ca01f0d';WHO='/root/final_skeptical/preservation_audit'
errors=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def objsha(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def load(p):return json.loads(p.read_text())
def check(v,msg):
 if not v:errors.append(msg)
def save(n,x):
 p=O/n;assert not p.exists(),p;p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def git(*args):return subprocess.run(['git',*args],check=True,capture_output=True).stdout
def rows(path,key):return load(path)[key]
def capture(c):return (B if c['root']=='artifact' else C/'queue/preliminary-v5')/c['path']
core_hashes={p.name:sha(p) for p in sorted((P/'core').glob('*.json'))}
ds=rows(P/'core/decisions.json','decisions');ps=rows(P/'core/proposals.json','proposals');es=rows(P/'core/evidence.json','evidence');ls=rows(P/'core/proposal-lineage.json','rows')
od=rows(N/'decisions.json','decisions');op=rows(N/'proposals.json','proposals');oe=rows(N/'evidence.json','evidence')
oldD={x['case_id']:x for x in od};oldP={x['proposal_id']:x for x in op};newP={x['proposal_id']:x for x in ps};newE={x['evidence_id']:x for x in es}

# Authenticate the frozen shard and historical manifest directly against original Git bytes again.
git_auth=[]
for f in [B/'contracts/shard-05.json',N/'MANIFEST.sha256']:
 old=git('show',H+':'+str(f.relative_to(W)))
 check(old==f.read_bytes(),'Git-authenticated artifact differs: '+str(f))
 git_auth.append(dict(path=str(f.relative_to(W)),sha256=sha(f),source_head=H,exact=old==f.read_bytes()))
ownership={};caseobjects={};shardbindings=[]
for f in sorted((C/'queue/preliminary-v5/shards').glob('shard-*.json')):
 x=load(f);shardbindings.append(dict(path=str(f),sha256=sha(f),worker=x['worker_slot'],cases=len(x['cases'])))
 for c in x['cases']:
  check(c['case_id'] not in ownership,'Duplicate campaign case '+c['case_id'])
  ownership[c['case_id']]=dict(worker=x['worker_slot'],case_input_sha256=objsha(c));caseobjects[c['case_id']]=c
check(ownership==load(O/'campaign-ownership.json')['ownership'],'Campaign case bytes or ownership differ from first audit')
assigned={k for k,v in ownership.items() if v['worker']==5}
check({d['case_id'] for d in ds}==assigned==set(oldD),'Final decision case-set differs')
check(len(ds)==len({d['case_id'] for d in ds}),'Duplicate final case')
casechecks=[]
for d in ds:
 cid=d['case_id'];raw=caseobjects[cid];old=oldD[cid]
 unchanged={k:d.get(k)==old.get(k) for k in ['case_input_sha256','source','occurrence_ids','preserved_downstream_holds']}
 check(all(unchanged.values()),'Source case fields changed '+cid)
 check(d['case_input_sha256']==objsha(raw),'Raw case SHA differs '+cid)
 check(set(d['occurrence_ids'])=={x['occurrence_id'] for x in raw.get('occurrences',[])},'Raw occurrence set differs '+cid)
 check({k:v for k,v in d.get('preserved_source_holds',{}).items() if k!='policy'}=={k:v for k,v in old.get('preserved_source_holds',{}).items() if k!='policy'},'Substantive source holds changed '+cid)
 check(all(i in newP for i in d['proposal_ids']),'Missing proposal linkage '+cid)
 check(all(i in newE for i in d['evidence_ids']),'Missing evidence linkage '+cid)
 casechecks.append(dict(case_id=cid,case_input_sha256=d['case_input_sha256'],occurrence_ids=d['occurrence_ids'],source= d['source'],preserved_fields=unchanged))
check(len(newP)==len(ps)==len(ls),'Proposal or lineage duplicate')
seen=[];lineagechecks=[]
for lin in ls:
 pid=lin['proposal_id'];p=newP[pid];pp=capture(p['after_capture'])
 check(sha(pp)==p['after_capture']['sha256'],'Payload hash differs '+pid)
 check(lin['successor_after_capture']==p['after_capture'],'Lineage selected capture differs '+pid)
 check(set(p['case_ids'])<=assigned,'Proposal claims foreign case '+pid)
 before=p.get('before_sha256')
 if before:check(sha(W/p['owner_path'])==before,'Before owner differs '+pid)
 oid=lin.get('predecessor_proposal_id')
 rec=dict(proposal_id=pid,predecessor_proposal_id=oid,selected_capture=p['after_capture'],before_sha256=before,owner_path=p['owner_path'])
 if oid:
  seen.append(oid);old=oldP[oid]
  check(lin['predecessor_proposal_sha256']==objsha(old),'Predecessor object differs '+pid)
  check(old['before_sha256']==before and old['owner_path']==p['owner_path'],'Predecessor owner identity changed '+pid)
  check(lin['predecessor_after_capture']==old['after_capture'],'Predecessor capture differs '+pid)
  oldy=yaml.safe_load(capture(old['after_capture']).read_text());newy=yaml.safe_load(pp.read_text());history=oldy.get('curation_history',[])
  historyok=newy.get('curation_history',[])[:len(history)]==history
  negatives=[v for v in oldy.get('synonyms',[]) if v.get('synonym_type')=='REJECTED_LABEL'];negok=all(v in newy.get('synonyms',[]) for v in negatives)
  check(historyok and negok,'History or inherited negative changed '+pid)
  rec.update(history_prefix_preserved=historyok,inherited_negative_objects_preserved=negok)
 lineagechecks.append(rec)
check(len(seen)==len(set(seen))==len(oldP) and set(seen)==set(oldP),'Original selected proposal lineage not one-to-one')

capturechecks=[]
for e in es:
 c=e['capture'];f=capture(c);got=sha(f) if f.is_file() else None
 check(got==c['sha256'],'Evidence capture changed/missing '+e['evidence_id'])
 check(set(e.get('case_ids',[]))<=assigned,'Evidence claims foreign case '+e['evidence_id'])
 capturechecks.append(dict(evidence_id=e['evidence_id'],capture=c,actual_sha256=got))
check({e['evidence_id'] for e in oe}<=set(newE),'Old evidence ID omitted')
for e in oe:
 n=newE[e['evidence_id']]
 for k in ['capture','url','accessed_at']:check(e.get(k)==n.get(k),'Original evidence provenance changed '+e['evidence_id']+' '+k)

# Exact public review files and their immutable private source copies.
reviewchecks=[]
bindings=load(P/'control/final-review-bindings.json')
for lane,r in bindings.items():
 public=W/r['path'];private=S/('review-'+lane)/public.name;got=sha(public)
 check(got==r['sha256'],'Public scientific review SHA differs '+lane)
 check(private.read_bytes()==public.read_bytes(),'Public/private scientific review copy differs '+lane)
 e=newE[r['evidence_id']]
 check(e['capture']['sha256']==got and capture(e['capture'])==public,'Scientific review evidence binding differs '+lane)
 content=load(public)
 case_ids={x['case_id'] for x in content['case_reviews']}
 check(case_ids==set(e['case_ids']),'Scientific review evidence case scope differs '+lane)
 reviewchecks.append(dict(lane=lane,reviewer=r['reviewer'],path=r['path'],sha256=got,private_path=str(private.relative_to(W)),cases=len(content['case_reviews']),payloads=len(content['payload_reviews']),copy_exact=True))

# Read parent's preservation summary and independently repeat its inventories.
parent=load(P/'validation/final-preservation.json');inventorychecks=[]
for entry in parent['inventories']:
 path=W/entry['inventory'];check(sha(path)==entry['inventory_sha256'],'Parent inventory SHA differs '+str(path));x=load(path)
 inventorychecks.append(dict(path=entry['inventory'],sha256=sha(path),parent_verified_members=entry['verified_members']))
protected=load(S/'control/protected-inputs.json')['inputs']
for x in protected:check(sha(Path(x['path']))==x['sha256'],'Protected input differs '+x['path'])
owners=load(S/'control/maintained-baseline-preservation-start.json')['records']
actualowners={str(x.relative_to(W)) for x in (W/'data/ingredients').rglob('*.yaml')}
check(actualowners=={r['path'] for r in owners},'Maintained owner file set differs')
for r in owners:check(sha(W/r['path'])==r['sha256'],'Maintained owner bytes differ '+r['path'])
oldmembers=[]
for line in (N/'MANIFEST.sha256').read_text().splitlines():
 digest,rel=line.split(None,1);rel=rel.lstrip('*');got=sha(N/rel);check(got==digest,'Old manifest member differs '+rel);oldmembers.append(dict(path=rel,sha256=got))
fm=load(F/'MANIFEST.json');comparisonmembers=[]
for r in fm['files']:
 got=sha(F/r['path']);check(got==r['sha256'],'Private comparison member differs '+r['path']);comparisonmembers.append(dict(path=r['path'],sha256=got))
check({str(p.relative_to(F)) for p in F.rglob('*') if p.is_file()}=={r['path'] for r in fm['files']}|{'MANIFEST.json'},'Private comparison file inventory differs')
check(sha(F/'MANIFEST.json')==load(O/'PRESERVATION-RECEIPT.json')['comparison']['manifest_sha256'],'Private comparison manifest differs')
check(all(sha(O/x['path'])==x['sha256'] for x in load(O/'MANIFEST.json')['files']),'First preservation audit seal changed')

head=git('rev-parse','HEAD').decode().strip();branch=git('branch','--show-current').decode().strip();status=git('status','--porcelain=v1').decode();diff=git('diff','--name-status',H,'--').decode()
check(head==H,'Current source head differs');check(not diff,'Tracked bytes differ from original source head')
check(core_hashes=={p.name:sha(p) for p in sorted((P/'core').glob('*.json'))},'Core changed during independent readback')
save('FINAL-PRESERVATION-DETAILS-v2.json',dict(reviewer=WHO,core_hashes=core_hashes,case_checks=casechecks,lineage_checks=lineagechecks,evidence_capture_checks=capturechecks,scientific_review_copy_checks=reviewchecks,parent_inventory_checks=inventorychecks,authenticated_source_head_artifacts=git_auth))
receipt=dict(reviewer=WHO,completed_at=datetime.now(timezone.utc).isoformat(),scope='Final mechanical preservation readback only; no independent chemical/source-applicability judgment',source_head=head,branch=branch,git_diff_from_original_head=diff,git_status=status,git_status_interpretation='New untracked native report output is recorded; it is not a maintained tracked-source edit.',core_hashes=core_hashes,counts=dict(final_cases=len(ds),final_proposals=len(ps),final_evidence=len(es),original_proposals_accounted=len(seen),additional_proposals=len(ps)-len(seen),campaign_cases=len(ownership),worker05_cases=len(assigned),maintained_owner_files=len(owners),historical_manifest_members=len(oldmembers),comparison_manifest_members=len(comparisonmembers),comparison_families=fm['counts']['families'],scientific_review_cases=sum(r['cases'] for r in reviewchecks),scientific_review_payloads=sum(r['payloads'] for r in reviewchecks)),parent_preservation=dict(path=str((P/'validation/final-preservation.json').relative_to(W)),sha256=sha(P/'validation/final-preservation.json'),status=parent['status'],independent_agreement=not errors),scientific_review_bindings=reviewchecks,first_audit_preserved=True,errors=errors,status='PASS' if not errors else 'FAIL',limits=['Hash/count/lineage agreement is not chemical or source-applicability approval.','Native review semantics and final integration acceptance belong to the parent reviewer/coordinator.','All evidence paths were checked at their actual public artifact or frozen source roots; no private-path fallback concealed missing published captures.'])
save('FINAL-PRESERVATION-RECEIPT-v2.json',receipt)
names=['audit_final_readback_v2.py','FINAL-PRESERVATION-DETAILS-v2.json','FINAL-PRESERVATION-RECEIPT-v2.json']
save('MANIFEST-v2.json',dict(reviewer=WHO,completed_at=receipt['completed_at'],predecessor_manifest_sha256=sha(O/'MANIFEST.json'),files=[dict(path=n,sha256=sha(O/n),bytes=(O/n).stat().st_size) for n in names]))
print(json.dumps(dict(status=receipt['status'],errors=errors,counts=receipt['counts'],receipt_sha256=sha(O/'FINAL-PRESERVATION-RECEIPT-v2.json'),manifest_sha256=sha(O/'MANIFEST-v2.json')),indent=2))
