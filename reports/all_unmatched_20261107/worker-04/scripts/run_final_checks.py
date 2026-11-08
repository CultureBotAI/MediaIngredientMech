"""Run final read-only proposal/campaign checks and retain actual return codes."""
import subprocess,json,hashlib,datetime,sys,concurrent.futures
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];ART=ROOT/'reports/all_unmatched_20261107/worker-04';CAMPAIGN=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107');QUEUE=CAMPAIGN/'queue/preliminary-v5';PYTHON=ROOT/'.temp/all-unmatched-worker-04/venv/bin/python';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
bound_paths={ART/'decisions.json',ART/'evidence.json',ART/'proposals.json',ART/'scripts/validate_proposal_overlay.py',ROOT/'scripts/validate_strict.py',CAMPAIGN/'scripts/audit_worker_outcomes_v1.py',ROOT/'src/mediaingredientmech/schema/mediaingredientmech.yaml',ROOT/'src/mediaingredientmech/validation/component_partonomy.py'}
for e in json.loads((ART/'evidence.json').read_text())['evidence']:
    cap=e['capture'];path=(ART if cap['root']=='artifact' else QUEUE)/cap['path'];assert sha(path)==cap['sha256'];bound_paths.add(path)
for p in json.loads((ART/'proposals.json').read_text())['proposals']:
    bound_paths.add(ART/p['after_capture']['path'])
    if p['kind']=='edit_existing_owner':bound_paths.add(ROOT/p['owner_path'])
bindings=[{'path':str(p),'sha256':sha(p)} for p in sorted(bound_paths)]
commands={
'structural':[str(PYTHON),'-B',str(CAMPAIGN/'scripts/audit_worker_outcomes_v1.py'),'--shard',str(QUEUE/'shards/shard-04.json'),'--decisions',str(ART/'decisions.json'),'--evidence',str(ART/'evidence.json'),'--proposals',str(ART/'proposals.json'),'--artifact-root',str(ART),'--source-root',str(QUEUE),'--mim-root',str(ROOT),'--output',str(ART/'structural-audit-v1.json')],
'schema':[str(PYTHON),'-B','scripts/validate_strict.py',str(ART/'proposals'),'--out',str(ART/'validation/proposal-schema-final.tsv')],
'overlay':[str(PYTHON),'-B',str(ART/'scripts/validate_proposal_overlay.py')],
}
logs={'structural':'validation/structural-audit-final.log','schema':'validation/proposal-schema-final.log','overlay':'validation/proposal-overlay-final.log'}
def run(name):
    started=datetime.datetime.now(datetime.timezone.utc).isoformat();p=ART/logs[name]
    with p.open('wb') as out:r=subprocess.run(commands[name],stdout=out,stderr=subprocess.STDOUT,cwd=ROOT)
    return name,{'command':commands[name],'started_at':started,'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':r.returncode,'log':logs[name],'log_sha256':sha(p)}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:receipts=dict(pool.map(run,commands))
ledger=json.loads((ART/'validation/command-ledger.json').read_text())['commands'];prior=next(x for x in ledger if x['log']=='validation/auditor-negative-controls-retry.log');assert prior['exit_code']==0
assert all(sha(Path(b['path']))==b['sha256'] for b in bindings),'Inputs changed during final checks'
(ART/'validation/final-input-bindings.json').write_text(json.dumps({'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':bindings},indent=2)+'\n')
receipts['auditor-controls']={'command':prior['command'],'exit_code':prior['exit_code'],'log':prior['log'],'log_sha256':sha(ART/prior['log']),'execution_note':'Earlier actual run reused; no claim of rerunning controls here.'}
for receipt in receipts.values():receipt['input_bindings_sha256']=sha(ART/'validation/final-input-bindings.json')
(ART/'validation/final-command-receipts.json').write_text(json.dumps(receipts,indent=2)+'\n')
print(json.dumps({k:{'exit_code':v['exit_code'],'log':v['log']} for k,v in receipts.items()},indent=2));sys.exit(any(x['exit_code'] for x in receipts.values()))
