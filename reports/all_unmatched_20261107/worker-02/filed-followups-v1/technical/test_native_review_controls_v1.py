"""Independent native positive/publication negatives; no author payload approval."""
from pathlib import Path
import importlib.util,json,os
import pytest,yaml
R=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('reviewed_successor',R/'build_successor_v2.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
proposals=json.loads((m.S/'proposals.json').read_bytes())['proposals']
old_path=m.A/next(p['after_capture']['path'] for p in proposals if p['proposal_id']==m.PID)

def test_native_closed_schema_roundtrip_then_exclusive_publication(tmp_path):
    frozen=m.FrozenFile.capture(old_path)
    old=yaml.safe_load(frozen.content);value=m.correct_payload(old)
    stage=tmp_path/'stage.yaml';m.write_validated_ingredient(value,stage)
    assert yaml.safe_load(stage.read_bytes())==value
    target=tmp_path/'published.yaml'
    m.publish_new_files([(target,stage.read_bytes())],frozen.verify)
    frozen.verify()
    assert target.read_bytes()==stage.read_bytes()
    m.validate_payload_delta(old,yaml.safe_load(target.read_bytes()))

def test_native_duplicate_destinations_refused_before_creation(tmp_path):
    target=tmp_path/'one'
    with pytest.raises(ValueError,match='collide'):
        m.publish_new_files([(target,b'a'),(target,b'b')],lambda:None)
    assert not target.exists()

def test_native_output_symlink_refused_and_target_bytes_preserved(tmp_path):
    original=tmp_path/'original';original.write_bytes(b'original')
    link=tmp_path/'link';link.symlink_to(original)
    with pytest.raises((OSError,ValueError)):
        m.publish_new_files([(link,b'new')],lambda:None)
    assert link.is_symlink() and original.read_bytes()==b'original'

def test_native_frozen_input_rejects_hardlink_alias(tmp_path):
    original=tmp_path/'original';original.write_bytes(b'original')
    alias=tmp_path/'alias';os.link(original,alias)
    with pytest.raises((OSError,ValueError)):
        m.FrozenFile.capture(original)
    assert original.read_bytes()==alias.read_bytes()==b'original'

def test_native_second_output_collision_removes_only_owned_reservation(tmp_path):
    fresh=tmp_path/'fresh';existing=tmp_path/'existing';existing.write_bytes(b'keep')
    with pytest.raises((OSError,ValueError)):
        m.publish_new_files([(fresh,b'first'),(existing,b'second')],lambda:None)
    assert not fresh.exists() and existing.read_bytes()==b'keep'
