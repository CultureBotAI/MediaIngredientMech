"""Hash explicit source-bound owner/proposal targets with native inspection."""
from pathlib import Path
import json,subprocess,sys,datetime
R=Path.cwd();O=R/'reports/all_unmatched_20261107/worker-05';N=O/'native';N.mkdir(exist_ok=True)
D=[d for n in ['root','media','materials','chemicals'] for d in json.loads((O/n/'decisions.json').read_text())['decisions']]
P=[p for n in ['root','media','materials','chemicals'] for p in json.loads((O/n/'proposals.json').read_text())['proposals']]
owners=sorted({o['path'] for d in D for o in d['owner_records']})
targets=[{'target_id':'OWNER-'+Path(p).stem,'path':p,'label':Path(p).stem,'record_class':'Ingredient','kind':'maintained','selector':'Source-case identity/form/alias boundary only; other claims excluded','owner_paths':[{'repository':'CultureBotAI/MediaIngredientMech','path':p,'role':'maintained individual owner; unchanged frozen baseline'}]} for p in owners]
targets += [{'target_id':p['proposal_id'],'path':(O/p['after_capture']['path']).relative_to(R).as_posix(),'label':p['description'],'record_class':'Ingredient','kind':'source','selector':'Isolated candidate payload; proposed changes only; inherited claims not approved','owner_paths':[{'repository':'CultureBotAI/MediaIngredientMech','path':p['owner_path'],'role':'future guarded-write owner; before SHA256 '+p['before_sha256']}]} for p in P]
(N/'targets.json').write_text(json.dumps({'targets':targets},indent=2)+'\n')
inputs=['MAPPING_SEMANTICS.md','src/mediaingredientmech/schema/mediaingredientmech.yaml','schema/record_review.yaml','conf/record_review.yaml','docs/record-review-profile.md','docs/record-reviews.md']
inputs += [str((O/n/f).relative_to(R)) for n in ['root','media','materials','chemicals'] for f in ['decisions.json','evidence.json','proposals.json']]
inputs += [str((O/f).relative_to(R)) for f in ['decisions.json','evidence.json','proposals.json','subagent-scopes.json','structural-audit-v1.json','validation/proposed-validation.json']]
E=json.loads((O/'evidence.json').read_text())['evidence']
inputs += sorted({str((O/e['capture']['path']).relative_to(R)) for e in E if e['kind']=='independent_review' and e['capture']['root']=='artifact'})
# Registry captures bind exact original source URLs/times/bytes; inputs above bind their manifests.
cmd=[sys.executable,'scripts/record_review.py','inspect','--targets',str(N/'targets.json')]
for p in inputs:cmd+=['--input',p]
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
r=subprocess.run(cmd,capture_output=True,text=True);(N/'inspect.json').write_text(r.stdout);(N/'inspect.stderr').write_text(r.stderr)
(N/'inspection-run.json').write_text(json.dumps({'started_at':started,'completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':cmd,'exit_code':r.returncode},indent=2)+'\n')
print(r.returncode,len(targets),'targets',len(owners),'baseline owners',len(P),'proposals');sys.exit(r.returncode)
