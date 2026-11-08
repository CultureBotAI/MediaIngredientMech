from pathlib import Path
import json,copy,hashlib,datetime
R=Path('reports/all_unmatched_20261107/worker-01');N=R/'shard/named_stocks/atmosphere1167';patch=json.loads((N/'proposal-patches.json').read_text())['proposals'];ev=json.loads((N/'evidence-patches.json').read_text())['evidence'];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for rel in ['shard/concentration_stocks','shard/root_substances/kg26']:
 O=R/rel;D=json.loads((O/'decisions.fragment.json').read_text());E=json.loads((O/'evidence.fragment.json').read_text());Q=json.loads((O/'proposals.fragment.json').read_text());ids={q['proposal_id'] for q in Q['proposals']};cases={d['case_id'] for d in D['decisions']};selected=[copy.deepcopy(q) for q in patch if q['proposal_id'] in ids];archive=O/'before-atmosphere1167-v1';archive.mkdir()
 for n in ['decisions','evidence','proposals']:(archive/(n+'.fragment.json')).write_bytes((O/(n+'.fragment.json')).read_bytes())
 affected=set()
 for q in selected:
  assert sha(R/q['after_capture']['path'])==q['after_capture']['sha256'];old=next(x for x in Q['proposals'] if x['proposal_id']==q['proposal_id']);old.update(q);old['native_author_review']={'review_id':'20261108T050119Z-w01-atmosphere-material-successors','capture':copy.deepcopy(ev[1]['capture'])};affected.update(q['case_ids'])
 for e in ev:
  x=copy.deepcopy(e);x['case_ids']=sorted(set(x['case_ids'])&cases);E['evidence'].append(x)
 for d in D['decisions']:
  if d['case_id'] in affected:
   d['evidence_ids']=list(dict.fromkeys(d['evidence_ids']+[e['evidence_id'] for e in ev]));d['issue_refs']=list(dict.fromkeys(d['issue_refs']+['https://github.com/CultureBotAI/MediaIngredientMech/issues/1167']));d['reasoning']+=' MIM #1167 successor removes the preparation/storage atmosphere gas from material components while retaining the actual gas condition in source evidence and notes. No gas-solute amount or final dissolved speciation is inferred.'
 for n,a in [('decisions',D),('evidence',E),('proposals',Q)]: (O/(n+'.fragment.json')).write_text(json.dumps(a,indent=2,ensure_ascii=False)+'\n')
 print(rel,'updated',len(selected),'proposals')
script=R/'shard/root_substances/kg26/validate_final_fragments_v4.py';s=script.read_text().replace("root=B if c['root']=='artifact' else S","root=(R if str(p).startswith(('shard/','canary/')) else B) if c['root']=='artifact' else S").replace('fragment-integrity-completeness-v4.json','fragment-integrity-completeness-v5.json');(script.parent/'validate_final_fragments_v5.py').write_text(s)
