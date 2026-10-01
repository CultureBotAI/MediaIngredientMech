# YAML Record Review: Arabinoxylan (Rye Flour)

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Arabinoxylan_Rye_Flour.yaml`
- Started UTC: 2026-10-01T05:01:26Z
- Finished UTC: 2026-10-01T05:01:27Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Arabinoxylan_Rye_Flour.yaml`
- Identifier: `kgmicrobe.ingredient:arabinoxylan_rye_flour`
- Preferred term: Arabinoxylan (Rye Flour)
- Mapping status: `MAPPED`
- Ingredient type: `UNDEFINED_MIXTURE`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Arabinoxylan_Rye_Flour.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `kgmicrobe.ingredient:arabinoxylan_rye_flour`.
- Ontology label: `Arabinoxylan (Rye Flour)`.
- Mapping quality: `FALLBACK_REGISTRY`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Arabinoxylan_Rye_Flour.md` after the record changed from 0fa877c442c77b43f94f673b3009f8a9bbf22c28374e4ffa7223216a091a76f7 to eed0ccdc99fba905c26e90c39684cfa8a0682cc9909ec94e2fac40e33e734adf; preserved the previous blocker finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `eed0ccdc99fba905c26e90c39684cfa8a0682cc9909ec94e2fac40e33e734adf`.
- Previous review: `reports/yaml_record_review/Arabinoxylan_Rye_Flour.md`.
- Previous record SHA-256: `0fa877c442c77b43f94f673b3009f8a9bbf22c28374e4ffa7223216a091a76f7`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: CORRECTED by mim_semantic_review_20260921 at 2026-09-21T21:33:25.379198+00:00: The named rye-derived arabinoxylan material is not rye flour FOODON:03302492. A manufacturer uses exactly this name for an arabinoxylan preparation with residual protein/ash. Retain a local material identity, without asserting procurement from that supplier, exact purity, or whole-mixture equivalence to pure polymer. Evidence: https://www.megazyme.com/arabinoxylan-rye-flour
- Active SSSOM state: 1 active row(s) for `MIM:Arabinoxylan_Rye_Flour`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Arabinoxylan_Rye_Flour.md` after the record changed from 0fa877c442c77b43f94f673b3009f8a9bbf22c28374e4ffa7223216a091a76f7 to eed0ccdc99fba905c26e90c39684cfa8a0682cc9909ec94e2fac40e33e734adf; preserved the previous blocker finding floor pending targeted retirement.

## Findings

- **blocker**: The previous finding set in `reports/yaml_record_review/Arabinoxylan_Rye_Flour.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The active FoodOn identifier and SSSOM exactMatch denote rye flour rather than the arabinoxylan ingredient.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Arabinoxylan_Rye_Flour.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Arabinoxylan_Rye_Flour.yaml`, `just validate-terms data/ingredients/mapped/Arabinoxylan_Rye_Flour.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Arabinoxylan_Rye_Flour.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Arabinoxylan_Rye_Flour.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
