# Approved step 1: bounded unified mapping and provenance review

- Review: 20261101T035857Z-approved-plan-step1-unified-review
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-11-01T03:58:14Z
- Finished UTC: 2026-11-01T03:58:57Z
- Reviewer: Codex independent reviewer /root/step1_independent_review (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

No unresolved in-scope findings remain in the frozen 66-target review. Required structural/provenance checks pass, including the nine representatives, two unresolved supplied forms, exact 33 source holds and the complete 4,170-row native artifact. The existing full semantic-release FAIL remains explicit.

## Scope And Provenance

66 declared targets: 33 artifacts and 33 exact unified snapshot rows. Structural checks cover every unified row. Ontology identity interpretation is limited to the nine representatives, two unresolved forms and finite 33 negative source-label decisions.

Selection: Approved-plan step-1 changed source/records/ledger and core generated outputs, protected excluded pin files, and every row of the finite source-hold cohort. No random sampling.
Coverage: full; 66 reviewed / 66 in the declared population.
Source: working_tree at Git base 2add44fbfe37544218d2f4daeb322b35debc5dd4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| data/ingredients/mapped/Calcium_Chloride.yaml | data/ingredients/mapped/Calcium_Chloride.yaml | maintained | Calcium_Chloride.yaml |
| data/ingredients/mapped/Cinnamic_Acid.yaml | data/ingredients/mapped/Cinnamic_Acid.yaml | maintained | Cinnamic_Acid.yaml |
| data/ingredients/mapped/Cocl2_X_6_H2o.yaml | data/ingredients/mapped/Cocl2_X_6_H2o.yaml | maintained | Cocl2_X_6_H2o.yaml |
| data/ingredients/mapped/Mgcl2x_6_H2o.yaml | data/ingredients/mapped/Mgcl2x_6_H2o.yaml | maintained | Mgcl2x_6_H2o.yaml |
| data/ingredients/mapped/Na-glutamate.yaml | data/ingredients/mapped/Na-glutamate.yaml | maintained | Na-glutamate.yaml |
| data/ingredients/mapped/Na2moo42h2o.yaml | data/ingredients/mapped/Na2moo42h2o.yaml | maintained | Na2moo42h2o.yaml |
| data/ingredients/mapped/Nah2po4h2o.yaml | data/ingredients/mapped/Nah2po4h2o.yaml | maintained | Nah2po4h2o.yaml |
| data/ingredients/mapped/Sodium_Citrate.yaml | data/ingredients/mapped/Sodium_Citrate.yaml | maintained | Sodium_Citrate.yaml |
| data/ingredients/mapped/Trisodium_Citrate_X_2_H2o.yaml | data/ingredients/mapped/Trisodium_Citrate_X_2_H2o.yaml | maintained | Trisodium_Citrate_X_2_H2o.yaml |
| data/ingredients/unmapped/Na2moo4_X_H2o.yaml | data/ingredients/unmapped/Na2moo4_X_H2o.yaml | maintained | Na2moo4_X_H2o.yaml |
| data/ingredients/unmapped/Trisodium_Citrate_X_3_H2o.yaml | data/ingredients/unmapped/Trisodium_Citrate_X_3_H2o.yaml | maintained | Trisodium_Citrate_X_3_H2o.yaml |
| scripts/apply_312_batch1.py | scripts/apply_312_batch1.py | maintained | apply_312_batch1.py |
| scripts/apply_312_batch4.py | scripts/apply_312_batch4.py | maintained | apply_312_batch4.py |
| scripts/check_unified_rejections.py | scripts/check_unified_rejections.py | maintained | check_unified_rejections.py |
| scripts/fix_merge_tombstone_resolution.py | scripts/fix_merge_tombstone_resolution.py | maintained | fix_merge_tombstone_resolution.py |
| scripts/merge_mapped_records.py | scripts/merge_mapped_records.py | maintained | merge_mapped_records.py |
| scripts/retire_wrong_form_names.py | scripts/retire_wrong_form_names.py | maintained | retire_wrong_form_names.py |
| tests/test_fix_merge_tombstone_resolution.py | tests/test_fix_merge_tombstone_resolution.py | maintained | test_fix_merge_tombstone_resolution.py |
| tests/test_merge_mapped_records.py | tests/test_merge_mapped_records.py | maintained | test_merge_mapped_records.py |
| tests/test_unified_rejections.py | tests/test_unified_rejections.py | maintained | test_unified_rejections.py |
| mappings/unified_mapping_rejections.tsv | mappings/unified_mapping_rejections.tsv | maintained | unified_mapping_rejections.tsv |
| data/curated/mapped_ingredients.yaml | data/curated/mapped_ingredients.yaml | maintained | mapped_ingredients.yaml |
| data/curated/unmapped_ingredients.yaml | data/curated/unmapped_ingredients.yaml | maintained | unmapped_ingredients.yaml |
| reports/semantic_review_20260921/resolution/finding-dispositions.tsv | reports/semantic_review_20260921/resolution/finding-dispositions.tsv | maintained | finding-dispositions.tsv |
| .github/workflows/qc-evidence.yaml | .github/workflows/qc-evidence.yaml | maintained | qc-evidence.yaml |
| scripts/.vendored_canon_ref | scripts/.vendored_canon_ref | maintained | .vendored_canon_ref |
| UNIFIED_INGREDIENT_MAPPING.tsv | UNIFIED_INGREDIENT_MAPPING.tsv | generated | UNIFIED_INGREDIENT_MAPPING.tsv |
| UNIFIED_INGREDIENT_MAPPING.provenance.json | UNIFIED_INGREDIENT_MAPPING.provenance.json | generated | UNIFIED_INGREDIENT_MAPPING.provenance.json |
| docs/data/label_index.csv | docs/data/label_index.csv | generated | label_index.csv |
| reports/semantic_review_20260921/resolution/current-review.json | reports/semantic_review_20260921/resolution/current-review.json | generated | current-review.json |
| mappings/ingredient_mappings.sssom.tsv | mappings/ingredient_mappings.sssom.tsv | generated | ingredient_mappings.sssom.tsv |
| docs/UNIFIED_MAPPING_REJECTIONS.md | docs/UNIFIED_MAPPING_REJECTIONS.md | maintained | UNIFIED_MAPPING_REJECTIONS.md |
| tests/test_unified_source_holds.py | tests/test_unified_source_holds.py | maintained | test_unified_source_holds.py |
| held-source-75b6be4855ac | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "1 M K2HPO4" | snapshot_row | 1 M K2HPO4 (withhold CHEBI:131527) |
| held-source-71272ca0256b | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "1 M KH2PO4" | snapshot_row | 1 M KH2PO4 (withhold CHEBI:63036) |
| held-source-d7ebfb492d5b | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "1 M Sodium acetate solution" | snapshot_row | 1 M Sodium acetate solution (withhold CHEBI:32954) |
| held-source-15ba44ba7cd2 | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "1 M Tris base (pH 8)" | snapshot_row | 1 M Tris base (pH 8) (withhold CHEBI:9754) |
| held-source-c6f37a149c7f | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "1 N NaOH" | snapshot_row | 1 N NaOH (withhold CHEBI:32145) |
| held-source-ccc30f9dedb1 | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "10% Glucose solution" | snapshot_row | 10% Glucose solution (withhold CHEBI:17234) |
| held-source-aa607f02029a | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "25% HCl (7.7 M)" | snapshot_row | 25% HCl (7.7 M) (withhold CHEBI:17883) |
| held-source-c5ba604021fa | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "5% L-Cysteine·HCl·H2O solution" | snapshot_row | 5% L-Cysteine·HCl·H2O solution (withhold CHEBI:91248) |
| held-source-f63aedfafd31 | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "5% Na2S·9H2O solution" | snapshot_row | 5% Na2S·9H2O solution (withhold CHEBI:76209) |
| held-source-7e65c46c2293 | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "8% NaHCO3 solution" | snapshot_row | 8% NaHCO3 solution (withhold CHEBI:32139) |
| held-source-dace2106e06b | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "Cyanocobalamin (Vitamin B12)" | snapshot_row | Cyanocobalamin (Vitamin B12) (withhold CHEBI:176843) |
| held-source-3a3b5e39bb77 | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "MnSO4·xH2O" | snapshot_row | MnSO4·xH2O (withhold CHEBI:86360) |
| held-source-c8eb7b83415a | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "1 M CaCl2 solution" | snapshot_row | 1 M CaCl2 solution (withhold CHEBI:3312) |
| held-source-d93760b262a3 | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "1 M K2HPO4 solution" | snapshot_row | 1 M K2HPO4 solution (withhold CHEBI:131527) |
| held-source-4b310c169232 | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "1 M MgCl2 solution" | snapshot_row | 1 M MgCl2 solution (withhold CHEBI:6636) |
| held-source-4a8883d91734 | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "1 M Sodium fumarate solution" | snapshot_row | 1 M Sodium fumarate solution (withhold CHEBI:115156) |
| held-source-a8866814ba73 | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "1 N KOH" | snapshot_row | 1 N KOH (withhold CHEBI:32035) |
| held-source-3a5de9f5d9a3 | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "2 M NH4Cl solution" | snapshot_row | 2 M NH4Cl solution (withhold CHEBI:31206) |
| held-source-1069c74d36aa | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "3% L-Cysteine HCl x H2O solution" | snapshot_row | 3% L-Cysteine HCl x H2O solution (withhold CHEBI:91248) |
| held-source-eafe22a42e90 | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "3% Na2S x 9 H2O solution" | snapshot_row | 3% Na2S x 9 H2O solution (withhold CHEBI:76209) |
| held-source-562a206a3c27 | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "4 M NH4Cl solution" | snapshot_row | 4 M NH4Cl solution (withhold CHEBI:31206) |
| held-source-d70db50995af | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "5% Na2S x 9 H2O solution" | snapshot_row | 5% Na2S x 9 H2O solution (withhold CHEBI:76209) |
| held-source-8ebfaa26db29 | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "Ethanol (95 %)" | snapshot_row | Ethanol (95 %) (withhold CHEBI:16236) |
| held-source-7ec2823f4bfb | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "FeSO4 x 7 H2O (0.1% w/v in 0.1 N H2SO4)" | snapshot_row | FeSO4 x 7 H2O (0.1% w/v in 0.1 N H2SO4) (withhold CHEBI:75836) |
| held-source-783cf521df3c | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "HEPES buffer pH 7.8" | snapshot_row | HEPES buffer pH 7.8 (withhold CHEBI:42334) |
| held-source-764c8c8dafdd | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "KOH solution" | snapshot_row | KOH solution (withhold CHEBI:32035) |
| held-source-e524fe3c1ab2 | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "NaOH (1 N)" | snapshot_row | NaOH (1 N) (withhold CHEBI:32145) |
| held-source-660ea2039881 | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "Sulfuric acid (concentrated)" | snapshot_row | Sulfuric acid (concentrated) (withhold CHEBI:26836) |
| held-source-458fec7ef628 | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "Tricine (pH 8)" | snapshot_row | Tricine (pH 8) (withhold CHEBI:46760) |
| held-source-69c98a290efb | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "MnSO4 x xH2O" | snapshot_row | MnSO4 x xH2O (withhold CHEBI:86360) |
| held-source-38acc372c42d | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "MnSO4.xH2O" | snapshot_row | MnSO4.xH2O (withhold CHEBI:86360) |
| held-source-6d07f7e6c3a8 | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "Cyanocobalamin (B12)" | snapshot_row | Cyanocobalamin (B12) (withhold CHEBI:176843) |
| held-source-715cfe1166c2 | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name = "Vitamin B12 (Cobalamin)" | snapshot_row | Vitamin B12 (Cobalamin) (withhold CHEBI:176843) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused regressions | passed | True | data/ingredients/mapped/Calcium_Chloride.yaml, data/ingredients/mapped/Cinnamic_Acid.yaml, data/ingredients/mapped/Cocl2_X_6_H2o.yaml, data/ingredients/mapped/Mgcl2x_6_H2o.yaml, data/ingredients/mapped/Na-glutamate.yaml, data/ingredients/mapped/Na2moo42h2o.yaml, data/ingredients/mapped/Nah2po4h2o.yaml, data/ingredients/mapped/Sodium_Citrate.yaml, data/ingredients/mapped/Trisodium_Citrate_X_2_H2o.yaml, data/ingredients/unmapped/Na2moo4_X_H2o.yaml, data/ingredients/unmapped/Trisodium_Citrate_X_3_H2o.yaml, scripts/apply_312_batch1.py, scripts/apply_312_batch4.py, scripts/check_unified_rejections.py, scripts/fix_merge_tombstone_resolution.py, scripts/merge_mapped_records.py, scripts/retire_wrong_form_names.py, tests/test_fix_merge_tombstone_resolution.py, tests/test_merge_mapped_records.py, tests/test_unified_rejections.py, tests/test_unified_source_holds.py, held-source-75b6be4855ac, held-source-71272ca0256b, held-source-d7ebfb492d5b, held-source-15ba44ba7cd2, held-source-c6f37a149c7f, held-source-ccc30f9dedb1, held-source-aa607f02029a, held-source-c5ba604021fa, held-source-f63aedfafd31, held-source-7e65c46c2293, held-source-dace2106e06b, held-source-3a3b5e39bb77, held-source-c8eb7b83415a, held-source-d93760b262a3, held-source-4b310c169232, held-source-4a8883d91734, held-source-a8866814ba73, held-source-3a5de9f5d9a3, held-source-1069c74d36aa, held-source-eafe22a42e90, held-source-562a206a3c27, held-source-d70db50995af, held-source-8ebfaa26db29, held-source-7ec2823f4bfb, held-source-783cf521df3c, held-source-764c8c8dafdd, held-source-e524fe3c1ab2, held-source-660ea2039881, held-source-458fec7ef628, held-source-69c98a290efb, held-source-38acc372c42d, held-source-6d07f7e6c3a8, held-source-715cfe1166c2, mappings/unified_mapping_rejections.tsv, UNIFIED_INGREDIENT_MAPPING.tsv | 67 tests passed, covering repaired history, identifiers, representative routing, both ledger scopes and the final held cohort. |
| Approved step-1 acceptance | passed | True | data/ingredients/mapped/Calcium_Chloride.yaml, data/ingredients/mapped/Cinnamic_Acid.yaml, data/ingredients/mapped/Cocl2_X_6_H2o.yaml, data/ingredients/mapped/Mgcl2x_6_H2o.yaml, data/ingredients/mapped/Na-glutamate.yaml, data/ingredients/mapped/Na2moo42h2o.yaml, data/ingredients/mapped/Nah2po4h2o.yaml, data/ingredients/mapped/Sodium_Citrate.yaml, data/ingredients/mapped/Trisodium_Citrate_X_2_H2o.yaml, data/ingredients/unmapped/Na2moo4_X_H2o.yaml, data/ingredients/unmapped/Trisodium_Citrate_X_3_H2o.yaml, mappings/unified_mapping_rejections.tsv, UNIFIED_INGREDIENT_MAPPING.tsv, .github/workflows/qc-evidence.yaml, scripts/.vendored_canon_ref | All required identity invariants and preserved histories/pins pass. |
| All-row native-output comparison and receipt verification | passed | True | UNIFIED_INGREDIENT_MAPPING.tsv, UNIFIED_INGREDIENT_MAPPING.provenance.json, mappings/ingredient_mappings.sssom.tsv, held-source-75b6be4855ac, held-source-71272ca0256b, held-source-d7ebfb492d5b, held-source-15ba44ba7cd2, held-source-c6f37a149c7f, held-source-ccc30f9dedb1, held-source-aa607f02029a, held-source-c5ba604021fa, held-source-f63aedfafd31, held-source-7e65c46c2293, held-source-dace2106e06b, held-source-3a3b5e39bb77, held-source-c8eb7b83415a, held-source-d93760b262a3, held-source-4b310c169232, held-source-4a8883d91734, held-source-a8866814ba73, held-source-3a5de9f5d9a3, held-source-1069c74d36aa, held-source-eafe22a42e90, held-source-562a206a3c27, held-source-d70db50995af, held-source-8ebfaa26db29, held-source-7ec2823f4bfb, held-source-783cf521df3c, held-source-764c8c8dafdd, held-source-e524fe3c1ab2, held-source-660ea2039881, held-source-458fec7ef628, held-source-69c98a290efb, held-source-38acc372c42d, held-source-6d07f7e6c3a8, held-source-715cfe1166c2 | 4,170 rows match; 33 held labels change; 4,137 other rows and all source count/example fields stay identical. All 18,873 generation inputs match recorded hashes. |
| Ledger-source and stale-output negative control | passed | True | mappings/unified_mapping_rejections.tsv, scripts/check_unified_rejections.py, held-source-75b6be4855ac, held-source-71272ca0256b, held-source-d7ebfb492d5b, held-source-15ba44ba7cd2, held-source-c6f37a149c7f, held-source-ccc30f9dedb1, held-source-aa607f02029a, held-source-c5ba604021fa, held-source-f63aedfafd31, held-source-7e65c46c2293, held-source-dace2106e06b, held-source-3a3b5e39bb77, held-source-c8eb7b83415a, held-source-d93760b262a3, held-source-4b310c169232, held-source-4a8883d91734, held-source-a8866814ba73, held-source-3a5de9f5d9a3, held-source-1069c74d36aa, held-source-eafe22a42e90, held-source-562a206a3c27, held-source-d70db50995af, held-source-8ebfaa26db29, held-source-7ec2823f4bfb, held-source-783cf521df3c, held-source-764c8c8dafdd, held-source-e524fe3c1ab2, held-source-660ea2039881, held-source-458fec7ef628, held-source-69c98a290efb, held-source-38acc372c42d, held-source-6d07f7e6c3a8, held-source-715cfe1166c2 | All 33 cited source selectors match; all 57 prior ledger rows form an exact prefix. The pre-hold export is rejected with 126 messages covering all 33 held labels. |
| Full native QC | passed | True | data/ingredients/mapped/Calcium_Chloride.yaml, data/ingredients/mapped/Cinnamic_Acid.yaml, data/ingredients/mapped/Cocl2_X_6_H2o.yaml, data/ingredients/mapped/Mgcl2x_6_H2o.yaml, data/ingredients/mapped/Na-glutamate.yaml, data/ingredients/mapped/Na2moo42h2o.yaml, data/ingredients/mapped/Nah2po4h2o.yaml, data/ingredients/mapped/Sodium_Citrate.yaml, data/ingredients/mapped/Trisodium_Citrate_X_2_H2o.yaml, data/ingredients/unmapped/Na2moo4_X_H2o.yaml, data/ingredients/unmapped/Trisodium_Citrate_X_3_H2o.yaml, scripts/apply_312_batch1.py, scripts/apply_312_batch4.py, scripts/check_unified_rejections.py, scripts/fix_merge_tombstone_resolution.py, scripts/merge_mapped_records.py, scripts/retire_wrong_form_names.py, tests/test_fix_merge_tombstone_resolution.py, tests/test_merge_mapped_records.py, tests/test_unified_rejections.py, mappings/unified_mapping_rejections.tsv, data/curated/mapped_ingredients.yaml, data/curated/unmapped_ingredients.yaml, reports/semantic_review_20260921/resolution/finding-dispositions.tsv, .github/workflows/qc-evidence.yaml, scripts/.vendored_canon_ref, UNIFIED_INGREDIENT_MAPPING.tsv, UNIFIED_INGREDIENT_MAPPING.provenance.json, docs/data/label_index.csv, reports/semantic_review_20260921/resolution/current-review.json, mappings/ingredient_mappings.sssom.tsv, docs/UNIFIED_MAPPING_REJECTIONS.md, tests/test_unified_source_holds.py, held-source-75b6be4855ac, held-source-71272ca0256b, held-source-d7ebfb492d5b, held-source-15ba44ba7cd2, held-source-c6f37a149c7f, held-source-ccc30f9dedb1, held-source-aa607f02029a, held-source-c5ba604021fa, held-source-f63aedfafd31, held-source-7e65c46c2293, held-source-dace2106e06b, held-source-3a3b5e39bb77, held-source-c8eb7b83415a, held-source-d93760b262a3, held-source-4b310c169232, held-source-4a8883d91734, held-source-a8866814ba73, held-source-3a5de9f5d9a3, held-source-1069c74d36aa, held-source-eafe22a42e90, held-source-562a206a3c27, held-source-d70db50995af, held-source-8ebfaa26db29, held-source-7ec2823f4bfb, held-source-783cf521df3c, held-source-764c8c8dafdd, held-source-e524fe3c1ab2, held-source-660ea2039881, held-source-458fec7ef628, held-source-69c98a290efb, held-source-38acc372c42d, held-source-6d07f7e6c3a8, held-source-715cfe1166c2 | Full just qc passes, including schema/strict, evidence, SSSOM, roundtrip, visualization currency and flat export coverage. Execution was by the root agent; this reviewer inspected the final log and verified its hash. |
| SSSOM receipt replay | passed | True | mappings/ingredient_mappings.sssom.tsv | Replay reproduces all 2,987 rows with 1,740 SUPPORTED and 1,247 WITHHOLD dispositions. |
| Reviewed SSSOM and schema | passed | True | mappings/ingredient_mappings.sssom.tsv | Existing reviewed SSSOM export and schema validation pass. |
| Supported KGX | passed | True | reports/semantic_review_20260921/resolution/current-review.json | Supported KGX validation passes while preserving excluded claims. |
| Companion bundle | passed | True | UNIFIED_INGREDIENT_MAPPING.tsv, mappings/ingredient_mappings.sssom.tsv | Companion bundle validation passes against the unchanged manifest. |
| Native semantic-review integrity | passed | True | reports/semantic_review_20260921/resolution/current-review.json, reports/semantic_review_20260921/resolution/finding-dispositions.tsv | Integrity passes; the full semantic release remains FAIL with the preexisting 1,733 finding and 2,272 assertion blockers. |
| optional visual regeneration | failed | False | data/curated/mapped_ingredients.yaml, docs/data/label_index.csv | Initial combined sync/export run completed those exports but optional visualization regeneration failed because the isolated embedding cache was absent. Final native QC independently verifies the exports and current published visualizations. |
| visualization currency | passed | True | data/curated/mapped_ingredients.yaml, docs/data/label_index.csv | Both published visualization products are current with 2,340 live nodes each; the final full QC also repeats the currency gate. |

## Scientific And Domain Assessments

### Explicit live representatives for rejected aliases

identity: supported. Targets: data/ingredients/mapped/Calcium_Chloride.yaml, data/ingredients/mapped/Cinnamic_Acid.yaml, data/ingredients/mapped/Cocl2_X_6_H2o.yaml, data/ingredients/mapped/Mgcl2x_6_H2o.yaml, data/ingredients/mapped/Na-glutamate.yaml, data/ingredients/mapped/Na2moo42h2o.yaml, data/ingredients/mapped/Nah2po4h2o.yaml, data/ingredients/mapped/Sodium_Citrate.yaml, data/ingredients/mapped/Trisodium_Citrate_X_2_H2o.yaml.

All nine tombstones retain REJECTED status and point to the reviewed live representatives. Form-specific targets preserve hydrate, salt and stereochemical boundaries.

This assesses representative routing and selected refused synonyms. Historical inactive chemistry, role and evidence fields retained in tombstones are not newly scientifically approved.

### Unmapped monohydrate and trihydrate surface forms

identity: supported. Targets: data/ingredients/unmapped/Na2moo4_X_H2o.yaml, data/ingredients/unmapped/Trisodium_Citrate_X_3_H2o.yaml.

UNMAPPED_0851 and UNMAPPED_0852 preserve the sodium-molybdate monohydrate and trisodium-citrate trihydrate surface forms without a guessed ontology identity. All nine synonyms resolve to the intended owner and both corrections append history.

### Append-only repairs and corrected rationale

provenance: supported. Targets: scripts/fix_merge_tombstone_resolution.py, tests/test_fix_merge_tombstone_resolution.py, data/ingredients/mapped/Na-glutamate.yaml, data/ingredients/mapped/Sodium_Citrate.yaml.

Repeated necessary repairs preserve the earlier event prefix and become idempotent. Corrected future rationale and appended CORRECTED_PROVENANCE events resolve the two wrong ontology citations while preserving older history.

### Merge and retirement identity routing

representation: supported. Targets: scripts/apply_312_batch1.py, scripts/apply_312_batch4.py, scripts/fix_merge_tombstone_resolution.py, scripts/merge_mapped_records.py, scripts/retire_wrong_form_names.py, tests/test_merge_mapped_records.py.

The changed writers record explicit representatives and avoid new REJECTED status transitions that could hide a documented merge. New repair allocations avoid the retired placeholder IDs; regression tests cover representative creation and repair behavior.

### Identity-wide rejections and exact source-label holds

consistency: supported. Targets: scripts/check_unified_rejections.py, docs/UNIFIED_MAPPING_REJECTIONS.md, mappings/unified_mapping_rejections.tsv, tests/test_unified_rejections.py, tests/test_unified_source_holds.py.

The 90-row ledger preserves its 57-row prefix and adds exactly the 33 reviewed blank-replacement pairs. The checker retains legacy identity preservation, rejects malformed cells and catches held IDs in all five identity columns without creating a global empty-identity rule.

Independent different-ID ownership remains permitted by the consumer; the producer validates owner contradictions before generation. The finite final corpus has no independent owners for the 33 held labels.

### Finite preparation-scope withholding

scope: supported. Targets: held-source-75b6be4855ac, held-source-71272ca0256b, held-source-d7ebfb492d5b, held-source-15ba44ba7cd2, held-source-c6f37a149c7f, held-source-ccc30f9dedb1, held-source-aa607f02029a, held-source-c5ba604021fa, held-source-f63aedfafd31, held-source-7e65c46c2293, held-source-c8eb7b83415a, held-source-d93760b262a3, held-source-4b310c169232, held-source-4a8883d91734, held-source-a8866814ba73, held-source-3a5de9f5d9a3, held-source-1069c74d36aa, held-source-eafe22a42e90, held-source-562a206a3c27, held-source-d70db50995af, held-source-8ebfaa26db29, held-source-7ec2823f4bfb, held-source-783cf521df3c, held-source-764c8c8dafdd, held-source-e524fe3c1ab2, held-source-660ea2039881, held-source-458fec7ef628.

All 27 explicit concentration, solvent, solution or pH-qualified source labels remain UNMAPPED pending preparation curation. No neat-reagent identity or borrowed metadata survives, and all source labels, counts and media examples remain.

### Variable manganese-sulfate hydration

identity: supported. Targets: held-source-3a3b5e39bb77, held-source-69c98a290efb, held-source-38acc372c42d.

All three variable-hydration source labels withhold the anhydrous manganese(II) sulfate ID. They retain their source occurrence information without inventing a specific hydrate identity.

### Vitamin B12 class/member boundaries

scope: supported. Targets: held-source-dace2106e06b, held-source-6d07f7e6c3a8, held-source-715cfe1166c2.

The two explicitly cyanocobalamin labels withhold the broad vitamin B12 class. Vitamin B12 (Cobalamin) remains held pending scope clarification; no substitute identity is selected.

The cobalamin hold is a conservative unresolved-scope decision, distinct from the two explicit cyanocobalamin/class mismatches. These assessments support withholding rather than scientific approval of an alternate mapping.

### Synchronized and reproducible generated products

consistency: supported. Targets: data/curated/mapped_ingredients.yaml, data/curated/unmapped_ingredients.yaml, docs/data/label_index.csv, UNIFIED_INGREDIENT_MAPPING.tsv, UNIFIED_INGREDIENT_MAPPING.provenance.json.

Native QC validates synchronized records, indexes and current list/browser products. All 4,170 unified rows match the native builder and the provenance digest matches 2,955 MIM inputs. The final hold-only delta changes exactly 33 rows and preserves all source occurrence counts and examples.

The provenance mim_rev intentionally records the durable merge-base under the existing freshness contract; exact current input hashes establish the working-tree content. The initial 54 changed identities and 290 added labels were screened for this fallback mechanism, not comprehensively scientifically approved.

### Unchanged canonical mapping and retained receipt dispositions

consistency: supported. Targets: mappings/ingredient_mappings.sssom.tsv.

Canonical SSSOM remains byte-identical to baseline 2add44fb: 2,987 rows with SHA256 a2b83ccdcaad67d89943ccf0f0e30d796cdbc5e418ead247313631b713e89722. Native invariants and receipt replay pass; supported/withheld dispositions remain unchanged.

### Current hashes with preserved scientific-release holds

provenance: supported. Targets: reports/semantic_review_20260921/resolution/current-review.json, reports/semantic_review_20260921/resolution/finding-dispositions.tsv.

The current native review has valid integrity. Nine finding rows update only current-record hashes; blocker identities and all dispositions remain unchanged. Full semantic release still fails on 1,733 findings and 2,272 assertions.

This positive assessment concerns faithful preservation of native evidence and release boundaries. It does not resolve or approve the preexisting scientific backlog.

### Approved dependency boundary

scope: supported. Targets: .github/workflows/qc-evidence.yaml, scripts/.vendored_canon_ref.

Both excluded pin/workflow files match baseline. The unified producer uses the separately reviewed merged Claw source-hold change while the evidence validator remains on its approved pinned revision.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: data/ingredients/mapped/Calcium_Chloride.yaml, data/ingredients/mapped/Cinnamic_Acid.yaml, data/ingredients/mapped/Cocl2_X_6_H2o.yaml, data/ingredients/mapped/Mgcl2x_6_H2o.yaml, data/ingredients/mapped/Na-glutamate.yaml, data/ingredients/mapped/Na2moo42h2o.yaml, data/ingredients/mapped/Nah2po4h2o.yaml, data/ingredients/mapped/Sodium_Citrate.yaml, data/ingredients/mapped/Trisodium_Citrate_X_2_H2o.yaml, data/ingredients/unmapped/Na2moo4_X_H2o.yaml, data/ingredients/unmapped/Trisodium_Citrate_X_3_H2o.yaml. Keep rejected merge history attached to explicit representatives and keep unresolved mono-/trihydrate surface forms distinct from sibling hydrates.
- defer: held-source-75b6be4855ac, held-source-71272ca0256b, held-source-d7ebfb492d5b, held-source-15ba44ba7cd2, held-source-c6f37a149c7f, held-source-ccc30f9dedb1, held-source-aa607f02029a, held-source-c5ba604021fa, held-source-f63aedfafd31, held-source-7e65c46c2293, held-source-dace2106e06b, held-source-3a3b5e39bb77, held-source-c8eb7b83415a, held-source-d93760b262a3, held-source-4b310c169232, held-source-4a8883d91734, held-source-a8866814ba73, held-source-3a5de9f5d9a3, held-source-1069c74d36aa, held-source-eafe22a42e90, held-source-562a206a3c27, held-source-d70db50995af, held-source-8ebfaa26db29, held-source-7ec2823f4bfb, held-source-783cf521df3c, held-source-764c8c8dafdd, held-source-e524fe3c1ab2, held-source-660ea2039881, held-source-458fec7ef628, held-source-69c98a290efb, held-source-38acc372c42d, held-source-6d07f7e6c3a8, held-source-715cfe1166c2. Withhold only the reviewed source-label/ID pairs pending preparation, hydration or class/member curation; assert no replacement identity.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| acceptance | reports/unified_mapping_redo_20261101/checks/source-hold-final/independent-final-acceptance.json | supports | Independent frozen-artifact acceptance: nine representatives, eleven history prefixes, nine unmapped synonyms, 34 identity-scoped additions, 33 held rows, zero required identity leaks and unchanged protected pins. |
| tests | reports/unified_mapping_redo_20261101/checks/source-hold-final/independent-final-tests.log | supports | All 67 focused tests passed; 12 dependency deprecation warnings did not affect results. |
| test_receipt | reports/unified_mapping_redo_20261101/checks/source-hold-final/independent-final-checks.json | supports | Actual independent commands, exit codes, input hashes and output hashes for the final acceptance and test run. |
| snapshot | reports/unified_mapping_redo_20261101/checks/source-hold-final/independent-final-snapshot-probe.json | supports | All 4,170 rows match the native builder, exactly 33 held labels changed, all 4,137 other rows and every count/example remain identical; all 18,873 receipt inputs verified. |
| hold_sources | reports/unified_mapping_redo_20261101/checks/source-hold-final/independent-mim-source-hold-probe.json | supports | The exact 57-row ledger prefix and all 33 appended pairs were verified; each source commit/path/hash/selector contains the stated label and ID. The old snapshot fails for every held label. |
| semantic_boundary | reports/unified_mapping_redo_20261101/checks/source-hold-final/independent-semantic-boundary-check.json | supports | Baseline and final release verdicts remain FAIL with identical blocker-ID lists. Exactly nine finding-disposition rows change only their current-record hash. |
| generation | reports/unified_mapping_redo_20261101/checks/source-hold-final/unified-generation-receipt.json | supports | Guarded native generation binds the frozen CultureMech recipes, MIM records/index/ledger and merged Claw producer to the final TSV. |
| ontology_cache | reports/unified_mapping_redo_20261101/checks/independent-chebi-cache-verification.json | supports | Inspected local ChEBI labels/formulas corroborate the eight distinct representative targets and identify the two wrong historical rationale accessions. |
| legacy_ledger | reports/unified_mapping_redo_20261101/checks/independent-ledger-and-owner-checks.json | supports | The 34 identity-scoped additions agree with the referenced YAML primary identifiers and exported exact label owners. |
| prefixed_history | reports/unified_mapping_redo_20261101/checks/independent-history-reproduction.json | supports | Pre-fix probe demonstrates that another necessary repair removed its prior repair event; retained as historical evidence for #1022. |
| prior_findings | reports/unified_mapping_redo_20261101/checks/independent-pre-fix-observations.json | supports | Pre-fix source hashes and observations support the filed defects without inventing prior structured-review lineage. |
| initial_delta | reports/unified_mapping_redo_20261101/checks/independent-unified-54-identity-owner-check.json | supports | Bounded screen of the 54 initially changed preexisting MIM identities distinguishes exact owners from fallback assignments. |
| fallback_findings | reports/unified_mapping_redo_20261101/checks/independent-unified-fallback-findings.json | supports | Pre-hold observations identify preparation, variable hydration and vitamer/class boundary escapes in the refreshed source fallback. |
| hold_cohort | reports/unified_mapping_redo_20261101/checks/independent-proposed-source-holds.json | supports | Finite 33-pair cohort with exact source contexts: 27 preparation, three hydration-state and three vitamer/class holds. |
| semantics | MAPPING_SEMANTICS.md; Section 0 and identity/SSSOM rules | supports | Identity, preparation scope, salt/hydrate/stereo distinctions, mapping predicates and publication remain governed by the repository contract. |
| profile | docs/record-review-profile.md | supports | A bounded structural/provenance review preserves native scientific release holds and does not promote record status. |
| contract | docs/UNIFIED_MAPPING_REJECTIONS.md | supports | The consumer documents exact source-label holds, intentional blank replacement cells, independent ownership and unchanged identity-wide behavior. |
| claw_review | reports/unified_mapping_redo_20261101/checks/claw697-review/final-3756b6f.json | supports | Independent producer review at exact head 3756b6f passed with 171 unified tests and an all-row corpus comparison; no in-scope findings. |
| claw_merge | reports/unified_mapping_redo_20261101/checks/claw697-validation/verified-merge-cleanup.json | supports | The merged producer 0cc221bd preserves all three reviewed source/doc/test hashes and records queue merge and branch cleanup. |
| record1 | data/ingredients/mapped/Calcium_Chloride.yaml | supports | Inspected current identity/status, representative or unresolved form, synonyms and append-only curation history. |
| record2 | data/ingredients/mapped/Cinnamic_Acid.yaml | supports | Inspected current identity/status, representative or unresolved form, synonyms and append-only curation history. |
| record3 | data/ingredients/mapped/Cocl2_X_6_H2o.yaml | supports | Inspected current identity/status, representative or unresolved form, synonyms and append-only curation history. |
| record4 | data/ingredients/mapped/Mgcl2x_6_H2o.yaml | supports | Inspected current identity/status, representative or unresolved form, synonyms and append-only curation history. |
| record5 | data/ingredients/mapped/Na-glutamate.yaml | supports | Inspected current identity/status, representative or unresolved form, synonyms and append-only curation history. |
| record6 | data/ingredients/mapped/Na2moo42h2o.yaml | supports | Inspected current identity/status, representative or unresolved form, synonyms and append-only curation history. |
| record7 | data/ingredients/mapped/Nah2po4h2o.yaml | supports | Inspected current identity/status, representative or unresolved form, synonyms and append-only curation history. |
| record8 | data/ingredients/mapped/Sodium_Citrate.yaml | supports | Inspected current identity/status, representative or unresolved form, synonyms and append-only curation history. |
| record9 | data/ingredients/mapped/Trisodium_Citrate_X_2_H2o.yaml | supports | Inspected current identity/status, representative or unresolved form, synonyms and append-only curation history. |
| record10 | data/ingredients/unmapped/Na2moo4_X_H2o.yaml | supports | Inspected current identity/status, representative or unresolved form, synonyms and append-only curation history. |
| record11 | data/ingredients/unmapped/Trisodium_Citrate_X_3_H2o.yaml | supports | Inspected current identity/status, representative or unresolved form, synonyms and append-only curation history. |
| glutamate_authority | https://www.ebi.ac.uk/chebi/CHEBI:29988; Entry identity, definition/formula or ontology relations as applicable | supports | ChEBI identifies the L-glutamate dianion, supporting the corrected rationale rather than the former unrelated accession. |
| chloride_authority | https://www.ebi.ac.uk/chebi/CHEBI:63041; Entry identity, definition/formula or ontology relations as applicable | supports | ChEBI identifies manganese(II) chloride, corroborating that this accession cannot support the older citrate rationale. |
| manganese_authority | https://www.ebi.ac.uk/chebi/CHEBI:86360; Entry identity, definition/formula or ontology relations as applicable | supports | The inspected manganese(II) sulfate entry has formula Mn.O4S; it does not establish exact identity for the explicitly hydrated source labels. |
| b12_authority | https://www.ebi.ac.uk/chebi/CHEBI:176843; Entry identity, definition/formula or ontology relations as applicable | supports | ChEBI defines a class spanning several cobalamin vitamers; an explicitly named cyanocobalamin source is more specific. |
| cobalamin_authority | https://www.ebi.ac.uk/chebi/CHEBI:30411; Entry identity, definition/formula or ontology relations as applicable | supports | The cobalamin entry is placed below cobalamins, supporting retained scope uncertainty for the qualified source label. |
| cobalamins_authority | https://www.ebi.ac.uk/chebi/CHEBI:23334; Entry identity, definition/formula or ontology relations as applicable | supports | The ontology places cobalamins beneath vitamin B12; the hierarchy supports withholding an unreviewed exact class/member identity. |
| native_qc_evidence | reports/unified_mapping_redo_20261101/checks/source-hold-final/source-holds-full-qc.log | supports | Full just qc passes, including schema/strict, evidence, SSSOM, roundtrip, visualization currency and flat export coverage. Execution was by the root agent; this reviewer inspected the final log and verified its hash. |
| receipt_replay_evidence | reports/unified_mapping_redo_20261101/checks/source-hold-final/source-holds-receipt-replay.log | supports | Replay reproduces all 2,987 rows with 1,740 SUPPORTED and 1,247 WITHHOLD dispositions. |
| reviewed_sssom_evidence | reports/unified_mapping_redo_20261101/checks/source-hold-final/source-holds-reviewed-release.log | supports | Existing reviewed SSSOM export and schema validation pass. |
| supported_kgx_evidence | reports/unified_mapping_redo_20261101/checks/source-hold-final/source-holds-supported-release.log | supports | Supported KGX validation passes while preserving excluded claims. |
| companion_evidence | reports/unified_mapping_redo_20261101/checks/source-hold-final/source-holds-companion-release.log | supports | Companion bundle validation passes against the unchanged manifest. |
| semantic_integrity_evidence | reports/unified_mapping_redo_20261101/checks/source-hold-final/source-holds-semantic-integrity.log | supports | Integrity passes; the full semantic release remains FAIL with the preexisting 1,733 finding and 2,272 assertion blockers. |
| optional_visual_regeneration_evidence | reports/unified_mapping_redo_20261101/checks/sync-and-exports.log | supports | Initial combined sync/export run completed those exports but optional visualization regeneration failed because the isolated embedding cache was absent. Final native QC independently verifies the exports and current published visualizations. |
| visualization_currency_evidence | reports/unified_mapping_redo_20261101/checks/visualization-currency.log | supports | Both published visualization products are current with 2,340 live nodes each; the final full QC also repeats the currency gate. |

## Limits And Additional Notes

- The review is structural/provenance-focused with bounded ontology identity checks; scientific_review is false. It does not approve every field of the 11 ingredient records or any of the other corpus records.
- Full semantic release remains FAIL with the same 1,733 blocking findings and 2,272 blocking assertions. Its native integrity and supported-export checks pass without clearing those holds.
- The 54 initially changed MIM identities and 290 added source labels were screened for the identified fallback mechanism. This is not a comprehensive chemical review of those populations.
- An optional visualization regeneration attempt lacked the isolated embedding cache. Required visualization-currency and final full-QC checks pass on the existing products.
- Root executed the complete native QC/release checks; the independent reviewer inspected their hash-bound logs and independently ran the focused tests, acceptance, source-selector and all-row artifact probes.
- This is a working-tree attestation on an actual detached checkout at durable baseline 2add44fb, overlaid with the exact frozen PR source/evidence bytes. The later final committed PR head requires a separate read-only verification.
- Pre-fix observations and mutations are retained as evidence. The corrected defects link to MIM #1021, #1022, #1023 and #1025 plus Claw #697/#698. They were not prior structured findings, so no previous_occurrences or synthetic terminal finding dispositions are created.
- The original feature-head inspection was not saved. A fresh actual durable-base capture avoids retaining a squash-discarded feature commit as the native source revision. No source revision was manually relabeled.
- MIM #869, #882, #894 and #808 supply the approved step-1 context. No future-step curation or paid provider research is included.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261101T035857Z-approved-plan-step1-unified-review
kind: repository
repository: CultureBotAI/MediaIngredientMech
title: 'Approved step 1: bounded unified mapping and provenance review'
started_at: '2026-11-01T03:58:14Z'
finished_at: '2026-11-01T03:58:57Z'
reviewer:
  identity: Codex independent reviewer /root/step1_independent_review
  kind: agent
  independence: independent
  independence_basis: Reviewer identified defects and recommended bounded withholding,
    but authored no implementation, repository tests, ledger, ingredient data or generated
    products. Root and a separate author implemented changes. Reviewer writes only
    new review artifacts and external probes.
skill: review-yaml-category; review-sssom-output
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: No unresolved in-scope findings remain in the frozen 66-target review. Required
  structural/provenance checks pass, including the nine representatives, two unresolved
  supplied forms, exact 33 source holds and the complete 4,170-row native artifact.
  The existing full semantic-release FAIL remains explicit.
source:
  git_revision: 2add44fbfe37544218d2f4daeb322b35debc5dd4
  state: working_tree
  inputs:
  - path: .github/workflows/qc-evidence.yaml
    sha256: 288ef1795582105763952c4104d1455c1fef273a65528949f1e558d39c7306f3
    role: target
  - path: AGENTS.md
    sha256: fc7728986d82b43359a9055ae233bcf0d4ebaef8bb657ef1b4bb4aa87b2cbaaf
    role: context
  - path: MAPPING_SEMANTICS.md
    sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
    role: context
  - path: UNIFIED_INGREDIENT_MAPPING.provenance.json
    sha256: aa8222c699ba234974469641baa275689b1b7c9c8e2cbe3c1530b0e6be93757f
    role: target
  - path: UNIFIED_INGREDIENT_MAPPING.tsv
    sha256: fd9a44beb940d8bc484a633f562de95a13e1f75a6e01c42b8965356800f1b215
    role: target
  - path: data/curated/mapped_ingredients.yaml
    sha256: a79ee59dde715022ed70bf45b7b7cc836b0cde670dcdd69f655f3d1aeda1990f
    role: target
  - path: data/curated/unmapped_ingredients.yaml
    sha256: 79ae28fa73901b24a4bc54cc058b4360735dc3b74f6698b91d017f11233e69d2
    role: target
  - path: data/ingredients/mapped/Calcium_Chloride.yaml
    sha256: 14a47e745967b921cceb9f947ef2ef668504063a2fecc440299aa69ef8b84e56
    role: target
  - path: data/ingredients/mapped/Cinnamic_Acid.yaml
    sha256: b6a625455de0f9f339d71ee5fff4a25a0d66c8e318e2863fe8af1f4ac91be89a
    role: target
  - path: data/ingredients/mapped/Cocl2_X_6_H2o.yaml
    sha256: 1155e44909ee569b943117d26a240f072f7aea1fc0f0afcb705ce5edc14bed22
    role: target
  - path: data/ingredients/mapped/Mgcl2x_6_H2o.yaml
    sha256: 520ebd239f456859bdff9e576a27faf95eb564fe6a6a10bbf16013bee01c6d83
    role: target
  - path: data/ingredients/mapped/Na-glutamate.yaml
    sha256: 1b54cebe01112e2c8973e78127a1b2eb83a801535ab1967015545bfa137b5f0e
    role: target
  - path: data/ingredients/mapped/Na2moo42h2o.yaml
    sha256: 5a6b277f3274ca6a6ea7feaf988927939c51513fe63fd95e40b6f435ff0a8f17
    role: target
  - path: data/ingredients/mapped/Nah2po4h2o.yaml
    sha256: ff636e9f09fa3f0767d05ad811a4ee706be655fb9007194505d4419741b2595c
    role: target
  - path: data/ingredients/mapped/Sodium_Citrate.yaml
    sha256: 8d5931b67aa99c5877679aa2e956234eef16e5c3ba3ea767e03f47c302d5b27e
    role: target
  - path: data/ingredients/mapped/Trisodium_Citrate_X_2_H2o.yaml
    sha256: 69e37553e442f91d155193d4c69077afe54da649e74e11666821b2e30255112a
    role: target
  - path: data/ingredients/unmapped/Na2moo4_X_H2o.yaml
    sha256: 0bcee9de76e0455f426fb0e12469a48e1091ad91a2251d5530923869b18e3de8
    role: target
  - path: data/ingredients/unmapped/Trisodium_Citrate_X_3_H2o.yaml
    sha256: 1bd94f0ca085cb4be39f87fadea062b3efdcae0f908fe0dff47a8ba95b40b456
    role: target
  - path: docs/INGREDIENT_SCOPE_PROFILE.md
    sha256: 82729da420d79ceb2a1313580089866a6ed6ff06dd70f317ac61fce17433c642
    role: context
  - path: docs/UNIFIED_MAPPING_REJECTIONS.md
    sha256: b0989f6b82dd40e6a3593c297935aaf21c8f9fc6591b456e484e38e78d3a3317
    role: target
  - path: docs/data/label_index.csv
    sha256: 4fe7d5c8926022d8b4887aae6c73f274fcd33a414aa371bd48b77fb203acbcf1
    role: target
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
    sha256: a2b83ccdcaad67d89943ccf0f0e30d796cdbc5e418ead247313631b713e89722
    role: target
  - path: mappings/unified_mapping_rejections.tsv
    sha256: 82d7d79172a5efd966f0a6a97ead4faae186128f6d6fdb327366f041ad06aba4
    role: target
  - path: reports/semantic_review_20260921/resolution/current-review.json
    sha256: 98b04f6ff7b87ab6eeaed6ef6512b8f5458d7fa3805087866c316dc94e8e6b94
    role: target
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: 2ed6d42dbf78d4a4a973d231647342c2797aec8b0d36aa7e84772dd945fc92b5
    role: target
  - path: reports/unified_mapping_redo_20261101/README.md
    sha256: 3050ca525f1c05e626fe7eed72ebc3c62379e1d3d1a4ca1ad743d82d59276700
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/claw697-review/corpus-probe.json
    sha256: 7a182f0b18974762e6c2ff2ea3066a5f784c980f613ccc8b438ad62d654636a4
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/claw697-review/final-3756b6f.json
    sha256: 79f93152fd2e7d0b4ce1748aef0a35ea71e9effaeca9316d48238197cb80f91e
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/claw697-review/final-3756b6f.md
    sha256: 4292394936e444f5740fc0971618cc85be6003695f477ba8c6ab1eda5dbde4de
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/claw697-review/tests-3756b6f.log
    sha256: eb3f4bd7d628772e9c9d2ab5142f3dfe2758f6627d9ac5342a14b65bfbf42a46
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/claw697-validation/verified-merge-cleanup.json
    sha256: c182d354bd3d4fc66d3e5c28ddd6bf5e046f629dd669b56841c816becb248450
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/independent-chebi-cache-verification.json
    sha256: 2ddecbc31901fb660eef70a6380317a277e3a3895f76f5094150f01471eb6e95
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/independent-history-reproduction.json
    sha256: 675b6cc994269e46387d7c76dc957c57c2fd52c8a1485c260fe34215c9a0c6a8
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/independent-ledger-and-owner-checks.json
    sha256: f3f2cd23c40a4b68857b3f7f8516c675e0d58102d0d25f2b73a8531f015657d1
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/independent-pre-fix-observations.json
    sha256: 201b785ead5b266e4f585ce54d379ccd32d93f8b676ee8b77a4eb8a63c0f608f
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/independent-proposed-source-holds.json
    sha256: 105dfc13469d3f404bd68111c11e032a61eef1f748e7187ee6bded10ea34e76c
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/independent-unified-54-identity-owner-check.json
    sha256: 8ba171f377fe8dab081e020ea6397659a30a16588391a4d632380e38048d833b
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/independent-unified-fallback-findings.json
    sha256: 4c021d55c2b3d308e4f6790cf3690e1309e17a749559062f8e5b6bad3402dd1a
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/source-hold-final/independent-final-acceptance.json
    sha256: d7193668156e09fcdffc3407508e72c4dc5efbfc47a84649a26a1d0538a874d2
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/source-hold-final/independent-final-checks.json
    sha256: e35b390631d3a1bede69dd3073fa3650607a9f6aac273c7cfe072aa3efbfbd1c
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/source-hold-final/independent-final-snapshot-probe.json
    sha256: a7a124f19d439d861a42bfeaf8c48978921cb790d323e67344e3e4083dd79c26
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/source-hold-final/independent-final-snapshot-probe.log
    sha256: d71f644780ad722fb97cff9f5b3a84547c2328eaca9279865fa40b1037d327c9
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/source-hold-final/independent-final-tests.log
    sha256: f2533ee162109748fd8a3952cb4d608e21e8f6c7b902caa398257250d717abf7
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/source-hold-final/independent-mim-source-hold-probe.json
    sha256: 2b37e1fc8cd3a519838898435dea0ae279ff28830664f3f725c40c7f449eff88
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/source-hold-final/independent-semantic-boundary-check.json
    sha256: 67689a96f1801b9b736693805d783af92399adbfb599a50893306423cd27e3c9
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/source-hold-final/source-holds-companion-release.json
    sha256: 993ee6b5fa5cf8a3a6f443abe89378aaa3f18f8c070e5266257445dc3a05e9da
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/source-hold-final/source-holds-companion-release.log
    sha256: 8ebcd9844e21f9e0ad5cc0502f944f93a87cf7b2dba9d1a7badee02c12269ff5
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/source-hold-final/source-holds-full-qc.json
    sha256: 44ed009be1823b3dc32c4cb68694117da86066823c2db0fd812ccb76ee71f301
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/source-hold-final/source-holds-full-qc.log
    sha256: d20034a4067581ba50b8ca21f88c90b5bd25f25fed71a99702a6e83caec5dd53
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/source-hold-final/source-holds-receipt-replay.json
    sha256: cf54ae1442ccb63d2a0bbcee2384d80bdfe8247d49475cbf52ea7f8704c5ed2a
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/source-hold-final/source-holds-receipt-replay.log
    sha256: 710484b8faef7b4592edeb4f762119c2b8f7863c30a31709de9f808a75ae599e
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/source-hold-final/source-holds-reviewed-release.json
    sha256: 94b4788c48f98391d9256aee2304d2da3ff095960ffd4caea8a5c0e90a83fb34
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/source-hold-final/source-holds-reviewed-release.log
    sha256: eaa0723a3cb9c90f815752f64ce76258ecb24c2bc3f5dfdecd682f60234756d6
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/source-hold-final/source-holds-semantic-integrity.json
    sha256: 88cab278cf48584722d0f2e4e766c1ae7380b4a0862f64667ce72309ce2ee6dd
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/source-hold-final/source-holds-semantic-integrity.log
    sha256: 90eb85ea6aac322e5f500e252bac25fb0cde9acbc1817fba8d2bd9d0ebfcee81
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/source-hold-final/source-holds-supported-release.json
    sha256: 3f9f2f52125ea83944b70a1976a430ac8ce48679ff25cea8dfceee32409f2820
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/source-hold-final/source-holds-supported-release.log
    sha256: 17c33094ba60156dd91757753e07e75793bb8b290d7fffd280c62748532e4bdc
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/source-hold-final/unified-generation-receipt.json
    sha256: f65d90b10e8bd74feb34603d773c2281a06a7e58a2d396fe8dac569abd5ccc10
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/step1-history-mutation-tests.json
    sha256: 508e21b6df9f53ade156fad219b1bc21b5682ac531f2833f45ac660063b5be39
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/step1-history-mutation-tests.log
    sha256: 679626baba0e5b80ab056ecec2d67937152e5b545c0d6ab7ef414537777d5b60
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/step1-identifier-mutation-tests.json
    sha256: 9d01ab913e4bca4c8624a7d6a446a2e6298957f73cc4d730a9dc1da759a2c3b0
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/step1-identifier-mutation-tests.log
    sha256: 8c38f22a166c22910145760e55491d26563b561bf44fad08ffd5a4eb9862fd1f
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/step1-provenance-mutation-tests.json
    sha256: 192175a98446a33e2df60af1a1c944d819ac4b29940bc058cc8ed0cda6fe6b91
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/step1-provenance-mutation-tests.log
    sha256: a9f50c2dc58fb2d4e401f02a945b3c1e4414492956d12bc911ecb80c3e623f25
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/sync-and-exports.json
    sha256: c3eb77c1d6cf09aceec2520d667f1bd473950f812fb50339efec7cf40e5c8374
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/sync-and-exports.log
    sha256: 8868fbd73acf0779d479bcf9e4c90b276411a78d27a2073e8613c856b5f9990d
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/visualization-currency.json
    sha256: e2addf6110f1326bef555b752329105513ba499a95f9f32856e39229fd3b7210
    role: context
  - path: reports/unified_mapping_redo_20261101/checks/visualization-currency.log
    sha256: 69a1810deba009f5758a3d67b474b763ad8e1ac4c81d54d15184f6f206ad4f04
    role: context
  - path: reports/unified_mapping_redo_20261101/evidence-index.json
    sha256: 7492617578679a59b7d52a97dd7bb78fcb2d19f80fe34466fcf997491bc7a267
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/.vendored_canon_ref
    sha256: ecbdb08d2094917a5ed8147086f46579e976df869eaea3942060c552d2e2015c
    role: target
  - path: scripts/apply_312_batch1.py
    sha256: cdc359a6ebd9652853c2bee9cb8b5a7f5c830fd18a2badd2f7f50051319a8e04
    role: target
  - path: scripts/apply_312_batch4.py
    sha256: 0d3540554f65bb4e106ce6bd55fb6f91da51d3f27d0da7a81de0b60b0e78e2fd
    role: target
  - path: scripts/check_unified_rejections.py
    sha256: 4f7faf1f103f50be1a59e826b0238061d1a9214afcec9d1cf0b029237e71238c
    role: target
  - path: scripts/fix_merge_tombstone_resolution.py
    sha256: d2ef8947f61934407f193aa569d9b2533641e5eaae4364b47242e86f5fc25873
    role: target
  - path: scripts/merge_mapped_records.py
    sha256: 00c8d18d1a6c05655580aba366b96893991b34eca40563a52e884abe69c3e070
    role: target
  - path: scripts/retire_wrong_form_names.py
    sha256: 8e04b6cf6e7dae48548bc6690c72ec1d9f43639a55a8b651ea7d5156401accb8
    role: target
  - path: src/mediaingredientmech/schema/mediaingredientmech.yaml
    sha256: bb43dee29b21fdee72a48022456e733e49e95824c4c09674f9b3165c290fe012
    role: context
  - path: tests/test_fix_merge_tombstone_resolution.py
    sha256: d44736cc03159677c69bfbe2e6043924cb61a2295e7499658976b1cd971d3205
    role: target
  - path: tests/test_merge_mapped_records.py
    sha256: c9637e1467cb67903f79ed4fe0e2e3d2e87aec75141c51e0101653e43b808888
    role: target
  - path: tests/test_unified_rejections.py
    sha256: bbe49bccf9e17587cb110adc4ec98a1f2f14223caddd2c53eb18bb879c9760ad
    role: target
  - path: tests/test_unified_source_holds.py
    sha256: bbdb713efce35ac87ec68e1dd5f6ffc9397fb3cdc20870992796368f630a0ec7
    role: target
scope:
  description: '66 declared targets: 33 artifacts and 33 exact unified snapshot rows.
    Structural checks cover every unified row. Ontology identity interpretation is
    limited to the nine representatives, two unresolved forms and finite 33 negative
    source-label decisions.'
  selection: Approved-plan step-1 changed source/records/ledger and core generated
    outputs, protected excluded pin files, and every row of the finite source-hold
    cohort. No random sampling.
  coverage: full
  population_size: 66
  reviewed_target_ids:
  - data/ingredients/mapped/Calcium_Chloride.yaml
  - data/ingredients/mapped/Cinnamic_Acid.yaml
  - data/ingredients/mapped/Cocl2_X_6_H2o.yaml
  - data/ingredients/mapped/Mgcl2x_6_H2o.yaml
  - data/ingredients/mapped/Na-glutamate.yaml
  - data/ingredients/mapped/Na2moo42h2o.yaml
  - data/ingredients/mapped/Nah2po4h2o.yaml
  - data/ingredients/mapped/Sodium_Citrate.yaml
  - data/ingredients/mapped/Trisodium_Citrate_X_2_H2o.yaml
  - data/ingredients/unmapped/Na2moo4_X_H2o.yaml
  - data/ingredients/unmapped/Trisodium_Citrate_X_3_H2o.yaml
  - scripts/apply_312_batch1.py
  - scripts/apply_312_batch4.py
  - scripts/check_unified_rejections.py
  - scripts/fix_merge_tombstone_resolution.py
  - scripts/merge_mapped_records.py
  - scripts/retire_wrong_form_names.py
  - tests/test_fix_merge_tombstone_resolution.py
  - tests/test_merge_mapped_records.py
  - tests/test_unified_rejections.py
  - mappings/unified_mapping_rejections.tsv
  - data/curated/mapped_ingredients.yaml
  - data/curated/unmapped_ingredients.yaml
  - reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  - .github/workflows/qc-evidence.yaml
  - scripts/.vendored_canon_ref
  - UNIFIED_INGREDIENT_MAPPING.tsv
  - UNIFIED_INGREDIENT_MAPPING.provenance.json
  - docs/data/label_index.csv
  - reports/semantic_review_20260921/resolution/current-review.json
  - mappings/ingredient_mappings.sssom.tsv
  - docs/UNIFIED_MAPPING_REJECTIONS.md
  - tests/test_unified_source_holds.py
  - held-source-75b6be4855ac
  - held-source-71272ca0256b
  - held-source-d7ebfb492d5b
  - held-source-15ba44ba7cd2
  - held-source-c6f37a149c7f
  - held-source-ccc30f9dedb1
  - held-source-aa607f02029a
  - held-source-c5ba604021fa
  - held-source-f63aedfafd31
  - held-source-7e65c46c2293
  - held-source-dace2106e06b
  - held-source-3a3b5e39bb77
  - held-source-c8eb7b83415a
  - held-source-d93760b262a3
  - held-source-4b310c169232
  - held-source-4a8883d91734
  - held-source-a8866814ba73
  - held-source-3a5de9f5d9a3
  - held-source-1069c74d36aa
  - held-source-eafe22a42e90
  - held-source-562a206a3c27
  - held-source-d70db50995af
  - held-source-8ebfaa26db29
  - held-source-7ec2823f4bfb
  - held-source-783cf521df3c
  - held-source-764c8c8dafdd
  - held-source-e524fe3c1ab2
  - held-source-660ea2039881
  - held-source-458fec7ef628
  - held-source-69c98a290efb
  - held-source-38acc372c42d
  - held-source-6d07f7e6c3a8
  - held-source-715cfe1166c2
  exclusions:
  - target: All other ingredient identities, chemistry, roles, citations and SSSOM
      alias claims
    reason: Structural validation and source-fallback screening do not establish corpus-wide
      scientific approval.
  - target: Existing full semantic-release backlog
    reason: The 1,733 finding and 2,272 assertion blockers retain their native dispositions
      and remain outside this repair scope.
  - target: Later approved-plan steps and SSSOM owned-name exclusivity policy
    reason: This review only covers step 1 and its source-hold prerequisite.
targets:
- target_id: data/ingredients/mapped/Calcium_Chloride.yaml
  path: data/ingredients/mapped/Calcium_Chloride.yaml
  label: Calcium_Chloride.yaml
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Calcium_Chloride.yaml
    role: maintained input
- target_id: data/ingredients/mapped/Cinnamic_Acid.yaml
  path: data/ingredients/mapped/Cinnamic_Acid.yaml
  label: Cinnamic_Acid.yaml
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cinnamic_Acid.yaml
    role: maintained input
- target_id: data/ingredients/mapped/Cocl2_X_6_H2o.yaml
  path: data/ingredients/mapped/Cocl2_X_6_H2o.yaml
  label: Cocl2_X_6_H2o.yaml
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cocl2_X_6_H2o.yaml
    role: maintained input
- target_id: data/ingredients/mapped/Mgcl2x_6_H2o.yaml
  path: data/ingredients/mapped/Mgcl2x_6_H2o.yaml
  label: Mgcl2x_6_H2o.yaml
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Mgcl2x_6_H2o.yaml
    role: maintained input
- target_id: data/ingredients/mapped/Na-glutamate.yaml
  path: data/ingredients/mapped/Na-glutamate.yaml
  label: Na-glutamate.yaml
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na-glutamate.yaml
    role: maintained input
- target_id: data/ingredients/mapped/Na2moo42h2o.yaml
  path: data/ingredients/mapped/Na2moo42h2o.yaml
  label: Na2moo42h2o.yaml
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2moo42h2o.yaml
    role: maintained input
- target_id: data/ingredients/mapped/Nah2po4h2o.yaml
  path: data/ingredients/mapped/Nah2po4h2o.yaml
  label: Nah2po4h2o.yaml
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nah2po4h2o.yaml
    role: maintained input
- target_id: data/ingredients/mapped/Sodium_Citrate.yaml
  path: data/ingredients/mapped/Sodium_Citrate.yaml
  label: Sodium_Citrate.yaml
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_Citrate.yaml
    role: maintained input
- target_id: data/ingredients/mapped/Trisodium_Citrate_X_2_H2o.yaml
  path: data/ingredients/mapped/Trisodium_Citrate_X_2_H2o.yaml
  label: Trisodium_Citrate_X_2_H2o.yaml
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trisodium_Citrate_X_2_H2o.yaml
    role: maintained input
- target_id: data/ingredients/unmapped/Na2moo4_X_H2o.yaml
  path: data/ingredients/unmapped/Na2moo4_X_H2o.yaml
  label: Na2moo4_X_H2o.yaml
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/unmapped/Na2moo4_X_H2o.yaml
    role: maintained input
- target_id: data/ingredients/unmapped/Trisodium_Citrate_X_3_H2o.yaml
  path: data/ingredients/unmapped/Trisodium_Citrate_X_3_H2o.yaml
  label: Trisodium_Citrate_X_3_H2o.yaml
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/unmapped/Trisodium_Citrate_X_3_H2o.yaml
    role: maintained input
- target_id: scripts/apply_312_batch1.py
  path: scripts/apply_312_batch1.py
  label: apply_312_batch1.py
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: scripts/apply_312_batch1.py
    role: maintained input
- target_id: scripts/apply_312_batch4.py
  path: scripts/apply_312_batch4.py
  label: apply_312_batch4.py
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: scripts/apply_312_batch4.py
    role: maintained input
- target_id: scripts/check_unified_rejections.py
  path: scripts/check_unified_rejections.py
  label: check_unified_rejections.py
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: scripts/check_unified_rejections.py
    role: maintained input
- target_id: scripts/fix_merge_tombstone_resolution.py
  path: scripts/fix_merge_tombstone_resolution.py
  label: fix_merge_tombstone_resolution.py
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: scripts/fix_merge_tombstone_resolution.py
    role: maintained input
- target_id: scripts/merge_mapped_records.py
  path: scripts/merge_mapped_records.py
  label: merge_mapped_records.py
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: scripts/merge_mapped_records.py
    role: maintained input
- target_id: scripts/retire_wrong_form_names.py
  path: scripts/retire_wrong_form_names.py
  label: retire_wrong_form_names.py
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: scripts/retire_wrong_form_names.py
    role: maintained input
- target_id: tests/test_fix_merge_tombstone_resolution.py
  path: tests/test_fix_merge_tombstone_resolution.py
  label: test_fix_merge_tombstone_resolution.py
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: tests/test_fix_merge_tombstone_resolution.py
    role: maintained input
- target_id: tests/test_merge_mapped_records.py
  path: tests/test_merge_mapped_records.py
  label: test_merge_mapped_records.py
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: tests/test_merge_mapped_records.py
    role: maintained input
- target_id: tests/test_unified_rejections.py
  path: tests/test_unified_rejections.py
  label: test_unified_rejections.py
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: tests/test_unified_rejections.py
    role: maintained input
- target_id: mappings/unified_mapping_rejections.tsv
  path: mappings/unified_mapping_rejections.tsv
  label: unified_mapping_rejections.tsv
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: maintained input
- target_id: data/curated/mapped_ingredients.yaml
  path: data/curated/mapped_ingredients.yaml
  label: mapped_ingredients.yaml
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: maintained input
- target_id: data/curated/unmapped_ingredients.yaml
  path: data/curated/unmapped_ingredients.yaml
  label: unmapped_ingredients.yaml
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/unmapped_ingredients.yaml
    role: maintained input
- target_id: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  label: finding-dispositions.tsv
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    role: maintained input
- target_id: .github/workflows/qc-evidence.yaml
  path: .github/workflows/qc-evidence.yaml
  label: qc-evidence.yaml
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: .github/workflows/qc-evidence.yaml
    role: maintained input
- target_id: scripts/.vendored_canon_ref
  path: scripts/.vendored_canon_ref
  label: .vendored_canon_ref
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: scripts/.vendored_canon_ref
    role: maintained input
- target_id: UNIFIED_INGREDIENT_MAPPING.tsv
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  label: UNIFIED_INGREDIENT_MAPPING.tsv
  kind: generated
  owner_paths:
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients
    role: maintained ingredient inputs
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: negative mapping rules
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml
    role: source ingredient occurrences
- target_id: UNIFIED_INGREDIENT_MAPPING.provenance.json
  path: UNIFIED_INGREDIENT_MAPPING.provenance.json
  label: UNIFIED_INGREDIENT_MAPPING.provenance.json
  kind: generated
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: scripts/check_unified_freshness.py
    role: producer
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients
    role: maintained ingredient inputs
- target_id: docs/data/label_index.csv
  path: docs/data/label_index.csv
  label: label_index.csv
  kind: generated
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: scripts/export_lists.py
    role: producer
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients
    role: maintained ingredient inputs
- target_id: reports/semantic_review_20260921/resolution/current-review.json
  path: reports/semantic_review_20260921/resolution/current-review.json
  label: current-review.json
  kind: generated
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: reports/semantic_review_20260921/resolution/build_review.py
    role: producer
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients
    role: maintained ingredient inputs
- target_id: mappings/ingredient_mappings.sssom.tsv
  path: mappings/ingredient_mappings.sssom.tsv
  label: ingredient_mappings.sssom.tsv
  kind: generated
  owner_paths:
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_mim_ingredient_sssom.py
    role: producer
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients
    role: maintained ingredient inputs
- target_id: docs/UNIFIED_MAPPING_REJECTIONS.md
  path: docs/UNIFIED_MAPPING_REJECTIONS.md
  label: UNIFIED_MAPPING_REJECTIONS.md
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: docs/UNIFIED_MAPPING_REJECTIONS.md
    role: maintained consumer contract
- target_id: tests/test_unified_source_holds.py
  path: tests/test_unified_source_holds.py
  label: test_unified_source_holds.py
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: tests/test_unified_source_holds.py
    role: consumer regression tests
- target_id: held-source-75b6be4855ac
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "1 M K2HPO4"
  label: 1 M K2HPO4 (withhold CHEBI:131527)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M1265_Modified_Cellulolytic_Haloarchaea_Medium.yaml
    role: upstream source occurrence context
- target_id: held-source-71272ca0256b
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "1 M KH2PO4"
  label: 1 M KH2PO4 (withhold CHEBI:63036)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M1265_Modified_Cellulolytic_Haloarchaea_Medium.yaml
    role: upstream source occurrence context
- target_id: held-source-d7ebfb492d5b
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "1 M Sodium acetate solution"
  label: 1 M Sodium acetate solution (withhold CHEBI:32954)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M873_Syfac_Medium.yaml
    role: upstream source occurrence context
- target_id: held-source-15ba44ba7cd2
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "1 M Tris base (pH 8)"
  label: 1 M Tris base (pH 8) (withhold CHEBI:9754)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M970_Peat_Medium_2_For_Methanobacteria.yaml
    role: upstream source occurrence context
- target_id: held-source-c6f37a149c7f
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "1 N NaOH"
  label: 1 N NaOH (withhold CHEBI:32145)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brucella_blood_agar_with_hemin_menadione.yaml
    role: upstream source occurrence context
- target_id: held-source-ccc30f9dedb1
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "10% Glucose solution"
  label: 10% Glucose solution (withhold CHEBI:17234)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_4784_Main_sol_J825.yaml
    role: upstream source occurrence context
- target_id: held-source-aa607f02029a
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "25% HCl (7.7 M)"
  label: 25% HCl (7.7 M) (withhold CHEBI:17883)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J1427_MODIFIED_METHANOBACTERIUM_MEDIUM.yaml
    role: upstream source occurrence context
- target_id: held-source-c5ba604021fa
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "5% L-Cysteine·HCl·H2O solution"
  label: 5% L-Cysteine·HCl·H2O solution (withhold CHEBI:91248)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J1422_METHANOCORPUSCULUM_AGGREGANS_MEDIUM.yaml
    role: upstream source occurrence context
- target_id: held-source-f63aedfafd31
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "5% Na2S·9H2O solution"
  label: 5% Na2S·9H2O solution (withhold CHEBI:76209)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J1422_METHANOCORPUSCULUM_AGGREGANS_MEDIUM.yaml
    role: upstream source occurrence context
- target_id: held-source-7e65c46c2293
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "8% NaHCO3 solution"
  label: 8% NaHCO3 solution (withhold CHEBI:32139)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J1422_METHANOCORPUSCULUM_AGGREGANS_MEDIUM.yaml
    role: upstream source occurrence context
- target_id: held-source-dace2106e06b
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "Cyanocobalamin (Vitamin B12)"
  label: Cyanocobalamin (Vitamin B12) (withhold CHEBI:176843)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/yt75s_v.yaml
    role: upstream source occurrence context
- target_id: held-source-3a3b5e39bb77
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "MnSO4·xH2O"
  label: MnSO4·xH2O (withhold CHEBI:86360)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1503_AUTOTROPHIC_NITROBACTER_MEDIUM.yaml
    role: upstream source occurrence context
- target_id: held-source-c8eb7b83415a
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "1 M CaCl2 solution"
  label: 1 M CaCl2 solution (withhold CHEBI:3312)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M1265_Modified_Cellulolytic_Haloarchaea_Medium.yaml
    role: upstream source occurrence context
- target_id: held-source-d93760b262a3
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "1 M K2HPO4 solution"
  label: 1 M K2HPO4 solution (withhold CHEBI:131527)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1220_Natronospira_Proteinivora_Medium.yaml
    role: upstream source occurrence context
- target_id: held-source-4b310c169232
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "1 M MgCl2 solution"
  label: 1 M MgCl2 solution (withhold CHEBI:6636)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M1150_Natranaeroarchaeum_Medium.yaml
    role: upstream source occurrence context
- target_id: held-source-4a8883d91734
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "1 M Sodium fumarate solution"
  label: 1 M Sodium fumarate solution (withhold CHEBI:115156)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M873_Syfac_Medium.yaml
    role: upstream source occurrence context
- target_id: held-source-a8866814ba73
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "1 N KOH"
  label: 1 N KOH (withhold CHEBI:32035)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/wees.yaml
    role: upstream source occurrence context
- target_id: held-source-3a5de9f5d9a3
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "2 M NH4Cl solution"
  label: 2 M NH4Cl solution (withhold CHEBI:31206)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1220_Natronospira_Proteinivora_Medium.yaml
    role: upstream source occurrence context
- target_id: held-source-1069c74d36aa
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "3% L-Cysteine HCl x H2O solution"
  label: 3% L-Cysteine HCl x H2O solution (withhold CHEBI:91248)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_4784_Main_sol_J825.yaml
    role: upstream source occurrence context
- target_id: held-source-eafe22a42e90
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "3% Na2S x 9 H2O solution"
  label: 3% Na2S x 9 H2O solution (withhold CHEBI:76209)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_4784_Main_sol_J825.yaml
    role: upstream source occurrence context
- target_id: held-source-562a206a3c27
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "4 M NH4Cl solution"
  label: 4 M NH4Cl solution (withhold CHEBI:31206)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M1150_Natranaeroarchaeum_Medium.yaml
    role: upstream source occurrence context
- target_id: held-source-d70db50995af
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "5% Na2S x 9 H2O solution"
  label: 5% Na2S x 9 H2O solution (withhold CHEBI:76209)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M873_Syfac_Medium.yaml
    role: upstream source occurrence context
- target_id: held-source-8ebfaa26db29
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "Ethanol (95 %)"
  label: Ethanol (95 %) (withhold CHEBI:16236)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/treponema_rectale_medium.yaml
    role: upstream source occurrence context
- target_id: held-source-7ec2823f4bfb
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "FeSO4 x 7 H2O (0.1% w/v in 0.1 N H2SO4)"
  label: FeSO4 x 7 H2O (0.1% w/v in 0.1 N H2SO4) (withhold CHEBI:75836)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/methanofollis_medium.yaml
    role: upstream source occurrence context
- target_id: held-source-783cf521df3c
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "HEPES buffer pH 7.8"
  label: HEPES buffer pH 7.8 (withhold CHEBI:42334)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/P49_Medium.yaml
    role: upstream source occurrence context
- target_id: held-source-764c8c8dafdd
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "KOH solution"
  label: KOH solution (withhold CHEBI:32035)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/methanobacterium_medium_ii_with_formae.yaml
    role: upstream source occurrence context
- target_id: held-source-e524fe3c1ab2
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "NaOH (1 N)"
  label: NaOH (1 N) (withhold CHEBI:32145)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/taiyang_medium_no_9_prototype.yaml
    role: upstream source occurrence context
- target_id: held-source-660ea2039881
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "Sulfuric acid (concentrated)"
  label: Sulfuric acid (concentrated) (withhold CHEBI:26836)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/Bold_Trace_Stock.yaml
    role: upstream source occurrence context
- target_id: held-source-458fec7ef628
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "Tricine (pH 8)"
  label: Tricine (pH 8) (withhold CHEBI:46760)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DAS_Vitamin_Cocktail.yaml
    role: upstream source occurrence context
- target_id: held-source-69c98a290efb
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "MnSO4 x xH2O"
  label: MnSO4 x xH2O (withhold CHEBI:86360)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/freshwater_thiosulfate_oxidizing_bacteria_medium.yaml
    role: upstream source occurrence context
- target_id: held-source-38acc372c42d
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "MnSO4.xH2O"
  label: MnSO4.xH2O (withhold CHEBI:86360)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M332_PE_Medium_pH_7.2.yaml
    role: upstream source occurrence context
- target_id: held-source-6d07f7e6c3a8
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "Cyanocobalamin (B12)"
  label: Cyanocobalamin (B12) (withhold CHEBI:176843)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/rs_medium_nutrient_medium_nm_component.yaml
    role: upstream source occurrence context
- target_id: held-source-715cfe1166c2
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  selector: ingredient_name = "Vitamin B12 (Cobalamin)"
  label: Vitamin B12 (Cobalamin) (withhold CHEBI:176843)
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: reviewed negative source-identity decision
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: producer
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DAS_Vitamin_Cocktail.yaml
    role: upstream source occurrence context
checks:
- check_id: independent_tests
  name: Focused regressions
  status: passed
  required: true
  summary: 67 tests passed, covering repaired history, identifiers, representative
    routing, both ledger scopes and the final held cohort.
  target_ids:
  - data/ingredients/mapped/Calcium_Chloride.yaml
  - data/ingredients/mapped/Cinnamic_Acid.yaml
  - data/ingredients/mapped/Cocl2_X_6_H2o.yaml
  - data/ingredients/mapped/Mgcl2x_6_H2o.yaml
  - data/ingredients/mapped/Na-glutamate.yaml
  - data/ingredients/mapped/Na2moo42h2o.yaml
  - data/ingredients/mapped/Nah2po4h2o.yaml
  - data/ingredients/mapped/Sodium_Citrate.yaml
  - data/ingredients/mapped/Trisodium_Citrate_X_2_H2o.yaml
  - data/ingredients/unmapped/Na2moo4_X_H2o.yaml
  - data/ingredients/unmapped/Trisodium_Citrate_X_3_H2o.yaml
  - scripts/apply_312_batch1.py
  - scripts/apply_312_batch4.py
  - scripts/check_unified_rejections.py
  - scripts/fix_merge_tombstone_resolution.py
  - scripts/merge_mapped_records.py
  - scripts/retire_wrong_form_names.py
  - tests/test_fix_merge_tombstone_resolution.py
  - tests/test_merge_mapped_records.py
  - tests/test_unified_rejections.py
  - tests/test_unified_source_holds.py
  - held-source-75b6be4855ac
  - held-source-71272ca0256b
  - held-source-d7ebfb492d5b
  - held-source-15ba44ba7cd2
  - held-source-c6f37a149c7f
  - held-source-ccc30f9dedb1
  - held-source-aa607f02029a
  - held-source-c5ba604021fa
  - held-source-f63aedfafd31
  - held-source-7e65c46c2293
  - held-source-dace2106e06b
  - held-source-3a3b5e39bb77
  - held-source-c8eb7b83415a
  - held-source-d93760b262a3
  - held-source-4b310c169232
  - held-source-4a8883d91734
  - held-source-a8866814ba73
  - held-source-3a5de9f5d9a3
  - held-source-1069c74d36aa
  - held-source-eafe22a42e90
  - held-source-562a206a3c27
  - held-source-d70db50995af
  - held-source-8ebfaa26db29
  - held-source-7ec2823f4bfb
  - held-source-783cf521df3c
  - held-source-764c8c8dafdd
  - held-source-e524fe3c1ab2
  - held-source-660ea2039881
  - held-source-458fec7ef628
  - held-source-69c98a290efb
  - held-source-38acc372c42d
  - held-source-6d07f7e6c3a8
  - held-source-715cfe1166c2
  - mappings/unified_mapping_rejections.tsv
  - UNIFIED_INGREDIENT_MAPPING.tsv
  evidence_ids:
  - tests
  - test_receipt
  command: /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/approved-plan-20261101T031134Z/envs/mim/bin/python
    -m pytest -q -o addopts= -p no:cacheprovider tests/test_fix_merge_tombstone_resolution.py
    tests/test_merge_mapped_records.py tests/test_unified_rejections.py tests/test_unified_source_holds.py
  exit_code: 0
  scope_note: Focused tests exercise changed writer and rejection behavior plus persisted
    record/snapshot regressions. Other artifact checks and positive assessments are
    recorded separately.
- check_id: independent_acceptance
  name: Approved step-1 acceptance
  status: passed
  required: true
  summary: All required identity invariants and preserved histories/pins pass.
  target_ids:
  - data/ingredients/mapped/Calcium_Chloride.yaml
  - data/ingredients/mapped/Cinnamic_Acid.yaml
  - data/ingredients/mapped/Cocl2_X_6_H2o.yaml
  - data/ingredients/mapped/Mgcl2x_6_H2o.yaml
  - data/ingredients/mapped/Na-glutamate.yaml
  - data/ingredients/mapped/Na2moo42h2o.yaml
  - data/ingredients/mapped/Nah2po4h2o.yaml
  - data/ingredients/mapped/Sodium_Citrate.yaml
  - data/ingredients/mapped/Trisodium_Citrate_X_2_H2o.yaml
  - data/ingredients/unmapped/Na2moo4_X_H2o.yaml
  - data/ingredients/unmapped/Trisodium_Citrate_X_3_H2o.yaml
  - mappings/unified_mapping_rejections.tsv
  - UNIFIED_INGREDIENT_MAPPING.tsv
  - .github/workflows/qc-evidence.yaml
  - scripts/.vendored_canon_ref
  evidence_ids:
  - acceptance
  - test_receipt
  command: /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/approved-plan-20261101T031134Z/envs/mim/bin/python
    /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/approved-plan-20261101T031134Z/step1-independent/verify_step1.py
    /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/approved-plan-20261101T031134Z/step1-mim
  exit_code: 0
- check_id: independent_snapshot
  name: All-row native-output comparison and receipt verification
  status: passed
  required: true
  summary: 4,170 rows match; 33 held labels change; 4,137 other rows and all source
    count/example fields stay identical. All 18,873 generation inputs match recorded
    hashes.
  target_ids:
  - UNIFIED_INGREDIENT_MAPPING.tsv
  - UNIFIED_INGREDIENT_MAPPING.provenance.json
  - mappings/ingredient_mappings.sssom.tsv
  - held-source-75b6be4855ac
  - held-source-71272ca0256b
  - held-source-d7ebfb492d5b
  - held-source-15ba44ba7cd2
  - held-source-c6f37a149c7f
  - held-source-ccc30f9dedb1
  - held-source-aa607f02029a
  - held-source-c5ba604021fa
  - held-source-f63aedfafd31
  - held-source-7e65c46c2293
  - held-source-dace2106e06b
  - held-source-3a3b5e39bb77
  - held-source-c8eb7b83415a
  - held-source-d93760b262a3
  - held-source-4b310c169232
  - held-source-4a8883d91734
  - held-source-a8866814ba73
  - held-source-3a5de9f5d9a3
  - held-source-1069c74d36aa
  - held-source-eafe22a42e90
  - held-source-562a206a3c27
  - held-source-d70db50995af
  - held-source-8ebfaa26db29
  - held-source-7ec2823f4bfb
  - held-source-783cf521df3c
  - held-source-764c8c8dafdd
  - held-source-e524fe3c1ab2
  - held-source-660ea2039881
  - held-source-458fec7ef628
  - held-source-69c98a290efb
  - held-source-38acc372c42d
  - held-source-6d07f7e6c3a8
  - held-source-715cfe1166c2
  evidence_ids:
  - snapshot
  - generation
  command: PYTHONDONTWRITEBYTECODE=1 ../envs/mim/bin/python ../step1-independent/probe_final_snapshot.py
  exit_code: 0
- check_id: source_provenance
  name: Ledger-source and stale-output negative control
  status: passed
  required: true
  summary: All 33 cited source selectors match; all 57 prior ledger rows form an exact
    prefix. The pre-hold export is rejected with 126 messages covering all 33 held
    labels.
  target_ids:
  - mappings/unified_mapping_rejections.tsv
  - scripts/check_unified_rejections.py
  - held-source-75b6be4855ac
  - held-source-71272ca0256b
  - held-source-d7ebfb492d5b
  - held-source-15ba44ba7cd2
  - held-source-c6f37a149c7f
  - held-source-ccc30f9dedb1
  - held-source-aa607f02029a
  - held-source-c5ba604021fa
  - held-source-f63aedfafd31
  - held-source-7e65c46c2293
  - held-source-dace2106e06b
  - held-source-3a3b5e39bb77
  - held-source-c8eb7b83415a
  - held-source-d93760b262a3
  - held-source-4b310c169232
  - held-source-4a8883d91734
  - held-source-a8866814ba73
  - held-source-3a5de9f5d9a3
  - held-source-1069c74d36aa
  - held-source-eafe22a42e90
  - held-source-562a206a3c27
  - held-source-d70db50995af
  - held-source-8ebfaa26db29
  - held-source-7ec2823f4bfb
  - held-source-783cf521df3c
  - held-source-764c8c8dafdd
  - held-source-e524fe3c1ab2
  - held-source-660ea2039881
  - held-source-458fec7ef628
  - held-source-69c98a290efb
  - held-source-38acc372c42d
  - held-source-6d07f7e6c3a8
  - held-source-715cfe1166c2
  evidence_ids:
  - hold_sources
  command: PYTHONDONTWRITEBYTECODE=1 ../envs/mim/bin/python ../step1-independent/probe_mim_source_holds.py
  exit_code: 0
- check_id: native_qc
  name: Full native QC
  status: passed
  required: true
  summary: Full just qc passes, including schema/strict, evidence, SSSOM, roundtrip,
    visualization currency and flat export coverage. Execution was by the root agent;
    this reviewer inspected the final log and verified its hash.
  target_ids:
  - data/ingredients/mapped/Calcium_Chloride.yaml
  - data/ingredients/mapped/Cinnamic_Acid.yaml
  - data/ingredients/mapped/Cocl2_X_6_H2o.yaml
  - data/ingredients/mapped/Mgcl2x_6_H2o.yaml
  - data/ingredients/mapped/Na-glutamate.yaml
  - data/ingredients/mapped/Na2moo42h2o.yaml
  - data/ingredients/mapped/Nah2po4h2o.yaml
  - data/ingredients/mapped/Sodium_Citrate.yaml
  - data/ingredients/mapped/Trisodium_Citrate_X_2_H2o.yaml
  - data/ingredients/unmapped/Na2moo4_X_H2o.yaml
  - data/ingredients/unmapped/Trisodium_Citrate_X_3_H2o.yaml
  - scripts/apply_312_batch1.py
  - scripts/apply_312_batch4.py
  - scripts/check_unified_rejections.py
  - scripts/fix_merge_tombstone_resolution.py
  - scripts/merge_mapped_records.py
  - scripts/retire_wrong_form_names.py
  - tests/test_fix_merge_tombstone_resolution.py
  - tests/test_merge_mapped_records.py
  - tests/test_unified_rejections.py
  - mappings/unified_mapping_rejections.tsv
  - data/curated/mapped_ingredients.yaml
  - data/curated/unmapped_ingredients.yaml
  - reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  - .github/workflows/qc-evidence.yaml
  - scripts/.vendored_canon_ref
  - UNIFIED_INGREDIENT_MAPPING.tsv
  - UNIFIED_INGREDIENT_MAPPING.provenance.json
  - docs/data/label_index.csv
  - reports/semantic_review_20260921/resolution/current-review.json
  - mappings/ingredient_mappings.sssom.tsv
  - docs/UNIFIED_MAPPING_REJECTIONS.md
  - tests/test_unified_source_holds.py
  - held-source-75b6be4855ac
  - held-source-71272ca0256b
  - held-source-d7ebfb492d5b
  - held-source-15ba44ba7cd2
  - held-source-c6f37a149c7f
  - held-source-ccc30f9dedb1
  - held-source-aa607f02029a
  - held-source-c5ba604021fa
  - held-source-f63aedfafd31
  - held-source-7e65c46c2293
  - held-source-dace2106e06b
  - held-source-3a3b5e39bb77
  - held-source-c8eb7b83415a
  - held-source-d93760b262a3
  - held-source-4b310c169232
  - held-source-4a8883d91734
  - held-source-a8866814ba73
  - held-source-3a5de9f5d9a3
  - held-source-1069c74d36aa
  - held-source-eafe22a42e90
  - held-source-562a206a3c27
  - held-source-d70db50995af
  - held-source-8ebfaa26db29
  - held-source-7ec2823f4bfb
  - held-source-783cf521df3c
  - held-source-764c8c8dafdd
  - held-source-e524fe3c1ab2
  - held-source-660ea2039881
  - held-source-458fec7ef628
  - held-source-69c98a290efb
  - held-source-38acc372c42d
  - held-source-6d07f7e6c3a8
  - held-source-715cfe1166c2
  evidence_ids:
  - native_qc_evidence
  command: just qc
  exit_code: 0
- check_id: receipt_replay
  name: SSSOM receipt replay
  status: passed
  required: true
  summary: Replay reproduces all 2,987 rows with 1,740 SUPPORTED and 1,247 WITHHOLD
    dispositions.
  target_ids:
  - mappings/ingredient_mappings.sssom.tsv
  evidence_ids:
  - receipt_replay_evidence
  command: uv run --frozen python reports/sssom_completion_20260921/assemble_review.py
    --check
  exit_code: 0
- check_id: reviewed_sssom
  name: Reviewed SSSOM and schema
  status: passed
  required: true
  summary: Existing reviewed SSSOM export and schema validation pass.
  target_ids:
  - mappings/ingredient_mappings.sssom.tsv
  evidence_ids:
  - reviewed_sssom_evidence
  command: just qc-reviewed-sssom reports/sssom_completion_20260921/review.json output/step1-reviewed-sssom
  exit_code: 0
- check_id: supported_kgx
  name: Supported KGX
  status: passed
  required: true
  summary: Supported KGX validation passes while preserving excluded claims.
  target_ids:
  - reports/semantic_review_20260921/resolution/current-review.json
  evidence_ids:
  - supported_kgx_evidence
  command: just qc-supported-kgx reports/semantic_review_20260921/resolution/current-review.json
    output/step1-supported-kgx
  exit_code: 0
- check_id: companion
  name: Companion bundle
  status: passed
  required: true
  summary: Companion bundle validation passes against the unchanged manifest.
  target_ids:
  - UNIFIED_INGREDIENT_MAPPING.tsv
  - mappings/ingredient_mappings.sssom.tsv
  evidence_ids:
  - companion_evidence
  command: python -m mediaingredientmech.export.ingredient_bundle validate output/step1-ingredient-bundle
    --manifest-sha256 169bc30207fc65485a687f1a03b88f2c6241bdbca9939d459f97619a5192b0d6
  exit_code: 0
- check_id: semantic_integrity
  name: Native semantic-review integrity
  status: passed
  required: true
  summary: Integrity passes; the full semantic release remains FAIL with the preexisting
    1,733 finding and 2,272 assertion blockers.
  target_ids:
  - reports/semantic_review_20260921/resolution/current-review.json
  - reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  evidence_ids:
  - semantic_integrity_evidence
  command: python -m mediaingredientmech.validation.semantic_release --root . --report
    reports/semantic_review_20260921/resolution/current-review.json
  exit_code: 0
- check_id: optional_visual_regeneration
  name: optional visual regeneration
  status: failed
  required: false
  summary: Initial combined sync/export run completed those exports but optional visualization
    regeneration failed because the isolated embedding cache was absent. Final native
    QC independently verifies the exports and current published visualizations.
  target_ids:
  - data/curated/mapped_ingredients.yaml
  - docs/data/label_index.csv
  evidence_ids:
  - optional_visual_regeneration_evidence
  command: just sync-curated export-indexes export-lists export-browser generate-visualizations
  exit_code: 2
- check_id: visualization_currency
  name: visualization currency
  status: passed
  required: true
  summary: Both published visualization products are current with 2,340 live nodes
    each; the final full QC also repeats the currency gate.
  target_ids:
  - data/curated/mapped_ingredients.yaml
  - docs/data/label_index.csv
  evidence_ids:
  - visualization_currency_evidence
  command: just check-visualizations
  exit_code: 0
evidence:
- evidence_id: acceptance
  kind: validation
  reference: reports/unified_mapping_redo_20261101/checks/source-hold-final/independent-final-acceptance.json
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: 'Independent frozen-artifact acceptance: nine representatives, eleven history
    prefixes, nine unmapped synonyms, 34 identity-scoped additions, 33 held rows,
    zero required identity leaks and unchanged protected pins.'
  snapshot_sha256: d7193668156e09fcdffc3407508e72c4dc5efbfc47a84649a26a1d0538a874d2
- evidence_id: tests
  kind: validation
  reference: reports/unified_mapping_redo_20261101/checks/source-hold-final/independent-final-tests.log
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: All 67 focused tests passed; 12 dependency deprecation warnings did not
    affect results.
  snapshot_sha256: f2533ee162109748fd8a3952cb4d608e21e8f6c7b902caa398257250d717abf7
- evidence_id: test_receipt
  kind: validation
  reference: reports/unified_mapping_redo_20261101/checks/source-hold-final/independent-final-checks.json
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: Actual independent commands, exit codes, input hashes and output hashes
    for the final acceptance and test run.
  snapshot_sha256: e35b390631d3a1bede69dd3073fa3650607a9f6aac273c7cfe072aa3efbfbd1c
- evidence_id: snapshot
  kind: validation
  reference: reports/unified_mapping_redo_20261101/checks/source-hold-final/independent-final-snapshot-probe.json
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: All 4,170 rows match the native builder, exactly 33 held labels changed,
    all 4,137 other rows and every count/example remain identical; all 18,873 receipt
    inputs verified.
  snapshot_sha256: a7a124f19d439d861a42bfeaf8c48978921cb790d323e67344e3e4083dd79c26
- evidence_id: hold_sources
  kind: validation
  reference: reports/unified_mapping_redo_20261101/checks/source-hold-final/independent-mim-source-hold-probe.json
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: The exact 57-row ledger prefix and all 33 appended pairs were verified;
    each source commit/path/hash/selector contains the stated label and ID. The old
    snapshot fails for every held label.
  snapshot_sha256: 2b37e1fc8cd3a519838898435dea0ae279ff28830664f3f725c40c7f449eff88
- evidence_id: semantic_boundary
  kind: validation
  reference: reports/unified_mapping_redo_20261101/checks/source-hold-final/independent-semantic-boundary-check.json
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: Baseline and final release verdicts remain FAIL with identical blocker-ID
    lists. Exactly nine finding-disposition rows change only their current-record
    hash.
  snapshot_sha256: 67689a96f1801b9b736693805d783af92399adbfb599a50893306423cd27e3c9
- evidence_id: generation
  kind: validation
  reference: reports/unified_mapping_redo_20261101/checks/source-hold-final/unified-generation-receipt.json
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: Guarded native generation binds the frozen CultureMech recipes, MIM records/index/ledger
    and merged Claw producer to the final TSV.
  snapshot_sha256: f65d90b10e8bd74feb34603d773c2281a06a7e58a2d396fe8dac569abd5ccc10
- evidence_id: ontology_cache
  kind: database
  reference: reports/unified_mapping_redo_20261101/checks/independent-chebi-cache-verification.json
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: Inspected local ChEBI labels/formulas corroborate the eight distinct representative
    targets and identify the two wrong historical rationale accessions.
  snapshot_sha256: 2ddecbc31901fb660eef70a6380317a277e3a3895f76f5094150f01471eb6e95
- evidence_id: legacy_ledger
  kind: validation
  reference: reports/unified_mapping_redo_20261101/checks/independent-ledger-and-owner-checks.json
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: The 34 identity-scoped additions agree with the referenced YAML primary
    identifiers and exported exact label owners.
  snapshot_sha256: f3f2cd23c40a4b68857b3f7f8516c675e0d58102d0d25f2b73a8531f015657d1
- evidence_id: prefixed_history
  kind: prior_review
  reference: reports/unified_mapping_redo_20261101/checks/independent-history-reproduction.json
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: 'Pre-fix probe demonstrates that another necessary repair removed its prior
    repair event; retained as historical evidence for #1022.'
  snapshot_sha256: 675b6cc994269e46387d7c76dc957c57c2fd52c8a1485c260fe34215c9a0c6a8
- evidence_id: prior_findings
  kind: prior_review
  reference: reports/unified_mapping_redo_20261101/checks/independent-pre-fix-observations.json
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: Pre-fix source hashes and observations support the filed defects without
    inventing prior structured-review lineage.
  snapshot_sha256: 201b785ead5b266e4f585ce54d379ccd32d93f8b676ee8b77a4eb8a63c0f608f
- evidence_id: initial_delta
  kind: validation
  reference: reports/unified_mapping_redo_20261101/checks/independent-unified-54-identity-owner-check.json
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: Bounded screen of the 54 initially changed preexisting MIM identities distinguishes
    exact owners from fallback assignments.
  snapshot_sha256: 8ba171f377fe8dab081e020ea6397659a30a16588391a4d632380e38048d833b
- evidence_id: fallback_findings
  kind: prior_review
  reference: reports/unified_mapping_redo_20261101/checks/independent-unified-fallback-findings.json
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: Pre-hold observations identify preparation, variable hydration and vitamer/class
    boundary escapes in the refreshed source fallback.
  snapshot_sha256: 4c021d55c2b3d308e4f6790cf3690e1309e17a749559062f8e5b6bad3402dd1a
- evidence_id: hold_cohort
  kind: record_content
  reference: reports/unified_mapping_redo_20261101/checks/independent-proposed-source-holds.json
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: 'Finite 33-pair cohort with exact source contexts: 27 preparation, three
    hydration-state and three vitamer/class holds.'
  snapshot_sha256: 105dfc13469d3f404bd68111c11e032a61eef1f748e7187ee6bded10ea34e76c
- evidence_id: semantics
  kind: authority
  reference: MAPPING_SEMANTICS.md
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: Identity, preparation scope, salt/hydrate/stereo distinctions, mapping
    predicates and publication remain governed by the repository contract.
  snapshot_sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
  locator: Section 0 and identity/SSSOM rules
- evidence_id: profile
  kind: authority
  reference: docs/record-review-profile.md
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: A bounded structural/provenance review preserves native scientific release
    holds and does not promote record status.
  snapshot_sha256: da17e2048a13514a422bc94bd2f8d48943cffc5689b96e3f07da26423248d1a7
- evidence_id: contract
  kind: record_content
  reference: docs/UNIFIED_MAPPING_REJECTIONS.md
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: The consumer documents exact source-label holds, intentional blank replacement
    cells, independent ownership and unchanged identity-wide behavior.
  snapshot_sha256: b0989f6b82dd40e6a3593c297935aaf21c8f9fc6591b456e484e38e78d3a3317
- evidence_id: claw_review
  kind: prior_review
  reference: reports/unified_mapping_redo_20261101/checks/claw697-review/final-3756b6f.json
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: Independent producer review at exact head 3756b6f passed with 171 unified
    tests and an all-row corpus comparison; no in-scope findings.
  snapshot_sha256: 79f93152fd2e7d0b4ce1748aef0a35ea71e9effaeca9316d48238197cb80f91e
- evidence_id: claw_merge
  kind: validation
  reference: reports/unified_mapping_redo_20261101/checks/claw697-validation/verified-merge-cleanup.json
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: The merged producer 0cc221bd preserves all three reviewed source/doc/test
    hashes and records queue merge and branch cleanup.
  snapshot_sha256: c182d354bd3d4fc66d3e5c28ddd6bf5e046f629dd669b56841c816becb248450
- evidence_id: record1
  kind: record_content
  reference: data/ingredients/mapped/Calcium_Chloride.yaml
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: Inspected current identity/status, representative or unresolved form, synonyms
    and append-only curation history.
  snapshot_sha256: 14a47e745967b921cceb9f947ef2ef668504063a2fecc440299aa69ef8b84e56
- evidence_id: record2
  kind: record_content
  reference: data/ingredients/mapped/Cinnamic_Acid.yaml
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: Inspected current identity/status, representative or unresolved form, synonyms
    and append-only curation history.
  snapshot_sha256: b6a625455de0f9f339d71ee5fff4a25a0d66c8e318e2863fe8af1f4ac91be89a
- evidence_id: record3
  kind: record_content
  reference: data/ingredients/mapped/Cocl2_X_6_H2o.yaml
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: Inspected current identity/status, representative or unresolved form, synonyms
    and append-only curation history.
  snapshot_sha256: 1155e44909ee569b943117d26a240f072f7aea1fc0f0afcb705ce5edc14bed22
- evidence_id: record4
  kind: record_content
  reference: data/ingredients/mapped/Mgcl2x_6_H2o.yaml
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: Inspected current identity/status, representative or unresolved form, synonyms
    and append-only curation history.
  snapshot_sha256: 520ebd239f456859bdff9e576a27faf95eb564fe6a6a10bbf16013bee01c6d83
- evidence_id: record5
  kind: record_content
  reference: data/ingredients/mapped/Na-glutamate.yaml
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: Inspected current identity/status, representative or unresolved form, synonyms
    and append-only curation history.
  snapshot_sha256: 1b54cebe01112e2c8973e78127a1b2eb83a801535ab1967015545bfa137b5f0e
- evidence_id: record6
  kind: record_content
  reference: data/ingredients/mapped/Na2moo42h2o.yaml
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: Inspected current identity/status, representative or unresolved form, synonyms
    and append-only curation history.
  snapshot_sha256: 5a6b277f3274ca6a6ea7feaf988927939c51513fe63fd95e40b6f435ff0a8f17
- evidence_id: record7
  kind: record_content
  reference: data/ingredients/mapped/Nah2po4h2o.yaml
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: Inspected current identity/status, representative or unresolved form, synonyms
    and append-only curation history.
  snapshot_sha256: ff636e9f09fa3f0767d05ad811a4ee706be655fb9007194505d4419741b2595c
- evidence_id: record8
  kind: record_content
  reference: data/ingredients/mapped/Sodium_Citrate.yaml
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: Inspected current identity/status, representative or unresolved form, synonyms
    and append-only curation history.
  snapshot_sha256: 8d5931b67aa99c5877679aa2e956234eef16e5c3ba3ea767e03f47c302d5b27e
- evidence_id: record9
  kind: record_content
  reference: data/ingredients/mapped/Trisodium_Citrate_X_2_H2o.yaml
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: Inspected current identity/status, representative or unresolved form, synonyms
    and append-only curation history.
  snapshot_sha256: 69e37553e442f91d155193d4c69077afe54da649e74e11666821b2e30255112a
- evidence_id: record10
  kind: record_content
  reference: data/ingredients/unmapped/Na2moo4_X_H2o.yaml
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: Inspected current identity/status, representative or unresolved form, synonyms
    and append-only curation history.
  snapshot_sha256: 0bcee9de76e0455f426fb0e12469a48e1091ad91a2251d5530923869b18e3de8
- evidence_id: record11
  kind: record_content
  reference: data/ingredients/unmapped/Trisodium_Citrate_X_3_H2o.yaml
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: Inspected current identity/status, representative or unresolved form, synonyms
    and append-only curation history.
  snapshot_sha256: 1bd94f0ca085cb4be39f87fadea062b3efdcae0f908fe0dff47a8ba95b40b456
- evidence_id: glutamate_authority
  kind: primary_source
  reference: https://www.ebi.ac.uk/chebi/CHEBI:29988
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: ChEBI identifies the L-glutamate dianion, supporting the corrected rationale
    rather than the former unrelated accession.
  locator: Entry identity, definition/formula or ontology relations as applicable
- evidence_id: chloride_authority
  kind: primary_source
  reference: https://www.ebi.ac.uk/chebi/CHEBI:63041
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: ChEBI identifies manganese(II) chloride, corroborating that this accession
    cannot support the older citrate rationale.
  locator: Entry identity, definition/formula or ontology relations as applicable
- evidence_id: manganese_authority
  kind: primary_source
  reference: https://www.ebi.ac.uk/chebi/CHEBI:86360
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: The inspected manganese(II) sulfate entry has formula Mn.O4S; it does not
    establish exact identity for the explicitly hydrated source labels.
  locator: Entry identity, definition/formula or ontology relations as applicable
- evidence_id: b12_authority
  kind: primary_source
  reference: https://www.ebi.ac.uk/chebi/CHEBI:176843
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: ChEBI defines a class spanning several cobalamin vitamers; an explicitly
    named cyanocobalamin source is more specific.
  locator: Entry identity, definition/formula or ontology relations as applicable
- evidence_id: cobalamin_authority
  kind: primary_source
  reference: https://www.ebi.ac.uk/chebi/CHEBI:30411
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: The cobalamin entry is placed below cobalamins, supporting retained scope
    uncertainty for the qualified source label.
  locator: Entry identity, definition/formula or ontology relations as applicable
- evidence_id: cobalamins_authority
  kind: primary_source
  reference: https://www.ebi.ac.uk/chebi/CHEBI:23334
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: The ontology places cobalamins beneath vitamin B12; the hierarchy supports
    withholding an unreviewed exact class/member identity.
  locator: Entry identity, definition/formula or ontology relations as applicable
- evidence_id: native_qc_evidence
  kind: validation
  reference: reports/unified_mapping_redo_20261101/checks/source-hold-final/source-holds-full-qc.log
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: Full just qc passes, including schema/strict, evidence, SSSOM, roundtrip,
    visualization currency and flat export coverage. Execution was by the root agent;
    this reviewer inspected the final log and verified its hash.
  snapshot_sha256: d20034a4067581ba50b8ca21f88c90b5bd25f25fed71a99702a6e83caec5dd53
- evidence_id: receipt_replay_evidence
  kind: validation
  reference: reports/unified_mapping_redo_20261101/checks/source-hold-final/source-holds-receipt-replay.log
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: Replay reproduces all 2,987 rows with 1,740 SUPPORTED and 1,247 WITHHOLD
    dispositions.
  snapshot_sha256: 710484b8faef7b4592edeb4f762119c2b8f7863c30a31709de9f808a75ae599e
- evidence_id: reviewed_sssom_evidence
  kind: validation
  reference: reports/unified_mapping_redo_20261101/checks/source-hold-final/source-holds-reviewed-release.log
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: Existing reviewed SSSOM export and schema validation pass.
  snapshot_sha256: eaa0723a3cb9c90f815752f64ce76258ecb24c2bc3f5dfdecd682f60234756d6
- evidence_id: supported_kgx_evidence
  kind: validation
  reference: reports/unified_mapping_redo_20261101/checks/source-hold-final/source-holds-supported-release.log
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: Supported KGX validation passes while preserving excluded claims.
  snapshot_sha256: 17c33094ba60156dd91757753e07e75793bb8b290d7fffd280c62748532e4bdc
- evidence_id: companion_evidence
  kind: validation
  reference: reports/unified_mapping_redo_20261101/checks/source-hold-final/source-holds-companion-release.log
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: Companion bundle validation passes against the unchanged manifest.
  snapshot_sha256: 8ebcd9844e21f9e0ad5cc0502f944f93a87cf7b2dba9d1a7badee02c12269ff5
- evidence_id: semantic_integrity_evidence
  kind: validation
  reference: reports/unified_mapping_redo_20261101/checks/source-hold-final/source-holds-semantic-integrity.log
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: Integrity passes; the full semantic release remains FAIL with the preexisting
    1,733 finding and 2,272 assertion blockers.
  snapshot_sha256: 90eb85ea6aac322e5f500e252bac25fb0cde9acbc1817fba8d2bd9d0ebfcee81
- evidence_id: optional_visual_regeneration_evidence
  kind: validation
  reference: reports/unified_mapping_redo_20261101/checks/sync-and-exports.log
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: Initial combined sync/export run completed those exports but optional visualization
    regeneration failed because the isolated embedding cache was absent. Final native
    QC independently verifies the exports and current published visualizations.
  snapshot_sha256: 8868fbd73acf0779d479bcf9e4c90b276411a78d27a2073e8613c856b5f9990d
- evidence_id: visualization_currency_evidence
  kind: validation
  reference: reports/unified_mapping_redo_20261101/checks/visualization-currency.log
  accessed_at: '2026-11-01T03:58:30Z'
  support: supports
  summary: Both published visualization products are current with 2,340 live nodes
    each; the final full QC also repeats the currency gate.
  snapshot_sha256: 69a1810deba009f5758a3d67b474b763ad8e1ac4c81d54d15184f6f206ad4f04
assessments:
- assessment_id: representatives
  area: identity
  topic: Explicit live representatives for rejected aliases
  outcome: supported
  summary: All nine tombstones retain REJECTED status and point to the reviewed live
    representatives. Form-specific targets preserve hydrate, salt and stereochemical
    boundaries.
  target_ids:
  - data/ingredients/mapped/Calcium_Chloride.yaml
  - data/ingredients/mapped/Cinnamic_Acid.yaml
  - data/ingredients/mapped/Cocl2_X_6_H2o.yaml
  - data/ingredients/mapped/Mgcl2x_6_H2o.yaml
  - data/ingredients/mapped/Na-glutamate.yaml
  - data/ingredients/mapped/Na2moo42h2o.yaml
  - data/ingredients/mapped/Nah2po4h2o.yaml
  - data/ingredients/mapped/Sodium_Citrate.yaml
  - data/ingredients/mapped/Trisodium_Citrate_X_2_H2o.yaml
  evidence_ids:
  - acceptance
  - ontology_cache
  - tests
  - record1
  - record2
  - record3
  - record4
  - record5
  - record6
  - record7
  - record8
  - record9
  details: This assesses representative routing and selected refused synonyms. Historical
    inactive chemistry, role and evidence fields retained in tombstones are not newly
    scientifically approved.
- assessment_id: unresolved_forms
  area: identity
  topic: Unmapped monohydrate and trihydrate surface forms
  outcome: supported
  summary: UNMAPPED_0851 and UNMAPPED_0852 preserve the sodium-molybdate monohydrate
    and trisodium-citrate trihydrate surface forms without a guessed ontology identity.
    All nine synonyms resolve to the intended owner and both corrections append history.
  target_ids:
  - data/ingredients/unmapped/Na2moo4_X_H2o.yaml
  - data/ingredients/unmapped/Trisodium_Citrate_X_3_H2o.yaml
  evidence_ids:
  - acceptance
  - tests
  - record10
  - record11
- assessment_id: provenance
  area: provenance
  topic: Append-only repairs and corrected rationale
  outcome: supported
  summary: Repeated necessary repairs preserve the earlier event prefix and become
    idempotent. Corrected future rationale and appended CORRECTED_PROVENANCE events
    resolve the two wrong ontology citations while preserving older history.
  target_ids:
  - scripts/fix_merge_tombstone_resolution.py
  - tests/test_fix_merge_tombstone_resolution.py
  - data/ingredients/mapped/Na-glutamate.yaml
  - data/ingredients/mapped/Sodium_Citrate.yaml
  evidence_ids:
  - tests
  - prefixed_history
  - prior_findings
  - glutamate_authority
  - chloride_authority
- assessment_id: writers
  area: representation
  topic: Merge and retirement identity routing
  outcome: supported
  summary: The changed writers record explicit representatives and avoid new REJECTED
    status transitions that could hide a documented merge. New repair allocations
    avoid the retired placeholder IDs; regression tests cover representative creation
    and repair behavior.
  target_ids:
  - scripts/apply_312_batch1.py
  - scripts/apply_312_batch4.py
  - scripts/fix_merge_tombstone_resolution.py
  - scripts/merge_mapped_records.py
  - scripts/retire_wrong_form_names.py
  - tests/test_merge_mapped_records.py
  evidence_ids:
  - tests
  - acceptance
  - semantics
- assessment_id: rejection_contract
  area: consistency
  topic: Identity-wide rejections and exact source-label holds
  outcome: supported
  summary: The 90-row ledger preserves its 57-row prefix and adds exactly the 33 reviewed
    blank-replacement pairs. The checker retains legacy identity preservation, rejects
    malformed cells and catches held IDs in all five identity columns without creating
    a global empty-identity rule.
  target_ids:
  - scripts/check_unified_rejections.py
  - docs/UNIFIED_MAPPING_REJECTIONS.md
  - mappings/unified_mapping_rejections.tsv
  - tests/test_unified_rejections.py
  - tests/test_unified_source_holds.py
  evidence_ids:
  - contract
  - tests
  - hold_sources
  - legacy_ledger
  - claw_review
  - claw_merge
  details: Independent different-ID ownership remains permitted by the consumer; the
    producer validates owner contradictions before generation. The finite final corpus
    has no independent owners for the 33 held labels.
- assessment_id: preparation_holds
  area: scope
  topic: Finite preparation-scope withholding
  outcome: supported
  summary: All 27 explicit concentration, solvent, solution or pH-qualified source
    labels remain UNMAPPED pending preparation curation. No neat-reagent identity
    or borrowed metadata survives, and all source labels, counts and media examples
    remain.
  target_ids:
  - held-source-75b6be4855ac
  - held-source-71272ca0256b
  - held-source-d7ebfb492d5b
  - held-source-15ba44ba7cd2
  - held-source-c6f37a149c7f
  - held-source-ccc30f9dedb1
  - held-source-aa607f02029a
  - held-source-c5ba604021fa
  - held-source-f63aedfafd31
  - held-source-7e65c46c2293
  - held-source-c8eb7b83415a
  - held-source-d93760b262a3
  - held-source-4b310c169232
  - held-source-4a8883d91734
  - held-source-a8866814ba73
  - held-source-3a5de9f5d9a3
  - held-source-1069c74d36aa
  - held-source-eafe22a42e90
  - held-source-562a206a3c27
  - held-source-d70db50995af
  - held-source-8ebfaa26db29
  - held-source-7ec2823f4bfb
  - held-source-783cf521df3c
  - held-source-764c8c8dafdd
  - held-source-e524fe3c1ab2
  - held-source-660ea2039881
  - held-source-458fec7ef628
  evidence_ids:
  - semantics
  - hold_sources
  - snapshot
  - hold_cohort
  dimensions:
  - name: decision_scope
    value: negative source-label/ID hold; no replacement asserted
    definition: The reviewed decision withholds an unestablished exact supplied-preparation
      identity; it does not choose a new ingredient record.
    evidence_ids:
    - semantics
    - hold_sources
- assessment_id: hydrate_holds
  area: identity
  topic: Variable manganese-sulfate hydration
  outcome: supported
  summary: All three variable-hydration source labels withhold the anhydrous manganese(II)
    sulfate ID. They retain their source occurrence information without inventing
    a specific hydrate identity.
  target_ids:
  - held-source-3a3b5e39bb77
  - held-source-69c98a290efb
  - held-source-38acc372c42d
  evidence_ids:
  - semantics
  - hold_sources
  - snapshot
  - hold_cohort
  - manganese_authority
- assessment_id: vitamer_holds
  area: scope
  topic: Vitamin B12 class/member boundaries
  outcome: supported
  summary: The two explicitly cyanocobalamin labels withhold the broad vitamin B12
    class. Vitamin B12 (Cobalamin) remains held pending scope clarification; no substitute
    identity is selected.
  target_ids:
  - held-source-dace2106e06b
  - held-source-6d07f7e6c3a8
  - held-source-715cfe1166c2
  evidence_ids:
  - semantics
  - hold_sources
  - snapshot
  - hold_cohort
  - b12_authority
  - cobalamin_authority
  - cobalamins_authority
  details: The cobalamin hold is a conservative unresolved-scope decision, distinct
    from the two explicit cyanocobalamin/class mismatches. These assessments support
    withholding rather than scientific approval of an alternate mapping.
- assessment_id: products
  area: consistency
  topic: Synchronized and reproducible generated products
  outcome: supported
  summary: Native QC validates synchronized records, indexes and current list/browser
    products. All 4,170 unified rows match the native builder and the provenance digest
    matches 2,955 MIM inputs. The final hold-only delta changes exactly 33 rows and
    preserves all source occurrence counts and examples.
  target_ids:
  - data/curated/mapped_ingredients.yaml
  - data/curated/unmapped_ingredients.yaml
  - docs/data/label_index.csv
  - UNIFIED_INGREDIENT_MAPPING.tsv
  - UNIFIED_INGREDIENT_MAPPING.provenance.json
  evidence_ids:
  - native_qc_evidence
  - acceptance
  - snapshot
  - generation
  details: The provenance mim_rev intentionally records the durable merge-base under
    the existing freshness contract; exact current input hashes establish the working-tree
    content. The initial 54 changed identities and 290 added labels were screened
    for this fallback mechanism, not comprehensively scientifically approved.
  metrics:
  - name: structurally compared unified rows
    value: 4170
    unit: rows
    definition: Rows compared to the native builder; not a count of scientifically
      reviewed ingredients.
    denominator: 4170
  - name: source occurrences retained
    value: 209330
    unit: occurrences
    definition: Sum of occurrence_count across the final unified rows.
- assessment_id: sssom
  area: consistency
  topic: Unchanged canonical mapping and retained receipt dispositions
  outcome: supported
  summary: 'Canonical SSSOM remains byte-identical to baseline 2add44fb: 2,987 rows
    with SHA256 a2b83ccdcaad67d89943ccf0f0e30d796cdbc5e418ead247313631b713e89722.
    Native invariants and receipt replay pass; supported/withheld dispositions remain
    unchanged.'
  target_ids:
  - mappings/ingredient_mappings.sssom.tsv
  evidence_ids:
  - snapshot
  - receipt_replay_evidence
  - reviewed_sssom_evidence
- assessment_id: semantic_boundary
  area: provenance
  topic: Current hashes with preserved scientific-release holds
  outcome: supported
  summary: The current native review has valid integrity. Nine finding rows update
    only current-record hashes; blocker identities and all dispositions remain unchanged.
    Full semantic release still fails on 1,733 findings and 2,272 assertions.
  target_ids:
  - reports/semantic_review_20260921/resolution/current-review.json
  - reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  evidence_ids:
  - semantic_boundary
  - semantic_integrity_evidence
  - supported_kgx_evidence
  - profile
  details: This positive assessment concerns faithful preservation of native evidence
    and release boundaries. It does not resolve or approve the preexisting scientific
    backlog.
- assessment_id: protected_pins
  area: scope
  topic: Approved dependency boundary
  outcome: supported
  summary: Both excluded pin/workflow files match baseline. The unified producer uses
    the separately reviewed merged Claw source-hold change while the evidence validator
    remains on its approved pinned revision.
  target_ids:
  - .github/workflows/qc-evidence.yaml
  - scripts/.vendored_canon_ref
  evidence_ids:
  - acceptance
  - claw_merge
  - native_qc_evidence
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - data/ingredients/mapped/Calcium_Chloride.yaml
  - data/ingredients/mapped/Cinnamic_Acid.yaml
  - data/ingredients/mapped/Cocl2_X_6_H2o.yaml
  - data/ingredients/mapped/Mgcl2x_6_H2o.yaml
  - data/ingredients/mapped/Na-glutamate.yaml
  - data/ingredients/mapped/Na2moo42h2o.yaml
  - data/ingredients/mapped/Nah2po4h2o.yaml
  - data/ingredients/mapped/Sodium_Citrate.yaml
  - data/ingredients/mapped/Trisodium_Citrate_X_2_H2o.yaml
  - data/ingredients/unmapped/Na2moo4_X_H2o.yaml
  - data/ingredients/unmapped/Trisodium_Citrate_X_3_H2o.yaml
  rationale: Keep rejected merge history attached to explicit representatives and
    keep unresolved mono-/trihydrate surface forms distinct from sibling hydrates.
  evidence_ids:
  - semantics
  - acceptance
- action: defer
  target_ids:
  - held-source-75b6be4855ac
  - held-source-71272ca0256b
  - held-source-d7ebfb492d5b
  - held-source-15ba44ba7cd2
  - held-source-c6f37a149c7f
  - held-source-ccc30f9dedb1
  - held-source-aa607f02029a
  - held-source-c5ba604021fa
  - held-source-f63aedfafd31
  - held-source-7e65c46c2293
  - held-source-dace2106e06b
  - held-source-3a3b5e39bb77
  - held-source-c8eb7b83415a
  - held-source-d93760b262a3
  - held-source-4b310c169232
  - held-source-4a8883d91734
  - held-source-a8866814ba73
  - held-source-3a5de9f5d9a3
  - held-source-1069c74d36aa
  - held-source-eafe22a42e90
  - held-source-562a206a3c27
  - held-source-d70db50995af
  - held-source-8ebfaa26db29
  - held-source-7ec2823f4bfb
  - held-source-783cf521df3c
  - held-source-764c8c8dafdd
  - held-source-e524fe3c1ab2
  - held-source-660ea2039881
  - held-source-458fec7ef628
  - held-source-69c98a290efb
  - held-source-38acc372c42d
  - held-source-6d07f7e6c3a8
  - held-source-715cfe1166c2
  rationale: Withhold only the reviewed source-label/ID pairs pending preparation,
    hydration or class/member curation; assert no replacement identity.
  evidence_ids:
  - semantics
  - hold_sources
  - snapshot
limitations:
- The review is structural/provenance-focused with bounded ontology identity checks;
  scientific_review is false. It does not approve every field of the 11 ingredient
  records or any of the other corpus records.
- Full semantic release remains FAIL with the same 1,733 blocking findings and 2,272
  blocking assertions. Its native integrity and supported-export checks pass without
  clearing those holds.
- The 54 initially changed MIM identities and 290 added source labels were screened
  for the identified fallback mechanism. This is not a comprehensive chemical review
  of those populations.
- An optional visualization regeneration attempt lacked the isolated embedding cache.
  Required visualization-currency and final full-QC checks pass on the existing products.
- Root executed the complete native QC/release checks; the independent reviewer inspected
  their hash-bound logs and independently ran the focused tests, acceptance, source-selector
  and all-row artifact probes.
- This is a working-tree attestation on an actual detached checkout at durable baseline
  2add44fb, overlaid with the exact frozen PR source/evidence bytes. The later final
  committed PR head requires a separate read-only verification.
notes:
- 'Pre-fix observations and mutations are retained as evidence. The corrected defects
  link to MIM #1021, #1022, #1023 and #1025 plus Claw #697/#698. They were not prior
  structured findings, so no previous_occurrences or synthetic terminal finding dispositions
  are created.'
- The original feature-head inspection was not saved. A fresh actual durable-base
  capture avoids retaining a squash-discarded feature commit as the native source
  revision. No source revision was manually relabeled.
- 'MIM #869, #882, #894 and #808 supply the approved step-1 context. No future-step
  curation or paid provider research is included.'
links:
- https://github.com/CultureBotAI/MediaIngredientMech/issues/869
- https://github.com/CultureBotAI/MediaIngredientMech/issues/882
- https://github.com/CultureBotAI/MediaIngredientMech/issues/894
- https://github.com/CultureBotAI/MediaIngredientMech/issues/808
- https://github.com/CultureBotAI/MediaIngredientMech/issues/1021
- https://github.com/CultureBotAI/MediaIngredientMech/issues/1022
- https://github.com/CultureBotAI/MediaIngredientMech/issues/1023
- https://github.com/CultureBotAI/MediaIngredientMech/issues/1025
- https://github.com/CultureBotAI/culturebotai-claw/issues/697
- https://github.com/CultureBotAI/culturebotai-claw/pull/698
tags:
- approved-plan-step1
- unified-mapping
- bounded-review
- provenance
```
