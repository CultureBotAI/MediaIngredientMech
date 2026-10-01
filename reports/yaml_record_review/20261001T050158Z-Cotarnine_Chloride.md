# YAML Record Review: Cotarnine Chloride

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Cotarnine_Chloride.yaml`
- Started UTC: 2026-10-01T05:01:58Z
- Finished UTC: 2026-10-01T05:01:59Z
- Verdict: pass

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Cotarnine_Chloride.yaml`
- Identifier: `NCIT:C79997`
- Preferred term: Cotarnine Chloride
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Cotarnine_Chloride.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `NCIT:C79997`.
- Ontology label: `Cotarnine Chloride`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Cotarnine_Chloride.md` after the record changed from 09e9f1b848eeee6d7a10e92b38f7b7941b6f3342c4b00f7181b90c4c7c6b2863 to 821fd7dd0dd3c8308727c3e6a4999c860eb6be69a42d6bb996b6d3a94b2a4860; no prior finding is carried forward.

## Evidence

- Current record SHA-256: `821fd7dd0dd3c8308727c3e6a4999c860eb6be69a42d6bb996b6d3a94b2a4860`.
- Previous review: `reports/yaml_record_review/Cotarnine_Chloride.md`.
- Previous record SHA-256: `09e9f1b848eeee6d7a10e92b38f7b7941b6f3342c4b00f7181b90c4c7c6b2863`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: CORRECTED by kgmicrobe_identity_review_20260924 at 2026-09-24T07:10:47.883058+00:00: Source CAS, NCIT and FDA 03F6B8N3QN agree on the 1:1 cotarninium chloride salt. Preserve that salt, not free cotarnine or its isolated cation.
- Active SSSOM state: 1 active row(s) for `MIM:Cotarnine_Chloride`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: None found.

## Findings

None found.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Cotarnine_Chloride.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Cotarnine_Chloride.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
