# YAML Record Review: BC Lignin Sorghum

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/unmapped/BC_Lignin_Sorghum.yaml`
- Started UTC: 2026-10-01T04:46:41Z
- Finished UTC: 2026-10-01T04:46:42Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/unmapped/BC_Lignin_Sorghum.yaml`
- Identifier: `UNMAPPED_0169`
- Preferred term: BC Lignin Sorghum
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

- Current record SHA-256: `0b2938ae1a8932c29247a8bb83b194b85cdee9590a764449fce10d1f8feba0b4`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: ANNOTATED by edison_literature_identity at 2026-08-06T00:00:00+00:00: Edison LITERATURE (PaperQA3) identity research; report at research/ingredients/BC_Lignin_Sorghum-edison-literature.md (local artifact — research/ is gitignored, so the findings are quoted here rather than linked). Report verdict: **Recommended interpretation:** a source-specific, sorghum-derived lignin material or fraction of unresolved preparation—not a single chemical, salt, hydrate, buffer, or standardized formulation. Lignin is itself a heterogeneous aromatic biopolymer assembled principally from p-coumaryl, coniferyl, and sinapyl alcohols, yielding H, G, and S structural units rather than one invariant molecular speci No ontology CURIE was proposed. Recorded as provenance only — no grounding applied from this run. Edison's recommendations are deliberately conservative, and a plausible identifier promoted by a mechanism that never decided anything is what #203 and #263 exist to undo. Any CURIE above is a curator's to accept or reject.
- Active SSSOM state: No active row for `MIM:BC_Lignin_Sorghum`, as expected for `UNMAPPED`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.
- The 2026-09-01 unmapped review explains the residual unmapped policy: named media, undefined mixtures, and exact single-ingredient residuals must stay unmapped until exact same-form evidence is available.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.
- Consequential unresolved item: Mixture/extract/preparation is intentionally left unmapped until the source supports a component decomposition or exact preparation identity.

## Findings

- **major**: `data/ingredients/unmapped/BC_Lignin_Sorghum.yaml` remains `UNMAPPED`; the label denotes a mixture, extract, or incompletely specified preparation. Do not exact-match it to a broader parent, component, hydrate, salt, or lookalike label.

## Recommended Edits

- Curate an exact same-form identity or decomposition for `data/ingredients/unmapped/BC_Lignin_Sorghum.yaml` before mapping it.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/unmapped/BC_Lignin_Sorghum.yaml`, `just validate-terms data/ingredients/unmapped/BC_Lignin_Sorghum.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/unmapped/BC_Lignin_Sorghum.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/unmapped/BC_Lignin_Sorghum.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
