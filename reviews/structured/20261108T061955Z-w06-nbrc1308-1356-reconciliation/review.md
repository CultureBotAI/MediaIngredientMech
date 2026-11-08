# Reconcile uninstalled NBRC1308 and NBRC1356 nominal stock proposals

- Review: 20261108T061955Z-w06-nbrc1308-1356-reconciliation
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-11-08T06:08:11.314625Z
- Finished UTC: 2026-11-08T06:19:55Z
- Reviewer: /root, worker06 successor author; separate skeptical review by /root/research_b (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

One source-backed shared nominal stock replaces two uninstalled proposals in a99-proposal/188-case successor selection. The original100-proposal published evidence remains immutable. All source holds and processing/quantity uncertainties survive; no maintained owner was merged or changed.

## Scope And Provenance

Bounded proposal-identity cohort:two historical payloads,one shared successor payload,and two exact frozen source cases covering four occurrences(two apply,two remain excluded).

Selection: Exact NEWOWNER-DUP-002 pair and every affected case; no other source case is newly scientifically reassessed.
Coverage: full; 5 reviewed / 5 in the declared population.
Source: working_tree at Git base d5a7613c931d45d057eaca7b5ec15280aca76c9e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| A-P-NBRC1308-TRACE | reports/all_unmatched_20261107/worker-06/research-a/payloads/nbrc_1308_trace_elements_solution.yaml | source | A-P-NBRC1308-TRACE |
| C-P-NBRC1356-TRACE | reports/all_unmatched_20261107/worker-06/research-c/after/nbrc_1356_trace_elements_stock.yaml | source | C-P-NBRC1356-TRACE |
| V2-P-NBRC1308-1356-TRACE | reports/all_unmatched_20261107/worker-06/successor-v2/payloads/nbrc_1308_1356_trace_elements_stock.yaml | source | V2-P-NBRC1308-1356-TRACE |
| CM_NAME:13cefff78cf8e9a8c3f2814ab5e4406a797d0ab1ccd53fb9ea6c63036fa08e4b | reports/all_unmatched_20261107/worker-06/native-inputs/frozen-shard-06.json # cases[case_id=CM_NAME:13cefff78cf8e9a8c3f2814ab5e4406a797d0ab1ccd53fb9ea6c63036fa08e4b] | snapshot_row | Trace element solution** |
| CM_NAME:dfa4a8d37ab889934a8f5907c93a8dfbe24898eb5641f6b038c55477dd355230 | reports/all_unmatched_20261107/worker-06/native-inputs/frozen-shard-06.json # cases[case_id=CM_NAME:dfa4a8d37ab889934a8f5907c93a8dfbe24898eb5641f6b038c55477dd355230] | snapshot_row | Trace element solution**** |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full188-case structural binding | passed | True | A-P-NBRC1308-TRACE, C-P-NBRC1356-TRACE, V2-P-NBRC1308-1356-TRACE, CM_NAME:13cefff78cf8e9a8c3f2814ab5e4406a797d0ab1ccd53fb9ea6c63036fa08e4b, CM_NAME:dfa4a8d37ab889934a8f5907c93a8dfbe24898eb5641f6b038c55477dd355230 | Actual execution passed; exact scope, inputs and result retained in reports/all_unmatched_20261107/worker-06/successor-v2/final/logs/structural-command.json |
| Strict99-payload schema | passed | True | A-P-NBRC1308-TRACE, C-P-NBRC1356-TRACE, V2-P-NBRC1308-1356-TRACE, CM_NAME:13cefff78cf8e9a8c3f2814ab5e4406a797d0ab1ccd53fb9ea6c63036fa08e4b, CM_NAME:dfa4a8d37ab889934a8f5907c93a8dfbe24898eb5641f6b038c55477dd355230 | Actual execution passed; exact scope, inputs and result retained in reports/all_unmatched_20261107/worker-06/successor-v2/final/logs/schema-command.json |
| Native full-catalog isolated successor partonomy | passed | True | A-P-NBRC1308-TRACE, C-P-NBRC1356-TRACE, V2-P-NBRC1308-1356-TRACE, CM_NAME:13cefff78cf8e9a8c3f2814ab5e4406a797d0ab1ccd53fb9ea6c63036fa08e4b, CM_NAME:dfa4a8d37ab889934a8f5907c93a8dfbe24898eb5641f6b038c55477dd355230 | Actual execution passed; exact scope, inputs and result retained in reports/all_unmatched_20261107/worker-06/successor-v2/final/logs/partonomy-successor.json |
| Frozen and published evidence/occurrence/owner invariants | passed | True | A-P-NBRC1308-TRACE, C-P-NBRC1356-TRACE, V2-P-NBRC1308-1356-TRACE, CM_NAME:13cefff78cf8e9a8c3f2814ab5e4406a797d0ab1ccd53fb9ea6c63036fa08e4b, CM_NAME:dfa4a8d37ab889934a8f5907c93a8dfbe24898eb5641f6b038c55477dd355230 | Actual execution passed; exact scope, inputs and result retained in reports/all_unmatched_20261107/worker-06/successor-v2/final/logs/invariants.json |

## Scientific And Domain Assessments

### One nominal formulation; source numbers do not distinguish substances

identity: supported. Targets: A-P-NBRC1308-TRACE, C-P-NBRC1356-TRACE, V2-P-NBRC1308-1356-TRACE.

Both original stock proposals specify the identical13-solute and1L-water input table with the same NTA→NaOH pH6.5→minerals and finalpH7.0 instruction. One shared registry identity is justified on composition and preparation, before selecting the joint name/path.

### Unknown titrant, water input, child forms and processing endpoints

quantity: supported. Targets: V2-P-NBRC1308-1356-TRACE.

The successor retains15 input components:13 quantified solutes,1L water input, and NaOH without quantity/unit. No final-volume make-up, missing hydrate form, equilibrium species or final-pH adjustment reagent is invented; UNKNOWN completeness is conservative for unspecified final adjustment, not proof that unquantified NaOH is absent.

Exact payload SHA256 194d39c6301961eba8719f01d02762effb19c1b4a7fdfac247210f41c038127c. No whole-to-part identity relation or global starred synonym.

### Complete source-case reassessment and exact occurrence partition

scope: supported. Targets: CM_NAME:13cefff78cf8e9a8c3f2814ab5e4406a797d0ab1ccd53fb9ea6c63036fa08e4b.

Complete primary tables distinguish NBRC1020/824 (shared NTA/KOH stock, separate Se/W supplement) from NBRC1308. Independent comparison now shows that NBRC1308 and NBRC1356 have the same13 specified solutes,1L water input, NTA→NaOH pH6.5→minerals and stated finalpH7.0 preparation. Two uninstalled identities are therefore replaced by one reconciled nominal formulation proposal. RecipeIDs, footnotes and metadata differences do not establish another substance.

All three original occurrences remain. Only CultureMech:007471 ingredients/8, source nbrc.medium:1308, occurrence CM_OCC:e689137127cd84bead1063ab24e931745a4a44fb673a953471ea3ab33e3a3df5 uses the reconciled stock (1ml, autoclaved with receiving medium underN2/CO2 80/20). CultureMech:007450 ingredients/8 and CultureMech:007496 ingredients/7 remain exclusively A-P-NBRC1020-824-TRACE. Raw Trace element solution** is occurrence-local. No source file basename is used to infer the NBRC accession. NaOH quantity/concentration and any reagent/amount for reaching final pH7.0 remain unspecified; water is a1L input, not asserted final volume. Retain source-specific dose/processing and all existing source/owner/export holds; no global starred-label identity or post-processing chemical equivalence.

### Complete source-case reassessment and exact occurrence partition

scope: supported. Targets: CM_NAME:dfa4a8d37ab889934a8f5907c93a8dfbe24898eb5641f6b038c55477dd355230.

NBRC1356 has the same complete13-solute/water table and NTA/NaOH preparation as NBRC1308. It does not warrant a distinct whole-stock registry owner merely because its local label has four stars or NaOH metadata/closure were encoded differently. One successor proposal replaces both uninstalled proposals; unknown quantities, water basis and chemical forms remain explicit.

The only occurrence, CultureMech:007474 ingredients/6, nbrc.medium:1356, CM_OCC:2c345cfde3bd9095fd0dad8782a6d904e0bf1ef8beb5c12333b78d7916f8cb03, links to the shared nominal formulation. Its10ml filter-sterile concentrated-stock addition inN2-handled medium stays distinct from1308 processing. Raw Trace element solution**** remains local provenance, not a global synonym. Equality of nominal formulation does not assert identical post-processing endpoints. NaOH quantity/concentration and any reagent/amount for reaching final pH7.0 remain unspecified; water is a1L input, not asserted final volume. Retain source-specific dose/processing and all existing source/owner/export holds; no global starred-label identity or post-processing chemical equivalence.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### coordinator-intake

Use successor-v2/final/selection.json and its99-proposal ledger; do not install either superseded uninstalled owner. Integrate only through coordinator guarded workflows after other-worker review and source/owner/export gates.

- Preserve all four affected occurrence links and the unchanged NBRC1020/824 sibling stock.
- Retain both old author/reviewer lineages and original100-proposal evidence; compare exact new before/after hashes.
- Keep all88downstream holds and other source flags until separately authorized content-bound review resolves them.

## Category Boundaries

- lump: A-P-NBRC1308-TRACE, C-P-NBRC1356-TRACE. Complete primary composition and nominal stock preparation agree; separate identifiers/recipe accessions and different NaOH/completeness serialization do not establish distinct substances. Retire both uninstalled selections in favor of the shared successor.
- retain: CM_NAME:13cefff78cf8e9a8c3f2814ab5e4406a797d0ab1ccd53fb9ea6c63036fa08e4b, CM_NAME:dfa4a8d37ab889934a8f5907c93a8dfbe24898eb5641f6b038c55477dd355230. Do not lump source cases or erase occurrences:case19 retains its two excluded NBRC1020/824 siblings; NBRC1308 and1356 doses and sterilization context remain distinct.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| A-E-CAPTURE-149 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1308; Complete source recipe/product table and preparation; inspect the exact source label and context named in each case applicability; complete trace-elements table and surrounding receiving-medium preparation | supports | Full source table establishes the nominal formulation and its own occurrence processing. Original retrieval timestamp and capture bytes retained; no new retrieval is claimed. |
| C-E-nbrc-1356 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1356; nbrc-1356; exact captured source response; complete trace-elements table and surrounding receiving-medium preparation | supports | Full source table establishes the nominal formulation and its own occurrence processing. Original retrieval timestamp and capture bytes retained; no new retrieval is claimed. |
| OWNER | reports/all_unmatched_20261107/worker-06/successor-v2/research-c/existing-owner-search.json | supports | Bounded search of all2956 maintained owners including ignored files, plus full original100proposals; exact stock not established in maintained owners. Unknown generic stocks are not chemically disproved. |
| COMPARE | reports/all_unmatched_20261107/worker-06/successor-v2/research-a/nbrc1308-1356-comparison.json | supports | Complete table comparison and all4 frozen contexts; contribution by original1308 author, not final independent review. |
| LINEAGE | reports/all_unmatched_20261107/worker-06/successor-v2/lineage.json | supports | Both author histories, payloads, source links and original skeptical-review receipts retained unchanged. |
| REVIEW | reports/all_unmatched_20261107/worker-06/successor-v2/research-b/scientific-review.json | supports | Separate skeptical review by research_b of root-authored final shared payload and both exact affected outcomes. |
| BIND | reports/all_unmatched_20261107/worker-06/successor-v2/research-b/final-binding-v2.json | supports | Final assembled successor binding:188 cases,99 payloads, all evidence and exact occurrence partitions; no release approval. |
| FINDING | reports/all_unmatched_20261107/worker-06/successor-v2/context/confirmed-findings-supplement-v1.json | supports | Non-native immutable coordinator supplement NEWOWNER-DUP-002; two original payloads denote one nominal formulation. |
| AUDIT | reports/all_unmatched_20261107/worker-06/successor-v2/final/logs/structural-audit.json | supports | Full188-case source/evidence/payload/backlink structural audit; no scientific approval implied. |
| SCHEMA | reports/all_unmatched_20261107/worker-06/successor-v2/final/logs/schema-command.json | supports | Actual strict schema command validates99 selected payloads. |
| PARTONOMY | reports/all_unmatched_20261107/worker-06/successor-v2/final/logs/partonomy-successor.json | supports | Native full-catalog partonomy validation of isolated overlay with all99 selected proposals; no maintained installation. |
| INVARIANTS | reports/all_unmatched_20261107/worker-06/successor-v2/final/logs/invariants.json | supports | Original1758 manifest files, sourceholds88, all188 frozen cases and97unchanged payloads retained; exact capture and before/after hashes verified. |

## Limits And Additional Notes

- Nominal stock formulation equality does not establish identical sterilization endpoints or solution speciation.
- NaOH amount/concentration, any final-pH correction and final stock volume remain unspecified.
- The coordinator duplicate finding is a non-native supplement. It is cited exactly as prior evidence; no nonexistent native previous_occurrences identifier or issue closure is invented. No new unresolved discrepancy was found in the bounded successor selection.
- The existing-owner search does not prove underspecified generic stock records chemically different; none is sufficiently established to select as an exact owner.
- This review is not source-case, whole-owner or export approval; worker03 historical review of d5a7613 stays valid as historical evidence.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261108T061955Z-w06-nbrc1308-1356-reconciliation
kind: category
repository: CultureBotAI/MediaIngredientMech
title: Reconcile uninstalled NBRC1308 and NBRC1356 nominal stock proposals
started_at: '2026-11-08T06:08:11.314625Z'
finished_at: '2026-11-08T06:19:55Z'
reviewer:
  identity: /root, worker06 successor author; separate skeptical review by /root/research_b
  kind: agent
  independence: self_review
  independence_basis: This native synthesis is authored by the successor author. The
    exact payload and all affected case outcomes were separately reviewed by research_b;
    original1308/1356 authors contributed source comparison and existing-owner search,
    not final successor approval.
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: One source-backed shared nominal stock replaces two uninstalled proposals
  in a99-proposal/188-case successor selection. The original100-proposal published
  evidence remains immutable. All source holds and processing/quantity uncertainties
  survive; no maintained owner was merged or changed.
source:
  git_revision: d5a7613c931d45d057eaca7b5ec15280aca76c9e
  state: working_tree
  inputs:
  - path: MAPPING_SEMANTICS.md
    sha256: 6b52f2ac48109ddd5d81996a136b19776cab55efa69a5ec832cf716d6885a062
    role: context
  - path: conf/record_review.yaml
    sha256: 07a8fa6d17ee664c7a2bc2d5b5821bd106f6aa454299b4f3e0440176876cd82e
    role: context
  - path: docs/record-review-profile.md
    sha256: da17e2048a13514a422bc94bd2f8d48943cffc5689b96e3f07da26423248d1a7
    role: context
  - path: docs/stock_components.md
    sha256: 62a8a5393db91e943f6f3903bd624a00e3567f6f0a2ca2391742e97dc0c19d49
    role: context
  - path: reports/all_unmatched_20261107/worker-06/independent/root-review-a/final-review-v2.json
    sha256: 298769ce427a77c5dede04e26637203fe973140828fcb1ab08278e510b076ed0
    role: context
  - path: reports/all_unmatched_20261107/worker-06/native-inputs/frozen-shard-06.json
    sha256: 6e5d487b0ffb05a867766fe51bc90074c7aa2e48459335cf983f021720ce2808
    role: target
  - path: reports/all_unmatched_20261107/worker-06/proposals.json
    sha256: fc838985c5b79ef4cef5a502efe3242cdc1b87c8baf805e9b7f56e96de4ed61f
    role: context
  - path: reports/all_unmatched_20261107/worker-06/research-a/captures/0fd90bae1b54ca6d.raw
    sha256: d00ccd979e58433b8e97aa0d84dbee50d3aa8c571e934f39dd7f261f99a7b8be
    role: context
  - path: reports/all_unmatched_20261107/worker-06/research-a/payloads/nbrc_1308_trace_elements_solution.yaml
    sha256: 6a8f4ebc4562e888207270f5fce1dfdc425c581494d9183bd6b8aed5e896a2aa
    role: target
  - path: reports/all_unmatched_20261107/worker-06/research-b/review-c/review-final.json
    sha256: 06c6ec89b395069f8d1e2e50be689fc9b87305ee619e75bb4b9d5cac1797db99
    role: context
  - path: reports/all_unmatched_20261107/worker-06/research-c/after/nbrc_1356_trace_elements_stock.yaml
    sha256: 5894ab52e5e649cee09bcd3d149d3723ed42cca6661848dcceaf30078bc170cb
    role: target
  - path: reports/all_unmatched_20261107/worker-06/research-c/captures/nbrc-1356.txt
    sha256: 87b9e6d80867f35b31318154c798b6869c3246bb526a19dccc8e8be94019dd49
    role: context
  - path: reports/all_unmatched_20261107/worker-06/successor-v2/context/confirmed-findings-supplement-v1.json
    sha256: e309179928a0130bf05fd34f95f501bb5339bc44e4fbfd6f05ac2d6ebc11345a
    role: context
  - path: reports/all_unmatched_20261107/worker-06/successor-v2/context/issue-1207.json
    sha256: c5e820524027cc7f030dd78eb5694a425c5e04ecc1c1145bf31a17ccc065710e
    role: context
  - path: reports/all_unmatched_20261107/worker-06/successor-v2/final/decisions.json
    sha256: 815ea3441a231f3d2464a57089338c7c78d07ac3f9c3f77e77f4865b39c01acd
    role: context
  - path: reports/all_unmatched_20261107/worker-06/successor-v2/final/evidence.json
    sha256: 3abee21eb759145e210d5fa5ee3f77fcc3aba0bc0c71eccde35d9b890022fec3
    role: context
  - path: reports/all_unmatched_20261107/worker-06/successor-v2/final/logs/invariants.json
    sha256: 332a8cd491c2a4dd0efc79efc185bcbb2d5c08eb35755c13832aebb07c29b8b8
    role: context
  - path: reports/all_unmatched_20261107/worker-06/successor-v2/final/logs/partonomy-successor.json
    sha256: a6a742dac61fcf77d10ba5c8bf1cac80ee2db9e69f7c4fc5f9634f922fce3590
    role: context
  - path: reports/all_unmatched_20261107/worker-06/successor-v2/final/logs/partonomy-successor.log
    sha256: 2a18677e30f7e1aec501bd6a14fe7b9f83a172555fcc4df267c62ec0081bbf10
    role: context
  - path: reports/all_unmatched_20261107/worker-06/successor-v2/final/logs/schema-command.json
    sha256: e13ae747161a6c1b70825125e8c8fbdc328790388a1f7a31611c2efae557e92d
    role: context
  - path: reports/all_unmatched_20261107/worker-06/successor-v2/final/logs/schema.tsv
    sha256: 4ccba8b77ce80cf210105b5284b5953747729aba576ccdeecb81f7db84eb721b
    role: context
  - path: reports/all_unmatched_20261107/worker-06/successor-v2/final/logs/structural-audit.json
    sha256: 11e73d9f18d805bac208bbe9a409b70744b6c72434f3669ed67c9d19ab41093e
    role: context
  - path: reports/all_unmatched_20261107/worker-06/successor-v2/final/proposals.json
    sha256: 2244c896a5b1cf50681da7d7f15c4ccabae916aa31cc9e40e18b95d72e0dfd14
    role: context
  - path: reports/all_unmatched_20261107/worker-06/successor-v2/final/selection.json
    sha256: 4d716bee7fafb8fe081e1604da305d8ecfd0c05fc3e40bcdf3aa6ba0cd0d157a
    role: context
  - path: reports/all_unmatched_20261107/worker-06/successor-v2/final/source-holds.json
    sha256: eaddfd7ffe5ba2ba1be011696ad741e1b010db2cc9ca4678954a640484f70b77
    role: context
  - path: reports/all_unmatched_20261107/worker-06/successor-v2/lineage.json
    sha256: 35ebf1795329c3c64233982cf463433e57b1d9cc8af871bf3c34725f330989d8
    role: context
  - path: reports/all_unmatched_20261107/worker-06/successor-v2/payloads/nbrc_1308_1356_trace_elements_stock.yaml
    sha256: 194d39c6301961eba8719f01d02762effb19c1b4a7fdfac247210f41c038127c
    role: target
  - path: reports/all_unmatched_20261107/worker-06/successor-v2/research-a/nbrc1308-1356-comparison.json
    sha256: ab26374ea8cd9cec47a645c33f366b22cf851df727eac35270270bb2c0b2bcf0
    role: context
  - path: reports/all_unmatched_20261107/worker-06/successor-v2/research-b/final-binding-v2.json
    sha256: 7c1259804b8f07a12628a5013da60b52a43053b834fb2a9410b552add0909a43
    role: context
  - path: reports/all_unmatched_20261107/worker-06/successor-v2/research-b/scientific-review.json
    sha256: f82cdd0841cf518c0e11e56c7a281f57e1e80e15f107c5f88ed6a8508710b5c2
    role: context
  - path: reports/all_unmatched_20261107/worker-06/successor-v2/research-c/existing-owner-search.json
    sha256: ae5dd4d820e402fddc4868c9f1cc1f345ec361439c6d34db8f3d705da4ae5aca
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/mediaingredientmech/schema/mediaingredientmech.yaml
    sha256: bb43dee29b21fdee72a48022456e733e49e95824c4c09674f9b3165c290fe012
    role: context
scope:
  description: Bounded proposal-identity cohort:two historical payloads,one shared
    successor payload,and two exact frozen source cases covering four occurrences(two
    apply,two remain excluded).
  selection: Exact NEWOWNER-DUP-002 pair and every affected case; no other source
    case is newly scientifically reassessed.
  coverage: full
  population_size: 5
  reviewed_target_ids:
  - A-P-NBRC1308-TRACE
  - C-P-NBRC1356-TRACE
  - V2-P-NBRC1308-1356-TRACE
  - CM_NAME:13cefff78cf8e9a8c3f2814ab5e4406a797d0ab1ccd53fb9ea6c63036fa08e4b
  - CM_NAME:dfa4a8d37ab889934a8f5907c93a8dfbe24898eb5641f6b038c55477dd355230
  exclusions:
  - target: Other186source cases and98other selected payloads
    reason: 184cases/97payloads retain prior science unchanged; the Merck component-label
      correction and its two source cases are reviewed separately. Full-shard checks
      are rerun.
  - target: Maintained installation, post-sterilization chemical equivalence and source/owner/export
      release
    reason: Coordinator integration and separate content-bound gates remain required.
targets:
- target_id: A-P-NBRC1308-TRACE
  path: reports/all_unmatched_20261107/worker-06/research-a/payloads/nbrc_1308_trace_elements_solution.yaml
  label: A-P-NBRC1308-TRACE
  kind: source
  ownership_note: No maintained whole-stock owner was established by the bounded ignored-inclusive
    search. These are uninstalled source/proposal artifacts, not invented maintained
    owners; intended shared path appears only in the proposal.
- target_id: C-P-NBRC1356-TRACE
  path: reports/all_unmatched_20261107/worker-06/research-c/after/nbrc_1356_trace_elements_stock.yaml
  label: C-P-NBRC1356-TRACE
  kind: source
  ownership_note: No maintained whole-stock owner was established by the bounded ignored-inclusive
    search. These are uninstalled source/proposal artifacts, not invented maintained
    owners; intended shared path appears only in the proposal.
- target_id: V2-P-NBRC1308-1356-TRACE
  path: reports/all_unmatched_20261107/worker-06/successor-v2/payloads/nbrc_1308_1356_trace_elements_stock.yaml
  label: V2-P-NBRC1308-1356-TRACE
  kind: source
  ownership_note: No maintained whole-stock owner was established by the bounded ignored-inclusive
    search. These are uninstalled source/proposal artifacts, not invented maintained
    owners; intended shared path appears only in the proposal.
- target_id: CM_NAME:13cefff78cf8e9a8c3f2814ab5e4406a797d0ab1ccd53fb9ea6c63036fa08e4b
  path: reports/all_unmatched_20261107/worker-06/native-inputs/frozen-shard-06.json
  selector: cases[case_id=CM_NAME:13cefff78cf8e9a8c3f2814ab5e4406a797d0ab1ccd53fb9ea6c63036fa08e4b]
  label: Trace element solution**
  kind: snapshot_row
  ownership_note: No maintained whole-stock owner was established by the bounded ignored-inclusive
    search. These are uninstalled source/proposal artifacts, not invented maintained
    owners; intended shared path appears only in the proposal.
- target_id: CM_NAME:dfa4a8d37ab889934a8f5907c93a8dfbe24898eb5641f6b038c55477dd355230
  path: reports/all_unmatched_20261107/worker-06/native-inputs/frozen-shard-06.json
  selector: cases[case_id=CM_NAME:dfa4a8d37ab889934a8f5907c93a8dfbe24898eb5641f6b038c55477dd355230]
  label: Trace element solution****
  kind: snapshot_row
  ownership_note: No maintained whole-stock owner was established by the bounded ignored-inclusive
    search. These are uninstalled source/proposal artifacts, not invented maintained
    owners; intended shared path appears only in the proposal.
checks:
- check_id: whole-shard
  name: Full188-case structural binding
  status: passed
  required: true
  summary: Actual execution passed; exact scope, inputs and result retained in reports/all_unmatched_20261107/worker-06/successor-v2/final/logs/structural-command.json
  target_ids:
  - A-P-NBRC1308-TRACE
  - C-P-NBRC1356-TRACE
  - V2-P-NBRC1308-1356-TRACE
  - CM_NAME:13cefff78cf8e9a8c3f2814ab5e4406a797d0ab1ccd53fb9ea6c63036fa08e4b
  - CM_NAME:dfa4a8d37ab889934a8f5907c93a8dfbe24898eb5641f6b038c55477dd355230
  command: /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.venv/bin/python
    /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/scripts/audit_worker_outcomes_v1.py
    --shard /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5/shards/shard-06.json
    --decisions /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/workers/w06/worktree/reports/all_unmatched_20261107/worker-06/successor-v2/final/decisions.json
    --evidence /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/workers/w06/worktree/reports/all_unmatched_20261107/worker-06/successor-v2/final/evidence.json
    --proposals /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/workers/w06/worktree/reports/all_unmatched_20261107/worker-06/successor-v2/final/proposals.json
    --artifact-root /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/workers/w06/worktree/reports/all_unmatched_20261107/worker-06
    --source-root /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5
    --mim-root /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/workers/w06/worktree
    --output /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/workers/w06/worktree/reports/all_unmatched_20261107/worker-06/successor-v2/final/logs/structural-audit.json
  exit_code: 0
  evidence_ids:
  - AUDIT
- check_id: schema
  name: Strict99-payload schema
  status: passed
  required: true
  summary: Actual execution passed; exact scope, inputs and result retained in reports/all_unmatched_20261107/worker-06/successor-v2/final/logs/schema-command.json
  target_ids:
  - A-P-NBRC1308-TRACE
  - C-P-NBRC1356-TRACE
  - V2-P-NBRC1308-1356-TRACE
  - CM_NAME:13cefff78cf8e9a8c3f2814ab5e4406a797d0ab1ccd53fb9ea6c63036fa08e4b
  - CM_NAME:dfa4a8d37ab889934a8f5907c93a8dfbe24898eb5641f6b038c55477dd355230
  command: /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.venv/bin/python
    scripts/validate_strict.py reports/all_unmatched_20261107/worker-06/research-a/payloads/Calcium_Pantothenate.yaml
    reports/all_unmatched_20261107/worker-06/research-a/payloads/Calcium_DL-Pantothenate.yaml
    reports/all_unmatched_20261107/worker-06/research-a/payloads/D-glucose.yaml reports/all_unmatched_20261107/worker-06/research-a/payloads/Lanthanum_III_Chloride_Heptahydrate.yaml
    reports/all_unmatched_20261107/worker-06/successor-v2/final/payloads/Merck_108339_Sabouraud_2percent_Dextrose_Broth.yaml
    reports/all_unmatched_20261107/worker-06/research-a/payloads/nbrc_1407_boiled_bakers_yeast_extract.yaml
    reports/all_unmatched_20261107/worker-06/research-a/payloads/dsmz_29_40_sodium_carbonate_1m_stock.yaml
    reports/all_unmatched_20261107/worker-06/research-a/payloads/atcc_1249_component_i.yaml
    reports/all_unmatched_20261107/worker-06/research-a/payloads/jcm_167_sl6_trace_elements.yaml
    reports/all_unmatched_20261107/worker-06/research-a/payloads/atcc_1257_sodium_carbonate_4_percent_stock.yaml
    reports/all_unmatched_20261107/worker-06/research-a/payloads/jcm_1136_548_glucose_1m_stock.yaml
    reports/all_unmatched_20261107/worker-06/research-a/payloads/jcm_933_rst_trace_elements.yaml
    reports/all_unmatched_20261107/worker-06/research-a/payloads/jcm_340_sl4_trace_elements.yaml
    reports/all_unmatched_20261107/worker-06/research-a/payloads/atcc_md_tms_formulation_20261108.yaml
    reports/all_unmatched_20261107/worker-06/research-a/payloads/jcm_1088_trace_vitamins.yaml
    reports/all_unmatched_20261107/worker-06/research-a/payloads/jcm_1344_yeast_extract_1_percent_stock.yaml
    reports/all_unmatched_20261107/worker-06/research-a/payloads/jcm_1353_phosphate_buffered_trace_vitamins.yaml
    reports/all_unmatched_20261107/worker-06/research-a/payloads/nbrc_1050_trace_elements_solution.yaml
    reports/all_unmatched_20261107/worker-06/research-a/payloads/nbrc_1086_trace_elements_solution.yaml
    reports/all_unmatched_20261107/worker-06/research-a/payloads/nbrc_925_trace_elements_solution.yaml
    reports/all_unmatched_20261107/worker-06/research-a/payloads/nbrc_1274_trace_elements_solution.yaml
    reports/all_unmatched_20261107/worker-06/successor-v2/payloads/nbrc_1308_1356_trace_elements_stock.yaml
    reports/all_unmatched_20261107/worker-06/research-a/payloads/nbrc_1020_824_trace_element_solution.yaml
    reports/all_unmatched_20261107/worker-06/research-a/payloads/jcm_576_sl12_trace_metals.yaml
    reports/all_unmatched_20261107/worker-06/research-a/payloads/togo_2665_koh_solution_unspecified_strength.yaml
    reports/all_unmatched_20261107/worker-06/research-a/payloads/roscoff_pcrs11_fecl3_na2edta_stock_2019.yaml
    reports/all_unmatched_20261107/worker-06/research-a/payloads/dried_yeast_material.yaml
    reports/all_unmatched_20261107/worker-06/research-a/payloads/pressed_yeast_material.yaml
    reports/all_unmatched_20261107/worker-06/research-a/payloads/porphyra_thalli_material.yaml
    reports/all_unmatched_20261107/worker-06/research-a/payloads/Rye_Grass.yaml reports/all_unmatched_20261107/worker-06/research-a/payloads/wako_hipolypepton_casein_hydrolysate.yaml
    reports/all_unmatched_20261107/worker-06/research-a/payloads/Polypeptone.yaml
    reports/all_unmatched_20261107/worker-06/research-a/payloads/bd_difco_yeast_carbon_base_family.yaml
    reports/all_unmatched_20261107/worker-06/research-b/proposed-owners/Yeast_Extract.yaml
    reports/all_unmatched_20261107/worker-06/research-b/proposed-owners/Alpha-d-glucose.yaml
    reports/all_unmatched_20261107/worker-06/research-b/proposed-owners/3-_N-morpholinopropanesulfonic_Acid.yaml
    reports/all_unmatched_20261107/worker-06/research-b/proposed-owners/Chromium_Iii_Chloride_Hexahydrate.yaml
    reports/all_unmatched_20261107/worker-06/research-b/proposed-owners/nbrc_1257_1321_trace_element_mixture.yaml
    reports/all_unmatched_20261107/worker-06/research-b/proposed-owners/nbrc_1117_sl7_trace_element_solution.yaml
    reports/all_unmatched_20261107/worker-06/research-b/proposed-owners/nbrc_268_trace_salts_solution.yaml
    reports/all_unmatched_20261107/worker-06/research-b/proposed-owners/atcc_1464_trace_metals.yaml
    reports/all_unmatched_20261107/worker-06/research-b/proposed-owners/jcm_301_growth_stimulating_factors.yaml
    reports/all_unmatched_20261107/worker-06/research-b/proposed-owners/mediadive_124_haemin_0p05_percent_stock.yaml
    reports/all_unmatched_20261107/worker-06/research-b/proposed-owners/dsmz_1033_ferric_chloride_0p17_mm_stock.yaml
    reports/all_unmatched_20261107/worker-06/research-b/proposed-owners/jcm_977_glucose_20_percent_wv_stock.yaml
    reports/all_unmatched_20261107/worker-06/research-b/proposed-owners/togo_2601_a5_cobalt_trace_metal_stock.yaml
    reports/all_unmatched_20261107/worker-06/research-b/proposed-owners/atcc_957_a5_trace_metals.yaml
    reports/all_unmatched_20261107/worker-06/research-b/proposed-owners/atcc_461_castenholz_salts_2x.yaml
    reports/all_unmatched_20261107/worker-06/research-b/proposed-owners/togo_2788_vogel_bonner_salts_50x.yaml
    reports/all_unmatched_20261107/worker-06/research-b/proposed-owners/dsmz_135_339a_sodium_carbonate_5_percent_wv_stock.yaml
    reports/all_unmatched_20261107/worker-06/research-b/proposed-owners/jcm_273_nitsch_trace_elements.yaml
    reports/all_unmatched_20261107/worker-06/research-b/proposed-owners/nbrc_1226_trace_element_solution.yaml
    reports/all_unmatched_20261107/worker-06/research-b/proposed-owners/nbrc_392_trace_element_solution.yaml
    reports/all_unmatched_20261107/worker-06/research-b/proposed-owners/jcm_1435_trace_element_solution.yaml
    reports/all_unmatched_20261107/worker-06/research-b/proposed-owners/togo_3181_rm_trace_vitamins.yaml
    reports/all_unmatched_20261107/worker-06/research-b/proposed-owners/atcc_1612_sodium_carbonate_5_percent_stock.yaml
    reports/all_unmatched_20261107/worker-06/research-b/proposed-owners/Proteose_Yeastolate.yaml
    reports/all_unmatched_20261107/worker-06/research-b/proposed-owners/bd_difco_ynb_without_amino_acids_and_ammonium_sulfate_family.yaml
    reports/all_unmatched_20261107/worker-06/research-c/after/N-Z-Amine_A.yaml reports/all_unmatched_20261107/worker-06/research-c/after/Sulfur.yaml
    reports/all_unmatched_20261107/worker-06/research-c/after/L-ornithine_Monohydrochloride.yaml
    reports/all_unmatched_20261107/worker-06/research-c/after/Trace_Element_Solution_See_Medium_No_187.yaml
    reports/all_unmatched_20261107/worker-06/research-c/after/Trace_Minerals_See_Medium_No_151.yaml
    reports/all_unmatched_20261107/worker-06/research-c/after/Trace_Vitamins_Solution_See_Medium_No_284.yaml
    reports/all_unmatched_20261107/worker-06/research-c/after/JCM_197_Trace_Vitamins.yaml
    reports/all_unmatched_20261107/worker-06/research-c/after/Alginic_Acid.yaml reports/all_unmatched_20261107/worker-06/research-c/after/JCM_899_Trace_Element_Solution.yaml
    reports/all_unmatched_20261107/worker-06/research-c/after/JCM_1355_Modified_Trace_Minerals.yaml
    reports/all_unmatched_20261107/worker-06/research-c/after/JCM_1079_Trace_Element_Solution.yaml
    reports/all_unmatched_20261107/worker-06/research-c/after/JCM_284_Trace_Element_Solution.yaml
    reports/all_unmatched_20261107/worker-06/research-c/after/togo_2809_ticl3_20_percent_wv_stock.yaml
    reports/all_unmatched_20261107/worker-06/research-c/after/jcm_1375_1435_825_glucose_10_percent_stock.yaml
    reports/all_unmatched_20261107/worker-06/research-c/after/togo_2231_sodium_carbonate_4g_per_l_stock.yaml
    reports/all_unmatched_20261107/worker-06/research-c/after/togo_2790_glucose_20_percent_stock.yaml
    reports/all_unmatched_20261107/worker-06/research-c/after/jcm_1435_oxoid_yeast_extract_10_percent_stock.yaml
    reports/all_unmatched_20261107/worker-06/research-c/after/togo_2568_glucose_10_percent_stock.yaml
    reports/all_unmatched_20261107/worker-06/research-c/after/jcm_1009_anaerobic_glucose_20_percent_wv_stock.yaml
    reports/all_unmatched_20261107/worker-06/research-c/after/nbrc_1169_trace_elements_stock.yaml
    reports/all_unmatched_20261107/worker-06/research-c/after/nbrc_857_936_trace_elements_stock.yaml
    reports/all_unmatched_20261107/worker-06/research-c/after/jcm_1389_acc8_conditioned_supernatant.yaml
    reports/all_unmatched_20261107/worker-06/research-c/after/bd_difco_tc_yeastolate.yaml
    reports/all_unmatched_20261107/worker-06/research-c/after/bd_difco_ynb_without_amino_acids_family.yaml
    reports/all_unmatched_20261107/worker-06/research-c/after/roscoff_pcrs11_2019_gaffron_se_stock.yaml
    reports/all_unmatched_20261107/worker-06/research-root/proposed-owners/R-P-ALPHA-GLUCOSE-MONOHYDRATE.yaml
    reports/all_unmatched_20261107/worker-06/research-root/proposed-owners/R-P-JCM243-STOCK.yaml
    reports/all_unmatched_20261107/worker-06/research-root/proposed-owners/R-P-MODIFIED-VITAMINS.yaml
    reports/all_unmatched_20261107/worker-06/research-root/proposed-owners/R-P-NEODYMIUM-FORM.yaml
    reports/all_unmatched_20261107/worker-06/research-root/proposed-owners/R-P-YEAST-CELL-PASTE.yaml
    reports/all_unmatched_20261107/worker-06/research-root/proposed-owners/R-P-XANTHOCIDIN-EVIDENCE.yaml
    reports/all_unmatched_20261107/worker-06/research-root/proposed-owners/R-P-JCM209-STOCK.yaml
    reports/all_unmatched_20261107/worker-06/research-root/proposed-owners/R-P-GYP-BROTH.yaml
    reports/all_unmatched_20261107/worker-06/research-root/proposed-owners/R-P-VIRIDOGRISEIN-EVIDENCE.yaml
    reports/all_unmatched_20261107/worker-06/research-root/proposed-owners/R-P-ARDACIN-C.yaml
    reports/all_unmatched_20261107/worker-06/research-root/proposed-owners/R-P-JCM1167-TRACE-STOCK.yaml
    reports/all_unmatched_20261107/worker-06/research-root/proposed-owners/R-P-JCM1211-TRACE-STOCK.yaml
    reports/all_unmatched_20261107/worker-06/research-root/proposed-owners/R-P-JCM820-TRACE-STOCK.yaml
    reports/all_unmatched_20261107/worker-06/research-root/proposed-owners/R-P-DSMZ1566-GLUCOSE10.yaml
    reports/all_unmatched_20261107/worker-06/research-root/proposed-owners/R-P-SIGMA-C7290.yaml
    reports/all_unmatched_20261107/worker-06/research-root/proposed-owners/R-P-PYGS-SOURCE-EVIDENCE.yaml
    --out reports/all_unmatched_20261107/worker-06/successor-v2/final/logs/schema.tsv
    --workers 1
  exit_code: 0
  evidence_ids:
  - SCHEMA
- check_id: partonomy
  name: Native full-catalog isolated successor partonomy
  status: passed
  required: true
  summary: Actual execution passed; exact scope, inputs and result retained in reports/all_unmatched_20261107/worker-06/successor-v2/final/logs/partonomy-successor.json
  target_ids:
  - A-P-NBRC1308-TRACE
  - C-P-NBRC1356-TRACE
  - V2-P-NBRC1308-1356-TRACE
  - CM_NAME:13cefff78cf8e9a8c3f2814ab5e4406a797d0ab1ccd53fb9ea6c63036fa08e4b
  - CM_NAME:dfa4a8d37ab889934a8f5907c93a8dfbe24898eb5641f6b038c55477dd355230
  command: /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.venv/bin/python
    scripts/validate_component_partonomy.py --curated-dir .temp/all-unmatched-worker-06/successor-v2/final-validation/partonomy-overlay
  exit_code: 0
  evidence_ids:
  - PARTONOMY
- check_id: invariants
  name: Frozen and published evidence/occurrence/owner invariants
  status: passed
  required: true
  summary: Actual execution passed; exact scope, inputs and result retained in reports/all_unmatched_20261107/worker-06/successor-v2/final/logs/invariants.json
  target_ids:
  - A-P-NBRC1308-TRACE
  - C-P-NBRC1356-TRACE
  - V2-P-NBRC1308-1356-TRACE
  - CM_NAME:13cefff78cf8e9a8c3f2814ab5e4406a797d0ab1ccd53fb9ea6c63036fa08e4b
  - CM_NAME:dfa4a8d37ab889934a8f5907c93a8dfbe24898eb5641f6b038c55477dd355230
  command: /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.venv/bin/python
    .temp/all-unmatched-worker-06/successor-v2/validate_final.py
  exit_code: 0
  evidence_ids:
  - INVARIANTS
evidence:
- evidence_id: A-E-CAPTURE-149
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1308
  locator: Complete source recipe/product table and preparation; inspect the exact
    source label and context named in each case applicability; complete trace-elements
    table and surrounding receiving-medium preparation
  accessed_at: '2026-11-08T05:07:01.897272Z'
  support: supports
  summary: Full source table establishes the nominal formulation and its own occurrence
    processing. Original retrieval timestamp and capture bytes retained; no new retrieval
    is claimed.
  snapshot_sha256: d00ccd979e58433b8e97aa0d84dbee50d3aa8c571e934f39dd7f261f99a7b8be
- evidence_id: C-E-nbrc-1356
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1356
  locator: nbrc-1356; exact captured source response; complete trace-elements table
    and surrounding receiving-medium preparation
  accessed_at: '2026-11-08T05:07:36.621369Z'
  support: supports
  summary: Full source table establishes the nominal formulation and its own occurrence
    processing. Original retrieval timestamp and capture bytes retained; no new retrieval
    is claimed.
  snapshot_sha256: 87b9e6d80867f35b31318154c798b6869c3246bb526a19dccc8e8be94019dd49
- evidence_id: OWNER
  kind: search
  reference: reports/all_unmatched_20261107/worker-06/successor-v2/research-c/existing-owner-search.json
  accessed_at: '2026-11-08T06:19:55Z'
  support: supports
  summary: Bounded search of all2956 maintained owners including ignored files, plus
    full original100proposals; exact stock not established in maintained owners. Unknown
    generic stocks are not chemically disproved.
  snapshot_sha256: ae5dd4d820e402fddc4868c9f1cc1f345ec361439c6d34db8f3d705da4ae5aca
  search_scope: All2956 maintained individual YAML records and both collections, rg
    --no-ignore --hidden enumeration; NTA/formula/component/source/label candidates
    and original100 proposed owners. No global ontology or underspecified-owner absence
    claim.
- evidence_id: COMPARE
  kind: prior_review
  reference: reports/all_unmatched_20261107/worker-06/successor-v2/research-a/nbrc1308-1356-comparison.json
  accessed_at: '2026-11-08T06:19:55Z'
  support: supports
  summary: Complete table comparison and all4 frozen contexts; contribution by original1308
    author, not final independent review.
  snapshot_sha256: ab26374ea8cd9cec47a645c33f366b22cf851df727eac35270270bb2c0b2bcf0
- evidence_id: LINEAGE
  kind: record_content
  reference: reports/all_unmatched_20261107/worker-06/successor-v2/lineage.json
  accessed_at: '2026-11-08T06:19:55Z'
  support: supports
  summary: Both author histories, payloads, source links and original skeptical-review
    receipts retained unchanged.
  snapshot_sha256: 35ebf1795329c3c64233982cf463433e57b1d9cc8af871bf3c34725f330989d8
- evidence_id: REVIEW
  kind: prior_review
  reference: reports/all_unmatched_20261107/worker-06/successor-v2/research-b/scientific-review.json
  accessed_at: '2026-11-08T06:19:55Z'
  support: supports
  summary: Separate skeptical review by research_b of root-authored final shared payload
    and both exact affected outcomes.
  snapshot_sha256: f82cdd0841cf518c0e11e56c7a281f57e1e80e15f107c5f88ed6a8508710b5c2
- evidence_id: BIND
  kind: prior_review
  reference: reports/all_unmatched_20261107/worker-06/successor-v2/research-b/final-binding-v2.json
  accessed_at: '2026-11-08T06:19:55Z'
  support: supports
  summary: Final assembled successor binding:188 cases,99 payloads, all evidence and
    exact occurrence partitions; no release approval.
  snapshot_sha256: 7c1259804b8f07a12628a5013da60b52a43053b834fb2a9410b552add0909a43
- evidence_id: FINDING
  kind: prior_review
  reference: reports/all_unmatched_20261107/worker-06/successor-v2/context/confirmed-findings-supplement-v1.json
  accessed_at: '2026-11-08T06:19:55Z'
  support: supports
  summary: Non-native immutable coordinator supplement NEWOWNER-DUP-002; two original
    payloads denote one nominal formulation.
  snapshot_sha256: e309179928a0130bf05fd34f95f501bb5339bc44e4fbfd6f05ac2d6ebc11345a
- evidence_id: AUDIT
  kind: validation
  reference: reports/all_unmatched_20261107/worker-06/successor-v2/final/logs/structural-audit.json
  accessed_at: '2026-11-08T06:19:55Z'
  support: supports
  summary: Full188-case source/evidence/payload/backlink structural audit; no scientific
    approval implied.
  snapshot_sha256: 11e73d9f18d805bac208bbe9a409b70744b6c72434f3669ed67c9d19ab41093e
- evidence_id: SCHEMA
  kind: validation
  reference: reports/all_unmatched_20261107/worker-06/successor-v2/final/logs/schema-command.json
  accessed_at: '2026-11-08T06:19:55Z'
  support: supports
  summary: Actual strict schema command validates99 selected payloads.
  snapshot_sha256: e13ae747161a6c1b70825125e8c8fbdc328790388a1f7a31611c2efae557e92d
- evidence_id: PARTONOMY
  kind: validation
  reference: reports/all_unmatched_20261107/worker-06/successor-v2/final/logs/partonomy-successor.json
  accessed_at: '2026-11-08T06:19:55Z'
  support: supports
  summary: Native full-catalog partonomy validation of isolated overlay with all99
    selected proposals; no maintained installation.
  snapshot_sha256: a6a742dac61fcf77d10ba5c8bf1cac80ee2db9e69f7c4fc5f9634f922fce3590
- evidence_id: INVARIANTS
  kind: validation
  reference: reports/all_unmatched_20261107/worker-06/successor-v2/final/logs/invariants.json
  accessed_at: '2026-11-08T06:19:55Z'
  support: supports
  summary: Original1758 manifest files, sourceholds88, all188 frozen cases and97unchanged
    payloads retained; exact capture and before/after hashes verified.
  snapshot_sha256: 332a8cd491c2a4dd0efc79efc185bcbb2d5c08eb35755c13832aebb07c29b8b8
assessments:
- assessment_id: shared-formulation
  area: identity
  topic: One nominal formulation; source numbers do not distinguish substances
  outcome: supported
  summary: Both original stock proposals specify the identical13-solute and1L-water
    input table with the same NTA→NaOH pH6.5→minerals and finalpH7.0 instruction.
    One shared registry identity is justified on composition and preparation, before
    selecting the joint name/path.
  target_ids:
  - A-P-NBRC1308-TRACE
  - C-P-NBRC1356-TRACE
  - V2-P-NBRC1308-1356-TRACE
  evidence_ids:
  - A-E-CAPTURE-149
  - C-E-nbrc-1356
  - COMPARE
  - REVIEW
  - BIND
  - OWNER
  - LINEAGE
- assessment_id: unknowns
  area: quantity
  topic: Unknown titrant, water input, child forms and processing endpoints
  outcome: supported
  summary: The successor retains15 input components:13 quantified solutes,1L water
    input, and NaOH without quantity/unit. No final-volume make-up, missing hydrate
    form, equilibrium species or final-pH adjustment reagent is invented; UNKNOWN
    completeness is conservative for unspecified final adjustment, not proof that
    unquantified NaOH is absent.
  target_ids:
  - V2-P-NBRC1308-1356-TRACE
  evidence_ids:
  - A-E-CAPTURE-149
  - C-E-nbrc-1356
  - COMPARE
  - REVIEW
  - BIND
  - SCHEMA
  - PARTONOMY
  details: Exact payload SHA256 194d39c6301961eba8719f01d02762effb19c1b4a7fdfac247210f41c038127c.
    No whole-to-part identity relation or global starred synonym.
- assessment_id: case-19
  area: scope
  topic: Complete source-case reassessment and exact occurrence partition
  outcome: supported
  summary: Complete primary tables distinguish NBRC1020/824 (shared NTA/KOH stock,
    separate Se/W supplement) from NBRC1308. Independent comparison now shows that
    NBRC1308 and NBRC1356 have the same13 specified solutes,1L water input, NTA→NaOH
    pH6.5→minerals and stated finalpH7.0 preparation. Two uninstalled identities are
    therefore replaced by one reconciled nominal formulation proposal. RecipeIDs,
    footnotes and metadata differences do not establish another substance.
  details: All three original occurrences remain. Only CultureMech:007471 ingredients/8,
    source nbrc.medium:1308, occurrence CM_OCC:e689137127cd84bead1063ab24e931745a4a44fb673a953471ea3ab33e3a3df5
    uses the reconciled stock (1ml, autoclaved with receiving medium underN2/CO2 80/20).
    CultureMech:007450 ingredients/8 and CultureMech:007496 ingredients/7 remain exclusively
    A-P-NBRC1020-824-TRACE. Raw Trace element solution** is occurrence-local. No source
    file basename is used to infer the NBRC accession. NaOH quantity/concentration
    and any reagent/amount for reaching final pH7.0 remain unspecified; water is a1L
    input, not asserted final volume. Retain source-specific dose/processing and all
    existing source/owner/export holds; no global starred-label identity or post-processing
    chemical equivalence.
  target_ids:
  - CM_NAME:13cefff78cf8e9a8c3f2814ab5e4406a797d0ab1ccd53fb9ea6c63036fa08e4b
  evidence_ids:
  - A-E-CAPTURE-149
  - C-E-nbrc-1356
  - COMPARE
  - REVIEW
  - BIND
  - LINEAGE
  - INVARIANTS
- assessment_id: case-133
  area: scope
  topic: Complete source-case reassessment and exact occurrence partition
  outcome: supported
  summary: NBRC1356 has the same complete13-solute/water table and NTA/NaOH preparation
    as NBRC1308. It does not warrant a distinct whole-stock registry owner merely
    because its local label has four stars or NaOH metadata/closure were encoded differently.
    One successor proposal replaces both uninstalled proposals; unknown quantities,
    water basis and chemical forms remain explicit.
  details: The only occurrence, CultureMech:007474 ingredients/6, nbrc.medium:1356,
    CM_OCC:2c345cfde3bd9095fd0dad8782a6d904e0bf1ef8beb5c12333b78d7916f8cb03, links
    to the shared nominal formulation. Its10ml filter-sterile concentrated-stock addition
    inN2-handled medium stays distinct from1308 processing. Raw Trace element solution****
    remains local provenance, not a global synonym. Equality of nominal formulation
    does not assert identical post-processing endpoints. NaOH quantity/concentration
    and any reagent/amount for reaching final pH7.0 remain unspecified; water is a1L
    input, not asserted final volume. Retain source-specific dose/processing and all
    existing source/owner/export holds; no global starred-label identity or post-processing
    chemical equivalence.
  target_ids:
  - CM_NAME:dfa4a8d37ab889934a8f5907c93a8dfbe24898eb5641f6b038c55477dd355230
  evidence_ids:
  - A-E-CAPTURE-149
  - C-E-nbrc-1356
  - COMPARE
  - REVIEW
  - BIND
  - LINEAGE
  - INVARIANTS
findings: []
actions:
- action_id: coordinator-intake
  description: Use successor-v2/final/selection.json and its99-proposal ledger; do
    not install either superseded uninstalled owner. Integrate only through coordinator
    guarded workflows after other-worker review and source/owner/export gates.
  finding_ids: []
  target_ids:
  - A-P-NBRC1308-TRACE
  - C-P-NBRC1356-TRACE
  - V2-P-NBRC1308-1356-TRACE
  - CM_NAME:13cefff78cf8e9a8c3f2814ab5e4406a797d0ab1ccd53fb9ea6c63036fa08e4b
  - CM_NAME:dfa4a8d37ab889934a8f5907c93a8dfbe24898eb5641f6b038c55477dd355230
  ownership_note: No maintained whole-stock owner was established by the bounded ignored-inclusive
    search. These are uninstalled source/proposal artifacts, not invented maintained
    owners; intended shared path appears only in the proposal.
  acceptance_checks:
  - Preserve all four affected occurrence links and the unchanged NBRC1020/824 sibling
    stock.
  - Retain both old author/reviewer lineages and original100-proposal evidence; compare
    exact new before/after hashes.
  - Keep all88downstream holds and other source flags until separately authorized
    content-bound review resolves them.
boundary_decisions:
- action: lump
  target_ids:
  - A-P-NBRC1308-TRACE
  - C-P-NBRC1356-TRACE
  rationale: Complete primary composition and nominal stock preparation agree; separate
    identifiers/recipe accessions and different NaOH/completeness serialization do
    not establish distinct substances. Retire both uninstalled selections in favor
    of the shared successor.
  evidence_ids:
  - A-E-CAPTURE-149
  - C-E-nbrc-1356
  - COMPARE
  - REVIEW
  - BIND
  - FINDING
  proposed_groups:
  - label: V2-P-NBRC1308-1356-TRACE
    target_ids:
    - A-P-NBRC1308-TRACE
    - C-P-NBRC1356-TRACE
- action: retain
  target_ids:
  - CM_NAME:13cefff78cf8e9a8c3f2814ab5e4406a797d0ab1ccd53fb9ea6c63036fa08e4b
  - CM_NAME:dfa4a8d37ab889934a8f5907c93a8dfbe24898eb5641f6b038c55477dd355230
  rationale: Do not lump source cases or erase occurrences:case19 retains its two
    excluded NBRC1020/824 siblings; NBRC1308 and1356 doses and sterilization context
    remain distinct.
  evidence_ids:
  - A-E-CAPTURE-149
  - C-E-nbrc-1356
  - COMPARE
  - REVIEW
  - BIND
  - INVARIANTS
limitations:
- Nominal stock formulation equality does not establish identical sterilization endpoints
  or solution speciation.
- NaOH amount/concentration, any final-pH correction and final stock volume remain
  unspecified.
- The coordinator duplicate finding is a non-native supplement. It is cited exactly
  as prior evidence; no nonexistent native previous_occurrences identifier or issue
  closure is invented. No new unresolved discrepancy was found in the bounded successor
  selection.
- The existing-owner search does not prove underspecified generic stock records chemically
  different; none is sufficiently established to select as an exact owner.
- This review is not source-case, whole-owner or export approval; worker03 historical
  review of d5a7613 stays valid as historical evidence.
related_reviews:
- repository: CultureBotAI/MediaIngredientMech
  review_id: 20261108T055544Z-w06-source-shard
  relationship: Historical source-shard synthesis remains immutable; superseded only
    for the two affected decisions and two replaced proposal selections.
links:
- https://github.com/CultureBotAI/MediaIngredientMech/issues/1207
tags:
- worker06
- proposal-reconciliation
- nbrc1308
- nbrc1356
```
