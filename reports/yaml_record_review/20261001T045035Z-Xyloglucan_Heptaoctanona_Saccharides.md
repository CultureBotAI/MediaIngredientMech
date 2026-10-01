# YAML Record Review: Xyloglucan (hepta+octa+nona saccharides)

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/unmapped/Xyloglucan_Heptaoctanona_Saccharides.yaml`
- Started UTC: 2026-10-01T04:50:35Z
- Finished UTC: 2026-10-01T04:50:36Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/unmapped/Xyloglucan_Heptaoctanona_Saccharides.yaml`
- Identifier: `UNMAPPED_0174`
- Preferred term: Xyloglucan (hepta+octa+nona saccharides)
- Mapping status: `UNMAPPED`
- Ingredient type: `UNDEFINED_MIXTURE`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/unmapped data/ingredients/mapped/Na2-citrate.yaml data/ingredients/mapped/Nitrilotriacetic_Acid_Trisodium_Salt.yaml --out /tmp/mim_remaining_review_validation.tsv --workers 4 --quiet`; 275 files scanned and 0 ERROR rows.
- Passed: `just validate-terms data/ingredients/unmapped/Xyloglucan_Heptaoctanona_Saccharides.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `UNMAPPED`.
- Ontology ID: `CHEBI:18233`.
- Ontology label: `xyloglucan`.
- Mapping quality: `NARROW_MATCH`.
- Active SSSOM rows for this subject: 0.
- Identity judgement: Mixture/extract/preparation is intentionally left unmapped until the source supports a component decomposition or exact preparation identity.

## Evidence

- Current record SHA-256: `295bf2d993db3c5a5090a1619dbf750bf652ff11d41a43ee388740aaeb9ac834`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: ANNOTATED by edison_literature_identity at 2026-08-06T00:00:00+00:00: Edison LITERATURE (PaperQA3) identity research; report at research/ingredients/Xyloglucan_heptaoctanona_saccharides-edison-literature.md (local artifact — research/ is gitignored, so the findings are quoted here rather than linked). Report verdict: **Recommended interpretation:** a preparation-defined mixture/fraction of xyloglucan-derived oligosaccharides, not a single chemical and not generic polymeric xyloglucan. Complete EG-II digestion of partially purified tamarind xyloglucan yielded four principal products—XXXG, XLXG, XXLG, and XLLG—and the isolated fraction was described as containing oligosaccharides of 7–9 residues. (marry2003struc CURIEs discussed: CHEBI:18233. Recorded as provenance only — no grounding applied from this run. Edison's recommendations are deliberately conservative, and a plausible identifier promoted by a mechanism that never decided anything is what #203 and #263 exist to undo. Any CURIE above is a curator's to accept or reject.
- Active SSSOM state: No active row for `MIM:Xyloglucan_Heptaoctanona_Saccharides`, as expected for `UNMAPPED`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.
- The 2026-09-01 unmapped review explains the residual unmapped policy: named media, undefined mixtures, and exact single-ingredient residuals must stay unmapped until exact same-form evidence is available.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.
- Consequential unresolved item: Mixture/extract/preparation is intentionally left unmapped until the source supports a component decomposition or exact preparation identity.

## Findings

- **major**: `data/ingredients/unmapped/Xyloglucan_Heptaoctanona_Saccharides.yaml` remains `UNMAPPED`; the label denotes a mixture, extract, or incompletely specified preparation. Do not exact-match it to a broader parent, component, hydrate, salt, or lookalike label.

## Recommended Edits

- Curate an exact same-form identity or decomposition for `data/ingredients/unmapped/Xyloglucan_Heptaoctanona_Saccharides.yaml` before mapping it.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/unmapped/Xyloglucan_Heptaoctanona_Saccharides.yaml`, `just validate-terms data/ingredients/unmapped/Xyloglucan_Heptaoctanona_Saccharides.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/unmapped/Xyloglucan_Heptaoctanona_Saccharides.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/unmapped/Xyloglucan_Heptaoctanona_Saccharides.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
