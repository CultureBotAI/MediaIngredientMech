# YAML Record Review: Hydroxystreptomycin

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Hydroxystreptomycin.yaml`
- Started UTC: 2026-10-01T05:02:29Z
- Finished UTC: 2026-10-01T05:02:30Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Hydroxystreptomycin.yaml`
- Identifier: `CHEBI:24750`
- Preferred term: Hydroxystreptomycin
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Hydroxystreptomycin.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:24750`.
- Ontology label: `5'-hydroxystreptomycin`.
- Mapping quality: `SYNONYM_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Hydroxystreptomycin.md` after the record changed from df30dff42d82b226e7fbc8833f2728c70b6d40166f3a408b5d06c632e5857dc3 to 0f2e4d1c8968e7a23945f91ad68545c464cf3867b79f2e9ce26f9a1311e40179; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `0f2e4d1c8968e7a23945f91ad68545c464cf3867b79f2e9ce26f9a1311e40179`.
- Previous review: `reports/yaml_record_review/Hydroxystreptomycin.md`.
- Previous record SHA-256: `df30dff42d82b226e7fbc8833f2728c70b6d40166f3a408b5d06c632e5857dc3`.
- Source occurrence traceability: 0 active occurrence(s) across 0 medium/media; source rows: microbedecoder: 1.
- Latest curation event: REGRADED_MAPPING_QUALITY by claude at 2026-09-22T23:25:50.998756+00:00: mapping_quality CLOSE_MATCH -> SYNONYM_MATCH (#312). 'Hydroxystreptomycin' is a verbatim ChEBI related synonym of CHEBI:24750 and of no other term, and the term carries xref cas:6835-00-3. The earlier CLOSE_MATCH note ('the term names the position and the label does not') understated a unique synonym resolution, which Section 0 grades SYNONYM_MATCH. Identifier unchanged.
- Active SSSOM state: 1 active row(s) for `MIM:Hydroxystreptomycin`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Hydroxystreptomycin.md` after the record changed from df30dff42d82b226e7fbc8833f2728c70b6d40166f3a408b5d06c632e5857dc3 to 0f2e4d1c8968e7a23945f91ad68545c464cf3867b79f2e9ce26f9a1311e40179; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Hydroxystreptomycin.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The CHEBI:24750 target is graded as close but also used as the primary identifier, forcing an exact own-identifier SSSOM row.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Hydroxystreptomycin.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Hydroxystreptomycin.yaml`, `just validate-terms data/ingredients/mapped/Hydroxystreptomycin.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Hydroxystreptomycin.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Hydroxystreptomycin.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
