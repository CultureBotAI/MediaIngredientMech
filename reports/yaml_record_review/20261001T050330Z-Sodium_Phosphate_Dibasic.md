# YAML Record Review: Sodium phosphate dibasic

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml`
- Started UTC: 2026-10-01T05:03:30Z
- Finished UTC: 2026-10-01T05:03:31Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml`
- Identifier: `CHEBI:37583`
- Preferred term: Sodium phosphate dibasic
- Mapping status: `REJECTED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `REJECTED`.
- Ontology ID: `CHEBI:37583`.
- Ontology label: `trisodium phosphate`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 0.
- Identity judgement: Refreshed `reports/yaml_record_review/Sodium_Phosphate_Dibasic.md` after the record changed from b4e7a80f4f611b0cf35a46f701a382a49ac0b2d706eba3f5714fdeb79e13e955 to aabdf39c562aff24b8326456268b4a1e0ac1716934d4d24d428072a8e138e674; preserved the previous blocker finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `aabdf39c562aff24b8326456268b4a1e0ac1716934d4d24d428072a8e138e674`.
- Previous review: `reports/yaml_record_review/Sodium_Phosphate_Dibasic.md`.
- Previous record SHA-256: `b4e7a80f4f611b0cf35a46f701a382a49ac0b2d706eba3f5714fdeb79e13e955`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: MERGED_INTO by mim_semantic_review_20260921 at 2026-09-21T21:33:25.379198+00:00: Merged into CHEBI:34683 (Na2HPO4). Dibasic sodium phosphate is disodium hydrogenphosphate, not trisodium phosphate. Sodium dihydrogen phosphate is monobasic and is a REJECTED_LABEL here; its 78 recipe rows are excluded from this transfer. Original fields remain only on this excluded tombstone. Evidence: https://www.ebi.ac.uk/chebi/CHEBI:34683
- Active SSSOM state: No active row for `MIM:Sodium_Phosphate_Dibasic`, as expected for `REJECTED`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Sodium_Phosphate_Dibasic.md` after the record changed from b4e7a80f4f611b0cf35a46f701a382a49ac0b2d706eba3f5714fdeb79e13e955 to aabdf39c562aff24b8326456268b4a1e0ac1716934d4d24d428072a8e138e674; preserved the previous blocker finding floor pending targeted retirement.

## Findings

- **blocker**: The previous finding set in `reports/yaml_record_review/Sodium_Phosphate_Dibasic.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: Sodium phosphate dibasic is exact-mapped to trisodium phosphate and exports monosodium phosphate as a synonym.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Sodium_Phosphate_Dibasic.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml`, `just validate-terms data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
