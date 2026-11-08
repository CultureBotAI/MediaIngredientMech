# Worker03 frozen source-review handoff

All 188 assigned cases received source-context assessment, primary-source research and separate skeptical review. The final bundle contains 74 isolated proposals (39 new owners and 35 existing-owner edits), 852 evidence entries, and 71 precisely unresolved outcomes. Reviewed does not mean resolved or approved for release.

Branch: `review/all-unmatched-w03-source-review-20261107`. Frozen base: `e000d66dd26ab053e9b17ce7bf8d3c873c3dde99`. Shard SHA256: `90d5d5df1ae9609c08593c93216d78449f6ac2781f1d5e7e95695751fdd0c228`. Dependency PR1158 was still open and unmerged at the final live read in `context/pr1158-final.json`; the assignment was not rebased. The final push receipt supplies the exact branch commit without a self-referential commit hash here.

## Case accounting and actual review scopes

| Disposition | Cases |
| --- | ---: |
| broad_parent_relation_only | 2 |
| existing_identity_or_alias | 32 |
| malformed_or_nonchemical_token | 4 |
| new_distinct_ingredient_proposal | 40 |
| stock_product_mixture_context | 26 |
| supplied_form_correction | 13 |
| unresolved | 71 |

| Primary author | Cases | Proposals | Separate skeptical reviewer |
| --- | ---: | ---: | --- |
| /root/broths | 86 | 20 | /root/materials |
| /root/chemicals | 51 | 34 | /root/broths |
| /root/materials | 51 | 20 | /root/chemicals |

The three independent captures bind exact case lists, complete author/core hashes, every proposed payload and retained findings/re-review. `agent-scopes.json` records actual scopes. `decisions.json` retains every frozen occurrence and explicit per-case evidence applicability. `unresolved-requirements.tsv` lists the exact remaining scientific requirements. All 188 cases are accounted for; no source cases from another shard are claimed.

Primary retrieval was not uniformly successful. The two microbedecoder `sugar` cases (`KG_CASE:33c13b23fafbf9588be9c5570e87b1ec40a840bd1da2c1616a3cd9f3913d1478` and `KG_CASE:4fb6d439270ed94097d3ade71c3f52468c7b915b2bcff39b0fadcbc4b223aa19`) retain their frozen provenance and failed-access evidence. Final publisher retries retrieved the Gardnerella chapter abstract, whose several carbohydrate examples do not identify the extracted generic substrate; its full-text link returned the abstract. Alkaliflexus publisher attempts failed. Neither original full substrate passage was retrieved in this review; both identities remain unresolved. `validation/bergey-supplement-review.json` independently assesses the exact added captures. These bounded failures do not establish global unavailability. Other unsuccessful searches and source-version limitations remain explicit per case; no failed retrieval is used as identity evidence.

## Artifacts and checks

- `decisions.json`, `evidence.json`, `proposals.json`: the structural campaign contract; exact hashes in `HANDOFF.json` and `manifest.sha256`.
- `proposal-inventory.tsv`: intended owner paths, unchanged before hashes and exact after payloads. These are proposals only.
- `validation/structural-audit-final-v2.json`: whole-shard audit including the bounded final Bergey followup; structural validity is not scientific approval.
- `validation/proposal-validation-final.json`: all 74 exact payloads pass closed-schema, full-catalog component overlay, new active-identifier collision and history checks. Biological role/causal-graph fields on existing owners are unchanged.
- `validation/final-id-label-coverage.json`: all 28 proposed ontology targets have verified canonical/synonym labels. MICRO uses primary OLS term objects because the local adapter/table is unavailable; NCIT is verified in local semsql. No ontology refresh was run.
- `validation/maintained-surface-final.json`: all 3,060 baseline maintained files and original owner-file membership unchanged; 187 full source recipes and 52 frozen KG owner hashes verified.
- Auditor failure controls: 22 tests passed (`validation/structural-auditor-controls-final.log`). Proposal-wrapper controls: 6 tests passed (`validation/proposal-wrapper-controls-final-v2.log`); only retained dependency deprecation warnings.
- Native formal review: `reviews/structured/20261108T054135Z-worker03-source-owner-assessment/review.yaml` and generated `review.md`, created through native inspect/validate/save. It assesses 133 cases against 85 actual existing owners and has verdict `needs_curation`. The 55 source-only cases stay in the campaign contract; no MIM target was invented.
- Final independent branch review and native check logs are retained in `validation/`; they are separate from the scientific reviewer captures.

The unrestricted `git diff --check` reports whitespace in retained source captures and native-generated Markdown. Those bytes are preserved for provenance and canonical rendering; the authored-artifact check is reported separately. No whitespace rule or repository gate was disabled.

No full maintained-data rebuild gates were invoked because no maintained data were changed. No exports or downstream products were regenerated. The original shared primary-cache manifest was verified as `0a8c6b1d8fd3a60de0b5c269613cf25e30ee94f4ae20aa987679639d603e27d5`; exact reused capture bytes and original timestamps remain with their per-case applicability. Cache integrity grants no case or owner approval.

## Findings and remaining integration

- [bd211065](https://github.com/CultureBotAI/MediaIngredientMech/issues/1182): BD 211065 is brain-heart infusion agar, but its MIM owner maps to heart infusion agar
- [molasses](https://github.com/CultureBotAI/MediaIngredientMech/issues/1183): Sugar beet molasses maps to sugar beet root despite an exact molasses term
- [phb](https://github.com/CultureBotAI/MediaIngredientMech/issues/1184): Reconcile PHB polymer identities without merging R-specific and unspecified polymers
- [citrate](https://github.com/CultureBotAI/MediaIngredientMech/issues/1185): Citric acid monohydrate retains resolving citrate(1-) aliases
- [hsm](https://github.com/CultureBotAI/CultureMech/issues/676): HSM extraction turns the Sterile 1% Marmite stock heading into a Sterile ingredient
- [nh4-s4](https://github.com/CultureBotAI/MediaIngredientMech/issues/1186): Ammonium sulfate incorrectly resolves the source formula (NH4)2S4 as an exact synonym

Five corrected proposal/review findings are recorded in [https://github.com/CultureBotAI/MediaIngredientMech/issues/1196](https://github.com/CultureBotAI/MediaIngredientMech/issues/1196). The JCM431 inherited numbered-pointer miss is tracked under #1173's IR-SHARD-ARTIFACT-9 and #718 with an exact re-review comment, preserving the earlier missed review and proposal bytes. The named Metals44 stock was independently distinguished from the providerless numbered pointer using its source formula and ontology definition.

`cross-shard-owner-references.json` records nine frozen other-shard case references sharing five proposed existing-owner paths, plus the separately observed actual worker01 JCM431 proposal overlap. The JCM431 before hash remains `ad02ea5d31f05ad4f5a71af9718cab059c17a983d01fb0aa101d6b61b8a94549`; the corrected worker03 after hash is `83ffd40a40010e3b5c997565750e523539ebe3bfc9bc5332d42f2f7aef16db1f`. Its bare numbered aliases are provenance-only REJECTED_LABEL. The two workers' full payloads, component grounding and source-case sets still need coordinator reconciliation. This inventory is not a complete cross-shard conflict detector, especially for new-owner or lexical overlaps.

Coordinator next steps: reconcile all overlapping proposals and coordinated PHB tombstones before guarded application; preserve source identities, native/source/downstream holds and the explicit requirements; withdraw inherited support for changed owner bytes; perform complete changed-payload review and the maintained synchronization/export gates. New-owner admission remains constrained by #1165. No mapping review here clears roles, mechanisms, whole-record or publication obligations. No worker PR, merge, downstream rebuild or external session was opened.
