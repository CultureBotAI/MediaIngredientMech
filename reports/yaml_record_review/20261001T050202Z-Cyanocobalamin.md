# YAML Record Review: Cyanocobalamin

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Cyanocobalamin.yaml`
- Started UTC: 2026-10-01T05:02:02Z
- Finished UTC: 2026-10-01T05:02:03Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Cyanocobalamin.yaml`
- Identifier: `CHEBI:17439`
- Preferred term: Cyanocobalamin
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Cyanocobalamin.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:17439`.
- Ontology label: `cyanocob(III)alamin`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Cyanocobalamin.md` after the record changed from e027bb18ec8466c3cad95ffcf6fde523a3b57d3bec17635601085224f9403b1d to c5040ab3a4bc376296676ced54da7265cce36b34c573668be6e28592161d260c; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `c5040ab3a4bc376296676ced54da7265cce36b34c573668be6e28592161d260c`.
- Previous review: `reports/yaml_record_review/Cyanocobalamin.md`.
- Previous record SHA-256: `e027bb18ec8466c3cad95ffcf6fde523a3b57d3bec17635601085224f9403b1d`.
- Source occurrence traceability: 275 occurrence(s) across 265 medium/media.
- Latest curation event: REJECTED_WRONG_SUBSTANCE_SYNONYMS by claude at 2026-09-24T07:48:22.735873+00:00: Retyped REJECTED_LABEL: 'Vitamin B12' (EXACT): ChEBI assigns 'vitamin B12' to CHEBI:176843, the class record, not to cyanocobalamin CHEBI:17439 (#669). Kept as provenance only; it must not resolve, be exported, or enter the SSSOM other column.
- Active SSSOM state: 1 active row(s) for `MIM:Cyanocobalamin`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Cyanocobalamin.md` after the record changed from e027bb18ec8466c3cad95ffcf6fde523a3b57d3bec17635601085224f9403b1d to c5040ab3a4bc376296676ced54da7265cce36b34c573668be6e28592161d260c; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Cyanocobalamin.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The exact CHEBI cyanocobalamin identity, structure, count, and role pass, but final SSSOM still exports B12 OCR fragments and broader vitamer labels.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Cyanocobalamin.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Cyanocobalamin.yaml`, `just validate-terms data/ingredients/mapped/Cyanocobalamin.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Cyanocobalamin.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Cyanocobalamin.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
