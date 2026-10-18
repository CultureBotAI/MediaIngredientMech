# YAML Record Review: poly(L-lysine) polymer

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Poly_L-lysine_Polymer.yaml`
- Started UTC: 2026-10-01T05:03:10Z
- Finished UTC: 2026-10-01T05:03:11Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Poly_L-lysine_Polymer.yaml`
- Identifier: `CHEBI:61490`
- Preferred term: poly(L-lysine) polymer
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Poly_L-lysine_Polymer.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:61490`.
- Ontology label: `poly(L-lysine) polymer`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Poly_L-lysine_Polymer.md` after the record changed from 78eed5f98aeb1643c346cf7dab73b62c176808a283ea24398acaa913bbb28de6 to ed9c38b708f8ebda2e72d8abf682816c3d9ace52dd7d8ab3cafdac68e82e6f75; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `ed9c38b708f8ebda2e72d8abf682816c3d9ace52dd7d8ab3cafdac68e82e6f75`.
- Previous review: `reports/yaml_record_review/Poly_L-lysine_Polymer.md`.
- Previous record SHA-256: `78eed5f98aeb1643c346cf7dab73b62c176808a283ea24398acaa913bbb28de6`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: REJECTED_TRAIT_SYNONYMS by claude at 2026-09-22T06:14:49.563933+00:00: Retyped activity/assay phrases as provenance-only REJECTED_LABEL because they describe a process or organism trait, not an ingredient name (#703): 'produces: poly(L-lysine) polymer'. Preserved original text and source metadata. No identity, mapping, role, or remaining-synonym claim was adjudicated.
- Active SSSOM state: 1 active row(s) for `MIM:Poly_L-lysine_Polymer`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Poly_L-lysine_Polymer.md` after the record changed from 78eed5f98aeb1643c346cf7dab73b62c176808a283ea24398acaa913bbb28de6 to ed9c38b708f8ebda2e72d8abf682816c3d9ace52dd7d8ab3cafdac68e82e6f75; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Poly_L-lysine_Polymer.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The exact CHEBI:61490 identity passes, but final SSSOM still exports a process-qualified produces token.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Poly_L-lysine_Polymer.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Poly_L-lysine_Polymer.yaml`, `just validate-terms data/ingredients/mapped/Poly_L-lysine_Polymer.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Poly_L-lysine_Polymer.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Poly_L-lysine_Polymer.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
