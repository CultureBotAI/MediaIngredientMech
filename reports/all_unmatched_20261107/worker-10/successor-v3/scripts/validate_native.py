"""Unapplied complete overlay validation using existing native semantics; no gate changes."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys,subprocess,yaml,collections,copy,importlib.util
from mediaingredientmech.validation.write_validated import write_validated_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
from mediaingredientmech.synonym_policy import is_resolving_synonym, preferred_term_owners
R=Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v3';B=A/'successor-v2';core=S/(sys.argv[1] if len(sys.argv)>1 else 'assembly-v1');N=S/(sys.argv[2] if len(sys.argv)>2 else 'validation-v1');N.mkdir(parents=True,exist_ok=True);scratch=R/'.temp/all-unmatched-worker-10/successor-v3'/N.name;scratch.mkdir(parents=True,exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();load=lambda p:json.loads(p.read_text())
def save(p,d):
 with p.open('x') as f:json.dump(d,f,indent=2,ensure_ascii=False);f.write('\n')
D=load(core/'decisions.json')['decisions'];P=load(core/'proposals.json')['proposals'];owners=sorted({x['path'] for d in D for x in d['owner_records']}|{p['owner_path'] for p in P if p['before_sha256']});payloads=[A/p['after_capture']['path'] for p in P]
cmd=['.temp/all-unmatched-worker-10/venv/bin/python','scripts/validate_strict.py',*owners,*[str(p.relative_to(R)) for p in payloads],'--workers','1','--out',str((N/'strict-failures.tsv').relative_to(R))];proc=subprocess.run(cmd,text=True,capture_output=True)
for n,t in [('strict.stdout',proc.stdout),('strict.stderr',proc.stderr)]:
 with (N/n).open('x') as f:f.write(t)
save(N/'strict-command.json',{'at':datetime.now(timezone.utc).isoformat(),'argv':cmd,'exit_code':proc.returncode,'owners':len(owners),'payloads':len(payloads)});assert proc.returncode==0
copies=[]
for p,f in zip(P,payloads):
 assert sha(f)==p['after_capture']['sha256'];d=yaml.safe_load(f.read_text());dest=scratch/(p['proposal_id']+'.yaml');assert not dest.exists();write_validated_ingredient(d,dest);assert yaml.safe_load(dest.read_text())==d;assert sha(f)==p['after_capture']['sha256'];copies.append({'proposal_id':p['proposal_id'],'source_sha256':sha(f),'scratch_sha256':sha(dest),'semantic_roundtrip_equal':True})
save(N/'guarded-roundtrip.json',{'at':datetime.now(timezone.utc).isoformat(),'writer':'write_validated_ingredient','scope':'Private scratch copies only; dictionary equality after native guarded serialization; no aggregate/SSSOM/export rebuild claimed.','copies':copies})
baseline={str(f.relative_to(R)):yaml.safe_load(f.read_text()) for f in sorted((R/'data/ingredients').rglob('*.yaml'))}
def overlay(props):
 records=copy.deepcopy(baseline)
 for p in props:
  f=A/p['after_capture']['path'];assert sha(f)==p['after_capture']['sha256']
  if p['kind']=='edit_existing_owner':assert sha(R/p['owner_path'])==p['before_sha256'];records.pop(p['owner_path'])
  else:assert p['before_sha256'] is None and not (R/p['owner_path']).exists()
  dest=p.get('destination_path',p['owner_path']);assert dest not in records;records[dest]=yaml.safe_load(f.read_text())
 return records
old=overlay(load(B/'proposals.json')['proposals']);records=overlay(P);bv=validate_component_partonomy(list(baseline.values()));ov=validate_component_partonomy(list(old.values()));violations=validate_component_partonomy(list(records.values()));save(N/'partonomy.json',{'at':datetime.now(timezone.utc).isoformat(),'baseline_records':len(baseline),'baseline_violations':[str(x) for x in bv],'predecessor_projected_records':len(old),'predecessor_violations':[str(x) for x in ov],'projected_records':len(records),'selected_payloads':len(P),'violations':[str(x) for x in violations],'scope':'Whole frozen catalog plus complete selected replacements/additions in memory. No application or release approval.'});assert not bv and not ov and not violations
spec=importlib.util.spec_from_file_location('native_duplicate_audit',R/'scripts/audit_duplicate_identifiers.py');native=importlib.util.module_from_spec(spec);spec.loader.exec_module(native)
def collisions(rs):
 ids=collections.defaultdict(list)
 for path,r in rs.items():
  if r.get('mapping_status') not in native.NOT_A_CLAIM:ids[r['identifier']].append(path)
 return {k:sorted(v) for k,v in ids.items() if len(v)>1}
def aliases(rs):
 mapped={k:v for k,v in rs.items() if '/mapped/' in k};owned=preferred_term_owners(mapped);out=[]
 for path,r in mapped.items():
  if r.get('mapping_status')=='REJECTED':continue
  for i,s in enumerate(r.get('synonyms') or []):
   if not is_resolving_synonym(s):continue
   label=str(s.get('synonym_text','')).strip().casefold();others=owned.get(label,frozenset())-{path}
   if others:out.append({'owner_path':path,'field':f'synonyms[{i}]','text':s['synonym_text'],'other_preferred_owners':sorted(others)})
 return out
ci={k:collisions(v) for k,v in [('maintained',baseline),('predecessor',old),('successor',records)]};newcoll={k:v for k,v in ci['successor'].items() if v!=ci['predecessor'].get(k)};aa={k:aliases(v) for k,v in [('maintained',baseline),('predecessor',old),('successor',records)]}
# Renaming the authentic owner path is a routed identity transition, not a new alias claim.
def canon_alias(row):return (row['owner_path'],row['text'],tuple(row['other_preferred_owners']))
old_alias={canon_alias(x) for x in aa['predecessor']};newalias=[x for x in aa['successor'] if canon_alias(x) not in old_alias]
save(N/'identifier-alias-projection.json',{'at':datetime.now(timezone.utc).isoformat(),'native_functions':['scripts/audit_duplicate_identifiers.py NOT_A_CLAIM','mediaingredientmech.synonym_policy.preferred_term_owners','mediaingredientmech.synonym_policy.is_resolving_synonym'],'catalogs':{k:len(v) for k,v in [('maintained',baseline),('predecessor',old),('successor',records)]},'duplicate_identifier_groups':ci,'new_or_changed_identifier_groups':newcoll,'owned_alias_conflicts':aa,'new_alias_conflicts_vs_predecessor':newalias,'meaning':'Read-only complete overlay observation. Inherited conflicts retain existing holds and are not approved by this report; any new collision needs source-specific assessment before selection. No baseline/gate/threshold change.'})
assert not newcoll,newcoll
ids=collections.defaultdict(list)
for p,f in zip(P,payloads):ids[yaml.safe_load(f.read_text())['identifier']].append(p['proposal_id'])
assert all(len(v)==1 for v in ids.values());assert len({p['owner_path'] for p in P})==len(P)
bad=dict(yaml.safe_load(payloads[0].read_text()));bad['invalid_successor_probe']=True;dest=scratch/'must-not-exist-invalid.yaml'
try:write_validated_ingredient(bad,dest)
except Exception as exc:err=type(exc).__name__+': '+str(exc)
else:raise AssertionError('native guard accepted invalid field')
assert not dest.exists();save(N/'negative-control.json',{'unknown_field_refused':True,'destination_absent':True,'error':err,'scientific_validation':False})
save(N/'validation-receipt.json',{'at':datetime.now(timezone.utc).isoformat(),'status':'PASS' if not newalias else 'NATIVE_SCHEMA_PARTONOMY_PASS_ALIAS_REVIEW_REQUIRED','core_hashes':{n:sha(core/n) for n in ['decisions.json','evidence.json','proposals.json']},'strict_exit_code':proc.returncode,'owners':len(owners),'payloads':len(P),'guarded_copies':len(copies),'partonomy_records':len(records),'partonomy_violations':0,'new_identifier_groups':len(newcoll),'new_alias_conflicts':len(newalias),'negative_control_refused':True,'script_sha256':sha(Path(__file__)),'approval':False})
print(json.dumps(load(N/'validation-receipt.json'),indent=2))
