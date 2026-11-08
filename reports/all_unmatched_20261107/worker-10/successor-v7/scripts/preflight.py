from pathlib import Path
import datetime, hashlib, json, subprocess

R=Path.cwd(); C=R.parents[2]; O=R/'.temp/columbia-controls-successor-v1'
A=R/'reports/all_unmatched_20261107/worker-10'; S=A/'successor-v7'
P=C/'workers/w07/worktree/.temp/columbia-continuity-independent-v1'
Q=C/'preflight/central24-25-independent-v1'
BASE='c66d6d3665368fe1ae8986fb7c16340a103582c1'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def js(p): return json.loads(p.read_text())
def save(p,d):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x') as f:json.dump(d,f,indent=2,ensure_ascii=False);f.write('\n')
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def git(root,*args):return subprocess.check_output(['git','-C',str(root),*args])
def bind(p):return {'path':str(p.relative_to(A)),'sha256':sha(p)}
assert git(R,'rev-parse','HEAD').decode().strip()==BASE
assert sha(P/'HANDOFF.json')=='262baa33bb32dc864e4a5d3da6bef1dc9a58fc23f18696e3436b9c7d102a84d9'
assert sha(P/'MANIFEST.json')=='9b4e4bdde13e226fecf3dc04fde7b65aa3b37afbbb82ed16b3720c7131ce6463'
assert sha(Q/'HANDOFF.json')=='7a24f3cf7a8229028ec7091be34a99e78e0e13b67832a383e1cfc6767ce275dc'
assert sha(Q/'MANIFEST.json')=='90ad498a098dbe1d4b1a446be09242ceba6649b53b2136e0d6cb65ad6c30d363'
checks=[]
for root,key in [(P,'files'),(Q,'members')]:
 m=js(root/'MANIFEST.json')
 for row in m[key]:
  p=root/row['path'];assert p.is_file() and not p.is_symlink() and sha(p)==row['sha256'],p
  assert p.stat().st_size==row['bytes'],p
 checks.append({'manifest':str(root/'MANIFEST.json'),'sha256':sha(root/'MANIFEST.json'),'verified_members':len(m[key])})
S.mkdir(exist_ok=False)
for d in ['inputs','proposed','diffs','scripts','reviews','validation']:(S/d).mkdir()
copies=[]
def copy(src,rel,role):
 dest=S/rel;dest.parent.mkdir(parents=True,exist_ok=True)
 with dest.open('xb') as f:f.write(src.read_bytes())
 assert sha(dest)==sha(src)
 copies.append({'original_path':str(src),'capture':{'root':'artifact',**bind(dest)},'bytes':dest.stat().st_size,'role':role})
 return bind(dest)
for src,n in [(P/'HANDOFF.json','w07-HANDOFF.json'),(P/'MANIFEST.json','w07-MANIFEST.json'),(P/'decision/continuity-decision-v3.json','columbia-decision-v3.json'),(P/'inputs/selected-source-bindings.json','columbia-source-bindings.json'),(P/'inputs/input-index.json','w07-input-index.json'),(P/'validation/current-origin-bridges.json','w07-current-origin-bridges.json'),(P/'review/science/current-source-occurrence-matrix.json','columbia-seven-contexts.json'),(Q/'findings.json','central24-25-findings.json'),(Q/'HANDOFF.json','central24-25-HANDOFF.json'),(Q/'MANIFEST.json','central24-25-MANIFEST.json'),(Q/'original-record-fields.json','central24-25-original-record-fields.json')]:
 copy(src,'inputs/'+n,'Exact immutable review/decision input; its authorship and original scope remain unchanged')
for id in [6720201281,6720201502]:
 raw=js(O/f'inputs/issue1237-comment{id}.json');p=raw['parsed']
 save(S/f'inputs/issue1237-comment{id}.json',{'url':p['html_url'],'id':p['id'],'created_at':p['created_at'],'updated_at':p['updated_at'],'retrieved_at':raw['retrieved_at'],'body':p['body'],'capture_kind':'Exact public issue body and timestamps; account/profile data omitted from publication'})
copy(R/'data/ingredients/unmapped/Columbia_Blood_Agar_Base.yaml','inputs/Columbia_Blood_Agar_Base.before.yaml','Authentic same-path maintained beforeimage, exclusively for UNMAPPED_0118 edit')
assert sha(S/'inputs/Columbia_Blood_Agar_Base.before.yaml')=='29ed63a00d3f4f7a1652beee549526d625eef231f29b40691bd128d2f7608324'
copy(C/'integration/family-reconciliations-v2/blocked-prototypes/Columbia_Blood_Agar_Base_Oxoid_39g_Formulation.yaml','inputs/Oxoid39g.coordinator-prototype.yaml','Read-only previous coordinator composition input; not a W10-authored or independently installed owner')
sources=js(P/'inputs/selected-source-bindings.json')
w04=next(x for x in sources if x['worker']=='w04' and x['proposal']['owner_path'].endswith('/Oxoid_CM0331_Columbia_Blood_Agar_Base.yaml'))
W=C/'workers/w04/worktree';head=git(W,'rev-parse','HEAD').decode().strip();p=w04['payload'];blob=git(W,'show',head+':'+p['git_path'])
assert hashlib.sha256(blob).hexdigest()==p['sha256']=='4a3d54349a5c37167c2e13823d67808114c84212cea7dadc876334d4b10904d7'
assert (W/p['git_path']).read_bytes()==blob
copy(W/p['git_path'],'inputs/W04-Oxoid-CM0331.current-origin.yaml','Exact current committed W04 origin; copied read-only, no W10 authorship claim')
save(S/'inputs/w04-current-origin.json',{'observed_at':now(),'selected_head':w04['source_head'],'observed_local_head':head,'selected_payload_git_path':p['git_path'],'payload_sha256':p['sha256'],'local_equals_commit':True,'original_proposal':w04['proposal'],'original_decisions':w04['decisions'],'original_evidence':w04['evidence'],'approval':'Origin binding only; W04 source identity and histories remain original. No W04 case imported into W10.'})
for row in w04['evidence']:
 e=row['evidence'];b=row['capture_binding']
 if e['kind'] in ['primary_source','source_snapshot']:
  copy(P/b['capture'],'inputs/w04-captures/'+b['sha256'],'Exact captured W04 source body; original evidence metadata is retained in w04-current-origin.json')
matrix=js(P/'review/science/current-source-occurrence-matrix.json')
for row in matrix['rows']:
 b=row['recipe_capture'];src=P/'review/science'/b['snapshot'];assert sha(src)==b['sha256']
 copy(src,'inputs/context-recipes/'+b['sha256'],'Exact complete later owner-related source recipe; contextual routing, not a new assigned W10 occurrence')
ownsel=js(A/'successor-v6/selection.json'); core={}
for n,b in ownsel['authoritative_core'].items():
 path=A/b['path'];assert sha(path)==b['sha256'];assert git(R,'show',BASE+':'+str(path.relative_to(R)))==path.read_bytes();core[n]=js(path)
for p in core['proposals.json']['proposals']:
 path=A/p['after_capture']['path'];assert sha(path)==p['after_capture']['sha256'];assert git(R,'show',BASE+':'+str(path.relative_to(R)))==path.read_bytes()
snapshot={'at':now(),'predecessor_head':BASE,'prior_selector':{'path':'successor-v6/selection.json','sha256':sha(A/'successor-v6/selection.json')},'prior_core':ownsel['authoritative_core'],'prior_counts':{'cases':len(core['decisions.json']['decisions']),'proposals':len(core['proposals.json']['proposals']),'evidence':len(core['evidence.json']['evidence']),'occurrences':sum(len(d['occurrence_ids']) for d in core['decisions.json']['decisions'])},'verified_manifests':checks,'current_W04_origin':bind(S/'inputs/w04-current-origin.json'),'immutable_copies':copies,'seven_context_rows_not_new_assigned_cases':True,'scientific_or_release_approval':False}
save(S/'preflight.json',snapshot)
copy(Path(__file__),'scripts/preflight.py','Actual root preflight/capture script')
print(json.dumps({'status':'PASS','manifest_members':checks,'source_counts':snapshot['prior_counts'],'W04_observed_head':head,'copied_inputs':len(copies),'copied_bytes':sum(x['bytes'] for x in copies)},indent=2))
