# YAML Record Review: sn-Glycerol 3-phosphate lithium salt

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Sn-Glycerol_3-phosphate_Lithium_Salt.yaml`
- Started UTC: 2026-10-01T05:03:22Z
- Finished UTC: 2026-10-01T05:03:23Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Sn-Glycerol_3-phosphate_Lithium_Salt.yaml`
- Identifier: `cas:17989-41-2`
- Preferred term: sn-Glycerol 3-phosphate lithium salt
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Sn-Glycerol_3-phosphate_Lithium_Salt.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:15978`.
- Ontology label: `sn-glycerol 3-phosphate`.
- Mapping quality: `NARROW_MATCH`.
- Active SSSOM rows for this subject: 3.
- Identity judgement: Refreshed `reports/yaml_record_review/Sn-Glycerol_3-phosphate_Lithium_Salt.md` after the record changed from 67ccdc054e9653131dc7f80beed6b6763edbb22b7ce799eebfdfcfa651018e0c to 94fff493bf4b0ddc19144054a44305ea29de113477254be64e1dc86c0f128f51; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `94fff493bf4b0ddc19144054a44305ea29de113477254be64e1dc86c0f128f51`.
- Previous review: `reports/yaml_record_review/Sn-Glycerol_3-phosphate_Lithium_Salt.md`.
- Previous record SHA-256: `67ccdc054e9653131dc7f80beed6b6763edbb22b7ce799eebfdfcfa651018e0c`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: REJECTED_PARENT_NAME_SYNONYMS by claude at 2026-09-22T20:41:14.285965+00:00: Retyped names of the parent compound or of a different hydrate as provenance-only REJECTED_LABEL, because this record is a distinct salt, hydrate or tombstone form and the label index resolved the parent's name here (#232): '(2R)-2,3-dihydroxypropyl dihydrogen phosphate'; 'sn-glycerol 3-(dihydrogen phosphate)'. Preserved original text and source metadata. No identity, mapping, role, or remaining-synonym claim was adjudicated.
- Active SSSOM state: 3 active row(s) for `MIM:Sn-Glycerol_3-phosphate_Lithium_Salt`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Sn-Glycerol_3-phosphate_Lithium_Salt.md` after the record changed from 67ccdc054e9653131dc7f80beed6b6763edbb22b7ce799eebfdfcfa651018e0c to 94fff493bf4b0ddc19144054a44305ea29de113477254be64e1dc86c0f128f51; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Sn-Glycerol_3-phosphate_Lithium_Salt.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The narrow parent and exact registry rows pass, but final SSSOM exports free-acid parent synonyms and CARBON_SOURCE is provisional.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Sn-Glycerol_3-phosphate_Lithium_Salt.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Sn-Glycerol_3-phosphate_Lithium_Salt.yaml`, `just validate-terms data/ingredients/mapped/Sn-Glycerol_3-phosphate_Lithium_Salt.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Sn-Glycerol_3-phosphate_Lithium_Salt.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Sn-Glycerol_3-phosphate_Lithium_Salt.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
