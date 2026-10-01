# YAML Record Review: b-Glucan from Oat

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/B-Glucan_From_Oat.yaml`
- Started UTC: 2026-10-01T05:01:33Z
- Finished UTC: 2026-10-01T05:01:34Z
- Verdict: pass

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/B-Glucan_From_Oat.yaml`
- Identifier: `kgmicrobe.ingredient:b-glucan_from_oat`
- Preferred term: b-Glucan from Oat
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/B-Glucan_From_Oat.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:18504`.
- Ontology label: `(1->3,1->4)-beta-D-glucan`.
- Mapping quality: `NARROW_MATCH`.
- Active SSSOM rows for this subject: 2.
- Identity judgement: Refreshed `reports/yaml_record_review/B-Glucan_From_Oat.md` after the record changed from c7aef82024119ec7d23eddf78b334a68ee4d0dc35c0fbb97997f43601f79c171 to 6f0bb326a91377a9a0784cac42469d9c347963159b4d59b8c7f5724971e56554; no prior finding is carried forward.

## Evidence

- Current record SHA-256: `6f0bb326a91377a9a0784cac42469d9c347963159b4d59b8c7f5724971e56554`.
- Previous review: `reports/yaml_record_review/B-Glucan_From_Oat.md`.
- Previous record SHA-256: `c7aef82024119ec7d23eddf78b334a68ee4d0dc35c0fbb97997f43601f79c171`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: MINTED_REGISTRY_IDENTIFIER by claude at 2026-09-23T03:41:22.729918+00:00: identifier CHEBI:28793 -> kgmicrobe.ingredient:b-glucan_from_oat; ontology CHEBI:28793 ('beta-D-glucan') -> CHEBI:18504 ('(1->3,1->4)-beta-D-glucan'); mapping_quality CAS_RN_LOOKUP -> NARROW_MATCH. CHEBI:28793 'beta-D-glucan' is the linkage-agnostic class with 18 subclasses (cellulose, nitrocellulose, schizophyllan, ...); an exactMatch licensed substituting oat beta-glucan for the whole class, and MIM:Cellulose already sits under it. Oat beta-glucan is the mixed-linkage (1->3,1->4)-beta-D-glucan, CHEBI:18504, and the record is source-qualified ('from Oat'), so it is narrower than that term too. Section 3 step 3, the Amylopectin_From_Maize / Lichenan shape: registry identity, broadMatch CHEBI:18504. CAS 9041-22-9 is the generic beta-glucan registration (ChEBI xrefs it on CHEBI:28793) and stays in chemical_properties as such. (#312)
- Active SSSOM state: 2 active row(s) for `MIM:B-Glucan_From_Oat`.
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

- Re-run strict schema validation on `data/ingredients/mapped/B-Glucan_From_Oat.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/B-Glucan_From_Oat.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
