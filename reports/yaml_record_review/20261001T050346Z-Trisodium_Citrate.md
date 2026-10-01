# YAML Record Review: Trisodium citrate

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Trisodium_Citrate.yaml`
- Started UTC: 2026-10-01T05:03:46Z
- Finished UTC: 2026-10-01T05:03:47Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Trisodium_Citrate.yaml`
- Identifier: `CHEBI:53258`
- Preferred term: Trisodium citrate
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Trisodium_Citrate.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:53258`.
- Ontology label: `sodium citrate`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Trisodium_Citrate.md` after the record changed from 950d213a0b33c9df93652767f8477daf8309a42322e37c14ff3a9a3e3f357ec1 to 18e92ef91df77a9dccc34e47371223f06bde14a937573765f4c0c67ce49e71b9; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `18e92ef91df77a9dccc34e47371223f06bde14a937573765f4c0c67ce49e71b9`.
- Previous review: `reports/yaml_record_review/Trisodium_Citrate.md`.
- Previous record SHA-256: `950d213a0b33c9df93652767f8477daf8309a42322e37c14ff3a9a3e3f357ec1`.
- Source occurrence traceability: 179 occurrence(s) across 179 medium/media.
- Latest curation event: REFRESHED_OCCURRENCE_STATISTICS by claude at 2026-09-24T07:50:13.970481+00:00: occurrence_statistics 182/182 -> 179/179 after the #704 identity split/re-grounding moved recipe memberships.
- Active SSSOM state: 1 active row(s) for `MIM:Trisodium_Citrate`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Trisodium_Citrate.md` after the record changed from 950d213a0b33c9df93652767f8477daf8309a42322e37c14ff3a9a3e3f357ec1 to 18e92ef91df77a9dccc34e47371223f06bde14a937573765f4c0c67ce49e71b9; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Trisodium_Citrate.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The exact anhydrous CHEBI identity passes, but Na2-citrate and Citric Acid are stale merged synonyms that leak into final SSSOM other.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Trisodium_Citrate.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Trisodium_Citrate.yaml`, `just validate-terms data/ingredients/mapped/Trisodium_Citrate.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Trisodium_Citrate.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Trisodium_Citrate.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
