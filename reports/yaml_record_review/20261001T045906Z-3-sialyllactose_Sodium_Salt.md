# YAML Record Review: 3'-sialyllactose sodium salt

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/3-sialyllactose_Sodium_Salt.yaml`
- Started UTC: 2026-10-01T04:59:06Z
- Finished UTC: 2026-10-01T04:59:07Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/3-sialyllactose_Sodium_Salt.yaml`
- Identifier: `cas:128596-80-5`
- Preferred term: 3'-sialyllactose sodium salt
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/3-sialyllactose_Sodium_Salt.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:151472`.
- Ontology label: `N-acetyl-alpha-neuraminyl-(2->3)-beta-D-galactosyl-(1->4)-D-glucose`.
- Mapping quality: `NARROW_MATCH`.
- Active SSSOM rows for this subject: 3.
- Identity judgement: Refreshed `reports/yaml_record_review/3-sialyllactose_Sodium_Salt.md` after the record changed from 56429ef25370e4fcf9496a5e4e8381515d809e658f8c2ae576b4fb1a192a097a to 790ac9da83e8e57aac81645c8e91a04392bba7a82523b80979af801e68ca84a0; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `790ac9da83e8e57aac81645c8e91a04392bba7a82523b80979af801e68ca84a0`.
- Previous review: `reports/yaml_record_review/3-sialyllactose_Sodium_Salt.md`.
- Previous record SHA-256: `56429ef25370e4fcf9496a5e4e8381515d809e658f8c2ae576b4fb1a192a097a`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: REGROUNDED_PARENT_TERM by claude at 2026-09-22T23:25:51.030915+00:00: broadMatch parent CHEBI:26714 ('sodium salt') -> CHEBI:151472 ('N-acetyl-alpha-neuraminyl-(2->3)-beta-D-galactosyl-(1->4)-D-glucose') (#312). CHEBI:26714 'sodium salt' is the class of all sodium salts: it keeps the counterion and discards the compound (#322). The label names 3'-sialyllactose, and ChEBI has it: CHEBI:151472 carries the related synonym "3'-sialyllactose" and xref cas:35890-38-1 (the free trisaccharide). The reground_compositional_classes NO_PARENT claim 'no sialyllactose term of any form' was false. cas:128596-80-5 identity, NARROW_MATCH grade and both registry rows unchanged (Section 3 step 2, #245).
- Active SSSOM state: 3 active row(s) for `MIM:3-sialyllactose_Sodium_Salt`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/3-sialyllactose_Sodium_Salt.md` after the record changed from 56429ef25370e4fcf9496a5e4e8381515d809e658f8c2ae576b4fb1a192a097a to 790ac9da83e8e57aac81645c8e91a04392bba7a82523b80979af801e68ca84a0; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/3-sialyllactose_Sodium_Salt.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: CAS-backed sodium-salt identity and PubChem chemistry pass, but the ChEBI parent is still generic sodium salt, SSSOM other carries a propionate label, and CARBON_SOURCE is provisional.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/3-sialyllactose_Sodium_Salt.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/3-sialyllactose_Sodium_Salt.yaml`, `just validate-terms data/ingredients/mapped/3-sialyllactose_Sodium_Salt.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/3-sialyllactose_Sodium_Salt.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/3-sialyllactose_Sodium_Salt.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
