from copy import deepcopy
import importlib.util,json
from pathlib import Path
import pytest,yaml
p=Path(__file__).with_name('build_successor_v2.py');s=importlib.util.spec_from_file_location('seven_builder',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
L=json.loads((m.R/'context/hash-ledger.json').read_text());ROWS={x['proposal_id']:x for x in L['rows']};D=json.loads((m.S/'decisions.json').read_text())['decisions'];P=json.loads((m.S/'proposals.json').read_text())['proposals']
OLD={pid:yaml.safe_load(Path(row['payload']['path']).read_text()) for pid,row in ROWS.items()}
@pytest.mark.parametrize('pid',m.TARGET_IDS)
def test_actual_complete_candidate_preserves_every_unrequested_field(pid):
 row=ROWS[pid];old=OLD[pid];path=m.R/'review-input-v1/after'/(pid+'.yaml');new=yaml.safe_load(path.read_text());m.validate_payload_delta(old,new,pid)
 assert set(new)==set(old)
 assert {k:v for k,v in old.items() if k not in ['solution_type','curation_history']}=={k:v for k,v in new.items() if k not in ['solution_type','curation_history']}
 assert new['curation_history'][:-1]==old['curation_history'] and len(new['curation_history'])==row['history_length']+1
 assert new['curation_history'][-1]['llm_assisted'] is True
@pytest.mark.parametrize('field',[k for k in OLD[m.TARGET_IDS[0]] if k not in ['solution_type','curation_history']])
def test_any_unrequested_field_mutation_is_rejected(field):
 pid=m.TARGET_IDS[0];new=m.correct_payload(OLD[pid],ROWS[pid]);new[field]={'unrequested_mutation':True}
 with pytest.raises(ValueError):m.validate_payload_delta(OLD[pid],new,pid)
@pytest.mark.parametrize('kind',['quantity','component_reference','completeness','history_prefix','llm_false','human_author','extra_history','missing_history','same_type','wrong_type','future_scope'])
def test_scientific_and_provenance_negative_paths(kind):
 pid=m.TARGET_IDS[0];new=m.correct_payload(OLD[pid],ROWS[pid])
 if kind=='quantity':new['components'][0]['concentration_value']='999'
 elif kind=='component_reference':new['components'][0]['component_id']='CHEBI:15377'
 elif kind=='completeness':new['component_assertion']['completeness']='UNKNOWN' if new['component_assertion']['completeness']!='UNKNOWN' else 'COMPLETE'
 elif kind=='history_prefix':new['curation_history'][0]['changes']='rewrite'
 elif kind=='llm_false':new['curation_history'][-1]['llm_assisted']=False
 elif kind=='human_author':new['curation_history'][-1]['curator']='human reviewer'
 elif kind=='extra_history':new['curation_history'].append(deepcopy(new['curation_history'][-1]))
 elif kind=='missing_history':new['curation_history'].pop()
 elif kind=='same_type':new['solution_type']='MINERAL_STOCK'
 elif kind=='wrong_type':new['solution_type']='BUFFER_SOLUTION'
 else:new['curation_history'][-1]['changes']='All source owners and exports approved'
 with pytest.raises(ValueError):m.validate_payload_delta(OLD[pid],new,pid)
def test_wrong_preimage_or_eighth_target_refused():
 pid=m.TARGET_IDS[0];bad=deepcopy(ROWS[pid]);bad['history_length']+=1
 with pytest.raises(ValueError):m.correct_payload(OLD[pid],bad)
 bad=deepcopy(ROWS[pid]);bad['proposal_id']='a2-proposal-dsmz40-mixed-cde'
 with pytest.raises(ValueError):m.correct_payload(OLD[pid],bad)
@pytest.mark.parametrize('field',['occurrence_ids','source','case_input_sha256','reasoning','applicability','missing_requirement'])
def test_case58_source_and_hold_changes_refused(field):
 new=m.pending_case(D[58]);new[field]='unrequested'
 with pytest.raises(ValueError):m.validate_case_delta(D[58],new,58)
def test_case58_all24_and188_case_science_preserved():
 after=json.loads((m.R/'review-input-v1/decisions.json').read_text())['decisions'];assert len(after)==188 and len(after[58]['occurrence_ids'])==24
 for i,(old,new) in enumerate(zip(D,after,strict=True)):m.validate_case_delta(old,new,i)
 assert sum(len(d['occurrence_ids']) for d in after)==322
 copies=json.loads((m.R/'context/frozen-recipe-copies.json').read_text());assert len(copies)==24
 for c in copies:assert m.sha(Path(c['original_path']))==m.sha(m.W/c['copy_path'])==c['sha256']
def test117_selection_exact110_untouched_and_dsmz40():
 after=json.loads((m.R/'review-input-v1/proposals.json').read_text())['proposals'];caps={p['proposal_id']:p['after_capture'] for p in after if p['proposal_id'] in m.TARGET_IDS};m.validate_proposal_delta(P,after,caps)
 count=0;boundary=0
 for old,new in zip(P,after,strict=True):
  assert m.sha(m.A/new['after_capture']['path'])==new['after_capture']['sha256']
  if new['proposal_id'] not in m.TARGET_IDS:
   assert new==old;assert (m.A/new['after_capture']['path']).read_bytes()==(m.A/old['after_capture']['path']).read_bytes();count+=1
   if 'dsmz40' in new['proposal_id']:boundary+=1
 assert count==110 and boundary>=1
@pytest.mark.parametrize('mutation',['omit','duplicate','reverse','extra_target','non_target_change'])
def test_bad_proposal_selection_refused(mutation):
 after=deepcopy(P);caps={p['proposal_id']:p['after_capture'] for p in after if p['proposal_id'] in m.TARGET_IDS}
 if mutation=='omit':after.pop()
 elif mutation=='duplicate':after[-1]=deepcopy(after[0])
 elif mutation=='reverse':after.reverse()
 elif mutation=='extra_target':caps['dsmz40']={}
 else:after[0]['owner_path']='data/ingredients/mapped/changed.yaml'
 with pytest.raises(ValueError):m.validate_proposal_delta(P,after,caps)
def test_prior_evidence_raw_objects_preserved():
 old=(m.S/'evidence.json').read_bytes();new=(m.R/'review-input-v1/evidence.json').read_bytes();a=m.raw_array_objects(old,'evidence');b=m.raw_array_objects(new,'evidence');assert len(a)==1824 and b[:1824]==a and len(b)==1826
def test_native_invalid_field_enum_and_partonomy(tmp_path):
 from mediaingredientmech.validation.write_validated import ValidationFailedError
 from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
 pid=m.TARGET_IDS[0];valid=m.correct_payload(OLD[pid],ROWS[pid])
 for key,value in [('unknown_probe',True),('solution_type','UNDEFINED_FAKE')]:
  bad=deepcopy(valid);bad[key]=value;target=tmp_path/(key+'.yaml')
  with pytest.raises(ValidationFailedError):m.write_validated_ingredient(bad,target)
  assert not target.exists()
 bad=deepcopy(valid);bad['components'][0].update(reference_scope='UNMAPPED',component_id='CHEBI:15377')
 assert any('UNMAPPED_WITH_ID' in str(v) for v in validate_component_partonomy([bad]))
def test_native_stale_alias_existing_outputs(tmp_path):
 p=tmp_path/'source';p.write_bytes(b'before');f=m.FrozenFile.capture(p);p.write_bytes(b'after');out=tmp_path/'out'
 with pytest.raises((ValueError,OSError)):m.publish_new_files([(out,b'candidate')],f.verify)
 assert not out.exists()
 p.write_bytes(b'kept')
 with pytest.raises((ValueError,OSError)):m.publish_new_files([(p,b'replaced')],lambda:None)
 assert p.read_bytes()==b'kept'
 symlink=tmp_path/'alias';symlink.symlink_to(p)
 with pytest.raises((ValueError,OSError)):m.FrozenFile.capture(symlink)
 hard=tmp_path/'hard';hard.hardlink_to(p)
 with pytest.raises((ValueError,OSError)):m.FrozenFile.capture(hard)
def test_output_scope_and_existing_directory_refused(tmp_path):
 x=tmp_path/'exists';x.mkdir()
 with pytest.raises(FileExistsError):m.require_output(x,tmp_path)
 with pytest.raises(ValueError):m.require_output(tmp_path/'a'/'..'/'escape',tmp_path)
 link=tmp_path/'alias';link.symlink_to(x,target_is_directory=True)
 with pytest.raises((ValueError,OSError)):m.require_output(link/'out',tmp_path)
 with pytest.raises(ValueError):m.require_pin(b'altered',m.LEDGER_SHA)
