# YAML Record Review: a-Ketoglutaric acid disodium salt hydrate

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/A-Ketoglutaric_Acid_Disodium_Salt_Hydrate.yaml`
- Started UTC: 2026-10-01T05:01:11Z
- Finished UTC: 2026-10-01T05:01:12Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/A-Ketoglutaric_Acid_Disodium_Salt_Hydrate.yaml`
- Identifier: `cas:305-72-6`
- Preferred term: a-Ketoglutaric acid disodium salt hydrate
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/A-Ketoglutaric_Acid_Disodium_Salt_Hydrate.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:30915`.
- Ontology label: `2-oxoglutaric acid`.
- Mapping quality: `CLOSE_MATCH`.
- Active SSSOM rows for this subject: 2.
- Identity judgement: Refreshed `reports/yaml_record_review/A-Ketoglutaric_Acid_Disodium_Salt_Hydrate.md` after the record changed from 09dcea028f806cc4d490096bd79e8e1391c27d23ff523f97e732016ab83f0450 to bc096f0393d86296abd52781a877b306d64b8830a026b73df84a27508e4c846c; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `bc096f0393d86296abd52781a877b306d64b8830a026b73df84a27508e4c846c`.
- Previous review: `reports/yaml_record_review/A-Ketoglutaric_Acid_Disodium_Salt_Hydrate.md`.
- Previous record SHA-256: `09dcea028f806cc4d490096bd79e8e1391c27d23ff523f97e732016ab83f0450`.
- Source occurrence traceability: 11 occurrence(s) across 11 medium/media.
- Latest curation event: REJECTED_WRONG_FORM_SYNONYMS by claude at 2026-09-23T06:21:57.287844+00:00: Retyped REJECTED_LABEL: 'a-Ketoglutaric acid' (EXACT_SYNONYM): names the free acid (Alpha-ketoglutaric_Acid holds it), not the disodium salt hydrate (#232). The token is kept as provenance only; it must not resolve, be exported, or enter the SSSOM other column.
- Active SSSOM state: 2 active row(s) for `MIM:A-Ketoglutaric_Acid_Disodium_Salt_Hydrate`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/A-Ketoglutaric_Acid_Disodium_Salt_Hydrate.md` after the record changed from 09dcea028f806cc4d490096bd79e8e1391c27d23ff523f97e732016ab83f0450 to bc096f0393d86296abd52781a877b306d64b8830a026b73df84a27508e4c846c; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/A-Ketoglutaric_Acid_Disodium_Salt_Hydrate.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The CAS identity and close anhydrous-acid match are intentionally preserved, but the chemistry lacks hydrate water, a neutral-acid label is exported as exact other, and the roles are provisional.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/A-Ketoglutaric_Acid_Disodium_Salt_Hydrate.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/A-Ketoglutaric_Acid_Disodium_Salt_Hydrate.yaml`, `just validate-terms data/ingredients/mapped/A-Ketoglutaric_Acid_Disodium_Salt_Hydrate.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/A-Ketoglutaric_Acid_Disodium_Salt_Hydrate.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/A-Ketoglutaric_Acid_Disodium_Salt_Hydrate.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
