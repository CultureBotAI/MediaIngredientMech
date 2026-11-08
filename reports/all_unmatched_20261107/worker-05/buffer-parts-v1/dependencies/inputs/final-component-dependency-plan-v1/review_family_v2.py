from pathlib import Path
import json,yaml,hashlib,subprocess,sys,datetime,copy
R=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech');C=R/'.temp/all-unmatched-20261107';A=C/'integration/family-reconciliations-v2';V=C/'integration/family-reconciliations-v1';O=Path(__file__).parent/'family-v2-independent';O.mkdir(exist_ok=True)
sha=lambda b:hashlib.sha256(b).hexdigest();pins={}
def read(p):
 b=p.read_bytes();pins[str(p)]=sha(b);return b
def load(p):return json.loads(read(p))
def rec(p):return yaml.safe_load(read(p))
def put(n,v):
 with(O/n).open('x')as f:json.dump(v,f,indent=2,ensure_ascii=False);f.write('\n')
def diff(a,b,p=''):
 if type(a)!=type(b):return[p]
 if isinstance(a,dict):return sum([diff(a.get(k),b.get(k),p+'/'+k)for k in sorted(a.keys()|b.keys())],[])
 if isinstance(a,list):return []if a==b else[p]
 return []if a==b else[p]
checks=[]
for root in [A,V,C/'preflight/four-family-review-triage-v1']:
 m=load(root/'MANIFEST.json'); entries=m['files']; actual={p.relative_to(root).as_posix()for p in root.rglob('*')if p.is_file()and p.name!='MANIFEST.json'}; listed=set()
 for e in entries:
  p=root/e['path'];assert not p.is_symlink();assert sha(read(p))==e['sha256'],p;listed.add(e['path'])
 # Old manifests may have deliberately excluded small self-seal documents; compare declared members only and record leftovers honestly.
 checks.append({'root':str(root),'manifest_sha256':pins[str(root/'MANIFEST.json')],'declared_members_checked':len(entries),'unlisted_regular_files':sorted(actual-listed)})
sel=load(A/'SELECTOR.json');bridges=load(A/'current-origin-bridges.json');idx=load(A/'candidate-index.json');fields=[];records=[]
for e in idx:
 p=A/e['payload'];q=V/e['payload'];a=rec(q);b=rec(p);assert pins[str(p)]==e['payload_sha256'];assert pins[str(q)]==e['predecessor_payload_sha256'];ds=diff(a,b)
 assert set(ds)<= {'/curation_history','/notes'},(e['group'],ds)
 assert b.get('curation_history',[])[:len(a.get('curation_history',[]))]==a.get('curation_history',[])
 assert a.get('components')==b.get('components') and a.get('component_assertion')==b.get('component_assertion')
 for o in bridges:
  if o['origin_index']not in e['origin_indices']:continue
  pr=rec(A/o['payload']['path'])
  for ev in pr.get('curation_history',[]):assert ev in b.get('curation_history',[]),(e['group'],o['origin_index'],ev)
 fields.append({'group':e['group'],'payload_sha256':e['payload_sha256'],'predecessor_sha256':e['predecessor_payload_sha256'],'changed_field_paths':ds,'full_old_history_exact_prefix':True,'all_current_origin_events_retained':True,'component_claims_exact':True,'note_before':a.get('notes')if'/notes'in ds else None,'note_after':b.get('notes')if'/notes'in ds else None,'eligibility':e['eligibility']});records.append(b)
originproof=[]
for o in bridges:
 W=C/f"workers/w{o['worker']:02d}/worktree";head=o['remote_and_local_head']; checked=[]
 for e in list(o['current_core'].values())+[o['payload']]:
  b=read(A/e['path']);assert sha(b)==e['sha256'];g=subprocess.check_output(['git','-C',str(W),'show',head+':'+e['git_path']]);assert b==g;checked.append({'git_path':e['git_path'],'sha256':sha(b)})
 originproof.append({'origin_index':o['origin_index'],'worker':o['worker'],'published_git_head':head,'checked_committed_core_and_payload':checked,'local_head_observed':subprocess.check_output(['git','-C',str(W),'rev-parse','HEAD'],text=True).strip(),'no_new_remote_observation':True})
route=load(A/'case-occurrence-routing.json');oldroute=load(V/'case-occurrence-routing.json');assert route==oldroute
cases=[c for g in route for c in g['cases']];occ=[x for c in cases for x in c.get('occurrences',[])];assert len(cases)==12 and len(occ)==15
ff1=load(A/'FF001-source-binding.json');recipe=rec(A/ff1['recipe']['path']);assert pins[str(A/ff1['recipe']['path'])]==ff1['recipe']['sha256'];case=ff1['full_case_and_original_decision']['source_case'];assert case['case_id']==ff1['full_case_and_original_decision']['binding']['case_id'];assert recipe['ingredients'][1]==case['occurrences'][0]['raw_component']
ff2=load(A/'FF002-evidence-binding.json');body=read(A/ff2['capture']['path']).decode();assert 'Columbia'in body and '44'in body;bdmeta=load(A/'BD-original-retrieval-provenance.json');failed=load(A/'failed-bd-response-binding.json')
for e in bdmeta:
 assert sha(read(A/e['path']))==e['sha256']
# Reproduce narrow native checks without corpus writes.
sys.path.insert(0,str(C/'integration/worktree/src'))
from mediaingredientmech.validation.write_validated import validate_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
errs=[validate_ingredient(r)for r in records];assert not any(errs),errs
base=C/'preflight/final-intake-candidate-v1/snapshot/baseline';inv=load(A/'baseline-owner-inventory.json');inv=inv.get('owners',inv);baseline=[]
for n,h in inv.items():
 p=base/n;assert sha(read(p))==h;baseline.append(rec(p))
be=[str(e)for e in validate_component_partonomy(baseline)];ae=[str(e)for e in validate_component_partonomy(baseline+records)];assert not be and not ae
bad=copy.deepcopy(records[0]);bad['invented_approval']=True;negative=validate_ingredient(bad);assert negative
native=rec(A/'author-observation.yaml');nativeinputs=[]
for e in native['source']['inputs']:
 p=R/e['path'];assert sha(read(p))==e['sha256'];nativeinputs.append(e)
# Precise final membership and pin rechecks.
for p,h in pins.items():assert sha(Path(p).read_bytes())==h,p
put('checks.json',{'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'manifest_checks':checks,'candidate_deltas':fields,'git_origin_checks':originproof,'routing_exact':True,'cases':len(cases),'occurrences':len(occ),'schema_candidates':4,'baseline_owners':len(baseline),'baseline_partonomy':be,'overlay_partonomy':ae,'unknown_field_rejected':bool(negative),'native_author_review_inputs_rechecked':len(nativeinputs),'native_author_review_independence':native['reviewer'],'native_author_source':native['source']['state'],'native_author_git_revision':native['source']['git_revision'],'maintained_save_not_run':True,'new_remote_head_claim':False})
put('input-pins.json',pins)
print(json.dumps({'manifest_members':[x['declared_members_checked']for x in checks],'deltas':[(x['group'],x['changed_field_paths'])for x in fields],'baseline':len(baseline),'native_author_inputs':len(nativeinputs),'zero_partonomy':not ae},indent=2))
