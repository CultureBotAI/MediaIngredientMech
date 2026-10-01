# YAML Record Review: Sodium phosphate monobasic monohydrate

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Sodium_phosphate_monobasic_monohydrate.yaml`
- Started UTC: 2026-10-01T05:03:32Z
- Finished UTC: 2026-10-01T05:03:33Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Sodium_phosphate_monobasic_monohydrate.yaml`
- Identifier: `CHEBI:114249`
- Preferred term: Sodium phosphate monobasic monohydrate
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Sodium_phosphate_monobasic_monohydrate.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:114249`.
- Ontology label: `sodium dihydrogenphosphate monohydrate`.
- Mapping quality: `CAS_RN_LOOKUP`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Sodium_phosphate_monobasic_monohydrate.md` after the record changed from 03a04c1897d54a7d57a924d99d4f8411a87c990a4e02b5405ee4d26608a885e0 to e11652b78ae7590718cd4e259026cac5da0d9d51777792c7d12513355f4b1022; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `e11652b78ae7590718cd4e259026cac5da0d9d51777792c7d12513355f4b1022`.
- Previous review: `reports/yaml_record_review/Sodium_phosphate_monobasic_monohydrate.md`.
- Previous record SHA-256: `03a04c1897d54a7d57a924d99d4f8411a87c990a4e02b5405ee4d26608a885e0`.
- Source occurrence traceability: 50 occurrence(s) across 50 medium/media.
- Latest curation event: CORRECTED by claude at 2026-09-23T04:53:11.738703+00:00: evidence note added. The 2026-08-06 promotion used the Section 3 step 2 cas: fallback on the premise that ChEBI has no hydrate term. CHEBI:114249 'sodium dihydrogenphosphate monohydrate' (H2O.H2O4P.Na, InChIKey BBMHARZCALWXSL-UHFFFAOYSA-M) exists and xrefs cas:10049-21-5, the very CAS the record was keyed on, and Sodium_phosphate_monobasic_monohydrate already holds it: one substance under two identifiers -> merge (#312).
- Active SSSOM state: 1 active row(s) for `MIM:Sodium_phosphate_monobasic_monohydrate`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Sodium_phosphate_monobasic_monohydrate.md` after the record changed from 03a04c1897d54a7d57a924d99d4f8411a87c990a4e02b5405ee4d26608a885e0 to e11652b78ae7590718cd4e259026cac5da0d9d51777792c7d12513355f4b1022; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Sodium_phosphate_monobasic_monohydrate.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The exact CHEBI:114249 identity, CAS, hydrate synonyms, and final SSSOM row pass, but BUFFER is provisional.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Sodium_phosphate_monobasic_monohydrate.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Sodium_phosphate_monobasic_monohydrate.yaml`, `just validate-terms data/ingredients/mapped/Sodium_phosphate_monobasic_monohydrate.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Sodium_phosphate_monobasic_monohydrate.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Sodium_phosphate_monobasic_monohydrate.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
