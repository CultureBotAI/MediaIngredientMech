from pathlib import Path
import collections, datetime, hashlib, json, subprocess, yaml
from mediaingredientmech.validation.write_validated import validate_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy

B=Path('reports/all_unmatched_20261107/worker-05'); C=B/'correction-1193-v1'; O=C/'media'
S=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
BASE='e000d66dd26ab053e9b17ce7bf8d3c873c3dde99'; F=O/'followon-cooked-meat'
sha=lambda b:hashlib.sha256(b).hexdigest()
read=lambda p:json.loads(p.read_text())
inputs={f:sha((O/f).read_bytes()) for f in ['decisions.json','evidence.json','proposals.json']}
D=read(O/'decisions.json')['decisions']; E=read(O/'evidence.json')['evidence']; P=read(O/'proposals.json')['proposals']
di={d['case_id']:d for d in D}; ei={e['evidence_id']:e for e in E}; pi={p['proposal_id']:p for p in P}
assert len(di)==len(D)==60 and len(ei)==len(E) and len(pi)==len(P)
for d in read(B/'media/decisions.json')['decisions']:
 for k in ['case_input_sha256','source','occurrence_ids']: assert di[d['case_id']][k]==d[k]
for e in read(B/'media/evidence.json')['evidence']: assert ei[e['evidence_id']]==e
for e in E:
 c=e['capture']; p=(B if c['root']=='artifact' else S)/c['path']; assert sha(p.read_bytes())==c['sha256'],p
 assert e['kind'] in ['primary_source','source_snapshot','ontology','native_record_review','independent_review','unsuccessful_search','local_validation']
for d in D:
 assert set(d['evidence_ids'])<=ei.keys() and set(d['proposal_ids'])<=pi.keys()
 assert d['correction_reassessment']['status']=='complete'
 for own in d['owner_records']: assert sha(subprocess.check_output(['git','show',BASE+':'+own['path']]))==own['sha256']
schema_errors=[]
for p in P:
 assert set(p['evidence_ids'])<=ei.keys() and set(p['case_ids'])<=di.keys()
 raw=(B/p['after_capture']['path']).read_bytes(); assert sha(raw)==p['after_capture']['sha256']
 schema_errors += [str(v) for v in validate_ingredient(yaml.safe_load(raw))]
 if p['before_sha256']: assert sha(subprocess.check_output(['git','show',BASE+':'+p['owner_path']]))==p['before_sha256']
 else: assert not Path(p['owner_path']).exists()
assert not schema_errors,schema_errors
assert len({p['owner_path'] for p in P})==len(P)

# Explicit filesystem globs include ignored records. Ensure tracked maintained data
# still equals the frozen baseline, then bind every included file's actual bytes.
subprocess.run(['git','diff','--quiet',BASE,'--','data/ingredients'],check=True)
catalog={}; catalog_hashes={}
for p in sorted([*Path('data/ingredients/mapped').glob('*.yaml'),*Path('data/ingredients/unmapped').glob('*.yaml')]):
 raw=p.read_bytes(); catalog[str(p)]=yaml.safe_load(raw); catalog_hashes[str(p)]=sha(raw)
(F/'catalog-inputs.json').write_text(json.dumps(catalog_hashes,indent=2)+'\n')
baseline_violations={str(v) for v in validate_component_partonomy(catalog.values())}

def apply(proposals, archive=None):
 out=dict(catalog); destinations=[]; bindings=[]
 assert len({p['owner_path'] for p in proposals})==len(proposals)
 for p in proposals:
  owner=p['owner_path']; dest=p.get('destination_owner_path',owner)
  raw=((archive/'after-payloads'/p['proposal_id']/Path(p['after_capture']['path']).name) if archive else B/p['after_capture']['path']).read_bytes()
  assert sha(raw)==p['after_capture']['sha256'],p['proposal_id']
  if p['before_sha256']:
   assert catalog_hashes[owner]==p['before_sha256'],owner
   out.pop(owner)
  else: assert owner not in catalog,owner
  assert dest not in out,dest
  out[dest]=yaml.safe_load(raw); destinations.append(dest)
  bindings.append({'proposal_id':p['proposal_id'],'owner_path':owner,'destination_owner_path':dest,'after_sha256':sha(raw)})
 assert len(set(destinations))==len(destinations)
 errors={str(v) for v in validate_component_partonomy(out.values())}
 new=sorted(errors-baseline_violations)
 return {'proposal_count':len(proposals),'catalog_size':len(out),'new_partonomy_violations':new,'total_partonomy_violations':len(errors),'bindings':bindings},out

pre=O/'superseded/pre-followon-integration'; prior=read(pre/'proposals.json')['proposals']
prior_receipt,_=apply(prior,pre)
ours=[p for p in P if p['proposal_id'].startswith('M1193-P-FOLLOWON-')]
intermediate,intermediate_catalog=apply(prior+ours)
live=[]; live_inputs={}
for g in ['root','chemicals','materials','media']:
 p=C/g/'proposals.json'; raw=p.read_bytes(); live_inputs[str(p.relative_to(B))]=sha(raw); live.extend(json.loads(raw)['proposals'])
combined,combined_catalog=apply(live)
target_ids=['kgmicrobe.ingredient:modified_cooked_meat_medium','kgmicrobe.ingredient:fastidious_anaerobe_broth_with_meat_granules']
for label,rows in [('intermediate',intermediate_catalog),('combined',combined_catalog)]:
 assert not any(r.get('identifier')=='FOODON:03305103' for r in rows.values()),label
 assert not any(any(c.get('component_id')=='FOODON:03305103' for c in r.get('components',[])) for r in rows.values()),label
 assert not any(any(t in e for t in target_ids) for e in (intermediate if label=='intermediate' else combined)['new_partonomy_violations'])
for p,h in live_inputs.items(): assert sha((B/p).read_bytes())==h,'Concurrent proposal mutation'
for f,h in inputs.items(): assert sha((O/f).read_bytes())==h,'Concurrent media mutation'
out={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS' if not combined['new_partonomy_violations'] else 'MEDIA_FOLLOWON_PASS_COMBINED_OTHER_FAILURES','scientific_review':False,'reviewed_inputs':inputs,'counts':{'decisions':len(D),'evidence':len(E),'proposals':len(P),'cases_with_proposals':sum(bool(d['proposal_ids']) for d in D)},'catalog_scope':'Both maintained ingredient directories, explicit globs including ignored files; every old owner path is removed before its exact proposed after bytes are inserted at the destination path. No old identifier catalog ghosts are retained. In-memory validation only.','catalog_inputs_capture':{'path':str((F/'catalog-inputs.json').relative_to(B)),'sha256':sha((F/'catalog-inputs.json').read_bytes())},'baseline_catalog_size':len(catalog),'baseline_partonomy_violations':sorted(baseline_violations),'checks':['All60 original case/source/occurrence identities preserved','All213 predecessor evidence entries unchanged','Every482 capture and45 after hash verified','Every frozen owner before hash verified','All45 exact after YAMLs pass schema','Full path-based substitution closes both cooked-meat dependent references','No maintained data changes'],'preserved_133_reproduction':prior_receipt,'preserved_133_plus_two_media_followons':intermediate,'current_combined_inputs':live_inputs,'current_combined':combined,'validation_scope_correction':'Earlier media-integrity.py called validate_component_partonomy([record]) once per proposal. Its PASS did not establish combined full-catalog substitution closure; earlier full-catalog wording was too broad. Per-record validation cannot test references from unchanged dependent owners. The original receipt and script are preserved. This receipt performs path-based substitution across the complete catalog, and the coordinator final canonical full-substitution gate remains authoritative. Structural closure does not establish scientific approval or release approval.'}
(F/'validation.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['preserved_133_reproduction','preserved_133_plus_two_media_followons','current_combined','baseline_partonomy_violations']},indent=2))
for name,r in [('prior133',prior_receipt),('prior_plus_2',intermediate),('current',combined)]:print(name,r['proposal_count'],r['new_partonomy_violations'])
