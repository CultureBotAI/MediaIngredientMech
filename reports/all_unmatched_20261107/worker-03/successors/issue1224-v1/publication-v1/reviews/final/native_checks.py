from pathlib import Path
import sys,json,hashlib,importlib.util,collections
R=Path.cwd();W=R/'reports/all_unmatched_20261107/worker-03';S=W/'successors/issue1224-v1';D=S/'publication-v1';O=R/'.temp/w03-oxoid-successor-publication-v1/review';Q=R.parents[2]/'queue/preliminary-v5'
sys.path.insert(0,str(R/'src'));import yaml
from mediaingredientmech.validation.write_validated import validate_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
from mediaingredientmech.synonym_policy import is_resolving_synonym
spec=importlib.util.spec_from_file_location('frozen_auditor',W/'tools/audit_worker_outcomes_v1.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
audit=mod.audit(Q/'shards/shard-03.json',D/'decisions.json',D/'evidence.json',D/'proposals.json',W,Q,mim_root=R)
with (O/'native-structural-audit.json').open('x') as f:json.dump(audit,f,indent=2);f.write('\n')
p=S/'candidate/reinforced_clostridial_medium_oxoid_cm0149.yaml';d=yaml.safe_load(p.read_text());fs=sorted((R/'data/ingredients/mapped').glob('*.yaml'))+sorted((R/'data/ingredients/unmapped').glob('*.yaml'));bs=[yaml.safe_load(x.read_text()) for x in fs]
errs=[str(x) for x in validate_ingredient(d)];prior=[str(x) for x in validate_component_partonomy(bs)];after=[str(x) for x in validate_component_partonomy(bs+[d])];new=sorted(set(after)-set(prior));assert not errs and not new
# Ignored-independent bounded search. Recursive files are inventoried separately from native direct-child owners.
roots=[R/'data/ingredients',R/'data/curated'];scanned=[];matches=[]
for root in roots:
 for f in sorted(root.rglob('*')):
  if not f.is_file() or f.is_symlink():continue
  if f.suffix.lower() not in ['.yaml','.yml','.json','.tsv','.csv']:continue
  raw=f.read_bytes();scanned.append({'path':str(f.relative_to(R)),'sha256':hashlib.sha256(raw).hexdigest()})
  text=raw.decode('utf-8');terms=[t for t in ['reinforced_clostridial_medium_oxoid_cm0149','CM0149','CM149','Reinforced clostridial','Reinforced Clostridial','Dehydrated RCM'] if t.casefold() in text.casefold()]
  if terms:matches.append({'path':str(f.relative_to(R)),'terms':terms,'native_owner':f in fs})
ident=d['identifier'];holders=[str(f.relative_to(R)) for f,b in zip(fs,bs) if b.get('identifier')==ident and b.get('mapping_status')!='REJECTED'];assert not holders
native_lexical=[{'path':str(f.relative_to(R)),'identifier':b.get('identifier'),'label':b.get('preferred_term'),'synonyms':b.get('synonyms',[])} for f,b in zip(fs,bs) if 'reinforced clostridial' in json.dumps(b).casefold() or 'dehydrated rcm' in json.dumps(b).casefold()]
old=R.parents[2]/'integration/final-same-target-reconciliation-v2/candidates/NEW-OXOID-CM0149/reinforced_clostridial_medium_oxoid_cm0149.yaml';od=yaml.safe_load(old.read_text());assert d['curation_history'][:-1]==od['curation_history'];changed=[]
for i,(a,b) in enumerate(zip(od['ontology_mapping']['evidence'],d['ontology_mapping']['evidence'])):
 changed.append({'entry':i,'old_type':a['evidence_type'],'new_type':b['evidence_type'],'source_unchanged':a['source']==b['source']})
assert all(x['old_type']=='MANUAL_CURATION' and x['new_type']=='LLM_SUGGESTION' and x['source_unchanged'] for x in changed)
result={'native_schema_errors':errs,'native_schema_status':'PASS','baseline_owner_count':len(bs),'baseline_partonomy_violations':prior,'overlay_partonomy_violations':after,'new_partonomy_violations':new,'partonomy_note':'No component assertions on this deliberately composition-unspecified product: zero new violations is not a chemistry proof. Existing baseline findings remain.','active_identifier_holders':holders,'new_path_absent':not (R/'data/ingredients/mapped/reinforced_clostridial_medium_oxoid_cm0149.yaml').exists(),'resolving_synonyms':[s for s in d['synonyms'] if is_resolving_synonym(s)],'native_lexical_owner_contexts':native_lexical,'search_boundary':'Every file with YAML/YML/JSON/TSV/CSV extension recursively under data/ingredients and data/curated; pathlib.rglob includes ignored and hidden. Native owners are only direct-child mapped/unmapped YAML files. No credential, unrelated private/history root search and no global absence claim.','search_scanned_files':scanned,'search_matches':matches,'coordinator_pre1226_payload_sha256':hashlib.sha256(old.read_bytes()).hexdigest(),'coordinator_history_prefix_preserved':True,'issue1226_changes':changed,'maintained_data_written':False,'whole_owner_role_export_approval':False,'scientific_status':'Requires separate source assessment; checks alone do not establish it.'}
with (O/'native-candidate-checks.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps({'native_structural':audit['structural_accounting'],'cases':audit['accounted_case_count'],'proposals':audit['proposal_count'],'evidence':audit['evidence_count'],'review_counts':audit['independent_review_status_counts'],'schema_errors':errs,'new_partonomy_violations':new,'scanned_files':len(scanned),'active_identifier_holders':holders,'prefix':True}))
