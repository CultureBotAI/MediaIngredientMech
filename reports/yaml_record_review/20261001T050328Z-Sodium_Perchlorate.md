# YAML Record Review: Sodium perchlorate

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Sodium_Perchlorate.yaml`
- Started UTC: 2026-10-01T05:03:28Z
- Finished UTC: 2026-10-01T05:03:29Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Sodium_Perchlorate.yaml`
- Identifier: `CHEBI:132103`
- Preferred term: Sodium perchlorate
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Sodium_Perchlorate.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:132103`.
- Ontology label: `sodium perchlorate`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Sodium_Perchlorate.md` after the record changed from d1c9ae50b76e36da7622c4228f7020d2f4d24dd6f97db7cd979ab7643897140b to 5b8a68b008ebce2e98c040b9dfff7b5b16f2370b320bb77cf0d3db32e680e0e0; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `5b8a68b008ebce2e98c040b9dfff7b5b16f2370b320bb77cf0d3db32e680e0e0`.
- Previous review: `reports/yaml_record_review/Sodium_Perchlorate.md`.
- Previous record SHA-256: `d1c9ae50b76e36da7622c4228f7020d2f4d24dd6f97db7cd979ab7643897140b`.
- Source occurrence traceability: 4 occurrence(s) across 4 medium/media.
- Latest curation event: CORRECTED_ROLE_EVIDENCE by codex_issue_710_semantic_evidence_review at 2026-09-22T02:06:34+00:00: Added inspected primary-publication support and bounded organism/condition context to the cellular metabolic role (#710). Retained original computational provenance and confidence. See reports/semantic_review_20260921/resolution/roles/cellular-role-plan.json for the assertion-specific interpretation.
- Active SSSOM state: 1 active row(s) for `MIM:Sodium_Perchlorate`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Sodium_Perchlorate.md` after the record changed from d1c9ae50b76e36da7622c4228f7020d2f4d24dd6f97db7cd979ab7643897140b to 5b8a68b008ebce2e98c040b9dfff7b5b16f2370b320bb77cf0d3db32e680e0e0; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Sodium_Perchlorate.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The exact CHEBI:132103 identity, CAS, and ChEBI synonyms pass, but final SSSOM exports the monohydrate label and ELECTRON_ACCEPTOR is provisional.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Sodium_Perchlorate.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Sodium_Perchlorate.yaml`, `just validate-terms data/ingredients/mapped/Sodium_Perchlorate.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Sodium_Perchlorate.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Sodium_Perchlorate.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
