from pathlib import Path
import json,hashlib,datetime,yaml,collections
W=Path.cwd();S=W/'.temp/w05-buffer-parts-v1';R=S/'assembly-review';B=W/'reports/all_unmatched_20261107/worker-05';O=B/'tellurium-polypeptone-v1';F=S/'control/composed-final-v5';j=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();oh=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
old={k:j(O/'core'/f'{k}.json') for k in ['decisions','proposals','evidence','proposal-lineage']};new={k:j(F/f'{k}.json') for k in old};receipt=j(F/'composition-receipt.json');selection=j(S/'control/selection-final-v5.json');errors=[];checks=[]
def check(name,v,details=None):
 checks.append(dict(name=name,passed=bool(v),details=details))
 if not v:errors.append(checks[-1])
def ix(rows,k):
 result={x[k]:x for x in rows};check('unique '+k,len(result)==len(rows));return result
OD=ix(old['decisions']['decisions'],'case_id');ND=ix(new['decisions']['decisions'],'case_id');OP=ix(old['proposals']['proposals'],'proposal_id');NP=ix(new['proposals']['proposals'],'proposal_id');OE=ix(old['evidence']['evidence'],'evidence_id');NE=ix(new['evidence']['evidence'],'evidence_id');OL=ix(old['proposal-lineage']['rows'],'proposal_id');NL=ix(new['proposal-lineage']['rows'],'proposal_id')
check('exact original case IDs and order',list(OD)==list(ND));check('all prior proposal IDs retained',set(OP)<=set(NP));check('all prior evidence objects exact prefix',new['evidence']['evidence'][:len(OE)]==old['evidence']['evidence']);check('all prior lineage IDs retained',set(OL)<=set(NL));check('every proposal has lineage',set(NP)==set(NL));check('all 138 original lineage origins',sum(bool(x['predecessor_proposal_id']) for x in NL.values())==new['proposal-lineage']['original_count']==old['proposal-lineage']['original_count'])
selected_cases={r['case_id']:r for r in receipt['case_reviews']};selected_payloads={r['proposal_id']:r for r in receipt['payload_reviews']};owneradditions=[];casechanges=[]
for cid,d in ND.items():
 o=OD[cid]
 for field in ['case_id','case_input_sha256','source','occurrence_ids','preserved_source_holds','preserved_downstream_holds','disposition']:
  check('case preserved '+cid+' '+field,o.get(field)==d.get(field))
 for field in ['proposal_ids','evidence_ids','issue_refs','owner_records']:
  check('case retained '+cid+' '+field,all(v in d.get(field,[]) for v in o.get(field,[])))
 for v in d.get('owner_records',[]):
  if v not in o.get('owner_records',[]):owneradditions.append(dict(case_id=cid,owner=v))
 if cid in selected_cases:check('selected authored case hash '+cid,oh(d)==selected_cases[cid]['selected_decision_object_sha256'])
 else:check('unreviewed case unchanged '+cid,d==o)
 check('case links all current proposals '+cid,set(d['proposal_ids'])<=set(NP));check('case evidence links complete '+cid,set(d['evidence_ids'])<=set(NE))
 if o!=d:casechanges.append(dict(case_id=cid,fields=[k for k in set(o)|set(d) if o.get(k)!=d.get(k)]))
recordchecks=[]
for pid,p in NP.items():
 cap=p['after_capture'];path=B/cap['path'];check('payload capture '+pid,path.is_file() and sha(path)==cap['sha256']);r=yaml.safe_load(path.read_text());check('proposal cases existing '+pid,set(p['case_ids'])<=set(ND));check('proposal evidence existing '+pid,set(p.get('evidence_ids',[]))<=set(NE));check('lineage selected capture '+pid,NL[pid]['successor_after_capture']==cap)
 if pid in OP:
  q=OP[pid]
  for field in ['kind','owner_path','before_sha256','case_ids','applies_to_occurrence_ids','destination_owner_path']:check('proposal origin retained '+pid+' '+field,p.get(field)==q.get(field))
  oldr=yaml.safe_load((B/q['after_capture']['path']).read_text());hist=oldr.get('curation_history',[]);check('prior history prefix '+pid,r.get('curation_history',[])[:len(hist)]==hist);check('prior rejected labels '+pid,all(s in r.get('synonyms',[]) for s in oldr.get('synonyms',[]) if s.get('synonym_type')=='REJECTED_LABEL'))
  for field in set(oldr)|set(r):
   if 'occurrence' in field or field in ['roles','organism_roles','causal_graphs']:check('prior non-assigned scope '+pid+' '+field,r.get(field)==oldr.get(field))
  if pid not in selected_payloads:check('unreviewed prior proposal object unchanged '+pid,p==q)
  for field in ['predecessor_proposal_id','predecessor_proposal_sha256','predecessor_after_capture','owner_path','original_before_sha256','case_ids']:check('lineage original retained '+pid+' '+field,NL[pid].get(field)==OL[pid].get(field))
 else:
  before=W/p['owner_path'];check('authentic new dependent before '+pid,p['kind']=='edit_existing_owner' and sha(before)==p['before_sha256']);check('new dependent lineage not reauthored origin '+pid,NL[pid]['predecessor_proposal_id'] is None)
  oldr=yaml.safe_load(before.read_text());hist=oldr.get('curation_history',[]);check('dependent baseline history prefix '+pid,r.get('curation_history',[])[:len(hist)]==hist)
 recordchecks.append(dict(proposal_id=pid,after_capture=cap,source_owner_path=p['owner_path'],source_before_sha256=p.get('before_sha256'),selected_for_independent_review=pid in selected_payloads))
actual=[]
for lane,files in selection.items():
 for kind,rel in files.items():
  f=W/rel;public=B/'buffer-parts-v1'/f.relative_to(S);expected=next(x for x in receipt['fragments'] if x['lane']==lane and x['kind']==kind);check('fragment hash '+lane+' '+kind,sha(f)==expected['sha256']);check('public fragment exact '+lane+' '+kind,public.is_file() and sha(public)==sha(f));actual.append((lane,kind,rel))
check('all selected fragments in receipt',len(actual)==len(receipt['fragments']))
for e in NE.values():
 cap=e.get('capture')
 if cap and cap.get('root')=='artifact':
  p=B/cap['path'];check('artifact evidence capture '+e['evidence_id'],p.is_file() and sha(p)==cap['sha256'])
computed=dict(cases=len(ND),proposals=len(NP),evidence=len(NE),original_lineages=sum(bool(x['predecessor_proposal_id']) for x in NL.values()),reviewed_cases=len(selected_cases),reviewed_payloads=len(selected_payloads),new_authentic_origins=len(set(NP)-set(OP)),changed_existing_payloads=sum(NP[p]['after_capture']['sha256']!=OP[p]['after_capture']['sha256'] for p in OP))
check('computed receipt counts',computed==receipt['counts']);check('selected cases reflect every changed case',set(x['case_id'] for x in casechanges)==set(selected_cases))
out=dict(at=datetime.datetime.now(datetime.timezone.utc).isoformat(),reviewer='/root/assembly_audit',scope='Independent mechanical exact-byte audit of composed-final-v5 only. No source-scientific approval, final core wrapper/native review approval, owner/application or export approval.',status='PASS' if not errors else 'FAIL',counts=computed,old_counts=dict(cases=len(OD),proposals=len(OP),evidence=len(OE)),inputs=[dict(path=str((F/f'{k}.json').relative_to(W)),sha256=sha(F/f'{k}.json')) for k in old]+[dict(path=str((S/'control/selection-final-v5.json').relative_to(W)),sha256=sha(S/'control/selection-final-v5.json'))],checks=checks,errors=errors,case_changes=casechanges,owner_record_additions=owneradditions,payload_bindings=recordchecks)
q=R/'composition-v5-independent-audit.json';assert not q.exists();q.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(dict(status=out['status'],counts=computed,check_count=len(checks),errors=errors,sha256=sha(q))))
