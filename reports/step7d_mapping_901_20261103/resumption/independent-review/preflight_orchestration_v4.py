import pathlib,sys,importlib.util,hashlib,json,ast,datetime,subprocess,yaml,shlex
D=pathlib.Path(__file__).resolve().parents[1];R=D/'independent-review';W=D.parent/'step7d';p=D/'refresh_post1122_v4.py';sha=lambda b:hashlib.sha256(b).hexdigest();assert sha(p.read_bytes())=='76bb1e6a9dd8828a45c3033cfaa8c60651bf3a943c62998597e0562e898e98c7';prior=(D/'refresh_post1122_v3.py').read_text();text=p.read_text();expected=prior.replace("baseline_paths=set(git('ls-tree','-r','--name-only',BASE,'--',*source_roots).decode().splitlines())","baseline_paths={n for n in git('ls-tree','-r','--name-only','-z',BASE,'--',*source_roots).decode().split('\\0')if n}");assert expected==text
sys.path[:0]=[str(W),str(W/'src')];spec=importlib.util.spec_from_file_location('independent_post1122_v4',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
frozen,old_reports,before,replacements=m.preflight();assert len(replacements)==3
wf=yaml.safe_load((W/'.github/workflows/qc-supported-kgx.yaml').read_text());out=[]
for step in wf['jobs']['supported-graph']['steps']:
 for line in step.get('run','').replace('\\\n','').splitlines():
  if '-m mediaingredientmech.export.kgx 'in line:
   args=shlex.split(line);out.append(args[args.index('--output')+1])
assert out==[m.FULL]==['output/mim-kgx-710-full'];assert next(cmd for tag,cmd in m.COMMANDS if tag=='04-semantic-build')[-1]==m.FULL
for n in m.SELECTORS:assert replacements[n]==before[n].replace(m.PRIOR.encode(),m.SUCCESSOR.encode())
assert len(m.COMMANDS)==13
out={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':'/root/step7d_independent_review','head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=W,text=True).strip(),'operator_sha256':sha(p.read_bytes()),'status':'CURRENT_NATIVE_PREFLIGHT_AND_BOUNDED_V4_REVIEW_PASS','frozen_files':len(frozen),'immutable_old_report_files':len(old_reports),'replacement_files':list(replacements),'native_commands':13,'full_bundle_matches_unchanged_workflow':m.FULL,'changes_from_reviewed_v3':['NUL-delimited baseline Git inventory parser; exact-set guard unchanged'],'all_other_v3_bytes_unchanged':True,'findings':[],'maintained_writes':False,'final_head_approval':False,'limitations':['Bounded operator readiness after current native preflight, not successful execution or final-head approval. Full generated evidence, tests and CI must still pass.']}
p=R/'post1122-orchestration-v4-review.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));print('SHA256',sha(p.read_bytes()))
