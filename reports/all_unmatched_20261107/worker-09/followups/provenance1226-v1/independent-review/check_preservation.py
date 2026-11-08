from pathlib import Path
import hashlib, json, datetime

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
R=ROOT/'reports/all_unmatched_20261107/worker-09/followups/provenance1226-v1'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
canon=lambda v:hashlib.sha256(json.dumps(v,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
read=lambda p:json.loads(p.read_text())
pre=read(R/'preflight.json')
checks=[];errors=[]
for group in ['original_report_files','contracts']:
    members=pre[group]
    for row in members:
        if sha(ROOT/row['path'])!=row['sha256']:errors.append({'group':group,'path':row['path']})
    checks.append({'group':group,'member_count':len(members),'member_binding_digest':canon(members)})
plan=pre['planning_manifest'];mf=Path(plan['path']);base=mf.parent
if sha(mf)!=plan['sha256']:errors.append({'group':'planning_manifest'})
for row in plan['members']:
    if sha(base/row['path'])!=row['sha256']:errors.append({'group':'planning_members','path':row['path']})
checks.append({'group':'planning_packet','manifest_sha256':sha(mf),'member_count':len(plan['members'])})
for packet in pre['preserved_private_packets']:
    base=Path(packet['path']);mf=base/'FINAL-MANIFEST.json';m=read(mf)
    if sha(mf)!=packet['manifest_sha256']:errors.append({'group':'private_packet_manifest','path':str(mf)})
    for row in m['files']:
        if sha(base/row['path'])!=row['sha256']:errors.append({'group':'private_packet_member','path':str(base/row['path'])})
    actual={str(f.relative_to(base)) for f in base.rglob('*') if f.is_file()}
    expected={row['path'] for row in m['files']}|set(m['excludes'])
    if actual!=expected:errors.append({'group':'private_packet_membership','path':str(base)})
    checks.append({'group':'sealed_private_packet','path':str(base),'manifest_sha256':sha(mf),'member_count':len(m['files']),'exact_membership':actual==expected})
effective=Path(pre['w09_binding']['effective_decisions']['path'])
if (R/'effective-decisions.json').read_bytes()!=effective.read_bytes():errors.append({'group':'effective_decisions'})
baseline=read(OUT/'baseline-inspection.json');decision_data=read(R/'effective-decisions.json');current=decision_data['decisions']
casechecks=[{'case_id':x['case_id'],'full_row_sha256':canon(x)} for x in current]
if casechecks!=baseline['case_bindings']:errors.append({'group':'all187_case_bindings'})
for row in pre['w09_binding']['all_selected_payloads']:
    pid=row['entry_id'].split('::',1)[1];file=R/'predecessors'/f'{pid}.yaml'
    if sha(file)!=row['sha256'] or file.read_bytes()!=Path(row['path']).read_bytes():errors.append({'group':'predecessor_payload','proposal_id':pid})
out={'reviewer':'Codex /root/provenance1226_reviewer','checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
     'status':'FAIL' if errors else 'PASS','checks':checks,'all187_case_checks':casechecks,
     'predecessor_payloads':32,'effective_decisions_sha256':sha(R/'effective-decisions.json'),
     'retained_supersession_cases':[x['case_id'] for x in current if x.get('supersedes_source_assessment_only')],
     'errors':errors,'limit':'Exact byte/field preservation only; no independent scientific reassessment or renewed role/export approval.'}
with (OUT/'preservation.json').open('x') as f:json.dump(out,f,indent=2,ensure_ascii=False);f.write('\n')
print(json.dumps({'status':out['status'],'group_checks':checks,'cases':len(casechecks),'errors':errors}))
if errors:raise SystemExit(1)
