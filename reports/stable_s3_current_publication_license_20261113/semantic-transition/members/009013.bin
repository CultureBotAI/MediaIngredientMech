from pathlib import Path
import datetime,hashlib,json,subprocess,sys,yaml
O=Path(__file__).resolve().parent;C=O.parents[1];R=C.parents[1];h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
d=yaml.safe_load((O/'review-v2.yaml').read_text());controls=json.loads((O/'reproduced-author-controls-final.json').read_text());assert controls['total']==33 and controls['focused']['status']==controls['drift']['status']=='PASS'
for x in d['source']['inputs']:assert h(R/x['path'])==x['sha256']
paths={x['path'] for x in d['source']['inputs']}|{str((O/n).relative_to(R)) for n in ['reproduce_controls_final.py','reproduced-author-controls-final.json','reproduce-controls-final.log']}
cmd=[sys.executable,'-B',str(R/'scripts/record_review.py'),'--repo-root',str(R),'inspect','--targets',str(O/'native-targets.yaml')]
for p in sorted(paths):cmd+=['--input',p]
r=subprocess.run(cmd,capture_output=True,text=True,cwd=R)
for n,s in [('native-inspect-v3.stdout',r.stdout),('native-inspect-v3.stderr',r.stderr)]:
 with (O/n).open('x') as f:f.write(s)
assert r.returncode==0,r.stderr;ins=json.loads(r.stdout);d['source']=ins['source'];d['targets']=ins['targets']
t=datetime.datetime.now(datetime.UTC);d['finished_at']=t.isoformat().replace('+00:00','Z');d['review_id']=t.strftime('%Y%m%dT%H%M%SZ')+'-w03-peptone-published-head-independent'
for e in d['evidence']:
 if e['evidence_id']=='controls':
  p=O/'reproduced-author-controls-final.json';e.update(reference=str(p),locator=str(p.relative_to(R)),snapshot_sha256=h(p),accessed_at=d['finished_at'])
for c in d['checks']:
 if c['check_id']=='native-33':c['command']=str(R/'.temp/kgm-unmapped-20261107/env/bin/python')+' -B '+str(O/'reproduce_controls_final.py');c['exit_code']=0
d['limitations'].append('A second native-review draft refused the combined runner check because no actual whole-command exit code was supplied. The exact33 controls were rerun alone in a fresh private fixture; that complete command exited0. This final document binds its new actual receipt and preserves both invalid review drafts.')
class NoAlias(yaml.SafeDumper):
 def ignore_aliases(self,data):return True
with (O/'review-v3.yaml').open('x') as f:yaml.dump(d,f,Dumper=NoAlias,sort_keys=False,allow_unicode=True,width=100)
with (O/'native-inspection-v3.json').open('x') as f:json.dump(ins,f,indent=2);f.write('\n')
with (O/'native-inspect-v3-receipt.json').open('x') as f:json.dump({'argv':cmd,'exit_code':r.returncode,'stdout_sha256':hashlib.sha256(r.stdout.encode()).hexdigest()},f,indent=2);f.write('\n')
print(d['review_id'],len(d['targets']),'targets',len(d['source']['inputs']),'inputs')
