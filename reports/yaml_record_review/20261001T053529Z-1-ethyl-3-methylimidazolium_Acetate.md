# YAML Record Review: 1-ethyl-3-methylimidazolium acetate

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/1-ethyl-3-methylimidazolium_Acetate.yaml`
- Started UTC: 2026-10-01T05:35:29Z
- Finished UTC: 2026-10-01T05:35:30Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/1-ethyl-3-methylimidazolium_Acetate.yaml`
- Identifier: `cas:143314-17-4`
- Preferred term: 1-ethyl-3-methylimidazolium acetate
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/1-ethyl-3-methylimidazolium_Acetate.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:63895`.
- Ontology label: `ionic liquid`.
- Mapping quality: `NARROW_MATCH`.
- Active SSSOM rows for this subject: 3.
- Identity judgement: Refreshed `reports/yaml_record_review/1-ethyl-3-methylimidazolium_Acetate.md` after the record changed from 0406799826473dee458b6358022420cc7555ba9ee3fbbd2e0b7689cde32fa6d5 to 38814f2038706907038c87a8bff6785abaf177e4746c63ddfae6fcb8836acda5; preserved the previous minor finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `38814f2038706907038c87a8bff6785abaf177e4746c63ddfae6fcb8836acda5`.
- Previous review: `reports/yaml_record_review/1-ethyl-3-methylimidazolium_Acetate.md`.
- Previous record SHA-256: `0406799826473dee458b6358022420cc7555ba9ee3fbbd2e0b7689cde32fa6d5`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: REGROUNDED_PARENT_TERM by claude at 2026-09-22T23:25:51.013985+00:00: broadMatch parent CHEBI:61326 ('1-ethyl-3-methylimidazolium') -> CHEBI:63895 ('ionic liquid') (#312). The record is the neutral salt (CAS 143314-17-4, two-fragment SMILES). CHEBI:61326 '1-ethyl-3-methylimidazolium' is the bare cation, C6H11N2 charge +1: a component of the salt, not a broader term for it (Section 6). ChEBI has no term for the acetate salt, so the closest broader class is CHEBI:63895 'ionic liquid', the parent the sibling record 1-ethyl-3-methylimidazolium_Lysine already uses. cas: identity, NARROW_MATCH grade and both registry rows unchanged (Section 3 step 2).
- Active SSSOM state: 3 active row(s) for `MIM:1-ethyl-3-methylimidazolium_Acetate`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/1-ethyl-3-methylimidazolium_Acetate.md` after the record changed from 0406799826473dee458b6358022420cc7555ba9ee3fbbd2e0b7689cde32fa6d5 to 38814f2038706907038c87a8bff6785abaf177e4746c63ddfae6fcb8836acda5; preserved the previous minor finding floor pending targeted retirement.

## Findings

- **minor**: The previous finding set in `reports/yaml_record_review/1-ethyl-3-methylimidazolium_Acetate.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: CAS-primary salt identity and narrow cation mapping pass, but the open kgscan discussion is irrelevant and unattached.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/1-ethyl-3-methylimidazolium_Acetate.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/1-ethyl-3-methylimidazolium_Acetate.yaml`, `just validate-terms data/ingredients/mapped/1-ethyl-3-methylimidazolium_Acetate.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/1-ethyl-3-methylimidazolium_Acetate.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/1-ethyl-3-methylimidazolium_Acetate.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
