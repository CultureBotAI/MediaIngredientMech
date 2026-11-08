from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess
W=Path.cwd();S=W/'.temp/w05-final-correction-v1';P=W/'reports/all_unmatched_20261107/worker-05/final-correction-v1'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
base='43f7cf6e8681fa617b5d6d3529d94d537ca01f0d';branch='review/all-unmatched-w05-source-review-20261107'
head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
assert subprocess.check_output(['git','branch','--show-current'],text=True).strip()==branch
subprocess.run(['git','merge-base','--is-ancestor',base,head],check=True)
remote=subprocess.check_output(['git','ls-remote','--exit-code','origin','refs/heads/'+branch],text=True).strip();assert remote.split()[0]==head
manifest=P/'MANIFEST.json';m=json.loads(manifest.read_text());paths=[]
for r in m['files']:
 p=P/r['path'];assert sha(p)==r['sha256'];paths.append(p)
paths.append(manifest)
for r in m['native_review']:
 p=W/r['path'];assert sha(p)==r['sha256'];paths.append(p)
expected={str(p.relative_to(W)):hashlib.sha1(b'blob '+str(p.stat().st_size).encode()+b'\0'+p.read_bytes()).hexdigest() for p in paths}
native_dir=str((W/m['native_review'][0]['path']).parent.relative_to(W))
raw=subprocess.check_output(['git','ls-tree','-r','-z',head,'--',str(P.relative_to(W)),native_dir])
actual={}
for item in raw.split(b'\0'):
 if not item:continue
 meta,path=item.split(b'\t',1);mode,typ,digest=meta.split();assert typ==b'blob';actual[path.decode()]=digest.decode()
assert actual==expected,('published bytes mismatch',len(actual),len(expected))
changes=subprocess.check_output(['git','diff','--name-status','-z',base,head]).split(b'\0')
assert changes[-1]==b'';changes=changes[:-1];assert len(changes)%2==0
for i in range(0,len(changes),2):
 status,path=changes[i].decode(),changes[i+1].decode();assert status=='A' and path in expected,(status,path)
assert not subprocess.check_output(['git','status','--porcelain'],text=True).strip()
counts=json.loads((P/'final-counts.json').read_text());findings=json.loads((P/'finding-register.json').read_text());core=json.loads((P/'core/assembly-receipt.json').read_text())
q=S/'HANDOFF.json';assert not q.exists()
packet=dict(schema='worker05-final-scientific-correction-handoff-v1',at=datetime.now(timezone.utc).isoformat(),worker='W05',published_exact_head=head,branch=branch,
 preserved_source_head=base,ordinary_descendant_verified=True,remote_ref=remote,all_published_manifest_and_native_bytes_verified_against_git_tree=True,
 published_files=len(expected),manifest=dict(path=str(manifest),sha256=sha(manifest)),counts=counts,
 core=[dict(path=str(P/'core'/n),sha256=sha(P/'core'/n)) for n in ['decisions.json','proposals.json','evidence.json','proposal-lineage.json']],
 native_review=m['native_review'],native_verdict='needs_curation',scientific_reviews=m['independent_scientific_reviews'],final_assembly_review=m['final_assembly_review'],
 primary_scopes={lane:dict(author='/root/'+lane+'_research',cases=sum(v==lane for v in core['case_lane'].values()),payloads=sum(v==lane for v in core['proposal_lane'].values())) for lane in ['chemicals','materials','media']},
 additional_actual_review_scopes=['/root/materials_research/chemical_primary_crosscheck:28 case scopes,16 payload field sets,48 primary captures; full chemical reviewer owns the complete67case/58payload conclusion.', '/root/final_skeptical/preservation_audit: mechanical source/owner/review/comparison preservation; no chemical approval.'],
 original_finding_ids=[x['finding_id'] for x in findings['original_findings']],remaining_original_findings=[dict(finding_id=x['finding_id'],prerequisite=x['remaining_prerequisite']) for x in findings['original_findings'] if x['native_status']=='deferred'],
 new_scientific_findings=[x['finding_id'] for x in findings['new_scientific_findings']],report_findings=[x['finding_id'] for x in findings['report_findings']],
 important_boundaries=['All188 frozen source cases,388 occurrence memberships,138 original proposal origins and1879 campaign ownership boundaries retained. No whole-owner or source/export admission follows from review completion.',
 'HEPES/Wolfe/ethanol conditional matrices remain; missing details prove neither identity nor distinction. Coordinator union and Peptone dependency obligations remain separate.',
 'Monohydrate candidate uses one local form across six NBRC occurrences; no CAS, structure, chloride stoichiometry, supplier or parent guessed. Dihydrate false CAS removed without replacement; pure thiamine exact9532 and source-specific holds remain.',
 'Historical mapping evidence and component enums remain distinct. Claim-specific agent-authored typing changes do not confer new mapping or human approval.'],
 validation=dict(guarded_closed_schema='PASS142 complete payloads',strict_schema='PASS142, zero errors',full_path_overlay='PASS3029 records, component/filename/introduced-identifier checks',native_outcome_accounting='PASS188cases,142proposals,1537evidence',native_row_projection='PASS4 claims; all rows preserved/withdrawn as documented',retained_native_reviews='PASS1022 declared-scope reviews',historical_preservation='PASS2956 maintained records,1857 predecessor manifest members,390 comparison members,10shards1879cases'),
 protected_comparison_manifest_sha256=m['protected_comparison_manifest_sha256'],
 coordinator_action='Root owns deduplication, combined family/shared-owner reconciliation, final acceptance, maintained application and export approval. Worker is complete and idle. No GitHub writes, merge, force-push, paid provider, external session or downstream rebuild performed.',
 private_handoff_not_in_commit='Written after successful ordinary push to record exact final head without a self-referential commit hash.')
q.write_text(json.dumps(packet,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(dict(head=head,handoff=str(q),handoff_sha256=sha(q),manifest_sha256=sha(manifest),published_files=len(expected))))
