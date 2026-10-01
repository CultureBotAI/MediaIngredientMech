# YAML Record Review: Phenyl acetic acid

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Phenyl_Acetic_Acid.yaml`
- Started UTC: 2026-10-01T05:03:08Z
- Finished UTC: 2026-10-01T05:03:09Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Phenyl_Acetic_Acid.yaml`
- Identifier: `CHEBI:30745`
- Preferred term: Phenyl acetic acid
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Phenyl_Acetic_Acid.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:30745`.
- Ontology label: `phenylacetic acid`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Phenyl_Acetic_Acid.md` after the record changed from 9b3c34056f552c0fe0d5645ba43b914fdf287f85c7afd1cafd2fd0a19a08bc58 to 2d658c1eee89159e16e54af30159cd7345983f57fce943ab5858d00bc43e1a7b; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `2d658c1eee89159e16e54af30159cd7345983f57fce943ab5858d00bc43e1a7b`.
- Previous review: `reports/yaml_record_review/Phenyl_Acetic_Acid.md`.
- Previous record SHA-256: `9b3c34056f552c0fe0d5645ba43b914fdf287f85c7afd1cafd2fd0a19a08bc58`.
- Source occurrence traceability: 6 occurrence(s) across 6 medium/media.
- Latest curation event: CORRECTED by retire_wrong_compound_synonyms at 2026-09-20T00:00:00Z: Marked 1 synonym(s) non-resolving: ['LSM-15166']. ChEBI gives these names to CHEBI:103822, not to this record's CHEBI:30745 -- phenylacetic acid is not LSM-15166. Kept as REJECTED_LABEL so a rebuild cannot restore them from kg-microbe's synonym list (#669).
- Active SSSOM state: 1 active row(s) for `MIM:Phenyl_Acetic_Acid`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Phenyl_Acetic_Acid.md` after the record changed from 9b3c34056f552c0fe0d5645ba43b914fdf287f85c7afd1cafd2fd0a19a08bc58 to 2d658c1eee89159e16e54af30159cd7345983f57fce943ab5858d00bc43e1a7b; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Phenyl_Acetic_Acid.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The corrected CHEBI:30745 phenylacetic-acid identity passes, but final other exports LSM-15166 and CARBON_SOURCE is provisional.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Phenyl_Acetic_Acid.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Phenyl_Acetic_Acid.yaml`, `just validate-terms data/ingredients/mapped/Phenyl_Acetic_Acid.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Phenyl_Acetic_Acid.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Phenyl_Acetic_Acid.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
