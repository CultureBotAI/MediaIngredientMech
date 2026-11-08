from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil
W=Path.cwd();S=W/'.temp/w05-final-correction-v1';P=W/'reports/all_unmatched_20261107/worker-05/final-correction-v1';B=P.parent
out=S/'remediation/chemical-report-v2';out.mkdir(exist_ok=False)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
dump=lambda p,x:p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
original=json.loads((B/'correction-1193-v1/decisions.json').read_text())['decisions'];old={d['case_id']:d for d in original}
src=S/'chemicals/decisions-v2.json';x=json.loads(src.read_text());rows=x['decisions'] if isinstance(x,dict) else x;changes=[]
for row in rows:
 if row['disposition']!='curation_proposal':continue
 after=old[row['case_id']]['disposition'];assert after in ['existing_identity_or_alias','stock_product_mixture_context','unresolved']
 changes.append(dict(case_id=row['case_id'],source=row['source'],before=row['disposition'],after=after,retained_followon_proposal_ids=row['proposal_ids'],missing_requirement=row['missing_requirement']))
 row['disposition']=after
assert len(changes)==3
dump(out/'decisions-v3.json',x)
dump(out/'assembly-finding-002.json',dict(finding_id='W05-FINAL-ASSEMBLY-002',author='/root',recorded_at=datetime.now(timezone.utc).isoformat(),
 category='outcome_disposition_enum',severity='minor',reported_to_coordinator_before_fix=True,
 source=dict(path=str(src.relative_to(W)),sha256=sha(src)),
 actual_native_failure='audit_worker_outcomes_v1.py: InvalidOutcome: invalid disposition',
 affected_cases=changes,bounded_fix='Restore each exact original native disposition. Preserve all proposal links, missing facts, source-specific scientific reasoning and no-change nulls for cases with a bounded follow-on. A follow-on proposal does not resolve the source case.',
 no_scientific_decision_or_payload_change=True))
dump(out/'remediation-receipt.json',dict(at=datetime.now(timezone.utc).isoformat(),author='/root',reviewer='/root/materials_research',
 finding_id='W05-FINAL-ASSEMBLY-002',changes=changes,
 previous_amendment='chemical-report-v1 selected evidence-v2 and primary-case-conclusions-v2 remain selected',
 all_capture_bytes_and_payloads_unchanged=True))
dump(out/'MANIFEST.json',dict(files=[dict(path=p.name,sha256=sha(p)) for p in sorted(out.iterdir())]))
shutil.copytree(out,P/'remediation/chemical-report-v2');print(sha(out/'MANIFEST.json'))
