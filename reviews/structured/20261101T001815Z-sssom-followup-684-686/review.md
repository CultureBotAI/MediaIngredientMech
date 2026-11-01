# SSSOM follow-up 684–686: final-head mechanical verification with source and review preservation

- Review: 20261101T001815Z-sssom-followup-684-686
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-11-01T00:15:42Z
- Finished UTC: 2026-11-01T00:18:15Z
- Reviewer: Codex validation agent /root/sssom_validation (not_applicable)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Canonical 2,987 rows remain unchanged. A new 2,980-row candidate from committed 9294730 passes native checks; exactly one generated stock alias namespace changes relative to the prior repaired output, with no inherited stamp for that new triple. All original 41 diagnostic outcomes remain satisfied. No promotion or scientific status change.

## Scope And Provenance

Bounded mechanical successor review of exact canonical and final 9294730 diagnostic output.

Selection: Two exact TSV targets with all rows evaluated by applicable native gates; original B5/K/G candidate finding identities and affected selectors retained.
Coverage: full; 2 reviewed / 2 in the declared population.
Source: working_tree at Git base bb65a909e5f56b2400f64a2e363d9ad60a2996a9.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| canonical | mappings/ingredient_mappings.sssom.tsv | generated | Unchanged maintained canonical mapping: 2,987 rows |
| candidate | output/sssom-followup-684-686/ingredient_mappings.sssom.tsv | generated | Final 9294730 diagnostic candidate: 2,980 rows; not promoted |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| followup generate candidate | passed | True | candidate | Unmodified native builder at committed 9294730, verified target and owned lock, generated 2,980 rows at a new path. Generator source SHA is identical before and after invocation. |
| followup candidate invariants | passed | True | candidate | Strict native rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L pass with header-only reject TSV. Default-path B4 skip is supplemented separately. |
| followup candidate schema | passed | True | candidate | SSSOM JSON Schema, prefix completeness and strict CURIE validation pass; native extension notices retained. |
| followup candidate curie | passed | True | candidate | 2,980 rows / 5,960 CURIEs pass native syntax and prefix checks. |
| followup candidate products | passed | True | candidate | Unchanged configured native label policy passes: 2,216 canonical, four synonym, four exception pairs; 3,736 no-adapter skips remain. |
| followup compare candidates final | passed | True | canonical, candidate | Final comparison proves exactly one alias replacement since the previous repaired candidate; 2,979 rows identical; no row dates, headers, predicates or other fields change. Original 41 diagnostic dispositions remain satisfied and native drift is zero. |
| followup full qc | passed | True | canonical | Full native just qc passes on unchanged maintained data, including roundtrip and flat coverage. Candidate validation is separate. |
| followup baseline curie | passed | True | canonical | Canonical 2,987 rows / 5,974 CURIEs pass; 20 tests passed and one skipped. |
| followup baseline reconcile | passed | True | canonical | Canonical GAP, ORPHAN, STALE, PREDICATE and GRADE counts are all zero. |
| followup baseline products | passed | True | canonical | Full product enforcement passes with 101 nonblocking warnings and 5,314 no-adapter skips. |
| followup baseline subjects | passed | False | canonical | Native checker retains 18 non-gating subject/filename warnings among 2,611 subjects and 2,953 record files. |
| followup candidate b4 actual | passed | False | candidate | Native B4 with actual read-only KG transforms reports zero findings; missing BTO/MICRO transforms and absent-ID skips remain. |
| followup baseline b4 actual | passed | False | canonical | Actual-path native B4 reports zero canonical findings with the same limits. |
| followup rule f integration | passed | True | candidate | Native YAML extraction and CLI writer retain two dateless synthetic records alongside one dated record. Unmodified native Rule F returns both dateless subjects and writes two rejects; Rule G returns zero. |
| followup focused restored | passed | True | candidate | All 84 focused regression tests pass on final source restored after mutation checks. |
| followup lint | passed | True | candidate | Repository-pinned Ruff passes for the final code. |
| followup mypy | passed | True | candidate | Native maintained type-check command passes. |
| followup full tests | passed | True | candidate | Full CLAW CI-style suite passes on exact final head; this checks code behavior, not scientific approval. |
| followup safety coverage | passed | True | candidate | Native safety-module coverage gate passes. |
| followup684 mutation | passed | False | candidate | Reverting registry namespace repair produces the expected test failure. |
| followup686 mutation mapping date | passed | False | candidate | Reverting the header mapping_date behavior produces the expected regression failure. |
| followup686 mutation mapping set version | passed | False | candidate | Reverting the header mapping_set_version behavior produces the expected regression failure. |
| followup compare candidates | failed | False | candidate | Initial diagnostic helper assertion omitted the legitimate historical-stamp removal on the new alias; it failed before writing comparisons. Final helper explicitly verifies that removal. |

## Scientific And Domain Assessments

### Canonical source remains unchanged and passes native QC

consistency: supported. Targets: canonical.

Canonical remains 2,987 rows at its prior hash; MIM records, aggregates, unified mapping, release review and original source checkouts are preserved. Full native QC and source validators pass.

### Final-head diagnostic candidate and exact delta

consistency: supported. Targets: candidate.

Candidate contains 2,980 rows. Versus prior repaired output, 2,979 are identical; the stock B1 alias changes compound to ingredient namespace, object_source/comment follow that namespace, and its historical UNKNOWN_TERM stamp is not copied to a new triple. No date, header, predicate or other-token changes. All original 41 diagnostics remain resolved and native drift is zero.

### Issue 686 native date and curator-review contract

provenance: supported. Targets: candidate.

ASCII calendar-valid histories determine maximum row dates. Mixed dateless rows remain explicit blanks for native Rule F rejection; an all-dateless set or malformed nonempty emitted dates are reported completely before writing. This run has no date changes; synthetic native integration proves both missing-date rejects without altering real source data.

### Final generator checks and independent review

consistency: supported. Targets: candidate.

Committed final generator passes focused tests, detected mutations, native lint/type checks, full CI-style suite and independent adversarial review. This assessment is mechanical and grants no scientific status.

### Historical holds and incomplete adapter coverage retained

scope: supported. Targets: canonical, candidate.

Candidate is not promoted. Scientific WITHHOLD decisions and prior validation stamps remain historical. Baseline retains 101 label warnings, 5,314 no-adapter skips and 18 non-gating subject warnings; candidate retains 3,736 no-adapter skips. Actual-path B4 omits BTO/MICRO and absent IDs under native semantics.

## Findings

### F-B5: Resolved: Builder adds a second incompatible registry identity

major / resolved / confirmed; issue key: sssom-builder-dual-local-namespace.

Reconfirmed on the newly generated exact 9294730 candidate. All original affected candidate selectors are retained below; removed historical rows intentionally lack a current counterpart. The builder recognizes an already emitted registry identity in either permitted local namespace before synthesizing B1 backfill. All 14 maintained primary identities remain; the 14 competing generated identities disappear. Native B5 and the complete invariant suite pass. No YAML identifier was changed. Resolution is scoped to observed working-tree output, not a statement that its fixing PR is merged or that a scientific release hold is cleared.

Disposition: The new candidate independently satisfies every original diagnostic disposition, with native invariants passing. The additional stock B1 alias intentionally changes namespace and receives no copied validation stamp; all maintained primary identities and parent predicates remain unchanged. Historical scientific holds are not cleared.

### F-K: Resolved: Candidate publishes synonyms owned by distinct records

major / resolved / confirmed; issue key: sssom-builder-cross-record-synonyms.

Reconfirmed on the newly generated exact 9294730 candidate. All original affected candidate selectors are retained below; removed historical rows intentionally lack a current counterpart. External object aliases are inherited only for final exactMatch rows. All eleven originally rejected tokens are absent; seventeen target-only tokens are removed overall while curated subject aliases survive. Final predicates and registry identities are preserved. Native K and label checks pass. No synonym curation or scientific identity choice was applied. Resolution is scoped to observed working-tree output, not a statement that its fixing PR is merged or that a scientific release hold is cleared.

Disposition: The new candidate independently satisfies every original diagnostic disposition, with native invariants passing. The additional stock B1 alias intentionally changes namespace and receives no copied validation stamp; all maintained primary identities and parent predicates remain unchanged. Historical scientific holds are not cleared.

### F-G: Resolved: Generated header dates disagree with newest row date

minor / resolved / confirmed; issue key: sssom-builder-header-date-policy.

Reconfirmed on the newly generated exact 9294730 candidate. All original affected candidate selectors are retained below; removed historical rows intentionally lack a current counterpart. Both header dates now equal 2026-10-15, the newest emitted row date. Native G passes; source row dates were not rewritten to manufacture agreement. Resolution is scoped to observed working-tree output, not a statement that its fixing PR is merged or that a scientific release hold is cleared.

Disposition: The new candidate independently satisfies every original diagnostic disposition, with native invariants passing. The additional stock B1 alias intentionally changes namespace and receives no copied validation stamp; all maintained primary identities and parent predicates remain unchanged. Historical scientific holds are not cleared.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| log-followup_generate_candidate | reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_generate_candidate.log | supports | Unmodified native builder at committed 9294730, verified target and owned lock, generated 2,980 rows at a new path. Generator source SHA is identical before and after invocation. |
| log-followup_candidate_invariants | reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_candidate_invariants.log | supports | Strict native rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L pass with header-only reject TSV. Default-path B4 skip is supplemented separately. |
| log-followup_candidate_schema | reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_candidate_schema.log | supports | SSSOM JSON Schema, prefix completeness and strict CURIE validation pass; native extension notices retained. |
| log-followup_candidate_curie | reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_candidate_curie.log | supports | 2,980 rows / 5,960 CURIEs pass native syntax and prefix checks. |
| log-followup_candidate_products | reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_candidate_products.log | supports | Unchanged configured native label policy passes: 2,216 canonical, four synonym, four exception pairs; 3,736 no-adapter skips remain. |
| log-followup_compare_candidates_final | reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_compare_candidates_final.log | supports | Final comparison proves exactly one alias replacement since the previous repaired candidate; 2,979 rows identical; no row dates, headers, predicates or other fields change. Original 41 diagnostic dispositions remain satisfied and native drift is zero. |
| log-followup_full_qc | reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_full_qc.log | supports | Full native just qc passes on unchanged maintained data, including roundtrip and flat coverage. Candidate validation is separate. |
| log-followup_baseline_curie | reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_baseline_curie.log | supports | Canonical 2,987 rows / 5,974 CURIEs pass; 20 tests passed and one skipped. |
| log-followup_baseline_reconcile | reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_baseline_reconcile.log | supports | Canonical GAP, ORPHAN, STALE, PREDICATE and GRADE counts are all zero. |
| log-followup_baseline_products | reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_baseline_products.log | supports | Full product enforcement passes with 101 nonblocking warnings and 5,314 no-adapter skips. |
| log-followup_baseline_subjects | reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_baseline_subjects.log | supports | Native checker retains 18 non-gating subject/filename warnings among 2,611 subjects and 2,953 record files. |
| log-followup_candidate_b4_actual | reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_candidate_b4_actual.log | supports | Native B4 with actual read-only KG transforms reports zero findings; missing BTO/MICRO transforms and absent-ID skips remain. |
| log-followup_baseline_b4_actual | reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_baseline_b4_actual.log | supports | Actual-path native B4 reports zero canonical findings with the same limits. |
| log-followup_rule_f_integration | reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_rule_f_integration.log | supports | Native YAML extraction and CLI writer retain two dateless synthetic records alongside one dated record. Unmodified native Rule F returns both dateless subjects and writes two rejects; Rule G returns zero. |
| log-followup_focused_restored | reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_focused_restored.log | supports | All 84 focused regression tests pass on final source restored after mutation checks. |
| log-followup_lint | reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_lint.log | supports | Repository-pinned Ruff passes for the final code. |
| log-followup_mypy | reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_mypy.log | supports | Native maintained type-check command passes. |
| log-followup_full_tests | reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_full_tests.log | supports | Full CLAW CI-style suite passes on exact final head; this checks code behavior, not scientific approval. |
| log-followup_safety_coverage | reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_safety_coverage.log | supports | Native safety-module coverage gate passes. |
| log-followup684_mutation | reports/sssom_generation_repair_20261031/followup-684-686/logs/followup684_mutation.log | supports | Reverting registry namespace repair produces the expected test failure. |
| log-followup686_mutation_mapping_date | reports/sssom_generation_repair_20261031/followup-684-686/logs/followup686_mutation_mapping_date.log | supports | Reverting the header mapping_date behavior produces the expected regression failure. |
| log-followup686_mutation_mapping_set_version | reports/sssom_generation_repair_20261031/followup-684-686/logs/followup686_mutation_mapping_set_version.log | supports | Reverting the header mapping_set_version behavior produces the expected regression failure. |
| log-followup_compare_candidates | reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_compare_candidates.log | context_only | Initial diagnostic helper assertion omitted the legitimate historical-stamp removal on the new alias; it failed before writing comparisons. Final helper explicitly verifies that removal. |
| prior-review | reviews/structured/20261031T233012Z-sssom-native-repair-mechanical/review.yaml | context_only | Immutable prior review; all affected candidate target IDs and original issue keys are preserved. |
| comparison | reports/sssom_generation_repair_20261031/followup-684-686/candidate-comparison.json | supports | Exact separate comparisons with previous repaired candidate, original rejected candidate and canonical mapping. |
| previous-changes | reports/sssom_generation_repair_20261031/followup-684-686/previous-candidate-changes.json | supports | Removed compound alias and added ingredient alias, with corresponding source/comment changes and blank validation_method on the new triple. Curated identifier and parent relation unchanged. |
| remediation | reports/sssom_generation_repair_20261031/followup-684-686/original-41-remediation.json | supports | All 28 B5, eleven K and two G original diagnostics retain exact selectors and current outcomes. |
| inputs | reports/sssom_generation_repair_20261031/followup-684-686/validation-inputs.json | supports | Exact current input revisions/hashes, including MIM records, aggregate/canonical/release inputs, KG unified mapping, comparison-only CM/Mediadive data and ontology DBs. |
| generation | reports/sssom_generation_repair_20261031/followup-684-686/generation-result.json | supports | Committed generator head 9294730aeb19d269899177678db87406f4251555 and identical before/after source hashes bind this fresh native candidate. |
| date-contract | reports/sssom_generation_repair_20261031/followup-684-686/date-contract.json | supports | Explicit issue 686 decision: preserve blank dates for native Rule F in mixed sets; no clock fallback; reject all-dateless or malformed emitted dates before writing. |
| rule-f-proof | reports/sssom_generation_repair_20261031/followup-684-686/rule-f-integration/receipt.json | supports | Real native extraction/writer plus native validator proof, with exact synthetic row/reject hashes. |
| independent-review | reports/sssom_generation_repair_20261031/followup-684-686/adversarial-review-code.json | supports | Independent adversarial review of exact 9294730 found no new defects, with scientific and rule-coverage limitations retained. |
| preservation | reports/sssom_generation_repair_20261031/followup-684-686/post-validation-preservation.json | supports | Original repositories, current scientific inputs and all 87 pre-existing evidence files remain unchanged; separate live PR file overlap remains empty. |
| holds | reports/sssom_generation_repair_20261031/followup-684-686/historical-rule-k-holds.json | context_only | Eleven historical corresponding canonical rows remain WITHHOLD; mechanical fixes do not clear release holds. |
| semantics | MAPPING_SEMANTICS.md | supports | Identity/predicate/synonym contracts and per-row curator reject process. |
| pinned-release | reports/sssom_completion_20260921/review.json | context_only | Pinned scientific release input remains unchanged; not a new approval. |
| target-canonical | mappings/ingredient_mappings.sssom.tsv | supports | Exact inspected Unchanged maintained canonical mapping: 2,987 rows. |
| target-candidate | output/sssom-followup-684-686/ingredient_mappings.sssom.tsv | supports | Exact inspected Final 9294730 diagnostic candidate: 2,980 rows; not promoted. |

## Limits And Additional Notes

- Mechanical verification does not approve identities, relation scope, historical validation stamps or scientific release claims. Candidate is not promoted.
- CultureMech ingredient outputs and KG Mediadive nodes are comparison-only inputs; raw generation consumes maintained MIM records, copied residual classifications and actual KG unified mappings plus ontology labels. No bulk import.
- Actual-path B4 retains native absent-ID skips and missing BTO/MICRO transforms. Configured label no-adapter skips, 101 baseline warnings and 18 subject warnings remain.
- Generated full candidates and large inputs remain local diagnostic artifacts. Saved working-tree hashes attest inspected bytes and do not claim full outputs are committed.
- Canonical-versus-candidate differences are broader than this follow-up. This is not an approved replacement for canonical or the supported/withheld partition.
- Native B5 groups by subject and slug, not subject alone; targeted regression tests and exact delta review cover the different-slug namespace defect without silently redefining the downstream validator.
- The first comparison helper run failed an overstrict stamp assertion; an intermediate summary reused a loop variable. Both setup receipts are retained; final comparison explicitly verifies the alias and blank stamp, with all native validators unaffected.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261101T001815Z-sssom-followup-684-686
kind: repository
repository: CultureBotAI/MediaIngredientMech
title: 'SSSOM follow-up 684–686: final-head mechanical verification with source and
  review preservation'
started_at: '2026-11-01T00:15:42Z'
finished_at: '2026-11-01T00:18:15Z'
reviewer:
  identity: Codex validation agent /root/sssom_validation
  kind: agent
  independence: not_applicable
  independence_basis: Validation/provenance task separate from generator implementation;
    this agent advised the date contract and authored earlier K tests. Independent
    code review is separately attributed. No scientific-review independence claimed.
skill: .claude/skills/review-sssom-output/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: Current final-head diagnostic candidate passes native checks; original
  findings remain resolved; scientific holds unchanged
scientific_review: false
summary: Canonical 2,987 rows remain unchanged. A new 2,980-row candidate from committed
  9294730 passes native checks; exactly one generated stock alias namespace changes
  relative to the prior repaired output, with no inherited stamp for that new triple.
  All original 41 diagnostic outcomes remain satisfied. No promotion or scientific
  status change.
source:
  git_revision: bb65a909e5f56b2400f64a2e363d9ad60a2996a9
  state: working_tree
  inputs:
  - path: .claude/skills/review-sssom-output/SKILL.md
    sha256: 2e05b30eefce620fbb78196386e476c330b81e36738f2461b4be64391a61ecd5
    role: context
  - path: AGENTS.md
    sha256: fc7728986d82b43359a9055ae233bcf0d4ebaef8bb657ef1b4bb4aa87b2cbaaf
    role: context
  - path: MAPPING_SEMANTICS.md
    sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
    role: context
  - path: UNIFIED_INGREDIENT_MAPPING.tsv
    sha256: a9bfb265b6a92e495c241d57fb637096ec6af398af7e87ea026574444672cc40
    role: context
  - path: conf/id_label_targets.yaml
    sha256: 3931943e0f0d4fe9477b946df84aa39348ebaba302c2eeac46becfdea29ff817
    role: context
  - path: conf/record_review.yaml
    sha256: 07a8fa6d17ee664c7a2bc2d5b5821bd106f6aa454299b4f3e0440176876cd82e
    role: context
  - path: data/curated/mapped_ingredients.yaml
    sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
    role: context
  - path: data/curated/unmapped_ingredients.yaml
    sha256: 8f574be094e741f1d59d55618cc14bf375304644732508bd7a5cd4a817c7fce2
    role: context
  - path: data/ingredients/mapped/Sodium_Nitrate_070_M_Stock.yaml
    sha256: eca7428c811737e50f6146e617e8e6530a96c07d8be51069abf11aaf31aae98c
    role: context
  - path: docs/SSSOM_RELEASE.md
    sha256: dd726c781166ad45735b65f98ffeee5852e19d99ccfac9b9d53932d48947079e
    role: context
  - path: docs/record-review-profile.md
    sha256: da17e2048a13514a422bc94bd2f8d48943cffc5689b96e3f07da26423248d1a7
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: mappings/ingredient_mappings.sssom.tsv
    sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
    role: target
  - path: mappings/other_cross_record_baseline.tsv
    sha256: b717cfa99d0ad0e386fe2dc9d8c93b6b0d902fbfdbd3358f5a149697ee71e41b
    role: context
  - path: output/sssom-followup-684-686/ingredient_mappings.sssom.tsv
    sha256: 9fff31e31008a4aba70de846febe9f7de07770d84e86e4e7730c9acc69fffe31
    role: target
  - path: output/sssom-followup-684-686/native-rejected-rows.tsv
    sha256: e638bc52978e8503320e3386814dcdb5bc6b1c1c72e96487ba327ea58701f127
    role: context
  - path: output/sssom-repair/final-code-replay-r2.sssom.tsv
    sha256: 04159ba36b221d1c8ebf6e281972c846a333cf4fe5e868b06bb5326f2b02e3a7
    role: context
  - path: reports/sssom_completion_20260921/review.json
    sha256: 6c74c7cc3eb8075ec18e20ab594a9b5eae9910b08b98c9d0746b3374af6c7ac6
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/README.md
    sha256: 544ca2c8f79d60187a11596d993bca16a5bd2396e46f932207cfaf343ed99e52
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/adversarial-registry-result.json
    sha256: 51d45ca9f0ba2f2481a5db7f24b74bd85ca8c84ca1420b1cc47bd1950143adfd
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/adversarial-review-code.json
    sha256: 7ac5d05e51eb2dcb329af74e5efab83c4e41edbd45f2886b50dc3502b15ab254
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/adversarial-review-code.md
    sha256: 218b778a02294a62636a2909eb7a028412dbcf5c18fc50c0b8a9f83a8fe25b4f
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/adversarial_registry.py
    sha256: edc6ac64fb93ac1bea0db92dd56698f50c9af0fcb5060450227c8dd0246f47af
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/author_review.py
    sha256: c9d0038467451d5351fb0cddbd5ae5120c846e5766c23177a8b229d0724c476d
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/baseline-b4-actual.json
    sha256: a93b970ed6afa525c13ac834d47bad8767f4ca7869dfc851cba3611d32785fbd
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/candidate-b4-actual.json
    sha256: a4ee7fcff999f8c881627d62b8fedb1bed2e370da991db6bcbe57ee01f60828c
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/candidate-comparison.json
    sha256: 266ff3f69585da30906715786c39faf25b27bb34dd95b39282c26391dcd20742
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/candidate-id-label-config.json
    sha256: 9b457a186327ef9fcd84ef440e0a3f44deecc65c665de7e8373571204ba8a72b
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/candidate-id-label-config.yaml
    sha256: ffba1d6fec331af194a6591f6ed8939dfd2cbfbc96aa29e6a4126c42f977d669
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/candidate-native-drift.json
    sha256: 2429604ab6b30758b72696906bcc2a341cacb8d1a01a9047409cb360a82fd4d1
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/canonical-candidate-changes.json
    sha256: 8a1a6344116146d87d4ce48519b25db3dfd4b9a775ade0d6587fc5f845a3a8f9
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/capture_validation_inputs.py
    sha256: 355cdb5f3e5e0f2d3e58a9feb763919c7c50d300e0dae17a75fc40f329a02960
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/check_b1_b5.py
    sha256: 91354b065c475439af5dcb49c341af82aad85fa96fa05ab7f4043a91f20c3e62
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/check_b4_actual.py
    sha256: d83c6b1defab1dbbe3a61fe5687721f209c17e8bbfa9c7472d96ec83f23d520a
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/claw-pr-preflight.json
    sha256: dec7ef0301105e3066b7034271546c5f08b1d4e5edf1cc0e1006a2b115784e96
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/compare_candidates.py
    sha256: 746f7ab7ad10ac3cb06806491fa5c542a4bbe309d4d13e1bddad1b78d6775b65
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/date-contract.json
    sha256: 4b2ae778b2ad314cee47cf1b4bbaf4f7e4cd45da692125d857c1cd21a1e95cc4
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/date-mutation-results.json
    sha256: c5b5c24393a9f896e130da4787b72930bc2fa25b9722df8bcdf9fc36a2599b62
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/generation-result.json
    sha256: 0b30ab393f7c4ea403d18f653142bbb40f2fb28a7f71e9014f4ab2ed4b1c0ac9
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/generation-start.json
    sha256: 0493feb031cbb53bff4c0276385a94da67b2e914fff906e1dbc38f227e57ba66
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/generator-followup.patch
    sha256: 095ae6173d2c3a9c51ca2137bc7f67c4a928968a3058b22c57e7870cb8f9460e
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/historical-rule-k-holds.json
    sha256: a3ab2487192691c441a53cd6a33ba48bb3272dbec67fe8819ef5b15a8e575334
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/issue-684.json
    sha256: b89ded85a97cbfcf5ca0ff7ad6b900cd031f6154c27f5480eca7cdedcabcd003
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/issue-685.json
    sha256: 045f5788c96ecf815969c9b29b34a293b290227b1a7e48c4576e3c54b3ae5a55
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/issue-686.json
    sha256: f6912412f68a7a62fdf072879831702844017c9c47306a1d590b18ee9f3ac925
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/locked_generation.py
    sha256: b4acc68c765aa3230b62f7561f6ce79e75daaa1fe72d439ed97a65517cc62511
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup684_green.json
    sha256: e438afe9e2f48f480228fdabf1aa26e619162e02e967adca659d0015b821f09f
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup684_green.log
    sha256: 56064bd35b8b5b212acf7d72c7a8c2e8f8a15498cb878a3f44734087398eaa70
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup684_mutation.json
    sha256: 5cba6c93c57ab15c0caa839f62e787af97b97bfa7f14f04005d84faef44610d1
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup684_mutation.log
    sha256: 2319a501303728d69f2503cc584091b1c7287fe1885658f7eb93bf5f0cb4afb0
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup684_native_b1_b5.json
    sha256: c3bc2b9d47f190b4c1cf81be59a05a9c1c63f2c669d1925bedb8b16b936a38cf
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup684_native_b1_b5.log
    sha256: 3cd708da04cf603976e60593214493a03ad16586199d6d5b8af0973c10a7bd88
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup684_red.json
    sha256: 16b6e21966b88cdb08e54ee871e827edaf9d62b4a27afc36204d80b9e48b6135
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup684_red.log
    sha256: cfbaf2f235fa47726ab5068230ebe2a4c16a33041e67ba99c3c802b2ee2120b0
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup684_restored.json
    sha256: 1811493528a821a405294d44c16ebb0163fefed69e45ea6635e1c3cd170a2e43
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup684_restored.log
    sha256: 56064bd35b8b5b212acf7d72c7a8c2e8f8a15498cb878a3f44734087398eaa70
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup684_ruff.json
    sha256: 90e9ddfe32310c9845e50bf0e5ddd13de359e52fb1cc2bd731ed8b30cc33be93
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup684_ruff.log
    sha256: ab960078234ac3697fb507c8fdadea23ac7e81c44106a364eadf43bd5b0a42b6
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup684_ruff_offline.json
    sha256: 5433fa6222eee9fd5960b37a672c4d92762295701debcec717fad3dd7c2f1faf
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup684_ruff_offline.log
    sha256: 82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup686_green.json
    sha256: 34bc4d3d8703cd114fa2e134e046cb4ee004069ede6d9cd57fcd308207fb995d
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup686_green.log
    sha256: 92255cd92a064074a66b46e5ca14f00e91042146d69627ec984664821f3a5d81
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup686_mutation_mapping_date.json
    sha256: 35d7143b57ed9fc5d568e8da68dc6ef745233e1db69db4134779f39d222c652f
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup686_mutation_mapping_date.log
    sha256: 39253bad335d22a61599b6adb361d7ce747ce9af67547ca21cd6ff70d595e572
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup686_mutation_mapping_set_version.json
    sha256: b34738c2d450cd0ff54fe158d5fd4c36128fb7470e29d23b39e1226af0f2fc00
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup686_mutation_mapping_set_version.log
    sha256: b165a9a5567393672ad2b19893291d9e25e8fc698a5cd953af60af431c292594
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup686_red.json
    sha256: 9b8d726547d48a810ec9faf7d9ff2c188b78680c6692336177be89d07c2753f3
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup686_red.log
    sha256: 4f81cddfd71608c0a38907e45f3cd64fd435713c2f2f778ef0f32eadc67c5076
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_baseline_b4_actual.json
    sha256: 823c5cf69471facde0d81fe35142fd6b253413983ba0c9bcfee253ddcde56815
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_baseline_b4_actual.log
    sha256: 2dc591600b6984cf158d2eaf18d714516fc4a5dba63aa84f3f5aeaf7b05ca66e
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_baseline_curie.json
    sha256: 7c5cdc2a1904cadf40fdffc08f23ad4d126fe69e421ce33f52efb1d474ebbf11
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_baseline_curie.log
    sha256: 6676b7749496134b25fcfb996fc3a5fed1106c96ba37f1c13735b6800ca48fad
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_baseline_products.json
    sha256: 94aaf96723f483286fd897869ffddec25bc64492f6fede9d41991e5a56840ee8
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_baseline_products.log
    sha256: 1fa143fbbbdb204cfca441d722014ca3b2ab5eda915eb2f6de1b7dc997e1d335
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_baseline_reconcile.json
    sha256: 2e0e0a4efa09ad34c0283fae4cd3eb59d3fdca3381cc88a213c07a6ca91d766c
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_baseline_reconcile.log
    sha256: 8bf18010d973e92de327bf8580964cbe3306206d7191c45a7b1731df9c7d61d7
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_baseline_subjects.json
    sha256: f636ee115560ee279641e1a502fb393120f74e501cbb2226b1095c3a658d37fe
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_baseline_subjects.log
    sha256: a16772841d62c8f1f9be43c85a24d0e9c1e687b6ec493652fd2c5be113da7762
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_candidate_b4_actual.json
    sha256: 56784668fe4f56bda9345c3cbdee43a23ebe5a01562dff0ce0f9a6b26566aa5a
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_candidate_b4_actual.log
    sha256: 18f5e330290bcd99ff8fba6b38e29a7d501d863493834219d6de51c6a5a29acd
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_candidate_curie.json
    sha256: 0a06ee4a818251c95c0a8387cd070b033359015c56101dc324725e71dbd8f194
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_candidate_curie.log
    sha256: 31ca9b6d8a11e0181035e649476ee2a2c01b4b1cc04d7df1c6f0ebb182fab99e
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_candidate_invariants.json
    sha256: 720a9f73b86b58974a8eff8dcff55d7f6b38621a22c6cbac0985a9254b8ef8a5
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_candidate_invariants.log
    sha256: 614aed9ff60f6b713118d760bfbf23d452531ffcc336fd089b0ebbfb74a2eb43
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_candidate_products.json
    sha256: 31509c6f67351b740dc469e17eb728329d4f5080205c031ad1de6dd5f4882dad
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_candidate_products.log
    sha256: b0695b05145765cb47f8ce259be004e003f012c9fdc69ecc502c598d22a8f38d
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_candidate_schema.json
    sha256: 31bd61a1fc27a8171289cd5a505e934656c0ec91021417dc34f4f6065e90a4a0
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_candidate_schema.log
    sha256: 6bb3a5fb4906f5382c09aa0eb0a8e6dbe45d2fe31c6dd726e030e30461fa4c2c
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_capture_inputs.json
    sha256: 27da133dd832e69c1985c4ead154901b27c3e1c579968a7f7a87175c98f4c30a
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_capture_inputs.log
    sha256: bf4e7c23f25bce4f887ada80c00b2a2f587e2d6caa15275b077916a02fd07ce2
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_compare_candidates.json
    sha256: 3c1105bd82034180e3e312df73031d21bbbdd96a96e7e0116ae6cf0c92d6081b
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_compare_candidates.log
    sha256: a03d239c21d000fa89843765fef95481fd8df2922142b7e9762f0a598e32a28d
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_compare_candidates_final.json
    sha256: 1ead259875e68597323dcae39002e97bcbd9cd7e2d571597e56777c5a0f38ade
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_compare_candidates_final.log
    sha256: 266ff3f69585da30906715786c39faf25b27bb34dd95b39282c26391dcd20742
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_compare_candidates_retry.json
    sha256: a771984087cf024c722a5a9f7d6f98e00d0958342f131fe4003016bb65943df9
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_compare_candidates_retry.log
    sha256: 57978937674f4e99d64986c89d01026fb7d48f628592d75ecd1dd58852391a3e
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_config_validate.json
    sha256: 0da8e656c9f27df17d890928a841e4c9529b7101fb2d68f1a54db0545d38db59
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_config_validate.log
    sha256: 8530b860a1a29e581c4807df15a46ddfbbe0a16a8485e6339366c14ca44cb24c
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_focused.json
    sha256: 64bf7d13fd479b94515434765d4f51bc3eb078a4e7f01e859b39ac89a6c9c034
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_focused.log
    sha256: cd69b353884e21a1527ed705ef0ce9ed7af14246b850fed98c52974e5131154c
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_focused_restored.json
    sha256: b82fb496ec3f5fe328fb65666b93275c106900a6ec08d5f7d6940a84cc0ca82d
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_focused_restored.log
    sha256: cd69b353884e21a1527ed705ef0ce9ed7af14246b850fed98c52974e5131154c
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_full_qc.json
    sha256: ba8fc27bf764f313658b19bb9a7e16ea1ccac7c7bfa21167778f1aa9242e4ddc
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_full_qc.log
    sha256: 00c92232a98db7fd0c00bfaad7a407ce386e48930912b123fdb9150e2b305a00
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_full_tests.json
    sha256: 0d600c4a8c1fe2c9d40b380077e536785c2f7bc69cac2bb1c800c4f51916587b
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_full_tests.log
    sha256: 8990e85b0a29a76e7fc64b910a7883c26b2e1544272b7d4d3d947e30b054caeb
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_generate_candidate.json
    sha256: 31dd39b9e0caae7114d3a7576eeb6e444efdf1b771428038057222dfaadd9903
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_generate_candidate.log
    sha256: 9035c77289683a4e178d8d3fbffe379841a645c7160fc37827f21770144e656f
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_lint.json
    sha256: ed736fbcc1abf9092a411d83f557bc4b7348d17500de1d2eb968ee6602449683
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_lint.log
    sha256: 82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_mypy.json
    sha256: c736fcca82367caff072a523de0eaeaa271e96e8f0b9f677f375fce3e81d6a52
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_mypy.log
    sha256: a97cee1ee1bdb5e2d1ca7098f7b33a6c6a21263225643192fdeb78654687ed89
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_rule_f_integration.json
    sha256: 268876b8b09105a6fefd96ebb2ff1957ecc874b4855f033669c131686e4009bb
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_rule_f_integration.log
    sha256: a237187037282eb9a823a8c7865129999ce33618ceae7896757d56680ca80ce2
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_safety_coverage.json
    sha256: 04e7a03783e46174d7b5df77156f4aadfc0b9675119416d8fa9f7144b0893d99
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_safety_coverage.log
    sha256: 90fc585c5e2ac307496927dd7dcc250d711e1419be9211038e6850ccb26aee5a
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/mim-pr-preflight.json
    sha256: 1ccbebed654407e2cf87b69200f4352be56f654eea6dc1d1be8b386ab8541521
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/old-candidate-changes.json
    sha256: 42ff29f9bcbd4d1545998020eb705664cea668f52a19ced698090826031c5bff
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/original-41-remediation.json
    sha256: 15646d0468a3bb985eb0f4510968c338f1fc764a3dcc75719e84289267df83bf
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/other-field-changes.json
    sha256: ef4eb44db9a5f9f4f311633250044a0f0a8704a77de4c5d544a5269c1e27db68
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/overlap-pr-snapshots.json
    sha256: cb44be1357eba398a5555529d61ab447e59755ae120788e60f7f1f7e614d8d95
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/path-overlap.json
    sha256: 7596a73e052f8a3f31d591c4648980cfcae839d7849c442b5a38d7d951d26977
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/post-validation-preservation.json
    sha256: a199df86c51d669c6ff5b9214d23a838ab592eda0039cf7cf93347f0e4deacf9
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/previous-candidate-changes.json
    sha256: 48c95563717636db4a98697922e3f2c840c8a62b8a2a20ccf7e63c6f583300b9
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/prove_rule_f_integration.py
    sha256: 41d7fcf4e66ab3ec1bfa0ec4cac24314dd41cc64381813654cf4496eea7d07a3
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/recipes/run.py
    sha256: 4666d3c7428ff05b28492675fe75182c87a80dbc1925e29d8911f21c68a2d2c8
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/review-targets.json
    sha256: 23d84ac8d61c7ca70622efd5353412e8e8c332f904d257eec58940d8db3ff30c
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/rule-f-integration/native-rule-f-rejects.tsv
    sha256: afcd76f28988eee0a50a6f245fc782aa184642dc1b6ae65dd81ed3c9b9cbc17a
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/rule-f-integration/receipt.json
    sha256: 19c412100d7cb54659808d6c1821476b80f0d4cf9c723937a8883f5d7af393bd
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/rule-f-integration/records/Dated.yaml
    sha256: 5824513df338c3447c434c8ee280f3fa09c93ce5a002d5f8853a9881291dba72
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/rule-f-integration/records/Dateless_One.yaml
    sha256: aea26f011fd36c07ddc031b367d75f9ef7d638b2fbc3cc544c29d78253f154bc
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/rule-f-integration/records/Dateless_Two.yaml
    sha256: 91e6468ffbdfbeea67b05a00f198d7c12ba6d988c57f3646f8b7a64f84d6d8dc
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/rule-f-integration/synthetic.sssom.tsv
    sha256: dd53b1cf36dbc9ee3007528682de51410538a721ef7ee173885b99da90206edf
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/source-baseline.json
    sha256: 10069d0e920c60a7f36d0c6e31cbbdbf849c2e26227d76d9b96a4d0020ca3694
    role: context
  - path: reports/sssom_generation_repair_20261031/followup-684-686/validation-inputs.json
    sha256: 9523ad34a1477521a95c1dd6216d80262a50d83fd56f68ad00d0983e49ae82ab
    role: context
  - path: reviews/structured/20261031T214143Z-sssom-current-inputs-mechanical/review.yaml
    sha256: 56a5186a8db1280d39a0e4c021bd79de77d2dd0116c026e3e754a128c30e594e
    role: context
  - path: reviews/structured/20261031T233012Z-sssom-native-repair-mechanical/review.yaml
    sha256: f36a34f9adc63223b55710ed721cf0127c78ed4db9cfe27531ef1eab02c75a59
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/reconcile_sssom.py
    sha256: 7a0d1b248a1ae1777a827bde4e795474531db565c17b35beaab66fb2631daba7
    role: context
  - path: scripts/validate_sssom_invariants.py
    sha256: 89821559f9cbf999675b163396140c4b035cac7bf3ae23dd709f8b76e149de77
    role: context
  - path: src/mediaingredientmech/schema/mediaingredientmech.yaml
    sha256: bb43dee29b21fdee72a48022456e733e49e95824c4c09674f9b3165c290fe012
    role: context
scope:
  description: Bounded mechanical successor review of exact canonical and final 9294730
    diagnostic output.
  selection: Two exact TSV targets with all rows evaluated by applicable native gates;
    original B5/K/G candidate finding identities and affected selectors retained.
  coverage: full
  population_size: 2
  reviewed_target_ids:
  - canonical
  - candidate
  exclusions:
  - target: Scientific relation/identity review and release approval
    reason: No new source research, paid provider calls or identity choices; historical
      nonexact release holds remain.
  - target: Supported/withheld partition regeneration
    reason: The prior partition remains historical canonical evidence; this task does
      not rebind it to candidate bytes.
  - target: CultureMech import or unified mapping replacement
    reason: Current CM outputs and KG Mediadive nodes remain comparison-only; no bulk
      import or overlap with separate unified-mapping work.
targets:
- target_id: canonical
  path: mappings/ingredient_mappings.sssom.tsv
  label: 'Unchanged maintained canonical mapping: 2,987 rows'
  kind: generated
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Maintained identity/mapping/synonym owner; no curation change in this run.
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_mim_ingredient_sssom.py
    role: External SSSOM generator; follow-up 684-686 at exact 9294730aeb19d269899177678db87406f4251555;
      prior repairs retained.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_Nitrate_070_M_Stock.yaml
    role: Maintained primary identifier and parent relation for the generated B1 alias
      namespace change; record bytes unchanged.
- target_id: candidate
  path: output/sssom-followup-684-686/ingredient_mappings.sssom.tsv
  label: 'Final 9294730 diagnostic candidate: 2,980 rows; not promoted'
  kind: generated
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Maintained identity/mapping/synonym owner; no curation change in this run.
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_mim_ingredient_sssom.py
    role: External SSSOM generator; follow-up 684-686 at exact 9294730aeb19d269899177678db87406f4251555;
      prior repairs retained.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_Nitrate_070_M_Stock.yaml
    role: Maintained primary identifier and parent relation for the generated B1 alias
      namespace change; record bytes unchanged.
checks:
- check_id: followup_generate_candidate
  name: followup generate candidate
  status: passed
  required: true
  summary: Unmodified native builder at committed 9294730, verified target and owned
    lock, generated 2,980 rows at a new path. Generator source SHA is identical before
    and after invocation.
  target_ids:
  - candidate
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/claw
    && uv run python ../followup-684-686/locked_generation.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-followup_generate_candidate
  scope_note: Actual run 2026-11-01T00:12:33.617607+00:00 through 2026-11-01T00:14:20.828318+00:00;
    original log at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/followup_generate_candidate.log.
- check_id: followup_candidate_invariants
  name: followup candidate invariants
  status: passed
  required: true
  summary: Strict native rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L pass
    with header-only reject TSV. Default-path B4 skip is supplemented separately.
  target_ids:
  - candidate
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/mim
    && uv run python scripts/validate_sssom_invariants.py output/sssom-followup-684-686/ingredient_mappings.sssom.tsv
    --reject-tsv output/sssom-followup-684-686/native-rejected-rows.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-followup_candidate_invariants
  scope_note: Actual run 2026-11-01T00:14:28.669774+00:00 through 2026-11-01T00:14:37.219467+00:00;
    original log at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/followup_candidate_invariants.log.
- check_id: followup_candidate_schema
  name: followup candidate schema
  status: passed
  required: true
  summary: SSSOM JSON Schema, prefix completeness and strict CURIE validation pass;
    native extension notices retained.
  target_ids:
  - candidate
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/mim
    && sssom validate -V JsonSchema -V PrefixMapCompleteness -V StrictCurieFormat
    output/sssom-followup-684-686/ingredient_mappings.sssom.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-followup_candidate_schema
  scope_note: Actual run 2026-11-01T00:14:28.665454+00:00 through 2026-11-01T00:14:30.623862+00:00;
    original log at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/followup_candidate_schema.log.
- check_id: followup_candidate_curie
  name: followup candidate curie
  status: passed
  required: true
  summary: 2,980 rows / 5,960 CURIEs pass native syntax and prefix checks.
  target_ids:
  - candidate
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/mim
    && uv run python scripts/validate_published_curies.py output/sssom-followup-684-686/ingredient_mappings.sssom.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-followup_candidate_curie
  scope_note: Actual run 2026-11-01T00:14:28.666941+00:00 through 2026-11-01T00:14:28.717788+00:00;
    original log at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/followup_candidate_curie.log.
- check_id: followup_candidate_products
  name: followup candidate products
  status: passed
  required: true
  summary: 'Unchanged configured native label policy passes: 2,216 canonical, four
    synonym, four exception pairs; 3,736 no-adapter skips remain.'
  target_ids:
  - candidate
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/mim
    && uv run python scripts/validate_id_label_correspondence.py --config ../followup-684-686/candidate-id-label-config.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-followup_candidate_products
  scope_note: Actual run 2026-11-01T00:14:28.671371+00:00 through 2026-11-01T00:15:01.827706+00:00;
    original log at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/followup_candidate_products.log.
- check_id: followup_compare_candidates_final
  name: followup compare candidates final
  status: passed
  required: true
  summary: Final comparison proves exactly one alias replacement since the previous
    repaired candidate; 2,979 rows identical; no row dates, headers, predicates or
    other fields change. Original 41 diagnostic dispositions remain satisfied and
    native drift is zero.
  target_ids:
  - canonical
  - candidate
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/mim
    && uv run python ../followup-684-686/compare_candidates.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-followup_compare_candidates_final
  scope_note: Actual run 2026-11-01T00:14:58.976559+00:00 through 2026-11-01T00:14:59.995247+00:00;
    original log at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/followup_compare_candidates_final.log.
- check_id: followup_full_qc
  name: followup full qc
  status: passed
  required: true
  summary: Full native just qc passes on unchanged maintained data, including roundtrip
    and flat coverage. Candidate validation is separate.
  target_ids:
  - canonical
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/mim
    && just qc
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-followup_full_qc
  scope_note: Actual run 2026-11-01T00:12:23.364625+00:00 through 2026-11-01T00:14:46.312948+00:00;
    original log at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/followup_full_qc.log.
- check_id: followup_baseline_curie
  name: followup baseline curie
  status: passed
  required: true
  summary: Canonical 2,987 rows / 5,974 CURIEs pass; 20 tests passed and one skipped.
  target_ids:
  - canonical
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/mim
    && just curie-validate
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-followup_baseline_curie
  scope_note: Actual run 2026-11-01T00:12:44.500377+00:00 through 2026-11-01T00:12:45.053146+00:00;
    original log at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/followup_baseline_curie.log.
- check_id: followup_baseline_reconcile
  name: followup baseline reconcile
  status: passed
  required: true
  summary: Canonical GAP, ORPHAN, STALE, PREDICATE and GRADE counts are all zero.
  target_ids:
  - canonical
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/mim
    && uv run python scripts/reconcile_sssom.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-followup_baseline_reconcile
  scope_note: Actual run 2026-11-01T00:12:44.500374+00:00 through 2026-11-01T00:12:50.503391+00:00;
    original log at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/followup_baseline_reconcile.log.
- check_id: followup_baseline_products
  name: followup baseline products
  status: passed
  required: true
  summary: Full product enforcement passes with 101 nonblocking warnings and 5,314
    no-adapter skips.
  target_ids:
  - canonical
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/mim
    && just validate-products
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-followup_baseline_products
  scope_note: Actual run 2026-11-01T00:12:34.780535+00:00 through 2026-11-01T00:13:37.155425+00:00;
    original log at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/followup_baseline_products.log.
- check_id: followup_baseline_subjects
  name: followup baseline subjects
  status: passed
  required: false
  summary: Native checker retains 18 non-gating subject/filename warnings among 2,611
    subjects and 2,953 record files.
  target_ids:
  - canonical
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/mim
    && uv run python scripts/check_sssom_subject_files.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-followup_baseline_subjects
  scope_note: Actual run 2026-11-01T00:12:44.500679+00:00 through 2026-11-01T00:12:44.552060+00:00;
    original log at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/followup_baseline_subjects.log.
- check_id: followup_candidate_b4_actual
  name: followup candidate b4 actual
  status: passed
  required: false
  summary: Native B4 with actual read-only KG transforms reports zero findings; missing
    BTO/MICRO transforms and absent-ID skips remain.
  target_ids:
  - candidate
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/mim
    && uv run python ../followup-684-686/check_b4_actual.py output/sssom-followup-684-686/ingredient_mappings.sssom.tsv
    candidate
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-followup_candidate_b4_actual
  scope_note: Actual run 2026-11-01T00:14:28.658472+00:00 through 2026-11-01T00:14:29.526333+00:00;
    original log at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/followup_candidate_b4_actual.log.
- check_id: followup_baseline_b4_actual
  name: followup baseline b4 actual
  status: passed
  required: false
  summary: Actual-path native B4 reports zero canonical findings with the same limits.
  target_ids:
  - canonical
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/mim
    && uv run python ../followup-684-686/check_b4_actual.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-followup_baseline_b4_actual
  scope_note: Actual run 2026-11-01T00:13:40.660889+00:00 through 2026-11-01T00:13:41.484534+00:00;
    original log at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/followup_baseline_b4_actual.log.
- check_id: followup_rule_f_integration
  name: followup rule f integration
  status: passed
  required: true
  summary: Native YAML extraction and CLI writer retain two dateless synthetic records
    alongside one dated record. Unmodified native Rule F returns both dateless subjects
    and writes two rejects; Rule G returns zero.
  target_ids:
  - candidate
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/claw
    && uv run python ../followup-684-686/prove_rule_f_integration.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-followup_rule_f_integration
  scope_note: Actual run 2026-11-01T00:12:23.364618+00:00 through 2026-11-01T00:12:23.491621+00:00;
    original log at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/followup_rule_f_integration.log.
- check_id: followup_focused_restored
  name: followup focused restored
  status: passed
  required: true
  summary: All 84 focused regression tests pass on final source restored after mutation
    checks.
  target_ids:
  - candidate
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/claw
    && uv run --extra dev python -m pytest -q --no-cov tests/test_mapping_date.py
    tests/test_mim_sssom_header_dates.py tests/test_sssom_identity_row.py tests/test_mim_synonym_scope.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-followup_focused_restored
  scope_note: Actual run 2026-11-01T00:11:46.950665+00:00 through 2026-11-01T00:11:47.393979+00:00;
    original log at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/followup_focused_restored.log.
- check_id: followup_lint
  name: followup lint
  status: passed
  required: true
  summary: Repository-pinned Ruff passes for the final code.
  target_ids:
  - candidate
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/claw
    && uvx --offline ruff@0.16.3 check cli plugins pipelines src tests scripts/build_mim_ingredient_sssom.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-followup_lint
  scope_note: Actual run 2026-11-01T00:11:46.950584+00:00 through 2026-11-01T00:11:46.976394+00:00;
    original log at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/followup_lint.log.
- check_id: followup_mypy
  name: followup mypy
  status: passed
  required: true
  summary: Native maintained type-check command passes.
  target_ids:
  - candidate
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/claw
    && uv run --extra dev mypy cli/main.py plugins/repository_settings.py plugins/lock_manager.py
    plugins/git_integration.py plugins/just_runner.py src/kg_microbe_history src/kg_microbe_kgscan
    src/kg_microbe_fleet src/kg_microbe_embeddings src/kg_microbe_merge_queue src/kg_microbe_research
    src/kg_microbe_write src/kg_microbe_workflows src/kg_microbe_progress src/kg_microbe_consistency
    src/kg_microbe_patches src/kg_microbe_governance/__init__.py src/kg_microbe_governance/__main__.py
    src/kg_microbe_governance/fleet_audit.py src/kg_microbe_governance/artifacts/scripts/check_vendored_sync.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-followup_mypy
  scope_note: Actual run 2026-11-01T00:11:57.833941+00:00 through 2026-11-01T00:12:03.031019+00:00;
    original log at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/followup_mypy.log.
- check_id: followup_full_tests
  name: followup full tests
  status: passed
  required: true
  summary: Full CLAW CI-style suite passes on exact final head; this checks code behavior,
    not scientific approval.
  target_ids:
  - candidate
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/claw
    && uv run --extra dev python -m pytest -q --cov=src --cov=cli.main --cov=plugins.repository_settings
    --cov=plugins.lock_manager --cov=plugins.git_integration --cov=plugins.just_runner
    --cov-report=term-missing --cov-fail-under=70
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-followup_full_tests
  scope_note: Actual run 2026-11-01T00:12:06.207505+00:00 through 2026-11-01T00:17:42.585973+00:00;
    original log at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/followup_full_tests.log.
- check_id: followup_safety_coverage
  name: followup safety coverage
  status: passed
  required: true
  summary: Native safety-module coverage gate passes.
  target_ids:
  - candidate
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/claw
    && uv run --extra dev coverage report --include=cli/main.py,plugins/repository_settings.py,plugins/lock_manager.py,plugins/git_integration.py,plugins/just_runner.py
    --fail-under=60
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-followup_safety_coverage
  scope_note: Actual run 2026-11-01T00:18:01.215721+00:00 through 2026-11-01T00:18:01.381623+00:00;
    original log at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/followup_safety_coverage.log.
- check_id: followup684_mutation
  name: followup684 mutation
  status: passed
  required: false
  summary: Reverting registry namespace repair produces the expected test failure.
  target_ids:
  - candidate
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/claw
    && uv run python -m pytest -q -p no:cacheprovider --basetemp ../test-tmp/followup684-mutation
    tests/test_sssom_identity_row.py
  exit_code: 1
  expected_exit_code: 1
  evidence_ids:
  - log-followup684_mutation
  scope_note: Actual run 2026-11-01T00:11:01.909815+00:00 through 2026-11-01T00:11:02.265719+00:00;
    original log at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/followup684_mutation.log.
- check_id: followup686_mutation_mapping_date
  name: followup686 mutation mapping date
  status: passed
  required: false
  summary: Reverting the header mapping_date behavior produces the expected regression
    failure.
  target_ids:
  - candidate
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/claw
    && uv run --extra dev python -m pytest -q --no-cov tests/test_mapping_date.py
  exit_code: 1
  expected_exit_code: 1
  evidence_ids:
  - log-followup686_mutation_mapping_date
  scope_note: Actual run 2026-11-01T00:11:40.862750+00:00 through 2026-11-01T00:11:41.305656+00:00;
    original log at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/followup686_mutation_mapping_date.log.
- check_id: followup686_mutation_mapping_set_version
  name: followup686 mutation mapping set version
  status: passed
  required: false
  summary: Reverting the header mapping_set_version behavior produces the expected
    regression failure.
  target_ids:
  - candidate
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/claw
    && uv run --extra dev python -m pytest -q --no-cov tests/test_mim_sssom_header_dates.py
  exit_code: 1
  expected_exit_code: 1
  evidence_ids:
  - log-followup686_mutation_mapping_set_version
  scope_note: Actual run 2026-11-01T00:11:41.333321+00:00 through 2026-11-01T00:11:41.709379+00:00;
    original log at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/followup686_mutation_mapping_set_version.log.
- check_id: followup_compare_candidates
  name: followup compare candidates
  status: failed
  required: false
  summary: Initial diagnostic helper assertion omitted the legitimate historical-stamp
    removal on the new alias; it failed before writing comparisons. Final helper explicitly
    verifies that removal.
  target_ids:
  - candidate
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/mim
    && uv run python ../followup-684-686/compare_candidates.py
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - log-followup_compare_candidates
  scope_note: Actual run 2026-11-01T00:14:28.660976+00:00 through 2026-11-01T00:14:28.745109+00:00;
    original log at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/followup_compare_candidates.log.
evidence:
- evidence_id: log-followup_generate_candidate
  kind: validation
  reference: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_generate_candidate.log
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: Unmodified native builder at committed 9294730, verified target and owned
    lock, generated 2,980 rows at a new path. Generator source SHA is identical before
    and after invocation.
  snapshot_sha256: 9035c77289683a4e178d8d3fbffe379841a645c7160fc37827f21770144e656f
- evidence_id: log-followup_candidate_invariants
  kind: validation
  reference: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_candidate_invariants.log
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: Strict native rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L pass
    with header-only reject TSV. Default-path B4 skip is supplemented separately.
  snapshot_sha256: 614aed9ff60f6b713118d760bfbf23d452531ffcc336fd089b0ebbfb74a2eb43
- evidence_id: log-followup_candidate_schema
  kind: validation
  reference: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_candidate_schema.log
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: SSSOM JSON Schema, prefix completeness and strict CURIE validation pass;
    native extension notices retained.
  snapshot_sha256: 6bb3a5fb4906f5382c09aa0eb0a8e6dbe45d2fe31c6dd726e030e30461fa4c2c
- evidence_id: log-followup_candidate_curie
  kind: validation
  reference: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_candidate_curie.log
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: 2,980 rows / 5,960 CURIEs pass native syntax and prefix checks.
  snapshot_sha256: 31ca9b6d8a11e0181035e649476ee2a2c01b4b1cc04d7df1c6f0ebb182fab99e
- evidence_id: log-followup_candidate_products
  kind: validation
  reference: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_candidate_products.log
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: 'Unchanged configured native label policy passes: 2,216 canonical, four
    synonym, four exception pairs; 3,736 no-adapter skips remain.'
  snapshot_sha256: b0695b05145765cb47f8ce259be004e003f012c9fdc69ecc502c598d22a8f38d
- evidence_id: log-followup_compare_candidates_final
  kind: validation
  reference: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_compare_candidates_final.log
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: Final comparison proves exactly one alias replacement since the previous
    repaired candidate; 2,979 rows identical; no row dates, headers, predicates or
    other fields change. Original 41 diagnostic dispositions remain satisfied and
    native drift is zero.
  snapshot_sha256: 266ff3f69585da30906715786c39faf25b27bb34dd95b39282c26391dcd20742
- evidence_id: log-followup_full_qc
  kind: validation
  reference: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_full_qc.log
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: Full native just qc passes on unchanged maintained data, including roundtrip
    and flat coverage. Candidate validation is separate.
  snapshot_sha256: 00c92232a98db7fd0c00bfaad7a407ce386e48930912b123fdb9150e2b305a00
- evidence_id: log-followup_baseline_curie
  kind: validation
  reference: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_baseline_curie.log
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: Canonical 2,987 rows / 5,974 CURIEs pass; 20 tests passed and one skipped.
  snapshot_sha256: 6676b7749496134b25fcfb996fc3a5fed1106c96ba37f1c13735b6800ca48fad
- evidence_id: log-followup_baseline_reconcile
  kind: validation
  reference: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_baseline_reconcile.log
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: Canonical GAP, ORPHAN, STALE, PREDICATE and GRADE counts are all zero.
  snapshot_sha256: 8bf18010d973e92de327bf8580964cbe3306206d7191c45a7b1731df9c7d61d7
- evidence_id: log-followup_baseline_products
  kind: validation
  reference: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_baseline_products.log
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: Full product enforcement passes with 101 nonblocking warnings and 5,314
    no-adapter skips.
  snapshot_sha256: 1fa143fbbbdb204cfca441d722014ca3b2ab5eda915eb2f6de1b7dc997e1d335
- evidence_id: log-followup_baseline_subjects
  kind: validation
  reference: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_baseline_subjects.log
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: Native checker retains 18 non-gating subject/filename warnings among 2,611
    subjects and 2,953 record files.
  snapshot_sha256: a16772841d62c8f1f9be43c85a24d0e9c1e687b6ec493652fd2c5be113da7762
- evidence_id: log-followup_candidate_b4_actual
  kind: validation
  reference: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_candidate_b4_actual.log
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: Native B4 with actual read-only KG transforms reports zero findings; missing
    BTO/MICRO transforms and absent-ID skips remain.
  snapshot_sha256: 18f5e330290bcd99ff8fba6b38e29a7d501d863493834219d6de51c6a5a29acd
- evidence_id: log-followup_baseline_b4_actual
  kind: validation
  reference: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_baseline_b4_actual.log
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: Actual-path native B4 reports zero canonical findings with the same limits.
  snapshot_sha256: 2dc591600b6984cf158d2eaf18d714516fc4a5dba63aa84f3f5aeaf7b05ca66e
- evidence_id: log-followup_rule_f_integration
  kind: validation
  reference: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_rule_f_integration.log
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: Native YAML extraction and CLI writer retain two dateless synthetic records
    alongside one dated record. Unmodified native Rule F returns both dateless subjects
    and writes two rejects; Rule G returns zero.
  snapshot_sha256: a237187037282eb9a823a8c7865129999ce33618ceae7896757d56680ca80ce2
- evidence_id: log-followup_focused_restored
  kind: validation
  reference: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_focused_restored.log
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: All 84 focused regression tests pass on final source restored after mutation
    checks.
  snapshot_sha256: cd69b353884e21a1527ed705ef0ce9ed7af14246b850fed98c52974e5131154c
- evidence_id: log-followup_lint
  kind: validation
  reference: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_lint.log
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: Repository-pinned Ruff passes for the final code.
  snapshot_sha256: 82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18
- evidence_id: log-followup_mypy
  kind: validation
  reference: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_mypy.log
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: Native maintained type-check command passes.
  snapshot_sha256: a97cee1ee1bdb5e2d1ca7098f7b33a6c6a21263225643192fdeb78654687ed89
- evidence_id: log-followup_full_tests
  kind: validation
  reference: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_full_tests.log
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: Full CLAW CI-style suite passes on exact final head; this checks code behavior,
    not scientific approval.
  snapshot_sha256: 8990e85b0a29a76e7fc64b910a7883c26b2e1544272b7d4d3d947e30b054caeb
- evidence_id: log-followup_safety_coverage
  kind: validation
  reference: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_safety_coverage.log
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: Native safety-module coverage gate passes.
  snapshot_sha256: 90fc585c5e2ac307496927dd7dcc250d711e1419be9211038e6850ccb26aee5a
- evidence_id: log-followup684_mutation
  kind: validation
  reference: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup684_mutation.log
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: Reverting registry namespace repair produces the expected test failure.
  snapshot_sha256: 2319a501303728d69f2503cc584091b1c7287fe1885658f7eb93bf5f0cb4afb0
- evidence_id: log-followup686_mutation_mapping_date
  kind: validation
  reference: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup686_mutation_mapping_date.log
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: Reverting the header mapping_date behavior produces the expected regression
    failure.
  snapshot_sha256: 39253bad335d22a61599b6adb361d7ce747ce9af67547ca21cd6ff70d595e572
- evidence_id: log-followup686_mutation_mapping_set_version
  kind: validation
  reference: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup686_mutation_mapping_set_version.log
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: Reverting the header mapping_set_version behavior produces the expected
    regression failure.
  snapshot_sha256: b165a9a5567393672ad2b19893291d9e25e8fc698a5cd953af60af431c292594
- evidence_id: log-followup_compare_candidates
  kind: validation
  reference: reports/sssom_generation_repair_20261031/followup-684-686/logs/followup_compare_candidates.log
  accessed_at: '2026-11-01T00:18:15Z'
  support: context_only
  summary: Initial diagnostic helper assertion omitted the legitimate historical-stamp
    removal on the new alias; it failed before writing comparisons. Final helper explicitly
    verifies that removal.
  snapshot_sha256: a03d239c21d000fa89843765fef95481fd8df2922142b7e9762f0a598e32a28d
- evidence_id: prior-review
  kind: prior_review
  reference: reviews/structured/20261031T233012Z-sssom-native-repair-mechanical/review.yaml
  accessed_at: '2026-11-01T00:18:15Z'
  support: context_only
  summary: Immutable prior review; all affected candidate target IDs and original
    issue keys are preserved.
  snapshot_sha256: f36a34f9adc63223b55710ed721cf0127c78ed4db9cfe27531ef1eab02c75a59
- evidence_id: comparison
  kind: record_content
  reference: reports/sssom_generation_repair_20261031/followup-684-686/candidate-comparison.json
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: Exact separate comparisons with previous repaired candidate, original rejected
    candidate and canonical mapping.
  snapshot_sha256: 266ff3f69585da30906715786c39faf25b27bb34dd95b39282c26391dcd20742
- evidence_id: previous-changes
  kind: record_content
  reference: reports/sssom_generation_repair_20261031/followup-684-686/previous-candidate-changes.json
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: Removed compound alias and added ingredient alias, with corresponding source/comment
    changes and blank validation_method on the new triple. Curated identifier and
    parent relation unchanged.
  snapshot_sha256: 48c95563717636db4a98697922e3f2c840c8a62b8a2a20ccf7e63c6f583300b9
- evidence_id: remediation
  kind: record_content
  reference: reports/sssom_generation_repair_20261031/followup-684-686/original-41-remediation.json
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: All 28 B5, eleven K and two G original diagnostics retain exact selectors
    and current outcomes.
  snapshot_sha256: 15646d0468a3bb985eb0f4510968c338f1fc764a3dcc75719e84289267df83bf
- evidence_id: inputs
  kind: record_content
  reference: reports/sssom_generation_repair_20261031/followup-684-686/validation-inputs.json
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: Exact current input revisions/hashes, including MIM records, aggregate/canonical/release
    inputs, KG unified mapping, comparison-only CM/Mediadive data and ontology DBs.
  snapshot_sha256: 9523ad34a1477521a95c1dd6216d80262a50d83fd56f68ad00d0983e49ae82ab
- evidence_id: generation
  kind: validation
  reference: reports/sssom_generation_repair_20261031/followup-684-686/generation-result.json
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: Committed generator head 9294730aeb19d269899177678db87406f4251555 and identical
    before/after source hashes bind this fresh native candidate.
  snapshot_sha256: 0b30ab393f7c4ea403d18f653142bbb40f2fb28a7f71e9014f4ab2ed4b1c0ac9
- evidence_id: date-contract
  kind: authority
  reference: reports/sssom_generation_repair_20261031/followup-684-686/date-contract.json
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: 'Explicit issue 686 decision: preserve blank dates for native Rule F in
    mixed sets; no clock fallback; reject all-dateless or malformed emitted dates
    before writing.'
  snapshot_sha256: 4b2ae778b2ad314cee47cf1b4bbaf4f7e4cd45da692125d857c1cd21a1e95cc4
- evidence_id: rule-f-proof
  kind: validation
  reference: reports/sssom_generation_repair_20261031/followup-684-686/rule-f-integration/receipt.json
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: Real native extraction/writer plus native validator proof, with exact synthetic
    row/reject hashes.
  snapshot_sha256: 19c412100d7cb54659808d6c1821476b80f0d4cf9c723937a8883f5d7af393bd
- evidence_id: independent-review
  kind: prior_review
  reference: reports/sssom_generation_repair_20261031/followup-684-686/adversarial-review-code.json
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: Independent adversarial review of exact 9294730 found no new defects, with
    scientific and rule-coverage limitations retained.
  snapshot_sha256: 7ac5d05e51eb2dcb329af74e5efab83c4e41edbd45f2886b50dc3502b15ab254
- evidence_id: preservation
  kind: validation
  reference: reports/sssom_generation_repair_20261031/followup-684-686/post-validation-preservation.json
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: Original repositories, current scientific inputs and all 87 pre-existing
    evidence files remain unchanged; separate live PR file overlap remains empty.
  snapshot_sha256: a199df86c51d669c6ff5b9214d23a838ab592eda0039cf7cf93347f0e4deacf9
- evidence_id: holds
  kind: prior_review
  reference: reports/sssom_generation_repair_20261031/followup-684-686/historical-rule-k-holds.json
  accessed_at: '2026-11-01T00:18:15Z'
  support: context_only
  summary: Eleven historical corresponding canonical rows remain WITHHOLD; mechanical
    fixes do not clear release holds.
  snapshot_sha256: a3ab2487192691c441a53cd6a33ba48bb3272dbec67fe8819ef5b15a8e575334
- evidence_id: semantics
  kind: authority
  reference: MAPPING_SEMANTICS.md
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: Identity/predicate/synonym contracts and per-row curator reject process.
  snapshot_sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
- evidence_id: pinned-release
  kind: prior_review
  reference: reports/sssom_completion_20260921/review.json
  accessed_at: '2026-11-01T00:18:15Z'
  support: context_only
  summary: Pinned scientific release input remains unchanged; not a new approval.
  snapshot_sha256: 6c74c7cc3eb8075ec18e20ab594a9b5eae9910b08b98c9d0746b3374af6c7ac6
- evidence_id: target-canonical
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: 'Exact inspected Unchanged maintained canonical mapping: 2,987 rows.'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: target-candidate
  kind: record_content
  reference: output/sssom-followup-684-686/ingredient_mappings.sssom.tsv
  accessed_at: '2026-11-01T00:18:15Z'
  support: supports
  summary: 'Exact inspected Final 9294730 diagnostic candidate: 2,980 rows; not promoted.'
  snapshot_sha256: 9fff31e31008a4aba70de846febe9f7de07770d84e86e4e7730c9acc69fffe31
assessments:
- assessment_id: canonical-preserved
  area: consistency
  topic: Canonical source remains unchanged and passes native QC
  outcome: supported
  target_ids:
  - canonical
  evidence_ids:
  - target-canonical
  - preservation
  - log-followup_full_qc
  - log-followup_baseline_reconcile
  - log-followup_baseline_products
  summary: Canonical remains 2,987 rows at its prior hash; MIM records, aggregates,
    unified mapping, release review and original source checkouts are preserved. Full
    native QC and source validators pass.
- assessment_id: candidate-current
  area: consistency
  topic: Final-head diagnostic candidate and exact delta
  outcome: supported
  target_ids:
  - candidate
  evidence_ids:
  - target-candidate
  - generation
  - comparison
  - previous-changes
  - remediation
  - log-followup_candidate_invariants
  - log-followup_candidate_products
  summary: Candidate contains 2,980 rows. Versus prior repaired output, 2,979 are
    identical; the stock B1 alias changes compound to ingredient namespace, object_source/comment
    follow that namespace, and its historical UNKNOWN_TERM stamp is not copied to
    a new triple. No date, header, predicate or other-token changes. All original
    41 diagnostics remain resolved and native drift is zero.
- assessment_id: date-diagnostics
  area: provenance
  topic: Issue 686 native date and curator-review contract
  outcome: supported
  target_ids:
  - candidate
  evidence_ids:
  - date-contract
  - rule-f-proof
  - log-followup_rule_f_integration
  - log-followup_focused_restored
  - independent-review
  summary: ASCII calendar-valid histories determine maximum row dates. Mixed dateless
    rows remain explicit blanks for native Rule F rejection; an all-dateless set or
    malformed nonempty emitted dates are reported completely before writing. This
    run has no date changes; synthetic native integration proves both missing-date
    rejects without altering real source data.
- assessment_id: code-validation
  area: consistency
  topic: Final generator checks and independent review
  outcome: supported
  target_ids:
  - candidate
  evidence_ids:
  - independent-review
  - log-followup_focused_restored
  - log-followup_lint
  - log-followup_mypy
  - log-followup_full_tests
  summary: Committed final generator passes focused tests, detected mutations, native
    lint/type checks, full CI-style suite and independent adversarial review. This
    assessment is mechanical and grants no scientific status.
- assessment_id: limits-preserved
  area: scope
  topic: Historical holds and incomplete adapter coverage retained
  outcome: supported
  target_ids:
  - canonical
  - candidate
  evidence_ids:
  - holds
  - pinned-release
  - log-followup_candidate_products
  - log-followup_baseline_products
  - log-followup_baseline_subjects
  - log-followup_candidate_b4_actual
  summary: Candidate is not promoted. Scientific WITHHOLD decisions and prior validation
    stamps remain historical. Baseline retains 101 label warnings, 5,314 no-adapter
    skips and 18 non-gating subject warnings; candidate retains 3,736 no-adapter skips.
    Actual-path B4 omits BTO/MICRO and absent IDs under native semantics.
findings:
- finding_id: F-B5
  issue_key: sssom-builder-dual-local-namespace
  category: identity
  severity: major
  status: resolved
  certainty: confirmed
  title: 'Resolved: Builder adds a second incompatible registry identity'
  description: Reconfirmed on the newly generated exact 9294730 candidate. All original
    affected candidate selectors are retained below; removed historical rows intentionally
    lack a current counterpart. The builder recognizes an already emitted registry
    identity in either permitted local namespace before synthesizing B1 backfill.
    All 14 maintained primary identities remain; the 14 competing generated identities
    disappear. Native B5 and the complete invariant suite pass. No YAML identifier
    was changed. Resolution is scoped to observed working-tree output, not a statement
    that its fixing PR is merged or that a scientific release hold is cleared.
  target_ids:
  - candidate
  field_paths:
  - rows[subject_id="MIM:84_GL_NaHCO3_Solution", object_id="kgmicrobe.ingredient:84_gl_nahco3_solution",
    predicate_id="skos:exactMatch"]
  - rows[subject_id="MIM:84_GL_NaHCO3_Solution", object_id="kgmicrobe.compound:84_gl_nahco3_solution",
    predicate_id="skos:exactMatch"]
  - rows[subject_id="MIM:Amylopectin_From_Maize", object_id="kgmicrobe.ingredient:amylopectin_from_maize",
    predicate_id="skos:exactMatch"]
  - rows[subject_id="MIM:Amylopectin_From_Maize", object_id="kgmicrobe.compound:amylopectin_from_maize",
    predicate_id="skos:exactMatch"]
  - rows[subject_id="MIM:B-Glucan_From_Oat", object_id="kgmicrobe.ingredient:b-glucan_from_oat",
    predicate_id="skos:exactMatch"]
  - rows[subject_id="MIM:B-Glucan_From_Oat", object_id="kgmicrobe.compound:b-glucan_from_oat",
    predicate_id="skos:exactMatch"]
  - rows[subject_id="MIM:Casamino_Acids_Vitamin_Assay", object_id="kgmicrobe.ingredient:casamino_acids_vitamin_assay",
    predicate_id="skos:exactMatch"]
  - rows[subject_id="MIM:Casamino_Acids_Vitamin_Assay", object_id="kgmicrobe.compound:casamino_acids_vitamin_assay",
    predicate_id="skos:exactMatch"]
  - rows[subject_id="MIM:Cholesterol_Lipid_Concentrate", object_id="kgmicrobe.ingredient:cholesterol_lipid_concentrate",
    predicate_id="skos:exactMatch"]
  - rows[subject_id="MIM:Cholesterol_Lipid_Concentrate", object_id="kgmicrobe.compound:cholesterol_lipid_concentrate",
    predicate_id="skos:exactMatch"]
  - rows[subject_id="MIM:Fish-sperm_Dna", object_id="kgmicrobe.ingredient:fish-sperm_dna",
    predicate_id="skos:exactMatch"]
  - rows[subject_id="MIM:Fish-sperm_Dna", object_id="kgmicrobe.compound:fish-sperm_dna",
    predicate_id="skos:exactMatch"]
  - rows[subject_id="MIM:Heparin_Sodium_Salt_From_Porcine_Intestinal_Mucosa", object_id="kgmicrobe.ingredient:heparin_sodium_salt_from_porcine_intestinal_mucosa",
    predicate_id="skos:exactMatch"]
  - rows[subject_id="MIM:Heparin_Sodium_Salt_From_Porcine_Intestinal_Mucosa", object_id="kgmicrobe.compound:heparin_sodium_salt_from_porcine_intestinal_mucosa",
    predicate_id="skos:exactMatch"]
  - rows[subject_id="MIM:Lichenan_Icelandic_Moss", object_id="kgmicrobe.ingredient:lichenan_icelandic_moss",
    predicate_id="skos:exactMatch"]
  - rows[subject_id="MIM:Lichenan_Icelandic_Moss", object_id="kgmicrobe.compound:lichenan_icelandic_moss",
    predicate_id="skos:exactMatch"]
  - rows[subject_id="MIM:MES_Buffer", object_id="kgmicrobe.ingredient:mes_buffer",
    predicate_id="skos:exactMatch"]
  - rows[subject_id="MIM:MES_Buffer", object_id="kgmicrobe.compound:mes_buffer", predicate_id="skos:exactMatch"]
  - rows[subject_id="MIM:MOPS_2M_pH7", object_id="kgmicrobe.ingredient:mops_2m_ph7",
    predicate_id="skos:exactMatch"]
  - rows[subject_id="MIM:MOPS_2M_pH7", object_id="kgmicrobe.compound:mops_2m_ph7",
    predicate_id="skos:exactMatch"]
  - rows[subject_id="MIM:Menadione_Solution", object_id="kgmicrobe.ingredient:menadione_solution",
    predicate_id="skos:exactMatch"]
  - rows[subject_id="MIM:Menadione_Solution", object_id="kgmicrobe.compound:menadione_solution",
    predicate_id="skos:exactMatch"]
  - rows[subject_id="MIM:PBS", object_id="kgmicrobe.ingredient:pbs", predicate_id="skos:exactMatch"]
  - rows[subject_id="MIM:PBS", object_id="kgmicrobe.compound:pbs", predicate_id="skos:exactMatch"]
  - rows[subject_id="MIM:PIPES_Buffer", object_id="kgmicrobe.ingredient:pipes_buffer",
    predicate_id="skos:exactMatch"]
  - rows[subject_id="MIM:PIPES_Buffer", object_id="kgmicrobe.compound:pipes_buffer",
    predicate_id="skos:exactMatch"]
  - rows[subject_id="MIM:Ribonucleic_Acid_From_Torula_Yeast_Type_VI", object_id="kgmicrobe.ingredient:ribonucleic_acid_from_torula_yeast_type_vi",
    predicate_id="skos:exactMatch"]
  - rows[subject_id="MIM:Ribonucleic_Acid_From_Torula_Yeast_Type_VI", object_id="kgmicrobe.compound:ribonucleic_acid_from_torula_yeast_type_vi",
    predicate_id="skos:exactMatch"]
  evidence_ids:
  - prior-review
  - remediation
  - comparison
  - log-followup_candidate_invariants
  - generation
  rule_id: B5
  native_severity: Native exit-2 invariant rejection; no numeric or P1-P4 severity
    assigned
  normalization_reason: Major because systemic generator behavior introduces contradictory
    local identity claims; native validator assigns rule IDs and an exit-2 rejection,
    not P1-P4 grades.
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/84_GL_NaHCO3_Solution.yaml
    role: Maintained owner for MIM:84_GL_NaHCO3_Solution; inspect identifier, ingredient_type,
      ontology_mapping and synonyms.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Paired maintained entry selector ingredients[identifier="kgmicrobe.ingredient:84_gl_nahco3_solution"];
      synchronize only after an authorized source correction.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Amylopectin_From_Maize.yaml
    role: Maintained owner for MIM:Amylopectin_From_Maize; inspect identifier, ingredient_type,
      ontology_mapping and synonyms.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Paired maintained entry selector ingredients[identifier="kgmicrobe.ingredient:amylopectin_from_maize"];
      synchronize only after an authorized source correction.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/B-Glucan_From_Oat.yaml
    role: Maintained owner for MIM:B-Glucan_From_Oat; inspect identifier, ingredient_type,
      ontology_mapping and synonyms.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Paired maintained entry selector ingredients[identifier="kgmicrobe.ingredient:b-glucan_from_oat"];
      synchronize only after an authorized source correction.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Casamino_Acids_Vitamin_Assay.yaml
    role: Maintained owner for MIM:Casamino_Acids_Vitamin_Assay; inspect identifier,
      ingredient_type, ontology_mapping and synonyms.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Paired maintained entry selector ingredients[identifier="kgmicrobe.ingredient:casamino_acids_vitamin_assay"];
      synchronize only after an authorized source correction.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cholesterol_Lipid_Concentrate.yaml
    role: Maintained owner for MIM:Cholesterol_Lipid_Concentrate; inspect identifier,
      ingredient_type, ontology_mapping and synonyms.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Paired maintained entry selector ingredients[identifier="kgmicrobe.ingredient:cholesterol_lipid_concentrate"];
      synchronize only after an authorized source correction.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fish-sperm_Dna.yaml
    role: Maintained owner for MIM:Fish-sperm_Dna; inspect identifier, ingredient_type,
      ontology_mapping and synonyms.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Paired maintained entry selector ingredients[identifier="kgmicrobe.ingredient:fish-sperm_dna"];
      synchronize only after an authorized source correction.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Heparin_Sodium_Salt_From_Porcine_Intestinal_Mucosa.yaml
    role: Maintained owner for MIM:Heparin_Sodium_Salt_From_Porcine_Intestinal_Mucosa;
      inspect identifier, ingredient_type, ontology_mapping and synonyms.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Paired maintained entry selector ingredients[identifier="kgmicrobe.ingredient:heparin_sodium_salt_from_porcine_intestinal_mucosa"];
      synchronize only after an authorized source correction.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Lichenan_Icelandic_Moss.yaml
    role: Maintained owner for MIM:Lichenan_Icelandic_Moss; inspect identifier, ingredient_type,
      ontology_mapping and synonyms.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Paired maintained entry selector ingredients[identifier="kgmicrobe.ingredient:lichenan_icelandic_moss"];
      synchronize only after an authorized source correction.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/MES_Buffer.yaml
    role: Maintained owner for MIM:MES_Buffer; inspect identifier, ingredient_type,
      ontology_mapping and synonyms.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Paired maintained entry selector ingredients[identifier="kgmicrobe.ingredient:mes_buffer"];
      synchronize only after an authorized source correction.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/MOPS_2M_pH7.yaml
    role: Maintained owner for MIM:MOPS_2M_pH7; inspect identifier, ingredient_type,
      ontology_mapping and synonyms.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Paired maintained entry selector ingredients[identifier="kgmicrobe.ingredient:mops_2m_ph7"];
      synchronize only after an authorized source correction.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Menadione_Solution.yaml
    role: Maintained owner for MIM:Menadione_Solution; inspect identifier, ingredient_type,
      ontology_mapping and synonyms.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Paired maintained entry selector ingredients[identifier="kgmicrobe.ingredient:menadione_solution"];
      synchronize only after an authorized source correction.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/PBS.yaml
    role: Maintained owner for MIM:PBS; inspect identifier, ingredient_type, ontology_mapping
      and synonyms.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Paired maintained entry selector ingredients[identifier="kgmicrobe.ingredient:pbs"];
      synchronize only after an authorized source correction.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/PIPES_Buffer.yaml
    role: Maintained owner for MIM:PIPES_Buffer; inspect identifier, ingredient_type,
      ontology_mapping and synonyms.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Paired maintained entry selector ingredients[identifier="kgmicrobe.ingredient:pipes_buffer"];
      synchronize only after an authorized source correction.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Ribonucleic_Acid_From_Torula_Yeast_Type_VI.yaml
    role: Maintained owner for MIM:Ribonucleic_Acid_From_Torula_Yeast_Type_VI; inspect
      identifier, ingredient_type, ontology_mapping and synonyms.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Paired maintained entry selector ingredients[identifier="kgmicrobe.ingredient:ribonucleic_acid_from_torula_yeast_type_vi"];
      synchronize only after an authorized source correction.
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_mim_ingredient_sssom.py
    role: 'External builder owner: registry and synonym emission'
  disposition_reason: The new candidate independently satisfies every original diagnostic
    disposition, with native invariants passing. The additional stock B1 alias intentionally
    changes namespace and receives no copied validation stamp; all maintained primary
    identities and parent predicates remain unchanged. Historical scientific holds
    are not cleared.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261031T233012Z-sssom-native-repair-mechanical
    finding_id: F-B5
  external_issues:
  - https://github.com/CultureBotAI/culturebotai-claw/issues/679
- finding_id: F-K
  issue_key: sssom-builder-cross-record-synonyms
  category: identity
  severity: major
  status: resolved
  certainty: confirmed
  title: 'Resolved: Candidate publishes synonyms owned by distinct records'
  description: Reconfirmed on the newly generated exact 9294730 candidate. All original
    affected candidate selectors are retained below; removed historical rows intentionally
    lack a current counterpart. External object aliases are inherited only for final
    exactMatch rows. All eleven originally rejected tokens are absent; seventeen target-only
    tokens are removed overall while curated subject aliases survive. Final predicates
    and registry identities are preserved. Native K and label checks pass. No synonym
    curation or scientific identity choice was applied. Resolution is scoped to observed
    working-tree output, not a statement that its fixing PR is merged or that a scientific
    release hold is cleared.
  target_ids:
  - candidate
  field_paths:
  - rows[subject_id="MIM:Cucl2_X_6_H2o", object_id="CHEBI:49553", predicate_id="skos:closeMatch"]
  - rows[subject_id="MIM:Disodium_Phosphate_Heptahydrate_002_M_Stock", object_id="CHEBI:34683",
    predicate_id="skos:closeMatch"]
  - rows[subject_id="MIM:Fecl2_X_6_H2o", object_id="CHEBI:30812", predicate_id="skos:closeMatch"]
  - rows[subject_id="MIM:Fecl2_X_7_H2o", object_id="CHEBI:30812", predicate_id="skos:closeMatch"]
  - rows[subject_id="MIM:Mgcl2_X_7_H2o", object_id="CHEBI:6636", predicate_id="skos:closeMatch"]
  - rows[subject_id="MIM:Na2hpo4_X_3_H2o", object_id="CHEBI:34683", predicate_id="skos:closeMatch"]
  - rows[subject_id="MIM:Na2hpo4_X_6_H2o", object_id="CHEBI:34683", predicate_id="skos:closeMatch"]
  - rows[subject_id="MIM:Na2hpo4_X_7_H2o", object_id="CHEBI:34683", predicate_id="skos:closeMatch"]
  - rows[subject_id="MIM:Natural_Sea_Water", object_id="ENVO:00002149", predicate_id="skos:closeMatch"]
  - rows[subject_id="MIM:Pasteurized_Seawater", object_id="ENVO:00002149", predicate_id="skos:closeMatch"]
  - rows[subject_id="MIM:Supplemented_Seawater", object_id="ENVO:00002149", predicate_id="skos:closeMatch"]
  evidence_ids:
  - prior-review
  - remediation
  - comparison
  - log-followup_candidate_invariants
  - generation
  rule_id: K
  native_severity: Native exit-2 invariant rejection; no numeric or P1-P4 severity
    assigned
  normalization_reason: Major because cross-record synonym publication may create
    identity conflation; the native gate rejects Rule K without a P1-P4 grade.
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cucl2_X_6_H2o.yaml
    role: Maintained owner for MIM:Cucl2_X_6_H2o; inspect identifier, ingredient_type,
      ontology_mapping and synonyms.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Paired maintained entry selector ingredients[identifier="kgmicrobe.compound:cucl2_x_6_h2o"];
      synchronize only after an authorized source correction.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Disodium_Phosphate_Heptahydrate_002_M_Stock.yaml
    role: Maintained owner for MIM:Disodium_Phosphate_Heptahydrate_002_M_Stock; inspect
      identifier, ingredient_type, ontology_mapping and synonyms.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Paired maintained entry selector ingredients[identifier="kgmicrobe.ingredient:disodium_phosphate_heptahydrate_~28002_m_stock~29"];
      synchronize only after an authorized source correction.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fecl2_X_6_H2o.yaml
    role: Maintained owner for MIM:Fecl2_X_6_H2o; inspect identifier, ingredient_type,
      ontology_mapping and synonyms.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Paired maintained entry selector ingredients[identifier="kgmicrobe.compound:fecl2_x_6_h2o"];
      synchronize only after an authorized source correction.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fecl2_X_7_H2o.yaml
    role: Maintained owner for MIM:Fecl2_X_7_H2o; inspect identifier, ingredient_type,
      ontology_mapping and synonyms.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Paired maintained entry selector ingredients[identifier="kgmicrobe.compound:fecl2_x_7_h2o"];
      synchronize only after an authorized source correction.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Mgcl2_X_7_H2o.yaml
    role: Maintained owner for MIM:Mgcl2_X_7_H2o; inspect identifier, ingredient_type,
      ontology_mapping and synonyms.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Paired maintained entry selector ingredients[identifier="kgmicrobe.compound:mgcl2_x_7_h2o"];
      synchronize only after an authorized source correction.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2hpo4_X_3_H2o.yaml
    role: Maintained owner for MIM:Na2hpo4_X_3_H2o; inspect identifier, ingredient_type,
      ontology_mapping and synonyms.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Paired maintained entry selector ingredients[identifier="kgmicrobe.compound:na2hpo4_x_3_h2o"];
      synchronize only after an authorized source correction.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2hpo4_X_6_H2o.yaml
    role: Maintained owner for MIM:Na2hpo4_X_6_H2o; inspect identifier, ingredient_type,
      ontology_mapping and synonyms.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Paired maintained entry selector ingredients[identifier="kgmicrobe.compound:na2hpo4_x_6_h2o"];
      synchronize only after an authorized source correction.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
    role: Maintained owner for MIM:Na2hpo4_X_7_H2o; inspect identifier, ingredient_type,
      ontology_mapping and synonyms.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Paired maintained entry selector ingredients[identifier="kgmicrobe.compound:na2hpo4_x_7_h2o"];
      synchronize only after an authorized source correction.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Natural_Sea_Water.yaml
    role: Maintained owner for MIM:Natural_Sea_Water; inspect identifier, ingredient_type,
      ontology_mapping and synonyms.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Paired maintained entry selector ingredients[identifier="kgmicrobe.ingredient:natural_sea_water"];
      synchronize only after an authorized source correction.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Pasteurized_Seawater.yaml
    role: Maintained owner for MIM:Pasteurized_Seawater; inspect identifier, ingredient_type,
      ontology_mapping and synonyms.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Paired maintained entry selector ingredients[identifier="kgmicrobe.ingredient:pasteurized_seawater"];
      synchronize only after an authorized source correction.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Supplemented_Seawater.yaml
    role: Maintained owner for MIM:Supplemented_Seawater; inspect identifier, ingredient_type,
      ontology_mapping and synonyms.
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Paired maintained entry selector ingredients[identifier="kgmicrobe.ingredient:supplemented_seawater"];
      synchronize only after an authorized source correction.
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_mim_ingredient_sssom.py
    role: 'External builder owner: registry and synonym emission'
  disposition_reason: The new candidate independently satisfies every original diagnostic
    disposition, with native invariants passing. The additional stock B1 alias intentionally
    changes namespace and receives no copied validation stamp; all maintained primary
    identities and parent predicates remain unchanged. Historical scientific holds
    are not cleared.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261031T233012Z-sssom-native-repair-mechanical
    finding_id: F-K
  external_issues:
  - https://github.com/CultureBotAI/culturebotai-claw/issues/680
- finding_id: F-G
  issue_key: sssom-builder-header-date-policy
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: 'Resolved: Generated header dates disagree with newest row date'
  description: Reconfirmed on the newly generated exact 9294730 candidate. All original
    affected candidate selectors are retained below; removed historical rows intentionally
    lack a current counterpart. Both header dates now equal 2026-10-15, the newest
    emitted row date. Native G passes; source row dates were not rewritten to manufacture
    agreement. Resolution is scoped to observed working-tree output, not a statement
    that its fixing PR is merged or that a scientific release hold is cleared.
  target_ids:
  - candidate
  field_paths:
  - header.mapping_date
  - header.mapping_set_version
  evidence_ids:
  - prior-review
  - remediation
  - comparison
  - log-followup_candidate_invariants
  - generation
  rule_id: G
  native_severity: Native exit-2 invariant rejection; no numeric or P1-P4 severity
    assigned
  normalization_reason: Minor because bounded provenance/version metadata is inconsistent
    while identity rows are unchanged by this defect; native Rule G still blocks promotion
    and is not waived.
  owner_paths:
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_mim_ingredient_sssom.py
    role: 'External builder owner: header/version emission'
  disposition_reason: The new candidate independently satisfies every original diagnostic
    disposition, with native invariants passing. The additional stock B1 alias intentionally
    changes namespace and receives no copied validation stamp; all maintained primary
    identities and parent predicates remain unchanged. Historical scientific holds
    are not cleared.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261031T233012Z-sssom-native-repair-mechanical
    finding_id: F-G
  external_issues:
  - https://github.com/CultureBotAI/culturebotai-claw/issues/681
actions: []
limitations:
- Mechanical verification does not approve identities, relation scope, historical
  validation stamps or scientific release claims. Candidate is not promoted.
- CultureMech ingredient outputs and KG Mediadive nodes are comparison-only inputs;
  raw generation consumes maintained MIM records, copied residual classifications
  and actual KG unified mappings plus ontology labels. No bulk import.
- Actual-path B4 retains native absent-ID skips and missing BTO/MICRO transforms.
  Configured label no-adapter skips, 101 baseline warnings and 18 subject warnings
  remain.
- Generated full candidates and large inputs remain local diagnostic artifacts. Saved
  working-tree hashes attest inspected bytes and do not claim full outputs are committed.
- Canonical-versus-candidate differences are broader than this follow-up. This is
  not an approved replacement for canonical or the supported/withheld partition.
- Native B5 groups by subject and slug, not subject alone; targeted regression tests
  and exact delta review cover the different-slug namespace defect without silently
  redefining the downstream validator.
- The first comparison helper run failed an overstrict stamp assertion; an intermediate
  summary reused a loop variable. Both setup receipts are retained; final comparison
  explicitly verifies the alias and blank stamp, with all native validators unaffected.
related_reviews:
- repository: CultureBotAI/MediaIngredientMech
  review_id: 20261031T233012Z-sssom-native-repair-mechanical
  relationship: Reconfirms the same three original finding keys on a newly generated
    final-head candidate; prior review bytes remain immutable.
links:
- https://github.com/CultureBotAI/culturebotai-claw/issues/679
- https://github.com/CultureBotAI/culturebotai-claw/issues/680
- https://github.com/CultureBotAI/culturebotai-claw/issues/681
- https://github.com/CultureBotAI/culturebotai-claw/issues/682
- https://github.com/CultureBotAI/culturebotai-claw/issues/683
- https://github.com/CultureBotAI/culturebotai-claw/issues/684
- https://github.com/CultureBotAI/culturebotai-claw/issues/685
- https://github.com/CultureBotAI/culturebotai-claw/issues/686
tags:
- sssom
- mechanical-review
- append-only-evidence
- historical-holds-preserved
```
