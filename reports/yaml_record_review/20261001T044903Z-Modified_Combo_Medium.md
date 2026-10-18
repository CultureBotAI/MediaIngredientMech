# YAML Record Review: Modified COMBO Medium

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/unmapped/Modified_Combo_Medium.yaml`
- Started UTC: 2026-10-01T04:49:03Z
- Finished UTC: 2026-10-01T04:49:04Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/unmapped/Modified_Combo_Medium.yaml`
- Identifier: `UNMAPPED_0111`
- Preferred term: Modified COMBO Medium
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

- Current record SHA-256: `a6f6b58cc1aa69e0c48286e504356dd4fc36ab01efb2d0140e798e9b822065e9`.
- Source occurrence traceability: 1 occurrence(s) across 1 medium/media.
- Latest curation event: ANNOTATED by edison_literature_identity at 2026-08-06T00:00:00+00:00: Edison LITERATURE (PaperQA3) identity research; report at research/ingredients/Modified_Combo_Medium-edison-literature.md (local artifact — research/ is gitignored, so the findings are quoted here rather than linked). Report verdict: **Recommended interpretation:** an **ambiguous, formulation-level label for a modified defined freshwater culture medium**, not a single chemical, hydrate, salt, buffer, extract, or uniquely specified recipe. COMBO is described as a defined freshwater medium and has been used for freshwater algae, including *Nitzschia palea*, *Uronema confervicolum*, and *Chlamydomonas reinhardtii*. (loustau2021th No ontology CURIE was proposed. Recorded as provenance only — no grounding applied from this run. Edison's recommendations are deliberately conservative, and a plausible identifier promoted by a mechanism that never decided anything is what #203 and #263 exist to undo. Any CURIE above is a curator's to accept or reject.
- Active SSSOM state: No active row for `MIM:Modified_Combo_Medium`, as expected for `UNMAPPED`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.
- The 2026-09-01 unmapped review explains the residual unmapped policy: named media, undefined mixtures, and exact single-ingredient residuals must stay unmapped until exact same-form evidence is available.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.
- Consequential unresolved item: Named medium/formulation is intentionally left unmapped until a recipe-level CultureMech representation owns the formulation.

## Findings

- **major**: `data/ingredients/unmapped/Modified_Combo_Medium.yaml` remains `UNMAPPED`; the label denotes a named medium or formulation rather than one exact chemical substance. Do not exact-match it to a broader parent, component, hydrate, salt, or lookalike label.

## Recommended Edits

- Curate an exact same-form identity or decomposition for `data/ingredients/unmapped/Modified_Combo_Medium.yaml` before mapping it.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/unmapped/Modified_Combo_Medium.yaml`, `just validate-terms data/ingredients/unmapped/Modified_Combo_Medium.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/unmapped/Modified_Combo_Medium.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/unmapped/Modified_Combo_Medium.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
