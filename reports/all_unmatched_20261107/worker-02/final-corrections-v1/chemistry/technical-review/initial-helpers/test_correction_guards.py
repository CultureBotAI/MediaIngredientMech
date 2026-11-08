"""Private controls for claim binding, native failures, and publication scope."""
from copy import deepcopy
import importlib.util,json,os
from pathlib import Path
import pytest

HERE=Path(__file__).resolve().parent
def module(name):
 spec=importlib.util.spec_from_file_location(name,HERE/(name+'.py'));m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
types=module('correct_evidence_types');validation=module('validate_selection')
assembly=module('assemble_selection')
from mediaingredientmech.curate.publication_guard import FrozenFile
from mediaingredientmech.ingredient_bundle_refresh import publish_new_files
from mediaingredientmech.validation.write_validated import write_validated_ingredient,ValidationFailedError
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy

@pytest.fixture
def evidence_record():
 return {'identifier':'kgmicrobe.ingredient:guard_fixture','preferred_term':'Guard fixture',
  'mapping_status':'MAPPED','ingredient_type':'STOCK_SOLUTION',
  'ontology_mapping':{'ontology_id':'kgmicrobe.ingredient:guard_fixture','ontology_label':'Guard fixture','ontology_source':'kgmicrobe.ingredient','mapping_quality':'FALLBACK_REGISTRY','evidence':[{'evidence_type':'MANUAL_CURATION','source':'agent source interpretation','notes':'Source-qualified preparation; carrier unknown.'}]},
  'components':[{'component_name':'unknown source material','reference_scope':'UNMAPPED'}],
  'component_assertion':{'method':'CURATED_INTERPRETATION','completeness':'UNKNOWN','evidence':[{'evidence_type':'MANUAL_CURATION','source':'component source'}]},
  'curation_history':[{'timestamp':'2026-11-08T08:00:00+00:00','curator':'worker02 fixture','action':'CREATED','llm_assisted':True}]}
def edit(record):
 return {'evidence_index':0,'expected_complete_entry':deepcopy(record['ontology_mapping']['evidence'][0]),'new_type':'LLM_SUGGESTION','classification':'new_agent_record','basis':'Exact agent-authored applicability judgment absent from baseline','original_flag_indices':[0]}

def test_exact_claim_preserves_component_enum_and_quality(evidence_record):
 result,proof=types.apply_exact_edits(evidence_record,None,[edit(evidence_record)])
 assert result['component_assertion']==evidence_record['component_assertion']
 assert result['ontology_mapping']['mapping_quality']=='FALLBACK_REGISTRY'
 expected=deepcopy(evidence_record);expected['ontology_mapping']['evidence'][0]['evidence_type']='LLM_SUGGESTION'
 assert result==expected and proof[0]['before']['notes']==proof[0]['after']['notes']

def test_unchanged_historical_human_object_refused(evidence_record):
 with pytest.raises(ValueError,match='Historical unchanged'):types.apply_exact_edits(evidence_record,deepcopy(evidence_record),[edit(evidence_record)])

def test_same_source_but_different_historical_claim_is_not_misclassified(evidence_record):
 baseline=deepcopy(evidence_record);baseline['ontology_mapping']['evidence'][0]['notes']='Historical human evidence for a different claim'
 result,_=types.apply_exact_edits(evidence_record,baseline,[edit(evidence_record)])
 assert result['ontology_mapping']['evidence'][0]['evidence_type']=='LLM_SUGGESTION'
 assert baseline['ontology_mapping']['evidence'][0]['evidence_type']=='MANUAL_CURATION'

def test_mutated_full_entry_refused(evidence_record):
 plan=edit(evidence_record);evidence_record['ontology_mapping']['evidence'][0]['notes']+=' altered'
 with pytest.raises(ValueError,match='Complete evidence'):types.apply_exact_edits(evidence_record,None,[plan])

def test_duplicate_evidence_pointer_refused(evidence_record):
 with pytest.raises(ValueError,match='Duplicate'):types.apply_exact_edits(evidence_record,None,[edit(evidence_record),edit(evidence_record)])

@pytest.mark.parametrize('key,value',[('new_type','MANUAL_REVIEW'),('classification','ambiguous_needs_review'),('basis',''),('original_flag_indices',[])])
def test_missing_or_inappropriate_provenance_refused(evidence_record,key,value):
 change=edit(evidence_record);change[key]=value
 with pytest.raises(ValueError):types.apply_exact_edits(evidence_record,None,[change])

def test_source_or_hydrate_change_detected_by_frozen_input(tmp_path):
 p=tmp_path/'source';p.write_bytes(b'six waters');held=FrozenFile.capture(p);p.write_bytes(b'seven waters')
 with pytest.raises(ValueError,match='changed'):held.verify()

@pytest.mark.parametrize('kind',['symlink','hardlink'])
def test_frozen_input_alias_refused(tmp_path,kind):
 p=tmp_path/'source';p.write_bytes(b'original');alias=tmp_path/'alias'
 if kind=='symlink':alias.symlink_to(p)
 else:os.link(p,alias)
 with pytest.raises(ValueError):FrozenFile.capture(alias)

def test_existing_output_not_overwritten(tmp_path):
 p=tmp_path/'existing';p.write_bytes(b'preserved')
 with pytest.raises((ValueError,FileExistsError)):publish_new_files([(p,b'changed')],lambda:None)
 assert p.read_bytes()==b'preserved'

def test_output_parent_alias_refused(tmp_path):
 real=tmp_path/'real';real.mkdir();alias=tmp_path/'alias';alias.symlink_to(real,target_is_directory=True)
 with pytest.raises(ValueError):publish_new_files([(alias/'new',b'new')],lambda:None)
 assert not (real/'new').exists()

def test_stale_snapshot_refuses_publication(tmp_path):
 p=tmp_path/'input';p.write_bytes(b'old');held=FrozenFile.capture(p);p.write_bytes(b'new');out=tmp_path/'out'
 with pytest.raises(ValueError):publish_new_files([(out,b'candidate')],held.verify)
 assert not out.exists()

def test_duplicate_output_paths_refused(tmp_path):
 out=tmp_path/'out'
 with pytest.raises(ValueError):publish_new_files([(out,b'one'),(out,b'two')],lambda:None)
 assert not out.exists()

def test_native_unknown_field_refused_before_write(evidence_record,tmp_path):
 evidence_record['not_a_native_slot']='invalid';out=tmp_path/'invalid.yaml'
 with pytest.raises(ValidationFailedError):write_validated_ingredient(evidence_record,out)
 assert not out.exists()

def test_native_wrong_component_scope_refused(evidence_record,tmp_path):
 evidence_record['components'][0]['reference_scope']='GLOBAL_ALIAS';out=tmp_path/'invalid.yaml'
 with pytest.raises(ValidationFailedError):write_validated_ingredient(evidence_record,out)
 assert not out.exists()

def test_native_partonomy_missing_catalog_target(evidence_record):
 evidence_record['components'][0].update(reference_scope='MIM_CATALOG',component_id='CHEBI:999999999')
 assert validate_component_partonomy([evidence_record])

def test_output_outside_private_root_refused(tmp_path):
 root=tmp_path/'private';root.mkdir()
 with pytest.raises(ValueError):validation.confined(tmp_path/'elsewhere',root)

def test_proposal_duplicate_owner_refused(evidence_record,tmp_path,monkeypatch):
 monkeypatch.setattr(validation,'A',tmp_path);payload=tmp_path/'candidate.yaml';write_validated_ingredient(evidence_record,payload)
 proposal={'proposal_id':'p1','owner_path':'data/ingredients/mapped/New.yaml','kind':'new_owner','before_sha256':None,'after_capture':{'root':'artifact','path':'candidate.yaml','sha256':validation.sha(payload)}}
 second=deepcopy(proposal);second['proposal_id']='p2'
 with pytest.raises(ValueError,match='Duplicate'):validation.verify_proposals([proposal,second],{}, {})

def test_stale_owner_preimage_refused(evidence_record,tmp_path,monkeypatch):
 monkeypatch.setattr(validation,'A',tmp_path);owner='data/ingredients/mapped/Old.yaml'
 proposal={'proposal_id':'p','owner_path':owner,'kind':'edit_existing_owner','before_sha256':'0'*64,'after_capture':{}}
 with pytest.raises(ValueError,match='Stale authentic'):validation.verify_proposals([proposal],{owner:evidence_record},{owner:'1'*64})

def test_changed_payload_hash_refused(evidence_record,tmp_path,monkeypatch):
 monkeypatch.setattr(validation,'A',tmp_path);payload=tmp_path/'candidate.yaml';write_validated_ingredient(evidence_record,payload)
 proposal={'proposal_id':'p','owner_path':'data/ingredients/mapped/New.yaml','kind':'new_owner','before_sha256':None,'after_capture':{'root':'artifact','path':'candidate.yaml','sha256':'0'*64}}
 with pytest.raises(ValueError,match='Stale payload'):validation.verify_proposals([proposal],{}, {})

@pytest.mark.parametrize('indices',[list(range(57)),list(range(58))+[0],list(range(57))+[56]])
def test_omitted_duplicate_or_substituted_flag_refused(indices):
 with pytest.raises(ValueError):types.require_complete_flags([{'original_flag_indices':indices}])

@pytest.mark.parametrize('key,value',[('case_id','different'),('occurrence_ids',[]),('source',{'raw_source_label':'invented'})])
def test_frozen_case_scientific_scope_cannot_change(key,value):
 old={'case_id':'case','case_input_sha256':'0'*64,'source':{'raw_source_label':'literal'},'occurrence_ids':['occurrence']};new=deepcopy(old);new[key]=value
 with pytest.raises(ValueError,match='Frozen source'):assembly.verify_case_core(old,new)

def test_duplicate_case_rows_refused():
 with pytest.raises(ValueError,match='Duplicate'):assembly.unique([{'case_id':'c'},{'case_id':'c'}],'case_id')

def test_undeclared_conflicting_science_refused():
 old={'case_id':'case','case_input_sha256':'0'*64,'source':{'raw_source_label':'literal'},'occurrence_ids':['o'],'reasoning':'old'};a=deepcopy(old);b=deepcopy(old);a['reasoning']='one';b['reasoning']='two'
 with pytest.raises(ValueError,match='Scientific prose conflict'):assembly.compose_case(old,[('author-a',a),('author-b',b)])
