# YAML Record Review: Apramycin sulfate salt

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Apramycin_Sulfate_Salt.yaml`
- Started UTC: 2026-10-01T05:01:24Z
- Finished UTC: 2026-10-01T05:01:25Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Apramycin_Sulfate_Salt.yaml`
- Identifier: `CHEBI:190734`
- Preferred term: Apramycin sulfate salt
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Apramycin_Sulfate_Salt.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:190734`.
- Ontology label: `Apramycin sulfate`.
- Mapping quality: `CAS_RN_LOOKUP`.
- Active SSSOM rows for this subject: 3.
- Identity judgement: Refreshed `reports/yaml_record_review/Apramycin_Sulfate_Salt.md` after the record changed from 33fd1bd6dd4db120ea6c8aa324092637da23d0503ddb7d5f45b4d3f827dc3bcb to acc3fbd3cd049b34e685ac0f6539e33c2afc116e803ae4ad9a84e6e6ed6c7f5e; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `acc3fbd3cd049b34e685ac0f6539e33c2afc116e803ae4ad9a84e6e6ed6c7f5e`.
- Previous review: `reports/yaml_record_review/Apramycin_Sulfate_Salt.md`.
- Previous record SHA-256: `33fd1bd6dd4db120ea6c8aa324092637da23d0503ddb7d5f45b4d3f827dc3bcb`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: REGRADED_PARENT_TO_IDENTITY by claude at 2026-09-23T00:44:54.453584+00:00: identifier cas:65710-07-8 -> CHEBI:190734; ontology CHEBI:190734 ('Apramycin sulfate') -> CHEBI:190734 ('Apramycin sulfate'); mapping_quality NARROW_MATCH -> CAS_RN_LOOKUP. The 'no CHEBI entry exists' note was wrong: CHEBI:190734 'Apramycin sulfate' (C21H41N5O11.H2O4S = the record's C21H43N5O15S) has InChIKey WGLYHYWDYPSNPF-RQFIXDHTSA-N, and the record's CAS 65710-07-8 resolves on PubChem (CID 3081544) to the same InChIKey. The broadMatch parent is the substance itself; Section 3 step 1 promotes it to the identifier (#326 precedent), graded CAS_RN_LOOKUP because the CAS, not the label, established it. The CAS stays on its registry row; the kgmicrobe.compound row is dropped. (#312)
- Active SSSOM state: 3 active row(s) for `MIM:Apramycin_Sulfate_Salt`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Apramycin_Sulfate_Salt.md` after the record changed from 33fd1bd6dd4db120ea6c8aa324092637da23d0503ddb7d5f45b4d3f827dc3bcb to acc3fbd3cd049b34e685ac0f6539e33c2afc116e803ae4ad9a84e6e6ed6c7f5e; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Apramycin_Sulfate_Salt.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The CAS and PubChem chemistry match ChEBI Apramycin sulfate, but the ChEBI relation is undergraded and the selective-agent role is only a provisional name-pattern inference.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Apramycin_Sulfate_Salt.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Apramycin_Sulfate_Salt.yaml`, `just validate-terms data/ingredients/mapped/Apramycin_Sulfate_Salt.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Apramycin_Sulfate_Salt.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Apramycin_Sulfate_Salt.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
