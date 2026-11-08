# Worker 02 coordinator handoff

Completed the full frozen shard. **188/188 source cases independently reviewed; 25 active isolated owner proposals (18 edits, 7 new owners).** No maintained YAML, SSSOM, unified snapshot, selectors or publication inputs were changed. No merges or downstream rebuilds ran.

## Assignment and delivery

- Branch: `review/all-unmatched-w02-source-review-20261107`.
- Assigned base: `e000d66dd26ab053e9b17ce7bf8d3c873c3dde99`; explicit unmerged dependency [PR #1158](https://github.com/CultureBotAI/MediaIngredientMech/pull/1158). Dependency observation is in `context/dependency-pr-1158.json`; no newer baseline was adopted.
- Frozen shard SHA256: `993e393b8a50e6061e4a9863bd60b3ab2a48ee584907a97e3066c1cbc03d6db0`. Exact bytes: `context/frozen-shard-02.json`.
- Final branch/head and remote verification are recorded after push in the local operational `delivery-receipt.json` and final coordinator message. That post-push receipt is intentionally outside the committed manifest to avoid a self-referential commit hash.
- Active integration inputs are ONLY root `decisions.json`, `evidence.json`, `proposals.json` and the exact after-captures they name. `integration-v1`, `a/review-revisions/withdrawn`, `b/superseded-atp-proposal`, and earlier review versions preserve superseded history. Do not apply superseded drafts.

## Accounting and review independence

130 CultureMech cases preserve 322 exact occurrence IDs. The other 58 are 53 MediaDive, four metatraits and one metatraits/GTDB case; their empty occurrence-ID lists do not mean zero observations. There are 84 actual baseline comparison/target owners and 59 source-only cases without an established current MIM owner. The 1,430 indexed evidence entries include seven final independent-review captures; entries are not counts of distinct primary publications.

Disposition counts: broad_parent_relation_only: 19, existing_identity_or_alias: 38, new_distinct_ingredient_proposal: 7, stock_product_mixture_context: 59, supplied_form_correction: 22, unresolved: 43.

Primary authors: A63, B67, C58. Independent routing: B reviewed A63 and C166; A reviewed C57 and B65; C reviewed B66. The B65/C166 exceptions avoid review of a reviewer’s own shared proposal. C separately reviewed root composition of Mohr salt, ammonium nickel sulfate hexahydrate and clarified rumen fluid; B reviewed final A1/C166 links and A reviewed final B65 linkage. Exact scopes, reasoning, input/after hashes and all resolved challenges are retained in `subagent-scopes-final.json` (actual final scopes), historical `subagent-scopes.json`, `integration/independent-review-coverage.json`, and the linked reviewer receipts. Root’s native bundle declares compilation/self-review rather than false independence.

See [case report](CASE_REPORT.md) and exact per-case reasoning in [decisions](decisions.json). Independent challenges withdrew neutral GDP, free zinc-ion and generic ATP new-owner proposals; fixed chromium nitrate nonahydrate to exact MeSH M0321544; recovered original ATP and L-arginine-HCl qualifiers; and corrected retrieval/evidence and source-unit claims. Withdrawn drafts remain historical only.

## Active proposals

| Proposal | Proposed substance / identifier | Kind | Cases |
| --- | --- | --- | --- |
| a-proposal-chrome-alum | CrKSO42 x 12 H2O / cas:7788-99-0 | edit_existing_owner | 2 |
| a-proposal-urea | Urea / CHEBI:16199 | edit_existing_owner | 1 |
| a-proposal-anhydrous-alum | AlK(SO4)2 / CHEBI:86463 | edit_existing_owner | 2 |
| a-proposal-strontium-sulfate | Strontium sulfate / CHEBI:747199 | new_owner | 1 |
| a-proposal-magnesium-sulfate-dihydrate | Magnesium sulfate dihydrate / cas:17830-05-6 | new_owner | 1 |
| a-proposal-chromium-iii-nitrate-nonahydrate | Chromium(III) nitrate nonahydrate / mesh:M0321544 | new_owner | 1 |
| a-proposal-iron-ii-sulfate-tetrahydrate | Iron(II) sulfate tetrahydrate / cas:20908-72-9 | new_owner | 1 |
| b-proposal-paba | p-Aminobenzoic acid / CHEBI:30753 | edit_existing_owner | 1 |
| b-proposal-ammonium_carbonate | NH42CO3 / CHEBI:229630 | edit_existing_owner | 1 |
| b-proposal-ferrous_hepta | FeSO4 x 7 H2O / CHEBI:75836 | edit_existing_owner | 1 |
| b-proposal-ferric_variable | Fe2(SO4)3 x n H2O / kgmicrobe.compound:fe2_so43_x_n_h2o | edit_existing_owner | 2 |
| b-proposal-trimethyl | Trimethylamine-HCl / CHEBI:64700 | edit_existing_owner | 1 |
| b-proposal-selenous | H2SeO3 / CHEBI:26642 | edit_existing_owner | 1 |
| b-proposal-silver_nitrate | silver(1+) nitrate / CHEBI:32130 | new_owner | 1 |
| b-proposal-heedta | N-(hydroxyethyl)ethylenediaminetriacetic acid / mesh:M0085998 | new_owner | 1 |
| b-proposal-ferric_ammonium_dodeca | Ammonium ferric sulfate dodecahydrate / mesh:M0141705 | new_owner | 1 |
| c-proposal-cerium-nitrate-hexahydrate | cerium(III) nitrate hexahydrate / cas:10294-41-4 | edit_existing_owner | 2 |
| c-proposal-lanthanum-nitrate-hexahydrate | lanthanum(III) nitrate hexahydrate / mesh:M0313204 | edit_existing_owner | 2 |
| c-proposal-reject-dl-aliases-on-l-malate | Sodium malate / CHEBI:91261 | edit_existing_owner | 6 |
| c-proposal-nickel-sulfate-6-water-properties | NiSO4 x 6 H2O / CHEBI:53437 | edit_existing_owner | 1 |
| c-proposal-nickel-sulfate-7-water-properties | NiSO4 x 7 H2O / CHEBI:53504 | edit_existing_owner | 1 |
| c-proposal-o-carbamyl-d-serine-scope | O-carbamyl-D-serine / mesh:M0040464 | edit_existing_owner | 1 |
| w02-proposal-mohr-hexahydrate | Fe(NH4)2(SO4)2 x 6 H2O / CHEBI:76181 | edit_existing_owner | 6 |
| w02-proposal-ammonium-nickel-hexahydrate | (NH4)2Ni(SO4)2 x 6 H2O / CHEBI:86149 | edit_existing_owner | 3 |
| w02-proposal-clarified-rumen-fluid | Clarified rumen fluid / MICRO:0000520 | edit_existing_owner | 2 |

## Validation and limits

- Whole-shard auditor: PASS, 188/188; all final independent-review statuses complete. Receipt: `validation/structural-final.json`. Its scientific-approval field remains false by design.
- Exact active after-payloads: strict LinkML validation PASS, 25 files, zero errors (`validation/proposal-schema-final.*`).
- Canonical label/deprecation check: 24 confirmed; unchanged MICRO:0000520 has no available adapter. The actual exit 1 is preserved in `validation/proposal-labels-final.json`. This is a declared remaining label-check limitation, not a universal pass. MeSH M concepts pass current available native schema/canonical-label checks; coordinator must establish downstream compatibility.
- Integration helper negative tests: 16 passed (`validation/helpers-final.log`); external auditor synthetic tests: 22 passed (`validation/auditor-tests-final.log`).
- Native inspect/validate/save succeeded for [review.yaml](../../../reviews/structured/20261108T054002Z-w02-all-unmatched-source-review/review.yaml) and [review.md](../../../reviews/structured/20261108T054002Z-w02-all-unmatched-source-review/review.md). Verdict `needs_curation`, full 188-case source scope; 1,094 hashed inputs. The 146 retained requirement observations include integration obligations and are not 146 new chemical errors. Initial rejected native draft attempts and their repairs are retained in validator logs.
- Native full retained-review check: PASS for 1,020 retained bundles, limited to their declared scopes (`validation/native-check-final.*`). Final staged diff review is recorded in `b/review-final-staged.json`.
- Maintained input comparison: unchanged frozen bytes, including gitignore-independent enumeration; see `validation/maintained-surfaces-unchanged.json` and `b/review-final-integration.json`. No generated-data gate or downstream build was run for proposal-only artifacts.

## Dependencies and retained holds

`cross-shard-dependencies.json` scans every immutable shard for explicit owner paths and exact lexical overlaps. It found no outside-worker match for these active proposals under that bounded scan. `c/integration-followup/owner-dependencies.json` additionally scans the six identifier-collision owner paths across all ten shards: only worker02 references were found. This does not claim other source-only cases cannot concern the same substance.

Three identifier collisions need different treatment: the alternate FeSO4·7H2O file is an existing REJECTED merge record; NiSO4·6H2O cleanup affects a REJECTED record whose active survivor already has hydrate-specific chemistry; the active bare ammonium nickel sulfate owner remains a genuine unresolved form conflict under [#1050](https://github.com/CultureBotAI/MediaIngredientMech/issues/1050). No duplicate merge, occurrence transfer or rejected-record reactivation is proposed. Details: `c/integration-followup/collision-dependency-supplement.md`.

All changed-owner bytes invalidate inherited positive support. Coordinator must reconcile exact original before hashes, assess each whole resulting owner payload, preserve existing WITHHOLD/REJECTED/source-material and role holds, and perform guarded writes and synchronized native generation/gates. Source stocks and processed biological materials retain preparation/concentration boundaries. Unqualified or contradictory hydrates, malate stereochemistry, source assay compounds, butamine/chaninin and inherited producer metadata remain explicitly scoped in decisions. Available primary research was pursued; unresolved does not mean approved by name.

The optional shared-owner cache was integrity-checked (`validation/shared-cache-verification.json`) against manifest SHA256 `0a8c6b1d8fd3a60de0b5c269613cf25e30ee94f4ae20aa987679639d603e27d5`. Cache integrity grants no source-case, owner or export approval. Primary captures and actual original retrieval timestamps remain individually bound in evidence; no retrieval time was replaced merely because bytes were reused.

## Findings and tracking

New deduplicated issues filed: [CultureMech #675](https://github.com/CultureBotAI/CultureMech/issues/675) Se-acid ambiguity; [CultureMech #677](https://github.com/CultureBotAI/CultureMech/issues/677) six source-specific identity corrections; [MIM #1181](https://github.com/CultureBotAI/MediaIngredientMech/issues/1181) methylamine alias on trimethylamine hydrochloride; [MIM #1199](https://github.com/CultureBotAI/MediaIngredientMech/issues/1199) O-carbamyl-D-serine concept specificity.

Existing trackers received bounded evidence updates: [CultureMech #408](https://github.com/CultureBotAI/CultureMech/issues/408) (also referencing #150) quantity and stock stages; [MIM #321](https://github.com/CultureBotAI/MediaIngredientMech/issues/321#issuecomment-6717843876) nickel chemistry residuals; [MIM #811](https://github.com/CultureBotAI/MediaIngredientMech/issues/811#issuecomment-6717844045) foreign alum aliases. Exact creation/comment receipts and reviewed body files are in `context/`. Historical SEM finding IDs and dispositions remain intact; a partial proposal does not close a larger prior finding. MIM #811/#868 already cover DL aliases on L-malate, and #1050 retains the bare nickel double-salt hold. No issue was closed or merged.

## Evidence integrity and handoff boundary

`SHA256SUMS` records every published worker artifact and the native YAML/Markdown pair, except itself and the operational post-push delivery receipt, whose self-inclusion would be circular. Final independent diff review records the actual staged inventory and exact root outcome hashes. All three subagent handoffs are retained under `a/`, `b/`, `c/`. Final delivery leaves this branch and workspace in place for coordinator integration; no cleanup or further worker execution is scheduled.

## Core artifact hashes

| Artifact | SHA256 |
| --- | --- |
| `decisions.json` | `5c93d77656130831940e5cf8c49a1492d0a83374f7ff811739436bad10d00271` |
| `evidence.json` | `43cdc2cd67d8a3860ee9b31b2ba7cdb917003f4fead45f73b6df96315a311174` |
| `proposals.json` | `de2e18c79dee62118e88c2c4b885c2abaaccdb7ad5631860df82b136a6e556a9` |
| `integration/independent-review-coverage.json` | `a6b87289efb1b3e840448231896e63ed70533b9e5d641a86a7be0d71a5c52bcd` |
