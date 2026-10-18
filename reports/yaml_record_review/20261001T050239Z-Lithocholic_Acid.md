# YAML Record Review: Lithocholic acid

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Lithocholic_Acid.yaml`
- Started UTC: 2026-10-01T05:02:39Z
- Finished UTC: 2026-10-01T05:02:40Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Lithocholic_Acid.yaml`
- Identifier: `CHEBI:16325`
- Preferred term: Lithocholic acid
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Lithocholic_Acid.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:16325`.
- Ontology label: `lithocholic acid`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Lithocholic_Acid.md` after the record changed from ba2c2f990be8c59549f721b580dedc5cfbd74891e818264f4fe17667a33dece3 to 1903f7d9517c2c068dbb76387fd4efcd1c497d76da7d1dd4c9a82639879d92f2; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `1903f7d9517c2c068dbb76387fd4efcd1c497d76da7d1dd4c9a82639879d92f2`.
- Previous review: `reports/yaml_record_review/Lithocholic_Acid.md`.
- Previous record SHA-256: `ba2c2f990be8c59549f721b580dedc5cfbd74891e818264f4fe17667a33dece3`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: CORRECTED by retire_wrong_compound_synonyms at 2026-09-20T00:00:00Z: Marked 1 synonym(s) non-resolving: ['berbaman']. ChEBI gives these names to CHEBI:35920, not to this record's CHEBI:16325 -- lithocholic acid is not berbaman. Kept as REJECTED_LABEL so a rebuild cannot restore them from kg-microbe's synonym list (#669).
- Active SSSOM state: 1 active row(s) for `MIM:Lithocholic_Acid`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Lithocholic_Acid.md` after the record changed from ba2c2f990be8c59549f721b580dedc5cfbd74891e818264f4fe17667a33dece3 to 1903f7d9517c2c068dbb76387fd4efcd1c497d76da7d1dd4c9a82639879d92f2; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Lithocholic_Acid.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The CHEBI:16325 identity, CAS value, PubChem structure, and real ChEBI synonym pass, but Tricine and berbaman labels are exported as final SSSOM synonyms.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Lithocholic_Acid.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Lithocholic_Acid.yaml`, `just validate-terms data/ingredients/mapped/Lithocholic_Acid.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Lithocholic_Acid.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Lithocholic_Acid.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
