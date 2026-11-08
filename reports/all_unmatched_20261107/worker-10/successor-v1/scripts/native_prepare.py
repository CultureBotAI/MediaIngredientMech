import pathlib,json,yaml,subprocess,datetime,hashlib,collections
from mediaingredientmech.validation.write_validated import write_validated_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
R=pathlib.Path.cwd();P=R/'reports/all_unmatched_20261107/worker-10';S=P/'successor-v1';N=S/'native';N.mkdir(exist_ok=True)
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
def dump(f,x):f.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
ds=json.loads((S/'decisions.json').read_text())['decisions'];ps=json.loads((S/'proposals.json').read_text())['proposals'];owners=sorted({o['path'] for d in ds for o in d['owner_records']});targets=[]
for i,d in enumerate(ds):
 targets.append({'target_id':d['case_id'],'path':str((S/'context/shard-10.json').relative_to(R)),'selector':'$.cases['+str(i)+']','label':d['source']['source_label'] or '(empty raw label)','kind':'snapshot_row','ownership_note':'Exact immutable assigned sourcecase, not a fabricated MIMowner. Actual candidate ownerpreimages and source producer remain explicitly bound in decisions.json. No source-table correction or alias-release authorized.'})
for p in ps:
 f=P/p['after_capture']['path'];o=yaml.safe_load(f.read_text());assert sha(f)==p['after_capture']['sha256']
 targets.append({'target_id':'PROPOSAL:'+p['proposal_id'],'path':str(f.relative_to(R)),'label':o['preferred_term'],'kind':'source','record_class':'IngredientRecord','ownership_note':'Isolated unapplied proposed bytes for '+p['owner_path']+'; old owner hash '+str(p['before_sha256'])+'. Future maintained owner is not yet modified.'})
dump(N/'targets.json',{'targets':targets})
cmd=['.temp/all-unmatched-worker-10/venv/bin/python','scripts/validate_strict.py',*owners,*[str((P/x['after_capture']['path']).relative_to(R)) for x in ps],'--workers','1','--out',str((N/'strict-failures.tsv').relative_to(R))]
r=subprocess.run(cmd,text=True,capture_output=True);(N/'strict-validation.log').write_text(r.stdout+r.stderr);dump(N/'strict-command.json',{'argv':cmd,'exit_code':r.returncode,'before_owners':len(owners),'proposals':len(ps)});assert r.returncode==0;print('strict',len(owners),len(ps),flush=True)
scratch=R/'.temp/all-unmatched-worker-10/successor-v1/guarded-validation';scratch.mkdir(exist_ok=True);out=[]
for p in ps:
 f=P/p['after_capture']['path'];o=yaml.safe_load(f.read_text());dest=scratch/(p['proposal_id']+'.yaml');write_validated_ingredient(o,dest);assert yaml.safe_load(dest.read_text())==o;assert sha(f)==p['after_capture']['sha256'];out.append({'proposal_id':p['proposal_id'],'payload_sha256':sha(f),'scratch_sha256':sha(dest),'parsed_equal':True})
dump(N/'guarded-validation.json',{'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'count':len(out),'writer':'write_validated_ingredient','scope':'Private scratch only; immutable proposed capture bytes retained','proposals':out});print('guarded',len(out),flush=True)
replace={p['owner_path']:yaml.safe_load((P/p['after_capture']['path']).read_text()) for p in ps if p['kind']=='edit_existing_owner'}
records=[replace.get(str(f.relative_to(R)),yaml.safe_load(f.read_text())) for f in sorted((R/'data/ingredients').rglob('*.yaml'))];records+=[yaml.safe_load((P/p['after_capture']['path']).read_text()) for p in ps if p['kind']=='new_owner']
v=validate_component_partonomy(records);dump(N/'combined-partonomy.json',{'method':'Native validate_component_partonomy on full baseline plus all isolated replacements/additions in memory; no maintained writes','records':len(records),'proposal_count':len(ps),'violations':[str(x) for x in v],'release_approval':False});assert not v;print('partonomy',len(records),len(v),flush=True)
ident=collections.defaultdict(list)
for p in ps:ident[yaml.safe_load((P/p['after_capture']['path']).read_text())['identifier']].append(p['proposal_id'])
dump(N/'proposal-collisions.json',{'duplicate_owner_paths':[x for x,n in collections.Counter(p['owner_path'] for p in ps).items() if n>1],'duplicate_proposed_identifiers':{k:v for k,v in ident.items() if len(v)>1},'limits':'Existing catalog/global alias collisions remain source-specific integration holds; absence of duplicate proposed owner paths does not approve cross-shard merge.'})
