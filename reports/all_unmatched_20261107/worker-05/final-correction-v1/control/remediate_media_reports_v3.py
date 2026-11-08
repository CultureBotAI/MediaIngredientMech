"""Append the reviewer-confirmed LB report identifier correction."""
from pathlib import Path
import json,hashlib,shutil
from datetime import datetime,timezone
W=Path.cwd();S=W/'.temp/w05-final-correction-v1';P=W/'reports/all_unmatched_20261107/worker-05/final-correction-v1'
old=S/'remediation/media-report-v2';out=S/'remediation/media-report-v3';out.mkdir(exist_ok=False)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
dump=lambda p,x:p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
changes=[]
for name,key in [('decisions.json','decisions'),('primary-read-ledger.json','cases')]:
 x=json.loads((old/name).read_text())
 for row in x[key]:
  index=row['case_index'];node=row['final_correction_reassessment'] if key=='decisions' else row
  if index not in [159,174]:continue
  before=node['assessment']
  if index==159:
   assert 'generic LB source1708' in before
   node['assessment']=before.replace('generic LB source1708','supplier-unspecified LB powder mediadive.ingredient:1999')
  else:
   assert 'Source1708/JCM1111' in before
   node['assessment']=before.replace('Source1708/JCM1111','mediadive.ingredient:1999/JCM1111')
  changes.append(dict(path=name,case_index=index,before=before,after=node['assessment']))
 dump(out/name,x)
receipt=dict(at=datetime.now(timezone.utc).isoformat(),author='/root',reviewer='/root/final_skeptical',
 finding_id='W05-FINAL-MEDIA-REVIEW-03',reported_to_coordinator_before_fix=True,
 finding=dict(path=str((S/'review-media/new-findings-v2.json').relative_to(W)),sha256=sha(S/'review-media/new-findings-v2.json')),
 predecessor_manifest_sha256=sha(old/'MANIFEST.json'),changed_fields=changes,
 exact_source=dict(path='reports/all_unmatched_20261107/worker-05/media/captures/8accfcb3006f5d17f6.html',sha256=sha(W/'reports/all_unmatched_20261107/worker-05/media/captures/8accfcb3006f5d17f6.html')),
 unchanged_payloads=True,unchanged_source_fields=True,selected_other_report_files='Retain the media-report-v2 finding-dispositions, mapping-evidence-typing and superseding report prose unchanged.')
dump(out/'remediation-receipt.json',receipt)
dump(out/'MANIFEST.json',dict(files=[dict(path=p.name,sha256=sha(p)) for p in sorted(out.iterdir())]))
shutil.copytree(out,P/'remediation/media-report-v3')
print(sha(out/'MANIFEST.json'))
