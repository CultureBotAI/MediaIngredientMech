from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

P=Path(__file__).resolve().parent
W=P.parents[2]
A=W/'reports/all_unmatched_20261107/worker-08'
O=A/'successors/issue-1237-mc-dependent-v1'
B=A/'successors/issue-1237-tenvit-v1'

def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def canonical(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
checks=[]
def check(label,condition):
    checks.append({'check':label,'passed':bool(condition)})
    if not condition:raise AssertionError(label)
def dump(name,value):
    with (P/name).open('x') as f:json.dump(value,f,ensure_ascii=False,indent=2);f.write('\n')
def bind(capture,label):
    check(label+' artifact root',capture['root']=='artifact')
    path=A/capture['path']
    check(label+' exact bytes',sha(path)==capture['sha256'])
    return path

seal_hash='dddad253901ed39243f235a732cd0a51ceb888ce4e0eca7d8d73edc9ad743ad3'
check('sealed science receipt preserved',sha(P/'review.json')==seal_hash)
review=read(P/'review.json')
selection=read(O/'selection.json')
check('exact frozen final selection',sha(O/'selection.json')=='33f0f1f5166e75283a3e0488f6172844002919cc2461a04f2089f8c4f8fedab8')
for name,c in selection['authoritative_inputs'].items():bind(c,'selector '+name)
bind(selection['predecessor_selection'],'predecessor selector')
bind(selection['payload'],'final selected Mc payload')
bind(selection['dependency'],'dependency')
bind(selection['effective_source_ref_index'],'effective source index')
bind(selection['thesis_publication_scope'],'thesis relocation')
for kind,c in selection['independent_reviews'].items():bind(c,kind+' peer receipt')
check('published science receipt equals sealed private receipt',sha(bind(selection['independent_reviews']['science'],'copied peer'))==seal_hash)

d=read(O/'decisions.json')['decisions'];p=read(O/'proposals.json')['proposals'];e=read(O/'evidence.json')['evidence']
old_d=read(B/'decisions.json')['decisions'];old_p=read(B/'proposals.json')['proposals'];old_e=read(B/'evidence.json')['evidence']
dm={r['case_id']:r for r in d};pm={r['proposal_id']:r for r in p};em={r['evidence_id']:r for r in e}
odm={r['case_id']:r for r in old_d};opm={r['proposal_id']:r for r in old_p}
cid=selection['changed_case_id'];pid=selection['new_dependent_proposal']
check('188 exact unique case IDs',len(d)==len(dm)==188 and set(dm)==set(odm))
check('115 exact unique proposal IDs',len(p)==len(pm)==115 and set(pm)-set(opm)=={pid})
check('1114 unique evidence IDs',len(e)==len(em)==1114)
check('1101 exact original evidence prefix',len(old_e)==1101 and e[:1101]==old_e)
check('114 exact predecessor proposal objects as prefix',len(old_p)==114 and p[:114]==old_p)
check('320 frozen occurrence entries',sum(len(r['occurrence_ids']) for r in d)==320)
for case_id,case in dm.items():
    check('case frozen digest retained '+case_id,case['case_input_sha256']==odm[case_id]['case_input_sha256'])
    check('case occurrences retained '+case_id,case['occurrence_ids']==odm[case_id]['occurrence_ids'])
    if case_id!=cid:check('unchanged entire case '+case_id,case==odm[case_id])
    for eid in case['evidence_ids']:check('case evidence ref '+case_id+' '+eid,eid in em)
    for prop_id in case['proposal_ids']:check('case proposal ref '+case_id+' '+prop_id,prop_id in pm)
for prop_id,proposal in pm.items():
    bind(proposal['after_capture'],'selected payload '+prop_id)
    if prop_id!=pid:check('entire predecessor proposal exact '+prop_id,proposal==opm[prop_id])
    for case_id in proposal['case_ids']:check('proposal case reference '+prop_id+' '+case_id,case_id in dm)

authored_case=read(O/'author/decision.json');authored_proposal=read(O/'author/proposal.json')
check('sealed authored case file unchanged',sha(O/'author/decision.json')==review['input_hashes']['successors/issue-1237-mc-dependent-v1/author/decision.json'])
check('sealed authored proposal file unchanged',sha(O/'author/proposal.json')==review['input_hashes']['successors/issue-1237-mc-dependent-v1/author/proposal.json'])
check('final case metadata-only differences',{k for k in set(dm[cid])|set(authored_case) if dm[cid].get(k)!=authored_case.get(k)}=={'evidence_ids','independent_review'})
check('final proposal metadata-only difference',{k for k in set(pm[pid])|set(authored_proposal) if pm[pid].get(k)!=authored_proposal.get(k)}=={'evidence_ids'})
for current,authored,label in [(dm[cid],authored_case,'case'),(pm[pid],authored_proposal,'proposal')]:
    check(label+' evidence suffix only',current['evidence_ids'][:len(authored['evidence_ids'])]==authored['evidence_ids'])
check('completed peer metadata names actual receipts',dm[cid]['independent_review']=={'status':'complete','evidence_ids':['mc1237-science','mc1237-lineage']})
check('full candidate unchanged from science review',pm[pid]['after_capture']['sha256']==review['payload_hashes'][pid])
check('authentic owner preimage unchanged',pm[pid]['before_sha256']=='59c53dfe4e273ebfc7c3fe86fd4244978868ff1879dcde97af64bbeb61c07123')
check('exact one-occurrence causal dependency',pm[pid]['source_occurrence_ids']==['CM_OCC:a181b24b7eb91c50c771bd1c1fc3012fd0cf28f45b49f2750c3d43bda9cdd531'])
check('no Mc campaign occurrences',pm[pid]['mc_campaign_occurrence_count']==selection['counts']['mc_campaign_occurrences']==0)

new_evidence=e[1101:]
for row in new_evidence:
    bind(row['capture'],'new evidence '+row['evidence_id'])
    check('new evidence only actual mixed case '+row['evidence_id'],row['case_ids']==[cid])
    if row['kind']=='primary_source':check('primary evidence original URL and time present '+row['evidence_id'],bool(row.get('url')) and bool(row.get('accessed_at')))
check('exact new evidence suffix selection',set(pm[pid]['evidence_ids'])=={r['evidence_id'] for r in new_evidence})
ols_probe=read(O/'inputs/w09-continuity/primary/probes/ols31345-retry.json')
check('original OLS timestamp preserved',em['mc1237-chebi31345']['accessed_at']==ols_probe['accessed_at_start'])
check('original OLS URL preserved',em['mc1237-chebi31345']['url']==ols_probe['url'])
check('original OLS exact primary hash',em['mc1237-chebi31345']['capture']['sha256']==ols_probe['body_sha256'])

lineage=read(O/'lineage.json')
check('lineage count values exact',lineage['counts']==selection['counts'])
check('lineage covers every case',len(lineage['cases'])==188 and {r['case_id'] for r in lineage['cases']}==set(dm))
for r in lineage['cases']:
    check('lineage old case hash '+r['case_id'],r['before_sha256']==canonical(odm[r['case_id']]))
    check('lineage final case hash '+r['case_id'],r['after_sha256']==canonical(dm[r['case_id']]))
    check('lineage unchanged case flag '+r['case_id'],r['unchanged']==(r['case_id']!=cid))
check('lineage covers every payload',len(lineage['payloads'])==115 and {r['proposal_id'] for r in lineage['payloads']}==set(pm))
for r in lineage['payloads']:
    pr=pm[r['proposal_id']]
    check('lineage exact selected capture '+r['proposal_id'],r['selected_capture']==pr['after_capture'])
    check('lineage exact before '+r['proposal_id'],r['original_before_sha256']==pr['before_sha256'])
    if r['proposal_id']!=pid:check('lineage original proposal hash '+r['proposal_id'],r['original_proposal_object_sha256']==canonical(opm[r['proposal_id']]))

idx=read(O/'inputs/source-ref-index-v2.json');prior_idx=read(O/'inputs/source-ref-index.json')
check('historical source index unchanged',sha(O/'inputs/source-ref-index.json')==review['input_hashes']['successors/issue-1237-mc-dependent-v1/inputs/source-ref-index.json'])
check('source index preserves entry count',len(idx['selected_captures'])==len(prior_idx['selected_captures']))
private_rows=[]
for row,oldrow in zip(idx['selected_captures'],prior_idx['selected_captures']):
    check('source index exact original bytes '+row['original_path'],sha(Path(row['original_path']))==row['sha256']==oldrow['sha256'])
    if 'private_capture_path' in row:
        private_rows.append(row)
        check('private original capture unchanged '+row['original_path'],sha(Path(row['private_capture_path']))==row['sha256'])
        check('previous public copy absent '+row['original_path'],not (W/row['unpublished_prior_copy_path']).exists())
        check('removed only public path and added explicit private metadata '+row['original_path'],{k:v for k,v in row.items() if k not in ['private_capture_path','unpublished_prior_copy_path','publication_status']}=={k:v for k,v in oldrow.items() if k!='published_path'})
    else:
        check('non-thesis source index row exact '+row['original_path'],row==oldrow)
        check('non-thesis source public copy exact '+row['original_path'],sha(W/row['published_path'])==row['sha256'])
check('exactly PDF and TXT relocated',len(private_rows)==2 and {Path(r['private_capture_path']).suffix for r in private_rows}=={'.pdf','.txt'})
relocation=read(O/'inputs/thesis-publication-scope.json')
thesis_probe=read(O/'inputs/w09-continuity/mc-primary/probes/mc-thesis2014.pdf.retry.json')
check('original thesis URL preserved',relocation['source_url']==thesis_probe['url'])
check('original thesis acquisition preserved',relocation['original_acquired_at']==thesis_probe['started_at'])
for row in relocation['relocations']:
    check('relocation exact private and upstream bytes '+row['sha256'],sha(Path(row['private_exact_capture']))==sha(Path(row['original_path']))==row['sha256'])
    check('public full text flag false '+row['sha256'],row['published_full_text'] is False)
    check('original public path absent '+row['sha256'],not (W/row['previous_unpublished_copy_path']).exists())
# Filesystem traversal includes ignored/hidden paths; only equal-size candidate files need hashing.
private_sizes={Path(r['private_exact_capture']).stat().st_size:r['sha256'] for r in relocation['relocations']}
duplicate_paths=[]
for f in O.rglob('*'):
    if f.is_file() and f.stat().st_size in private_sizes and sha(f)==private_sizes[f.stat().st_size]:duplicate_paths.append(str(f))
check('no exact full thesis bytes elsewhere in new public successor',not duplicate_paths)
check('cross-owner routing explicitly pending',selection['cross_owner_routing']=='PENDING_W04_CROSS_OWNER_DECISION')
check('no application or role/export approval',selection['maintained_application'] is False and selection['whole_owner_role_export_approval'] is False)
check('original TSB Bacto admission retained',selection['prior_TSB_Bacto_admission']=='FAILED/HELD unchanged')
check('external envelope unchanged',selection['external_source_envelope_counts']==read(O/'inputs/w09-continuity/source-routing-and-origin-bindings.json')['counts'])
check('sealed science receipt still unchanged at exit',sha(P/'review.json')==seal_hash)
for name,c in selection['authoritative_inputs'].items():bind(c,'exit core '+name)

dump('final-bindings-checks.json',{'status':'PASS','checks':checks,'check_count':len(checks),'scope':'Exact final-index and source-relocation readback; no fresh approval of 114 unchanged proposal sciences and no native gate reruns.'})
receipt={
 'reviewer':'worker08:/root/organics','author':'worker08:/root','status':'PASS','at':datetime.now(timezone.utc).isoformat(),
 'scope':'Bind the sealed independent Mc science review to actual immutable final selection, complete core preservation, metadata-only case/proposal changes and bounded thesis publication relocation.',
 'prior_science_receipt':{'path':'review.json','sha256':seal_hash,'preserved':True},
 'selection':{'path':str((O/'selection.json').relative_to(A)),'sha256':sha(O/'selection.json')},
 'input_hashes':{str(p.relative_to(A)):sha(p) for p in [O/'selection.json',O/'decisions.json',O/'proposals.json',O/'evidence.json',O/'lineage.json',O/'inputs/source-ref-index-v2.json',O/'inputs/thesis-publication-scope.json',O/'author/source-readback.json']},
 'counts_verified':selection['counts'], 'evidence_prefix_verified':1101,
 'changed_case':{'case_id':cid,'canonical_final_sha256':canonical(dm[cid]),'author_sha256':sha(O/'author/decision.json'),'difference_fields':['evidence_ids','independent_review'],'scientific_fields_exact':True},
 'new_proposal':{'proposal_id':pid,'canonical_final_sha256':canonical(pm[pid]),'author_sha256':sha(O/'author/proposal.json'),'difference_fields':['evidence_ids'],'payload_sha256':pm[pid]['after_capture']['sha256'],'full_payload_identical_to_science_review':True},
 'evidence_appraisal':'All thirteen added evidence rows were read and hash-bound. Local validation, saved peer receipts and source snapshots are labeled according to their provenance; the ontology primary response keeps its original URL and acquisition time. Historical local readback paths are resolved explicitly by the new relocation receipt, not silently restamped.',
 'publication_observation_disposition':'Resolved for exact full thesis PDF/text copies: both retain original bytes privately, their old public copies are absent including an ignored-inclusive successor scan, and a bounded factual summary preserves URL/time/hash and the no-genealogy/no-exclusive-owner limits. The earlier observational index and science receipt remain unchanged.',
 'checks':{'path':'final-bindings-checks.json','sha256':sha(P/'final-bindings-checks.json'),'count':len(checks)},
 'open_blocking_findings':[],
 'remaining_limits':review['retained_holds'],
 'no_scope_expansion':'This receipt does not freshly approve other 114 owners, resolve cross-owner routing, alter the eighteen planning holds, approve maintained application, role/export release, or certify native technical gates not inspected in this task.'}
dump('final-bindings.json',receipt)
print(json.dumps({'status':'PASS','checks':len(checks),'final_bindings_sha256':sha(P/'final-bindings.json'),'checks_sha256':sha(P/'final-bindings-checks.json')},indent=2))
