"""Assemble a complete active shard from immutable predecessor and reviewed successors."""
import copy,datetime,hashlib,json
from pathlib import Path
S=Path(__file__).resolve().parents[1]; W=Path(__file__).resolve().parents[3]; R=Path(__file__).resolve().parents[6]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def digest(obj):return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def build():
 old=json.loads((W/'decisions.json').read_text()); prior={d['case_id']:d for d in old['decisions']}; active=copy.deepcopy(prior)
 evidence={e['evidence_id']:e for e in json.loads((W/'evidence.json').read_text())['evidence']}; props={p['proposal_id']:p for p in json.loads((W/'proposals.json').read_text())['proposals']}
 bindings=[];assessments=[];changes={};superseded=[];new_props=[]
 pairs={'biological':'media','chemistry':'biological','media':'chemistry'}
 selection=json.loads((S/'independent-review/review-selection.json').read_text())
 for group,reviewer in pairs.items():
  review_path=S/selection[group]['path'];assert review_path.is_relative_to(S/'independent-review')
  assert sha(review_path)==selection[group]['sha256'],('review selection changed',group)
  review=json.loads(review_path.read_text());assert review['status']=='complete',group
  assert review['scientific_disposition']=='accepted_narrow_scope',('unresolved skeptical review findings',group)
  hashes=review['reviewed_fragment_hashes']; fragments={}
  for kind in ['reassessments','decisions','evidence','proposals']:
   rel=f'fragments/{group}-{kind}.json';p=S/rel;expected=hashes.get(rel,hashes.get(p.name));assert expected==sha(p),(rel,expected,sha(p));fragments[kind]=json.loads(p.read_text())[kind]
  assigned={x['published_decision']['case_id'] for x in json.loads((S/'fragments'/f'{group}-assignment.json').read_text())['cases']}
  reassessed={x['case_id'] for x in fragments['reassessments']};assert assigned==reassessed and len(reassessed)==len(fragments['reassessments'])
  for a in fragments['reassessments']:
   original_hash=a.get('old_decision_sha256',a.get('predecessor_decision_sha256',a.get('published_decision_sha256')))
   assert original_hash==digest(prior[a['case_id']]),('reassessment predecessor mismatch',a['case_id'])
  changed={d['case_id'] for d in fragments['decisions']}; reviewed={x['case_id'] for x in review['case_reviews']};assert assigned|changed<=reviewed<=set(prior)
  payload_reviews={p['proposal_id']:p for p in review['payload_reviews']}
  assert len(payload_reviews)==len(review['payload_reviews'])
  assert set(payload_reviews)=={p['proposal_id'] for p in fragments['proposals']},('payload review coverage',group)
  for p in fragments['proposals']:
   pr=payload_reviews[p['proposal_id']]
   assert pr['full_payload_read'] is True and pr['sha256']==p['after_capture']['sha256'] and pr['path']==p['after_capture']['path'],('payload review binding',p['proposal_id'])
   assert sha(W/p['after_capture']['path'])==pr['sha256'],('reviewed payload changed',p['proposal_id'])
  rid='I1201-INDEPENDENT-'+group
  evidence[rid]={'evidence_id':rid,'kind':'independent_review','capture':{'root':'artifact','path':str(review_path.relative_to(W)),'sha256':sha(review_path)},'url':None,'locator':'All assigned no-change reassessments and every changed case/payload, with exact final fragment hashes','supports_or_contradicts':'Authorship-separated skeptical successor review. No maintained owner, role, source hold or export approval.','case_ids':sorted(reviewed)}
  for e in fragments['evidence']:
   if e['evidence_id'] in evidence:assert evidence[e['evidence_id']]==e,('conflicting reused evidence',e['evidence_id'])
   else:evidence[e['evidence_id']]=e
  for d in fragments['decisions']:
   cid=d['case_id'];assert cid in prior and cid not in changes,cid
   for key in ['case_id','case_input_sha256','source','occurrence_ids']:assert d[key]==prior[cid][key],(cid,key)
   for key in prior[cid]:
    if 'hold' in key:assert d.get(key)==prior[cid][key],('changed inherited hold',cid,key)
   author_digest=digest(d);d=copy.deepcopy(d);d['independent_review']={'status':'complete','evidence_ids':[rid]}
   d['successor_assessment']={'issue':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1201','predecessor_head':'0d2c73e5aee5adb88782537755472d9ca0c5c3cd','predecessor_decision_sha256':digest(prior[cid]),'author_fragment_decision_sha256':author_digest,'scope':'Source-specific assessment/proposal binding; all native holds and no-role/no-release scope retained.'}
   active[cid]=d;changes[cid]={'group':group,'predecessor_sha256':digest(prior[cid]),'author_sha256':author_digest,'active_sha256':digest(d),'independent_review':rid}
  for p in fragments['proposals']:
   assert p['proposal_id'] not in props and p['proposal_id'] not in {x['proposal_id'] for x in new_props}
   for old_id in p.get('supersedes_proposal_ids',[]):
    assert old_id in props,('missing/doubly superseded proposal',old_id)
    old_p=props.pop(old_id);assert set(old_p['case_ids'])<=set(p['case_ids']),('lost case backlink',old_id)
    assert p['owner_path']==old_p['owner_path'] and p['before_sha256']==old_p['before_sha256'],('changed owner baseline',old_id)
    superseded.append({'predecessor_proposal_id':old_id,'successor_proposal_id':p['proposal_id'],'predecessor_payload':old_p['after_capture'],'successor_payload':p['after_capture']})
   new_props.append(p)
  assessments.extend(fragments['reassessments']);bindings.append({'group':group,'primary_case_count':len(assigned),'changed_case_count':len(changed),'reviewed_case_ids':sorted(reviewed),'review':str(review_path.relative_to(W)),'review_sha256':sha(review_path),'fragment_hashes':hashes})
 for p in new_props:props[p['proposal_id']]=p
 assert len(assessments)==108 and len({a['case_id'] for a in assessments})==108
 assert {a['case_id'] for a in assessments}=={d['case_id'] for d in prior.values() if not d['proposal_ids']}
 assert len({p['owner_path'] for p in props.values()})==len(props),'multiple active payloads for same owner'
 for d in active.values():
  for pid in d['proposal_ids']:assert pid in props and d['case_id'] in props[pid]['case_ids'],('case proposal backlink',d['case_id'],pid)
  for eid in d['evidence_ids']+d['independent_review']['evidence_ids']:assert eid in evidence,(d['case_id'],eid)
 for p in props.values():
  for cid in p['case_ids']:assert p['proposal_id'] in active[cid]['proposal_ids'],('proposal case backlink',p['proposal_id'],cid)
  for eid in p['evidence_ids']:assert eid in evidence,(p['proposal_id'],eid)
 normalizations=[]
 for e in evidence.values():
  if 'case_ids' in e and len(e['case_ids'])!=len(set(e['case_ids'])):
   before=e['case_ids'];e['case_ids']=list(dict.fromkeys(before));normalizations.append({'evidence_id':e['evidence_id'],'before':before,'after':e['case_ids'],'scope':'Set-preserving duplicate reference removal only; original fragment untouched.'})
 result=copy.deepcopy(old);result['decisions']=[active[d['case_id']] for d in old['decisions']]
 for name,obj in [('decisions',result),('evidence',{'schema_version':1,'evidence':list(evidence.values())}),('proposals',{'schema_version':1,'proposals':list(props.values())}),('reassessments',{'schema_version':1,'reassessments':assessments})]:(S/f'{name}.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
 receipt={'assembled_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'predecessor_head':'0d2c73e5aee5adb88782537755472d9ca0c5c3cd','bindings':bindings,'changed_cases':changes,'superseded_proposals':superseded,'normalizations':normalizations,'case_count':len(active),'reassessed_no_change_count':len(assessments),'changed_case_count':len(changes),'new_successor_proposal_count':len(new_props),'active_proposal_count':len(props),'evidence_count':len(evidence),'scientific_or_release_approval':False}
 (S/'validation/assembly-bindings.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({k:v for k,v in receipt.items() if k.endswith('_count')},indent=2))
if __name__=='__main__':build()
