from pathlib import Path
import json,yaml,hashlib,subprocess,datetime
R=Path.cwd();C=R.parents[2];O=R/'.temp/peptone-final-dependencies-v1';S=O/'skeptical-review';sha=lambda b:hashlib.sha256(b).hexdigest();can=lambda x:json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
sel=json.loads((O/'dependency-selection.json').read_text());plan=json.loads((O/'author-plan-v2.json').read_text());led=json.loads((O/'machine-ledger.json').read_text());draft=json.loads((O/'inputs/draft-selection.json').read_text());assert len(sel['dependency_proposals'])==3 and sel['new_frozen_source_cases']==0
for r in sel['dependency_proposals']:
 p=next(x for x in plan['rows'] if x['dependency_id']==r['dependency_id']); assert r['preserved_foreign_source_origin']==p['predecessor_origin'];assert r['frozen_W03_case_ids']==[] and not r['native_source_core_member'];assert r['before_sha256']==sha((R/r['owner_path']).read_bytes());assert r['causal_relationship']==p['causal_parent'];assert sha((O/r['payload']['path']).read_bytes())==r['payload']['sha256'];assert r['selected'] is True
 orig=r['preserved_foreign_source_origin']
 if orig:
  work=C/'workers'/f"w{orig['worker']:02d}"/'worktree';blob=subprocess.check_output(['git','-C',str(work),'show',orig['head']+':'+orig['git_path']]);assert sha(blob)==orig['payload']['sha256'];assert blob==(O/r['input_payload']['path']).read_bytes();assert orig['proposal_object_sha256']==sha(can(orig['proposal']))
for x in sel['preserved_W03_source_core']:assert sha((R/x['path']).read_bytes())==x['sha256']
refs=[]
for p in sorted((R/'data/ingredients').rglob('*.yaml')):
 d=yaml.safe_load(p.read_bytes())
 for i,c in enumerate(d.get('components',[])):
  if c.get('component_id')=='MICRO:0000178' and c.get('reference_scope')=='MIM_CATALOG':refs.append((str(p.relative_to(R)),i,sha(p.read_bytes()),c))
assert len(refs)==19
assert {(a,b,c) for a,b,c,d in refs}=={(x['owner_path'],x['component_index'],x['before_sha256']) for x in led['rows']}
bydraft={x['owner_path']:x for x in draft['parent_incoming_reference_closure']};w05=C/'workers/w05/worktree';count=0;contexts=[]
for row in led['rows']:
 d=bydraft[row['owner_path']];assert row['before_component']==d['before_component']
 if row['existing_W05_proposal']:
  p=row['existing_W05_proposal'];assert p==d['published_w05_proposal'];path=p['payload']['path'].split('inputs-phase2-v1/workers/w05/',1)[1];blob=subprocess.check_output(['git','-C',str(w05),'show','108e213e96f7d423ee345ce265d692e79063127c:'+path]);assert sha(blob)==p['payload']['sha256'];record=yaml.safe_load(blob);assert record['components'][row['component_index']]==row['existing_W05_component'];count+=1
  contexts.append({'owner_path':row['owner_path'],'proposal_id':p['proposal_id'],'git_path':path,'payload_sha256':sha(blob),'in_combined37':row['in_combined37'],'component':row['existing_W05_component'],'scope':'Accounting/hold preservation only; no reapproval of all W05 scientific fields.'})
assert count==16 and sum(x['in_combined37'] for x in contexts)==3
result={'reviewer':'/root/peptone_final_skeptic','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS_BOUNDED_SELECTOR_ORIGIN_AND19_REFERENCE_ACCOUNTING','selector_sha256':sha((O/'dependency-selection.json').read_bytes()),'ledger_sha256':sha((O/'machine-ledger.json').read_bytes()),'source_core_preserved':sel['preserved_counts'],'frozen_W03_cases_added':0,'baseline_native_incoming':19,'actual_W05_bound':16,'W05_inside_combined37':3,'W03_new_dependencies':3,'current16Gitbindings':contexts,'search_boundary':'Every YAML under native maintained data/ingredients including ignored files via Path.rglob. No assertion about all historical/private files, credentials or unrelated roots. Selected10core GYPS absence separately bound in lineage-review; no invented GYPS source case.','limits':['19=16+3 counts owners once; combined37 membership is not extra dependency.','MRSsi genuine new-owner dependency is outside baseline19; no double-count.','Foreign original proposal objects/cases preserved exactly; all native frozen W03 core bytes/188decisions remain unchanged.','This sidecar is not a native OUTCOME core addition. If native-core ingestion is required, source workers must perform actual adoption/backlinks under existing contract.','No whole-owner, role, export, W05 scientific reapproval or finalcombined37approval.']};p=S/'selector-origin-accounting-v2.json';assert not p.exists();p.write_text(json.dumps(result,indent=2)+'\n');print(sha(p.read_bytes()));print({k:result[k] for k in ['status','baseline_native_incoming','actual_W05_bound','W05_inside_combined37','W03_new_dependencies']})
