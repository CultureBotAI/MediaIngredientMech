# YAML Record Review: 3-O-methylgallate

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/3-O-methylgallate.yaml`
- Started UTC: 2026-10-01T04:59:04Z
- Finished UTC: 2026-10-01T04:59:05Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/3-O-methylgallate.yaml`
- Identifier: `CHEBI:28647`
- Preferred term: 3-O-methylgallate
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/3-O-methylgallate.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:28647`.
- Ontology label: `3-O-methylgallic acid`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/3-O-methylgallate.md` after the record changed from d19390c1755ee7bfe2f0d42ac31f6493f5d97a7f0e211579f172acc3809393ec to 93f4f492afefcea318cfcd7c5eb1407c5713e4576ca675ae50a6838720a4f094; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `93f4f492afefcea318cfcd7c5eb1407c5713e4576ca675ae50a6838720a4f094`.
- Previous review: `reports/yaml_record_review/3-O-methylgallate.md`.
- Previous record SHA-256: `d19390c1755ee7bfe2f0d42ac31f6493f5d97a7f0e211579f172acc3809393ec`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: REJECTED_TRAIT_SYNONYMS by claude at 2026-09-22T06:14:49.563933+00:00: Retyped activity/assay phrases as provenance-only REJECTED_LABEL because they describe a process or organism trait, not an ingredient name (#703): 'reduction: 3-O-methylgallate'. Preserved original text and source metadata. No identity, mapping, role, or remaining-synonym claim was adjudicated.
- Active SSSOM state: 1 active row(s) for `MIM:3-O-methylgallate`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/3-O-methylgallate.md` after the record changed from d19390c1755ee7bfe2f0d42ac31f6493f5d97a7f0e211579f172acc3809393ec to 93f4f492afefcea318cfcd7c5eb1407c5713e4576ca675ae50a6838720a4f094; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/3-O-methylgallate.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: Active CHEBI identity and chemistry pass, but non-label source context remains in RAW_TEXT and exports through SSSOM other.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/3-O-methylgallate.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/3-O-methylgallate.yaml`, `just validate-terms data/ingredients/mapped/3-O-methylgallate.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/3-O-methylgallate.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/3-O-methylgallate.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
