"""Append-only assembly of independently reviewed W05 source-origin supplements."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,copy,hashlib,json
W=Path.cwd();S=W/'.temp/w05-tellurium-polypeptone-v1';B=W/'reports/all_unmatched_20261107/worker-05';O=B/'postseal-source-corrections-v1';P=B/'tellurium-polypeptone-v1'
ap=argparse.ArgumentParser();ap.add_argument('--selection',type=Path,required=True);ap.add_argument('--review',type=Path,required=True);a=ap.parse_args()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();j=lambda p:json.loads(p.read_text());objsha=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def rows(p,k):
 x=j(p);return x[k] if isinstance(x,dict) else x
def put(p,x):
 assert not p.exists(),p;p.parent.mkdir(exist_ok=True,parents=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
oldD=j(O/'core/decisions.json');oldP=j(O/'core/proposals.json');oldE=j(O/'core/evidence.json');oldL=j(O/'core/proposal-lineage.json')
D=copy.deepcopy(oldD);PS=copy.deepcopy(oldP);E=copy.deepcopy(oldE);L=copy.deepcopy(oldL)
di={x['case_id']:i for i,x in enumerate(D['decisions'])};pi={x['proposal_id']:i for i,x in enumerate(PS['proposals'])};ei={x['evidence_id']:x for x in E['evidence']}
rb=j(a.review);peerpath=W/rb['path'];assert sha(peerpath)==rb['sha256'];peer=j(peerpath);selection=j(a.selection);seenD=set();seenP=set();dc=[];pc=[];fragments=[]
for lane,paths in selection.items():
 for kind in ['decisions','proposals','evidence']:
  q=W/paths[kind];fragments.append(dict(lane=lane,kind=kind,path=str(q.relative_to(W)),sha256=sha(q)))
 for d in rows(W/paths['decisions'],'decisions'):
  cid=d['case_id'];assert cid in di and cid not in seenD;seenD.add(cid);old=oldD['decisions'][di[cid]]
  for k in ['case_id','case_input_sha256','source','occurrence_ids','owner_records','preserved_source_holds','preserved_downstream_holds']:assert d.get(k)==old.get(k),(cid,k)
  rv=next(x for x in peer['case_reviews'] if x['case_id']==cid);assert rv['selected_decision_object_sha256']==objsha(d),(cid,'review')
  n=copy.deepcopy(d);n['previous_supplement_independent_review']=copy.deepcopy(old['independent_review']);n['independent_review']=dict(status='complete',evidence_ids=[rb['evidence_id']],reviewer=rb['reviewer'],scope='Exact declared supplement source decision and full linked payload reviewed; source/owner/role/export holds retained.')
  n['evidence_ids']=list(dict.fromkeys(n['evidence_ids']+[rb['evidence_id']]))
  n['tellurium_polypeptone_assembly_provenance']=dict(compiler='/root',primary_lane=lane,selected_fragment_path=paths['decisions'],selected_fragment_sha256=sha(W/paths['decisions']),selected_decision_object_sha256=objsha(d),predecessor_decision_object_sha256=objsha(old),predecessor_source_head='76bca688b4f55e8bdf791079df8d4156cded6c4c',prior_assembly_scope='All retained earlier assembly/review metadata binds its own historical bytes; this entry binds the current authored supplement.')
  D['decisions'][di[cid]]=n;dc.append(dict(case_id=cid,lane=lane,before_object_sha256=objsha(old),authored_object_sha256=objsha(d),canonical_object_sha256=objsha(n),authored_scientific_object_changed=(d!=old)))
 for p in rows(W/paths['proposals'],'proposals'):
  pid=p['proposal_id'];assert pid in pi and pid not in seenP;seenP.add(pid);old=oldP['proposals'][pi[pid]]
  for k in ['proposal_id','kind','owner_path','before_sha256','case_ids','applies_to_occurrence_ids','destination_owner_path']:assert p.get(k)==old.get(k),(pid,k)
  assert sha(B/p['after_capture']['path'])==p['after_capture']['sha256'];rv=next(x for x in peer['payload_reviews'] if x['proposal_id']==pid);assert rv['after_capture']['sha256']==p['after_capture']['sha256']
  PS['proposals'][pi[pid]]=copy.deepcopy(p);changed=p['after_capture']['sha256']!=old['after_capture']['sha256'];pc.append(dict(proposal_id=pid,lane=lane,before_object_sha256=objsha(old),after_object_sha256=objsha(p),object_changed=p!=old,payload_changed=changed,before_capture=old['after_capture'],after_capture=p['after_capture']))
  if changed:
   lr=next(x for x in L['rows'] if x['proposal_id']==pid);lr['pre_supplement_successor_after_capture']=copy.deepcopy(lr['successor_after_capture']);lr['successor_after_capture']=copy.deepcopy(p['after_capture']);lr['tellurium_polypeptone_predecessor_head']='76bca688b4f55e8bdf791079df8d4156cded6c4c'
 for e in rows(W/paths['evidence'],'evidence'):
  eid=e['evidence_id']
  if eid in ei:assert ei[eid]==e,('inherited evidence changed',eid)
  else:ei[eid]=copy.deepcopy(e);E['evidence'].append(copy.deepcopy(e))
e=dict(evidence_id=rb['evidence_id'],kind='independent_review',capture=dict(root='artifact',path=str(peerpath.relative_to(B)),sha256=rb['sha256']),url=None,locator='Full exact declared source-origin supplement, changed Polypeptone and retained Tellurium/Hipolypepton scopes; actual case/payload/primary bindings in receipt.',supports_or_contradicts='Authorship-separated source science review, with unresolved Japanese historical product bridge and all owner/source/role/export limits retained. No coordinator combined-union approval.',case_ids=sorted(seenD),accessed_at=rb['completed_at'],reviewer=rb['reviewer']);assert e['evidence_id'] not in ei;E['evidence'].append(e)
assert E['evidence'][:len(oldE['evidence'])]==oldE['evidence']
for i,d in enumerate(D['decisions']):
 if d['case_id'] not in seenD:assert d==oldD['decisions'][i]
for i,p in enumerate(PS['proposals']):
 if p['proposal_id'] not in seenP:assert p==oldP['proposals'][i]
L['tellurium_polypeptone_predecessor_manifest']=dict(path=str((O/'MANIFEST.json').relative_to(W)),sha256=sha(O/'MANIFEST.json'));L['tellurium_polypeptone_changed_proposals']=[x['proposal_id'] for x in pc if x['payload_changed']]
for n,x in [('decisions.json',D),('proposals.json',PS),('evidence.json',E),('proposal-lineage.json',L)]:put(P/'core'/n,x)
receipt=dict(at=datetime.now(timezone.utc).isoformat(),compiler='/root',base='76bca688b4f55e8bdf791079df8d4156cded6c4c',case_count=len(D['decisions']),selected_proposals=len(PS['proposals']),original_proposal_lineages=L['original_count'],evidence_count=len(E['evidence']),retained_evidence_objects=len(oldE['evidence']),reviewed_case_count=len(seenD),reviewed_payload_count=len(seenP),changed_payload_count=sum(x['payload_changed'] for x in pc),changed_proposal_object_count=sum(x['object_changed'] for x in pc),unchanged_cases=len(D['decisions'])-len(seenD),unchanged_payloads=len(PS['proposals'])-sum(x['payload_changed'] for x in pc),case_changes=dc,proposal_reviews=pc,fragment_bindings=fragments,review=rb,source_boundaries_and_holds_preserved=True,no_union_or_maintained_application=True)
put(P/'core/assembly-receipt.json',receipt);print(json.dumps({k:receipt[k] for k in ['case_count','selected_proposals','original_proposal_lineages','evidence_count','reviewed_case_count','reviewed_payload_count','changed_payload_count']}))
