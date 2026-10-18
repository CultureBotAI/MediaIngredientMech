# YAML Record Review: Wako Isomaltooligosaccharides

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/unmapped/Wako_Isomaltooligosaccharides.yaml`
- Started UTC: 2026-10-01T04:50:27Z
- Finished UTC: 2026-10-01T04:50:28Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/unmapped/Wako_Isomaltooligosaccharides.yaml`
- Identifier: `UNMAPPED_0222`
- Preferred term: Wako Isomaltooligosaccharides
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

- Current record SHA-256: `b22cfaa5abee26bea34abd644b275e112aa3067e3de37d0190477c6c1462131a`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: ANNOTATED by edison_literature_identity at 2026-08-06T00:00:00+00:00: Edison LITERATURE (PaperQA3) identity research; report at research/ingredients/Wako_Isomaltooligosaccharides-edison-literature.md (local artifact — research/ is gitignored, so the findings are quoted here rather than linked). Report verdict: **Recommended interpretation:** a **supplier-qualified, compositionally undefined isomaltooligosaccharide (IMO) preparation**, not a single chemical. The “Wako” qualifier likely denotes the supplier associated with the source material, but the retrieved evidence did not resolve a catalog number, grade, product name, certificate of analysis, or fixed formulation. Therefore, the record should not be CURIEs discussed: MESH:D009842, MESH:D058407. Recorded as provenance only — no grounding applied from this run. Edison's recommendations are deliberately conservative, and a plausible identifier promoted by a mechanism that never decided anything is what #203 and #263 exist to undo. Any CURIE above is a curator's to accept or reject.
- Active SSSOM state: No active row for `MIM:Wako_Isomaltooligosaccharides`, as expected for `UNMAPPED`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.
- The 2026-09-01 unmapped review explains the residual unmapped policy: named media, undefined mixtures, and exact single-ingredient residuals must stay unmapped until exact same-form evidence is available.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.
- Consequential unresolved item: Mixture/extract/preparation is intentionally left unmapped until the source supports a component decomposition or exact preparation identity.

## Findings

- **major**: `data/ingredients/unmapped/Wako_Isomaltooligosaccharides.yaml` remains `UNMAPPED`; the label denotes a mixture, extract, or incompletely specified preparation. Do not exact-match it to a broader parent, component, hydrate, salt, or lookalike label.

## Recommended Edits

- Curate an exact same-form identity or decomposition for `data/ingredients/unmapped/Wako_Isomaltooligosaccharides.yaml` before mapping it.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/unmapped/Wako_Isomaltooligosaccharides.yaml`, `just validate-terms data/ingredients/unmapped/Wako_Isomaltooligosaccharides.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/unmapped/Wako_Isomaltooligosaccharides.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/unmapped/Wako_Isomaltooligosaccharides.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
