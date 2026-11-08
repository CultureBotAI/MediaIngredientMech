import datetime,hashlib,json,shutil,subprocess
from pathlib import Path
R=Path.cwd();P=R/'.temp/all-unmatched-worker-08/plain-flour-process-replay-v1';A=R/'reports/all_unmatched_20261107/worker-08';O=A/'process-replays/plain-flour-v1'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def ref(p):return {'path':str(p.relative_to(R)),'sha256':sha(p)}
def save(p,x):
 with p.open('x') as f:json.dump(x,f,indent=2,ensure_ascii=False);f.write('\n')
assert read(O/'independent/review.json')['status']=='PASS';assert read(O/'independent/final-bindings.json')['status']=='PASS'
n=read(O/'native/receipt.json');assert n['status']=='PASS'
subprocess.run(['git','diff','--exit-code','HEAD','--'],check=True,capture_output=True)
head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip();assert head=='4a4042561328f2a507770d3c85100a7790855aaa'
assert (P/'receipts/remote-before.txt').read_text().split()==[head,'refs/heads/review/all-unmatched-w08-source-review-20261107']
for name in ['seal.py']:shutil.copy2(P/name,O/'provenance'/name)
for name in ['native-review.log','checks.log','remote-before.txt']:shutil.copy2(P/'receipts'/name,O/'provenance'/name)
replay=read(O/'replay/receipt.json');assert replay['complete_payload_bytes_equal'] and replay['complete_final_event_equal'] and replay['selected_record_events_added']==0
handoff={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'COMPLETE_IMMUTABLE_PROCESS_REPLAY; coordinator_final_head_disposition_pending','finding_id':'W08-PF-PROCESS-001','finding_alias':'W08-PF-WORKFLOW-001','issue':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1227#issuecomment-6719637789','branch':'review/all-unmatched-w08-source-review-20261107','parent_head':head,'original_author_script_sha256':'1790bb6525e047fde7158a4f84ab9a623de43ba8b4a85aa96fc09b5244d8b0c0','predecessor_payload_sha256':replay['predecessor_sha256'],'selected_and_replay_payload_sha256':replay['selected_payload_sha256'],'complete_event_and_payload_equivalent':True,'semantic_differences':[],'historical_event':replay['historical_event'],'actual_replay_time':replay['replayed_at'],'selected_history_events_added':0,'selected_source_payloads_changed':0,'new_source_cases':0,'new_source_proposals':0,'active_source_selector_unchanged':ref(A/'successors/issue-1237-tenvit-v1/selection.json'),'active_source_counts':read(A/'successors/issue-1237-tenvit-v1/selection.json')['counts'],'replay_script':ref(O/'provenance/replay.py'),'replay_receipt':ref(O/'replay/receipt.json'),'replay_specimen':ref(O/'replay/Plain_Flour.yaml'),'native_call_proof':'receipt.actual_calls records real native code objects: one record_curation_event with llm_assisted=True and exact historical kwargs, then one write_validated_ingredient; no mocks.','author_controls':ref(O/'controls/receipt.json'),'independent_review':ref(O/'independent/review.json'),'independent_final_bindings':ref(O/'independent/final-bindings.json'),'native_review_yaml':n['review_yaml'],'native_review_markdown':n['review_markdown'],'native_receipt':ref(O/'native/receipt.json'),'preservation':ref(O/'preservation.json'),'reviewer_identity':'worker08:/root/inorganics, separate from replay author worker08:/root; prior Plain Flour skeptical involvement disclosed','scientific_review':False,'scope':'Immutable workflow evidence only. Old script remains an honest direct-append execution record. Replaying the original transition does not append another event to or replace the selected scientific payload. No current primary lookup, chemical reassessment or experimental evidence is claimed.','holds':'All source/scientific/owner/role/export holds remain, including separate PF-LINEAGE-001, Trypticase/Bacto FAILED/HELD and nominal vitamin central reconciliation.','failure_preservation':'Initial preflight sibling-path error preserved with corrected path successor; no native/source failure concealed.','publication_receipt':str((P/'publication-receipt.json').relative_to(R)),'maintained_edits':False,'GitHub_mutation':False,'paid_research':False,'external_sessions':False,'release_approval':False}
save(O/'HANDOFF.json',handoff)
with (O/'HANDOFF.md').open('x') as f:f.write('''# W08 Plain Flour native-event-helper replay

W08-PF-PROCESS-001 was filed on issue1227 comment6719637789 before this follow-up. The published author script and its truthful history remain unchanged. This new evidence packet reconstructs the original correction from the exact five-event predecessor using `record_curation_event(..., llm_assisted=True)` and `write_validated_ingredient`.

The complete resulting sixth event, complete six-event history, full record and serialized payload equal the published `884fee1ea6a5082a51b8769f2a827199b1703972ad80fa48e1bb8d2d09ab3873` bytes. Original timestamp2026-11-08T08:38:45.690887+00:00, attribution and meaning remain exact; actual replay time is recorded separately. No second/no-op event is appended to the selected record, no changed candidate is selected, and no source case is invented.

The actual independent reviewer `/root/inorganics` inspected and executed the workflow, verified complete equivalence and actual native calls, and exercised meaningful negative controls. Its prior Plain Flour reviewer involvement is disclosed; the replay author is `/root`. Native YAML/Markdown records process evidence only (`scientific_review: false`). This is no fresh chemical/source review and grants no role, owner or export approval.

The active vitamin selector and all188cases/114proposals/320occurrences remain unchanged. The full vitamin and Plain Flour manifests were rehashed. All prior source work and frozen review packets remain intact. Existing PF-LINEAGE-001 and Trypticase/Bacto FAILED/HELD, all scientific/role/export holds and nominal vitamin reconciliation remain separate.

`HANDOFF.json` binds the exact replay script, runtime call trace, complete payload/event proof, independent controls/review, native pair, current source selector and preservation receipt. The new ordinary commit adds evidence only; no old scientific or workflow artifact is rewritten. Coordinator final-head acceptance and issue disposition remain separate.
''')
paths=[f for f in O.rglob('*') if f.is_file()]+[R/n['review_yaml']['path'],R/n['review_markdown']['path']]
assert len(paths)==len(set(paths)) and not any(p.is_symlink() for p in paths)
manifest=O/'MANIFEST.sha256'
with manifest.open('x') as f:
 for p in sorted(paths):f.write(sha(p)+'  '+str(p.relative_to(R))+'\n')
for line in manifest.read_text().splitlines():digest,path=line.split('  ',1);assert sha(R/path)==digest
save(P/'precommit-seal.json',{'status':'PASS','parent_head':head,'manifest':ref(manifest),'manifest_members':len(paths),'handoff':ref(O/'HANDOFF.json'),'replay':ref(O/'replay/receipt.json'),'source_selector':ref(A/'successors/issue-1237-tenvit-v1/selection.json'),'native':n})
assert not subprocess.check_output(['git','diff','--cached','--name-only']).strip()
paths.append(manifest)
for p in paths:assert subprocess.run(['git','cat-file','-e','HEAD:'+str(p.relative_to(R))],capture_output=True).returncode!=0
with (P/'publish-paths.nul').open('xb') as f:f.write(b'\0'.join(str(p.relative_to(R)).encode() for p in paths)+b'\0')
print(json.dumps(read(P/'precommit-seal.json'),indent=2))
