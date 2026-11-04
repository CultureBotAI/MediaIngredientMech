from pathlib import Path
import importlib.util,json,hashlib,datetime,sys
ROOT=Path.cwd();OUT=ROOT.parent/'next23-execution-20261103/independent-review/context-probes-v3';TEST=ROOT/'tests/test_owned_name_suppression_refresh.py'
assert not OUT.exists(); OUT.mkdir()
spec=importlib.util.spec_from_file_location('independent_suppression_fixture_v2',TEST);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
results=[]
for mutation in ['control','publication-log-is-plan','publication-log-is-canonical','publication-log-hardlinks-plan','post-capture-log-hardlinks-plan']:
 case=m.build_case(OUT/mutation)
 if mutation=='publication-log-is-plan':
  case['manifest'][m.policy.UPDATE][-1]['publication_log']=m.PLAN;m.repin(case)
 if mutation=='publication-log-is-canonical':
  case['manifest'][m.policy.UPDATE][-1]['publication_log']=m.policy.SSSOM_SOURCE;m.repin(case)
 if mutation in ['publication-log-hardlinks-plan','post-capture-log-hardlinks-plan']:
  log=case['root']/m.PUBLOG
  if mutation=='post-capture-log-hardlinks-plan':
   m.write(case['root'],m.PUBLOG,(case['root']/m.PLAN).read_bytes()); prior=m.verify(case)
  log.unlink();log.hardlink_to(case['root']/m.PLAN)
 try:
  if mutation=='post-capture-log-hardlinks-plan':
   m.policy.recheck_inventory(case['root'],prior); proof=prior
  else: proof=m.verify(case)
  result={'accepted':True,'scientific_approval_added':proof['scientific_approval_added'],'input_count':len(proof['input_sha256'])}
 except ValueError as e:result={'accepted':False,'error':type(e).__name__+': '+str(e)}
 assert result['accepted']==(mutation=='control'), (mutation,result)
 if mutation!='control': assert 'publication log' in result['error']
 results.append({'mutation':mutation,**result})
report={'reviewer':'/root/step7d_independent_review','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Independent re-execution of original context counterexamples plus inode alias/post-capture cases in private native-chain fixtures; no maintained mutations.','source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [ROOT/'src/mediaingredientmech/owned_name_suppression_refresh.py',ROOT/'src/mediaingredientmech/ingredient_bundle_refresh.py',TEST]},'results':results}
(OUT/'results.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
