"""Report-local replay of unchanged native gates; never applies proposals."""
import argparse, collections, hashlib, importlib.util, json, unicodedata
from pathlib import Path
from datetime import datetime, timezone
import yaml
from mediaingredientmech.validation.write_validated import validate_ingredient, write_validated_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy

parser=argparse.ArgumentParser()
parser.add_argument('--proposals',type=Path,required=True)
parser.add_argument('--out',type=Path,required=True)
args=parser.parse_args()
W=Path.cwd();B=W/'reports/all_unmatched_20261107/worker-05';S=W/'.temp/w05-final-correction-v1'
out=args.out;out.mkdir(parents=True,exist_ok=False)
(out/'guarded-readback').mkdir()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
nfc=lambda p:unicodedata.normalize('NFC',str(p))
dump=lambda p,x:p.write_text(json.dumps(x,indent=2,ensure_ascii=False,default=str)+'\n')
raw=json.loads(args.proposals.read_text());proposals=raw['proposals'] if isinstance(raw,dict) else raw
baseline={nfc(p.relative_to(W)):(p,yaml.safe_load(p.read_text())) for p in (W/'data/ingredients').rglob('*.yaml')}
overlay={p:r for p,(_,r) in baseline.items()};checks=[];errors=[];owners=set();destinations=set()
for i,p in enumerate(proposals):
 cap=p['after_capture']; src=B/cap['path']
 if not src.is_file() and cap['path'].startswith('final-correction-v1/'):
  src=S/cap['path'].removeprefix('final-correction-v1/')
 assert sha(src)==cap['sha256'],src
 r=yaml.safe_load(src.read_text()); owner=nfc(p['owner_path']);dest=nfc(p.get('destination_owner_path',owner))
 assert owner not in owners,('repeated owner',owner)
 assert dest not in destinations,('repeated destination',dest)
 owners.add(owner);destinations.add(dest)
 old=baseline.get(owner)
 if p['kind']=='edit_existing_owner':
  assert old and sha(old[0])==p['before_sha256'],owner
  assert r.get('curation_history',[])[:len(old[1].get('curation_history',[]))]==old[1].get('curation_history',[]),('lost history',owner)
  negatives=[s for s in old[1].get('synonyms',[]) if s.get('synonym_type')=='REJECTED_LABEL']
  assert all(s in r.get('synonyms',[]) for s in negatives),('lost negative',owner)
 else: assert old is None and p.get('before_sha256') is None,('new owner collision',owner)
 if dest!=owner: assert dest not in baseline,('destination collision',dest)
 assert ('/mapped/' in dest)==(r.get('mapping_status') not in ['UNMAPPED']),('mapped destination',dest,r.get('mapping_status'))
 schema_errors=validate_ingredient(r)
 assert not schema_errors,(p['proposal_id'],schema_errors)
 guard=out/'guarded-readback'/f'{i:03d}-{src.name}'
 write_validated_ingredient(r,guard)
 assert yaml.safe_load(guard.read_text())==r
 overlay.pop(owner,None);overlay[dest]=r
 checks.append(dict(proposal_id=p['proposal_id'],owner_path=owner,destination_owner_path=dest,
   selected_capture=cap,guarded_readback_sha256=sha(guard),guarded_schema='PASS',
   baseline_before_sha256=p.get('before_sha256'),history_preserved=True,negative_labels_preserved=True))
violations=validate_component_partonomy(overlay.values())
spec=importlib.util.spec_from_file_location('native_case',W/'scripts/check_record_filename_case.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
case_collisions=mod.find_collisions(set(overlay));drift=mod.find_drift(set(baseline),set(overlay))
active=lambda records:{k:[p for p,r in records.items() if r.get('mapping_status')!='REJECTED' and r.get('identifier')==k] for k in {r.get('identifier') for r in records.values() if r.get('mapping_status')!='REJECTED'}}
before_index=active({p:r for p,(_,r) in baseline.items()}); after_index=active(overlay)
new_collisions={k:v for k,v in after_index.items() if len(v)>1 and set(v)!=set(before_index.get(k,[]))}
errors += [str(v) for v in violations]
errors += ['case collisions:'+str(case_collisions)] if case_collisions else []
errors += ['case drift:'+str(drift)] if drift else []
errors += ['new identifier collisions:'+str(new_collisions)] if new_collisions else []
dump(out/'overlay-paths.json',[dict(path=p,identifier=r.get('identifier'),mapping_status=r.get('mapping_status')) for p,r in sorted(overlay.items())])
dump(out/'native-validation.json',dict(at=datetime.now(timezone.utc).isoformat(),
 author='/root',scope='Full path-keyed baseline substitution, isolated replay only; no maintained application, generated exports or source/owner release.',
 inputs=dict(proposals=dict(path=str(args.proposals),sha256=sha(args.proposals))),
 native_implementations=[dict(path=n,sha256=sha(W/n)) for n in ['src/mediaingredientmech/validation/write_validated.py','src/mediaingredientmech/schema/mediaingredientmech.yaml','src/mediaingredientmech/validation/component_partonomy.py','scripts/check_record_filename_case.py']],
 baseline_records=len(baseline),candidate_payloads=len(proposals),overlay_records=len(overlay),
 overlay_decompositions=sum(bool(r.get('components')) for r in overlay.values()),
 overlay_parts=sum(len(r.get('components',[])) for r in overlay.values()),
 guarded_payloads=checks,partonomy_violations=[str(v) for v in violations],filename_case_collisions=case_collisions,
 filename_case_drift=drift,new_identifier_collisions=new_collisions,
 preserved_baseline_duplicate_identifiers={k:v for k,v in after_index.items() if len(v)>1 and k not in new_collisions},
 errors=errors,status='PASS' if not errors else 'FAIL'))
print(json.dumps(dict(status='PASS' if not errors else 'FAIL',payloads=len(proposals),overlay=len(overlay),errors=errors)))
raise SystemExit(bool(errors))
