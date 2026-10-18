# YAML Record Review: Calcium Chloride

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Calcium_Chloride.yaml`
- Started UTC: 2026-10-01T05:01:42Z
- Finished UTC: 2026-10-01T05:01:43Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Calcium_Chloride.yaml`
- Identifier: `CHEBI:3312`
- Preferred term: Calcium Chloride
- Mapping status: `REJECTED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Calcium_Chloride.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `REJECTED`.
- Ontology ID: `CHEBI:3312`.
- Ontology label: `calcium dichloride`.
- Mapping quality: `SYNONYM_MATCH`.
- Active SSSOM rows for this subject: 0.
- Identity judgement: Refreshed `reports/yaml_record_review/Calcium_Chloride.md` after the record changed from c26d211d61d5df94a3e6c9f282b16dd84c0f060473aeb4ec40f742dfad86d079 to 9c8d517e9746cd4a01454b479be86eaaeee67623a3ae162a93557978df1a4742; preserved the previous minor finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `9c8d517e9746cd4a01454b479be86eaaeee67623a3ae162a93557978df1a4742`.
- Previous review: `reports/yaml_record_review/Calcium_Chloride.md`.
- Previous record SHA-256: `c26d211d61d5df94a3e6c9f282b16dd84c0f060473aeb4ec40f742dfad86d079`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: REJECTED_WRONG_FORM_SYNONYMS by claude at 2026-09-23T06:21:57.501233+00:00: Retyped REJECTED_LABEL: 'CaCl2 × 2 H2O' (HYDRATE_FORM), 'CaCl2*2H2O' (HYDRATE_FORM): dihydrate labels on the anhydrous CHEBI:3312 tombstone; the dihydrate is Cacl2_X_2_H2o (#232). The token is kept as provenance only; it must not resolve, be exported, or enter the SSSOM other column.
- Active SSSOM state: No active row for `MIM:Calcium_Chloride`, as expected for `REJECTED`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Calcium_Chloride.md` after the record changed from c26d211d61d5df94a3e6c9f282b16dd84c0f060473aeb4ec40f742dfad86d079 to 9c8d517e9746cd4a01454b479be86eaaeee67623a3ae162a93557978df1a4742; preserved the previous minor finding floor pending targeted retirement.

## Findings

- **minor**: The previous finding set in `reports/yaml_record_review/Calcium_Chloride.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The rejected anhydrous calcium chloride duplicate is unpublished in SSSOM, but old hydrate synonyms, chemistry, and role fields remain.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Calcium_Chloride.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Calcium_Chloride.yaml`, `just validate-terms data/ingredients/mapped/Calcium_Chloride.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Calcium_Chloride.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Calcium_Chloride.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
