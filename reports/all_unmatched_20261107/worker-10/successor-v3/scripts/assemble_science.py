from pathlib import Path
from datetime import datetime,timezone
import json,copy,hashlib,collections,yaml
R=Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';B=A/'successor-v2';S=A/'successor-v3';O=S/'science-v1';O.mkdir(exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();canon=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest();load=lambda p:json.loads(p.read_text())
def save(p,d):
 with p.open('x') as f:json.dump(d,f,indent=2,ensure_ascii=False);f.write('\n')
D=load(B/'decisions.json');P=load(B/'proposals.json');E=load(B/'evidence.json');oldD=copy.deepcopy(D);oldP=copy.deepcopy(P);oldE=copy.deepcopy(E);bycase={d['case_id']:i for i,d in enumerate(D['decisions'])};new={};changed=set()
for group in ['hcl-manual','serums']:
 for d in load(S/group/'decision-fragment.json')['decisions']:
  i=bycase[d['case_id']];assert i not in changed;changed.add(i)
  prior=D['decisions'][i]
  for field in ['case_id','case_input_sha256','source','occurrence_ids']:assert d[field]==prior[field],(i,field)
  D['decisions'][i]=d
 for p in load(S/group/'proposals-fragment.json')['proposals']:
  oldid=p['supersedes']['proposal_id'];assert oldid not in new;new[oldid]=p
 E['evidence']+=load(S/group/'evidence-fragment.json')['evidence']
retired={'sv1-kg-calf-serum1303'};assert retired.isdisjoint(new)
selected=[];bridge=[]
for old in P['proposals']:
 pid=old['proposal_id'];p=new.get(pid,old) if pid not in retired else None
 if p:selected.append(p)
 bridge.append({'old_proposal_id':pid,'old_proposal_sha256':canon(old),'old_payload':old['after_capture'],'old_owner_path':old['owner_path'],'old_before_sha256':old['before_sha256'],'old_case_ids':old['case_ids'],'selected_proposal_id':p['proposal_id'] if p else None,'selected_payload':p['after_capture'] if p else None,'selected_owner_path':p['owner_path'] if p else None,'selected_before_sha256':p['before_sha256'] if p else None,'selected_case_ids':p['case_ids'] if p else [],'disposition':'retained_exact' if p==old else 'source_corrected_successor' if p else 'retired_active_candidate_mixed_owner_continuity_hold','reason':'BIO-F03 mixed whole-owner applicability unresolved; exact original proposal remains historical, not co-installed.' if not p else p.get('supersedes',{}).get('reason','Unchanged predecessor selected bytes and source scope; original author attribution retained.'),'historical_proposal':old})
P['proposals']=selected
assert len({e['evidence_id'] for e in E['evidence']})==len(E['evidence'])
assert changed=={19,28,40,42,53,61,65,87,94,98,102,105,109,125,129,158,178,181},changed
assert len(D['decisions'])==len(oldD['decisions'])==188
ps={p['proposal_id']:p for p in selected};assert len(ps)==len(selected)
for i,d in enumerate(D['decisions']):
 if i not in changed:assert d==oldD['decisions'][i]
 for pid in d['proposal_ids']:assert pid in ps and d['case_id'] in ps[pid]['case_ids'],(i,pid)
for p in selected:
 assert sha(A/p['after_capture']['path'])==p['after_capture']['sha256'];assert set(p['case_ids'])=={d['case_id'] for d in D['decisions'] if p['proposal_id'] in d['proposal_ids']}
 if p['before_sha256']:assert sha(R/p['owner_path'])==p['before_sha256']
for i in [143,187,21]:assert D['decisions'][i]==oldD['decisions'][i]
assert E['evidence'][:len(oldE['evidence'])]==oldE['evidence']
for n,x in [('decisions.json',D),('proposals.json',P),('evidence.json',E)]:save(O/n,x)
save(O/'retirement-bridge.json',{'at':datetime.now(timezone.utc).isoformat(),'predecessor_head':'808ff934f9cdec7ad8fdc8cdcaa583f1ae068d5e','predecessor_core_sha256':sha(B/'proposals.json'),'old_proposal_count':len(oldP['proposals']),'selected_proposal_count':len(selected),'rows':bridge,'all_old_proposals_and_case_backlinks_preserved':True,'scope':'Authoritative selection bridge at source-correction stage; later claim-specific enum metadata may supersede exact capture but never erase this bridge.'})
save(O/'delta.json',{'changed_scientific_indices':sorted(changed),'retained_exact_decision_indices':[i for i in range(188) if i not in changed],'case_changes':[{'source_index':i,'old_decision_sha256':canon(oldD['decisions'][i]),'new_decision_sha256':canon(D['decisions'][i]),'old':oldD['decisions'][i],'new':D['decisions'][i]} for i in sorted(changed)],'original_evidence_prefix_count':len(oldE['evidence']),'two_case_successor_preserved':{'case143_exact':True,'case187_exact':True,'case21_exact':True,'isp4_payload_exact':ps['sv2-isp4-jcm58-complete-formulation']['after_capture']==next(p['after_capture'] for p in oldP['proposals'] if p['proposal_id']=='sv2-isp4-jcm58-complete-formulation'),'carbonate_payload_exact_before1226':True}})
print(json.dumps({'science_cases':len(changed),'selected_proposals':len(selected),'retired':sorted(retired),'evidence':len(E['evidence'])}))
