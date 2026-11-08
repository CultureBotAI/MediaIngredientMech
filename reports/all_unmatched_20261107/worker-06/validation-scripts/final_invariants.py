from pathlib import Path
import json,hashlib,subprocess,datetime,yaml,collections
R=Path('reports/all_unmatched_20261107/worker-06');Q=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
D=json.loads((R/'decisions.json').read_text())['decisions'];E=json.loads((R/'evidence.json').read_text())['evidence'];P=json.loads((R/'proposals.json').read_text())['proposals'];C=json.loads((Q/'shards/shard-06.json').read_text())['cases'];H=json.loads((R/'source-holds.json').read_text())['cases']
errors=[]
def check(ok,msg):
 if not ok:errors.append(msg)
check(len(D)==len(C)==len(H)==188,'Case cardinality')
check([d['case_id'] for d in D]==[c['case_id'] for c in C],'Exact frozen case order')
for c,h in zip(C,H):
 check(c['case_id']==h['case_id'],'Hold case ID')
 for k,v in h['frozen_source_state'].items():check((c[k] if k in c else c.get('original_kg_entry',{}).get(k))==v,f'Changed hold {c["case_id"]} {k}')
 check(h['frozen_case_sha256']==hashlib.sha256(json.dumps(c,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest(),'Hold full-case digest')
holds=sum(len(h['frozen_source_state'].get('downstream_holds',[])) for h in H);check(holds==88,'Expected frozen88 holds')
base='e000d66dd26ab053e9b17ce7bf8d3c873c3dde99'
owners={o['path']:o['sha256'] for d in D for o in d['owner_records']}
for p in P:
 if p['kind']=='edit_existing_owner':owners[p['owner_path']]=p['before_sha256']
for path,expected in owners.items():
 check(sha(Path(path))==expected,'Owner changed '+path)
 before=subprocess.check_output(['git','show',base+':'+path]);check(hashlib.sha256(before).hexdigest()==expected,'Before hash not frozen '+path)
check(len({p['owner_path'] for p in P})==len(P),'Duplicate final owner paths')
check(len({p['proposal_id'] for p in P})==len(P),'Duplicate final proposal IDs')
paths=subprocess.check_output(['rg','--files','--no-ignore','--hidden','data/ingredients'],text=True).splitlines();catalog=collections.defaultdict(list)
for path in paths:
 if path.endswith('.yaml'):
  y=yaml.safe_load(Path(path).read_text());
  if isinstance(y,dict) and y.get('identifier'):catalog[y['identifier']].append(path)
new_ids=collections.defaultdict(list);collisions=[]
for p in P:
 f=R/p['after_capture']['path'];check(sha(f)==p['after_capture']['sha256'],'Payload hash mismatch '+p['proposal_id']);y=yaml.safe_load(f.read_text());new_ids[y['identifier']].append(p['proposal_id'])
 if p['kind']=='new_owner':
  check(not Path(p['owner_path']).exists(),'New owner path already exists '+p['owner_path']);check(not catalog.get(y['identifier']),'New identifier collision '+y['identifier'])
 check(y.get('curation_history',[])[-1].get('llm_assisted') is True,'Missing truthful LLM history '+p['proposal_id'])
 check(datetime.datetime.fromisoformat(y['curation_history'][-1]['timestamp'].replace('Z','+00:00'))<=datetime.datetime.now(datetime.timezone.utc),'Future curation timestamp '+p['proposal_id'])
 for existing in catalog.get(y['identifier'],[]):
  if existing!=p['owner_path']:collisions.append({'proposal_id':p['proposal_id'],'identifier':y['identifier'],'existing_path':existing,'obligation':'Existing shared identifiers require coordinator reconciliation; never a global identity merge.'})
check(not any(len(v)>1 for v in new_ids.values()),'Duplicate proposed identity')
changed=subprocess.check_output(['git','diff','--name-only',base,'--','data','mappings','src','conf','docs','UNIFIED_INGREDIENT_MAPPING.tsv','MAPPING_SEMANTICS.md'],text=True).splitlines();check(not changed,'Maintained paths changed '+str(changed))
out={'status':'PASS' if not errors else 'FAIL','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':'PYTHONDONTWRITEBYTECODE=1 maintained Python3.13 .temp/all-unmatched-worker-06/final_invariants.py','case_count':len(D),'source_counts':dict(collections.Counter(d['source']['source'] for d in D)),'cm_occurrence_id_count':sum(len(d['occurrence_ids']) for d in D),'frozen_hold_row_count':holds,'proposal_count':len(P),'proposal_kinds':dict(collections.Counter(p['kind'] for p in P)),'evidence_count':len(E),'independently_reviewed_case_count':sum(d['independent_review']['status']=='complete' for d in D),'actual_baseline_owner_count':len(owners),'maintained_files_enumerated_including_ignored':len(paths),'existing_shared_identifier_obligations':collisions,'maintained_changed_paths':changed,'errors':errors,'inputs':{str(R/f):sha(R/f) for f in ['decisions.json','evidence.json','proposals.json','source-holds.json']}}
(R/'logs/final-invariants.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n');print(json.dumps(out,indent=2));raise SystemExit(bool(errors))
