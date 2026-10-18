# YAML Record Review: Glycerol-asparagine agar

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/unmapped/Glycerol-asparagine_Agar.yaml`
- Started UTC: 2026-10-01T04:48:13Z
- Finished UTC: 2026-10-01T04:48:14Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/unmapped/Glycerol-asparagine_Agar.yaml`
- Identifier: `UNMAPPED_0122`
- Preferred term: Glycerol-asparagine agar
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

- Current record SHA-256: `a20ab80bfd721b38622db05c4890f6f5ae80540ae038959e0e91446d9edaf5d5`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: ANNOTATED by edison_literature_identity at 2026-08-06T00:00:00+00:00: Edison LITERATURE (PaperQA3) identity research; report at research/ingredients/Glycerol-asparagine_Agar-edison-literature.md (local artifact — research/ is gitignored, so the findings are quoted here rather than linked). Report verdict: ### Recommended synonyms — - `ISP medium 5` — supported synonym. CURIEs discussed: CHEBI:2509. Recorded as provenance only — no grounding applied from this run. Edison's recommendations are deliberately conservative, and a plausible identifier promoted by a mechanism that never decided anything is what #203 and #263 exist to undo. Any CURIE above is a curator's to accept or reject.
- Active SSSOM state: No active row for `MIM:Glycerol-asparagine_Agar`, as expected for `UNMAPPED`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.
- The 2026-09-01 unmapped review explains the residual unmapped policy: named media, undefined mixtures, and exact single-ingredient residuals must stay unmapped until exact same-form evidence is available.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.
- Consequential unresolved item: Named medium/formulation is intentionally left unmapped until a recipe-level CultureMech representation owns the formulation.

## Findings

- **major**: `data/ingredients/unmapped/Glycerol-asparagine_Agar.yaml` remains `UNMAPPED`; the label denotes a named medium or formulation rather than one exact chemical substance. Do not exact-match it to a broader parent, component, hydrate, salt, or lookalike label.

## Recommended Edits

- Curate an exact same-form identity or decomposition for `data/ingredients/unmapped/Glycerol-asparagine_Agar.yaml` before mapping it.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/unmapped/Glycerol-asparagine_Agar.yaml`, `just validate-terms data/ingredients/unmapped/Glycerol-asparagine_Agar.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/unmapped/Glycerol-asparagine_Agar.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/unmapped/Glycerol-asparagine_Agar.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
