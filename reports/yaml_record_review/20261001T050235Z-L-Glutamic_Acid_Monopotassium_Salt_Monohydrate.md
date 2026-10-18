# YAML Record Review: L-Glutamic acid monopotassium salt monohydrate

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml`
- Started UTC: 2026-10-01T05:02:35Z
- Finished UTC: 2026-10-01T05:02:36Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml`
- Identifier: `cas:6382-01-0`
- Preferred term: L-Glutamic acid monopotassium salt monohydrate
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:16015`.
- Ontology label: `L-glutamic acid`.
- Mapping quality: `CLOSE_MATCH`.
- Active SSSOM rows for this subject: 2.
- Identity judgement: Refreshed `reports/yaml_record_review/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.md` after the record changed from b81046e7b35a714c71af86de076d1c15c18c454eafce07e5b3508935b3c0cc9d to 0026680a282b367ec2a228dcc4f04e70aec4ed812ca8629652e0137838b9636e; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `0026680a282b367ec2a228dcc4f04e70aec4ed812ca8629652e0137838b9636e`.
- Previous review: `reports/yaml_record_review/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.md`.
- Previous record SHA-256: `b81046e7b35a714c71af86de076d1c15c18c454eafce07e5b3508935b3c0cc9d`.
- Source occurrence traceability: 16 occurrence(s) across 16 medium/media.
- Latest curation event: REJECTED_PARENT_NAME_SYNONYMS by claude at 2026-09-22T20:41:14.285965+00:00: Retyped names of the parent compound or of a different hydrate as provenance-only REJECTED_LABEL, because this record is a distinct salt, hydrate or tombstone form and the label index resolved the parent's name here (#232): '(2S)-2-aminopentanedioic acid'; 'GLUTAMIC ACID'. Preserved original text and source metadata. No identity, mapping, role, or remaining-synonym claim was adjudicated.
- Active SSSOM state: 2 active row(s) for `MIM:L-Glutamic_Acid_Monopotassium_Salt_Monohydrate`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.md` after the record changed from b81046e7b35a714c71af86de076d1c15c18c454eafce07e5b3508935b3c0cc9d to 0026680a282b367ec2a228dcc4f04e70aec4ed812ca8629652e0137838b9636e; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The CAS primary identity, PubChem monohydrate structure, close parent, exact CAS row, and hydrate review pass, but the local registry anchor is missing, parent synonyms publish, and AMINO_ACID_SOURCE is provisional.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml`, `just validate-terms data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
