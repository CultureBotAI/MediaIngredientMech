# YAML Record Review: DL-2-Aminoadipic acid

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml`
- Started UTC: 2026-10-01T05:02:08Z
- Finished UTC: 2026-10-01T05:02:09Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml`
- Identifier: `cas:542-32-5`
- Preferred term: DL-2-Aminoadipic acid
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `cas:542-32-5`.
- Ontology label: `DL-2-Aminoadipic acid`.
- Mapping quality: `FALLBACK_REGISTRY`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/DL-2-Aminoadipic_Acid.md` after the record changed from 35142da6bf1867b5b00847f2334a6fa7380af1f43a215bfe701f4e1118f30dc4 to fa26e653b29c8d1aeeaea8a1feee468acaa737cb322b9b525eb454c8e5604d7e; preserved the previous blocker finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `fa26e653b29c8d1aeeaea8a1feee468acaa737cb322b9b525eb454c8e5604d7e`.
- Previous review: `reports/yaml_record_review/DL-2-Aminoadipic_Acid.md`.
- Previous record SHA-256: `35142da6bf1867b5b00847f2334a6fa7380af1f43a215bfe701f4e1118f30dc4`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: CORRECTED by mim_semantic_review_20260921 at 2026-09-21T21:33:25.379198+00:00: Retain the explicitly DL source substance as CAS 542-32-5. Withdraw L-enantiomer CHEBI:37023 and its stereospecific synonym/structure; a racemate is not one enantiomer. CAS registry identity does not imply that a new exact ChEBI search was exhaustive. Evidence: https://www.sigmaaldrich.com/DE/en/product/sial/52458
- Active SSSOM state: 1 active row(s) for `MIM:DL-2-Aminoadipic_Acid`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/DL-2-Aminoadipic_Acid.md` after the record changed from 35142da6bf1867b5b00847f2334a6fa7380af1f43a215bfe701f4e1118f30dc4 to fa26e653b29c8d1aeeaea8a1feee468acaa737cb322b9b525eb454c8e5604d7e; preserved the previous blocker finding floor pending targeted retirement.

## Findings

- **blocker**: The previous finding set in `reports/yaml_record_review/DL-2-Aminoadipic_Acid.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The DL record is still exact-mapped to the L-enantiomer and exports an L-specific SSSOM synonym.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/DL-2-Aminoadipic_Acid.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml`, `just validate-terms data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
