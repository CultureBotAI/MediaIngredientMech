from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess
R=Path.cwd();C=R.parents[2];A=R/'reports/all_unmatched_20261107/worker-10';O=A/'successor-v2';P=R/'.temp/all-unmatched-worker-10/successor-v2';V=C/'workers/w07/worktree/.temp/w10-published-head-independent-review-v1';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected={'REPORT.md':'14ac9b9f3d64f5496ded72b3c98ca5ed8c2456f7ef70adf581586c862cf96920','findings.json':'73922a93a1fe8ebbf8b18ce2d5f26e9dbfa897186707fdb91dbe7dfa07a3d899','SHA256SUMS':'b800ba2b0d3c7363eb3704da82bd0bd157363ef6391af06c15858ed810c5c592'}
for n,h in expected.items():assert sha(V/n)==h
rows=[]
for line in (V/'SHA256SUMS').read_text().splitlines():
 h,n=line.split('  ',1);assert sha(V/n)==h;rows.append({'path':n,'sha256':h})
assert len(rows)==342
comp=R/'.temp/final-preparation-comparison-v1';m=json.loads((comp/'MANIFEST.json').read_text());assert sha(comp/'MANIFEST.json')=='b63eef440fb6ca056382f6ac6a899efa4f8629f5f2eb96e6d771858eadfef1b8'
for x in m['files']:assert sha(comp/x['path'])==x['sha256']
head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip();branch=subprocess.check_output(['git','branch','--show-current'],text=True).strip();assert head=='468766d941e35a74eb2de3c95096660987277d9b';assert branch=='review/all-unmatched-w10-source-review-20261107'
oldfiles={str(p.relative_to(R)):sha(p) for p in A.rglob('*') if p.is_file() and not p.is_relative_to(O)};owners={str(p.relative_to(R)):sha(p) for p in (R/'data/ingredients').rglob('*.yaml')};shard=C/'queue/preliminary-v5/shards/shard-10.json';assert sha(shard)=='9767ffc8100e3cd8cd0c4101cc8e9ebe8d8fda8aaab4c42ba4e11b8c3c5693cc'
accept={'schema_version':1,'worker_slot':10,'session':'same worker10 /root in-process session','at':datetime.now(timezone.utc).isoformat(),'branch':branch,'head':head,'frozen_scientific_base':'e000d66dd26ab053e9b17ce7bf8d3c873c3dde99','shard':str(shard),'shard_sha256':sha(shard),'output_root':str(O.relative_to(R)),'phase':'bounded append-only successor for issue1201 C-001/C-002; full188accounting retained','comparison_sealed':{'manifest_sha256':sha(comp/'MANIFEST.json'),'files_verified':len(m['files']),'scope':'19families96entries420uniquecomparisons remain frozen and author-excluded'},'independent_findings_bundle':{'root':str(V),'hashes':expected,'members_verified':len(rows)},'changed_case_indices':[143,187],'unchanged_scientific_decisions_required':186,'prohibited':'No maintained data, shared sources, roles, release/gates, PR/merge/reset/force/paid providers/session restart; EDTA/other inherited owner questions remain root integration scope.'}
for n,d in [('acceptance.json',accept),('progress-initial.json',{'at':accept['at'],'phase':'preflight_complete','assigned':188,'newly_changed_cases':[143,187],'primary_review':'in_progress','skeptical_review':'pending'})]:
 with (O/n).open('x') as f:json.dump(d,f,indent=2);f.write('\n')
for n,d in [('preservation-baseline.json',{'old_artifact_files':oldfiles,'owners':owners,'old_comparison_manifest':m,'independent_review_files':rows}),('preflight-receipt.json',accept)]:
 with (P/n).open('x') as f:json.dump(d,f,indent=2);f.write('\n')
for n in ['REPORT.md','findings.json','SHA256SUMS']:(O/'inputs'/('independent-'+n)).write_bytes((V/n).read_bytes())
(O/'inputs/coordinator-issue1201-comment.md').write_bytes((C/'preflight/root-integration-findings-v1/issue1201-w10-final-completeness-v1.md').read_bytes())
print(json.dumps({'status':'PASS','external_review_members':len(rows),'sealed_comparison_members':len(m['files']),'old_source_artifacts':len(oldfiles),'catalog_owners':len(owners)},indent=2))
