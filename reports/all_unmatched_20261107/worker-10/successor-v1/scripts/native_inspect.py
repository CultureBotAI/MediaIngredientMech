import subprocess,pathlib,json,datetime
R=pathlib.Path.cwd();S=R/'reports/all_unmatched_20261107/worker-10/successor-v1';N=S/'native'
inputs=['MAPPING_SEMANTICS.md','src/mediaingredientmech/schema/mediaingredientmech.yaml','docs/record-review-profile.md','.claude/skills/add-media/SKILL.md']+[str((S/n).relative_to(R)) for n in ['decisions.json','evidence.json','proposals.json','subagent-scopes.json','accounting.json','reviews/final-review-bindings.json']]
cmd=['.temp/all-unmatched-worker-10/venv/bin/python','scripts/record_review.py','inspect','--targets',str((N/'targets.json').relative_to(R))]
for f in inputs:cmd+=['--input',f]
r=subprocess.run(cmd,capture_output=True,text=True);(N/'inspection.json').write_text(r.stdout);(N/'inspection.stderr').write_text(r.stderr);(N/'inspection-command.json').write_text(json.dumps({'argv':cmd,'exit_code':r.returncode,'inspected_at':datetime.datetime.now(datetime.timezone.utc).isoformat()},indent=2)+'\n');print('inspection',r.returncode,r.stderr);assert r.returncode==0
