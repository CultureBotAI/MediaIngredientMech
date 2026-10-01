# YAML Record Review: 5-Hydroxydodecanoate

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/5-Hydroxydodecanoate.yaml`
- Started UTC: 2026-10-01T05:01:09Z
- Finished UTC: 2026-10-01T05:01:10Z
- Verdict: pass

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/5-Hydroxydodecanoate.yaml`
- Identifier: `CHEBI:195418`
- Preferred term: 5-Hydroxydodecanoate
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/5-Hydroxydodecanoate.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:195418`.
- Ontology label: `5-hydroxylaurate`.
- Mapping quality: `SYNONYM_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/5-Hydroxydodecanoate.md` after the record changed from 13177c872b3d36f38f0f9031617feb070324fed1ff05c6e21f1223ca3b7262c8 to 8581590274f3cd14a09a221558cc957aedf50ae833699b9b9ec8237484942253; no prior finding is carried forward.

## Evidence

- Current record SHA-256: `8581590274f3cd14a09a221558cc957aedf50ae833699b9b9ec8237484942253`.
- Previous review: `reports/yaml_record_review/5-Hydroxydodecanoate.md`.
- Previous record SHA-256: `13177c872b3d36f38f0f9031617feb070324fed1ff05c6e21f1223ca3b7262c8`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: REGRADED_MAPPING_QUALITY by claude at 2026-09-22T23:25:50.793291+00:00: mapping_quality EXACT_MATCH -> SYNONYM_MATCH (#312). The label '5-Hydroxydodecanoate' resolves through the ChEBI related synonym '5-hydroxydodecanoate'; the primary label is '5-hydroxylaurate'. Section 0: a resolution through a unique ontology synonym is SYNONYM_MATCH, not EXACT_MATCH. Identifier and term unchanged; the own-identifier row stays skos:exactMatch (Rule D).
- Active SSSOM state: 1 active row(s) for `MIM:5-Hydroxydodecanoate`.
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

- Re-run strict schema validation on `data/ingredients/mapped/5-Hydroxydodecanoate.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/5-Hydroxydodecanoate.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
