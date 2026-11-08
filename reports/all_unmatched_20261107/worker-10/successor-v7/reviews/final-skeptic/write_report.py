"""Persist the bounded final assembly review after actual checks; no source writes."""
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib
P=Path(__file__).resolve().parent
R=Path.cwd();S=R/'reports/all_unmatched_20261107/worker-10/successor-v7'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ref(p):return {'path':str(p),'sha256':sha(p)}
def read(p):return json.loads(Path(p).read_text())
checks=read(P/'final-assembly-checks-v3.json')
assert checks['status']=='PASS' and all(x['passed'] for x in checks['checks'])
command=read(P/'check-v3-command.json')
assert command['exit_code']==0
native=read(S/'native-v3/saved-pair.json')
report={
 'review_id':'worker10-columbia-controls-final-assembly-review-v1',
 'reviewer':'worker10:/root/buffers_research',
 'verdict':'pass_with_limitations',
 'status':'PASS_BOUNDED_FINAL_ASSEMBLY_METADATA_NATIVE_AND_RETENTION',
 'completion':'completed',
 'scientific_review':False,
 'findings':[],
 'timing':{
  'exact_first_read_utc':None,
  'qualification':'Final metadata and native document reading began before the retained audit commands; exact first-reading start was not recorded. These command intervals are actual execution times, not the entire review interval.',
  'first_retained_audit_started_at':read(P/'check-v1-command.json')['started_at'],
  'successful_audit_started_at':command['started_at'],
  'successful_audit_finished_at':command['finished_at'],
  'successful_audit_runtime_seconds':command['runtime_seconds'],
  'review_completed_at':datetime.now(timezone.utc).isoformat()},
 'authorship_and_independence':{
  'current_root_author_independent':True,
  'prior_authorship':'I authored the original W10 Tris/HCl0.2M DSM273 and HEPES2M JCM556/1200 proposals, other W10 buffer/HCl proposals and later serum corrections. I did not author the current root S7 payloads, original W10 Difco/Oxoid payloads or W04 source origin. I performed previous technical/metadata and some independent scientific reviews elsewhere in this ongoing campaign.',
  'current_scope':'Independent of root final assembly authorship for technical/metadata integrity only. This does not independently approve original buffer science or renew scientific acceptance for unchanged records.',
  'source_science':'The separate /root/preparation_skeptic report is the author-independent source-science review; its exact author-v3 scope, source reads, prior skeptical involvement and limitations are retained.',
  'other_reviewer':'The /root/bio_research lineage reviewer discloses original Oxoid and later Difco-support authorship and supplies metadata review only.',
  'native_wrapper':'Root authored the native wrapper and correctly declares self_review. No human-review or historically uninvolved-review claim is made.'},
 'reviewed_author_freeze':ref(S/'author-freeze-v3.json'),
 'reviewed_selector':ref(S/'selection.json'),
 'final_core':read(S/'selection.json')['authoritative_core'],
 'reviewed_handoff':ref(S/'HANDOFF-author.json'),
 'counts':checks['counts'],
 'exact_scope':{
  'all_selected_payload_bytes':128,
  'all_case_objects':188,
  'assigned_CultureMech_occurrence_ids':304,
  'complete_bridge_rows':316,
  'evidence_objects_and_capture_bindings':1229,
  'all_original_evidence_objects_retained':1218,
  'author_v3_evidence_prefix_retained':1224,
  'new_final_metadata_evidence':5,
  'maintained_owner_hashes_verified_against_frozen_independent_baseline':2956,
  'current_maintained_mapped_unmapped_yaml_count_observed':2956,
  'contract_hashes_verified':15,
  'native_targets':325,
  'native_assessments':325,
  'native_input_bindings':1053,
  'native_bounded_primary_science_check_targets':checks['native_science_targets'],
  'fresh_science_by_this_reviewer':False},
 'assessments':[
  {'area':'final metadata delta','outcome':'supported','detail':'Compared every author-v3 and final core field. Only decisions80/118/135/178 and five proposal objects gain actual review evidence/status/pointers, bounded current-scope wording and historical-enum recheck references. All other author-v3 objects are exact. The full literal changes are retained in final-assembly-checks-v3.json; no scientific payload or original history changed during finalization.'},
  {'area':'complete source/proposal retention','outcome':'supported','detail':'Independently recomputed every complete-bridge before/after canonical hash, source/raw-case binding, occurrence list, owner record, proposal ID association, selected capture, maintained beforehash and unchanged flag. All188case/304occurrence membership and127original proposal IDs persist; one genuine existing-owner dependency is added. No sourcecase, vendor identity, foreign owner or prototype enters the W10 selector.'},
  {'area':'payload/owner continuity','outcome':'supported','detail':'All128selected files match actual selector and final proposal hashes and reviewed author-v3 payloads. Relative to c66, three original payloads change and124 remain exact. The new0118 candidate has actual29ed maintained beforeimage and0bbc afterimage; Difco/Oxoid new-owner null beforeimages remain null. All2956 frozen maintained owner hashes and15 native contracts remain exact. No tracked source mutation was present at the audit.'},
  {'area':'source routes and foreign origin','outcome':'supported','detail':'The final route/cross-worker ledgers differ only in completed-review receipts and finalization metadata. All seven original raw rows, recipe captures, retrieval metadata, literal quantities and holds are exact to author-v3. Three bounded Difco dry contexts are supported; four prepared1L Oxoid contexts retain null target routes. Each coupled0118 dependency binds the actual samepath before/after. Actual W04 and W10 Oxoid source origins and the5846prototype remain read-only inputs; a single composed family candidate remains a coordinator prerequisite.'},
  {'area':'actual reviewer attribution','outcome':'supported','detail':'The science/lineage/technical reports and all canonical technical support copies match their frozen exact bytes. The native self_review declaration and subagent-scopes accurately distinguish source science from original-author technical/lineage review. Independent_review=complete is bounded candidate review, not unchanged whole-owner acceptance or source application.'},
  {'area':'native complete pair','outcome':'supported','detail':'Freshly loaded the actual saved YAML using scripts/record_review.py, ran native validate_review, and reproduced native render_markdown byte-exact. All325targets are declared and assessed exactly once; each of128proposal target paths and188case selectors binds the effective bytes. All1053input files and19native evidence snapshots match actual hashes. Native source is c66 working_tree, not a future commit. The PRIMARY-SCIENCE check is restricted to14 declared targets; other coverage is retention/native validation.'},
  {'area':'native execution and timing','outcome':'supported','detail':'Read successful inspect/validate/save receipts and preserved two failed root attempts. The native started_at equals the retained preflight milestone; it does not establish an earlier cognitive start. Nine reused primary evidence timestamps preserve their original UTC instants and original literal strings in summaries. Ten current local report/validation re-reads have later actual access timestamps. Eleven additional v3input files are exclusively the retained v2failed-attempt artifacts and author script; all1042preceding inputs remain exact.'},
  {'area':'handoff and limits','outcome':'supported','detail':'HANDOFF-author.json exactly binds the selector, effective core, complete counts, review receipts, saved native pair, held context routes, genuine owner dependency and authentic W04origin. It explicitly leaves final assembly/publication and future published-head review pending, and gives no arbitrary combined Oxoid owner or inherited whole-owner/role/export approval. Root may append the actual final receipt binding and seal afterward; those future bytes are not reviewed here.'}
 ],
 'fresh_executions':{
  'successful_command':ref(P/'check-v3-command.json'),
  'actual_checker':ref(P/'check_final_assembly_v3.py'),
  'complete_results':ref(P/'final-assembly-checks-v3.json'),
  'assertions':len(checks['checks']),
  'distinct_input_paths_recorded':len(checks['input_hashes']),
  'exit_code':0,
  'stderr':'Only the native LinkML topClass deprecation message. No validation error.',
  'broad_suite_rerun':False},
 'native_pair':native,
 'exact_review_dependencies':[
  ref(S/'reviews/science/scientific-review-v1.json'),
  ref(S/'reviews/lineage/author-v3-lineage-review.json'),
  ref(S/'reviews/technical/author-technical-review-v1.json'),
  ref(S/'reviews/final-lineage/final-core-lineage-review-v1.json'),
  ref(S/'subagent-scopes.json')],
 'reviewer_method_diagnostics':[
  {'attempt':ref(P/'check-v1-command.json'),'checker':ref(P/'check_final_assembly.py'),'cause':'My first checker incorrectly required all native evidence access timestamps to preserve one instant. That rule applies to reused primary retrievals, whereas actual local report re-reads legitimately have later access times. Failed script/stdout/stderr retained. No target correction required.'},
  {'attempt':ref(P/'check-v2-command.json'),'checker':ref(P/'check_final_assembly_v2.py'),'cause':'The second checker omitted the legitimate11input additions preserving the prior failed native attempt. Direct per-input comparison found no removals/changed preceding objects. V3 requires exactly the enumerated11retained-attempt artifacts and verifies every actual hash. Failed script/stdout/stderr retained. No target correction required.'}
 ],
 'limitations':[
  'This review verifies final assembly metadata/native integrity and preservation, not fresh original source science. I am the original author of controls941/955.',
  'The four changed records and unchanged Oxoid source origin have the separately attributed bounded science review; 325native targets do not mean325fresh scientific approvals.',
  'All original source, quantity, chemistry, source-version, owner, role and export holds remain. Generic compound2046 and nominal preparation names acquire no global identity.',
  'The four prepared-base contexts cannot be converted to dry39g. Coordinator must compose and review one final Oxoid family owner from authentic W04/W10 inputs before application.',
  'No maintained-data/source mutation, schema/gate change, synchronization, downstream rebuild, external session, paid research or Git/GitHub write was performed by this reviewer.',
  'No future commit/head, final seal, staged-file set or coordinator acceptance is approved by this prepublication review. A later appended handoff/manifest and final published-head check remain separate.',
  'Full native corpus check is not rerun here; fresh checks validate this exact saved pair and all its declared inputs. Source-author focused payload/overlay checks remain bound by exact immutable receipts.',
  'Preservation here directly covers all selected payloads, case/proposal/evidence objects and captures, full maintained-owner baseline, contracts and frozen technical subtree. Broader historical-seal claims retain the attributed preflight and lineage proofs rather than an invented repeat audit.'
 ],
 'application_or_publication_approval':False,
 'new_scientific_finding_or_issue_closure':False,
 'write_scope':'Only .temp/columbia-controls-successor-v1/final-skeptic; no prior technical artifact or input was changed.'
}
rp=P/'final-assembly-review-v1.json'
with rp.open('x') as f:json.dump(report,f,indent=2,ensure_ascii=False);f.write('\n')
md='''Final assembly metadata review: **pass with limitations**. No new findings.

Reviewed the exact S7 selector, 128 selected payloads, 188 cases, 304 assigned occurrences, 1,229 evidence bindings and all 316 complete-bridge rows. Author-v3 to final changes are bounded review metadata only. Relative to c66, 124 original payloads remain exact, three change, and one genuine existing-owner Columbia dependency is added.

The native saved pair passes the actual native validator and renders to the exact saved Markdown. All 325 targets are assessed once and all 1,053 input hashes match. Fresh source-science coverage is explicitly restricted to 14 targets. Root correctly declares the wrapper self-review; the separate scientist's scope remains distinct from the original authors' technical and lineage reviews.

Three source-specific Difco dry routes remain supported; four prepared-base contexts remain held. Genuine0118 before/after provenance and null vendor preimages are retained. W04/W10 Oxoid source inputs remain separate authentic origins pending one coordinator-composed candidate. No whole-owner, role, export or maintained application approval is given.

I authored the original Tris/HEPES target proposals. This review is independent of root final-assembly authorship and covers metadata/native integrity, not independent renewal of my original science. Two failed checker assumptions (local review-access timestamps and added failed-attempt inputs) are preserved and explicitly corrected. The successful audit executed 9,891 assertions with exit0; exact commands, results and hashes are retained.

This binds HANDOFF-author and the current prepublication c66 working tree. A later final receipt binding, manifest, staged set and published head remain outside this review. No further writes will occur in this frozen review subtree.
'''
with (P/'final-assembly-review-v1.md').open('x') as f:f.write(md)
files=[ref(p) for p in sorted(P.rglob('*')) if p.is_file()]
with (P/'REVIEW_MANIFEST.json').open('x') as f:json.dump({'at':datetime.now(timezone.utc).isoformat(),'files':files,'count':len(files),'scope':'All final-skeptic files before this manifest; immutable metadata/native review, no source-science renewal.'},f,indent=2);f.write('\n')
print(json.dumps({'review':ref(rp),'markdown':ref(P/'final-assembly-review-v1.md'),'manifest':ref(P/'REVIEW_MANIFEST.json'),'files':len(files)},indent=2))
