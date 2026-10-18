# YAML Record Review: Nitrilotriacetic acid disodium salt

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Nitrilotriacetic_Acid_Disodium_Salt.yaml`
- Started UTC: 2026-10-01T05:03:05Z
- Finished UTC: 2026-10-01T05:03:06Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Nitrilotriacetic_Acid_Disodium_Salt.yaml`
- Identifier: `cas:15467-20-6`
- Preferred term: Nitrilotriacetic acid disodium salt
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Nitrilotriacetic_Acid_Disodium_Salt.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:44557`.
- Ontology label: `nitrilotriacetic acid`.
- Mapping quality: `NARROW_MATCH`.
- Active SSSOM rows for this subject: 3.
- Identity judgement: Refreshed `reports/yaml_record_review/Nitrilotriacetic_Acid_Disodium_Salt.md` after the record changed from 2470f9fdda8b8d450302d24f12e7ef005c06a0f6e795372d0b68217839ee30a8 to fd8ee83cb2fad4bc16bd842f755b21c676ca1e4f42cabefd35516b7631acbb0d; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `fd8ee83cb2fad4bc16bd842f755b21c676ca1e4f42cabefd35516b7631acbb0d`.
- Previous review: `reports/yaml_record_review/Nitrilotriacetic_Acid_Disodium_Salt.md`.
- Previous record SHA-256: `2470f9fdda8b8d450302d24f12e7ef005c06a0f6e795372d0b68217839ee30a8`.
- Source occurrence traceability: 7 occurrence(s) across 7 medium/media.
- Latest curation event: REJECTED_PARENT_NAME_SYNONYMS by claude at 2026-09-22T20:41:14.285965+00:00: Retyped names of the parent compound or of a different hydrate as provenance-only REJECTED_LABEL, because this record is a distinct salt, hydrate or tombstone form and the label index resolved the parent's name here (#232): 'N,N-bis(carboxymethyl)glycine'. Preserved original text and source metadata. No identity, mapping, role, or remaining-synonym claim was adjudicated.
- Active SSSOM state: 3 active row(s) for `MIM:Nitrilotriacetic_Acid_Disodium_Salt`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Nitrilotriacetic_Acid_Disodium_Salt.md` after the record changed from 2470f9fdda8b8d450302d24f12e7ef005c06a0f6e795372d0b68217839ee30a8 to fd8ee83cb2fad4bc16bd842f755b21c676ca1e4f42cabefd35516b7631acbb0d; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Nitrilotriacetic_Acid_Disodium_Salt.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The CAS disodium identity and parent rows pass, but stale parent structure/synonym data and a provisional CHELATOR role remain.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Nitrilotriacetic_Acid_Disodium_Salt.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Nitrilotriacetic_Acid_Disodium_Salt.yaml`, `just validate-terms data/ingredients/mapped/Nitrilotriacetic_Acid_Disodium_Salt.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Nitrilotriacetic_Acid_Disodium_Salt.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Nitrilotriacetic_Acid_Disodium_Salt.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
