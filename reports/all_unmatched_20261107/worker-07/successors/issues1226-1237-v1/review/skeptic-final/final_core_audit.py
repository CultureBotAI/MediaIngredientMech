from pathlib import Path
import json,hashlib,datetime,copy
R=Path('reports/all_unmatched_20261107/worker-07');N=R/'successors/issues1226-1237-v1';S=Path('.temp/worker07-issues1226-1237-v1/skeptic')
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bind(p):return {'path':str(p),'sha256':sha(p)}
selector=read(N/'SELECTOR.json')
for v in selector['ledgers'].values():assert sha(R/v['path'])==v['sha256']
Dp=read(N/'draft-v1/decisions.json')['decisions'];Df=read(N/'decisions.json')['decisions'];Do=read(R/'successors/issue1203-v1/decisions.json')['decisions'];Pp=read(N/'draft-v1/proposals.json')['proposals'];Pf=read(N/'proposals.json')['proposals'];Ep=read(N/'draft-v1/evidence.json')['evidence'];Ef=read(N/'evidence.json')['evidence'];Eo=read(R/'successors/issue1203-v1/evidence.json')['evidence'];assert Ef[:len(Ep)]==Ep;assert Ef[:len(Eo)]==Eo;assert len(Ef)==1503
changed=[]
for a,b,o in zip(Dp,Df,Do):
 assert a['case_id']==b['case_id']==o['case_id']
 if a!=b:
  assert {k for k in a.keys()|b.keys() if a.get(k)!=b.get(k)}=={'evidence_ids','independent_review'}
  assert b['independent_review']['status']=='complete'; assert b['evidence_ids'][:len(a['evidence_ids'])]==a['evidence_ids']; assert 'Not whole-owner/role/export approval' in b['independent_review']['scope'];changed.append(b['case_id'])
assert len(changed)==8;assert sum(a==b for a,b in zip(Do,Df))==180
for a,b in zip(Pp,Pf):
 assert set(a).issubset(b);assert {k for k in b if a.get(k)!=b[k]}=={'successor_review_bindings'}
 assert sha(R/b['after_capture']['path'])==b['after_capture']['sha256'];assert b['after_capture']==a['after_capture'];assert b['successor_review_bindings']['metadata_full_diff']['sha256']==sha(S/'independent-skeptical-draft-review-v1.json')
 if 'source_science' in b['successor_review_bindings']:assert b['successor_review_bindings']['source_science']['sha256']==sha(N/'review/science/independent-science-review-v1.json')
for e in Ef[len(Ep):]:assert sha(R/e['capture']['path'])==e['capture']['sha256'];assert set(e['case_ids'])==set(changed)
strict=read(N/'validation/strict-final.json');assert strict['structural_accounting']=='PASS';assert strict['accounted_case_count']==188;assert strict['independent_review_status_counts']=={'complete':188};hashed=[]
for name,digest in strict['input_hashes'].items():
 p=Path(name);assert sha(p)==digest,name;hashed.append({'path':name,'sha256':digest})
lineage=read(N/'native-review-lineage.json')
for a in lineage['attempts']:
 for field in ['input','validation']:assert sha(R/a[field]['path'])==a[field]['sha256']
 result=read(R/a['validation']['path']);assert result['returncode']==a['exit_code']
assert sha(R/lineage['actual_saved_receipt']['path'])==lineage['actual_saved_receipt']['sha256']
x={'reviewer':'/root/successor1226_1237_skeptic','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'FINAL_CORES_EXACT_DRAFT_BRIDGE_PASS_PENDING_HANDOFF_AND_NATIVE_INTEGRITY_CHECK','selector':bind(N/'SELECTOR.json'),'final_cores':[bind(N/x) for x in ['decisions.json','evidence.json','proposals.json']],'draft_payloads_unchanged':100,'final_decision_changes_from_reviewed_draft':'Only8actualreview attachments; allscientificwording/scope/holds identical','original_case_objects_unchanged':180,'all_case_ids_digests_occurrences_dispositions_preserved':True,'evidence_original_prefix_preserved':1498,'evidence_draft_prefix_preserved':1500,'final_evidence':1503,'strict_auditor_inputs_rehashed':len(hashed),'strict_auditor_inputs':hashed,'strict_final':bind(N/'validation/strict-final.json'),'native_attempt_lineage':bind(N/'native-review-lineage.json'),'native_failure_accounting':'v1invalidissue_key;v2missingaction;v3validate/savepassed. Legacyfailed_v1_retained key points tov2andisexplicitlycorrectedin immutable lineage. No new payload bytes or review timing invented.','approval':'Bounded report-only assembly. Originalsourcecases, wholeowners, roles,exports, cross-shardunionsandrelease remain separate.'}
f=S/'final-core-binding-v1.json';assert not f.exists();f.write_text(json.dumps(x,indent=2)+'\n');print({'path':str(f),'sha256':sha(f),'strict_inputs':len(hashed)})
