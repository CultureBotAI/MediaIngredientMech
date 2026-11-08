from copy import deepcopy
import importlib.util,json
from pathlib import Path
import pytest,yaml
p=Path(__file__).with_name('build_successor_v2.py');s=importlib.util.spec_from_file_location('followup',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
D=json.loads((m.S/'decisions.json').read_text())['decisions'];P=json.loads((m.S/'proposals.json').read_text())['proposals'];OLD=yaml.safe_load((m.A/next(p['after_capture']['path'] for p in P if p['proposal_id']==m.PID)).read_text())
def test_exact_payload_positive_preserves_all_chemistry():
 after=m.correct_payload(OLD);m.validate_payload_delta(OLD,after)
 assert after['solution_type']=='OTHER' and after['components']==OLD['components'] and after['component_assertion']==OLD['component_assertion']
 assert after['curation_history'][:-1]==OLD['curation_history']
def test_exact_case_positive_and_shared_scope():
 for i in m.AFFECTED:m.validate_case_delta(D[i],m.correct_case(D[i],i),i)
 assert len(D[114]['occurrence_ids'])==6 and len(D[118]['occurrence_ids'])==1
 for i in [114,118]:assert 'shared proposal covers seven occurrences' in m.correct_case(D[i],i)['reasoning']
 assert m.sha(m.A/next(p['after_capture']['path'] for p in P if p['proposal_id']==m.ACID))==m.ACID_SHA
@pytest.mark.parametrize('mutation',[
 lambda x:x['components'][0].update(concentration_value='1'),
 lambda x:x['components'][0].update(concentration_unit='G_PER_L'),
 lambda x:x['components'][0].update(component_name='Resazurin'),
 lambda x:x['components'][0].update(reference_scope='MIM_CATALOG',component_id='CHEBI:8806'),
 lambda x:x['component_assertion'].update(completeness='COMPLETE'),
 lambda x:x.update(identifier='kgmicrobe.ingredient:other'),
 lambda x:x['ontology_mapping']['evidence'][0].update(evidence_type='MANUAL_CURATION'),
 lambda x:x['curation_history'][0].update(changes='rewritten history'),
 lambda x:x['curation_history'][-1].update(llm_assisted=False),
 lambda x:x['curation_history'][-1].update(curator='human reviewer'),
 lambda x:x['curation_history'].append(deepcopy(x['curation_history'][-1])),
 lambda x:x.update(solution_type='MINERAL_STOCK'),
])
def test_payload_rejects_unapproved_or_untruthful_change(mutation):
 after=m.correct_payload(OLD);mutation(after)
 with pytest.raises(ValueError):m.validate_payload_delta(OLD,after)
@pytest.mark.parametrize('mutation',[
 lambda x:x['occurrence_ids'].pop(),
 lambda x:x['occurrence_ids'].reverse(),
 lambda x:x['source'].update(raw_source_label='10 M H2SO4'),
 lambda x:x.update(case_input_sha256='0'*64),
 lambda x:x.update(missing_requirement='owner hold removed'),
 lambda x:x.update(reasoning='All seven occurrences are in this individual case.'),
 lambda x:x.update(independent_review={'status':'complete','evidence_ids':['old-proof']}),
])
def test_case_rejects_frozen_scope_hold_or_old_approval_changes(mutation):
 after=m.correct_case(D[114],114);mutation(after)
 with pytest.raises(ValueError):m.validate_case_delta(D[114],after,114)
def test_unaffected_case_must_remain_exact():
 after=deepcopy(D[0]);after['reasoning']+=' extra'
 with pytest.raises(ValueError):m.validate_case_delta(D[0],after,0)
def test_changed_predecessor_pin_refused():
 with pytest.raises(ValueError):m.require_pin(b'changed',m.MANIFEST_SHA)
def test_wrong_stock_preimage_refused():
 wrong=deepcopy(OLD);wrong['component_assertion']['completeness']='COMPLETE'
 with pytest.raises(ValueError):m.correct_payload(wrong)
def test_output_existing_traversal_symlink_refused(tmp_path):
 existing=tmp_path/'existing';existing.mkdir()
 with pytest.raises(FileExistsError):m.require_output(existing,tmp_path)
 with pytest.raises(ValueError):m.require_output(tmp_path/'inside'/'..'/'escape',tmp_path)
 link=tmp_path/'link';link.symlink_to(existing,target_is_directory=True)
 with pytest.raises((ValueError,OSError)):m.require_output(link/'output',tmp_path)
def test_stale_native_input_refuses_publication(tmp_path):
 f=tmp_path/'input';f.write_text('before');held=m.FrozenFile.capture(f);f.write_text('after');target=tmp_path/'output'
 with pytest.raises((ValueError,OSError)):m.publish_new_files([(target,b'value')],held.verify)
 assert not target.exists()
def test_native_writer_negative_unknown_field_no_output(tmp_path):
 from mediaingredientmech.validation.write_validated import ValidationFailedError
 bad=m.correct_payload(OLD);bad['extra_unsupported_followup_field']=True;target=tmp_path/'bad.yaml'
 with pytest.raises(ValidationFailedError):m.write_validated_ingredient(bad,target)
 assert not target.exists()
def test_native_publisher_existing_output_preserved(tmp_path):
 f=tmp_path/'existing';f.write_bytes(b'original')
 with pytest.raises((ValueError,OSError)):m.publish_new_files([(f,b'bad')],lambda:None)
 assert f.read_bytes()==b'original'
