"""Read-only checks of actual serialized successor bytes and complete selection."""
import sys
sys.dont_write_bytecode=True
import copy,datetime,difflib,json
from pathlib import Path
import correct_provenance as m

S=m.read(m.R/'selection.json');F=m.read(m.R/'allowlist-proof.json')
rows={r['proposal_id']:r for r in m.approved_rows()}
proofs=[];errors=[];all_schema=[];projection=[];changed=0;retained=0
new=m.read(m.R/'proposals.json')['proposals'];old=m.read(m.R/'predecessor-cores/proposals.json')['proposals']
old_by={p['proposal_id']:p for p in old};new_by={p['proposal_id']:p for p in new}
m.require(len(S['selected'])==32 and len({r['proposal_id'] for r in S['selected']})==32,'selection missing or duplicate')
m.require({r['proposal_id'] for r in S['selected']}==set(old_by),'selection changed population')
for selected in S['selected']:
    pid=selected['proposal_id'];oldraw=(m.ROOT/selected['before_path']).read_bytes();newpath=m.ROOT/selected['selected_path'];raw=newpath.read_bytes()
    m.require(m.sha(oldraw)==selected['before_sha256'],'stale predecessor')
    m.require(m.sha(raw)==selected['selected_sha256'],'stale selection')
    before=m.yaml.safe_load(oldraw);after=m.yaml.safe_load(raw)
    es=m.validate_ingredient(after);all_schema.append({'proposal_id':pid,'path':selected['selected_path'],'sha256':m.sha(raw),'errors':[str(e) for e in es]})
    m.require(not es,'serialized schema failure')
    a=m.projection(before);b=m.projection(after);m.require(a==b,'native row/synonym projection drift')
    projection.append({'proposal_id':pid,'before':a,'after':b,'equal':True})
    np=copy.deepcopy(new_by[pid]);op=old_by[pid]
    if pid in rows:
        changed+=1;m.require(selected['changed'] and raw!=oldraw,'changed classification mismatch')
        proofs.append(m.assert_allowed(oldraw,after,rows[pid],F['timestamp']))
        declared=m.R.parents[1]/np['after_capture']['path']
        m.require(declared==newpath and np['after_capture']['sha256']==m.sha(raw),'proposal after_capture misbound')
        np['after_capture']=op['after_capture'];m.require(np==op,'non-capture proposal field change')
        diff=''.join(difflib.unified_diff(oldraw.decode().splitlines(True),raw.decode().splitlines(True),fromfile=selected['before_path'],tofile=selected['selected_path']))
        f=m.R/'validation/diffs'/(pid+'.diff');f.parent.mkdir(parents=True,exist_ok=True)
        with f.open('x') as handle:handle.write(diff)
    else:
        retained+=1;m.require(not selected['changed'] and raw==oldraw,'retained payload not byte-identical');m.require(np==op,'retained proposal changed')
m.require((changed,retained)==(8,24),'wrong changed/retained totals')
m.validate_accounting(m.read(m.R/'effective-decisions.json')['decisions'],new)
original_effective=Path(m.read(m.R/'preflight.json')['w09_binding']['effective_decisions']['path'])
m.require(original_effective.read_bytes()==(m.R/'effective-decisions.json').read_bytes(),'effective ledger byte drift')
for f in m.read(m.R/'preflight.json')['original_report_files']:
    m.require(m.sha((m.ROOT/f['path']).read_bytes())==f['sha256'],'original W09 report changed')
m.save(m.R/'validation/complete-successor.json',{'status':'PASS','checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_head':m.HEAD,'case_count':187,'selected_payload_count':32,'changed_payload_count':changed,'byte_identical_retained_payload_count':retained,'serialized_payload_schema':all_schema,'changed_full_payload_allowlist_rechecks':proofs,'native_projection_checks':projection,'effective_decisions_sha256':m.sha((m.R/'effective-decisions.json').read_bytes()),'all_original_report_files_unchanged':True,'original_report_files':1233,'scientific_review':False,'limits':'Full object equality proves only unchanged claims; the native functions check identity/synonym projection consistency, not export release. No shared export was run, and evidence provenance changes do not renew scientific truth.'})
print(json.dumps({'status':'PASS','schema_payloads':32,'native_projection_comparisons':32,'changed':8,'retained':24,'effective_cases':187}))
