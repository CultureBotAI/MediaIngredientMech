# YAML Record Review: ammonium molybdate tetrahydrate

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Ammonium_Molybdate_Tetrahydrate.yaml`
- Started UTC: 2026-10-01T05:01:19Z
- Finished UTC: 2026-10-01T05:01:20Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Ammonium_Molybdate_Tetrahydrate.yaml`
- Identifier: `CHEBI:86244`
- Preferred term: ammonium molybdate tetrahydrate
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Ammonium_Molybdate_Tetrahydrate.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:86244`.
- Ontology label: `hexaammonium heptamolybdate tetrahydrate`.
- Mapping quality: `SYNONYM_MATCH`.
- Active SSSOM rows for this subject: 2.
- Identity judgement: Refreshed `reports/yaml_record_review/Ammonium_Molybdate_Tetrahydrate.md` after the record changed from ca53eb1f057f8e1ee877edeb4f05e232b10b47b3512d969b5711a525f4305ddd to 8aa0782e111cd434c6337345cfe51234abda0233d56857fd7a34c75a5636bf15; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `8aa0782e111cd434c6337345cfe51234abda0233d56857fd7a34c75a5636bf15`.
- Previous review: `reports/yaml_record_review/Ammonium_Molybdate_Tetrahydrate.md`.
- Previous record SHA-256: `ca53eb1f057f8e1ee877edeb4f05e232b10b47b3512d969b5711a525f4305ddd`.
- Source occurrence traceability: 12 occurrence(s) across 12 medium/media.
- Latest curation event: REGROUNDED_IDENTITY by claude at 2026-09-23T00:44:54.421176+00:00: identifier cas:12054-85-2 -> CHEBI:86244; ontology CHEBI:91249 ('ammonium molybdate') -> CHEBI:86244 ('hexaammonium heptamolybdate tetrahydrate'); mapping_quality CLOSE_MATCH -> SYNONYM_MATCH. The record (H32Mo7N6O28, CAS 12054-85-2) is the heptamolybdate; CHEBI:91249 'ammonium molybdate' is the diammonium orthomolybdate (2H4N.MoO4, one Mo), a different polyanion, not the anhydrous parent of this hydrate. ChEBI has the substance: CHEBI:86244 'hexaammonium heptamolybdate tetrahydrate' (4H2O.6H4N.Mo7O24) carries the related synonym 'ammonium molybdate tetrahydrate', the record's exact label, on no other term. Section 3 step 1 with a unique synonym: SYNONYM_MATCH. The CAS stays on its registry row. (#312) Synonyms added: ammonium heptamolybdate tetrahydrate, ammonium paramolybdate tetrahydrate.
- Active SSSOM state: 2 active row(s) for `MIM:Ammonium_Molybdate_Tetrahydrate`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Ammonium_Molybdate_Tetrahydrate.md` after the record changed from ca53eb1f057f8e1ee877edeb4f05e232b10b47b3512d969b5711a525f4305ddd to 8aa0782e111cd434c6337345cfe51234abda0233d56857fd7a34c75a5636bf15; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Ammonium_Molybdate_Tetrahydrate.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The CAS tetrahydrate identity, close anhydrous parent, exact CAS SSSOM row, 12 memberships, and hydrate regrade pass, but an anhydrous-parent synonym is exact and the trace-element role remains provisional.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Ammonium_Molybdate_Tetrahydrate.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Ammonium_Molybdate_Tetrahydrate.yaml`, `just validate-terms data/ingredients/mapped/Ammonium_Molybdate_Tetrahydrate.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Ammonium_Molybdate_Tetrahydrate.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Ammonium_Molybdate_Tetrahydrate.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
