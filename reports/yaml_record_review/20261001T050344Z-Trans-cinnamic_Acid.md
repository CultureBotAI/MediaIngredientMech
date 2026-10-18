# YAML Record Review: trans-Cinnamic acid

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Trans-cinnamic_Acid.yaml`
- Started UTC: 2026-10-01T05:03:44Z
- Finished UTC: 2026-10-01T05:03:45Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Trans-cinnamic_Acid.yaml`
- Identifier: `CHEBI:35697`
- Preferred term: trans-Cinnamic acid
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Trans-cinnamic_Acid.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:35697`.
- Ontology label: `trans-cinnamic acid`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Trans-cinnamic_Acid.md` after the record changed from a47a4dad1bd7204ee15edc4307a9491b6da91d3b51d0586e6018982e416f1003 to 317e87dde94dea859dced9aa22b75134ee97a4b43e1a7c178e44a73f58e1f8d9; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `317e87dde94dea859dced9aa22b75134ee97a4b43e1a7c178e44a73f58e1f8d9`.
- Previous review: `reports/yaml_record_review/Trans-cinnamic_Acid.md`.
- Previous record SHA-256: `a47a4dad1bd7204ee15edc4307a9491b6da91d3b51d0586e6018982e416f1003`.
- Source occurrence traceability: 3 occurrence(s) across 3 medium/media.
- Latest curation event: CORRECTED by claude at 2026-09-23T04:53:11.683397+00:00: '3-phenylprop-2-enoic acid' -> REJECTED_LABEL (the exact synonym of the geometry-unspecified parent CHEBI:27386, not of the trans isomer); evidence note added. The record's only source-supplied identity is CAS 140-10-3 (CultureBotHT), which ChEBI xrefs on CHEBI:35697 trans-cinnamic acid only; the geometry-unspecified CHEBI:27386's sole CAS is 621-82-9. Section 3 step 4's evidence hatch picks the trans isomer, which Trans-cinnamic_Acid already holds, so the two records denote one substance (#312).
- Active SSSOM state: 1 active row(s) for `MIM:Trans-cinnamic_Acid`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Trans-cinnamic_Acid.md` after the record changed from a47a4dad1bd7204ee15edc4307a9491b6da91d3b51d0586e6018982e416f1003 to 317e87dde94dea859dced9aa22b75134ee97a4b43e1a7c178e44a73f58e1f8d9; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Trans-cinnamic_Acid.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The exact CHEBI identity and final SSSOM row pass, but CARBON_SOURCE is provisional in-session LLM evidence.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Trans-cinnamic_Acid.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Trans-cinnamic_Acid.yaml`, `just validate-terms data/ingredients/mapped/Trans-cinnamic_Acid.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Trans-cinnamic_Acid.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Trans-cinnamic_Acid.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
