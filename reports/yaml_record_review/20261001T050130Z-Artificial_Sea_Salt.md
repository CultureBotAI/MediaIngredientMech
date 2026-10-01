# YAML Record Review: Artificial Sea Salt

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Artificial_Sea_Salt.yaml`
- Started UTC: 2026-10-01T05:01:30Z
- Finished UTC: 2026-10-01T05:01:31Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Artificial_Sea_Salt.yaml`
- Identifier: `kgmicrobe.ingredient:artificial_sea_salt`
- Preferred term: Artificial Sea Salt
- Mapping status: `MAPPED`
- Ingredient type: `UNDEFINED_MIXTURE`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Artificial_Sea_Salt.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `kgmicrobe.ingredient:artificial_sea_salt`.
- Ontology label: `Artificial Sea Salt`.
- Mapping quality: `FALLBACK_REGISTRY`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Artificial_Sea_Salt.md` after the record changed from b012529ebd6f2bc6688ab74f29631ea6405d7905a005fdd67b71c07ea08ee0e4 to effd1c0c9ca3056f20eceebebb7ab9c5dddff4434d0ed12dba6c344c7f91c389; preserved the previous blocker finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `effd1c0c9ca3056f20eceebebb7ab9c5dddff4434d0ed12dba6c344c7f91c389`.
- Previous review: `reports/yaml_record_review/Artificial_Sea_Salt.md`.
- Previous record SHA-256: `b012529ebd6f2bc6688ab74f29631ea6405d7905a005fdd67b71c07ea08ee0e4`.
- Source occurrence traceability: 12 occurrence(s) across 12 medium/media.
- Latest curation event: CORRECTED by mim_semantic_review_20260921 at 2026-09-21T21:33:25.379198+00:00: The source is an artificial sea-salt preparation, not natural evaporated sea salt. Replace lexical MICRO:0001647 identity with a local preparation identity; no composition is invented. Evidence: https://mediadive.dsmz.de/ingredients/2146
- Active SSSOM state: 1 active row(s) for `MIM:Artificial_Sea_Salt`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Artificial_Sea_Salt.md` after the record changed from b012529ebd6f2bc6688ab74f29631ea6405d7905a005fdd67b71c07ea08ee0e4 to effd1c0c9ca3056f20eceebebb7ab9c5dddff4434d0ed12dba6c344c7f91c389; preserved the previous blocker finding floor pending targeted retirement.

## Findings

- **blocker**: The previous finding set in `reports/yaml_record_review/Artificial_Sea_Salt.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The record exact-maps artificial sea salt to generic evaporated sea salt after a stem-substring upgrade that dropped the artificial qualifier.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Artificial_Sea_Salt.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Artificial_Sea_Salt.yaml`, `just validate-terms data/ingredients/mapped/Artificial_Sea_Salt.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Artificial_Sea_Salt.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Artificial_Sea_Salt.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
