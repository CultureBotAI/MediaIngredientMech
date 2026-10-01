# YAML Record Review: Trisodium citrate x 2 H2O

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Trisodium_Citrate_X_2_H2o.yaml`
- Started UTC: 2026-10-01T05:03:47Z
- Finished UTC: 2026-10-01T05:03:48Z
- Verdict: pass_with_minor_issues

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Trisodium_Citrate_X_2_H2o.yaml`
- Identifier: `CHEBI:32142`
- Preferred term: Trisodium citrate x 2 H2O
- Mapping status: `REJECTED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Trisodium_Citrate_X_2_H2o.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `REJECTED`.
- Ontology ID: `CHEBI:32142`.
- Ontology label: `sodium citrate dihydrate`.
- Mapping quality: `NARROW_MATCH`.
- Active SSSOM rows for this subject: 0.
- Identity judgement: Refreshed `reports/yaml_record_review/Trisodium_Citrate_X_2_H2o.md` after the record changed from 2ff97169ff4b12e889f319d92958ae786a0b0e05bfb86c0f5d5bc97ff5d30b40 to 434f429cbbb51fd5704ae557b55bb4c48440461840db61265bf51c6ba1365e7f; preserved the previous minor finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `434f429cbbb51fd5704ae557b55bb4c48440461840db61265bf51c6ba1365e7f`.
- Previous review: `reports/yaml_record_review/Trisodium_Citrate_X_2_H2o.md`.
- Previous record SHA-256: `2ff97169ff4b12e889f319d92958ae786a0b0e05bfb86c0f5d5bc97ff5d30b40`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: REJECTED_WRONG_FORM_SYNONYMS by claude at 2026-09-23T06:21:57.689391+00:00: Retyped REJECTED_LABEL: 'trisodium 2-hydroxypropane-1,2,3-tricarboxylate' (EXACT_SYNONYM): the anhydrous trisodium citrate CHEBI:53258 name on the sodium citrate dihydrate CHEBI:32142 tombstone (#232). The token is kept as provenance only; it must not resolve, be exported, or enter the SSSOM other column.
- Active SSSOM state: No active row for `MIM:Trisodium_Citrate_X_2_H2o`, as expected for `REJECTED`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: None found.

## Findings

- **minor**: The previous finding set in `reports/yaml_record_review/Trisodium_Citrate_X_2_H2o.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The rejected duplicate points at the live CHEBI:32142 sodium citrate dihydrate target and emits no final SSSOM row, but stale tombstone synonyms remain.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Trisodium_Citrate_X_2_H2o.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Trisodium_Citrate_X_2_H2o.yaml`, `just validate-terms data/ingredients/mapped/Trisodium_Citrate_X_2_H2o.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Trisodium_Citrate_X_2_H2o.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Trisodium_Citrate_X_2_H2o.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
