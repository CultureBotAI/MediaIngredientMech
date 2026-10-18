# YAML Record Review: Sodium succinate dibasic

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Sodium_Succinate_Dibasic.yaml`
- Started UTC: 2026-10-01T05:03:31Z
- Finished UTC: 2026-10-01T05:03:32Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Sodium_Succinate_Dibasic.yaml`
- Identifier: `cas:150-90-3`
- Preferred term: Sodium succinate dibasic
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Sodium_Succinate_Dibasic.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:63675`.
- Ontology label: `sodium succinate (anhydrous)`.
- Mapping quality: `NARROW_MATCH`.
- Active SSSOM rows for this subject: 3.
- Identity judgement: Refreshed `reports/yaml_record_review/Sodium_Succinate_Dibasic.md` after the record changed from 79ed1bee5feb79154020816ebb98eac852a870cd28ca0d4b81fcad05d052287d to 6575a964dee14894c20d9f6b27630d6b14818b1ce59e7d395d5c849dc69368ac; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `6575a964dee14894c20d9f6b27630d6b14818b1ce59e7d395d5c849dc69368ac`.
- Previous review: `reports/yaml_record_review/Sodium_Succinate_Dibasic.md`.
- Previous record SHA-256: `79ed1bee5feb79154020816ebb98eac852a870cd28ca0d4b81fcad05d052287d`.
- Source occurrence traceability: 6 occurrence(s) across 6 medium/media.
- Latest curation event: CORRECTED by retire_wrong_compound_synonyms at 2026-09-21T03:52:08Z: Marked 3 synonym(s) non-resolving: ['(2S,3S,4R,5S,6S)-2-[(3R,4R,5S,6R)-2,3-Dihydroxy-6-(hydroxymethyl)-5-[(2R,3R,4S,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)oxan-2-yl]oxyoxan-4-yl]oxy-6-methyloxane-3,4,5-triol', '6-deoxy-alpha-L-galacto-hexopyranosyl-(1->3)-[alpha-D-gluco-hexopyranosyl-(1->4)]-D-galacto-hexopyranose', 'Fuc(a1-3)[Glc(a1-4)]Gal']. ChEBI gives these names to CHEBI:150903, not to this record's cas:150-90-3 -- disodium succinate is not the trisaccharide at CHEBI:150903 -- its CAS 150-90-3 read as an accession. Kept as REJECTED_LABEL so a rebuild cannot restore them from kg-microbe's synonym list (#669).
- Active SSSOM state: 3 active row(s) for `MIM:Sodium_Succinate_Dibasic`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Sodium_Succinate_Dibasic.md` after the record changed from 79ed1bee5feb79154020816ebb98eac852a870cd28ca0d4b81fcad05d052287d to 6575a964dee14894c20d9f6b27630d6b14818b1ce59e7d395d5c849dc69368ac; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Sodium_Succinate_Dibasic.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The CAS now points at sodium succinate, but stale CHEBI:150903 glycoside aliases and roles still publish.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Sodium_Succinate_Dibasic.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Sodium_Succinate_Dibasic.yaml`, `just validate-terms data/ingredients/mapped/Sodium_Succinate_Dibasic.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Sodium_Succinate_Dibasic.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Sodium_Succinate_Dibasic.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
