# YAML Record Review: Tetrachloroethene

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Tetrachloroethene.yaml`
- Started UTC: 2026-10-01T05:03:41Z
- Finished UTC: 2026-10-01T05:03:42Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Tetrachloroethene.yaml`
- Identifier: `CHEBI:17300`
- Preferred term: Tetrachloroethene
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Tetrachloroethene.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:17300`.
- Ontology label: `tetrachloroethene`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Tetrachloroethene.md` after the record changed from e13bca32bdfc597091a6ee6458eab2c0d50f3140514ef5eac0fbdb24bbbbab7a to b8e43c00cd45e09f72e7e496b1cc606e1d64e44ce559fa34a1ee7a6781f07a82; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `b8e43c00cd45e09f72e7e496b1cc606e1d64e44ce559fa34a1ee7a6781f07a82`.
- Previous review: `reports/yaml_record_review/Tetrachloroethene.md`.
- Previous record SHA-256: `e13bca32bdfc597091a6ee6458eab2c0d50f3140514ef5eac0fbdb24bbbbab7a`.
- Source occurrence traceability: 11 occurrence(s) across 11 medium/media.
- Latest curation event: CORRECTED_ROLE_EVIDENCE by codex_issue_710_semantic_evidence_review at 2026-09-22T02:06:34+00:00: Added inspected primary-publication support and bounded organism/condition context to the cellular metabolic role (#710). Retained original computational provenance and confidence. See reports/semantic_review_20260921/resolution/roles/cellular-role-plan.json for the assertion-specific interpretation.
- Active SSSOM state: 1 active row(s) for `MIM:Tetrachloroethene`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Tetrachloroethene.md` after the record changed from e13bca32bdfc597091a6ee6458eab2c0d50f3140514ef5eac0fbdb24bbbbab7a to b8e43c00cd45e09f72e7e496b1cc606e1d64e44ce559fa34a1ee7a6781f07a82; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Tetrachloroethene.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The exact CHEBI:17300 identity passes, but ELECTRON_ACCEPTOR is still only a provisional in-session LLM role.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Tetrachloroethene.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Tetrachloroethene.yaml`, `just validate-terms data/ingredients/mapped/Tetrachloroethene.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Tetrachloroethene.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Tetrachloroethene.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
