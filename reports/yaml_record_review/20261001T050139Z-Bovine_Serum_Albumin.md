# YAML Record Review: bovine serum albumin

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Bovine_Serum_Albumin.yaml`
- Started UTC: 2026-10-01T05:01:39Z
- Finished UTC: 2026-10-01T05:01:40Z
- Verdict: pass

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Bovine_Serum_Albumin.yaml`
- Identifier: `NCIT:C85253`
- Preferred term: bovine serum albumin
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Bovine_Serum_Albumin.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `NCIT:C85253`.
- Ontology label: `Bovine Serum Albumin`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Bovine_Serum_Albumin.md` after the record changed from 7ecc32dc73554cc43983799ebe63081b4a50285971ff6b9e8ec65cfc93ffd9b6 to 43ceecb07d1bfa49f863a4c9d2618c79f8ab93385a8752ea88f07a6924b0f094; no prior finding is carried forward.

## Evidence

- Current record SHA-256: `43ceecb07d1bfa49f863a4c9d2618c79f8ab93385a8752ea88f07a6924b0f094`.
- Previous review: `reports/yaml_record_review/Bovine_Serum_Albumin.md`.
- Previous record SHA-256: `7ecc32dc73554cc43983799ebe63081b4a50285971ff6b9e8ec65cfc93ffd9b6`.
- Source occurrence traceability: 7 occurrence(s) across 7 medium/media.
- Latest curation event: CORRECTED by kgmicrobe_identity_review_20260924 at 2026-09-24T07:10:47.880128+00:00: Review the generic bovine albumin ingredient at NCIT:C85253. FDA qualifies CAS 9048-46-8 as GENERIC (FAMILY). Retain source Sigma A7030 and other recipe-specific fraction V/products as supplied forms, not exact synonyms. Preserve all seven original recipe memberships and their preparation qualifiers.
- Active SSSOM state: 1 active row(s) for `MIM:Bovine_Serum_Albumin`.
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

- Re-run strict schema validation on `data/ingredients/mapped/Bovine_Serum_Albumin.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Bovine_Serum_Albumin.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
