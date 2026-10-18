# YAML Record Review: Atrop Abyssomicin C

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Atrop_Abyssomicin_C.yaml`
- Started UTC: 2026-10-01T05:01:32Z
- Finished UTC: 2026-10-01T05:01:33Z
- Verdict: pass

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Atrop_Abyssomicin_C.yaml`
- Identifier: `CHEBI:208735`
- Preferred term: Atrop Abyssomicin C
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Atrop_Abyssomicin_C.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:208735`.
- Ontology label: `Atrop-Abybetaomicin C`.
- Mapping quality: `MANUAL_CURATION`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Atrop_Abyssomicin_C.md` after the record changed from 7088d46275f1119f14a81d379bad38ad24eae23d82a93a8e888dffa635be7187 to c4e80c84b617f9577c8320bed14f15cebf5262cda47c58bae73a586e292a7ca1; no prior finding is carried forward.

## Evidence

- Current record SHA-256: `c4e80c84b617f9577c8320bed14f15cebf5262cda47c58bae73a586e292a7ca1`.
- Previous review: `reports/yaml_record_review/Atrop_Abyssomicin_C.md`.
- Previous record SHA-256: `7088d46275f1119f14a81d379bad38ad24eae23d82a93a8e888dffa635be7187`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: REGROUNDED_IDENTITY by claude at 2026-09-23T00:44:54.462592+00:00: identifier mesh:C509797 -> CHEBI:208735; ontology mesh:C509797 ('abyssomicin C') -> CHEBI:208735 ('Atrop-Abybetaomicin C'); mapping_quality EXACT_MATCH -> MANUAL_CURATION. MeSH SCR C509797 is 'abyssomicin C'; NLM lists 'atrop-abyssomicin C' as a separate, narrower concept (M0511053) that OLS flattened into a synonym, so the record sat on the broader compound. ChEBI has the atropisomer as CHEBI:208735 'Atrop-Abybetaomicin C' (the label's 'ss' was corrupted to 'beta' upstream), C19H22O6, InChIKey FNEADFUPWHAVTA-PLNGDYQASA-N, which equals PubChem CID 23232701 'atrop-abyssomicin C'. No name matches lexically because of the corruption and the record has no CAS, so the grade is MANUAL_CURATION: identity rests on the InChIKey/IUPAC agreement. (#312)
- Active SSSOM state: 1 active row(s) for `MIM:Atrop_Abyssomicin_C`.
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

- Re-run strict schema validation on `data/ingredients/mapped/Atrop_Abyssomicin_C.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Atrop_Abyssomicin_C.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
