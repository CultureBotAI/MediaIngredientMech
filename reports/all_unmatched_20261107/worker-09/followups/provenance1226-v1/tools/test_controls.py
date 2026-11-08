"""Focused positive/negative tests, confined to a new durable private test directory."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import copy,datetime,hashlib,json,os,traceback
import correct_provenance as m

P=m.ROOT/'.temp/w09-provenance1226-successor-v1'
label=sys.argv[1] if len(sys.argv)>1 else 'controls'
m.require(label in {'controls','controls-v2'},'unsupported control-run label')
T=P/label;T.mkdir(exist_ok=False)
timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
rows=m.approved_rows();row=rows[0];raw=(m.R/'predecessors'/(row['proposal_id']+'.yaml')).read_bytes()
records={r['proposal_id']:(m.R/'predecessors'/(r['proposal_id']+'.yaml')).read_bytes() for r in rows}
results=[]

def test(name,fn):
    try:detail=fn();results.append({'name':name,'status':'PASS','detail':detail})
    except Exception as e:results.append({'name':name,'status':'FAIL','exception':repr(e),'traceback':traceback.format_exc()})

def refused(fn):
    try:fn()
    except (ValueError,FileExistsError,m.ValidationFailedError if hasattr(m,'ValidationFailedError') else ValueError) as e:return {'refused':type(e).__name__,'message':str(e)}
    raise AssertionError('Unsafe operation unexpectedly accepted')

def positive_all():
    proofs=[]
    for r in rows:
        b=records[r['proposal_id']];after=m.corrected(b,r,timestamp)
        assert not m.validate_ingredient(after)
        assert m.projection(m.yaml.safe_load(b))==m.projection(after)
        assert m.original_width(b) in (80,100)
        proofs.append(m.assert_allowed(b,after,r,timestamp))
    return {'eight_complete_objects':proofs}

test('all8_exact_allowlisted_positive_and_native_schema_projection',positive_all)
test('unmapped_projection_preserves_hold_without_fabricated_identity_row',lambda:{'projection':m.projection({'identifier':'UNMAPPED_TEST','preferred_term':'unresolved control','mapping_status':'UNMAPPED','synonyms':[]})} if m.projection({'identifier':'UNMAPPED_TEST','preferred_term':'unresolved control','mapping_status':'UNMAPPED','synonyms':[]})['identity_or_ontology_row_asserted'] is False else (_ for _ in ()).throw(AssertionError('fabricated row')))
test('stale_raw_payload',lambda:refused(lambda:m.bind(raw+b'\n',row)))
def bad_object():
    bad=copy.deepcopy(row);bad['full_value']['notes']+=' altered';bad['full_value_sha256']=m.canon(bad['full_value'])
    return refused(lambda:m.bind(raw,bad))
test('stale_complete_evidence_object_even_with_recomputed_object_hash',bad_object)
def wrong_field():
    bad=copy.deepcopy(rows);bad[0]['field']='ontology_mapping.evidence[1]'
    return refused(lambda:m.approved_rows(bad))
test('wrong_field_index',wrong_field)
test('duplicate_field_selection',lambda:refused(lambda:m.approved_rows(rows[:-1]+[rows[0]])))
def bad_after(kind):
    r=next(x for x in rows if x['proposal_id']==('ma-casamino-distinct' if kind in ['historical','history'] else 'ma-stock-jcm_226_czapek_concentrate'))
    b=records[r['proposal_id']];a=m.corrected(b,r,timestamp)
    if kind=='component':a['component_assertion']['evidence'][0]['evidence_type']='MANUAL_CURATION'
    elif kind=='historical':a['ontology_mapping']['evidence'][1]['evidence_type']='LLM_SUGGESTION'
    elif kind=='source':a['ontology_mapping']['evidence'][0]['source']='https://example.invalid/unreviewed'
    elif kind=='claim':a['ontology_mapping']['evidence'][0]['notes']+=' Exact equality is approved.'
    elif kind=='alias':a['synonyms'].append({'synonym_text':'generic stock','synonym_type':'EXACT_SYNONYM'})
    elif kind=='role':a['nutritional_roles']=[{'role':'CARBON_SOURCE'}]
    elif kind=='identity':a['identifier']='CHEBI:15377'
    elif kind=='history':a['curation_history'].pop(0)
    elif kind=='extra_history':a['curation_history'].append(copy.deepcopy(a['curation_history'][-1]))
    return refused(lambda:m.assert_allowed(b,a,r,timestamp))
for kind in ['component','historical','source','claim','alias','role','identity','history','extra_history']:
    test('reject_'+kind+'_change',lambda kind=kind:bad_after(kind))
decisions=m.read(m.R/'effective-decisions.json')['decisions'];proposals=m.read(m.R/'predecessor-cores/proposals.json')['proposals']
test('omitted_case',lambda:refused(lambda:m.validate_accounting(decisions[:-1],proposals)))
test('duplicated_case',lambda:refused(lambda:m.validate_accounting(decisions[:-1]+[decisions[0]],proposals)))
test('omitted_proposal',lambda:refused(lambda:m.validate_accounting(decisions,proposals[:-1])))
test('duplicated_proposal',lambda:refused(lambda:m.validate_accounting(decisions,proposals[:-1]+[proposals[0]])))
def changed_outcome():
    bad=copy.deepcopy(decisions);bad[0]['reasoning']+=' unrestricted release'
    return refused(lambda:m.validate_accounting(bad,proposals))
test('changed_source_outcome',changed_outcome)
test('full187_32_accounting_positive',lambda:(m.validate_accounting(decisions,proposals) or {'cases':187,'proposals':32}))
def existing():
    f=T/'preexisting.yaml';f.write_bytes(b'preserved sentinel\n');before=m.sha(f.read_bytes())
    result=refused(lambda:m.ReservedOutput(f,T));assert m.sha(f.read_bytes())==before;return result
test('preexisting_output_unchanged',existing)
def symlink_output():
    f=T/'aliased.yaml';target=T/'preexisting.yaml';f.symlink_to(target)
    result=refused(lambda:m.ReservedOutput(f,T));assert target.read_bytes()==b'preserved sentinel\n';return result
test('symlink_output_unchanged',symlink_output)
def symlink_parent():
    real=T/'real';real.mkdir();alias=T/'alias-parent';alias.symlink_to(real,target_is_directory=True)
    result=refused(lambda:m.ReservedOutput(alias/'out.yaml',T));assert not (real/'out.yaml').exists();return result
test('symlink_parent_refused_without_escaped_write',symlink_parent)
def hardlink_output():
    target=T/'preexisting.yaml';f=T/'hardlink.yaml';os.link(target,f)
    result=refused(lambda:m.ReservedOutput(f,T));assert target.read_bytes()==b'preserved sentinel\n';return result
test('hardlink_output_refused',hardlink_output)
test('outside_boundary',lambda:refused(lambda:m.ReservedOutput(P/'outside-must-not-exist.yaml',T)))
test('dotdot_path_refused',lambda:refused(lambda:m.ReservedOutput(T/'..'/'escape.yaml',T)))
def native_fd_positive():
    f=T/'positive-native.yaml';a=m.corrected(raw,row,timestamp);out=m.ReservedOutput(f,T)
    try:m.write_validated_ingredient(a,out,yaml_kwargs={'width':m.original_width(raw)})
    finally:out.close()
    result=m.assert_allowed(raw,m.yaml.safe_load(f.read_bytes()),row,timestamp)
    assert len(list(T.glob('positive-native.yaml')))==1
    return {'after_sha256':m.sha(f.read_bytes()),'complete_object_proof':result}
test('native_writer_exclusive_fd_positive',native_fd_positive)
out={'status':'FAIL' if any(r['status']=='FAIL' for r in results) else 'PASS','timestamp':timestamp,'tests':results,'test_count':len(results),'failure_count':sum(r['status']=='FAIL' for r in results),'scope':'Private negative/positive controls only. Fixtures and failures retained; no source mutation or broad gate invocation.'}
m.save(m.R/'validation'/(label+'.json'),out)
print(json.dumps({'status':out['status'],'test_count':len(results),'failure_count':out['failure_count']}))
if out['failure_count']:raise SystemExit(1)
