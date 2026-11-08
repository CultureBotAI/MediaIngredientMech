"""Independent native-helper replay and failure-oriented workflow controls."""
import copy
import datetime
import hashlib
import json
from pathlib import Path
import sys
import yaml
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.write_validated import write_validated_ingredient, ValidationFailedError

W = Path.cwd()
A = W / 'reports/all_unmatched_20261107/worker-08'
O = W / '.temp/all-unmatched-worker-08/plain-flour-process-replay-v1/independent'
FIX = O / 'fixtures'
BEFORE = A / 'successors/issue-1227-v1/research/organic_products/proposed_owners/Plain_Flour.yaml'
PUBLISHED = A / 'successors/issue-1227-plain-flour-v1/payloads/Plain_Flour.yaml'
EXPECTED_BEFORE = 'aa8390f17f1ed9f9c083fd6b487ee1c40228e754072b7e390b97dfb2fd6eae83'
EXPECTED_AFTER = '884fee1ea6a5082a51b8769f2a827199b1703972ad80fa48e1bb8d2d09ab3873'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
def canon(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode()).hexdigest()

assert sha(BEFORE) == EXPECTED_BEFORE
assert sha(PUBLISHED) == EXPECTED_AFTER
before = yaml.safe_load(BEFORE.read_text())
published = yaml.safe_load(PUBLISHED.read_text())
assert len(before['curation_history']) == 5
assert published['curation_history'][:-1] == before['curation_history']
event = copy.deepcopy(published['curation_history'][-1])
assert event['llm_assisted'] is True
assert set(event) == {'timestamp','curator','action','changes','previous_status','new_status','llm_assisted','llm_model'}
FIX.mkdir(exist_ok=False)

calls = []
codes = {record_curation_event.__code__: 'native_record_curation_event', write_validated_ingredient.__code__: 'native_write_validated_ingredient'}
def profile(frame, what, arg):
    if what == 'call' and frame.f_code in codes:
        calls.append({'operation': codes[frame.f_code], 'native_file': frame.f_code.co_filename, 'line': frame.f_code.co_firstlineno})

def build(mode):
    """Replay only the already reviewed non-history delta from the same predecessor."""
    assert sha(BEFORE) == EXPECTED_BEFORE, 'wrong predecessor bytes'
    rec = copy.deepcopy(before)
    if mode == 'wrong_predecessor_identity':
        rec['identifier'] = 'FOODON:00001056'
    assert rec['identifier'] == 'FOODON:00004510', 'wrong predecessor identity'
    rec['preferred_term'] = published['preferred_term']
    rec['notes'] = published['notes']
    rec['ontology_mapping']['evidence'] = copy.deepcopy(published['ontology_mapping']['evidence'])
    args = copy.deepcopy(event)
    if mode == 'wrong_historical_timestamp':
        args['timestamp'] = '2026-11-08T08:38:46.690887+00:00'
    elif mode == 'wrong_llm_flag':
        args['llm_assisted'] = False
    elif mode == 'wrong_curator':
        args['curator'] = 'unrelated replay actor'
    elif mode == 'wrong_status':
        args['previous_status'] = 'UNMAPPED'
    if mode == 'direct_append_bypass':
        # Deliberate control: even equal output cannot prove use of the helper.
        rec['curation_history'].append(args)
        result = args
    else:
        result = record_curation_event(rec, **args)
        if mode == 'duplicate_event':
            record_curation_event(rec, **args)
    if mode == 'unreviewed_field_delta':
        rec['occurrence_statistics']['total_occurrences'] = 1
    assert len([x for x in calls if x['operation'] == 'native_record_curation_event']) == 1, 'must execute native helper exactly once'
    assert result == event, 'complete returned event differs'
    assert rec['curation_history'] == published['curation_history'], 'complete history differs'
    assert rec == published, 'complete payload differs'
    return rec

results = []
for mode in ['positive', 'positive_second_fresh_replay', 'wrong_predecessor_identity', 'wrong_historical_timestamp', 'wrong_llm_flag', 'wrong_curator', 'wrong_status', 'duplicate_event', 'unreviewed_field_delta', 'direct_append_bypass']:
    calls = []
    dest = FIX / (mode + '.yaml')
    expected_accept = mode.startswith('positive')
    sys.setprofile(profile)
    try:
        rec = build(mode)
        write_validated_ingredient(rec, dest)
        assert sha(dest) == EXPECTED_AFTER, 'complete serialized payload bytes differ'
        assert sum(x['operation'] == 'native_write_validated_ingredient' for x in calls) == 1
        observed = 'ACCEPTED_EXACT'
        diagnostic = None
    except AssertionError as exc:
        observed = 'REFUSED'
        diagnostic = str(exc)
    finally:
        sys.setprofile(None)
    assert (observed == 'ACCEPTED_EXACT') == expected_accept, (mode, observed, diagnostic)
    if not expected_accept:
        assert not dest.exists(), 'failed process control produced a replay payload'
    results.append({'mode':mode,'expected_accept':expected_accept,'observed':observed,'diagnostic':diagnostic,'actual_native_calls':copy.deepcopy(calls),'output_exists':dest.exists(),'output_sha256':sha(dest) if dest.exists() else None})

# Native closed-schema checks are separate from exact-history/process checks.
for mode in ['native_unknown_field', 'native_bad_action_pattern']:
    rec = copy.deepcopy(published)
    if mode == 'native_unknown_field':
        rec['plain_flour_replay_unknown_field'] = True
    else:
        rec['curation_history'][-1]['action'] = 'bad action'
    dest = FIX / (mode + '.yaml')
    calls = []
    sys.setprofile(profile)
    try:
        write_validated_ingredient(rec, dest)
        raise AssertionError('native schema accepted invalid fixture')
    except ValidationFailedError as exc:
        diagnostic = exc.summary()
    finally:
        sys.setprofile(None)
    assert not dest.exists()
    results.append({'mode':mode,'expected_accept':False,'observed':'NATIVE_SCHEMA_REFUSED','error_type':'ValidationFailedError','diagnostic':diagnostic,'actual_native_calls':copy.deepcopy(calls),'input_canonical_sha256':canon(rec),'output_exists':False})

out = {
    'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'status':'PASS','reviewer':'worker08:/root/inorganics','scope':'Independent workflow replay and controls only; no new source/identity decision or whole-owner approval.',
    'predecessor':{'path':str(BEFORE.relative_to(W)),'sha256':sha(BEFORE)},
    'published':{'path':str(PUBLISHED.relative_to(W)),'sha256':sha(PUBLISHED)},
    'complete_event':event,'event_canonical_sha256':canon(event),
    'history_canonical_sha256':canon(published['curation_history']),
    'native_helper':{'path':'src/mediaingredientmech/curate/curation_event.py','sha256':sha(W/'src/mediaingredientmech/curate/curation_event.py')},
    'native_writer':{'path':'src/mediaingredientmech/validation/write_validated.py','sha256':sha(W/'src/mediaingredientmech/validation/write_validated.py')},
    'results':results,'positive_count':sum(x['expected_accept'] for x in results),'negative_count':sum(not x['expected_accept'] for x in results),
    'process_measurement':'sys.setprofile observes the actual unchanged native code objects; no monkeypatch, helper mock, native-source edit or writer bypass. Deliberate direct-append mutant is refused despite potential event equality.',
    'timestamp_interpretation':'The original timestamp is passed as the helper-supported deterministic snapshot override. The receipt time is current execution time. No new historical event or scientific review time is invented.',
    'limitations':['These independent fixtures do not by themselves prove the separate root replay script uses the helper; its actual full source and receipts require separate review.','Other than two exact copies, every process/schema control refuses before writing output.','No maintained corpus, selection, SSSOM, earlier artifact, native gate or Git state was changed.']
}
dest = O/'independent-probes.json';assert not dest.exists();dest.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'status':'PASS','positives':out['positive_count'],'negatives':out['negative_count'],'receipt':str(dest),'sha256':sha(dest)},indent=2))
