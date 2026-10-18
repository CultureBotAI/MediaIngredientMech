# YAML Record Review: 4-Hydroxynonenal

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/4-Hydroxynonenal.yaml`
- Started UTC: 2026-10-01T05:01:05Z
- Finished UTC: 2026-10-01T05:01:06Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/4-Hydroxynonenal.yaml`
- Identifier: `CHEBI:58968`
- Preferred term: 4-Hydroxynonenal
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/4-Hydroxynonenal.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:58968`.
- Ontology label: `(E)-4-hydroxynon-2-enal`.
- Mapping quality: `CAS_RN_LOOKUP`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/4-Hydroxynonenal.md` after the record changed from bae45d2ab0f6bdf92477de089014bf8fee6c4deb7bbba9cde2d66e7e6e1ca4b7 to 48bbdf4756b18d395bcec9494331923d9fce646b3fc5d64da37d11e0b908617d; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `48bbdf4756b18d395bcec9494331923d9fce646b3fc5d64da37d11e0b908617d`.
- Previous review: `reports/yaml_record_review/4-Hydroxynonenal.md`.
- Previous record SHA-256: `bae45d2ab0f6bdf92477de089014bf8fee6c4deb7bbba9cde2d66e7e6e1ca4b7`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: REGROUNDED_IDENTITY by claude at 2026-09-23T00:44:54.402559+00:00: identifier CHEBI:142593 -> CHEBI:58968; ontology CHEBI:142593 ('4-hydroxynonenal') -> CHEBI:58968 ('(E)-4-hydroxynon-2-enal'); mapping_quality EXACT_MATCH -> CAS_RN_LOOKUP. CHEBI:142593 '4-hydroxynonenal' is a class (definition: double bond 'at any position'; wildcard SMILES '*C([H])=O', which had been copied into the record; no InChIKey, no CAS). The record has carried CAS 75899-68-2 since creation; PubChem resolves it to CID 5283344 with InChIKey JVJFIQYAHPMBBX-FNORWQNLSA-N, which is CHEBI:58968 '(E)-4-hydroxynon-2-enal' (synonyms '4-hydroxynonenal', 'HNE'). Section 3 step 4's evidence hatch: the CAS picks the member. Structure fields refreshed from the term. (#312)
- Active SSSOM state: 1 active row(s) for `MIM:4-Hydroxynonenal`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/4-Hydroxynonenal.md` after the record changed from bae45d2ab0f6bdf92477de089014bf8fee6c4deb7bbba9cde2d66e7e6e1ca4b7 to 48bbdf4756b18d395bcec9494331923d9fce646b3fc5d64da37d11e0b908617d; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/4-Hydroxynonenal.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The active CHEBI grounding and formula are plausible, but the record stores a wildcard aldehyde-fragment SMILES while carrying a CAS that resolves to a specific 4-hydroxy-2E-nonenal.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/4-Hydroxynonenal.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/4-Hydroxynonenal.yaml`, `just validate-terms data/ingredients/mapped/4-Hydroxynonenal.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/4-Hydroxynonenal.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/4-Hydroxynonenal.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
