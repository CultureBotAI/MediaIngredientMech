from pathlib import Path
import json,hashlib,yaml,datetime
W=Path.cwd();S=W/'.temp/w05-buffer-parts-v1';R=S/'assembly-review';B=W/'reports/all_unmatched_20261107/worker-05';P=B/'buffer-parts-v1';V=P/'validation';j=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();candidate=S/'control/composed-final-v5/proposals.json';ps=j(candidate)['proposals'];pi={p['proposal_id']:p for p in ps};native=j(V/'full-overlay/native-validation.json');rows=j(V/'native-row-projections.json');bindings=[]
assert sha(candidate)==sha(V/'input-proposals.json')==native['inputs']['proposals']['sha256']
assert native['status']=='PASS' and not native['errors'] and native['candidate_payloads']==len(ps)
assert native['baseline_records']==2956 and native['overlay_records']==3029
assert set(x['proposal_id'] for x in native['guarded_payloads'])==set(pi)
for i,p in enumerate(ps):
 c=p['after_capture'];f=B/c['path'];r=yaml.safe_load(f.read_text());g=next(x for x in native['guarded_payloads'] if x['proposal_id']==p['proposal_id']);assert g['selected_capture']==c
 guard=V/'full-overlay/guarded-readback'/f'{i:03d}-{f.name}';assert sha(guard)==g['guarded_readback_sha256'];assert yaml.safe_load(guard.read_text())==r
 row=next(x for x in rows['reviewed_projections'] if x['proposal_id']==p['proposal_id']);assert row['after_capture']==c and row['after_identifier']==r['identifier']
 bindings.append(dict(proposal_id=p['proposal_id'],after_capture=c,guarded_readback=dict(path=str(guard.relative_to(W)),sha256=sha(guard)),native_rows=len(row['after_rows']),native_identifier=row['after_identifier']))
assert len(rows['reviewed_projections'])==len(pi)
for name in ['full-overlay','full-strict','consolidated-validation']:
 rc=j(V/(name+'.receipt.json'));assert rc['exit_code']==0 and rc['command']
for m in native['native_implementations']:assert sha(W/m['path'])==m['sha256']
assert sha(Path(rows['builder']['path']))==rows['builder']['sha256']
refs=['input-proposals.json','full-overlay/native-validation.json','native-row-projections.json','full-overlay.receipt.json','full-strict.receipt.json','consolidated-validation.receipt.json']
x=dict(at=datetime.datetime.now(datetime.timezone.utc).isoformat(),reviewer='/root/assembly_audit',status='PASS',scope='Mechanical exact-byte binding of actual full-payload native/schema/component/filename/identifier results to composed-final-v5. No scientific, source-admission, owner-application or export approval; commands were run by root and reviewed here, not reattributed as independently executed.',payload_count=len(ps),projection_rows=sum(len(x['after_rows']) for x in rows['reviewed_projections']),baseline_records=native['baseline_records'],overlay_records=native['overlay_records'],result_bindings=[dict(path=str((V/f).relative_to(W)),sha256=sha(V/f)) for f in refs],payload_bindings=bindings,native_implementations=native['native_implementations'],native_builder=rows['builder'])
f=R/'native-result-binding-independent-v1.json';assert not f.exists();f.write_text(json.dumps(x,indent=2)+'\n');print(json.dumps(dict(status='PASS',payloads=len(ps),rows=x['projection_rows'],sha256=sha(f))))
