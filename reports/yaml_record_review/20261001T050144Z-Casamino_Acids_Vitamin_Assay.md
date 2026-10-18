# YAML Record Review: Casamino acids (vitamin assay)

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Casamino_Acids_Vitamin_Assay.yaml`
- Started UTC: 2026-10-01T05:01:44Z
- Finished UTC: 2026-10-01T05:01:45Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Casamino_Acids_Vitamin_Assay.yaml`
- Identifier: `kgmicrobe.ingredient:casamino_acids_vitamin_assay`
- Preferred term: Casamino acids (vitamin assay)
- Mapping status: `MAPPED`
- Ingredient type: `UNDEFINED_MIXTURE`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Casamino_Acids_Vitamin_Assay.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `mesh:C017721`.
- Ontology label: `casamino acids`.
- Mapping quality: `NARROW_MATCH`.
- Active SSSOM rows for this subject: 2.
- Identity judgement: Refreshed `reports/yaml_record_review/Casamino_Acids_Vitamin_Assay.md` after the record changed from 03949c8795c9ad931a6c2437d48dcc500cb9dcca7deff08f59dda01b788d34c4 to 4a2fcdff99d8afac9b325e4b2f148b91c7cfcfde0fafa4633352dbfe71d435da; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `4a2fcdff99d8afac9b325e4b2f148b91c7cfcfde0fafa4633352dbfe71d435da`.
- Previous review: `reports/yaml_record_review/Casamino_Acids_Vitamin_Assay.md`.
- Previous record SHA-256: `03949c8795c9ad931a6c2437d48dcc500cb9dcca7deff08f59dda01b788d34c4`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: MINTED_REGISTRY_IDENTIFIER by claude at 2026-09-23T03:41:22.738468+00:00: identifier mesh:C017721 -> kgmicrobe.ingredient:casamino_acids_vitamin_assay; ontology mesh:C017721 ('casamino acids') -> mesh:C017721 ('casamino acids'); mapping_quality LEXICAL_MATCH -> NARROW_MATCH. mesh:C017721 'casamino acids' is the generic acid-hydrolysed casein (scope note 'acid hydrolyzed casein'); this record is the vitamin-depleted Difco/BD vitamin-assay grade, ordered separately, and MIM holds a separate generic Casamino_Acids record. An exactMatch collapsed a narrower product into its parent. Section 3 step 3: registry identity, broadMatch to the MeSH descriptor. (#312)
- Active SSSOM state: 2 active row(s) for `MIM:Casamino_Acids_Vitamin_Assay`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Casamino_Acids_Vitamin_Assay.md` after the record changed from 03949c8795c9ad931a6c2437d48dcc500cb9dcca7deff08f59dda01b788d34c4 to 4a2fcdff99d8afac9b325e4b2f148b91c7cfcfde0fafa4633352dbfe71d435da; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Casamino_Acids_Vitamin_Assay.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The exact MeSH Casamino acids variant mapping passes, but PROTEIN_SOURCE is only a provisional name-pattern prediction.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Casamino_Acids_Vitamin_Assay.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Casamino_Acids_Vitamin_Assay.yaml`, `just validate-terms data/ingredients/mapped/Casamino_Acids_Vitamin_Assay.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Casamino_Acids_Vitamin_Assay.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Casamino_Acids_Vitamin_Assay.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
