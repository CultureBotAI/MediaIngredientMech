# YAML Record Review: Algal Trace Elements Solution

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml`
- Started UTC: 2026-10-01T05:01:17Z
- Finished UTC: 2026-10-01T05:01:18Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml`
- Identifier: `kgmicrobe.ingredient:algal_trace_elements_solution`
- Preferred term: Algal Trace Elements Solution
- Mapping status: `MAPPED`
- Ingredient type: `STOCK_SOLUTION`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `MICRO:0000455`.
- Ontology label: `trace elements solution`.
- Mapping quality: `NARROW_MATCH`.
- Active SSSOM rows for this subject: 2.
- Identity judgement: Refreshed `reports/yaml_record_review/Algal_Trace_Elements_Solution.md` after the record changed from 3f3ae6752048a4120c5c2accff72118a4a546bd2d1bdb1e675be4415b8a9ffbc to 44d6579cade933d4544f51f7aadd20aef899337b28b5d55d50f8f07d47897d0f; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `44d6579cade933d4544f51f7aadd20aef899337b28b5d55d50f8f07d47897d0f`.
- Previous review: `reports/yaml_record_review/Algal_Trace_Elements_Solution.md`.
- Previous record SHA-256: `3f3ae6752048a4120c5c2accff72118a4a546bd2d1bdb1e675be4415b8a9ffbc`.
- Source occurrence traceability: 1 occurrence(s) across 1 medium/media.
- Latest curation event: MINTED_REGISTRY_IDENTIFIER by claude at 2026-09-23T03:41:22.513892+00:00: identifier MICRO:0000455 -> kgmicrobe.ingredient:algal_trace_elements_solution; ontology MICRO:0000455 ('trace elements solution') -> MICRO:0000455 ('trace elements solution'); mapping_quality LEXICAL_MATCH -> NARROW_MATCH. MICRO:0000455 'trace elements solution' is a class ('a solution of trace elements ..., sometimes also having an organic chelator'), and two MIM records held it as their identifier (this one and WC Trace Elements Solution): two different recipes collapsed onto one node. This is the UTEX algal trace-element recipe, a specific formulation. Section 3 step 3: mint a registry identity, broadMatch to the class, the Proteose_Peptone_No_2 shape. (#312)
- Active SSSOM state: 2 active row(s) for `MIM:Algal_Trace_Elements_Solution`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Algal_Trace_Elements_Solution.md` after the record changed from 3f3ae6752048a4120c5c2accff72118a4a546bd2d1bdb1e675be4415b8a9ffbc to 44d6579cade933d4544f51f7aadd20aef899337b28b5d55d50f8f07d47897d0f; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Algal_Trace_Elements_Solution.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The MICRO term resolves, but Algal and WC trace-elements solutions share the same generic MICRO:0000455 exact identity and this stock solution needs its own exact ID and components.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Algal_Trace_Elements_Solution.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml`, `just validate-terms data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
