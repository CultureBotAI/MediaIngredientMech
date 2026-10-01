# YAML Record Review: Sodium Citrate

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Sodium_Citrate.yaml`
- Started UTC: 2026-10-01T05:03:26Z
- Finished UTC: 2026-10-01T05:03:27Z
- Verdict: pass_with_minor_issues

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Sodium_Citrate.yaml`
- Identifier: `CHEBI:32142`
- Preferred term: Sodium Citrate
- Mapping status: `REJECTED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Sodium_Citrate.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `REJECTED`.
- Ontology ID: `CHEBI:32142`.
- Ontology label: `sodium citrate dihydrate`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 0.
- Identity judgement: Refreshed `reports/yaml_record_review/Sodium_Citrate.md` after the record changed from 4194495543653bc48777b0c89dfb8e43f62165b39702c03b175df0b11c884bfa to dede4bf4630f673fc6fe4ac5b70791b6d91e583c905f1d2ca0df56249640dbc9; preserved the previous minor finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `dede4bf4630f673fc6fe4ac5b70791b6d91e583c905f1d2ca0df56249640dbc9`.
- Previous review: `reports/yaml_record_review/Sodium_Citrate.md`.
- Previous record SHA-256: `4194495543653bc48777b0c89dfb8e43f62165b39702c03b175df0b11c884bfa`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: REJECTED_WRONG_FORM_SYNONYMS by claude at 2026-09-23T06:21:57.674086+00:00: Retyped REJECTED_LABEL: 'trisodium 2-hydroxypropane-1,2,3-tricarboxylate' (EXACT_SYNONYM): the anhydrous trisodium citrate CHEBI:53258 name on the sodium citrate dihydrate CHEBI:32142 tombstone (#232). The token is kept as provenance only; it must not resolve, be exported, or enter the SSSOM other column.
- Active SSSOM state: No active row for `MIM:Sodium_Citrate`, as expected for `REJECTED`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: None found.

## Findings

- **minor**: The previous finding set in `reports/yaml_record_review/Sodium_Citrate.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The rejected dihydrate duplicate is absent from final SSSOM; stale anhydrous structure and mixed synonyms are contained in its tombstone.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Sodium_Citrate.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Sodium_Citrate.yaml`, `just validate-terms data/ingredients/mapped/Sodium_Citrate.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Sodium_Citrate.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Sodium_Citrate.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
