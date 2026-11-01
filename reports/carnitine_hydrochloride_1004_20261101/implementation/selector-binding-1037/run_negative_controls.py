"""Read-only production verification and fresh-process negative controls in copied inputs."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys,datetime
B=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/approved-plan-20261101T031134Z')
R=B/'step3-mim';REL=Path('reports/carnitine_hydrochloride_1004_20261101/implementation');P=R/REL
E=B/'step3-selector-binding-1037';E.mkdir(exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
refs={}
for name in ['repository-references.json','maintained-source-references.json']:refs.update(json.loads((P/name).read_text())['files'])
for name,e in refs.items():assert sha(R/name)==e['sha256'],name
source_hashes={name:sha(R/name) for name in refs}
fixture=E/'copied-repository';fixture.mkdir()
for name in refs:
 d=fixture/name;d.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(R/name,d)
shutil.copytree(P,fixture/REL)
package=fixture/REL
index={'scope':'Provisional isolated snapshot for selector-binding negative controls; final publication adds these results and freezes separately.','files':{str(p.relative_to(package)):{'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(package.rglob('*')) if p.is_file() and p!=package/'manifest.json'}}
(package/'manifest.json').write_text(json.dumps(index,indent=2)+'\n')
with (E/'provisional-manifest.json').open('x') as f:json.dump(index,f,indent=2);f.write('\n')
results=[]
for name,relative,replacement in [('baseline',None,None),('arbitrary_selector','.github/workflows/qc-reviewed-sssom.yaml',(b'reports/ingredient_bundle_20261101_carnitine1004/review.json',b'reports/unreviewed-arbitrary/review.json')),('protected_qc_evidence','.github/workflows/qc-evidence.yaml',None)]:
 if relative:
  target=fixture/relative;before=target.read_bytes()
  if replacement:
   old,new=replacement;assert before.count(old)==1;target.write_bytes(before.replace(old,new))
  else:target.write_bytes(before+b'\n# unauthorized negative-control alteration\n')
 started=datetime.datetime.now(datetime.timezone.utc).isoformat()
 argv=[sys.executable,str(package/'verify.py'),'--repository-root',str(fixture)]
 proc=subprocess.run(argv,cwd=fixture,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
 log=E/f'{name}.log'
 with log.open('x') as f:f.write(proc.stdout)
 if relative:
  mutation_hash=sha(target);target.write_bytes(before)
  accepted=proc.returncode==1 and 'AssertionError:' in proc.stdout and relative in proc.stdout
 else:mutation_hash=None;accepted=proc.returncode==0 and '"status": "PASS"' in proc.stdout
 results.append({'name':name,'argv':argv,'started_at':started,'exit_code':proc.returncode,'expected_result_observed':accepted,'mutation_sha256':mutation_hash,'asserted_reference':relative,'log_sha256':sha(log)})
 assert accepted,results[-1]
assert {name:sha(R/name) for name in refs}==source_hashes
receipt={'verifier_sha256':sha(P/'verify.py'),'verifier_unchanged_from_original':sha(P/'verify.py')==json.loads((P/'selector-binding-1037/original-manifest.json').read_text())['files']['verify.py']['sha256'],'provisional_manifest_sha256':sha(E/'provisional-manifest.json'),'reference_hashes':source_hashes,'production_references_unchanged':True,'fresh_process_controls':results,'limits':'Controls ran on a complete copied provisional package and copied referenced inputs. Final publication manifest includes these results and is verified separately. No production file edited.'}
with (E/'negative-controls.json').open('x') as f:json.dump(receipt,f,indent=2);f.write('\n')
print(json.dumps({'verifier_unchanged':receipt['verifier_unchanged_from_original'],'reference_count':len(refs),'controls':[{k:e[k] for k in ['name','exit_code','expected_result_observed']} for e in results],'production_references_unchanged':True},indent=2))
