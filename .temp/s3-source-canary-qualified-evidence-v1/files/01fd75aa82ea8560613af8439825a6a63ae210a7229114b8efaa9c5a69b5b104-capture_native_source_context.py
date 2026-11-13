"""2026-11-12: genuine independent native four-source review input capture.

Read exact source inspection and all mandatory/current/evidence inputs, then run
record_review.main(inspect) once in-process to avoid macOS argv-size limits.
No source-bindings export, generation, application, shared check or assessment.
"""
from pathlib import Path
from datetime import datetime, timezone
import contextlib, hashlib, io, json, os, sys, types

HERE=Path(__file__).absolute().parent
TC=HERE.parents[1]
C=TC.parents[1]
PY=C/'integration/stable-campaign-adoption-worktree/.venv/bin/python3'
B=TC/'.temp/real-canary-source-binding-request-v1'
assert Path.cwd()==TC and sys.executable==str(PY)
assert {p.name for p in HERE.iterdir()}=={'capture_native_source_context.py'}
def sha(raw):return hashlib.sha256(raw).hexdigest()
def now():return datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
def put(name,value):
    with (HERE/name).open('x') as f:json.dump(value,f,indent=2,ensure_ascii=False);f.write('\n')
pins={'TARGETS.json':'ad146736026fa40c98d3f7fd5d6a9a0b9c485adf6297a674c11287137fb13d62',
'PAYLOADS.json':'0556b24df914dd84b4ed47164cca44e18c0b4cf9c9177c1e85ca3d987a1c79b8',
'INSPECTION.json':'dc7c987cb4d632caa4157f08d4b1d5afa49898c8130ac1eeab7a85eb73b2aa29',
'REVIEW-INPUTS.json':'261ec0b51124ae6c5696b8596625f903974d43fd6854d568e8ea18fa8b9852b4',
'REQUEST.json':'b6c76f85aea1ab4bd6585b202fb2d69dc3016c7561272fa0ed252c85892938f8'}
for n,h in pins.items():assert sha((B/n).read_bytes())==h,n
request=json.loads((B/'REQUEST.json').read_bytes())
inspection=json.loads((B/'INSPECTION.json').read_bytes())
assert inspection['status']=='inspection_only' and len(inspection['targets'])==4
assert inspection['targets']==json.loads((B/'TARGETS.json').read_bytes())['targets']
assert request['external_review'] is None
expected={**inspection['inputs'],**request['inputs']}
for n,h in expected.items():assert sha((TC/n).read_bytes())==h,n
names=set(expected)|{
str((B/n).relative_to(TC)) for n in pins}
names.update(['AGENTS.md','MAPPING_SEMANTICS.md','conf/record_review.yaml','schema/record_review.yaml',
'scripts/record_review.py','.claude/skills/review-ingredients/SKILL.md',
'docs/record-reviews.md','docs/record-review-profile.md','docs/SOURCE_IDENTITY_CANDIDATES.md',
'src/mediaingredientmech/export/source_bindings.py','src/mediaingredientmech/stable_ids.py',
'.temp/stable-adoption1303-real-canary-applied-v1/application.json',str(Path(__file__).relative_to(TC))])
argv=['--repo-root',str(TC),'inspect','--targets',str(B/'TARGETS.json')]
for n in sorted(names):argv.extend(['--input',n])
script=TC/'scripts/record_review.py';raw=script.read_bytes()
native=types.ModuleType('_independent_native_source_review_capture')
native.__file__=str(script);sys.modules[native.__name__]=native
exec(compile(raw,str(script),'exec'),native.__dict__)
stdout,stderr=io.StringIO(),io.StringIO();start=now()
put('START.json',{'started_at':start,'pid':os.getpid(),'cwd':str(TC),'executable':sys.executable,
'native_main_argv':argv,'native_script_sha256':sha(raw),'mode':'Native main inspect, in-process argv; no scientific vote'})
with contextlib.redirect_stdout(stdout),contextlib.redirect_stderr(stderr):
    code=native.main(argv)
for n,v in [('inspection.json',stdout.getvalue()),('inspection.stderr.txt',stderr.getvalue())]:
    with (HERE/n).open('x') as f:f.write(v)
put('inspect-COMMAND.json',{'started_at':start,'finished_at':now(),'exit_code':code,
'native_main_argv':argv,'executable':sys.executable,'cwd':str(TC),
'native_script_sha256':sha(raw),'stdout_sha256':sha(stdout.getvalue().encode()),
'stderr_sha256':sha(stderr.getvalue().encode()),'env_overlay':{k:os.environ.get(k) for k in ['PYTHONPATH','PYTHONDONTWRITEBYTECODE','GIT_OPTIONAL_LOCKS']}})
assert code==0,'Native inspect failed; exact outputs preserved'
result=json.loads(stdout.getvalue());assert result['status']=='inspection_only'
for n,h in expected.items():assert sha((TC/n).read_bytes())==h,n
print(json.dumps({'exit_code':code,'targets':len(result['targets']),'inputs':len(result['source']['inputs']),
'inspection_sha256':sha(stdout.getvalue().encode()),'receipt':str(HERE/'inspect-COMMAND.json')}))
