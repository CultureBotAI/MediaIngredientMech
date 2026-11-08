"""Fixed-path immutable capture preparation; no maintained-data writes."""
from pathlib import Path
import hashlib,json,subprocess,datetime,shutil
R=Path.cwd(); C=R.parents[2]; A=R/'.temp/w03-oxoid-successor-v1'; P=R/'reports/all_unmatched_20261107/worker-03'; I=C/'integration/final-same-target-reconciliation-v2'; S=C/'preflight/existing-owner-scope-decisions-v1'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x):
 with p.open('x') as f:json.dump(x,f,indent=2);f.write('\n')
checks={}
for root in [I,S]:
 m=json.loads((root/'MANIFEST.json').read_text());rows=m['files'];rows=[dict(v,path=k) for k,v in rows.items()] if isinstance(rows,dict) else rows
 errors=[x['path'] for x in rows if sha(root/x['path'])!=x['sha256']]
 checks[str(root)]={'manifest_sha256':sha(root/'MANIFEST.json'),'members':len(rows),'errors':errors}
 assert not errors,errors
tracked=subprocess.check_output(['git','ls-files','-z']).decode().split('\0');tracked=[x for x in tracked if x]
dump(A/'context/tracked-before.json', {x:sha(R/x) for x in tracked if (R/x).is_file()})
old_manifest=P/'manifest.sha256';errors=[];count=0
for line in old_manifest.read_text().splitlines():
 h,n=line.split(None,1);n=n.lstrip('*');count+=1
 if sha(R/n)!=h:errors.append(n)
assert not errors,errors
checks['original_published_manifest']={'sha256':sha(old_manifest),'members':count,'errors':errors}
for name in ['HANDOFF.json','MANIFEST.json','publication-v4/candidate-summary-v4.json','publication-v4/candidates/NEW-OXOID-CM0149/trace.json','publication-v4/candidates/NEW-OXOID-CM0149/reinforced_clostridial_medium_oxoid_cm0149.yaml']:
 target=A/'context/coordinator-v4'/name;target.parent.mkdir(parents=True,exist_ok=True)
 with target.open('xb') as f:f.write((I/name).read_bytes())
checks['input_captures']=[{'source':str(I/n),'capture':str((A/'context/coordinator-v4'/n).relative_to(A)),'sha256':sha(I/n)} for n in ['HANDOFF.json','MANIFEST.json','publication-v4/candidate-summary-v4.json','publication-v4/candidates/NEW-OXOID-CM0149/trace.json','publication-v4/candidates/NEW-OXOID-CM0149/reinforced_clostridial_medium_oxoid_cm0149.yaml']]
checks['at']=datetime.datetime.now(datetime.timezone.utc).isoformat();checks['local_head']=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip();checks['remote_head_observed']='1196d5bc3aaba7563b829d5cbe7e54722fccc35d';checks['remote_observation_method']='git ls-remote --heads origin review/all-unmatched-w03-source-review-20261107; successful read-only escalated request after sandbox DNS failure';checks['publication_condition']='Pending explicit coordinator communication of completed W01 review and findings/dispositions; no acceptance inferred.'
dump(A/'context/input-verification.json',checks)
print(json.dumps({k:v for k,v in checks.items() if k not in ['input_captures']},indent=2))
