# YAML Record Review: UW concentrated base no sulfur

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/UW_Concentrated_Base_No_Sulfur.yaml`
- Started UTC: 2026-10-01T05:03:49Z
- Finished UTC: 2026-10-01T05:03:50Z
- Verdict: pass

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/UW_Concentrated_Base_No_Sulfur.yaml`
- Identifier: `kgmicrobe.ingredient:uw_concentrated_base_no_sulfur`
- Preferred term: UW concentrated base no sulfur
- Mapping status: `MAPPED`
- Ingredient type: `STOCK_SOLUTION`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/UW_Concentrated_Base_No_Sulfur.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `kgmicrobe.ingredient:uw_concentrated_base_no_sulfur`.
- Ontology label: `UW concentrated base no sulfur`.
- Mapping quality: `FALLBACK_REGISTRY`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/UW_Concentrated_Base_No_Sulfur.md` after the record changed from 8e21f39d0f744ddf42c91a05ff234c29167bec026d599e41b7cfd8b02c04f6d7 to ab68055139180f35162d25ad6f43160fbad7e09838d653419b10967c3558a28f; no prior finding is carried forward.

## Evidence

- Current record SHA-256: `ab68055139180f35162d25ad6f43160fbad7e09838d653419b10967c3558a28f`.
- Previous review: `reports/yaml_record_review/UW_Concentrated_Base_No_Sulfur.md`.
- Previous record SHA-256: `8e21f39d0f744ddf42c91a05ff234c29167bec026d599e41b7cfd8b02c04f6d7`.
- Source occurrence traceability: 1 occurrence(s) across 1 medium/media.
- Latest curation event: RESCOPED_COMPONENT by claude at 2026-09-23T01:09:00.614023+00:00: components[3] 'ammonium molybdate tetrahydrate' component_id cas:12054-85-2 -> CHEBI:86244: the referenced MIM record was re-grounded (#312); the part identity and amount are unchanged.
- Active SSSOM state: 1 active row(s) for `MIM:UW_Concentrated_Base_No_Sulfur`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: None found.

## Findings

None found.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/UW_Concentrated_Base_No_Sulfur.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/UW_Concentrated_Base_No_Sulfur.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
