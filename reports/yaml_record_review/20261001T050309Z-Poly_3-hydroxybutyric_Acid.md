# YAML Record Review: Poly(3-hydroxybutyric acid)

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml`
- Started UTC: 2026-10-01T05:03:09Z
- Finished UTC: 2026-10-01T05:03:10Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml`
- Identifier: `cas:29435-48-1`
- Preferred term: Poly(3-hydroxybutyric acid)
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:20067`.
- Ontology label: `3-hydroxybutyric acid`.
- Mapping quality: `NARROW_MATCH`.
- Active SSSOM rows for this subject: 3.
- Identity judgement: Refreshed `reports/yaml_record_review/Poly_3-hydroxybutyric_Acid.md` after the record changed from 7b40c7f28a9424e0cda7c685c3c53d839d54193ac278f265a461a29afaa53c34 to 9e0e563c06141faa41510a655cc3e1821d7a225c09236b309e2a2c1d541b7848; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `9e0e563c06141faa41510a655cc3e1821d7a225c09236b309e2a2c1d541b7848`.
- Previous review: `reports/yaml_record_review/Poly_3-hydroxybutyric_Acid.md`.
- Previous record SHA-256: `7b40c7f28a9424e0cda7c685c3c53d839d54193ac278f265a461a29afaa53c34`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: REJECTED_PARENT_NAME_SYNONYMS by claude at 2026-09-22T20:41:14.285965+00:00: Retyped names of the parent compound or of a different hydrate as provenance-only REJECTED_LABEL, because this record is a distinct salt, hydrate or tombstone form and the label index resolved the parent's name here (#232): '3-hydroxybutanoic acid'. Preserved original text and source metadata. No identity, mapping, role, or remaining-synonym claim was adjudicated.
- Active SSSOM state: 3 active row(s) for `MIM:Poly_3-hydroxybutyric_Acid`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Poly_3-hydroxybutyric_Acid.md` after the record changed from 7b40c7f28a9424e0cda7c685c3c53d839d54193ac278f265a461a29afaa53c34 to 9e0e563c06141faa41510a655cc3e1821d7a225c09236b309e2a2c1d541b7848; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Poly_3-hydroxybutyric_Acid.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The CAS identity is preserved, but the parent mapping and exported monomer synonym point at 3-hydroxybutyric acid.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Poly_3-hydroxybutyric_Acid.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml`, `just validate-terms data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
