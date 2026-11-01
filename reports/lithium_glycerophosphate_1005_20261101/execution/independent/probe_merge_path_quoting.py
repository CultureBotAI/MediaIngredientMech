from pathlib import Path
import json,subprocess,tempfile
with tempfile.TemporaryDirectory(prefix='mim-merge-path-proof-') as d:
 p=Path(d); name='Α-lipoic_Acid.yaml'
 def git(*args):return subprocess.check_output(['git',*args],cwd=p)
 git('init','-q');git('config','user.name','Fixture');git('config','user.email','fixture@example.invalid')
 (p/name).write_text('base\n');git('add','--',name);git('commit','-qm','base');base=git('rev-parse','HEAD').decode().strip()
 (p/name).write_text('reviewed\n');git('commit','-qam','reviewed');head=git('rev-parse','HEAD').decode().strip()
 (p/name).write_text('different\n');git('commit','-qam','different merge payload');merge=git('rev-parse','HEAD').decode().strip()
 legacy=git('diff','--name-only',base,head,'--').decode().splitlines()
 missed=git('diff',head,merge,'--',*legacy)
 exact=[x for x in git('diff','--name-only','-z',base,head,'--').decode().split('\0') if x]
 detected=git('diff',head,merge,'--',*exact)
 assert not missed and detected and exact==[name]
 result={'fixture_only':True,'name':name,'legacy_paths':legacy,'legacy_reports_no_content_difference':not bool(missed),'nul_paths':exact,'nul_detects_content_difference':bool(detected),'historical_production_merge_defect_claimed':False}
 print(json.dumps(result,indent=2))
