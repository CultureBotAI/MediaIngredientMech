from pathlib import Path
import json,subprocess,datetime
R=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech');C=R/'.temp/all-unmatched-20261107';O=Path(__file__).parent;cfg=json.loads((C/'integration/final-application-accounting-v1/observer-config-v4.json').read_text());ws=[w for w in cfg['workers']if w['worker_slot']in [1,2,3,4,5,6]];rows=[]
for w in ws:
 branch=subprocess.check_output(['git','-C',w['worktree'],'branch','--show-current'],text=True).strip();head=subprocess.check_output(['git','-C',w['worktree'],'rev-parse','HEAD'],text=True).strip();rows.append({'slot':w['worker_slot'],'branch':branch,'local_head':head,'selected_head':w['head'],'worktree':w['worktree']})
cmd=['git','-C',ws[0]['worktree'],'ls-remote','--heads','origin']+['refs/heads/'+r['branch']for r in rows];p=subprocess.run(cmd,capture_output=True,text=True,timeout=45);(O/'live-source-heads-v2.stdout').write_text(p.stdout);(O/'live-source-heads-v2.stderr').write_text(p.stderr)
rem={line.split()[1]:line.split()[0]for line in p.stdout.splitlines()if len(line.split())==2}
for r in rows:r['remote_head']=rem.get('refs/heads/'+r['branch']);r['selected_still_current']=p.returncode==0 and r['remote_head']==r['local_head']==r['selected_head']
(O/'live-source-heads-v2.json').write_text(json.dumps({'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':cmd,'exit_code':p.returncode,'rows':rows,'read_only':True},indent=2)+'\n');print(json.dumps(rows,indent=2));raise SystemExit(p.returncode)
