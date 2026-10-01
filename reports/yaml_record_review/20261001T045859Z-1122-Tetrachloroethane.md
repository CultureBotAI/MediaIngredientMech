# YAML Record Review: 1,1,2,2-tetrachloroethane

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/1122-Tetrachloroethane.yaml`
- Started UTC: 2026-10-01T04:58:59Z
- Finished UTC: 2026-10-01T04:59:00Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/1122-Tetrachloroethane.yaml`
- Identifier: `CHEBI:36026`
- Preferred term: 1,1,2,2-tetrachloroethane
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/1122-Tetrachloroethane.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:36026`.
- Ontology label: `1,1,2,2-tetrachloroethane`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/1122-Tetrachloroethane.md` after the record changed from b0a7327db273c860ba78aaecb8864949d4579b70186a4b9869845b0425b8938c to 99b1b45739d34c71ab1bf0656fb1ee4d3e67728f350642e70b7b23730e97580e; preserved the previous blocker finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `99b1b45739d34c71ab1bf0656fb1ee4d3e67728f350642e70b7b23730e97580e`.
- Previous review: `reports/yaml_record_review/1122-Tetrachloroethane.md`.
- Previous record SHA-256: `b0a7327db273c860ba78aaecb8864949d4579b70186a4b9869845b0425b8938c`.
- Source occurrence traceability: 0 active occurrence(s) across 0 medium/media; source rows: microbedecoder: 1.
- Latest curation event: RESOLVED_FROM_ORIGINAL_SOURCE by mim_semantic_review_710 at 2026-09-22T02:07:38.917319+00:00: The complete original MicrobeDecoder CSV label is 1,1,2,2-tetrachloroethane, in the sole matching source row (BacDive 140462); the same BacDive record explicitly identifies CHEBI:36026. This replaces unsupported comma-tail inference with original-source disambiguation. Evidence: https://bacdive.dsmz.de/strain/140462 ; https://www.ebi.ac.uk/chebi/CHEBI:36026
- Active SSSOM state: 1 active row(s) for `MIM:1122-Tetrachloroethane`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/1122-Tetrachloroethane.md` after the record changed from b0a7327db273c860ba78aaecb8864949d4579b70186a4b9869845b0425b8938c to 99b1b45739d34c71ab1bf0656fb1ee4d3e67728f350642e70b7b23730e97580e; preserved the previous blocker finding floor pending targeted retirement.

## Findings

- **blocker**: The previous finding set in `reports/yaml_record_review/1122-Tetrachloroethane.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: 2-tetrachloroethane is ambiguous between CHEBI:34024 and CHEBI:36026, but the record publishes an unsupported exact CHEBI:36026 identity.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/1122-Tetrachloroethane.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/1122-Tetrachloroethane.yaml`, `just validate-terms data/ingredients/mapped/1122-Tetrachloroethane.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/1122-Tetrachloroethane.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/1122-Tetrachloroethane.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
