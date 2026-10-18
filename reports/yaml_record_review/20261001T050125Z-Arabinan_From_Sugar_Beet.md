# YAML Record Review: Arabinan from Sugar Beet

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Arabinan_From_Sugar_Beet.yaml`
- Started UTC: 2026-10-01T05:01:25Z
- Finished UTC: 2026-10-01T05:01:26Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Arabinan_From_Sugar_Beet.yaml`
- Identifier: `cas:11078-27-6`
- Preferred term: Arabinan from Sugar Beet
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Arabinan_From_Sugar_Beet.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:22590`.
- Ontology label: `arabinan`.
- Mapping quality: `NARROW_MATCH`.
- Active SSSOM rows for this subject: 3.
- Identity judgement: Refreshed `reports/yaml_record_review/Arabinan_From_Sugar_Beet.md` after the record changed from 19a9fd51cb7035f164d0f9595afaeb54b049a41abe00dc8d50452203897b56c1 to 0f7efcf2d026ed5ad88d0b062e4cb3553a2a4b3eb44ffc9c1f5ce1d1c1e42aa2; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `0f7efcf2d026ed5ad88d0b062e4cb3553a2a4b3eb44ffc9c1f5ce1d1c1e42aa2`.
- Previous review: `reports/yaml_record_review/Arabinan_From_Sugar_Beet.md`.
- Previous record SHA-256: `19a9fd51cb7035f164d0f9595afaeb54b049a41abe00dc8d50452203897b56c1`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: REGROUNDED_PARENT_TERM by claude at 2026-09-22T23:25:51.045781+00:00: broadMatch parent FOODON:00003412 ('sugar beet') -> CHEBI:22590 ('arabinan') (#312). FOODON:00003412 'sugar beet' is the source organ the stem-substring matcher took from the trailing qualifier; a polysaccharide is not a kind of a root. The head noun is arabinan, CHEBI:22590, the closest broader term (the botanical source stays in the preferred_term). cas:11078-27-6 identity, NARROW_MATCH grade and both registry rows unchanged (Section 3 step 2, #245).
- Active SSSOM state: 3 active row(s) for `MIM:Arabinan_From_Sugar_Beet`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Arabinan_From_Sugar_Beet.md` after the record changed from 19a9fd51cb7035f164d0f9595afaeb54b049a41abe00dc8d50452203897b56c1 to 0f7efcf2d026ed5ad88d0b062e4cb3553a2a4b3eb44ffc9c1f5ce1d1c1e42aa2; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Arabinan_From_Sugar_Beet.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The CAS fallback rows are synchronized, but the FoodOn parent denotes the sugar-beet root rather than arabinan extracted from sugar beet.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Arabinan_From_Sugar_Beet.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Arabinan_From_Sugar_Beet.yaml`, `just validate-terms data/ingredients/mapped/Arabinan_From_Sugar_Beet.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Arabinan_From_Sugar_Beet.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Arabinan_From_Sugar_Beet.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
