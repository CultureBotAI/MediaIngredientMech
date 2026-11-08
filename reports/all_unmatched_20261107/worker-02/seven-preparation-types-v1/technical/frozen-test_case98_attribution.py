from copy import deepcopy
import importlib.util,json,sys
from pathlib import Path
import pytest
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R));s=importlib.util.spec_from_file_location('case98',R/'add_case98_attribution_v2.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
D=json.loads((m.S/'decisions.json').read_text())['decisions'];N=json.loads((m.OUT/'decisions.json').read_text())['decisions']
def test_actual_complete_case98_two_field_delta_and_outcome():
 m.validate_delta(D[98],N[98]);assert len(N[98]['occurrence_ids'])==1 and N[98]['proposal_ids']==[]
 for k in D[98]:
  if k not in ['reasoning','applicability','independent_review']:assert N[98][k]==D[98][k]
 assert 'TOGO M2509 capture reports the NIES table/footnote' in N[98]['reasoning'] and 'unsuccessful formulation lookup' in N[98]['reasoning']
 assert 'Existing CHEBI131524 is the five-water substance' in N[98]['reasoning']
@pytest.mark.parametrize('field',['disposition','case_id','case_input_sha256','occurrence_ids','source','evidence_ids','owner_records','proposal_ids','no_change_reason','missing_requirement','issue_refs'])
def test_unrequested_case98_field_mutation_refused(field):
 new=deepcopy(N[98]);new[field]='unrequested'
 with pytest.raises(ValueError):m.validate_delta(D[98],new)
@pytest.mark.parametrize('field',['reasoning','applicability'])
def test_false_successful_original_or_changed_hydrate_refused(field):
 new=deepcopy(N[98]);new[field]='Direct NIES successfully confirms heptahydrate'
 with pytest.raises(ValueError):m.validate_delta(D[98],new)
def test_original_source_hashes_and_failed_capture_preserved():
 assert m.b.sha(m.b.A/'b/captures/retry-togo-M2509.json')==m.TOGO_SHA
 assert m.b.sha(m.b.A/'b/captures/source-c533a17a8ded25f29384.bin')==m.NIES_SHA
def test117_payloads_and186_other_cases_exact():
 assert (m.S/'proposals.json').read_bytes()==(m.OUT/'proposals.json').read_bytes()
 for p in json.loads((m.OUT/'proposals.json').read_text())['proposals']:assert m.b.sha(m.b.A/p['after_capture']['path'])==p['after_capture']['sha256']
 for i in range(188):
  if i not in [58,98]:assert D[i]==N[i]
 assert N[58]==m.b.pending_case(D[58]) and len(N[58]['occurrence_ids'])==24
 assert sum(len(d['occurrence_ids']) for d in N)==322
def test_full1827_prior_evidence_prefix_and_queued_prompt():
 a=m.b.raw_array_objects((m.S/'evidence.json').read_bytes(),'evidence');b=m.b.raw_array_objects((m.OUT/'evidence.json').read_bytes(),'evidence');assert len(a)==1827 and len(b)==1829 and b[:len(a)]==a
 receipt=json.loads((m.OUT/'case98-preservation-receipt.json').read_text());assert receipt['queued_prompt']['covered_by_this_active_successor'] and not receipt['queued_prompt']['separate_publication_required']
def test_pin_receipt_exact_and_changed_refusal():
 raw=m.PIN_FILE.read_bytes();m.validate_pin_receipt(raw)
 with pytest.raises(ValueError):m.validate_pin_receipt(raw+b'\n')
def test_stale_local_pin_refuses_before_outputs(tmp_path,monkeypatch):
 p=tmp_path/'pins.json';p.write_bytes(m.PIN_FILE.read_bytes()+b'\n');out=tmp_path/'output';monkeypatch.setattr(m,'PIN_FILE',p);monkeypatch.setattr(m,'OUT',out);monkeypatch.setattr(m.b,'require_output',lambda x:x)
 with pytest.raises(ValueError):m.main()
 assert not out.exists()
