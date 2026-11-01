# Unified mapping redo of PR #914

This rebuild starts from MIM `2add44fbfe37544218d2f4daeb322b35debc5dd4` and ports the approved changes from `e9c3ca2`, `dec5e80`, `e30b6d0`, `b173371` and `720e2d2`. The last patch was already present after `b173371`; its intent is retained in an empty cherry-pick commit. The old merge commit and evidence-validator pin/workflow changes are excluded. The original PR branch is preserved.

The nine rejected merge tombstones now retain their explicit representatives. Wrong-form aliases remain rejected, while sodium molybdate monohydrate and trisodium citrate trihydrate retain distinct unmapped records. This does not bulk-import CultureMech ingredients. The approved issue decisions are recorded for [#869](https://github.com/CultureBotAI/MediaIngredientMech/issues/869), [#882](https://github.com/CultureBotAI/MediaIngredientMech/issues/882), [#894](https://github.com/CultureBotAI/MediaIngredientMech/issues/894) and [#808](https://github.com/CultureBotAI/MediaIngredientMech/issues/808).

## Review findings repaired

- [#1021](https://github.com/CultureBotAI/MediaIngredientMech/issues/1021): historical identifier reuse was removed. The two new unmapped records use `UNMAPPED_0851` and `UNMAPPED_0852`, selected after a Git-history and ignored-file-inclusive assignment inventory. Existing history remains intact.
- [#1022](https://github.com/CultureBotAI/MediaIngredientMech/issues/1022): a repeated tombstone repair no longer removes an earlier repair event. Regression tests prove history-prefix preservation and subsequent idempotence.
- [#1023](https://github.com/CultureBotAI/MediaIngredientMech/issues/1023): the future writer uses the correct glutamate accession (`CHEBI:29988`) and removes the unrelated citrate rationale accession. Guarded record updates append corrections without rewriting older history.
- [#1025](https://github.com/CultureBotAI/MediaIngredientMech/issues/1025): refreshed source IDs could lend unrelated identities to 33 raw labels. Merged [Claw #698](https://github.com/CultureBotAI/culturebotai-claw/pull/698), fixing [Claw #697](https://github.com/CultureBotAI/culturebotai-claw/issues/697), adds exact source-label/ID holds. All 57 existing ledger rows are preserved byte-for-byte, followed by 33 explicit blank-replacement rows. These cover 27 preparation labels, three variable-hydrate labels and three vitamin-B12 class/member labels. Each cites its source commit, path, selector and hash. No replacement identity is inferred.

The actual MIM resolver found no independent owner for any of those 33 labels. After regeneration they retain labels, counts and example media but carry no borrowed identity or synonym metadata. The independent producer probe proved that legacy behavior is unchanged without holds; applying the holds changes exactly 33 rows and leaves 4,137 unchanged. Source holds preserve independently curated owners when present. They do not globally ban an identifier or implement the later SSSOM alias policy.

## Generated artifact

| Comparison with main | Rows |
|---|---:|
| Main snapshot | 3,904 |
| Final snapshot | 4,170 |
| Added source labels | 290 |
| Removed source labels | 24 |
| Shared rows with changed fields | 1,481 |
| Unchanged shared rows | 2,399 |

The source refresh represents 209,330 occurrences across 15,915 CultureMech recipe files. Final statuses are 2,629 `MAPPED`, 1,424 `UNMAPPED`, 94 `TERM_ID_NO_MIM`, and 23 `CHEBI_NO_MIM`. Added/removed labels reflect the source snapshot, not ingredient-record import/deletion. Among shared rows, changes include occurrence counts (1,353), examples (549), source IDs (291), synonyms (160), statuses (105), MIM identities (42), CHEBI IDs (80), CAS values (32), and KG-Microbe node IDs (18); these field counts overlap. The [complete main-row delta](checks/source-hold-final/unified-main-delta.json) and [33-row withdrawal delta](checks/source-hold-final/source-hold-row-delta.json) preserve every changed value.

Final TSV SHA-256: `fd9a44beb940d8bc484a633f562de95a13e1f75a6e01c42b8965356800f1b215`. Both required rejection counts are zero: no REJECTED row has an empty MIM identity, and no `kgmicrobe.compound` row carries CHEBI in an identity column. All nine representatives pass the explicit regression.

Canonical SSSOM is byte-identical to main: 2,987 rows, SHA-256 `a2b83ccdcaad67d89943ccf0f0e30d796cdbc5e418ead247313631b713e89722`. Receipt replay preserves 1,740 supported and 1,247 withheld mappings. The current semantic review was regenerated for the changed records and complete graph. Its integrity passes; the full scientific release remains FAIL with 1,733 blocking findings and 2,272 assertions. This PR does not waive those holds or infer new scientific approval from structural QC.

## Inputs and validation

The producer is the clean isolated merged Claw commit `0cc221bd0f4eb460030eb2e5d14b91a311ed2965`; the evidence validator remains pinned at `16fd7c9484d98b14a53aec55616d26dae70a0af7`. CultureMech is `a74dd489720c9df96cc073ffd11568d407d3c06c`. The generation receipt binds all 18,873 recipe, record, index, ledger and producer input hashes. MIM's 2,955 input records include this branch's working changes, not merely its base revision. The read-only kg-microbe checkout and comparison-output hashes are retained in [input revisions](checks/input-revisions.json). The shared checkouts, Intel Cycle 12 work and evidence workflow/pin are preserved. No paid research providers were called.

Final validation passed: `just qc` (including qc-sssom, strict/schema, evidence, roundtrip and flat-export gates), unified rejection/freshness gates, 85 focused tests, receipt replay, reviewed SSSOM/schema validation, supported KGX validation, semantic-review integrity, and the unchanged companion-bundle manifest. Independent acceptance passed 67 focused tests and rechecked all generation hashes, nine representatives, history prefixes, the 33 holds and the complete native-generated artifact. Fresh-process negative controls prove the repaired distinctions. The pre-existing six cross-prefix node-ID advisories and 25 ambiguous indexed labels remain reported.

The initial unsafe candidate, failed local setup attempts and subsequent successful checks are retained separately from final validation. Claw's complete CI passed 6,271 tests with 87.02% coverage; 13 local monitor-fixture failures were sandbox `/bin/ps` denials, and all 56 tests in that module passed with process access. Claw's final head had an independent review with no findings, green queue checks, verified squash content and branch deletion. See its [review](checks/claw697-review/final-3756b6f.md) and [merge/cleanup receipt](checks/claw697-validation/verified-merge-cleanup.json).

All portable evidence files are hash-indexed in [evidence-index.json](evidence-index.json). The native independent assessment is saved under [structured reviews](../../reviews/structured/); the PR links its exact YAML/Markdown pair and the final-head re-review. The review separates complete structural checks from bounded identity interpretation and does not approve the full scientific corpus. This is standalone approved-plan work; no supervisor, goal or cycle binding is invented.
