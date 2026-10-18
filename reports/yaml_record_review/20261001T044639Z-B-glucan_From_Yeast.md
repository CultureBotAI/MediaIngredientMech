# YAML Record Review: B-glucan from yeast

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/unmapped/B-glucan_From_Yeast.yaml`
- Started UTC: 2026-10-01T04:46:39Z
- Finished UTC: 2026-10-01T04:46:40Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/unmapped/B-glucan_From_Yeast.yaml`
- Identifier: `UNMAPPED_0235`
- Preferred term: B-glucan from yeast
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

- Current record SHA-256: `0f4d1e87026ec3ae39c3eeb10a84750ff1fd021c361011220ba2917956f982ea`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: ANNOTATED by edison_literature_identity at 2026-08-06T00:00:00+00:00: Edison LITERATURE (PaperQA3) identity research; report at research/ingredients/B-glucan_from_yeast-edison-literature.md (local artifact — research/ is gitignored, so the findings are quoted here rather than linked). Report verdict: **Recommended interpretation:** a **source-defined polysaccharide family/preparation**, not a single chemical, salt, hydrate, buffer, or uniquely specified commercial formulation. The normalized label should be **“β-glucan from yeast”** or **“yeast β-glucan.”** In the common *Saccharomyces cerevisiae* context, the material is dominated by β-(1→3)-D-glucan chains together with β-(1→6)-linked branch CURIEs discussed: MESH:D001812. Recorded as provenance only — no grounding applied from this run. Edison's recommendations are deliberately conservative, and a plausible identifier promoted by a mechanism that never decided anything is what #203 and #263 exist to undo. Any CURIE above is a curator's to accept or reject.
- Active SSSOM state: No active row for `MIM:B-glucan_From_Yeast`, as expected for `UNMAPPED`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.
- The 2026-09-01 unmapped review explains the residual unmapped policy: named media, undefined mixtures, and exact single-ingredient residuals must stay unmapped until exact same-form evidence is available.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.
- Consequential unresolved item: Mixture/extract/preparation is intentionally left unmapped until the source supports a component decomposition or exact preparation identity.

## Findings

- **major**: `data/ingredients/unmapped/B-glucan_From_Yeast.yaml` remains `UNMAPPED`; the label denotes a mixture, extract, or incompletely specified preparation. Do not exact-match it to a broader parent, component, hydrate, salt, or lookalike label.

## Recommended Edits

- Curate an exact same-form identity or decomposition for `data/ingredients/unmapped/B-glucan_From_Yeast.yaml` before mapping it.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/unmapped/B-glucan_From_Yeast.yaml`, `just validate-terms data/ingredients/unmapped/B-glucan_From_Yeast.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/unmapped/B-glucan_From_Yeast.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/unmapped/B-glucan_From_Yeast.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
