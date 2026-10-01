# YAML Record Review: 2-chloro-4ethylamino-6-isopropylamino-1,3,5-triazine

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/2-chloro-4ethylamino-6-isopropylamino-135-triazine.yaml`
- Started UTC: 2026-10-01T04:59:01Z
- Finished UTC: 2026-10-01T04:59:02Z
- Verdict: pass_with_minor_issues

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/2-chloro-4ethylamino-6-isopropylamino-135-triazine.yaml`
- Identifier: `CHEBI:15930`
- Preferred term: 2-chloro-4ethylamino-6-isopropylamino-1,3,5-triazine
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/2-chloro-4ethylamino-6-isopropylamino-135-triazine.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:15930`.
- Ontology label: `atrazine`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/2-chloro-4ethylamino-6-isopropylamino-135-triazine.md` after the record changed from 5dbf00ae4cb7644279e476a238e3be0760a1b1e929b9faeeecd821f402b52a86 to 30705d7e1866a55fbcb9e5cba58f2ddd34e86073d5cb968bfaa332afab64151b; preserved the previous minor finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `30705d7e1866a55fbcb9e5cba58f2ddd34e86073d5cb968bfaa332afab64151b`.
- Previous review: `reports/yaml_record_review/2-chloro-4ethylamino-6-isopropylamino-135-triazine.md`.
- Previous record SHA-256: `5dbf00ae4cb7644279e476a238e3be0760a1b1e929b9faeeecd821f402b52a86`.
- Source occurrence traceability: 1 occurrence(s) across 1 medium/media.
- Latest curation event: MERGED_FROM_DUPLICATES by mim_semantic_review_20260921 at 2026-09-21T21:33:25.379198+00:00: Absorbed Atrazin. Atrazin is the atrazine name variant. Correct CAS is 1912-24-9; imported 1924-24-9 was erroneous. Survivor already has the exact atrazine ontology identity. Synonym dispositions and role evidence retained. Counts recomputed from distinct recipe membership where nonzero. Evidence: https://www.ebi.ac.uk/chebi/CHEBI:15930
- Active SSSOM state: 1 active row(s) for `MIM:2-chloro-4ethylamino-6-isopropylamino-135-triazine`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: None found.

## Findings

- **minor**: The previous finding set in `reports/yaml_record_review/2-chloro-4ethylamino-6-isopropylamino-135-triazine.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: Active CHEBI atrazine identity, CultureMech alias, SSSOM, aggregate, and docs pass; only stale advisory rows and optional chemistry enrichment remain.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/2-chloro-4ethylamino-6-isopropylamino-135-triazine.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/2-chloro-4ethylamino-6-isopropylamino-135-triazine.yaml`, `just validate-terms data/ingredients/mapped/2-chloro-4ethylamino-6-isopropylamino-135-triazine.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/2-chloro-4ethylamino-6-isopropylamino-135-triazine.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/2-chloro-4ethylamino-6-isopropylamino-135-triazine.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
