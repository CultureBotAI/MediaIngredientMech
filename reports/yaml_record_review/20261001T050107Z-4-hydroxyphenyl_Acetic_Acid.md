# YAML Record Review: 4-Hydroxyphenyl acetic acid

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/4-hydroxyphenyl_Acetic_Acid.yaml`
- Started UTC: 2026-10-01T05:01:07Z
- Finished UTC: 2026-10-01T05:01:08Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/4-hydroxyphenyl_Acetic_Acid.yaml`
- Identifier: `CHEBI:18101`
- Preferred term: 4-Hydroxyphenyl acetic acid
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/4-hydroxyphenyl_Acetic_Acid.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:18101`.
- Ontology label: `4-hydroxyphenylacetic acid`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/4-hydroxyphenyl_Acetic_Acid.md` after the record changed from ce453fe01660537285720b57586f1f141fd88da554845ee0731d49bc508860b8 to 8cfb1babc44f71177b516e9ba3c12927220e4f77fac5ff8f5f04fdb49e962622; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `8cfb1babc44f71177b516e9ba3c12927220e4f77fac5ff8f5f04fdb49e962622`.
- Previous review: `reports/yaml_record_review/4-hydroxyphenyl_Acetic_Acid.md`.
- Previous record SHA-256: `ce453fe01660537285720b57586f1f141fd88da554845ee0731d49bc508860b8`.
- Source occurrence traceability: 7 occurrence(s) across 7 medium/media.
- Latest curation event: CORRECTED by retire_wrong_compound_synonyms at 2026-09-20T00:00:00Z: Marked 2 synonym(s) non-resolving: ['(5S,6R)-5-hydroxy-6-methyl-3-[(2S,3S)-3-methyloxiran-2-yl]-5,6-dihydro-2H-pyran-2-one', 'aspyrone']. ChEBI gives these names to CHEBI:156387, not to this record's CHEBI:18101 -- 4-hydroxyphenylacetic acid is not aspyrone. Kept as REJECTED_LABEL so a rebuild cannot restore them from kg-microbe's synonym list (#669).
- Active SSSOM state: 1 active row(s) for `MIM:4-hydroxyphenyl_Acetic_Acid`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/4-hydroxyphenyl_Acetic_Acid.md` after the record changed from ce453fe01660537285720b57586f1f141fd88da554845ee0731d49bc508860b8 to 8cfb1babc44f71177b516e9ba3c12927220e4f77fac5ff8f5f04fdb49e962622; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/4-hydroxyphenyl_Acetic_Acid.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: CHEBI identity and CAS pass, but two exact synonyms still denote the old wrong aspyrone compound and the carbon-source role is unsupported.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/4-hydroxyphenyl_Acetic_Acid.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/4-hydroxyphenyl_Acetic_Acid.yaml`, `just validate-terms data/ingredients/mapped/4-hydroxyphenyl_Acetic_Acid.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/4-hydroxyphenyl_Acetic_Acid.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/4-hydroxyphenyl_Acetic_Acid.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
