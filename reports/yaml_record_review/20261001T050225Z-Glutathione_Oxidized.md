# YAML Record Review: Glutathione oxidized

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Glutathione_Oxidized.yaml`
- Started UTC: 2026-10-01T05:02:25Z
- Finished UTC: 2026-10-01T05:02:26Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Glutathione_Oxidized.yaml`
- Identifier: `CHEBI:17858`
- Preferred term: Glutathione oxidized
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Glutathione_Oxidized.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:17858`.
- Ontology label: `glutathione disulfide`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Glutathione_Oxidized.md` after the record changed from 10eeb8853420eda024dd2160b11e9fea95320d3feda6674526d9afd7d102b0fd to 237c2672c76699d883cb59b13b6e7a34693ff6a21dcaf55a2e5764fb9d53d0c5; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `237c2672c76699d883cb59b13b6e7a34693ff6a21dcaf55a2e5764fb9d53d0c5`.
- Previous review: `reports/yaml_record_review/Glutathione_Oxidized.md`.
- Previous record SHA-256: `10eeb8853420eda024dd2160b11e9fea95320d3feda6674526d9afd7d102b0fd`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: REJECTED_TRAIT_SYNONYMS by claude at 2026-09-22T06:14:49.563933+00:00: Retyped activity/assay phrases as provenance-only REJECTED_LABEL because they describe a process or organism trait, not an ingredient name (#703): 'reduction: glutathione oxidized'. Preserved original text and source metadata. No identity, mapping, role, or remaining-synonym claim was adjudicated.
- Active SSSOM state: 1 active row(s) for `MIM:Glutathione_Oxidized`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Glutathione_Oxidized.md` after the record changed from 10eeb8853420eda024dd2160b11e9fea95320d3feda6674526d9afd7d102b0fd to 237c2672c76699d883cb59b13b6e7a34693ff6a21dcaf55a2e5764fb9d53d0c5; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Glutathione_Oxidized.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The exact oxidized-glutathione identity passes, but final SSSOM exports process text in other.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Glutathione_Oxidized.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Glutathione_Oxidized.yaml`, `just validate-terms data/ingredients/mapped/Glutathione_Oxidized.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Glutathione_Oxidized.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Glutathione_Oxidized.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
