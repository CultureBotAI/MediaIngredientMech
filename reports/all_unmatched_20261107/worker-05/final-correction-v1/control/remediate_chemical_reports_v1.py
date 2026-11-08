"""Append two report-only corrections after recorded review/gate findings."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil
W=Path.cwd();S=W/'.temp/w05-final-correction-v1';P=W/'reports/all_unmatched_20261107/worker-05/final-correction-v1'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
dump=lambda p,x:p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
out=S/'remediation/chemical-report-v1';out.mkdir(parents=True,exist_ok=False)
source=S/'chemicals';changes=[]
name='primary-case-conclusions-v1.json';x=json.loads((source/name).read_text());row=x['case_reviews'][0]
assert row['case_id']=='CM_NAME:0aaa9e92307c43baf12b66d61715b0bb66b69a915820768fc229f570b35e73a0'
before=row['assessment']
assert 'zero-valent' in before
row['assessment']='JCM628 bottom layer contains 50 ml washed FeS preparation, 50 ml Modified Wolfe mineral solution and 1 g agarose. JCM629 explicitly reuses Medium628 with artificial saltwater replacing Modified Wolfe mineral solution. Both therefore contain the FeS preparation and agarose; the demonstrated distinguishing input is mineral solution versus artificial saltwater. Preserve receiving-layer and top-layer boundaries, processing and exact occurrence routing; neither bottom layer is neat FeS or a zero-valent iron preparation.'
changes.append(dict(finding_id='W05-FINAL-SKEPTIC-CHEM-001',path=name,json_pointer='/case_reviews/0/assessment',before=before,after=row['assessment']))
dump(out/'primary-case-conclusions-v2.json',x)
e=json.loads((source/'evidence-v1.json').read_text());rows=e['evidence'] if isinstance(e,dict) else e;missing=[]
for row in rows:
 if not row.get('supports_or_contradicts'):
  assert isinstance(row.get('observation'),str) and row['observation']
  missing.append(dict(evidence_id=row['evidence_id'],capture=row['capture'],observation=row['observation']))
  row['supports_or_contradicts']=row['observation']
assert len(missing)==14
dump(out/'evidence-v2.json',e)
finding=dict(finding_id='W05-FINAL-ASSEMBLY-001',author='/root',recorded_at=datetime.now(timezone.utc).isoformat(),
 category='outcome_evidence_envelope',severity='minor',reported_to_coordinator_before_fix=True,
 source=dict(path=str((source/'evidence-v1.json').relative_to(W)),sha256=sha(source/'evidence-v1.json')),
 actual_native_failure='audit_worker_outcomes_v1.py: InvalidOutcome: evidence applicability: nonempty string required',
 reproduction='Every listed entry has observation but lacks required supports_or_contradicts. The unchanged auditor rejects the final draft envelope before scientific adequacy is assessed.',
 affected_entries=missing,bounded_fix='Copy each existing observation verbatim into supports_or_contradicts in an immutable successor. Preserve original observation, source capture, URL, timestamp, kind and all other fields. No gate change or new scientific assertion.',
 scientific_scope='Metadata envelope only; primary applicability remains subject to full independent chemical case/payload/source review.')
dump(out/'assembly-finding-001.json',finding)
dump(out/'remediation-receipt.json',dict(at=datetime.now(timezone.utc).isoformat(),author='/root',
 reviewer='/root/materials_research',findings=['W05-FINAL-SKEPTIC-CHEM-001','W05-FINAL-ASSEMBLY-001'],
 reported_to_coordinator_before_fix=True,changed_conclusions=changes,
 evidence_changes=[dict(evidence_id=r['evidence_id'],added_field='supports_or_contradicts',exact_copy_of='observation') for r in missing],
 prior_finding=dict(path=str((S/'review-chemicals/finding-001-initial.json').relative_to(W)),sha256=sha(S/'review-chemicals/finding-001-initial.json')),
 unchanged_payloads=True,unchanged_capture_bytes_urls_timestamps=True,
 source_bindings=[dict(path=str((source/n).relative_to(W)),sha256=sha(source/n)) for n in [name,'evidence-v1.json','read-text/ROOT-jcm-628.txt','read-text/ROOT-jcm-629.txt']]))
dump(out/'MANIFEST.json',dict(files=[dict(path=p.name,sha256=sha(p)) for p in sorted(out.iterdir())]))
shutil.copytree(out,P/'remediation/chemical-report-v1')
print(sha(out/'MANIFEST.json'))
