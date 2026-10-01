# YAML Record Review: Thiamine pyrophosphate

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Thiamine_pyrophosphate.yaml`
- Started UTC: 2026-10-01T05:03:42Z
- Finished UTC: 2026-10-01T05:03:43Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Thiamine_pyrophosphate.yaml`
- Identifier: `CHEBI:9532`
- Preferred term: Thiamine pyrophosphate
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Thiamine_pyrophosphate.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:9532`.
- Ontology label: `thiamine(1+) diphosphate`.
- Mapping quality: `SYNONYM_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Thiamine_pyrophosphate.md` after the record changed from 328fa914b8bae7bb0119ec14608fdce5b1c1d8158ef6c6cabaa8e92c0b87017f to 627c0ae9eea1d8845c5165172edeea792c8b32c6d4d4cc00974d1f7ad90704ad; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `627c0ae9eea1d8845c5165172edeea792c8b32c6d4d4cc00974d1f7ad90704ad`.
- Previous review: `reports/yaml_record_review/Thiamine_pyrophosphate.md`.
- Previous record SHA-256: `328fa914b8bae7bb0119ec14608fdce5b1c1d8158ef6c6cabaa8e92c0b87017f`.
- Source occurrence traceability: 26 occurrence(s) across 26 medium/media.
- Latest curation event: CORRECTED by retire_wrong_compound_synonyms at 2026-09-20T00:00:00Z: Marked 3 synonym(s) non-resolving: ['1-[(4-amino-2-methylpyrimidin-5-yl)methyl]-3-(2-{[hydroxy(phosphonooxy)phosphoryl]oxy}ethyl)-2-methylpyridinium', 'pyrithiamine diphosphate', 'pyrithiamine pyrophosphate']. ChEBI gives these names to CHEBI:45395, not to this record's CHEBI:9532 -- thiamine pyrophosphate is not pyrithiamine pyrophosphate, its antagonist. Kept as REJECTED_LABEL so a rebuild cannot restore them from kg-microbe's synonym list (#669).
- Active SSSOM state: 1 active row(s) for `MIM:Thiamine_pyrophosphate`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Thiamine_pyrophosphate.md` after the record changed from 328fa914b8bae7bb0119ec14608fdce5b1c1d8158ef6c6cabaa8e92c0b87017f to 627c0ae9eea1d8845c5165172edeea792c8b32c6d4d4cc00974d1f7ad90704ad; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Thiamine_pyrophosphate.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The CHEBI:9532 identity passes, but chloride-salt structure fields and chloride-specific final SSSOM other values remain from the pre-#319/#320 grounding.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Thiamine_pyrophosphate.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Thiamine_pyrophosphate.yaml`, `just validate-terms data/ingredients/mapped/Thiamine_pyrophosphate.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Thiamine_pyrophosphate.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Thiamine_pyrophosphate.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
