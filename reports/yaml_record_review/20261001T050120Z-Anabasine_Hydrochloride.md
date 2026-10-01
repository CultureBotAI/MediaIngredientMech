# YAML Record Review: Anabasine Hydrochloride

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Anabasine_Hydrochloride.yaml`
- Started UTC: 2026-10-01T05:01:20Z
- Finished UTC: 2026-10-01T05:01:21Z
- Verdict: pass

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Anabasine_Hydrochloride.yaml`
- Identifier: `NCIT:C216370`
- Preferred term: Anabasine Hydrochloride
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Anabasine_Hydrochloride.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `NCIT:C216370`.
- Ontology label: `Anabasine Hydrochloride`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Anabasine_Hydrochloride.md` after the record changed from 9eb9c44a594ba93b72bc22e26de3559d84697b04f23343b36669236fd03aa42f to c9c693f7bc5354b5c472efaf4472f66b56e5c4e8d3a814490982da1d94810215; no prior finding is carried forward.

## Evidence

- Current record SHA-256: `c9c693f7bc5354b5c472efaf4472f66b56e5c4e8d3a814490982da1d94810215`.
- Previous review: `reports/yaml_record_review/Anabasine_Hydrochloride.md`.
- Previous record SHA-256: `9eb9c44a594ba93b72bc22e26de3559d84697b04f23343b36669236fd03aa42f`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: CORRECTED by kgmicrobe_identity_review_20260924 at 2026-09-24T07:10:47.876708+00:00: Source CAS, NCIT, FDA W4917XZ12G and PubChem 3041330 agree on the stereospecific monohydrochloride. Preserve the existing stereochemical InChI and align its SMILES; no free base or other salt is substituted.
- Active SSSOM state: 1 active row(s) for `MIM:Anabasine_Hydrochloride`.
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

- Re-run strict schema validation on `data/ingredients/mapped/Anabasine_Hydrochloride.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Anabasine_Hydrochloride.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
