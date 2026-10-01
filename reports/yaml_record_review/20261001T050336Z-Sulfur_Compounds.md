# YAML Record Review: Sulfur compounds

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Sulfur_Compounds.yaml`
- Started UTC: 2026-10-01T05:03:36Z
- Finished UTC: 2026-10-01T05:03:37Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Sulfur_Compounds.yaml`
- Identifier: `CHEBI:26835`
- Preferred term: Sulfur compounds
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Sulfur_Compounds.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:26835`.
- Ontology label: `sulfur molecular entity`.
- Mapping quality: `SYNONYM_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Sulfur_Compounds.md` after the record changed from 3d8ac41e9765b8038020977bf46ea6a73d381cef95577bc0e831d815eeb272ea to c573c64dac5ecfc50b9f4095faae9e8d14b4307d2c5a14cefc57b8e3dad2f4f6; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `c573c64dac5ecfc50b9f4095faae9e8d14b4307d2c5a14cefc57b8e3dad2f4f6`.
- Previous review: `reports/yaml_record_review/Sulfur_Compounds.md`.
- Previous record SHA-256: `3d8ac41e9765b8038020977bf46ea6a73d381cef95577bc0e831d815eeb272ea`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: REJECTED_TRAIT_SYNONYMS by claude at 2026-09-22T06:14:49.563933+00:00: Retyped activity/assay phrases as provenance-only REJECTED_LABEL because they describe a process or organism trait, not an ingredient name (#703): 'oxidation in darkness: sulfur compounds'. Preserved original text and source metadata. No identity, mapping, role, or remaining-synonym claim was adjudicated.
- Active SSSOM state: 1 active row(s) for `MIM:Sulfur_Compounds`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Sulfur_Compounds.md` after the record changed from 3d8ac41e9765b8038020977bf46ea6a73d381cef95577bc0e831d815eeb272ea to c573c64dac5ecfc50b9f4095faae9e8d14b4307d2c5a14cefc57b8e3dad2f4f6; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Sulfur_Compounds.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The CHEBI:26835 class grounding passes, but SSSOM other publishes a process-qualified metatrait label.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Sulfur_Compounds.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Sulfur_Compounds.yaml`, `just validate-terms data/ingredients/mapped/Sulfur_Compounds.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Sulfur_Compounds.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Sulfur_Compounds.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
