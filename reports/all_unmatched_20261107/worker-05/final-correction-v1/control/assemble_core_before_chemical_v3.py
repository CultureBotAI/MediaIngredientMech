"""Compile exact authored fragments with explicit lineage, never select owner winners."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,copy,hashlib,json
W=Path.cwd();S=W/'.temp/w05-final-correction-v1';B=W/'reports/all_unmatched_20261107/worker-05';N=B/'correction-1193-v1'
parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True);parser.add_argument('--review-bindings',type=Path)
a=parser.parse_args();out=a.out;out.mkdir(parents=True,exist_ok=False)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
objsha=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def rows(p,k):
 x=json.loads(p.read_text());return x[k] if isinstance(x,dict) else x
def put(n,x):(out/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
oldD=rows(N/'decisions.json','decisions');oldP=rows(N/'proposals.json','proposals');oldE=rows(N/'evidence.json','evidence')
case_order={d['case_id']:i for i,d in enumerate(oldD)};old_by_id={p['proposal_id']:p for p in oldP}
old_cases={d['case_id']:d for d in oldD};evidence={e['evidence_id']:copy.deepcopy(e) for e in oldE}
decisions=[];proposals=[];lineage=[];fragment_bindings=[];case_lane={};payload_lane={};evidence_changes=[]
for lane,dp,pp,ep in [
 ('chemicals',S/'chemicals/decisions-v2.json',S/'chemicals/proposals-v2.json',S/'chemicals/evidence-v1.json'),
 ('materials',S/'materials/decisions.json',S/'materials/proposals.json',S/'materials/evidence.json'),
 ('media',S/'remediation/media-report-v3/decisions.json',S/'media/proposals.json',S/'media/evidence.json')]:
 assignment=json.loads((S/f'control/{lane}-assignment.json').read_text())
 ds=rows(dp,'decisions');ps=rows(pp,'proposals');es=rows(ep,'evidence')
 assert {d['case_id'] for d in ds}==set(assignment['case_ids'])
 for path in [dp,pp,ep]:fragment_bindings.append(dict(lane=lane,path=str(path.relative_to(W)),sha256=sha(path)))
 for d in ds:
  cid=d['case_id'];assert cid not in case_lane;case_lane[cid]=lane
  old=old_cases[cid]
  for key in ['case_input_sha256','source','occurrence_ids','preserved_downstream_holds']:
   assert d.get(key)==old.get(key),(cid,key)
  old_holds=old.get('preserved_source_holds',{});new_holds=d.get('preserved_source_holds',{})
  assert {k:v for k,v in old_holds.items() if k!='policy'}=={k:v for k,v in new_holds.items() if k!='policy'},(cid,'substantive holds')
  # Primary author metadata remains verbatim in the immutable fragment.
  d=copy.deepcopy(d)
  d['final_assembly_provenance']=dict(compiler='/root',primary_lane=lane,
    selected_fragment_path=str(dp.relative_to(W)),selected_fragment_sha256=sha(dp),
    selected_decision_object_sha256=objsha(d),predecessor_decision_object_sha256=objsha(old),
    source_hold_policy_wording=dict(before=old_holds.get('policy'),after=new_holds.get('policy'),substantive_hold_objects_unchanged=True),
    prior_review_scope='Historical reviews do not approve successor bytes.',
    native_scope='This final source-case snapshot and each complete linked proposal are explicit native review targets. No owner or export admission follows.')
  d['independent_review']={'status':'pending','evidence_ids':[]}
  decisions.append(d)
 for p in ps:
  pid=p['proposal_id'];assert pid not in payload_lane;payload_lane[pid]=lane
  predecessors=[q for q in oldP if q['proposal_id']==pid or q['proposal_id'] in p.get('replaces_proposal_ids',[])]
  assert len(predecessors)<=1,(pid,[q['proposal_id'] for q in predecessors])
  predecessor=predecessors[0] if predecessors else None
  if predecessor:
   assert predecessor['owner_path']==p['owner_path'] and predecessor['before_sha256']==p['before_sha256']
  lineage.append(dict(proposal_id=pid,lane=lane,
   predecessor_proposal_id=predecessor['proposal_id'] if predecessor else None,
   predecessor_proposal_sha256=objsha(predecessor) if predecessor else None,
   predecessor_after_capture=predecessor['after_capture'] if predecessor else None,
   successor_after_capture=p['after_capture'],owner_path=p['owner_path'],
   original_before_sha256=p['before_sha256'],case_ids=p['case_ids'],
   classification='original_selected_proposal_successor' if predecessor else 'additional_bounded_existing_owner_followon'))
  proposals.append(copy.deepcopy(p))
 for e in es:
  eid=e['evidence_id']
  if eid in evidence and e!=evidence[eid]:
   evidence_changes.append(dict(evidence_id=eid,lane=lane,predecessor=evidence[eid],successor=e,
     changes=[k for k in set(evidence[eid])|set(e) if evidence[eid].get(k)!=e.get(k)]))
   assert e.get('capture')==evidence[eid].get('capture'),('old source capture changed',eid)
   assert e.get('accessed_at')==evidence[eid].get('accessed_at'),('old source time changed',eid)
  evidence[eid]=copy.deepcopy(e)
assert len(decisions)==len(oldD) and set(case_lane)==set(old_cases)
covered=[x['predecessor_proposal_id'] for x in lineage if x['predecessor_proposal_id']]
assert len(covered)==len(set(covered))==len(oldP) and set(covered)==set(old_by_id)
decisions.sort(key=lambda d:case_order[d['case_id']])
# The later report amendment is a separate evidence object, not a rewritten historical ledger.
amend=S/'remediation/media-report-v3/primary-read-ledger.json'
amend_id='FINAL-ROOT-MEDIA-REPORT-AMENDMENT-V3'
evidence[amend_id]=dict(evidence_id=amend_id,kind='source_snapshot',
 capture=dict(root='artifact',path='final-correction-v1/remediation/media-report-v3/primary-read-ledger.json',sha256=sha(amend)),
 url=None,locator='Cases136,159,174 report wording only; see v2/v3 amendment receipts and independent rereview.',
 supports_or_contradicts='Root-corrected report metadata supersedes unsupported human attribution and LB source caption; scientific author remains /root/media_research. Source captures/timestamps and all selected payloads unchanged.',
 case_ids=[d['case_id'] for d in decisions if case_lane[d['case_id']]=='media'],
 accessed_at=datetime.now(timezone.utc).isoformat())
for d in decisions:
 if case_lane[d['case_id']]=='media':d['evidence_ids'].append(amend_id)
if a.review_bindings:
 reviews=json.loads(a.review_bindings.read_text())
 for lane,r in reviews.items():
  path=W/r['path'];assert sha(path)==r['sha256']
  e=dict(evidence_id=r['evidence_id'],kind='independent_review',
    capture=dict(root='artifact',path=str(path.relative_to(B)),sha256=r['sha256']),
    url=None,locator='Complete disjoint case/payload scope with exact selected hashes, source assessments, findings and rereview.',
    supports_or_contradicts='Authorship-separated scientific review of this final scope, subject to all stated unresolved identity, source, role, owner and export holds.',
    case_ids=[d['case_id'] for d in decisions if case_lane[d['case_id']]==lane],
    accessed_at=r['completed_at'],reviewer=r['reviewer'])
  evidence[e['evidence_id']]=e
  for d in decisions:
   if case_lane[d['case_id']]==lane:
    d['independent_review']={'status':'complete','evidence_ids':[e['evidence_id']],
     'scope':'Review complete, not all scientific questions resolved or any admission approved.','reviewer':r['reviewer']}
    d['evidence_ids'].append(e['evidence_id'])
put('decisions.json',dict(schema_version=1,decisions=decisions))
put('proposals.json',dict(schema_version=1,proposals=proposals))
put('evidence.json',dict(schema_version=1,evidence=list(evidence.values())))
put('proposal-lineage.json',dict(source_head='43f7cf6e8681fa617b5d6d3529d94d537ca01f0d',original_count=len(oldP),successor_count=len(proposals),rows=lineage))
put('assembly-receipt.json',dict(at=datetime.now(timezone.utc).isoformat(),compiler='/root',
 source_head='43f7cf6e8681fa617b5d6d3529d94d537ca01f0d',case_count=len(decisions),
 original_proposal_count=len(oldP),selected_proposal_count=len(proposals),additional_proposals=len(proposals)-len(oldP),
 evidence_count=len(evidence),all_original_evidence_ids_retained=set(e['evidence_id'] for e in oldE)<=set(evidence),
 original_evidence_metadata_changes=evidence_changes,fragment_bindings=fragment_bindings,
 case_lane=case_lane,proposal_lane=payload_lane,independent_reviews_bound=bool(a.review_bindings),
 decisions_with_proposals=sum(bool(d['proposal_ids']) for d in decisions),
 source_case_occurrence_ids=sum(len(d['occurrence_ids']) for d in decisions),
 no_owner_winner_selected=True,no_maintained_changes=True))
print(json.dumps(dict(cases=len(decisions),proposals=len(proposals),evidence=len(evidence),reviewed=bool(a.review_bindings))))
