# YAML Record Review: Sodium deoxycholate monohydrate

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Sodium_Deoxycholate_Monohydrate.yaml`
- Started UTC: 2026-10-01T05:03:27Z
- Finished UTC: 2026-10-01T05:03:28Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Sodium_Deoxycholate_Monohydrate.yaml`
- Identifier: `cas:145224-92-6`
- Preferred term: Sodium deoxycholate monohydrate
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Sodium_Deoxycholate_Monohydrate.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:9177`.
- Ontology label: `sodium deoxycholate`.
- Mapping quality: `CLOSE_MATCH`.
- Active SSSOM rows for this subject: 2.
- Identity judgement: Refreshed `reports/yaml_record_review/Sodium_Deoxycholate_Monohydrate.md` after the record changed from 568b9c617152c8e53847ecbfedbac08b527fb52bd154665ae3b78dea49a7db99 to 221d045730234ed597aa3a75ad8880a0ffd43aefd881832b29b33108172abd99; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `221d045730234ed597aa3a75ad8880a0ffd43aefd881832b29b33108172abd99`.
- Previous review: `reports/yaml_record_review/Sodium_Deoxycholate_Monohydrate.md`.
- Previous record SHA-256: `568b9c617152c8e53847ecbfedbac08b527fb52bd154665ae3b78dea49a7db99`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: REJECTED_PARENT_NAME_SYNONYMS by claude at 2026-09-22T20:41:14.285965+00:00: Retyped names of the parent compound or of a different hydrate as provenance-only REJECTED_LABEL, because this record is a distinct salt, hydrate or tombstone form and the label index resolved the parent's name here (#232): 'sodium 3alpha,12alpha-dihydroxy-5beta-cholan-24-oate'. Preserved original text and source metadata. No identity, mapping, role, or remaining-synonym claim was adjudicated.
- Active SSSOM state: 2 active row(s) for `MIM:Sodium_Deoxycholate_Monohydrate`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Sodium_Deoxycholate_Monohydrate.md` after the record changed from 568b9c617152c8e53847ecbfedbac08b527fb52bd154665ae3b78dea49a7db99 to 221d045730234ed597aa3a75ad8880a0ffd43aefd881832b29b33108172abd99; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Sodium_Deoxycholate_Monohydrate.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The CAS hydrate identity and close ChEBI parent pass, but final SSSOM lacks the kgmicrobe.compound anchor and exports unsafe synonyms.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Sodium_Deoxycholate_Monohydrate.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Sodium_Deoxycholate_Monohydrate.yaml`, `just validate-terms data/ingredients/mapped/Sodium_Deoxycholate_Monohydrate.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Sodium_Deoxycholate_Monohydrate.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Sodium_Deoxycholate_Monohydrate.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
