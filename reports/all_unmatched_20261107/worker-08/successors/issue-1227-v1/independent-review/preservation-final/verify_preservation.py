from pathlib import Path
import hashlib,json,datetime,subprocess,os,stat
from concurrent.futures import ThreadPoolExecutor
R=Path('reports/all_unmatched_20261107/worker-08');S=R/'successors/issue-1227-v1';O=S/'independent-review/preservation-final';start=datetime.datetime.now(datetime.timezone.utc).isoformat()
def h(p):
 digest=hashlib.sha256()
 with Path(p).open('rb') as f:
  for block in iter(lambda:f.read(1024*1024),b''):digest.update(block)
 return digest.hexdigest()
def data(p):return json.loads(Path(p).read_text())
def canon(a):return hashlib.sha256(json.dumps(a,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def save(n,x):
 p=O/n;assert not p.exists();p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
checks=[];groups={};inventories={}
def check(group,path,expected,kind='file_bytes',basis=None):
 p=Path(path);r={'group':group,'path':str(p),'expected_sha256':expected,'kind':kind}
 if basis:r['basis']=basis
 try:
  actual=hashlib.sha256(os.readlink(p).encode()).hexdigest() if kind=='symlink_target_bytes' else h(p)
  r['actual_sha256']=actual;r['passed']=actual==expected
 except Exception as e:r['passed']=False;r['error']=type(e).__name__+': '+str(e)
 return r
def batch(group,rows,basis=None):
 jobs=[(group,Path(p),sha,'file_bytes',basis) for p,sha in rows]
 with ThreadPoolExecutor(max_workers=8) as pool:results=list(pool.map(lambda args:check(*args),jobs))
 checks.extend(results);groups[group]={'checks':len(results),'passed':sum(r['passed'] for r in results),'failed':sum(not r['passed'] for r in results)}
 print(group,groups[group],flush=True)
pre_path=S/'provenance/predecessor-working-bytes.json';pre=data(pre_path)
batch('initial_hashed_working_files',[(r['path'],r['sha256']) for r in pre['files']],str(pre_path))
# The initial receipt omitted ten entries. Compare these independently with exact git blob bytes.
known={r['path'] for r in pre['files']};extra=[]
for raw in subprocess.check_output(['git','ls-tree','-rz',pre['head']]).split(b'\0'):
 if not raw:continue
 meta,name=raw.decode().split('\t',1);mode,typ,oid=meta.split()
 if name not in known:
  blob=subprocess.check_output(['git','cat-file','blob',oid]);sha=hashlib.sha256(blob).hexdigest();r=check('supplemental_ten_baseline_entries',name,sha,'symlink_target_bytes' if mode=='120000' else 'file_bytes',pre['head']+':'+name);r.update(git_mode=mode,git_blob=oid);extra.append(r)
checks+=extra;groups['supplemental_ten_baseline_entries']={'checks':len(extra),'passed':sum(r['passed'] for r in extra),'failed':sum(not r['passed'] for r in extra),'qualification':'Nine non-ASCII paths and one directory symlink were absent from the original15,633-row working-byte inventory. Compared against exact predecessor commit blobs here; not represented as originally captured working hashes.'}
W=Path(pre['w05_sealed_review']['root']);seal_path=W/'SEAL.json';man_path=W/'MANIFEST.sha256';seal=data(seal_path)
batch('w05_seal_manifest_handoff',[(seal_path,pre['w05_sealed_review']['seal_sha256']),(man_path,pre['w05_sealed_review']['manifest_sha256']),(W/'HANDOFF.md',pre['w05_sealed_review']['handoff_sha256'])],str(pre_path))
wrows=[]
for line in man_path.read_text().splitlines():
 sha,name=line.split('  ',1);assert len(sha)==64;wrows.append((W/name,sha))
batch('w05_all_manifest_members',wrows,str(man_path))
expected={str(p.relative_to(W)) for p,s in wrows};actual={str(p.relative_to(W)) for p in W.rglob('*') if p.is_file() and p.name not in [] and str(p.relative_to(W)) not in ['MANIFEST.sha256','SEAL.json']};inventories['w05']={'root':str(W),'method':'Path.rglob, including hidden and gitignored files; no gitignore filtering. Exact original regular-file scope, excluding only top-level SEAL.json and MANIFEST.sha256.','expected_members':len(expected),'actual_members':len(actual),'missing':sorted(expected-actual),'unmanifested':sorted(actual-expected),'declared_manifest_members':seal['manifest_members']}
assert seal['manifest_sha256']==pre['w05_sealed_review']['manifest_sha256']
# IF authoritative sealed review and transitive content bindings.
IF=S/'independent-review/inorganic_forms';completion=data(IF/'completion.json');review=data(IF/'review.json');sl=data(IF/'source-read-ledger.json')
rows=[(IF/'completion.json','b60524adc31603179d0be00c4ebc8d2c90604420b191bd80b1803d040fb47e33')]+[(IF/n,sha) for n,sha in completion['files'].items()]+[(R/x['path'],x['sha256']) for x in review['supporting_receipts'].values()]+[(R/sl[n]['path'],sl[n]['sha256']) for n in ['read_log','beforeimage_comparison']]
batch('if_sealed_review_bindings',rows,'Published peer handoff hashes and completion/review/source ledger')
batch('if_review_final_input_bindings',[(R/p,sha) for p,sha in review['input_hashes'].items()],'Sealed independent review input_hashes; no scientific reassessment')
batch('if_primary_capture_bindings',[(R/r['path'],r['sha256']) for r in sl['captures']]+[(r['path'],r['sha256']) for r in sl['retained_primary_pages']],'Sealed source-read ledger; hash verification only')
D=data(S/'research/inorganic_forms/decisions.json');P=data(S/'research/inorganic_forms/proposals.json');badcases=[d['case_id'] for d in D if canon(d)!=review['case_hashes'].get(d['case_id'])];groups['if_canonical_cases']={'checks':len(D),'passed':len(D)-len(badcases),'failed':len(badcases),'bad_case_ids':badcases,'algorithm':"SHA256(canonical JSON, sort_keys=True, separators=(',',':'), ensure_ascii=False)"}
batch('if_selected_payload_bindings',[(R/p['after_capture']['path'],review['payload_hashes'][p['proposal_id']]) for p in P],'Sealed review proposal payload hashes')
bound_if={str(Path(p).relative_to(IF)) for p,sha in rows if Path(p).is_relative_to(IF)}
inventories['if']={'root':str(IF),'files':[{'path':str(p.relative_to(IF)),'sha256':h(p),'status':'verified_sealed_binding' if str(p.relative_to(IF)) in bound_if else 'current_inventory_only_no_prior_seal_hash'} for p in IF.rglob('*') if p.is_file()],'method':'Path.rglob includes hidden/ignored. Helper scripts and initial progress files without a prior seal hash are inventoried now; no historical preservation claim for those unbound files.'}
# VM v1 and v2 manifests and exact indices/selected payloads/evidence captures.
M=S/'research/vitamins_mixtures';V=M/'final-v1';T=M/'final-v2';v1man=M/'FINAL-v1-MANIFEST.json';v2man=T/'MANIFEST.json';v2add=T/'MANIFEST-ADDENDUM.json'
batch('vm_v1_manifest_members',[(M/r['path'],r['sha256']) for r in data(v1man)['files']],str(v1man))
batch('vm_v1_preservation_snapshot',[(p,sha) for p,sha in data(T/'v1-preservation-before.json').items()],'Frozen final-v2 start snapshot of all final-v1 bytes')
batch('vm_v2_manifest_members',[(T/p,sha) for p,sha in data(v2man)['files'].items()],str(v2man))
add=data(v2add);batch('vm_v2_manifest_addendum',[(v2man,add['original_manifest_sha256'])]+[(T/p,sha) for p,sha in add['additional_files'].items()],str(v2add))
batch('vm_announced_frozen_bindings',[(V/'HANDOFF.json','5d574b8567fc4675914f2dd9c373df931bfd4a4b2d1efc03d85fc60e59efdea8'),(T/'HANDOFF.json','8bea77607dfc38b98e1860f911098c17bbe1433ef35a1d306990bb73108286e4'),(T/'decisions.json','11c5a830c136e9bf6271ef190b4d18e2258713f22faf5632cf5a97f5a96e639c'),(T/'proposals.json','5d19fe5dd367411d00b8d08b304edc34ce77833d4c807dcdae0c512329b769df'),(T/'evidence-additions.json','8e609443ba14cb278642128212338fb5d4a421fffb65f7d9b4b1ba6eefcb0835'),(T/'validation-scope-addendum.json','6d151726fb37508db745f981e1ea6a545227765589ae3edbda9e00eedd8d85a8')],'Exact author handoff messages before this read-only task')
for version,folder in [('v1',V),('v2',T)]:
 pp=data(folder/'proposals.json');ee=data(folder/'evidence-additions.json')['evidence'];hh=data(folder/'HANDOFF.json')
 batch('vm_'+version+'_selected_payloads',[(R/p['after_capture']['path'],p['after_capture']['sha256']) for p in pp],str(folder/'proposals.json'))
 batch('vm_'+version+'_evidence_captures',[(R/e['capture']['path'],e['capture']['sha256']) for e in ee],str(folder/'evidence-additions.json'))
 if version=='v1':
  batch('vm_v1_handoff_inputs',[(R/c['path'],c['sha256']) for c in hh['inputs'].values()],str(folder/'HANDOFF.json'))
 else:batch('vm_v2_handoff_inputs',[(R/p,sha) for p,sha in hh['input_hashes'].items()],str(folder/'HANDOFF.json'))
 expected_set={str(Path(r['path']).relative_to('final-v1')) for r in data(v1man)['files']} if version=='v1' else set(data(v2man)['files'])|set(add['additional_files'])|{'MANIFEST.json','MANIFEST-ADDENDUM.json'}
 actual_set={str(p.relative_to(folder)) for p in folder.rglob('*') if p.is_file()};inventories['vm_'+version]={'root':str(folder),'expected_files':len(expected_set),'actual_files':len(actual_set),'missing':sorted(expected_set-actual_set),'unmanifested':sorted(actual_set-expected_set),'method':'Path.rglob including hidden and ignored files.'}
old={p['proposal_id']:p for p in data(V/'proposals.json')};new=data(T/'proposals.json');changed=[p['proposal_id'] for p in new if p['after_capture']['sha256']!=old[p['proposal_id']]['after_capture']['sha256']];groups['vm_successor_scope']={'cases_v1':len(data(V/'decisions.json')),'cases_v2':len(data(T/'decisions.json')),'proposals_v1':len(old),'proposals_v2':len(new),'changed_payloads':changed,'unchanged_payloads':len(new)-len(changed),'expected_changed_payloads':['vm-prop-new-29','vm-prop-new-98'],'passed':set(changed)=={'vm-prop-new-29','vm-prop-new-98'},'scientific_approval':False}
# All failing checks remain explicit; no exceptions hidden by aggregate counts.
failures=[r for r in checks if not r['passed']];inventory_errors={k:v for k,v in inventories.items() if v.get('missing') or v.get('unmanifested')};finished=datetime.datetime.now(datetime.timezone.utc).isoformat()
save('checks.json',{'started_at':start,'finished_at':finished,'checks':checks,'canonical_case_check':groups['if_canonical_cases']})
save('inventories.json',inventories)
receipt={'reviewer':'/root/vitamins','mode':'read_only_artifact_integrity','scientific_review':False,'self_scientific_approval':False,'started_at':start,'finished_at':finished,'status':'PASS' if not failures and not inventory_errors and not badcases and groups['vm_successor_scope']['passed'] else 'FAIL','predecessor_input':{'path':str(pre_path.relative_to(R)),'sha256':h(pre_path),'declared_tracked_count':pre['tracked_count'],'declared_readable_count':pre['readable_count'],'hashed_rows':len(pre['files'])},'groups':groups,'failure_count':len(failures),'failures':failures,'inventory_failures':inventory_errors,'receipt_files':{n:{'path':str((O/n).relative_to(R)),'sha256':h(O/n)} for n in ['checks.json','inventories.json']},'limitations':['This verifies bytes and frozen bindings only. No primary content was scientifically rereviewed and no native/schema/partonomy validator was rerun.','The original predecessor working-byte capture has15,633 hashed files, not15,643; ten additional git-tree entries were checked separately against b90a2fd commit blobs.','IF authoritative review/receipt/ledger files are checked against known sealed hashes. Unbound helper/progress files are inventoried, not claimed historically immutable.','Root unsealed assembly, selection and review files are excluded from immutability assertions. The VM validation-scope addendum remains effective: author diagnostic overlay used earlier organic proposals; the final root combined-overlay gate is separate.','VM files include reviewer-owned author material. These checks provide mechanical integrity only and cannot approve their scientific content.'],'commands':['Python3.13 hashlib streamed SHA256 over all manifest files','git ls-tree -rz b90a2fd4681d20e2586481b7b9b1114a78281b94','git cat-file blob for ten supplemental entries','Path.rglob for ignored-inclusive sealed-directory inventory'],'checked_write_boundary':str(O)}
save('receipt.json',receipt)
(O/'HANDOFF.md').write_text('Artifact-integrity verification: '+receipt['status']+'. Verified every15,633 initial hashed working file plus ten supplemental exact predecessor git-tree entries; all6,968 W05 manifest members and its seal/manifest/handoff bindings; sealed IF review, source/input/payload bindings; and VM final-v1/final-v2 manifests and exact payload/evidence bindings. Ignored and hidden files were included in sealed-directory inventories. No scientific or native validation approval is implied.\n\nReceipt SHA256: '+h(O/'receipt.json')+'\n')
print(json.dumps({'status':receipt['status'],'hash_checks':len(checks),'failures':len(failures),'inventory_failures':list(inventory_errors),'receipt_sha256':h(O/'receipt.json')}),flush=True)
