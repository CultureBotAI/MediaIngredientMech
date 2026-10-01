# YAML Record Review: Sodium adipate

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Sodium_Adipate.yaml`
- Started UTC: 2026-10-01T05:03:24Z
- Finished UTC: 2026-10-01T05:03:25Z
- Verdict: pass

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Sodium_Adipate.yaml`
- Identifier: `FOODON:03413240`
- Preferred term: Sodium adipate
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Sodium_Adipate.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `FOODON:03413240`.
- Ontology label: `sodium adipate`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Sodium_Adipate.md` after the record changed from 0fa341283044d05b8d0e2d990101d3503100e4b7e92d709d3322afd310c99eae to 0699b67ffbcc35d3566ff531350c753d93b677718cb4e550bdfa6257ba35886d; no prior finding is carried forward.

## Evidence

- Current record SHA-256: `0699b67ffbcc35d3566ff531350c753d93b677718cb4e550bdfa6257ba35886d`.
- Previous review: `reports/yaml_record_review/Sodium_Adipate.md`.
- Previous record SHA-256: `0fa341283044d05b8d0e2d990101d3503100e4b7e92d709d3322afd310c99eae`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: CORRECTED by kgmicrobe_identity_review_20260924 at 2026-09-24T07:10:47.897994+00:00: Original CAS, FoodOn INS 356 and JECFA identify disodium adipate. PubChem 24073 agrees with MIM formula and InChI containing two sodium ions. No monosodium form or hydrate is inferred.
- Active SSSOM state: 1 active row(s) for `MIM:Sodium_Adipate`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: None found.

## Findings

None found.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Sodium_Adipate.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Sodium_Adipate.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
