"""Narrow changed-record validation plus complete read-only partonomy overlay."""
from pathlib import Path
import copy,datetime,hashlib,json,sys,yaml,collections
from mediaingredientmech.validation.write_validated import validate_ingredient,write_validated_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
from mediaingredientmech.synonym_policy import is_resolving_synonym,preferred_term_owners
from mediaingredientmech.sssom_grading import predicate_for,confidence_for,justification_for
R=Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v4';P=R/'.temp/all-unmatched-worker-10/successor-v4';V=S/'validation';scratch=P/'native-scratch';scratch.mkdir()
load=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(path,value):
 with path.open('x') as f:json.dump(value,f,indent=2,ensure_ascii=False);f.write('\n')
oldprops=load(A/'successor-v3/proposals.json')['proposals'];props=load(S/'author-core/proposals.json')['proposals'];pid='sv1-buffers-carbonate_co2_nominal4percent_togo_m202'
old=next(x for x in oldprops if x['proposal_id']==pid);new=next(x for x in props if x['proposal_id']==pid);before=yaml.safe_load((A/old['after_capture']['path']).read_text());after=yaml.safe_load((A/new['after_capture']['path']).read_text());errors=validate_ingredient(after);assert not errors
dest=scratch/'roundtrip.yaml';assert not dest.exists();write_validated_ingredient(after,dest);assert yaml.safe_load(dest.read_text())==after;assert sha(dest)==new['after_capture']['sha256']
bad=copy.deepcopy(after);bad['component_assertion']['completeness']='UNSUPPORTED_ENUM';badpath=scratch/'invalid-must-not-exist.yaml'
try:write_validated_ingredient(bad,badpath)
except Exception as exc:negative={'error':type(exc).__name__+': '+str(exc),'destination_absent':not badpath.exists()}
else:raise AssertionError('native writer accepted invalid enum')
assert negative['destination_absent']
def projection(record):
 q=record['ontology_mapping']['mapping_quality'];return {'identifier':record['identifier'],'preferred_term':record['preferred_term'],'mapping_status':record['mapping_status'],'ontology_id':record['ontology_mapping']['ontology_id'],'ontology_label':record['ontology_mapping']['ontology_label'],'quality':q,'predicate':predicate_for(q),'confidence':str(confidence_for(q)),'justification':justification_for(q),'synonyms':[{'complete_row':x,'native_resolving':is_resolving_synonym(x)} for x in record.get('synonyms',[])]}
assert projection(before)==projection(after)
baseline={str(p.relative_to(R)):yaml.safe_load(p.read_text()) for p in sorted((R/'data/ingredients').rglob('*.yaml'))}
save(V/'catalog-hashes.json',{'files':[{'path':path,'sha256':sha(R/path)} for path in baseline]})
def overlay(proposals):
 result=copy.deepcopy(baseline)
 for p in proposals:
  path=A/p['after_capture']['path'];assert sha(path)==p['after_capture']['sha256']
  if p['kind']=='edit_existing_owner':assert sha(R/p['owner_path'])==p['before_sha256'];result.pop(p['owner_path'])
  else:assert p['before_sha256'] is None and not (R/p['owner_path']).exists()
  dest=p.get('destination_path',p['owner_path']);assert dest not in result;result[dest]=yaml.safe_load(path.read_text())
 return result
overlays={'predecessor':overlay(oldprops),'successor':overlay(props)}
partonomy={k:{'records':len(v),'violations':[str(x) for x in validate_component_partonomy(list(v.values()))]} for k,v in overlays.items()};assert all(not x['violations'] for x in partonomy.values())
def identities(records):return {p:{'identifier':d['identifier'],'preferred_term':d['preferred_term'],'mapping_status':d['mapping_status'],'synonyms':d.get('synonyms',[])} for p,d in records.items()}
assert identities(overlays['predecessor'])==identities(overlays['successor'])
def alias_projection(records):
 mapped={p:d for p,d in records.items() if '/mapped/' in p};owners=preferred_term_owners(mapped)
 return {'preferred_owners':{k:sorted(v) for k,v in owners.items()},'resolving_synonyms':{p:[s for s in d.get('synonyms',[]) if is_resolving_synonym(s)] for p,d in mapped.items()}}
assert alias_projection(overlays['predecessor'])==alias_projection(overlays['successor'])
save(V/'narrow-native.json',{'at':now(),'status':'PASS','predecessor':old['after_capture'],'successor':new['after_capture'],'closed_schema_errors':[],'guarded_scratch_roundtrip_byte_exact':True,'guarded_roundtrip_sha256':sha(dest),'invalid_enum_negative':negative,'partonomy':partonomy,'all_selected_payloads':len(props),'maintained_catalog_records':len(baseline),'exact_owner_preimage_hashes_checked':True,'all_identifiers_labels_statuses_aliases_unchanged':True,'native_alias_projection_equal':True,'native_mapping_projection_before':projection(before),'native_mapping_projection_after':projection(after),'no_export_produced':True,'whole_owner_source_role_export_approval':False,'scope':'One changed record; complete in-memory predecessor/successor partonomy and identity/alias projections. No maintained write, rebuild or new gate.'})
print(json.dumps({'status':'PASS','partonomy':partonomy,'payloads':len(props),'guarded_roundtrip_byte_exact':True},indent=2))
