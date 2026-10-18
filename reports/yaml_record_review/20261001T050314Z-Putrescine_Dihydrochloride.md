# YAML Record Review: Putrescine Dihydrochloride

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Putrescine_Dihydrochloride.yaml`
- Started UTC: 2026-10-01T05:03:14Z
- Finished UTC: 2026-10-01T05:03:15Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Putrescine_Dihydrochloride.yaml`
- Identifier: `cas:333-93-7`
- Preferred term: Putrescine Dihydrochloride
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Putrescine_Dihydrochloride.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:201718`.
- Ontology label: `1,4-Diaminobutane dihydrochloride`.
- Mapping quality: `NARROW_MATCH`.
- Active SSSOM rows for this subject: 3.
- Identity judgement: Refreshed `reports/yaml_record_review/Putrescine_Dihydrochloride.md` after the record changed from c791fb8dcdf14d80412a7642afd20b34182707565840de1f38a74995147fd652 to d0afce92c76850d141b4d0aeadc377a217efa26487a5e9966ff2e03298d7c491; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `d0afce92c76850d141b4d0aeadc377a217efa26487a5e9966ff2e03298d7c491`.
- Previous review: `reports/yaml_record_review/Putrescine_Dihydrochloride.md`.
- Previous record SHA-256: `c791fb8dcdf14d80412a7642afd20b34182707565840de1f38a74995147fd652`.
- Source occurrence traceability: 2 occurrence(s) across 2 medium/media.
- Latest curation event: REJECTED_WRONG_SUBSTANCE_SYNONYMS by claude at 2026-09-24T07:48:22.703216+00:00: Retyped REJECTED_LABEL: 'Putrescine' (EXACT_SYNONYM): the free base's name on the dihydrochloride salt (Section 3: salts are not the parent) (#669). Kept as provenance only; it must not resolve, be exported, or enter the SSSOM other column.
- Active SSSOM state: 3 active row(s) for `MIM:Putrescine_Dihydrochloride`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Putrescine_Dihydrochloride.md` after the record changed from c791fb8dcdf14d80412a7642afd20b34182707565840de1f38a74995147fd652 to d0afce92c76850d141b4d0aeadc377a217efa26487a5e9966ff2e03298d7c491; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Putrescine_Dihydrochloride.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: CHEBI:201718 is now an exact salt term and the final SSSOM other field exports the free-base Putrescine label.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Putrescine_Dihydrochloride.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Putrescine_Dihydrochloride.yaml`, `just validate-terms data/ingredients/mapped/Putrescine_Dihydrochloride.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Putrescine_Dihydrochloride.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Putrescine_Dihydrochloride.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
