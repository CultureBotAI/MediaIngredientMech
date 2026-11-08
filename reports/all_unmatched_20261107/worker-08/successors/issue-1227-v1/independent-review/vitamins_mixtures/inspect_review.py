"""Read-only independent inspection, writing only this review's read ledger."""
import datetime, hashlib, json, re, subprocess, sys
from pathlib import Path
from html import unescape
import yaml
B=Path('reports/all_unmatched_20261107/worker-08')
S=B/'successors/issue-1227-v1'
M=S/'research/vitamins_mixtures'
R=S/'independent-review/vitamins_mixtures'
SRC=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rows(p,key):
 x=json.loads(p.read_text());return x[key] if isinstance(x,dict) else x
A=json.loads((M/'assignment.json').read_text())
E={e['evidence_id']:e for e in rows(B/'successors/issue-1201-v1/evidence.json','evidence')}
P=rows(M/'final-v1/proposals.json','proposals')
D=rows(M/'final-v1/decisions.json','decisions')
C={c['case_id']:c for c in rows(B/'provenance/shard-08.json','cases')}
def log(p,purpose,locator):
 with (R/'read-log.jsonl').open('a') as f:f.write(json.dumps({'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'path':str(p),'sha256':sha(p),'purpose':purpose,'locator':locator})+'\n')
def text(p):
 b=p.read_bytes()
 if b.startswith(b'%PDF'):return subprocess.run(['pdftotext','-layout',str(p),'-'],check=True,text=True,capture_output=True).stdout
 t=b.decode(errors='replace');t=re.sub(r'<script\b[^>]*>.*?</script>|<style\b[^>]*>.*?</style>',' ',t,flags=re.S|re.I)
 return unescape(re.sub('<[^>]+>',' ',t))
mode=sys.argv[1]
if mode=='start':
 (R/'progress.json').write_text(json.dumps({'reviewer':'/root/organics','author':'/root/vitamins','scope':{'cases':len(D),'payloads':len(P)},'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'reading original sources and beforeimages; author final freeze pending','completed_cases':0,'completed_payloads':0},indent=2)+'\n')
elif mode=='list':
 for i,p in enumerate(P):
  q=B/p['after_capture']['path'];x=yaml.safe_load(q.read_text());print(i,p['proposal_id'],x['preferred_term'],len(x.get('components',[])),q.name)
elif mode=='payload':
 for i in map(int,sys.argv[2:]):
  p=P[i];q=B/p['after_capture']['path'];print('\nPAYLOAD',i,p['proposal_id'],sha(q));print(q.read_text());log(q,'Complete candidate owner displayed including history','entire YAML')
elif mode=='compact':
 for i in map(int,sys.argv[2:]):
  p=P[i];q=B/p['after_capture']['path'];x=yaml.safe_load(q.read_text())
  for c in x.get('components',[]):
   if 'source' in c:
    c['source']=re.sub(r'Issue 1227 IR003 component-specific adjudication: The cited recipe names (.*?); the inspected active catalog and primary ontology identity (.*?) match this stated chemical form\. Source spelling, amount, unit and preparation boundary are preserved; no role, owner-wide or export approval is transferred\.',r'[Repeated literal form-match assertion: source=\1; target=\2; amounts/boundary preserved; no role/export approval.]',c['source'])
  print('\nPAYLOAD',i,p['proposal_id'],sha(q));print(yaml.safe_dump(x,sort_keys=False,allow_unicode=True));log(q,'Complete owner parsed and displayed, only previously read repeated exact component-source template abbreviated','all fields; no identity/quantity/history omitted')
elif mode=='source':
 for eid in sys.argv[2:]:
  e=E[eid];cap=e['capture'];q=(B if cap['root']=='artifact' else SRC)/cap['path'];assert sha(q)==cap['sha256'];print('\nSOURCE',eid,e.get('url'),e['locator']);print(re.sub(r'\s+',' ',text(q)));log(q,'Actual retained source capture displayed',e['locator'])
elif mode=='sources':
 for i in map(int,sys.argv[2:]):
  p=P[i];print('\n',i,p['proposal_id'])
  for eid in p['evidence_ids']:
   if eid in E:
    e=E[eid]
    if e['kind'] in ['primary_source','ontology','unsuccessful_search']:print(eid,e.get('url'),e['capture']['path'])
elif mode=='case':
 for i in map(int,sys.argv[2:]):
  d=D[i];c=C[d['case_id']];print('\nCASE',i,json.dumps(d,ensure_ascii=False));print('FROZEN',json.dumps(c,ensure_ascii=False));log(B/'provenance/shard-08.json','Full original case displayed',d['case_id']);log(M/'decisions.json','Full final/draft decision displayed',d['case_id'])
elif mode=='apitable':
 for eid in sys.argv[2:]:
  e=E[eid];q=B/e['capture']['path'];assert sha(q)==e['capture']['sha256'];x=json.loads(q.read_text());d=x.get('data',x);print('\nSOURCE',eid,e.get('url'))
  if 'recipe' in d:
   print(d.get('id'),d.get('name'),d.get('volume'));print(json.dumps([{k:v for k,v in row.items()if v is not None} for row in d['recipe']],ensure_ascii=False));print('STEPS',json.dumps(d.get('steps'),ensure_ascii=False))
  else:print(json.dumps(x,ensure_ascii=False))
  log(q,'Entire source JSON parsed; recipe and every preparation step displayed','data.recipe and data.steps; outer metadata hash-bound')
elif mode=='casecompact':
 for i in map(int,sys.argv[2:]):
  d=D[i];c=C[d['case_id']];print('\nCASE',i,d['case_id'],d['source']['source_label']);print(json.dumps({k:v for k,v in d.items()if k not in ['evidence_ids','occurrence_ids','independent_review','source','case_id','case_input_sha256','applicability','issue_refs','owner_records','publication_scope']},ensure_ascii=False));print('APPLICABILITY',d['applicability'].replace(d['reasoning'],'[Identical reasoning already displayed]'))
  print('BASELINE',json.dumps({k:v for k,v in c.items()if k in ['baseline_outcome','native_match_result','native_occurrence_count','prior_dependency']},ensure_ascii=False))
  for oc in c.get('occurrences',[]):
   q=SRC/oc['full_recipe_snapshot'];assert sha(q)==oc['source_file_sha256'];recipe=yaml.safe_load(q.read_text());v=recipe
   for t in oc['component_path'].split('/'):v=v[int(t)]if isinstance(v,list)else v[t]
   assert v==oc['raw_component'];print('OCCURRENCE',oc['recipe_id'],oc['component_path'],json.dumps(oc['raw_component'],ensure_ascii=False));log(q,'Full recipe parsed; exact assigned row and source pointer inspected',oc['component_path'])
  log(B/'provenance/shard-08.json','Full case parsed; all occurrence raw components displayed; metadata retained by hash',d['case_id']);log(M/'final-v1/decisions.json','Complete operative reasoning, applicability, limits and outcomes displayed',d['case_id'])
elif mode=='file':
 for n in sys.argv[2:]:
  p=Path(n);print('\nFILE',p,sha(p));print(text(p));log(p,'Full independent inspection','entire file')
