"""Run source-only successor gates and bind actual results to exact input bytes."""
import concurrent.futures,datetime,hashlib,json,subprocess,sys,shutil
from pathlib import Path
S=Path(__file__).resolve().parents[1];W=Path(__file__).resolve().parents[3];R=Path(__file__).resolve().parents[6]
C=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107');Q=C/'queue/preliminary-v5';PY=R/'.temp/all-unmatched-worker-04/venv/bin/python';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def run():
 bound={S/x for x in ['decisions.json','evidence.json','proposals.json','reassessments.json']};bound.update((S/'scripts').glob('*.py'));bound.update([R/'src/mediaingredientmech/schema/mediaingredientmech.yaml',R/'schema/record_review.yaml',R/'MAPPING_SEMANTICS.md',R/'.claude/skills/add-media/SKILL.md',R/'src/mediaingredientmech/validation/write_validated.py',R/'src/mediaingredientmech/validation/component_partonomy.py',C/'scripts/audit_worker_outcomes_v1.py',R/'scripts/validate_strict.py'])
 bound.update((S/'fragments').glob('*.json'))
 bound.update(S/x for x in ['validation/assembly-bindings.json','independent-review/review-selection.json','cross-shard-dependencies.json','provenance/published-predecessor-files.json'])
 for e in json.loads((S/'evidence.json').read_text())['evidence']:
  cap=e['capture'];p=(W if cap['root']=='artifact' else Q)/cap['path'];assert sha(p)==cap['sha256'],p;bound.add(p)
 for p in json.loads((S/'proposals.json').read_text())['proposals']:
  bound.add(W/p['after_capture']['path'])
  if p['kind']=='edit_existing_owner':bound.add(R/p['owner_path'])
 schema_dir=R/'.temp/all-unmatched-worker-04/issue-1201-v1'/('active-schema-'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'));schema_dir.mkdir(parents=True)
 schema_inputs=[]
 for p in json.loads((S/'proposals.json').read_text())['proposals']:
  original=W/p['after_capture']['path'];target=schema_dir/(hashlib.sha256(p['proposal_id'].encode()).hexdigest()+'.yaml');shutil.copyfile(original,target);assert sha(target)==p['after_capture']['sha256'];schema_inputs.append({'proposal_id':p['proposal_id'],'original':str(original),'copy':str(target),'sha256':sha(target)})
  bound.add(target)
 (S/'validation/schema-inputs.json').write_text(json.dumps(schema_inputs,indent=2)+'\n');bound.add(S/'validation/schema-inputs.json')
 binding=[{'path':str(p),'sha256':sha(p)} for p in sorted(bound)]
 audit_version=1
 while (S/f'structural-audit-v{audit_version}.json').exists():audit_version+=1
 audit_path=S/f'structural-audit-v{audit_version}.json'
 commands={
  'predecessor':[str(PY),'-B',str(S/'scripts/check_predecessor.py')],
  'structural':[str(PY),'-B',str(C/'scripts/audit_worker_outcomes_v1.py'),'--shard',str(Q/'shards/shard-04.json'),'--decisions',str(S/'decisions.json'),'--evidence',str(S/'evidence.json'),'--proposals',str(S/'proposals.json'),'--artifact-root',str(W),'--source-root',str(Q),'--mim-root',str(R),'--output',str(audit_path)],
  'schema':[str(PY),'-B','scripts/validate_strict.py',str(schema_dir),'--out',str(S/'validation/proposal-schema.tsv')],
  'overlay':[str(PY),'-B',str(S/'scripts/validate_overlay.py')],
  'guarded_writer':[str(PY),'-B',str(S/'scripts/guarded_replay.py')],
  'auditor_controls':[str(PY),'-B','-m','pytest','-c','/dev/null','--rootdir','.',str(C/'scripts/test_audit_worker_outcomes_v1.py'),'-q','--basetemp',str(R/'.temp/all-unmatched-worker-04/issue-1201-v1/auditor-tests')]
 }
 def one(name):
  start=datetime.datetime.now(datetime.timezone.utc).isoformat();log=S/'validation'/f'{name}.log'
  with log.open('wb') as out:r=subprocess.run(commands[name],cwd=R,stdout=out,stderr=subprocess.STDOUT)
  return name,{'command':commands[name],'exit_code':r.returncode,'started_at':start,'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'log':str(log.relative_to(S)),'log_sha256':sha(log)}
 with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:receipts=dict(pool.map(one,commands))
 assert all(sha(Path(x['path']))==x['sha256'] for x in binding),'Bound input mutated during checks'
 outputs=[audit_path]+[S/x for x in ['validation/proposal-schema.tsv','validation/proposal-overlay.json','validation/guarded-writer-replay.json']]
 if audit_path.is_file():receipts['structural'].update(result_path=str(audit_path.relative_to(S)),result_sha256=sha(audit_path))
 bp=S/'validation/input-bindings.json';bp.write_text(json.dumps({'files':binding,'gate_outputs':[{'path':str(p),'sha256':sha(p)} for p in outputs if p.is_file()],'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat()},indent=2)+'\n')
 for row in receipts.values():row['input_binding_sha256']=sha(bp)
 (S/'validation/command-receipts.json').write_text(json.dumps(receipts,indent=2)+'\n');print(json.dumps({k:v['exit_code'] for k,v in receipts.items()},indent=2));return any(v['exit_code'] for v in receipts.values())
if __name__=='__main__':sys.exit(run())
