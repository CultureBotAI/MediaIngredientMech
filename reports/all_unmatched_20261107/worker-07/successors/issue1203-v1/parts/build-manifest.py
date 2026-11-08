"""2026-11-08: hash append-only successor and exact external/predecessor references.

Final independent inventory receipt is explicitly excluded to avoid self-reference.
No previous manifest or source bytes are changed.
"""
import datetime, hashlib, json
from pathlib import Path
R=Path('reports/all_unmatched_20261107/worker-07');S=R/'successors/issue1203-v1'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
excluded=['MANIFEST.json','review/independent-manifest-integrity-v1.json']
dest=S/'MANIFEST.json';assert not dest.exists()
files={str(p.relative_to(S)):sha(p) for p in sorted(S.rglob('*')) if p.is_file() and str(p.relative_to(S)) not in excluded}
assert not any('__pycache__' in p or p.endswith('.pyc') for p in files)
native=json.loads((S/'native-review-receipt.json').read_text())['files']
refs={}
for item in json.loads((S/'evidence.json').read_text())['evidence']:
    c=item['capture'];key=c['root']+':'+c['path']
    assert key not in refs or refs[key]==c['sha256']
    refs[key]=c['sha256']
obj={'schema_version':1,'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'root':str(S),'predecessor_commit':'be2f4c36d3d4ed79aabe29401c555ae3fd65d7b0','predecessor_manifest':{'path':str(R/'MANIFEST.json'),'sha256':sha(R/'MANIFEST.json')},'files':files,'native_review_files':{x['path']:x['sha256'] for x in native},'evidence_capture_references':refs,'excluded':excluded,'current_ledgers':{n:sha(S/n) for n in ['decisions.json','evidence.json','proposals.json']},'limits':'Hash integrity only; scientific scopes and remaining holds are in independent receipts and HANDOFF. Published predecessors are immutable.'}
dest.write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps({'manifest_sha256':sha(dest),'successor_files':len(files),'native_files':len(native),'unique_evidence_capture_references':len(refs)}))
