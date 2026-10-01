# YAML Record Review: 3,4'-Dihydroxyflavone

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/34-Dihydroxyflavone.yaml`
- Started UTC: 2026-10-01T05:01:04Z
- Finished UTC: 2026-10-01T05:01:05Z
- Verdict: pass_with_minor_issues

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/34-Dihydroxyflavone.yaml`
- Identifier: `mesh:C559991`
- Preferred term: 3,4'-Dihydroxyflavone
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/34-Dihydroxyflavone.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `mesh:C559991`.
- Ontology label: `3,4'-dihydroxyflavone`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 3.
- Identity judgement: Refreshed `reports/yaml_record_review/34-Dihydroxyflavone.md` after the record changed from 296ec518f7547378fac65ffb57f20aaccb83f94fd42194c239a32d25ee5954a7 to dbe304ccf30a76bb3aa1bcafc14c249fe2854bdebd3991a88ddf1e847163b33f; preserved the previous minor finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `dbe304ccf30a76bb3aa1bcafc14c249fe2854bdebd3991a88ddf1e847163b33f`.
- Previous review: `reports/yaml_record_review/34-Dihydroxyflavone.md`.
- Previous record SHA-256: `296ec518f7547378fac65ffb57f20aaccb83f94fd42194c239a32d25ee5954a7`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: REGRADED_PARENT_TO_IDENTITY by claude at 2026-09-23T00:44:54.166138+00:00: identifier cas:14919-49-4 -> mesh:C559991; ontology mesh:C559991 ('3,4'-dihydroxyflavone') -> mesh:C559991 ('3,4'-dihydroxyflavone'); mapping_quality NARROW_MATCH -> EXACT_MATCH. mesh.db gives MESH:C559991 the label "3,4'-dihydroxyflavone", identical to the record's label and distinct from MESH:C028288 "3',4'-dihydroxyflavone". chebi.db has no term for this compound (CAS 14919-49-4 and the name resolve to nothing). A broadMatch from a record to the same compound is false; Section 3 step 1 makes the MeSH term the identifier (68 records already carry mesh: primaries) with EXACT_MATCH. The CAS stays in chemical_properties and on its registry row; the kgmicrobe.compound row is dropped as #326 did for 72-Dihydroxyflavone. (#312)
- Active SSSOM state: 3 active row(s) for `MIM:34-Dihydroxyflavone`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: None found.

## Findings

- **minor**: The previous finding set in `reports/yaml_record_review/34-Dihydroxyflavone.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: CAS-backed 3,4'-Dihydroxyflavone identity, MeSH parent, registry rows, chemistry, SSSOM, and aggregate pass; only stale prefix-validator advisory rows remain.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/34-Dihydroxyflavone.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/34-Dihydroxyflavone.yaml`, `just validate-terms data/ingredients/mapped/34-Dihydroxyflavone.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/34-Dihydroxyflavone.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/34-Dihydroxyflavone.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
