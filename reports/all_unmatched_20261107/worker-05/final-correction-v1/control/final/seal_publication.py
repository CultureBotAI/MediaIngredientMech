from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
W=Path.cwd();S=W/'.temp/w05-final-correction-v1';P=W/'reports/all_unmatched_20261107/worker-05/final-correction-v1'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
counts=json.loads((P/'final-counts.json').read_text());native=json.loads((P/'native-review-preparation-v2/review-content.json').read_text());N=W/'reviews/structured'/native['review_id']
manifest=P/'MANIFEST.json';assert not manifest.exists()
files=[dict(path=str(p.relative_to(P)),sha256=sha(p),bytes=p.stat().st_size) for p in sorted(P.rglob('*')) if p.is_file()]
assert files and all(not p.is_symlink() for p in P.rglob('*'))
packet=dict(schema='worker05-final-scientific-correction-manifest-v1',sealed_at=datetime.now(timezone.utc).isoformat(),compiler='/root',
 preserved_published_source_head='43f7cf6e8681fa617b5d6d3529d94d537ca01f0d',branch='review/all-unmatched-w05-source-review-20261107',
 exact_published_successor_head='Recorded after ordinary push in the single authoritative private .temp/w05-final-correction-v1/HANDOFF.json; no self-referential commit claim.',
 counts=counts,selected_core=[dict(path='core/'+n,sha256=sha(P/'core'/n)) for n in ['decisions.json','proposals.json','evidence.json','proposal-lineage.json']],
 independent_scientific_reviews=json.loads((S/'control/final-review-bindings.json').read_text()),
 final_assembly_review=dict(path='reviews/assembly/FINAL-MANIFEST-v1.json',sha256=sha(P/'reviews/assembly/FINAL-MANIFEST-v1.json')),
 native_review=[dict(path=str(p.relative_to(W)),sha256=sha(p)) for p in sorted(N.iterdir()) if p.is_file()],
 preservation=dict(path='validation/final-preservation.json',sha256=sha(P/'validation/final-preservation.json')),
 retained_review_check=dict(path='validation/final-native-review-check.json',sha256=sha(P/'validation/final-native-review-check.json')),
 protected_comparison_manifest_sha256=sha(W/'.temp/final-preparation-comparison-v1/MANIFEST.json'),
 scope='Append-only report successor; original138 proposal origins and188 source scopes preserved. No maintained owner, source, export, gate, schema, workflow or pin changes. Conditional preparations are alternatives, not approved co-installations. Coordinator owns final acceptance/integration/release.',
 self_exclusion='This manifest excludes itself; all other published successor files are included. Native YAML/Markdown are separately bound outside this directory.',files=files)
manifest.write_text(json.dumps(packet,indent=2,ensure_ascii=False)+'\n')
for r in files:assert sha(P/r['path'])==r['sha256']
print(json.dumps(dict(manifest=str(manifest.relative_to(W)),sha256=sha(manifest),files=len(files),bytes=sum(r['bytes'] for r in files),native_review=native['review_id'])))
