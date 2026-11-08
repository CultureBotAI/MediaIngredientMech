from pathlib import Path
import datetime,hashlib,json,subprocess,yaml
O=Path(__file__).resolve().parent; W=O.parents[2]; C=W.parents[2]
def digest(b):return hashlib.sha256(b).hexdigest()
def show(head,path):return subprocess.check_output(['git','show',f'{head}:{path}'],cwd=W)
S=C/'integration/final-application-accounting-v1/materialized-v3/publication-selections.json'
raw=S.read_bytes(); assert digest(raw)=='b9bab76e022d4b9e8f02f30eaabaaffbc5a92ded15464a39892c9915e0b65750'
workers=[]; records=[]; hits=[]
for worker in json.loads(raw):
 slot=worker['worker_slot']; head=worker['selected_head']; core=worker['core']['proposals']
 b=show(head,core['published_path']); assert digest(b)==core['sha256']
 ledger=json.loads(b); props=ledger if isinstance(ledger,list) else ledger['proposals']
 workers.append({'worker_slot':slot,'selected_head':head,'ledger':core,'proposal_count':len(props),'source_acceptance':worker['source_acceptance'],'pending_successor':worker['pending_successor']})
 for p in props:
  cap=p['after_capture']; assert cap['root']=='artifact'
  path=f'reports/all_unmatched_20261107/worker-{slot:02d}/'+cap['path']
  body=show(head,path); assert digest(body)==cap['sha256']
  rec=yaml.safe_load(body); names=[rec.get('identifier',''),rec.get('preferred_term','')]+[s.get('synonym_text','') for s in rec.get('synonyms',[])]
  row={'worker_slot':slot,'head':head,'proposal_id':p['proposal_id'],'published_path':path,'sha256':digest(body),'identifier':rec.get('identifier'),'preferred_term':rec.get('preferred_term'),'names':names}
  records.append(row)
  if any(('apple' in str(n).casefold() and 'pectin' in str(n).casefold()) or 'c84042' in str(n).casefold() for n in names):hits.append(row)
catalog=[]
for root in [W/'data/ingredients',C/'integration/worktree/data/ingredients']:
 files=list(root.rglob('*.yaml'));matches=[]
 for path in files:
  b=path.read_bytes();rec=yaml.safe_load(b)
  if not isinstance(rec,dict):continue
  names=[rec.get('identifier',''),rec.get('preferred_term','')]+[s.get('synonym_text','') for s in rec.get('synonyms',[])]
  if any(('apple' in str(n).casefold() and 'pectin' in str(n).casefold()) or 'c84042' in str(n).casefold() for n in names):matches.append({'path':str(path),'sha256':digest(b),'names':names})
 catalog.append({'root':str(root),'ignored_files_included':True,'yaml_count':len(files),'apple_or_ncit_identity_matches':matches})
result={'schema':'w06-independent-material-current-intake-dedup-v1','reviewer':'/root/residual_material_review','recorded_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'selector_path':str(S),'selector_sha256':digest(raw),'selection_scope':'Explicit materialized-v3 publication selection only; includes per-worker pending successor and acceptance limits. This search neither accepts a later head nor grants owner/role/export approval.','workers':workers,'selected_payload_count':len(records),'selected_payloads':records,'apple_or_ncit_identity_matches':hits,'native_catalogue':catalog,'global_absence_claim':False}
with (O/'current-selector-dedup.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps({'payload_count':len(records),'selected_matches':len(hits),'catalogue_counts':[c['yaml_count'] for c in catalog],'catalogue_matches':[len(c['apple_or_ncit_identity_matches']) for c in catalog]}))
