from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
read=lambda n:json.loads((R/n).read_text())
sha=lambda n:hashlib.sha256((R/n).read_bytes()).hexdigest()
rows=read('allowlist-proof.json')['entries']
table='\n'.join('| '+str(r['flag_index'])+' | '+r['proposal_id']+' | `'+r['field']+'` | `'+r['after_payload_sha256']+'` |' for r in rows)
text='''# Worker09 provenance-only successor for issue1226

Eight confirmed new-agent MappingEvidence entries have been corrected from `MANUAL_CURATION` to `LLM_SUGGESTION`, each with one native appended curation event. The eight complete payloads are isolated report candidates. Nothing was applied to maintained owners. This successor preserves the complete scientific claims, identities, predicates, mapping quality, source text, notes, properties, components, quantities, synonyms, roles, status and all prior history.

The dispatched assignment SHA256 is `5b52e6967ef232e3507b8425934c43127549728ce0170d1d621ac5b4d5977fe7`. The user's dispatch authorizes ordinary commit and non-force push after checks and independent review, superseding the draft's deferred-dispatch language. Accepted source head is `77d6beaea5793a0a763957b99e8141ff12b216d2` on `review/all-unmatched-w09-source-review-20261107`. Local HEAD and the live remote branch matched before work; exact selection, current cores and Git blobs matched all dispatch pins. No unexpected work was overwritten.

## Exact changes

| Audit flag | Original proposal ID retained | Only existing field changed | New complete payload SHA256 |
|---|---|---|---|
'''+table+'''

Each correction preserves the original evidence object's `source`, `notes` and all other keys and values. The full object and its parent mapping were rebound to the original raw payload, rather than matched by array position or citation alone. Each added history event identifies Codex worker09, `llm_assisted: true`, the exact field, flag and original complete-object hash, issue1226, and the absence of scientific or release changes. Original history is an exact ordered prefix. Original native formatting is retained: each textual diff removes exactly one old evidence-type line and adds its replacement and the appended event.

The maintained `EvidenceTypeEnum.MANUAL_CURATION` specifically describes evidence supplied by a human reviewer. These eight entries contain new worker-agent identity, source-applicability or formulation judgments. Their cited database, manufacturer or publication is not the author of the MIM curation judgment. LLM_SUGGESTION records that attribution without changing the claim. The audit's conditional DATABASE_MATCH alternatives were not selected; no statement was narrowed or rewritten to manufacture a database-only assertion. `evidence_source`, component evidence and SSSOM justification vocabulary are distinct and unchanged.

The separately ambiguous historical Casamino `ontology_mapping.evidence[1]` remains exact, including its newer historical wrapper and older #263 claim. Its canonical complete-object SHA256 remains `172fc3c050e5737dfc774001fa18e3263d7c33242119f5a00aec64fc2fd915c9`. Older process history and the wrapper do not establish who supplied the original evidence. The new Casamino evidence[2] is the independently justified correction. No ComponentEvidenceTypeEnum field was changed.

The full issue1226 body, all five comments returned at preflight and final audit comment6718717543 were read and captured. The W02 provenance ledger and type matrix were rehashed at `98bfa525356aa223a08fcd2be11d9dc7476231aa6cd9efa4db1f85b2e66109e2` and `9ca6b04f03fdaabd65dacd90a160cf9f51dc549e607b5f5634616469532f1b33`. The complete nine W09 rows are retained in `inputs/w02-nine-row-audit-extract.json`; they provide attribution evidence, not renewed scientific mapping approval. All 135 planning-packet members were verified.

## Complete retained population

`selection.json` explicitly bridges all 32 original proposal IDs: eight new full payload hashes and 24 byte-identical retained payloads. `proposals.json` retains every complete proposal object; only the eight selected `after_capture` paths/hashes change. Capture paths remain relative to the original worker09 artifact root. All original proposal IDs, cases, owner paths, explanations, evidence references and publication obligations remain.

`effective-decisions.json` is a raw-byte copy of the accepted `followups/hexahydrates-v1/validation/integrated-decisions.json`, SHA256 `ff27e5f3b5663ab977e9c9b2b01861b4e1c5c8eed3bd6e7d0e1fbae652a58e8e`. All 187 complete effective outcome objects, source labels/kinds, case-input hashes, occurrences, evidence references and holds remain unchanged. `outcome-retention.json` binds each case to its exact frozen original and effective decision. The two superseded original CoCl2/NiCl2 cases remain superseded by the accepted follow-up; this packet does not revert to the earlier root decisions or widen source-association-only conclusions.

All 1,233 predecessor W09 report files remain byte-identical. Their evidence captures and original independent reviews remain authoritative historical receipts within their recorded scope. The sealed companion437-member, W04 1,730-member and W06 11,215-member packets retain their exact files, membership and manifests. No old report was rewritten. The predecessor source head remains available in Git.

## Guards, controls and validation

The native `record_curation_event` helper appends the event and `write_validated_ingredient` performs closed-schema validation and serialization. A narrow wrapper supplies an exclusively reserved output file descriptor, checks lexical/real path containment and directory aliases, refuses existing paths, uses O_EXCL/O_NOFOLLOW, and checks reserved inode identity and link count. The native writer itself is not described as providing those reservation protections. All eight planned content objects and destinations are checked before the first candidate write. Partial artifacts would be retained on failure; no hostile-concurrency or atomic eight-file transaction guarantee is claimed.

The allowlist proof restores only the permitted enum and removes only the one exact appended event, then requires equality of the complete reconstructed object to the predecessor. This detects edits to source/notes, all scientific fields, components, aliases, roles, mapping context or history. Parent mapping hashes, full evidence-object hashes and each top-level field hash are recorded.

All 32 serialized selected payloads pass native closed-schema validation. Native synonym resolution and grading-based identity/ontology projection are unchanged for every payload, including the unchanged unresolved owner with no ontology mapping. These are consistency checks, not a generated export or release gate. No shared SSSOM, KGX, aggregate, canonical, workflow, pin or gate was changed or rebuilt.

The final focused controls pass **28/28**. They include stale payload and complete-object checks; wrong and duplicate field selection; accidental component-enum edits; historical Casamino retyping; changes to source, scientific claims, aliases, roles or identity; history loss/addition; omitted or duplicate case/proposal; altered outcome; pre-existing, symlink and hardlink outputs; symlink parents; out-of-bound and dot-dot paths; exact positive native writing; all-eight schema/projection checks; and the unresolved no-mapping projection. Original 27-control results and the later 28-control run are both retained.

Failed probes are explicit. Initial sandbox DNS checks failed before authorized read-only retrieval succeeded. The first broader32 validator assumed an ontology_mapping on an unchanged unresolved record and raised KeyError; its exact failure and helper sources are preserved in `validation/probes/`. The corrected validator represents absence without inventing a row. This was a private check-helper error, not a payload or scientific finding. No candidate was changed to make the check pass and no gate was weakened.

## Review and publication boundary

The separate final reviewer is `/root/provenance1226_reviewer`, who did not author W09 or this successor. Its exact full-payload attribution assessments, all187/32 retention checks, historical exception check, writer/control assessment and native review pair are retained under `independent-review/`. Review completion authorizes only this provenance successor within its stated limits. `scientific_review: false` is required: chemistry, source applicability, roles, inherited whole-owner claims and publication support were not renewed.

Current identity/formulation/source assertions and their genuine uncertainties remain exactly as authored. Historical Casamino roles, source-specific stocks, unqualified form questions, primary-term/owner integration obligations and every existing role/export WITHHOLD remain. No audit verdict becomes a scientific approval. No new scientific finding, issue mutation, person mention, paid provider, external session, maintained write, merge or deletion is part of this task.

The publication manifest seals the completed report packet. After the ordinary commit, every report member, selected payload and native input is rebound to exact committed blobs, and the live remote head is checked after the non-force push. Those publication receipts live in the durable private task directory and the final handoff reports the resulting exact head; embedding a commit's own hash in its contents would be self-referential.
'''
with (R/'REPORT.md').open('x') as f:f.write(text)
print('REPORT.md',sha('REPORT.md'))
