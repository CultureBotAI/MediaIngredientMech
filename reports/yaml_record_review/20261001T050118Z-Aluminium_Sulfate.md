# YAML Record Review: Aluminium sulfate

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Aluminium_Sulfate.yaml`
- Started UTC: 2026-10-01T05:01:18Z
- Finished UTC: 2026-10-01T05:01:19Z
- Verdict: pass

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Aluminium_Sulfate.yaml`
- Identifier: `CHEBI:74768`
- Preferred term: Aluminium sulfate
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Aluminium_Sulfate.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:74768`.
- Ontology label: `aluminium sulfate (anhydrous)`.
- Mapping quality: `CAS_RN_LOOKUP`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Aluminium_Sulfate.md` after the record changed from 8bdb3e5f2f5124be6fac24226d72f78c19bd48ec9285ffe8911a05c8fad7eca6 to 90cf0c8408d79d3594864b886ec960c84451e808db41be54d620975b0f78117e; no prior finding is carried forward.

## Evidence

- Current record SHA-256: `90cf0c8408d79d3594864b886ec960c84451e808db41be54d620975b0f78117e`.
- Previous review: `reports/yaml_record_review/Aluminium_Sulfate.md`.
- Previous record SHA-256: `8bdb3e5f2f5124be6fac24226d72f78c19bd48ec9285ffe8911a05c8fad7eca6`.
- Source occurrence traceability: 1 occurrence(s) across 1 medium/media.
- Latest curation event: REGROUNDED_IDENTITY by claude at 2026-09-23T00:44:54.446218+00:00: identifier CHEBI:74772 -> CHEBI:74768; ontology CHEBI:74772 ('aluminium sulfate') -> CHEBI:74768 ('aluminium sulfate (anhydrous)'); mapping_quality EXACT_MATCH -> CAS_RN_LOOKUP. CHEBI:74772 'aluminium sulfate' is a class ('any inorganic sulfate salt ...'; no formula, InChIKey or CAS) with three members: anhydrous, hexadecahydrate, octadecahydrate. The record's CAS 10043-01-3 came from the CultureBotHT source row with FW 342.15, the anhydrous mass, and ChEBI xrefs that CAS on exactly one term, CHEBI:74768 'aluminium sulfate (anhydrous)'. Section 3 step 4's evidence hatch: the CAS picks the member; the mapping was lexical, so the CAS is independent evidence. (#312)
- Active SSSOM state: 1 active row(s) for `MIM:Aluminium_Sulfate`.
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

- Re-run strict schema validation on `data/ingredients/mapped/Aluminium_Sulfate.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Aluminium_Sulfate.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
