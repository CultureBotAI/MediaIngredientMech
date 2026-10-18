# YAML Record Review: 2-oxobutyric acid sodium salt

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/2-oxobutyric_Acid_Sodium_Salt.yaml`
- Started UTC: 2026-10-01T04:59:03Z
- Finished UTC: 2026-10-01T04:59:04Z
- Verdict: pass_with_minor_issues

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/2-oxobutyric_Acid_Sodium_Salt.yaml`
- Identifier: `cas:2013-26-5`
- Preferred term: 2-oxobutyric acid sodium salt
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/2-oxobutyric_Acid_Sodium_Salt.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:30831`.
- Ontology label: `2-oxobutanoic acid`.
- Mapping quality: `NARROW_MATCH`.
- Active SSSOM rows for this subject: 3.
- Identity judgement: Refreshed `reports/yaml_record_review/2-oxobutyric_Acid_Sodium_Salt.md` after the record changed from 29c226a36ff7126b5b2e97a0c1837dbb4c92c4cc209603765a3a9a66b057485b to 0502ce13109f88ded61ed70501531d0820adc2ab56b8ba6b470c6070f3b8f17d; preserved the previous minor finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `0502ce13109f88ded61ed70501531d0820adc2ab56b8ba6b470c6070f3b8f17d`.
- Previous review: `reports/yaml_record_review/2-oxobutyric_Acid_Sodium_Salt.md`.
- Previous record SHA-256: `29c226a36ff7126b5b2e97a0c1837dbb4c92c4cc209603765a3a9a66b057485b`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: REGROUNDED_PARENT_TERM by claude at 2026-09-22T23:25:51.023682+00:00: broadMatch parent CHEBI:16763 ('2-oxobutanoate') -> CHEBI:30831 ('2-oxobutanoic acid') (#312). Section 3: for a salt the broadMatch parent follows the label, and '...Acid sodium salt' names the acid. The #322 note said ChEBI has no '2-oxobutanoic acid' term; it does: CHEBI:30831, xref cas:600-18-0, synonym '2-Oxobutyric acid'. The anion CHEBI:16763 was the fallback for a false premise. cas: identity unchanged.
- Active SSSOM state: 3 active row(s) for `MIM:2-oxobutyric_Acid_Sodium_Salt`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: None found.

## Findings

- **minor**: The previous finding set in `reports/yaml_record_review/2-oxobutyric_Acid_Sodium_Salt.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: CAS salt identity and narrow CHEBI:16763 parent mapping pass after the generic sodium-salt repair; only optional salt chemistry enrichment and stale advisory rows remain.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/2-oxobutyric_Acid_Sodium_Salt.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/2-oxobutyric_Acid_Sodium_Salt.yaml`, `just validate-terms data/ingredients/mapped/2-oxobutyric_Acid_Sodium_Salt.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/2-oxobutyric_Acid_Sodium_Salt.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/2-oxobutyric_Acid_Sodium_Salt.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
