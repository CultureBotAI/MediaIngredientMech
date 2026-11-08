# Worker 08 final coordinator handoff

The full frozen shard is complete: **188/188 cases**, **320 frozen occurrence references**, **736 evidence entries**, and **46 isolated proposals** (17 existing-owner deltas and 29 proposed new owners). All cases and proposals have separate skeptical review. No maintained data, canonical SSSOM, publication selectors or downstream products were changed. No merge, worker PR, downstream rebuild or additional external session was performed.

Branch: `review/all-unmatched-w08-source-review-20261107`. Frozen base and unmerged dependency [PR1158](https://github.com/CultureBotAI/MediaIngredientMech/pull/1158): `e000d66dd26ab053e9b17ce7bf8d3c873c3dde99`. The live dependency check is in `github/dependency-pr-1158-final.json`. The delivered commit is the commit containing this handoff; the final transport receipt and user handoff provide its exact SHA without embedding a self-referential commit hash here.

Frozen shard SHA256: `1367782d93a2a9733c6ee9fc4e1f69fbdb4ffd08ba0f7ad74849916ea34ba9e0`. The source split is 142 CultureMech and 46 KG cases (40 MediaDive, 4 MetaTraits, 2 MetaTraits GTDB). Exact cases, raw labels, all occurrences, preimages, missing requirements and preserved native holds are in `decisions.json`; `CASE-INDEX.tsv` is the navigable index.

| Final artifact | SHA256 |
| --- | --- |
| `decisions.json` | `c21fbc7eb1772f9c840900bc86c4c32eaaf061390afc518dddee8adfcb916361` |
| `evidence.json` | `b5e4ead92bc4adb35aa9b8c9938185d3107592f78a7144d776f1f34f44e9f603` |
| `proposals.json` | `167e71e699f78c40f3389c8e5000bf26303b6083c1146e35875ab53dd95d1a41` |
| `structural-audit-v2.json` | `305950704c288a50985c197c93dbb9c01cc212762c2aefd2d44b4672f22cc314` |

## Actual review scopes

| Primary author | Primary scope | Separate skeptical reviewer | Final receipt |
| --- | --- | --- | --- |
| /root/inorganics | 80 cases; 8 proposals | /root/organics | `independent/organics-reviews-inorganics/review.json` |
| /root/organics | 51 cases; 11 proposals | /root/vitamins | `independent/vitamins-reviews-organics/review.json` |
| /root/vitamins | 57 cases; 27 proposals | /root/inorganics | `independent/inorganics-reviews-vitamins/review-v2.json` |

`team-scopes.json` gives every actual case ID and exact review/input hash. Root verified baseline and live issue decisions, supplied additional primary captures, diagnosed source extraction/resolver failures, assembled and validated the bundle, and owns transport. The three in-process reviewers resolved nine scientific peer-review findings. Examples include the retired EDTA owner, unsafe CO/Co casefold alias, exact alias-source attribution, dTMP missing amount, the generic glycerol-asparagine owner versus exact JCM60 recipe, and accurate B12/B6/mineral-base hold explanations. Original versions remain preserved. Mechanical assembler review is separate from scientific approval.

## Outcomes and proposal scope

| Disposition | Cases |
| --- | ---: |
| broad_parent_relation_only | 7 |
| stock_product_mixture_context | 67 |
| new_distinct_ingredient_proposal | 33 |
| existing_identity_or_alias | 30 |
| unresolved | 41 |
| malformed_or_nonchemical_token | 7 |
| supplied_form_correction | 3 |

55 cases support one or more proposals; 131 retain a precise missing requirement. Disposition counts are case counts, not owner counts or publication approvals. Six new pure/form-specific owners plus 23 source-qualified stock/formulation owners account for the 29 new-owner proposals. Existing-owner deltas add justified raw spellings, reject foreign/hydrate-conflicting aliases, or record bounded source provenance. `proposals.json` selects exact payload paths, original before hashes, evidence, consequences and integration conditions.

## Integration dependencies and source holds

- Preserve original before-owner hashes. Shared sodium dithionite owner work overlaps worker07 [issue1169](https://github.com/CultureBotAI/MediaIngredientMech/issues/1169); reject six foreign scutellarin aliases without reviving the retired duplicate. Reconcile overlapping deltas before application.
- The sodium phosphate mono/dihydrate pair is only a staged part of [issue758](https://github.com/CultureBotAI/MediaIngredientMech/issues/758). Apply aliases, six source-label overrides, three-form membership/counts and fresh native receipts together. K2HPO4 trihydrate duplicate/grade obligations remain under issues656/901.
- New-owner native positive SSSOM admission remains an integration requirement under [issue1165](https://github.com/CultureBotAI/MediaIngredientMech/issues/1165). Do not weaken admission gates or infer admission from schema/partonomy PASS. Withdraw inherited content-bound support for every changed owner and review its full resulting payload before release.
- `CO` remains a source-specific identity assertion with no global alias proposal: the native full-index overlay conflates `CO` and `Co`. Newly filed [issue1178](https://github.com/CultureBotAI/MediaIngredientMech/issues/1178) binds the reproductions. The final peer receipt links the issue; the primary fragment was kept frozen.
- `Na` is truncated from all six Na-sesquicarbonate buffer notes by the actual source regex. Newly filed [issue1172](https://github.com/CultureBotAI/MediaIngredientMech/issues/1172) binds the exact live parser and reproduction. Do not map it to sodium metal/ion or a guessed buffer formulation.
- Source recipe quantity errors stay held: volume versus mass substitution is already tracked by CultureMech408; NBRC1601 molybdate and NBRC1394 PQQ source comparisons document scale errors. Source repair is outside this worktree. MediaDive653/552 contaminated cross-references do not override primary identities.
- Four B12 alternatives in the 4-YACo primary methods mean one chosen reagent, not a defined four-component stock. The B6 methods name two forms and a range without resolving each-versus-total allocation. Neither is promoted to an exact mixture. The direct primary factual capture preserves original URL/time/raw hash; the full article remains private.
- JCM149 Hutner and worker01 NBRC943 differ in quantities, hydration, water basis and nested Metals44 composition. `cross-shard/` and the vitamin peer receipt support distinct source formulations, without claiming review of worker01 cases. Generic starred stock labels must not become unscoped aliases.
- Sodium nicotinate and sodium ammonium phosphate tetrahydrate exact-form ontology searches are bounded observations, not universal absence proofs. Recheck current exact terms and cross-worker equivalent owners before integration.
- The generic glycerol-asparagine owner remains UNMAPPED. Its proposal records the independently verified source1754-to-JCM60 recipe while explicitly withholding equivalence of the old generic Agar-derived owner. Existing Tris, hydrate, role and inherited publication holds remain.

## Validation and native review

- Whole-shard official auditor: PASS, all188 cases, all736 evidence entries and all46 proposals; no canary/sample mode. Structural acceptance does not judge scientific truth.
- All46 selected payloads pass native closed-schema validation. Exact frozen preimages match; no duplicate proposal target or new identifier collision was found in the ignored-inclusive local catalog check.
- Native partonomy: zero violations in both the 2956-record baseline and 2985-record in-memory overlay. No catalog writes performed.
- All3043 monitored maintained files, including ignored files, have unchanged hashes and membership. `validation/combined-validation.json` records exact commands and results.
- Official auditor controls: 22 passed. Assembler controls: one positive plus eight invalid-input controls passed, preserving scientific fields and rejecting stale hashes, omissions, mutated source/occurrences/digests, duplicate IDs and self-review.
- Native formal review: [reviews/structured/20261108T053536Z-w08-final-isolated-proposals/review.yaml](../../../reviews/structured/20261108T053536Z-w08-final-isolated-proposals/review.yaml) and [derived Markdown](../../../reviews/structured/20261108T053536Z-w08-final-isolated-proposals/review.md), verdict `pass_with_limitations` for all46 proposed deltas. Root declares its assembly self-review accurately; independent scientific receipts remain separate. Source-only cases without a MIM owner stay in the campaign format and never receive invented owners.
- The final branch review checked the actual staged paths/blobs and byte-preserving archive remediation. `git diff --check` reports whitespace in retained primary HTML/text and historical validator output; those evidence bytes were deliberately preserved. The derived case index uses LF line endings. This is not a clean-whitespace claim.
- `validation/native-review-check.log` records the immutable native review check. Full maintained-data sync/QC, release approval and downstream rebuilds are not applicable to this proposal-only shard and were not run.

One early auditor-test invocation failed from inherited pytest coverage options; the corrected standalone invocation passed without changing project gates. An initial native draft was rejected for YAML aliases, corrected before any save using a no-alias dumper, and successfully validated/saved. Both actual failure logs remain. Final artifact review finding FBR-001 separately identified two oversized literature archives and a derivative text extraction; original bytes were preserved privately and replaced with bounded factual captures, with an independent applicability recheck, versioned evidence and a successor native review. All scientific decisions and proposed payloads remained unchanged. The earlier native review and exact assembly inputs remain immutable history. A public evidence fetch was once denied by automatic review; the permitted web/read-only route supplied the evidence and no work remains blocked. No permission or model/account settings were changed.

## Delivery

Only this report tree and the new native review pair are eligible for the worker commit. `SHA256SUMS` is the final repository-relative file manifest. The final branch reviewer inspects this exact artifact scope before transport. The coordinator must integrate nonconflicting proposals through guarded writers, perform complete native owner/export review, synchronize maintained surfaces and generate coherent downstream outputs separately. This worker leaves the branch and session intact after ordinary non-force push.
