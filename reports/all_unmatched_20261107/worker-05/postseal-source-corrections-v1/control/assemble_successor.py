from pathlib import Path
from datetime import datetime,timezone
import argparse,copy,hashlib,json
W=Path.cwd();S=W/'.temp/w05-postseal-source-corrections-v1';B=W/'reports/all_unmatched_20261107/worker-05';OLD=B/'final-correction-v1';P=B/'postseal-source-corrections-v1'
ap=argparse.ArgumentParser();ap.add_argument('--selection',type=Path,required=True);ap.add_argument('--review',type=Path,required=True);ap.add_argument('--family-ledger',type=Path,required=True);a=ap.parse_args()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
objsha=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def rows(p,k):
 x=json.loads(p.read_text());return x[k] if isinstance(x,dict) else x
def put(p,x):
 assert not p.exists(),p;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
oldD=json.loads((OLD/'core/decisions.json').read_text());oldP=json.loads((OLD/'core/proposals.json').read_text());oldE=json.loads((OLD/'core/evidence.json').read_text());oldL=json.loads((OLD/'core/proposal-lineage.json').read_text())
D=copy.deepcopy(oldD);PS=copy.deepcopy(oldP);E=copy.deepcopy(oldE);L=copy.deepcopy(oldL)
di={d['case_id']:i for i,d in enumerate(D['decisions'])};pi={p['proposal_id']:i for i,p in enumerate(PS['proposals'])};ei={e['evidence_id']:e for e in E['evidence']}
selection=json.loads(a.selection.read_text());rb=json.loads(a.review.read_text());review_path=W/rb['path'];assert sha(review_path)==rb['sha256'];review=json.loads(review_path.read_text())
case_changes=[];proposal_changes=[];fragments=[];seenD=set();seenP=set()
for lane,files in selection.items():
 for kind in ['decisions','proposals','evidence']:
  path=W/files[kind];fragments.append(dict(lane=lane,kind=kind,path=str(path.relative_to(W)),sha256=sha(path)))
 ds=rows(W/files['decisions'],'decisions');ps=rows(W/files['proposals'],'proposals');es=rows(W/files['evidence'],'evidence')
 for d in ds:
  cid=d['case_id'];assert cid in di and cid not in seenD;seenD.add(cid);before=D['decisions'][di[cid]]
  for key in ['case_id','case_input_sha256','source','occurrence_ids','preserved_source_holds','preserved_downstream_holds']:
   assert d.get(key)==before.get(key),(cid,key)
  peer=next(x for x in review['case_reviews'] if x['case_id']==cid);assert peer['selected_decision_object_sha256']==objsha(d),(cid,'review decision mismatch')
  item=copy.deepcopy(d);item['previous_independent_review']=copy.deepcopy(before['independent_review']);item['independent_review']=dict(status='complete',evidence_ids=[rb['evidence_id']],reviewer=rb['reviewer'],scope='Exact full selected source decision and linked changed payload reviewed; no whole-owner, source-role or export admission.')
  item['evidence_ids']=list(dict.fromkeys(item['evidence_ids']+[rb['evidence_id']]))
  item['postseal_assembly_provenance']=dict(compiler='/root',primary_lane=lane,selected_fragment_path=files['decisions'],selected_fragment_sha256=sha(W/files['decisions']),selected_decision_object_sha256=objsha(d),predecessor_decision_object_sha256=objsha(before),predecessor_source_head='5156d92bec6bd885ca8bae3c5e18bfdce0069176',historical_final_assembly_provenance_scope='The retained earlier provenance binds the predecessor snapshot only; current binding is this postseal object.')
  D['decisions'][di[cid]]=item;case_changes.append(dict(case_id=cid,lane=lane,before_object_sha256=objsha(before),authored_successor_object_sha256=objsha(d),canonical_successor_object_sha256=objsha(item)))
 for p in ps:
  pid=p['proposal_id'];assert pid in pi and pid not in seenP;seenP.add(pid);before=PS['proposals'][pi[pid]]
  for key in ['proposal_id','kind','owner_path','before_sha256','case_ids','applies_to_occurrence_ids','destination_owner_path']:
   assert p.get(key)==before.get(key),(pid,key)
  assert sha(B/p['after_capture']['path'])==p['after_capture']['sha256']
  peer=next(x for x in review['payload_reviews'] if x['proposal_id']==pid);assert peer['after_capture']['sha256']==p['after_capture']['sha256'],(pid,'peer mismatch')
  PS['proposals'][pi[pid]]=copy.deepcopy(p);proposal_changes.append(dict(proposal_id=pid,lane=lane,before_object_sha256=objsha(before),after_object_sha256=objsha(p),before_capture=before['after_capture'],after_capture=p['after_capture']))
  lr=next(r for r in L['rows'] if r['proposal_id']==pid);lr['previous_successor_after_capture']=copy.deepcopy(lr['successor_after_capture']);lr['successor_after_capture']=copy.deepcopy(p['after_capture']);lr['postseal_predecessor_source_head']='5156d92bec6bd885ca8bae3c5e18bfdce0069176'
 for e in es:
  eid=e['evidence_id']
  if eid in ei:assert ei[eid]==e,('changed inherited evidence',eid)
  else:ei[eid]=copy.deepcopy(e);E['evidence'].append(copy.deepcopy(e))
# Reuse original reviews only for exact unchanged case objects and payloads. New review covers changed entries.
e=dict(evidence_id=rb['evidence_id'],kind='independent_review',capture=dict(root='artifact',path=str(review_path.relative_to(B)),sha256=rb['sha256']),url=None,locator='Exact changed full payloads/case decisions, full source applicability, already-correct Tris/family audit and preserved limitations.',supports_or_contradicts='Authorship-separated scientific review of the declared postseal scope only; authentic earlier reviews support unchanged content with their real attribution.',case_ids=sorted(seenD),accessed_at=rb['completed_at'],reviewer=rb['reviewer'])
assert e['evidence_id'] not in ei;E['evidence'].append(e)
ledger=a.family_ledger.resolve();ledger_id='POSTSEAL-ROOT-FAMILY-LEDGER-SUCCESSOR';cid='CM_NAME:c98f85469e959e1e268c0a4c07a445d17a3e19ba15f579493d946f9cac1c92c8'
E['evidence'].append(dict(evidence_id=ledger_id,kind='source_snapshot',capture=dict(root='artifact',path=str(ledger.relative_to(B)),sha256=sha(ledger)),url=None,locator='Complete current family applicability ledger after four independently identified explanatory-string corrections.',supports_or_contradicts='Supersedes only the four incorrect other-origin explanatory captions in the preserved initial postseal family ledger. Author /root/chemicals_research; independently rereviewed. All source_disposition objects, source IDs, W05 scientific payloads and case reasoning remain unchanged by this ledger amendment.',case_ids=[cid],accessed_at=datetime.now(timezone.utc).isoformat()))
D['decisions'][di[cid]]['evidence_ids'].append(ledger_id)
for change in case_changes:
 if change['case_id']==cid:change['canonical_successor_object_sha256']=objsha(D['decisions'][di[cid]])

assert len(D['decisions'])==len(oldD['decisions']) and set(di)=={d['case_id'] for d in D['decisions']}
assert len(PS['proposals'])==len(oldP['proposals']) and set(pi)=={p['proposal_id'] for p in PS['proposals']}
for i,d in enumerate(D['decisions']):
 if d['case_id'] not in seenD:assert d==oldD['decisions'][i]
for i,p in enumerate(PS['proposals']):
 if p['proposal_id'] not in seenP:assert p==oldP['proposals'][i]
assert E['evidence'][:len(oldE['evidence'])]==oldE['evidence']
L['postseal_predecessor_manifest']=dict(path=str((OLD/'MANIFEST.json').relative_to(W)),sha256=sha(OLD/'MANIFEST.json'));L['postseal_changed_proposals']=sorted(seenP)
for name,x in [('decisions.json',D),('proposals.json',PS),('evidence.json',E),('proposal-lineage.json',L)]:put(P/'core'/name,x)
put(P/'core/assembly-receipt.json',dict(at=datetime.now(timezone.utc).isoformat(),compiler='/root',base='5156d92bec6bd885ca8bae3c5e18bfdce0069176',case_count=len(D['decisions']),selected_proposals=len(PS['proposals']),original_proposal_lineages=oldL['original_count'],evidence_count=len(E['evidence']),retained_evidence_objects=len(oldE['evidence']),changed_case_count=len(seenD),changed_payload_count=len(seenP),unchanged_cases=len(D['decisions'])-len(seenD),unchanged_payloads=len(PS['proposals'])-len(seenP),case_changes=case_changes,proposal_changes=proposal_changes,fragment_bindings=fragments,review=rb,all_source_occurrences_and_holds_preserved=True,no_union_or_owner_application=True))
print(json.dumps(dict(cases=len(D['decisions']),proposals=len(PS['proposals']),evidence=len(E['evidence']),changed_cases=len(seenD),changed_payloads=len(seenP))))
