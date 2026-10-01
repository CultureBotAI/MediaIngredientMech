# YAML Record Review: Locust bean gum

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Locust_Bean_Gum.yaml`
- Started UTC: 2026-10-01T05:02:40Z
- Finished UTC: 2026-10-01T05:02:41Z
- Verdict: pass

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Locust_Bean_Gum.yaml`
- Identifier: `FOODON:03413132`
- Preferred term: Locust bean gum
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Locust_Bean_Gum.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `FOODON:03413132`.
- Ontology label: `locust bean gum`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Locust_Bean_Gum.md` after the record changed from f2a0a6b6de77bf5012b7d53c6809b4e44ac89b0e1e5b43202f5ab65673ceeca0 to 973e02f8ba4ad966f8fc9acf5174d47f9aa6cc17c9f45afb632c6e9776276cfd; no prior finding is carried forward.

## Evidence

- Current record SHA-256: `973e02f8ba4ad966f8fc9acf5174d47f9aa6cc17c9f45afb632c6e9776276cfd`.
- Previous review: `reports/yaml_record_review/Locust_Bean_Gum.md`.
- Previous record SHA-256: `f2a0a6b6de77bf5012b7d53c6809b4e44ac89b0e1e5b43202f5ab65673ceeca0`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: CORRECTED by kgmicrobe_identity_review_20260924 at 2026-09-24T07:10:47.886428+00:00: Source Sigma G0753, JECFA INS 410 and FoodOn identify the same generic seed-derived locust/carob gum. Retain the supplier and original autoclaved qualifier in supplied_form notes; it is not an exact synonym or evidence for clarified gum.
- Active SSSOM state: 1 active row(s) for `MIM:Locust_Bean_Gum`.
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

- Re-run strict schema validation on `data/ingredients/mapped/Locust_Bean_Gum.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Locust_Bean_Gum.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
