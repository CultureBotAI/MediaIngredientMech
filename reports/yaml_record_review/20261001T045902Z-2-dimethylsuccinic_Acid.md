# YAML Record Review: 2,2-dimethylsuccinic acid

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/2-dimethylsuccinic_Acid.yaml`
- Started UTC: 2026-10-01T04:59:02Z
- Finished UTC: 2026-10-01T04:59:03Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/2-dimethylsuccinic_Acid.yaml`
- Identifier: `CHEBI:86537`
- Preferred term: 2,2-dimethylsuccinic acid
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/2-dimethylsuccinic_Acid.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:86537`.
- Ontology label: `2,2-dimethylsuccinic acid`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/2-dimethylsuccinic_Acid.md` after the record changed from dc520ce3cede726df5bc33151ccc9d201044e65cde8d66f4a4b9a936a7982b05 to 929b011788ee8e749b5442164a49c2f4e2aa41edfc970a0f750586d18216ed62; preserved the previous blocker finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `929b011788ee8e749b5442164a49c2f4e2aa41edfc970a0f750586d18216ed62`.
- Previous review: `reports/yaml_record_review/2-dimethylsuccinic_Acid.md`.
- Previous record SHA-256: `dc520ce3cede726df5bc33151ccc9d201044e65cde8d66f4a4b9a936a7982b05`.
- Source occurrence traceability: 0 active occurrence(s) across 0 medium/media; source rows: microbedecoder: 4.
- Latest curation event: RESOLVED_FROM_ORIGINAL_SOURCE by mim_semantic_review_710 at 2026-09-22T02:07:38.917319+00:00: All four original MicrobeDecoder source rows explicitly name 2,2-dimethylsuccinic acid. Their BacDive records identify CHEBI:86537. The historical 2,3-isomer CHEBI:167506 is rejected; this is a distinct constitutional isomer, not a close match. Evidence: https://bacdive.dsmz.de/strain/140942 ; https://bacdive.dsmz.de/strain/168456 ; https://bacdive.dsmz.de/strain/140923 ; https://bacdive.dsmz.de/strain/158680 ; https://www.ebi.ac.uk/chebi/CHEBI:86537
- Active SSSOM state: 1 active row(s) for `MIM:2-dimethylsuccinic_Acid`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/2-dimethylsuccinic_Acid.md` after the record changed from dc520ce3cede726df5bc33151ccc9d201044e65cde8d66f4a4b9a936a7982b05 to 929b011788ee8e749b5442164a49c2f4e2aa41edfc970a0f750586d18216ed62; preserved the previous blocker finding floor pending targeted retirement.

## Findings

- **blocker**: The previous finding set in `reports/yaml_record_review/2-dimethylsuccinic_Acid.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The record publishes an exact identity row to CHEBI:167506, but CHEBI:167506 is the 2,3 isomer and the record only documents a non-exact truncated-label rationale.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/2-dimethylsuccinic_Acid.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/2-dimethylsuccinic_Acid.yaml`, `just validate-terms data/ingredients/mapped/2-dimethylsuccinic_Acid.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/2-dimethylsuccinic_Acid.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/2-dimethylsuccinic_Acid.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
