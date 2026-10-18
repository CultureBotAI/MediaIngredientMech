# YAML Record Review: 3-Indolyl acetic acid

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/3-indolyl_Acetic_Acid.yaml`
- Started UTC: 2026-10-01T04:59:05Z
- Finished UTC: 2026-10-01T04:59:06Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/3-indolyl_Acetic_Acid.yaml`
- Identifier: `CHEBI:16411`
- Preferred term: 3-Indolyl acetic acid
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/3-indolyl_Acetic_Acid.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:16411`.
- Ontology label: `indole-3-acetic acid`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/3-indolyl_Acetic_Acid.md` after the record changed from 22148559e025f0af3a312d9add22048016742b39ab48fce002fcee0598f0f2d5 to c72fab92961e79927836c2873ef13c86121ee6b349f0d48ec916e518ede67feb; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `c72fab92961e79927836c2873ef13c86121ee6b349f0d48ec916e518ede67feb`.
- Previous review: `reports/yaml_record_review/3-indolyl_Acetic_Acid.md`.
- Previous record SHA-256: `22148559e025f0af3a312d9add22048016742b39ab48fce002fcee0598f0f2d5`.
- Source occurrence traceability: 6 occurrence(s) across 6 medium/media.
- Latest curation event: CORRECTED by retire_wrong_compound_synonyms at 2026-09-20T00:00:00Z: Marked 2 synonym(s) non-resolving: ['ethyl 2-hexenoate', 'ethyl hex-2-enoate']. ChEBI gives these names to CHEBI:87514, not to this record's CHEBI:16411 -- indole-3-acetic acid is not ethyl 2-hexenoate. Kept as REJECTED_LABEL so a rebuild cannot restore them from kg-microbe's synonym list (#669).
- Active SSSOM state: 1 active row(s) for `MIM:3-indolyl_Acetic_Acid`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/3-indolyl_Acetic_Acid.md` after the record changed from 22148559e025f0af3a312d9add22048016742b39ab48fce002fcee0598f0f2d5 to c72fab92961e79927836c2873ef13c86121ee6b349f0d48ec916e518ede67feb; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/3-indolyl_Acetic_Acid.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: Active CHEBI indole-3-acetic-acid identity, CAS, chemistry, occurrence count, SSSOM, and aggregate pass, but two exact synonyms still name the prior ethyl 2-hexenoate mapping.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/3-indolyl_Acetic_Acid.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/3-indolyl_Acetic_Acid.yaml`, `just validate-terms data/ingredients/mapped/3-indolyl_Acetic_Acid.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/3-indolyl_Acetic_Acid.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/3-indolyl_Acetic_Acid.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
