"""Publish exact historical observations and their scoped successor bindings.

This makes no terminal finding disposition and supplies no scientific approval.
"""
import argparse,hashlib,json,re
from datetime import datetime,timezone
from pathlib import Path
import yaml
W=Path(__file__).resolve().parents[4];R=Path(__file__).resolve().parent;A=R.parent
B=W/'.temp/w02-final-corrections-v1/frozen-w04-review'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def load(p):return yaml.safe_load(p.read_text()) if p.suffix in ['.yaml','.yml'] else json.loads(p.read_text())
def save(p,x):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x') as f:json.dump(x,f,indent=2,ensure_ascii=False);f.write('\n')
def pointer(doc,value):
 for key in value.lstrip('/').split('/'):
  key=key.replace('~1','/').replace('~0','~');doc=doc[int(key)] if isinstance(doc,list) else doc[key]
 return doc
def walk(x):
 yield x
 if isinstance(x,dict):
  for value in x.values():yield from walk(value)
 elif isinstance(x,list):
  for value in x:yield from walk(value)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--selection',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
 args.out.mkdir(parents=True,exist_ok=False)
 old=load(A/'continuation-1201-v1/decisions.json')['decisions'];new=load(args.selection/'decisions.json')['decisions'];proposals=load(args.selection/'proposals.json')['proposals']
 assert len(old)==len(new)==188
 oldby={x['case_id']:x for x in old};newby={x['case_id']:x for x in new};assert oldby.keys()==newby.keys()
 index={i:d['case_id'] for i,d in enumerate(load(A/'decisions.json')['decisions'])}
 history=load(B/'assembly-v2/all-historical-object-bindings.json');groups=load(B/'assembly-v2/prior-finding-dispositions.json')['groups'];holds=load(B/'assembly-v2/retained-owner-and-source-obligations.json')
 matrix=load(R/'context/w02-final-issue-plan-v1/ACTIONABLE-MATRIX.json')
 assert len(history['objects'])==735 and len(groups)==72
 docs={};copied={}
 def source_original(original):
  p=W/original['path'];assert sha(p)==original['file_sha256']
  if str(p) not in docs:docs[str(p)]=load(p)
  assert pointer(docs[str(p)],original['pointer'])==original['finding']
  return docs[str(p)]
 def capture_peer_refs(value):
  for node in walk(value):
   if not isinstance(node,dict) or 'path' not in node or 'sha256' not in node:continue
   rel=Path(node['path'])
   if rel.is_absolute():
    marker='w02-published-head-independent-review-v1/'
    if marker not in str(rel):continue
    rel=Path(str(rel).split(marker,1)[1])
   if '..' in rel.parts:raise ValueError('Unsafe peer reference')
   p=B/rel
   if not p.is_file():continue
   assert sha(p)==node['sha256'],str(p)
   dest=R/'context/w04-disposition-inputs'/rel
   if not dest.exists():
    dest.parent.mkdir(parents=True,exist_ok=True)
    with dest.open('xb') as f:f.write(p.read_bytes())
   assert sha(dest)==sha(p)
   copied[str(rel)]={'source_sha256':sha(p),'published_path':str(dest.relative_to(W))}
 def cases_of(value):
  result=set()
  for node in walk(value):
   if isinstance(node,str) and node in oldby:result.add(node)
   if isinstance(node,dict):
    for key in ['scope_index','case_index','shard_case_index']:
     if isinstance(node.get(key),int) and node[key] in index:result.add(index[node[key]])
    for key in ['cases','case_indices','affected_case_indices','all_prior_case_indices','all_prior_indices','assigned_case_indices','scope']:
     if isinstance(node.get(key),list):
      result.update(index[i] for i in node[key] if isinstance(i,int) and i in index)
  return sorted(result)
 def bindings(cids):
  return [{'case_id':cid,'old_decision_sha256':digest(oldby[cid]),'successor_decision_sha256':digest(newby[cid]),'source_case_sha256':oldby[cid]['case_input_sha256'],'scientific_source_fields_preserved':all(oldby[cid][k]==newby[cid][k] for k in ['case_id','case_input_sha256','source','occurrence_ids']),
           'current_case_payload_context':[{'proposal_id':p['proposal_id'],'after_capture':p['after_capture'],'owner_path':p['owner_path']} for p in proposals if cid in p['case_ids']],
           'review_status':'Fresh independent successor review required for changed content; original W04 judgments remain historical observations.'} for cid in cids]
 objects=[]
 for i,obj in enumerate(history['objects']):
  doc=source_original(obj['original']);capture_peer_refs(obj);cids=cases_of(obj)
  targetids=obj['original']['finding'].get('target_ids',[])
  targetmap={t['target_id']:t for t in doc.get('targets',[]) if isinstance(t,dict) and 'target_id' in t} if isinstance(doc,dict) else {}
  resolved=[targetmap[t] for t in targetids if t in targetmap]
  objects.append({'historical_object_id':f'W02-HIST-{i:04d}','exact_w04_object':obj,'original_object_sha256':digest(obj['original']['finding']),
                  'complete_original_target_ids':targetids,'original_native_targets':resolved,'target_resolution_note':'All original scope fields and reference objects are retained verbatim. References to previous reviews keep their original repository/review/finding identity; no missing target is invented.',
                  'source_case_bindings':bindings(cids),'deduplicated_issue_refs':sorted(set(re.findall(r'https://github\.com/CultureBotAI/MediaIngredientMech/issues/\d+(?:#issuecomment-\d+)?',json.dumps(obj)))),
                  'disposition':'Preserved exact historical observation and W04 independent dispositions; no blanket reopen, closure or owner approval. Current correction and independent re-review are separate bound ledgers.'})
 stable=[]
 for group in groups:
  for original in group['originals']:source_original(original)
  capture_peer_refs(group);cids=cases_of(group)
  stable.append({'finding_id':group['finding_id'],'exact_w04_disposition_group':group,
                 'original_objects':[{'path':x['path'],'file_sha256':x['file_sha256'],'pointer':x['pointer'],'object_sha256':digest(x['finding'])} for x in group['originals']],
                 'source_case_bindings':bindings(cids),'historical_scientific_dispositions':group.get('independent_dispositions',[]),
                 'current_status':'Historical exact scoped outcomes retained. Changed candidate bytes require current independent assessment; pre-existing unresolved source/owner/role/export obligations remain.',
                 'publication_issue':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1241'})
 save(args.out/'historical-object-lineage.json',{'author':'worker02 /root','created_at':datetime.now(timezone.utc).isoformat(),'objects':objects,'count':735,'original_source_files_verified':len(docs),'scientific_approval':False})
 save(args.out/'stable-finding-lineage.json',{'author':'worker02 /root','groups':stable,'count':72,'scientific_approval':False})
 save(args.out/'retained-holds.json',{'exact_w04_obligations':holds,'declared_frozen_hold_count':337,'rule':'All exact source and owner obligations retained; corrections are unapplied proposals. No source/owner/role/export hold is cleared by publication of this ledger.'})
 save(args.out/'peer-assessment-copies.json',{'copies':copied,'count':len(copied),'original_manifest_sha256':sha(B/'SHA256SUMS')})
 save(args.out/'family-routing.json',{'all16families':matrix['families'],'additional_dependency':matrix['additional_existing_dependency'],'current_successor_selection':{'decisions_sha256':sha(args.selection/'decisions.json'),'proposals_sha256':sha(args.selection/'proposals.json')},'disposition':'Qualified coordinator findings govern. Final per-family correction and exact independent review receipt must be bound separately; no superseded broad wording is applied automatically.'})
 print(json.dumps({'historical_objects':len(objects),'stable_ids':len(stable),'source_files_verified':len(docs),'peer_assessment_copies':len(copied)}))
if __name__=='__main__':main()
