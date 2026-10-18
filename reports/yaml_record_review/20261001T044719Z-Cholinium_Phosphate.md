# YAML Record Review: Cholinium phosphate

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/unmapped/Cholinium_Phosphate.yaml`
- Started UTC: 2026-10-01T04:47:19Z
- Finished UTC: 2026-10-01T04:47:20Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/unmapped/Cholinium_Phosphate.yaml`
- Identifier: `UNMAPPED_0160`
- Preferred term: Cholinium phosphate
- Mapping status: `UNMAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
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
- Identity judgement: Specific single-ingredient residual remains unresolved: current evidence does not support an exact ontology or stable-registry identity.

## Evidence

- Current record SHA-256: `e02446cfe63863f26b3cb61c9db60240d19ee60f5793d8ec1db9109cfb1f1d87`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: ANNOTATED by edison_literature_identity at 2026-08-06T00:00:00+00:00: Edison LITERATURE (PaperQA3) identity research; report at research/ingredients/Cholinium_phosphate-edison-literature.md (local artifact — research/ is gitignored, so the findings are quoted here rather than linked). Report verdict: **Recommendation: retain `UNMAPPED`.** The imported label denotes a cholinium–phosphate salt but does not specify the phosphate protonation state, ion ratio, hydrate state, or formulation water content. It is therefore an **ambiguous single-salt label**, not a sufficiently defined chemical identity. No ontology CURIE was proposed. Recorded as provenance only — no grounding applied from this run. Edison's recommendations are deliberately conservative, and a plausible identifier promoted by a mechanism that never decided anything is what #203 and #263 exist to undo. Any CURIE above is a curator's to accept or reject.
- Active SSSOM state: No active row for `MIM:Cholinium_Phosphate`, as expected for `UNMAPPED`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.
- The 2026-09-01 unmapped review explains the residual unmapped policy: named media, undefined mixtures, and exact single-ingredient residuals must stay unmapped until exact same-form evidence is available.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.
- Consequential unresolved item: Specific single-ingredient residual remains unresolved: current evidence does not support an exact ontology or stable-registry identity.

## Findings

- **major**: `data/ingredients/unmapped/Cholinium_Phosphate.yaml` remains `UNMAPPED`; no exact ontology term or independently supported registry identity is recorded. Do not exact-match it to a broader parent, component, hydrate, salt, or lookalike label.

## Recommended Edits

- Curate an exact same-form identity or decomposition for `data/ingredients/unmapped/Cholinium_Phosphate.yaml` before mapping it.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/unmapped/Cholinium_Phosphate.yaml`, `just validate-terms data/ingredients/unmapped/Cholinium_Phosphate.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/unmapped/Cholinium_Phosphate.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/unmapped/Cholinium_Phosphate.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
