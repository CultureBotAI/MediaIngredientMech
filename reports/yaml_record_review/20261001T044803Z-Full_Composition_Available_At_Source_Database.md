# YAML Record Review: Full composition available at source database

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/unmapped/Full_Composition_Available_At_Source_Database.yaml`
- Started UTC: 2026-10-01T04:48:03Z
- Finished UTC: 2026-10-01T04:48:04Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/unmapped/Full_Composition_Available_At_Source_Database.yaml`
- Identifier: `UNMAPPED_0001`
- Preferred term: Full composition available at source database
- Mapping status: `UNMAPPED`
- Ingredient type: `UNDEFINED_MIXTURE`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/unmapped data/ingredients/mapped/Na2-citrate.yaml data/ingredients/mapped/Nitrilotriacetic_Acid_Trisodium_Salt.yaml --out /tmp/mim_remaining_review_validation.tsv --workers 4 --quiet`; 275 files scanned and 0 ERROR rows.
- Not checked: this record has no `ontology_mapping.ontology_id`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `UNMAPPED`.
- Ontology ID: `None`.
- Ontology label: `None`.
- Mapping quality: `None`.
- Active SSSOM rows for this subject: 0.
- Identity judgement: Mixture/extract/preparation is intentionally left unmapped until the source supports a component decomposition or exact preparation identity.

## Evidence

- Current record SHA-256: `3521b19020100e3a606627502c3e066dca7f9b6343af0352206837891bef82c0`.
- Source occurrence traceability: 196 occurrence(s) across 196 medium/media.
- Latest curation event: FLAGGED_NON_INGREDIENT by cbclaw_followups_114 at 2026-07-05T00:00:00+00:00: Flagged as NON_INGREDIENT / source-composition placeholder (not a chemical or mixture identity). Retained UNMAPPED; no ontology mapping invented and record not deleted.
- Active SSSOM state: No active row for `MIM:Full_Composition_Available_At_Source_Database`, as expected for `UNMAPPED`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.
- The 2026-09-01 unmapped review explains the residual unmapped policy: named media, undefined mixtures, and exact single-ingredient residuals must stay unmapped until exact same-form evidence is available.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.
- Consequential unresolved item: Mixture/extract/preparation is intentionally left unmapped until the source supports a component decomposition or exact preparation identity.

## Findings

- **major**: `data/ingredients/unmapped/Full_Composition_Available_At_Source_Database.yaml` remains `UNMAPPED`; the label denotes a mixture, extract, or incompletely specified preparation. Do not exact-match it to a broader parent, component, hydrate, salt, or lookalike label.

## Recommended Edits

- Curate an exact same-form identity or decomposition for `data/ingredients/unmapped/Full_Composition_Available_At_Source_Database.yaml` before mapping it.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/unmapped/Full_Composition_Available_At_Source_Database.yaml`, `just validate-terms data/ingredients/unmapped/Full_Composition_Available_At_Source_Database.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/unmapped/Full_Composition_Available_At_Source_Database.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/unmapped/Full_Composition_Available_At_Source_Database.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
