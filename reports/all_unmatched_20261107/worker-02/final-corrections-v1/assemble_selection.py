"""Compose explicit author fragments without altering frozen source fields."""
from copy import deepcopy
from datetime import datetime,timezone
import argparse,hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parent;A=R.parent
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def contained_output(path):
 if '..' in path.parts:raise ValueError('Traversal in output path')
 absolute=path.absolute()
 if absolute!=absolute.resolve() or not absolute.resolve().is_relative_to(R.resolve()):raise ValueError('Output outside new report packet')
 return absolute
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def unique(rows,key):
 result={}
 for row in rows:
  if row[key] in result:raise ValueError('Duplicate '+key)
  result[row[key]]=row
 return result
def verify_case_core(old,new):
 for key in ['case_id','case_input_sha256','source','occurrence_ids']:
  if old[key]!=new[key]:raise ValueError('Frozen source field changed: '+key)
def union(values):
 result=[]
 for value in values:
  for item in value:
   if item not in result:result.append(item)
 return result
def compose_case(old,updates):
 for _,d in updates:verify_case_core(old,d)
 result=deepcopy(old);authors=[]
 for author,_ in updates:
  if author not in authors:authors.append(author)
 keys=set().union(*(d.keys() for _,d in updates))
 for key in keys:
  changed=[d[key] for _,d in updates if key in d and d[key]!=old.get(key)]
  if not changed:continue
  if key=='independent_review':continue
  if all(value==changed[0] for value in changed):result[key]=deepcopy(changed[0])
  elif key in ['evidence_ids','issue_refs','proposal_ids','owner_records']:
   result[key]=union(changed)
  elif key in ['reasoning','applicability']:
   # Only explicit source-scope compositions; each whole author argument retained.
   allowed={'CM_NAME:03abc18649d46be7f284bcdfb767b82ea714e6b17ea60540cd8debedb5d2bdf6','CM_NAME:73beedc4877a52651a2da1b739bf1ac1cb6e8a1be8fee22a5b7591dad508b754'}
   if old['case_id'] not in allowed:raise ValueError('Scientific prose conflict requires explicit adjudication: '+old['case_id'])
   result[key]=' '.join(dict.fromkeys(changed))
  elif key=='primary_author':result[key]='worker02 /root (explicit composition of separately attributed authors)'
  elif key=='final_correction_notes':result[key]=union([v if isinstance(v,list) else [v] for v in changed])
  else:raise ValueError('Unresolved author conflict: '+old['case_id']+' '+key)
 result['independent_review']={'status':'pending','evidence_ids':[]}
 return result,authors
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--inputs',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
 spec=load(args.inputs);args.out=contained_output(args.out);args.out.mkdir(parents=True,exist_ok=False)
 originals={n:load(A/'continuation-1201-v1'/(n+'.json')) for n in ['decisions','proposals','evidence']}
 decisions=unique(originals['decisions']['decisions'],'case_id');proposals=unique(originals['proposals']['proposals'],'proposal_id');evidence=unique(originals['evidence']['evidence'],'evidence_id')
 updates={};retired=[];authors={};capture_inputs=[];eid_replacements={}
 for block in spec['fragments']:
  author=block['author'];doc={}
  for key,ref in block['files'].items():
   path=R/ref['path'];assert sha(path)==ref['sha256'],str(path);capture_inputs.append({'path':str(path),'sha256':ref['sha256']});value=load(path)
   if key=='fragment':doc.update(value)
   else:doc[key]=value[key]
   if isinstance(value,dict) and value.get('superseded_proposal_ids'):retired.extend(value['superseded_proposal_ids'])
  retired.extend(doc.get('superseded_proposal_ids',[]));eid_replacements.update(doc.get('evidence_id_replacements',{}))
  for d in doc.get('decisions',[]):
   if d['case_id'] not in decisions:raise ValueError('Foreign case')
   updates.setdefault(d['case_id'],[]).append((author,d))
  for p in doc.get('proposals',[]):
   if p['proposal_id'] in authors:raise ValueError('Concurrent proposal authors require explicit full composition')
   proposals[p['proposal_id']]=p;authors[p['proposal_id']]=[author]
  for e in doc.get('evidence',[]):
   if e['evidence_id'] in evidence:raise ValueError('Duplicate evidence ID')
   evidence[e['evidence_id']]=e
 case_authors={};compositions=[]
 for cid,rows in updates.items():
  result,who=compose_case(decisions[cid],rows);compositions.append({'case_id':cid,'old_sha256':digest(decisions[cid]),'author_fragments':[{'author':a,'decision':d,'sha256':digest(d)} for a,d in rows],'successor_sha256':digest(result),'composition_author':'worker02 /root' if len(rows)>1 else who[0]});decisions[cid]=result;case_authors[cid]=who+(['worker02 /root'] if len(rows)>1 else [])
 for ref in spec.get('context_patches',[]):
  path=R/ref['path'];assert sha(path)==ref['sha256'];patch=load(path);cid=patch['case_id'];d=decisions[cid];verify_case_core(d,patch)
  if cid!='CM_NAME:73beedc4877a52651a2da1b739bf1ac1cb6e8a1be8fee22a5b7591dad508b754':raise ValueError('Unreviewed context-only patch')
  before=deepcopy(d)
  if ref.get('already_applied'):
   assert patch['append_reasoning'] in d['reasoning']
   for key in ['proposal_ids','evidence_ids','issue_refs']:assert all(x in d[key] for x in patch['append_'+key])
   assert d['context_only_proposal_ids']==patch['context_only_proposal_ids']
  else:
   for key in ['proposal_ids','evidence_ids','issue_refs']:d[key]=union([d[key],patch['append_'+key]])
   d['reasoning']+=' '+patch['append_reasoning'];d['applicability']+=' '+patch['append_reasoning']
   d['context_only_proposal_ids']=patch['context_only_proposal_ids'];d['independent_review']={'status':'pending','evidence_ids':[]}
  case_authors[cid]=list(dict.fromkeys(case_authors.get(cid,[])+['worker02 /root/research_c','worker02 /root']))
  compositions.append({'case_id':cid,'prior_composed_sha256':digest(before),'context_patch':ref,'successor_sha256':digest(d),'scope':patch['patch_scope']});capture_inputs.append({'path':str(path),'sha256':ref['sha256']})
 superseded=[]
 for pid in dict.fromkeys(retired):
  superseded.append(proposals.pop(pid));authors.pop(pid,None)
 for p in proposals.values():p['evidence_ids']=list(dict.fromkeys(eid_replacements.get(e,e) for e in p['evidence_ids']))
 for d in decisions.values():
  d['evidence_ids']=list(dict.fromkeys(eid_replacements.get(e,e) for e in d['evidence_ids']))
  if any(pid in retired for pid in d['proposal_ids']):raise ValueError('Retired proposal still selected by case')
 for e in eid_replacements:
  if e in evidence:del evidence[e]
 for p in proposals.values():
  for cid in p['case_ids']:
   if p['proposal_id'] not in decisions[cid]['proposal_ids']:raise ValueError('Missing case backlink: '+p['proposal_id']+' '+cid)
 for d in decisions.values():
  for pid in d['proposal_ids']:
   if d['case_id'] not in proposals[pid]['case_ids']:raise ValueError('Missing proposal backlink: '+pid)
 for original in originals['decisions']['decisions']:verify_case_core(original,decisions[original['case_id']])
 if len(decisions)!=188:raise ValueError('Full case accounting changed')
 result={'decisions':dict(originals['decisions'],decisions=[decisions[d['case_id']] for d in originals['decisions']['decisions']]),'proposals':{'schema_version':1,'proposals':list(proposals.values())},'evidence':{'schema_version':1,'evidence':list(evidence.values())},'composition':{'assembled_at':datetime.now(timezone.utc).isoformat(),'author':'worker02 /root','inputs':capture_inputs,'case_compositions':compositions,'retired_selected_proposals':superseded,'proposal_authors':authors,'case_authors':case_authors,'evidence_id_replacements':eid_replacements,'scientific_approval':False}}
 for name,value in result.items():
  with (args.out/(name+'.json')).open('x') as f:json.dump(value,f,indent=2,ensure_ascii=False);f.write('\n')
 print(json.dumps({'cases':len(decisions),'proposals':len(proposals),'changed_case_fragments':len(updates),'retired':len(superseded),'evidence':len(evidence)}))
if __name__=='__main__':main()
