# Bounded SSSOM provenance restoration and unchanged companion refresh

- Review: 20261101T020938Z-sssom-followup-mechanical
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-11-01T02:04:46.796294Z
- Finished UTC: 2026-11-01T02:09:38.381188Z
- Reviewer: Codex /root/sssom_validation (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Two generated targets: canonical retains 2,987 rows with exactly nine changed payloads versus 4625afd and 1,740/1,247 dispositions; the companion preserves 51 claims and 20 owner records. No new scientific approval is inferred.

## Scope And Provenance

Mechanical integrity and preservation of two exact generated outputs after issues 1012-1018; source/comment restoration and dependency-only successor generation.

Selection: Canonical SSSOM and the new follow-up companion review only. All rows/decisions of those artifacts are compared; scientific correctness of every original claim is not reassessed.
Coverage: full; 2 reviewed / 2 in the declared population.
Source: working_tree at Git base 612860e467aff74ecc1339df7c3c32b1bf940b95.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| canonical | mappings/ingredient_mappings.sssom.tsv | generated | Canonical SSSOM after the bounded source/comment restoration |
| companion | reports/ingredient_bundle_20261101_followup/review.json | generated | Dependency-only companion successor retaining the selected claims and owners |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| followup native target audit | passed | True | canonical, companion | Exact row, receipt, selected-claim, owner and protected-file comparison passes. |
| followup full qc | passed | True | canonical | Full just qc passes; native A/B1/B2/B3/B5/C/D/E/F/G/H/I/J/K/L invariants have zero rejects. Native B4 skips absent sibling transforms. |
| followup1014 assemble check | passed | True | canonical | Complete native mapping review reproduces the restored source bytes and receipt chain. |
| followup semantic build | passed | True | canonical | Native semantic builder completes; global scientific result remains FAIL with 1,733 findings / 2,272 assertions. |
| followup semantic integrity | passed | True | canonical | Native semantic integrity passes without changing the separate global scientific FAIL verdict. |
| followup supported export | passed | True | canonical | Supported KGX export completes for the already approved subset; backlog remains separate. |
| followup supported validate | passed | True | canonical | Supported graph integrity passes: 1,740 SSSOM rows / 2,220 approved edges; 2,272 excluded assertions remain. |
| followup reviewed export | passed | True | canonical | Reviewed SSSOM exporter preserves the 1,740 SUPPORTED / 1,247 WITHHOLD partition. |
| followup reviewed validate | passed | True | canonical | Native reviewed-export integrity and schema validation pass for both partitions. |
| followup refresh final tests | passed | True | companion | 82 current companion refresh and consumer tests pass, including changed-data refusals, dates, symlink paths and reservation races. |
| followup refresh final replay | passed | True | companion | Current maintained producer reproduces the successor bytes exactly: d391ec9e0dc004494431f76a81c392efef114746e7bf1eca57c7ce4dc7dec14c. |
| issue1018 receipt green | passed | True | canonical | 64 focused compatibility and collision tests pass, including no-source-write failure/successful-late-open replacement races. |
| issue1017 receipt suite | passed | True | canonical | Native mapping receipt and assembler regression suite passes; coexisting synonym/mapping-change evidence survives. |
| followup typecheck final | passed | True | canonical, companion | Maintained package type check passes for 52 source files. |
| followup python lint | passed | True | canonical, companion | Ruff passes for maintained producer, guards, assembler and changed tests. |
| followup format check online | passed | True | canonical, companion | Black check passes for the two changed maintained package modules. |
| followup full lint | passed | True | canonical, companion | Ruff passes for the full maintained package. |
| followup full format | passed | True | canonical, companion | Black check passes for the full maintained package. |
| followup package coverage | passed | True | canonical, companion | Maintained package coverage is 71%, exceeding the actual 35% gate; this is distinct from the whole package-plus-script aggregate. |
| followup full tests | passed | True | canonical, companion | Complete repository pytest suite passes: 3,276 passed, 6 skipped, 32 warnings. A non-executable annotation added during the run is separately covered by the final 82-test bundle suite, mypy and byte-identical replay. |

## Scientific And Domain Assessments

### Exact row and disposition preservation

consistency: supported. Targets: canonical.

All 2,987 row identities and positions persist; exactly nine payloads differ from 4625afd. Seven change only other; carnitine parent changes other/date and registry row changes date. Every historical source cell and the #390 comment are restored; 2,978 other payloads are identical. All nine changed rows remain withheld; all dispositions match the preceding PR head.

### Dependency refresh preserves selected scientific content

provenance: supported. Targets: companion.

The 51 decisions and claims (18 identifier, 20 mapping, 10 occurrence, 3 product), 20 owner bytes and selected complete mapping rows remain unchanged. Only validated global dependency bindings change. The final maintained producer replays the successor byte-for-byte without overwriting historical reviews or adding approval.

### Evidence reservation and native assembly regressions

representation: supported. Targets: canonical, companion.

Shared receipt/backup reservation checks still-owned device/inode identities before mutator entry and removes only owned partial reservations. The companion publisher retains exclusive handles. Collision and replacement probes preserve competing evidence and refuse source writes. Native assembly retains simultaneous synonym_correction and mapping_change bases on rows 184, 901 and 2528.

### Mechanical validity does not grant scientific release approval

scope: supported. Targets: canonical, companion.

Integrity and reviewed subset exports pass while the global scientific release remains FAIL with 1,733 findings and 2,272 assertions. No holds are retired, no approvals are carried to changed owner payloads, and no earlier structured scientific review is superseded by this mechanical observation.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| followup_native_target_audit | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup_native_target_audit.log | supports | Exact row, receipt, selected-claim, owner and protected-file comparison passes. |
| followup_native_target_audit-receipt | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup_native_target_audit.json | context_only | Actual command, working directory, start/finish, exit and original log hash. |
| followup-full-qc | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-full-qc.log | supports | Full just qc passes; native A/B1/B2/B3/B5/C/D/E/F/G/H/I/J/K/L invariants have zero rejects. Native B4 skips absent sibling transforms. |
| followup-full-qc-receipt | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-full-qc.json | context_only | Actual command, working directory, start/finish, exit and original log hash. |
| followup1014-assemble-check | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup1014-assemble-check.log | supports | Complete native mapping review reproduces the restored source bytes and receipt chain. |
| followup1014-assemble-check-receipt | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup1014-assemble-check.json | context_only | Actual command, working directory, start/finish, exit and original log hash. |
| followup-semantic-build | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-semantic-build.log | supports | Native semantic builder completes; global scientific result remains FAIL with 1,733 findings / 2,272 assertions. |
| followup-semantic-build-receipt | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-semantic-build.json | context_only | Actual command, working directory, start/finish, exit and original log hash. |
| followup-semantic-integrity | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-semantic-integrity.log | supports | Native semantic integrity passes without changing the separate global scientific FAIL verdict. |
| followup-semantic-integrity-receipt | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-semantic-integrity.json | context_only | Actual command, working directory, start/finish, exit and original log hash. |
| followup-supported-export | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-supported-export.log | supports | Supported KGX export completes for the already approved subset; backlog remains separate. |
| followup-supported-export-receipt | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-supported-export.json | context_only | Actual command, working directory, start/finish, exit and original log hash. |
| followup-supported-validate | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-supported-validate.log | supports | Supported graph integrity passes: 1,740 SSSOM rows / 2,220 approved edges; 2,272 excluded assertions remain. |
| followup-supported-validate-receipt | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-supported-validate.json | context_only | Actual command, working directory, start/finish, exit and original log hash. |
| followup-reviewed-export | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-reviewed-export.log | supports | Reviewed SSSOM exporter preserves the 1,740 SUPPORTED / 1,247 WITHHOLD partition. |
| followup-reviewed-export-receipt | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-reviewed-export.json | context_only | Actual command, working directory, start/finish, exit and original log hash. |
| followup-reviewed-validate | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-reviewed-validate.log | supports | Native reviewed-export integrity and schema validation pass for both partitions. |
| followup-reviewed-validate-receipt | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-reviewed-validate.json | context_only | Actual command, working directory, start/finish, exit and original log hash. |
| followup-refresh-final-tests | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-refresh-final-tests.log | supports | 82 current companion refresh and consumer tests pass, including changed-data refusals, dates, symlink paths and reservation races. |
| followup-refresh-final-tests-receipt | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-refresh-final-tests.json | context_only | Actual command, working directory, start/finish, exit and original log hash. |
| followup-refresh-final-replay | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-refresh-final-replay.log | supports | Current maintained producer reproduces the successor bytes exactly: d391ec9e0dc004494431f76a81c392efef114746e7bf1eca57c7ce4dc7dec14c. |
| followup-refresh-final-replay-receipt | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-refresh-final-replay.json | context_only | Actual command, working directory, start/finish, exit and original log hash. |
| issue1018_receipt_green | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/issue1018_receipt_green.log | supports | 64 focused compatibility and collision tests pass, including no-source-write failure/successful-late-open replacement races. |
| issue1018_receipt_green-receipt | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/issue1018_receipt_green.json | context_only | Actual command, working directory, start/finish, exit and original log hash. |
| issue1017_receipt_suite | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/issue1017_receipt_suite.log | supports | Native mapping receipt and assembler regression suite passes; coexisting synonym/mapping-change evidence survives. |
| issue1017_receipt_suite-receipt | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/issue1017_receipt_suite.json | context_only | Actual command, working directory, start/finish, exit and original log hash. |
| followup-typecheck-final | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-typecheck-final.log | supports | Maintained package type check passes for 52 source files. |
| followup-typecheck-final-receipt | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-typecheck-final.json | context_only | Actual command, working directory, start/finish, exit and original log hash. |
| followup-python-lint | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-python-lint.log | supports | Ruff passes for maintained producer, guards, assembler and changed tests. |
| followup-python-lint-receipt | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-python-lint.json | context_only | Actual command, working directory, start/finish, exit and original log hash. |
| followup-format-check-online | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-format-check-online.log | supports | Black check passes for the two changed maintained package modules. |
| followup-format-check-online-receipt | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-format-check-online.json | context_only | Actual command, working directory, start/finish, exit and original log hash. |
| followup-full-lint | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-full-lint.log | supports | Ruff passes for the full maintained package. |
| followup-full-lint-receipt | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-full-lint.json | context_only | Actual command, working directory, start/finish, exit and original log hash. |
| followup-full-format | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-full-format.log | supports | Black check passes for the full maintained package. |
| followup-full-format-receipt | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-full-format.json | context_only | Actual command, working directory, start/finish, exit and original log hash. |
| followup-package-coverage | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-package-coverage.log | supports | Maintained package coverage is 71%, exceeding the actual 35% gate; this is distinct from the whole package-plus-script aggregate. |
| followup-package-coverage-receipt | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-package-coverage.json | context_only | Actual command, working directory, start/finish, exit and original log hash. |
| followup-full-tests | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-full-tests.log | supports | Complete repository pytest suite passes: 3,276 passed, 6 skipped, 32 warnings. A non-executable annotation added during the run is separately covered by the final 82-test bundle suite, mypy and byte-identical replay. |
| followup-full-tests-receipt | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-full-tests.json | context_only | Actual command, working directory, start/finish, exit and original log hash. |
| target-audit | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/target-audit.json | supports | Fresh exact baseline comparison and preserved target claims; exact selectors and changed fields for all nine rows. |
| receipt14 | reports/sssom_completion_20260921/mapping_changes/issue669-1003-scoped-alias-corrections.json | supports | Preserved original nine-row scientific correction receipt; this follow-up does not repeat its scientific review. |
| receipt15 | reports/sssom_completion_20260921/mapping_changes/issue1014-provenance-restoration.json | supports | Append-only provenance restoration changes only two existing rows and grants no approval. |
| mapping-review | reports/sssom_completion_20260921/review.json | supports | Current native decisions retain 1,740 SUPPORTED and 1,247 WITHHOLD rows. |
| dependency | reports/ingredient_bundle_20261101_followup/dependency-refresh.json | supports | Original successor execution receipt proves the 51-claim/20-owner cohort unchanged; final maintained producer replay separately confirms the same review bytes. |
| prior-companion | reports/ingredient_bundle_20261101/review.json | supports | Historical companion decision/owner baseline, retained unchanged. |
| semantics | MAPPING_SEMANTICS.md | supports | Identity, predicates, provenance columns and same-subject synonym contract. |
| semantic-status | reports/semantic_review_20260921/resolution/current-review.json | context_only | Full scientific release remains FAIL; 1,733 finding IDs / 2,272 assertion IDs remain blocked. |
| reservation-reprobe | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/receipt-reservation-cleanup-fixed.json | supports | Separate reviewer reproduced successful and failed late-reservation replacement cases; mutator never entered and competing receipts survived. |
| check-provenance | reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/verification.json | supports | Published command/log hash inventory, current source hashes and explicit broad-suite/final-annotation chronology. |

## Limits And Additional Notes

- The verdict is limited to mechanical consistency/provenance of two specified generated artifacts, not a new scientific assessment of the corpus or companion claims.
- The global semantic release remains FAIL with 1,733 blocking findings and 2,272 blocked assertions; 1,247 mapping rows remain withheld, including both carnitine rows and the six rows for unresolved issues 1004/1005.
- Native just qc skips Rule B4 because the expected sibling ontology transforms are absent. This review does not claim a new ontology label or actual-directory B4 evaluation.
- Earlier product-label, reconciliation and opaque-subject diagnostics remain historical; this follow-up changes provenance cells only relative to the preceding canonical head and does not re-certify unresolved synonym or identity policy.
- The original companion generation receipt binds its original producer hash. The later final-code replay is separate evidence of identical successor bytes; historical receipts are not rewritten to claim a later code hash.
- The final BinaryIO/local-list annotation was added during the broad suite without changing executable writer logic. The final annotated module separately passed 82 focused bundle tests, mypy and byte-identical native replay. The broad run is not misrepresented as an exact static-byte test of the final annotation.
- Review source is the inspected working tree based on 612860e, not a claim of final committed-head independence. Separate independent review remains required by the parent workflow.
- Evidence paths retain the exact original command receipts; file discovery for copied evidence includes ignored report files. No whole-candidate promotion or scientific-status change is authorized by this review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261101T020938Z-sssom-followup-mechanical
kind: repository
repository: CultureBotAI/MediaIngredientMech
title: Bounded SSSOM provenance restoration and unchanged companion refresh
started_at: '2026-11-01T02:04:46.796294Z'
finished_at: '2026-11-01T02:09:38.381188Z'
reviewer:
  identity: Codex /root/sssom_validation
  kind: agent
  model: gpt-6
  independence: self_review
  independence_basis: Author of shared reservation fixes and their tests; this is
    a mechanical author assessment. Separate final-head adversarial review is not
    replaced.
skill: .claude/skills/review-sssom-output/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: false
native_verdict: Mechanical follow-up gates pass; scientific release remains FAIL
summary: 'Two generated targets: canonical retains 2,987 rows with exactly nine changed
  payloads versus 4625afd and 1,740/1,247 dispositions; the companion preserves 51
  claims and 20 owner records. No new scientific approval is inferred.'
source:
  git_revision: 612860e467aff74ecc1339df7c3c32b1bf940b95
  state: working_tree
  inputs:
  - path: .claude/skills/review-sssom-output/SKILL.md
    sha256: 2e05b30eefce620fbb78196386e476c330b81e36738f2461b4be64391a61ecd5
    role: context
  - path: .github/workflows/qc-evidence.yaml
    sha256: 5814a583a571b3e622a493942dd5483656c7d69531485e560db7c8075e1d7751
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
  - path: conf/record_review.yaml
    sha256: 07a8fa6d17ee664c7a2bc2d5b5821bd106f6aa454299b4f3e0440176876cd82e
    role: context
  - path: data/curated/mapped_ingredients.yaml
    sha256: 56e9eae4e0dd282e9c5a5d6d8c972faa99ddda76127bb26a9df5f5934abce09d
    role: context
  - path: data/ingredients/mapped/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.yaml
    sha256: 8d5da3b1c891a79adf823a2ea778b04ef2658cc6bc175469631251c3874a314b
    role: context
  - path: data/ingredients/mapped/84_GL_NaHCO3_Solution.yaml
    sha256: 1a8f4136f2de11105febf3112e5ca27fd95fcf9266ca1bb2283210267f70a509
    role: context
  - path: data/ingredients/mapped/Acriflavine.yaml
    sha256: d8ec8d8d5d56bfde012c54709bd80b33dff64660df7ce111d28de40707e9824e
    role: context
  - path: data/ingredients/mapped/Anabasine_Hydrochloride.yaml
    sha256: c9c693f7bc5354b5c472efaf4472f66b56e5c4e8d3a814490982da1d94810215
    role: context
  - path: data/ingredients/mapped/Betaine_Hydrochloride.yaml
    sha256: 77cf04f3fafb04a92080656711b7807ed4e9af7c79f7852ffd31a09fe428f4ac
    role: context
  - path: data/ingredients/mapped/Bovine_Serum_Albumin.yaml
    sha256: 43ceecb07d1bfa49f863a4c9d2618c79f8ab93385a8752ea88f07a6924b0f094
    role: context
  - path: data/ingredients/mapped/Carnitine_Hydrochloride.yaml
    sha256: c03c1c66b9e70436da2e841d1edf2a700f05830674c715fc265ac7fde9705722
    role: context
  - path: data/ingredients/mapped/Cotarnine_Chloride.yaml
    sha256: 821fd7dd0dd3c8308727c3e6a4999c860eb6be69a42d6bb996b6d3a94b2a4860
    role: context
  - path: data/ingredients/mapped/D-Mannose_6-phosphate_Sodium_Salt.yaml
    sha256: 280c8b5687a3ccd348984cd3b37518d2d1d298a80d1cd0c2b9a911b06f9a0535
    role: context
  - path: data/ingredients/mapped/Locust_Bean_Gum.yaml
    sha256: 973e02f8ba4ad966f8fc9acf5174d47f9aa6cc17c9f45afb632c6e9776276cfd
    role: context
  - path: data/ingredients/mapped/Lysozyme.yaml
    sha256: 797929d4ebcbf1c034daeaf8f45bc28c4de79196fff8e30e926a087f0afdff2f
    role: context
  - path: data/ingredients/mapped/MES_Hydrat.yaml
    sha256: 24292497ec7bae482bb3611b8afb9cd1f795332d655be8900f4c59f8d929ebb6
    role: context
  - path: data/ingredients/mapped/Polymyxin_B.yaml
    sha256: d722a6e60a46c79b843b9a1c539b989d9a066619792dcebaa0167aaab20d5bb2
    role: context
  - path: data/ingredients/mapped/Pretomanid.yaml
    sha256: 7b02eca54a257804e1203999faede7e6fade61657d201fa2fd0f21f1a7ee89af
    role: context
  - path: data/ingredients/mapped/Proteose_Peptone_No_2.yaml
    sha256: 67ca4baee47a98b1ccd293403503a20d1ed757055d179658689f9ab7a6a17533
    role: context
  - path: data/ingredients/mapped/Rabbit_Serum.yaml
    sha256: 031bddb1376c30e284b08ab91209ff3c5465cc5a0b49a82b70a4758aae0a0f7c
    role: context
  - path: data/ingredients/mapped/Rifamycin.yaml
    sha256: 0319c48944ab91a2af53000f5e7488646224cf4683c327a2839ba6d56c8a2a8e
    role: context
  - path: data/ingredients/mapped/Rifamycin_Sv.yaml
    sha256: 7e2cf0690eb1c0e345eed29f9f69a339bb53a5e14f69ebd230c6e86174db77e2
    role: context
  - path: data/ingredients/mapped/Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt.yaml
    sha256: 185d299a1d5a117e5ce42e2826e3f9fb83cba57459c5fc7e09f2dcf263a660f1
    role: context
  - path: data/ingredients/mapped/Sodium_Adipate.yaml
    sha256: 0699b67ffbcc35d3566ff531350c753d93b677718cb4e550bdfa6257ba35886d
    role: context
  - path: data/ingredients/mapped/Sodium_Perchlorate.yaml
    sha256: 5b8a68b008ebce2e98c040b9dfff7b5b16f2370b320bb77cf0d3db32e680e0e0
    role: context
  - path: data/ingredients/mapped/Sorbitan_Monooleate.yaml
    sha256: 09a88638de346c0f2cb44d3c09fd751b03f6266c9abdf7b6b927dec56c17d083
    role: context
  - path: data/ingredients/mapped/Sunflower_Oil.yaml
    sha256: b6c22eaea1a8bd7c243b5eb9da1b4c6c36c6b9de1e3ac25768283684d1dc9e03
    role: context
  - path: data/ingredients/mapped/Sutezolid.yaml
    sha256: 61bda78a8cb9a9d96639219d4ef514a4ed7de658d0fe1b373edf20a9f1cebf7b
    role: context
  - path: data/ingredients/mapped/Tara_Gum.yaml
    sha256: d52f83dbd41f5fac0215e6d47bbf9d9b46ee39aa2a7c78a5552cb7ccdebe693b
    role: context
  - path: data/ingredients/mapped/V-8_Juice.yaml
    sha256: 44229e30128f51e28f1b117122f0f7f6bf405ba52b6b38cf3eaf0a66a129798f
    role: context
  - path: data/ingredients/mapped/Xanthine.yaml
    sha256: c72c948fb793dd36ba53def8a77230d0ac337bec0962369f01c6e29848bccd22
    role: context
  - path: data/ingredients/mapped/Zymosan.yaml
    sha256: a445e9bbdf842cd2a732fd2fe999014ddbffe7b9ace8f6bf0c273d7981f80662
    role: context
  - path: docs/INGREDIENT_BUNDLE.md
    sha256: 356d0bc9e1c7cba37b9770750137cd4fc4e3779ccbfc4edb4c64ea7071697d28
    role: context
  - path: docs/SSSOM_RELEASE.md
    sha256: 7f818575b1afe568b7bf8273b4c89c6e86e2eaed1fda845718157b7c1e8e9ec9
    role: context
  - path: docs/record-review-profile.md
    sha256: da17e2048a13514a422bc94bd2f8d48943cffc5689b96e3f07da26423248d1a7
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: 2f9d651697f2ded0202084d94ee1f402c3d4bdea43c756bc53958299b2774b51
    role: context
  - path: mappings/ingredient_mappings.sssom.tsv
    sha256: a2b83ccdcaad67d89943ccf0f0e30d796cdbc5e418ead247313631b713e89722
    role: target
  - path: mappings/other_cross_record_baseline.tsv
    sha256: 170368983e4105773348122d44da5417745e675dfa9151f72270f19da7a26008
    role: context
  - path: reports/ingredient_bundle_20260924/claims.json
    sha256: 52c5c0e9938725524ed9680c736e1015b74dba1c603c2b76da62b7cc17175a8b
    role: context
  - path: reports/ingredient_bundle_20260924/review-evidence.json
    sha256: 34e8e6575bb4e80fd09234661a0c6a8db0c061d449b9529bb9dd74aad4a4e6d1
    role: context
  - path: reports/ingredient_bundle_20261101/review.json
    sha256: 84e3572174748d0b801c9da8a0f87541cdfbc01756e10b884da6c4fdb9b23260
    role: context
  - path: reports/ingredient_bundle_20261101_followup/dependency-refresh.json
    sha256: f33432a0b360db6eb24e6dba0bfdecba74ae4348adc8c6ca8f7b4c528c73cedf
    role: context
  - path: reports/ingredient_bundle_20261101_followup/prior-review.json
    sha256: 84e3572174748d0b801c9da8a0f87541cdfbc01756e10b884da6c4fdb9b23260
    role: context
  - path: reports/ingredient_bundle_20261101_followup/review.json
    sha256: d391ec9e0dc004494431f76a81c392efef114746e7bf1eca57c7ce4dc7dec14c
    role: target
  - path: reports/semantic_review_20260921/resolution/assertion-dispositions.tsv
    sha256: 55237338c3c788dc7c2cba51cfee4e25b28d428ef166de49ccb047e61f5055ee
    role: context
  - path: reports/semantic_review_20260921/resolution/current-review.json
    sha256: ebc636c818583a687ac6dc54db6393deecbb31a614cf8b0453e01eab448b5d89
    role: context
  - path: reports/semantic_review_20260921/resolution/release-holds.json
    sha256: 4cc32c739edc69521fe26f871cc70511699762de1f555621406057edf1981275
    role: context
  - path: reports/sssom_completion_20260921/assemble_review.py
    sha256: 64d1816c9a299898e1422b01cff5c5707733e96134942937b08be091434f7f91
    role: context
  - path: reports/sssom_completion_20260921/mapping-evidence.json
    sha256: 554206d28461b7dd713da20333c20706c25d6b057d91ad3871aa3bb5025e0ef6
    role: context
  - path: reports/sssom_completion_20260921/mapping_changes/issue1014-provenance-restoration.json
    sha256: fbeec3fbfee71be85541353683df135f96dc1d0021c6bfb3877bcc5eca8813d0
    role: context
  - path: reports/sssom_completion_20260921/mapping_changes/issue669-1003-scoped-alias-corrections.json
    sha256: 00049aa1d2b19565020d4ecbec999fc723d2cf5954968ec6bf5cebdc0da73f34
    role: context
  - path: reports/sssom_completion_20260921/review.json
    sha256: 36a22b230bd9bc4c82a1816438d21e28a0aa2fcf21f21e63cd30b6459bb8d23c
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/.gitattributes
    sha256: e97602ab9cac70102245345c5ab0fc9830df8b17f1072b188265a662a3a547ae
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/audit_targets.py
    sha256: 9719f28aea4d26b65156b9846822201ce0166c05dc7f515d85877ef4060d3803
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/final-replay-receipt.json
    sha256: f0c46615b19bdcad6ea502114c6fea1f05505ecef78ca9d8e0b71e33c014a87c
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-format-check-online.json
    sha256: 218c5b23506a640f3ac5b0a0c781f1b09c082be9e7c3654d54875d9ee1479c4b
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-format-check-online.log
    sha256: 4a5fc18fee2a67ffdccc0e848f94767f7dc9db38e8412be925bcdeaec1d8cae9
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-format-check.json
    sha256: 17ae01957e31f69c14382de24dd46814e6aafb8e91fe88304e30bbb271b17b0e
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-format-check.log
    sha256: 51de76ab79062c49d0e8f86dc0a4d8d179099057d9c7b7471fe652226014c1a8
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-full-format.json
    sha256: fc6328e8826e5668a974b12e7f3c4afa798c642d2bd4d1c8efcde7a542e3f8d1
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-full-format.log
    sha256: d11359bb762585719915d9cf73b2eea8dca135ee78f4bd90fa4f8407ffa05465
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-full-graph.json
    sha256: 5bc376071dd6e191197733270ce3bcc4318757e49736b5dd9d441e87bd4fbd11
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-full-graph.log
    sha256: c0e35108b0df8c8f7c2b311057cad2badd54385fa389b3ba3a4824008ddd8396
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-full-lint.json
    sha256: 684898aafb57aec01bb761f67d807c2435bb77a7f245e643c35cc70df32317e6
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-full-lint.log
    sha256: 82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-full-qc.json
    sha256: 24281111d8565c540df0eaf556b692f223f153f5bd4a9d63a23bb32db8c8404d
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-full-qc.log
    sha256: 8f5177be2974fcf25998666f6a9123a65e2f1de92ef1746ea8e0e02338f29c06
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-full-tests.json
    sha256: f7666606a9c84e37556b1812f4383197df8085854f6e1a452282f82239c1c44f
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-full-tests.log
    sha256: affa913d9c282570a69abeeb526684586864e8653a9cdceebe4a3198130b4580
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-legacy-coverage.json
    sha256: 6e4b0fb634c7b43c74eb2c96a20ceafecd73124a55d25312aabb7b7a37ea9f3e
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-legacy-coverage.log
    sha256: 1517668d86811bbf0c2a3eac591afdeffaf09b2f225312a29a2495c326954f9c
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-package-coverage.json
    sha256: 1ba8344ea8acf4bfe4f40694948269a435d0f2d61c4ec5208add1e9b541965c1
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-package-coverage.log
    sha256: 67646653df9163fe3014eb5737220202a44d88b33eeaedcdd808b36dd5540a70
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-promotion-audit.json
    sha256: 1301d8ddced82d1044645c05b04ed57ba9d49b656761ae1cee94bc078fd04ea8
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-promotion-audit.log
    sha256: 5a87dd1f88018779c25e5acf82c5a31773d7ea5fece4e020be18b1f7970adc30
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-python-lint.json
    sha256: 6262260c0fdb77100788a00d1fd63c9af12095520cc4862000136fe23677bddf
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-python-lint.log
    sha256: 82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-refresh-final-replay.json
    sha256: 39367fcd14f8a6156a7b1dca126da8c4ef1b8ba9f666eaa8a8895f1f3e762b29
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-refresh-final-replay.log
    sha256: 3fbf7141e83e8ec95ff418cc0cc0ce03f9308c45a490585a9640ca16fc314df3
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-refresh-final-tests.json
    sha256: 1e510c983b3db301af353f2e146caf8b6466b9441af64022fa98db92e173af47
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-refresh-final-tests.log
    sha256: 175559255234c45dc574ecfec55cca5a66055fbf24a04576ba8773ec9b933428
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-reviewed-export.json
    sha256: b11a906b3c506c00d1c020408f8ff4551c20044bd5800e0255808e72fa2898ab
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-reviewed-export.log
    sha256: a66626045e4eb717eb204825aff16e29b3de912d11c9e1cecf01bb3dc6524906
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-reviewed-validate.json
    sha256: c56a91e69b0c2ed3eb6fd5c3d383b0a30d5696dde2d14f54f11a2133057b2ff2
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-reviewed-validate.log
    sha256: f5faa6c28be05c18d7be47c6c067a42828331c91043927ddf262f17760858f18
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-semantic-build.json
    sha256: 0e7bd6173eafd6495574313a88170008d79a7717481c2567f1e31334de4fe118
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-semantic-build.log
    sha256: 45227309c3e4b80579e6e6a46a429d26cf6fd2d3ace7e1f1ba28aa63b8fcc16f
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-semantic-integrity.json
    sha256: a2f688b594a356af2479df852a2faea95c63aad5ddfb4b1d5a2798d5be4190b7
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-semantic-integrity.log
    sha256: 90eb85ea6aac322e5f500e252bac25fb0cde9acbc1817fba8d2bd9d0ebfcee81
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-supported-export.json
    sha256: 80c3b45eb16e340dccb4a5ccd563a636191943836bedd56a1cd7c51fd1536cd8
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-supported-export.log
    sha256: 99b23ef78d62cb2caabc6b3f70cb31889213a4bc4a73a766314b76acca2e2013
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-supported-validate.json
    sha256: 6a5e6d9c9075a3fc045c9a7ae8c83cae476d171ec109800d85312ea9d9a4df88
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-supported-validate.log
    sha256: afdef6db20674d2a32fd778f72d78356e71850824c2fbd29889d4a1638fab428
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-typecheck-final.json
    sha256: 3586ec138aed6d350b22d1a60177b1ba8253766fbb21c585d1f473d71bb86a91
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-typecheck-final.log
    sha256: 0f0451a70963ae73be675ad208919e74e8bf1cfecdd4689aabe892085d717fc7
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-typecheck-overlay.json
    sha256: 1fee4a54cf1d029a991682bcb3ddd55d5e9fa02fab7e5ea5b8f95b8c911e6da0
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-typecheck-overlay.log
    sha256: 95bebd47e118e67d42264c8c40163e9f8b2a051b1e026072f79edd8a76d2e3cd
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-typecheck.json
    sha256: a12cc75f1a5b4fc2d9f103e0d6e02f546cd9caa38acb5a76b6bd2669f34a75b2
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-typecheck.log
    sha256: 3d26669326245155efb2d0e7a3122c10a91a8e45342124cb838a99ab550fea31
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup1014-apply.json
    sha256: 28d40fd1b9fb33815611c2c295d48008e62d40dc5c9f6ca563fdd0bbc51d31f4
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup1014-apply.log
    sha256: b98a526c0b90cfabcaf2985f2a94ca706f24d610ea50f37ad32aeaa8d8425840
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup1014-assemble-check.json
    sha256: e39a0be7a4228799b0d33e353ea89baa4f1798ba84ae2ecb601a27b8739a9408
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup1014-assemble-check.log
    sha256: 710484b8faef7b4592edeb4f762119c2b8f7863c30a31709de9f808a75ae599e
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup1014-assemble.json
    sha256: 026b39f150ebc504c0f266f70f19ad163467f9dac7275c6cac1aad8ad64bef30
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup1014-assemble.log
    sha256: 74bcf3a43bd46c4741e54693e9db8208148c16f2ff3ff54a6e60890c31703c2c
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup1014-receipt.json
    sha256: d6040b94089405e71508f510f6533013838a193ea23f2d590e83f05167472f71
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup1014-receipt.log
    sha256: 2262a693f8ba71f056e816a758cc1cb645407ec23c17d4bfa0aca5e330156453
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup1014-ruff-offline.json
    sha256: 4b82241fb3b803bd35d21dac879b5505da205882b201508b71ef2496d77f2542
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup1014-ruff-offline.log
    sha256: 82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup1014-ruff.json
    sha256: 5717362372b4b6d33e4636b5a276194b97764103e4df0ef1f8b4dd3e5f7cb447
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup1014-ruff.log
    sha256: ab960078234ac3697fb507c8fdadea23ac7e81c44106a364eadf43bd5b0a42b6
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup1014-tests.json
    sha256: b11128dea83c15419cb1ea1cf5556548d188b6766d0648671bc8c026915a3cde
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup1014-tests.log
    sha256: 393293b479e82097aa9f94cde722e6d3874ae866a0a54dae74acf04f75bfb8d1
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup_native_target_audit.json
    sha256: c5299b28eafe143f15e5b87d0287e1bcd41adb3c4b9d056e8efb84eb4c9586ba
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup_native_target_audit.log
    sha256: d1d4e80ee60cddd22ad7817867f37fbce6d16c02790d30da9455fb88247cc408
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/inspection-initial.json
    sha256: 49f2376475cd4af86e110dd08675a4fd0a5f6478d7a4036a46f73efaee7d13ea
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/issue1015_green.json
    sha256: 2b11884e34239e4c99375057a5e0b95c989fb260587855cf818a4bb2fa83c70e
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/issue1015_green.log
    sha256: 1af1478405cd59061cad7ba41ad454f3b14435eceafc02f68e12ef14d68d2401
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/issue1015_lint.json
    sha256: 3b3d6324c18b073c72bad52b0cf63d902fec9439602601c3a62baa9b22594d9e
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/issue1015_lint.log
    sha256: 82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/issue1015_red.json
    sha256: 304d140b1face45dce34c3d47442bd58b62e92314e6034b380ae02f94b129869
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/issue1015_red.log
    sha256: 1bf14d75079a06e6ba64e079be2efa26aa67796ce6817c08c7d2a89ea15a4179
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/issue1017_receipt_suite.json
    sha256: 11a84af1022ba93e1b283cc94ede966510df6c2d6a48d2d6ee04d16fc8130f89
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/issue1017_receipt_suite.log
    sha256: 4157a126f35629a82329961a3bce5a8927ef0fab56d0ccafaf7652f932008206
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/issue1017_regression_green.json
    sha256: 41932db23d7ddd83a5a0b8441a170c20e75b77f163fcfd73e4a2791f61f18bae
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/issue1017_regression_green.log
    sha256: e78ec817b39f99132ad170284772c2f3486c56d06e8a8d87a867ba272bba7a5e
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/issue1017_regression_red.json
    sha256: 7b3878c2bf73debdcdb71cc1df4bf37e7c13c6e243bb6666fe543c21759938fd
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/issue1017_regression_red.log
    sha256: af5c1897d4a9bbbbc933a4dcc650fd072a01cf29bfa5ef387054d4e1218d8190
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/issue1018_receipt_green.json
    sha256: 576b23c9b814ce51e71c6f07937b890b885ff05e6446b69fbfcc62da40da5ee0
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/issue1018_receipt_green.log
    sha256: 04e179c1859d0c7c3e60d480ef38c6f12eb8b86fb1b007a152873d03bf009071
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/issue1018_receipt_lint.json
    sha256: f07c2e70862f97bf8e4d6dbd4b094ee781a05d5b1d4996261e68408fc62609b1
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/issue1018_receipt_lint.log
    sha256: 82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/issue1018_receipt_red.json
    sha256: d1c22a8512dda864b48e42e829aa1997fa96bb3271f17bafa412524011e5ae3c
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/issue1018_receipt_red.log
    sha256: 717826029b3555c36f5732a3527d0de63146167b7ee33229b06e16e42d6dad6d
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/output-reservation-symlink-race.json
    sha256: 48ebd7a6865726365f81d5d77fa38c63cdb730f3cd0a3769f0b76dd6c719915c
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/provenance-restoration.json
    sha256: cae4ebdac309dd94f6d19de1ada7049ad03a9cf50cea05c843641a85f0b5c412
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/ready-candidate-drift.json
    sha256: 2429604ab6b30758b72696906bcc2a341cacb8d1a01a9047409cb360a82fd4d1
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/ready-promotion-row-delta.json
    sha256: 69d2a453fe537f36d217f500f7ba01f13b51e947fe2b9a52c1e80221a16f3093
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/ready-promotion-summary.json
    sha256: 5a87dd1f88018779c25e5acf82c5a31773d7ea5fece4e020be18b1f7970adc30
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/receipt-reservation-cleanup-fixed.json
    sha256: f294d1fb36fa1460cdbf3fb88058d61f5ca897d5ef3ea96b73fadf4839bdc0bb
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/receipt-reservation-cleanup-race.json
    sha256: 527537c521b87604ed2cf4770a9c6bf2b5817988c63bc3bb6fc11da007c887d7
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/reservation-reprobe-firstfix.json
    sha256: 2b137b18e89e521fce359492820a4abcccf673e32ca6ab7a74e0230f2141c97c
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/target-audit.json
    sha256: 10b20a6045105ee22fced93eff91f8b17c78622fb0292ce8e4b198cd0972b482
    role: context
  - path: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/verification.json
    sha256: 033101ebd357aec04d240249dee2f4d54a4c463b1824b41aa1320f571faf60a6
    role: context
  - path: scripts/refresh_unchanged_cohort.py
    sha256: 40d29bc094aa20fd8d1c4501a30bf5f754e4bc23247762df53ada5541068ecdf
    role: context
  - path: scripts/restore_carnitine_mapping_provenance.py
    sha256: 0284caea353d355ea341344201902dac8029c19df9fb027d3595ae2159ea1d9d
    role: context
  - path: scripts/retire_reviewed_generated_aliases.py
    sha256: e3192528e66ad0f671ce1ea3d9ee7dc620110df8fab7b057f7b465fc9302d88c
    role: context
  - path: src/mediaingredientmech/curate/apply_receipt.py
    sha256: 6c7c613a1a9c2211c68b20a2483e99009c34fd908c9bf3b3acbac63eedb72a3f
    role: context
  - path: src/mediaingredientmech/export/reviewed_sssom.py
    sha256: ab74bae77709ba59623b2aa4612a16b692361c4f46bbb9b5a597f31bd6716ec3
    role: context
  - path: src/mediaingredientmech/ingredient_bundle_contract.py
    sha256: 9285d9d2423d108e0b1e3a960ddcbdd5e9b94eb44e099632042fc7e1e95e51b2
    role: context
  - path: src/mediaingredientmech/ingredient_bundle_refresh.py
    sha256: a86dd3995bc47ab053f372cdff5251e6d53e8c10f9aa433d631920b6941d4acb
    role: context
  - path: src/mediaingredientmech/profiles/ingredient_bundle_v1.schema.json
    sha256: c0faabc0870bdcb3f03847f5e6597bbe4e245ccc775fc398f536c7c3f0ea4ab2
    role: context
  - path: src/mediaingredientmech/profiles/ingredient_scope_v1.yaml
    sha256: dd2f78e6b6fcbdf8a715bebcec14e0f86c1e431bf28e5b9d7f3524a62e5bce3a
    role: context
  - path: src/mediaingredientmech/schema/mediaingredientmech.yaml
    sha256: bb43dee29b21fdee72a48022456e733e49e95824c4c09674f9b3165c290fe012
    role: context
  - path: src/mediaingredientmech/validation/semantic_release.py
    sha256: 0490b67b9304114ad78ef429ff619268207a39665fd296997fd43d4c64febd90
    role: context
  - path: tests/test_curation_receipt_collisions.py
    sha256: a11c251918f21d5d418cf1e443068adb1cb5638faabffca10b430e461738ef12
    role: context
  - path: tests/test_ingredient_bundle.py
    sha256: cefc4dba1ba84b61c134575321e7dc4ee8d9d5e7307931b40a0a56545a13e2d1
    role: context
  - path: tests/test_ingredient_bundle_dependency_refresh.py
    sha256: 024e7630836c23d9d37f1ac215a54ad857084bac0b12c5241f4ad1b291dedc0a
    role: context
  - path: tests/test_mapping_change_receipt.py
    sha256: 1a85144205f790ecd1a8fe7de84c8233e7baf1b48a002573bbf0e7e5da6f2208
    role: context
  - path: tests/test_reject_carnitinamide_synonym.py
    sha256: c6afca04719ac2b720428f6687c2ae796ba5345769ad624e49c55698155c5c64
    role: context
  - path: tests/test_restore_carnitine_mapping_provenance.py
    sha256: c78d71fa878af7da8d4d23322aa6eed2a714174a2a6b12ec6981724885b18767
    role: context
  - path: tests/test_retire_reviewed_generated_aliases.py
    sha256: 5d54eb7819b271d3426edbef61e45c7a495afa31c4cf9bf1d40f8f95ba534390
    role: context
  - path: workflow/mech-workflow.yaml
    sha256: 45d7c23d67f490cea6b31e336e5d2ac98b7ce8fa4e791bd9d3be092cfdb5a10d
    role: context
targets:
- target_id: canonical
  path: mappings/ingredient_mappings.sssom.tsv
  label: Canonical SSSOM after the bounded source/comment restoration
  kind: generated
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Maintained ingredient owners; science unchanged by this follow-up
  - repository: CultureBotAI/MediaIngredientMech
    path: scripts/restore_carnitine_mapping_provenance.py
    role: Guarded restoration of exact historical carnitine provenance cells
  - repository: CultureBotAI/MediaIngredientMech
    path: scripts/retire_reviewed_generated_aliases.py
    role: Guarded seven-alias retirement with exclusive evidence reservations
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_mim_ingredient_sssom.py
    role: External native generator for the earlier diagnostic; not rerun or broadly
      promoted in this follow-up
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Carnitine_Hydrochloride.yaml
    role: Exact maintained owner of a bounded row correction in receipt 14; unchanged
      by this follow-up
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.yaml
    role: Exact maintained owner of a bounded row correction in receipt 14; unchanged
      by this follow-up
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/84_GL_NaHCO3_Solution.yaml
    role: Exact maintained owner of a bounded row correction in receipt 14; unchanged
      by this follow-up
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Betaine_Hydrochloride.yaml
    role: Exact maintained owner of a bounded row correction in receipt 14; unchanged
      by this follow-up
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-Mannose_6-phosphate_Sodium_Salt.yaml
    role: Exact maintained owner of a bounded row correction in receipt 14; unchanged
      by this follow-up
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/MES_Hydrat.yaml
    role: Exact maintained owner of a bounded row correction in receipt 14; unchanged
      by this follow-up
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt.yaml
    role: Exact maintained owner of a bounded row correction in receipt 14; unchanged
      by this follow-up
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_Perchlorate.yaml
    role: Exact maintained owner of a bounded row correction in receipt 14; unchanged
      by this follow-up
- target_id: companion
  path: reports/ingredient_bundle_20261101_followup/review.json
  label: Dependency-only companion successor retaining the selected claims and owners
  kind: generated
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: reports/ingredient_bundle_20260924/claims.json
    role: Frozen selected scientific claims; actual owner paths are hash-bound in
      record_inputs
  - repository: CultureBotAI/MediaIngredientMech
    path: reports/ingredient_bundle_20261101/review.json
    role: Immutable prior companion decisions and owner hashes
  - repository: CultureBotAI/MediaIngredientMech
    path: scripts/refresh_unchanged_cohort.py
    role: Maintained explicit-baseline CLI
  - repository: CultureBotAI/MediaIngredientMech
    path: src/mediaingredientmech/ingredient_bundle_refresh.py
    role: Cohort equivalence proof and exclusive immutable output publisher
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Acriflavine.yaml
    role: Exact maintained owner, byte-identical to the prior companion
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Anabasine_Hydrochloride.yaml
    role: Exact maintained owner, byte-identical to the prior companion
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bovine_Serum_Albumin.yaml
    role: Exact maintained owner, byte-identical to the prior companion
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cotarnine_Chloride.yaml
    role: Exact maintained owner, byte-identical to the prior companion
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Locust_Bean_Gum.yaml
    role: Exact maintained owner, byte-identical to the prior companion
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Lysozyme.yaml
    role: Exact maintained owner, byte-identical to the prior companion
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Polymyxin_B.yaml
    role: Exact maintained owner, byte-identical to the prior companion
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Pretomanid.yaml
    role: Exact maintained owner, byte-identical to the prior companion
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Proteose_Peptone_No_2.yaml
    role: Exact maintained owner, byte-identical to the prior companion
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Rabbit_Serum.yaml
    role: Exact maintained owner, byte-identical to the prior companion
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Rifamycin.yaml
    role: Exact maintained owner, byte-identical to the prior companion
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Rifamycin_Sv.yaml
    role: Exact maintained owner, byte-identical to the prior companion
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_Adipate.yaml
    role: Exact maintained owner, byte-identical to the prior companion
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sorbitan_Monooleate.yaml
    role: Exact maintained owner, byte-identical to the prior companion
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sunflower_Oil.yaml
    role: Exact maintained owner, byte-identical to the prior companion
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sutezolid.yaml
    role: Exact maintained owner, byte-identical to the prior companion
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Tara_Gum.yaml
    role: Exact maintained owner, byte-identical to the prior companion
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/V-8_Juice.yaml
    role: Exact maintained owner, byte-identical to the prior companion
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Xanthine.yaml
    role: Exact maintained owner, byte-identical to the prior companion
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Zymosan.yaml
    role: Exact maintained owner, byte-identical to the prior companion
scope:
  description: Mechanical integrity and preservation of two exact generated outputs
    after issues 1012-1018; source/comment restoration and dependency-only successor
    generation.
  selection: Canonical SSSOM and the new follow-up companion review only. All rows/decisions
    of those artifacts are compared; scientific correctness of every original claim
    is not reassessed.
  coverage: full
  population_size: 2
  reviewed_target_ids:
  - canonical
  - companion
  exclusions:
  - target: New chemical, role, component or identifier approval
    reason: This deterministic/provenance assessment does not repeat literature review
      or clear any scientific holds.
  - target: Whole raw diagnostic promotion or unified mapping rebuild
    reason: The diagnostic candidate is unpromoted; only bounded previously adjudicated
      corrections and restored provenance are maintained.
  - target: Independent final-head approval
    reason: A separate reviewer assesses the final committed head; this bundle is
      explicitly author review.
checks:
- check_id: followup_native_target_audit
  name: followup native target audit
  required: true
  target_ids:
  - canonical
  - companion
  status: passed
  summary: Exact row, receipt, selected-claim, owner and protected-file comparison
    passes.
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && python3 ../followup-1012-1017/native-review/audit_targets.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - followup_native_target_audit
  - followup_native_target_audit-receipt
  scope_note: Re-read this completed run and verified its log SHA256; run time remains
    in the command receipt.
- check_id: followup-full-qc
  name: followup full qc
  required: true
  target_ids:
  - canonical
  status: passed
  summary: Full just qc passes; native A/B1/B2/B3/B5/C/D/E/F/G/H/I/J/K/L invariants
    have zero rejects. Native B4 skips absent sibling transforms.
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && just qc
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - followup-full-qc
  - followup-full-qc-receipt
  scope_note: Re-read this completed run and verified its log SHA256; run time remains
    in the command receipt.
- check_id: followup1014-assemble-check
  name: followup1014 assemble check
  required: true
  target_ids:
  - canonical
  status: passed
  summary: Complete native mapping review reproduces the restored source bytes and
    receipt chain.
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && uv run python reports/sssom_completion_20260921/assemble_review.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - followup1014-assemble-check
  - followup1014-assemble-check-receipt
  scope_note: Re-read this completed run and verified its log SHA256; run time remains
    in the command receipt.
- check_id: followup-semantic-build
  name: followup semantic build
  required: true
  target_ids:
  - canonical
  status: passed
  summary: Native semantic builder completes; global scientific result remains FAIL
    with 1,733 findings / 2,272 assertions.
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && uv run python reports/semantic_review_20260921/resolution/build_review.py --bundle
    output/mim-kgx-710-full
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - followup-semantic-build
  - followup-semantic-build-receipt
  scope_note: Re-read this completed run and verified its log SHA256; run time remains
    in the command receipt.
- check_id: followup-semantic-integrity
  name: followup semantic integrity
  required: true
  target_ids:
  - canonical
  status: passed
  summary: Native semantic integrity passes without changing the separate global scientific
    FAIL verdict.
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && uv run python -m mediaingredientmech.validation.semantic_release --root . --report
    reports/semantic_review_20260921/resolution/current-review.json
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - followup-semantic-integrity
  - followup-semantic-integrity-receipt
  scope_note: Re-read this completed run and verified its log SHA256; run time remains
    in the command receipt.
- check_id: followup-supported-export
  name: followup supported export
  required: true
  target_ids:
  - canonical
  status: passed
  summary: Supported KGX export completes for the already approved subset; backlog
    remains separate.
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && just export-supported-kgx reports/semantic_review_20260921/resolution/current-review.json
    output/mim-supported-1014
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - followup-supported-export
  - followup-supported-export-receipt
  scope_note: Re-read this completed run and verified its log SHA256; run time remains
    in the command receipt.
- check_id: followup-supported-validate
  name: followup supported validate
  required: true
  target_ids:
  - canonical
  status: passed
  summary: 'Supported graph integrity passes: 1,740 SSSOM rows / 2,220 approved edges;
    2,272 excluded assertions remain.'
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && just qc-supported-kgx reports/semantic_review_20260921/resolution/current-review.json
    output/mim-supported-1014
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - followup-supported-validate
  - followup-supported-validate-receipt
  scope_note: Re-read this completed run and verified its log SHA256; run time remains
    in the command receipt.
- check_id: followup-reviewed-export
  name: followup reviewed export
  required: true
  target_ids:
  - canonical
  status: passed
  summary: Reviewed SSSOM exporter preserves the 1,740 SUPPORTED / 1,247 WITHHOLD
    partition.
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && just export-reviewed-sssom reports/sssom_completion_20260921/review.json output/mim-reviewed-1014
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - followup-reviewed-export
  - followup-reviewed-export-receipt
  scope_note: Re-read this completed run and verified its log SHA256; run time remains
    in the command receipt.
- check_id: followup-reviewed-validate
  name: followup reviewed validate
  required: true
  target_ids:
  - canonical
  status: passed
  summary: Native reviewed-export integrity and schema validation pass for both partitions.
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && just qc-reviewed-sssom reports/sssom_completion_20260921/review.json output/mim-reviewed-1014
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - followup-reviewed-validate
  - followup-reviewed-validate-receipt
  scope_note: Re-read this completed run and verified its log SHA256; run time remains
    in the command receipt.
- check_id: followup-refresh-final-tests
  name: followup refresh final tests
  required: true
  target_ids:
  - companion
  status: passed
  summary: 82 current companion refresh and consumer tests pass, including changed-data
    refusals, dates, symlink paths and reservation races.
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && uv run python -m pytest -o addopts= tests/test_ingredient_bundle_dependency_refresh.py
    tests/test_ingredient_bundle.py -q
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - followup-refresh-final-tests
  - followup-refresh-final-tests-receipt
  scope_note: Re-read this completed run and verified its log SHA256; run time remains
    in the command receipt.
- check_id: followup-refresh-final-replay
  name: followup refresh final replay
  required: true
  target_ids:
  - companion
  status: passed
  summary: 'Current maintained producer reproduces the successor bytes exactly: d391ec9e0dc004494431f76a81c392efef114746e7bf1eca57c7ce4dc7dec14c.'
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && uv run python scripts/refresh_unchanged_cohort.py --baseline 612860e467aff74ecc1339df7c3c32b1bf940b95
    --prior-review reports/ingredient_bundle_20261101/review.json --output ../followup-1012-1017/final-replay-review.json
    --receipt ../followup-1012-1017/final-replay-receipt.json --prior-copy ../followup-1012-1017/final-replay-prior.json
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - followup-refresh-final-replay
  - followup-refresh-final-replay-receipt
  scope_note: Re-read this completed run and verified its log SHA256; run time remains
    in the command receipt.
- check_id: issue1018_receipt_green
  name: issue1018 receipt green
  required: true
  target_ids:
  - canonical
  status: passed
  summary: 64 focused compatibility and collision tests pass, including no-source-write
    failure/successful-late-open replacement races.
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && uv run pytest -q --no-cov tests/test_retire_reviewed_generated_aliases.py tests/test_curation_receipt_collisions.py
    tests/test_reject_carnitinamide_synonym.py tests/test_restore_carnitine_mapping_provenance.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - issue1018_receipt_green
  - issue1018_receipt_green-receipt
  scope_note: Re-read this completed run and verified its log SHA256; run time remains
    in the command receipt.
- check_id: issue1017_receipt_suite
  name: issue1017 receipt suite
  required: true
  target_ids:
  - canonical
  status: passed
  summary: Native mapping receipt and assembler regression suite passes; coexisting
    synonym/mapping-change evidence survives.
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && python -m pytest tests/test_mapping_change_receipt.py tests/test_mapping_followup.py
    tests/test_record_refresh.py --no-cov -q
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - issue1017_receipt_suite
  - issue1017_receipt_suite-receipt
  scope_note: Re-read this completed run and verified its log SHA256; run time remains
    in the command receipt.
- check_id: followup-typecheck-final
  name: followup typecheck final
  required: true
  target_ids:
  - canonical
  - companion
  status: passed
  summary: Maintained package type check passes for 52 source files.
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && uv run --offline --with mypy==1.19.1 mypy src/mediaingredientmech
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - followup-typecheck-final
  - followup-typecheck-final-receipt
  scope_note: Re-read this completed run and verified its log SHA256; run time remains
    in the command receipt.
- check_id: followup-python-lint
  name: followup python lint
  required: true
  target_ids:
  - canonical
  - companion
  status: passed
  summary: Ruff passes for maintained producer, guards, assembler and changed tests.
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && uvx --offline ruff check src/mediaingredientmech/ingredient_bundle_refresh.py
    src/mediaingredientmech/curate/apply_receipt.py scripts/refresh_unchanged_cohort.py
    scripts/restore_carnitine_mapping_provenance.py scripts/retire_reviewed_generated_aliases.py
    reports/sssom_completion_20260921/assemble_review.py tests/test_ingredient_bundle_dependency_refresh.py
    tests/test_ingredient_bundle.py tests/test_restore_carnitine_mapping_provenance.py
    tests/test_retire_reviewed_generated_aliases.py tests/test_mapping_change_receipt.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - followup-python-lint
  - followup-python-lint-receipt
  scope_note: Re-read this completed run and verified its log SHA256; run time remains
    in the command receipt.
- check_id: followup-format-check-online
  name: followup format check online
  required: true
  target_ids:
  - canonical
  - companion
  status: passed
  summary: Black check passes for the two changed maintained package modules.
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && uvx black --check src/mediaingredientmech/ingredient_bundle_refresh.py src/mediaingredientmech/curate/apply_receipt.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - followup-format-check-online
  - followup-format-check-online-receipt
  scope_note: Re-read this completed run and verified its log SHA256; run time remains
    in the command receipt.
- check_id: followup-full-lint
  name: followup full lint
  required: true
  target_ids:
  - canonical
  - companion
  status: passed
  summary: Ruff passes for the full maintained package.
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && uvx --offline ruff check src/mediaingredientmech
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - followup-full-lint
  - followup-full-lint-receipt
  scope_note: Re-read this completed run and verified its log SHA256; run time remains
    in the command receipt.
- check_id: followup-full-format
  name: followup full format
  required: true
  target_ids:
  - canonical
  - companion
  status: passed
  summary: Black check passes for the full maintained package.
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && uvx --offline black --check src/mediaingredientmech
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - followup-full-format
  - followup-full-format-receipt
  scope_note: Re-read this completed run and verified its log SHA256; run time remains
    in the command receipt.
- check_id: followup-package-coverage
  name: followup package coverage
  required: true
  target_ids:
  - canonical
  - companion
  status: passed
  summary: Maintained package coverage is 71%, exceeding the actual 35% gate; this
    is distinct from the whole package-plus-script aggregate.
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && uv run --offline --with pytest --with pytest-cov coverage report '--include=src/mediaingredientmech/*'
    --fail-under=35
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - followup-package-coverage
  - followup-package-coverage-receipt
  scope_note: Re-read this completed run and verified its log SHA256; run time remains
    in the command receipt.
- check_id: followup-full-tests
  name: followup full tests
  required: true
  target_ids:
  - canonical
  - companion
  status: passed
  summary: 'Complete repository pytest suite passes: 3,276 passed, 6 skipped, 32 warnings.
    A non-executable annotation added during the run is separately covered by the
    final 82-test bundle suite, mypy and byte-identical replay.'
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && env -u MEDIAINGREDIENTMECH_ROOT -u CULTUREMECH_ROOT -u KGMICROBE_ROOT -u CLAW_ROOT
    -u CLAW_SRC -u OPENCLAW_ORCHESTRATION_ROOT -u OPENCLAW_WORKSPACE RECORD_REVIEW_BASE=4625afd492b6cf43e3b499d1425d2453d490009d
    uv run --with pytest --with pytest-cov pytest
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - followup-full-tests
  - followup-full-tests-receipt
  scope_note: Re-read this completed run and verified its log SHA256; run time remains
    in the command receipt.
evidence:
- evidence_id: followup_native_target_audit
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup_native_target_audit.log
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: supports
  summary: Exact row, receipt, selected-claim, owner and protected-file comparison
    passes.
  snapshot_sha256: d1d4e80ee60cddd22ad7817867f37fbce6d16c02790d30da9455fb88247cc408
- evidence_id: followup_native_target_audit-receipt
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup_native_target_audit.json
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: context_only
  summary: Actual command, working directory, start/finish, exit and original log
    hash.
  snapshot_sha256: c5299b28eafe143f15e5b87d0287e1bcd41adb3c4b9d056e8efb84eb4c9586ba
- evidence_id: followup-full-qc
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-full-qc.log
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: supports
  summary: Full just qc passes; native A/B1/B2/B3/B5/C/D/E/F/G/H/I/J/K/L invariants
    have zero rejects. Native B4 skips absent sibling transforms.
  snapshot_sha256: 8f5177be2974fcf25998666f6a9123a65e2f1de92ef1746ea8e0e02338f29c06
- evidence_id: followup-full-qc-receipt
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-full-qc.json
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: context_only
  summary: Actual command, working directory, start/finish, exit and original log
    hash.
  snapshot_sha256: 24281111d8565c540df0eaf556b692f223f153f5bd4a9d63a23bb32db8c8404d
- evidence_id: followup1014-assemble-check
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup1014-assemble-check.log
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: supports
  summary: Complete native mapping review reproduces the restored source bytes and
    receipt chain.
  snapshot_sha256: 710484b8faef7b4592edeb4f762119c2b8f7863c30a31709de9f808a75ae599e
- evidence_id: followup1014-assemble-check-receipt
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup1014-assemble-check.json
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: context_only
  summary: Actual command, working directory, start/finish, exit and original log
    hash.
  snapshot_sha256: e39a0be7a4228799b0d33e353ea89baa4f1798ba84ae2ecb601a27b8739a9408
- evidence_id: followup-semantic-build
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-semantic-build.log
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: supports
  summary: Native semantic builder completes; global scientific result remains FAIL
    with 1,733 findings / 2,272 assertions.
  snapshot_sha256: 45227309c3e4b80579e6e6a46a429d26cf6fd2d3ace7e1f1ba28aa63b8fcc16f
- evidence_id: followup-semantic-build-receipt
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-semantic-build.json
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: context_only
  summary: Actual command, working directory, start/finish, exit and original log
    hash.
  snapshot_sha256: 0e7bd6173eafd6495574313a88170008d79a7717481c2567f1e31334de4fe118
- evidence_id: followup-semantic-integrity
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-semantic-integrity.log
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: supports
  summary: Native semantic integrity passes without changing the separate global scientific
    FAIL verdict.
  snapshot_sha256: 90eb85ea6aac322e5f500e252bac25fb0cde9acbc1817fba8d2bd9d0ebfcee81
- evidence_id: followup-semantic-integrity-receipt
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-semantic-integrity.json
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: context_only
  summary: Actual command, working directory, start/finish, exit and original log
    hash.
  snapshot_sha256: a2f688b594a356af2479df852a2faea95c63aad5ddfb4b1d5a2798d5be4190b7
- evidence_id: followup-supported-export
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-supported-export.log
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: supports
  summary: Supported KGX export completes for the already approved subset; backlog
    remains separate.
  snapshot_sha256: 99b23ef78d62cb2caabc6b3f70cb31889213a4bc4a73a766314b76acca2e2013
- evidence_id: followup-supported-export-receipt
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-supported-export.json
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: context_only
  summary: Actual command, working directory, start/finish, exit and original log
    hash.
  snapshot_sha256: 80c3b45eb16e340dccb4a5ccd563a636191943836bedd56a1cd7c51fd1536cd8
- evidence_id: followup-supported-validate
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-supported-validate.log
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: supports
  summary: 'Supported graph integrity passes: 1,740 SSSOM rows / 2,220 approved edges;
    2,272 excluded assertions remain.'
  snapshot_sha256: afdef6db20674d2a32fd778f72d78356e71850824c2fbd29889d4a1638fab428
- evidence_id: followup-supported-validate-receipt
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-supported-validate.json
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: context_only
  summary: Actual command, working directory, start/finish, exit and original log
    hash.
  snapshot_sha256: 6a5e6d9c9075a3fc045c9a7ae8c83cae476d171ec109800d85312ea9d9a4df88
- evidence_id: followup-reviewed-export
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-reviewed-export.log
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: supports
  summary: Reviewed SSSOM exporter preserves the 1,740 SUPPORTED / 1,247 WITHHOLD
    partition.
  snapshot_sha256: a66626045e4eb717eb204825aff16e29b3de912d11c9e1cecf01bb3dc6524906
- evidence_id: followup-reviewed-export-receipt
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-reviewed-export.json
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: context_only
  summary: Actual command, working directory, start/finish, exit and original log
    hash.
  snapshot_sha256: b11a906b3c506c00d1c020408f8ff4551c20044bd5800e0255808e72fa2898ab
- evidence_id: followup-reviewed-validate
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-reviewed-validate.log
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: supports
  summary: Native reviewed-export integrity and schema validation pass for both partitions.
  snapshot_sha256: f5faa6c28be05c18d7be47c6c067a42828331c91043927ddf262f17760858f18
- evidence_id: followup-reviewed-validate-receipt
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-reviewed-validate.json
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: context_only
  summary: Actual command, working directory, start/finish, exit and original log
    hash.
  snapshot_sha256: c56a91e69b0c2ed3eb6fd5c3d383b0a30d5696dde2d14f54f11a2133057b2ff2
- evidence_id: followup-refresh-final-tests
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-refresh-final-tests.log
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: supports
  summary: 82 current companion refresh and consumer tests pass, including changed-data
    refusals, dates, symlink paths and reservation races.
  snapshot_sha256: 175559255234c45dc574ecfec55cca5a66055fbf24a04576ba8773ec9b933428
- evidence_id: followup-refresh-final-tests-receipt
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-refresh-final-tests.json
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: context_only
  summary: Actual command, working directory, start/finish, exit and original log
    hash.
  snapshot_sha256: 1e510c983b3db301af353f2e146caf8b6466b9441af64022fa98db92e173af47
- evidence_id: followup-refresh-final-replay
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-refresh-final-replay.log
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: supports
  summary: 'Current maintained producer reproduces the successor bytes exactly: d391ec9e0dc004494431f76a81c392efef114746e7bf1eca57c7ce4dc7dec14c.'
  snapshot_sha256: 3fbf7141e83e8ec95ff418cc0cc0ce03f9308c45a490585a9640ca16fc314df3
- evidence_id: followup-refresh-final-replay-receipt
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-refresh-final-replay.json
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: context_only
  summary: Actual command, working directory, start/finish, exit and original log
    hash.
  snapshot_sha256: 39367fcd14f8a6156a7b1dca126da8c4ef1b8ba9f666eaa8a8895f1f3e762b29
- evidence_id: issue1018_receipt_green
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/issue1018_receipt_green.log
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: supports
  summary: 64 focused compatibility and collision tests pass, including no-source-write
    failure/successful-late-open replacement races.
  snapshot_sha256: 04e179c1859d0c7c3e60d480ef38c6f12eb8b86fb1b007a152873d03bf009071
- evidence_id: issue1018_receipt_green-receipt
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/issue1018_receipt_green.json
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: context_only
  summary: Actual command, working directory, start/finish, exit and original log
    hash.
  snapshot_sha256: 576b23c9b814ce51e71c6f07937b890b885ff05e6446b69fbfcc62da40da5ee0
- evidence_id: issue1017_receipt_suite
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/issue1017_receipt_suite.log
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: supports
  summary: Native mapping receipt and assembler regression suite passes; coexisting
    synonym/mapping-change evidence survives.
  snapshot_sha256: 4157a126f35629a82329961a3bce5a8927ef0fab56d0ccafaf7652f932008206
- evidence_id: issue1017_receipt_suite-receipt
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/issue1017_receipt_suite.json
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: context_only
  summary: Actual command, working directory, start/finish, exit and original log
    hash.
  snapshot_sha256: 11a84af1022ba93e1b283cc94ede966510df6c2d6a48d2d6ee04d16fc8130f89
- evidence_id: followup-typecheck-final
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-typecheck-final.log
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: supports
  summary: Maintained package type check passes for 52 source files.
  snapshot_sha256: 0f0451a70963ae73be675ad208919e74e8bf1cfecdd4689aabe892085d717fc7
- evidence_id: followup-typecheck-final-receipt
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-typecheck-final.json
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: context_only
  summary: Actual command, working directory, start/finish, exit and original log
    hash.
  snapshot_sha256: 3586ec138aed6d350b22d1a60177b1ba8253766fbb21c585d1f473d71bb86a91
- evidence_id: followup-python-lint
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-python-lint.log
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: supports
  summary: Ruff passes for maintained producer, guards, assembler and changed tests.
  snapshot_sha256: 82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18
- evidence_id: followup-python-lint-receipt
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-python-lint.json
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: context_only
  summary: Actual command, working directory, start/finish, exit and original log
    hash.
  snapshot_sha256: 6262260c0fdb77100788a00d1fd63c9af12095520cc4862000136fe23677bddf
- evidence_id: followup-format-check-online
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-format-check-online.log
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: supports
  summary: Black check passes for the two changed maintained package modules.
  snapshot_sha256: 4a5fc18fee2a67ffdccc0e848f94767f7dc9db38e8412be925bcdeaec1d8cae9
- evidence_id: followup-format-check-online-receipt
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-format-check-online.json
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: context_only
  summary: Actual command, working directory, start/finish, exit and original log
    hash.
  snapshot_sha256: 218c5b23506a640f3ac5b0a0c781f1b09c082be9e7c3654d54875d9ee1479c4b
- evidence_id: followup-full-lint
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-full-lint.log
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: supports
  summary: Ruff passes for the full maintained package.
  snapshot_sha256: 82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18
- evidence_id: followup-full-lint-receipt
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-full-lint.json
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: context_only
  summary: Actual command, working directory, start/finish, exit and original log
    hash.
  snapshot_sha256: 684898aafb57aec01bb761f67d807c2435bb77a7f245e643c35cc70df32317e6
- evidence_id: followup-full-format
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-full-format.log
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: supports
  summary: Black check passes for the full maintained package.
  snapshot_sha256: d11359bb762585719915d9cf73b2eea8dca135ee78f4bd90fa4f8407ffa05465
- evidence_id: followup-full-format-receipt
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-full-format.json
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: context_only
  summary: Actual command, working directory, start/finish, exit and original log
    hash.
  snapshot_sha256: fc6328e8826e5668a974b12e7f3c4afa798c642d2bd4d1c8efcde7a542e3f8d1
- evidence_id: followup-package-coverage
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-package-coverage.log
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: supports
  summary: Maintained package coverage is 71%, exceeding the actual 35% gate; this
    is distinct from the whole package-plus-script aggregate.
  snapshot_sha256: 67646653df9163fe3014eb5737220202a44d88b33eeaedcdd808b36dd5540a70
- evidence_id: followup-package-coverage-receipt
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-package-coverage.json
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: context_only
  summary: Actual command, working directory, start/finish, exit and original log
    hash.
  snapshot_sha256: 1ba8344ea8acf4bfe4f40694948269a435d0f2d61c4ec5208add1e9b541965c1
- evidence_id: followup-full-tests
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-full-tests.log
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: supports
  summary: 'Complete repository pytest suite passes: 3,276 passed, 6 skipped, 32 warnings.
    A non-executable annotation added during the run is separately covered by the
    final 82-test bundle suite, mypy and byte-identical replay.'
  snapshot_sha256: affa913d9c282570a69abeeb526684586864e8653a9cdceebe4a3198130b4580
- evidence_id: followup-full-tests-receipt
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/followup-full-tests.json
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: context_only
  summary: Actual command, working directory, start/finish, exit and original log
    hash.
  snapshot_sha256: f7666606a9c84e37556b1812f4383197df8085854f6e1a452282f82239c1c44f
- evidence_id: target-audit
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/target-audit.json
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: supports
  summary: Fresh exact baseline comparison and preserved target claims; exact selectors
    and changed fields for all nine rows.
  snapshot_sha256: 10b20a6045105ee22fced93eff91f8b17c78622fb0292ce8e4b198cd0972b482
- evidence_id: receipt14
  kind: prior_review
  reference: reports/sssom_completion_20260921/mapping_changes/issue669-1003-scoped-alias-corrections.json
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: supports
  summary: Preserved original nine-row scientific correction receipt; this follow-up
    does not repeat its scientific review.
  snapshot_sha256: 00049aa1d2b19565020d4ecbec999fc723d2cf5954968ec6bf5cebdc0da73f34
- evidence_id: receipt15
  kind: record_content
  reference: reports/sssom_completion_20260921/mapping_changes/issue1014-provenance-restoration.json
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: supports
  summary: Append-only provenance restoration changes only two existing rows and grants
    no approval.
  snapshot_sha256: fbeec3fbfee71be85541353683df135f96dc1d0021c6bfb3877bcc5eca8813d0
- evidence_id: mapping-review
  kind: record_content
  reference: reports/sssom_completion_20260921/review.json
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: supports
  summary: Current native decisions retain 1,740 SUPPORTED and 1,247 WITHHOLD rows.
  snapshot_sha256: 36a22b230bd9bc4c82a1816438d21e28a0aa2fcf21f21e63cd30b6459bb8d23c
- evidence_id: dependency
  kind: record_content
  reference: reports/ingredient_bundle_20261101_followup/dependency-refresh.json
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: supports
  summary: Original successor execution receipt proves the 51-claim/20-owner cohort
    unchanged; final maintained producer replay separately confirms the same review
    bytes.
  snapshot_sha256: f33432a0b360db6eb24e6dba0bfdecba74ae4348adc8c6ca8f7b4c528c73cedf
- evidence_id: prior-companion
  kind: prior_review
  reference: reports/ingredient_bundle_20261101/review.json
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: supports
  summary: Historical companion decision/owner baseline, retained unchanged.
  snapshot_sha256: 84e3572174748d0b801c9da8a0f87541cdfbc01756e10b884da6c4fdb9b23260
- evidence_id: semantics
  kind: authority
  reference: MAPPING_SEMANTICS.md
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: supports
  summary: Identity, predicates, provenance columns and same-subject synonym contract.
  snapshot_sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
- evidence_id: semantic-status
  kind: record_content
  reference: reports/semantic_review_20260921/resolution/current-review.json
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: context_only
  summary: Full scientific release remains FAIL; 1,733 finding IDs / 2,272 assertion
    IDs remain blocked.
  snapshot_sha256: ebc636c818583a687ac6dc54db6393deecbb31a614cf8b0453e01eab448b5d89
- evidence_id: reservation-reprobe
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/receipt-reservation-cleanup-fixed.json
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: supports
  summary: Separate reviewer reproduced successful and failed late-reservation replacement
    cases; mutator never entered and competing receipts survived.
  snapshot_sha256: f294d1fb36fa1460cdbf3fb88058d61f5ca897d5ef3ea96b73fadf4839bdc0bb
- evidence_id: check-provenance
  kind: record_content
  reference: reports/sssom_scientific_curation_20261101/followup-1012-1017/checks/verification.json
  accessed_at: '2026-11-01T02:09:38.381188Z'
  support: supports
  summary: Published command/log hash inventory, current source hashes and explicit
    broad-suite/final-annotation chronology.
  snapshot_sha256: 033101ebd357aec04d240249dee2f4d54a4c463b1824b41aa1320f571faf60a6
assessments:
- assessment_id: canonical-preservation
  area: consistency
  topic: Exact row and disposition preservation
  outcome: supported
  target_ids:
  - canonical
  evidence_ids:
  - target-audit
  - receipt14
  - receipt15
  - followup-full-qc
  - mapping-review
  summary: 'All 2,987 row identities and positions persist; exactly nine payloads
    differ from 4625afd. Seven change only other; carnitine parent changes other/date
    and registry row changes date. Every historical source cell and the #390 comment
    are restored; 2,978 other payloads are identical. All nine changed rows remain
    withheld; all dispositions match the preceding PR head.'
- assessment_id: companion-equivalence
  area: provenance
  topic: Dependency refresh preserves selected scientific content
  outcome: supported
  target_ids:
  - companion
  evidence_ids:
  - dependency
  - prior-companion
  - target-audit
  - followup-refresh-final-replay
  - followup-refresh-final-tests
  summary: The 51 decisions and claims (18 identifier, 20 mapping, 10 occurrence,
    3 product), 20 owner bytes and selected complete mapping rows remain unchanged.
    Only validated global dependency bindings change. The final maintained producer
    replays the successor byte-for-byte without overwriting historical reviews or
    adding approval.
- assessment_id: guarded-producer
  area: representation
  topic: Evidence reservation and native assembly regressions
  outcome: supported
  target_ids:
  - canonical
  - companion
  evidence_ids:
  - issue1018_receipt_green
  - reservation-reprobe
  - followup-refresh-final-tests
  - issue1017_receipt_suite
  summary: Shared receipt/backup reservation checks still-owned device/inode identities
    before mutator entry and removes only owned partial reservations. The companion
    publisher retains exclusive handles. Collision and replacement probes preserve
    competing evidence and refuse source writes. Native assembly retains simultaneous
    synonym_correction and mapping_change bases on rows 184, 901 and 2528.
- assessment_id: release-boundary
  area: scope
  topic: Mechanical validity does not grant scientific release approval
  outcome: supported
  target_ids:
  - canonical
  - companion
  evidence_ids:
  - followup-semantic-integrity
  - semantic-status
  - followup-supported-validate
  - followup-reviewed-validate
  - dependency
  summary: Integrity and reviewed subset exports pass while the global scientific
    release remains FAIL with 1,733 findings and 2,272 assertions. No holds are retired,
    no approvals are carried to changed owner payloads, and no earlier structured
    scientific review is superseded by this mechanical observation.
findings: []
actions: []
limitations:
- The verdict is limited to mechanical consistency/provenance of two specified generated
  artifacts, not a new scientific assessment of the corpus or companion claims.
- The global semantic release remains FAIL with 1,733 blocking findings and 2,272
  blocked assertions; 1,247 mapping rows remain withheld, including both carnitine
  rows and the six rows for unresolved issues 1004/1005.
- Native just qc skips Rule B4 because the expected sibling ontology transforms are
  absent. This review does not claim a new ontology label or actual-directory B4 evaluation.
- Earlier product-label, reconciliation and opaque-subject diagnostics remain historical;
  this follow-up changes provenance cells only relative to the preceding canonical
  head and does not re-certify unresolved synonym or identity policy.
- The original companion generation receipt binds its original producer hash. The
  later final-code replay is separate evidence of identical successor bytes; historical
  receipts are not rewritten to claim a later code hash.
- The final BinaryIO/local-list annotation was added during the broad suite without
  changing executable writer logic. The final annotated module separately passed 82
  focused bundle tests, mypy and byte-identical native replay. The broad run is not
  misrepresented as an exact static-byte test of the final annotation.
- Review source is the inspected working tree based on 612860e, not a claim of final
  committed-head independence. Separate independent review remains required by the
  parent workflow.
notes:
- Evidence paths retain the exact original command receipts; file discovery for copied
  evidence includes ignored report files. No whole-candidate promotion or scientific-status
  change is authorized by this review.
links:
- https://github.com/CultureBotAI/MediaIngredientMech/issues/1012
- https://github.com/CultureBotAI/MediaIngredientMech/issues/1013
- https://github.com/CultureBotAI/MediaIngredientMech/issues/1014
- https://github.com/CultureBotAI/MediaIngredientMech/issues/1015
- https://github.com/CultureBotAI/MediaIngredientMech/issues/1016
- https://github.com/CultureBotAI/MediaIngredientMech/issues/1017
- https://github.com/CultureBotAI/MediaIngredientMech/issues/1018
tags:
- sssom
- mechanical-review
- dependency-refresh
- preserved-holds
- author-review
```
