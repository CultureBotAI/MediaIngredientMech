# YAML Record Review: 6'-O-sialyllactose sodium salt

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml`
- Started UTC: 2026-10-01T05:01:10Z
- Finished UTC: 2026-10-01T05:01:11Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml`
- Identifier: `cas:157574-76-0`
- Preferred term: 6'-O-sialyllactose sodium salt
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:153372`.
- Ontology label: `5-acetamido-3,5-dideoxy-D-glycero-alpha-D-galacto-non-2-ulopyranonosyl-(2->6)-beta-D-galactopyranosyl-(1->4)-D-glucopyranose`.
- Mapping quality: `NARROW_MATCH`.
- Active SSSOM rows for this subject: 3.
- Identity judgement: Refreshed `reports/yaml_record_review/6-O-sialyllactose_Sodium_Salt.md` after the record changed from f2ddbc9dd0209c5ed904ebfa976bbc245cc84d951f57c4d0a91a6c10bad0ba41 to 252e3146582a0917fbc3827e3ef009885696d96a077b7f0ffdf48bd268cc598e; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `252e3146582a0917fbc3827e3ef009885696d96a077b7f0ffdf48bd268cc598e`.
- Previous review: `reports/yaml_record_review/6-O-sialyllactose_Sodium_Salt.md`.
- Previous record SHA-256: `f2ddbc9dd0209c5ed904ebfa976bbc245cc84d951f57c4d0a91a6c10bad0ba41`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: REGROUNDED_PARENT_TERM by claude at 2026-09-22T23:25:51.038995+00:00: broadMatch parent CHEBI:26714 ('sodium salt') -> CHEBI:153372 ('5-acetamido-3,5-dideoxy-D-glycero-alpha-D-galacto-non-2-ulopyranonosyl-(2->6)-beta-D-galactopyranosyl-(1->4)-D-glucopyranose') (#312). As for the 3'-isomer: CHEBI:26714 is the class of sodium salts. The label names 6'-sialyllactose, and CHEBI:153372 carries the related synonyms "6'-sialyllactose" and "6'SL"; it is the anomer-unspecified D-glucopyranose form, so it is the closest broader term for the salt. cas:157574-76-0 identity, NARROW_MATCH grade and both registry rows unchanged (Section 3 step 2, #245).
- Active SSSOM state: 3 active row(s) for `MIM:6-O-sialyllactose_Sodium_Salt`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/6-O-sialyllactose_Sodium_Salt.md` after the record changed from f2ddbc9dd0209c5ed904ebfa976bbc245cc84d951f57c4d0a91a6c10bad0ba41 to 252e3146582a0917fbc3827e3ef009885696d96a077b7f0ffdf48bd268cc598e; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/6-O-sialyllactose_Sodium_Salt.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The local CAS identity, PubChem chemistry, and registry rows pass, but the ChEBI parent is the generic sodium salt class, SSSOM exports an unrelated propionate label, and the carbon-source role is provisional.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/6-O-sialyllactose_Sodium_Salt.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml`, `just validate-terms data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
