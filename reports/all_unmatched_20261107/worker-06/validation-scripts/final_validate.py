from pathlib import Path
import json, subprocess, hashlib, datetime, shutil
R=Path('reports/all_unmatched_20261107/worker-06').resolve()
Q=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
C=Q.parent.parent
PY='/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.venv/bin/python'
P=json.loads((R/'proposals.json').read_text())['proposals']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,j):p.write_text(json.dumps(j,indent=2,ensure_ascii=False)+'\n')
logs=R/'logs'
cmd=[PY,str(C/'scripts/audit_worker_outcomes_v1.py'),'--shard',str(Q/'shards/shard-06.json'),'--decisions',str(R/'decisions.json'),'--evidence',str(R/'evidence.json'),'--proposals',str(R/'proposals.json'),'--artifact-root',str(R),'--source-root',str(Q),'--mim-root',str(Path.cwd()),'--output',str(R/'structural-audit-final.json')]
r=subprocess.run(cmd,capture_output=True,text=True);(logs/'structural-audit-final.log').write_text(r.stdout+r.stderr);dump(logs/'structural-audit-command.json',{'command':cmd,'exit_code':r.returncode});assert r.returncode==0,r.stdout+r.stderr
for name in ['proposal-schema-final.tsv','proposal-schema-final.log','proposal-schema-command.json']:
 p=logs/name
 if p.exists():p.rename(logs/('before-final100-'+name))
cmd=[PY,'scripts/validate_strict.py',*[str((R/p['after_capture']['path']).relative_to(Path.cwd())) for p in P],'--out',str(logs/'proposal-schema-final.tsv'),'--workers','1']
r=subprocess.run(cmd,capture_output=True,text=True)
(logs/'proposal-schema-final.log').write_text(f'Ran scripts/validate_strict.py for {len(P)} final payloads; exit {r.returncode}. Exact argv and payload hashes: proposal-schema-command.json.\nProducer stdout/stderr follows (empty means no diagnostic output):\n'+r.stdout+r.stderr)
dump(logs/'proposal-schema-command.json',{'command':cmd,'exit_code':r.returncode,'proposal_count':len(P),'payload_hashes':{p['proposal_id']:p['after_capture']['sha256'] for p in P}});assert r.returncode==0,r.stdout+r.stderr
cmd=[PY,'.temp/all-unmatched-worker-06/final_invariants.py'];r=subprocess.run(cmd,capture_output=True,text=True);(logs/'final-invariants-command.log').write_text(r.stdout+r.stderr);assert r.returncode==0,r.stdout+r.stderr
for f in ['assemble.py','final_invariants.py','final_validate.py','native_review.py']:
 shutil.copyfile(Path('.temp/all-unmatched-worker-06')/f,R/'validation-scripts'/f)
print('Final structural/schema/invariant validators PASS',len(P),'payloads')
