# YAML Record Review: D-Maltose monohydrate

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/D-Maltose_Monohydrate.yaml`
- Started UTC: 2026-10-01T05:02:04Z
- Finished UTC: 2026-10-01T05:02:05Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/D-Maltose_Monohydrate.yaml`
- Identifier: `cas:6363-53-7`
- Preferred term: D-Maltose monohydrate
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/D-Maltose_Monohydrate.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:17306`.
- Ontology label: `maltose`.
- Mapping quality: `CLOSE_MATCH`.
- Active SSSOM rows for this subject: 2.
- Identity judgement: Refreshed `reports/yaml_record_review/D-Maltose_Monohydrate.md` after the record changed from 26a9eeab846dc7bcc7bcca78b8c2f067389444a3bd23e4b85373dd61f9091bec to cda53191390133b9a1059b87938333b4d965e2b9009497dcd7e046af9b1f04d5; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `cda53191390133b9a1059b87938333b4d965e2b9009497dcd7e046af9b1f04d5`.
- Previous review: `reports/yaml_record_review/D-Maltose_Monohydrate.md`.
- Previous record SHA-256: `26a9eeab846dc7bcc7bcca78b8c2f067389444a3bd23e4b85373dd61f9091bec`.
- Source occurrence traceability: 20 occurrence(s) across 20 medium/media.
- Latest curation event: REJECTED_PARENT_NAME_SYNONYMS by claude at 2026-09-22T20:41:14.285965+00:00: Retyped names of the parent compound or of a different hydrate as provenance-only REJECTED_LABEL, because this record is a distinct salt, hydrate or tombstone form and the label index resolved the parent's name here (#232): 'alpha-D-glucopyranosyl-(1->4)-D-glucopyranose'; 'alpha-D-glucopyranosyl-(1->4)-D-glucose'. Preserved original text and source metadata. No identity, mapping, role, or remaining-synonym claim was adjudicated.
- Active SSSOM state: 2 active row(s) for `MIM:D-Maltose_Monohydrate`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/D-Maltose_Monohydrate.md` after the record changed from 26a9eeab846dc7bcc7bcca78b8c2f067389444a3bd23e4b85373dd61f9091bec to cda53191390133b9a1059b87938333b4d965e2b9009497dcd7e046af9b1f04d5; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/D-Maltose_Monohydrate.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The CAS primary, close maltose parent, and 20/20 count pass, but final SSSOM exports anhydrous synonyms and the carbon/energy roles are computational.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/D-Maltose_Monohydrate.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/D-Maltose_Monohydrate.yaml`, `just validate-terms data/ingredients/mapped/D-Maltose_Monohydrate.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/D-Maltose_Monohydrate.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/D-Maltose_Monohydrate.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
