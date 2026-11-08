"""Private native failure probes; all mutations are in-memory copies only."""
from pathlib import Path
import sys,copy,json
R=Path.cwd();sys.path.insert(0,str(R/'src'));import yaml
from mediaingredientmech.validation.write_validated import validate_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
from mediaingredientmech.synonym_policy import is_resolving_synonym
p=R/'reports/all_unmatched_20261107/worker-03/successors/issue1224-v1/candidate/reinforced_clostridial_medium_oxoid_cm0149.yaml';d=yaml.safe_load(p.read_text());rows=[]
bad=copy.deepcopy(d);bad['invented_gate_bypass']=True;err=[str(x) for x in validate_ingredient(bad)];assert err;rows.append({'control':'unknown schema slot rejected','observed_errors':err})
bad=copy.deepcopy(d);bad['ontology_mapping']['evidence'][0]['evidence_type']='RECIPE_SOURCE';err=[str(x) for x in validate_ingredient(bad)];assert err;rows.append({'control':'component-only evidence type rejected in mapping evidence','observed_errors':err})
bad=copy.deepcopy(d);bad['components']=[{'component_name':'Hypothetical part','component_id':'CHEBI:15377','reference_scope':'UNMAPPED'}];err=[str(x) for x in validate_component_partonomy([bad])];assert any('UNMAPPED_WITH_ID' in x for x in err) and any('MISSING_ASSERTION' in x for x in err);rows.append({'control':'component missing assertion and conflicting UNMAPPED ID rejected','observed_errors':err})
bad=copy.deepcopy(d);bad['components']=[{'component_name':'Hypothetical part','component_id':'CHEBI:15377','reference_scope':'MIM_CATALOG'}];err=[str(x) for x in validate_component_partonomy([bad])];assert any('UNRESOLVED_MIM_REFERENCE' in x for x in err);rows.append({'control':'unresolved local component reference rejected in isolated fixture','observed_errors':err})
a=copy.deepcopy(d['synonyms'][0]);assert is_resolving_synonym(a);a['synonym_type']='REJECTED_LABEL';assert not is_resolving_synonym(a);rows.append({'control':'native synonym policy distinguishes current resolving catalog alias from provenance-only rejected label','pass':True})
print(json.dumps({'status':'PASS','controls':rows,'count':len(rows),'writes':'none; in-memory fixtures only','limitation':'Failure controls establish structural enforcement only; no primary evidence or chemistry approval.'},indent=2))
