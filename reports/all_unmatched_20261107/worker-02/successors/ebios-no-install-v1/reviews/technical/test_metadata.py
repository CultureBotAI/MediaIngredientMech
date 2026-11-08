from copy import deepcopy
import json
import pytest
import metadata_checks as m
import verify_published_retirement as v

def test_actual_twelve_files_and_real_old_source_git_proof():
    assert m.run()['source_git_proof']['status'] == 'PASS'

@pytest.mark.parametrize('key,value', [
    ('origin_id', 'w01::wrong'), ('origin_proposal_sha256', '0'*64),
    ('kind', 'edit'), ('reason', 'different reason'), ('successors', {'w01::other':'0'*64}),
    ('successors', []), ('successors', None), ('schema_version', '1'), ('schema_version', None),
])
def test_native_statement_exact_comparison_rejects_changes(key, value):
    obj = deepcopy(m.EXPECTED); obj[key] = value
    with pytest.raises(ValueError): m.statement_check(obj)

@pytest.mark.parametrize('mode', ['missing', 'extra'])
def test_native_closed_shape(mode):
    obj = deepcopy(m.EXPECTED)
    if mode == 'missing': del obj['successors']
    else: obj['extra'] = 'not permitted'
    with pytest.raises(ValueError, match='unknown/missing'): m.statement_check(obj)

@pytest.mark.parametrize('value', [True, 1.0])
def test_comparator_type_limitation_not_a_published_counterexample(value):
    obj = deepcopy(m.EXPECTED); obj['schema_version'] = value
    m.statement_check(obj)  # Exact observed native comparator acceptance.
    with pytest.raises(ValueError, match='not integer'): m.statement_check(obj, True)

@pytest.mark.parametrize('raw', ['{"a":1,"a":2}', '{"a":NaN}', '{"a":Infinity}'])
def test_native_json_rejects_duplicate_nonfinite(raw):
    with pytest.raises(ValueError): m.cw.read_json(raw)

@pytest.mark.parametrize('mode', ['object_hash', 'payload_hash', 'proposal_content', 'worker_bool', 'published_path'])
def test_real_native_original_proof_mutations(mode):
    origin, binding = v.source_context(m.W, v.BASE, m.native, m.cw)
    if mode == 'object_hash': origin['proposal_object_sha256'] = '0'*64
    if mode == 'payload_hash': origin['payload_sha256'] = '0'*64
    if mode == 'proposal_content': origin['proposal']['kind'] = 'edit'
    if mode == 'worker_bool': origin['worker_slot'] = True
    if mode == 'published_path': binding['payload']['published_path'] = v.LEDGER
    with pytest.raises(ValueError): m.cw._verify_origin(origin, binding, m.cw.Proofs(m.W, m.native))

@pytest.mark.parametrize('mode', ['case', 'occurrence', 'evidence', 'preimage', 'held_limit'])
def test_metadata_full_value_preservation(mode):
    names = ['selector.json','source-case-reconciliation.json','original/proposal.json','original/case-decision.json','original/evidence.json']
    packet = {name: m.cw.read_json((m.P/name).read_bytes()) for name in names}
    if mode == 'case': packet['original/case-decision.json']['reasoning'] = 'mutated'
    if mode == 'occurrence': packet['source-case-reconciliation.json']['original_occurrence_ids'] = []
    if mode == 'evidence': packet['original/evidence.json']['evidence'][0]['summary'] = 'mutated'
    if mode == 'preimage': packet['source-case-reconciliation.json']['original_before_sha256'] = '0'*64
    if mode == 'held_limit': packet['source-case-reconciliation.json']['held_limits'] = []
    with pytest.raises(ValueError): m.core_and_copies(packet)

def test_future_verifier_refuses_old_metadata_head():
    with pytest.raises(ValueError, match='cannot be published at original'):
        v.verify(m.W, v.BASE, m.native, m.cw)

def test_future_verifier_refuses_unselected_head():
    with pytest.raises(ValueError, match='not actual local HEAD'):
        v.verify(m.W, 'f'*40, m.native, m.cw)

def test_native_duplicate_and_omitted_origin_accounting():
    origin, binding = v.source_context(m.W, v.BASE, m.native, m.cw)
    with pytest.raises(ValueError, match='duplicate origin denominator'):
        m.cw.validate_resolution_crosswalk([origin,origin], [], root=m.W, origin_bindings=[binding])
    with pytest.raises(ValueError, match='omits/adds origins'):
        m.cw.validate_resolution_crosswalk([origin], [], root=m.W, origin_bindings=[binding])

def test_native_wrong_file_hash_and_alias_paths():
    proof = m.cw.Proofs(m.W, m.native)
    with pytest.raises(ValueError, match='hash differs'):
        proof.ref({'path': v.LEDGER, 'sha256': '0'*64})
    with pytest.raises(ValueError):
        proof.ref({'path': '../outside', 'sha256': '0'*64})
