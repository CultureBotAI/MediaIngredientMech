"""Independent read-only package audit; refusal fixtures live only under this output."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,sys,shutil
OUT=Path(__file__).resolve().parent
RUN=OUT.parents[2]
MIM=RUN/'step3-mim'
PACKAGE_REL=Path('reports/carnitine_hydrochloride_1004_20261101/implementation')
P=MIM/PACKAGE_REL
OLD=RUN/'step3-implementation-checkpoints/original-ebabc642'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda p:json.loads(p.read_bytes())
expected='89dd30961cc14cb1dfa8926133d263779685c2a6cdf74428a1c8a9adb6d65baf'
assert sha(P/'manifest.json')==expected
manifest=load(P/'manifest.json');original=load(OLD/'manifest.json')
assert sha(OLD/'manifest.json')=='ebabc64251b29f0008a53f88a750c7c586ed4dfbefc2f2a556f8d0ac1bb58eaf'
for root,data in [(P,manifest),(OLD,original)]:
 paths={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file()}
 assert paths==set(data['files'])|{'manifest.json'}
 for name,item in data['files'].items():
  p=root/name;assert p.is_file() and not p.is_symlink()
  assert sha(p)==item['sha256'] and p.stat().st_size==item['bytes']
oldnames=set(original['files']);newnames=set(manifest['files'])
assert oldnames<=newnames
changed=[name for name in sorted(oldnames) if (OLD/name).read_bytes()!=(P/name).read_bytes()]
assert changed==['README.md','maintained-source-references.json']
assert len(oldnames)-len(changed)==233
assert (P/'verify.py').read_bytes()==(OLD/'verify.py').read_bytes()
references={}
for f in ['repository-references.json','maintained-source-references.json']:
 for name,item in load(P/f)['files'].items():
  assert not Path(name).is_absolute() and '..' not in Path(name).parts
  if name in references:assert references[name]==item
  references[name]=item
  p=MIM/name;assert p.is_file() and not p.is_symlink()
  assert sha(p)==item['sha256'] and p.stat().st_size==item['bytes']
oldref=load(OLD/'maintained-source-references.json')['files'];newref=load(P/'maintained-source-references.json')['files']
refchanges=[name for name in oldref if oldref[name]!=newref[name]]
assert refchanges==['.github/workflows/qc-reviewed-sssom.yaml']
selector=P/'selector-binding-1037';proof=load(selector/'change-proof.json')
before=(selector/'qc-reviewed-sssom.before.yaml').read_bytes();after=(selector/'qc-reviewed-sssom.after.yaml').read_bytes()
assert before.count(proof['old_selector'].encode())==1
assert before.replace(proof['old_selector'].encode(),proof['new_selector'].encode(),1)==after
assert (MIM/proof['workflow']).read_bytes()==after
assert before==subprocess.check_output(['git','show','99fe4b44d78126d78041a69eeb366c52bedf0caa:'+proof['workflow']],cwd=MIM)
protected=[name for name in references if name in ['.github/workflows/qc-evidence.yaml','scripts/.vendored_canon_ref'] or name.startswith('reviews/workflow/')]
for name in protected:assert (MIM/name).read_bytes()==subprocess.check_output(['git','show','99fe4b44d78126d78041a69eeb366c52bedf0caa:'+name],cwd=MIM)
originalcopies={}
for index in sorted(P.rglob('original-paths*.json')):
 for relative,item in load(index).items():
  target=index.parent/relative;source=Path(item['original_path'])
  assert target.read_bytes()==source.read_bytes(),(target,source)
  assert sha(target)==item['sha256'] and target.stat().st_size==item['bytes']
  originalcopies[str(target.relative_to(P))]={'original':str(source),'sha256':sha(target)}
for index in [selector/'control-original-paths.json']:
 for relative,item in load(index).items():
  target=index.parent/relative;source=Path(item['original_path']);assert target.read_bytes()==source.read_bytes() and sha(target)==item['sha256']
  originalcopies[str(target.relative_to(P))]={'original':str(source),'sha256':sha(target)}
independent={k:v for k,v in originalcopies.items() if k.startswith('independent/')}
assert independent
companion=selector/'native-companion';prior=load(companion/'prior-review.json');successor=load(companion/'review.json');refresh=load(companion/'dependency-refresh.json')
assert len(prior['decisions'])==len(successor['decisions'])==51 and prior['decisions']==successor['decisions']
assert prior['record_inputs']==successor['record_inputs'] and len(successor['record_inputs'])==20
assert prior['claims_sha256']==successor['claims_sha256'] and refresh['scientific_approval_added'] is False
assert all(sha(MIM/name)==h for name,h in refresh['owner_hashes_unchanged'].items())
assert not any('Carnitine' in name or 'NLDM' in name for name in successor['record_inputs'])
basepath='reports/sssom_completion_20260921/review.json';evpath='reports/sssom_completion_20260921/mapping-evidence.json'
baseold=json.loads(subprocess.check_output(['git','show','99fe4b44d78126d78041a69eeb366c52bedf0caa:'+basepath],cwd=MIM));basenew=load(MIM/basepath)
evold=json.loads(subprocess.check_output(['git','show','99fe4b44d78126d78041a69eeb366c52bedf0caa:'+evpath],cwd=MIM));evnew=load(MIM/evpath)
olddec={str(x['source_position']):x for x in baseold['decisions']};newdec={str(x['source_position']):x for x in basenew['decisions']}
semantic=lambda x:{k:v for k,v in x.items() if k not in {'source_position','evidence_key'}}
relocated=[]
for item in refresh['selected_mapping_evidence_unchanged']:
 loc=item['base_decision_locations'];oldpos=str(loc['before']['source_position']);newpos=str(loc['after']['source_position'])
 assert olddec[oldpos]==item['base_decision']
 assert semantic(olddec[oldpos])==semantic(newdec[newpos])
 assert evold['entries'][str(loc['before']['evidence_key'])]==evnew['entries'][str(loc['after']['evidence_key'])]==item['base_evidence']
 if loc['before']!=loc['after']:relocated.append({'claim_id':item['claim_id'],'locations':loc})
assert len(relocated)==17
assert all(d['before']==d['after'] for d in refresh['header_date_changes'].values())
commands=[]
def execute(label,script,root):
 argv=[str(RUN/'envs/mim/bin/python'),str(script),'--repository-root',str(root)]
 started=datetime.now(timezone.utc).isoformat();p=subprocess.run(argv,cwd=root,capture_output=True,text=True)
 log=OUT/(label+'.log');log.write_text(p.stdout+p.stderr)
 receipt={'argv':argv,'cwd':str(root),'started_at':started,'finished_at':datetime.now(timezone.utc).isoformat(),'exit_code':p.returncode,'log':str(log),'log_sha256':sha(log)}
 (OUT/(label+'.json')).write_text(json.dumps(receipt,indent=2)+'\n');commands.append(receipt);return p
native=execute('current-native-verifier',P/'verify.py',MIM);assert native.returncode==0;assert json.loads(native.stdout)['repository_references']==102
fixture=OUT/'refusal-fixture';shutil.copytree(P,fixture/PACKAGE_REL)
for name in references:
 target=fixture/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(MIM/name,target)
control=execute('copied-baseline',fixture/PACKAGE_REL/'verify.py',fixture);assert control.returncode==0
for name,label in [(proof['workflow'],'arbitrary-selector-refused'),('.github/workflows/qc-evidence.yaml','protected-evidence-refused')]:
 path=fixture/name;saved=path.read_bytes();path.write_bytes(saved+b'\n# independent refusal control\n')
 refused=execute(label,fixture/PACKAGE_REL/'verify.py',fixture)
 assert refused.returncode!=0 and name in refused.stderr and 'AssertionError' in refused.stderr
 path.write_bytes(saved)
assert sha(P/'manifest.json')==expected
for name,item in manifest['files'].items():assert sha(P/name)==item['sha256']
result={'checked_at':datetime.now(timezone.utc).isoformat(),'verdict':'PASS_BOUNDED_PACKAGE_AUDIT','current_manifest_sha256':expected,'current_indexed_files':len(manifest['files']),'old_manifest_sha256':sha(OLD/'manifest.json'),'old_total_files':len(original['files'])+1,'unchanged_old_indexed_files':len(oldnames)-len(changed),'changed_old_indexed_files':changed,'new_indexed_paths':sorted(newnames-oldnames),'current_repository_reference_count':len(references),'old_reference_value_changes':refchanges,'new_reference_paths':sorted(set(newref)-set(oldref)),'selector_exact_one_replacement':proof,'protected_paths':{name:sha(MIM/name) for name in protected},'verbatim_original_copy_count':len(originalcopies),'independent_verbatim_copy_count':len(independent),'copied_original_bindings':originalcopies,'companion_decisions_exactly_unchanged':51,'companion_owners_exactly_unchanged':20,'native_selected_mapping_payloads_unchanged':20,'native_selected_locations_changed':relocated,'commands':commands,'findings':[],'production_edits':False,'scope_limit':'Package/reference/retention audit only; not final scientific review, native structured review, committed-head audit or full gate certification.'}
(OUT/'receipt.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['selector_exact_one_replacement','new_reference_paths','copied_original_bindings','commands','new_indexed_paths','native_selected_locations_changed']},indent=2))
