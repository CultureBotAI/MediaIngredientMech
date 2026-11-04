from pathlib import Path
import importlib.util,json,hashlib,datetime
ROOT=Path.cwd();OUT=ROOT.parent/'next23-execution-20261103/independent-review/context-probes-v1';TEST=ROOT/'tests/test_owned_name_suppression_refresh.py'
spec=importlib.util.spec_from_file_location('independent_suppression_fixture',TEST);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
results=[]
for mutation in ['control','publication-log-is-plan','publication-log-is-canonical','selected-evidence-replaced']:
 case=m.build_case(OUT/mutation)
 if mutation=='publication-log-is-plan':
  case['manifest'][m.policy.UPDATE][-1]['publication_log']=m.PLAN;m.repin(case)
 if mutation=='publication-log-is-canonical':
  case['manifest'][m.policy.UPDATE][-1]['publication_log']=m.policy.SSSOM_SOURCE;m.repin(case)
 if mutation=='selected-evidence-replaced':
  base=m.read_json(case['current'][m.BASE_REVIEW]);base['decisions'][0]['review_reason']='A new, unsupported explanation substituted after suppression'
  case['current'][m.BASE_REVIEW]=m.encoded(base);m.write(case['root'],m.BASE_REVIEW,case['current'][m.BASE_REVIEW])
  doc=m.read_json(case['current'][m.EVIDENCE]);doc['entries']['1']={'disposition':'WITHHOLD','basis':'unrelated invented replacement evidence'};case['current'][m.EVIDENCE]=m.encoded(doc);m.write(case['root'],m.EVIDENCE,case['current'][m.EVIDENCE])
 try:
  proof=m.verify(case);result={'accepted':True,'scientific_approval_added':proof['scientific_approval_added'],'input_count':len(proof['input_sha256'])}
 except Exception as e:result={'accepted':False,'error':type(e).__name__+': '+str(e)}
 results.append({'mutation':mutation,**result})
report={'reviewer':'/root/step7d_independent_review/projection_adversarial','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Private fixtures using author native-chain fixture; no maintained state changes. These API probes are not production findings until assessed against boundary contract.','source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [ROOT/'src/mediaingredientmech/owned_name_suppression_refresh.py',ROOT/'src/mediaingredientmech/ingredient_bundle_refresh.py',TEST]},'results':results}
(OUT/'results.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
