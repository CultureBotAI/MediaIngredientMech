# YAML Record Review: Casein peptone

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Casein_Peptone.yaml`
- Started UTC: 2026-10-01T05:01:45Z
- Finished UTC: 2026-10-01T05:01:46Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Casein_Peptone.yaml`
- Identifier: `FOODON:03315719`
- Preferred term: Casein peptone
- Mapping status: `MAPPED`
- Ingredient type: `UNDEFINED_MIXTURE`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Casein_Peptone.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `FOODON:03315719`.
- Ontology label: `mammalian milk protein (hydrolyzed)`.
- Mapping quality: `CLOSE_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Casein_Peptone.md` after the record changed from fb7511438af2b5a01352f441376690282c1f399a40ed5bc9de564dbe3c929724 to 6c8f30e9340d2df5b8477791831810db38cdf6a03df96643304e43f1e2157a64; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `6c8f30e9340d2df5b8477791831810db38cdf6a03df96643304e43f1e2157a64`.
- Previous review: `reports/yaml_record_review/Casein_Peptone.md`.
- Previous record SHA-256: `fb7511438af2b5a01352f441376690282c1f399a40ed5bc9de564dbe3c929724`.
- Source occurrence traceability: 1313 occurrence(s) across 1247 medium/media.
- Latest curation event: REJECTED_WRONG_SUBSTANCE_SYNONYMS by claude at 2026-09-24T07:48:22.676543+00:00: Retyped REJECTED_LABEL: 'Casein hydrolysate' (EXACT_SYNONYM): the acid hydrolysate product has its own record (Casein_hydrolysate, MICRO:0001366) (#669). Kept as provenance only; it must not resolve, be exported, or enter the SSSOM other column.
- Active SSSOM state: 1 active row(s) for `MIM:Casein_Peptone`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Casein_Peptone.md` after the record changed from fb7511438af2b5a01352f441376690282c1f399a40ed5bc9de564dbe3c929724 to 6c8f30e9340d2df5b8477791831810db38cdf6a03df96643304e43f1e2157a64; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Casein_Peptone.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The FoodOn casein-peptone parent grounding passes, but PROTEIN_SOURCE is only a provisional name-pattern prediction.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Casein_Peptone.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Casein_Peptone.yaml`, `just validate-terms data/ingredients/mapped/Casein_Peptone.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Casein_Peptone.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Casein_Peptone.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
