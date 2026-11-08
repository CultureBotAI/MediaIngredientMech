import json,hashlib,copy,sys
from pathlib import Path
from datetime import datetime,timezone
R=Path.cwd();S=R/'.temp/w05-buffer-parts-v1';B=R/'reports/all_unmatched_20261107/worker-05/tellurium-polypeptone-v1/core';Q=S/'review'
D=Path(sys.argv[1]);out=Q/sys.argv[2]
def j(p):return json.loads(Path(p).read_text())
def h(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def oh(v):return hashlib.sha256(json.dumps(v,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def bind(p):return {'path':str(Path(p).relative_to(R)) if Path(p).is_absolute() else str(p),'sha256':h(p)}
base=j(B/'decisions.json');bd={x['case_id']:x for x in base['decisions']};expected=copy.deepcopy(bd);cur=j(D/'decisions.json');cd={x['case_id']:x for x in cur['decisions']};receipt=j(D/'composition-receipt.json')
unionfields={'evidence_ids','proposal_ids','owner_records','issue_refs'};assignments={};fragments=[]
def union(target,k,vals):
 a=target.setdefault(k,[])
 for v in vals:
  if v not in a:a.append(v)
for x in receipt['fragments']:
 p=R/x['path'];assert h(p)==x['sha256'];fragments.append(x);d=j(p)
 if x['kind']=='decisions':
  for row in d['decisions']:
   cid=row['case_id'];before=bd[cid];target=expected[cid]
   for k in row.keys()|before.keys():
    if row.get(k)==before.get(k):continue
    assert k in row,('unexpected deletion',cid,k)
    if k in unionfields:union(target,k,row[k])
    else:
     key=(cid,k)
     if key in assignments:assert assignments[key]==row[k],('conflicting authors',key)
     assignments[key]=copy.deepcopy(row[k]);target[k]=copy.deepcopy(row[k])
 elif x['kind']=='case_deltas':
  for row in d.get('case_deltas',d.get('deltas',[])):
   target=expected[row['case_id']]
   for k,v in row.items():
    if k.startswith('union_'):union(target,k[6:],v)
   for k,v in row.get('additions',{}).items():union(target,k,v)
   for k,v in row.get('set_distinct_field',{}).items():
    assert k not in target or target[k]==v;target[k]=copy.deepcopy(v)
   if 'soy_continuity_reassessment' in row:target['soy_continuity_reassessment']=copy.deepcopy(row['soy_continuity_reassessment'])
assert set(cd)==set(bd) and len(cur['decisions'])==len(bd)
assert {k:v for k,v in cur.items() if k!='decisions'}=={k:v for k,v in base.items() if k!='decisions'}
errors=[];rows=[]
for cid,d in cd.items():
 if d!=expected[cid]:errors.append({'case_id':cid,'fields':[k for k in d.keys()|expected[cid].keys() if d.get(k)!=expected[cid].get(k)]})
 protected={k:bd[cid].get(k)==d.get(k) for k in ['case_id','case_input_sha256','source','occurrence_ids','source_holds','owner_holds','export_holds','negative_evidence','inherited_negatives','holds','source_record','disposition'] if k in bd[cid] or k in d}
 assert all(protected.values()),(cid,protected)
 changed=[k for k in d.keys()|bd[cid].keys() if d.get(k)!=bd[cid].get(k)]
 if changed:rows.append({'case_id':cid,'source':d['source'],'selected_decision_object_sha256':oh(d),'changed_fields':sorted(changed),'protected_fields':protected,'old_object_sha256':oh(bd[cid])})
assert not errors,errors
oldE=j(B/'evidence.json')['evidence'];e=j(D/'evidence.json')['evidence'];ei={x['evidence_id']:x for x in e};assert len(ei)==len(e)
for x in oldE:assert ei[x['evidence_id']]==x
oldP={x['proposal_id']:x for x in j(B/'proposals.json')['proposals']};ps=j(D/'proposals.json')['proposals'];pi={x['proposal_id']:x for x in ps};assert len(pi)==len(ps) and set(oldP)<=set(pi)
pchecks=[]
for p in ps:
 assert all(c in bd for c in p['case_ids'])
 old=oldP.get(p['proposal_id']);pchecks.append({'proposal_id':p['proposal_id'],'object_sha256':oh(p),'after_capture':p['after_capture'],'existing_proposal':old is not None,'exact_old_object':old==p if old else False,'same_old_payload':old['after_capture']==p['after_capture'] if old else False,'original_case_ids_preserved':p['case_ids']==old['case_ids'] if old else None})
 if old:assert p['case_ids']==old['case_ids']
v={'reviewer':'/root/final_skeptical','at':datetime.now(timezone.utc).isoformat(),'scope':'Independent reconstruction of root full-case composition against published0bac. Mechanical identity/source/hold preservation, separate from lane scientific review.','input_core':[bind(D/(n+'.json')) for n in ['decisions','proposals','evidence','proposal-lineage']],'fragment_bindings':fragments,'full_decision_composition_exact':True,'decision_count':len(cd),'changed_decision_count':len(rows),'changed_decisions':rows,'proposal_count':len(ps),'prior_proposal_count':len(oldP),'new_proposal_count':len(pi)-len(oldP),'proposal_checks':pchecks,'old_evidence_count':len(oldE),'current_evidence_count':len(e),'old_evidence_objects_identical':True,'errors':errors,'limitation':'Does not approve unreviewed current Polypeptone or other final delta merely because compiled bytes match. Exact final selected science must be bound separately.'}
assert not out.exists();out.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n');print(h(out),len(rows),len(ps),len(e))
