# Worker07 source-review handoff

All 188 assigned cases have primary-source assessments and separate skeptical-review outcomes. The candidate set contains 100 isolated owner proposals: 30 edits and 70 new owners. No maintained source, mapping, unified snapshot, review selector or publication gate was changed.

Use **decisions.json**, **evidence.json** and **proposals.json** as the final candidate manifest. `parts/`, preliminary receipts and unselected `proposed_owners/` files preserve the research and correction history; they are not additional active proposals.

| Disposition | Cases |
| --- | ---: |
| stock_product_mixture_context | 77 |
| malformed_or_nonchemical_token | 4 |
| unresolved | 50 |
| existing_identity_or_alias | 42 |
| broad_parent_relation_only | 5 |
| supplied_form_correction | 6 |
| new_distinct_ingredient_proposal | 4 |

The unresolved outcomes retain case-specific requirements after primary-source pursuit. Completion of review does not mean that every identity was resolved. Holds also remain within proposed cases, including eight of the seventeen sodium ammonium phosphate occurrences. [CASE-LEDGER.md](CASE-LEDGER.md) lists every source case and remaining requirement; `HANDOFF.json` provides exact paths and hashes.

Primary and skeptical authorship is explicit in [subagent-scopes.json](subagent-scopes.json). A reviewed B's 70 cases, B reviewed C's 48, and C reviewed A's 70. The separate integration reviewer authored none of those decisions and reviewed the combined owners, shared Hutner formulation, four later root-authored stock decisions, final transformations and staged boundaries. Shared proposal cases reference both their applicability reviewer and their independent payload reviewer.

Review corrected source attribution, formulation completeness, omitted source quantities and stock proposals. It also recovered the Sigma V6629 cyanocobalamin identity and the original Schaechter tetrahydrate formulation. The JCM900 and JCM979 Hutner subrecipes now share one nominal stock proposal; malformed molybdate wording remains unresolved. Candidate stock equivalence remains to be reconciled before minting all new owners; source IDs alone do not establish different chemistry. Exact groups are retained in captures/integration-nominal-stock-overlap-leads.json.

The three filed findings are [dithionite/scutellarin aliases](https://github.com/CultureBotAI/MediaIngredientMech/issues/1169), [L/DL lactate alias](https://github.com/CultureBotAI/MediaIngredientMech/issues/1170), and [CultureMech phosphate/citrate ontology pointers](https://github.com/CultureBotAI/CultureMech/issues/672). The source-volume normalization defects are already tracked by [CultureMech #408](https://github.com/CultureBotAI/CultureMech/issues/408); calcium-pantothenate, cysteine/QSY9 and malate concerns retain their existing issue links.

The native owner comparison covers 77 actual maintained owners with verdict `needs_curation`, five open identity-synonym findings, and explicit claim-scope exclusions. [Native YAML](../../../reviews/structured/20261108T054535Z-worker07-source-owner-comparison/review.yaml) and [rendered Markdown](../../../reviews/structured/20261108T054535Z-worker07-source-owner-comparison/review.md) were saved through the maintained helper. Source-only cases do not invent native owners. The earlier native observation is retained unchanged; this successor preserves its 77 targets and four open findings while adding the omitted malate-alias finding. These reports grant no role, whole-owner or export approval.

Validation: all 100 final payloads passed the native closed schema and full catalogue component-partonomy check; no new identifier collision or historical rewrite was introduced. All 5459 baseline files retained their original hashes. Whole-shard structural integrity, auditor negative controls and native review validation/save/check logs are retained under `logs/`; structural PASS explicitly does not certify scientific truth. Earlier failed attempts remain visible with their later corrections.

[cross-shard-dependencies.json](cross-shard-dependencies.json) lists 31 other-shard cases referencing the same owners or exact labels, across worker slots 1, 2, 3, 4, 6, 8, 9, 10. These are dependency leads, not reviewed identities. In particular, NTA monohydrate source 1930 shares the source 1482 owner with worker 09; calcium pantothenate overlaps worker 06; dithionite and several hydrates overlap worker 08. Existing duplicate owner IDs are reported by the final proposal validator, not merged.

The coordinator must retain original before-owner hashes, reconcile cross-shard and nominal-stock equivalence, and distinguish source-specific stock occurrences from the pure solute. Apply accepted proposals through guarded writers, withdraw inherited support for changed owner bytes, synchronize native surfaces and review every resulting published payload. PR1158 remains the explicit unmerged baseline dependency. This worker performs no merge, downstream rebuild or worker PR.

The final pushed commit and remote-tip verification are supplied in the session handoff receipt after commit. The bundle SHA256 manifest covers the final retained artifacts without trying to hash itself.

Final independent integration receipt: [JSON](captures/integration-review-final.json) and [readable review](parts/integration-review-final.md). All four integration findings are resolved in the isolated artifacts; source and publication holds remain.
