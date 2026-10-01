# YAML Record Review: Esculin Monohydrate

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Esculin_Monohydrate.yaml`
- Started UTC: 2026-10-01T05:02:14Z
- Finished UTC: 2026-10-01T05:02:15Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Esculin_Monohydrate.yaml`
- Identifier: `CHEBI:73111`
- Preferred term: Esculin Monohydrate
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Esculin_Monohydrate.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:73111`.
- Ontology label: `esculin hydrate`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Esculin_Monohydrate.md` after the record changed from b3c02996a796411b1dea434894a2be3cb72c9521c76f46d81af86901e58d30bb to 4c3f361d47f5f459d7d7969b001909e15a0fe847a494480156ba5a5e6e23bf92; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `4c3f361d47f5f459d7d7969b001909e15a0fe847a494480156ba5a5e6e23bf92`.
- Previous review: `reports/yaml_record_review/Esculin_Monohydrate.md`.
- Previous record SHA-256: `b3c02996a796411b1dea434894a2be3cb72c9521c76f46d81af86901e58d30bb`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: REJECTED_TRAIT_SYNONYMS by claude at 2026-09-22T06:14:49.563933+00:00: Retyped activity/assay phrases as provenance-only REJECTED_LABEL because they describe a process or organism trait, not an ingredient name (#703): 'hydrolysis: esculin'. Preserved original text and source metadata. No identity, mapping, role, or remaining-synonym claim was adjudicated.
- Active SSSOM state: 1 active row(s) for `MIM:Esculin_Monohydrate`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Esculin_Monohydrate.md` after the record changed from b3c02996a796411b1dea434894a2be3cb72c9521c76f46d81af86901e58d30bb to 4c3f361d47f5f459d7d7969b001909e15a0fe847a494480156ba5a5e6e23bf92; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Esculin_Monohydrate.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The exact ChEBI hydrate identity passes, but final SSSOM still exports hydrolysis assay text as a synonym.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Esculin_Monohydrate.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Esculin_Monohydrate.yaml`, `just validate-terms data/ingredients/mapped/Esculin_Monohydrate.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Esculin_Monohydrate.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Esculin_Monohydrate.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
