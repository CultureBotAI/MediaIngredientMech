# YAML Record Review: L-Aspartic acid sodium salt monohydrate

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml`
- Started UTC: 2026-10-01T05:02:34Z
- Finished UTC: 2026-10-01T05:02:35Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml`
- Identifier: `cas:323194-76-9`
- Preferred term: L-Aspartic acid sodium salt monohydrate
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:17053`.
- Ontology label: `L-aspartic acid`.
- Mapping quality: `CLOSE_MATCH`.
- Active SSSOM rows for this subject: 2.
- Identity judgement: Refreshed `reports/yaml_record_review/L-Aspartic_Acid_Sodium_Salt_Monohydrate.md` after the record changed from 2adc6833819d70d555e0573db31372d89bac15511a6d6f3c994297304808579e to b08b501b65a3b83edd2af58a9c3818b3f998c3c2e382458d6af07dae5a6cb0aa; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `b08b501b65a3b83edd2af58a9c3818b3f998c3c2e382458d6af07dae5a6cb0aa`.
- Previous review: `reports/yaml_record_review/L-Aspartic_Acid_Sodium_Salt_Monohydrate.md`.
- Previous record SHA-256: `2adc6833819d70d555e0573db31372d89bac15511a6d6f3c994297304808579e`.
- Source occurrence traceability: 2 occurrence(s) across 2 medium/media.
- Latest curation event: REJECTED_PARENT_NAME_SYNONYMS by claude at 2026-09-22T20:41:14.285965+00:00: Retyped names of the parent compound or of a different hydrate as provenance-only REJECTED_LABEL, because this record is a distinct salt, hydrate or tombstone form and the label index resolved the parent's name here (#232): '(2S)-2-aminobutanedioic acid'; 'ASPARTIC ACID'. Preserved original text and source metadata. No identity, mapping, role, or remaining-synonym claim was adjudicated.
- Active SSSOM state: 2 active row(s) for `MIM:L-Aspartic_Acid_Sodium_Salt_Monohydrate`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/L-Aspartic_Acid_Sodium_Salt_Monohydrate.md` after the record changed from 2adc6833819d70d555e0573db31372d89bac15511a6d6f3c994297304808579e to b08b501b65a3b83edd2af58a9c3818b3f998c3c2e382458d6af07dae5a6cb0aa; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/L-Aspartic_Acid_Sodium_Salt_Monohydrate.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The CAS primary identity, sodium-salt monohydrate structure, close parent mapping, exact CAS row, and hydrate review pass, but the local registry anchor is missing, parent synonyms publish, and AMINO_ACID_SOURCE is provisional.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/L-Aspartic_Acid_Sodium_Salt_Monohydrate.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml`, `just validate-terms data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
