from pathlib import Path
import json,hashlib,collections,datetime
R=Path.cwd();O=R/'reports/all_unmatched_20261107/worker-05';D=json.loads((O/'decisions.json').read_text())['decisions'];P=json.loads((O/'proposals.json').read_text())['proposals'];E=json.loads((O/'evidence.json').read_text())['evidence'];counts=collections.Counter(d['disposition'] for d in D);native=R/'reviews/structured/20261108T052743Z-worker05-source-bound-owner-proposals';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
lines=['# All 188 source-case outcomes','', 'Every row below has primary/source-context evidence and a separate skeptical assessment in the canonical JSON. A supported disposition does not approve the source case, complete owner or export.','']
for i,d in enumerate(D):
 lines += ['## '+str(i)+' — '+(d['source']['raw_source_label'] or '(blank source label)'),'', '`'+d['case_id']+'` · '+d['disposition']+' · reviewer '+d['independent_review']['status'],'',d['reasoning'],'',d['applicability'],'',('Proposal: '+', '.join(d['proposal_ids'])) if d['proposal_ids'] else 'No owner edit: '+d['no_change_reason'],'']
 if d['missing_requirement']:lines += ['Remaining requirement: '+d['missing_requirement'],'']
 lines += ['Primary author: '+d['primary_author']+'. Evidence: '+', '.join(d['evidence_ids'])+'. Independent review: '+', '.join(d['independent_review']['evidence_ids'])+'.','']
(O/'CASE_REVIEW.md').write_text('\n'.join(lines))
artifacts=['decisions.json','evidence.json','proposals.json','structural-audit-v1.json','review-bindings.json','subagent-scopes.json','cross-shard-dependencies.json','validation/proposed-validation.json','validation/assembly-controls.json']
hashes={p:sha(O/p) for p in artifacts};hashes.update({str(p.relative_to(R)):sha(p) for p in [native/'review.yaml',native/'review.md']})
rows='\n'.join('| '+k+' | '+str(v)+' |' for k,v in sorted(counts.items()))
props='\n'.join('| `'+p['proposal_id']+'` | `'+p['owner_path']+'` | '+str(len(p['case_ids']))+' |' for p in P)
issues='[1176](https://github.com/CultureBotAI/MediaIngredientMech/issues/1176), [1177](https://github.com/CultureBotAI/MediaIngredientMech/issues/1177), [1180](https://github.com/CultureBotAI/MediaIngredientMech/issues/1180)'
text=f'''# Worker05 coordinator handoff

Complete source review of **{len(D)}/188 cases**, including **{sum(len(d['occurrence_ids']) for d in D)} explicit CultureMech occurrences**, with **{len(E)} evidence entries** and **{len(P)} isolated proposals affecting {sum(bool(d['proposal_ids']) for d in D)} source cases**. Every final case has separate skeptical review; 17 outcomes remain scientifically unresolved with exact next requirements. All negative source/owner/export holds remain.

Assigned branch: `review/all-unmatched-w05-source-review-20261107`. Frozen base: `e000d66dd26ab053e9b17ce7bf8d3c873c3dde99`; assigned dependency PR1158. Exact shard SHA256: `457c957af21271b120190093dd311bf4044b82a3ad26b54e2fc5b52083dec1c4`. The final commit/push SHA and manifest hash are recorded after publication in `.temp/all-unmatched-worker-05/coordinator-handoff.json` and the session's final response, avoiding a self-referential commit receipt.

No maintained YAML, collection, canonical SSSOM, unified snapshot, release selector or downstream output was changed. No merge, worker PR, paid research or additional external session was performed.

## Case accounting

| Disposition | Cases |
|---|---:|
{rows}

KG cases retain their full raw observations and source holds through exact case digests; their empty explicit occurrence-ID arrays do not mean zero observations. {sum(not d['owner_records'] for d in D)} source-only cases have no invented MIM owner. All case reasoning is readable in [CASE_REVIEW.md](CASE_REVIEW.md).

## Review and verification

Primary scopes: root25, media60, materials61, chemicals42. Separate skeptical scopes: media reviewed root25+chemicals42; chemicals reviewed materials61; materials reviewed media60. Exact scopes, reviewed hashes, limitations and original findings are in `subagent-scopes.json`, `review-bindings.json` and the referenced reviews. Concrete corrected findings include unsupported root functional subtype, incomplete owner bindings, tellurite misidentified as dioxide, unsupported Sea Salts closeMatch, empty JCM HTTP200 response and unsupported supplier-form assertions. Historical candidate-byte limitations are explicit in README/review receipts.

- Whole-shard auditor: PASS, 188/188 accounted, 188 independent statuses complete, `scientific_adequacy_or_approval_established: false`.
- Strict native candidate schema: 21 files, zero errors.
- Native component validator: baseline and in-memory proposed corpus both zero violations; no maintained write.
- Auditor synthetic controls: 22 passed. Assembly controls: seven passed, including stale/open/pending/duplicate failures and exact nested owner-hold preservation.
- Native `inspect`, `validate`, `save`: saved 105 scoped targets (84 baseline owners +21 exact proposed payloads), verdict `needs_curation`, reviewer `self_review`; separate skeptical evidence is retained. Review: [{native.name}/review.yaml](../../../{str((native/'review.yaml').relative_to(R))}), [derived Markdown](../../../{str((native/'review.md').relative_to(R))}). Native `check --base` passed (1020 valid saved reviews, declared scopes only). Final diff review receipts/logs accompany this bundle.
- Optional whitespace diff check returned 17 cosmetic trailing-space warnings in native saver-rendered Markdown. The immutable native pair was preserved and passes native check.
- Full maintained-data sync/export/QC and downstream builds were not run: integration belongs to the coordinator. No native or structural result grants release approval.

## Exact proposed changes

| Proposal | Maintained owner | Source cases |
|---|---|---:|
{props}

Proposal bytes are under the author directories, bound by exact before-owner and after-payload SHA256 in `proposals.json`. Thiamine and L15/ISP7 source-stock aliases remain unmapped where specified. Peptone, salicin and chloride-specific label rejections preserve provenance. Local-registry changes identify source preparations, without unsupported generic parent relations or function assignments.

## Dependencies and remaining decisions

`cross-shard-dependencies.json` distinguishes84 referenced owners from21 proposed owners and records18 owners with other-shard frozen hints. Compare every campaign worker's actual proposed-owner inventory before integrating; frozen hints miss source-only discoveries. The pure thiamine-pyrophosphate owner is explicitly shared with worker09: retain CAS136-09-4, exact9532 WITHHOLD and prior319/320 reasoning; chloride CAS154-87-0 is distinct. The source778 counterion/protonation and complete published payload remain unresolved. The0.2%stock andJCM403bufferedstock are separate.

Other exact requirements include tartrate stereochemistry, thiamine hydrochloride monohydrate specification, guanine hydrochloride form, EDDS stereochemistry/source handles, 3-O-methyl sugar anomer/aglycon, iron-citrate specification, ATCC2811 Wolfe formulation, historical BBL/Oxoid peptone catalogs and the unnumbered albumin fraction. Bacteriocin producer reclassification is supported, but peptide provenance and the CHEBI204272 structure discrepancy still block exact promotion. All remaining requirements are enumerated per case.

Deduplicated new findings: {issues}. Existing source-unit/hierarchy defects retain CultureMech408/150/214 references; UCM frozen TeO2/stock recurrence retains276/283 with their captured status distinctions. Existing MIM718/902/1157/1165 and relevant prior decisions are preserved. The issue bodies, original timestamps, live searches/comments and filing receipts are in `issues/`.

## Artifact hashes

| Artifact | SHA256 |
|---|---|
'''+ '\n'.join('| `'+p+'` | `'+h+'` |' for p,h in hashes.items())+'''

`MANIFEST.sha256` covers the final worker evidence files (excluding itself). The saved native review pair is separately hash-bound above. Final publication receipt verifies the exact remote branch/head and unchanged maintained surfaces. Leave this branch and worktree intact for coordinator integration.
'''
(O/'HANDOFF.md').write_text(text);(O/'handoff-artifact-hashes.json').write_text(json.dumps(hashes,indent=2)+'\n');print(len(D),len(E),len(P),'handoff written')
