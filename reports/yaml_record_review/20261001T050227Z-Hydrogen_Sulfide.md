# YAML Record Review: Hydrogen sulfide

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Hydrogen_Sulfide.yaml`
- Started UTC: 2026-10-01T05:02:27Z
- Finished UTC: 2026-10-01T05:02:28Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Hydrogen_Sulfide.yaml`
- Identifier: `CHEBI:16136`
- Preferred term: Hydrogen sulfide
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Hydrogen_Sulfide.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:16136`.
- Ontology label: `hydrogen sulfide`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Hydrogen_Sulfide.md` after the record changed from 4a1ef8d395dca14c4b5948070a67fe7566124db1b70971f42e124a72eb8583e3 to 86a9e7563630ce4704cc3046ee639708650888be6bdaf7bd389e4a66711671a0; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `86a9e7563630ce4704cc3046ee639708650888be6bdaf7bd389e4a66711671a0`.
- Previous review: `reports/yaml_record_review/Hydrogen_Sulfide.md`.
- Previous record SHA-256: `4a1ef8d395dca14c4b5948070a67fe7566124db1b70971f42e124a72eb8583e3`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: REJECTED_TRAIT_SYNONYMS by claude at 2026-09-22T06:14:49.563933+00:00: Retyped activity/assay phrases as provenance-only REJECTED_LABEL because they describe a process or organism trait, not an ingredient name (#703): 'produces: hydrogen sulfide'. Preserved original text and source metadata. No identity, mapping, role, or remaining-synonym claim was adjudicated.
- Active SSSOM state: 1 active row(s) for `MIM:Hydrogen_Sulfide`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Hydrogen_Sulfide.md` after the record changed from 4a1ef8d395dca14c4b5948070a67fe7566124db1b70971f42e124a72eb8583e3 to 86a9e7563630ce4704cc3046ee639708650888be6bdaf7bd389e4a66711671a0; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Hydrogen_Sulfide.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The exact hydrogen sulfide identity passes, but process-qualified text is exported as a synonym and role/context claims are unsupported.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Hydrogen_Sulfide.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Hydrogen_Sulfide.yaml`, `just validate-terms data/ingredients/mapped/Hydrogen_Sulfide.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Hydrogen_Sulfide.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Hydrogen_Sulfide.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
