from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,copy
R=Path.cwd();S=R/'reports/all_unmatched_20261107/worker-10/successor-v3';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();load=lambda p:json.loads(p.read_text())
def bind(p):return {'path':str(p.relative_to(R)),'sha256':sha(p)}
def save(p,d):
 with p.open('x') as f:json.dump(d,f,indent=2,ensure_ascii=False);f.write('\n')
peer=S/'reviews/skeptic/assembly-review-v1.json';assert peer.exists();d=load(S/'HANDOFF-draft-v1.json');d['at']=datetime.now(timezone.utc).isoformat();d['status']='Bounded source/provenance correction and final assembly review complete; ready for authorized ordinary same-branch publication';d['independent_final_assembly']=bind(peer);d['reviewed_draft']=bind(S/'HANDOFF-draft-v1.json');d['final_handoff_review_path']=str((S/'reviews/skeptic/final-handoff-review-v1.json').relative_to(R));save(S/'HANDOFF.json',d)
a=load(S/'accounting.json');native=load(S/'native-v2/saved-pair.json');check=load(S/'native-check.stdout');control=load(S/'enum/claim-dispositions.json')['counts'];pres=load(S/'preservation.json')['counts'];comp=load(S/'comparison-impact.json');nfiles={Path(f['path']).suffix:f['path'] for f in native['files']}
text=f'''Worker10 completed the report-only successor for [preparation findings 1237](https://github.com/CultureBotAI/MediaIngredientMech/issues/1237) and [evidence provenance 1226](https://github.com/CultureBotAI/MediaIngredientMech/issues/1226), with disjoint primary authors and separate whole-scope skeptical review. The authoritative selection is `selection.json`, backed by `decisions.json`, `evidence.json` and `proposals.json` in this directory.

All {a['case_count']} cases and {a['source_occurrence_count']} frozen occurrences are accounted. The selected ledger contains {a['selected_proposal_count']} proposals: {a['proposal_kinds']['edit_existing_owner']} existing-owner edits and {a['proposal_kinds']['new_owner']} new-owner proposals. Eighteen source decisions were corrected and {a['retained_exact_decision_count']} remain exact. The complete bridge accounts for every predecessor proposal; no count was forced.

- Swine serum uses the authentic `UNMAPPED_0536` / MediaDive960 owner and original filename, preserving all original history. Its former new-owner proposal remains historical. The generic raw-label application hold remains.
- The parallel JCM1303 calf-serum proposal is retired from active selection. Its known heat/filter facts remain; the mixed existing owner's occurrence routing has precise unresolved prerequisites and options. No broader owner was narrowed or merged.
- Serum negative exclusions, treatment ordering and sterility are corrected without inferred missing facts. Frozen M2578 and the current ATCC reformulation retain separate version applicability.
- Difco support now binds the actual 2009 manufacturer manual, preserving older editions, search wrappers and failures. HCl comparisons retain literal percentages and conditional relations where bases are unknown.
- Of 123 audited mapping claims, {control['retyped_exact_surviving_agent_claim']} exact surviving claims were retyped, {control['superseded_by_source_reassessed_agent_claim']} were replaced by source-reassessed agent claims, and {control['historical_candidate_retired_from_active_selection']} belongs to the retired calf candidate. Two unchanged historical MappingEvidence objects remain untouched; their human authorship is not recertified. Component evidence and historical events remain intact.

The prior ISP4 payload is byte-exact. Carbonate keeps its source science and both case backlinks; only the audited evidence type and appended history change. Its pure-carbonate alias rejection remains exact. See `two-case-successor-preservation.json`.

Strict native schema checks covered 273 authentic owners and 127 selected payloads. All 127 guarded scratch copies roundtripped, and 3,037 projected records passed native partonomy. No new identifier groups or owned-name alias conflicts arose relative to the predecessor. The complete native review check passed {check['valid_reviews']} declared review scopes. The new review pair is [{Path(nfiles['.yaml']).name}](../../../../{nfiles['.yaml']}) / [{Path(nfiles['.md']).name}](../../../../{nfiles['.md']}); its per-target assessments distinguish source science, provenance-only review and retained historical science.

All {pres['old_artifacts']} prior source artifacts, {pres['owners']} maintained owners and {pres['native_reviews']} prior canonical review files remain byte-exact. The sealed 19-family comparison remains unchanged ({comp['verified_sealed_files']} verified files; no W10-authored assigned input). `comparison-impact.json` lists exact changed source bindings for other frozen reviews, including metadata-only deltas for root-owned phosphate/Columbia reconciliation.

Coordinator follow-up remains explicit: review the published head; settle Swine raw-label scope and calf occurrence routing before application; reconcile conditional preparation relationships and shared candidates; deduplicate/file the new calf-blood explanation defect before its bounded fix. The wording defect is preserved, not silently corrected. Prior ISP4 trace-stock, EDTA, source-qualified alias, role and export holds remain. No maintained data, shared source, export, gate, PR or merge changed.

`HANDOFF.json` binds the exact core, authors, reviewers, lineage and validation evidence. `SHA256SUMS` seals the successor and native review files, excluding itself. A committed handoff cannot contain its own commit hash: the exact ordinary commit/nonforce-push receipts and verified remote SHA are saved after publication under `.temp/all-unmatched-worker-10/successor-v3/completion-receipt.json` and reported to the coordinator. No scientific, whole-owner or export approval is inherited from this packet. Leave the branch and worktree intact.
'''
with (S/'HANDOFF.md').open('x') as f:f.write(text)
print(json.dumps({'json':bind(S/'HANDOFF.json'),'markdown':bind(S/'HANDOFF.md')},indent=2))
