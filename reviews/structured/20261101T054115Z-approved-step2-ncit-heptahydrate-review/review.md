# Approved step 2: exact NCIT heptahydrate correction and preserved approval boundary

- Review: 20261101T054115Z-approved-step2-ncit-heptahydrate-review
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-11-01T05:37:18Z
- Finished UTC: 2026-11-01T05:41:15Z
- Reviewer: Codex independent reviewer /root/step1_independent_review (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

No unresolved in-scope implementation finding remains in the frozen 40-target, 256-input review. The approved exact-form identity is implemented with one canonical row, paired rejection-owner migration and bounded generated deltas. Native QC and independent proofs pass; new mapping remains WITHHOLD and existing chemistry/BUFFER scientific holds remain OPEN.

## Scope And Provenance

40 declared targets: 35 artifacts and 5 exact mapping/rejection/unified rows. Full structural comparison covers 2,986 canonical and 4,170 unified rows; exact identity interpretation is limited to one heptahydrate and its published spellings.

Selection: Approved #875 owner, ledger, mapping and product delta; prerequisite #1028 refresh and #1029 writer repairs; their authoritative evidence, release gates and protected dependencies. No random sampling.
Coverage: full; 40 reviewed / 40 in the declared population.
Source: working_tree at Git base 40b787d37d33d544551389ff019f2d64ad63d7cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml | data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml | maintained | Na2hpo4_X_7_H2o.yaml |
| mappings/unified_mapping_rejections.tsv | mappings/unified_mapping_rejections.tsv | maintained | unified_mapping_rejections.tsv |
| scripts/promote_heptahydrate_ncit.py | scripts/promote_heptahydrate_ncit.py | maintained | promote_heptahydrate_ncit.py |
| tests/test_promote_heptahydrate_ncit.py | tests/test_promote_heptahydrate_ncit.py | maintained | test_promote_heptahydrate_ncit.py |
| src/mediaingredientmech/ingredient_bundle_refresh.py | src/mediaingredientmech/ingredient_bundle_refresh.py | maintained | ingredient_bundle_refresh.py |
| tests/test_ingredient_bundle_dependency_refresh.py | tests/test_ingredient_bundle_dependency_refresh.py | maintained | test_ingredient_bundle_dependency_refresh.py |
| tests/test_ingredient_bundle.py | tests/test_ingredient_bundle.py | maintained | test_ingredient_bundle.py |
| reports/sssom_completion_20260921/assemble_review.py | reports/sssom_completion_20260921/assemble_review.py | maintained | assemble_review.py |
| .github/workflows/qc-reviewed-sssom.yaml | .github/workflows/qc-reviewed-sssom.yaml | maintained | qc-reviewed-sssom.yaml |
| .github/workflows/qc-evidence.yaml | .github/workflows/qc-evidence.yaml | maintained | qc-evidence.yaml |
| scripts/.vendored_canon_ref | scripts/.vendored_canon_ref | maintained | .vendored_canon_ref |
| docs/SSSOM_RELEASE.md | docs/SSSOM_RELEASE.md | maintained | SSSOM_RELEASE.md |
| docs/INGREDIENT_BUNDLE.md | docs/INGREDIENT_BUNDLE.md | maintained | INGREDIENT_BUNDLE.md |
| reports/ncit_heptahydrate_875_20261101/README.md | reports/ncit_heptahydrate_875_20261101/README.md | maintained | README.md |
| reports/ncit_heptahydrate_875_20261101/execution/README.md | reports/ncit_heptahydrate_875_20261101/execution/README.md | maintained | README.md |
| data/curated/mapped_ingredients.yaml | data/curated/mapped_ingredients.yaml | generated | mapped_ingredients.yaml |
| data/curated/unmapped_ingredients.yaml | data/curated/unmapped_ingredients.yaml | generated | unmapped_ingredients.yaml |
| docs/data/label_index.csv | docs/data/label_index.csv | generated | label_index.csv |
| docs/data/ingredients.json | docs/data/ingredients.json | generated | ingredients.json |
| UNIFIED_INGREDIENT_MAPPING.tsv | UNIFIED_INGREDIENT_MAPPING.tsv | generated | UNIFIED_INGREDIENT_MAPPING.tsv |
| UNIFIED_INGREDIENT_MAPPING.provenance.json | UNIFIED_INGREDIENT_MAPPING.provenance.json | generated | UNIFIED_INGREDIENT_MAPPING.provenance.json |
| mappings/ingredient_mappings.sssom.tsv | mappings/ingredient_mappings.sssom.tsv | generated | ingredient_mappings.sssom.tsv |
| reports/sssom_completion_20260921/mapping_changes/issue875-ncit-exact-heptahydrate.json | reports/sssom_completion_20260921/mapping_changes/issue875-ncit-exact-heptahydrate.json | generated | issue875-ncit-exact-heptahydrate.json |
| reports/sssom_completion_20260921/review.json | reports/sssom_completion_20260921/review.json | generated | review.json |
| reports/sssom_completion_20260921/mapping-evidence.json | reports/sssom_completion_20260921/mapping-evidence.json | generated | mapping-evidence.json |
| reports/semantic_review_20260921/resolution/current-review.json | reports/semantic_review_20260921/resolution/current-review.json | generated | current-review.json |
| reports/semantic_review_20260921/resolution/finding-dispositions.tsv | reports/semantic_review_20260921/resolution/finding-dispositions.tsv | generated | finding-dispositions.tsv |
| reports/semantic_review_20260921/resolution/assertion-dispositions.tsv | reports/semantic_review_20260921/resolution/assertion-dispositions.tsv | generated | assertion-dispositions.tsv |
| reports/ingredient_bundle_20261101_ncit875/review.json | reports/ingredient_bundle_20261101_ncit875/review.json | generated | review.json |
| reports/ingredient_bundle_20261101_ncit875/dependency-refresh.json | reports/ingredient_bundle_20261101_ncit875/dependency-refresh.json | generated | dependency-refresh.json |
| reports/ingredient_bundle_20261101_ncit875/prior-review.json | reports/ingredient_bundle_20261101_ncit875/prior-review.json | generated | prior-review.json |
| reports/ncit_heptahydrate_875_20261101/execution/application/source-apply.json | reports/ncit_heptahydrate_875_20261101/execution/application/source-apply.json | generated | source-apply.json |
| reports/ncit_heptahydrate_875_20261101/execution/application/mapping-promotion.json | reports/ncit_heptahydrate_875_20261101/execution/application/mapping-promotion.json | generated | mapping-promotion.json |
| reports/ncit_heptahydrate_875_20261101/sources/ncit-C61946.json | reports/ncit_heptahydrate_875_20261101/sources/ncit-C61946.json | source | ncit-C61946.json |
| reports/ncit_heptahydrate_875_20261101/sources/ncit-C61946-receipt.json | reports/ncit_heptahydrate_875_20261101/sources/ncit-C61946-receipt.json | source | ncit-C61946-receipt.json |
| issue875:mapping-row | mappings/ingredient_mappings.sssom.tsv # subject_id = "MIM:Na2hpo4_X_7_H2o" AND predicate_id = "skos:exactMatch" AND object_id = "NCIT:C61946" | snapshot_row | Exact heptahydrate mapping |
| issue875:rejection-row | mappings/unified_mapping_rejections.tsv # ingredient_name = "Na2HPO4 x 7 H2O" AND rejected_id = "CHEBI:34683" AND mim_id = "NCIT:C61946" | snapshot_row | Heptahydrate stale-parent rejection |
| issue875:unified-1 | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "Na2HPO4 x 7 H2O" | snapshot_row | Na2HPO4 x 7 H2O |
| issue875:unified-2 | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "Na2HPO4.7H2O" | snapshot_row | Na2HPO4.7H2O |
| issue875:unified-3 | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "Na2HPO4·7H2O" | snapshot_row | Na2HPO4·7H2O |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Complete native QC | passed | True | data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml, mappings/unified_mapping_rejections.tsv, scripts/promote_heptahydrate_ncit.py, tests/test_promote_heptahydrate_ncit.py, src/mediaingredientmech/ingredient_bundle_refresh.py, tests/test_ingredient_bundle_dependency_refresh.py, tests/test_ingredient_bundle.py, reports/sssom_completion_20260921/assemble_review.py, .github/workflows/qc-reviewed-sssom.yaml, .github/workflows/qc-evidence.yaml, scripts/.vendored_canon_ref, docs/SSSOM_RELEASE.md, docs/INGREDIENT_BUNDLE.md, reports/ncit_heptahydrate_875_20261101/README.md, reports/ncit_heptahydrate_875_20261101/execution/README.md, data/curated/mapped_ingredients.yaml, data/curated/unmapped_ingredients.yaml, docs/data/label_index.csv, docs/data/ingredients.json, UNIFIED_INGREDIENT_MAPPING.tsv, UNIFIED_INGREDIENT_MAPPING.provenance.json, mappings/ingredient_mappings.sssom.tsv, reports/sssom_completion_20260921/mapping_changes/issue875-ncit-exact-heptahydrate.json, reports/sssom_completion_20260921/review.json, reports/sssom_completion_20260921/mapping-evidence.json, reports/semantic_review_20260921/resolution/current-review.json, reports/semantic_review_20260921/resolution/finding-dispositions.tsv, reports/semantic_review_20260921/resolution/assertion-dispositions.tsv, reports/ingredient_bundle_20261101_ncit875/review.json, reports/ingredient_bundle_20261101_ncit875/dependency-refresh.json, reports/ingredient_bundle_20261101_ncit875/prior-review.json, reports/ncit_heptahydrate_875_20261101/execution/application/source-apply.json, reports/ncit_heptahydrate_875_20261101/execution/application/mapping-promotion.json, reports/ncit_heptahydrate_875_20261101/sources/ncit-C61946.json, reports/ncit_heptahydrate_875_20261101/sources/ncit-C61946-receipt.json, issue875:mapping-row, issue875:rejection-row, issue875:unified-1, issue875:unified-2, issue875:unified-3 | Final just qc exited 0 at 2026-11-01T05:35:25Z after synchronized exports/visual metadata; log SHA 717f4c100ff3dc91fa8f46eefd4674294f4c2f0b5a2efa838ac74c1a6c11fefe. |
| Receipt replay and reviewed SSSOM validation | passed | True | mappings/ingredient_mappings.sssom.tsv, reports/sssom_completion_20260921/review.json | Native assembler replay, supported/withheld export replay and schemas pass for 2,986 canonical rows. |
| Canonical SSSOM native invariants | passed | True | mappings/ingredient_mappings.sssom.tsv | Canonical invariants pass against available actual KG transforms; missing BTO/MICRO transform limits remain explicit. |
| Product label validation | passed | True | mappings/ingredient_mappings.sssom.tsv, docs/data/label_index.csv | Native product-label command exits 0 while retaining 101 nonblocking warnings and 5,312 pairs without an adapter; this is not complete label approval. |
| Native semantic report integrity | passed | True | reports/semantic_review_20260921/resolution/current-review.json | Current-review integrity passes while complete scientific release remains FAIL. |
| Supported graph and excluded backlog replay | passed | True | reports/semantic_review_20260921/resolution/current-review.json | Native supported-KGX replay validates exact approved selection and retained excluded claims. |
| Companion portable validation | passed | True | reports/ingredient_bundle_20261101_ncit875/review.json, reports/ingredient_bundle_20261101_ncit875/dependency-refresh.json | Native companion validates its manifest, source/evidence bindings and all complete claim payloads. |
| Receipt and release regression tests | passed | True | reports/sssom_completion_20260921/assemble_review.py, src/mediaingredientmech/ingredient_bundle_refresh.py | Final post-generation regression suite passes 207 tests; prior stale-unified failure remains historical diagnostic only. |
| Maintained writer audit | passed | True | scripts/promote_heptahydrate_ncit.py | Native writer audit passes for the final maintained writer. |
| Unified rejection and freshness gates | passed | True | UNIFIED_INGREDIENT_MAPPING.tsv, UNIFIED_INGREDIENT_MAPPING.provenance.json | Native stamp and rejection/freshness checks pass after completed unified generation. |
| Independent writer and refresh regression tests | passed | True | scripts/promote_heptahydrate_ncit.py, tests/test_promote_heptahydrate_ncit.py, src/mediaingredientmech/ingredient_bundle_refresh.py, tests/test_ingredient_bundle_dependency_refresh.py | 133 tests pass, including current published heptahydrate surfaces and both prerequisite repairs. |
| Independent complete applied-data and candidate-hash verification | passed | True | data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml, mappings/unified_mapping_rejections.tsv, mappings/ingredient_mappings.sssom.tsv | All 2,691 generation inputs, four label maps, five comparison inputs and actual source, promotion, receipt and journal hashes verified; exact bounded data scope preserved. |
| Independent successor and artifact proof | passed | True | UNIFIED_INGREDIENT_MAPPING.tsv, reports/ingredient_bundle_20261101_ncit875/review.json, reports/semantic_review_20260921/resolution/current-review.json | Exact companion/audit replay, complete unified delta and preservation of non-target scientific decisions pass; all 18,873 unified input hashes independently verified. |
| Independent real-native reservation regression | passed | True | scripts/promote_heptahydrate_ncit.py, tests/test_promote_heptahydrate_ncit.py | All 16 independent reservation-replacement cases refuse false completion and preserve required recovery evidence. |
| Portable evidence inventory verification | passed | True | reports/ncit_heptahydrate_875_20261101/execution/README.md | 185 archived files verified; two supplemental independent proof files separately verified. |
| Optional live EVS recheck | unavailable | False | reports/ncit_heptahydrate_875_20261101/sources/ncit-C61946.json | The web tool could not access this API endpoint. Complete archived official response and its successful HTTP fetch receipt were inspected and hash-verified. |

## Scientific And Domain Assessments

### Approved exact supplied-form identity

identity: supported. Targets: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml, issue875:mapping-row, reports/ncit_heptahydrate_875_20261101/sources/ncit-C61946.json, reports/ncit_heptahydrate_875_20261101/sources/ncit-C61946-receipt.json.

The approved record denotes disodium hydrogenphosphate heptahydrate. The inspected NCI database assertion names that exact form and agrees with its CAS/formula; NCIT:C61946 replaces the local identity and anhydrous-parent mapping under section 3 step 1.

This assessment supports the bounded implementation identity choice. It does not approve inherited anhydrous InChI/SMILES or provisional BUFFER, and it does not create a native positive mapping disposition.

### Append-only owner evidence and history

provenance: supported. Targets: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml, reports/ncit_heptahydrate_875_20261101/execution/application/source-apply.json.

Exactly one history event and one mapping-evidence entry are appended. All earlier history/evidence and unrelated owner fields remain identical. Actual source receipt hashes bind paired owner/ledger application; historical applied producer is preserved separately from the repaired producer.

### Paired rejection-owner migration

consistency: supported. Targets: mappings/unified_mapping_rejections.tsv, issue875:rejection-row.

The 90-row ledger changes exactly the heptahydrate owner and rationale to NCIT:C61946. CHEBI:34683 remains rejected in unified identity columns; all other rows and the existing 33 source holds remain unchanged.

### Guarded publication and recovery

representation: supported. Targets: scripts/promote_heptahydrate_ncit.py, tests/test_promote_heptahydrate_ncit.py.

The bounded writer validates exact input/candidate hashes, rejects partial or duplicate-destination states, preserves history and non-target rows, and treats a true repeat as a no-op. The repaired writer checks held reservation identities before mutation and around completion; all independent native race probes refuse false success.

Individual replacements are atomic; a multi-file I/O failure may require explicit native-journal recovery. The writer does not claim whole-transaction filesystem atomicity or silently overwrite another writer’s evidence.

### One exact mapping and bounded canonical promotion

grounding: supported. Targets: mappings/ingredient_mappings.sssom.tsv, reports/ncit_heptahydrate_875_20261101/execution/application/mapping-promotion.json, reports/sssom_completion_20260921/mapping_changes/issue875-ncit-exact-heptahydrate.json.

The 2,979-row diagnostic candidate contributes only the exact target row. Canonical SSSOM changes 2,987 to 2,986 rows: one ontology slot changed and one obsolete local registry row removed; every unrelated byte is preserved. Accepted hydrate aliases/CAS and historical provenance remain; obsolete ChEBI validation stamp is cleared.

### Synchronized maintained and generated surfaces

consistency: supported. Targets: data/curated/mapped_ingredients.yaml, data/curated/unmapped_ingredients.yaml, docs/data/label_index.csv, docs/data/ingredients.json.

Both aggregate collections preserve all non-target records and agree with the final owner. Full QC validates current indexes, browser/list exports and visualization metadata; only the target identity metadata changes in the visual products.

### Complete unified comparison with bounded identity interpretation

consistency: supported. Targets: UNIFIED_INGREDIENT_MAPPING.tsv, UNIFIED_INGREDIENT_MAPPING.provenance.json, issue875:unified-1, issue875:unified-2, issue875:unified-3.

All 4,170 rows were structurally compared. Exactly three target spellings change mim_id and gain the NCI label; 4,167 rows, every occurrence count and recipe example remain identical. All 18,873 generation input hashes verify. No REJECTED row has an empty mim_id and no kgmicrobe.compound row leaks CHEBI.

### Location changes without scientific approval

provenance: supported. Targets: src/mediaingredientmech/ingredient_bundle_refresh.py, tests/test_ingredient_bundle_dependency_refresh.py, reports/ingredient_bundle_20261101_ncit875/review.json, reports/ingredient_bundle_20261101_ncit875/dependency-refresh.json, reports/ingredient_bundle_20261101_ncit875/prior-review.json.

The maintained refresh preserves all 20 owners, 51 complete claims/decisions, selected row payloads and complete resolved evidence. Fourteen verified locations move; source_position and evidence_key alone are excluded from semantic decision comparison. Native successor bytes and every audit field replay exactly; no approval is added.

### Retained mapping-specific withholding

scope: supported. Targets: reports/sssom_completion_20260921/assemble_review.py, reports/sssom_completion_20260921/review.json, reports/sssom_completion_20260921/mapping-evidence.json, docs/SSSOM_RELEASE.md.

The 16th receipt preserves the full prior chain and grants no approval. The new NCIT row remains WITHHOLD. Every other mapping decision and complete evidence entry is preserved through the position map; 1,740 supported and 1,246 withheld rows remain explicit.

### Preserved unresolved chemistry and role findings

scope: supported. Targets: reports/semantic_review_20260921/resolution/current-review.json, reports/semantic_review_20260921/resolution/finding-dispositions.tsv, reports/semantic_review_20260921/resolution/assertion-dispositions.tsv.

The target BUFFER assertion remains OPEN and the two existing finding rows update only owner hashes. Nonmapping approvals are unchanged. Full scientific release remains FAIL with 1,733 blocking findings and 2,271 blocking assertions; one withheld registry assertion was removed, with no new approval.

### Explicit companion selection and protected dependencies

ownership: supported. Targets: .github/workflows/qc-reviewed-sssom.yaml, tests/test_ingredient_bundle.py, docs/INGREDIENT_BUNDLE.md, .github/workflows/qc-evidence.yaml, scripts/.vendored_canon_ref.

CI, public instructions and integration tests explicitly select the verified immutable successor. Prior reports remain preserved. The evidence workflow and canonical validator pin are byte-identical to durable baseline 40b787d.

### Portable evidence and explicit execution limits

provenance: supported. Targets: reports/ncit_heptahydrate_875_20261101/README.md, reports/ncit_heptahydrate_875_20261101/execution/README.md.

Portable reports preserve exact source/candidate/application/receipt evidence, original failures and repaired results, historical producer bytes, and the complete QC snapshot. Diagnostic 2,979-row candidate, final 2,986-row canonical table, native approval boundaries and incomplete ontology-adapter coverage are distinguished.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml, issue875:mapping-row. Keep the specific seven-water substance distinct from anhydrous and sibling hydrates; use the approved exact NCIT term rather than the superseded local/parent pair.
- defer: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml, reports/semantic_review_20260921/resolution/current-review.json. Preserve open chemistry/BUFFER findings and mapping WITHHOLD. No full-record or positive native mapping approval follows from this bounded implementation review.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| authority | MAPPING_SEMANTICS.md | supports | Section 3 step 1 selects an exact supplied-form ontology term and one exact row; unrelated chemistry and roles remain separate claims. |
| profile | docs/record-review-profile.md | supports | Native review does not replace scientific release approvals or resolve existing claim holds. |
| owner | data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml | supports | Inspected exact heptahydrate identity, retained CAS/aliases/rejected sibling labels, complete history and explicit unresolved chemistry/BUFFER caveats. |
| ncit | reports/ncit_heptahydrate_875_20261101/sources/ncit-C61946.json | supports | Complete archived official EVS response: active C61946 in NCIt 26.10d, exact heptahydrate label, CAS 7782-85-6, formula 2Na.HO4P.7H2O and UNII 70WT22SF4B. This is a database assertion. |
| ncit_receipt | reports/ncit_heptahydrate_875_20261101/sources/ncit-C61946-receipt.json | supports | Official endpoint, HTTP 200, actual retrieval time and exact archived source hash. |
| applied | reports/ncit_heptahydrate_875_20261101/execution/final-checks/independent-review/applied-verification.json | supports | Independent actual-data checks verify owner/history/ledger scope, both aggregate collections, all 2,691 candidate input hashes, all receipt bindings and canonical one-changed-row/one-removed-row scope. |
| products | reports/ncit_heptahydrate_875_20261101/execution/final-checks/independent-review/products-verification.json | supports | Independent exact companion/audit replay; all non-target mapping evidence and approvals retained; three unified rows changed and all other rows identical. |
| unified_inputs | reports/ncit_heptahydrate_875_20261101_unified_review/unified-input-verification.json | supports | Independent verification of all 18,873 actual unified-generation input hashes and producer, baseline, before/after artifact bindings. |
| candidate | reports/ncit_heptahydrate_875_20261101/execution/generation/generation-receipt.json | supports | Native diagnostic candidate binds producer 0cc221bd, all generation inputs, returned label maps and prior validation stamps; no approval supplied. |
| source_apply | reports/ncit_heptahydrate_875_20261101/execution/application/source-apply.json | supports | Completed actual source application binds exact owner and coupled rejection-ledger hashes; no scientific approval. |
| promotion | reports/ncit_heptahydrate_875_20261101/execution/application/mapping-promotion.json | supports | Actual bounded promotion binds source receipt and candidatehash, records one changed ontology row and one removed registry row. |
| receipt | reports/sssom_completion_20260921/mapping_changes/issue875-ncit-exact-heptahydrate.json | supports | Approval-free chain link 16 preserves prior full rows and position map, exact owner before/after hashes, and inspected verification. |
| race_before | reports/ncit_heptahydrate_875_20261101/execution/final-checks/independent-review/reservation-race.json | supports | Original real-native probe shows source changes and false success after receipt/backup reservation replacement; supports filed-before-fix#1029. |
| historical_writer | reports/ncit_heptahydrate_875_20261101/execution/final-checks/independent-review/writer-before-reservation-fix.py | supports | Exact producer used for historical application is preserved separately from the repaired writer. |
| race_after | reports/ncit_heptahydrate_875_20261101/execution/final-checks/independent-review/reservation-fixed/results.json | supports | Independent repaired real-native 16 cases refuse false completion, preserve competitors, avoid precommit mutation, and retain postcommit recovery journals. |
| tests | reports/ncit_heptahydrate_875_20261101/execution/final-checks/independent-review/focused-tests-fixed.log | supports | Independent writer/refresh suite passes 133 tests including actual regenerated surfaces and native transactions; 12 dependency deprecation warnings. |
| refresh | reports/ingredient_bundle_20261101_ncit875/dependency-refresh.json | supports | Native unchanged-cohort receipt preserves 20 owners and 51 claims, records 14 verified location changes and explicitly adds no scientific approval. |
| visual | reports/ncit_heptahydrate_875_20261101/execution/final-checks/visualization-delta.json | supports | Both 2,340-node visualization products change only five target identity/mapping metadata fields; all other nodes and coordinates remain unchanged. |
| inventory | reports/ncit_heptahydrate_875_20261101/execution/inventory.json | supports | Frozen 185-file portable execution inventory includes original failures, corrected gates and independent review proof. |
| supplement | reports/ncit_heptahydrate_875_20261101_unified_review/inventory.json | supports | Append-only two-file supplement preserves the late independent unified-input proof without changing the earlier frozen inventory. |
| documentation | reports/ncit_heptahydrate_875_20261101/README.md | supports | Approved bounded identity, writer operation, receipt provenance and explicit separate chemistry/BUFFER limitations. |
| full_qc_receipt | reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-full-qc-after-exports.json | supports | Final just qc exited 0 at 2026-11-01T05:35:25Z after synchronized exports/visual metadata; log SHA 717f4c100ff3dc91fa8f46eefd4674294f4c2f0b5a2efa838ac74c1a6c11fefe. Actual command, times, exit status and log digest retained. |
| full_qc_log | reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-full-qc-after-exports.log.gz | supports | Final just qc exited 0 at 2026-11-01T05:35:25Z after synchronized exports/visual metadata; log SHA 717f4c100ff3dc91fa8f46eefd4674294f4c2f0b5a2efa838ac74c1a6c11fefe. Inspected final log; gzip when used is lossless. |
| mapping_qc_receipt | reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-reviewed-sssom-qc.json | supports | Native assembler replay, supported/withheld export replay and schemas pass for 2,986 canonical rows. Actual command, times, exit status and log digest retained. |
| mapping_qc_log | reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-reviewed-sssom-qc.log | supports | Native assembler replay, supported/withheld export replay and schemas pass for 2,986 canonical rows. Inspected final log; gzip when used is lossless. |
| canonical_invariants_receipt | reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-canonical-invariants-actual-kg.json | supports | Canonical invariants pass against available actual KG transforms; missing BTO/MICRO transform limits remain explicit. Actual command, times, exit status and log digest retained. |
| canonical_invariants_log | reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-canonical-invariants-actual-kg.log | supports | Canonical invariants pass against available actual KG transforms; missing BTO/MICRO transform limits remain explicit. Inspected final log; gzip when used is lossless. |
| product_labels_receipt | reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-product-labels.json | supports | Native product-label command exits 0 while retaining 101 nonblocking warnings and 5,312 pairs without an adapter; this is not complete label approval. Actual command, times, exit status and log digest retained. |
| product_labels_log | reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-product-labels.log | supports | Native product-label command exits 0 while retaining 101 nonblocking warnings and 5,312 pairs without an adapter; this is not complete label approval. Inspected final log; gzip when used is lossless. |
| semantic_integrity_receipt | reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-semantic-integrity.json | supports | Current-review integrity passes while complete scientific release remains FAIL. Actual command, times, exit status and log digest retained. |
| semantic_integrity_log | reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-semantic-integrity.log | supports | Current-review integrity passes while complete scientific release remains FAIL. Inspected final log; gzip when used is lossless. |
| supported_kgx_receipt | reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-supported-kgx-qc.json | supports | Native supported-KGX replay validates exact approved selection and retained excluded claims. Actual command, times, exit status and log digest retained. |
| supported_kgx_log | reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-supported-kgx-qc.log | supports | Native supported-KGX replay validates exact approved selection and retained excluded claims. Inspected final log; gzip when used is lossless. |
| companion_validate_receipt | reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-companion-validate.json | supports | Native companion validates its manifest, source/evidence bindings and all complete claim payloads. Actual command, times, exit status and log digest retained. |
| companion_validate_log | reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-companion-validate.log | supports | Native companion validates its manifest, source/evidence bindings and all complete claim payloads. Inspected final log; gzip when used is lossless. |
| receipt_tests_receipt | reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-receipt-regression-tests-after-generation.json | supports | Final post-generation regression suite passes 207 tests; prior stale-unified failure remains historical diagnostic only. Actual command, times, exit status and log digest retained. |
| receipt_tests_log | reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-receipt-regression-tests-after-generation.log | supports | Final post-generation regression suite passes 207 tests; prior stale-unified failure remains historical diagnostic only. Inspected final log; gzip when used is lossless. |
| writer_audit_receipt | reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-writer-audit.json | supports | Native writer audit passes for the final maintained writer. Actual command, times, exit status and log digest retained. |
| writer_audit_log | reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-writer-audit.log | supports | Native writer audit passes for the final maintained writer. Inspected final log; gzip when used is lossless. |
| freshness_receipt | reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-unified-stamp.json | supports | Native stamp and rejection/freshness checks pass after completed unified generation. Actual command, times, exit status and log digest retained. |
| freshness_log | reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-unified-stamp.log | supports | Native stamp and rejection/freshness checks pass after completed unified generation. Inspected final log; gzip when used is lossless. |

## Limits And Additional Notes

- This structural/provenance-focused review includes bounded exact-form identity checks only; scientific_review is false and no native approval is authored.
- Inherited anhydrous InChI/SMILES and provisional BUFFER evidence remain unresolved. Full scientific release remains FAIL with 1,733 blocking findings and 2,271 blocking assertions.
- Native canonical invariants skip B4 where BTO and MICRO transform inputs are absent. Product label validation retains 101 nonblocking warnings and 5,312 pairs without an adapter; no comprehensive ontology-label approval is claimed.
- A live web-tool EVS recheck was unavailable. The complete official response fetched at 2026-11-01T04:19:28Z and its exact hash-bound HTTP receipt were inspected instead.
- Root executed full native QC and release gates; the reviewer verified their exact receipts/logs and independently ran 133 focused tests, real-native race probes, all candidate/unified input hashes and complete bounded artifact/approval comparisons.
- The native source is the actual working tree on durable merged base 40b787d with frozen index ad33965a8b3f599aec721ca84f7eeb3658be7379. Final committed-head verification and remote CI remain separate subsequent requirements.
- #1028 and #1029 were filed before fixes. Original failure probes and historical applied writer are retained alongside repaired checks. They were not earlier structured findings; no previous_occurrences or invented terminal finding dispositions are created.
- Historical pre-generation test/QC failures and the incorrect comment-filtered TSV comparison remain explicit diagnostics; final corrected runs and the proper plain-TSV comparison support this review.
- This review captures 235 staged file hashes and full index/tree equality before inspecting 256 native inputs. No source revision was relabeled and no transient feature commit was used.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261101T054115Z-approved-step2-ncit-heptahydrate-review
kind: repository
repository: CultureBotAI/MediaIngredientMech
title: 'Approved step 2: exact NCIT heptahydrate correction and preserved approval
  boundary'
started_at: '2026-11-01T05:37:18Z'
finished_at: '2026-11-01T05:41:15Z'
reviewer:
  identity: Codex independent reviewer /root/step1_independent_review
  kind: agent
  independence: independent
  independence_basis: Reviewer authored no implementation, repository tests, ingredient
    data, rejection ledger or generated products. Root and a separate implementation
    agent authored the changes. Reviewer identified defects, wrote external read-only
    probes and this review only; a separate edge reviewer also inspected the refresh
    fix.
skill: curate-yaml-record (audit-only); review-sssom-output contract
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: No unresolved in-scope implementation finding remains in the frozen 40-target,
  256-input review. The approved exact-form identity is implemented with one canonical
  row, paired rejection-owner migration and bounded generated deltas. Native QC and
  independent proofs pass; new mapping remains WITHHOLD and existing chemistry/BUFFER
  scientific holds remain OPEN.
source:
  git_revision: 40b787d37d33d544551389ff019f2d64ad63d7cc
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/SKILL.md
    sha256: 4ea8fcaf92b4c05f17c6bee8daa9485bc58da1bb93103a53a582dc1a891b6f7a
    role: context
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: d4df94935abfd922e84c3512e9a9b7735240f8e266d9a3ae23bb4933926b04eb
    role: context
  - path: .github/workflows/qc-evidence.yaml
    sha256: 288ef1795582105763952c4104d1455c1fef273a65528949f1e558d39c7306f3
    role: target
  - path: .github/workflows/qc-reviewed-sssom.yaml
    sha256: 70a6cf78722adb6f29630c8c032403641026b7bb2554578cd91fafdcd0a82321
    role: target
  - path: AGENTS.md
    sha256: fc7728986d82b43359a9055ae233bcf0d4ebaef8bb657ef1b4bb4aa87b2cbaaf
    role: context
  - path: MAPPING_SEMANTICS.md
    sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
    role: context
  - path: UNIFIED_INGREDIENT_MAPPING.provenance.json
    sha256: 0f828858e17f867db967f589a72cdb0e6a8fbc3091aae63a2a4ab730094e7108
    role: target
  - path: UNIFIED_INGREDIENT_MAPPING.tsv
    sha256: 6126d33febe2a577ff60295a36d6e5dd649a39e73c218f4d18468f3813adbce9
    role: target
  - path: conf/record_review.yaml
    sha256: 07a8fa6d17ee664c7a2bc2d5b5821bd106f6aa454299b4f3e0440176876cd82e
    role: context
  - path: data/curated/ALL_INGREDIENTS.md
    sha256: 46a9b035fb9462ae4db4473973aa3ccd9db7dbab1c51b873ff577bec8561ff71
    role: context
  - path: data/curated/MAPPED_INGREDIENTS.md
    sha256: e1677f3e7f08300438a068264fb631f3a4c0b72ae81a96fd7e0b68718990accd
    role: context
  - path: data/curated/all_ingredients_index.csv
    sha256: ee09f438202e3b9eb4a81bca0fedbcde5b43f1bc98743e9f7025cfd9dfe6436b
    role: context
  - path: data/curated/all_ingredients_index.json
    sha256: 6129e3e856f4d952026bc63c031afbec659120d552848d3f1e1242a7c09460e0
    role: context
  - path: data/curated/mapped_ingredients.yaml
    sha256: 2bc4b3663ea6beae04693bd517e2901ce69cf912d828599a0b1f7c19d2f8ba77
    role: target
  - path: data/curated/mapped_ingredients_index.csv
    sha256: db1320e75f1128b26febf9742a4b253053e688dbfbd3896b705a8ba9341e5d92
    role: context
  - path: data/curated/mapped_ingredients_index.json
    sha256: 4e8f64ed64b3dac29e5829d76ab7c84802a781f94054ff45735157bd4b674c35
    role: context
  - path: data/curated/unmapped_ingredients.yaml
    sha256: 22ececf4e0e7a37ca0636d4635ed5408a6517ba7ef6e7a1daf713f09a7802cd8
    role: target
  - path: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
    sha256: 6e816ef6a1dad8dab9c3ddd711ca84d8a3489bedb175d540ea3cb618c7068873
    role: target
  - path: docs/INGREDIENT_BUNDLE.md
    sha256: 03cbd45a57a57de8acc3cfe01bcdcf50f4b9fdefdc664552bfd679eb8eeb88b9
    role: target
  - path: docs/SSSOM_RELEASE.md
    sha256: 348f1489c606d96df806b0c90582b46ed31756dc69d3da2b3b5d131e734f4e25
    role: target
  - path: docs/UNIFIED_MAPPING_REJECTIONS.md
    sha256: b0989f6b82dd40e6a3593c297935aaf21c8f9fc6591b456e484e38e78d3a3317
    role: context
  - path: docs/data/all_ingredients.csv
    sha256: a71b787316565bcd452e4b82e51dfecc6e5ad7a4d17feaf13add3e8565d36e36
    role: context
  - path: docs/data/all_ingredients.json
    sha256: 66ef00902dc1097d3747a219b5a866b9f9feeb7de73284f3e077796c83d88601
    role: context
  - path: docs/data/all_ingredients.md
    sha256: b46f0c2f2a3387e5b15645eb52ab42d83473e28babb284bdfe4956bc2e13d27c
    role: context
  - path: docs/data/ingredient_graph.json
    sha256: 33210b7ee9422ac600fdd75f9e7729cbc959f9319996bfd8af019ffdf2e30769
    role: context
  - path: docs/data/ingredient_umap.json
    sha256: 60e39651d79798fcac92e03f39727e73d2298d9e5204fad3f329da7bc7fbe7b7
    role: context
  - path: docs/data/ingredients.json
    sha256: 843f3ab4bcf5a6fd412491fbb348f04969fe2ac6183dd74f4a1382c895c7abc2
    role: target
  - path: docs/data/label_index.csv
    sha256: 97488a74286f196abed443eab72401531b0edbb27b29a3218525dff8299f703f
    role: target
  - path: docs/data/mapped_ingredients.csv
    sha256: 5ddc4dadb117160ebddd0a425c1f46885dc35ff0a6306bcbb7475afb7a1ef8a2
    role: context
  - path: docs/data/mapped_ingredients.json
    sha256: 8f6ddf0dfee4b4e4aafa553259210b16aa9f9f36f07e58cf825e7da097f8186c
    role: context
  - path: docs/data/mapped_ingredients.md
    sha256: 962b070d1e8b8d9e3df889b91a3ee646d27b4281e0897bdd08b3aa31ead747c3
    role: context
  - path: docs/data/unmapped_ingredients.md
    sha256: f81d931b9a8422974e3ac1252c74bcfe5537300606a600b86f14477d8109599e
    role: context
  - path: docs/record-review-profile.md
    sha256: da17e2048a13514a422bc94bd2f8d48943cffc5689b96e3f07da26423248d1a7
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: a1237b64f4a5e11a473e99b34ed88b4a0d3a7f23e701bca649248325d83ba57a
    role: context
  - path: mappings/ingredient_mappings.sssom.tsv
    sha256: 68552edd452d5dccf1262b5d03190a6b668341952a554f349149f269403cca67
    role: target
  - path: mappings/unified_mapping_rejections.tsv
    sha256: 717289ca0e45046dcb96f6839b843838a6636fd8e120cf4d9b9ac48de3d9016d
    role: target
  - path: reports/ingredient_bundle_20261101_ncit875/README.md
    sha256: 345fab013b72a195cfefc668137e968863e6c2772bcf287fb0c69d3cd3022c24
    role: context
  - path: reports/ingredient_bundle_20261101_ncit875/dependency-refresh.json
    sha256: 3e422eeffe4ba4415a46314cd69f086a23d46ce3e164bb06aa1782eeb1c15a09
    role: target
  - path: reports/ingredient_bundle_20261101_ncit875/prior-review.json
    sha256: d391ec9e0dc004494431f76a81c392efef114746e7bf1eca57c7ce4dc7dec14c
    role: target
  - path: reports/ingredient_bundle_20261101_ncit875/review.json
    sha256: 7ea74db32bcc33b464a39101e9d81319729dcc73ffd2eba997fa8c99cfb735f5
    role: target
  - path: reports/ncit_heptahydrate_875_20261101/README.md
    sha256: 1e04dc58c21b76fc7d5fb90c49b7f8f4e8141417f868eb69680e897dd6785e7e
    role: target
  - path: reports/ncit_heptahydrate_875_20261101/execution/README.md
    sha256: 2e5fa5932c20329d5a5f3266f4ce2e8722e85e5510382a4a4556ffaf80f30ac1
    role: target
  - path: reports/ncit_heptahydrate_875_20261101/execution/application/mapping-promotion.json
    sha256: 6f2688c95739c65106a79c535b7a6513c5ad6d2a6d4a6c0c0251a4d114ac8b41
    role: target
  - path: reports/ncit_heptahydrate_875_20261101/execution/application/receipt-publication.json
    sha256: 0d3d1f417d2589f401e0d7d366ac755bcaee9d34e0011733359bb7bae9ac86c6
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/application/source-apply.before-ledger.tsv
    sha256: 82d7d79172a5efd966f0a6a97ead4faae186128f6d6fdb327366f041ad06aba4
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/application/source-apply.before.yaml
    sha256: e4f20bded8bb984f76d381636cf79b522983413046bf24bc6168e1065c027636
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/application/source-apply.json
    sha256: b24dab0665d4e2c6508ea13bbf39dc0ebb85b69241dc856a613000bc37944326
    role: target
  - path: reports/ncit_heptahydrate_875_20261101/execution/artifact-locations.json
    sha256: 36e291a97b1890ae63309e9b0576610a70efb9fe34246c684dca19d9be660001
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/context.json
    sha256: 0270b3fbb94b86bce5a63e685991971012f033629e59bac757017621e509f0b2
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/excerpts/before-target.tsv
    sha256: 0998451597630a5c571051e9bc279416915b2dd04c3c765f6db6c09c2d65f5e0
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/excerpts/candidate-target.tsv
    sha256: f72028c6dff4fd0d58f73eb7b7cc9307927dfc18339bebf17968259ad4b0f3a3
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/excerpts/canonical-target.tsv
    sha256: 67a56d28955151eb632371df98a5868525e2ebbdf885ee8454267e349f92838d
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/excerpts/mapping-review-target.json
    sha256: d4b5b83f132b177a6190de6ed62f4a3dd6e3a052e561f1087ad405eea96d0e96
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/README.md
    sha256: df3dc80d626cf110088b30ef98c68baeb7fb3933639394a8998307735fe05caf
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/canonical-invariants/receipt.json
    sha256: 103b5048a0c14e9c5727b0be4f6453a0acd8123e195614b1636dcb61361eef97
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/canonical-invariants/rejects.tsv
    sha256: 9401ca51a25ee4f9a0aadafa73cc8f9266d0ffc60df7f037d1727e482367fc7f
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/harnesses/analyze_step2_final.py
    sha256: 3099c70a843c54a84af5df56ea8557f509fdc7ab8680e3915688479f961cc5b4
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/harnesses/guarded_unified_revision.py
    sha256: 889c609593c98a3ebbd998d0db717e8606f9e9fd394f8c7d18a0557c06f30149
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/independent-review/applied-verification.json
    sha256: d815db12ad00056fce3518d762d0d304da65535b5b7ab2ffa8fe638a06133242
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/independent-review/applied-verification.log
    sha256: 74c6f61a6b98d0d2a6d5016a290872348b6786504a02aa8f2e82aa812dda1fa4
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/independent-review/evidence-index.json
    sha256: a9bfa9b60de957e6c28bfd16f00a7f3d2d839b5b29d240e883ab95d8d08450b8
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/independent-review/focused-tests-fixed.log
    sha256: 257e5b10abe05922a55c7cea19d54fcb2525574b9a4a3c900ceecfcff6b19d14
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/independent-review/focused-tests.log
    sha256: 90063dfa901461484dee9ef160d1f921ce0dcaedd610e822e5f6b8b8a806cccd
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/independent-review/probe_reservation_fixed.py
    sha256: e7cb7bb9e9d53f7321d1157e95aa353105696a66d6577f44ac1061da71f40579
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/independent-review/probe_reservation_race.py
    sha256: 6b3ed3ee1e0083cdf6e8ead0eb8216d912542d4c7242060e525a56131a19261e
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/independent-review/products-verification.json
    sha256: 7cb98bd00d9c4f27ba88f0a17277244fd052b4cf847a191a16cb189e62f19182
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/independent-review/products-verification.log
    sha256: 8bc3779b1a7edd08d6f7aed3ca246dad8712f510e519ca759991d412f5a8e0e4
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/independent-review/reservation-fixed.log
    sha256: 51605401ac3e7b94fe2c6e1a80c1f4324e0e40889f210425ab1837dceeeccb20
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/independent-review/reservation-fixed/results.json
    sha256: 691709b8a12cd004f711318230470f10e6a58b4fecee07494ffe20679a85e7d9
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/independent-review/reservation-race.json
    sha256: e7d2d840b53eee5dbb3a23cdc372a7ff961a5504020817deccef997a78021085
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/independent-review/reservation-race.log
    sha256: e7d2d840b53eee5dbb3a23cdc372a7ff961a5504020817deccef997a78021085
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/independent-review/review.md
    sha256: 41f1ccf8d32e3255828c1a5195b66e22ff774bda4160ea64157559cd183173ac
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/independent-review/verify_applied.py
    sha256: 2912a0f1444904ebe550077256447a4a327cfe1ad31024f322074f7ba9b0504a
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/independent-review/verify_products.py
    sha256: 17d474a9625ce12127224dff81fcf9cc95abafbd7cc4d9ea45b716bfb1cf475b
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/independent-review/writer-before-reservation-fix.py
    sha256: a66389a3379a761ee263aceb08222b6508f57cb9b8e69e996e82af732b59bb85
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/initial-artifact-locations.json
    sha256: 246e3bef34a64c4c701d5e499763df87bd025c1b7931d56162c5ed70602d9873
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-assemble-review.json
    sha256: c23df9a081230a35e669cbae039a4a12003a64b3348bdba6f1819ccb179f6387
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-assemble-review.log
    sha256: 623224fefd78d12969ac84056e2194844977c5c701550885daf1b401a62ca382
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-bounded-delta-correct-tsv-reader.json
    sha256: d9ef1d080bd2553d31ecaabe33ed9853870c2d43960cbb33a3e369c1aaa2fb96
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-bounded-delta-correct-tsv-reader.log
    sha256: 7f7db8caaab6d9ce14f5c2f96b4e4963c36d67d7e9a7f4409273dfae887b6d4f
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-canonical-invariants-actual-kg.json
    sha256: 1967ed8fae5804e940cf9549fc5b9e757e0b8c43f2ecf245aa45fd0dc73c25f8
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-canonical-invariants-actual-kg.log
    sha256: e359124fa08279491b2032a31f005a93801de8104eb3cb9a81264637c5baa910
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-companion-export.json
    sha256: ca972edd1d6aec3f0b769202450b83dc3233a49636bfa8c56e4a3ff71a60a527
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-companion-export.log
    sha256: 3e86f5a9b08481d3e0845ef5787355048f4a1d36a5af9946ec02ffe1b4b605c8
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-companion-refresh.json
    sha256: a6b657db189aaad21d30501e38512be24d74d0694989dad01150c6de73a8d1c2
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-companion-refresh.log
    sha256: 44150a692785956fdd4b537d4b037590de05f14a3729d97d409f62e9f064a7fa
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-companion-regression-tests.json
    sha256: a469d1d1d576a80249150d22509250f5b196e25abad0d56dca90ad1c376f184f
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-companion-regression-tests.log
    sha256: 875c3c5c4441fcfe21d55c181f56f4f024493c8d55d5522c93747bb6bea1fbde
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-companion-validate.json
    sha256: ecfa9021094032cf3aa228402f473143781a036fba398568c9befd7ddca0d785
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-companion-validate.log
    sha256: ce1e341213b171743cc30ebffe8905ffed4d4d4edbf8ab4d35f184dfdf154d41
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-focused-refresh-tests.json
    sha256: 4053a03049ba09ac4753c3a106cc2bd33bd383d1018edbf491490365152c8085
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-focused-refresh-tests.log
    sha256: 1fabedf6dbbdae288b3949354e71e8f3f196da9ff75f3f37788364bfe2d7830a
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-full-kgx.json
    sha256: 5a1a4f9c1376124969e063611222552bdf52f926712e076c03ba78411fc8c345
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-full-kgx.log
    sha256: 308a823acf7e18474b76c9e547ec336af6c28bb777a47ebe53271bc5f22565ed
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-full-qc-after-exports.json
    sha256: af40b8b3761d54be0b96a9b7a5bbebb922d6c02d33be72453e81955c2ec9187d
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-full-qc-after-exports.log.gz
    sha256: 774e1bf4fe4bb77aec20802e420c80582f3febf9326d72e790e4134416222c5d
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-full-qc.json
    sha256: d717163764d2e8bcca8e62a342402f44b12930ce7b27e8f94561311c793139f3
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-full-qc.log.gz
    sha256: 58204cb445032954e4bf8cad0046f4c7c864fa78cbd42fd6ef2174bafbd36b8b
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-product-labels.json
    sha256: 919d4bc1db4419cb79518db4e8125efb84286c336f35003708249cdf8ed1b92a
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-product-labels.log
    sha256: 0398a65c658f872dd271612d18e18befa04dfded300d1f85dc313b0d51d6d80f
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-receipt-regression-tests-after-generation.json
    sha256: a7bd727afa4725d6782e83d2428acf87fcd0dec9d224efba03f846e8a639abe6
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-receipt-regression-tests-after-generation.log
    sha256: e3c6db86bd88d95a35de6b4f30e2eff3ee427ab94874b85fc2acf85336ece906
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-receipt-regression-tests.json
    sha256: 52bb53e0c693e6f11ff846f22f224af4087dbf219d2cad61d219836267d9d467
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-receipt-regression-tests.log
    sha256: 574c6b0216088d066b31a51a98eeca0e5764d450630b6bbfeaffbf9b3e448fed
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-reconcile-sssom.json
    sha256: deaa31ad4f271d965f52553faaeb9879c437ec5c5d71aba2d757fdc216934c66
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-reconcile-sssom.log
    sha256: 8bf18010d973e92de327bf8580964cbe3306206d7191c45a7b1731df9c7d61d7
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-refresh-49-tests.json
    sha256: e607f89ecd56c00212392fd3b064a04a72f5dd91c7a665ca4349d77953f15a66
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-refresh-49-tests.log
    sha256: a57ec66333404f7a2589d3d9825aff41c600c3c50fae406496fae547a86759d3
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-refresh-original-negative.json
    sha256: 7087ef409aba89da372ed9e9214d3167501f9d67bb9216011e377322395b1ded
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-refresh-original-negative.log
    sha256: fc8512395b5d98f01b91c766584c20abe42079a0e44311b743f998aba8a5a5ce
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-reviewed-sssom-export.json
    sha256: b53b47c83408e6b7d36f4eafa32a8bf88ab9cf91de80fb98b8a751609b1b5f5a
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-reviewed-sssom-export.log
    sha256: ea42c3393adad836b0a987a5588f98dc8ffbfb3b34adea118141cbb379e4f621
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-reviewed-sssom-qc.json
    sha256: 6bd6d71f70d47331914911d12eb46aca6704948eaaf87a5f114d82b170517fe9
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-reviewed-sssom-qc.log
    sha256: af9b5a362fad00b223ca94107d3d90ff26e370d1c36eaa78c42d9b11e70ba186
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-semantic-build.json
    sha256: 8ef9e5815ff99e8fadfc80994c4f5bd09ffc669ff708d50093e79bf0126392bf
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-semantic-build.log
    sha256: 9ad3af191a6b02eb58ee21ee25ee417d62e4d52653cd5f9dff02d09a20477f19
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-semantic-integrity.json
    sha256: 25748c1ba5c9c83e11daf7f98af8f421196f40cf352da72f8b0ebee140c00387
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-semantic-integrity.log
    sha256: b2f1341524d27201138e509b4ca6c7d3c0a14c4874543aa6cabe488eb049ddab
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-sssom-curies-subjects.json
    sha256: 65a67cfa3a65a7d3e4fdd2e7d8dadf07971b576f34804c1b607ef3db2592e48f
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-sssom-curies-subjects.log
    sha256: 365a95943ad509767c3e60e2d9c9d8f07988ea7fbf85fe49982d6e40aa817f68
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-subject-resolution.json
    sha256: 2e34327cfa4fc6b521707929a4895850ed663977c66eb892f956905a7445fe25
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-subject-resolution.log
    sha256: 8fdc3a97e377a127234d02d20f7e456c27ec6444d6effa2ba2a7bcf8874aedef
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-supported-kgx-export.json
    sha256: 7026887988fb2727ff0a4de5c31406cea9e265e397e4afc83d00e9bb7540af93
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-supported-kgx-export.log
    sha256: 383a95ae1e74d795bac34d09234a474f8e2856f566fe06cd1d1a94caa1afbbc2
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-supported-kgx-qc.json
    sha256: df9bca33a2d4b53b949e07c5020301b11717bdbc5cf178b43e206327c8ec3ad6
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-supported-kgx-qc.log
    sha256: 76585cbf11b4249faf99cb3c31583d72dfc51dc094902f6e4f9dd4e2084816b7
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-unified-generation.json
    sha256: cec72cc7e3044ff4c4f9b7fd3f0ab38c6c95c2db7c038ed4b24361a929fee847
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-unified-generation.log
    sha256: 47b26d8cb8e8b4742f03b2d21db16ff2e68d7de80ce7a7261cda65ec81d8e905
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-unified-stamp.json
    sha256: 0e53c5228dd2f26b5b46121a53d0c5c08c68c372a74263ff2f50f4d966ea0480
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-unified-stamp.log
    sha256: d9aa9bda5950b09fc0431413f2032e4138a4bdcf006912a50d3b9487c6f036ff
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-visualization-metadata.json
    sha256: 959682b8ce312d865698bca28e799739bf072a449876f407c2c0a0214c297912
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-visualization-metadata.log
    sha256: 43b707c879588b6e3de22422f59d81996e6e8fa558d339707a3c1ef579f7cc2c
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-writer-audit.json
    sha256: 108cc86085d82594891bb43762a2e736bb1d82cfa48f35216a9bdf9acff780c3
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-writer-audit.log
    sha256: 7cc62649a4c51e8faccb5698731bfc39e5b0bfcf6c877486418c041b91742778
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/qc-artifact-locations.json
    sha256: d850cfbb78184395f5b03c9950e47ee171a37b3eab5e5953406693173d7f0ad6
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/unified/diagnostic-incorrect-final-comparison-v1.json
    sha256: b9f7a39577084ef0356f7689c6a2b08194f1cb3888ce8b5a6ad6dda9e641d289
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/unified/final-comparison-v2.json
    sha256: 7f7db8caaab6d9ce14f5c2f96b4e4963c36d67d7e9a7f4409273dfae887b6d4f
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/unified/unified-generation-receipt.json.gz
    sha256: ceea2fc32bbfb4a5dafbe66165219015731e98eb8c18551ba38c4558fedb78b9
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/final-checks/visualization-delta.json
    sha256: de40a68a3618a1b499b878cba89c26a99275b247eb15479873ac12ef64bad375
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/generation/comparison-inputs.json
    sha256: 37f6b3bb4efecb31ef0932ca1d4c81f31b871d0a1f460bd3b244b8abd382236f
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/generation/generation-receipt.json
    sha256: a86995fa1754a56ed86afc1606794915582570c667685435353e3f3fc37e5c97
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/generation/inputs-after.json
    sha256: c067ca3c4a8e8c5f4dcde5b024fea5501a0d48b591e6e5910851d6a71d054fef
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/generation/inputs-before.json
    sha256: c067ca3c4a8e8c5f4dcde5b024fea5501a0d48b591e6e5910851d6a71d054fef
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/generation/label-config.json
    sha256: af3a2d009ea262ee7ab3e2a34b52b496efdc203dbf839bbd163888e1ecd1722b
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/generation/label-config.yaml
    sha256: 642b5a240656f7608a1feb9f0e2bde5026bf45ce9357e3556b99b2e7778fab9d
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/generation/label-input-01.json
    sha256: 5af1c53287825190cd9e83288e3e7986ea2fa8932bb62bd745a6910088ee5496
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/generation/label-input-02.json
    sha256: 86c893b193db6f4f0140a364561a41b79cd6fd682dc7717395fe7094ecd13baf
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/generation/label-input-03.json
    sha256: 8274ff142aa0a59e5904c8545637c73c3442b1f66c438e973de20fc4c61c4f5d
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/generation/label-input-04.json
    sha256: 988e8f5d852b681deadc95465380afc2fa298639730b5c806ccb48267abda0b1
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/generation/label-report.tsv
    sha256: 1b8dfc04bcc2e2b0f654c2115bf40d64a3e1fe4830c86afc3bf65a12cc08a691
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/generation/native-invariants/receipt.json
    sha256: 38c0e579ac4a03923af9ec420a722affb8f075fae1333fa4ff3a41deebc4c671
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/generation/native-invariants/rejects.tsv
    sha256: 9912547da4ff594c686b21a13cd11d06997878514645162518fa712f99d13cea
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/generation/repository-context.json
    sha256: 400a5c4891c52a3314b4b8440b66625287886561b340cb3ead43bb47525d89b6
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/harnesses/generate_candidate.py
    sha256: d8e7a2299eb593c9aa1c341bafd6dcd5d2f6a71c6e4aaeff3f3ce325a04981bc
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/harnesses/make_step2_receipt.py
    sha256: 38caf83833db5ad0181c1e7b73207fc2e820a7c7ba1100b5dc2b405d62e507f4
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/harnesses/run.py
    sha256: 3c652925904f6a195336ef4c3239f4a26dc53b5fd564121d3f529d2bd1f160c7
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/harnesses/validate_candidate.py
    sha256: bbb919eedc990552445af562ab5cb7b0ea06ce95ab18d614cd5cba80e4b6ca5f
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/inventory.json
    sha256: b393caa80bbc698e671d2192f8a4d04995a2a53d66722ce259cc2ac58e2ef64a
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-baseline-strict.json
    sha256: d91905fea331c34b626beeb0ac2615e864ee6db900d96c605f8f6e43650a7534
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-baseline-strict.log
    sha256: c8113e528f5d73ed3e969e51944d7ed422a8fd10ed6f1903633d698c35485a5e
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-baseline-terms.json
    sha256: 4721d228279cf7f9d6ede0d3d720dceb0a76b88b280d50fdb7bb98bc2e6be55f
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-baseline-terms.log
    sha256: 23acda1c1d3194d12bc947d897d07de83f4a076a9d93c135148885108530e018
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-candidate-curies.json
    sha256: 893cbfecb82baa9c9c8844a8e3296003d917aa27dd44ac667ebdb26ce8110b27
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-candidate-curies.log
    sha256: a35610365e5d321a4cb1420b060769332eab86d7e860a6b5ea2e62634db888cb
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-candidate-invariants.json
    sha256: 72774783d688f00884e4740404bcca2fd71a09954d859939d3e549c46f2ba476
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-candidate-invariants.log
    sha256: b6d42b782f1d58cddedbe2b3ce7456b614a7dc8a13320dacf2f426a9dcfbcc55
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-candidate-labels.json
    sha256: 3423403d06c3928f6ae17fba127edad21785bbd478fbf57555937ee0b0d57491
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-candidate-labels.log
    sha256: 32fbd671e667c6a05b080bc4b37ad9b7050461ee0b7aa9d1ea0c3fea3ece4778
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-mapping-promotion.json
    sha256: e90c5b47b3960eb927dcdd857f60726e81f3a249eb74d403c3d98017c310fcdd
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-mapping-promotion.log
    sha256: a8793139b4874844e5813e3cb2caaea3a90194add244bb8365d35a66eb47380b
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-native-candidate.json
    sha256: d7c404ae5b1d5389fc2c8572b9618fff7c3a335bb195e6112e6798770314043f
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-native-candidate.log
    sha256: 6f394e5a79ed916840e28d4d9fbf73b117e21ee70b6b01022e3a7b3d32efe0fa
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-native-mapping-receipt.json
    sha256: 84778c8ac894c0e925a0d3f8983a0fb574620c9f182692a4fa8179f06e8673e3
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-native-mapping-receipt.log
    sha256: 367f2d8454ea8cd1c0b2eacb377a883ec0c39e48b336b70b083943d146f2a6ef
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-promotion-dry-run.json
    sha256: 5f10f70870da9538df735578bad31e1c27731ac6cb40c9ece54423fa1ff65d3b
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-promotion-dry-run.log
    sha256: d059bac855a52ad5c4e9d643d09e2c06172af095838bcad777bebc422d15a984
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-source-apply.json
    sha256: 225dc922277caf7f8ce8612baf2e4ef2f79aa8ecba933589bec347689ed6670e
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-source-apply.log
    sha256: 9964eaf0815d3fbf18e43ed8163ebc1170810fb61a48986273543b8bdacad44d
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-sync-curated.json
    sha256: d1e5408602dd7277118b60975158d2b1614ce93954cb065d90c0e43f379c8c3c
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-sync-curated.log
    sha256: a6a4d17209dc246ccc51a5153e7a31a709534dc9f78b949c863455a3493a75ad
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-writer-committed-preapply-red.json
    sha256: 8002a42b27b3be8f7611dbc148907715aa7526af6223fae0a19e7a15285350d3
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-writer-committed-preapply-red.log
    sha256: 93765aa69cb6548ac775832e8331290b9ac569230602f87ee02a02820b0e2c38
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-writer-config-preflight.json
    sha256: fe296f99f9cb9ad24f03edaa368f533ec1464d5c6dabb64e341871f8bc0503c9
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-writer-config-preflight.log
    sha256: 8530b860a1a29e581c4807df15a46ddfbbe0a16a8485e6339366c14ca44cb24c
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-writer-focused-green.json
    sha256: b68c1b87ec0a2da92797b009a8cc6818a6942389be1c3817367a60c7097a991a
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-writer-focused-green.log
    sha256: 8870c877b6b2d0fd7a0b9139049846469dd898094c832e71fea0814f360edb0f
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-writer-lint-final.json
    sha256: 6b87b2c7da97eeabb15d7f768df224bacc584a8da15ce4a00449f011b603bdd8
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-writer-lint-final.log
    sha256: 82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-writer-mutations.json
    sha256: ba92fca26016bc7e714bccc3545786c517243ed2857363965c9ba420156e3dd0
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-writer-mutations.log
    sha256: 3663dba44bb71689cb65d3e041fa9e61ed6b341132263f9ee6ae888dd751df23
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-writer-production-dry-run.json
    sha256: f6efe65f8b0deec534f513144309ebef493e7b7dd5b8fb8da70bb53ff7bd7e10
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/logs/step2-writer-production-dry-run.log
    sha256: 0a0ca1ef7778474090114ae71a5463f8d385a5be886d1e583908ed13af3e635e
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/package_evidence.py
    sha256: 9d2bf4373edab5dbf6eb1785cf758c659db79962dac7449f1ae65536f390e012
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/preflight/baseline-and-probes.json
    sha256: 22a3063f555a438d4f1de941cdc79236085894155706babe6427715bfb7f6a18
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/preflight/ncit-C61946-local-readonly.json
    sha256: 28a261db7c9a8b35ba0e1e6c4c04f7296f302de44a79a75e43bb337cd72c70ef
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/preflight/producer-compatibility-probes.json
    sha256: eb730e1466f85add7e7830579a9c6c0522246779ca1c634db5d9853e50b7a44e
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/reservation-repair/README.md
    sha256: 43304ae55f9c81e5c77abf54cb295cfdd8cda7af6314f6e65c40f93f16128b4e
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/reservation-repair/artifact-locations.json
    sha256: 7eb81008a722ead207ab31d84fc87669771f36bf00d54671888f17a7965ba499
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/reservation-repair/historical-applied-writer.py
    sha256: a66389a3379a761ee263aceb08222b6508f57cb9b8e69e996e82af732b59bb85
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/reservation-repair/independent-original-probe.py
    sha256: 6b3ed3ee1e0083cdf6e8ead0eb8216d912542d4c7242060e525a56131a19261e
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/reservation-repair/independent-original-race.json
    sha256: e7d2d840b53eee5dbb3a23cdc372a7ff961a5504020817deccef997a78021085
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/reservation-repair/logs/step2-reservation-green.json
    sha256: 0df7584f16f80a4f896a2ef4420fc423f3ca34c25efa288f00b2943dc03ebb4a
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/reservation-repair/logs/step2-reservation-green.log
    sha256: 43cdbd3d447ef68f21548bfabf73a673ffe47700fa856ff839096a2d400e002c
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/reservation-repair/logs/step2-reservation-lint.json
    sha256: 97d3d72e31119010f467b25a2209fe5fdf29e0fe2ade519ed873b86492126967
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/reservation-repair/logs/step2-reservation-lint.log
    sha256: 82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/reservation-repair/logs/step2-reservation-red.json
    sha256: e8a84743560bc55b996fbdcc5f2773ffbd5e2d70f7679780db06259bb96911bd
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/reservation-repair/logs/step2-reservation-red.log
    sha256: 3d499b23414988ede4a5fa0c0e601a93dca610431c8a283623d4c910b07e7f38
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/reservation-repair/logs/step2-reservation-replay.json
    sha256: 6138308212616d1f779701419b9b1169a8ba7e3c585a9f3d7ca7805bb5506a58
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/reservation-repair/logs/step2-reservation-replay.log
    sha256: 321c3033d48caca033e8dc02704e10f7bba2ab30de1e0353ca60e7b3a291b060
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/reservation-repair/repair-summary.json
    sha256: b115798a178ba7f0f3a40fdea11199b46b9e4c74c645fd4bbf7de58edb9be3d7
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/reservation-repair/replay-result.json
    sha256: 5b85f6ed30b48f76ffa4c38548f497852dba6fd476d0cb6327afb1e48e4ba340
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/reservation-repair/replay_repaired_writer.py
    sha256: 779602f87de64a174682db2e94cba4cab8e67ef11764425f3f0f882c4f0f7ced
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/snapshot-checks.json
    sha256: f340a18e31f78e92508a9e29dfa579153f81049891b3c618ed1a9635ea580afb
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/verify_inventory.py
    sha256: 8137139159a0a158657eabe8a8d2c84ec083fea23160f4be410179e056c4d931
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/writer/mutation-results.json
    sha256: c1439f18dea9bed26ed1e7b3bbc57140a6ad6dda2bbf0b146b206ceb236a4995
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/writer/mutations/allow_inherited_validation_stamp.log
    sha256: 9742cb8f33ff2271d1e5005bccdb6bf7811f7be720db3c80f5b8b2e79d4db412
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/writer/mutations/discard_historical_source_tokens.log
    sha256: 15a9c09d9f01d48be25ee8d69b7ad67cc87ddd150f5e1013fb18ae7e57e0152a
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/writer/mutations/discard_previous_history.log
    sha256: d28af8c7d38856fc16cb96abac6659fa60c6ed680c671409f2a62225c8f5d139
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/writer/mutations/ignore_candidate_hash.log
    sha256: aceefb26bba15cd6b13fe3429db70a680a69b9dd3c2170db561169c04a9f5210
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/writer/mutations/ignore_input_race.log
    sha256: 466f869c031c02bf078d9ed442a5e8cd97cd9770f5eed8689ec7d66dcd23c568
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/writer/mutations/omit_ledger_migration.log
    sha256: c46e45ead354d08cfde65790f23931df278033ab5558bbddb063608a7504b90c
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/writer/mutations/positive.log
    sha256: 0cb0b5615da6633a9ef2268d92555af73f841232945127c140ebc8cccff260e7
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/writer/run_mutations.py
    sha256: 501cc62eb1125951b0d6c7fc930b367c2809333111b00e8e9f0d338903c532b5
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/execution/writer/stable-inputs.json
    sha256: c56b7f4bbadfed70d07c88fb26a0a9cca6c1ce667602b815dd0344096ead1d58
    role: context
  - path: reports/ncit_heptahydrate_875_20261101/sources/ncit-C61946-receipt.json
    sha256: 9e6c6364182d4450114a8662eecf9a1db38d16a47cdcbbfc3f71cce21bb1bebb
    role: target
  - path: reports/ncit_heptahydrate_875_20261101/sources/ncit-C61946.json
    sha256: a112c3e91dd6aa46feb112621ba5d13673df69f1b20665e042e22b8aa05a1d83
    role: target
  - path: reports/ncit_heptahydrate_875_20261101_unified_review/README.md
    sha256: 57abb1054808171f58abc06cf1222efbb12c6f69b18fb97956197dc3a328236e
    role: context
  - path: reports/ncit_heptahydrate_875_20261101_unified_review/inventory.json
    sha256: ba8f1490d1e42a61ff365a894341fdbb70092b00599b2c84b429da7bcbecd91a
    role: context
  - path: reports/ncit_heptahydrate_875_20261101_unified_review/unified-input-verification.json
    sha256: 505b110e0715dff059020e860c8a8ce5d77cdc38aff2cbe7d70864afcd855530
    role: context
  - path: reports/ncit_heptahydrate_875_20261101_unified_review/unified-input-verification.log
    sha256: 106e57a6afb47d69ee2f69b68490c074c09a2d78675599439520768577eb9f91
    role: context
  - path: reports/semantic_review_20260921/resolution/assertion-dispositions.tsv
    sha256: 1fc422a342632befd63d7632002fb95f4c0ee49a42d0baacdff8dbf2a70daa62
    role: target
  - path: reports/semantic_review_20260921/resolution/current-review.json
    sha256: 2bc6fd01874ae295fd8812ff6249ea96e3163623957d51d622c85a398e69cb4a
    role: target
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: 39a9d49626034f1bccecb2b2ad20e2f0b5ac70a13719c22a9c62144c2db6259c
    role: target
  - path: reports/sssom_completion_20260921/README.md
    sha256: 49382bd28b7d0869c8d888429547a1486491ea72e50a0281c62f53e8d0a3a02b
    role: context
  - path: reports/sssom_completion_20260921/assemble_review.py
    sha256: 6165143f5058d6e1f0fa51bbf4aaa5265dbdc9b8f510a63ed80579577b8aad88
    role: target
  - path: reports/sssom_completion_20260921/mapping-evidence.json
    sha256: 0e30206fe5a040f46aff6d2ce7002592ec0a05d259d7ea9bc26f922c915e7ca4
    role: target
  - path: reports/sssom_completion_20260921/mapping_changes/issue875-ncit-exact-heptahydrate.json
    sha256: 28bd529e14104cfbf9160e9532b3d859dbe6259dbac00a9d877bac1daec8a2b8
    role: target
  - path: reports/sssom_completion_20260921/review.json
    sha256: 368aa926912b7ff675849fbe3491230eb9083af473efdca9d10ae4c11f91b5b0
    role: target
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/.vendored_canon_ref
    sha256: ecbdb08d2094917a5ed8147086f46579e976df869eaea3942060c552d2e2015c
    role: target
  - path: scripts/check_unified_freshness.py
    sha256: 95efa627ea1cc0e6ee2d055815f54a9e121971b1ac843d4be3453176f13d2c90
    role: context
  - path: scripts/check_unified_rejections.py
    sha256: 4f7faf1f103f50be1a59e826b0238061d1a9214afcec9d1cf0b029237e71238c
    role: context
  - path: scripts/promote_heptahydrate_ncit.py
    sha256: f7cd1b46dc464cc8801a73f6b1cbd251bd5c0c7ffdf7241eff0e9cbee6f1c131
    role: target
  - path: src/mediaingredientmech/curate/apply_receipt.py
    sha256: 6c7c613a1a9c2211c68b20a2483e99009c34fd908c9bf3b3acbac63eedb72a3f
    role: context
  - path: src/mediaingredientmech/curate/curation_event.py
    sha256: 22dc7ed373e356045c472b0bfa61c7e4915bd9aabc34fac108e21789b01acc34
    role: context
  - path: src/mediaingredientmech/export/reviewed_sssom.py
    sha256: ab74bae77709ba59623b2aa4612a16b692361c4f46bbb9b5a597f31bd6716ec3
    role: context
  - path: src/mediaingredientmech/ingredient_bundle_contract.py
    sha256: 9285d9d2423d108e0b1e3a960ddcbdd5e9b94eb44e099632042fc7e1e95e51b2
    role: context
  - path: src/mediaingredientmech/ingredient_bundle_refresh.py
    sha256: 58193f16b7231aba75932bf7316c1bf8394709bc7cff96687accb11eb6963946
    role: target
  - path: src/mediaingredientmech/review_claims.py
    sha256: bf214f5791223ed318b017db7206bc4ba8cf48bc9ce30d80fba5728cc5ca62fd
    role: context
  - path: src/mediaingredientmech/schema/mediaingredientmech.yaml
    sha256: bb43dee29b21fdee72a48022456e733e49e95824c4c09674f9b3165c290fe012
    role: context
  - path: src/mediaingredientmech/validation/write_validated.py
    sha256: 6763083be385b38dceb911f13dbd9575aea0dc42425204ccc43360f93c0dcbc9
    role: context
  - path: tests/fixtures/issue875-owner-before.yaml
    sha256: e4f20bded8bb984f76d381636cf79b522983413046bf24bc6168e1065c027636
    role: context
  - path: tests/test_ingredient_bundle.py
    sha256: ad3192652ebad0918d52a1eb8d73047bb1e56f8e7eda9ae5fac8391a52a0c852
    role: target
  - path: tests/test_ingredient_bundle_dependency_refresh.py
    sha256: b5ec52682e41861529f99bd414e5b06219ed3024289f3a59e5a2045e0ce64967
    role: target
  - path: tests/test_promote_heptahydrate_ncit.py
    sha256: 8adfdd21e8042059abd058b94ae846d1fc1e432bb876d64f5db79ad7ddf87e51
    role: target
scope:
  description: '40 declared targets: 35 artifacts and 5 exact mapping/rejection/unified
    rows. Full structural comparison covers 2,986 canonical and 4,170 unified rows;
    exact identity interpretation is limited to one heptahydrate and its published
    spellings.'
  selection: 'Approved #875 owner, ledger, mapping and product delta; prerequisite
    #1028 refresh and #1029 writer repairs; their authoritative evidence, release
    gates and protected dependencies. No random sampling.'
  coverage: full
  population_size: 40
  reviewed_target_ids:
  - data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
  - mappings/unified_mapping_rejections.tsv
  - scripts/promote_heptahydrate_ncit.py
  - tests/test_promote_heptahydrate_ncit.py
  - src/mediaingredientmech/ingredient_bundle_refresh.py
  - tests/test_ingredient_bundle_dependency_refresh.py
  - tests/test_ingredient_bundle.py
  - reports/sssom_completion_20260921/assemble_review.py
  - .github/workflows/qc-reviewed-sssom.yaml
  - .github/workflows/qc-evidence.yaml
  - scripts/.vendored_canon_ref
  - docs/SSSOM_RELEASE.md
  - docs/INGREDIENT_BUNDLE.md
  - reports/ncit_heptahydrate_875_20261101/README.md
  - reports/ncit_heptahydrate_875_20261101/execution/README.md
  - data/curated/mapped_ingredients.yaml
  - data/curated/unmapped_ingredients.yaml
  - docs/data/label_index.csv
  - docs/data/ingredients.json
  - UNIFIED_INGREDIENT_MAPPING.tsv
  - UNIFIED_INGREDIENT_MAPPING.provenance.json
  - mappings/ingredient_mappings.sssom.tsv
  - reports/sssom_completion_20260921/mapping_changes/issue875-ncit-exact-heptahydrate.json
  - reports/sssom_completion_20260921/review.json
  - reports/sssom_completion_20260921/mapping-evidence.json
  - reports/semantic_review_20260921/resolution/current-review.json
  - reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  - reports/semantic_review_20260921/resolution/assertion-dispositions.tsv
  - reports/ingredient_bundle_20261101_ncit875/review.json
  - reports/ingredient_bundle_20261101_ncit875/dependency-refresh.json
  - reports/ingredient_bundle_20261101_ncit875/prior-review.json
  - reports/ncit_heptahydrate_875_20261101/execution/application/source-apply.json
  - reports/ncit_heptahydrate_875_20261101/execution/application/mapping-promotion.json
  - reports/ncit_heptahydrate_875_20261101/sources/ncit-C61946.json
  - reports/ncit_heptahydrate_875_20261101/sources/ncit-C61946-receipt.json
  - issue875:mapping-row
  - issue875:rejection-row
  - issue875:unified-1
  - issue875:unified-2
  - issue875:unified-3
  exclusions:
  - target: Inherited chemical structures and provisional BUFFER role
    reason: Explicitly remain open; the approved step 2 is an exact identity/receipt
      correction, not full chemical or role curation.
  - target: Every other ingredient scientific identity, role and alias claim
    reason: Global structural and preservation checks are not corpus-wide scientific
      approval.
  - target: Full scientific-release backlog and later approved-plan steps
    reason: Existing native holds remain; this common review does not supersede them
      or implement the later approval model.
targets:
- target_id: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
  path: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
  label: Na2hpo4_X_7_H2o.yaml
  kind: maintained
  ownership_note: Authoritative distinct heptahydrate record; review is limited to
    the approved identity correction and preserved unresolved claims.
- target_id: mappings/unified_mapping_rejections.tsv
  path: mappings/unified_mapping_rejections.tsv
  label: unified_mapping_rejections.tsv
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
    role: maintained owner of the reviewed heptahydrate delta
  ownership_note: Whole-file structural/currentness and non-target preservation checks;
    exact scientific identity scope is the one reviewed heptahydrate. Unified producer
    and source snapshots are bound by generation receipts.
- target_id: scripts/promote_heptahydrate_ncit.py
  path: scripts/promote_heptahydrate_ncit.py
  label: promote_heptahydrate_ncit.py
  kind: maintained
  ownership_note: Repository-maintained implementation, review gate, scoped provenance
    or release-selection artifact; review confers no scientific approval.
- target_id: tests/test_promote_heptahydrate_ncit.py
  path: tests/test_promote_heptahydrate_ncit.py
  label: test_promote_heptahydrate_ncit.py
  kind: maintained
  ownership_note: Repository-maintained implementation, review gate, scoped provenance
    or release-selection artifact; review confers no scientific approval.
- target_id: src/mediaingredientmech/ingredient_bundle_refresh.py
  path: src/mediaingredientmech/ingredient_bundle_refresh.py
  label: ingredient_bundle_refresh.py
  kind: maintained
  ownership_note: Repository-maintained implementation, review gate, scoped provenance
    or release-selection artifact; review confers no scientific approval.
- target_id: tests/test_ingredient_bundle_dependency_refresh.py
  path: tests/test_ingredient_bundle_dependency_refresh.py
  label: test_ingredient_bundle_dependency_refresh.py
  kind: maintained
  ownership_note: Repository-maintained implementation, review gate, scoped provenance
    or release-selection artifact; review confers no scientific approval.
- target_id: tests/test_ingredient_bundle.py
  path: tests/test_ingredient_bundle.py
  label: test_ingredient_bundle.py
  kind: maintained
  ownership_note: Repository-maintained implementation, review gate, scoped provenance
    or release-selection artifact; review confers no scientific approval.
- target_id: reports/sssom_completion_20260921/assemble_review.py
  path: reports/sssom_completion_20260921/assemble_review.py
  label: assemble_review.py
  kind: maintained
  ownership_note: Repository-maintained implementation, review gate, scoped provenance
    or release-selection artifact; review confers no scientific approval.
- target_id: .github/workflows/qc-reviewed-sssom.yaml
  path: .github/workflows/qc-reviewed-sssom.yaml
  label: qc-reviewed-sssom.yaml
  kind: maintained
  ownership_note: Repository-maintained implementation, review gate, scoped provenance
    or release-selection artifact; review confers no scientific approval.
- target_id: .github/workflows/qc-evidence.yaml
  path: .github/workflows/qc-evidence.yaml
  label: qc-evidence.yaml
  kind: maintained
  ownership_note: Repository-maintained implementation, review gate, scoped provenance
    or release-selection artifact; review confers no scientific approval.
- target_id: scripts/.vendored_canon_ref
  path: scripts/.vendored_canon_ref
  label: .vendored_canon_ref
  kind: maintained
  ownership_note: Repository-maintained implementation, review gate, scoped provenance
    or release-selection artifact; review confers no scientific approval.
- target_id: docs/SSSOM_RELEASE.md
  path: docs/SSSOM_RELEASE.md
  label: SSSOM_RELEASE.md
  kind: maintained
  ownership_note: Repository-maintained implementation, review gate, scoped provenance
    or release-selection artifact; review confers no scientific approval.
- target_id: docs/INGREDIENT_BUNDLE.md
  path: docs/INGREDIENT_BUNDLE.md
  label: INGREDIENT_BUNDLE.md
  kind: maintained
  ownership_note: Repository-maintained implementation, review gate, scoped provenance
    or release-selection artifact; review confers no scientific approval.
- target_id: reports/ncit_heptahydrate_875_20261101/README.md
  path: reports/ncit_heptahydrate_875_20261101/README.md
  label: README.md
  kind: maintained
  ownership_note: Repository-maintained implementation, review gate, scoped provenance
    or release-selection artifact; review confers no scientific approval.
- target_id: reports/ncit_heptahydrate_875_20261101/execution/README.md
  path: reports/ncit_heptahydrate_875_20261101/execution/README.md
  label: README.md
  kind: maintained
  ownership_note: Repository-maintained implementation, review gate, scoped provenance
    or release-selection artifact; review confers no scientific approval.
- target_id: data/curated/mapped_ingredients.yaml
  path: data/curated/mapped_ingredients.yaml
  label: mapped_ingredients.yaml
  kind: generated
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
    role: maintained owner of the reviewed heptahydrate delta
  ownership_note: Whole-file structural/currentness and non-target preservation checks;
    exact scientific identity scope is the one reviewed heptahydrate. Unified producer
    and source snapshots are bound by generation receipts.
- target_id: data/curated/unmapped_ingredients.yaml
  path: data/curated/unmapped_ingredients.yaml
  label: unmapped_ingredients.yaml
  kind: generated
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
    role: maintained owner of the reviewed heptahydrate delta
  ownership_note: Whole-file structural/currentness and non-target preservation checks;
    exact scientific identity scope is the one reviewed heptahydrate. Unified producer
    and source snapshots are bound by generation receipts.
- target_id: docs/data/label_index.csv
  path: docs/data/label_index.csv
  label: label_index.csv
  kind: generated
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
    role: maintained owner of the reviewed heptahydrate delta
  ownership_note: Whole-file structural/currentness and non-target preservation checks;
    exact scientific identity scope is the one reviewed heptahydrate. Unified producer
    and source snapshots are bound by generation receipts.
- target_id: docs/data/ingredients.json
  path: docs/data/ingredients.json
  label: ingredients.json
  kind: generated
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
    role: maintained owner of the reviewed heptahydrate delta
  ownership_note: Whole-file structural/currentness and non-target preservation checks;
    exact scientific identity scope is the one reviewed heptahydrate. Unified producer
    and source snapshots are bound by generation receipts.
- target_id: UNIFIED_INGREDIENT_MAPPING.tsv
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  label: UNIFIED_INGREDIENT_MAPPING.tsv
  kind: generated
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
    role: maintained owner of the reviewed heptahydrate delta
  ownership_note: Whole-file structural/currentness and non-target preservation checks;
    exact scientific identity scope is the one reviewed heptahydrate. Unified producer
    and source snapshots are bound by generation receipts.
- target_id: UNIFIED_INGREDIENT_MAPPING.provenance.json
  path: UNIFIED_INGREDIENT_MAPPING.provenance.json
  label: UNIFIED_INGREDIENT_MAPPING.provenance.json
  kind: generated
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
    role: maintained owner of the reviewed heptahydrate delta
  ownership_note: Whole-file structural/currentness and non-target preservation checks;
    exact scientific identity scope is the one reviewed heptahydrate. Unified producer
    and source snapshots are bound by generation receipts.
- target_id: mappings/ingredient_mappings.sssom.tsv
  path: mappings/ingredient_mappings.sssom.tsv
  label: ingredient_mappings.sssom.tsv
  kind: generated
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
    role: maintained owner of the reviewed heptahydrate delta
  ownership_note: Whole-file structural/currentness and non-target preservation checks;
    exact scientific identity scope is the one reviewed heptahydrate. Unified producer
    and source snapshots are bound by generation receipts.
- target_id: reports/sssom_completion_20260921/mapping_changes/issue875-ncit-exact-heptahydrate.json
  path: reports/sssom_completion_20260921/mapping_changes/issue875-ncit-exact-heptahydrate.json
  label: issue875-ncit-exact-heptahydrate.json
  kind: generated
  ownership_note: Repository-maintained implementation, review gate, scoped provenance
    or release-selection artifact; review confers no scientific approval.
- target_id: reports/sssom_completion_20260921/review.json
  path: reports/sssom_completion_20260921/review.json
  label: review.json
  kind: generated
  ownership_note: Repository-maintained implementation, review gate, scoped provenance
    or release-selection artifact; review confers no scientific approval.
- target_id: reports/sssom_completion_20260921/mapping-evidence.json
  path: reports/sssom_completion_20260921/mapping-evidence.json
  label: mapping-evidence.json
  kind: generated
  ownership_note: Repository-maintained implementation, review gate, scoped provenance
    or release-selection artifact; review confers no scientific approval.
- target_id: reports/semantic_review_20260921/resolution/current-review.json
  path: reports/semantic_review_20260921/resolution/current-review.json
  label: current-review.json
  kind: generated
  ownership_note: Repository-maintained implementation, review gate, scoped provenance
    or release-selection artifact; review confers no scientific approval.
- target_id: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  label: finding-dispositions.tsv
  kind: generated
  ownership_note: Repository-maintained implementation, review gate, scoped provenance
    or release-selection artifact; review confers no scientific approval.
- target_id: reports/semantic_review_20260921/resolution/assertion-dispositions.tsv
  path: reports/semantic_review_20260921/resolution/assertion-dispositions.tsv
  label: assertion-dispositions.tsv
  kind: generated
  ownership_note: Repository-maintained implementation, review gate, scoped provenance
    or release-selection artifact; review confers no scientific approval.
- target_id: reports/ingredient_bundle_20261101_ncit875/review.json
  path: reports/ingredient_bundle_20261101_ncit875/review.json
  label: review.json
  kind: generated
  ownership_note: Repository-maintained implementation, review gate, scoped provenance
    or release-selection artifact; review confers no scientific approval.
- target_id: reports/ingredient_bundle_20261101_ncit875/dependency-refresh.json
  path: reports/ingredient_bundle_20261101_ncit875/dependency-refresh.json
  label: dependency-refresh.json
  kind: generated
  ownership_note: Repository-maintained implementation, review gate, scoped provenance
    or release-selection artifact; review confers no scientific approval.
- target_id: reports/ingredient_bundle_20261101_ncit875/prior-review.json
  path: reports/ingredient_bundle_20261101_ncit875/prior-review.json
  label: prior-review.json
  kind: generated
  ownership_note: Repository-maintained implementation, review gate, scoped provenance
    or release-selection artifact; review confers no scientific approval.
- target_id: reports/ncit_heptahydrate_875_20261101/execution/application/source-apply.json
  path: reports/ncit_heptahydrate_875_20261101/execution/application/source-apply.json
  label: source-apply.json
  kind: generated
  ownership_note: Repository-maintained implementation, review gate, scoped provenance
    or release-selection artifact; review confers no scientific approval.
- target_id: reports/ncit_heptahydrate_875_20261101/execution/application/mapping-promotion.json
  path: reports/ncit_heptahydrate_875_20261101/execution/application/mapping-promotion.json
  label: mapping-promotion.json
  kind: generated
  ownership_note: Repository-maintained implementation, review gate, scoped provenance
    or release-selection artifact; review confers no scientific approval.
- target_id: reports/ncit_heptahydrate_875_20261101/sources/ncit-C61946.json
  path: reports/ncit_heptahydrate_875_20261101/sources/ncit-C61946.json
  label: ncit-C61946.json
  kind: source
  ownership_note: Archived official NCI EVS database response and retrieval receipt;
    external authority owns the ontology assertion.
- target_id: reports/ncit_heptahydrate_875_20261101/sources/ncit-C61946-receipt.json
  path: reports/ncit_heptahydrate_875_20261101/sources/ncit-C61946-receipt.json
  label: ncit-C61946-receipt.json
  kind: source
  ownership_note: Archived official NCI EVS database response and retrieval receipt;
    external authority owns the ontology assertion.
- target_id: issue875:mapping-row
  path: mappings/ingredient_mappings.sssom.tsv
  label: Exact heptahydrate mapping
  kind: snapshot_row
  selector: subject_id = "MIM:Na2hpo4_X_7_H2o" AND predicate_id = "skos:exactMatch"
    AND object_id = "NCIT:C61946"
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
    role: exact ingredient identity owner
- target_id: issue875:rejection-row
  path: mappings/unified_mapping_rejections.tsv
  label: Heptahydrate stale-parent rejection
  kind: snapshot_row
  selector: ingredient_name = "Na2HPO4 x 7 H2O" AND rejected_id = "CHEBI:34683" AND
    mim_id = "NCIT:C61946"
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
    role: exact ingredient identity owner
- target_id: issue875:unified-1
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  label: Na2HPO4 x 7 H2O
  kind: snapshot_row
  selector: ingredient_name = "Na2HPO4 x 7 H2O"
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
    role: exact ingredient identity owner
- target_id: issue875:unified-2
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  label: Na2HPO4.7H2O
  kind: snapshot_row
  selector: ingredient_name = "Na2HPO4.7H2O"
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
    role: exact ingredient identity owner
- target_id: issue875:unified-3
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  label: Na2HPO4·7H2O
  kind: snapshot_row
  selector: ingredient_name = "Na2HPO4·7H2O"
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
    role: exact ingredient identity owner
checks:
- check_id: full_qc
  name: Complete native QC
  command: just qc
  target_ids:
  - data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
  - mappings/unified_mapping_rejections.tsv
  - scripts/promote_heptahydrate_ncit.py
  - tests/test_promote_heptahydrate_ncit.py
  - src/mediaingredientmech/ingredient_bundle_refresh.py
  - tests/test_ingredient_bundle_dependency_refresh.py
  - tests/test_ingredient_bundle.py
  - reports/sssom_completion_20260921/assemble_review.py
  - .github/workflows/qc-reviewed-sssom.yaml
  - .github/workflows/qc-evidence.yaml
  - scripts/.vendored_canon_ref
  - docs/SSSOM_RELEASE.md
  - docs/INGREDIENT_BUNDLE.md
  - reports/ncit_heptahydrate_875_20261101/README.md
  - reports/ncit_heptahydrate_875_20261101/execution/README.md
  - data/curated/mapped_ingredients.yaml
  - data/curated/unmapped_ingredients.yaml
  - docs/data/label_index.csv
  - docs/data/ingredients.json
  - UNIFIED_INGREDIENT_MAPPING.tsv
  - UNIFIED_INGREDIENT_MAPPING.provenance.json
  - mappings/ingredient_mappings.sssom.tsv
  - reports/sssom_completion_20260921/mapping_changes/issue875-ncit-exact-heptahydrate.json
  - reports/sssom_completion_20260921/review.json
  - reports/sssom_completion_20260921/mapping-evidence.json
  - reports/semantic_review_20260921/resolution/current-review.json
  - reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  - reports/semantic_review_20260921/resolution/assertion-dispositions.tsv
  - reports/ingredient_bundle_20261101_ncit875/review.json
  - reports/ingredient_bundle_20261101_ncit875/dependency-refresh.json
  - reports/ingredient_bundle_20261101_ncit875/prior-review.json
  - reports/ncit_heptahydrate_875_20261101/execution/application/source-apply.json
  - reports/ncit_heptahydrate_875_20261101/execution/application/mapping-promotion.json
  - reports/ncit_heptahydrate_875_20261101/sources/ncit-C61946.json
  - reports/ncit_heptahydrate_875_20261101/sources/ncit-C61946-receipt.json
  - issue875:mapping-row
  - issue875:rejection-row
  - issue875:unified-1
  - issue875:unified-2
  - issue875:unified-3
  evidence_ids:
  - full_qc_receipt
  - full_qc_log
  summary: Final just qc exited 0 at 2026-11-01T05:35:25Z after synchronized exports/visual
    metadata; log SHA 717f4c100ff3dc91fa8f46eefd4674294f4c2f0b5a2efa838ac74c1a6c11fefe.
  required: true
  status: passed
  exit_code: 0
  scope_note: Executed by root in the isolated worktree; reviewer independently inspected
    the hash-bound command receipt and complete log.
- check_id: mapping_qc
  name: Receipt replay and reviewed SSSOM validation
  command: just qc-reviewed-sssom
  target_ids:
  - mappings/ingredient_mappings.sssom.tsv
  - reports/sssom_completion_20260921/review.json
  evidence_ids:
  - mapping_qc_receipt
  - mapping_qc_log
  summary: Native assembler replay, supported/withheld export replay and schemas pass
    for 2,986 canonical rows.
  required: true
  status: passed
  exit_code: 0
  scope_note: Executed by root in the isolated worktree; reviewer independently inspected
    the hash-bound command receipt and complete log.
- check_id: canonical_invariants
  name: Canonical SSSOM native invariants
  command: python ../validate_candidate.py mappings/ingredient_mappings.sssom.tsv
    output/step2-canonical-native-invariants
  target_ids:
  - mappings/ingredient_mappings.sssom.tsv
  evidence_ids:
  - canonical_invariants_receipt
  - canonical_invariants_log
  summary: Canonical invariants pass against available actual KG transforms; missing
    BTO/MICRO transform limits remain explicit.
  required: true
  status: passed
  exit_code: 0
  scope_note: Executed by root in the isolated worktree; reviewer independently inspected
    the hash-bound command receipt and complete log.
- check_id: product_labels
  name: Product label validation
  command: just validate-products
  target_ids:
  - mappings/ingredient_mappings.sssom.tsv
  - docs/data/label_index.csv
  evidence_ids:
  - product_labels_receipt
  - product_labels_log
  summary: Native product-label command exits 0 while retaining 101 nonblocking warnings
    and 5,312 pairs without an adapter; this is not complete label approval.
  required: true
  status: passed
  exit_code: 0
  scope_note: Executed by root in the isolated worktree; reviewer independently inspected
    the hash-bound command receipt and complete log.
- check_id: semantic_integrity
  name: Native semantic report integrity
  command: python -m mediaingredientmech.validation.semantic_release --root . --report
    reports/semantic_review_20260921/resolution/current-review.json
  target_ids:
  - reports/semantic_review_20260921/resolution/current-review.json
  evidence_ids:
  - semantic_integrity_receipt
  - semantic_integrity_log
  summary: Current-review integrity passes while complete scientific release remains
    FAIL.
  required: true
  status: passed
  exit_code: 0
  scope_note: Executed by root in the isolated worktree; reviewer independently inspected
    the hash-bound command receipt and complete log.
- check_id: supported_kgx
  name: Supported graph and excluded backlog replay
  command: just qc-supported-kgx reports/semantic_review_20260921/resolution/current-review.json
    output/step2-supported-kgx
  target_ids:
  - reports/semantic_review_20260921/resolution/current-review.json
  evidence_ids:
  - supported_kgx_receipt
  - supported_kgx_log
  summary: Native supported-KGX replay validates exact approved selection and retained
    excluded claims.
  required: true
  status: passed
  exit_code: 0
  scope_note: Executed by root in the isolated worktree; reviewer independently inspected
    the hash-bound command receipt and complete log.
- check_id: companion_validate
  name: Companion portable validation
  command: python -m mediaingredientmech.export.ingredient_bundle validate output/step2-ingredient-bundle
    --manifest-sha256 ffb67b060ba8c574e0ebe8cfb83fb5d5b2bbd90adb0d5ac13acfc8bbf0a370ae
  target_ids:
  - reports/ingredient_bundle_20261101_ncit875/review.json
  - reports/ingredient_bundle_20261101_ncit875/dependency-refresh.json
  evidence_ids:
  - companion_validate_receipt
  - companion_validate_log
  summary: Native companion validates its manifest, source/evidence bindings and all
    complete claim payloads.
  required: true
  status: passed
  exit_code: 0
  scope_note: Executed by root in the isolated worktree; reviewer independently inspected
    the hash-bound command receipt and complete log.
- check_id: receipt_tests
  name: Receipt and release regression tests
  command: python -m pytest -q -o addopts= -p no:cacheprovider tests/test_mapping_change_receipt.py
    tests/test_reviewed_sssom.py tests/test_semantic_review_builder.py tests/test_semantic_mapping_review.py
    tests/test_unified_rejections.py tests/test_unified_source_holds.py
  target_ids:
  - reports/sssom_completion_20260921/assemble_review.py
  - src/mediaingredientmech/ingredient_bundle_refresh.py
  evidence_ids:
  - receipt_tests_receipt
  - receipt_tests_log
  summary: Final post-generation regression suite passes 207 tests; prior stale-unified
    failure remains historical diagnostic only.
  required: true
  status: passed
  exit_code: 0
  scope_note: Executed by root in the isolated worktree; reviewer independently inspected
    the hash-bound command receipt and complete log.
- check_id: writer_audit
  name: Maintained writer audit
  command: just audit-writers
  target_ids:
  - scripts/promote_heptahydrate_ncit.py
  evidence_ids:
  - writer_audit_receipt
  - writer_audit_log
  summary: Native writer audit passes for the final maintained writer.
  required: true
  status: passed
  exit_code: 0
  scope_note: Executed by root in the isolated worktree; reviewer independently inspected
    the hash-bound command receipt and complete log.
- check_id: freshness
  name: Unified rejection and freshness gates
  command: just stamp-unified-freshness check-unified-rejections check-unified-freshness
  target_ids:
  - UNIFIED_INGREDIENT_MAPPING.tsv
  - UNIFIED_INGREDIENT_MAPPING.provenance.json
  evidence_ids:
  - freshness_receipt
  - freshness_log
  summary: Native stamp and rejection/freshness checks pass after completed unified
    generation.
  required: true
  status: passed
  exit_code: 0
  scope_note: Executed by root in the isolated worktree; reviewer independently inspected
    the hash-bound command receipt and complete log.
- check_id: independent_tests
  name: Independent writer and refresh regression tests
  command: PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$PWD/src:$PWD/../claw-source/src:$PWD/../claw-source"
    ../envs/mim/bin/python -m pytest -q -o addopts= -p no:cacheprovider tests/test_promote_heptahydrate_ncit.py
    tests/test_ingredient_bundle_dependency_refresh.py
  target_ids:
  - scripts/promote_heptahydrate_ncit.py
  - tests/test_promote_heptahydrate_ncit.py
  - src/mediaingredientmech/ingredient_bundle_refresh.py
  - tests/test_ingredient_bundle_dependency_refresh.py
  evidence_ids:
  - tests
  - race_after
  summary: 133 tests pass, including current published heptahydrate surfaces and both
    prerequisite repairs.
  required: true
  status: passed
  exit_code: 0
- check_id: independent_applied
  name: Independent complete applied-data and candidate-hash verification
  command: PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$PWD/src" ../envs/mim/bin/python
    ../step2-independent/integration-preliminary/verify_applied.py "$PWD"
  target_ids:
  - data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
  - mappings/unified_mapping_rejections.tsv
  - mappings/ingredient_mappings.sssom.tsv
  evidence_ids:
  - applied
  summary: All 2,691 generation inputs, four label maps, five comparison inputs and
    actual source, promotion, receipt and journal hashes verified; exact bounded data
    scope preserved.
  required: true
  status: passed
  exit_code: 0
- check_id: independent_products
  name: Independent successor and artifact proof
  command: PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$PWD/src" ../envs/mim/bin/python
    ../step2-independent/integration-preliminary/verify_products.py "$PWD"
  target_ids:
  - UNIFIED_INGREDIENT_MAPPING.tsv
  - reports/ingredient_bundle_20261101_ncit875/review.json
  - reports/semantic_review_20260921/resolution/current-review.json
  evidence_ids:
  - products
  - unified_inputs
  summary: Exact companion/audit replay, complete unified delta and preservation of
    non-target scientific decisions pass; all 18,873 unified input hashes independently
    verified.
  required: true
  status: passed
  exit_code: 0
- check_id: independent_race
  name: Independent real-native reservation regression
  command: PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$PWD/src:$PWD/../claw-source/src:$PWD/../claw-source"
    ../envs/mim/bin/python ../step2-independent/integration-preliminary/probe_reservation_fixed.py
    "$PWD"
  target_ids:
  - scripts/promote_heptahydrate_ncit.py
  - tests/test_promote_heptahydrate_ncit.py
  evidence_ids:
  - race_after
  summary: All 16 independent reservation-replacement cases refuse false completion
    and preserve required recovery evidence.
  required: true
  status: passed
  exit_code: 0
- check_id: portable_inventory
  name: Portable evidence inventory verification
  command: PYTHONDONTWRITEBYTECODE=1 ../envs/mim/bin/python reports/ncit_heptahydrate_875_20261101/execution/verify_inventory.py
  target_ids:
  - reports/ncit_heptahydrate_875_20261101/execution/README.md
  evidence_ids:
  - inventory
  - supplement
  summary: 185 archived files verified; two supplemental independent proof files separately
    verified.
  required: true
  status: passed
  exit_code: 0
- check_id: live_endpoint
  name: Optional live EVS recheck
  command: web.open https://api-evsrest.nci.nih.gov/api/v1/concept/ncit/C61946?include=full
  target_ids:
  - reports/ncit_heptahydrate_875_20261101/sources/ncit-C61946.json
  evidence_ids:
  - ncit
  - ncit_receipt
  summary: The web tool could not access this API endpoint. Complete archived official
    response and its successful HTTP fetch receipt were inspected and hash-verified.
  required: false
  status: unavailable
evidence:
- evidence_id: authority
  kind: authority
  reference: MAPPING_SEMANTICS.md
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Section 3 step 1 selects an exact supplied-form ontology term and one exact
    row; unrelated chemistry and roles remain separate claims.
  snapshot_sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
- evidence_id: profile
  kind: authority
  reference: docs/record-review-profile.md
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Native review does not replace scientific release approvals or resolve
    existing claim holds.
  snapshot_sha256: da17e2048a13514a422bc94bd2f8d48943cffc5689b96e3f07da26423248d1a7
- evidence_id: owner
  kind: record_content
  reference: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Inspected exact heptahydrate identity, retained CAS/aliases/rejected sibling
    labels, complete history and explicit unresolved chemistry/BUFFER caveats.
  snapshot_sha256: 6e816ef6a1dad8dab9c3ddd711ca84d8a3489bedb175d540ea3cb618c7068873
- evidence_id: ncit
  kind: database
  reference: reports/ncit_heptahydrate_875_20261101/sources/ncit-C61946.json
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: 'Complete archived official EVS response: active C61946 in NCIt 26.10d,
    exact heptahydrate label, CAS 7782-85-6, formula 2Na.HO4P.7H2O and UNII 70WT22SF4B.
    This is a database assertion.'
  snapshot_sha256: a112c3e91dd6aa46feb112621ba5d13673df69f1b20665e042e22b8aa05a1d83
- evidence_id: ncit_receipt
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/sources/ncit-C61946-receipt.json
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Official endpoint, HTTP 200, actual retrieval time and exact archived source
    hash.
  snapshot_sha256: 9e6c6364182d4450114a8662eecf9a1db38d16a47cdcbbfc3f71cce21bb1bebb
- evidence_id: applied
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/execution/final-checks/independent-review/applied-verification.json
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Independent actual-data checks verify owner/history/ledger scope, both
    aggregate collections, all 2,691 candidate input hashes, all receipt bindings
    and canonical one-changed-row/one-removed-row scope.
  snapshot_sha256: d815db12ad00056fce3518d762d0d304da65535b5b7ab2ffa8fe638a06133242
- evidence_id: products
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/execution/final-checks/independent-review/products-verification.json
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Independent exact companion/audit replay; all non-target mapping evidence
    and approvals retained; three unified rows changed and all other rows identical.
  snapshot_sha256: 7cb98bd00d9c4f27ba88f0a17277244fd052b4cf847a191a16cb189e62f19182
- evidence_id: unified_inputs
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101_unified_review/unified-input-verification.json
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Independent verification of all 18,873 actual unified-generation input
    hashes and producer, baseline, before/after artifact bindings.
  snapshot_sha256: 505b110e0715dff059020e860c8a8ce5d77cdc38aff2cbe7d70864afcd855530
- evidence_id: candidate
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/execution/generation/generation-receipt.json
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Native diagnostic candidate binds producer 0cc221bd, all generation inputs,
    returned label maps and prior validation stamps; no approval supplied.
  snapshot_sha256: a86995fa1754a56ed86afc1606794915582570c667685435353e3f3fc37e5c97
- evidence_id: source_apply
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/execution/application/source-apply.json
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Completed actual source application binds exact owner and coupled rejection-ledger
    hashes; no scientific approval.
  snapshot_sha256: b24dab0665d4e2c6508ea13bbf39dc0ebb85b69241dc856a613000bc37944326
- evidence_id: promotion
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/execution/application/mapping-promotion.json
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Actual bounded promotion binds source receipt and candidatehash, records
    one changed ontology row and one removed registry row.
  snapshot_sha256: 6f2688c95739c65106a79c535b7a6513c5ad6d2a6d4a6c0c0251a4d114ac8b41
- evidence_id: receipt
  kind: validation
  reference: reports/sssom_completion_20260921/mapping_changes/issue875-ncit-exact-heptahydrate.json
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Approval-free chain link 16 preserves prior full rows and position map,
    exact owner before/after hashes, and inspected verification.
  snapshot_sha256: 28bd529e14104cfbf9160e9532b3d859dbe6259dbac00a9d877bac1daec8a2b8
- evidence_id: race_before
  kind: prior_review
  reference: reports/ncit_heptahydrate_875_20261101/execution/final-checks/independent-review/reservation-race.json
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Original real-native probe shows source changes and false success after
    receipt/backup reservation replacement; supports filed-before-fix#1029.
  snapshot_sha256: e7d2d840b53eee5dbb3a23cdc372a7ff961a5504020817deccef997a78021085
- evidence_id: historical_writer
  kind: prior_review
  reference: reports/ncit_heptahydrate_875_20261101/execution/final-checks/independent-review/writer-before-reservation-fix.py
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Exact producer used for historical application is preserved separately
    from the repaired writer.
  snapshot_sha256: a66389a3379a761ee263aceb08222b6508f57cb9b8e69e996e82af732b59bb85
- evidence_id: race_after
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/execution/final-checks/independent-review/reservation-fixed/results.json
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Independent repaired real-native 16 cases refuse false completion, preserve
    competitors, avoid precommit mutation, and retain postcommit recovery journals.
  snapshot_sha256: 691709b8a12cd004f711318230470f10e6a58b4fecee07494ffe20679a85e7d9
- evidence_id: tests
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/execution/final-checks/independent-review/focused-tests-fixed.log
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Independent writer/refresh suite passes 133 tests including actual regenerated
    surfaces and native transactions; 12 dependency deprecation warnings.
  snapshot_sha256: 257e5b10abe05922a55c7cea19d54fcb2525574b9a4a3c900ceecfcff6b19d14
- evidence_id: refresh
  kind: validation
  reference: reports/ingredient_bundle_20261101_ncit875/dependency-refresh.json
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Native unchanged-cohort receipt preserves 20 owners and 51 claims, records
    14 verified location changes and explicitly adds no scientific approval.
  snapshot_sha256: 3e422eeffe4ba4415a46314cd69f086a23d46ce3e164bb06aa1782eeb1c15a09
- evidence_id: visual
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/execution/final-checks/visualization-delta.json
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Both 2,340-node visualization products change only five target identity/mapping
    metadata fields; all other nodes and coordinates remain unchanged.
  snapshot_sha256: de40a68a3618a1b499b878cba89c26a99275b247eb15479873ac12ef64bad375
- evidence_id: inventory
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/execution/inventory.json
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Frozen 185-file portable execution inventory includes original failures,
    corrected gates and independent review proof.
  snapshot_sha256: b393caa80bbc698e671d2192f8a4d04995a2a53d66722ce259cc2ac58e2ef64a
- evidence_id: supplement
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101_unified_review/inventory.json
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Append-only two-file supplement preserves the late independent unified-input
    proof without changing the earlier frozen inventory.
  snapshot_sha256: ba8f1490d1e42a61ff365a894341fdbb70092b00599b2c84b429da7bcbecd91a
- evidence_id: documentation
  kind: record_content
  reference: reports/ncit_heptahydrate_875_20261101/README.md
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Approved bounded identity, writer operation, receipt provenance and explicit
    separate chemistry/BUFFER limitations.
  snapshot_sha256: 1e04dc58c21b76fc7d5fb90c49b7f8f4e8141417f868eb69680e897dd6785e7e
- evidence_id: full_qc_receipt
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-full-qc-after-exports.json
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Final just qc exited 0 at 2026-11-01T05:35:25Z after synchronized exports/visual
    metadata; log SHA 717f4c100ff3dc91fa8f46eefd4674294f4c2f0b5a2efa838ac74c1a6c11fefe.
    Actual command, times, exit status and log digest retained.
  snapshot_sha256: af40b8b3761d54be0b96a9b7a5bbebb922d6c02d33be72453e81955c2ec9187d
- evidence_id: full_qc_log
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-full-qc-after-exports.log.gz
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Final just qc exited 0 at 2026-11-01T05:35:25Z after synchronized exports/visual
    metadata; log SHA 717f4c100ff3dc91fa8f46eefd4674294f4c2f0b5a2efa838ac74c1a6c11fefe.
    Inspected final log; gzip when used is lossless.
  snapshot_sha256: 774e1bf4fe4bb77aec20802e420c80582f3febf9326d72e790e4134416222c5d
- evidence_id: mapping_qc_receipt
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-reviewed-sssom-qc.json
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Native assembler replay, supported/withheld export replay and schemas pass
    for 2,986 canonical rows. Actual command, times, exit status and log digest retained.
  snapshot_sha256: 6bd6d71f70d47331914911d12eb46aca6704948eaaf87a5f114d82b170517fe9
- evidence_id: mapping_qc_log
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-reviewed-sssom-qc.log
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Native assembler replay, supported/withheld export replay and schemas pass
    for 2,986 canonical rows. Inspected final log; gzip when used is lossless.
  snapshot_sha256: af9b5a362fad00b223ca94107d3d90ff26e370d1c36eaa78c42d9b11e70ba186
- evidence_id: canonical_invariants_receipt
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-canonical-invariants-actual-kg.json
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Canonical invariants pass against available actual KG transforms; missing
    BTO/MICRO transform limits remain explicit. Actual command, times, exit status
    and log digest retained.
  snapshot_sha256: 1967ed8fae5804e940cf9549fc5b9e757e0b8c43f2ecf245aa45fd0dc73c25f8
- evidence_id: canonical_invariants_log
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-canonical-invariants-actual-kg.log
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Canonical invariants pass against available actual KG transforms; missing
    BTO/MICRO transform limits remain explicit. Inspected final log; gzip when used
    is lossless.
  snapshot_sha256: e359124fa08279491b2032a31f005a93801de8104eb3cb9a81264637c5baa910
- evidence_id: product_labels_receipt
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-product-labels.json
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Native product-label command exits 0 while retaining 101 nonblocking warnings
    and 5,312 pairs without an adapter; this is not complete label approval. Actual
    command, times, exit status and log digest retained.
  snapshot_sha256: 919d4bc1db4419cb79518db4e8125efb84286c336f35003708249cdf8ed1b92a
- evidence_id: product_labels_log
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-product-labels.log
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Native product-label command exits 0 while retaining 101 nonblocking warnings
    and 5,312 pairs without an adapter; this is not complete label approval. Inspected
    final log; gzip when used is lossless.
  snapshot_sha256: 0398a65c658f872dd271612d18e18befa04dfded300d1f85dc313b0d51d6d80f
- evidence_id: semantic_integrity_receipt
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-semantic-integrity.json
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Current-review integrity passes while complete scientific release remains
    FAIL. Actual command, times, exit status and log digest retained.
  snapshot_sha256: 25748c1ba5c9c83e11daf7f98af8f421196f40cf352da72f8b0ebee140c00387
- evidence_id: semantic_integrity_log
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-semantic-integrity.log
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Current-review integrity passes while complete scientific release remains
    FAIL. Inspected final log; gzip when used is lossless.
  snapshot_sha256: b2f1341524d27201138e509b4ca6c7d3c0a14c4874543aa6cabe488eb049ddab
- evidence_id: supported_kgx_receipt
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-supported-kgx-qc.json
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Native supported-KGX replay validates exact approved selection and retained
    excluded claims. Actual command, times, exit status and log digest retained.
  snapshot_sha256: df9bca33a2d4b53b949e07c5020301b11717bdbc5cf178b43e206327c8ec3ad6
- evidence_id: supported_kgx_log
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-supported-kgx-qc.log
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Native supported-KGX replay validates exact approved selection and retained
    excluded claims. Inspected final log; gzip when used is lossless.
  snapshot_sha256: 76585cbf11b4249faf99cb3c31583d72dfc51dc094902f6e4f9dd4e2084816b7
- evidence_id: companion_validate_receipt
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-companion-validate.json
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Native companion validates its manifest, source/evidence bindings and all
    complete claim payloads. Actual command, times, exit status and log digest retained.
  snapshot_sha256: ecfa9021094032cf3aa228402f473143781a036fba398568c9befd7ddca0d785
- evidence_id: companion_validate_log
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-companion-validate.log
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Native companion validates its manifest, source/evidence bindings and all
    complete claim payloads. Inspected final log; gzip when used is lossless.
  snapshot_sha256: ce1e341213b171743cc30ebffe8905ffed4d4d4edbf8ab4d35f184dfdf154d41
- evidence_id: receipt_tests_receipt
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-receipt-regression-tests-after-generation.json
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Final post-generation regression suite passes 207 tests; prior stale-unified
    failure remains historical diagnostic only. Actual command, times, exit status
    and log digest retained.
  snapshot_sha256: a7bd727afa4725d6782e83d2428acf87fcd0dec9d224efba03f846e8a639abe6
- evidence_id: receipt_tests_log
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-receipt-regression-tests-after-generation.log
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Final post-generation regression suite passes 207 tests; prior stale-unified
    failure remains historical diagnostic only. Inspected final log; gzip when used
    is lossless.
  snapshot_sha256: e3c6db86bd88d95a35de6b4f30e2eff3ee427ab94874b85fc2acf85336ece906
- evidence_id: writer_audit_receipt
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-writer-audit.json
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Native writer audit passes for the final maintained writer. Actual command,
    times, exit status and log digest retained.
  snapshot_sha256: 108cc86085d82594891bb43762a2e736bb1d82cfa48f35216a9bdf9acff780c3
- evidence_id: writer_audit_log
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-writer-audit.log
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Native writer audit passes for the final maintained writer. Inspected final
    log; gzip when used is lossless.
  snapshot_sha256: 7cc62649a4c51e8faccb5698731bfc39e5b0bfcf6c877486418c041b91742778
- evidence_id: freshness_receipt
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-unified-stamp.json
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Native stamp and rejection/freshness checks pass after completed unified
    generation. Actual command, times, exit status and log digest retained.
  snapshot_sha256: 0e53c5228dd2f26b5b46121a53d0c5c08c68c372a74263ff2f50f4d966ea0480
- evidence_id: freshness_log
  kind: validation
  reference: reports/ncit_heptahydrate_875_20261101/execution/final-checks/logs/step2-unified-stamp.log
  accessed_at: '2026-11-01T05:39:24Z'
  support: supports
  summary: Native stamp and rejection/freshness checks pass after completed unified
    generation. Inspected final log; gzip when used is lossless.
  snapshot_sha256: d9aa9bda5950b09fc0431413f2032e4138a4bdcf006912a50d3b9487c6f036ff
assessments:
- assessment_id: identity
  area: identity
  topic: Approved exact supplied-form identity
  outcome: supported
  target_ids:
  - data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
  - issue875:mapping-row
  - reports/ncit_heptahydrate_875_20261101/sources/ncit-C61946.json
  - reports/ncit_heptahydrate_875_20261101/sources/ncit-C61946-receipt.json
  evidence_ids:
  - authority
  - owner
  - ncit
  - ncit_receipt
  - applied
  summary: The approved record denotes disodium hydrogenphosphate heptahydrate. The
    inspected NCI database assertion names that exact form and agrees with its CAS/formula;
    NCIT:C61946 replaces the local identity and anhydrous-parent mapping under section
    3 step 1.
  details: This assessment supports the bounded implementation identity choice. It
    does not approve inherited anhydrous InChI/SMILES or provisional BUFFER, and it
    does not create a native positive mapping disposition.
  dimensions:
  - name: exact_form
    value: disodium hydrogenphosphate heptahydrate
    definition: Specific seven-water supplied form; no anhydrous or sibling hydrate
      collapse.
    evidence_ids:
    - ncit
    - owner
  - name: evidence_tier
    value: official ontology database assertion
    definition: NCI EVS record inspected; no experimental role or mechanism inference.
    evidence_ids:
    - ncit
    - ncit_receipt
- assessment_id: history
  area: provenance
  topic: Append-only owner evidence and history
  outcome: supported
  target_ids:
  - data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
  - reports/ncit_heptahydrate_875_20261101/execution/application/source-apply.json
  evidence_ids:
  - applied
  - source_apply
  - historical_writer
  summary: Exactly one history event and one mapping-evidence entry are appended.
    All earlier history/evidence and unrelated owner fields remain identical. Actual
    source receipt hashes bind paired owner/ledger application; historical applied
    producer is preserved separately from the repaired producer.
- assessment_id: ledger
  area: consistency
  topic: Paired rejection-owner migration
  outcome: supported
  target_ids:
  - mappings/unified_mapping_rejections.tsv
  - issue875:rejection-row
  evidence_ids:
  - applied
  - products
  - source_apply
  summary: The 90-row ledger changes exactly the heptahydrate owner and rationale
    to NCIT:C61946. CHEBI:34683 remains rejected in unified identity columns; all
    other rows and the existing 33 source holds remain unchanged.
- assessment_id: writer
  area: representation
  topic: Guarded publication and recovery
  outcome: supported
  target_ids:
  - scripts/promote_heptahydrate_ncit.py
  - tests/test_promote_heptahydrate_ncit.py
  evidence_ids:
  - tests
  - race_before
  - race_after
  - writer_audit_receipt
  summary: The bounded writer validates exact input/candidate hashes, rejects partial
    or duplicate-destination states, preserves history and non-target rows, and treats
    a true repeat as a no-op. The repaired writer checks held reservation identities
    before mutation and around completion; all independent native race probes refuse
    false success.
  details: Individual replacements are atomic; a multi-file I/O failure may require
    explicit native-journal recovery. The writer does not claim whole-transaction
    filesystem atomicity or silently overwrite another writer’s evidence.
- assessment_id: canonical
  area: grounding
  topic: One exact mapping and bounded canonical promotion
  outcome: supported
  target_ids:
  - mappings/ingredient_mappings.sssom.tsv
  - reports/ncit_heptahydrate_875_20261101/execution/application/mapping-promotion.json
  - reports/sssom_completion_20260921/mapping_changes/issue875-ncit-exact-heptahydrate.json
  evidence_ids:
  - applied
  - candidate
  - promotion
  - receipt
  - mapping_qc_receipt
  - canonical_invariants_receipt
  summary: 'The 2,979-row diagnostic candidate contributes only the exact target row.
    Canonical SSSOM changes 2,987 to 2,986 rows: one ontology slot changed and one
    obsolete local registry row removed; every unrelated byte is preserved. Accepted
    hydrate aliases/CAS and historical provenance remain; obsolete ChEBI validation
    stamp is cleared.'
  metrics:
  - name: canonical rows
    value: 2986
    unit: rows
    definition: Complete final canonical table checked structurally; only one ingredient
      identity is scientifically in scope.
  - name: promoted canonical target rows
    value: 1
    unit: rows
    definition: One reviewed exact heptahydrate row selected from the native diagnostic
      candidate.
    denominator: 2979
- assessment_id: surfaces
  area: consistency
  topic: Synchronized maintained and generated surfaces
  outcome: supported
  target_ids:
  - data/curated/mapped_ingredients.yaml
  - data/curated/unmapped_ingredients.yaml
  - docs/data/label_index.csv
  - docs/data/ingredients.json
  evidence_ids:
  - applied
  - full_qc_receipt
  - visual
  summary: Both aggregate collections preserve all non-target records and agree with
    the final owner. Full QC validates current indexes, browser/list exports and visualization
    metadata; only the target identity metadata changes in the visual products.
- assessment_id: unified
  area: consistency
  topic: Complete unified comparison with bounded identity interpretation
  outcome: supported
  target_ids:
  - UNIFIED_INGREDIENT_MAPPING.tsv
  - UNIFIED_INGREDIENT_MAPPING.provenance.json
  - issue875:unified-1
  - issue875:unified-2
  - issue875:unified-3
  evidence_ids:
  - products
  - unified_inputs
  - freshness_receipt
  summary: All 4,170 rows were structurally compared. Exactly three target spellings
    change mim_id and gain the NCI label; 4,167 rows, every occurrence count and recipe
    example remain identical. All 18,873 generation input hashes verify. No REJECTED
    row has an empty mim_id and no kgmicrobe.compound row leaks CHEBI.
  metrics:
  - name: structurally compared unified rows
    value: 4170
    unit: rows
    definition: All final rows compared to baseline; not a count of scientifically
      reviewed ingredients.
    denominator: 4170
  - name: unchanged rows
    value: 4167
    unit: rows
    definition: Byte-equivalent row payloads under the proper plain TSV reader.
    denominator: 4170
  - name: retained source occurrences
    value: 209330
    unit: occurrences
    definition: Sum of all occurrence_count values, unchanged from baseline.
- assessment_id: refresh
  area: provenance
  topic: Location changes without scientific approval
  outcome: supported
  target_ids:
  - src/mediaingredientmech/ingredient_bundle_refresh.py
  - tests/test_ingredient_bundle_dependency_refresh.py
  - reports/ingredient_bundle_20261101_ncit875/review.json
  - reports/ingredient_bundle_20261101_ncit875/dependency-refresh.json
  - reports/ingredient_bundle_20261101_ncit875/prior-review.json
  evidence_ids:
  - refresh
  - products
  - tests
  - companion_validate_receipt
  summary: The maintained refresh preserves all 20 owners, 51 complete claims/decisions,
    selected row payloads and complete resolved evidence. Fourteen verified locations
    move; source_position and evidence_key alone are excluded from semantic decision
    comparison. Native successor bytes and every audit field replay exactly; no approval
    is added.
- assessment_id: mapping_review
  area: scope
  topic: Retained mapping-specific withholding
  outcome: supported
  target_ids:
  - reports/sssom_completion_20260921/assemble_review.py
  - reports/sssom_completion_20260921/review.json
  - reports/sssom_completion_20260921/mapping-evidence.json
  - docs/SSSOM_RELEASE.md
  evidence_ids:
  - receipt
  - mapping_qc_receipt
  - products
  - profile
  summary: The 16th receipt preserves the full prior chain and grants no approval.
    The new NCIT row remains WITHHOLD. Every other mapping decision and complete evidence
    entry is preserved through the position map; 1,740 supported and 1,246 withheld
    rows remain explicit.
- assessment_id: semantic
  area: scope
  topic: Preserved unresolved chemistry and role findings
  outcome: supported
  target_ids:
  - reports/semantic_review_20260921/resolution/current-review.json
  - reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  - reports/semantic_review_20260921/resolution/assertion-dispositions.tsv
  evidence_ids:
  - products
  - semantic_integrity_receipt
  - supported_kgx_receipt
  - profile
  summary: The target BUFFER assertion remains OPEN and the two existing finding rows
    update only owner hashes. Nonmapping approvals are unchanged. Full scientific
    release remains FAIL with 1,733 blocking findings and 2,271 blocking assertions;
    one withheld registry assertion was removed, with no new approval.
- assessment_id: selection
  area: ownership
  topic: Explicit companion selection and protected dependencies
  outcome: supported
  target_ids:
  - .github/workflows/qc-reviewed-sssom.yaml
  - tests/test_ingredient_bundle.py
  - docs/INGREDIENT_BUNDLE.md
  - .github/workflows/qc-evidence.yaml
  - scripts/.vendored_canon_ref
  evidence_ids:
  - refresh
  - companion_validate_receipt
  - full_qc_receipt
  summary: CI, public instructions and integration tests explicitly select the verified
    immutable successor. Prior reports remain preserved. The evidence workflow and
    canonical validator pin are byte-identical to durable baseline 40b787d.
- assessment_id: documentation
  area: provenance
  topic: Portable evidence and explicit execution limits
  outcome: supported
  target_ids:
  - reports/ncit_heptahydrate_875_20261101/README.md
  - reports/ncit_heptahydrate_875_20261101/execution/README.md
  evidence_ids:
  - documentation
  - inventory
  - supplement
  - historical_writer
  - race_after
  summary: Portable reports preserve exact source/candidate/application/receipt evidence,
    original failures and repaired results, historical producer bytes, and the complete
    QC snapshot. Diagnostic 2,979-row candidate, final 2,986-row canonical table,
    native approval boundaries and incomplete ontology-adapter coverage are distinguished.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
  - issue875:mapping-row
  rationale: Keep the specific seven-water substance distinct from anhydrous and sibling
    hydrates; use the approved exact NCIT term rather than the superseded local/parent
    pair.
  evidence_ids:
  - authority
  - ncit
  - applied
- action: defer
  target_ids:
  - data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
  - reports/semantic_review_20260921/resolution/current-review.json
  rationale: Preserve open chemistry/BUFFER findings and mapping WITHHOLD. No full-record
    or positive native mapping approval follows from this bounded implementation review.
  evidence_ids:
  - owner
  - products
  - profile
limitations:
- This structural/provenance-focused review includes bounded exact-form identity checks
  only; scientific_review is false and no native approval is authored.
- Inherited anhydrous InChI/SMILES and provisional BUFFER evidence remain unresolved.
  Full scientific release remains FAIL with 1,733 blocking findings and 2,271 blocking
  assertions.
- Native canonical invariants skip B4 where BTO and MICRO transform inputs are absent.
  Product label validation retains 101 nonblocking warnings and 5,312 pairs without
  an adapter; no comprehensive ontology-label approval is claimed.
- A live web-tool EVS recheck was unavailable. The complete official response fetched
  at 2026-11-01T04:19:28Z and its exact hash-bound HTTP receipt were inspected instead.
- Root executed full native QC and release gates; the reviewer verified their exact
  receipts/logs and independently ran 133 focused tests, real-native race probes,
  all candidate/unified input hashes and complete bounded artifact/approval comparisons.
- The native source is the actual working tree on durable merged base 40b787d with
  frozen index ad33965a8b3f599aec721ca84f7eeb3658be7379. Final committed-head verification
  and remote CI remain separate subsequent requirements.
notes:
- '#1028 and #1029 were filed before fixes. Original failure probes and historical
  applied writer are retained alongside repaired checks. They were not earlier structured
  findings; no previous_occurrences or invented terminal finding dispositions are
  created.'
- Historical pre-generation test/QC failures and the incorrect comment-filtered TSV
  comparison remain explicit diagnostics; final corrected runs and the proper plain-TSV
  comparison support this review.
- This review captures 235 staged file hashes and full index/tree equality before
  inspecting 256 native inputs. No source revision was relabeled and no transient
  feature commit was used.
links:
- https://github.com/CultureBotAI/MediaIngredientMech/issues/875
- https://github.com/CultureBotAI/MediaIngredientMech/issues/1028
- https://github.com/CultureBotAI/MediaIngredientMech/issues/1029
tags:
- approved-plan-step2
- exact-heptahydrate
- bounded-review
- no-scientific-approval
```
