# YAML Record Review: GAM Broth mod. powder

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/unmapped/GAM_Broth_Mod_Powder.yaml`
- Started UTC: 2026-10-01T04:48:06Z
- Finished UTC: 2026-10-01T04:48:07Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/unmapped/GAM_Broth_Mod_Powder.yaml`
- Identifier: `UNMAPPED_0389`
- Preferred term: GAM Broth mod. powder
- Mapping status: `UNMAPPED`
- Ingredient type: `NAMED_MEDIUM`
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
- Identity judgement: Named medium/formulation is intentionally left unmapped until a recipe-level CultureMech representation owns the formulation.

## Evidence

- Current record SHA-256: `f5a5ac22fdcdb9431b535af9c8094422d795304389e40207c7a92c9509885100`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: ANNOTATED by edison_literature_identity at 2026-08-06T00:00:00+00:00: Edison LITERATURE (PaperQA3) identity research; report at research/ingredients/GAM_Broth_Mod_Powder-edison-literature.md (local artifact — research/ is gitignored, so the findings are quoted here rather than linked). Report verdict: **Recommended interpretation:** `GAM Broth mod. powder` is a **dehydrated, multicomponent complete culture-medium formulation** used to prepare modified GAM (mGAM) broth. It is not a single chemical, salt, hydrate, buffer, or ingredient-level extract. The current `ingredient_type: DEFINED_MEDIUM` is therefore appropriate at the record-model level, although “defined” here means a named complete med No ontology CURIE was proposed. Recorded as provenance only — no grounding applied from this run. Edison's recommendations are deliberately conservative, and a plausible identifier promoted by a mechanism that never decided anything is what #203 and #263 exist to undo. Any CURIE above is a curator's to accept or reject.
- Active SSSOM state: No active row for `MIM:GAM_Broth_Mod_Powder`, as expected for `UNMAPPED`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.
- The 2026-09-01 unmapped review explains the residual unmapped policy: named media, undefined mixtures, and exact single-ingredient residuals must stay unmapped until exact same-form evidence is available.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.
- Consequential unresolved item: Named medium/formulation is intentionally left unmapped until a recipe-level CultureMech representation owns the formulation.

## Findings

- **major**: `data/ingredients/unmapped/GAM_Broth_Mod_Powder.yaml` remains `UNMAPPED`; the label denotes a named medium or formulation rather than one exact chemical substance. Do not exact-match it to a broader parent, component, hydrate, salt, or lookalike label.

## Recommended Edits

- Curate an exact same-form identity or decomposition for `data/ingredients/unmapped/GAM_Broth_Mod_Powder.yaml` before mapping it.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/unmapped/GAM_Broth_Mod_Powder.yaml`, `just validate-terms data/ingredients/unmapped/GAM_Broth_Mod_Powder.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/unmapped/GAM_Broth_Mod_Powder.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/unmapped/GAM_Broth_Mod_Powder.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
