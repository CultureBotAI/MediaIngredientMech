# YAML Record Review: Sodium perchlorate monohydrate

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Sodium_Perchlorate_Monohydrate.yaml`
- Started UTC: 2026-10-01T05:03:29Z
- Finished UTC: 2026-10-01T05:03:30Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Sodium_Perchlorate_Monohydrate.yaml`
- Identifier: `cas:7791-07-3`
- Preferred term: Sodium perchlorate monohydrate
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Sodium_Perchlorate_Monohydrate.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:132103`.
- Ontology label: `sodium perchlorate`.
- Mapping quality: `CLOSE_MATCH`.
- Active SSSOM rows for this subject: 2.
- Identity judgement: Refreshed `reports/yaml_record_review/Sodium_Perchlorate_Monohydrate.md` after the record changed from 83a5b1cf514bd048c0e253a3ec7e4b99710b732587286dd370dfb27e6012de24 to 1f39286747eb8f3a2ec3da7919f9e6cb197221fcfef46af69a6784afd8f83ccc; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `1f39286747eb8f3a2ec3da7919f9e6cb197221fcfef46af69a6784afd8f83ccc`.
- Previous review: `reports/yaml_record_review/Sodium_Perchlorate_Monohydrate.md`.
- Previous record SHA-256: `83a5b1cf514bd048c0e253a3ec7e4b99710b732587286dd370dfb27e6012de24`.
- Source occurrence traceability: 1 occurrence(s) across 1 medium/media.
- Latest curation event: CORRECTED_ROLE_EVIDENCE by codex_issue_710_semantic_evidence_review at 2026-09-22T02:06:34+00:00: Added inspected primary-publication support and bounded organism/condition context to the cellular metabolic role (#710). Retained original computational provenance and confidence. See reports/semantic_review_20260921/resolution/roles/cellular-role-plan.json for the assertion-specific interpretation.
- Active SSSOM state: 2 active row(s) for `MIM:Sodium_Perchlorate_Monohydrate`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Sodium_Perchlorate_Monohydrate.md` after the record changed from 83a5b1cf514bd048c0e253a3ec7e4b99710b732587286dd370dfb27e6012de24 to 1f39286747eb8f3a2ec3da7919f9e6cb197221fcfef46af69a6784afd8f83ccc; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Sodium_Perchlorate_Monohydrate.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The CAS hydrate identity, close ChEBI parent, and exact CAS row pass, but ELECTRON_ACCEPTOR is provisional.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Sodium_Perchlorate_Monohydrate.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Sodium_Perchlorate_Monohydrate.yaml`, `just validate-terms data/ingredients/mapped/Sodium_Perchlorate_Monohydrate.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Sodium_Perchlorate_Monohydrate.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Sodium_Perchlorate_Monohydrate.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
