# YAML Record Review: DL-mevalonic acid

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Dl-mevalonic_Acid.yaml`
- Started UTC: 2026-10-01T05:02:10Z
- Finished UTC: 2026-10-01T05:02:11Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Dl-mevalonic_Acid.yaml`
- Identifier: `CHEBI:25351`
- Preferred term: DL-mevalonic acid
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Dl-mevalonic_Acid.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:25351`.
- Ontology label: `mevalonic acid`.
- Mapping quality: `SYNONYM_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Dl-mevalonic_Acid.md` after the record changed from 2286c5f2dccd7eee68191f856425771fb7d4d4bb62cfa9e37d2835cfcb128d78 to 7fd9e8630dce65d4ff8aab42622cb23d6ea695aee428a49be0fc8a63afb1c1be; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `7fd9e8630dce65d4ff8aab42622cb23d6ea695aee428a49be0fc8a63afb1c1be`.
- Previous review: `reports/yaml_record_review/Dl-mevalonic_Acid.md`.
- Previous record SHA-256: `2286c5f2dccd7eee68191f856425771fb7d4d4bb62cfa9e37d2835cfcb128d78`.
- Source occurrence traceability: 6 occurrence(s) across 6 medium/media.
- Latest curation event: CORRECTED by retire_wrong_compound_synonyms at 2026-09-21T03:52:08Z: Marked 1 synonym(s) non-resolving: ['(2R,4S,5R,6R)-5-Acetamido-2-[(2R,3S,4R,5S)-5-acetamido-4-[(2R,3R,4R,5S,6R)-3-acetamido-6-(hydroxymethyl)-5-[(2S,3R,4S,5R,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)oxan-2-yl]oxy-4-[(2S,3S,4R,5S,6S)-3,4,5-trihydroxy-6-methyloxan-2-yl]oxyoxan-2-yl]oxy-2,3,6-trihydroxyhexoxy]-4-hydroxy-6-[(1R,2R)-1,2,3-trihydroxypropyl]oxane-2-carboxylic acid']. ChEBI gives these names to CHEBI:150970, not to this record's CHEBI:25351 -- mevalonic acid is not the oligosaccharide at CHEBI:150970 -- its CAS 150-97-0 read as an accession. Kept as REJECTED_LABEL so a rebuild cannot restore them from kg-microbe's synonym list (#669).
- Active SSSOM state: 1 active row(s) for `MIM:Dl-mevalonic_Acid`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Dl-mevalonic_Acid.md` after the record changed from 2286c5f2dccd7eee68191f856425771fb7d4d4bb62cfa9e37d2835cfcb128d78 to 7fd9e8630dce65d4ff8aab42622cb23d6ea695aee428a49be0fc8a63afb1c1be; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Dl-mevalonic_Acid.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The mevalonic acid identity passes, but an unrelated polysaccharide synonym leaks into SSSOM and the carbon-source role is computational.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Dl-mevalonic_Acid.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Dl-mevalonic_Acid.yaml`, `just validate-terms data/ingredients/mapped/Dl-mevalonic_Acid.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Dl-mevalonic_Acid.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Dl-mevalonic_Acid.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
