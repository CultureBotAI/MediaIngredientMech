"""Independent native roundtrips and multi-output/copied-source negative controls."""
from pathlib import Path
import importlib.util,json,hashlib
import pytest,yaml
R=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location('seven_review_builder',R/'build_successor_v2.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
@pytest.mark.parametrize('pid',m.TARGET_IDS)
def test_each_actual_new_payload_native_writer_roundtrip_and_publication(pid,tmp_path):
    source=m.FrozenFile.capture(R/'review-input-v1/after'/(pid+'.yaml'));value=yaml.safe_load(source.content)
    stage=tmp_path/'stage.yaml';m.write_validated_ingredient(value,stage)
    assert yaml.safe_load(stage.read_bytes())==value
    target=tmp_path/'published.yaml';m.publish_new_files([(target,stage.read_bytes())],source.verify)
    assert target.read_bytes()==stage.read_bytes();source.verify()

def test_multioutput_second_collision_cleans_owned_first_reservation(tmp_path):
    fresh=tmp_path/'fresh';existing=tmp_path/'existing';existing.write_bytes(b'keep')
    with pytest.raises((ValueError,OSError)):
        m.publish_new_files([(fresh,b'one'),(existing,b'two')],lambda:None)
    assert not fresh.exists() and existing.read_bytes()==b'keep'

def test_hardlinked_original_change_after_copy_refused_before_publish(tmp_path):
    original=tmp_path/'original';original.write_bytes(b'frozen original');alias=tmp_path/'alias';alias.hardlink_to(original)
    expected=hashlib.sha256(original.read_bytes()).hexdigest()
    copy=tmp_path/'private-copy';copy.write_bytes(original.read_bytes());held=m.FrozenFile.capture(copy)
    alias.write_bytes(b'changed original');target=tmp_path/'candidate'
    def verify():
        held.verify();m.require_pin(original.read_bytes(),expected)
    with pytest.raises(ValueError):m.publish_new_files([(target,b'value')],verify)
    assert not target.exists() and copy.read_bytes()==b'frozen original'
