from pathlib import Path
import datetime, hashlib, json, subprocess

W=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/workers/w06/worktree')
R=W/'reports/all_unmatched_20261107/worker-06'; S=R/'successor-v5'
O=Path(__file__).parent; A=O.parent; M=A/'final-metadata-residual'
def j(p):return json.loads(Path(p).read_text())
def h(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ch(x):return hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':'),allow_nan=False).encode()).hexdigest()
def ref(p):return {'path':str(p),'sha256':h(p)}
def rows(p,k,ik):return {x[ik]:x for x in j(p)[k]}
def save(n,x):
 p=O/n;assert not p.exists();p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def diff(a,b,p=''):
 if type(a)!=type(b):return [{'path':p,'before':a,'after':b}]
 if isinstance(a,dict):
  out=[]
  for k in sorted(a.keys()|b.keys()):
   q=p+'/'+k.replace('~','~0').replace('/','~1')
   if k not in a:out.append({'path':q,'before_absent':True,'after':b[k]})
   elif k not in b:out.append({'path':q,'before':a[k],'after_absent':True})
   else:out+=diff(a[k],b[k],q)
  return out
 if isinstance(a,list):
  if len(a)!=len(b):return [{'path':p,'before':a,'after':b}]
  return sum((diff(x,y,p+'/'+str(i)) for i,(x,y) in enumerate(zip(a,b))),[])
 return [] if a==b else [{'path':p,'before':a,'after':b}]

manifests=[A/'MANIFEST-science-v1.json',M/'MANIFEST-v1.json',W/'.temp/residual1217-correction-v1/independent-stock/MANIFEST.json',W/'.temp/residual1217-correction-v1/independent-stock-final-binding-v1/MANIFEST.json']
preserved=[]
for p in manifests:
 members=[]
 for x in j(p)['files']:
  f=p.parent/x['path'];assert h(f)==x['sha256'];members.append(ref(f))
 preserved.append({'manifest':ref(p),'verified_member_count':len(members),'members':members})
timing=M/'timing-qualification-v1.json';assert h(timing)=='98f2c67b93bb512afd2540e957a76aaff304ec399aaf363edd187f0dfc63b206'
assert (S/'independent-a5/final-metadata-residual/timing-qualification-v1.json').read_bytes()==timing.read_bytes()
a5=j(A/'final-science-v1.json'); meta=j(M/'final-science-v1.json'); mt=j(M/'fieldtrace-v1.json')
assert h(A/'final-science-v1.json')=='65f7eaf55ede72ae4be6ec435b1d4fd01aaa1915ed9505fdcfec844e6c1566cd'
assert h(M/'final-science-v1.json')=='80c52b74c3e94ad4923812afe8e21cd79f8ae4f7d9572c32eef9409d6ddc6953'
selection=j(S/'selection.json');assert h(S/'selection.json')=='2a8a71a478814d89169122ed3ef6c34ee26bc9ba0d75dbb62d6e349468864348'
for n,x in selection['core'].items():assert h(W/x['path'])==x['sha256']
D=rows(S/'decisions.json','decisions','case_id');P=rows(S/'proposals.json','proposals','proposal_id');E=rows(S/'evidence.json','evidence','evidence_id')
PD=rows(S/'reviewed-draft/proposals.json','proposals','proposal_id');ED=rows(S/'reviewed-draft/evidence.json','evidence','evidence_id')
EA=rows(S/'author-draft/evidence.json','evidence','evidence_id')
binds=[];traces=[]
scopes=[(112,a5['reviewed_full_source_outcome'],'V5-IR-A5',A/'final-science-v1.json')]+[(x['binding']['case_index'],x['complete_after_decision'],'V5-IR-STOCK-META-'+str(x['binding']['case_index']),M/'final-science-v1.json') for x in mt['targets']]
for ci,old,ir,receipt in scopes:
 cid=old['case_id'];new=D[cid];ds=diff(old,new)
 assert {x['path'] for x in ds}=={'/evidence_ids','/independent_review/evidence_ids','/independent_review/status'}
 assert new['evidence_ids']==old['evidence_ids']+[ir]
 assert old['independent_review']=={'status':'pending','evidence_ids':[]}
 assert new['independent_review']=={'status':'complete','evidence_ids':[ir]}
 peer=E[ir];assert peer['case_ids']==[cid] and peer['kind']=='independent_review'
 assert peer['capture']['sha256']==h(receipt)
 assert (R/peer['capture']['path']).read_bytes()==receipt.read_bytes()
 for eid in old['evidence_ids']:
  baseline=EA if ci==112 else ED
  assert E[eid]==baseline[eid],eid
  if 'capture' in E[eid]:
   cap=E[eid]['capture'];base={'artifact':R,'source':W.parents[2]/'queue/preliminary-v5'}[cap['root']]
   assert h(base/cap['path'])==cap['sha256'],eid
 binds.append({'case_index':ci,'case_id':cid,'sealed_reviewed_outcome_canonical_sha256':ch(old),'final_full_outcome_canonical_sha256':ch(new),'case_input_sha256':new['case_input_sha256'],'occurrence_ids':new['occurrence_ids'],'receipt':ref(receipt),'receipt_evidence_id':ir,'all_other_complete_fields_unchanged':True})
 traces.append({'case_index':ci,'complete_sealed_reviewed_outcome':old,'complete_final_outcome':new,'exact_delta':ds,'final_receipt_evidence':peer})

held=j(S/'held-proposals.json');assert h(S/'held-proposals.json')==a5['input_bindings'][str((S/'held-proposals.json').relative_to(W))]
hp=held['held_proposals'][0];assert hp==a5['reviewed_full_held_proposal'] and ch(hp)==a5['held_proposal_canonical_sha256']
assert hp['installable'] is False and hp['status']=='NONINSTALLABLE_SOURCE_TRANSCRIPTION' and held['excluded_from_proposals_json'] is True
assert D[scopes[0][1]['case_id']]['proposal_ids']==[]
assert all(x['owner_path']!=hp['owner_path'] for x in P.values())
held_path=R/hp['after_capture']['path'];assert h(held_path)==a5['final_payload_sha256']
before=R/hp['before_capture']['path'];assert h(before)==a5['before_payload_sha256']
assert (W/hp['owner_path']).read_bytes()==before.read_bytes()
payloads=[{'scope':'held A5 source-relative draft','payload':ref(held_path),'before':ref(before),'held_proposal_canonical_sha256':ch(hp),'held_status':'NONINSTALLABLE; independent_review pending conservatively retained in held ledger; source outcome links exact complete receipt'}]
for t in mt['targets']:
 b=t['binding'];pid=b['proposal_id'];assert P[pid]==t['complete_proposal_unchanged']==PD[pid]
 p=R/P[pid]['after_capture']['path'];assert h(p)==b['full_payload']['sha256']
 payloads.append({'scope':'case '+str(b['case_index']),'proposal_id':pid,'payload':ref(p),'proposal_canonical_sha256':ch(P[pid]),'complete_proposal_unchanged':True})
for eid in ['A-E-CAPTURE-078','A-E-CAPTURE-102','A-E-COMPLETION-09','V5-E-STOCK-CLAIM-SUPERSESSION']:
 assert E[eid]==ED[eid]
for t in mt['targets']:assert E[t['complete_after_evidence']['evidence_id']]==t['complete_after_evidence']
assert E['A-E-CAPTURE-102']['supports_or_contradicts'].split('case38:')[0]==next(x for x in mt['targets'] if x['binding']['case_index']==38)['complete_before_evidence']['supports_or_contradicts'].split('case38:')[0]
assert h(S/'claim-supersessions.json')==meta['claim_supersession']['sha256']
assert h(Path(meta['historical_native']['path']))==meta['historical_native']['sha256']
oldp=rows(R/'successor-v4/proposals.json','proposals','proposal_id'); retained=[]
for pid,p in oldp.items():
 assert P[pid]['after_capture']==p['after_capture']
 f=R/p['after_capture']['path'];assert h(f)==p['after_capture']['sha256'];retained.append({'proposal_id':pid,**ref(f)})
assert len(retained)==104
save('fieldtrace-v1.json',{'canonical_algorithm':'SHA256 sorted-key compact UTF-8 JSON ensure_ascii=False allow_nan=False no newline','full_case_traces':traces,'complete_held_proposal_unchanged':hp,'complete_current_scoped_evidence':[E[x] for x in ['C-E-112-SOURCE-1','C-E-togo-M2499','V5-E-A5-CONTINUITY','V5-E-AUTHOR','A-E-CAPTURE-078','A-E-CAPTURE-102','A-E-COMPLETION-09','V5-E-STOCK-CLAIM-SUPERSESSION']],'previous_payloads_byte_verification_only':retained})
receipt={'schema_version':'1.0.0','review_id':'W06-V5-FINAL-CORE-BINDING-A5-STOCK','reviewer':'/root/residual_stock_review','author':'Codex worker06 /root','llm_assisted':True,'observed_started_at':'2026-11-08T08:45:01Z','finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=W,text=True).strip(),'status':'pass_exact_review_metadata_binding','scope':'Additive final-core binding of full A5 case112/held payload and full stock case20/38 outcomes/evidence to exact previously sealed scientific reviews. No new science authored or no additional scientific scope accepted.','selection':ref(S/'selection.json'),'core':{k:ref(W/v['path']) for k,v in selection['core'].items()},'bound_cases':binds,'bound_payloads':payloads,'checks':{'only_exact_expected_case_paths_changed':['/evidence_ids','/independent_review/evidence_ids','/independent_review/status'],'exact_expected_review_ids':['V5-IR-A5','V5-IR-STOCK-META-20','V5-IR-STOCK-META-38'],'all_scoped_science_evidence_objects_unchanged':True,'all_three_payloads_unchanged':True,'original_104_payload_bytes_unchanged':True,'original_102_case27_prefix_unchanged':True,'original_capture_urls_times_hashes_unchanged':True,'A5_held_proposal_entire_object_unchanged':True,'A5_excluded_from_active_proposals':True,'A5_authentic_beforeimage_matches_current_native':True,'new_native_schema_or_full_partonomy_run_for_metadata_only_binding':False,'final_native_metadata_review_assigned_separately':'/root/residual_assembly_review'},'observed_final_counts':{'cases':len(D),'active_proposals':len(P),'retained_predecessor_payloads':len(retained),'held_noninstallable':len(held['held_proposals']),'evidence':len(E)},'preserved_previous_manifests':preserved,'timing_qualification_preserved':ref(timing),'timing_qualification_durable_copy':ref(S/'independent-a5/final-metadata-residual/timing-qualification-v1.json'),'fieldtrace':ref(O/'fieldtrace-v1.json'),'new_findings':[],'limitations':['This binding asserts exact reviewed scientific bytes and limited review metadata additions only. Final native assembly checks are separate and not claimed here.','A5 remains NONINSTALLABLE pending authentic copper identity and whole existing-owner source applicability; literal malformed CuSO2·5H2O is not silently repaired.','KOH stock carrier/form/strength/amount and yeast stock carrier/percent basis/product/volume unknowns remain explicit.','No coordinator source-case acceptance, source release, owner integration, role or export approval is granted.'],'coordinator_acceptance':False,'whole_owner_role_export_approval':False}
save('final-core-binding-v1.json',receipt)
save('MANIFEST-v1.json',{'scope':'Additive final-core binding; prior four manifests and timing qualifier are preserved, not rewritten.','files':[{'path':str(p.relative_to(O)),'bytes':p.stat().st_size,'sha256':h(p)} for p in sorted(O.iterdir()) if p.is_file()]})
print(json.dumps({'receipt':ref(O/'final-core-binding-v1.json'),'fieldtrace':ref(O/'fieldtrace-v1.json'),'manifest':ref(O/'MANIFEST-v1.json'),'bound_cases':binds},indent=2))
