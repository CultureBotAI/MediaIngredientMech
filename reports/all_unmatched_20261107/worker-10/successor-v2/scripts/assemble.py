"""Append-only C001/C002 successor assembly; original author objects stay immutable."""
from pathlib import Path
from datetime import datetime,timezone
import json,copy,hashlib,collections,sys
R=Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v2';V=A/'successor-v1';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();canon=lambda d:hashlib.sha256(json.dumps(d,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest();load=lambda p:json.loads(p.read_text())
def save(p,d):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x') as f:json.dump(d,f,indent=2,ensure_ascii=False);f.write('\n')
D=copy.deepcopy(load(V/'decisions.json'));E=copy.deepcopy(load(V/'evidence.json'));P=copy.deepcopy(load(V/'proposals.json'));oldD=copy.deepcopy(D);oldP=copy.deepcopy(P);oldE=copy.deepcopy(E)
for group,idx in [('isp4',143),('carbonate',187)]:
 d=load(S/group/'decision-fragment.json');assert d['case_id']==D['decisions'][idx]['case_id'];D['decisions'][idx]=d
 es=load(S/group/'evidence-fragment.json')['evidence'];E['evidence']+=es
isp=load(S/'isp4/proposals-fragment.json')['proposals'];assert len(isp)==1,'Nested stock must not be duplicated'
new=isp[0];old='kg-isp4-remove-salt-parent';pos=next(i for i,p in enumerate(P['proposals']) if p['proposal_id']==old);P['proposals'][pos]=new
carbonate=load(S/'carbonate/proposal-fragment.json');pos=next(i for i,p in enumerate(P['proposals']) if p['proposal_id']==carbonate['proposal_id']);P['proposals'][pos]=carbonate
for i in [143,187]:
 D['decisions'][i]['issue_refs']=list(dict.fromkeys(D['decisions'][i]['issue_refs']+['https://github.com/CultureBotAI/MediaIngredientMech/issues/1201#issuecomment-6718398061']))
for i in range(188):
 if i not in [143,187]:assert D['decisions'][i]==oldD['decisions'][i],i
assert len(P['proposals'])==128 and len(D['decisions'])==188
assert E['evidence'][:len(oldE['evidence'])]==oldE['evidence'];assert len({e['evidence_id'] for e in E['evidence']})==len(E['evidence'])
oldps={p['proposal_id']:p for p in oldP['proposals']};newps={p['proposal_id']:p for p in P['proposals']};unchanged=[]
for pid,p in oldps.items():
 if pid in [old,carbonate['proposal_id']]:continue
 assert newps[pid]==p,pid;unchanged.append(pid)
assert len(unchanged)==126
for p in P['proposals']:assert sha(A/p['after_capture']['path'])==p['after_capture']['sha256']
assert carbonate['after_capture']==oldps[carbonate['proposal_id']]['after_capture'];assert carbonate['before_sha256']==oldps[carbonate['proposal_id']]['before_sha256']
assert new['before_sha256']==oldps[old]['before_sha256'];assert new['owner_path']==oldps[old]['owner_path']
assert len({p['owner_path'] for p in P['proposals']})==128
now=datetime.now(timezone.utc).isoformat();changes={'at':now,'predecessor_head':'468766d941e35a74eb2de3c95096660987277d9b','case_changes':[{'source_index':i,'case_id':D['decisions'][i]['case_id'],'old_decision_sha256':canon(oldD['decisions'][i]),'new_decision_sha256':canon(D['decisions'][i]),'old_decision':oldD['decisions'][i],'new_decision':D['decisions'][i]} for i in [143,187]],'unchanged_case_indices':[i for i in range(188) if i not in [143,187]],'unchanged_decision_count':186,'unchanged_proposal_object_count':126,'unchanged_payload_count':127,'proposal_supersession':{'old':oldps[old],'new':new,'meaning':'New isolated formulation preserves old owner/history and parent-removal correction; prior proposal and bytes remain immutable historical artifacts.'},'metadata_only_stock_binding':{'old':oldps[carbonate['proposal_id']],'new':carbonate,'payload_changed':False},'original_evidence_entries_preserved':len(oldE['evidence']),'other_inherited_owner_findings':'Unchanged and reserved for root integration; no EDTA or unrelated alias correction.'}
out=S/'assembly-v1'
for name,d in [('decisions.json',D),('evidence.json',E),('proposals.json',P),('delta.json',changes)]:save(out/name,d)
account={'cases':188,'changed_scientific_decisions':2,'retained_exact_scientific_decisions':186,'proposal_count':128,'changed_payloads':1,'retained_exact_payloads':127,'retained_exact_proposal_objects':126,'metadata_only_proposal_changes':1,'source_occurrence_ids':sum(len(d['occurrence_ids']) for d in D['decisions']),'actual_owner_preimages':len({o['path'] for d in D['decisions'] for o in d['owner_records']}),'evidence_entries':len(E['evidence']),'proposal_kinds':dict(collections.Counter(p['kind'] for p in P['proposals'])),'cases_with_proposals':sum(bool(d['proposal_ids']) for d in D['decisions']),'no_proposal_cases':sum(not d['proposal_ids'] for d in D['decisions']),'scientific_release_approval':False}
save(out/'accounting.json',account);print(json.dumps(account,indent=2))
