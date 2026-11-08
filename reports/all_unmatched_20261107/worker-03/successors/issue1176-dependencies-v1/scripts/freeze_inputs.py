import pathlib,json,hashlib,subprocess,datetime,shutil
R=pathlib.Path.cwd(); C=R.parents[2]; O=R/'.temp/peptone-final-dependencies-v1'
def sha(b): return hashlib.sha256(b).hexdigest()
def git(r,*a): return subprocess.check_output(['git','-C',str(r),*a],text=True).strip()
def capture(p,name):
 b=p.read_bytes(); t=O/'inputs'/name; t.parent.mkdir(parents=True,exist_ok=True); assert not t.exists(); t.write_bytes(b); return {'source_path':str(p),'capture_path':str(t.relative_to(O)),'sha256':sha(b),'size':len(b)}
rows=[]
for n in ['GYPS','PYGS','Marine_agar_2216']: rows.append(capture(R/'data/ingredients/mapped'/f'{n}.yaml',f'before/{n}.yaml'))
p=C/'integration/final-same-target-reconciliation-v4/blocked-validation-v1/draft-selection.json';rows.append(capture(p,'draft-selection.json'))
for p in [R/'MAPPING_SEMANTICS.md',R/'src/mediaingredientmech/validation/write_validated.py',R/'src/mediaingredientmech/curate/curation_event.py',R/'src/mediaingredientmech/schema/mediaingredientmech.yaml',R/'docs/stock_components.md']: rows.append(capture(p,'contracts/'+p.name))
prior=[]
for d in ['peptone-consumer-independent-v1','combined-products-independent-v1','w03-provenance-successor-v1','complete-identifier-dependencies-v1']:
 for n in ['HANDOFF.json','HANDOFF-v2.json','MANIFEST.json','SELECTION.json','PUBLICATION-RECEIPT.json']:
  p=R/'.temp'/d/n
  if p.is_file():prior.append({'path':str(p.relative_to(R)),'sha256':sha(p.read_bytes())})
heads=[]
for w in ['w03','w04','w05','w06']:
 r=C/'workers'/w/'worktree'; heads.append({'worker':w,'local_head':git(r,'rev-parse','HEAD'),'branch':git(r,'branch','--show-current')})
obj={'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'root_head':git(R,'rev-parse','HEAD'),'root_tracked_status':git(R,'status','--short'),'inputs':rows,'prior_seals':prior,'local_head_observations':heads,'boundary':'Only this task output is mutable; all preserved source cores/seals remain immutable. No assertion of all historical/private absence.'}
(O/'input-freeze.json').write_text(json.dumps(obj,indent=2)+'\n'); print(json.dumps(obj,indent=2))
