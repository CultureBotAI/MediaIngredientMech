# YAML Record Review: Fructooligosaccharides (FOS)

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Fructooligosaccharides_Fos.yaml`
- Started UTC: 2026-10-01T05:02:21Z
- Finished UTC: 2026-10-01T05:02:22Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Fructooligosaccharides_Fos.yaml`
- Identifier: `cas:308066-66-2`
- Preferred term: Fructooligosaccharides (FOS)
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Fructooligosaccharides_Fos.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:28645`.
- Ontology label: `beta-D-fructofuranose`.
- Mapping quality: `NARROW_MATCH`.
- Active SSSOM rows for this subject: 3.
- Identity judgement: Refreshed `reports/yaml_record_review/Fructooligosaccharides_Fos.md` after the record changed from 8022579be56266c4756c407e16fd411cddb5810b5a2e131c4b1b0a882c44c9df to d894a5bae9ec92f003959d7676de82bb62fe39d8cbd9b33efafce2f6add5aa07; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `d894a5bae9ec92f003959d7676de82bb62fe39d8cbd9b33efafce2f6add5aa07`.
- Previous review: `reports/yaml_record_review/Fructooligosaccharides_Fos.md`.
- Previous record SHA-256: `8022579be56266c4756c407e16fd411cddb5810b5a2e131c4b1b0a882c44c9df`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: REJECTED_WRONG_SUBSTANCE_SYNONYMS by claude at 2026-09-24T07:48:22.781028+00:00: Retyped REJECTED_LABEL: 'FRUCTOSE' (EXACT_SYNONYM): the monomer's name on the oligosaccharide record (#669). Kept as provenance only; it must not resolve, be exported, or enter the SSSOM other column.
- Active SSSOM state: 3 active row(s) for `MIM:Fructooligosaccharides_Fos`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Fructooligosaccharides_Fos.md` after the record changed from 8022579be56266c4756c407e16fd411cddb5810b5a2e131c4b1b0a882c44c9df to d894a5bae9ec92f003959d7676de82bb62fe39d8cbd9b33efafce2f6add5aa07; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Fructooligosaccharides_Fos.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The FOS subject is incorrectly grounded through a beta-D-fructose CAS, parent row, structure block, and SSSOM synonym.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Fructooligosaccharides_Fos.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Fructooligosaccharides_Fos.yaml`, `just validate-terms data/ingredients/mapped/Fructooligosaccharides_Fos.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Fructooligosaccharides_Fos.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Fructooligosaccharides_Fos.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
