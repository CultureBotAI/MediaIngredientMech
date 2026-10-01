# YAML Record Review: Aromatic compound

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Aromatic_Compound.yaml`
- Started UTC: 2026-10-01T05:01:27Z
- Finished UTC: 2026-10-01T05:01:28Z
- Verdict: pass

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Aromatic_Compound.yaml`
- Identifier: `CHEBI:33655`
- Preferred term: Aromatic compound
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Aromatic_Compound.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:33655`.
- Ontology label: `aromatic compound`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Aromatic_Compound.md` after the record changed from 1b934b840f9941aadbc305120f44c072f113ccd89745915ea190ecc588a4d9c9 to bbbfcafd33a763fc81b1a1bc425a4e270c791aac6e51d668726798ee16ff47b6; no prior finding is carried forward.

## Evidence

- Current record SHA-256: `bbbfcafd33a763fc81b1a1bc425a4e270c791aac6e51d668726798ee16ff47b6`.
- Previous review: `reports/yaml_record_review/Aromatic_Compound.md`.
- Previous record SHA-256: `1b934b840f9941aadbc305120f44c072f113ccd89745915ea190ecc588a4d9c9`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: REJECTED_TRAIT_SYNONYMS by claude at 2026-09-22T06:14:49.563933+00:00: Retyped activity/assay phrases as provenance-only REJECTED_LABEL because they describe a process or organism trait, not an ingredient name (#703): 'degradation: aromatic compound'. Preserved original text and source metadata. No identity, mapping, role, or remaining-synonym claim was adjudicated.
- Active SSSOM state: 1 active row(s) for `MIM:Aromatic_Compound`.
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

- Re-run strict schema validation on `data/ingredients/mapped/Aromatic_Compound.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Aromatic_Compound.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
