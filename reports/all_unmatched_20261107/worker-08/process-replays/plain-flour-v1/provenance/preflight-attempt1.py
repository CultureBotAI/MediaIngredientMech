import datetime,hashlib,json,shutil,subprocess
from pathlib import Path
R=Path.cwd();P=R/'.temp/all-unmatched-worker-08/plain-flour-process-replay-v1';A=R/'reports/all_unmatched_20261107/worker-08';O=A/'process-replays/plain-flour-v1';W09=R.parents[2]/'w09/worktree/.temp/w08-plain-flour-final-independent-v1'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def save(p,x):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x') as f:json.dump(x,f,indent=2);f.write('\n')
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()=='4a4042561328f2a507770d3c85100a7790855aaa'
assert sha(W09/'HANDOFF.json')=='18b584da35922845905ea7a1f1076b28ead45bb45f5a43acd26c31954ba17f93'
assert sha(W09/'MANIFEST.json')=='cd6e9558844a53a5201aa9071dfac1a27750400db900829ad2cb3bbd103c7976'
manifest=read(W09/'MANIFEST.json');members={r['path']:r for r in manifest['files']}
O.mkdir(parents=True,exist_ok=False);shutil.copytree(P/'inputs',O/'inputs');(O/'inputs/w09').mkdir()
names=['HANDOFF.json','HANDOFF.md','REPORT.md','machine-findings.json','actual-reviewer-scopes.json','bridge/workflow-and-independence-review.json','skeptic/process-referral.json','native/review.yaml','native/review.md','MANIFEST.json']
refs=[]
for name in names:
 src=W09/name;digest=sha(src)
 if name!='MANIFEST.json':assert members[name]['sha256']==digest,name
 dst=O/'inputs/w09'/name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst);refs.append({'original_path':str(src),'public_path':str(dst.relative_to(R)),'sha256':digest})
old=A/'successors/issue-1227-plain-flour-v1';prior=A/'successors/issue-1227-v1/research/organic_products/proposed_owners/Plain_Flour.yaml'
assert sha(old/'provenance/author.py')=='1790bb6525e047fde7158a4f84ab9a623de43ba8b4a85aa96fc09b5244d8b0c0'
assert sha(prior)=='aa8390f17f1ed9f9c083fd6b487ee1c40228e754072b7e390b97dfb2fd6eae83'
assert sha(old/'payloads/Plain_Flour.yaml')=='884fee1ea6a5082a51b8769f2a827199b1703972ad80fa48e1bb8d2d09ab3873'
for label,src in [('original-author.py',old/'provenance/author.py'),('predecessor.yaml',prior),('selected-payload.yaml',old/'payloads/Plain_Flour.yaml'),('original-label-resolution.json',old/'research/primary-label-resolution.json')]:
 dst=O/'inputs'/label;shutil.copy2(src,dst);refs.append({'original_path':str(src.relative_to(R)),'public_path':str(dst.relative_to(R)),'sha256':sha(src)})
selector=A/'successors/issue-1237-tenvit-v1/selection.json';s=read(selector)
assert sha(selector)=='fb16bf5c29b981dc7dd60cf8d963a9aea25c12a65d6a0e55e29d84dfb2a26699'
for cap in s['authoritative_inputs'].values():assert sha(A/cap['path'])==cap['sha256']
props=read(A/s['authoritative_inputs']['proposals.json']['path'])['proposals'];assert len(props)==114
for p in props:assert sha(A/p['after_capture']['path'])==p['after_capture']['sha256']
save(O/'inputs/input-bindings.json',{'captured_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':refs,'W09_manifest_scope':'Pinned complete manifest and verified copied relevant members only; no claim of rerunning W09 full scientific or895-input review.','original_script_deviation':'Native guarded writer called, history event directly appended. Truthful and schema-valid; workflow-only follow-up.','current_source_selector':{'path':str(selector.relative_to(R)),'sha256':sha(selector)},'current_source_counts':s['counts'],'all114_current_payload_hashes_verified':True,'scope':'No selector/case/proposal update authorized or necessary; replay provenance only.'})
save(P/'acceptance.json',{'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'head':'4a4042561328f2a507770d3c85100a7790855aaa','branch':'review/all-unmatched-w08-source-review-20261107','finding':'W08-PF-PROCESS-001','filed_comment_sha256':sha(P/'inputs/issue1227-comment6719637789.json'),'public_evidence_root':str(O.relative_to(R)),'source_case_additions':0,'selected_payload_changes':0})
(O/'provenance').mkdir();shutil.copy2(P/'preflight.py',O/'provenance/preflight.py')
print(json.dumps({'status':'PASS','captured_inputs':len(refs),'current_selector':sha(selector),'new_source_cases':0,'payload_changes':0},indent=2))
