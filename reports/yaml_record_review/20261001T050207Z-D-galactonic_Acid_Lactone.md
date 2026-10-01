# YAML Record Review: D-galactonic Acid Lactone

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/D-galactonic_Acid_Lactone.yaml`
- Started UTC: 2026-10-01T05:02:07Z
- Finished UTC: 2026-10-01T05:02:08Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/D-galactonic_Acid_Lactone.yaml`
- Identifier: `CHEBI:15895`
- Preferred term: D-galactonic Acid Lactone
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/D-galactonic_Acid_Lactone.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:15895`.
- Ontology label: `D-galactono-1,4-lactone`.
- Mapping quality: `CLOSE_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/D-galactonic_Acid_Lactone.md` after the record changed from 0fa355ac400aef25629c958b9f0f73ac10d8219a8a457db63620cbd5cb7c16ae to 08c156a1b6463282970f4015e75189c91e108034f1e24477b54ae3b4199e80d6; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `08c156a1b6463282970f4015e75189c91e108034f1e24477b54ae3b4199e80d6`.
- Previous review: `reports/yaml_record_review/D-galactonic_Acid_Lactone.md`.
- Previous record SHA-256: `0fa355ac400aef25629c958b9f0f73ac10d8219a8a457db63620cbd5cb7c16ae`.
- Source occurrence traceability: 0 active occurrence(s) across 0 medium/media; source rows: microbedecoder: 21.
- Latest curation event: REGRADED_MAPPING_QUALITY by claude at 2026-09-22T23:25:50.992216+00:00: mapping_quality SYNONYM_MATCH -> CLOSE_MATCH (#312). 'D-galactonic Acid Lactone' is not a label or synonym of any ChEBI term: every name on CHEBI:15895 states gamma or 1,4, and the bare 'D-Galactonolactone' is a synonym of the 1,5-lactone CHEBI:15945. The ring size was supplied from outside ChEBI (the Biolog substrate is the gamma-lactone), so the grade is CLOSE_MATCH per Section 0. Identifier unchanged; the own-identifier row stays skos:exactMatch (Rule D).
- Active SSSOM state: 1 active row(s) for `MIM:D-galactonic_Acid_Lactone`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/D-galactonic_Acid_Lactone.md` after the record changed from 0fa355ac400aef25629c958b9f0f73ac10d8219a8a457db63620cbd5cb7c16ae to 08c156a1b6463282970f4015e75189c91e108034f1e24477b54ae3b4199e80d6; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/D-galactonic_Acid_Lactone.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The CHEBI target is active and structurally consistent, but the source label omits the gamma/1,4 specificity needed for a confident exactMatch to CHEBI:15895.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/D-galactonic_Acid_Lactone.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/D-galactonic_Acid_Lactone.yaml`, `just validate-terms data/ingredients/mapped/D-galactonic_Acid_Lactone.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/D-galactonic_Acid_Lactone.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/D-galactonic_Acid_Lactone.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
