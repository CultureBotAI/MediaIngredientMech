# SSSOM native invariant repair: mechanical resolution with historical holds preserved

- Review: 20261031T233012Z-sssom-native-repair-mechanical
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-31T23:29:19Z
- Finished UTC: 2026-10-31T23:30:12Z
- Reviewer: Codex validation agent /root/sssom_validation (not_applicable)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Bounded mechanical review of unchanged canonical SSSOM (2,987 rows) and final-code diagnostic candidate (2,980 rows). The predecessor's three findings resolve through exact evidence for all 41 native rejections. Native invariant/schema/CURIE/label and reconciliation checks pass. Candidate is not promoted; reviewed-release decisions and scientific holds remain unchanged.

## Scope And Provenance

Exact current canonical and final-code diagnostic candidate snapshots; successor disposition limited to predecessor B5, K and G findings.

Selection: Two declared artifacts, all rows checked by their applicable native deterministic gates; artifact count is the scope denominator and row/diagnostic denominators are separate.
Coverage: full; 2 reviewed / 2 in the declared population.
Source: working_tree at Git base e6156a57ba5dda74a14de7987d8f83c1c7713c1c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| canonical | mappings/ingredient_mappings.sssom.tsv | generated | Unchanged maintained canonical mapping: 2,987 rows |
| candidate | output/sssom-repair/final-code-replay.sssom.tsv | generated | Final-code diagnostic candidate: 2,980 rows; not promoted |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| regenerated candidate | passed | True | candidate | Supported native builder generated 2,980 diagnostic rows with code loaded before removal of an unused timezone import. Loaded/final code hashes are distinguished by final-code replay evidence. |
| final code replay retry | passed | True | candidate | Final code reproduces byte-identical 2,980-row output using captured emitted-object label values. No new label lookup/provider calls. Forty-eight requested CHEBI IDs absent from emitted rows are explicitly listed in the replay receipt. |
| candidate invariants retry | passed | True | candidate | Native strict invariants pass A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K and L; reject output contains header only. B4 actual-path supplement is separate. |
| candidate schema | passed | True | candidate | SSSOM JSON Schema, PrefixMapCompleteness and StrictCurieFormat pass. Native extension-field notices remain in the log. |
| candidate curie | passed | True | candidate | 2,980 rows and 5,960 CURIEs pass native syntax and known-prefix checks. |
| candidate products | passed | True | candidate | Native candidate label policy passes: 2,216 canonical, four synonyms, four configured exceptions and 3,736 no-adapter skips. Only target selection/path changed from native configuration. |
| compare candidates retry | passed | True | canonical, candidate | All 41 original diagnostics reconciled. Relative to old candidate: 14 surplus registry rows removed and 17 other fields changed, only by removing 17 inherited object aliases; no added rows, remaining-row predicate changes or curated-subject synonym removals. Native find_drift reports all five categories zero. |
| full qc | passed | True | canonical | Repository composite just qc passes on unchanged maintained MIM sources; this does not certify scientific truth or promote the candidate. |
| baseline curie | passed | True | canonical | Canonical 2,987 rows/5,974 CURIEs pass; 20 tests pass, one skips. |
| baseline reconcile | passed | True | canonical | Canonical GAP, ORPHAN, STALE, PREDICATE and GRADE counts are all zero. |
| baseline products | passed | True | canonical | Configured full product validation passes with 101 nonblocking warnings and 5,314 no-adapter skips; retained for transparency. |
| baseline subjects | passed | False | canonical | Native checker reports 18 non-gating opaque-slug/filename mismatches among 2,611 subjects; no new gate imposed. |
| candidate b4 actual | passed | False | candidate | Unmodified native B4 using actual read-only KG transform directory reports zero findings for repaired bytes; BTO/MICRO transforms absent and native absent-ID skips retained. |
| baseline b4 actual | passed | False | canonical | Unmodified native B4 against actual read-only KG transforms reports zero findings for canonical source, with the same BTO/MICRO coverage limits. |
| focused final | passed | True | candidate | All 64 focused builder regression tests pass on final source; this is code behavior evidence, not scientific review. |
| candidate invariants | failed | False | candidate | Initial invocation used unsupported --sssom-path; argument parsing failed before validation. Correct positional invocation subsequently passed. |
| compare candidates | failed | False | candidate | Diagnostic comparison helper initially passed mapping values to Counter.update; failed before its assertions/output. Corrected helper subsequently completed all assertions. |
| final code replay | failed | False | candidate | Replay preparation initially included non-lookup registry labels with multiple subject labels; it stopped before generation. Replay then restricted capture to actual lookup prefixes and produced byte-identical output. |

## Scientific And Domain Assessments

### Unchanged maintained source remains mechanically valid

consistency: supported. Targets: canonical.

The canonical mapping remains 2,987 rows with its original SHA-256. MIM records, aggregates, unified mapping and pinned review remain unchanged. Native full QC and scoped source validators pass.

### All predecessor mechanical defects resolved without scientific reassignment

consistency: supported. Targets: candidate.

The final-code candidate contains 2,980 rows and zero native invariant rejects. All 41 prior B5/K/G diagnostics have explicit evidence-linked outcomes. Against the old candidate, only fourteen surplus registry rows, seventeen inherited other aliases and two header dates change.

### Loaded and final generator identities distinguished

provenance: supported. Targets: candidate.

Generation began with the repaired code before a later unused-import cleanup. The final source reproduces exactly the same mapping bytes using captured emitted-label values and native generation/stamp behavior. This replay is not a fresh ontology lookup or scientific review.

### Native warning, skip and release boundaries retained

scope: supported. Targets: canonical, candidate.

Scoped mechanical gates pass with documented native limits: 101 nonblocking full-product warnings; 5,314 baseline and 3,736 candidate no-adapter skips; 18 non-gating subject warnings; BTO/MICRO transform skips. Historical scientific WITHHOLD decisions and prior validation stamps remain historical; no candidate promotion occurred.

## Findings

### F-B5: Resolved: Builder adds a second incompatible registry identity

major / resolved / confirmed; issue key: sssom-builder-dual-local-namespace.

The prior mechanical defect is resolved in this exact final-code diagnostic candidate. The builder recognizes an already emitted registry identity in either permitted local namespace before synthesizing B1 backfill. All 14 maintained primary identities remain; the 14 competing generated identities disappear. Native B5 and the complete invariant suite pass. No YAML identifier was changed. Original selectors below identify the earlier observed rows/headers; removed rows intentionally have no current counterpart.

Disposition: The builder recognizes an already emitted registry identity in either permitted local namespace before synthesizing B1 backfill. All 14 maintained primary identities remain; the 14 competing generated identities disappear. Native B5 and the complete invariant suite pass. No YAML identifier was changed. Resolution is scoped to observed working-tree output, not a statement that its fixing PR is merged or that a scientific release hold is cleared.

### F-K: Resolved: Candidate publishes synonyms owned by distinct records

major / resolved / confirmed; issue key: sssom-builder-cross-record-synonyms.

The prior mechanical defect is resolved in this exact final-code diagnostic candidate. External object aliases are inherited only for final exactMatch rows. All eleven originally rejected tokens are absent; seventeen target-only tokens are removed overall while curated subject aliases survive. Final predicates and registry identities are preserved. Native K and label checks pass. No synonym curation or scientific identity choice was applied. Original selectors below identify the earlier observed rows/headers; removed rows intentionally have no current counterpart.

Disposition: External object aliases are inherited only for final exactMatch rows. All eleven originally rejected tokens are absent; seventeen target-only tokens are removed overall while curated subject aliases survive. Final predicates and registry identities are preserved. Native K and label checks pass. No synonym curation or scientific identity choice was applied. Resolution is scoped to observed working-tree output, not a statement that its fixing PR is merged or that a scientific release hold is cleared.

### F-G: Resolved: Generated header dates disagree with newest row date

minor / resolved / confirmed; issue key: sssom-builder-header-date-policy.

The prior mechanical defect is resolved in this exact final-code diagnostic candidate. Both header dates now equal 2026-10-15, the newest emitted row date. Native G passes; source row dates were not rewritten to manufacture agreement. Original selectors below identify the earlier observed rows/headers; removed rows intentionally have no current counterpart.

Disposition: Both header dates now equal 2026-10-15, the newest emitted row date. Native G passes; source row dates were not rewritten to manufacture agreement. Resolution is scoped to observed working-tree output, not a statement that its fixing PR is merged or that a scientific release hold is cleared.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| log-regenerated_candidate | reports/sssom_generation_repair_20261031/logs/regenerated_candidate.log | supports | Supported native builder generated 2,980 diagnostic rows with code loaded before removal of an unused timezone import. Loaded/final code hashes are distinguished by final-code replay evidence. |
| log-final_code_replay_retry | reports/sssom_generation_repair_20261031/logs/final_code_replay_retry.log | supports | Final code reproduces byte-identical 2,980-row output using captured emitted-object label values. No new label lookup/provider calls. Forty-eight requested CHEBI IDs absent from emitted rows are explicitly listed in the replay receipt. |
| log-candidate_invariants_retry | reports/sssom_generation_repair_20261031/logs/candidate_invariants_retry.log | supports | Native strict invariants pass A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K and L; reject output contains header only. B4 actual-path supplement is separate. |
| log-candidate_schema | reports/sssom_generation_repair_20261031/logs/candidate_schema.log | supports | SSSOM JSON Schema, PrefixMapCompleteness and StrictCurieFormat pass. Native extension-field notices remain in the log. |
| log-candidate_curie | reports/sssom_generation_repair_20261031/logs/candidate_curie.log | supports | 2,980 rows and 5,960 CURIEs pass native syntax and known-prefix checks. |
| log-candidate_products | reports/sssom_generation_repair_20261031/logs/candidate_products.log | supports | Native candidate label policy passes: 2,216 canonical, four synonyms, four configured exceptions and 3,736 no-adapter skips. Only target selection/path changed from native configuration. |
| log-compare_candidates_retry | reports/sssom_generation_repair_20261031/logs/compare_candidates_retry.log | supports | All 41 original diagnostics reconciled. Relative to old candidate: 14 surplus registry rows removed and 17 other fields changed, only by removing 17 inherited object aliases; no added rows, remaining-row predicate changes or curated-subject synonym removals. Native find_drift reports all five categories zero. |
| log-full_qc | reports/sssom_generation_repair_20261031/logs/full_qc.log | supports | Repository composite just qc passes on unchanged maintained MIM sources; this does not certify scientific truth or promote the candidate. |
| log-baseline_curie | reports/sssom_generation_repair_20261031/logs/baseline_curie.log | supports | Canonical 2,987 rows/5,974 CURIEs pass; 20 tests pass, one skips. |
| log-baseline_reconcile | reports/sssom_generation_repair_20261031/logs/baseline_reconcile.log | supports | Canonical GAP, ORPHAN, STALE, PREDICATE and GRADE counts are all zero. |
| log-baseline_products | reports/sssom_generation_repair_20261031/logs/baseline_products.log | supports | Configured full product validation passes with 101 nonblocking warnings and 5,314 no-adapter skips; retained for transparency. |
| log-baseline_subjects | reports/sssom_generation_repair_20261031/logs/baseline_subjects.log | supports | Native checker reports 18 non-gating opaque-slug/filename mismatches among 2,611 subjects; no new gate imposed. |
| log-candidate_b4_actual | reports/sssom_generation_repair_20261031/logs/candidate_b4_actual.log | supports | Unmodified native B4 using actual read-only KG transform directory reports zero findings for repaired bytes; BTO/MICRO transforms absent and native absent-ID skips retained. |
| log-baseline_b4_actual | reports/sssom_generation_repair_20261031/logs/baseline_b4_actual.log | supports | Unmodified native B4 against actual read-only KG transforms reports zero findings for canonical source, with the same BTO/MICRO coverage limits. |
| log-focused_final | reports/sssom_generation_repair_20261031/logs/focused_final.log | supports | All 64 focused builder regression tests pass on final source; this is code behavior evidence, not scientific review. |
| log-candidate_invariants | reports/sssom_generation_repair_20261031/logs/candidate_invariants.log | context_only | Initial invocation used unsupported --sssom-path; argument parsing failed before validation. Correct positional invocation subsequently passed. |
| log-compare_candidates | reports/sssom_generation_repair_20261031/logs/compare_candidates.log | context_only | Diagnostic comparison helper initially passed mapping values to Counter.update; failed before its assertions/output. Corrected helper subsequently completed all assertions. |
| log-final_code_replay | reports/sssom_generation_repair_20261031/logs/final_code_replay.log | context_only | Replay preparation initially included non-lookup registry labels with multiple subject labels; it stopped before generation. Replay then restricted capture to actual lookup prefixes and produced byte-identical output. |
| prior-review | reviews/structured/20261031T214143Z-sssom-current-inputs-mechanical/review.yaml | context_only | Exact predecessor observation copied byte-for-byte; only its three candidate mechanical findings are reconciled here. |
| semantics | MAPPING_SEMANTICS.md | supports | Identity, registry namespace, predicate and synonym contracts remain authoritative. No scientific claim is inferred from passing diagnostics. |
| comparison | reports/sssom_generation_repair_20261031/candidate-comparison.json | supports | Separate comparisons against old raw candidate and unchanged maintained canonical mapping, including counts, exact changed fields and native drift results. |
| remediation | reports/sssom_generation_repair_20261031/original-41-remediation.json | supports | Every original B5/K/G diagnostic retains exact selector/reason and explicit current disposition. Fourteen maintained primary identity rows survive; fourteen extra identities are removed; eleven K tokens disappear; two headers match newest row date. |
| other-changes | reports/sssom_generation_repair_20261031/other-field-changes.json | supports | Exact 17 changed row triples with before/after other payloads; 17 removed tokens and no added tokens. No removed token is a publishable curated subject synonym. |
| inputs | reports/sssom_generation_repair_20261031/validation-inputs.json | supports | Current SHA-256 provenance for 2,985 files including every MIM record, maintained aggregates, canonical/review pins, copied residual, actual KG mapping/Medidive inputs and ontology DBs. Repository revisions and working-tree diff hashes distinguish local code changes. |
| generator-revisions | reports/sssom_generation_repair_20261031/generator-revisions.json | supports | Original generator-loaded hash and final source hash differ only by unused timezone import removal; exact reconstruction verifies this distinction. |
| final-code-replay | reports/sssom_generation_repair_20261031/final-code-replay.json | supports | Final-code output hash equals the independently validated regenerated output hash. Captured values are emitted object labels, not a complete archive of original lookup responses. |
| candidate-config | reports/sssom_generation_repair_20261031/candidate-id-label-config.json | supports | All native label policy/adapters/exceptions unchanged; only targets narrowed to sssom and glob redirected. |
| b4-inputs | reports/sssom_generation_repair_20261031/candidate-b4-actual.json | supports | Exact available ontology transform hashes and BTO/MICRO missing-prefix limits; no fake paths or labels. |
| historical-holds | reports/sssom_generation_repair_20261031/historical-rule-k-holds.json | context_only | All eleven corresponding canonical non-exact rows remain WITHHOLD in the pinned release. Mechanical repairs neither approve their relation/synonym scope nor change identity. |
| pinned-review | reports/sssom_completion_20260921/review.json | context_only | Historical content-bound scientific release decisions remain unchanged; this review is not a successor release ledger. |
| mutations | reports/sssom_generation_repair_20261031/mutation-results.json | supports | Each B5/K/G code reversion was detected by focused tests. Raw expected-failure receipts remain diagnostic evidence, not a failing final gate. |
| target-canonical | mappings/ingredient_mappings.sssom.tsv | supports | Exact inspected Unchanged maintained canonical mapping: 2,987 rows. |
| target-candidate | output/sssom-repair/final-code-replay.sssom.tsv | supports | Exact inspected Final-code diagnostic candidate: 2,980 rows; not promoted. |

## Limits And Additional Notes

- Mechanical resolution is confined to the exact inspected candidate, not to merged/published state or scientific approval.
- Historical WITHHOLD decisions, unresolved nonexact relation/synonym-scope obligations and prior validation_method stamps are not approved, recalibrated or migrated.
- Native B4 remains best-effort with missing BTO/MICRO transform files and absent-ID skips. Missing-file checks include ignored files at the exact actual KG transform directory.
- Configured no-adapter label skips, 101 nonblocking baseline warnings and 18 opaque-slug warnings remain; passing enforcement is not complete scientific coverage.
- Final-code replay uses labels captured from emitted rows, not full original lookup responses. Forty-eight requested CHEBI IDs absent from output are listed; exact output equality was verified and replay made no network/provider calls.
- Candidate differs substantially from maintained canonical source beyond this bounded repair; separate canonical comparison is retained. It must not be treated as a drop-in approved release.
- Generated full mappings and large ontology/source inputs remain diagnostic/local. Copied tracked reports retain exact hashes, commands, before/after selectors and results; working-tree attestations do not claim those full inputs were committed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261031T233012Z-sssom-native-repair-mechanical
kind: repository
repository: CultureBotAI/MediaIngredientMech
title: 'SSSOM native invariant repair: mechanical resolution with historical holds
  preserved'
started_at: '2026-10-31T23:29:19Z'
finished_at: '2026-10-31T23:30:12Z'
reviewer:
  identity: Codex validation agent /root/sssom_validation
  kind: agent
  independence: not_applicable
  independence_basis: Separate validation task from parent generator implementation;
    this agent authored K regression tests. No claim of independent scientific review
    or PR approval.
skill: .claude/skills/review-sssom-output/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: All three prior mechanical findings resolved on diagnostic output;
  native scientific holds unchanged
scientific_review: false
summary: Bounded mechanical review of unchanged canonical SSSOM (2,987 rows) and final-code
  diagnostic candidate (2,980 rows). The predecessor's three findings resolve through
  exact evidence for all 41 native rejections. Native invariant/schema/CURIE/label
  and reconciliation checks pass. Candidate is not promoted; reviewed-release decisions
  and scientific holds remain unchanged.
source:
  git_revision: e6156a57ba5dda74a14de7987d8f83c1c7713c1c
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
  - path: output/sssom-repair/final-code-replay.sssom.tsv
    sha256: 04159ba36b221d1c8ebf6e281972c846a333cf4fe5e868b06bb5326f2b02e3a7
    role: target
  - path: output/sssom-repair/ingredient_mappings.sssom.tsv
    sha256: 04159ba36b221d1c8ebf6e281972c846a333cf4fe5e868b06bb5326f2b02e3a7
    role: context
  - path: output/sssom-repair/rejected-rows-current.tsv
    sha256: e638bc52978e8503320e3386814dcdb5bc6b1c1c72e96487ba327ea58701f127
    role: context
  - path: reports/sssom_completion_20260921/review.json
    sha256: 6c74c7cc3eb8075ec18e20ab594a9b5eae9910b08b98c9d0746b3374af6c7ac6
    role: context
  - path: reports/sssom_generation_repair_20261031/baseline-b4-actual.json
    sha256: 069e9680a63af1b26c97cf905ad26300e1d5b80f6fe6ff2841a4681dab9dff5e
    role: context
  - path: reports/sssom_generation_repair_20261031/candidate-b4-actual.json
    sha256: 3ffb788739125200983ae47963f0a7ccbb27d188103ed526f61a7a704a86bf31
    role: context
  - path: reports/sssom_generation_repair_20261031/candidate-comparison.json
    sha256: 81b343763b935350f12c356330e4ff1e9b3542d0e04520312c952d87123dca71
    role: context
  - path: reports/sssom_generation_repair_20261031/candidate-id-label-config.json
    sha256: 1fa9c2494e9b5c5966d14b030030f88dddea0c9c7f4a2228ba5f528a23a601a7
    role: context
  - path: reports/sssom_generation_repair_20261031/candidate-id-label-config.yaml
    sha256: 3ad00967d0db507225965a27641093a743d264d84d0395fb23e26e903c50ca98
    role: context
  - path: reports/sssom_generation_repair_20261031/candidate-native-drift.json
    sha256: 2429604ab6b30758b72696906bcc2a341cacb8d1a01a9047409cb360a82fd4d1
    role: context
  - path: reports/sssom_generation_repair_20261031/final-code-replay.json
    sha256: 4a7e0f07358175f1bc50ed55db98a255fc17063a4b9f956edfe7faafbc741946
    role: context
  - path: reports/sssom_generation_repair_20261031/generator-revisions.json
    sha256: 04293c14ed9b202fbc59b5f58023eb83007fce179d614ba72d1b0d6c037f6111
    role: context
  - path: reports/sssom_generation_repair_20261031/historical-rule-k-holds.json
    sha256: a3ab2487192691c441a53cd6a33ba48bb3272dbec67fe8819ef5b15a8e575334
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/baseline_b4_actual.json
    sha256: bc64e836a4e28dd39bddbc19d4770b9e91de75ad20e61b8f97660edbdd4181f3
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/baseline_b4_actual.log
    sha256: 181adf3eb5d1c4d4fcf30ddd35ce808edb8ec7a0278ea341916f22c51dd07360
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/baseline_curie.json
    sha256: a08b222a812e34315d67d163d844aeb3fb9756d95c431854abd4656637c2181f
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/baseline_curie.log
    sha256: e9845a5693dde19e1fb1bf6da791d6ad6c620ce1458815fb998dc62a3c4e511b
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/baseline_products.json
    sha256: 27ead6974b697d1d8e233c6184c0941ebd9b6b9837866bffaa3aa23ebc6bb1a3
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/baseline_products.log
    sha256: 1fa143fbbbdb204cfca441d722014ca3b2ab5eda915eb2f6de1b7dc997e1d335
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/baseline_reconcile.json
    sha256: 5d67e617c9abf74a740d88b787f238cebb956c047f5e58950c77fd3ee1ca6c5f
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/baseline_reconcile.log
    sha256: 8bf18010d973e92de327bf8580964cbe3306206d7191c45a7b1731df9c7d61d7
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/baseline_subjects.json
    sha256: 1694f4e8397b402dc7e443c453a27ae931b89b12c7a5a3ee512a9ea6ab999a3e
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/baseline_subjects.log
    sha256: a16772841d62c8f1f9be43c85a24d0e9c1e687b6ec493652fd2c5be113da7762
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/candidate_b4_actual.json
    sha256: 3cedb7f86323b0ed2e07e6eca848578ffadf72671eecc427da8ae6a873324e31
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/candidate_b4_actual.log
    sha256: 8e1e50ddfdeaef5dc6fafeb76974f6a559db5141bf846b6f6d0d9dbc3ba0739e
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/candidate_curie.json
    sha256: fd028ea8f544843af0d64b74fbde7f39d4705bb45afac0e0dd266ef2a45815dd
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/candidate_curie.log
    sha256: 31ca9b6d8a11e0181035e649476ee2a2c01b4b1cc04d7df1c6f0ebb182fab99e
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/candidate_invariants.json
    sha256: e3218cd2472bc2b397f1e420e19f65414f486e1f900a3855adc4dcda1d5a0b5b
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/candidate_invariants.log
    sha256: 789bc919eadbf502f0b64b73779eecdb3d853a1482c03c7b6d5ff9960a5cc5f6
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/candidate_invariants_retry.json
    sha256: 3f01370fa4ba53b86750972f80bcb47968da384ee9c976791353b9cad2fc38f2
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/candidate_invariants_retry.log
    sha256: bfd845c17cfe56ef91d33d46a3374aff05b0705d8e0445d5e4a8161244ac44ce
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/candidate_products.json
    sha256: 6279e68140a305fad76b2d0ceb081eabfa0de90c450e8f6dd446cd8bf8237607
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/candidate_products.log
    sha256: b0695b05145765cb47f8ce259be004e003f012c9fdc69ecc502c598d22a8f38d
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/candidate_schema.json
    sha256: 8d5e72ef41194a99553d1d18f5539c30df78e7a686bd0b95202331f0968e4824
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/candidate_schema.log
    sha256: 6bb3a5fb4906f5382c09aa0eb0a8e6dbe45d2fe31c6dd726e030e30461fa4c2c
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/compare_candidates.json
    sha256: 1bbfb718b68ea69619aaed1862f8afdca42f6c6635a45b9549547b8a788bf729
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/compare_candidates.log
    sha256: c7914e3306b18554122d905ccd99f9ff84685d56f0fb538412bb779d9c5955d1
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/compare_candidates_retry.json
    sha256: 30a8f0ed13af4d5f05dc272dbaa638f42c2ac8379e4c783f2d670b6b11d7e044
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/compare_candidates_retry.log
    sha256: 81b343763b935350f12c356330e4ff1e9b3542d0e04520312c952d87123dca71
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/final_code_replay.json
    sha256: c7d5d9dbb4438a7f20a99261f9e8fe75265dccca5c48cbe381a13283f9411ec2
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/final_code_replay.log
    sha256: c22a8e76515603ae72ece1f0870c5ec3c3371a043e8ed19d0504d49be05a55a8
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/final_code_replay_retry.json
    sha256: 8bb8e2f38f1af6cd76ab1b5cb9cff09ce9830ed50df73ef22d739890fa698114
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/final_code_replay_retry.log
    sha256: 7d18299bf2def43986d31329e236bc089d7b54f794f25da034a2aba4f5ad0935
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/focused_final.json
    sha256: 5b9d178826b61af16c226c87c38d80b72ffc2bc79d407292f9dc81d8be75e310
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/focused_final.log
    sha256: 8a0f611592f19c13c80f67616b2006a8c83056d068810e1fb48bdac8a86eecc3
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/full_qc.json
    sha256: 6a5f4fa828a777ec6d9d24aacb3e04d9a37ae61c575b8edf000a5d3238944f1d
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/full_qc.log
    sha256: cb2e3db3661f7131926f0ddb0ff0bcb4c6bad81dcb5b874473c67bab4077e39d
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/mutation_b5.json
    sha256: acdb30c446027adc2800562b926d334de30e4bf34b5e9e8cb796e5b557ea106f
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/mutation_b5.log
    sha256: 2639b613a9ff20b2cb3dd54f0c710aeb53632786135c27c875a35af953185d31
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/mutation_g.json
    sha256: 6fc3cc414ee9d5f4bbadb4fb083ba6cfed224377553dd407c139d86cf346774b
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/mutation_g.log
    sha256: 1f0b7371bc695742c5394e164d1f2382abca453e73744e4859c0616dcd0db1c2
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/mutation_k.json
    sha256: 0556eb6f71f58c3dd3376f49617d5537691af5191bd390831a2c73ce4a962397
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/mutation_k.log
    sha256: 93a31111ffd4bd06cd4bbc4bcc9bb08439e6def1f53e739b8acf44388ff9aca1
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/regenerated_candidate.json
    sha256: 907f5254364ce2106dc81a8b5bec20ca78b6f77c501c5b99a4209241d9de405e
    role: context
  - path: reports/sssom_generation_repair_20261031/logs/regenerated_candidate.log
    sha256: fa037fc3b55744ed0d582f375bccbe20aef5d66ccdf04fe2ec3215875b56c3d2
    role: context
  - path: reports/sssom_generation_repair_20261031/mutation-results.json
    sha256: 0b617d1cae50ec5e1e3c07424bd145ece522d11997e46fd402f630f26c02c9ed
    role: context
  - path: reports/sssom_generation_repair_20261031/original-41-remediation.json
    sha256: 15646d0468a3bb985eb0f4510968c338f1fc764a3dcc75719e84289267df83bf
    role: context
  - path: reports/sssom_generation_repair_20261031/other-field-changes.json
    sha256: ef4eb44db9a5f9f4f311633250044a0f0a8704a77de4c5d544a5269c1e27db68
    role: context
  - path: reports/sssom_generation_repair_20261031/validation-inputs.json
    sha256: 0068f36c4912e33249978cbdcd4817474e649fcf171c63801ce9a56953a4bc72
    role: context
  - path: reviews/structured/20261031T214143Z-sssom-current-inputs-mechanical/review.md
    sha256: 538a74e95b579f239f3bcb07575ac64aff449ac90006bbefaaba522538312955
    role: context
  - path: reviews/structured/20261031T214143Z-sssom-current-inputs-mechanical/review.yaml
    sha256: 56a5186a8db1280d39a0e4c021bd79de77d2dd0116c026e3e754a128c30e594e
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/reconcile_sssom.py
    sha256: 7a0d1b248a1ae1777a827bde4e795474531db565c17b35beaab66fb2631daba7
    role: context
  - path: scripts/validate_id_label_correspondence.py
    sha256: b5ff41bb52d24f5d7819fb12769e216440f75ec3fb3df3e3cb2c5082fffb40e0
    role: context
  - path: scripts/validate_sssom_invariants.py
    sha256: 89821559f9cbf999675b163396140c4b035cac7bf3ae23dd709f8b76e149de77
    role: context
  - path: src/mediaingredientmech/schema/mediaingredientmech.yaml
    sha256: bb43dee29b21fdee72a48022456e733e49e95824c4c09674f9b3165c290fe012
    role: context
scope:
  description: Exact current canonical and final-code diagnostic candidate snapshots;
    successor disposition limited to predecessor B5, K and G findings.
  selection: Two declared artifacts, all rows checked by their applicable native deterministic
    gates; artifact count is the scope denominator and row/diagnostic denominators
    are separate.
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
    role: External SSSOM generator repaired under issues 679, 680 and 681.
- target_id: candidate
  path: output/sssom-repair/final-code-replay.sssom.tsv
  label: 'Final-code diagnostic candidate: 2,980 rows; not promoted'
  kind: generated
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Maintained identity/mapping/synonym owner; no curation change in this run.
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_mim_ingredient_sssom.py
    role: External SSSOM generator repaired under issues 679, 680 and 681.
checks:
- check_id: regenerated_candidate
  name: regenerated candidate
  status: passed
  required: true
  summary: Supported native builder generated 2,980 diagnostic rows with code loaded
    before removal of an unused timezone import. Loaded/final code hashes are distinguished
    by final-code replay evidence.
  target_ids:
  - candidate
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/claw
    && uv run python ../locked_generation.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-regenerated_candidate
  scope_note: Actual run 2026-10-31T23:24:52.897761+00:00 through 2026-10-31T23:26:41.208918+00:00;
    original log retained at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/regenerated_candidate.log.
    Copied receipt preserves actual command and log hash.
- check_id: final_code_replay_retry
  name: final code replay retry
  status: passed
  required: true
  summary: Final code reproduces byte-identical 2,980-row output using captured emitted-object
    label values. No new label lookup/provider calls. Forty-eight requested CHEBI
    IDs absent from emitted rows are explicitly listed in the replay receipt.
  target_ids:
  - candidate
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/claw
    && uv run python ../replay_final_generator.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-final_code_replay_retry
  scope_note: Actual run 2026-10-31T23:28:14.522933+00:00 through 2026-10-31T23:28:26.768994+00:00;
    original log retained at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/final_code_replay_retry.log.
    Copied receipt preserves actual command and log hash.
- check_id: candidate_invariants_retry
  name: candidate invariants retry
  status: passed
  required: true
  summary: Native strict invariants pass A, B1, B2, B3, B5, C, D, E, F, G, H, I, J,
    K and L; reject output contains header only. B4 actual-path supplement is separate.
  target_ids:
  - candidate
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/mim
    && uv run python scripts/validate_sssom_invariants.py output/sssom-repair/ingredient_mappings.sssom.tsv
    --reject-tsv output/sssom-repair/rejected-rows-current.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-candidate_invariants_retry
  scope_note: Actual run 2026-10-31T23:26:58.039425+00:00 through 2026-10-31T23:27:06.939874+00:00;
    original log retained at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/candidate_invariants_retry.log.
    Copied receipt preserves actual command and log hash.
- check_id: candidate_schema
  name: candidate schema
  status: passed
  required: true
  summary: SSSOM JSON Schema, PrefixMapCompleteness and StrictCurieFormat pass. Native
    extension-field notices remain in the log.
  target_ids:
  - candidate
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/mim
    && sssom validate -V JsonSchema -V PrefixMapCompleteness -V StrictCurieFormat
    output/sssom-repair/ingredient_mappings.sssom.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-candidate_schema
  scope_note: Actual run 2026-10-31T23:26:49.862366+00:00 through 2026-10-31T23:26:51.808667+00:00;
    original log retained at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/candidate_schema.log.
    Copied receipt preserves actual command and log hash.
- check_id: candidate_curie
  name: candidate curie
  status: passed
  required: true
  summary: 2,980 rows and 5,960 CURIEs pass native syntax and known-prefix checks.
  target_ids:
  - candidate
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/mim
    && uv run python scripts/validate_published_curies.py output/sssom-repair/ingredient_mappings.sssom.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-candidate_curie
  scope_note: Actual run 2026-10-31T23:26:49.862459+00:00 through 2026-10-31T23:26:49.924505+00:00;
    original log retained at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/candidate_curie.log.
    Copied receipt preserves actual command and log hash.
- check_id: candidate_products
  name: candidate products
  status: passed
  required: true
  summary: 'Native candidate label policy passes: 2,216 canonical, four synonyms,
    four configured exceptions and 3,736 no-adapter skips. Only target selection/path
    changed from native configuration.'
  target_ids:
  - candidate
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/mim
    && uv run python scripts/validate_id_label_correspondence.py --config ../provenance/candidate-id-label-config.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-candidate_products
  scope_note: Actual run 2026-10-31T23:26:58.039420+00:00 through 2026-10-31T23:27:29.562713+00:00;
    original log retained at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/candidate_products.log.
    Copied receipt preserves actual command and log hash.
- check_id: compare_candidates_retry
  name: compare candidates retry
  status: passed
  required: true
  summary: 'All 41 original diagnostics reconciled. Relative to old candidate: 14
    surplus registry rows removed and 17 other fields changed, only by removing 17
    inherited object aliases; no added rows, remaining-row predicate changes or curated-subject
    synonym removals. Native find_drift reports all five categories zero.'
  target_ids:
  - canonical
  - candidate
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/mim
    && uv run python ../compare_candidates.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-compare_candidates_retry
  scope_note: Actual run 2026-10-31T23:27:36.325868+00:00 through 2026-10-31T23:27:37.292238+00:00;
    original log retained at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/compare_candidates_retry.log.
    Copied receipt preserves actual command and log hash.
- check_id: full_qc
  name: full qc
  status: passed
  required: true
  summary: Repository composite just qc passes on unchanged maintained MIM sources;
    this does not certify scientific truth or promote the candidate.
  target_ids:
  - canonical
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/mim
    && just qc
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-full_qc
  scope_note: Actual run 2026-10-31T23:24:30.912091+00:00 through 2026-10-31T23:26:51.079436+00:00;
    original log retained at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/full_qc.log.
    Copied receipt preserves actual command and log hash.
- check_id: baseline_curie
  name: baseline curie
  status: passed
  required: true
  summary: Canonical 2,987 rows/5,974 CURIEs pass; 20 tests pass, one skips.
  target_ids:
  - canonical
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/mim
    && just curie-validate
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-baseline_curie
  scope_note: Actual run 2026-10-31T23:25:49.842698+00:00 through 2026-10-31T23:25:50.390785+00:00;
    original log retained at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/baseline_curie.log.
    Copied receipt preserves actual command and log hash.
- check_id: baseline_reconcile
  name: baseline reconcile
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
  - log-baseline_reconcile
  scope_note: Actual run 2026-10-31T23:25:49.842702+00:00 through 2026-10-31T23:25:54.805305+00:00;
    original log retained at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/baseline_reconcile.log.
    Copied receipt preserves actual command and log hash.
- check_id: baseline_products
  name: baseline products
  status: passed
  required: true
  summary: Configured full product validation passes with 101 nonblocking warnings
    and 5,314 no-adapter skips; retained for transparency.
  target_ids:
  - canonical
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/mim
    && just validate-products
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-baseline_products
  scope_note: Actual run 2026-10-31T23:25:49.842781+00:00 through 2026-10-31T23:26:51.160037+00:00;
    original log retained at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/baseline_products.log.
    Copied receipt preserves actual command and log hash.
- check_id: baseline_subjects
  name: baseline subjects
  status: passed
  required: false
  summary: Native checker reports 18 non-gating opaque-slug/filename mismatches among
    2,611 subjects; no new gate imposed.
  target_ids:
  - canonical
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/mim
    && uv run python scripts/check_sssom_subject_files.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-baseline_subjects
  scope_note: Actual run 2026-10-31T23:25:49.842658+00:00 through 2026-10-31T23:25:49.894070+00:00;
    original log retained at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/baseline_subjects.log.
    Copied receipt preserves actual command and log hash.
- check_id: candidate_b4_actual
  name: candidate b4 actual
  status: passed
  required: false
  summary: Unmodified native B4 using actual read-only KG transform directory reports
    zero findings for repaired bytes; BTO/MICRO transforms absent and native absent-ID
    skips retained.
  target_ids:
  - candidate
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/mim
    && uv run python ../check_b4_actual.py output/sssom-repair/ingredient_mappings.sssom.tsv
    candidate
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-candidate_b4_actual
  scope_note: Actual run 2026-10-31T23:26:49.862328+00:00 through 2026-10-31T23:26:50.776334+00:00;
    original log retained at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/candidate_b4_actual.log.
    Copied receipt preserves actual command and log hash.
- check_id: baseline_b4_actual
  name: baseline b4 actual
  status: passed
  required: false
  summary: Unmodified native B4 against actual read-only KG transforms reports zero
    findings for canonical source, with the same BTO/MICRO coverage limits.
  target_ids:
  - canonical
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/mim
    && uv run python ../check_b4_actual.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-baseline_b4_actual
  scope_note: Actual run 2026-10-31T23:28:40.226303+00:00 through 2026-10-31T23:28:41.049791+00:00;
    original log retained at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/baseline_b4_actual.log.
    Copied receipt preserves actual command and log hash.
- check_id: focused_final
  name: focused final
  status: passed
  required: true
  summary: All 64 focused builder regression tests pass on final source; this is code
    behavior evidence, not scientific review.
  target_ids:
  - candidate
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/claw
    && uv run python -m pytest -q --no-cov tests/test_sssom_identity_row.py tests/test_mim_synonym_scope.py
    tests/test_mim_sssom_header_dates.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - log-focused_final
  scope_note: Actual run 2026-10-31T23:25:46.655707+00:00 through 2026-10-31T23:25:47.100501+00:00;
    original log retained at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/focused_final.log.
    Copied receipt preserves actual command and log hash.
- check_id: candidate_invariants
  name: candidate invariants
  status: failed
  required: false
  summary: Initial invocation used unsupported --sssom-path; argument parsing failed
    before validation. Correct positional invocation subsequently passed.
  target_ids:
  - candidate
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/mim
    && uv run python scripts/validate_sssom_invariants.py --sssom-path output/sssom-repair/ingredient_mappings.sssom.tsv
    --reject-tsv output/sssom-repair/rejected-rows-current.tsv
  exit_code: 2
  expected_exit_code: 0
  evidence_ids:
  - log-candidate_invariants
  scope_note: Actual run 2026-10-31T23:26:49.862368+00:00 through 2026-10-31T23:26:49.919502+00:00;
    original log retained at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/candidate_invariants.log.
    Copied receipt preserves actual command and log hash.
- check_id: compare_candidates
  name: compare candidates
  status: failed
  required: false
  summary: Diagnostic comparison helper initially passed mapping values to Counter.update;
    failed before its assertions/output. Corrected helper subsequently completed all
    assertions.
  target_ids:
  - candidate
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/mim
    && uv run python ../compare_candidates.py
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - log-compare_candidates
  scope_note: Actual run 2026-10-31T23:27:32.030870+00:00 through 2026-10-31T23:27:32.096586+00:00;
    original log retained at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/compare_candidates.log.
    Copied receipt preserves actual command and log hash.
- check_id: final_code_replay
  name: final code replay
  status: failed
  required: false
  summary: Replay preparation initially included non-lookup registry labels with multiple
    subject labels; it stopped before generation. Replay then restricted capture to
    actual lookup prefixes and produced byte-identical output.
  target_ids:
  - candidate
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/claw
    && uv run python ../replay_final_generator.py
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - log-final_code_replay
  scope_note: Actual run 2026-10-31T23:28:06.727074+00:00 through 2026-10-31T23:28:06.877920+00:00;
    original log retained at /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-repair-20261031T231945Z/logs/final_code_replay.log.
    Copied receipt preserves actual command and log hash.
evidence:
- evidence_id: log-regenerated_candidate
  kind: validation
  reference: reports/sssom_generation_repair_20261031/logs/regenerated_candidate.log
  accessed_at: '2026-10-31T23:30:12Z'
  support: supports
  summary: Supported native builder generated 2,980 diagnostic rows with code loaded
    before removal of an unused timezone import. Loaded/final code hashes are distinguished
    by final-code replay evidence.
  snapshot_sha256: fa037fc3b55744ed0d582f375bccbe20aef5d66ccdf04fe2ec3215875b56c3d2
- evidence_id: log-final_code_replay_retry
  kind: validation
  reference: reports/sssom_generation_repair_20261031/logs/final_code_replay_retry.log
  accessed_at: '2026-10-31T23:30:12Z'
  support: supports
  summary: Final code reproduces byte-identical 2,980-row output using captured emitted-object
    label values. No new label lookup/provider calls. Forty-eight requested CHEBI
    IDs absent from emitted rows are explicitly listed in the replay receipt.
  snapshot_sha256: 7d18299bf2def43986d31329e236bc089d7b54f794f25da034a2aba4f5ad0935
- evidence_id: log-candidate_invariants_retry
  kind: validation
  reference: reports/sssom_generation_repair_20261031/logs/candidate_invariants_retry.log
  accessed_at: '2026-10-31T23:30:12Z'
  support: supports
  summary: Native strict invariants pass A, B1, B2, B3, B5, C, D, E, F, G, H, I, J,
    K and L; reject output contains header only. B4 actual-path supplement is separate.
  snapshot_sha256: bfd845c17cfe56ef91d33d46a3374aff05b0705d8e0445d5e4a8161244ac44ce
- evidence_id: log-candidate_schema
  kind: validation
  reference: reports/sssom_generation_repair_20261031/logs/candidate_schema.log
  accessed_at: '2026-10-31T23:30:12Z'
  support: supports
  summary: SSSOM JSON Schema, PrefixMapCompleteness and StrictCurieFormat pass. Native
    extension-field notices remain in the log.
  snapshot_sha256: 6bb3a5fb4906f5382c09aa0eb0a8e6dbe45d2fe31c6dd726e030e30461fa4c2c
- evidence_id: log-candidate_curie
  kind: validation
  reference: reports/sssom_generation_repair_20261031/logs/candidate_curie.log
  accessed_at: '2026-10-31T23:30:12Z'
  support: supports
  summary: 2,980 rows and 5,960 CURIEs pass native syntax and known-prefix checks.
  snapshot_sha256: 31ca9b6d8a11e0181035e649476ee2a2c01b4b1cc04d7df1c6f0ebb182fab99e
- evidence_id: log-candidate_products
  kind: validation
  reference: reports/sssom_generation_repair_20261031/logs/candidate_products.log
  accessed_at: '2026-10-31T23:30:12Z'
  support: supports
  summary: 'Native candidate label policy passes: 2,216 canonical, four synonyms,
    four configured exceptions and 3,736 no-adapter skips. Only target selection/path
    changed from native configuration.'
  snapshot_sha256: b0695b05145765cb47f8ce259be004e003f012c9fdc69ecc502c598d22a8f38d
- evidence_id: log-compare_candidates_retry
  kind: validation
  reference: reports/sssom_generation_repair_20261031/logs/compare_candidates_retry.log
  accessed_at: '2026-10-31T23:30:12Z'
  support: supports
  summary: 'All 41 original diagnostics reconciled. Relative to old candidate: 14
    surplus registry rows removed and 17 other fields changed, only by removing 17
    inherited object aliases; no added rows, remaining-row predicate changes or curated-subject
    synonym removals. Native find_drift reports all five categories zero.'
  snapshot_sha256: 81b343763b935350f12c356330e4ff1e9b3542d0e04520312c952d87123dca71
- evidence_id: log-full_qc
  kind: validation
  reference: reports/sssom_generation_repair_20261031/logs/full_qc.log
  accessed_at: '2026-10-31T23:30:12Z'
  support: supports
  summary: Repository composite just qc passes on unchanged maintained MIM sources;
    this does not certify scientific truth or promote the candidate.
  snapshot_sha256: cb2e3db3661f7131926f0ddb0ff0bcb4c6bad81dcb5b874473c67bab4077e39d
- evidence_id: log-baseline_curie
  kind: validation
  reference: reports/sssom_generation_repair_20261031/logs/baseline_curie.log
  accessed_at: '2026-10-31T23:30:12Z'
  support: supports
  summary: Canonical 2,987 rows/5,974 CURIEs pass; 20 tests pass, one skips.
  snapshot_sha256: e9845a5693dde19e1fb1bf6da791d6ad6c620ce1458815fb998dc62a3c4e511b
- evidence_id: log-baseline_reconcile
  kind: validation
  reference: reports/sssom_generation_repair_20261031/logs/baseline_reconcile.log
  accessed_at: '2026-10-31T23:30:12Z'
  support: supports
  summary: Canonical GAP, ORPHAN, STALE, PREDICATE and GRADE counts are all zero.
  snapshot_sha256: 8bf18010d973e92de327bf8580964cbe3306206d7191c45a7b1731df9c7d61d7
- evidence_id: log-baseline_products
  kind: validation
  reference: reports/sssom_generation_repair_20261031/logs/baseline_products.log
  accessed_at: '2026-10-31T23:30:12Z'
  support: supports
  summary: Configured full product validation passes with 101 nonblocking warnings
    and 5,314 no-adapter skips; retained for transparency.
  snapshot_sha256: 1fa143fbbbdb204cfca441d722014ca3b2ab5eda915eb2f6de1b7dc997e1d335
- evidence_id: log-baseline_subjects
  kind: validation
  reference: reports/sssom_generation_repair_20261031/logs/baseline_subjects.log
  accessed_at: '2026-10-31T23:30:12Z'
  support: supports
  summary: Native checker reports 18 non-gating opaque-slug/filename mismatches among
    2,611 subjects; no new gate imposed.
  snapshot_sha256: a16772841d62c8f1f9be43c85a24d0e9c1e687b6ec493652fd2c5be113da7762
- evidence_id: log-candidate_b4_actual
  kind: validation
  reference: reports/sssom_generation_repair_20261031/logs/candidate_b4_actual.log
  accessed_at: '2026-10-31T23:30:12Z'
  support: supports
  summary: Unmodified native B4 using actual read-only KG transform directory reports
    zero findings for repaired bytes; BTO/MICRO transforms absent and native absent-ID
    skips retained.
  snapshot_sha256: 8e1e50ddfdeaef5dc6fafeb76974f6a559db5141bf846b6f6d0d9dbc3ba0739e
- evidence_id: log-baseline_b4_actual
  kind: validation
  reference: reports/sssom_generation_repair_20261031/logs/baseline_b4_actual.log
  accessed_at: '2026-10-31T23:30:12Z'
  support: supports
  summary: Unmodified native B4 against actual read-only KG transforms reports zero
    findings for canonical source, with the same BTO/MICRO coverage limits.
  snapshot_sha256: 181adf3eb5d1c4d4fcf30ddd35ce808edb8ec7a0278ea341916f22c51dd07360
- evidence_id: log-focused_final
  kind: validation
  reference: reports/sssom_generation_repair_20261031/logs/focused_final.log
  accessed_at: '2026-10-31T23:30:12Z'
  support: supports
  summary: All 64 focused builder regression tests pass on final source; this is code
    behavior evidence, not scientific review.
  snapshot_sha256: 8a0f611592f19c13c80f67616b2006a8c83056d068810e1fb48bdac8a86eecc3
- evidence_id: log-candidate_invariants
  kind: validation
  reference: reports/sssom_generation_repair_20261031/logs/candidate_invariants.log
  accessed_at: '2026-10-31T23:30:12Z'
  support: context_only
  summary: Initial invocation used unsupported --sssom-path; argument parsing failed
    before validation. Correct positional invocation subsequently passed.
  snapshot_sha256: 789bc919eadbf502f0b64b73779eecdb3d853a1482c03c7b6d5ff9960a5cc5f6
- evidence_id: log-compare_candidates
  kind: validation
  reference: reports/sssom_generation_repair_20261031/logs/compare_candidates.log
  accessed_at: '2026-10-31T23:30:12Z'
  support: context_only
  summary: Diagnostic comparison helper initially passed mapping values to Counter.update;
    failed before its assertions/output. Corrected helper subsequently completed all
    assertions.
  snapshot_sha256: c7914e3306b18554122d905ccd99f9ff84685d56f0fb538412bb779d9c5955d1
- evidence_id: log-final_code_replay
  kind: validation
  reference: reports/sssom_generation_repair_20261031/logs/final_code_replay.log
  accessed_at: '2026-10-31T23:30:12Z'
  support: context_only
  summary: Replay preparation initially included non-lookup registry labels with multiple
    subject labels; it stopped before generation. Replay then restricted capture to
    actual lookup prefixes and produced byte-identical output.
  snapshot_sha256: c22a8e76515603ae72ece1f0870c5ec3c3371a043e8ed19d0504d49be05a55a8
- evidence_id: prior-review
  kind: prior_review
  reference: reviews/structured/20261031T214143Z-sssom-current-inputs-mechanical/review.yaml
  accessed_at: '2026-10-31T23:30:12Z'
  support: context_only
  summary: Exact predecessor observation copied byte-for-byte; only its three candidate
    mechanical findings are reconciled here.
  snapshot_sha256: 56a5186a8db1280d39a0e4c021bd79de77d2dd0116c026e3e754a128c30e594e
- evidence_id: semantics
  kind: authority
  reference: MAPPING_SEMANTICS.md
  accessed_at: '2026-10-31T23:30:12Z'
  support: supports
  summary: Identity, registry namespace, predicate and synonym contracts remain authoritative.
    No scientific claim is inferred from passing diagnostics.
  snapshot_sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
- evidence_id: comparison
  kind: record_content
  reference: reports/sssom_generation_repair_20261031/candidate-comparison.json
  accessed_at: '2026-10-31T23:30:12Z'
  support: supports
  summary: Separate comparisons against old raw candidate and unchanged maintained
    canonical mapping, including counts, exact changed fields and native drift results.
  snapshot_sha256: 81b343763b935350f12c356330e4ff1e9b3542d0e04520312c952d87123dca71
- evidence_id: remediation
  kind: record_content
  reference: reports/sssom_generation_repair_20261031/original-41-remediation.json
  accessed_at: '2026-10-31T23:30:12Z'
  support: supports
  summary: Every original B5/K/G diagnostic retains exact selector/reason and explicit
    current disposition. Fourteen maintained primary identity rows survive; fourteen
    extra identities are removed; eleven K tokens disappear; two headers match newest
    row date.
  snapshot_sha256: 15646d0468a3bb985eb0f4510968c338f1fc764a3dcc75719e84289267df83bf
- evidence_id: other-changes
  kind: record_content
  reference: reports/sssom_generation_repair_20261031/other-field-changes.json
  accessed_at: '2026-10-31T23:30:12Z'
  support: supports
  summary: Exact 17 changed row triples with before/after other payloads; 17 removed
    tokens and no added tokens. No removed token is a publishable curated subject
    synonym.
  snapshot_sha256: ef4eb44db9a5f9f4f311633250044a0f0a8704a77de4c5d544a5269c1e27db68
- evidence_id: inputs
  kind: record_content
  reference: reports/sssom_generation_repair_20261031/validation-inputs.json
  accessed_at: '2026-10-31T23:30:12Z'
  support: supports
  summary: Current SHA-256 provenance for 2,985 files including every MIM record,
    maintained aggregates, canonical/review pins, copied residual, actual KG mapping/Medidive
    inputs and ontology DBs. Repository revisions and working-tree diff hashes distinguish
    local code changes.
  snapshot_sha256: 0068f36c4912e33249978cbdcd4817474e649fcf171c63801ce9a56953a4bc72
- evidence_id: generator-revisions
  kind: record_content
  reference: reports/sssom_generation_repair_20261031/generator-revisions.json
  accessed_at: '2026-10-31T23:30:12Z'
  support: supports
  summary: Original generator-loaded hash and final source hash differ only by unused
    timezone import removal; exact reconstruction verifies this distinction.
  snapshot_sha256: 04293c14ed9b202fbc59b5f58023eb83007fce179d614ba72d1b0d6c037f6111
- evidence_id: final-code-replay
  kind: validation
  reference: reports/sssom_generation_repair_20261031/final-code-replay.json
  accessed_at: '2026-10-31T23:30:12Z'
  support: supports
  summary: Final-code output hash equals the independently validated regenerated output
    hash. Captured values are emitted object labels, not a complete archive of original
    lookup responses.
  snapshot_sha256: 4a7e0f07358175f1bc50ed55db98a255fc17063a4b9f956edfe7faafbc741946
- evidence_id: candidate-config
  kind: record_content
  reference: reports/sssom_generation_repair_20261031/candidate-id-label-config.json
  accessed_at: '2026-10-31T23:30:12Z'
  support: supports
  summary: All native label policy/adapters/exceptions unchanged; only targets narrowed
    to sssom and glob redirected.
  snapshot_sha256: 1fa9c2494e9b5c5966d14b030030f88dddea0c9c7f4a2228ba5f528a23a601a7
- evidence_id: b4-inputs
  kind: validation
  reference: reports/sssom_generation_repair_20261031/candidate-b4-actual.json
  accessed_at: '2026-10-31T23:30:12Z'
  support: supports
  summary: Exact available ontology transform hashes and BTO/MICRO missing-prefix
    limits; no fake paths or labels.
  snapshot_sha256: 3ffb788739125200983ae47963f0a7ccbb27d188103ed526f61a7a704a86bf31
- evidence_id: historical-holds
  kind: prior_review
  reference: reports/sssom_generation_repair_20261031/historical-rule-k-holds.json
  accessed_at: '2026-10-31T23:30:12Z'
  support: context_only
  summary: All eleven corresponding canonical non-exact rows remain WITHHOLD in the
    pinned release. Mechanical repairs neither approve their relation/synonym scope
    nor change identity.
  snapshot_sha256: a3ab2487192691c441a53cd6a33ba48bb3272dbec67fe8819ef5b15a8e575334
- evidence_id: pinned-review
  kind: prior_review
  reference: reports/sssom_completion_20260921/review.json
  accessed_at: '2026-10-31T23:30:12Z'
  support: context_only
  summary: Historical content-bound scientific release decisions remain unchanged;
    this review is not a successor release ledger.
  snapshot_sha256: 6c74c7cc3eb8075ec18e20ab594a9b5eae9910b08b98c9d0746b3374af6c7ac6
- evidence_id: mutations
  kind: validation
  reference: reports/sssom_generation_repair_20261031/mutation-results.json
  accessed_at: '2026-10-31T23:30:12Z'
  support: supports
  summary: Each B5/K/G code reversion was detected by focused tests. Raw expected-failure
    receipts remain diagnostic evidence, not a failing final gate.
  snapshot_sha256: 0b617d1cae50ec5e1e3c07424bd145ece522d11997e46fd402f630f26c02c9ed
- evidence_id: target-canonical
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  accessed_at: '2026-10-31T23:30:12Z'
  support: supports
  summary: 'Exact inspected Unchanged maintained canonical mapping: 2,987 rows.'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: target-candidate
  kind: record_content
  reference: output/sssom-repair/final-code-replay.sssom.tsv
  accessed_at: '2026-10-31T23:30:12Z'
  support: supports
  summary: 'Exact inspected Final-code diagnostic candidate: 2,980 rows; not promoted.'
  snapshot_sha256: 04159ba36b221d1c8ebf6e281972c846a333cf4fe5e868b06bb5326f2b02e3a7
assessments:
- assessment_id: canonical-preserved
  area: consistency
  topic: Unchanged maintained source remains mechanically valid
  outcome: supported
  target_ids:
  - canonical
  evidence_ids:
  - target-canonical
  - inputs
  - comparison
  - log-full_qc
  - log-baseline_reconcile
  - log-baseline_curie
  - log-baseline_products
  summary: The canonical mapping remains 2,987 rows with its original SHA-256. MIM
    records, aggregates, unified mapping and pinned review remain unchanged. Native
    full QC and scoped source validators pass.
  metrics:
  - name: canonical_rows
    value: 2987
    unit: rows
    definition: Data rows excluding metadata and header.
    minimum: 0
- assessment_id: candidate-remediated
  area: consistency
  topic: All predecessor mechanical defects resolved without scientific reassignment
  outcome: supported
  target_ids:
  - candidate
  evidence_ids:
  - target-candidate
  - remediation
  - comparison
  - other-changes
  - log-candidate_invariants_retry
  - log-candidate_schema
  - log-candidate_curie
  - log-candidate_products
  summary: The final-code candidate contains 2,980 rows and zero native invariant
    rejects. All 41 prior B5/K/G diagnostics have explicit evidence-linked outcomes.
    Against the old candidate, only fourteen surplus registry rows, seventeen inherited
    other aliases and two header dates change.
  metrics:
  - name: candidate_rows
    value: 2980
    unit: rows
    definition: Final-code replay TSV data rows excluding metadata and header.
    minimum: 0
  - name: resolved_prior_diagnostics
    value: 41
    unit: diagnostics
    definition: 28 B5 row diagnostics, eleven K row diagnostics and two G header diagnostics.
    minimum: 0
    denominator: 41
  - name: removed_surplus_rows
    value: 14
    unit: rows
    definition: Competing generated registry identity rows removed; maintained primary
      identity rows retained.
    minimum: 0
    denominator: 2994
  - name: removed_inherited_aliases
    value: 17
    unit: tokens
    definition: Removed target-only tokens across seventeen nonexact rows; no curated
      subject synonym removed.
    minimum: 0
- assessment_id: final-code-equivalence
  area: provenance
  topic: Loaded and final generator identities distinguished
  outcome: supported
  target_ids:
  - candidate
  evidence_ids:
  - generator-revisions
  - final-code-replay
  - log-final_code_replay_retry
  - inputs
  summary: Generation began with the repaired code before a later unused-import cleanup.
    The final source reproduces exactly the same mapping bytes using captured emitted-label
    values and native generation/stamp behavior. This replay is not a fresh ontology
    lookup or scientific review.
- assessment_id: coverage-limits
  area: scope
  topic: Native warning, skip and release boundaries retained
  outcome: supported
  target_ids:
  - canonical
  - candidate
  evidence_ids:
  - log-baseline_products
  - log-baseline_subjects
  - log-candidate_products
  - b4-inputs
  - historical-holds
  - pinned-review
  - candidate-config
  summary: 'Scoped mechanical gates pass with documented native limits: 101 nonblocking
    full-product warnings; 5,314 baseline and 3,736 candidate no-adapter skips; 18
    non-gating subject warnings; BTO/MICRO transform skips. Historical scientific
    WITHHOLD decisions and prior validation stamps remain historical; no candidate
    promotion occurred.'
  metrics:
  - name: baseline_label_warnings
    value: 101
    unit: pair diagnostics
    definition: Native configured nonblocking full-product plausibility warnings;
      not unique records.
    minimum: 0
  - name: opaque_slug_warnings
    value: 18
    unit: subjects
    definition: Native non-gating unresolved filename/subject contract.
    minimum: 0
    denominator: 2611
findings:
- finding_id: F-B5
  issue_key: sssom-builder-dual-local-namespace
  category: identity
  severity: major
  status: resolved
  certainty: confirmed
  title: 'Resolved: Builder adds a second incompatible registry identity'
  description: The prior mechanical defect is resolved in this exact final-code diagnostic
    candidate. The builder recognizes an already emitted registry identity in either
    permitted local namespace before synthesizing B1 backfill. All 14 maintained primary
    identities remain; the 14 competing generated identities disappear. Native B5
    and the complete invariant suite pass. No YAML identifier was changed. Original
    selectors below identify the earlier observed rows/headers; removed rows intentionally
    have no current counterpart.
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
  - log-candidate_invariants_retry
  - log-final_code_replay_retry
  - other-changes
  - mutations
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
  disposition_reason: The builder recognizes an already emitted registry identity
    in either permitted local namespace before synthesizing B1 backfill. All 14 maintained
    primary identities remain; the 14 competing generated identities disappear. Native
    B5 and the complete invariant suite pass. No YAML identifier was changed. Resolution
    is scoped to observed working-tree output, not a statement that its fixing PR
    is merged or that a scientific release hold is cleared.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261031T214143Z-sssom-current-inputs-mechanical
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
  description: The prior mechanical defect is resolved in this exact final-code diagnostic
    candidate. External object aliases are inherited only for final exactMatch rows.
    All eleven originally rejected tokens are absent; seventeen target-only tokens
    are removed overall while curated subject aliases survive. Final predicates and
    registry identities are preserved. Native K and label checks pass. No synonym
    curation or scientific identity choice was applied. Original selectors below identify
    the earlier observed rows/headers; removed rows intentionally have no current
    counterpart.
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
  - log-candidate_invariants_retry
  - log-final_code_replay_retry
  - other-changes
  - mutations
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
  disposition_reason: External object aliases are inherited only for final exactMatch
    rows. All eleven originally rejected tokens are absent; seventeen target-only
    tokens are removed overall while curated subject aliases survive. Final predicates
    and registry identities are preserved. Native K and label checks pass. No synonym
    curation or scientific identity choice was applied. Resolution is scoped to observed
    working-tree output, not a statement that its fixing PR is merged or that a scientific
    release hold is cleared.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261031T214143Z-sssom-current-inputs-mechanical
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
  description: The prior mechanical defect is resolved in this exact final-code diagnostic
    candidate. Both header dates now equal 2026-10-15, the newest emitted row date.
    Native G passes; source row dates were not rewritten to manufacture agreement.
    Original selectors below identify the earlier observed rows/headers; removed rows
    intentionally have no current counterpart.
  target_ids:
  - candidate
  field_paths:
  - header.mapping_date
  - header.mapping_set_version
  evidence_ids:
  - prior-review
  - remediation
  - comparison
  - log-candidate_invariants_retry
  - log-final_code_replay_retry
  - other-changes
  - mutations
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
  disposition_reason: Both header dates now equal 2026-10-15, the newest emitted row
    date. Native G passes; source row dates were not rewritten to manufacture agreement.
    Resolution is scoped to observed working-tree output, not a statement that its
    fixing PR is merged or that a scientific release hold is cleared.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261031T214143Z-sssom-current-inputs-mechanical
    finding_id: F-G
  external_issues:
  - https://github.com/CultureBotAI/culturebotai-claw/issues/681
actions: []
limitations:
- Mechanical resolution is confined to the exact inspected candidate, not to merged/published
  state or scientific approval.
- Historical WITHHOLD decisions, unresolved nonexact relation/synonym-scope obligations
  and prior validation_method stamps are not approved, recalibrated or migrated.
- Native B4 remains best-effort with missing BTO/MICRO transform files and absent-ID
  skips. Missing-file checks include ignored files at the exact actual KG transform
  directory.
- Configured no-adapter label skips, 101 nonblocking baseline warnings and 18 opaque-slug
  warnings remain; passing enforcement is not complete scientific coverage.
- Final-code replay uses labels captured from emitted rows, not full original lookup
  responses. Forty-eight requested CHEBI IDs absent from output are listed; exact
  output equality was verified and replay made no network/provider calls.
- Candidate differs substantially from maintained canonical source beyond this bounded
  repair; separate canonical comparison is retained. It must not be treated as a drop-in
  approved release.
- Generated full mappings and large ontology/source inputs remain diagnostic/local.
  Copied tracked reports retain exact hashes, commands, before/after selectors and
  results; working-tree attestations do not claim those full inputs were committed.
related_reviews:
- repository: CultureBotAI/MediaIngredientMech
  review_id: 20261031T214143Z-sssom-current-inputs-mechanical
  relationship: Resolves only the predecessor candidate B5, K and G mechanical findings;
    preserves original observation byte-for-byte and retains scientific limits.
links:
- https://github.com/CultureBotAI/culturebotai-claw/issues/679
- https://github.com/CultureBotAI/culturebotai-claw/issues/680
- https://github.com/CultureBotAI/culturebotai-claw/issues/681
tags:
- sssom
- mechanical-review
- native-invariants
- historical-holds-preserved
```
