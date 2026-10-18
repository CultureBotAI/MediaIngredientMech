# YAML Record Review: Glutamyl-glutamic Acid

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Glutamyl-glutamic_Acid.yaml`
- Started UTC: 2026-10-01T05:02:24Z
- Finished UTC: 2026-10-01T05:02:25Z
- Verdict: pass_with_minor_issues

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Glutamyl-glutamic_Acid.yaml`
- Identifier: `CHEBI:5390`
- Preferred term: Glutamyl-glutamic Acid
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Glutamyl-glutamic_Acid.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:5390`.
- Ontology label: `Glu-Glu`.
- Mapping quality: `CLOSE_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Glutamyl-glutamic_Acid.md` after the record changed from 57328349e1b7e7b920db30865d254915a749ed26b651a8e4c7b4fa30b6a4095b to 780086a8bc4e2780898c53f5b6ae7d24ebf6f34f305e8714e1e02093180a6f1b; preserved the previous minor finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `780086a8bc4e2780898c53f5b6ae7d24ebf6f34f305e8714e1e02093180a6f1b`.
- Previous review: `reports/yaml_record_review/Glutamyl-glutamic_Acid.md`.
- Previous record SHA-256: `57328349e1b7e7b920db30865d254915a749ed26b651a8e4c7b4fa30b6a4095b`.
- Source occurrence traceability: 0 active occurrence(s) across 0 medium/media; source rows: microbedecoder: 3.
- Latest curation event: REGRADED_MAPPING_QUALITY by claude at 2026-09-22T23:25:51.005485+00:00: mapping_quality SYNONYM_MATCH -> CLOSE_MATCH (#312). 'Glutamyl-glutamic Acid' is not a name on CHEBI:5390 (its names are Glu-Glu and L-alpha-glutamyl-L-glutamic acid). The term is alpha-linked and L,L-specific; the label states neither, and the gamma isomer is the separate term CHEBI:73705. The alpha/L,L reading was supplied by peptide-nomenclature convention, so Section 0 grades it CLOSE_MATCH. Identifier unchanged; own-identifier row stays exactMatch.
- Active SSSOM state: 1 active row(s) for `MIM:Glutamyl-glutamic_Acid`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: None found.

## Findings

- **minor**: The previous finding set in `reports/yaml_record_review/Glutamyl-glutamic_Acid.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The Glu-Glu synonym match and final SSSOM row pass, but the stale top-level note needs cleanup.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Glutamyl-glutamic_Acid.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Glutamyl-glutamic_Acid.yaml`, `just validate-terms data/ingredients/mapped/Glutamyl-glutamic_Acid.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Glutamyl-glutamic_Acid.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Glutamyl-glutamic_Acid.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
