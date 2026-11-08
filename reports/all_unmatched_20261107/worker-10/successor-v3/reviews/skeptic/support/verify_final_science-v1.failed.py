from pathlib import Path
import json, hashlib, copy, re, subprocess, csv, datetime
import yaml

R=Path.cwd(); A=R/'reports/all_unmatched_20261107/worker-10'; S=A/'successor-v3'; P=R/'.temp/all-unmatched-worker-10/successor-v3/skeptic'
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def canon(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def read(p): return json.loads(Path(p).read_text())
def cap(c):
    assert c.get('root','artifact')=='artifact',c
    return A/c['path']
def rec(c): return yaml.safe_load(cap(c).read_text())
def field(r,f):
    for k in re.findall(r'[^.\[\]]+',f): r=r[int(k)] if isinstance(r,list) else r[k]
    return r
checks=[]
def check(label,value): checks.append({'check':label,'pass':bool(value)})
oldps=read(A/'successor-v2/proposals.json')['proposals']; oldp={x['proposal_id']:x for x in oldps}
newps=read(S/'assembly-v1/proposals.json')['proposals']; newp={x['proposal_id']:x for x in newps}
oldds=read(A/'successor-v2/decisions.json')['decisions']; newds=read(S/'assembly-v1/decisions.json')['decisions']
od={x['case_id']:x for x in oldds}; nd={x['case_id']:x for x in newds}
science=[]
for group in ['serums','hcl-manual']:
    science+=read(S/group/'proposals-fragment.json')['proposals']
scip={x['proposal_id']:x for x in science}
bridge=read(S/'serums/retirement-supersession-bridge.json')['bridges']
bridge_by_new={x['new_proposal_id']:x for x in bridge if x.get('new_proposal_id')}
proof=read(S/'enum/metadata-change-proof.json'); proofp={x['proposal_id']:x for x in proof['changed_payloads']}
disp=read(S/'enum/claim-dispositions.json'); audited=read(S/'enum/w10-original-audit-rows.json')['rows']; ar={x['audit_row_id']:x for x in audited}
check('188 unique original and successor cases',len(od)==len(nd)==188 and set(od)==set(nd))
changedcases=[]
for cid,d in nd.items():
    o=od[cid]
    for k in ['case_id','case_input_sha256','source','occurrence_ids','source_index']:
        check(f'case {d["source_index"]} invariant {k}',d[k]==o[k])
    if d!=o: changedcases.append(d['source_index'])
    for pid in d.get('proposal_ids',[]):check(f'case {d["source_index"]} live proposal {pid}',pid in newp and cid in newp[pid]['case_ids'])
check('exactly 18 source changes',sorted(changedcases)==[19,28,40,42,53,61,65,87,94,98,102,105,109,125,129,158,178,181])
check('304 occurrence IDs preserved',sum(len(d['occurrence_ids']) for d in newds)==304)
check('127 unique selected proposals',len(newp)==len(newps)==127)
for group in ['serums','hcl-manual']:
    for d in read(S/group/'decision-fragment.json')['decisions']:
        check('author decision full object '+str(d['source_index']),nd[d['case_id']]==d)
freeze=read(S/'serums/FREEZE.json')
for f in freeze['files']:check('serum freeze '+f['path'],sha(R/f['path'])==f['sha256'])
check('serum freeze 54 files',len(freeze['files'])==54)
for b in bridge:
    op=oldp[b['old_proposal_id']]
    check('retired/superseded old object '+op['proposal_id'],canon(op)==b['old_proposal_object_sha256'])
    check('old inactive '+op['proposal_id'],op['proposal_id'] not in newp)
    check('old payload preserved '+op['proposal_id'],sha(cap(b['old_payload']))==b['old_payload']['sha256'])
    if b.get('new_proposal_id'):check('replacement preserves case set '+op['proposal_id'],set(newp[b['new_proposal_id']]['case_ids'])==set(op['case_ids']))
check('calf158 no proposal',not next(d for d in newds if d['source_index']==158)['proposal_ids'])
snapshots=[]; changes=[]
for np in newps:
    pid=np['proposal_id']; c=np['after_capture']; nr=rec(c)
    check('final capture hash '+pid,sha(cap(c))==c['sha256'])
    oid=bridge_by_new[pid]['old_proposal_id'] if pid in bridge_by_new else pid
    op=oldp[oid]; orr=rec(op['after_capture'])
    sr=rec(scip[pid]['after_capture']) if pid in scip else orr
    if pid in proofp:
        pf=proofp[pid]; check('proof final binding '+pid,pf['new_capture']==c)
        check('proof previous science binding '+pid,rec(pf['previous_capture'])==sr)
        rollback=copy.deepcopy(nr)
        for i in pf['indices']:
            check('exact MANUAL to LLM '+pid+':'+str(i),sr['ontology_mapping']['evidence'][i]['evidence_type']=='MANUAL_CURATION' and nr['ontology_mapping']['evidence'][i]['evidence_type']=='LLM_SUGGESTION')
            rollback['ontology_mapping']['evidence'][i]['evidence_type']='MANUAL_CURATION'
        event=rollback['curation_history'].pop()
        check('exact appended metadata history '+pid,event==pf['event'] and event['llm_assisted'] is True)
        check('whole final payload rollback equals full science preimage '+pid,rollback==sr)
    else:check('full final equals science/unchanged object '+pid,nr==sr)
    if pid not in scip:
        check('non-scientific proposal invariant '+pid,all(np.get(k)==v for k,v in op.items() if k not in ['after_capture','evidence_ids','provenance_correction','independent_review']))
    if pid in scip:
        check('source author proposal invariant '+pid,all(np.get(k)==v for k,v in scip[pid].items() if k not in ['after_capture','evidence_ids','provenance_correction','independent_review']))
    for cid in np['case_ids']:check('proposal back-link '+pid+cid,cid in nd and pid in nd[cid]['proposal_ids'])
    snapshots.append({'proposal_id':pid,'original_proposal_id':oid,'capture':c,'original_capture':op['after_capture'],'scientific_correction':pid in scip,'metadata_correction':pid in proofp,'byte_changed':c['sha256']!=op['after_capture']['sha256'],'full_record':nr})
    if c['sha256']!=op['after_capture']['sha256']:changes.append(pid)
check('101 changed payloads',len(changes)==101)
check('14 scientific payloads',len(scip)==14)
check('92 metadata payloads',len(proofp)==92)
check('123 audit rows one disposition each',len(disp['rows'])==len(ar)==123 and {r['audit_row_id'] for r in disp['rows']}==set(ar))
for row in disp['rows']:
    rid=row['audit_row_id']; a=ar[rid]
    check('full original claim '+rid,row['original_full_value']==a['full_value'] and canon(row['original_full_value'])==row['original_complete_claim_sha256']==a['full_value_sha256'])
    pid=row['selected_proposal_id']
    if pid is None:
        check('retirement has no active old claim '+rid,row['original_proposal_id'] not in newp)
        continue
    claim=field(rec(newp[pid]['after_capture']),row['selected_field'])
    check('complete final claim and capture '+rid,claim==row['selected_full_value'] and canon(claim)==row['selected_complete_claim_sha256'] and row['final_selected_capture']==newp[pid]['after_capture'])
    check('LLM type '+rid,claim['evidence_type']=='LLM_SUGGESTION')
    if row['disposition']=='retyped_exact_surviving_agent_claim':
        rr=copy.deepcopy(claim);rr['evidence_type']='MANUAL_CURATION'
        check('only type changed '+rid,rr==row['original_full_value'])
    else:
        corr=row['explicit_source_author_correspondence']
        check('full source replacement correspondence '+rid,corr['before_claim']==row['original_full_value'] and corr['after_claim']==claim)
for x in disp['historical_exclusions']:
    check('historical exclusion unchanged '+x['proposal_id'],field(rec(newp[x['proposal_id']]['after_capture']),x['field'])==x['full_value'])
for idx in [21,143,187]:check('S2 decision exact '+str(idx),next(d for d in oldds if d['source_index']==idx)==next(d for d in newds if d['source_index']==idx))
for pid in ['sv1-bio-heat_inactivated_fbs_dsmz1076b','sv1-bio-heat_inactivated_fbs_nbrc400']:
    check('other case109 proposal source scope exact '+pid,all(newp[pid].get(k)==v for k,v in oldp[pid].items() if k not in ['after_capture','evidence_ids','provenance_correction','independent_review']))
calf=read(S/'serums/calf-owner-occurrence-audit.json')
cmd=calf['historical_command']; result=subprocess.run(cmd,capture_output=True,text=True)
check('historical calf git-tree query exit',result.returncode==0)
found={x.split(':',1)[1] for x in result.stdout.splitlines()}
check('nine historical calf records exact',len(found)==9 and found=={x['path'] for x in calf['historical_records']})
for x in calf['historical_records']:check('historical calf capture '+x['path'],sha(R/x['capture'])==x['sha256'] and yaml.safe_load((R/x['capture']).read_text())==x['record'])
check('current local calf file hash',sha(calf['current_local_occurrence_file'])==calf['current_local_occurrence_sha256'])
with open(calf['current_local_occurrence_file']) as f: rows=[x for x in csv.DictReader(f,delimiter='\t') if x.get('resolved_identifier')=='MICRO:0001709']
check('eleven current local calf rows exact',len(rows)==11 and rows==calf['current_local_selected_rows'])
output={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':'Codex /root/preparation_skeptic; author-independent AI reviewer','script_sha256':sha(__file__),'input_core':{f:sha(S/'assembly-v1'/f) for f in ['decisions.json','proposals.json','evidence.json','accounting.json']},'check_count':len(checks),'checks':checks,'failures':[c for c in checks if not c['pass']],'counts':{'cases':len(nd),'occurrences':sum(len(d['occurrence_ids']) for d in newds),'proposals':len(newp),'changed_payloads':len(changes),'source_scientific_payloads':len(scip),'metadata_changed_payloads':len(proofp),'audited_claims':len(ar)},'changed_cases':sorted(changedcases),'changed_payload_ids':changes,'method':'Full prior 102 selected payloads and all 123 complete audited claims read independently; frozen 14 scientific source successors read completely; each final full YAML parsed and compared recursively without omitted fields, rollback checked against the actually read full science preimage, every complete changed claim bound and inspected. Metadata-only cohort receives provenance review, not renewed scientific truth/role/export approval.'}
(P/'final-science-checks-v1.json').write_text(json.dumps(output,indent=2,ensure_ascii=False)+'\n')
(P/'final-full-payload-snapshots-v1.json').write_text(json.dumps({'at':output['at'],'records':snapshots},indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:v for k,v in output.items() if k not in ['checks','changed_payload_ids']},indent=2))
