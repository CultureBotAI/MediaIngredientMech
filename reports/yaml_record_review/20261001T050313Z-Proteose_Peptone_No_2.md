# YAML Record Review: Proteose peptone no. 2

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Proteose_Peptone_No_2.yaml`
- Started UTC: 2026-10-01T05:03:13Z
- Finished UTC: 2026-10-01T05:03:14Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Proteose_Peptone_No_2.yaml`
- Identifier: `MICRO:0002393`
- Preferred term: Proteose peptone no. 2
- Mapping status: `MAPPED`
- Ingredient type: `UNDEFINED_MIXTURE`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Proteose_Peptone_No_2.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `MICRO:0002393`.
- Ontology label: `Proteose Peptone No. 2`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Proteose_Peptone_No_2.md` after the record changed from af94aaec0512002f2a0bc17f08a78937b0ed877ed419d232904e6553464890de to 67ca4baee47a98b1ccd293403503a20d1ed757055d179658689f9ab7a6a17533; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `67ca4baee47a98b1ccd293403503a20d1ed757055d179658689f9ab7a6a17533`.
- Previous review: `reports/yaml_record_review/Proteose_Peptone_No_2.md`.
- Previous record SHA-256: `af94aaec0512002f2a0bc17f08a78937b0ed877ed419d232904e6553464890de`.
- Source occurrence traceability: 7 occurrence(s) across 7 medium/media.
- Latest curation event: CORRECTED by restore_micro_source_identities at 2026-09-23T17:09:55.758900+00:00: Restore MICRO:0002393 'Proteose Peptone No. 2' from the pinned KG-Microbe MICRO KGX (#759). Both node snapshots contain this exact class label; current KGX parent(s): MICRO:0000180. Original IRI: http://purl.obolibrary.org/obo/MicrO.owl/MICRO_0002393. This supersedes #137's canonical-IRI-only rejection; it does not claim OLS defining-ontology status. No verified CAS RN is supplied for this material.
- Active SSSOM state: 1 active row(s) for `MIM:Proteose_Peptone_No_2`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Proteose_Peptone_No_2.md` after the record changed from af94aaec0512002f2a0bc17f08a78937b0ed877ed419d232904e6553464890de to 67ca4baee47a98b1ccd293403503a20d1ed757055d179658689f9ab7a6a17533; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Proteose_Peptone_No_2.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The local No. 2 identity and MICRO parent pass, but PROTEIN_SOURCE is provisional.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Proteose_Peptone_No_2.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Proteose_Peptone_No_2.yaml`, `just validate-terms data/ingredients/mapped/Proteose_Peptone_No_2.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Proteose_Peptone_No_2.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Proteose_Peptone_No_2.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
