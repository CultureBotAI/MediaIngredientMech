import json,pathlib,sys,hashlib,yaml,subprocess,re,html,datetime
R=pathlib.Path('reports/all_unmatched_20261107/worker-08');A=R/'successors/issue-1227-v1/research/organic_products';O=R/'successors/issue-1227-v1/independent-review/organic_products'
H=json.loads((A/'PRIMARY-HANDOFF.json').read_text());D=json.loads((A/H['final_selection']['decisions']).read_text());P=json.loads((A/H['final_selection']['proposals']).read_text())
D=D['decisions'] if isinstance(D,dict) else D;P=P['proposals'] if isinstance(P,dict) else P
old=json.loads((R/'successors/issue-1201-v1/evidence.json').read_text())['evidence'];new=json.loads((A/H['final_selection']['evidence_additions']).read_text());new=new.get('evidence',[]) if isinstance(new,dict) else new;E={x['evidence_id']:x for x in old+new}
C={x['case_id']:x for x in json.loads((R/'provenance/shard-08.json').read_text())['cases']}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def compact(x):
 s={};d={}
 def rec(x):
  if isinstance(x,str) and len(x)>150:
   if x not in s:k='S'+str(len(s)+1);s[x]=k;d[k]=x
   return {'$text':s[x]}
  if isinstance(x,list):return [rec(v) for v in x]
  if isinstance(x,dict):return {k:rec(v) for k,v in x.items()}
  return x
 y=rec(x);return json.dumps({'strings':d,'document':y},ensure_ascii=False,separators=(',',':'))
def log(kind,p,scope,eid=None):
 with (O/'read-events.jsonl').open('a') as f:f.write(json.dumps({'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'kind':kind,'path':str(p),'sha256':sha(p),'scope_rendered':scope,'evidence_id':eid})+'\n')
mode=sys.argv[1]
if mode=='payloads':
 for i in map(int,sys.argv[2:]):
  p=P[i];fp=R/p['after_capture']['path'];assert sha(fp)==p['after_capture']['sha256'];d=yaml.safe_load(fp.read_text());print('PAYLOAD',i,p['proposal_id'],p['after_capture']);print(compact(d));log('entire_payload',fp,'Entire semantic YAML including all history; repeated long strings interned losslessly.')
  before=pathlib.Path(p['owner_path'])
  if p['before_sha256']:
   assert sha(before)==p['before_sha256'];b=yaml.safe_load(before.read_text());delta={k:b.get(k) for k in set(b)|set(d) if b.get(k)!=d.get(k) and k!='curation_history'};delta['prior_history_is_prefix']=d.get('curation_history',[])[:len(b.get('curation_history',[]))]==b.get('curation_history',[]);print('PREIMAGE_DELTA',compact(delta));log('frozen_beforeimage',before,'Whole beforeimage read programmatically and semantic difference rendered; identical fields were read in whole selected payload.')
elif mode=='cases':
 for i in map(int,sys.argv[2:]):
  d=D[i];c=C[d['case_id']];print('CASE',i,compact(d));raw=c.get('original_kg_entry',{}).get('source_record');print('FROZEN_RAW',compact(raw if raw is not None else c.get('occurrences')))
elif mode=='source':
 for eid in sys.argv[2:]:
  e=E[eid];cap=e['capture'];print('EVIDENCE',json.dumps(e,ensure_ascii=False))
  if cap['root']!='artifact':print('NON_ARTIFACT');continue
  p=R/cap['path'];assert sha(p)==cap['sha256'];b=p.read_bytes()
  if b.startswith(b'%PDF'):text=subprocess.check_output(['pdftotext','-layout',str(p),'-']).decode()
  else:text=b.decode(errors='replace')
  if '<html' in text.lower() or '<!doctype' in text.lower():
   text=re.sub(r'<(script|style)\b[^>]*>.*?</\1>','',text,flags=re.S|re.I);text=html.unescape(re.sub('<[^>]*>',' ',text));text=re.sub(r'[ \t]+',' ',text);text=re.sub(r'\n\s*\n+','\n',text)
  try:
   obj=json.loads(text)
   if isinstance(obj,dict) and isinstance(obj.get('response'),str): print(obj['response'])
   else: print(compact(obj))
  except ValueError:print(text)
  log('actual_source',p,e.get('locator'),eid)
