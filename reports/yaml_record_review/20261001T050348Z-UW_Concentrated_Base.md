# YAML Record Review: UW concentrated base

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/UW_Concentrated_Base.yaml`
- Started UTC: 2026-10-01T05:03:48Z
- Finished UTC: 2026-10-01T05:03:49Z
- Verdict: pass

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/UW_Concentrated_Base.yaml`
- Identifier: `kgmicrobe.ingredient:uw_concentrated_base`
- Preferred term: UW concentrated base
- Mapping status: `MAPPED`
- Ingredient type: `STOCK_SOLUTION`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/UW_Concentrated_Base.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `kgmicrobe.ingredient:uw_concentrated_base`.
- Ontology label: `UW concentrated base`.
- Mapping quality: `FALLBACK_REGISTRY`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/UW_Concentrated_Base.md` after the record changed from b455758691d8f1ec6e5c6303502ed582461925a43b211ee5eb12eaa0590f3931 to e676b9237eadf613f04db4121c47cf5b273cf3e8322c1f01e367b9eb5d83b427; no prior finding is carried forward.

## Evidence

- Current record SHA-256: `e676b9237eadf613f04db4121c47cf5b273cf3e8322c1f01e367b9eb5d83b427`.
- Previous review: `reports/yaml_record_review/UW_Concentrated_Base.md`.
- Previous record SHA-256: `b455758691d8f1ec6e5c6303502ed582461925a43b211ee5eb12eaa0590f3931`.
- Source occurrence traceability: 9 occurrence(s) across 9 medium/media.
- Latest curation event: RESCOPED_COMPONENT by claude at 2026-09-23T01:09:00.338823+00:00: components[3] 'ammonium molybdate tetrahydrate' component_id cas:12054-85-2 -> CHEBI:86244: the referenced MIM record was re-grounded (#312); the part identity and amount are unchanged.
- Active SSSOM state: 1 active row(s) for `MIM:UW_Concentrated_Base`.
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

- Re-run strict schema validation on `data/ingredients/mapped/UW_Concentrated_Base.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/UW_Concentrated_Base.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
