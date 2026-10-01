# YAML Record Review: Anisodamine Hydrobromide

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Anisodamine_Hydrobromide.yaml`
- Started UTC: 2026-10-01T05:01:22Z
- Finished UTC: 2026-10-01T05:01:23Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Anisodamine_Hydrobromide.yaml`
- Identifier: `NCIT:C221850`
- Preferred term: Anisodamine Hydrobromide
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Anisodamine_Hydrobromide.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `NCIT:C221850`.
- Ontology label: `Anisodamine Hydrobromide`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 3.
- Identity judgement: Refreshed `reports/yaml_record_review/Anisodamine_Hydrobromide.md` after the record changed from 999580891233c556fcca8c92336b753e91846ced2b66c105e723159bd71f659c to 04d9d18f7fb88a8f10cad2dbdd8c1acc3738517b90cb6ee14c2e2ddabb07ecf7; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `04d9d18f7fb88a8f10cad2dbdd8c1acc3738517b90cb6ee14c2e2ddabb07ecf7`.
- Previous review: `reports/yaml_record_review/Anisodamine_Hydrobromide.md`.
- Previous record SHA-256: `999580891233c556fcca8c92336b753e91846ced2b66c105e723159bd71f659c`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: REGRADED_PARENT_TO_IDENTITY by claude at 2026-09-23T00:44:54.439691+00:00: identifier cas:17659-49-3 -> NCIT:C221850; ontology NCIT:C221850 ('Anisodamine Hydrobromide') -> NCIT:C221850 ('Anisodamine Hydrobromide'); mapping_quality NARROW_MATCH -> EXACT_MATCH. The label is the hydrobromide; the identifier cas:17659-49-3 is the free base (PubChem CID 2198, C17H23NO4, no bromine), so the published exactMatch asserted identity between a salt and its free base. NCIT:C221850 has the label 'Anisodamine Hydrobromide' exactly, once the empty '()' ingest artefact is stripped from the record's label (kept as RAW_TEXT). Section 3 step 1: the NCIT term is the identifier, EXACT_MATCH. The salt's CAS is 55449-49-5 (PubChem CID 118856046, C17H24BrNO4); the free-base InChI/SMILES are dropped and 17659-49-3 is recorded in the note as the upstream free-base CAS, not as identity. (#312) preferred_term 'Anisodamine Hydrobromide ()' -> 'Anisodamine Hydrobromide'; the raw string is kept as RAW_TEXT.
- Active SSSOM state: 3 active row(s) for `MIM:Anisodamine_Hydrobromide`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Anisodamine_Hydrobromide.md` after the record changed from 999580891233c556fcca8c92336b753e91846ced2b66c105e723159bd71f659c to 04d9d18f7fb88a8f10cad2dbdd8c1acc3738517b90cb6ee14c2e2ddabb07ecf7; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Anisodamine_Hydrobromide.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The NCIT hydrobromide term resolves, but the active CAS, PubChem CID, and chemistry describe base anisodamine rather than anisodamine hydrobromide.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Anisodamine_Hydrobromide.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Anisodamine_Hydrobromide.yaml`, `just validate-terms data/ingredients/mapped/Anisodamine_Hydrobromide.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Anisodamine_Hydrobromide.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Anisodamine_Hydrobromide.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
