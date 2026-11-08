# Worker 10 coordinator handoff

All 188 assigned source cases have an evidence-backed outcome and separate skeptical review. This is a completed source-review shard, not approval to publish every ingredient or source association. There are 36 active isolated proposals: 27 edits to existing owners and nine new owners. Forty-four cases support proposals. The other cases retain explicit no-change reasons and source-specific requirements.

The exact assigned branch is `review/all-unmatched-w10-source-review-20261107`, based on `e000d66dd26ab053e9b17ce7bf8d3c873c3dde99`. PR #1158 remains the explicit unmerged dependency. The frozen shard SHA256 is `9767ffc8100e3cd8cd0c4101cc8e9ebe8d8fda8aaab4c42ba4e11b8c3c5693cc`. No maintained YAML, aggregate collection, canonical SSSOM, unified snapshot, review selector or downstream product was changed. No merge, downstream build, separate worker PR, external session or paid research call was performed.

## Accounting and evidence

The shard contains 136 CultureMech cases with all 304 original occurrence references, plus 52 KG cases (29 MediaDive, 13 metatraits, eight metatraits_gtdb and two microbedecoder). KG occurrence lists are empty by the frozen contract, not a claim of zero observations. Complete KG source records and their original count definitions remain bound by case digests.

| Outcome | Cases |
| --- | ---: |
| broad_parent_relation_only | 6 |
| existing_identity_or_alias | 45 |
| malformed_or_nonchemical_token | 1 |
| new_distinct_ingredient_proposal | 8 |
| stock_product_mixture_context | 97 |
| supplied_form_correction | 7 |
| unresolved | 24 |

`decisions.json` contains exact raw identity fields, all original references, owner hashes, applicability, evidence, precise unresolved requirements and complete independent-review status. `case-index.tsv` is a readable navigation index. `evidence.json` contains 873 entries, including 288 primary-source entries, 74 ontology entries and four final independent-review entries. These are ledger entries, not counts of unique HTTP responses. Source snapshots and failed searches are explicitly typed.

`proposals.json` is the authoritative active proposal list; `proposal-index.tsv` summarizes it. Only its 36 referenced after-payloads are candidates for integration. Initial drafts under `chemicals/withdrawn/` and review input snapshots are historical rejected evidence. Do not apply them.

Original capture bytes, SHA256 and access timestamps are preserved. The supplied shared-owner cache README and manifest were inspected; manifest SHA256 `0a8c6b1d8fd3a60de0b5c269613cf25e30ee94f4ae20aa987679639d603e27d5` was verified. No partition reused that cache as its primary evidence. Separate captures and explicitly described local raw-TOGO reuse supplied the evidence. The latter preserves the dataset-reported timestamp and parent-file hash, and is not represented as a fresh HTTP response or a frozen Git-tracked source. See `chemicals/reused-togo-provenance.json`.

## Authorship and independent review

| Author | Cases | Skeptical reviewer | Final review |
| --- | ---: | --- | --- |
| `/root` chemicals | 37 | `/root/buffers_research` | `reviews/buffers-review-of-chemicals-v2.json` |
| `/root/buffers_research` | 43 | `/root/bio_research` | `reviews/bio-review-of-buffers-v1.json` |
| `/root/bio_research` | 56 | `/root/kg_research` | `reviews/kg-review-of-bio-v1.json` |
| `/root/kg_research` | 52 | `/root` | `reviews/root-review-of-kg-v1.json` |

`subagent-scopes.json` publishes exact case IDs, actual scopes, final fragment hashes, authors and reviewers. Each final proposed payload was reviewed by someone other than its author. Final engineering review separately checks consolidation and branch scope; it does not replace scientific review.

Review corrections include removal of source-local stock/navigation strings from global aliases, withdrawal of two unsupported chemical owners, direct primary-evidence binding for source-specific B12, honest treatment of empty/navigational responses, and correction of derived molarity being described as independent evidence. Inherited unsafe owner aliases remain explicit publication holds.

## Material scientific outcomes and holds

- The four active new chemical owners are deferoxamine mesylate, selenium dioxide, 17beta-estradiol and ortho-phthalic acid, with the exact registry/ontology scope recorded in each proposal. The five other new owners are source-specific phosphate/KP formulations and the named Wako Antifoam SI product.
- The initial acrylate owner was withdrawn: all four HMM recipes refer to Junlon PW110, and the original Hobbs paper describes polymer additives. Source normalization to a monomer needs correction before exact identity assignment. The initial methoxyacetate-anion owner was also withdrawn: the actual archived DSMZ478 PDF verifies the name and dose but does not establish the supplied acid/salt/counterion.
- NBRC823 contradicts itself between 20,000 and 200,000 U/ml penicillin G. JCM556 has an unresolved stock-volume arithmetic discrepancy. CultureMech #408 already tracks relevant source volume/unit defects. Neither contradiction was silently repaired.
- Levorin is a narrower NLM concept than the Candicidin descriptor; Ristocetin B must not inherit another ristocetin molecule's formula/structure; unsuffixed halomicin denotes a complex; ISP4 is a complete medium rather than an inorganic salt. Proposed corrections remain bounded and unapplied.
- The Metals44 recipe preserves exact source quantities. Na-EDTA stoichiometry, concentrated sulfuric acid and the borax owner reference remain unresolved components. The proposed new reference to CHEBI:131366 was withdrawn after checking #1168; reconcile the corrected borax owner before adding that reference.
- B12 source1238 supports cyanocobalamin only for those source-specific occurrences. Generic B12, unspecified EDTA/salt/hydrate forms, phosphate stocks and biological processing states retain their own requirements. No global B12 alias is proposed.
- Microbedecoder record6108 retains its combined-culture-context hold. Record19685 literally contains 3-methylacetate in prose and the structured minor-product field; its REJECTED/unresolved product hold remains. Neither source assertion is redirected.
- All existing WITHHOLD, REJECTED, source-material and unreviewed role claims remain intact. Even a supported new alias changes owner bytes and requires a fresh complete publication-payload review.

## Coordination before integration

The exact same reviewed payload is linked across CultureMech and KG for sodium tungstate dihydrate (case156 / `chem-proposal-85`) and JCM462 riboflavin stock (case179 / `buffers-riboflavin-jcm462`). Riboflavin's before hash belongs to the unmapped owner; `owner_path` names that preimage and `intended_destination` records the mapped destination. The move has not occurred.

Candidate owner references in other frozen shards occur for sodium tungstate (workers01/04), vanadyl sulfate pentahydrate (02), KH2PO4 (08), HEPES acid (04) and sodium carbonate (06). These are lexical/candidate references, not a claim that the other worker proposed or approved the same identity. Every proposal records its corresponding shard list. New owner collisions still require coordinator-wide reconciliation. The separate borax dependency is #1168.

Integrate only after checking before/after hashes, resolving owner conflicts, adjudicating the complete published alias/identity/role payload and preserving source-qualified associations. Use native guarded writers, then synchronize and run the coordinator's native release gates. This worker grants no export approval.

## Validation and formal review

- Whole-shard structural audit: PASS, 188/188 cases; all case digests, occurrence IDs, owner hashes, proposal backlinks and referenced capture hashes verified. `scientific_adequacy_or_approval_established` remains false by design.
- Native strict closed-schema validation: 80 actual before owners plus all 36 proposed payloads; zero errors.
- Native guarded writer: all 36 proposals validated into private scratch copies only.
- Native full-catalog component-partonomy check: 2,965 in-memory records with the 36 proposed changes; zero violations. Structural reference validity does not certify chemical identity.
- Native `inspect`, `validate` and `save` completed for [the authoritative owner review](../../../reviews/structured/20261108T052619Z-w10-source-owner-identity-review/review.yaml) and [rendered Markdown](../../../reviews/structured/20261108T052619Z-w10-source-owner-identity-review/review.md). Its verdict is `needs_curation`, with partial whole-owner claim coverage and 80 actual targets. The 89 source-only cases have no fabricated native owner; their campaign assessments and independent review are complete.
- Actual command receipts and logs, including corrected initial native-review formatting failures, are under `native/`. The final review validator reports one valid review. The native append-only bundle check passed: 1,020 valid retained reviews, coverage limited to their declared scopes.
- No downstream rebuild or data-synchronization command ran because maintained inputs were unchanged and the assignment prohibits downstream work.

## Published findings

Following the initial automatic approval rejection, the coordinator verified the existing user authorization in the original briefs and inspected the exact payload scope, then supplied those additional checks. No fresh user approval was supplied. The worker retained that evidence, rechecked all 645 visible live issues and the Mannan main-owner bytes, and retried the same exact Mannan body once through ordinary automatic approval review. It succeeded. The two exact reviewed KG bodies then succeeded through the same workflow:

- [#1187: yeast mannan organism parent and unrelated chemistry](https://github.com/CultureBotAI/MediaIngredientMech/issues/1187).
- [#1188: Levorin, ristocetin B, halomicin and ISP4 identity defects](https://github.com/CultureBotAI/MediaIngredientMech/issues/1188).
- [#1189: glyoxylate, vanadate, AQDS and carbonate form/stock aliases](https://github.com/CultureBotAI/MediaIngredientMech/issues/1189).

`issue-publication-receipts.json` binds the precise published URLs, reviewed body hashes and affected case IDs. Live read-back verified all three bodies against their approved payloads. `context/authorization-retry-payload-check.json` retains the authorization/dedup checks. `context/mannan-issue-response.json` preserves the original rejection; earlier draft plans and the native review record the historical blocked state at their own timestamps. This later receipt resolves that publication blocker without rewriting scientific reviews or their input hashes. Source assessments remain unchanged; join the new issue links by case ID from this receipt.

Existing applicable trackers, including #1168 for the borax dependency and #718 for the whole carbonate owner hold, remain intact. Filing these bounded findings grants no additional source, owner, role or export approval. There is no remaining issue-publication blocker.

## Final receipt

`SHA256SUMS` covers the final worker artifact files and the newly saved native review pair; the manifest excludes itself. Verify it from the repository root. The pushed branch head is recorded in the final user/coordinator message and durable worker-local `.temp/all-unmatched-worker-10/completion-receipt.json`. This committed document cannot embed its own commit hash. No separate worker PR is opened, as assigned. Leave this branch and worktree intact for coordinator integration.
